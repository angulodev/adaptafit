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

MODEL = "claude-sonnet-4-6"
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

def build_system_prompt(taxonomy, gold):
    ex_blocks = []
    for g in gold["examples"]:
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
rom_demand, contraindications, cautions, safe_for, confidence

joint_stress debe incluir SIEMPRE las 8 articulaciones."""


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
    ]
    for field, allowed in checks:
        v = rec.get(field)
        if v is not None and v not in allowed:
            problems.append(f"{field}={v!r} fuera de enum")

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
                system=system,
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
