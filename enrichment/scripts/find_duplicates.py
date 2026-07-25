#!/usr/bin/env python3
"""
Detecta ejercicios duplicados en el source comparando el texto de instrucciones.

El dataset trae variantes con nombre distinto e instrucciones identicas o casi
("dumbbell supported squat" vs "dumbbell squat"). Clasificarlos por separado es
trabajo repetido, y si llegan al indice la app muestra el mismo ejercicio dos
veces con nombres diferentes.

    python3 find_duplicates.py                 # umbral 0.90, solo equipo de casa
    python3 find_duplicates.py --threshold 0.95
    python3 find_duplicates.py --all-equipment
    python3 find_duplicates.py --json out.json

Salida: grupos de ejercicios equivalentes, marcando cual ya esta clasificado.
No modifica nada. La decision de colapsar es de E3.
"""
import argparse
import json
import os
import re
from difflib import SequenceMatcher

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "source", "exercises.json")
MANUAL = os.path.join(BASE, "output", "manual_classified.json")
GOLD = os.path.join(BASE, "gold", "gold_examples.json")

HOME = {"body weight", "dumbbell", "barbell", "band", "resistance band",
        "ez barbell", "olympic barbell", "weighted"}


def norm(text):
    """Normaliza para comparar: minusculas, sin puntuacion, espacios colapsados."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_done():
    done = set()
    for path, key in [(GOLD, "examples"), (MANUAL, None)]:
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        done |= {r["exercise_id"] for r in (data[key] if key else data)}
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=0.90)
    ap.add_argument("--all-equipment", action="store_true")
    ap.add_argument("--json", dest="json_out")
    args = ap.parse_args()

    src = json.load(open(SRC, encoding="utf-8"))
    if not args.all_equipment:
        src = [x for x in src if x["equipment"] in HOME]
    done = load_done()

    items = [(x["id"], x["name"], x["equipment"], x["body_part"],
              norm(x["instructions"]["en"])) for x in src]
    items = [i for i in items if i[4]]

    # Bloqueo por longitud: textos muy distintos no pueden parecerse lo
    # suficiente. Evita el O(n^2) completo sobre 895+ registros.
    items.sort(key=lambda i: len(i[4]))
    pairs = []
    for a in range(len(items)):
        la = len(items[a][4])
        for b in range(a + 1, len(items)):
            lb = len(items[b][4])
            if lb > la / args.threshold:
                break
            if SequenceMatcher(None, items[a][4], items[b][4]).ratio() >= args.threshold:
                pairs.append((items[a], items[b]))

    # Union-find para agrupar cadenas de equivalencia (A~B, B~C -> A,B,C)
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x, y in pairs:
        rx, ry = find(x[0]), find(y[0])
        if rx != ry:
            parent[rx] = ry

    groups = {}
    by_id = {i[0]: i for i in items}
    for eid in parent:
        groups.setdefault(find(eid), []).append(eid)
    groups = {k: sorted(v) for k, v in groups.items() if len(v) > 1}

    total_dupes = sum(len(v) - 1 for v in groups.values())
    pending_dupes = sum(
        len([e for e in v if e not in done]) - (0 if all(e in done for e in v) else 1)
        for v in groups.values())

    print(f"umbral        : {args.threshold}")
    print(f"universo      : {len(items)} ejercicios")
    print(f"grupos        : {len(groups)}")
    print(f"redundantes   : {total_dupes} (colapsables)")
    print(f"aun en cola   : ~{max(0, pending_dupes)} clasificaciones evitables\n")

    for g in sorted(groups.values(), key=lambda v: -len(v)):
        print(f"--- grupo de {len(g)} ---")
        for eid in g:
            _, name, equip, part, _ = by_id[eid]
            mark = "OK " if eid in done else "   "
            print(f"  {mark}[{eid}] {name}  | {equip} | {part}")
        print()

    if args.json_out:
        out = [[{"exercise_id": e, "name": by_id[e][1],
                 "equipment": by_id[e][2], "classified": e in done} for e in g]
               for g in groups.values()]
        json.dump(out, open(args.json_out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"escrito: {args.json_out}")


if __name__ == "__main__":
    main()
