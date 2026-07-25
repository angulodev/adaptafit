#!/usr/bin/env python3
"""Lote 27 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0452", "ez barbell reverse grip preacher curl", "seated", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_transfer_to_bench", "hypermobility"],
      caut=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis",
            "shoulder_impingement", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "lumbar_pain", "sciatica", "dysautonomia", "plantar_fasciitis",
            "cannot_sit_unsupported"],
      why="El nombre dice 'reverse grip' pero el texto dice 'underhand grip', "
           "que es supinado normal. Tercera vez que la familia predicador "
           "arrastra ese error de nombre (0452, 1414, y 0403 en el lote 26). "
           "Mantiene el rasgo del banco predicador: hypermobility a contra por "
           "la extension completa del codo sin posibilidad de encoger el "
           "hombro."),

    E("0613", "lying (side) quads stretch", "side_lying", floor=True,
      grip="light", lat="unilateral", sl=True,
      stress=js(knee="high", hip="moderate", lumbar="low"),
      pat="mobility_stretch", diff=1, rom="high",
      ortho="none", change="moderate", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="low", temp="low",
      contra=["knee_injury", "knee_replacement", "cannot_lie_on_side",
              "cannot_get_on_floor"],
      caut=["knee_pain", "osteoarthritis", "hip_pain", "si_joint_pain",
            "lumbar_pain", "hypermobility", "rheumatoid_arthritis",
            "limited_grip", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "osteoporosis",
            "hip_replacement", "lumbar_disc", "sciatica"],
      why="CORRECCION A E1: dijo supine, el texto dice 'lie on your side'. "
           "Mismo error que 0408 en el lote 17 — E1 colapsa toda posicion "
           "horizontal a supino. Estiramiento de cuadriceps en decubito "
           "lateral: la rodilla va a flexion maxima con traccion manual, por "
           "eso knee high pese a ser diff 1. Es la version accesible de 1512 "
           "all fours squad stretch — sin cargar la rotula contra el suelo, "
           "asi que knee_replacement sigue contra pero desaparece la muneca."),

    E("0627", "mixed grip chin-up", "hanging", oh=True,
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
      why="El nombre dice 'mixed grip' (una mano pronada y otra supinada) pero "
           "el texto describe las dos supinadas. Manda el texto: es un "
           "chin-up. Duplicado funcional de 1327 (lote 26), con el mismo "
           "perfil amable de hombro y duro de codo. Confianza 0.70."),

    E("0725", "single arm push-up", "plank", floor=True, bal="moderate",
      grip="none", lat="alternating",
      stress=js(wr="high", sh="high", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "hypermobility", "cannot_get_on_floor",
              "cannot_lie_prone", "one_arm_only", "elbow_injury",
              "recent_abdominal_surgery", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["shoulder_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "obesity", "elderly_65plus", "chronic_fatigue", "hernia_abdominal",
            "osteoporosis"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis"],
      why="DUPLICADO FUNCIONAL DE 3294 archer push up (lote 23): pese al "
           "nombre, el texto describe extender un brazo al costado mientras el "
           "otro sostiene, alternando. Decimo grupo de duplicados. Igual que "
           "3294, one_arm_only a contra — un ejercicio que carga un brazo "
           "necesita los dos."),

    E("0071", "barbell press sit-up", "supine", floor=True, grip="firm",
      flex="high", axial="low",
      stress=js(lumbar="high", cerv="low", hip="moderate", wr="moderate"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="high", iso="low",
      metab="moderate", laxity="low", pelvic="high", gripdur="high",
      temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "cannot_get_on_floor", "cannot_lie_supine", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "postpartum", "obesity",
            "elderly_65plus", "hypertension", "cardiac", "wrist_injury",
            "cervical_injury"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "dysautonomia"],
      why="Sit-up con barra sobre el pecho: septima entrada de la familia de "
           "flexion de tronco y la unica con valsalva high — sostener una barra "
           "cargada mientras se flexiona el tronco casi obliga a la apnea. "
           "Curiosidad: al ocupar las manos con la barra, el cuello NO se "
           "tracciona, asi que cerv baja a low y cervical_injury va a cautions."),

    E("0378", "dumbbell rear fly", "standing", standing=True, bal="moderate",
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
      why="CORRECCION A E1: dijo horizontal_push, es traccion — los brazos se "
           "abren juntando escapulas. SEGUNDA vez que E1 confunde una apertura "
           "posterior con empuje, despues de 0993 en el lote 26. Ya es patron. "
           "Ademas 'hinge forward at the hips' con mancuernas colgando deja el "
           "torso en voladizo: lumbar high y lumbar_disc a contra, igual que "
           "1330 y 1773."),

    E("1364", "standing pelvic tilt", "standing", standing=True, bal="low",
      grip="none", flex="low",
      stress=js(lumbar="low", hip="low", knee="low"),
      pat="mobility_stretch", diff=1, rom="low",
      ortho="moderate", change="none", valsalva="none", iso="moderate",
      metab="low", laxity="low", pelvic="moderate", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair"],
      caut=["lumbar_disc", "si_joint_pain", "sciatica", "dysautonomia",
            "limited_balance", "elderly_65plus", "hip_pain",
            "pelvic_floor_dysfunction"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "lumbar_pain", "osteoporosis",
            "hernia_abdominal", "pregnancy_1st", "pregnancy_2nd",
            "pregnancy_3rd"],
      why="LA VERSION DE PIE DE 1422. 25 en safe_for y dos contraindicaciones, "
           "segundo del ranking absoluto detras de 1403 neck side stretch. "
           "Como 1422, tiene lumbar_pain en safe_for por ser rehabilitacion "
           "lumbar estandar — pero sin exigir bajar al suelo, asi que llega a "
           "un perfil que 1422 no alcanza. Apto en los tres trimestres."),

    E("3224", "jack jump (male)", "standing", standing=True, bal="moderate",
      oh=True, grip="none", impact="high", lat="bilateral",
      stress=js(knee="high", ank="high", sh="moderate", hip="moderate",
                lumbar="low"),
      pat="cardio_interval", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement",
              "osteoporosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
              "no_overhead", "shoulder_impingement", "vertigo",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "rotator_cuff",
            "lumbar_pain", "dysautonomia", "hypertension", "cardiac",
            "obesity", "elderly_65plus", "chronic_fatigue", "asthma",
            "varicose_veins", "multiple_sclerosis", "postpartum",
            "pregnancy_1st"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "elbow_injury"],
      why="Saltos de tijera: impacto bilateral repetido MAS brazos sobre la "
           "cabeza. Es el unico cardio del proyecto que suma no_overhead y "
           "shoulder_impingement a las contraindicaciones — 0684, 3361 y 1688 "
           "dejaban el tren superior libre. pelvic high por el impacto."),

    E("0974", "band close-grip pulldown", "standing", standing=True, bal="low",
      oh=True, grip="light",
      stress=js(sh="moderate", el="moderate", wr="low", lumbar="low"),
      pat="vertical_pull", diff=1, rom="high",
      ortho="moderate", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff"],
      caut=["shoulder_pain", "elbow_injury", "tendinitis_elbow",
            "dysautonomia", "hypertension", "elderly_65plus", "limited_grip",
            "cervical_injury", "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "wrist_injury",
            "carpal_tunnel", "osteoporosis", "one_arm_only"],
      why="DUPLICADO FUNCIONAL DE 1013 (lote 26). Que el piso de accesibilidad "
           "de vertical_pull tenga DOS entradas es una buena noticia para la "
           "robustez —si una se filtra por equipamiento queda la otra— pero "
           "E4 debe elegir una sola al armar la rutina."),

    E("1414", "dumbbell one arm reverse preacher curl", "seated", grip="firm",
      lat="unilateral", stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_transfer_to_bench", "hypermobility"],
      caut=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis",
            "shoulder_impingement", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "lumbar_pain", "sciatica", "dysautonomia", "plantar_fasciitis",
            "cannot_sit_unsupported", "one_arm_only"],
      why="Version unilateral de 0452, con el mismo desajuste de nombre "
           "('reverse' pero el texto dice underhand). La familia predicador "
           "queda con cuatro entradas —1646, 1663, 0452, 1414— que difieren "
           "solo en lateralidad e implemento, sin cambiar ni una restriccion."),

    E("1421", "modified push up to lower arms", "plank", floor=True,
      grip="none", stress=js(el="high", wr="high", sh="moderate",
                             lumbar="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="high", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "elbow_injury",
              "tendinitis_elbow", "cannot_get_on_floor", "cannot_lie_prone",
              "shoulder_impingement", "recent_abdominal_surgery",
              "osteoarthritis", "rheumatoid_arthritis", "pregnancy_3rd"],
      caut=["rotator_cuff", "lumbar_pain", "lumbar_disc", "obesity",
            "elderly_65plus", "hernia_abdominal", "pelvic_floor_dysfunction",
            "postpartum", "osteoporosis", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "knee_injury", "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="OJO: parece la version facil de 1467 (lote 22) pero es lo "
           "contrario. Bajar de manos a antebrazos y volver a subir apoya el "
           "peso sobre los CODOS contra el suelo y exige empujar desde ahi: "
           "el high, wr high y position_change high. 1467 protege la muneca; "
           "este la castiga igual que una flexion normal Y ademas suma el "
           "codo. artritis y artrosis a contra por el impacto articular "
           "directo."),

    E("1430", "chest dip (on dip-pull-up cage)", "standing", standing=True,
      grip="firm", stress=js(sh="high", el="high", wr="moderate", cerv="low"),
      pat="vertical_push", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "wrist_injury", "elbow_injury",
              "tendinitis_elbow", "hypermobility", "cannot_stand",
              "one_arm_only", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["carpal_tunnel", "cervical_injury", "obesity", "elderly_65plus",
            "osteoporosis", "hypertension", "chronic_fatigue",
            "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "plantar_fasciitis"],
      why="CORRECCION A E1: marco overhead_position true, pero en los fondos "
           "los brazos estan ABAJO, sosteniendo el cuerpo. Por eso no_overhead "
           "esta en safe_for. Duplicado funcional de 2462 (lote 23). El error "
           "de E1 habria excluido el ejercicio para todo perfil sin rango "
           "overhead, que es justamente uno de los pocos empujes que si "
           "pueden hacer."),

    E("1650", "dumbbell alternating seated bicep curl on exercise ball",
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
      why="Quinta entrada de la familia pelota. Identica a 1659 y 0390 salvo "
           "la alternancia, que no cambia ninguna restriccion. El bloque de "
           "contraindicaciones por inestabilidad ya es un patron fijo: "
           "limited_balance, cannot_sit_unsupported, vertigo, "
           "multiple_sclerosis."),

    E("1652", "dumbbell bicep curl on exercise ball with leg raised", "seated",
      bal="high", grip="firm", sl=True, lat="unilateral",
      stress=js(el="moderate", lumbar="moderate", hip="moderate", wr="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="high",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["limited_balance", "cannot_sit_unsupported", "limited_grip",
              "elbow_injury", "vertigo", "multiple_sclerosis", "hip_pain",
              "si_joint_pain", "elderly_65plus", "osteoporosis"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "rheumatoid_arthritis", "hip_replacement",
            "chronic_fatigue", "knee_pain"],
      safe=["cannot_stand", "knee_injury", "ankle_injury", "no_overhead",
            "plantar_fasciitis"],
      why="EL MAS EXIGENTE DE LA FAMILIA PELOTA: superficie inestable Y una "
           "sola pierna en el suelo. bal high, iso high, sl true. "
           "elderly_65plus y osteoporosis suben a contraindicacion — no por el "
           "peso, que es minimo, sino porque una caida desde sentado con "
           "mancuernas en las manos y sin poder amortiguar es fractura de "
           "cadera. Contraindicacion por consecuencia, otra vez."),

    E("1656", "dumbbell biceps curl v sit on bosu ball", "seated",
      bal="moderate", grip="firm",
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
      why="Sexta entrada de la familia. El bosu es algo mas estable que la "
           "pelota completa, pero no lo suficiente para cambiar ninguna "
           "restriccion: mismo perfil que 1659, 0390 y 1650. El nombre "
           "menciona 'v sit' que el texto no describe — dice rodillas a 90 "
           "grados y pies en el suelo."),

    E("1658", "dumbbell lunge with bicep curl", "standing", standing=True,
      bal="high", sl=True, grip="firm", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", el="moderate", lumbar="moderate",
                ank="moderate"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "elbow_injury",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity", "osteoporosis",
            "tendinitis_elbow"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff"],
      why="Zancada con curl: combina el filtro de rodilla del patron lunge con "
           "el de agarre del curl. Frente a 1688 lunge with twist (lote 23), "
           "cambia rotacion por carga en las manos — sale lumbar_disc de "
           "contra a cautions, entra limited_grip a contra. Dos ejercicios "
           "compuestos casi iguales con filtros distintos."),

    E("1660", "dumbbell kneeling bicep curl exercise ball", "kneeling",
      floor=True, bal="low", grip="firm",
      stress=js(el="moderate", knee="high", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "limited_grip", "elbow_injury",
              "pregnancy_3rd"],
      caut=["knee_pain", "osteoarthritis", "tendinitis_elbow", "wrist_injury",
            "hip_pain", "rheumatoid_arthritis", "elderly_65plus",
            "shoulder_impingement", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "ankle_injury",
            "lumbar_disc", "lumbar_pain", "sciatica", "plantar_fasciitis",
            "dysautonomia"],
      why="Septima de la familia pelota y la unica que NO es inestable: la "
           "pelota se usa como apoyo de codos, no como asiento. Por eso "
           "limited_balance esta en safe_for y desaparecen vertigo y "
           "multiple_sclerosis. A cambio, arrodillarse mete knee high y toda "
           "la Capa A de rodilla. El mismo implemento en distinto rol invierte "
           "el perfil de restriccion."),

    E("1668", "dumbbell one arm seated bicep curl on exercise ball", "seated",
      bal="moderate", grip="firm", lat="unilateral",
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
      why="Octava de la familia pelota, version unilateral. Con 1659, 0390, "
           "1650, 1656 y 1668 el dataset tiene CINCO curls sentado en pelota "
           "que difieren solo en agarre y lateralidad, sin una sola diferencia "
           "de restriccion. Es el grupo de duplicados mas grande encontrado "
           "hasta ahora."),
]

CONFIDENCE_OVERRIDES = {
    "0627": 0.70,  # el nombre dice mixed grip, el texto describe supinado doble
    "1656": 0.70,  # el nombre dice 'v sit', el texto describe pies en el suelo
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
    print(f"lote 27: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
