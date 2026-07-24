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
MANUAL = os.path.join(BASE, "output", "manual_classified.json")

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

# Segundo bloque de few-shot, tomado de la clasificacion manual (no del gold).
# Estos no cubren espacio de posturas: cubren las REGLAS dificiles, los casos
# donde el texto engana. e2_validate.py los excluye del set de validacion.
MANUAL_FEWSHOT_IDS = [
    "1275",  # pectorales contraindicado para rodilla — mecanica > musculo objetivo
    "0352",  # codos pegados: pinzamiento baja de contra a caution
    "1330",  # "bend at the waist": torso en voladizo, contra para hernia discal
    "1317",  # pecho apoyado en el banco: MISMO patron, apto para hernia discal
    "0045",  # safe_for vacio + contraindicacion por consecuencia
    "0659",  # maxima accesibilidad: 15 safe_for, 2 contra
]


def build_system_prompt(taxonomy, gold, fewshot_only=True, manual=None):
    pool = gold["examples"]
    if fewshot_only:
        sel = [g for g in pool if g["exercise_id"] in FEWSHOT_IDS]
        pool = sel if len(sel) >= 8 else pool[:14]

    # Casos dificiles tomados de la clasificacion manual, en el orden de la lista.
    if manual:
        by_id = {r["exercise_id"]: r for r in manual}
        pool = pool + [by_id[i] for i in MANUAL_FEWSHOT_IDS if i in by_id]
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

## Las tres capas de condiciones

Cada condicion pertenece a una capa, y la capa determina que hace el motor con ella.
Clasificar sin saber esto produce errores graves en las dos direcciones.

{chr(10).join(f"- Capa {k}: {v}" for k, v in taxonomy["layer_semantics"].items())}

{json.dumps(taxonomy["condition_layers"], ensure_ascii=False, indent=1)}

Consecuencia practica:
- Capa A: son hechos objetivos sobre el cuerpo, no juicios medicos. Si el ejercicio
  exige pararse, `cannot_stand` va en contraindications, sin matices.
- Capa B: el motor aplica un umbral segun la severidad que declara el usuario. Por eso
  `joint_stress` tiene que ser COHERENTE con la lista de condiciones: si pones una
  lesion articular en cautions pero el `joint_stress` de esa articulacion es high, el
  motor la excluye igual y tu caution no sirve de nada.
- Capa C: nunca oculta, solo advierte y degrada el ranking. Podes ser generoso
  marcando condiciones sistemicas en cautions: el costo de un falso positivo es una
  advertencia de mas, no un ejercicio perdido.

## Lecciones de 396 ejercicios clasificados a mano

Estas reglas salieron de anotar el catalogo real. Son los errores que mas se repiten.

- CLASIFICA MECANICA, NO MUSCULO OBJETIVO. `drop push up` figura como ejercicio de
  pectorales y esta contraindicado para rodilla, porque el texto dice "drop your knees
  to the ground": impacto rotuliano repetido. Lee que hace el cuerpo, no que musculo
  dice el dataset.

- EL NOMBRE MIENTE MAS QUE EL TEXTO. Hay ejercicios llamados "wrist curl" cuyo texto
  describe un curl de codo, "planche" que describen una flexion, y "stretch" que son
  rotacion lumbar cargada. Ante conflicto mandan las instrucciones, y baja el
  confidence por debajo de 0.7.

- LA POSICION DEL CODO DECIDE EL HOMBRO. Mismo press con mancuernas: codos abiertos =
  pinzamiento contraindicado; codos pegados al cuerpo = pinzamiento en cautions. Busca
  "elbows flare out" vs "elbows close to your body" en el texto.

- EL APOYO DEL TORSO DECIDE LA LUMBAR. Un remo con el pecho apoyado en el banco es apto
  para hernia discal; el mismo remo con el torso en voladizo esta contraindicado. Si el
  texto dice "bend at the waist", la columna sostiene carga.

- UNA PROGRESION PUEDE INVERTIR EL VEREDICTO. El puente de gluteo simple es apto para
  protesis de cadera (extension pura); agregarle la marcha lleva la rodilla al pecho,
  supera los 90 grados y pasa a contraindicado. Clasifica el movimiento completo, no
  la posicion inicial.

- CONTRAINDICACION POR CONSECUENCIA. Si una perdida momentanea de control es
  catastrofica (barra sobre el cuello o la cara, inversion con carga), marca `epilepsy`
  y `vertigo` en contraindications aunque el ejercicio no exija nada vestibular.

- HEAD_BELOW_HEART APARECE DONDE NO SE ESPERA. Banco declinado, torso paralelo al suelo
  en kickbacks, prono con el pecho fuera del banco. No es solo inversiones.

- GRIP_DURATION NO ES GRIP_REQUIRED. Artritis y tunel carpiano toleran fuerza breve
  pero no sostenida. Una barra que se sostiene toda la serie es `high` aunque el peso
  sea bajo.

- SAFE_FOR VACIO ES UNA RESPUESTA VALIDA. En ejercicios muy agresivos (muscle up,
  handstand push-up, guillotine press) no existe ninguna condicion para la que se pueda
  afirmar seguridad. Dejarlo vacio es correcto; inventar entradas es el peor error.


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

    manual = (json.load(open(MANUAL, encoding="utf-8"))
              if os.path.exists(MANUAL) else [])
    system = build_system_prompt(taxonomy, gold, manual=manual)

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
