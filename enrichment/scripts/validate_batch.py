#!/usr/bin/env python3
"""
Validador de lotes de clasificacion manual.

Corre TODAS las comprobaciones que veniamos haciendo a mano en cada lote, mas
las reglas derivadas (D-020). Pensado para correr ANTES de aplicar el lote al
JSON, y tambien como auditoria sobre todo lo ya clasificado.

Uso:
    python3 validate_batch.py 45          # valida el lote 45 sin aplicarlo
    python3 validate_batch.py --all       # audita manual_classified.json entero
"""

import argparse
import importlib.util
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOLD = os.path.join(BASE, "gold")
TAX = os.path.join(BASE, "taxonomy", "taxonomy_v1.json")
MANUAL = os.path.join(BASE, "output", "manual_classified.json")
SRC = os.path.join(BASE, "source", "exercises.json")

JOINTS = {"knee", "hip", "lumbar_spine", "cervical_spine", "shoulder",
          "elbow", "wrist", "ankle"}

# D-020: frases que asignan un rol a la segunda mano.
DOS_MANOS = re.compile(r"in each hand|with both hands|hands (?:on|against) (?:a |the )?wall",
                       re.I)
MANO_APOYO = re.compile(r"\b(other|free|opposite|non-?working)\s+(hand|arm)\b", re.I)
# ...descontando las frases de alternancia, que NO son rol de apoyo.
ALTERNANCIA = re.compile(r"(switch|repeat|change)[^.]{0,30}\b(other|opposite)\s+(arm|hand|side)",
                         re.I)


def load_tax():
    t = json.load(open(TAX, encoding="utf-8"))
    conds = set()
    for items in t["condition_layers"].values():
        conds |= set(items if isinstance(items, list) else items.keys())
    return t["enums"], conds


def load_src_text():
    out = {}
    for x in json.load(open(SRC, encoding="utf-8")):
        i = x.get("instructions") or ""
        if isinstance(i, dict):
            i = i.get("en") or next(iter(i.values()), "")
        if isinstance(i, list):
            i = " ".join(map(str, i))
        out[x["id"]] = str(i)
    return out


def check(recs, enums, conds, texts, known_ids=()):
    errs, warns = [], []
    seen = set()
    for e in recs:
        i = e["exercise_id"]
        if i in seen:
            errs.append(f"{i}: duplicado dentro del lote")
        if i in known_ids:
            errs.append(f"{i}: ya clasificado en un lote anterior")
        seen.add(i)

        for field in ("start_position", "grip_required", "laterality",
                      "movement_pattern"):
            if e[field] not in enums[field]:
                errs.append(f"{i} {field} invalido: {e[field]!r}")

        if set(e["joint_stress"]) != JOINTS:
            falta = JOINTS - set(e["joint_stress"])
            errs.append(f"{i} joint_stress incompleto, falta {sorted(falta)}")

        for k in ("contraindications", "cautions", "safe_for"):
            for c in e[k]:
                if c not in conds:
                    errs.append(f"{i} {k}: condicion inexistente {c!r}")

        for a, b in (("contraindications", "safe_for"),
                     ("cautions", "safe_for"),
                     ("contraindications", "cautions")):
            ov = set(e[a]) & set(e[b])
            if ov:
                errs.append(f"{i} {a} y {b} se solapan en {sorted(ov)}")

        # --- D-020 ---
        # Ojo: laterality puede referirse a las PIERNAS. Una elevacion de
        # talon bilateral no ocupa las manos, asi que si es apta para
        # one_arm_only. El criterio duro solo aplica cuando hay agarre.
        if "one_arm_only" in e["safe_for"]:
            # Distinguir agarre que CARGA de agarre que solo estabiliza:
            # en una elevacion de talon las manos apoyan y basta una.
            PATRONES_BRAZO = {"vertical_pull", "horizontal_pull",
                              "vertical_push", "horizontal_push"}
            carga_manos = (e["movement_pattern"] in PATRONES_BRAZO
                           or e["grip_required"] == "firm")
            t = texts.get(i, "")
            t_sin_alt = ALTERNANCIA.sub(" ", t)
            rol_2a_mano = bool(DOS_MANOS.search(t_sin_alt)
                               or MANO_APOYO.search(t_sin_alt))
            if carga_manos and e["laterality"] != "unilateral":
                errs.append(f"{i} D-020: one_arm_only con agarre "
                            f"{e['grip_required']} y laterality="
                            f"{e['laterality']} — las dos manos cargan")
            elif carga_manos and rol_2a_mano:
                errs.append(f"{i} D-020: one_arm_only pero el texto asigna "
                            f"rol a la segunda mano")
            elif rol_2a_mano:
                warns.append(f"{i} D-020: sin agarre, pero el texto menciona "
                             f"las dos manos — apoyo de equilibrio? revisar")

        # --- coherencias blandas ---
        if e["single_leg_support"] and e["requires_balance"] in ("none", "low"):
            warns.append(f"{i}: single_leg_support con balance "
                         f"{e['requires_balance']} — revisar regla del apoyo")
        if e["overhead_position"] and "no_overhead" not in e["contraindications"]:
            errs.append(f"{i}: overhead_position sin no_overhead en contra")
        if e["requires_standing"] and "cannot_stand" not in e["contraindications"]:
            errs.append(f"{i}: requires_standing sin cannot_stand en contra")
        if e.get("confidence", 1) < 0.7 and not e.get("_reasoning"):
            warns.append(f"{i}: confidence baja sin razonamiento escrito")

    return errs, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lote", nargs="?", help="numero de lote, ej: 45")
    ap.add_argument("--all", action="store_true",
                    help="auditar manual_classified.json completo")
    a = ap.parse_args()

    enums, conds = load_tax()
    texts = load_src_text()

    if a.all:
        recs = json.load(open(MANUAL, encoding="utf-8"))
        known = ()
        etiqueta = f"auditoria completa ({len(recs)} fichas)"
    else:
        if not a.lote:
            ap.error("indica un numero de lote o usa --all")
        path = os.path.join(GOLD, f"batch_manual_{int(a.lote):02d}.py")
        spec = importlib.util.spec_from_file_location("lote", path)
        mod = importlib.util.module_from_spec(spec)
        sys.path.insert(0, GOLD)
        spec.loader.exec_module(mod)
        recs = mod.BATCH
        known = {r["exercise_id"]
                 for r in json.load(open(MANUAL, encoding="utf-8"))}
        etiqueta = f"lote {a.lote} ({len(recs)} fichas)"

    errs, warns = check(recs, enums, conds, texts, known)

    print(f"== {etiqueta} ==")
    if warns:
        print(f"\n{len(warns)} advertencia(s):")
        for w in warns:
            print("  ?", w)
    if errs:
        print(f"\n{len(errs)} ERROR(es):")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print("\nSIN ERRORES")


if __name__ == "__main__":
    main()
