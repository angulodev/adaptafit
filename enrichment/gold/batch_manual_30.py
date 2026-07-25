#!/usr/bin/env python3
"""Lote 30 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0089", "barbell seated close-grip concentration curl", "seated",
      grip="firm", flex="low",
      stress=js(el="moderate", wr="high", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "wrist_injury",
              "cannot_transfer_to_bench", "cannot_sit_unsupported",
              "one_arm_only"],
      caut=["tendinitis_elbow", "carpal_tunnel", "lumbar_pain", "dysautonomia",
            "rheumatoid_arthritis", "hip_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis", "lumbar_disc"],
      why="Version con barra recta de 1682 (lote 29). Aplica el criterio "
           "fijado con 0031 barbell curl: la barra recta fija la muneca en "
           "supinacion sin margen de acomodacion, asi que wr sube a high y "
           "wrist_injury pasa a contraindicacion — en 1682 con barra EZ estaba "
           "en cautions."),

    E("0267", "crunch (hands overhead)", "supine", floor=True, oh=True,
      grip="none", flex="high",
      stress=js(lumbar="high", sh="moderate", cerv="low", hip="low"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "cannot_get_on_floor",
              "cannot_lie_supine", "no_overhead", "shoulder_impingement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "rotator_cuff",
            "pelvic_floor_dysfunction", "postpartum", "obesity",
            "elderly_65plus", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "wrist_injury",
            "carpal_tunnel", "plantar_fasciitis", "dysautonomia",
            "cervical_injury", "neck_pain"],
      why="INTERCAMBIO DE RESTRICCIONES. Los brazos extendidos sobre la cabeza "
           "alargan el brazo de palanca (diff 3 frente a 2 del crunch comun) y "
           "meten no_overhead y hombro a contraindicacion. Pero al no llevar "
           "las manos a la nuca, cervical_injury y neck_pain entran en "
           "safe_for. Es el unico crunch del suelo apto para lesion cervical — "
           "junto con 1005, que es de pie."),

    E("0336", "dumbbell lunge", "standing", standing=True, bal="high", sl=True,
      grip="firm", impact="low", lat="alternating",
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
      why="Zancada con mancuernas sin gesto adicional: es la base de la que "
           "1658 (con curl), 1688 (con rotacion) y 1732 (con extension "
           "overhead) son variantes. Sirve de referencia — cada gesto agregado "
           "suma su propio bloque de restricciones sobre este perfil."),

    E("0406", "dumbbell shrug", "standing", standing=True, bal="low",
      grip="firm", axial="moderate",
      stress=js(cerv="high", sh="moderate", lumbar="moderate", wr="low"),
      pat="isolation", diff=1, rom="low",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "cervical_injury",
              "neck_pain"],
      caut=["osteoporosis", "lumbar_pain", "lumbar_disc",
            "shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypertension", "dysautonomia", "elderly_65plus",
            "rheumatoid_arthritis", "migraine"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "rotator_cuff", "one_arm_only"],
      why="Version con mancuernas de 0095. Las mancuernas cuelgan a los lados "
           "en vez de por delante, asi que la muneca no soporta traccion "
           "asimetrica: wrist_injury baja de contra a cautions. El cuello "
           "sigue en high — es la carga colgando de la cintura escapular lo "
           "que lo pone ahi, no el implemento."),

    E("0777", "spell caster", "standing", standing=True, bal="moderate",
      grip="firm", flex="high", rot="high", lat="alternating",
      stress=js(lumbar="high", hip="moderate", sh="moderate", knee="low"),
      pat="core_rotation", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "limited_grip",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "shoulder_impingement", "limited_balance",
            "hypertension", "obesity", "elderly_65plus", "dysautonomia",
            "vertigo", "pelvic_floor_dysfunction", "postpartum",
            "hypermobility", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "carpal_tunnel",
            "plantar_fasciitis", "wrist_injury"],
      why="Flexion Y rotacion cargadas de pie a la vez, alcanzando el pie "
           "contrario: la combinacion que 3231 (flexion) y 0562 (rotacion) "
           "tienen por separado. Mismo bloque de contraindicaciones lumbares "
           "que el landmine 180, pero con menos carga — por eso lumbar_pain "
           "sigue en contra pero desaparece hip_replacement."),

    E("1489", "sissy squat", "standing", standing=True, bal="high", grip="none",
      stress=js(knee="high", hip="low", ank="moderate", lumbar="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "osteoarthritis",
              "ankle_injury", "hip_replacement", "plantar_fasciitis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity", "osteoporosis",
            "hypermobility", "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "lumbar_disc", "sciatica"],
      why="El texto se contradice: 'leaning back' es el gesto de la sentadilla "
           "sissy, pero 'push through your heels' es de la sentadilla comun — "
           "la sissy se hace sobre las puntas. Clasificado por el gesto que da "
           "nombre. Es el ejercicio con mayor cizalla de rodilla del catalogo: "
           "flexion maxima con el femur adelantado y sin contrapeso de cadera. "
           "laxity high por la tension del ligamento cruzado. Curiosidad: "
           "lumbar_disc en safe_for, la columna no participa."),

    E("3645", "single leg bridge with outstretched leg", "supine", floor=True,
      grip="none", ext="moderate", sl=True, lat="unilateral",
      stress=js(hip="high", lumbar="moderate", knee="moderate"),
      pat="hinge", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="high", metab="moderate",
      laxity="moderate", pelvic="moderate", gripdur="none", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "hip_replacement",
              "si_joint_pain", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "sciatica", "hip_pain",
            "postpartum", "pelvic_floor_dysfunction", "hernia_abdominal",
            "knee_pain", "osteoarthritis", "chronic_fatigue"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "ankle_injury", "plantar_fasciitis",
            "dysautonomia", "one_arm_only"],
      why="Septima entrada de la familia del puente. El apoyo unipodal duplica "
           "la carga sobre una cadera y mete torque frontal en la "
           "sacroiliaca: hip high, si_joint_pain y hip_replacement a contra — "
           "mismo salto que 1774 hizo sobre 0705 en el puente lateral. La "
           "escala de la familia queda: 1422 < 0668=3013 < 3561 < 3645 < 1409."),

    E("0476", "hanging straight twisting leg hip raise", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high", rot="high",
      lat="alternating",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate",
                hip="moderate"),
      pat="core_rotation", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "cannot_stand", "one_arm_only", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "osteoporosis", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "hypertension", "postpartum", "hip_pain", "rheumatoid_arthritis"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="El peor de la familia de suspension: piernas RECTAS elevadas MAS "
           "torsion, o sea 2333 y 1761 combinados. 21 contraindicaciones. Es "
           "la rama terminal de la cadena — no hay progresion por encima de "
           "esta salvo agregarle lastre."),

    E("0721", "side wrist pull stretch", "standing", standing=True, bal="low",
      grip="light", lat="unilateral",
      stress=js(wr="moderate", el="low", sh="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="moderate", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="low", temp="low",
      contra=["cannot_stand", "wheelchair", "wrist_injury", "one_arm_only"],
      caut=["carpal_tunnel", "rheumatoid_arthritis", "osteoarthritis",
            "elbow_injury", "tendinitis_elbow", "hypermobility",
            "shoulder_impingement", "dysautonomia"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "osteoporosis",
            "hernia_abdominal", "cervical_injury",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      why="21 en safe_for, cuarto del ranking absoluto. Estiramiento de "
           "antebrazo de pie, sin carga ni equipamiento. Coherente con el "
           "criterio de los otros estiramientos: como la traccion es sobre la "
           "muneca, wrist_injury va a contraindicacion — no es la excepcion, "
           "es la regla de que un estiramiento contraindica la estructura que "
           "estira. one_arm_only a contra: hace falta la otra mano para tirar."),

    E("3672", "back and forth step", "standing", standing=True, bal="moderate",
      sl=True, grip="none", impact="low", lat="alternating",
      stress=js(knee="moderate", hip="moderate", ank="moderate",
                lumbar="low"),
      pat="cardio_steady", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "lumbar_pain",
            "si_joint_pain", "dysautonomia", "vertigo", "hypertension",
            "cardiac", "obesity", "elderly_65plus", "chronic_fatigue",
            "multiple_sclerosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "osteoporosis"],
      why="EL CARDIO MAS ACCESIBLE DEL PROYECTO. Zancadas alternas sin salto: "
           "impact low frente al high de 0684, 3656, 3223 y 3224. Eso saca "
           "osteoporosis, plantar_fasciitis y suelo pelvico de "
           "contraindicaciones — quedan en cautions o safe_for. 15 en "
           "safe_for. Sigue exigiendo rodilla sana, que es el techo de "
           "cualquier cardio de pie."),

    E("0776", "snatch pull", "standing", floor=True, standing=True,
      bal="high", oh=True, grip="firm", axial="high", impact="moderate",
      flex="moderate",
      stress=js(lumbar="high", knee="high", hip="high", sh="high",
                wr="high", ank="moderate", cerv="moderate", el="moderate"),
      pat="hinge", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "si_joint_pain", "osteoporosis",
              "knee_injury", "knee_replacement", "knee_pain",
              "hip_replacement", "ankle_injury", "wrist_injury",
              "carpal_tunnel", "limited_grip", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "cervical_injury",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cardiac", "elderly_65plus",
              "hypermobility", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "multiple_sclerosis", "vertigo",
            "hip_pain", "osteoarthritis", "epilepsy"],
      safe=[],
      why="UNDECIMO safe_for vacio y NUEVO RECORD: 28 contraindicaciones, "
           "empatado con 1201 dumbbell burpee. Es el power clean con "
           "recepcion SOBRE LA CABEZA en sentadilla profunda: suma "
           "no_overhead y hombro a todo lo de 0648. El agarre ancho de arranque "
           "con recepcion overhead es la posicion de maxima exigencia de "
           "movilidad de hombro que existe — laxity high."),

    E("0980", "band bent-over hip extension", "standing", standing=True,
      bal="moderate", sl=True, grip="light", flex="moderate",
      lat="alternating",
      stress=js(lumbar="high", hip="moderate", knee="low", ank="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="low",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "sciatica", "hip_replacement", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "dysautonomia", "elderly_65plus", "osteoporosis", "obesity",
            "knee_pain", "multiple_sclerosis", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "ankle_injury",
            "plantar_fasciitis"],
      why="La banda hace el trabajo pero el torso queda inclinado y sostenido "
           "por la lumbar durante toda la serie — lumbar high pese a la carga "
           "minima. Confirma el criterio del lote 19: lo que decide la lumbar "
           "es el APOYO DEL TORSO, no el peso. Es la version de pie de "
           "0668/3013 y mucho menos accesible que ellos."),

    E("0983", "band kneeling one arm pulldown", "kneeling", floor=True,
      oh=True, grip="light", lat="unilateral",
      stress=js(sh="moderate", el="moderate", knee="high", lumbar="low"),
      pat="vertical_pull", diff=2, rom="high",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "pregnancy_3rd"],
      caut=["knee_pain", "osteoarthritis", "shoulder_pain", "elbow_injury",
            "hip_pain", "limited_grip", "elderly_65plus", "hypermobility",
            "cervical_injury", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "wrist_injury", "carpal_tunnel",
            "ankle_injury", "hip_replacement", "lumbar_disc", "lumbar_pain",
            "sciatica", "plantar_fasciitis", "dysautonomia", "one_arm_only",
            "osteoporosis"],
      why="Tercer pulldown con banda (1013, 0974, 0983) y el menos accesible "
           "de los tres: arrodillarse mete todo el bloque de Capa A de rodilla "
           "que los otros dos no tienen. Util igual — es el unico de los tres "
           "que NO exige estar de pie, asi que cubre a quien puede arrodillarse "
           "pero no sostenerse erguido."),

    E("1007", "band standing twisting crunch", "standing", standing=True,
      bal="low", grip="light", flex="high", rot="high", lat="alternating",
      stress=js(lumbar="high", sh="moderate", hip="low"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "si_joint_pain", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "pelvic_floor_dysfunction", "postpartum",
            "shoulder_impingement", "dysautonomia", "hypertension", "obesity",
            "elderly_65plus", "limited_grip", "hip_pain"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "cervical_injury", "neck_pain"],
      why="Version con rotacion de 1005 (lote 26). Igual que su hermano, no "
           "requiere suelo y tiene cervical_injury en safe_for. La rotacion "
           "agrega si_joint_pain a contraindicaciones. Con 1005 y 1007, el "
           "trabajo abdominal de pie ya cubre flexion y rotacion — util para "
           "cannot_get_on_floor, que antes no tenia nada de core."),

    E("1010", "band straight leg deadlift", "standing", standing=True,
      bal="low", grip="light", flex="high",
      stress=js(lumbar="high", hip="high", knee="moderate"),
      pat="hinge", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "hernia_abdominal",
              "hip_replacement", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hypermobility", "knee_pain",
            "dysautonomia", "vertigo", "limited_balance", "elderly_65plus",
            "obesity", "limited_grip", "pelvic_floor_dysfunction",
            "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "ankle_injury", "plantar_fasciitis"],
      why="Peso muerto a piernas rectas: mismo gesto que 3231 two toe touch, "
           "con resistencia. Flexion lumbar completa MAS traccion isquiotibial "
           "— osteoporosis y lumbar_pain a contra, no solo lumbar_disc. La "
           "banda no lo suaviza: la resistencia es maxima abajo, que es donde "
           "el disco esta mas comprometido."),

    E("1012", "band twisting overhead press", "standing", standing=True,
      bal="low", oh=True, grip="light", rot="moderate", lat="alternating",
      stress=js(sh="high", el="moderate", lumbar="moderate", wr="low",
                cerv="low"),
      pat="vertical_push", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="moderate",
      laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "lumbar_disc",
              "sciatica"],
      caut=["shoulder_pain", "elbow_injury", "lumbar_pain", "si_joint_pain",
            "cervical_injury", "hypermobility", "dysautonomia", "hypertension",
            "elderly_65plus", "limited_grip", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "plantar_fasciitis"],
      why="EL vertical_push MAS ACCESIBLE HASTA AHORA: diff 2, agarre ligero, "
           "sin carga axial, muneca y tunel carpiano en safe_for. Pero NO "
           "sirve como piso del patron, porque el giro del torso mete "
           "lumbar_disc y sciatica en contraindicaciones. Un press con banda "
           "SIN rotacion seria el candidato limpio — vale buscarlo "
           "explicitamente en los lotes restantes."),

    E("1374", "box jump down with one leg stabilization", "standing",
      standing=True, bal="high", sl=True, grip="none", impact="high",
      lat="unilateral",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_interval", diff=5, rom="high",
      ortho="high", change="high", valsalva="low", iso="moderate",
      metab="high", laxity="high", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "vertigo", "multiple_sclerosis",
              "visual_impairment", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "osteoarthritis", "lumbar_pain", "si_joint_pain",
            "dysautonomia", "hypertension", "cardiac", "obesity",
            "chronic_fatigue", "postpartum", "epilepsy", "asthma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff"],
      why="Salto a cajon con aterrizaje y estabilizacion en UNA pierna: "
           "impact high concentrado en un solo tobillo y una sola rodilla. "
           "visual_impairment a contraindicacion — es el primer ejercicio del "
           "proyecto donde no ver la altura del cajon es un riesgo directo de "
           "caida, no una incomodidad."),

    E("1420", "kneeling jump squat", "kneeling", floor=True, grip="firm",
      axial="high", impact="high",
      stress=js(knee="high", lumbar="high", ank="high", hip="moderate",
                cerv="moderate"),
      pat="squat", diff=5, rom="high",
      ortho="none", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="high", gripdur="moderate", temp="high",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "knee_pain", "osteoarthritis",
              "ankle_injury", "hip_replacement", "osteoporosis", "lumbar_disc",
              "lumbar_pain", "sciatica", "cervical_injury", "limited_grip",
              "pelvic_floor_dysfunction", "hernia_abdominal",
              "recent_abdominal_surgery", "cardiac", "elderly_65plus",
              "plantar_fasciitis", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "dysautonomia", "obesity", "chronic_fatigue",
            "multiple_sclerosis", "hip_pain", "glaucoma",
            "retinal_detachment_risk", "epilepsy", "shoulder_impingement"],
      safe=[],
      why="DUODECIMO safe_for vacio. Saltar desde arrodillado CON UNA BARRA "
           "SOBRE LA ESPALDA: axial high, impact high y la rotula partiendo "
           "desde el suelo bajo carga. La combinacion de arrodillarse, "
           "explosividad y carga axial no aparece en ningun otro ejercicio del "
           "catalogo, y es la que peor reparte el impacto — el tobillo "
           "arranca en flexion plantar completa."),
]

CONFIDENCE_OVERRIDES = {
    "1489": 0.65,  # texto contradictorio: 'leaning back' vs 'push through heels'
}

for _e in BATCH:
    _e.pop("safe_hint", None)
    if _e["exercise_id"] in CONFIDENCE_OVERRIDES:
        _e["confidence"] = CONFIDENCE_OVERRIDES[_e["exercise_id"]]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 30: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
