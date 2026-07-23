#!/usr/bin/env python3
"""
Deriva los 10 atributos fisiologicos de v1.2 para los ejemplos del gold que
fueron anotados bajo v1.1.

Son derivaciones por regla, no anotacion humana: quedan marcadas con
_derived_v12 = true. E2 los clasifica desde el texto y puede corregirlos.
El objetivo aca es que el motor tenga con que trabajar para poder probarse.
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOLD = os.path.join(BASE, "gold", "gold_examples.json")

L = {"none": 0, "low": 1, "moderate": 2, "high": 3}
INV = {v: k for k, v in L.items()}

FLOOR = {"supine", "prone", "side_lying", "quadruped", "kneeling", "half_kneeling", "plank"}
RECLINED = {"supine", "prone", "side_lying", "bench_supine", "bench_prone"}

# Ejercicios donde la cabeza queda por debajo del corazon
HEAD_DOWN = {"3292",  # elevator - flexion de tronco
             "1471",  # inchworm - manos al suelo
             "0032",  # deadlift - tronco flexionado
             "3303",  # flag
             "3301"}  # frog planche


def derive(e):
    pos = e.get("start_position")
    bal = L.get(e.get("requires_balance") or "none", 0)
    impact = L.get(e.get("impact_level") or "none", 0)
    axial = L.get(e.get("axial_spinal_load") or "none", 0)
    rom = L.get(e.get("rom_demand") or "none", 0)
    diff = e.get("difficulty") or 3
    pat = e.get("movement_pattern") or ""
    grip = e.get("grip_required") or "none"
    eid = e["exercise_id"]

    # --- carga ortostatica: cuanto exige estar erguido ---
    # La carga ortostatica es sobre todo cuestion de VERTICALIDAD del torso.
    # Estar en cuadrupedia o en plancha no es estar erguido: la cabeza queda
    # a la altura del corazon. Confundir eso hace que POTS marque casi todo,
    # y una advertencia en todo no informa nada.
    if pos in RECLINED:
        ortho = "none"
    elif pos in {"quadruped", "plank"}:
        ortho = "none"
    elif pos in {"seated_machine", "bench_incline"}:
        ortho = "low"
    elif pos in {"seated", "kneeling", "half_kneeling"}:
        ortho = "low"
    elif pos == "hanging":
        ortho = "moderate"
    else:  # standing
        ortho = "high" if (e.get("overhead_position")
                           or L.get(e.get("impact_level") or "none", 0) >= 2) else "moderate"

    # --- cambio de posicion ---
    if e.get("requires_floor_transition"):
        change = "high"
    elif pos in FLOOR or eid in HEAD_DOWN:
        change = "moderate"
    elif pos in RECLINED:
        change = "low"
    else:
        change = "none"

    # --- Valsalva: sube con carga axial y dificultad ---
    val = max(axial, diff - 2 if diff >= 4 else 0)
    if pat in {"squat", "hinge", "vertical_push"} and axial >= 2:
        val = max(val, 3)

    # --- isometrica sostenida ---
    iso = 3 if pat == "core_antiextension" or eid in {"3303", "3301"} else \
          2 if pos == "plank" else \
          1 if pat == "carry" else "none_marker"
    iso = 0 if iso == "none_marker" else iso

    # --- intensidad metabolica ---
    if pat in {"cardio_steady", "cardio_interval"}:
        met = 3
    elif impact >= 3 or diff >= 5:
        met = 3
    elif pat in {"squat", "hinge", "lunge"} and diff >= 3:
        met = 2
    elif diff >= 4:
        met = 2
    elif diff <= 1:
        met = 0
    else:
        met = 1

    # --- laxitud articular: rango final bajo carga ---
    lax = 3 if rom >= 3 and axial >= 1 else (2 if rom >= 3 else (1 if rom >= 2 else 0))

    # --- suelo pelvico ---
    pf = max(impact, axial)
    if pat in {"core_flexion", "core_antiextension"}:
        pf = max(pf, 2)
    if pat == "hinge" and axial >= 2:
        pf = 3

    # --- temperatura: sigue a la intensidad ---
    temp = met

    # --- duracion de agarre ---
    if grip == "hanging_bodyweight":
        gd = 3
    elif grip == "firm":
        gd = 2 if pat in {"carry", "horizontal_pull", "vertical_pull"} else 1
    elif grip == "light":
        gd = 1
    else:
        gd = 0

    return {
        "orthostatic_load": ortho,
        "position_change": change,
        "head_below_heart": eid in HEAD_DOWN,
        "valsalva_risk": INV[min(val, 3)],
        "sustained_isometric": INV[min(iso, 3)],
        "metabolic_intensity": INV[min(met, 3)],
        "joint_laxity_risk": INV[min(lax, 3)],
        "pelvic_floor_load": INV[min(pf, 3)],
        "temperature_load": INV[min(temp, 3)],
        "grip_duration": INV[min(gd, 3)],
        "_derived_v12": True,
    }


def main():
    gold = json.load(open(GOLD, encoding="utf-8"))
    n = 0
    for e in gold["examples"]:
        if "orthostatic_load" in e:
            continue
        e.update(derive(e))
        n += 1
    gold["_note"] = gold.get("_note", "") + (
        " | v1.3: +10 atributos fisiologicos derivados por regla desde los "
        "atributos v1.1 (marcados _derived_v12). E2 los reclasifica desde el texto.")
    json.dump(gold, open(GOLD, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    from collections import Counter
    print(f"derivados en {n} ejemplos\n")
    for f in ["orthostatic_load", "metabolic_intensity", "valsalva_risk", "pelvic_floor_load"]:
        c = Counter(e.get(f) for e in gold["examples"])
        print(f"{f:22s} " + "  ".join(f"{k}={v}" for k, v in c.most_common()))


if __name__ == "__main__":
    main()
