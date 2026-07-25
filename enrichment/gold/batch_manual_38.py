#!/usr/bin/env python3
"""Lote 38 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0805", "suspended abdominal fallout", "standing", standing=True,
      bal="high", oh=True, grip="firm", ext="moderate",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate"),
      pat="core_antiextension", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "limited_grip",
              "no_overhead", "shoulder_impingement", "rotator_cuff",
              "shoulder_pain", "lumbar_disc", "lumbar_pain", "sciatica",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "hypermobility", "pregnancy_1st",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "si_joint_pain",
            "osteoporosis", "obesity", "elderly_65plus", "chronic_fatigue",
            "hypertension", "dysautonomia", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Rollout de pie en suspension: el core frena la extension lumbar "
           "mientras los brazos se van hacia adelante y arriba. Al final del "
           "recorrido el hombro llega cerca de los 180 grados de flexion, "
           "por eso no_overhead es contraindicacion pese a que nadie "
           "levanta nada. Requiere anclaje de suspension aunque el dataset "
           "lo liste como body weight."),

    E("2796", "dumbbell step-up lunge", "standing", standing=True, bal="high",
      sl=True, grip="firm", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="moderate",
                ank="moderate"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "vertigo", "visual_impairment",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia",
            "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Instrucciones equivalentes a 0431 dumbbell step-up: se sube al "
           "cajon con las dos piernas y se baja. El 'lunge' del nombre no "
           "aparece en el texto. Se clasifica igual que 0431. "
           "visual_impairment sigue en contraindicacion porque hay que "
           "calcular la altura del escalon sin verla."),

    E("3168", "bodyweight squatting row", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(knee="moderate", hip="moderate", sh="moderate",
                el="moderate", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["knee_injury", "knee_pain", "knee_replacement", "hip_replacement",
            "hip_pain", "osteoarthritis", "shoulder_impingement",
            "shoulder_pain", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "ankle_injury", "limited_balance", "lumbar_pain", "dysautonomia",
            "elderly_65plus", "obesity"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "lumbar_disc", "sciatica", "plantar_fasciitis", "osteoporosis"],
      why="Detalle que cambia la lectura: al sostenerse del anclaje, los "
           "brazos ASISTEN la sentadilla en vez de cargarla. Por eso "
           "requires_balance baja a low y knee queda en moderate, cuando "
           "toda sentadilla libre del catalogo va en high. Es una sentadilla "
           "asistida disfrazada de remo — util para quien necesita bajar y "
           "subir con apoyo, siempre que la mano aguante."),

    E("1757", "dumbbell single leg deadlift", "standing", standing=True,
      bal="high", sl=True, grip="firm", flex="moderate",
      stress=js(hip="high", lumbar="high", knee="moderate", ank="moderate"),
      lat="unilateral", pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "osteoporosis", "hip_replacement",
              "ankle_injury", "limited_grip", "vertigo", "hernia_abdominal",
              "multiple_sclerosis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "knee_pain", "knee_injury",
            "plantar_fasciitis", "visual_impairment", "hypertension",
            "glaucoma", "dysautonomia", "elderly_65plus", "obesity",
            "hypermobility", "osteoarthritis", "pelvic_floor_dysfunction",
            "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "elbow_injury"],
      why="Regresion de 1756 barbell single leg deadlift: la mancuerna cuelga "
           "de una mano cerca del cuerpo en vez de una barra larga que "
           "amplifica cada oscilacion. Difficulty baja de 5 a 4 y "
           "visual_impairment pasa de contraindicacion a precaucion —sin "
           "barra, perder el eje ya no arrastra dos metros de acero. Todo lo "
           "lumbar se mantiene igual."),

    E("2292", "dumbbell rear delt raise", "standing", standing=True,
      bal="low", grip="firm", flex="low",
      stress=js(lumbar="high", sh="high", hip="moderate", wr="low",
                el="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="high",
      metab="low", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "shoulder_impingement",
              "rotator_cuff", "limited_grip", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["shoulder_pain", "si_joint_pain", "hip_pain", "hip_replacement",
            "cervical_injury", "neck_pain", "elbow_injury", "wrist_injury",
            "hypertension", "glaucoma", "dysautonomia", "elderly_65plus",
            "hypermobility", "obesity", "hernia_abdominal"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "carpal_tunnel"],
      why="Version con mancuernas de 0075 barbell rear delt raise. El codo "
           "va ligeramente flexionado y la muneca queda neutra: wrist baja "
           "de moderate a low y carpal_tunnel entra en safe_for. Lo lumbar "
           "no mejora en nada —el tronco sigue inclinado sosteniendo peso "
           "toda la serie— asi que las contraindicaciones de columna son "
           "identicas. 1022 band standing rear delt row es el escalon "
           "anterior."),

    E("0363", "dumbbell one arm upright row", "standing", standing=True,
      bal="low", grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate",
                cerv="low"),
      lat="unilateral", pat="vertical_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip",
              "wrist_injury"],
      caut=["carpal_tunnel", "elbow_injury", "tendinitis_elbow", "neck_pain",
            "cervical_injury", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "hypermobility", "dysautonomia", "hypertension",
            "elderly_65plus", "osteoporosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "one_arm_only"],
      why="Remo al menton a una mano. Frente a 0120 y 0121 con barra gana "
           "one_arm_only en safe_for, pero el peso asimetrico obliga al "
           "tronco a contrarrestar la inclinacion lateral: lumbar sube de "
           "low a moderate. El arco de elevacion del hombro es el mismo, "
           "asi que sigue contraindicado para pinzamiento — el agarre "
           "unilateral no arregla eso."),

    E("0414", "dumbbell standing alternate overhead press", "standing",
      standing=True, bal="low", oh=True, grip="firm", axial="low",
      stress=js(lumbar="moderate", sh="high", el="moderate", wr="moderate"),
      lat="alternating", pat="vertical_push", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["shoulder_pain", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "lumbar_pain", "cervical_injury", "hypermobility",
            "dysautonomia", "hypertension", "elderly_65plus", "osteoporosis",
            "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Press alternado: mientras un brazo empuja, el otro sostiene la "
           "mancuerna a la altura del hombro. Ese sosten agrega isometrico "
           "moderate que 0361 a un brazo no tiene. one_arm_only NO va a "
           "safe_for aunque el gesto sea alternado: hacen falta las dos "
           "manos cargadas a la vez."),

    E("0991", "band pull through", "standing", standing=True, bal="low",
      grip="light", flex="low",
      stress=js(hip="high", lumbar="moderate", knee="low"),
      pat="hinge", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair"],
      caut=["lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
            "hip_pain", "hip_replacement", "osteoporosis", "hernia_abdominal",
            "limited_grip", "dysautonomia", "elderly_65plus", "obesity",
            "pelvic_floor_dysfunction", "hypertension", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Hallazgo del lote. La banda tira hacia ATRAS y abajo, no hacia el "
           "suelo: la columna nunca sostiene una carga vertical, que es lo "
           "que hace daño en 0432, 1459 y 0044. Con spinal_flexion low y "
           "solo dos contraindicaciones, es la bisagra de cadera mas barata "
           "del catalogo y el ejercicio con el que se le puede enseñar el "
           "patron a un perfil lumbar sensible antes de tocar una mancuerna."),

    E("2136", "dumbbell cuban press v. 2", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate"),
      pat="vertical_push", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip"],
      caut=["hypermobility", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "lumbar_disc", "lumbar_pain", "dysautonomia",
            "hypertension", "elderly_65plus", "osteoporosis", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Diferencia real con 0299 dumbbell cuban press: aca se presiona "
           "primero y se rota la muneca ARRIBA, con el brazo ya bloqueado, "
           "en vez de rotar durante el recorrido bajo carga. Eso baja "
           "joint_laxity_risk de high a moderate y saca hypermobility de "
           "contraindicacion a precaucion. Sigue siendo un press overhead: "
           "el hombro pinzado queda fuera igual."),

    E("0053", "barbell jump squat", "standing", standing=True, bal="high",
      grip="firm", axial="high", impact="high",
      stress=js(knee="high", hip="high", lumbar="high", cerv="moderate",
                ank="high"),
      pat="squat", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "lumbar_disc", "lumbar_pain", "sciatica",
              "si_joint_pain", "osteoporosis", "cervical_injury",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cardiac", "hypertension",
              "elderly_65plus", "plantar_fasciitis", "vertigo",
              "osteoarthritis", "limited_grip", "pregnancy_1st",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "multiple_sclerosis", "asthma",
            "hip_pain", "hypermobility", "epilepsy", "varicose_veins",
            "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury"],
      why="Carga axial sobre la columna MAS aterrizaje de alto impacto: la "
           "peor combinacion espinal del catalogo, peor que 0371 dumbbell "
           "plyo squat porque ahi el peso cuelga de las manos y aca comprime "
           "vertebra contra vertebra en cada caida. hypertension y cardiac "
           "suben a contraindicacion —no precaucion— por el valsalva "
           "obligado bajo barra. Difficulty 5."),

    E("0454", "ez barbell spider curl", "standing", standing=True, bal="low",
      grip="firm",
      stress=js(el="high", wr="moderate", sh="low", lumbar="moderate"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel"],
      caut=["hypermobility", "rheumatoid_arthritis", "shoulder_impingement",
            "lumbar_pain", "cervical_injury", "neck_pain", "dysautonomia",
            "osteoarthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "no_overhead", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "sciatica"],
      why="Curl con el brazo apoyado sobre el banco inclinado, pero de pie e "
           "inclinado sobre el: gana el aislamiento del codo de 0070 barbell "
           "preacher curl y ademas suma carga lumbar y cervical por la "
           "postura mantenida. 0070 y 0402 hacen lo mismo sentado. Si el "
           "objetivo es el biceps y no la resistencia postural, sentado gana."),

    E("0833", "weighted donkey calf raise", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(ank="high", knee="low", hip="low", lumbar="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis"],
      caut=["limited_balance", "knee_pain", "hip_pain", "hip_replacement",
            "osteoarthritis", "dysautonomia", "vertigo", "varicose_veins",
            "elderly_65plus", "osteoporosis", "limited_grip", "lumbar_pain",
            "rheumatoid_arthritis"],
      safe=["no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "lumbar_disc",
            "sciatica", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "hernia_abdominal"],
      why="Lo que cambia frente a 0284 donkey calf raise no es el peso sino "
           "la plataforma: con el talon colgando el tobillo baja por debajo "
           "de la horizontal y la fascia plantar se estira al maximo bajo "
           "carga. plantar_fasciitis pasa de precaucion a contraindicacion. "
           "Si el objetivo es gemelo sin castigar la fascia, 0284 en piso "
           "plano es la opcion."),

    E("0710", "side hip abduction", "standing", standing=True, bal="moderate",
      sl=True,
      stress=js(hip="moderate", knee="low", ank="low", lumbar="low"),
      lat="alternating", pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="none", iso="low", metab="low",
      laxity="low", pelvic="low", temp="low",
      contra=["cannot_stand", "wheelchair"],
      caut=["hip_pain", "si_joint_pain", "hip_replacement", "osteoarthritis",
            "limited_balance", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "lumbar_pain", "ankle_injury"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "sciatica", "knee_injury", "knee_pain",
            "plantar_fasciitis", "osteoporosis", "hernia_abdominal"],
      why="Dos contraindicaciones en total, las dos de Capa A. Trabaja "
           "gluteo medio, que es el musculo que sostiene la pelvis al "
           "caminar: para prevencion de caidas y para descargar rodilla "
           "vale mas que cualquier sentadilla. Difficulty 1 y safe_for de "
           "veinte condiciones. Para quien no puede estar de pie, 3006 "
           "resistance band seated hip abduction cubre lo mismo sentado."),

    E("0809", "suspended split squat", "standing", standing=True, bal="high",
      sl=True,
      stress=js(knee="high", hip="high", lumbar="moderate", ank="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "vertigo", "visual_impairment",
              "osteoarthritis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "plantar_fasciitis", "hypermobility", "dysautonomia",
            "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Split squat con el pie de atras colgando de la cinta: la base de "
           "apoyo no solo se reduce, ademas se mueve. Un escalon completo "
           "por encima de 2368 split squats —difficulty 3 a 4— y "
           "osteoarthritis sube a contraindicacion por la rodilla de "
           "adelante absorbiendo todo. Requiere anclaje de suspension."),

    E("1760", "dumbbell goblet squat", "standing", standing=True, bal="low",
      grip="firm",
      stress=js(knee="high", hip="moderate", lumbar="low", ank="moderate",
                el="moderate", sh="low"),
      pat="squat", diff=2, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip"],
      caut=["osteoarthritis", "hip_pain", "lumbar_pain", "ankle_injury",
            "plantar_fasciitis", "limited_balance", "dysautonomia",
            "elderly_65plus", "osteoporosis", "obesity", "elbow_injury",
            "shoulder_pain", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "sciatica", "lumbar_disc"],
      why="Segundo hallazgo del lote. La mancuerna contra el pecho funciona "
           "de contrapeso: obliga al tronco a mantenerse vertical, y ese "
           "detalle baja lumbar de moderate —como en 0413 dumbbell squat— a "
           "low, con lumbar_disc entrando a safe_for. Es la mejor sentadilla "
           "cargada del catalogo para columna sensible. La rodilla no "
           "mejora: sigue en high."),

    E("2803", "dumbbell supported squat", "standing", standing=True,
      bal="moderate", grip="firm",
      stress=js(knee="high", hip="moderate", lumbar="moderate",
                ank="moderate"),
      pat="squat", diff=2, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip",
              "pregnancy_3rd"],
      caut=["osteoarthritis", "hip_pain", "lumbar_pain", "lumbar_disc",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "dysautonomia", "elderly_65plus", "osteoporosis", "obesity",
            "multiple_sclerosis", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "sciatica"],
      why="El nombre dice 'supported' pero las instrucciones no mencionan "
           "ningun apoyo: describen exactamente 0413 dumbbell squat, "
           "mancuernas a los costados. Se clasifica identico a 0413 y se "
           "marca como duplicado probable. Si el apoyo existiera, "
           "requires_balance y limited_balance cambiarian, asi que no es un "
           "detalle cosmetico: hay que resolverlo en E3."),

    E("0285", "dumbbell alternate biceps curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      lat="alternating", pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["carpal_tunnel", "wrist_injury", "rheumatoid_arthritis",
            "shoulder_pain", "lumbar_pain", "dysautonomia", "hypertension",
            "varicose_veins"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica", "one_arm_only"],
      why="0294 dumbbell biceps curl pero un brazo por vez. La diferencia "
           "util no es de carga sino de accesibilidad: al ser alternado, "
           "one_arm_only entra en safe_for, cosa que en la version "
           "simultanea no corresponde. Mismo estres de codo, mismo agarre "
           "sostenido."),

    E("0286", "dumbbell alternate side press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low",
      stress=js(lumbar="moderate", sh="high", el="moderate", wr="moderate"),
      lat="alternating", pat="vertical_push", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["shoulder_pain", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "lumbar_pain", "cervical_injury", "hypermobility",
            "dysautonomia", "hypertension", "elderly_65plus", "osteoporosis",
            "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Instrucciones equivalentes a 0414 dumbbell standing alternate "
           "overhead press: se alterna el press manteniendo la otra "
           "mancuerna en el hombro. El 'side' del nombre no aparece en el "
           "texto —un side press real inclinaria el tronco al costado y "
           "cambiaria toda la carga lumbar. Cuarto duplicado probable del "
           "pipeline."),
]

CONFIDENCE_OVERRIDES = {
    "2803": 0.70,  # el nombre dice "supported" pero el texto describe 0413
    "0286": 0.70,  # el nombre dice "side press" pero el texto describe 0414
    "3168": 0.75,  # no se aclara el anclaje ni cuanto peso corporal asiste
    "2796": 0.75,  # el nombre dice lunge, el texto describe un step-up (0431)
    "0805": 0.80,  # requiere suspension, listado como body weight
    "0809": 0.80,  # requiere suspension, listado como body weight
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
    print(f"lote 38: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
