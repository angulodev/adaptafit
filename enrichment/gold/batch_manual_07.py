#!/usr/bin/env python3
"""Lote 7 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0643", "overhead triceps stretch", "seated", oh=True, lat="unilateral",
      stress=js(sh="moderate", el="low"), pat="isolation", diff=1, rom="high",
      ortho="low", iso="moderate", metab="none", laxity="moderate", temp="none",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["hypermobility", "elbow_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia", "chronic_fatigue",
            "hip_replacement"],
      why="DUPLICADO de 0817 (triceps stretch): texto casi identico. "
           "Sexto par duplicado detectado."),

    E("0813", "triceps dip (between benches)", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", metab="moderate", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc"],
      why="NOVENO duplicado del fondo en banco. Nueve entradas para un solo "
           "movimiento: el 1% del catalogo completo."),

    E("1379", "dumbbell seated calf raise", "seated", grip="firm",
      axial="low", stress=js(ank="moderate", knee="low", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="none", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["ankle_injury", "plantar_fasciitis"],
      caut=["knee_pain", "osteoarthritis", "hypermobility", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "lumbar_disc", "hip_replacement",
            "shoulder_impingement", "no_overhead", "dysautonomia",
            "cervical_injury", "elderly_65plus"],
      why="Version con mancuerna del 0088/1371. La mancuerna es mas facil de "
           "sostener que la barra, por eso limited_grip baja de contraindicacion "
           "a precaucion. Progresion natural para pantorrilla sentado."),

    E("3546", "dumbbell seated alternate shoulder", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low", lumbar="low"),
      lat="alternating", pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="low", metab="low", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility",
            "si_joint_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="NOVENO press de hombro sentado. Al sostener una mancuerna arriba "
           "mientras la otra baja, grip_duration sube a high: el brazo que "
           "espera esta en isometrico."),

    E("1284", "dumbbell lying pullover on exercise ball", "bench_supine",
      bal="moderate", grip="firm", oh=True, ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "limited_balance", "cannot_lie_supine", "vertigo",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "lumbar_pain", "hypertension", "multiple_sclerosis",
            "dysautonomia"],
      safe=["cannot_stand", "knee_pain", "ankle_injury"],
      why="DUPLICADO funcional de 1295 (pullover on exercise ball). "
           "Mismo substitute_group."),

    E("1286", "dumbbell one arm chest fly on exercise ball", "bench_supine",
      bal="high", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate", cerv="moderate"),
      lat="unilateral", pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_balance",
              "limited_grip", "vertigo", "cannot_lie_supine", "cervical_injury",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "lumbar_pain", "multiple_sclerosis", "dysautonomia",
            "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury"],
      why="Variante de 1288 donde la cabeza y el cuello quedan FUERA de la "
           "pelota, sin apoyo. Por eso cervical sube a moderate y aparece "
           "cervical_injury como contraindicacion, a diferencia del 1288."),

    E("3234", "hyght dumbbell fly", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="low", valsalva="low", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "elbow_injury"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="DUPLICADO de 0308 (dumbbell fly): texto identico salvo el nombre. "
           "Septimo par duplicado."),

    E("0324", "dumbbell incline palm-in press", "bench_incline", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "elbow_injury", "hypermobility",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="DUPLICADO de 0321 (incline hammer press): 'palm-in' y 'hammer' son "
           "el mismo agarre neutro. Octavo par."),

    E("3006", "resistance band seated hip abduction", "seated", grip="none",
      stress=js(hip="moderate", knee="low"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="low", laxity="low", temp="none",
      caut=["hip_pain", "si_joint_pain", "osteoarthritis", "hip_replacement"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "dysautonomia", "chronic_fatigue",
            "elderly_65plus", "hypertension", "cervical_injury"],
      why="CERO contraindicaciones duras y el safe_for mas amplio del catalogo "
           "hasta ahora (17). Abduccion en silla: sin agarre, sin carga axial, "
           "sin demanda cardiaca. La protesis de cadera es solo precaucion aca "
           "porque la abduccion es el movimiento SEGURO tras artroplastia "
           "(a diferencia de la aduccion y rotacion interna)."),

    E("0059", "barbell lying preacher curl", "bench_prone", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "rheumatoid_arthritis", "shoulder_impingement"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="CORRECCION A E1: dice 'sit on a preacher bench' pero 'chest against "
           "the pad' es prono. Es bench_prone. Septimo caso del mismo error de E1."),

    E("0082", "barbell reverse wrist curl", "seated", grip="firm",
      stress=js(wr="high", el="moderate"), pat="isolation", diff=2, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="Version invertida del 0126. El codo sube a moderate: la extension "
           "de muneca cargada es justo el mecanismo de la epicondilitis lateral, "
           "aunque tambien se use para rehabilitarla."),

    E("0870", "butt-ups", "supine", floor=True,
      flex="high", stress=js(lumbar="high", cerv="moderate", hip="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="moderate", metab="low",
      pelvic="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "cervical_injury"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Elevacion de cadera con las piernas al pecho: despega la pelvis del "
           "suelo, lo que carga la lumbar en flexion maxima. pelvic_floor_load "
           "high por la presion intraabdominal del movimiento."),

    E("0323", "dumbbell incline one arm lateral raise", "bench_incline",
      grip="firm", flex="low",
      stress=js(sh="high", el="low", lumbar="low"),
      lat="unilateral", pat="isolation", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["hypermobility", "cervical_injury", "lumbar_disc"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "dysautonomia"],
      why="Elevacion lateral con el brazo apoyado en el muslo: elimina el "
           "impulso del tronco. Aisla el deltoides medio mejor que la version "
           "libre (0396), pero el estres de hombro no baja."),

    E("0491", "incline leg hip raise (leg straight)", "bench_incline",
      flex="moderate", stress=js(hip="high", lumbar="high", cerv="low"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="moderate", iso="moderate",
      metab="low", pelvic="high", gripdur="low", temp="low",
      contra=["cannot_transfer_to_bench", "lumbar_disc", "sciatica",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "postpartum", "osteoporosis"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip"],
      why="Elevacion de piernas rectas en banco inclinado: version mas dura "
           "del 0620 porque el angulo aumenta el brazo de palanca del psoas "
           "sobre la lumbar."),

    E("0500", "isometric wipers", "supine", floor=True,
      rot="high", stress=js(lumbar="high", sh="moderate", hip="moderate"),
      lat="alternating", pat="core_rotation", diff=4, rom="high",
      ortho="none", change="high", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="high", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "sciatica", "si_joint_pain", "hernia_abdominal", "osteoporosis",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "shoulder_impingement", "postpartum",
            "hypermobility"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "no_overhead",
            "limited_grip"],
      why="Limpiaparabrisas: rotacion lumbar bajo carga con las piernas rectas "
           "como palanca larga. De los mas agresivos del catalogo para el disco. "
           "difficulty 4 y ocho contraindicaciones duras."),

    E("1623", "dumbbell palms in incline bench press", "bench_incline", grip="firm",
      stress=js(sh="moderate", el="high", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Casi identico a 0324/0321, pero el dataset lo clasifica como triceps: "
           "el codo pasa a high y el hombro baja a moderate. Diferencia de "
           "enfasis, no de movimiento. Mismo substitute_group."),

    E("2371", "weighted russian twist v. 2", "seated", floor=True, bal="moderate",
      grip="firm", flex="moderate", rot="high",
      stress=js(lumbar="high", hip="moderate", sh="moderate", cerv="low"),
      lat="alternating", pat="core_rotation", diff=3, rom="moderate",
      ortho="low", change="high", valsalva="moderate", iso="moderate",
      metab="moderate", pelvic="high", gripdur="moderate", temp="moderate",
      contra=["cannot_get_on_floor", "lumbar_disc", "sciatica", "si_joint_pain",
              "hernia_abdominal", "osteoporosis", "limited_grip",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "postpartum", "hypertension", "shoulder_impingement"],
      why="DUPLICADO de 0846. Noveno par 'v. 2' con texto equivalente."),

    E("2400", "inverse leg curl (on pull-up cable machine)", "bench_prone",
      grip="light", ext="moderate",
      stress=js(knee="moderate", lumbar="moderate", hip="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", metab="low",
      pelvic="low", gripdur="low", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "knee_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_injury", "knee_pain", "lumbar_disc", "hip_pain",
            "hypermobility", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "shoulder_impingement",
            "no_overhead", "wrist_injury", "carpal_tunnel", "dysautonomia",
            "cervical_injury"],
      why="CORRECCION A E1: lo marco overhead_position y grip hanging_bodyweight "
           "por el nombre 'pull-up cable machine', pero el ejercicio es un curl "
           "femoral boca abajo - las manos solo sostienen el banco. "
           "DUPLICADO funcional de 0496."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 7: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
