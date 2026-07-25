#!/usr/bin/env python3
"""Lote 32 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("3679", "sit-up with arms on chest", "supine", floor=True, grip="none",
      flex="high", stress=js(lumbar="high", hip="moderate", cerv="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="high", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "postpartum", "obesity",
            "elderly_65plus", "hypertension"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "dysautonomia", "cervical_injury", "neck_pain",
            "shoulder_impingement", "rotator_cuff"],
      why="Undecima entrada de core_flexion y la MENOS restrictiva del suelo: "
           "brazos cruzados sobre el pecho, sin traccion de cuello ni palanca "
           "sobre la cabeza. cervical_injury Y hombro en safe_for. Es la "
           "version que E4 debe ofrecer por defecto en vez de 3202 o 0992, que "
           "son el mismo sit-up con manos detras de la nuca."),

    E("0628", "monster walk", "standing", standing=True, bal="moderate",
      grip="none", impact="low", lat="alternating",
      stress=js(hip="moderate", knee="moderate", ank="low", lumbar="low"),
      pat="carry", diff=2, rom="low",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "hip_replacement"],
      caut=["hip_pain", "si_joint_pain", "knee_injury", "knee_pain",
            "osteoarthritis", "ankle_injury", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "plantar_fasciitis",
            "varicose_veins"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "lumbar_pain", "sciatica", "osteoporosis",
            "hernia_abdominal"],
      why="18 en safe_for y cuatro contraindicaciones. Segundo hallazgo "
           "seguido de tren inferior accesible, despues de 3007. Desplazamiento "
           "lateral con banda en los tobillos: sin impacto, sin carga axial, "
           "sin agarre. knee_injury en cautions —no contra— porque la rodilla "
           "se mantiene en flexion leve constante, sin ciclo de carga. "
           "hip_replacement si va a contra: la abduccion resistida es "
           "precaucion estandar post-artroplastia."),

    E("0310", "dumbbell front raise", "standing", standing=True, bal="low",
      grip="firm", stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury", "wrist_injury"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "sciatica", "plantar_fasciitis", "carpal_tunnel",
            "osteoporosis"],
      why="Version con mancuernas de 0041 (barra) y 0978 (banda). Cierra la "
           "terna de elevacion frontal y confirma la escala: con mancuernas "
           "las munecas trabajan independientes y el peso queda mas cerca del "
           "cuerpo, asi que wrist_injury baja a cautions y lumbar_disc entra en "
           "safe_for — en la version con barra los dos estaban peor."),

    E("0437", "dumbbell upright row", "standing", standing=True, bal="low",
      grip="firm", stress=js(sh="high", el="moderate", wr="moderate",
                             lumbar="low"),
      pat="vertical_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip",
              "hypermobility"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "neck_pain", "cervical_injury", "lumbar_pain",
            "dysautonomia", "hypertension", "elderly_65plus", "osteoporosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "plantar_fasciitis"],
      why="CORRECCION A E1 (dijo horizontal_pull, es vertical_pull) — mismo "
           "caso que 0120. Version con mancuernas: las manos pueden separarse "
           "en el ascenso en vez de quedar fijas al ancho de la barra, lo que "
           "reduce la desviacion cubital forzada. wrist_injury y carpal_tunnel "
           "bajan de contra a cautions. El pinzamiento sigue siendo intrinseco "
           "al gesto y no se arregla con el implemento."),

    E("1476", "one leg squat", "standing", standing=True, bal="high", sl=True,
      grip="none", stress=js(knee="high", hip="high", ank="high",
                             lumbar="moderate"),
      pat="squat", diff=5, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "osteoarthritis", "plantar_fasciitis",
              "elderly_65plus", "multiple_sclerosis", "vertigo",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "dysautonomia", "obesity", "osteoporosis", "hypermobility",
            "chronic_fatigue"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Sentadilla a una pierna: todo el peso corporal sobre una rodilla en "
           "flexion profunda, con el tobillo en dorsiflexion maxima para "
           "mantener el equilibrio. ank high, raro fuera de los saltos. diff 5 "
           "sin ninguna carga externa — es el unico ejercicio de peso corporal "
           "del catalogo que alcanza el maximo solo por demanda de "
           "estabilidad."),

    E("2271", "left hook. boxing", "standing", standing=True, bal="moderate",
      grip="none", rot="high", impact="low", lat="unilateral",
      stress=js(lumbar="moderate", sh="moderate", hip="moderate", knee="low"),
      pat="cardio_interval", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="moderate",
      laxity="moderate", pelvic="low", gripdur="none", temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "shoulder_impingement", "si_joint_pain"],
      caut=["lumbar_pain", "rotator_cuff", "shoulder_pain", "hip_pain",
            "knee_pain", "limited_balance", "dysautonomia", "vertigo",
            "elderly_65plus", "osteoporosis", "hypermobility",
            "multiple_sclerosis", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "ankle_injury", "plantar_fasciitis", "hip_replacement"],
      why="Primer ejercicio de boxeo del proyecto. Perfil interesante: impacto "
           "bajo y sin agarre, pero el gancho es rotacion explosiva de tronco "
           "con pivote — lumbar_disc a contra, igual que en swing 360 y las "
           "otras rotaciones de pie. El hombro en aduccion horizontal rapida "
           "saca tambien el pinzamiento. Util para quien tolera rotacion pero "
           "no impacto."),

    E("3219", "scissor jumps (male)", "standing", standing=True, bal="moderate",
      grip="none", impact="high", lat="alternating",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_interval", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement",
              "osteoporosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
              "vertigo", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "lumbar_pain",
            "lumbar_disc", "si_joint_pain", "dysautonomia", "hypertension",
            "cardiac", "obesity", "elderly_65plus", "chronic_fatigue",
            "asthma", "varicose_veins", "multiple_sclerosis", "postpartum",
            "pregnancy_1st"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Saltos alternando piernas cruzadas: el cruce agrega un componente "
           "de aduccion en el aterrizaje que 3223 y 3220 no tienen, pero no "
           "cambia el bloque de contraindicaciones. Sexto cardio de impacto "
           "alto del proyecto — todos con el mismo perfil de rodilla y tobillo."),

    E("3582", "lunge with jump", "standing", standing=True, bal="high",
      sl=True, grip="none", impact="high", lat="alternating",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", gripdur="none",
      temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "osteoarthritis", "vertigo",
              "elderly_65plus", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "dysautonomia", "hypertension", "cardiac", "obesity",
            "chronic_fatigue", "postpartum", "multiple_sclerosis", "asthma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Zancada con cambio de pierna en el aire: suma impact high y "
           "change high al patron de zancada. Frente a 0336 dumbbell lunge "
           "—la base sin salto ni carga— agrega seis contraindicaciones, todas "
           "de impacto: osteoporosis, fascitis, suelo pelvico, artrosis, "
           "vertigo y mayores de 65."),

    E("3698", "inchworm v. 2", "standing", floor=True, standing=True,
      bal="moderate", grip="none", flex="high",
      stress=js(wr="high", lumbar="high", sh="moderate", hip="high",
                el="moderate"),
      pat="core_antiextension", diff=3, rom="high",
      ortho="high", change="high", headdown=True, valsalva="moderate",
      iso="moderate", metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="none", temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_stand",
              "cannot_get_on_floor", "cannot_lie_prone", "lumbar_disc",
              "sciatica", "shoulder_impingement", "osteoporosis",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "rotator_cuff",
            "elbow_injury", "hypermobility", "obesity", "elderly_65plus",
            "dysautonomia", "vertigo", "glaucoma", "limited_balance",
            "knee_pain"],
      safe=["no_overhead", "limited_grip", "knee_injury", "hip_replacement",
            "ankle_injury", "plantar_fasciitis"],
      why="RIESGO ESCONDIDO. Parece un ejercicio de movilidad, pero 'keeping "
           "your legs straight, walk your feet towards your hands' es "
           "exactamente 3231 two toe touch — flexion lumbar completa con "
           "piernas rectas, repetida. lumbar_disc y osteoporosis a contra. "
           "Ademas suma plancha (muneca) y transiciones de pie a suelo "
           "(change high, head_below_heart). Acumula tres perfiles de riesgo "
           "distintos en un solo ejercicio."),

    E("0426", "dumbbell standing overhead press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate"),
      pat="vertical_push", diff=2, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
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
      why="Version bilateral de 0361, con perfil identico salvo one_arm_only "
           "(que aqui no aplica). Sigue siendo el mejor vertical_push "
           "disponible junto con 0361 — sin rotacion ni carga axial — y sigue "
           "sin ser piso limpio por el agarre firme."),

    E("2363", "wide-grip chest dip on high parallel bars", "standing",
      standing=True, grip="firm",
      stress=js(sh="high", el="high", wr="moderate", cerv="low"),
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
      why="CUARTA entrada de la familia de fondos y CUARTA correccion del "
           "mismo error de E1 (horizontal_push → vertical_push). El agarre "
           "ancho con inclinacion hacia adelante abre mas el hombro que "
           "2462/1430, pero no cambia ninguna restriccion — ya estaban todas "
           "a contra."),

    E("1684", "dumbbell step up single leg balance with bicep curl",
      "standing", standing=True, bal="high", sl=True, grip="firm",
      impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", el="moderate", lumbar="moderate",
                ank="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "elbow_injury", "vertigo",
              "visual_impairment", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia",
            "elderly_65plus", "multiple_sclerosis", "obesity", "osteoporosis",
            "tendinitis_elbow"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff"],
      why="Subida al cajon con rodilla al pecho, equilibrio unipodal y curl "
           "arriba. Tercera aparicion de visual_impairment en "
           "contraindicaciones (tras 1374 y 0114): la constante es calcular la "
           "altura de una plataforma. Ya se puede generalizar — cualquier "
           "ejercicio con cajon o step debe llevarla."),

    E("0038", "barbell drag curl", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(el="moderate", sh="moderate", wr="high", lumbar="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "wrist_injury", "shoulder_impingement"],
      caut=["tendinitis_elbow", "carpal_tunnel", "lumbar_pain", "lumbar_disc",
            "rotator_cuff", "dysautonomia", "limited_balance", "hypertension",
            "elderly_65plus", "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Curl con la barra pegada al cuerpo: los codos viajan hacia ATRAS, "
           "o sea extension de hombro bajo carga. Eso lo diferencia de 0031 y "
           "0447 — shoulder_impingement pasa a contraindicacion en un "
           "ejercicio de biceps, y sh sube a moderate. Mantiene el problema de "
           "muneca de la barra recta."),

    E("0117", "barbell sumo deadlift", "standing", floor=True, standing=True,
      bal="moderate", grip="firm", axial="high", flex="moderate",
      stress=js(lumbar="high", hip="high", knee="high", wr="moderate",
                cerv="moderate", ank="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "hip_replacement",
              "knee_injury", "knee_replacement", "limited_grip",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cardiac",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "knee_pain", "osteoarthritis", "hypertension",
            "glaucoma", "retinal_detachment_risk", "obesity", "dysautonomia",
            "elderly_65plus", "wrist_injury", "cervical_injury", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "carpal_tunnel",
            "ankle_injury", "plantar_fasciitis"],
      why="La postura sumo abre la cadera en abduccion y rotacion externa "
           "maximas bajo carga: hip_replacement a contra por la posicion, no "
           "por el peso. Menos flexion lumbar que el peso muerto convencional "
           "—el torso queda mas vertical— pero la carga axial sigue siendo "
           "high y la columna sostiene todo en el despegue."),

    E("0835", "weighted hyperextension (on stability ball)", "prone",
      bal="moderate", grip="none", ext="high",
      stress=js(lumbar="high", cerv="moderate", hip="moderate"),
      pat="core_antiextension", diff=3, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "cannot_lie_prone", "limited_balance", "vertigo",
              "hernia_abdominal", "recent_abdominal_surgery",
              "multiple_sclerosis", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "neck_pain", "hip_pain",
            "hypertension", "obesity", "elderly_65plus",
            "pelvic_floor_dysfunction", "postpartum", "dysautonomia"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis"],
      why="Duodecima entrada de la familia pelota, y la unica en decubito "
           "prono. Extension lumbar cargada sobre superficie inestable: "
           "combina el riesgo de 1423 reverse hyper con el bloque de "
           "inestabilidad. spinal_extension high — es uno de los pocos "
           "ejercicios donde la lumbar se compromete por extension y no por "
           "flexion."),

    E("0856", "weighted svend press", "standing", standing=True, bal="low",
      grip="firm", stress=js(sh="moderate", el="moderate", wr="moderate",
                             lumbar="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="high",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "dysautonomia", "hypertension",
            "elderly_65plus", "rheumatoid_arthritis", "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "osteoporosis"],
      why="HALLAZGO: empuje horizontal DE PIE con solo tres "
           "contraindicaciones y 16 en safe_for. Presionar un disco entre las "
           "palmas y extender al frente mantiene el hombro en el plano medio, "
           "lejos del arco de pinzamiento — por eso shoulder_impingement queda "
           "en cautions, algo que ninguna flexion consigue. Complementa a "
           "0659 push-up (wall): los dos son empuje horizontal sin suelo, pero "
           "este permite progresar la carga."),

    E("1310", "weighted drop push up", "plank", floor=True, grip="firm",
      impact="high", stress=js(wr="high", sh="high", el="high",
                               lumbar="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="none", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="moderate", gripdur="moderate", temp="high",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "elbow_injury",
              "tendinitis_elbow", "cannot_get_on_floor", "cannot_lie_prone",
              "hypermobility", "osteoporosis", "rheumatoid_arthritis",
              "osteoarthritis", "recent_abdominal_surgery", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "obesity", "chronic_fatigue",
            "hernia_abdominal", "pelvic_floor_dysfunction", "hypertension",
            "cardiac"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis"],
      why="Flexion pliometrica con cambio de posicion de manos en el aire: "
           "impact high sobre la MUNECA, algo que solo aparece aqui y en "
           "1275 drop push up. La recepcion con las manos separadas es la "
           "posicion de mayor tension del hombro. artritis y artrosis a contra "
           "por el impacto articular repetido."),

    E("1751", "barbell pin presses", "bench_supine", grip="firm",
      stress=js(sh="moderate", el="high", wr="moderate"),
      pat="horizontal_push", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="high", metab="moderate",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "wrist_injury", "one_arm_only",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "tendinitis_elbow",
            "carpal_tunnel", "hypertension", "cardiac", "osteoporosis",
            "elderly_65plus", "glaucoma"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis"],
      why="TEXTO INCOHERENTE: dice 'stand facing the barbell' y a la vez "
           "'position yourself underneath it' y 'hold it above your chest'. No "
           "se puede estar de pie y debajo de la barra. El pin press es una "
           "variante de press en banco desde pines, asi que se clasifico como "
           "bench_supine. Confianza 0.60. Dato util del pin press real: el "
           "recorrido parcial (rom low) protege el hombro, por eso el "
           "pinzamiento queda en cautions."),
]

CONFIDENCE_OVERRIDES = {
    "1751": 0.60,  # el texto describe estar de pie y acostado a la vez
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
    print(f"lote 32: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
