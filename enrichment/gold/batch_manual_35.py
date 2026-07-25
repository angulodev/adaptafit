#!/usr/bin/env python3
"""Lote 35 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0295", "dumbbell clean", "standing", standing=True, bal="moderate",
      grip="firm", axial="moderate", impact="moderate", flex="moderate",
      stress=js(knee="high", lumbar="high", sh="moderate", hip="moderate",
                wr="high", ank="moderate", el="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "osteoporosis", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "wrist_injury", "carpal_tunnel", "limited_grip",
              "hernia_abdominal", "pelvic_floor_dysfunction", "cardiac",
              "elderly_65plus", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "shoulder_impingement", "rotator_cuff",
            "osteoarthritis", "obesity", "dysautonomia", "chronic_fatigue",
            "glaucoma", "hip_pain", "multiple_sclerosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "plantar_fasciitis"],
      why="Version con mancuernas de 0648 power clean. Menos exigente en "
           "hombro —no hay que rotar los codos bajo una barra— pero mantiene "
           "el salto, la recepcion y la muneca en hiperextension al recibir. "
           "A diferencia de 0648, el safe_for NO queda vacio: sin barra "
           "desaparecen cervical_injury y las restricciones de rango de "
           "hombro, y no_overhead entra en safe_for porque las mancuernas "
           "paran a la altura del hombro."),

    E("0299", "dumbbell cuban press", "standing", standing=True, bal="low",
      oh=True, grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate"),
      pat="vertical_push", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "hypermobility"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "lumbar_disc", "lumbar_pain", "dysautonomia", "hypertension",
            "elderly_65plus", "osteoporosis", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Press que ROTA las munecas de pronacion a supinacion durante el "
           "recorrido, lo que arrastra rotacion externa de hombro bajo carga "
           "en la parte alta: laxity high y hypermobility a contraindicacion, "
           "unico del grupo de press overhead donde ocurre. Frente a 0426 "
           "—mismo press sin rotacion— es un escalon mas restrictivo."),

    E("0381", "dumbbell rear lunge", "standing", standing=True, bal="high",
      sl=True, grip="firm", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="moderate",
                ank="moderate"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Duplicado funcional de 0336 dumbbell lunge (lote 30) con paso hacia "
           "atras. La direccion reduce el impacto de rodilla en la practica, "
           "pero ningun campo de la taxonomia lo captura — es una limitacion "
           "conocida y aceptada: el patron lunge no distingue direccion."),

    E("1002", "band lying straight leg raise", "supine", floor=True,
      grip="light", flex="high",
      stress=js(lumbar="high", hip="high", sh="low"),
      pat="core_flexion", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="moderate",
      temp="low",
      contra=["lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cannot_get_on_floor",
              "cannot_lie_supine", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["postpartum", "obesity", "elderly_65plus", "hypertension",
            "hip_pain", "limited_grip", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="Elevacion de piernas rectas en el suelo: brazo de palanca completo "
           "sobre la lumbar, igual que 2802. La banda no asiste — anade "
           "resistencia justo en el punto bajo, que es donde la lumbar mas "
           "sufre. Duodecima entrada de core_flexion."),

    E("1459", "dumbbell romanian deadlift", "standing", standing=True,
      bal="moderate", grip="firm", flex="moderate",
      stress=js(lumbar="high", hip="high", knee="moderate"),
      pat="hinge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "hip_replacement", "limited_grip",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "knee_pain", "hypertension",
            "glaucoma", "obesity", "dysautonomia", "elderly_65plus",
            "hypermobility", "limited_balance", "pelvic_floor_dysfunction",
            "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "ankle_injury",
            "plantar_fasciitis"],
      why="Version con mancuernas de 0085 barbell romanian deadlift. Sin carga "
           "axial —el peso cuelga de las manos, no se apoya en la espalda— "
           "desaparecen cervical_injury, si_joint_pain y "
           "recent_abdominal_surgery de las contraindicaciones, y valsalva "
           "baja a moderate. Sigue sin ser apto para hernia discal: la familia "
           "de bisagras cargadas no tiene NINGUNA entrada que lo sea."),

    E("3217", "modified hindu push-up (male)", "plank", floor=True, oh=True,
      grip="none", stress=js(wr="high", sh="high", lumbar="moderate",
                             el="moderate", hip="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="high", headdown=True, valsalva="moderate",
      iso="moderate", metab="moderate", laxity="high", pelvic="moderate",
      gripdur="none", temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "no_overhead", "cannot_get_on_floor",
              "cannot_lie_prone", "hypermobility", "glaucoma",
              "retinal_detachment_risk", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "obesity", "elderly_65plus", "chronic_fatigue", "vertigo",
            "dysautonomia", "hip_pain", "shoulder_pain"],
      safe=["cannot_stand", "limited_grip", "knee_injury", "knee_pain",
            "hip_replacement", "ankle_injury", "plantar_fasciitis"],
      why="Version sin cobra de 3662 pike-to-cobra push-up: mantiene la fase "
           "de V invertida —cadera arriba, cabeza abajo, hombro en flexion "
           "maxima— pero elimina la extension lumbar. Eso saca lumbar_disc de "
           "contraindicacion a precaucion y baja diff de 5 a 4. "
           "head_below_heart se mantiene por la posicion de pike."),

    E("3222", "semi squat jump (male)", "standing", standing=True,
      bal="moderate", grip="none", impact="high",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_interval", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement",
              "osteoporosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
              "vertigo", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "lumbar_pain",
            "lumbar_disc", "dysautonomia", "hypertension", "cardiac",
            "obesity", "elderly_65plus", "chronic_fatigue", "asthma",
            "varicose_veins", "multiple_sclerosis", "postpartum",
            "pregnancy_1st"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Duplicado funcional de 3220 astride jumps y 3223 star jump: salto "
           "explosivo desde flexion de rodilla. El dataset tiene ya cuatro "
           "entradas de salto vertical con nombres distintos y el mismo "
           "perfil."),

    E("1387", "one leg floor calf raise", "standing", standing=True,
      bal="moderate", sl=True, grip="none",
      stress=js(ank="high", knee="low", hip="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain",
            "osteoarthritis", "dysautonomia", "vertigo", "elderly_65plus",
            "hip_replacement", "multiple_sclerosis", "varicose_veins",
            "osteoporosis"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "lumbar_disc", "lumbar_pain", "sciatica", "cannot_get_on_floor",
            "cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "hernia_abdominal",
            "knee_injury"],
      why="SEGUNDO CASO DE APOYO EXTERNO, tras 3636. El texto dice 'place your "
           "hands on a wall or sturdy object for balance': eso mantiene "
           "limited_balance en precaucion pese a ser apoyo unipodal — sin el "
           "apoyo seria contraindicacion, como en 0795 standing single leg "
           "curl. 18 en safe_for. Confirma que la mencion explicita de un "
           "apoyo en el texto debe rebajar un escalon el filtro de equilibrio."),

    E("0852", "weighted squat", "standing", standing=True, bal="moderate",
      grip="firm", axial="moderate",
      stress=js(knee="high", hip="moderate", lumbar="moderate",
                ank="moderate"),
      pat="squat", diff=3, rom="high",
      ortho="high", change="low", valsalva="high", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip", "osteoporosis",
              "pregnancy_3rd"],
      caut=["osteoarthritis", "hip_pain", "lumbar_pain", "lumbar_disc",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "dysautonomia", "elderly_65plus", "obesity", "hypertension",
            "cardiac", "multiple_sclerosis", "pelvic_floor_dysfunction",
            "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "sciatica"],
      why="Sentadilla con el peso al frente o sobre los hombros: a diferencia "
           "de 0413 (mancuernas colgando a los lados), la carga queda por "
           "delante del eje y sube valsalva a high y axial a moderate. "
           "osteoporosis entra en contraindicacion. La escala del patron squat "
           "queda: 3221 parcial < 0413 mancuernas < 0852 carga frontal < 0054 "
           "barra en la espalda."),

    E("1271", "chest and front of shoulder stretch", "standing",
      standing=True, bal="low", grip="none",
      stress=js(sh="moderate", el="low", cerv="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="moderate", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement"],
      caut=["rotator_cuff", "shoulder_pain", "hypermobility", "elbow_injury",
            "cervical_injury", "dysautonomia", "elderly_65plus",
            "limited_grip"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "no_overhead", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "lumbar_disc", "lumbar_pain", "sciatica",
            "plantar_fasciitis", "osteoporosis", "hernia_abdominal",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      why="Tercer estiramiento pectoral de pie (1405, 1167, 1271), 22 en "
           "safe_for. Entrelazar los dedos anade una exigencia minima de mano "
           "—limited_grip a cautions— que los otros dos no tienen. Los tres "
           "contraindican el pinzamiento por la misma razon: cruzar los brazos "
           "es aduccion horizontal."),

    E("0080", "barbell reverse curl", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(el="moderate", wr="high", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "lumbar_pain",
            "lumbar_disc", "dysautonomia", "limited_balance", "hypertension",
            "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Curl con agarre PRONADO: carga los extensores de muneca y el "
           "epicondilo lateral, o sea el tendon de la epicondilitis. "
           "tendinitis_elbow y carpal_tunnel a contraindicacion, lo que no "
           "ocurre en 0031 ni 0447 con agarre supinado. Mismo criterio ya "
           "aplicado a los curls de muneca invertidos (1411, 1441)."),

    E("3237", "landmine lateral raise", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "neck_pain",
            "cervical_injury", "hypermobility", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "hypertension", "elderly_65plus",
            "chronic_fatigue"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "sciatica"],
      why="El texto es confuso —dice apoyar la barra en los hombros y a la vez "
           "elevarla en diagonal— pero el gesto del landmine es claro: "
           "elevacion en arco con una barra anclada. El peso lejos del cuerpo "
           "y el brazo de palanca largo suben lumbar a moderate, algo que las "
           "elevaciones laterales con mancuerna no tienen."),

    E("0027", "barbell bent over row", "standing", standing=True,
      bal="moderate", grip="firm", flex="moderate",
      stress=js(lumbar="high", sh="moderate", el="moderate", wr="moderate",
                hip="moderate"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "si_joint_pain", "elbow_injury",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "shoulder_impingement", "rotator_cuff",
            "wrist_injury", "carpal_tunnel", "limited_balance", "hypertension",
            "obesity", "elderly_65plus", "osteoporosis", "dysautonomia",
            "hip_pain"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="SEXTA entrada de la familia de remos de pie (1330, 1773, 3017, "
           "0076, 0574, 0027) y duplicado funcional de las tres ultimas. Todas "
           "comparten el mismo problema estructural y ninguna es apta para "
           "hernia discal — es el patron con menos variedad util del "
           "catalogo."),

    E("0040", "barbell front raise and pullover", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low", ext="moderate",
      stress=js(sh="high", lumbar="high", wr="moderate", el="moderate",
                cerv="moderate"),
      pat="isolation", diff=4, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "wrist_injury", "hypermobility",
              "cervical_injury", "lumbar_disc", "osteoporosis"],
      caut=["neck_pain", "elbow_injury", "lumbar_pain", "dysautonomia",
            "hypertension", "elderly_65plus", "chronic_fatigue",
            "carpal_tunnel", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Elevacion frontal encadenada con la barra DETRAS DE LA CABEZA, de "
           "pie y con los brazos rectos: flexion completa de hombro a rango "
           "final con brazo de palanca maximo, y la lumbar se arquea para "
           "compensar. laxity high. Es la version de pie de 0037 decline "
           "pullover y comparte su perfil: el peor caso de hombro sin ser un "
           "ejercicio de fuerza."),

    E("0096", "barbell side bent v. 2", "standing", standing=True, bal="low",
      grip="firm", flex="moderate", rot="low", axial="low",
      lat="alternating",
      stress=js(lumbar="high", hip="low", sh="low", wr="moderate"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="high", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "cannot_stand", "wheelchair", "limited_grip",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "shoulder_impingement", "hypertension",
            "obesity", "elderly_65plus", "dysautonomia", "hypermobility",
            "pelvic_floor_dysfunction", "postpartum", "wrist_injury"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "carpal_tunnel"],
      why="TERCERA FLEXION LATERAL del proyecto (0407 con mancuerna, 0794 sin "
           "carga, 0096 con barra). Con tres casos independientes, la falta de "
           "spinal_lateral_flexion deja de ser una anecdota: es un campo "
           "necesario. Aqui la barra sostenida con las dos manos alarga el "
           "brazo de palanca lateral respecto de 0407."),

    E("0104", "barbell standing back wrist curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(wr="high", el="low", lumbar="low", sh="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "wrist_injury", "carpal_tunnel",
              "limited_grip", "tendinitis_elbow"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "elbow_injury",
            "dysautonomia", "hypertension", "elderly_65plus",
            "limited_balance"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "one_arm_only"],
      why="Curl de muneca invertido de pie: extensores y epicondilo lateral, "
           "mismo criterio que 1411, 1441 y 0080. Es la sexta entrada de la "
           "familia de muneca y la primera que NO se hace sentado — util para "
           "quien no puede transferirse a un banco. 17 en safe_for."),

    E("0119", "barbell upright row v. 2", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="high", lumbar="moderate",
                cerv="low"),
      pat="vertical_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip", "wrist_injury",
              "carpal_tunnel", "hypermobility"],
      caut=["elbow_injury", "tendinitis_elbow", "neck_pain",
            "cervical_injury", "lumbar_pain", "lumbar_disc", "dysautonomia",
            "hypertension", "elderly_65plus", "osteoporosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="TERCERA correccion del mismo error de E1 en remo al menton (0120, "
           "0437, 0119): dijo horizontal_pull, es vertical_pull. Duplicado "
           "exacto de 0120. El sesgo del upright row ya esta confirmado, tres "
           "de tres."),

    E("1457", "barbell standing wide military press", "standing",
      standing=True, bal="low", oh=True, grip="firm", axial="moderate",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="high",
                cerv="low"),
      pat="vertical_push", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "lumbar_disc", "osteoporosis"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "lumbar_pain", "sciatica", "hypertension", "cardiac", "glaucoma",
            "retinal_detachment_risk", "dysautonomia", "elderly_65plus",
            "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Press militar con barra y agarre ancho. Frente a 0426 y 0361 con "
           "mancuernas: la barra impone una trayectoria fija por delante de la "
           "cara, lo que obliga a arquear la lumbar para dejarla pasar — "
           "lumbar high y lumbar_disc a contraindicacion, cuando en las "
           "versiones con mancuerna estaba en precaucion. El agarre ancho "
           "ademas abre mas el hombro."),
]

CONFIDENCE_OVERRIDES = {
    "3237": 0.70,  # el texto describe apoyar la barra y elevarla a la vez
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
    print(f"lote 35: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
