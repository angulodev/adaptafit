#!/usr/bin/env python3
"""Lote 29 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1682", "ez bar seated close grip concentration curl", "seated",
      grip="firm", flex="low",
      stress=js(el="moderate", wr="moderate", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench",
              "cannot_sit_unsupported", "one_arm_only"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "dysautonomia", "rheumatoid_arthritis", "hip_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis", "lumbar_disc"],
      why="Curl de concentracion con barra EZ en vez de mancuerna: apoyar un "
           "codo en el muslo mientras la otra mano sostiene el otro extremo de "
           "la barra hace que one_arm_only pase a contraindicacion, al reves "
           "que en 1669 y 0403, donde estaba en safe_for. El implemento cambia "
           "el requisito de lateralidad."),

    E("3667", "side lying hip adduction (male)", "side_lying", floor=True,
      grip="none", lat="unilateral", sl=True,
      stress=js(hip="moderate", lumbar="low", knee="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_lie_on_side", "cannot_get_on_floor", "hip_replacement"],
      caut=["hip_pain", "si_joint_pain", "lumbar_pain", "osteoarthritis",
            "sciatica", "cervical_injury", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "dysautonomia",
            "lumbar_disc", "osteoporosis", "one_arm_only"],
      why="DOBLE PROBLEMA. (1) CORRECCION A E1: dijo supine, el texto dice "
           "'lie on your side' — tercer caso del mismo sesgo tras 0408 y 0613. "
           "(2) El nombre dice 'adduction' pero el texto dice 'lift your top "
           "leg', que es ABduccion — igual que en 1775. Es duplicado funcional "
           "de 1427 (lote 22). El brazo bajo la cabeza suma cervical a "
           "cautions, unica diferencia con 1427."),

    E("0699", "shoulder tap push-up", "plank", floor=True, bal="moderate",
      grip="none", lat="alternating",
      stress=js(wr="high", sh="high", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "cannot_get_on_floor", "cannot_lie_prone",
              "one_arm_only", "hypermobility", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "shoulder_pain", "lumbar_pain", "lumbar_disc",
            "si_joint_pain", "obesity", "elderly_65plus", "hernia_abdominal",
            "limited_balance", "chronic_fatigue"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis"],
      why="Combina la flexion completa con el toque de hombro de 3699/3239: "
           "cada repeticion termina con todo el peso en una muneca y un "
           "hombro. Mas duro que cualquiera de los dos por separado — diff 4 "
           "contra 3 de ambos. laxity high por la fase unilateral."),

    E("0981", "band jack knife sit-up", "supine", floor=True, oh=True,
      grip="light", flex="high",
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
      why="DUPLICADO FUNCIONAL DE 0969 (lote 28): V-up con banda sobre la "
           "cabeza. La unica diferencia textual es que 0969 alterna el cruce "
           "de piernas, lo que no mueve ninguna restriccion. Novena entrada de "
           "core_flexion y empatado con 0969 como la peor."),

    E("1367", "wide grip rear pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "cannot_stand", "one_arm_only", "hypermobility"],
      caut=["osteoporosis", "obesity", "elderly_65plus", "tendinitis_elbow",
            "rheumatoid_arthritis", "cervical_injury", "chronic_fatigue"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="CONFLICTO CON CONSECUENCIA REAL: el nombre dice 'rear' (barra detras "
           "de la nuca), que es una de las variantes mas lesivas de hombro y "
           "cuello que existen. El texto dice 'leading with your chest' — "
           "dominada normal. Se clasifico por el texto, o sea identico a 1429 "
           "wide grip pull-up. Si el nombre fuera correcto, cervical_injury "
           "deberia estar en contra. Va a E3 con prioridad: es un caso donde "
           "creerle al texto podria estar subestimando el riesgo."),

    E("1401", "muscle-up (on vertical bar)", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, ext="moderate",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "cannot_stand", "one_arm_only", "hypermobility",
              "lumbar_disc"],
      caut=["osteoporosis", "obesity", "elderly_65plus", "tendinitis_elbow",
            "cervical_injury", "chronic_fatigue", "rheumatoid_arthritis",
            "lumbar_pain"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="El nombre dice muscle-up pero el texto NO describe la transicion a "
           "fondo: termina con el pecho en la barra y los codos flexionados. "
           "Es una dominada al pecho con inclinacion hacia atras, como 0466 "
           "gironda. Por eso lumbar_disc a contra (hay arqueo en el aire) pero "
           "safe_for no queda vacio, a diferencia de 0558 y 3286 que si "
           "describen el muscle-up completo. Confianza 0.65."),

    E("0794", "standing lateral stretch", "standing", standing=True, bal="low",
      grip="none", flex="moderate", rot="low", lat="unilateral",
      stress=js(lumbar="moderate", sh="moderate", hip="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="high", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc",
              "shoulder_impingement"],
      caut=["lumbar_pain", "si_joint_pain", "sciatica", "osteoporosis",
            "rotator_cuff", "hypermobility", "dysautonomia", "vertigo",
            "limited_balance", "elderly_65plus", "hernia_abdominal"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="SEGUNDA FLEXION LATERAL del proyecto, tras 0407 dumbbell side bend "
           "(lote 22). Sin carga, asi que es mucho mas benigno, pero sigue "
           "sin haber campo que lo describa: quedo spinal_flexion moderate "
           "porque no existe spinal_lateral_flexion. Refuerza la propuesta de "
           "v1.3 — ya son dos casos, no uno."),

    E("3223", "star jump (male)", "standing", standing=True, bal="moderate",
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
      why="Casi identico a 3224 jack jump (lote 27), con una diferencia real: "
           "el salto es explosivo desde flexion de rodilla y los brazos se "
           "abren en cruz sin pasar sobre la cabeza. Por eso no_overhead queda "
           "en safe_for aca y en 3224 estaba en contra. El detalle de si los "
           "brazos suben o se abren decide una contraindicacion."),

    E("0386", "dumbbell rotation reverse fly", "standing", standing=True,
      bal="moderate", grip="firm", flex="moderate",
      stress=js(lumbar="high", sh="high", el="low", wr="moderate",
                hip="moderate"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "shoulder_impingement", "rotator_cuff",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_pain", "wrist_injury",
            "elbow_injury", "limited_balance", "hypertension", "obesity",
            "elderly_65plus", "osteoporosis", "dysautonomia", "hip_pain",
            "hypermobility"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "carpal_tunnel"],
      why="CUARTA VEZ que E1 clasifica una apertura posterior como "
           "horizontal_push (0993, 0378, 0383, 0386). Cuatro de cuatro. Este "
           "ademas rota los brazos a pronacion en el punto alto — la maniobra "
           "de 'lata vacia', que es la posicion de maximo pinzamiento: "
           "sh sube a high y rotator_cuff pasa a contra, unico de los cuatro "
           "rear fly donde ocurre."),

    E("0031", "barbell curl", "standing", standing=True, bal="low",
      grip="firm", axial="low",
      stress=js(el="moderate", wr="moderate", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "wrist_injury"],
      caut=["tendinitis_elbow", "carpal_tunnel", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "limited_balance", "hypertension",
            "elderly_65plus", "varicose_veins", "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="El curl con barra recta fija la muneca en supinacion completa, sin "
           "posibilidad de acomodar: wrist_injury a contra, a diferencia de "
           "todos los curls con mancuerna del proyecto, donde estaba en "
           "cautions. Es la razon clinica por la que existe la barra EZ. "
           "lumbar_disc en cautions y no en contra: de pie y erguido, la barra "
           "no genera voladizo."),

    E("0054", "barbell lunge", "standing", standing=True, bal="high", sl=True,
      grip="firm", axial="high", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="high", ank="moderate",
                cerv="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="moderate",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "lumbar_disc", "sciatica", "osteoporosis",
              "cervical_injury", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "obesity", "hypertension", "cardiac",
            "hernia_abdominal", "glaucoma", "retinal_detachment_risk"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement"],
      why="PRIMER EJERCICIO CON axial_spinal_load HIGH del proyecto. La barra "
           "sobre la espalda comprime la columna directamente: lumbar high, "
           "cervical moderate (la barra apoya sobre trapecio y C7), "
           "osteoporosis a contra y valsalva high. Frente a 1658 dumbbell "
           "lunge with curl, el mismo patron pero con la carga arriba suma "
           "cinco contraindicaciones nuevas de columna."),

    E("0095", "barbell shrug", "standing", standing=True, bal="low",
      grip="firm", axial="moderate",
      stress=js(cerv="high", lumbar="moderate", sh="moderate", wr="moderate"),
      pat="isolation", diff=2, rom="low",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "cervical_injury",
              "neck_pain", "wrist_injury"],
      caut=["osteoporosis", "lumbar_pain", "lumbar_disc", "shoulder_impingement",
            "carpal_tunnel", "hypertension", "dysautonomia", "elderly_65plus",
            "rheumatoid_arthritis", "migraine", "hernia_abdominal"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "rotator_cuff"],
      why="Unico ejercicio del proyecto con cervical_spine en high sin ser una "
           "inversion ni un crunch: la carga cuelga directamente de la "
           "cintura escapular y el cuello sostiene la tension. cervical_injury "
           "y neck_pain a contra. Curiosidad util: rotator_cuff en safe_for — "
           "el hombro solo se eleva, no rota ni se abduce."),

    E("0100", "barbell skier", "standing", standing=True, bal="moderate",
      grip="firm", axial="moderate", impact="moderate", flex="moderate",
      stress=js(lumbar="high", sh="moderate", knee="moderate", ank="moderate",
                wr="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="low",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "osteoporosis", "knee_injury",
              "ankle_injury", "hip_replacement", "limited_grip",
              "pelvic_floor_dysfunction", "hernia_abdominal",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "knee_pain", "shoulder_impingement",
            "hypertension", "cardiac", "obesity", "elderly_65plus",
            "chronic_fatigue", "dysautonomia", "plantar_fasciitis",
            "postpartum", "wrist_injury", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "carpal_tunnel", "rotator_cuff"],
      why="Bisagra explosiva con salto y tiron de barra: combina flexion de "
           "cadera cargada, impacto de aterrizaje y valsalva high. El "
           "componente balistico es lo que lo separa de un remo o un peso "
           "muerto — no hay control excentrico en la fase de vuelo, y la "
           "lumbar recibe el pico al recibir la barra."),

    E("0562", "landmine 180", "standing", standing=True, bal="moderate",
      grip="firm", rot="high", axial="low", lat="alternating",
      stress=js(lumbar="high", sh="moderate", hip="moderate", knee="low",
                wr="moderate"),
      pat="core_rotation", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="high", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "limited_grip",
              "hernia_abdominal", "recent_abdominal_surgery",
              "shoulder_impingement", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "rotator_cuff", "wrist_injury", "limited_balance",
            "hypertension", "obesity", "elderly_65plus", "dysautonomia",
            "vertigo", "pelvic_floor_dysfunction", "postpartum",
            "multiple_sclerosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "carpal_tunnel",
            "plantar_fasciitis"],
      why="Rotacion lumbar CARGADA y balistica de pie: el peor perfil de "
           "columna en rotacion del proyecto, por encima de 1419 y 0972. La "
           "barra describe un arco amplio con el peso lejos del eje, asi que "
           "el torque sobre el disco es maximo justo en el cambio de "
           "direccion. lumbar_pain a contra, no solo lumbar_disc."),

    E("0648", "power clean", "standing", floor=True, standing=True,
      bal="moderate", grip="firm", axial="high", impact="moderate",
      flex="moderate",
      stress=js(lumbar="high", knee="high", hip="high", sh="moderate",
                wr="high", ank="moderate", cerv="moderate", el="moderate"),
      pat="hinge", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "si_joint_pain", "osteoporosis",
              "knee_injury", "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "wrist_injury", "carpal_tunnel", "limited_grip",
              "shoulder_impingement", "rotator_cuff", "cervical_injury",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cardiac", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "hypermobility",
            "multiple_sclerosis", "vertigo", "hip_pain", "osteoarthritis"],
      safe=[],
      why="NOVENO safe_for vacio. Levantamiento olimpico completo: tira desde "
           "el suelo con la columna flexionada, acelera, se mete debajo de la "
           "barra y la recibe en posicion de sentadilla frontal. axial high, "
           "valsalva high, change high, metab high. 26 contraindicaciones. La "
           "muneca en hiperextension al recibir la barra es un detalle que "
           "suele pasarse por alto: wr high."),

    E("0786", "squat jerk", "standing", standing=True, bal="high", oh=True,
      grip="firm", axial="high", impact="moderate", sl=True,
      stress=js(sh="high", lumbar="high", knee="high", wr="high",
                el="moderate", hip="moderate", cerv="moderate", ank="moderate"),
      pat="vertical_push", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "lumbar_disc", "lumbar_pain", "sciatica", "osteoporosis",
              "knee_injury", "knee_replacement", "knee_pain",
              "hip_replacement", "ankle_injury", "wrist_injury",
              "carpal_tunnel", "limited_grip", "cervical_injury",
              "hernia_abdominal", "cardiac", "elderly_65plus", "vertigo",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "hypermobility",
            "multiple_sclerosis", "epilepsy", "hip_pain", "osteoarthritis",
            "pelvic_floor_dysfunction"],
      safe=[],
      why="DECIMO safe_for vacio y 27 contraindicaciones, segundo record "
           "detras de 1201 dumbbell burpee. Sentadilla completa MAS envion "
           "sobre la cabeza MAS recepcion en tijera. Es el unico "
           "vertical_push con axial_spinal_load high del proyecto — y sigue "
           "sin aparecer un piso de accesibilidad para ese patron."),

    E("0859", "wrist rollerer", "standing", standing=True, bal="low",
      grip="firm", stress=js(wr="high", sh="high", el="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="high", metab="moderate",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "wrist_injury", "carpal_tunnel",
              "limited_grip", "tendinitis_elbow", "shoulder_impingement"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "elbow_injury",
            "rotator_cuff", "dysautonomia", "hypertension", "elderly_65plus",
            "chronic_fatigue"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "lumbar_pain", "sciatica", "plantar_fasciitis"],
      why="Ejercicio de antebrazo que en realidad castiga el HOMBRO: mantener "
           "los brazos extendidos al frente durante todo el enrollado es un "
           "isometrico de deltoides anterior a 90 grados — sh high e iso high. "
           "shoulder_impingement a contra en un ejercicio catalogado como de "
           "antebrazos. Otro caso de mecanica sobre musculo objetivo."),

    E("0866", "weighted hanging leg-hip raise", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high", axial="low",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate",
                hip="moderate"),
      pat="core_flexion", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "lumbar_disc", "lumbar_pain", "sciatica", "cannot_stand",
              "one_arm_only", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hypermobility", "obesity", "elderly_65plus",
            "chronic_fatigue", "hypertension", "postpartum", "hip_pain",
            "rheumatoid_arthritis"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Version lastrada de 2333 (piernas rectas colgado): mismo perfil con "
           "diff 5. La cadena de suspension queda completa con cinco niveles "
           "reales — 0826 (paralelas, sin overhead) < 1764=2355 (rodillas) < "
           "2333 (rectas) < 0866 (lastrada), mas 1761 como rama con rotacion."),
]

CONFIDENCE_OVERRIDES = {
    "1367": 0.60,  # 'rear' implica tras la nuca; el texto describe pecho a la barra
    "1401": 0.65,  # el nombre dice muscle-up; el texto no describe la transicion
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
    print(f"lote 29: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
