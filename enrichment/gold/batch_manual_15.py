#!/usr/bin/env python3
"""Lote 15 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1647", "dumbbell alternate preacher curl", "seated_machine", grip="firm",
      lat="alternating", stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypermobility",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia"],
      why="Version alternada de 0372. El brazo que espera queda extendido bajo "
           "carga: gripdur high. La familia del curl predicador llega a siete."),

    E("0367", "dumbbell over bench one arm wrist curl", "seated", grip="firm",
      lat="unilateral", stress=js(wr="moderate", el="moderate"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="UNDECIMA entrada de la familia de muneca. Todas colapsan en dos "
           "substitute_group segun la palma mire arriba o abajo."),

    E("1621", "dumbbell one arm hammer press on exercise ball", "seated",
      bal="moderate", grip="firm", oh=True, lat="unilateral",
      stress=js(sh="moderate", el="moderate", lumbar="moderate", cerv="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "rotator_cuff", "limited_balance", "vertigo"],
      caut=["shoulder_impingement", "lumbar_pain", "hypertension",
            "elbow_injury", "multiple_sclerosis", "dysautonomia", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement"],
      why="Press vertical con agarre neutro sobre pelota: el agarre baja el "
           "hombro a moderate (pinzamiento como precaucion), pero la "
           "inestabilidad agrega equilibrio como contraindicacion dura. "
           "Los ejes se compensan en direcciones opuestas."),

    E("0301", "dumbbell decline bench press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "hypertension", "dysautonomia",
            "vertigo", "migraine", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "no_overhead"],
      why="Version con mancuernas de 0033. Mas rom que con barra pero mismo "
           "bloque ocular y cardiovascular por head_below_heart."),

    E("0306", "dumbbell decline triceps extension", "bench_supine", grip="firm",
      oh=True, stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="low",
      metab="low", gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip", "no_overhead",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "hypertension",
            "dysautonomia", "vertigo", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement"],
      why="Extension de triceps detras de la cabeza en declinado: suma "
           "overhead_position a head_below_heart. Diez contraindicaciones "
           "duras para un ejercicio de aislamiento."),

    E("0428", "dumbbell standing preacher curl", "standing", standing=True,
      grip="firm", stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="moderate", change="none", metab="low", laxity="moderate",
      gripdur="high", temp="low",
      contra=["cannot_stand", "limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypermobility", "dysautonomia",
            "limited_balance"],
      safe=["knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "shoulder_impingement"],
      why="CORRECCION A E1: lo marco bench_incline por la mencion del banco, "
           "pero el texto dice 'stand upright' - el banco solo apoya los "
           "brazos. Es standing. Unico curl predicador de pie del catalogo: "
           "pierde todo el safe_for de movilidad que tienen sus siete hermanos "
           "sentados."),

    E("1743", "dumbbell twisting bench press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="low", valsalva="low", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "hypermobility",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Press con rotacion de muneca durante el recorrido: laxity high por "
           "el componente rotacional bajo carga. Hipermovilidad pasa a "
           "contraindicacion, a diferencia del press recto (0289)."),

    E("0342", "dumbbell lying one arm press v. 2", "bench_supine", grip="firm",
      lat="unilateral", stress=js(sh="high", el="moderate", wr="low", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "hypermobility", "si_joint_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="DUPLICADO de 0343. Decimoquinto par 'v. 2' del dataset."),

    E("0872", "reverse crunch", "supine", floor=True,
      flex="moderate", stress=js(lumbar="moderate", hip="moderate", cerv="none"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "sciatica", "postpartum", "pelvic_floor_dysfunction"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "dysautonomia", "elderly_65plus"],
      why="Brazos a los costados: cervical NONE. Es el segundo abdominal de "
           "flexion apto con lesion cervical, junto a alternate heel touchers. "
           "La flexion viene de la pelvis, no del cuello."),

    E("1278", "dumbbell incline fly on exercise ball", "bench_incline",
      bal="moderate", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate", wr="low"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="low", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate",
      temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_balance",
              "limited_grip", "vertigo", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "lumbar_pain", "multiple_sclerosis",
            "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Apertura inclinada sobre pelota. Con 0319 (banco firme) forma el "
           "par que aisla el efecto de la superficie: la pelota agrega "
           "equilibrio como contraindicacion dura."),

    E("3314", "straddle maltese", "hanging", grip="hanging_bodyweight",
      ext="high", stress=js(sh="high", el="high", wr="high", lumbar="high"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="high",
      metab="high", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "lumbar_disc", "osteoporosis", "hypermobility", "hypertension",
              "cardiac", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["chronic_fatigue", "obesity", "si_joint_pain"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement"],
      why="Calistenia de elite en anillas. 16 contraindicaciones duras, empata "
           "con back lever. La apertura de piernas en straddle agrega carga de "
           "cadera: contraindicado con protesis."),

    E("0807", "suspended reverse crunch", "hanging", grip="hanging_bodyweight",
      flex="moderate", stress=js(sh="high", el="moderate", wr="high",
      lumbar="moderate", hip="moderate"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", pelvic="moderate", gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "hypertension", "postpartum",
            "pelvic_floor_dysfunction", "obesity", "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement", "hip_replacement", "cervical_injury"],
      why="Rodillas al pecho colgado: al flexionar la rodilla baja el brazo de "
           "palanca, por eso lumbar queda moderate y lumbar_disc es precaucion "
           "- frente a hanging leg raise (0472) con piernas rectas, donde es "
           "contraindicacion. Es su regresion correcta."),

    E("1160", "burpee", "standing", floor=True, standing=True, bal="moderate",
      impact="high", flex="moderate",
      stress=js(knee="high", hip="high", sh="high", wr="high", lumbar="moderate",
                ank="high"),
      pat="cardio_interval", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", temp="high", gripdur="low",
      contra=["cannot_stand", "cannot_get_on_floor", "limited_balance",
              "knee_injury", "knee_replacement", "hip_replacement",
              "ankle_injury", "wrist_injury", "carpal_tunnel", "osteoporosis",
              "pelvic_floor_dysfunction", "lumbar_disc",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cardiac", "hypertension", "obesity", "chronic_fatigue",
            "fibromyalgia", "dysautonomia", "asthma", "elderly_65plus",
            "shoulder_impingement", "postpartum"],
      why="El ejercicio con mas ejes en rojo simultaneos del catalogo: "
           "impacto alto, metabolico alto, ortostatico alto, temperatura alta, "
           "transicion al suelo repetida. Catorce contraindicaciones duras y "
           "diez precauciones. Es el caso que mejor justifica la existencia de "
           "los ejes fisiologicos: con solo start_position pareceria un "
           "ejercicio de pie mas."),

    E("1328", "dumbbell lying rear delt row", "bench_prone", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", metab="low", gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "elbow_injury", "carpal_tunnel",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="DUPLICADO funcional de 0327 y 0248. Remo con pecho apoyado: "
           "cero carga lumbar. La familia de remo prono ya tiene cuatro "
           "entradas, todas aptas para hernia discal."),

    E("1408", "band hip lift", "supine", floor=True, grip="none",
      ext="moderate", stress=js(hip="moderate", lumbar="low", knee="low"),
      pat="hinge", diff=1, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", pelvic="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hip_replacement", "lumbar_disc",
            "postpartum"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "dysautonomia", "chronic_fatigue", "elderly_65plus", "osteoporosis"],
      why="Puente de gluteo con banda sobre las rodillas: agrega abduccion "
           "resistida al patron de 0484. Mismo perfil de accesibilidad "
           "(15 safe_for, lumbar low) con mas activacion de gluteo medio. "
           "Progresion natural de 0484."),

    E("1766", "self assisted inverse leg curl (machine)", "bench_prone",
      grip="light", ext="low",
      stress=js(knee="moderate", hip="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", metab="low",
      pelvic="none", gripdur="low", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "knee_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_injury", "knee_pain", "hip_pain", "osteoarthritis",
            "hypermobility"],
      safe=["cannot_stand", "limited_balance", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "dysautonomia", "cervical_injury", "chronic_fatigue"],
      why="Curl femoral en maquina boca abajo. OJO: mismo nombre que 0697 pero "
           "texto distinto - aquel describe rodillas al pecho (core), este si "
           "es curl femoral. Segundo error de nomenclatura del dataset "
           "detectado en la misma familia. Quinto hinge/aislamiento de "
           "isquiotibiales accesible sin pararse."),

    E("1769", "bodyweight side lying biceps curl", "side_lying", floor=True,
      grip="none", lat="unilateral",
      stress=js(el="low", sh="low"), pat="isolation", diff=1, rom="moderate",
      ortho="none", change="high", metab="none", laxity="low", temp="none",
      contra=["cannot_get_on_floor", "cannot_lie_on_side"],
      caut=["elbow_injury", "tendinitis_elbow"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "limited_grip", "wrist_injury",
            "carpal_tunnel", "dysautonomia", "chronic_fatigue", "fibromyalgia",
            "elderly_65plus", "hypertension", "cervical_injury"],
      why="18 safe_for, segundo mas accesible del catalogo tras pelvic tilt. "
           "Curl sin resistencia externa: util solo como movilizacion o "
           "activacion muy temprana, pero cubre el patron para quien no puede "
           "sostener nada con las manos."),

    E("1772", "elbow lift - reverse push-up", "prone", floor=True, grip="none",
      ext="moderate", stress=js(sh="moderate", wr="moderate", lumbar="moderate",
      el="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", pelvic="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_prone", "wrist_injury",
              "carpal_tunnel", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "shoulder_impingement", "si_joint_pain",
            "osteoporosis", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "limited_grip",
            "dysautonomia"],
      why="Extension torácica boca abajo con retraccion escapular. El nombre "
           "dice push-up pero es trabajo de espalda alta. Similar a sphinx "
           "(1362) con componente activo de escapula."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 15: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
