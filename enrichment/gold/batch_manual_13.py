#!/usr/bin/env python3
"""Lote 13 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("2294", "dumbbell zottman preacher curl", "seated_machine", grip="firm",
      stress=js(el="high", wr="high", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow",
              "wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["hypermobility", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia"],
      why="DUPLICADO bilateral de 1672. La rotacion de muneca bajo carga es "
           "el sello del zottman: muneca high."),

    E("0401", "dumbbell seated palms up wrist curl", "seated", grip="firm",
      stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="Novena entrada de la familia flexion/extension de muneca. Todas "
           "colapsan en dos substitute_group: palma arriba y palma abajo."),

    E("1618", "dumbbell incline hammer press on exercise ball", "bench_supine",
      bal="moderate", grip="firm",
      stress=js(sh="moderate", el="high", lumbar="moderate", cerv="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", gripdur="moderate", temp="low",
      contra=["limited_balance", "limited_grip", "vertigo", "cannot_lie_supine",
              "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility",
            "multiple_sclerosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead"],
      why="CORRECCION A E1: dice 'sit on an exercise ball' pero luego rueda "
           "hasta quedar con cabeza y espalda alta apoyadas. Es bench_supine, "
           "no seated. La cabeza queda sin soporte estructural: cervical moderate."),

    E("0315", "dumbbell incline biceps curl", "bench_incline", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="TERCERA entrada identica a 0318 y 0317. El curl inclinado tiene tres "
           "registros con el mismo texto."),

    E("0351", "dumbbell lying triceps extension", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="DUPLICADO bilateral de 1735 y version con mancuernas de 0057/0061. "
           "El rompecraneos ya tiene cinco entradas."),

    E("0433", "dumbbell straight arm pullover", "bench_supine", grip="firm",
      oh=True, ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "elbow_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance", "dysautonomia"],
      why="El nombre explicita 'straight arm': confirma el par con 1316 "
           "(bent arm). laxity high vs moderate. Es el ejemplo mas limpio de "
           "la regla de flexion de codo como regresion."),

    E("0494", "incline reverse grip push-up", "plank", bal="low",
      stress=js(sh="moderate", el="moderate", wr="high", lumbar="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="low", pelvic="low", gripdur="low", temp="low",
      contra=["wrist_injury", "carpal_tunnel"],
      caut=["shoulder_impingement", "elbow_injury", "tendinitis_elbow",
            "rheumatoid_arthritis", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "limited_balance", "no_overhead",
            "dysautonomia"],
      why="Push-up inclinado con dedos hacia atras: la muneca queda en maxima "
           "extension con rotacion. wrist high pese a ser una regresion en "
           "todo lo demas. Quinto caso del eje de agarre."),

    E("1285", "dumbbell one arm bench fly", "bench_supine", grip="firm",
      lat="unilateral", stress=js(sh="high", el="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "elbow_injury", "si_joint_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Apertura unilateral en banco firme. Con 1279 (inclinado) y 1288 "
           "(pelota) forman el trio que aisla el efecto de cada variable: "
           "angulo, superficie y lateralidad."),

    E("0508", "janda sit-up", "supine", floor=True,
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Miembro del grupo de 10 abdominales con texto identico. "
           "Ironia del dataset: el janda sit-up real se define por inhibir el "
           "psoas con co-contraccion de isquiotibiales, y el texto no lo menciona."),

    E("1617", "dumbbell decline one arm hammer press", "bench_supine",
      grip="firm", lat="unilateral",
      stress=js(sh="moderate", el="high", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="low",
      metab="low", gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "dysautonomia", "vertigo",
            "migraine", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "no_overhead"],
      why="Agarre martillo en declinado unilateral: hombro moderate por el "
           "agarre neutro, pero head_below_heart activa el bloque ocular y "
           "cardiovascular. Los dos ejes operan independientes."),

    E("0489", "hyperextension", "bench_prone", grip="none",
      ext="high", flex="moderate",
      stress=js(lumbar="high", hip="moderate", cerv="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      iso="moderate", metab="low", pelvic="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "osteoporosis",
              "glaucoma", "retinal_detachment_risk",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "sciatica", "hypertension",
            "dysautonomia", "hypermobility", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel"],
      why="E1 no resolvio la postura. Extension lumbar activa contra gravedad "
           "con el torso en voladizo y la cabeza abajo. Como sphinx y lower "
           "back curl, en hernia discal la extension suele aliviar (precaucion), "
           "pero en osteoporosis la extension forzada es contraindicacion."),

    E("0635", "oblique crunches floor", "supine", floor=True,
      flex="high", rot="high",
      stress=js(lumbar="high", cerv="high", hip="low"),
      lat="alternating", pat="core_rotation", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "si_joint_pain", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "sciatica", "osteoporosis", "postpartum"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Flexion mas rotacion en suelo. El texto ofrece la alternativa de "
           "cruzar los brazos sobre el pecho, que bajaria cervical a moderate - "
           "pero se clasifica el peor caso por sesgo conservador."),

    E("0022", "barbell pullover to press", "bench_supine", grip="firm", oh=True,
      ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="moderate",
      laxity="high", gripdur="high", temp="moderate",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "elbow_injury", "hypermobility", "hypertension",
            "chronic_fatigue"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance"],
      why="Pullover encadenado con press: movimiento compuesto, por eso "
           "metabolic sube a moderate y difficulty a 4. Sexta entrada de la "
           "familia pullover."),

    E("3289", "impossible dips", "hanging", grip="firm", bal="moderate",
      stress=js(sh="high", el="high", wr="high"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", gripdur="high", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "hypermobility"],
      caut=["hypertension", "obesity", "cardiac"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement"],
      why="Tercera variante avanzada del fondo en paralelas, junto a ring dips "
           "y korean dips. La familia del fondo llega a catorce entradas."),

    E("3296", "front lever", "hanging", grip="hanging_bodyweight",
      ext="moderate",
      stress=js(sh="high", el="high", wr="high", lumbar="high", hip="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="high",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "lumbar_disc", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "hypermobility", "chronic_fatigue"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement", "hip_replacement"],
      why="Isometrica maxima de anti-extension colgado. valsalva high e "
           "iso high a la vez: es el perfil que peor tolera una condicion "
           "cardiaca. difficulty 5."),

    E("3297", "back lever", "hanging", grip="hanging_bodyweight",
      ext="high",
      stress=js(sh="high", el="high", wr="high", lumbar="high"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="moderate", change="high", headdown=True, valsalva="high",
      iso="high", metab="high", laxity="high", pelvic="moderate",
      gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "lumbar_disc", "osteoporosis", "hypermobility", "glaucoma",
              "retinal_detachment_risk", "hypertension", "cardiac",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["dysautonomia", "vertigo", "migraine", "chronic_fatigue"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement", "hip_replacement"],
      why="Segundo ejercicio mas contraindicado del catalogo tras handstand: "
           "16 contraindicaciones duras. Combina inversion, hiperextension de "
           "hombro en rango final e isometrica maxima. laxity high."),

    E("0139", "biceps narrow pull-ups", "hanging", grip="hanging_bodyweight",
      oh=True, stress=js(sh="high", el="high", wr="high", lumbar="low"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", valsalva="moderate", metab="moderate", laxity="moderate",
      gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "tendinitis_elbow"],
      caut=["hypertension", "obesity", "elderly_65plus", "hypermobility"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement", "limited_balance"],
      why="Quinta dominada del catalogo. Agarre cerrado supinado: carga codo "
           "y muneca mas que la version ancha. La familia vertical_pull "
           "colgada queda cerrada."),

    E("0283", "diamond push-up", "plank", floor=True, bal="low",
      stress=js(sh="moderate", el="high", wr="high", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="moderate", pelvic="low", gripdur="low", temp="moderate",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "tendinitis_elbow"],
      caut=["shoulder_impingement", "rheumatoid_arthritis",
            "pregnancy_2nd", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "limited_balance", "no_overhead"],
      why="Manos juntas: desplaza carga del hombro (moderate) al codo y la "
           "muneca (high). Mismo intercambio que el agarre cerrado en press. "
           "Su regresion es incline close-grip push-up (0490)."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 13: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
