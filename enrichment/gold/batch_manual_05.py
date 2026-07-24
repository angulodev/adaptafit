#!/usr/bin/env python3
"""Lote 5 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0394", "dumbbell seated kickback", "seated", grip="firm",
      flex="moderate", stress=js(el="moderate", sh="moderate", lumbar="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", change="low", headdown=True, metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "glaucoma", "retinal_detachment_risk"],
      caut=["lumbar_disc", "shoulder_impingement", "hypertension",
            "dysautonomia", "tendinitis_elbow"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead"],
      why="Se inclina hacia adelante desde la cadera: el torso queda horizontal "
           "y la cabeza baja del corazon. Cuarto caso de head_below_heart en un "
           "ejercicio que nadie llamaria inversion."),

    E("0129", "bench dip (knees bent)", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia"],
      why="SEPTIMO duplicado del fondo en banco. El dataset tiene siete entradas "
           "para el mismo movimiento. Confirma que E4 es imprescindible."),

    E("0290", "dumbbell bench seated press", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="Otro press de hombro sentado. Con 0405, 0438, 2397, 2137, 0287 y 3122 "
           "ya son siete variantes del mismo patron vertical_push sentado."),

    E("1548", "chair leg extended stretch", "seated",
      stress=js(hip="low", knee="low", lumbar="low"),
      lat="unilateral", pat="isolation", diff=1, rom="moderate",
      ortho="low", change="none", headdown=True, metab="none",
      laxity="moderate", temp="none",
      contra=["glaucoma", "retinal_detachment_risk"],
      caut=["lumbar_disc", "sciatica", "hypermobility", "knee_pain",
            "hypertension", "dysautonomia"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "chronic_fatigue", "elderly_65plus"],
      why="Estiramiento en silla sin bajar al suelo: raro y valioso. "
           "La inclinacion hacia adelante es leve pero suficiente para marcar "
           "head_below_heart. El texto dice quadriceps pero estira isquiotibiales."),

    E("0399", "dumbbell seated one arm rotate", "seated", grip="firm",
      rot="none", stress=js(sh="moderate", el="moderate", wr="moderate"),
      lat="unilateral", pat="isolation", diff=1, rom="moderate",
      ortho="low", metab="none", gripdur="moderate", laxity="moderate", temp="none",
      contra=["limited_grip", "rotator_cuff"],
      caut=["shoulder_impingement", "wrist_injury", "tendinitis_elbow",
            "hypermobility", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia", "chronic_fatigue"],
      why="Rotacion externa de hombro con codo pegado al cuerpo: es el ejercicio "
           "de rehabilitacion clasico del manguito rotador. Contraindicado con "
           "rotura confirmada, pero es de los pocos que trabajan esa zona sin "
           "posicion de pinzamiento."),

    E("1283", "dumbbell incline press on exercise ball", "bench_incline",
      bal="moderate", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="moderate",
      temp="low",
      contra=["limited_balance", "limited_grip", "vertigo",
              "cannot_lie_supine", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypermobility", "lumbar_pain",
            "multiple_sclerosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Press inclinado sobre pelota. La inestabilidad obliga a estabilizar "
           "con el core, de ahi el iso moderate. Equilibrio como contraindicacion "
           "dura por el riesgo de caida con mancuernas."),

    E("1288", "dumbbell one arm fly on exercise ball", "bench_supine",
      bal="high", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate", wr="low"),
      lat="unilateral", pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_balance",
              "limited_grip", "vertigo", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "lumbar_pain", "multiple_sclerosis",
            "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury"],
      why="Apertura a un brazo sobre pelota: la carga asimetrica sobre superficie "
           "inestable exige equilibrio alto y rotacion anti-lateral del core. "
           "difficulty 4 - de los mas exigentes en estabilidad del catalogo."),

    E("2317", "dumbbell seated bent arm lateral raise", "seated", grip="firm",
      stress=js(sh="moderate", el="low", cerv="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      caut=["shoulder_impingement", "rotator_cuff", "limited_grip",
            "cervical_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Codo flexionado a 90 grados: acorta el brazo de palanca y baja el "
           "estres de hombro de high (0396, brazo extendido) a moderate. "
           "Es la REGRESION correcta de la elevacion lateral - por eso el "
           "pinzamiento pasa de contraindicacion a precaucion."),

    E("0350", "dumbbell lying supine curl", "bench_supine", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="none", change="low", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_lie_supine",
              "cannot_transfer_to_bench", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["tendinitis_elbow", "shoulder_impingement", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="DUPLICADO de 1662 (lying wide curl): texto identico. "
           "Mismo substitute_group."),

    E("0846", "weighted russian twist", "seated", floor=True, bal="moderate",
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
      why="Version lastrada del 0687. El peso alarga el brazo de palanca sobre "
           "el disco: osteoporosis pasa a contraindicacion por riesgo de "
           "fractura vertebral por torsion bajo carga."),

    E("3785", "incline push-up (on box)", "plank", bal="low",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=1, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="low", pelvic="low", gripdur="low", temp="low",
      contra=["wrist_injury", "carpal_tunnel"],
      caut=["shoulder_impingement", "elbow_injury", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "limited_balance", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="DUPLICADO de 0493 (incline push-up). Ambos son la regresion clave "
           "del push-up para quien no puede bajar al suelo."),

    E("0088", "barbell seated calf raise", "seated", grip="firm",
      axial="low", stress=js(ank="moderate", knee="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", change="none", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["ankle_injury", "plantar_fasciitis", "limited_grip"],
      caut=["knee_pain", "osteoarthritis", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "lumbar_disc", "hip_replacement",
            "shoulder_impingement", "no_overhead", "dysautonomia",
            "cervical_injury"],
      why="Elevacion de talon sentado: el unico ejercicio de pantorrilla del "
           "catalogo apto para quien no puede pararse. La barra sobre los muslos "
           "no genera carga axial sobre la columna, a diferencia de la version de pie."),

    E("0090", "barbell seated good morning", "seated", grip="firm",
      axial="high", flex="high",
      stress=js(lumbar="high", hip="moderate", cerv="moderate", sh="moderate"),
      pat="hinge", diff=4, rom="moderate",
      ortho="low", change="low", headdown=True, valsalva="high",
      metab="moderate", pelvic="high", gripdur="moderate", temp="moderate",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "hernia_abdominal", "cervical_injury", "limited_grip",
              "glaucoma", "retinal_detachment_risk", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "lumbar_pain", "postpartum",
            "dysautonomia", "shoulder_impingement", "elderly_65plus"],
      why="El ejercicio mas riesgoso del lote pese a hacerse sentado. Barra "
           "sobre la espalda + flexion de tronco = carga axial alta con la "
           "columna en voladizo. valsalva high y cabeza bajo el corazon. "
           "Estar sentado NO lo vuelve seguro: buen caso contra el atajo mental "
           "'sentado = accesible'."),

    E("0304", "dumbbell decline shrug v. 2", "bench_prone", grip="firm",
      stress=js(cerv="moderate", sh="moderate", el="low"),
      pat="isolation", diff=2, rom="low",
      ortho="none", change="moderate", headdown=True, metab="low",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "cervical_injury", "glaucoma", "retinal_detachment_risk",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "dysautonomia", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "limited_balance", "hip_replacement"],
      why="DUPLICADO de 0305: texto casi identico. Tercer par 'v. 2' del dataset "
           "sin diferencia real."),

    E("0326", "dumbbell incline rear lateral raise", "bench_prone", grip="firm",
      stress=js(sh="moderate", el="low", cerv="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip"],
      caut=["shoulder_impingement", "rotator_cuff", "hypermobility",
            "cervical_injury", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="CORRECCION A E1: 'chest against the backrest' es prono, no inclinado. "
           "Sexto caso del mismo error. Deltoides posterior con pecho apoyado: "
           "excelente para postura sin cargar la lumbar."),

    E("0496", "inverse leg curl (bench support)", "bench_prone", grip="light",
      ext="moderate", stress=js(knee="moderate", lumbar="moderate", hip="moderate"),
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
      why="Curl femoral boca abajo: unico ejercicio de isquiotibiales sin "
           "carga axial ni necesidad de pararse. Muy util para quien no puede "
           "hacer bisagra de cadera de pie."),

    E("0620", "lying leg raise flat bench", "bench_supine",
      flex="moderate", stress=js(hip="high", lumbar="high", cerv="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="moderate",
      metab="low", pelvic="high", temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "postpartum", "osteoporosis"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "dysautonomia"],
      why="Elevacion de piernas rectas: el psoas tracciona la lumbar en "
           "anteversion. lumbar high y pelvic_floor_load high pese a que "
           "parece un abdominal suave. Contraindicado en disco."),

    E("0990", "band one arm twisting seated row", "seated", grip="light",
      rot="moderate", stress=js(sh="moderate", el="moderate", lumbar="low"),
      lat="unilateral", pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="none", metab="low", gripdur="moderate", temp="low",
      contra=["si_joint_pain"],
      caut=["shoulder_impingement", "lumbar_disc", "elbow_injury",
            "hypermobility", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "no_overhead", "limited_grip", "dysautonomia", "elderly_65plus",
            "chronic_fatigue"],
      why="Remo sentado con banda y rotacion leve: safe_for muy amplio y cubre "
           "el patron de tiron horizontal, que es el mas dificil de resolver "
           "para perfiles restringidos. Junto con 0996 y 3124, nucleo de rutina "
           "accesible."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 5: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
