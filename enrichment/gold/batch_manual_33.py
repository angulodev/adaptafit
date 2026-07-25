#!/usr/bin/env python3
"""Lote 33 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("2801", "twisted leg raise (female)", "supine", floor=True, grip="none",
      flex="high", rot="high", lat="alternating",
      stress=js(lumbar="high", hip="high", cerv="low"),
      pat="core_rotation", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="none",
      temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cannot_get_on_floor",
              "cannot_lie_supine", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "postpartum", "obesity",
            "elderly_65plus", "hypertension", "fibromyalgia"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "ankle_injury", "plantar_fasciitis", "dysautonomia"],
      why="Version con rodillas flexionadas de 2802 (lote 23), que las lleva "
           "rectas. El brazo de palanca es menor —diff 3 frente a 4— pero la "
           "rotacion sigue siendo el factor dominante: mismo bloque de "
           "contraindicaciones lumbares. hip_replacement a contra por la "
           "rodilla al hombro contrario, que es flexion con aduccion."),

    E("0333", "dumbbell kickback", "standing", standing=True, bal="moderate",
      grip="firm", flex="moderate",
      stress=js(lumbar="high", el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="low", laxity="low", pelvic="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "tendinitis_elbow", "limited_balance", "hypertension", "obesity",
            "elderly_65plus", "osteoporosis", "dysautonomia", "hip_pain"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "wrist_injury", "carpal_tunnel"],
      why="Version de pie de 1730 y 1737 (lote 28). Diferencia relevante: el "
           "texto dice 'hinge forward' sin especificar hasta la horizontal, "
           "asi que head_below_heart queda en false y desaparece toda la "
           "familia ocular que si tenian los sentados. El voladizo lumbar se "
           "mantiene."),

    E("0431", "dumbbell step-up", "standing", standing=True, bal="high",
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
            "elderly_65plus", "multiple_sclerosis", "obesity", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Primera aplicacion de la regla derivada en el lote 32: todo "
           "ejercicio con cajon o plataforma lleva visual_impairment en "
           "contraindicaciones. Cuarto caso (1374, 0114, 1684, 0431). Version "
           "sin carga axial de 0114 barbell step-up: sin la barra sobre la "
           "espalda desaparecen lumbar_disc, osteoporosis y cervical_injury de "
           "las contraindicaciones."),

    E("2368", "split squats", "standing", standing=True, bal="high", sl=True,
      grip="none", stress=js(knee="high", hip="moderate", ank="moderate",
                             lumbar="low"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "pregnancy_3rd"],
      caut=["hip_pain", "osteoarthritis", "lumbar_pain", "si_joint_pain",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "obesity", "osteoporosis", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "sciatica"],
      why="Zancada ESTATICA: los pies no se mueven entre repeticiones, asi que "
           "position_change baja a low y desaparece el componente de "
           "desplazamiento. Es la version mas conservadora del patron lunge y "
           "la unica con lumbar_disc y sciatica en safe_for — util como "
           "regresion de 0336 y de todas las zancadas cargadas."),

    E("1297", "isometric chest squeeze", "standing", standing=True, bal="low",
      grip="none", stress=js(sh="moderate", el="low", wr="low", lumbar="low"),
      pat="horizontal_push", diff=1, rom="low",
      ortho="moderate", change="none", valsalva="moderate", iso="high",
      metab="low", laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "hypertension", "cardiac", "dysautonomia", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury", "one_arm_only",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "lumbar_pain", "sciatica", "plantar_fasciitis",
            "osteoporosis", "hernia_abdominal",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      why="NUEVO MEJOR EMPUJE HORIZONTAL ACCESIBLE: 25 en safe_for y DOS "
           "contraindicaciones, solo las de bipedestacion. Supera a 0659 "
           "push-up (wall) —que tenia 15— y a 0856 svend press. Sin "
           "equipamiento, sin agarre, sin suelo, sin pared, sin recorrido "
           "articular: es contraccion isometrica pura. valsalva moderate "
           "porque apretar fuerte tiende a la apnea; conviene advertirlo. "
           "Tercero del ranking absoluto del proyecto."),

    E("3216", "chest tap push-up (male)", "plank", floor=True, bal="moderate",
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
      why="DUPLICADO FUNCIONAL DE 0699 shoulder tap push-up (lote 29): la "
           "unica diferencia es donde se toca —pecho en vez de hombro— y el "
           "momento del ciclo, lo que no cambia ninguna restriccion. En ambos, "
           "la mano que se despega deja todo el peso en una muneca."),

    E("3221", "half knee bends (male)", "standing", standing=True, bal="low",
      grip="none", stress=js(knee="moderate", hip="moderate", ank="low",
                             lumbar="low"),
      pat="squat", diff=1, rom="low",
      ortho="high", change="low", valsalva="low", iso="low", metab="moderate",
      laxity="low", pelvic="low", gripdur="none", temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_replacement"],
      caut=["knee_injury", "knee_pain", "osteoarthritis", "hip_pain",
            "hip_replacement", "limited_balance", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "ankle_injury",
            "plantar_fasciitis", "obesity"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "lumbar_pain", "sciatica", "osteoporosis",
            "hernia_abdominal"],
      why="LA SENTADILLA ACCESIBLE QUE FALTABA. 18 en safe_for y tres "
           "contraindicaciones. El rango PARCIAL es lo que la separa de todas "
           "las demas: knee_injury y knee_pain bajan a cautions y "
           "hip_replacement tambien, porque la cadera no supera los 90 grados. "
           "Frente a 1476 one leg squat (diff 5, rodilla a contra) es el otro "
           "extremo del mismo patron. Tercer hallazgo seguido de tren inferior "
           "accesible, tras 3007 y 0628."),

    E("1003", "band squat row", "standing", standing=True, bal="moderate",
      grip="light", stress=js(knee="moderate", hip="moderate", sh="moderate",
                              el="moderate", lumbar="moderate"),
      pat="squat", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="moderate",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_replacement",
              "limited_balance"],
      caut=["knee_injury", "knee_pain", "osteoarthritis", "hip_pain",
            "hip_replacement", "shoulder_impingement", "elbow_injury",
            "lumbar_pain", "lumbar_disc", "dysautonomia", "elderly_65plus",
            "limited_grip", "obesity", "multiple_sclerosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "ankle_injury",
            "plantar_fasciitis", "osteoporosis", "sciatica"],
      why="Sentadilla combinada con remo elastico: el tiron de la banda al "
           "frente contrarresta el peso corporal hacia atras, lo que ayuda al "
           "equilibrio y reduce la exigencia de rodilla frente a una sentadilla "
           "libre. Buen ejemplo de un compuesto que resulta MENOS restrictivo "
           "que sus partes por separado."),

    E("1009", "band stiff leg deadlift", "standing", standing=True, bal="low",
      grip="light", flex="high",
      stress=js(lumbar="high", hip="high", knee="moderate"),
      pat="hinge", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "hernia_abdominal",
              "hip_replacement", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hypermobility", "knee_pain",
            "dysautonomia", "vertigo", "limited_balance", "elderly_65plus",
            "obesity", "limited_grip", "pelvic_floor_dysfunction", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "ankle_injury", "plantar_fasciitis"],
      why="DUPLICADO FUNCIONAL DE 1010 (lote 30): peso muerto a piernas rectas "
           "con banda. El texto solo difiere en donde se coloca la banda — "
           "tobillos en vez de pies — lo que no cambia nada. Mismo bloque de "
           "contraindicaciones lumbares."),

    E("0834", "weighted front raise", "standing", standing=True, bal="low",
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
      why="DUPLICADO EXACTO de 0310 (lote 32): el texto es identico palabra por "
           "palabra, solo cambia la etiqueta de equipamiento de 'dumbbell' a "
           "'weighted'. Clasificado igual. Es el caso mas claro de que el campo "
           "equipment del dataset no es fiable por si solo."),

    E("0844", "weighted round arm", "standing", standing=True, bal="moderate",
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
      why="QUINTA apertura posterior del proyecto (0993, 0378, 0383, 0386, "
           "0844) y duplicado funcional de 0378. E1 no le asigno "
           "movement_pattern esta vez — dejo el campo vacio en vez de "
           "equivocarse, lo que es preferible. Clasificado como "
           "horizontal_pull."),

    E("3017", "barbell pendlay row", "standing", standing=True, bal="moderate",
      grip="firm", flex="moderate", axial="moderate",
      stress=js(lumbar="high", sh="moderate", el="moderate", wr="moderate",
                hip="moderate"),
      pat="horizontal_pull", diff=4, rom="moderate",
      ortho="high", change="moderate", valsalva="high", iso="high",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "lumbar_pain", "sciatica", "si_joint_pain", "osteoporosis",
              "hernia_abdominal", "elbow_injury",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "limited_balance", "hypertension", "cardiac",
            "obesity", "elderly_65plus", "glaucoma", "dysautonomia",
            "hip_pain"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Remo con el torso mantenido cerca de la horizontal y barra pesada: "
           "iso high porque la lumbar sostiene la posicion toda la serie, y "
           "valsalva high por la carga. lumbar_pain a contra, no solo "
           "lumbar_disc — es mas exigente que 1330 y 1773 porque el peso es "
           "mayor y bilateral."),

    E("3116", "band fixed back underhand pulldown", "standing", standing=True,
      bal="low", oh=True, grip="light",
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
      why="CUARTA entrada del pulldown con banda (1013, 0974, 0983, 3116) y "
           "tercer duplicado exacto de 1013. El piso de accesibilidad de "
           "vertical_pull esta muy bien cubierto — cuatro entradas para lo que "
           "en la practica son dos ejercicios (de pie y de rodillas)."),

    E("3236", "resistance band hip thrusts on knees (female)", "kneeling",
      floor=True, grip="none", ext="moderate",
      stress=js(knee="high", hip="moderate", lumbar="moderate", ank="moderate"),
      pat="hinge", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "knee_pain", "osteoarthritis",
              "hip_replacement", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "hip_pain",
            "ankle_injury", "postpartum", "pelvic_floor_dysfunction",
            "hernia_abdominal", "elderly_65plus", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "plantar_fasciitis",
            "dysautonomia", "one_arm_only", "sciatica"],
      why="Octava entrada de la familia del puente y la unica de rodillas. El "
           "cambio de apoyo invierte el perfil respecto de 0668: desaparece "
           "cannot_get_on_floor como unico filtro y entra todo el bloque de "
           "rodilla, con 'feet flexed' cargando ademas el empeine. Mismo "
           "principio que 1660 en la familia pelota — el apoyo decide, no el "
           "movimiento."),

    E("3290", "weighted one hand pull up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, lat="unilateral", axial="low",
      stress=js(sh="high", el="high", wr="high", lumbar="moderate",
                cerv="moderate"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "cannot_stand", "hypermobility", "osteoporosis",
              "elderly_65plus", "cervical_injury", "rheumatoid_arthritis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "obesity", "chronic_fatigue",
            "glaucoma", "retinal_detachment_risk", "lumbar_pain", "neck_pain"],
      safe=[],
      why="DECIMOCUARTO safe_for vacio. Dominada a UNA MANO con lastre: todo "
           "el peso corporal mas el peso extra sobre un solo hombro, codo y "
           "muneca. Es el unico ejercicio del catalogo donde one_arm_only NO "
           "es contraindicacion —se hace con un brazo— pero tampoco es "
           "safe_for, porque exige una fuerza que ese perfil rara vez tiene. "
           "Se omitio de las tres listas a proposito."),

    E("3312", "weighted muscle up (on bar)", "hanging", oh=True,
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
      why="DECIMOQUINTO safe_for vacio y duplicado funcional de 3286 (lote "
           "28). A diferencia de 1401, este texto SI describe la transicion "
           "completa: 'push down with your hands and drive your elbows back, "
           "lifting your body above the bar'. Confirma el criterio del lote "
           "29 — cuando el texto describe el muscle-up real, safe_for queda "
           "vacio."),

    E("0076", "barbell rear delt row", "standing", standing=True,
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
            "wrist_injury", "carpal_tunnel", "limited_balance",
            "hypertension", "obesity", "elderly_65plus", "osteoporosis",
            "dysautonomia", "hip_pain"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Remo inclinado con barra, mas ligero que 3017 pendlay: el texto no "
           "exige devolver la barra al suelo ni mantener el torso tan bajo, "
           "asi que lumbar_pain baja a cautions y valsalva a moderate. "
           "Comparte con toda la familia de remos de pie el mismo problema: "
           "torso en voladizo, lumbar_disc a contra."),

    E("0854", "weighted standing hand squeeze", "standing", standing=True,
      bal="low", grip="firm", stress=js(wr="moderate", sh="moderate",
                                        el="low"),
      pat="isolation", diff=1, rom="low",
      ortho="high", change="none", valsalva="moderate", iso="high",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis",
            "osteoarthritis", "shoulder_impingement", "elbow_injury",
            "dysautonomia", "hypertension", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "osteoporosis",
            "hernia_abdominal"],
      why="Isometrico de antebrazo de pie: 17 en safe_for. Mismo problema que "
           "0859 wrist rollerer —sostener los brazos extendidos al frente carga "
           "el deltoides— pero aqui sin recorrido ni carga excentrica, asi que "
           "el hombro queda en moderate y el pinzamiento en cautions. La "
           "columna no participa en absoluto."),
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
    print(f"lote 33: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
