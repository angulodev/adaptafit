#!/usr/bin/env python3
"""
Fase E2 — Clasificacion asistida por IA.

Completa los atributos que E1 no pudo derivar, con foco en la capa de seguridad
(joint_stress, contraindications, cautions, safe_for, columna, dificultad).

Uso:
    export ANTHROPIC_API_KEY=sk-ant-...
    pip install anthropic

    python enrich/e2_classify.py --dry-run        # ver 1 prompt sin gastar tokens
    python enrich/e2_classify.py --limit 32       # prueba con 2 lotes
    python enrich/e2_classify.py                  # corrida completa
    python enrich/e2_classify.py --validate       # medir acuerdo contra gold

Diseno (lecciones de KDP Book Studio):
  - Lotes chicos (16) para evitar truncado de respuesta
  - Salida JSON estricta, sin preambulo ni backticks
  - Parser de rescate para JSON parcial
  - Checkpoint incremental: si se corta, retoma donde quedo
  - Reintentos con backoff
"""

import argparse
import json
import os
import re
import sys
import time

# BASE = .../enrichment  (este script vive en enrichment/scripts/)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E1 = os.path.join(BASE, "output", "e1_output.json")
SRC = os.path.join(BASE, "source", "exercises.json")
TAX = os.path.join(BASE, "taxonomy", "taxonomy_v1.json")
GOLD = os.path.join(BASE, "gold", "gold_examples.json")
OUT = os.path.join(BASE, "output", "e2_output.json")
CKPT = os.path.join(BASE, "output", "e2_checkpoint.json")

MODEL = "claude-sonnet-5"
BATCH_SIZE = 8   # reducido de 16: menos riesgo de truncado en respuestas largas
MAX_RETRIES = 3

# Equipo disponible en casa — define el subconjunto a enriquecer
EQUIPMENT_FILTER = {
    "body weight", "dumbbell", "barbell", "band",
    "resistance band", "ez barbell", "olympic barbell", "weighted",
}


# --------------------------------------------------------------------------
# Prompt
# --------------------------------------------------------------------------

# Ejemplos que van DENTRO del prompt como few-shot. El resto del gold queda
# reservado como set de validacion: medir el acuerdo contra ejemplos que el
# modelo ya vio no mide nada. Elegidos para cubrir el espacio de posturas y
# patrones con el minimo de tokens.
FEWSHOT_IDS = [
    "0025",  # bench_supine  · horizontal_push · hombro alto
    "0043",  # standing      · squat           · carga axial maxima
    "1460",  # standing      · lunge           · unipodal, equilibrio alto
    "0651",  # hanging       · vertical_pull   · agarre como restriccion dura
    "0084",  # kneeling      · anti-extension  · doble restriccion Capa A
    "1712",  # side_lying    · isolation       · safe_for amplio
    "0372",  # seated_machine· isolation       · el mas seguro del catalogo
    "0049",  # bench_prone   · horizontal_pull · postura rara, corrige a E1
    "3360",  # quadruped     · cardio          · unica cuadrupedia
    "1604",  # half_kneeling · movilidad       · difficulty 2 vs rom_demand high
    "0493",  # bench_incline · regresion de push-up para cannot_get_on_floor
    "0514",  # standing      · pliometrico     · impact high
    "3016",  # supine        · core_flexion    · regresion segura
    "0126",  # seated        · el equipo cambia el riesgo del mismo movimiento
]


def build_system_prompt(taxonomy, gold, fewshot_only=True):
    pool = gold["examples"]
    if fewshot_only:
        sel = [g for g in pool if g["exercise_id"] in FEWSHOT_IDS]
        pool = sel if len(sel) >= 8 else pool[:14]
    ex_blocks = []
    for g in pool:
        payload = {k: v for k, v in g.items() if not k.startswith("_")}
        ex_blocks.append(
            f"Ejercicio: {g['_name']}\n"
            f"Razonamiento: {g['_reasoning']}\n"
            f"Salida:\n{json.dumps(payload, ensure_ascii=False, indent=1)}"
        )

    return f"""Eres un clasificador biomecanico. Analizas ejercicios de gimnasio y devuelves atributos estructurados que alimentan un motor de filtrado adaptativo para personas con limitaciones fisicas.

Este trabajo tiene consecuencias reales: las personas que usan la app dependen de tu clasificacion para evitar lesionarse. Un falso "seguro" es el peor error posible.

## Valores permitidos

{json.dumps(taxonomy["enums"], ensure_ascii=False, indent=1)}

## Definicion de cada campo

{json.dumps(taxonomy["field_definitions"], ensure_ascii=False, indent=1)}

## Reglas de clasificacion

{chr(10).join("- " + r for r in taxonomy["classification_rules"])}

## Ejemplos de referencia

{chr(10).join(ex_blocks)}

## Formato de salida

Devuelve UNICAMENTE un array JSON. Sin preambulo, sin explicacion, sin backticks, sin markdown.
Un objeto por ejercicio recibido, en el mismo orden, cada uno con exactamente estos campos:

exercise_id, start_position, requires_floor_transition, requires_standing,
requires_balance, single_leg_support, overhead_position, grip_required,
axial_spinal_load, spinal_flexion, spinal_extension, spinal_rotation,
impact_level, joint_stress, laterality, movement_pattern, difficulty,
rom_demand, orthostatic_load, position_change, head_below_heart,
valsalva_risk, sustained_isometric, metabolic_intensity, joint_laxity_risk,
pelvic_floor_load, temperature_load, grip_duration,
contraindications, cautions, safe_for, confidence

joint_stress debe incluir SIEMPRE las 8 articulaciones.
head_below_heart es booleano. difficulty es entero 1-5. confidence es 0.0-1.0.
El resto de los campos nuevos usan la escala none|low|moderate|high.

## Los campos fisiologicos (v1.2) - leer con atencion

Son los que permiten filtrar condiciones que NO dependen de que articulacion se
carga. Sin ellos la app no puede atender disautonomia, fatiga cronica ni
hipermovilidad. No los dejes en null.

- orthostatic_load: cuestion de VERTICALIDAD DEL TORSO, no de "no estar acostado".
  En cuadrupedia o plancha la cabeza queda a la altura del corazon: eso es none.
  Reclinado/cuadrupedia/plancha = none. Sentado/arrodillado = low.
  Colgado = moderate. De pie = moderate, o high si hay brazos elevados o impacto.

- metabolic_intensity: demanda cardiometabolica global. Un curl de biceps es low
  aunque sea pesado; burpees son high. Critico para fatiga cronica.

- valsalva_risk: probabilidad de que la persona aguante la respiracion bajo carga.
  Sube con carga axial y con dificultad. Sentadilla pesada = high, estiramiento = none.

- joint_laxity_risk: riesgo de trabajar en rango final con articulacion inestable.
  Alto en estiramientos profundos y en posiciones de maxima apertura.

- pelvic_floor_load: presion intraabdominal descendente. Alta en bisagra de cadera
  con carga, impacto, y trabajo de core intenso."""


def build_user_message(batch, e1_map):
    items = []
    for ex in batch:
        pre = e1_map.get(ex["id"], {})
        hints = {k: v for k, v in pre.items()
                 if k in ("start_position", "laterality", "movement_pattern",
                          "grip_required", "overhead_position", "impact_level",
                          "axial_spinal_load", "requires_balance")
                 and v is not None}
        items.append({
            "exercise_id": ex["id"],
            "name": ex["name"],
            "equipment": ex["equipment"],
            "body_part": ex["body_part"],
            "target": ex["target"],
            "secondary_muscles": ex.get("secondary_muscles", []),
            "instructions": ex["instructions"]["en"],
            "_preseed_hints": hints,
        })

    return (
        "Clasifica estos ejercicios. `_preseed_hints` son inferencias previas por "
        "reglas automaticas: usalas como referencia pero corregilas si el texto "
        "las contradice.\n\n"
        + json.dumps(items, ensure_ascii=False, indent=1)
    )


# --------------------------------------------------------------------------
# Parser de rescate
# --------------------------------------------------------------------------

def parse_response(text):
    """Devuelve (objetos, hubo_rescate)."""
    clean = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()

    try:
        data = json.loads(clean)
        return (data if isinstance(data, list) else [data]), False
    except json.JSONDecodeError:
        pass

    # Rescate: extraer objetos completos de un array truncado
    objs, depth, start, in_str, esc = [], 0, None, False, False
    for i, ch in enumerate(clean):
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                try:
                    objs.append(json.loads(clean[start:i + 1]))
                except json.JSONDecodeError:
                    pass
                start = None
    return objs, True


def validate_record(rec, taxonomy):
    """Devuelve lista de problemas. Vacia = registro sano."""
    problems = []
    e = taxonomy["enums"]

    checks = [
        ("start_position", e["start_position"]),
        ("requires_balance", e["level"]),
        ("grip_required", e["grip_required"]),
        ("axial_spinal_load", e["level"]),
        ("spinal_flexion", e["level"]),
        ("spinal_extension", e["level"]),
        ("spinal_rotation", e["level"]),
        ("impact_level", e["level"]),
        ("laterality", e["laterality"]),
        ("movement_pattern", e["movement_pattern"]),
        ("rom_demand", e["level"]),
        # v1.2 - campos fisiologicos
        ("orthostatic_load", e["level"]),
        ("position_change", e["level"]),
        ("valsalva_risk", e["level"]),
        ("sustained_isometric", e["level"]),
        ("metabolic_intensity", e["level"]),
        ("joint_laxity_risk", e["level"]),
        ("pelvic_floor_load", e["level"]),
        ("temperature_load", e["level"]),
        ("grip_duration", e["level"]),
    ]
    for field, allowed in checks:
        v = rec.get(field)
        if v is not None and v not in allowed:
            problems.append(f"{field}={v!r} fuera de enum")

    # Los campos fisiologicos son la razon de ser de v1.2: si vienen en null,
    # las condiciones tipo disautonomia quedan sin poder filtrar. Se marca.
    for f in ["orthostatic_load", "metabolic_intensity", "valsalva_risk"]:
        if rec.get(f) is None:
            problems.append(f"{f} en null (campo fisiologico requerido)")
    if rec.get("head_below_heart") is not None and not isinstance(rec["head_below_heart"], bool):
        problems.append("head_below_heart no es booleano")

    js = rec.get("joint_stress")
    if not isinstance(js, dict):
        problems.append("joint_stress ausente o mal formado")
    else:
        for j in e["joints"]:
            if j not in js:
                problems.append(f"joint_stress falta '{j}'")
            elif js[j] not in e["level"]:
                problems.append(f"joint_stress.{j}={js[j]!r} fuera de enum")

    for field in ("contraindications", "cautions", "safe_for"):
        v = rec.get(field)
        if not isinstance(v, list):
            problems.append(f"{field} no es lista")
        else:
            for c in v:
                if c not in e["conditions"]:
                    problems.append(f"{field}: condicion desconocida {c!r}")

    d = rec.get("difficulty")
    if not isinstance(d, int) or not 1 <= d <= 5:
        problems.append(f"difficulty={d!r} invalido")

    return problems


# --------------------------------------------------------------------------
# Llamada API
# --------------------------------------------------------------------------

def call_api(client, system, user):
    last = None
    for attempt in range(MAX_RETRIES):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=8000,
                # El system prompt (~4.200 tokens con la taxonomia y los 54
                # ejemplos) es identico en los 112 lotes. Cachearlo baja el
                # costo del input cacheado un 90%.
                system=[{
                    "type": "text",
                    "text": system,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=[{"role": "user", "content": user}],
            )
            return "".join(b.text for b in resp.content if b.type == "text")
        except Exception as exc:                      # noqa: BLE001
            last = exc
            wait = 2 ** attempt * 3
            print(f"    reintento {attempt+1}/{MAX_RETRIES} en {wait}s — {exc}")
            time.sleep(wait)
    raise RuntimeError(f"API fallo tras {MAX_RETRIES} intentos: {last}")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="imprime 1 prompt y sale")
    ap.add_argument("--limit", type=int, help="procesar solo N ejercicios")
    ap.add_argument("--validate", action="store_true", help="medir acuerdo contra gold")
    ap.add_argument("--all-equipment", action="store_true", help="no filtrar por equipo")
    args = ap.parse_args()

    taxonomy = json.load(open(TAX, encoding="utf-8"))
    gold = json.load(open(GOLD, encoding="utf-8"))
    exercises = json.load(open(SRC, encoding="utf-8"))
    e1 = json.load(open(E1, encoding="utf-8"))
    e1_map = {r["exercise_id"]: r for r in e1}

    if not args.all_equipment:
        exercises = [x for x in exercises if x["equipment"] in EQUIPMENT_FILTER]

    if args.validate:
        gold_ids = {g["exercise_id"] for g in gold["examples"]}
        exercises = [x for x in exercises if x["id"] in gold_ids]

    if args.limit:
        exercises = exercises[:args.limit]

    system = build_system_prompt(taxonomy, gold)

    # Checkpoint
    done = {}
    if os.path.exists(CKPT) and not args.dry_run:
        done = {r["exercise_id"]: r for r in json.load(open(CKPT, encoding="utf-8"))}
        print(f"Checkpoint: {len(done)} ya procesados")

    pending = [x for x in exercises if x["id"] not in done]
    batches = [pending[i:i + BATCH_SIZE] for i in range(0, len(pending), BATCH_SIZE)]

    print(f"Ejercicios objetivo : {len(exercises)}")
    print(f"Pendientes          : {len(pending)}")
    print(f"Lotes de {BATCH_SIZE}        : {len(batches)}")
    print(f"System prompt       : ~{len(system)//4} tokens\n")

    if args.dry_run:
        print("=" * 70)
        print(system[:2500])
        print("\n... [system truncado] ...\n")
        print("=" * 70)
        if batches:
            print(build_user_message(batches[0], e1_map)[:2500])
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("Falta el SDK: pip install anthropic")

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Falta ANTHROPIC_API_KEY en el entorno")

    client = anthropic.Anthropic()
    results = dict(done)
    stats = {"rescued": 0, "invalid": 0, "missing": 0}

    for n, batch in enumerate(batches, 1):
        ids = [x["id"] for x in batch]
        print(f"[{n}/{len(batches)}] {len(batch)} ejercicios...")

        raw = call_api(client, system, build_user_message(batch, e1_map))
        recs, rescued = parse_response(raw)
        if rescued:
            stats["rescued"] += 1
            print(f"    parser de rescate activado ({len(recs)}/{len(batch)} recuperados)")

        got = set()
        for rec in recs:
            rid = rec.get("exercise_id")
            if rid not in ids:
                continue
            problems = validate_record(rec, taxonomy)
            rec["_problems"] = problems
            rec["enrichment_source"] = "ai_e2"
            rec["reviewed_by"] = None
            if problems:
                stats["invalid"] += 1
            results[rid] = rec
            got.add(rid)

        missing = set(ids) - got
        if missing:
            stats["missing"] += len(missing)
            print(f"    sin respuesta: {sorted(missing)}")

        with open(CKPT, "w", encoding="utf-8") as f:
            json.dump(list(results.values()), f, ensure_ascii=False)

    final = list(results.values())
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=1)

    print(f"\nProcesados        : {len(final)}")
    print(f"Lotes rescatados  : {stats['rescued']}")
    print(f"Con problemas     : {stats['invalid']}")
    print(f"Sin respuesta     : {stats['missing']}")

    # Cola de revision humana (E3)
    review = [r for r in final
              if r.get("_problems")
              or r.get("confidence", 1) < 0.75
              or r.get("safe_for")]
    print(f"\nCola de revision E3: {len(review)}")
    print("  (problemas de validacion + confianza baja + todo lo que")
    print("   afirma 'safe_for', que es el material mas sensible)")
    print(f"\n-> {OUT}")

    if args.validate:
        print("\n=== ACUERDO CONTRA GOLD ===")
        gmap = {g["exercise_id"]: g for g in gold["examples"]}
        fields = ["start_position", "requires_standing", "requires_floor_transition",
                  "laterality", "movement_pattern", "difficulty", "axial_spinal_load"]
        agree = {f: [0, 0] for f in fields}
        for r in final:
            g = gmap.get(r["exercise_id"])
            if not g:
                continue
            for f in fields:
                agree[f][1] += 1
                if r.get(f) == g.get(f):
                    agree[f][0] += 1
        for f, (ok, tot) in agree.items():
            if tot:
                print(f"  {f:28s} {ok}/{tot}  ({ok/tot*100:.0f}%)")


if __name__ == "__main__":
    main()
