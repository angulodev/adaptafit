#!/usr/bin/env python3
"""
Mide el acuerdo entre la salida de E2 y la clasificacion manual.

El set manual (gold + lotes 1-N) es el patron de referencia. Los ejercicios
usados como few-shot dentro del prompt de E2 se EXCLUYEN: medir acuerdo sobre
ejemplos que el modelo ya vio no mide nada.

    python3 e2_validate.py                    # informe completo
    python3 e2_validate.py --field start_position
    python3 e2_validate.py --show-disagreements 20

Criterio de decision sugerido:
  - Campos estructurales   >= 90%  -> E2 es confiable para el resto del catalogo
  - Contraindicaciones     recall >= 95%  -> no se le escapan riesgos
  - Falsos "seguro"        <= 2%   -> el error que puede lesionar a alguien
"""
import argparse
import json
import os
import sys
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUAL = os.path.join(BASE, "output", "manual_classified.json")
E2 = os.path.join(BASE, "output", "e2_output.json")
GOLD = os.path.join(BASE, "gold", "gold_examples.json")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SCALAR_FIELDS = [
    "start_position", "requires_floor_transition", "requires_standing",
    "requires_balance", "single_leg_support", "overhead_position",
    "grip_required", "axial_spinal_load", "spinal_flexion", "spinal_extension",
    "spinal_rotation", "impact_level", "laterality", "movement_pattern",
    "difficulty", "rom_demand", "orthostatic_load", "position_change",
    "head_below_heart", "valsalva_risk", "sustained_isometric",
    "metabolic_intensity", "joint_laxity_risk", "pelvic_floor_load",
    "temperature_load", "grip_duration",
]
LEVELS = ["none", "low", "moderate", "high"]
JOINTS = ["knee", "hip", "lumbar_spine", "cervical_spine", "shoulder",
          "elbow", "wrist", "ankle"]


def load_fewshot_ids():
    """Ids que el modelo vio dentro del prompt. Se excluyen de la medicion."""
    ids = set()
    try:
        import e2_classify as e2
        ids |= set(getattr(e2, "FEWSHOT_IDS", []))
        ids |= set(getattr(e2, "MANUAL_FEWSHOT_IDS", []))
    except Exception:
        pass
    return ids


def level_distance(a, b):
    """Distancia en la escala none<low<moderate<high. None si no aplica."""
    if a in LEVELS and b in LEVELS:
        return abs(LEVELS.index(a) - LEVELS.index(b))
    return None


def compare(manual, e2out, skip_ids):
    man = {r["exercise_id"]: r for r in manual if r["exercise_id"] not in skip_ids}
    mod = {r["exercise_id"]: r for r in e2out}
    shared = sorted(set(man) & set(mod))

    field_hits = {f: [0, 0] for f in SCALAR_FIELDS}   # [aciertos, total]
    near_miss = Counter()                             # off-by-one en escalas
    disagreements = []

    joint_hits = [0, 0]
    joint_near = 0

    contra_tp = contra_fn = contra_fp = 0
    unsafe_calls = []      # el modelo dijo "seguro" donde el manual contraindica
    safe_tp = safe_fp = 0

    for eid in shared:
        a, b = man[eid], mod[eid]

        for f in SCALAR_FIELDS:
            if f not in a or f not in b:
                continue
            field_hits[f][1] += 1
            if a[f] == b[f]:
                field_hits[f][0] += 1
            else:
                d = level_distance(a[f], b[f])
                if d == 1:
                    near_miss[f] += 1
                disagreements.append((eid, a.get("_name", ""), f, a[f], b[f]))

        ja, jb = a.get("joint_stress", {}), b.get("joint_stress", {})
        for j in JOINTS:
            if j in ja and j in jb:
                joint_hits[1] += 1
                if ja[j] == jb[j]:
                    joint_hits[0] += 1
                elif level_distance(ja[j], jb[j]) == 1:
                    joint_near += 1

        ca, cb = set(a.get("contraindications", [])), set(b.get("contraindications", []))
        contra_tp += len(ca & cb)
        contra_fn += len(ca - cb)
        contra_fp += len(cb - ca)

        sa, sb = set(a.get("safe_for", [])), set(b.get("safe_for", []))
        safe_tp += len(sa & sb)
        safe_fp += len(sb - sa)

        # El error critico: el modelo declara seguro algo que el manual prohibe.
        bad = sb & (ca | set(a.get("cautions", [])))
        if bad:
            unsafe_calls.append((eid, a.get("_name", ""), sorted(bad)))

    return dict(shared=shared, field_hits=field_hits, near_miss=near_miss,
                joint_hits=joint_hits, joint_near=joint_near,
                contra=(contra_tp, contra_fn, contra_fp),
                safe=(safe_tp, safe_fp), unsafe_calls=unsafe_calls,
                disagreements=disagreements)


def bar(pct, width=24):
    n = int(round(pct / 100 * width))
    return "█" * n + "░" * (width - n)


def report(r, show_disagreements=0):
    n = len(r["shared"])
    print(f"\n{'='*68}\n  ACUERDO E2 vs CLASIFICACION MANUAL — {n} ejercicios comparados\n{'='*68}\n")

    print("Campos estructurales\n")
    rows = []
    for f, (hit, tot) in r["field_hits"].items():
        if tot:
            rows.append((hit / tot * 100, f, hit, tot, r["near_miss"][f]))
    rows.sort()
    for pct, f, hit, tot, near in rows:
        extra = f"  (+{near} a un nivel)" if near else ""
        print(f"  {f:26} {bar(pct)} {pct:5.1f}%  {hit}/{tot}{extra}")

    overall = sum(h for h, _ in r["field_hits"].values())
    total = sum(t for _, t in r["field_hits"].values())
    print(f"\n  {'GLOBAL':26} {bar(overall/total*100)} {overall/total*100:5.1f}%  {overall}/{total}\n")

    jh, jt = r["joint_hits"]
    print(f"joint_stress (8 articulaciones)\n")
    print(f"  {'exacto':26} {bar(jh/jt*100)} {jh/jt*100:5.1f}%  {jh}/{jt}")
    print(f"  {'a un nivel de distancia':26} {r['joint_near']} casos\n")

    tp, fn, fp = r["contra"]
    recall = tp / (tp + fn) * 100 if tp + fn else 0
    prec = tp / (tp + fp) * 100 if tp + fp else 0
    print("Contraindicaciones\n")
    print(f"  recall    {bar(recall)} {recall:5.1f}%   (encontro {tp} de {tp+fn})")
    print(f"  precision {bar(prec)} {prec:5.1f}%   ({fp} que el manual no marco)")
    print("\n  El recall es el numero que importa: cada contraindicacion perdida")
    print("  es un ejercicio peligroso que el motor va a ofrecer.\n")

    stp, sfp = r["safe"]
    print(f"safe_for\n  coincidencias {stp} · el modelo agrego {sfp}\n")

    bad = r["unsafe_calls"]
    print(f"{'-'*68}\n  FALSOS SEGURO — el error que puede lesionar\n{'-'*68}")
    if not bad:
        print("\n  Ninguno. El modelo nunca puso en safe_for algo que el manual")
        print("  marca como contraindicacion o precaucion.\n")
    else:
        pct = len(bad) / len(r["shared"]) * 100
        print(f"\n  {len(bad)} de {len(r['shared'])} ejercicios ({pct:.1f}%)\n")
        for eid, name, conds in bad[:25]:
            print(f"  [{eid}] {name}")
            print(f"         declara seguro: {', '.join(conds)}")
        if len(bad) > 25:
            print(f"\n  ... y {len(bad)-25} mas")
        print("\n  Estos van a revision humana en E3, sin excepcion.\n")

    if show_disagreements:
        print(f"{'-'*68}\n  DESACUERDOS (primeros {show_disagreements})\n{'-'*68}\n")
        for eid, name, f, a, b in r["disagreements"][:show_disagreements]:
            print(f"  [{eid}] {name[:38]:38} {f}")
            print(f"         manual={a!r}   e2={b!r}")
        print()

    print(f"{'='*68}\n  VEREDICTO\n{'='*68}\n")
    ok = (overall / total * 100 >= 90 and recall >= 95
          and len(bad) / len(r["shared"]) * 100 <= 2)
    if ok:
        print("  E2 pasa los tres umbrales. Es razonable correrlo sobre el resto")
        print("  del catalogo y mandar a E3 solo los de confidence baja y los")
        print("  falsos seguro detectados.\n")
    else:
        print("  E2 NO pasa algun umbral. Antes de confiar en el resto del")
        print("  catalogo conviene revisar el prompt en los campos peores, o")
        print("  seguir a mano en las familias donde mas falla.\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--field")
    ap.add_argument("--show-disagreements", type=int, default=0)
    a = ap.parse_args()

    if not os.path.exists(E2):
        sys.exit(f"Todavia no existe {E2}. Corre e2_classify.py primero.")

    manual = json.load(open(MANUAL, encoding="utf-8"))
    try:
        g = json.load(open(GOLD, encoding="utf-8"))
        manual = manual + g.get("examples", [])
    except Exception:
        pass

    e2out = json.load(open(E2, encoding="utf-8"))
    if isinstance(e2out, dict):
        e2out = e2out.get("records", e2out.get("results", []))

    skip = load_fewshot_ids()
    r = compare(manual, e2out, skip)

    if not r["shared"]:
        sys.exit("No hay ejercicios en comun entre el manual y la salida de E2.")

    print(f"\nExcluidos por haber sido few-shot en el prompt: {len(skip)}")

    if a.field:
        rows = [d for d in r["disagreements"] if d[2] == a.field]
        hit, tot = r["field_hits"].get(a.field, (0, 0))
        print(f"\n{a.field}: {hit}/{tot} ({hit/tot*100:.1f}%)\n")
        for eid, name, f, x, y in rows:
            print(f"  [{eid}] {name[:40]:40} manual={x!r}  e2={y!r}")
        return

    report(r, a.show_disagreements)


if __name__ == "__main__":
    main()
