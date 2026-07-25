#!/usr/bin/env python3
"""Lote 31 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1718", "barbell seated close grip behind neck triceps extension",
      "seated", oh=True, grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="moderate", wr="high",
                lumbar="low"),
      pat="isolation", diff=4, rom="high",
      ortho="moderate", change="low", valsalva="moderate", metab="low",
      laxity="high", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "shoulder_pain", "elbow_injury", "limited_grip", "wrist_injury",
              "cervical_injury", "hypermobility",
              "cannot_transfer_to_bench", "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "neck_pain", "hypertension", "osteoporosis",
            "dysautonomia", "carpal_tunnel", "elderly_65plus", "lumbar_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="Cuarta version del mismo gesto (2188, 0453, 0092, 1718) y la peor "
           "con diferencia: la barra parte DETRAS DEL CUELLO, no sobre la "
           "cabeza. Eso obliga a rotacion externa maxima con abduccion — "
           "laxity high, shoulder_pain e hypermobility a contra, y "
           "cervical_injury tambien porque el cuello se adelanta para dejar "
           "pasar la barra. diff 4 frente a 3 de las otras tres."),

    E("0858", "wind sprints", "standing", standing=True, bal="moderate",
      grip="none", impact="high", lat="alternating",
      stress=js(knee="high", ank="high", hip="high", lumbar="moderate"),
      pat="cardio_interval", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "hip_pain", "osteoporosis",
              "plantar_fasciitis", "pelvic_floor_dysfunction", "cardiac",
              "asthma", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["osteoarthritis", "lumbar_disc", "lumbar_pain", "si_joint_pain",
            "dysautonomia", "hypertension", "obesity", "chronic_fatigue",
            "multiple_sclerosis", "postpartum", "varicose_veins", "vertigo",
            "epilepsy"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Sprint a maxima velocidad: el cardio mas exigente del proyecto. "
           "asthma y cardiac pasan de cautions —donde estaban en los otros "
           "cinco cardios— a contraindicacion, porque el esfuerzo es maximo y "
           "no autorregulable. hip high por la zancada extendida, que es donde "
           "se rompen los isquiotibiales."),

    E("1472", "forward jump", "standing", standing=True, bal="high",
      grip="none", impact="high",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_interval", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", gripdur="none",
      temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "vertigo", "multiple_sclerosis",
              "elderly_65plus", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hip_pain", "osteoarthritis", "lumbar_disc", "lumbar_pain",
            "si_joint_pain", "dysautonomia", "hypertension", "cardiac",
            "obesity", "chronic_fatigue", "postpartum", "asthma", "epilepsy"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Salto horizontal encadenado: el desplazamiento hacia adelante "
           "obliga a frenar con la rodilla en cada aterrizaje, no solo a "
           "absorber verticalmente. bal high. Mismo bloque que 3223 y 1374, "
           "pero con el vector de fuerza en cizalla en vez de compresion."),

    E("3769", "curtsey squat", "standing", standing=True, bal="high", sl=True,
      grip="none", rot="low", impact="low", lat="alternating",
      stress=js(knee="high", hip="high", ank="moderate", lumbar="moderate"),
      pat="squat", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "si_joint_pain", "ankle_injury", "osteoarthritis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "sciatica",
            "dysautonomia", "vertigo", "elderly_65plus", "multiple_sclerosis",
            "obesity", "osteoporosis", "plantar_fasciitis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="El paso cruzado por detras lleva la cadera a ADUCCION con rotacion "
           "interna bajo carga — la triada que luxa una protesis, igual que en "
           "2466. hip_replacement y si_joint_pain a contra. Es la sentadilla "
           "con peor perfil de cadera del catalogo pese a no llevar peso."),

    E("3220", "astride jumps (male)", "standing", standing=True, bal="moderate",
      grip="none", impact="high", lat="bilateral",
      stress=js(knee="high", ank="high", sh="moderate", hip="moderate",
                lumbar="moderate"),
      pat="cardio_interval", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement",
              "osteoporosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
              "shoulder_impingement", "vertigo",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "rotator_cuff",
            "lumbar_pain", "lumbar_disc", "dysautonomia", "hypertension",
            "cardiac", "obesity", "elderly_65plus", "chronic_fatigue",
            "asthma", "varicose_veins", "multiple_sclerosis", "postpartum",
            "pregnancy_1st"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "elbow_injury", "no_overhead"],
      why="DUPLICADO FUNCIONAL DE 3223 star jump (lote 29): salto explosivo "
           "desde flexion con apertura de piernas y brazos en cruz. Igual que "
           "3223, los brazos se abren sin pasar sobre la cabeza, asi que "
           "no_overhead queda en safe_for."),

    E("3670", "weighted decline sit-up", "bench_supine", grip="firm",
      flex="high", axial="low",
      stress=js(lumbar="high", cerv="high", hip="moderate"),
      pat="core_flexion", diff=4, rom="high",
      ortho="none", change="moderate", headdown=True, valsalva="high",
      iso="low", metab="moderate", laxity="low", pelvic="high",
      gripdur="moderate", temp="low",
      contra=["lumbar_disc", "lumbar_pain", "sciatica", "cervical_injury",
              "neck_pain", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["si_joint_pain", "postpartum", "obesity", "elderly_65plus",
            "hypertension", "cardiac", "dysautonomia", "vertigo", "migraine",
            "limited_grip"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "cannot_get_on_floor"],
      why="EL PEOR core_flexion DEL CATALOGO. Acumula todo: declinado "
           "(head_below_heart y familia ocular), lastre (valsalva high), "
           "torso hasta la perpendicular (rango completo) y manos detras de la "
           "cabeza (cerv high). Decima entrada del patron y la unica con "
           "glaucoma en contraindicaciones."),

    E("0361", "dumbbell one arm shoulder press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low", lat="unilateral",
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
            "plantar_fasciitis", "one_arm_only"],
      why="EL MEJOR CANDIDATO A PISO DE vertical_push HASTA AHORA. Sin "
           "rotacion (a diferencia de 1012), sin carga axial (a diferencia de "
           "0786 y 3305), sin impulso de piernas (a diferencia de 1700): "
           "lumbar_disc baja a cautions, que es lo mejor que consigue el "
           "patron. Sigue sin ser un piso limpio porque exige agarre firme — "
           "limited_grip a contra. Un press con banda sin rotacion seguiria "
           "siendo mejor."),

    E("0114", "barbell step-up", "standing", standing=True, bal="high",
      sl=True, grip="firm", axial="high", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="high", ank="moderate",
                cerv="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="high", laxity="moderate", pelvic="moderate", gripdur="moderate",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "lumbar_disc", "sciatica", "osteoporosis",
              "cervical_injury", "limited_grip", "vertigo",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "dysautonomia", "elderly_65plus",
            "multiple_sclerosis", "obesity", "hypertension", "cardiac",
            "hernia_abdominal", "glaucoma", "visual_impairment"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement"],
      why="Subir a un cajon con barra sobre la espalda: mismo bloque axial que "
           "0054 barbell lunge mas la exigencia de calcular altura con carga "
           "encima. vertigo a contra y visual_impairment a cautions — segunda "
           "aparicion de la vision como factor, despues de 1374."),

    E("1651", "dumbbell bicep curl lunge with bowling motion", "standing",
      standing=True, bal="high", sl=True, grip="firm", rot="high",
      impact="low", lat="alternating",
      stress=js(knee="high", lumbar="high", hip="moderate", el="moderate",
                ank="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "elbow_injury", "lumbar_disc",
              "sciatica", "si_joint_pain",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "osteoarthritis", "plantar_fasciitis",
            "dysautonomia", "vertigo", "elderly_65plus", "multiple_sclerosis",
            "obesity", "osteoporosis", "tendinitis_elbow", "hernia_abdominal"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff"],
      why="Cuarto compuesto de la serie de zancadas y el mas cargado: suma "
           "rotacion de torso EN EL FONDO de la zancada, que es donde la "
           "cadera esta menos estable. Frente a 0336 (base), agrega el filtro "
           "de agarre del curl y el de columna de la rotacion: lumbar_disc y "
           "si_joint_pain a contra."),

    E("3007", "resistance band leg extension", "standing", standing=True,
      bal="moderate", sl=True, grip="none",
      stress=js(knee="moderate", hip="low", ank="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "knee_replacement"],
      caut=["knee_injury", "knee_pain", "osteoarthritis", "hip_pain",
            "dysautonomia", "vertigo", "elderly_65plus", "multiple_sclerosis",
            "ankle_injury", "plantar_fasciitis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "lumbar_pain", "sciatica", "osteoporosis",
            "hip_replacement", "hernia_abdominal"],
      why="19 en safe_for y solo cuatro contraindicaciones: es el ejercicio de "
           "PIERNA mas accesible del proyecto, muy por encima de cualquier "
           "sentadilla o zancada. La banda en el tobillo aisla el cuadriceps "
           "sin carga axial ni impacto, asi que knee_injury queda en cautions "
           "—no contra— y hasta hip_replacement entra en safe_for. Cubre "
           "parcialmente el hueco senalado en el lote 30: el tren inferior "
           "tenia techo de rodilla en todos los patrones de pie."),

    E("3305", "barbell thruster", "standing", standing=True, bal="moderate",
      oh=True, grip="firm", axial="high",
      stress=js(knee="high", sh="high", lumbar="high", wr="moderate",
                hip="moderate", cerv="moderate", el="moderate"),
      pat="vertical_push", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "lumbar_disc",
              "lumbar_pain", "sciatica", "osteoporosis", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "cervical_injury", "limited_grip", "cardiac",
              "hernia_abdominal", "pelvic_floor_dysfunction", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "vertigo", "wrist_injury",
            "ankle_injury", "multiple_sclerosis", "asthma"],
      safe=[],
      why="DECIMOTERCER safe_for vacio. Sentadilla completa encadenada con "
           "press sobre la cabeza, sin pausa: axial high, valsalva high, "
           "metab high y change high. Es el 0786 squat jerk sin la recepcion "
           "en tijera — algo mas simple tecnicamente, igual de excluyente."),

    E("3313", "weighted straight bar dip", "standing", standing=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", wr="moderate", cerv="low"),
      pat="vertical_push", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "wrist_injury", "elbow_injury",
              "tendinitis_elbow", "hypermobility", "cannot_stand",
              "one_arm_only", "osteoporosis", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["carpal_tunnel", "cervical_injury", "obesity", "hypertension",
            "cardiac", "chronic_fatigue", "rheumatoid_arthritis", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "plantar_fasciitis"],
      why="CORRECCION A E1: dijo horizontal_push, pero los fondos son "
           "vertical_push — el cuerpo se desplaza en vertical y el hombro "
           "trabaja en el plano sagital. Mismo criterio ya aplicado a 2462 y "
           "1430. Tercera entrada de la familia de fondos y la unica lastrada: "
           "el peso extra sube valsalva a high y saca osteoporosis y mayores "
           "de 65 a contraindicacion."),

    E("0041", "barbell front raise", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(sh="high", lumbar="moderate", wr="moderate", el="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip",
              "wrist_injury"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury", "lumbar_pain", "lumbar_disc", "carpal_tunnel"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "osteoporosis"],
      why="Version con barra de 0978 band front raise y 0376. La barra obliga "
           "a pronacion fija de las dos munecas a la vez y aleja el peso del "
           "cuerpo, lo que suma torque lumbar: wrist_injury a contra y "
           "lumbar_disc a cautions, ninguno de los cuales aparece en la "
           "version con banda. Tercera confirmacion del criterio de barra "
           "recta."),

    E("0044", "barbell good morning", "standing", standing=True, bal="moderate",
      grip="firm", axial="high", flex="moderate",
      stress=js(lumbar="high", hip="high", knee="moderate", cerv="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="moderate",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "hip_replacement",
              "cervical_injury", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "limited_grip", "limited_balance", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "knee_pain", "hypertension", "cardiac", "glaucoma",
            "retinal_detachment_risk", "obesity", "dysautonomia", "vertigo",
            "hypermobility", "postpartum", "osteoarthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "ankle_injury", "plantar_fasciitis"],
      why="EL PEOR PERFIL LUMBAR DEL CATALOGO junto con 0648. Barra sobre la "
           "espalda MAS torso hasta la horizontal: la carga axial actua en el "
           "extremo de un brazo de palanca de medio cuerpo. valsalva high y "
           "pelvic high. Es 1010 band straight leg deadlift con carga axial en "
           "vez de resistencia elastica — y esa diferencia agrega ocho "
           "contraindicaciones."),

    E("0102", "barbell squat (on knees)", "kneeling", floor=True, grip="firm",
      axial="high",
      stress=js(knee="high", lumbar="high", hip="moderate", cerv="moderate",
                ank="moderate"),
      pat="squat", diff=4, rom="moderate",
      ortho="none", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="moderate",
      temp="moderate",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "knee_pain", "osteoarthritis",
              "hip_replacement", "osteoporosis", "lumbar_disc", "lumbar_pain",
              "sciatica", "cervical_injury", "limited_grip", "ankle_injury",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "hypertension", "cardiac", "glaucoma",
            "retinal_detachment_risk", "obesity", "elderly_65plus",
            "dysautonomia", "hernia_abdominal", "rheumatoid_arthritis",
            "plantar_fasciitis"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "wrist_injury",
            "carpal_tunnel", "shoulder_impingement", "rotator_cuff",
            "elbow_injury"],
      why="Version sin salto de 1420 kneeling jump squat. Sin el componente "
           "balistico el safe_for deja de estar vacio, pero sigue siendo "
           "arrodillarse con barra sobre la espalda: rotula bajo carga axial "
           "contra el suelo. Curiosidad: cannot_stand en safe_for — es de los "
           "poquisimos ejercicios de pierna con carga que no exigen "
           "sostenerse erguido."),

    E("0112", "barbell standing twist", "standing", standing=True, bal="low",
      grip="firm", rot="high", axial="low", lat="alternating",
      stress=js(lumbar="high", sh="moderate", hip="moderate", wr="low"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "limited_grip",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "shoulder_impingement", "hypertension", "obesity",
            "elderly_65plus", "dysautonomia", "vertigo",
            "pelvic_floor_dysfunction", "postpartum", "hypermobility",
            "knee_pain"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "ankle_injury", "hip_replacement", "wrist_injury",
            "carpal_tunnel", "plantar_fasciitis"],
      why="Rotacion lumbar con barra al pecho. Menos agresivo que 0562 "
           "landmine 180 —no es balistico ni describe arco amplio— pero "
           "mantiene todo el bloque de contraindicaciones de columna en "
           "rotacion. Quinto ejercicio de rotacion cargada del proyecto: "
           "0407, 0562, 0777, 1007, 0112. Ninguno apto para hernia discal."),

    E("0120", "barbell upright row", "standing", standing=True, bal="low",
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
      why="CORRECCION A E1: dijo horizontal_pull, pero la barra viaja en "
           "VERTICAL pegada al cuerpo — es vertical_pull. Ademas es el "
           "ejercicio clasicamente senalado como productor de pinzamiento: "
           "abduccion con rotacion INTERNA, exactamente el gesto que cierra el "
           "espacio subacromial. laxity high. La muneca en desviacion cubital "
           "forzada lo saca tambien para tunel carpiano."),

    E("0447", "ez barbell curl", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(el="moderate", wr="moderate", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "lumbar_disc", "dysautonomia", "limited_balance", "hypertension",
            "elderly_65plus", "varicose_veins", "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Par directo de 0031 barbell curl (lote 29), identico salvo el "
           "implemento. La barra EZ permite semipronacion, asi que "
           "wrist_injury baja de contraindicacion a precaucion. Confirma por "
           "cuarta vez el criterio de la barra: mancuerna < EZ < recta."),
]

CONFIDENCE_OVERRIDES = {}

for _e in BATCH:
    if _e["exercise_id"] in CONFIDENCE_OVERRIDES:
        _e["confidence"] = CONFIDENCE_OVERRIDES[_e["exercise_id"]]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 31: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
