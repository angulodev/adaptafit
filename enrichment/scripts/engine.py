#!/usr/bin/env python3
"""
Motor de filtrado adaptativo — el nucleo del producto.

Dado un perfil de capacidades y restricciones, filtra el catalogo y devuelve
lo ejecutable, con el registro completo de por que se excluyo cada cosa.

Principio de diseno: TODA exclusion es explicable. Si el motor oculta algo,
tiene que poder decir cual regla lo hizo y de que capa vino. Un filtro que
oculta en silencio es un filtro en el que no se puede confiar.

Uso:
    python3 engine.py --demo              # corre los perfiles de ejemplo
    python3 engine.py --profile estefani  # un perfil puntual
"""

import argparse
import json
import os
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAX = os.path.join(BASE, "taxonomy", "taxonomy_v1.json")
GOLD = os.path.join(BASE, "gold", "gold_examples.json")
E2 = os.path.join(BASE, "output", "e2_output.json")

LEVEL = {"none": 0, "low": 1, "moderate": 2, "high": 3}


# ==========================================================================
# Capa A — restricciones de movilidad. FILTRO DURO.
# ==========================================================================
# Cada regla: condicion -> (funcion que detecta incompatibilidad, motivo legible)
# Objetivas, sin ambiguedad medica. "No me puedo parar" es un hecho, no un
# diagnostico. Por eso pueden excluir sin pedir permiso.

FLOOR_POSITIONS = {"supine", "prone", "side_lying", "quadruped",
                   "kneeling", "half_kneeling", "plank"}

LAYER_A = {
    "cannot_stand": (
        lambda a: a.get("requires_standing") is True,
        "requiere estar de pie"),
    "cannot_get_on_floor": (
        lambda a: a.get("requires_floor_transition") is True
                  or a.get("start_position") in FLOOR_POSITIONS,
        "requiere bajar al suelo"),
    "cannot_kneel": (
        lambda a: a.get("start_position") in {"kneeling", "half_kneeling", "quadruped"},
        "se hace arrodillado"),
    "cannot_lie_prone": (
        lambda a: a.get("start_position") in {"prone", "bench_prone"},
        "se hace boca abajo"),
    "cannot_lie_supine": (
        lambda a: a.get("start_position") in {"supine", "bench_supine"},
        "se hace boca arriba"),
    "cannot_lie_on_side": (
        lambda a: a.get("start_position") == "side_lying",
        "se hace de costado"),
    "no_overhead": (
        lambda a: a.get("overhead_position") is True,
        "exige levantar los brazos sobre la cabeza"),
    "limited_grip": (
        lambda a: a.get("grip_required") in {"firm", "hanging_bodyweight"},
        "exige agarre firme"),
    "limited_balance": (
        lambda a: LEVEL.get(a.get("requires_balance") or "none", 0) >= 2
                  or a.get("single_leg_support") is True,
        "exige equilibrio"),
    "cannot_sit_unsupported": (
        lambda a: a.get("start_position") == "seated"
                  and LEVEL.get(a.get("requires_balance") or "none", 0) >= 1,
        "exige sentarse sin respaldo"),
    "cannot_transfer_to_bench": (
        lambda a: str(a.get("start_position") or "").startswith("bench"),
        "requiere subir a un banco"),
    "one_arm_only": (
        lambda a: a.get("laterality") == "bilateral"
                  and a.get("grip_required") in {"firm", "hanging_bodyweight"},
        "necesita los dos brazos"),
    "visual_impairment": (
        lambda a: LEVEL.get(a.get("requires_balance") or "none", 0) >= 3
                  or LEVEL.get(a.get("impact_level") or "none", 0) >= 3,
        "exige equilibrio o impacto alto sin referencia visual"),
    "wheelchair": (
        lambda a: a.get("requires_standing") is True
                  or a.get("requires_floor_transition") is True
                  or a.get("start_position") in FLOOR_POSITIONS,
        "no es accesible en silla de ruedas"),
}


# ==========================================================================
# Capa B — lesion articular. FILTRO POR UMBRAL.
# ==========================================================================
# La severidad que declara la persona define el umbral de estres tolerado.

CONDITION_TO_JOINT = {
    "knee_injury": "knee", "knee_replacement": "knee",
    "hip_replacement": "hip",
    "lumbar_disc": "lumbar_spine", "lumbar_pain": "lumbar_spine",
    "cervical_injury": "cervical_spine",
    "shoulder_impingement": "shoulder", "rotator_cuff": "shoulder",
    "elbow_injury": "elbow", "wrist_injury": "wrist",
    "ankle_injury": "ankle",
    # v1.2 - condiciones de dolor (mas leves que _injury, mismo eje articular)
    "knee_pain": "knee", "shoulder_pain": "shoulder", "neck_pain": "cervical_spine",
    "hip_pain": "hip", "sciatica": "lumbar_spine", "si_joint_pain": "lumbar_spine",
    "plantar_fasciitis": "ankle", "tendinitis_elbow": "elbow",
    "carpal_tunnel": "wrist", "osteoarthritis": "knee",
    "rheumatoid_arthritis": "wrist",
}

JOINT_ES = {"knee": "rodilla", "hip": "cadera", "lumbar_spine": "espalda baja",
            "cervical_spine": "cuello", "shoulder": "hombro", "elbow": "codo",
            "wrist": "muneca", "ankle": "tobillo"}

# molestia -> excluye solo 'high' | lesion -> excluye 'moderate' y 'high'
# postoperatorio -> solo tolera 'none'
SEVERITY_THRESHOLD = {"molestia": 3, "lesion": 2, "postoperatorio": 1}


# ==========================================================================
# Capa C — sistemica. NO FILTRA: advierte.
# ==========================================================================

LAYER_C_ES = {
    "hypertension": "hipertension", "cardiac": "condicion cardiaca",
    "osteoporosis": "osteoporosis", "hernia_abdominal": "hernia abdominal",
    "pregnancy_1st": "embarazo (1er trimestre)",
    "pregnancy_2nd": "embarazo (2do trimestre)",
    "pregnancy_3rd": "embarazo (3er trimestre)",
    "vertigo": "vertigo", "glaucoma": "glaucoma",
    "obesity": "obesidad", "elderly_65plus": "65+ anos",
    "dysautonomia": "disautonomia", "chronic_fatigue": "fatiga cronica (EM/SFC)",
    "fibromyalgia": "fibromialgia", "hypermobility": "hipermovilidad",
    "multiple_sclerosis": "esclerosis multiple", "asthma": "asma",
    "diabetes": "diabetes", "epilepsy": "epilepsia", "migraine": "migrana",
    "anemia": "anemia", "varicose_veins": "varices", "postpartum": "posparto",
    "pelvic_floor_dysfunction": "suelo pelvico",
    "recent_abdominal_surgery": "cirugia abdominal reciente",
    "retinal_detachment_risk": "riesgo de desprendimiento de retina",
}


# ==========================================================================
# Capa C-fisiologica — condiciones que NO se filtran por articulacion
# ==========================================================================
# Disautonomia, EM/SFC, hipermovilidad y compania no dependen de que
# articulacion se carga sino de variables fisiologicas transversales.
# Sin estas reglas, agregarlas al enum no haria absolutamente nada.
#
# Cada entrada: condicion -> (atributo, umbral, motivo legible)
# Igual que el resto de la Capa C: ADVIERTE, no oculta.

PHYSIOLOGIC_RULES = {
    "dysautonomia": [
        ("orthostatic_load", 2, "exige estar erguido de forma sostenida"),
        ("position_change", 2, "implica cambios de posicion que pueden causar mareo"),
        ("metabolic_intensity", 3, "intensidad alta"),
        ("temperature_load", 3, "genera mucho calor corporal"),
    ],
    "chronic_fatigue": [
        ("metabolic_intensity", 2, "puede superar el umbral de esfuerzo"),
        ("orthostatic_load", 3, "carga ortostatica alta"),
    ],
    "fibromyalgia": [
        ("metabolic_intensity", 3, "intensidad alta"),
        ("impact_level", 2, "tiene impacto"),
    ],
    "hypermobility": [
        ("joint_laxity_risk", 2, "trabaja en rango final de movimiento"),
        ("rom_demand", 3, "exige rango de movimiento maximo"),
    ],
    "multiple_sclerosis": [
        ("temperature_load", 2, "genera calor (fenomeno de Uhthoff)"),
        ("requires_balance", 2, "exige equilibrio"),
    ],
    "hypertension": [
        ("valsalva_risk", 2, "riesgo de maniobra de Valsalva"),
        ("sustained_isometric", 3, "isometrica prolongada eleva la presion"),
        ("head_below_heart", True, "la cabeza queda por debajo del corazon"),
    ],
    "glaucoma": [
        ("head_below_heart", True, "la cabeza queda por debajo del corazon"),
        ("valsalva_risk", 2, "aumenta la presion intraocular"),
    ],
    "retinal_detachment_risk": [
        ("head_below_heart", True, "posicion invertida"),
        ("impact_level", 2, "impacto"),
        ("valsalva_risk", 3, "Valsalva intensa"),
    ],
    "pelvic_floor_dysfunction": [
        ("pelvic_floor_load", 2, "aumenta la presion sobre el suelo pelvico"),
        ("impact_level", 2, "impacto"),
    ],
    "postpartum": [
        ("pelvic_floor_load", 2, "carga sobre el suelo pelvico"),
        ("impact_level", 2, "impacto"),
    ],
    "recent_abdominal_surgery": [
        ("pelvic_floor_load", 1, "presion intraabdominal"),
        ("spinal_flexion", 2, "flexion de tronco"),
    ],
    "carpal_tunnel": [
        ("grip_duration", 2, "agarre sostenido"),
    ],
    "rheumatoid_arthritis": [
        ("grip_duration", 2, "agarre sostenido"),
        ("impact_level", 2, "impacto"),
    ],
    "varicose_veins": [
        ("orthostatic_load", 3, "de pie sostenido"),
        ("sustained_isometric", 3, "isometrica prolongada"),
    ],
    "asthma": [
        ("metabolic_intensity", 3, "intensidad alta"),
    ],
    "anemia": [
        ("metabolic_intensity", 3, "intensidad alta"),
        ("orthostatic_load", 3, "carga ortostatica alta"),
    ],
    "epilepsy": [
        ("head_below_heart", True, "posicion invertida"),
    ],
    "cardiac": [
        ("metabolic_intensity", 3, "intensidad alta"),
        ("valsalva_risk", 2, "Valsalva"),
        ("sustained_isometric", 3, "isometrica prolongada"),
    ],
}


def physiologic_warnings(attrs, systemic):
    """Advertencias fisiologicas. Devuelve lista de motivos legibles."""
    out = []
    for cond in systemic:
        for field, threshold, reason in PHYSIOLOGIC_RULES.get(cond, []):
            v = attrs.get(field)
            if v is None:
                continue
            trig = (v is True) if threshold is True else (LEVEL.get(v, 0) >= threshold)
            if trig:
                out.append(f"{LAYER_C_ES.get(cond, cond)}: {reason}")
                break
    return out

HOME_EQUIPMENT_PRESETS = {
    "sin_equipo": {"body weight"},
    "casa_basica": {"body weight", "dumbbell", "band", "resistance band"},
    "casa_completa": {"body weight", "dumbbell", "barbell", "band",
                      "resistance band", "ez barbell", "olympic barbell", "weighted"},
}


# ==========================================================================
# Motor
# ==========================================================================

class Result:
    def __init__(self):
        self.eligible = []
        self.excluded = []      # (id, nombre, capa, motivo)
        self.flagged = []       # (id, nombre, [advertencias])

    @property
    def exclusion_reasons(self):
        return Counter(f"{c} · {m}" for _, _, c, m in self.excluded)


def filter_catalog(catalog, profile):
    """
    profile = {
      "mobility":   ["cannot_stand", ...],            # Capa A
      "joints":     {"knee_injury": "lesion", ...},   # Capa B + severidad
      "systemic":   ["hypertension", ...],            # Capa C
      "equipment":  {"body weight", "dumbbell"},      # Capa D
    }
    """
    res = Result()
    mobility = profile.get("mobility", [])
    joints = profile.get("joints", {})
    systemic = profile.get("systemic", [])
    equipment = profile.get("equipment")

    for item in catalog:
        a = item["attrs"]
        eid, name = item["id"], item["name"]

        # --- Capa D: equipamiento (filtro duro, barato, va primero) ---
        if equipment is not None and item.get("equipment") not in equipment:
            res.excluded.append((eid, name, "equipo", f"necesita {item.get('equipment')}"))
            continue

        # --- Capa A: movilidad (filtro duro) ---
        hit = None
        for cond in mobility:
            rule = LAYER_A.get(cond)
            if rule and rule[0](a):
                hit = ("movilidad", rule[1])
                break
        if hit:
            res.excluded.append((eid, name, *hit))
            continue

        # --- Contraindicacion explicita del dataset enriquecido ---
        declared = set(a.get("contraindications") or [])
        blocking = declared & (set(mobility) | set(joints))
        if blocking:
            c = sorted(blocking)[0]
            res.excluded.append((eid, name, "contraindicado", f"contraindicado con {c}"))
            continue

        # --- Capa B: lesion articular por umbral ---
        hit = None
        for cond, severity in joints.items():
            joint = CONDITION_TO_JOINT.get(cond)
            if not joint:
                continue
            stress = (a.get("joint_stress") or {}).get(joint, "none")
            if LEVEL.get(stress, 0) >= SEVERITY_THRESHOLD.get(severity, 2):
                hit = ("lesion", f"carga {JOINT_ES.get(joint, joint)} ({stress})")
                break
        if hit:
            res.excluded.append((eid, name, *hit))
            continue

        # --- Capa C: sistemica -> NO excluye, marca ---
        warns = []
        for cond in systemic:
            if cond in (a.get("contraindications") or []):
                warns.append(f"desaconsejado con {LAYER_C_ES.get(cond, cond)}")
            elif cond in (a.get("cautions") or []):
                warns.append(f"precaucion por {LAYER_C_ES.get(cond, cond)}")
        # Reglas fisiologicas transversales (disautonomia, EM/SFC, etc.)
        warns += physiologic_warnings(a, systemic)
        if warns:
            res.flagged.append((eid, name, warns))

        res.eligible.append(item)

    return res


def rank(eligible, profile):
    """Ordena: primero lo explicitamente seguro, luego por dificultad cercana al nivel."""
    target = profile.get("level", 2)
    safe_set = set(profile.get("mobility", [])) | set(profile.get("joints", {}))

    def key(item):
        a = item["attrs"]
        n_safe = len(set(a.get("safe_for") or []) & safe_set)
        gap = abs((a.get("difficulty") or 3) - target)
        return (-n_safe, gap, a.get("setup_complexity") == "complex")

    return sorted(eligible, key=key)


# ==========================================================================
# Carga de datos
# ==========================================================================

def load_catalog():
    """Usa e2_output.json si existe; si no, el gold set (54 anotados a mano)."""
    src = json.load(open(os.path.join(BASE, "source", "exercises.json"), encoding="utf-8"))
    meta = {x["id"]: x for x in src}

    MANUAL = os.path.join(BASE, "output", "manual_classified.json")
    if os.path.exists(E2):
        recs = json.load(open(E2, encoding="utf-8"))
        origin = "e2_output.json"
    elif os.path.exists(MANUAL):
        # gold + lo clasificado a mano en chat
        recs = json.load(open(GOLD, encoding="utf-8"))["examples"]
        seen = {r["exercise_id"] for r in recs}
        recs += [r for r in json.load(open(MANUAL, encoding="utf-8"))
                 if r["exercise_id"] not in seen]
        origin = f"gold + manual ({len(recs)} clasificados a mano)"
    else:
        recs = json.load(open(GOLD, encoding="utf-8"))["examples"]
        origin = "gold_examples.json (54 anotados a mano)"

    catalog = []
    for r in recs:
        eid = r["exercise_id"]
        m = meta.get(eid, {})
        catalog.append({
            "id": eid,
            "name": m.get("name", r.get("_name", eid)),
            "equipment": m.get("equipment"),
            "body_part": m.get("body_part"),
            "attrs": {k: v for k, v in r.items() if not k.startswith("_")},
        })
    return catalog, origin


# ==========================================================================
# Perfiles de prueba
# ==========================================================================

PROFILES = {
    "sin_restricciones": {
        "_label": "Sin restricciones · casa completa",
        "equipment": HOME_EQUIPMENT_PRESETS["casa_completa"],
        "level": 3,
    },
    "estefani": {
        "_label": "Movilidad reducida · no puede pararse ni bajar al suelo",
        "mobility": ["cannot_stand", "cannot_get_on_floor", "limited_balance"],
        "joints": {"knee_injury": "lesion"},
        "equipment": HOME_EQUIPMENT_PRESETS["casa_basica"],
        "level": 1,
    },
    "espalda": {
        "_label": "Hernia discal lumbar · resto sin problemas",
        "joints": {"lumbar_disc": "lesion"},
        "equipment": HOME_EQUIPMENT_PRESETS["casa_completa"],
        "level": 2,
    },
    "hombro": {
        "_label": "Pinzamiento de hombro · sin levantar brazos",
        "mobility": ["no_overhead"],
        "joints": {"shoulder_impingement": "lesion"},
        "equipment": HOME_EQUIPMENT_PRESETS["casa_completa"],
        "level": 2,
    },
    "silla_ruedas": {
        "_label": "Usuario de silla de ruedas",
        "mobility": ["wheelchair", "cannot_stand", "cannot_get_on_floor"],
        "equipment": HOME_EQUIPMENT_PRESETS["casa_basica"],
        "level": 2,
    },
    "embarazo": {
        "_label": "Embarazo 2do trimestre · Capa C, solo advierte",
        "systemic": ["pregnancy_2nd"],
        "equipment": HOME_EQUIPMENT_PRESETS["casa_basica"],
        "level": 1,
    },
    "adulto_mayor": {
        "_label": "70 anos · equilibrio limitado, hipertension",
        "mobility": ["limited_balance", "cannot_get_on_floor"],
        "systemic": ["elderly_65plus", "hypertension", "osteoporosis"],
        "equipment": HOME_EQUIPMENT_PRESETS["casa_basica"],
        "level": 1,
    },
}


def filter_with_fallback(catalog, profile):
    """
    Filtra normal. Si el resultado queda vacio, relaja en orden definido y
    reporta que se relajo.

    NUNCA relaja la Capa A: si alguien no se puede parar, no se puede parar.
    Eso no es negociable por falta de opciones. Lo que se relaja es el
    equipamiento (se puede conseguir) y el umbral de lesion (con advertencia).
    """
    res = filter_catalog(catalog, profile)
    if res.eligible:
        return res, []

    relaxed = []

    # 1) Soltar el filtro de equipamiento: es lo mas barato de resolver.
    p = dict(profile); p["equipment"] = None
    res = filter_catalog(catalog, p)
    if res.eligible:
        relaxed.append("se ignoro el equipamiento disponible")
        return res, relaxed

    # 2) Aflojar el umbral de lesion un escalon, con advertencia explicita.
    p = dict(profile)
    p["joints"] = {k: ("lesion" if v == "postoperatorio" else "molestia")
                   for k, v in (profile.get("joints") or {}).items()}
    res = filter_catalog(catalog, p)
    if res.eligible:
        relaxed += ["se ignoro el equipamiento disponible",
                    "se aflojo el umbral de lesion — revisar cada ejercicio con criterio"]
        return res, relaxed

    return res, ["sin resultados ni relajando los filtros"]


def show(name, profile, catalog):
    res, relaxed = filter_with_fallback(catalog, profile)
    ranked = rank(res.eligible, profile)
    total = len(catalog)

    print("=" * 68)
    print(f"  {profile['_label']}")
    print("=" * 68)
    pct = len(res.eligible) / total * 100 if total else 0
    print(f"  {len(res.eligible)} de {total} ejercicios disponibles ({pct:.0f}%)")

    if res.exclusion_reasons:
        print(f"\n  Se ocultaron {len(res.excluded)}:")
        for reason, n in res.exclusion_reasons.most_common(6):
            print(f"    {n:3d}  {reason}")

    if ranked:
        print(f"\n  Recomendados:")
        for item in ranked[:6]:
            a = item["attrs"]
            print(f"    · {item['name'][:38]:40s} {str(a.get('start_position')):14s} dif {a.get('difficulty')}")

    if res.flagged:
        print(f"\n  Con advertencia (visibles, no ocultos): {len(res.flagged)}")
        for _, nm, ws in res.flagged[:3]:
            print(f"    ⚠ {nm[:36]:38s} {ws[0]}")

    if not ranked:
        print("\n  ⚠ CATALOGO VACIO — el perfil es demasiado restrictivo.")
    if relaxed:
        print(f"\n  ⚠ Sin resultados con el perfil exacto. Para no dejarte sin nada:")
        for r in relaxed:
            print(f"    · {r}")
    print()
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--profile")
    args = ap.parse_args()

    catalog, origin = load_catalog()
    print(f"\nCatalogo: {len(catalog)} ejercicios · fuente: {origin}\n")

    if args.profile:
        show(args.profile, PROFILES[args.profile], catalog)
    else:
        for name, prof in PROFILES.items():
            show(name, prof, catalog)


if __name__ == "__main__":
    main()
