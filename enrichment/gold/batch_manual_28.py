#!/usr/bin/env python3
"""Lote 28 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0092", "barbell seated overhead triceps extension", "seated", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", wr="moderate", cerv="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench",
              "cannot_sit_unsupported", "wrist_injury"],
      caut=["tendinitis_elbow", "cervical_injury", "neck_pain", "hypertension",
            "hypermobility", "osteoporosis", "dysautonomia", "lumbar_pain",
            "carpal_tunnel"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="Tercera version del mismo gesto (2188 mancuerna, 0453 barra EZ, "
           "0092 barra recta). La barra recta es la peor de las tres para la "
           "muneca: pronacion fija bajo carga con los brazos sobre la cabeza — "
           "wrist_injury sube a contraindicacion, algo que no ocurre en las "
           "otras dos."),

    E("0674", "reverse grip pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "cannot_stand", "one_arm_only"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "hypermobility", "osteoporosis", "obesity", "elderly_65plus",
            "rheumatoid_arthritis", "cervical_injury", "chronic_fatigue"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="Tercer chin-up del dataset (1327, 0627, 0674), todos con agarre "
           "supinado y el mismo perfil: hombro en cautions, codo a contra. El "
           "grupo de duplicados de dominadas ya tiene siete entradas para tres "
           "ejercicios reales — pronado, supinado y lastrado."),

    E("0969", "band alternating v-up", "supine", floor=True, oh=True,
      grip="light", flex="high", lat="alternating",
      stress=js(lumbar="high", hip="high", sh="moderate", cerv="low"),
      pat="core_flexion", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="moderate",
      temp="moderate",
      contra=["lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cannot_get_on_floor",
              "cannot_lie_supine", "no_overhead", "shoulder_impingement",
              "hip_replacement", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["rotator_cuff", "postpartum", "obesity", "elderly_65plus",
            "chronic_fatigue", "hypertension", "hip_pain", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="El V-up eleva tronco Y piernas rectas a la vez: los dos brazos de "
           "palanca completos sobre la lumbar al mismo tiempo. Con la banda "
           "sobre la cabeza suma no_overhead y hombro. Es el peor de las ocho "
           "entradas de core_flexion del proyecto."),

    E("3327", "full planche push-up", "plank", floor=True, bal="high",
      grip="none", stress=js(wr="high", sh="high", el="high", lumbar="high",
                             hip="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="none", change="moderate", valsalva="high", iso="high",
      metab="high", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "elbow_injury",
              "cannot_get_on_floor", "cannot_lie_prone", "hypermobility",
              "limited_balance", "lumbar_disc", "lumbar_pain",
              "hernia_abdominal", "recent_abdominal_surgery", "osteoporosis",
              "hip_replacement", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["si_joint_pain", "obesity", "elderly_65plus", "chronic_fatigue",
            "fibromyalgia", "hypertension", "cardiac",
            "pelvic_floor_dysfunction", "rheumatoid_arthritis"],
      safe=[],
      why="SEPTIMO safe_for vacio. A diferencia de 3300 y 3298, aca el texto SI "
           "describe una planche real: 'lift your feet off the ground, "
           "balancing on your hands'. Todo el cuerpo suspendido en horizontal "
           "sobre las munecas, con flexion simultanea. Es el ejercicio de "
           "empuje mas exigente del catalogo."),

    E("0383", "dumbbell reverse fly", "standing", standing=True, bal="moderate",
      grip="firm", flex="moderate",
      stress=js(lumbar="high", sh="moderate", el="low", wr="low",
                hip="moderate"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "shoulder_impingement",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "rotator_cuff", "shoulder_pain",
            "wrist_injury", "elbow_injury", "limited_balance", "hypertension",
            "obesity", "elderly_65plus", "osteoporosis", "dysautonomia",
            "hip_pain"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "carpal_tunnel"],
      why="CORRECCION A E1, TERCERA VEZ con el mismo error (0993, 0378, 0383): "
           "apertura posterior clasificada como horizontal_push. Es traccion. "
           "Duplicado funcional exacto de 0378 (lote 27) — mismo texto con "
           "otras palabras. El sesgo de E1 ya esta confirmado para toda la "
           "familia de rear fly."),

    E("3656", "short stride run", "standing", standing=True, bal="moderate",
      grip="none", impact="high", lat="alternating",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_steady", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="high",
      laxity="low", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement",
              "osteoporosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
              "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "lumbar_disc",
            "lumbar_pain", "si_joint_pain", "dysautonomia", "hypertension",
            "cardiac", "obesity", "elderly_65plus", "chronic_fatigue",
            "asthma", "varicose_veins", "multiple_sclerosis", "postpartum",
            "vertigo", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="DUPLICADO FUNCIONAL DE 0684 run (lote 26). La 'zancada corta' que "
           "promete el nombre no reduce el impacto en ningun campo medible de "
           "la taxonomia — sigue siendo carrera con fase de vuelo. Clasificado "
           "identico."),

    E("3231", "two toe touch (male)", "standing", standing=True, bal="low",
      grip="none", flex="high",
      stress=js(lumbar="high", hip="high", knee="moderate"),
      pat="mobility_stretch", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "cannot_stand",
              "wheelchair", "hernia_abdominal", "hip_replacement",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hypermobility",
            "knee_pain", "dysautonomia", "vertigo", "hypertension",
            "limited_balance", "elderly_65plus", "obesity", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "ankle_injury",
            "plantar_fasciitis"],
      why="TERCER ESTIRAMIENTO QUE ES UNA MANIOBRA DE PROVOCACION, despues de "
           "1405 (pinzamiento) y 1576 (Lasegue). Tocarse los pies con las "
           "piernas rectas es flexion lumbar completa sin apoyo Y estiramiento "
           "isquiotibial — la combinacion clasica de herniacion discal. "
           "osteoporosis a contra: la flexion espinal de pie es el gesto que "
           "produce fracturas vertebrales por compresion. La cabeza queda por "
           "debajo del corazon pero brevemente, asi que glaucoma va a cautions "
           "y no a contra."),

    E("0058", "barbell lying lifting (on hip)", "bench_supine", grip="firm",
      ext="moderate", axial="low",
      stress=js(hip="moderate", lumbar="moderate", knee="low", wr="low"),
      pat="hinge", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="low", pelvic="high", gripdur="moderate",
      temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "sciatica",
            "postpartum", "hypertension", "cardiac", "hip_replacement",
            "hip_pain", "obesity", "osteoporosis", "elderly_65plus",
            "knee_pain"],
      safe=["cannot_stand", "no_overhead", "shoulder_impingement",
            "rotator_cuff", "knee_injury", "ankle_injury", "plantar_fasciitis",
            "dysautonomia", "cannot_get_on_floor"],
      why="Empuje de cadera con barra apoyado en banco: es 1409 (lote 22) pero "
           "sobre banco en vez de suelo. Esa diferencia cambia dos filtros "
           "opuestos — cannot_get_on_floor entra en safe_for, pero "
           "cannot_transfer_to_bench pasa a contraindicacion. Sexta entrada de "
           "la familia del puente."),

    E("1673", "dumbbell preacher curl over exercise ball", "seated",
      bal="moderate", grip="firm", lat="unilateral",
      stress=js(el="high", lumbar="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["limited_balance", "cannot_sit_unsupported", "limited_grip",
              "elbow_injury", "tendinitis_elbow", "vertigo",
              "multiple_sclerosis", "hypermobility"],
      caut=["wrist_injury", "carpal_tunnel", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "elderly_65plus", "osteoporosis",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis"],
      why="Novena entrada de la familia pelota y la unica que combina los dos "
           "roles: sentado EN la pelota y con el codo apoyado SOBRE ella. "
           "Hereda el bloque de inestabilidad de los curls sentados y ademas "
           "la extension completa del codo del banco predicador — "
           "hypermobility y epicondilitis a contra."),

    E("1676", "dumbbell seated alternate hammer curl on exercise ball",
      "seated", bal="moderate", grip="firm", lat="alternating",
      stress=js(el="moderate", lumbar="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["limited_balance", "cannot_sit_unsupported", "limited_grip",
              "elbow_injury", "vertigo", "multiple_sclerosis"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "elderly_65plus", "osteoporosis",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "plantar_fasciitis"],
      why="Decima de la familia pelota y duplicado exacto de 1650 (lote 27): "
           "curl alternado sentado en pelota. La unica diferencia es el agarre "
           "martillo, que no mueve ninguna restriccion."),

    E("1679", "dumbbell seated one arm bicep curl on exercise ball with leg "
      "raised", "seated", bal="moderate", grip="firm", lat="unilateral",
      stress=js(el="moderate", lumbar="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["limited_balance", "cannot_sit_unsupported", "limited_grip",
              "elbow_injury", "vertigo", "multiple_sclerosis"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "elderly_65plus", "osteoporosis",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis"],
      why="EL NOMBRE DICE 'with leg raised' PERO EL TEXTO NO LO MENCIONA: dice "
           "'feet flat on the ground' y la otra mano en la cadera. Clasificado "
           "sin elevacion de pierna, o sea identico a 1668. Contrasta con 1652, "
           "donde el texto SI describe la pierna elevada y por eso sube a "
           "bal high con elderly_65plus a contra. Confianza 0.65 — si el nombre "
           "fuera el correcto, el perfil deberia ser el de 1652."),

    E("1730", "dumbbell seated bent over alternate kickback", "seated",
      grip="firm", flex="moderate", lat="alternating",
      stress=js(el="moderate", lumbar="high", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="moderate", headdown=True, valsalva="moderate",
      iso="moderate", metab="low", laxity="low", pelvic="low", gripdur="high",
      temp="low",
      contra=["lumbar_disc", "sciatica", "limited_grip", "elbow_injury",
              "cannot_transfer_to_bench", "cannot_sit_unsupported",
              "glaucoma", "retinal_detachment_risk",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "tendinitis_elbow", "dysautonomia", "vertigo", "migraine",
            "hypertension", "obesity", "hernia_abdominal"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis", "wrist_injury", "carpal_tunnel"],
      why="Sentado con el torso PARALELO AL SUELO: head_below_heart true, "
           "criterio ya fijado en el lote 12 para los kickbacks. La familia "
           "ocular a contra pese a ser un ejercicio de brazo trivial. La "
           "columna sin apoyo en voladizo desde sentado da lumbar high — peor "
           "que de pie, porque no hay cadera que reparta la carga."),

    E("1732", "dumbbell forward lunge triceps extension", "standing",
      standing=True, bal="high", sl=True, oh=True, grip="firm", impact="low",
      lat="alternating",
      stress=js(knee="high", sh="high", el="high", hip="moderate",
                lumbar="moderate", ank="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "elbow_injury", "no_overhead",
              "shoulder_impingement", "rotator_cuff",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity", "osteoporosis",
            "tendinitis_elbow", "cervical_injury"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "wrist_injury",
            "carpal_tunnel"],
      why="Zancada MAS extension sobre la cabeza: acumula el filtro de rodilla "
           "del lunge y el de hombro del overhead, dos bloques de Capa A que "
           "normalmente no coinciden. Solo 7 en safe_for. Tercer compuesto de "
           "la serie (1688 con rotacion, 1658 con curl, 1732 con extension) y "
           "el mas restrictivo de los tres."),

    E("1737", "dumbbell seated bent over triceps extension", "seated",
      grip="firm", flex="moderate",
      stress=js(el="moderate", lumbar="high", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="moderate", headdown=True, valsalva="moderate",
      iso="moderate", metab="low", laxity="low", pelvic="low", gripdur="high",
      temp="low",
      contra=["lumbar_disc", "sciatica", "limited_grip", "elbow_injury",
              "cannot_transfer_to_bench", "cannot_sit_unsupported",
              "glaucoma", "retinal_detachment_risk",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "tendinitis_elbow", "dysautonomia", "vertigo", "migraine",
            "hypertension", "obesity", "hernia_abdominal"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis", "wrist_injury", "carpal_tunnel"],
      why="Version bilateral de 1730, con el mismo perfil. El texto se "
           "contradice —'extend your arms straight back' pero 'elbows close to "
           "your head'— y manda la primera, que es el gesto del kickback. "
           "Mismo head_below_heart por el torso paralelo al suelo."),

    E("1738", "dumbbell seated reverse grip one arm overhead tricep extension",
      "seated", oh=True, grip="firm", lat="unilateral",
      stress=js(sh="high", el="high", wr="moderate", cerv="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "hypermobility", "osteoporosis", "dysautonomia",
            "lumbar_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "one_arm_only",
            "plantar_fasciitis"],
      why="Version unilateral y supinada de 2188. El agarre invertido con una "
           "sola mancuerna es mas comodo para la muneca que la barra recta de "
           "0092: wr queda en moderate. one_arm_only en safe_for, a diferencia "
           "de 0362, porque aca no se usa la otra mano para apoyarse."),

    E("2466", "bridge - mountain climber (cross body)", "plank", floor=True,
      bal="moderate", grip="none", rot="moderate", lat="alternating",
      stress=js(wr="high", sh="moderate", hip="high", lumbar="moderate"),
      pat="core_rotation", diff=3, rom="high",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="high", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement", "hip_replacement",
              "hip_pain", "si_joint_pain", "lumbar_disc",
              "recent_abdominal_surgery", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["rotator_cuff", "elbow_injury", "lumbar_pain", "sciatica",
            "obesity", "elderly_65plus", "chronic_fatigue", "hernia_abdominal",
            "knee_pain", "fibromyalgia"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "ankle_injury", "plantar_fasciitis", "dysautonomia"],
      why="El nombre dice 'bridge' pero el texto describe una plancha alta con "
           "rodilla cruzada al codo contrario — es un mountain climber, no un "
           "puente. La rodilla cruzando la linea media es flexion de cadera con "
           "aduccion y rotacion interna: la triada exacta que luxa una "
           "protesis. hip_replacement a contra."),

    E("3286", "weighted muscle up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, axial="low", ext="moderate",
      stress=js(sh="high", el="high", wr="high", lumbar="moderate",
                cerv="moderate"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "cannot_stand", "one_arm_only", "hypermobility", "osteoporosis",
              "elderly_65plus", "cervical_injury", "lumbar_disc",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "obesity", "chronic_fatigue",
            "rheumatoid_arthritis", "glaucoma", "retinal_detachment_risk",
            "neck_pain", "lumbar_pain"],
      safe=[],
      why="OCTAVO safe_for vacio. Version lastrada de 0558 kipping muscle up "
           "(lote 17). La transicion de traccion a fondo pasa por el punto mas "
           "debil del hombro, y aca con peso adicional: change high, valsalva "
           "high, laxity high. El unico ejercicio del catalogo que combina "
           "vertical_pull y vertical_push en el mismo gesto."),

    E("3548", "dumbbell single arm overhead carry", "standing", standing=True,
      bal="high", oh=True, grip="firm", axial="moderate", lat="unilateral",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate",
                cerv="moderate"),
      pat="carry", diff=4, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "hypermobility", "cervical_injury", "vertigo",
              "osteoporosis", "multiple_sclerosis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "neck_pain", "hypertension",
            "cardiac", "dysautonomia", "obesity", "elderly_65plus",
            "chronic_fatigue", "hernia_abdominal", "varicose_veins"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="SEGUNDO patron 'carry' del proyecto, despues de 2133 farmers walk. "
           "Contraste util: el farmers walk lleva el peso ABAJO y sale con 8 "
           "contraindicaciones; este lo lleva sobre la cabeza, caminando y a "
           "un solo lado, y salta a 15. bal high y laxity high — sostener carga "
           "overhead en movimiento es la posicion mas inestable del hombro."),
]

CONFIDENCE_OVERRIDES = {
    "1679": 0.65,  # el nombre dice 'leg raised', el texto dice pies en el suelo
    "1737": 0.70,  # texto contradictorio sobre la posicion del codo
}

for _e in BATCH:
    if _e["exercise_id"] in CONFIDENCE_OVERRIDES:
        _e["confidence"] = CONFIDENCE_OVERRIDES[_e["exercise_id"]]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 28: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
