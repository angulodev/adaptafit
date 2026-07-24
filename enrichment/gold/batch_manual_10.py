#!/usr/bin/env python3
"""Lote 10 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1381", "dumbbell seated one leg calf raise - palm up", "seated",
      grip="firm", axial="low", lat="unilateral",
      stress=js(ank="moderate", knee="low", wr="moderate"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="none", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["ankle_injury", "plantar_fasciitis"],
      caut=["knee_pain", "osteoarthritis", "hypermobility", "limited_grip",
            "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "limited_balance", "lumbar_disc", "hip_replacement",
            "shoulder_impingement", "no_overhead", "dysautonomia",
            "cervical_injury", "elderly_65plus"],
      why="Variante de 0400 con la palma hacia arriba: la muneca en supinacion "
           "sostenida sube de low a moderate. Diferencia real, aunque minima."),

    E("1672", "dumbbell one arm zottman preacher curl", "seated_machine",
      grip="firm", lat="unilateral",
      stress=js(el="high", wr="high", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow",
              "wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["hypermobility", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia"],
      why="El curl zottman rota la muneca de supinacion a pronacion bajo carga: "
           "muneca a high. Es la version del curl predicador MENOS apta para "
           "tunel carpiano, frente a 0372 que es de las mas seguras."),

    E("0340", "dumbbell lying hammer press", "bench_supine", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia", "elderly_65plus"],
      why="Press plano con agarre neutro: mismo principio que 0404 (parallel "
           "grip). El agarre neutro baja el hombro a moderate y vuelve el "
           "pinzamiento precaucion. Segunda pieza util para hombro comprometido."),

    E("0081", "barbell reverse preacher curl", "bench_prone", grip="firm",
      stress=js(el="high", wr="high", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "rheumatoid_arthritis", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia"],
      why="CORRECCION A E1: 'chest against the pad' es prono, no sentado. "
           "Noveno caso del mismo error. El agarre pronado carga muñeca y "
           "epicondilo: es el curl mas exigente para el codo del catalogo."),

    E("0443", "elbow-to-knee", "supine", floor=True,
      flex="high", rot="high",
      stress=js(lumbar="high", cerv="high", hip="moderate"),
      lat="alternating", pat="core_rotation", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="moderate",
      pelvic="moderate", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "sciatica", "si_joint_pain",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum",
            "pelvic_floor_dysfunction"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="DUPLICADO funcional de 0003 (air bike). Flexion + rotacion con manos "
           "detras de la cabeza: la combinacion mas desaconsejada para disco, "
           "y la mas repetida del catalogo."),

    E("1754", "weighted three bench dips", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="low", change="low", valsalva="moderate", metab="moderate",
      gripdur="moderate", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypertension", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc"],
      why="UNDECIMO duplicado del fondo en banco, con pies elevados y lastre. "
           "Es la progresion mas dura de la familia: difficulty 4."),

    E("0871", "tuck crunch", "supine", floor=True,
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "hip_pain"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Crunch con rodillas al pecho simultaneo. Manos detras de la cabeza: "
           "cervical high, como en todo el grupo."),

    E("0079", "barbell revers wrist curl v. 2", "seated", grip="firm",
      stress=js(wr="high", el="moderate"), pat="isolation", diff=2, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="DUPLICADO de 0082. Duodecimo par 'v. 2' del dataset."),

    E("0840", "weighted overhead crunch (on stability ball)", "seated",
      bal="moderate", grip="firm", oh=True, flex="high",
      stress=js(lumbar="high", sh="high", cerv="moderate"),
      pat="core_flexion", diff=4, rom="high",
      ortho="low", change="low", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="high", temp="moderate",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "lumbar_disc", "limited_balance", "limited_grip", "vertigo",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "hypertension", "osteoporosis",
            "postpartum", "multiple_sclerosis", "dysautonomia"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury"],
      why="Crunch con peso sobre la cabeza en pelota inestable: el brazo de "
           "palanca es maximo. Combina restriccion de hombro y de columna a la "
           "vez - once contraindicaciones duras."),

    E("0849", "weighted seated twist (on stability ball)", "seated",
      bal="moderate", grip="firm", rot="high",
      stress=js(lumbar="high", sh="low", hip="low"),
      lat="alternating", pat="core_rotation", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", pelvic="moderate", gripdur="moderate", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "limited_balance", "vertigo", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hernia_abdominal", "postpartum",
            "multiple_sclerosis", "elderly_65plus"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead"],
      why="Rotacion cargada sobre pelota. Hermano de 0850 (flexion lateral): "
           "misma base, distinto plano de movimiento."),

    E("3418", "l-pull-up", "hanging", grip="hanging_bodyweight", oh=True,
      flex="moderate",
      stress=js(sh="high", el="high", wr="high", lumbar="moderate", hip="high"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "lumbar_disc", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "obesity", "chronic_fatigue",
            "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement"],
      why="Dominada manteniendo L-sit: suma isometrica de core maxima al tiron "
           "vertical. difficulty 5. Aun asi es safe_for rodilla y tobillo - "
           "cero demanda de tren inferior."),

    E("3562", "barbell glute bridge two legs on bench", "seated", grip="firm",
      axial="moderate", ext="moderate",
      stress=js(hip="high", lumbar="moderate", knee="low", wr="low"),
      pat="hinge", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="moderate", iso="moderate",
      metab="moderate", pelvic="high", gripdur="moderate", temp="moderate",
      contra=["lumbar_disc", "limited_grip", "pelvic_floor_dysfunction",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hip_replacement", "postpartum",
            "hypertension", "osteoporosis"],
      safe=["cannot_stand", "limited_balance", "knee_pain", "ankle_injury",
            "shoulder_impingement", "no_overhead", "dysautonomia"],
      why="Version cargada del 0130/3523. Tercer hinge disponible para "
           "movilidad reducida, y el unico con carga progresiva real. "
           "pelvic_floor_load high por la barra sobre la cadera."),

    E("0020", "balance board", "standing", standing=True, bal="high", sl=True,
      stress=js(ank="moderate", knee="moderate", hip="low"),
      lat="unilateral", pat="isolation", diff=3, rom="low",
      ortho="moderate", change="moderate", valsalva="none", iso="high",
      metab="low", laxity="moderate", temp="low",
      contra=["cannot_stand", "limited_balance", "vertigo", "ankle_injury",
              "visual_impairment"],
      caut=["knee_injury", "knee_pain", "multiple_sclerosis", "elderly_65plus",
            "dysautonomia", "hypermobility", "osteoarthritis"],
      safe=["shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "lumbar_disc"],
      why="Primer ejercicio del catalogo donde visual_impairment es "
           "contraindicacion dura: el equilibrio unipodal sobre superficie "
           "inestable depende de referencia visual. Paradoja util: es un "
           "ejercicio DE equilibrio, asi que quien mas lo necesitaria es quien "
           "no puede hacerlo sin supervision."),

    E("0047", "barbell incline bench press", "bench_incline", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="moderate", metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["elbow_injury", "wrist_injury", "hypertension", "hypermobility",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Press inclinado con barra: menos rom que con mancuernas pero mas "
           "carga posible. La barra fija las manos, lo que reduce la libertad "
           "de la muneca."),

    E("0048", "barbell incline reverse-grip press", "bench_incline", grip="firm",
      stress=js(sh="moderate", el="high", wr="high"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="moderate", metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Agarre invertido: descarga el hombro (a moderate) pero carga muneca "
           "y codo a high. Intercambio claro - util para hombro comprometido "
           "con munecas sanas, inutil al reves."),

    E("0050", "barbell incline shoulder raise", "bench_incline", grip="firm",
      oh=True, stress=js(sh="high", cerv="low", el="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", valsalva="low", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_transfer_to_bench"],
      caut=["cervical_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="Elevacion escapular con barra por encima de la cabeza. Trabaja "
           "serrato: util para discinesia escapular, pero solo si el hombro "
           "tolera la posicion overhead."),

    E("0052", "barbell jm bench press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Hibrido entre press cerrado y rompecraneos: el codo soporta la "
           "transicion bajo carga. difficulty 4 por la tecnica, no por la "
           "demanda metabolica."),

    E("0055", "barbell lying close-grip press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="high"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "limited_grip", "cannot_lie_supine",
              "cannot_transfer_to_bench", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Version con barra de 0296/1731. El agarre cerrado en barra recta "
           "fuerza desviacion cubital: muneca a high, a diferencia de la "
           "version con mancuernas donde queda en moderate."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 10: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
