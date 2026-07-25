#!/usr/bin/env python3
"""Lote 34 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("3203", "prisoner half sit-up (male)", "supine", floor=True, grip="none",
      flex="high", stress=js(lumbar="high", cerv="high", hip="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="high", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "cervical_injury", "neck_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cannot_get_on_floor",
              "cannot_lie_supine", "shoulder_impingement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "postpartum", "obesity",
            "elderly_65plus", "migraine", "hypertension", "rotator_cuff"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "dysautonomia"],
      why="DUPLICADO FUNCIONAL DE 3202 (lote 24) con un matiz que si cuenta: "
           "'elbows pointing outwards' es la posicion de prisionero, que "
           "ademas de traccionar el cuello mantiene los hombros en abduccion "
           "y rotacion externa sostenida. shoulder_impingement pasa a "
           "contraindicacion — unico de la familia de sit-ups donde ocurre."),

    E("0253", "chin-ups (narrow parallel grip)", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(el="high", sh="moderate", wr="low"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "elbow_injury",
              "tendinitis_elbow", "cannot_stand", "one_arm_only"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "wrist_injury", "carpal_tunnel", "hypermobility", "osteoporosis",
            "obesity", "elderly_65plus", "rheumatoid_arthritis",
            "cervical_injury", "chronic_fatigue"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="LA DOMINADA MAS AMABLE DE TODA LA FAMILIA. El agarre NEUTRO y "
           "cerrado es mas favorable aun que el supinado de 1327: la muneca "
           "queda en posicion media (wr low, unica de las nueve entradas) y "
           "el hombro trabaja en el plano escapular. wrist_injury y "
           "carpal_tunnel bajan a cautions, cuando en el resto de la familia "
           "son contraindicacion. Es la sustitucion obligada de cualquier "
           "dominada para munecas sensibles."),

    E("0413", "dumbbell squat", "standing", standing=True, bal="moderate",
      grip="firm", stress=js(knee="high", hip="moderate", lumbar="moderate",
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
      why="Sentadilla a rango completo con mancuernas a los lados. Frente a "
           "3221 half knee bends —mismo patron, rango parcial— la profundidad "
           "sube knee_injury y hip_replacement de cautions a contraindicacion. "
           "Es la demostracion directa de que en el patron squat el RANGO "
           "decide mas que la carga."),

    E("1473", "backward jump", "standing", standing=True, bal="high",
      grip="none", impact="high",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_interval", diff=4, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "vertigo", "visual_impairment",
              "multiple_sclerosis", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "osteoarthritis", "lumbar_pain", "lumbar_disc",
            "si_joint_pain", "dysautonomia", "hypertension", "cardiac",
            "obesity", "chronic_fatigue", "postpartum", "asthma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Saltar HACIA ATRAS sin ver donde se aterriza: visual_impairment a "
           "contraindicacion por un motivo distinto al de los cajones — aqui "
           "no hay que calcular altura, sino que no se ve el destino en "
           "absoluto. Quinta aparicion del campo, y la primera que no depende "
           "de una plataforma."),

    E("0332", "dumbbell iron cross", "standing", standing=True, bal="low",
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
      why="Elevacion lateral con otro nombre. Duplicado funcional de 0334 y "
           "0376 (lote 17). El nombre 'iron cross' sugiere el elemento "
           "gimnastico de anillas, que no tiene nada que ver — otro caso de "
           "nombre que promete algo que el texto no describe."),

    E("0334", "dumbbell lateral raise", "standing", standing=True, bal="low",
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
      why="La entrada canonica de la elevacion lateral, identica a 0332 y "
           "0376. Tres nombres para el mismo ejercicio. El arco de 60 a 120 "
           "grados de abduccion es el del pinzamiento, por eso el hombro sale "
           "a contra pese a que el peso nunca pasa de la altura de los "
           "hombros — no_overhead en safe_for."),

    E("0666", "raise single arm push-up", "plank", floor=True, bal="moderate",
      grip="none", lat="unilateral",
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
      why="TERCER duplicado del grupo arquero (3294, 0725, 0666): flexion con "
           "un brazo extendido al costado. La unica diferencia es que este "
           "mantiene el brazo extendido durante toda la repeticion en vez de "
           "alternarlo, lo que no cambia ninguna restriccion."),

    E("1664", "dumbbell high curl", "standing", standing=True, bal="low",
      grip="firm", stress=js(el="moderate", sh="moderate", wr="low",
                             lumbar="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury"],
      caut=["tendinitis_elbow", "shoulder_impingement", "wrist_injury",
            "carpal_tunnel", "lumbar_pain", "dysautonomia", "limited_balance",
            "hypertension", "elderly_65plus", "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "rotator_cuff", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "lumbar_disc", "sciatica", "plantar_fasciitis"],
      why="Curl llevado 'lo mas alto posible': el final del recorrido "
           "incorpora flexion de hombro, por eso sh sube a moderate y "
           "shoulder_impingement entra en cautions. Menos agresivo que 0038 "
           "drag curl —donde el hombro va en extension y sale a contra— pero "
           "mas que un curl estandar."),

    E("1167", "dynamic chest stretch (male)", "standing", standing=True,
      bal="low", grip="none", stress=js(sh="moderate", el="low", cerv="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="moderate", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement"],
      caut=["rotator_cuff", "shoulder_pain", "hypermobility", "elbow_injury",
            "cervical_injury", "dysautonomia", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "lumbar_pain",
            "sciatica", "plantar_fasciitis", "osteoporosis",
            "hernia_abdominal", "pregnancy_1st", "pregnancy_2nd",
            "pregnancy_3rd"],
      why="22 en safe_for. Duplicado funcional de 1405 back pec stretch, con "
           "la diferencia de que aqui los brazos se cruzan al frente sin "
           "elevarse, asi que ortho baja a moderate. Igual que 1405, "
           "shoulder_impingement a contra: cruzar los brazos es aduccion "
           "horizontal, la maniobra de provocacion del pinzamiento."),

    E("3636", "high knee against wall", "standing", standing=True,
      bal="low", grip="none", impact="moderate", lat="alternating",
      stress=js(knee="moderate", hip="moderate", ank="moderate",
                lumbar="low", sh="low"),
      pat="cardio_steady", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="high",
      laxity="low", pelvic="moderate", gripdur="none", temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_replacement",
              "hip_replacement"],
      caut=["knee_injury", "knee_pain", "osteoarthritis", "hip_pain",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "dysautonomia", "hypertension", "cardiac", "obesity",
            "elderly_65plus", "chronic_fatigue", "asthma", "osteoporosis",
            "pelvic_floor_dysfunction", "multiple_sclerosis", "postpartum",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "lumbar_disc",
            "lumbar_pain", "sciatica"],
      why="EL CARDIO MAS ACCESIBLE, POR ENCIMA DE 3672. Las manos apoyadas en "
           "la pared aportan un tercer punto de apoyo: limited_balance baja de "
           "contraindicacion —donde esta en los siete cardios anteriores— a "
           "precaucion, y bal queda en low pese al movimiento rapido. Ademas "
           "el pie de apoyo nunca despega, asi que impact baja a moderate. "
           "15 en safe_for."),

    E("0078", "barbell rear lunge", "standing", standing=True, bal="high",
      sl=True, grip="firm", axial="high", impact="low", lat="unilateral",
      stress=js(knee="high", hip="moderate", lumbar="high", ank="moderate",
                cerv="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "lumbar_disc", "sciatica", "osteoporosis",
              "cervical_injury", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "obesity", "hypertension", "cardiac",
            "hernia_abdominal", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement"],
      why="Zancada hacia ATRAS con barra. La direccion del paso reduce el "
           "estres de rodilla frente a la zancada frontal —el peso queda sobre "
           "la pierna adelantada, que no se desplaza— pero con carga axial el "
           "bloque de contraindicaciones es identico a 0054. Duplicado "
           "funcional a efectos del motor."),

    E("0085", "barbell romanian deadlift", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", flex="moderate",
      stress=js(lumbar="high", hip="high", knee="moderate", cerv="moderate",
                wr="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "hip_replacement",
              "limited_grip", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "knee_pain", "hypertension", "cardiac", "glaucoma",
            "retinal_detachment_risk", "obesity", "dysautonomia",
            "elderly_65plus", "wrist_injury", "cervical_injury",
            "hypermobility", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "carpal_tunnel",
            "ankle_injury", "plantar_fasciitis"],
      why="Bisagra con barra y rodillas semiflexionadas. Menos extremo que "
           "0044 good morning —la barra cuelga de las manos en vez de apoyarse "
           "en la espalda, asi que el brazo de palanca es menor— pero mantiene "
           "carga axial alta y el mismo bloque lumbar. La familia de bisagras "
           "cargadas no tiene ninguna entrada apta para hernia discal."),

    E("0574", "lever bent over row", "standing", standing=True, bal="moderate",
      grip="firm", flex="moderate",
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
      why="Duplicado funcional de 0076 (lote 33): el nombre dice 'lever' pero "
           "el equipamiento es barra y el texto describe un remo inclinado "
           "comun. La familia de remos de pie ya tiene cinco entradas (1330, "
           "1773, 3017, 0076, 0574) con el mismo problema estructural: torso "
           "en voladizo, lumbar_disc a contra sin excepcion."),

    E("0989", "band one arm twisting chest press", "standing", standing=True,
      bal="moderate", grip="light", rot="moderate", lat="unilateral",
      stress=js(sh="moderate", el="moderate", lumbar="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "shoulder_impingement"],
      caut=["rotator_cuff", "shoulder_pain", "elbow_injury", "lumbar_pain",
            "si_joint_pain", "limited_grip", "limited_balance",
            "dysautonomia", "hypertension", "elderly_65plus", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "one_arm_only"],
      why="Empuje horizontal con banda, de pie y a un brazo. Mismo problema "
           "que 1012 en vertical_push: la ROTACION del torso mete lumbar_disc "
           "y sciatica a contraindicacion en un ejercicio que por lo demas "
           "seria muy accesible. El patron se repite — las versiones con banda "
           "del dataset tienden a incluir giro, y eso arruina su accesibilidad "
           "justo en el eje donde mas valen."),

    E("1370", "barbell floor calf raise", "standing", standing=True,
      bal="moderate", grip="none", axial="low",
      stress=js(ank="high", knee="low", hip="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis", "limited_balance"],
      caut=["knee_pain", "osteoarthritis", "dysautonomia", "vertigo",
            "elderly_65plus", "hip_replacement", "varicose_veins",
            "multiple_sclerosis", "osteoporosis"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "lumbar_disc", "lumbar_pain", "sciatica", "cannot_get_on_floor",
            "cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "hernia_abdominal",
            "knee_injury"],
      why="Elevacion de talones sobre el borde de una barra en el suelo: el "
           "rango completo con el talon por debajo del antepie sube ank a high "
           "y saca plantar_fasciitis a contraindicacion, a diferencia de 1397 "
           "standing calves (lote 18), donde estaba en cautions. 18 en "
           "safe_for igual — el resto del cuerpo no participa."),

    E("1767", "weighted triceps dip on high parallel bars", "standing",
      standing=True, grip="firm", axial="low",
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
      why="QUINTA correccion identica en la familia de fondos: E1 dijo "
           "horizontal_push, es vertical_push (2462, 1430, 3313, 2363, 1767). "
           "Duplicado funcional de 3313. El sesgo esta cerrado — cinco de "
           "cinco."),

    E("2987", "weighted close grip chin-up on dip cage", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, axial="low",
      stress=js(el="high", sh="moderate", wr="low"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="low",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "elbow_injury",
              "tendinitis_elbow", "cannot_stand", "one_arm_only",
              "osteoporosis", "elderly_65plus", "hypermobility",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "wrist_injury", "carpal_tunnel", "obesity", "chronic_fatigue",
            "cervical_injury", "hypertension", "glaucoma",
            "rheumatoid_arthritis"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="CORRECCION A E1 DE TIPO NUEVO: dijo horizontal_push para un "
           "CHIN-UP. No encaja en ninguno de los seis sesgos ya catalogados — "
           "probablemente arrastro el 'dip cage' del nombre. Es un aviso util: "
           "los sesgos identificados cubren la mayoria de los casos, pero no "
           "todos, y E3 no puede confiar solo en las busquedas por patron."),

    E("3641", "weighted kneeling step with swing", "kneeling", floor=True,
      oh=True, grip="firm", ext="moderate",
      stress=js(sh="high", lumbar="high", knee="high", el="moderate",
                cerv="moderate"),
      pat="vertical_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "knee_pain", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "lumbar_disc", "lumbar_pain", "limited_grip", "hypermobility",
              "osteoporosis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["osteoarthritis", "cervical_injury", "sciatica", "hip_pain",
            "elbow_injury", "elderly_65plus", "hypertension", "dysautonomia",
            "hernia_abdominal", "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "ankle_injury",
            "plantar_fasciitis", "carpal_tunnel"],
      why="Balanceo de pesos hasta sobre la cabeza, de rodillas y con los "
           "brazos rectos: el impulso lleva el hombro a flexion maxima sin "
           "control excentrico —laxity high— y la lumbar se arquea para "
           "acompanar. Combina el bloque de rodilla del arrodillado con el de "
           "hombro del overhead. Solo 5 en safe_for."),
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
    print(f"lote 34: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
