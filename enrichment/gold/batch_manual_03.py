#!/usr/bin/env python3
"""Lote 3 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0436", "dumbbell tate press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "dysautonomia"],
      why="CORRECCION A E1: dice 'sit on a flat bench' pero el press se ejecuta "
           "acostado. Es bench_supine. Triceps con codo muy cargado por el "
           "angulo de rotacion."),

    E("1424", "seated glute stretch", "seated", floor=True,
      stress=js(hip="moderate", knee="moderate", lumbar="low"),
      lat="unilateral", pat="isolation", diff=1, rom="high",
      ortho="low", change="high", metab="none", laxity="moderate", temp="none",
      contra=["cannot_get_on_floor", "hip_replacement"],
      caut=["hip_pain", "knee_pain", "si_joint_pain", "sciatica",
            "hypermobility", "pregnancy_3rd"],
      safe=["cannot_stand", "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "dysautonomia", "chronic_fatigue", "hypertension",
            "elderly_65plus"],
      why="Figura-4 sentado. Contraindicado con protesis de cadera: la rotacion "
           "externa con aduccion es justo la posicion de riesgo de luxacion."),

    E("2137", "dumbbell arnold press", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low", wr="moderate"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility",
            "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="La rotacion durante el press suma estres rotacional al hombro que el "
           "press recto no tiene. Con respaldo: apto para POTS pese al brazo arriba."),

    E("0570", "leg pull in flat bench", "seated", grip="light",
      flex="moderate", stress=js(hip="high", lumbar="moderate", sh="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", pelvic="moderate", gripdur="low", temp="low",
      contra=["lumbar_disc", "sciatica", "hernia_abdominal",
              "recent_abdominal_surgery", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "postpartum", "pelvic_floor_dysfunction", "lumbar_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_pain", "ankle_injury", "shoulder_impingement", "no_overhead",
            "dysautonomia"],
      why="Core en banco sin bajar al suelo: mismo hueco que cubre 0555. "
           "Rodillas al pecho carga menos el psoas que la pierna recta."),

    E("1295", "dumbbell pullover on exercise ball", "bench_supine", bal="moderate",
      grip="firm", oh=True, ext="moderate",
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
      why="Pullover sobre pelota: rango maximo de hombro sobre superficie "
           "inestable. laxity high y equilibrio como contraindicacion dura."),

    E("0349", "dumbbell lying supination", "bench_supine", grip="firm",
      stress=js(wr="moderate", el="moderate", sh="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="low", metab="none", gripdur="moderate", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["tendinitis_elbow", "rheumatoid_arthritis"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia", "chronic_fatigue"],
      why="Par del 0347 (pronacion), version supina. Demanda sistemica minima: "
           "de los pocos aptos en fatiga cronica."),

    E("0359", "dumbbell one arm reverse fly (with support)", "seated", grip="firm",
      flex="moderate", stress=js(sh="high", lumbar="low", el="low"),
      lat="unilateral", pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="low", headdown=True, metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "glaucoma", "retinal_detachment_risk"],
      caut=["lumbar_disc", "hypertension", "dysautonomia", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead"],
      why="Se inclina hacia adelante apoyando la mano libre: el torso queda "
           "horizontal y la cabeza baja del corazon. Otro caso de head_below_heart "
           "que no parece una inversion."),

    E("0395", "dumbbell seated lateral raise v. 2", "seated", grip="firm",
      stress=js(sh="high", el="low", cerv="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["cervical_injury", "hypermobility", "tendinitis_elbow"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="DUPLICADO de 0396: texto identico. El dataset trae 'v. 2' sin ninguna "
           "diferencia en las instrucciones. Mismo substitute_group."),

    E("0455", "finger curls", "seated", grip="firm",
      stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["carpal_tunnel", "wrist_injury", "limited_grip",
              "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="grip_duration high con grip_required firm: es exactamente el perfil "
           "que el tunel carpiano no tolera. Buen ejemplo de por que separamos "
           "fuerza de agarre y duracion de agarre."),

    E("0490", "incline close-grip push-up", "plank", bal="low",
      stress=js(sh="moderate", el="high", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="low", pelvic="low", gripdur="low", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "elbow_injury", "tendinitis_elbow"],
      caut=["shoulder_impingement", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "limited_balance", "dysautonomia"],
      why="Manos elevadas: no exige bajar al suelo pese a ser una plancha. "
           "Agarre cerrado desplaza la carga del hombro al codo."),

    E("0495", "incline twisting sit-up", "bench_incline", flex="high", rot="high",
      stress=js(lumbar="high", cerv="high", hip="moderate"),
      lat="alternating", pat="core_rotation", diff=3, rom="moderate",
      ortho="low", change="moderate", valsalva="moderate", metab="moderate",
      pelvic="moderate", temp="moderate",
      contra=["cannot_transfer_to_bench", "lumbar_disc", "cervical_injury",
              "sciatica", "si_joint_pain", "hernia_abdominal",
              "recent_abdominal_surgery", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["osteoporosis", "postpartum", "pelvic_floor_dysfunction",
            "hypertension", "lumbar_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance"],
      why="Flexion + rotacion lumbar bajo carga: la combinacion mas desaconsejada "
           "para disco. Peor que el russian twist porque suma el recorrido completo."),

    E("0994", "band reverse wrist curl", "seated", grip="light",
      stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="moderate", temp="none",
      contra=["wrist_injury", "carpal_tunnel"],
      caut=["tendinitis_elbow", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "limited_grip", "dysautonomia",
            "chronic_fatigue", "elderly_65plus"],
      why="Version con banda del 0126 (barra). El agarre ligero lo vuelve "
           "safe_for limited_grip, cosa que la version con barra no es. "
           "Progresion natural: banda -> barra."),

    E("1294", "dumbbell pullover hip extension on exercise ball", "bench_supine",
      bal="moderate", grip="firm", oh=True, ext="moderate",
      stress=js(sh="high", lumbar="moderate", hip="moderate", el="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="moderate",
      temp="moderate",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "limited_balance", "cannot_lie_supine", "vertigo",
              "lumbar_disc", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "hypertension", "multiple_sclerosis", "dysautonomia",
            "postpartum"],
      safe=["cannot_stand", "knee_pain", "ankle_injury"],
      why="Pullover manteniendo puente de cadera: isometrica de gluteo sostenida "
           "sobre pelota mientras el hombro va a rango maximo. Difficulty 4 real."),

    E("3541", "dumbbell incline y-raise", "bench_prone", grip="firm", oh=True,
      stress=js(sh="high", el="low", cerv="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["hypermobility", "cervical_injury",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="CORRECCION A E1: dice bench_incline pero 'lean forward and let your "
           "arms hang' con pecho apoyado es prone. Trabajo de trapecio inferior "
           "con pecho apoyado: excelente para postura sin cargar la lumbar."),

    E("3542", "dumbbell incline t-raise", "bench_prone", grip="firm",
      stress=js(sh="high", el="low", cerv="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["hypermobility", "cervical_injury",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Par del Y-raise a 90 grados. La T no pasa de la cabeza, por eso es "
           "safe_for no_overhead y el Y no."),

    E("3547", "dumbbell seated biceps curl to shoulder press", "seated",
      grip="firm", oh=True, axial="low",
      stress=js(sh="high", el="moderate", cerv="low", wr="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="moderate", gripdur="moderate",
      temp="moderate",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility",
            "chronic_fatigue"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="Movimiento compuesto (curl + press): metabolic_intensity sube a "
           "moderate aunque cada mitad por separado sea low. Relevante para "
           "fatiga cronica."),

    E("0070", "barbell preacher curl", "seated_machine", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow",
              "wrist_injury", "carpal_tunnel"],
      caut=["hypermobility", "rheumatoid_arthritis", "shoulder_impingement"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Version con barra del 0372. La barra recta fuerza supinacion fija: "
           "la muneca pasa a moderate y el agarre a contraindicacion. "
           "Progresion: mancuerna -> barra EZ -> barra recta."),

    E("0094", "barbell seated twist", "seated", grip="firm",
      rot="high", stress=js(lumbar="high", sh="moderate", cerv="low"),
      lat="alternating", pat="core_rotation", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="low",
      metab="low", pelvic="moderate", gripdur="moderate", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "limited_grip",
              "osteoporosis", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "shoulder_impingement", "postpartum",
            "pelvic_floor_dysfunction", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "no_overhead"],
      why="Rotacion lumbar con barra sobre los hombros: la palanca larga "
           "multiplica el torque sobre el disco. osteoporosis pasa a "
           "contraindicacion por riesgo de fractura vertebral por torsion."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 3: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
