#!/usr/bin/env python3
"""
Fase E1 — Pre-seed heuristico de atributos adaptativos.

Deriva atributos por reglas deterministas sobre:
  - la PRIMERA ORACION de instructions.en (declara la posicion inicial)
  - el nombre del ejercicio
  - equipment / body_part / target del dataset original

Salida: enrich/e1_output.json  (array de exercise_attributes parciales)
Todo campo no resuelto queda en null -> es el trabajo que hereda la fase E2 (IA).

Sesgo de diseno: CONSERVADOR. Ante ambiguedad se deja null, no se adivina.
Un atributo mal inferido en material de seguridad es peor que un null.
"""

import json
import os
import re
from collections import Counter, defaultdict

# BASE = .../enrichment  (este script vive en enrichment/scripts/)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "source", "exercises.json")
OUT_DIR = os.path.join(BASE, "output")
OUT = os.path.join(OUT_DIR, "e1_output.json")
REPORT = os.path.join(OUT_DIR, "e1_report.md")


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def first_sentences(text, n=2):
    """Primeras n oraciones: donde se declara la posicion inicial."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(parts[:n]).lower()


def has(pattern, text):
    return re.search(pattern, text) is not None


# --------------------------------------------------------------------------
# Regla 1 — start_position
# Orden de evaluacion = orden de especificidad. La primera que matchea gana.
# --------------------------------------------------------------------------

POSITION_RULES = [
    # (start_position, patron sobre primeras oraciones, patron de veto)
    ("hanging",       r"\bhang(ing)?\s+(from|on)\b|\bdead\s*hang\b", None),
    ("quadruped",     r"\ball\s+fours\b|\bhands\s+and\s+knees\b|\btabletop\s+position\b|\bquadruped\b", None),
    ("half_kneeling", r"\bhalf[- ]kneel|\bone\s+knee\s+on\s+the\s+(ground|floor)\b|\blunge\s+position\s+with\b", None),
    ("kneeling",      r"\bkneel(ing)?\b", None),
    ("plank",         r"\bplank\s+position\b|\bpush[- ]?up\s+position\b|\bhigh\s+plank\b|\bforearm\s+plank\b", None),
    ("bench_incline", r"\b(on|onto)\s+an?\s+incline\s+bench\b|\bincline\s+bench\b", None),
    ("bench_prone",   r"\b(lie|lying|lay)\s+(face\s+down|prone|chest\s+down)\s+on\s+(a|the)\s+bench\b", None),
    ("bench_supine",  r"\b(lie|lying|lay)\s+(flat\s+|back\s+|down\s+)?(on|onto)\s+(a|the|your)\s+(flat\s+)?bench\b", None),
    ("prone",         r"\b(lie|lying|lay|start\s+by\s+lying)\s+(face\s+down|prone|on\s+your\s+stomach|chest\s+down)\b", None),
    ("side_lying",    r"\b(lie|lying|lay)\s+on\s+your\s+(right|left)\s+side\b|\bside[- ]lying\b", None),
    ("supine",        r"\b(lie|lying|lay)\s+(flat\s+)?(down\s+)?on\s+(your|the)\s+(back|floor|ground|mat)\b|\blie\s+flat\b|\blie\s+on\s+your\s+back\b|\bsupine\b", None),
    ("seated_machine", r"\bsit\s+(down\s+)?(on|at|in)\s+(the|a)\s+\w*\s*(machine|apparatus|station|press|pulldown|row|curl|extension|ergometer|bike)\b", None),
    ("seated",        r"\bsit(ting)?\s+(down\s+)?(on|at|in|upright|with|tall)\b|\bseated\b|\bsit\s+on\b", None),
    ("standing",      r"\bstand(ing)?\b|\bstart\s+by\s+standing\b|\bupright\s+position\b|\bfeet\s+shoulder[- ]width\s+apart\b", None),
]

# Refuerzos desde el nombre del ejercicio (mas confiable que el cuerpo del texto)
NAME_POSITION_HINTS = [
    (r"\bseated\b", "seated"),
    (r"\blying\b|\bsupine\b", "supine"),
    (r"\bprone\b", "prone"),
    (r"\bkneeling\b", "kneeling"),
    (r"\bstanding\b", "standing"),
    (r"\bhanging\b", "hanging"),
    (r"\bincline\b", "bench_incline"),
    (r"\bdecline\b", "bench_supine"),
]

# Equipment que implica postura de forma casi determinista
EQUIPMENT_POSITION = {
    "stationary bike": "seated_machine",
    "elliptical machine": "standing",
    "stepmill machine": "standing",
    "skierg machine": "standing",
    "upper body ergometer": "seated_machine",
    "sled machine": "standing",
    "stability ball": None,
    "smith machine": None,
}


def infer_start_position(ex):
    """Devuelve (posicion, confianza, fuente)."""
    head = first_sentences(ex["instructions"]["en"])
    name = ex["name"].lower()

    name_hit = next((pos for pat, pos in NAME_POSITION_HINTS if has(pat, name)), None)
    text_hit = next((pos for pos, pat, veto in POSITION_RULES if has(pat, head)), None)

    # Pase de respaldo: muchas instrucciones abren con el montaje del equipo
    # ("Adjust the machine...", "Attach a cable to a low pulley...") y recien
    # despues declaran la posicion. Ampliamos la ventana.
    if text_hit is None:
        wide = first_sentences(ex["instructions"]["en"], n=4)
        text_hit = next((pos for pos, pat, veto in POSITION_RULES if has(pat, wide)), None)
        if text_hit and not name_hit:
            return text_hit, 0.72, "text(wide)"

    eq_hit = EQUIPMENT_POSITION.get(ex["equipment"])

    # Acuerdo nombre + texto => alta confianza
    if name_hit and text_hit and name_hit == text_hit:
        return text_hit, 0.97, "name+text"
    # El nombre es explicito y el texto no contradice groseramente
    if name_hit and not text_hit:
        return name_hit, 0.88, "name"
    # Desacuerdo: el texto describe el setup real, gana el texto pero baja confianza
    if name_hit and text_hit and name_hit != text_hit:
        return text_hit, 0.60, "text(conflict)"
    if text_hit:
        return text_hit, 0.85, "text"
    if eq_hit:
        return eq_hit, 0.80, "equipment"
    return None, 0.0, None


# --------------------------------------------------------------------------
# Regla 2 — derivados de la posicion
# --------------------------------------------------------------------------

FLOOR_POSITIONS = {"supine", "prone", "side_lying", "quadruped", "kneeling",
                   "half_kneeling", "plank"}
STANDING_POSITIONS = {"standing"}
BENCH_POSITIONS = {"bench_supine", "bench_prone", "bench_incline"}


def derive_from_position(pos):
    if pos is None:
        return {"requires_floor_transition": None, "requires_standing": None}
    return {
        "requires_floor_transition": pos in FLOOR_POSITIONS,
        "requires_standing": pos in STANDING_POSITIONS,
    }


# --------------------------------------------------------------------------
# Regla 3 — lateralidad
# --------------------------------------------------------------------------

def infer_laterality(ex):
    name = ex["name"].lower()
    body = ex["instructions"]["en"].lower()

    if has(r"\balternat", name) or has(r"\balternat", body):
        return "alternating", 0.92
    if has(r"\b(single|one)[- ](arm|leg|handed)\b|\bunilateral\b", name):
        return "unilateral", 0.95
    if has(r"\brepeat\s+(with|on)\s+the\s+other\s+(arm|leg|side)\b", body):
        return "unilateral", 0.88
    if has(r"\b(both|each)\s+(hands?|arms?|legs?)\b", body) and not has(r"\bone\s+(arm|leg)\b", body):
        return "bilateral", 0.75
    return None, 0.0


# --------------------------------------------------------------------------
# Regla 4 — overhead
# --------------------------------------------------------------------------

def infer_overhead(ex):
    name = ex["name"].lower()
    body = ex["instructions"]["en"].lower()
    if has(r"\boverhead\b|\bmilitary\s+press\b|\bshoulder\s+press\b|\bsnatch\b|\bjerk\b|\bpull[- ]?up\b|\bchin[- ]?up\b|\blat\s+pulldown\b", name):
        return True, 0.95
    if has(r"\babove\s+your\s+head\b|\boverhead\b|\bstraight\s+up\s+over\s+your\s+head\b|\bextend(ing)?\s+your\s+arms?\s+(fully\s+)?(up|overhead)\b", body):
        return True, 0.85
    return None, 0.0


# --------------------------------------------------------------------------
# Regla 5 — agarre requerido
# --------------------------------------------------------------------------

HANGING_EQUIP = {"body weight"}
NO_GRIP_EQUIP = {"body weight"}
FIRM_GRIP_EQUIP = {"barbell", "ez barbell", "olympic barbell", "kettlebell",
                   "dumbbell", "trap bar", "weighted", "medicine ball", "hammer"}
LIGHT_GRIP_EQUIP = {"band", "resistance band", "cable", "rope", "roller",
                    "wheel roller", "stability ball", "bosu ball"}


def infer_grip(ex, pos):
    name = ex["name"].lower()
    if pos == "hanging" or has(r"\bpull[- ]?up\b|\bchin[- ]?up\b|\bhang\b|\bmuscle[- ]?up\b", name):
        return "hanging_bodyweight", 0.93
    eq = ex["equipment"]
    if eq in FIRM_GRIP_EQUIP:
        return "firm", 0.85
    if eq in LIGHT_GRIP_EQUIP:
        return "light", 0.80
    if eq == "body weight":
        return "none", 0.70
    return None, 0.0


# --------------------------------------------------------------------------
# Regla 6 — patron de movimiento (parcial: solo lo inequivoco)
# --------------------------------------------------------------------------

PATTERN_RULES = [
    (r"\bsquat\b|\bleg\s+press\b|\bhack\b", "squat"),
    (r"\bdeadlift\b|\bgood\s+morning\b|\brdl\b|\bhip\s+thrust\b|\bhip\s+hinge\b", "hinge"),
    (r"\blunge\b|\bstep[- ]?up\b|\bsplit\s+squat\b", "lunge"),
    (r"\bbench\s+press\b|\bpush[- ]?up\b|\bchest\s+press\b|\bfly\b|\bflye\b|\bdip\b", "horizontal_push"),
    (r"\brow\b|\bface\s+pull\b", "horizontal_pull"),
    (r"\bshoulder\s+press\b|\bmilitary\s+press\b|\boverhead\s+press\b|\bpush\s+press\b|\bjerk\b", "vertical_push"),
    (r"\bpull[- ]?up\b|\bchin[- ]?up\b|\bpulldown\b|\bpull[- ]?down\b", "vertical_pull"),
    (r"\bcrunch\b|\bsit[- ]?up\b|\bleg\s+raise\b|\bknee\s+raise\b|\bv[- ]?up\b", "core_flexion"),
    (r"\bplank\b|\bhollow\b|\bdead\s*bug\b|\bab\s+wheel\b|\brollout\b", "core_antiextension"),
    (r"\btwist\b|\brotation\b|\bwood\s*chop\b|\brussian\b|\bside\s+bend\b", "core_rotation"),
    (r"\bcarry\b|\bfarmer", "carry"),
    (r"\bcurl\b|\bextension\b|\braise\b|\bkickback\b|\bshrug\b|\bcalf\b|\bfly\b", "isolation"),
]


def infer_pattern(ex):
    name = ex["name"].lower()
    if ex["body_part"] == "cardio":
        return "cardio_steady", 0.70
    for pat, val in PATTERN_RULES:
        if has(pat, name):
            return val, 0.85
    return None, 0.0


# --------------------------------------------------------------------------
# Regla 7 — carga axial espinal (solo casos claros)
# --------------------------------------------------------------------------

def infer_axial_load(ex, pos):
    name = ex["name"].lower()
    eq = ex["equipment"]
    # Barra sobre la espalda de pie = carga axial alta, inequivoco
    if has(r"\bsquat\b|\bgood\s+morning\b|\bdeadlift\b|\boverhead\s+press\b|\bmilitary\s+press\b", name) \
            and eq in {"barbell", "olympic barbell", "smith machine", "trap bar", "ez barbell"}:
        return "high", 0.90
    if pos in {"supine", "prone", "side_lying", "bench_supine", "bench_prone", "bench_incline"}:
        return "none", 0.90
    if pos in {"seated", "seated_machine"} and eq in {"body weight", "cable", "band", "resistance band"}:
        return "low", 0.75
    return None, 0.0


# --------------------------------------------------------------------------
# Regla 8 — impacto / pliometria
# --------------------------------------------------------------------------

def infer_impact(ex):
    name = ex["name"].lower()
    if has(r"\bjump\b|\bhop\b|\bplyo|\bbox\s+jump\b|\bburpee\b|\bjumping\b|\bskip", name):
        return "high", 0.92
    if has(r"\brun|\bsprint|\bjog", name):
        return "moderate", 0.85
    if ex["equipment"] in {"stationary bike", "elliptical machine", "upper body ergometer", "skierg machine"}:
        return "none", 0.90
    return None, 0.0


# --------------------------------------------------------------------------
# Regla 9 — equilibrio
# --------------------------------------------------------------------------

def infer_balance(ex, pos, laterality):
    name = ex["name"].lower()
    if has(r"\bsingle[- ]leg\b|\bone[- ]leg\b|\bpistol\b|\bbulgarian\b|\bstork\b", name):
        return "high", True, 0.92
    if pos in {"supine", "prone", "side_lying", "seated_machine", "bench_supine",
               "bench_prone", "bench_incline", "quadruped"}:
        return "none", False, 0.90
    if pos == "seated":
        return "low", False, 0.85
    if ex["equipment"] in {"stability ball", "bosu ball"}:
        return "high", None, 0.85
    if pos == "standing":
        return "moderate", None, 0.60   # requiere verificacion en E2
    return None, None, 0.0


# --------------------------------------------------------------------------
# Regla 10 — complejidad de montaje
# --------------------------------------------------------------------------

def infer_setup(ex):
    eq = ex["equipment"]
    if eq == "body weight":
        return "trivial", 0.90
    if eq in {"dumbbell", "kettlebell", "band", "resistance band", "medicine ball", "weighted"}:
        return "simple", 0.85
    if eq in {"barbell", "olympic barbell", "ez barbell", "smith machine",
              "leverage machine", "cable", "sled machine", "trap bar"}:
        return "complex", 0.80
    return None, 0.0


# --------------------------------------------------------------------------
# Motor
# --------------------------------------------------------------------------

def enrich(ex):
    pos, pos_conf, pos_src = infer_start_position(ex)
    lat, lat_conf = infer_laterality(ex)
    over, over_conf = infer_overhead(ex)
    grip, grip_conf = infer_grip(ex, pos)
    patt, patt_conf = infer_pattern(ex)
    axial, axial_conf = infer_axial_load(ex, pos)
    impact, impact_conf = infer_impact(ex)
    bal, single_leg, bal_conf = infer_balance(ex, pos, lat)
    setup, setup_conf = infer_setup(ex)

    derived = derive_from_position(pos)

    confs = [c for c in [pos_conf, lat_conf, over_conf, grip_conf, patt_conf,
                         axial_conf, impact_conf, bal_conf, setup_conf] if c > 0]

    return {
        "exercise_id": ex["id"],
        "_name": ex["name"],
        "_equipment": ex["equipment"],
        "_body_part": ex["body_part"],
        "_target": ex["target"],

        "start_position": pos,
        "requires_floor_transition": derived["requires_floor_transition"],
        "requires_standing": derived["requires_standing"],
        "requires_balance": bal,
        "single_leg_support": single_leg,
        "overhead_position": over,
        "grip_required": grip,

        "axial_spinal_load": axial,
        "impact_level": impact,

        # Estos NO se infieren por heuristica: son material de seguridad.
        # Se dejan explicitamente en null para que E2 (IA) + E3 (humano)
        # los resuelvan. Adivinarlos aca seria irresponsable.
        "spinal_flexion": None,
        "spinal_extension": None,
        "spinal_rotation": None,
        "joint_stress": None,
        "contraindications": None,
        "cautions": None,
        "safe_for": None,
        "rom_demand": None,
        "difficulty": None,

        "laterality": lat,
        "movement_pattern": patt,
        "setup_complexity": setup,

        "enrichment_source": "heuristic_e1",
        "confidence": round(sum(confs) / len(confs), 3) if confs else 0.0,
        "_field_confidence": {
            "start_position": pos_conf,
            "start_position_src": pos_src,
            "laterality": lat_conf,
            "overhead_position": over_conf,
            "grip_required": grip_conf,
            "movement_pattern": patt_conf,
            "axial_spinal_load": axial_conf,
            "impact_level": impact_conf,
            "requires_balance": bal_conf,
            "setup_complexity": setup_conf,
        },
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    data = json.load(open(SRC, encoding="utf-8"))
    out = [enrich(ex) for ex in data]

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    # ---------------- Reporte de cobertura ----------------
    total = len(out)
    heuristic_fields = ["start_position", "requires_balance", "overhead_position",
                        "grip_required", "laterality", "movement_pattern",
                        "axial_spinal_load", "impact_level", "setup_complexity"]

    lines = ["# E1 — Reporte de cobertura del pre-seed heuristico", "",
             f"**Total ejercicios:** {total}", "",
             "## Cobertura por campo", "",
             "| Campo | Resueltos | Cobertura | Pendiente para E2 |",
             "|---|---:|---:|---:|"]

    for field in heuristic_fields:
        n = sum(1 for r in out if r.get(field) is not None)
        lines.append(f"| `{field}` | {n} | {n/total*100:.1f}% | {total-n} |")

    lines += ["", "## Distribucion de `start_position`", "",
              "| Valor | N |", "|---|---:|"]
    for k, v in Counter(r["start_position"] for r in out).most_common():
        lines.append(f"| {k if k else '**(sin resolver)**'} | {v} |")

    lines += ["", "## Fuente de inferencia de `start_position`", "",
              "| Fuente | N |", "|---|---:|"]
    for k, v in Counter(r["_field_confidence"]["start_position_src"] for r in out).most_common():
        lines.append(f"| {k if k else '(ninguna)'} | {v} |")

    lines += ["", "## Distribucion de `movement_pattern`", "",
              "| Valor | N |", "|---|---:|"]
    for k, v in Counter(r["movement_pattern"] for r in out).most_common():
        lines.append(f"| {k if k else '**(sin resolver)**'} | {v} |")

    # Cola de trabajo para E2
    need_review = [r for r in out if r["confidence"] < 0.75 or r["start_position"] is None]
    lines += ["", "## Cola de trabajo para E2 (IA)", "",
              f"- Ejercicios con `start_position` sin resolver: "
              f"**{sum(1 for r in out if r['start_position'] is None)}**",
              f"- Ejercicios con confianza agregada < 0.75: **{len(need_review)}**",
              "- Campos de seguridad sin tocar por heuristica (100% pendiente): "
              "`joint_stress`, `contraindications`, `cautions`, `safe_for`, "
              "`spinal_flexion/extension/rotation`, `rom_demand`, `difficulty`", ""]

    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\n".join(lines))
    print(f"\n-> {OUT}")
    print(f"-> {REPORT}")


if __name__ == "__main__":
    main()
