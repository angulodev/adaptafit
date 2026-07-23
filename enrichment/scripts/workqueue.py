#!/usr/bin/env python3
"""
Cola de trabajo priorizada para la clasificacion en chat.

Ordena los 895 por VALOR, no por id. Si el trabajo se corta en cualquier punto,
lo hecho es lo mas util posible.

Criterio de prioridad (de mayor a menor peso):
  1. Accesibilidad     - sentado/reclinado/sin equipo puntua alto. Es el nucleo
                         del producto: lo que sirve a perfiles restringidos.
  2. Cobertura         - primer ejercicio de cada combinacion postura x patron
                         x zona. Evita 30 curls de biceps antes del primer remo.
  3. Fundamentalidad   - nombres cortos = ejercicios base, no variantes raras.
  4. Equipo disponible - peso corporal y mancuerna antes que barra.

Uso:
    python3 workqueue.py --next 20     # siguiente lote a clasificar
    python3 workqueue.py --status      # progreso
"""

import argparse
import json
import os
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "source", "exercises.json")
E1 = os.path.join(BASE, "output", "e1_output.json")
GOLD = os.path.join(BASE, "gold", "gold_examples.json")
MANUAL = os.path.join(BASE, "output", "manual_classified.json")

HOME = {"body weight", "dumbbell", "barbell", "band", "resistance band",
        "ez barbell", "olympic barbell", "weighted"}

ACCESSIBLE_POS = {"seated": 3, "seated_machine": 3, "bench_supine": 2,
                  "bench_incline": 2, "bench_prone": 2, "supine": 1,
                  "prone": 1, "side_lying": 1}
EQUIP_SCORE = {"body weight": 3, "dumbbell": 3, "band": 2, "resistance band": 2,
               "weighted": 1, "ez barbell": 1, "barbell": 1, "olympic barbell": 0}


def load_done():
    done = set()
    for path, key in [(GOLD, "examples"), (MANUAL, None)]:
        if not os.path.exists(path):
            continue
        data = json.load(open(path, encoding="utf-8"))
        recs = data[key] if key else data
        done |= {r["exercise_id"] for r in recs}
    return done


def build_queue():
    src = {x["id"]: x for x in json.load(open(SRC, encoding="utf-8"))}
    e1 = {r["exercise_id"]: r for r in json.load(open(E1, encoding="utf-8"))}
    done = load_done()

    pool = [i for i, x in src.items() if x["equipment"] in HOME and i not in done]

    # Cobertura: marcar el primero de cada celda (postura x patron x zona)
    seen_cells = set()
    scored = []
    for eid in sorted(pool, key=lambda i: len(src[i]["name"])):
        x, a = src[eid], e1.get(eid, {})
        cell = (a.get("start_position"), a.get("movement_pattern"), x["body_part"])
        novel = cell not in seen_cells
        seen_cells.add(cell)

        score = 0
        score += ACCESSIBLE_POS.get(a.get("start_position"), 0) * 3
        score += 10 if novel else 0
        score += EQUIP_SCORE.get(x["equipment"], 0) * 2
        score += max(0, 6 - len(x["name"].split()))        # nombre corto = base
        if a.get("requires_standing"):
            score -= 2
        if a.get("requires_floor_transition"):
            score -= 1
        scored.append((-score, eid))

    scored.sort()
    return [eid for _, eid in scored], src, e1, done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", type=int, default=0)
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    queue, src, e1, done = build_queue()
    total_home = sum(1 for x in src.values() if x["equipment"] in HOME)

    if args.status or not args.next:
        pct = len(done) / total_home * 100
        print(f"clasificados : {len(done)} de {total_home} ({pct:.1f}%)")
        print(f"en cola      : {len(queue)}")
        return

    batch = queue[:args.next]
    print(f"# Lote de {len(batch)} — quedan {len(queue)-len(batch)} en cola\n")
    for eid in batch:
        x, a = src[eid], e1.get(eid, {})
        hints = {k: v for k, v in a.items()
                 if k in ("start_position", "laterality", "movement_pattern",
                          "grip_required", "overhead_position")
                 and v is not None}
        print(f"### [{eid}] {x['name']} | {x['equipment']} | {x['body_part']} | {x['target']}")
        print(f"E1: {hints}")
        print(x["instructions"]["en"][:300].replace("\n", " "))
        print()


if __name__ == "__main__":
    main()
