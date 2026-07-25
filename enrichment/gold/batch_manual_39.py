#!/usr/bin/env python3
"""Lote 39 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0498", "inverted row with straps", "standing", standing=True,
      bal="moderate", grip="firm",
      stress=js(sh="moderate", el="moderate", lumbar="moderate", wr="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_grip", "one_arm_only"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "elbow_injury", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "lumbar_disc", "hypermobility", "osteoporosis", "obesity",
            "elderly_65plus", "chronic_fatigue", "dysautonomia",
            "hernia_abdominal"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "sciatica"],
      why="Lo importante no esta en los campos: caminando los pies hacia "
           "adelante o hacia atras se cambia el angulo del cuerpo y con eso "
           "el porcentaje de peso que se levanta. Es de los pocos ejercicios "
           "del catalogo con dificultad regulable de forma continua sin "
           "cambiar de ejercicio. Requiere anclaje de suspension aunque el "
           "dataset lo liste como body weight."),

    E("0309", "dumbbell front raise v. 2", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury", "wrist_injury"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "sciatica",
            "plantar_fasciitis", "carpal_tunnel", "osteoporosis"],
      why="Equivalente a 0310 dumbbell front raise; el 'v. 2' no introduce "
           "ninguna diferencia de ejecucion en el texto. Se clasifica "
           "identico. El brazo se detiene a la altura del hombro, por eso "
           "no_overhead sigue en safe_for."),

    E("0979", "band horizontal pallof press", "standing", standing=True,
      bal="moderate", grip="light",
      stress=js(lumbar="low", sh="moderate", el="low", wr="low", hip="low"),
      pat="core_antiextension", diff=2, rom="low",
      ortho="high", change="low", valsalva="low", iso="high", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["shoulder_impingement", "shoulder_pain", "rotator_cuff",
            "elbow_injury", "carpal_tunnel", "lumbar_pain", "lumbar_disc",
            "si_joint_pain", "limited_balance", "hypertension",
            "dysautonomia", "elderly_65plus", "hernia_abdominal",
            "pelvic_floor_dysfunction", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "osteoporosis", "sciatica"],
      why="Este es el pallof clasico y confirma la sospecha del lote 36: "
           "1015 'band vertical pallof press' describe exactamente lo mismo "
           "con otro nombre. Mismo valor de producto —anti-rotacion sin "
           "flexion lumbar, sin suelo y sin impacto— y mismos campos. E3 "
           "debe quedarse con uno de los dos."),

    E("0074", "barbell rack pull", "standing", standing=True, bal="low",
      grip="firm", flex="low",
      stress=js(lumbar="high", hip="high", knee="moderate"),
      pat="hinge", diff=3, rom="low",
      ortho="high", change="low", valsalva="high", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "limited_grip", "hernia_abdominal",
              "hip_replacement", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "knee_pain", "cervical_injury",
            "hypertension", "cardiac", "glaucoma", "retinal_detachment_risk",
            "dysautonomia", "elderly_65plus", "obesity",
            "pelvic_floor_dysfunction"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "knee_injury", "ankle_injury", "plantar_fasciitis"],
      why="Peso muerto parcial desde la altura de la rodilla: rom_demand low "
           "y spinal_flexion low, frente a high en 0432 dumbbell stiff leg "
           "deadlift. Como la barra arranca arriba, la rodilla casi no "
           "trabaja y knee_injury entra en safe_for, cosa rara en un "
           "ejercicio de pierna. Pero la carga tipica es la mas alta de todo "
           "el catalogo y el valsalva es alto: lo lumbar sigue "
           "contraindicado. Menos rango no es menos compresion."),

    E("0124", "barbell wide squat", "standing", standing=True, bal="moderate",
      grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="low",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "hip_pain", "limited_grip",
              "lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "osteoporosis", "pelvic_floor_dysfunction", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["osteoarthritis", "ankle_injury", "plantar_fasciitis",
            "limited_balance", "dysautonomia", "hypertension", "cardiac",
            "glaucoma", "elderly_65plus", "obesity", "hernia_abdominal",
            "cervical_injury", "multiple_sclerosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury"],
      why="La base ancha con puntas hacia afuera traslada carga de la rodilla "
           "a la cadera y al aductor, y exige abduccion mas rotacion externa "
           "de cadera bajo barra. Esa combinacion es precisamente la que una "
           "protesis de cadera no puede hacer, y por eso hip_pain sube a "
           "contraindicacion, cosa que no ocurre en 0413 dumbbell squat ni "
           "en 0054. Mas ancho no es mas comodo: es otra articulacion."),

    E("3642", "weighted stretch lunge", "standing", standing=True, bal="high",
      sl=True, grip="firm", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="moderate",
                ank="moderate"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Zancada frontal con peso en las manos: mismo movimiento que 0336 "
           "dumbbell lunge. El 'stretch' del nombre no aparece en el texto, "
           "que describe una zancada estandar hasta muslo paralelo. Se "
           "clasifica como 0336. La progresion de la familia queda 3470 sin "
           "peso, 0336/3642 con peso, 3582 con salto."),

    E("0123", "barbell wide-grip upright row", "standing", standing=True,
      bal="low", grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="moderate",
                cerv="low"),
      pat="vertical_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip",
              "wrist_injury"],
      caut=["carpal_tunnel", "elbow_injury", "tendinitis_elbow", "neck_pain",
            "cervical_injury", "lumbar_pain", "lumbar_disc", "hypermobility",
            "dysautonomia", "hypertension", "elderly_65plus", "osteoporosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="Tercera entrada de la familia remo al menton con barra, junto a "
           "0120 y 0121. Este y 0121 describen el mismo agarre ancho y "
           "reciben la misma clasificacion: carpal_tunnel en precaucion en "
           "vez de contraindicacion, hombro contraindicado igual. Los tres "
           "son colapsables a dos —estrecho y ancho— en el indice."),

    E("0788", "standing behind neck press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="moderate",
      stress=js(sh="high", cerv="moderate", el="moderate", wr="moderate",
                lumbar="high"),
      pat="vertical_push", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "cervical_injury", "neck_pain", "lumbar_disc",
              "osteoporosis", "hypermobility"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "sciatica", "hypertension", "cardiac", "glaucoma",
            "retinal_detachment_risk", "dysautonomia", "elderly_65plus",
            "vertigo"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="La peor posicion de hombro del catalogo: la barra pasa por detras "
           "de la cabeza, lo que obliga a rotacion externa maxima con "
           "abduccion horizontal, justo el punto donde el manguito queda sin "
           "espacio. Ademas hay que flexionar el cuello para dejarla pasar. "
           "cervical_injury y neck_pain entran a contraindicacion, cosa que "
           "no pasa en 1456 ni en 1457. Cualquier press por delante es "
           "estrictamente mejor."),

    E("1372", "barbell standing calf raise", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(ank="high", lumbar="moderate", knee="low", hip="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury", "osteoporosis",
              "lumbar_disc", "limited_grip"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain", "hip_pain",
            "hip_replacement", "osteoarthritis", "lumbar_pain", "sciatica",
            "cervical_injury", "dysautonomia", "vertigo", "varicose_veins",
            "elderly_65plus", "hypertension"],
      safe=["no_overhead", "shoulder_impingement", "rotator_cuff",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "hernia_abdominal"],
      why="Mal negocio articular. 0284 donkey calf raise hace el mismo "
           "trabajo de gemelo con tres contraindicaciones; ponerle una barra "
           "encima agrega carga axial y sube osteoporosis y lumbar_disc a "
           "contraindicacion, para un musculo que responde perfecto al peso "
           "corporal. 1386 o 0999 dan lo mismo sin tocar la columna."),

    E("1628", "ez barbell spider curl", "standing", standing=True, bal="low",
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
      why="Duplicado exacto de 0454: mismo nombre e instrucciones "
           "identicas. Confirmado por find_duplicates.py con umbral 0,99. "
           "Se clasifica igual para que E3 pueda colapsarlos sin comparar "
           "campo por campo."),

    E("0066", "barbell one arm side deadlift", "standing", standing=True,
      bal="moderate", grip="firm", flex="moderate", rot="low",
      stress=js(lumbar="high", hip="high", knee="moderate", sh="moderate",
                wr="moderate"),
      lat="unilateral", pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "hip_replacement",
              "limited_grip", "hernia_abdominal", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hip_pain", "knee_pain", "shoulder_pain", "wrist_injury",
            "limited_balance", "hypertension", "glaucoma", "dysautonomia",
            "elderly_65plus", "obesity", "hypermobility",
            "pelvic_floor_dysfunction", "cervical_injury"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "ankle_injury", "plantar_fasciitis", "one_arm_only"],
      why="Peso muerto tipo maleta: la carga cuelga de un solo lado, asi que "
           "la columna trabaja resistiendo flexion lateral durante toda la "
           "serie. Es el unico hinge del catalogo que carga el plano frontal "
           "de la columna. Curiosamente one_arm_only queda en safe_for —el "
           "gesto ya es de un brazo— pero si_joint_pain sube a "
           "contraindicacion por la pelvis descompensada."),

    E("0354", "dumbbell one arm kickback", "standing", standing=True,
      bal="moderate", grip="firm", flex="moderate",
      stress=js(lumbar="high", sh="moderate", el="moderate", wr="low"),
      lat="unilateral", pat="isolation", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="low", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "tendinitis_elbow", "limited_balance", "hypertension", "obesity",
            "elderly_65plus", "osteoporosis", "dysautonomia", "hip_pain"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "wrist_injury", "carpal_tunnel", "one_arm_only"],
      why="Tercera variante de kickback de pie junto a 0333 y 0420. La unica "
           "diferencia real es que al ser a un brazo, one_arm_only entra en "
           "safe_for. El isometrico lumbar en bisagra sostenida sigue siendo "
           "el limitante: 0394 dumbbell seated kickback lo resuelve sentado."),

    E("0370", "dumbbell peacher hammer curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["rheumatoid_arthritis", "wrist_injury", "shoulder_pain",
            "lumbar_pain", "dysautonomia", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica", "carpal_tunnel", "osteoporosis"],
      why="Caso de manual de D-018: el nombre dice preacher —banco "
           "inclinado, codo apoyado— pero las instrucciones describen un "
           "curl martillo de pie identico a 0313. Se clasifica por el texto, "
           "que es lo que define el movimiento, y se marca para que E3 "
           "corrija el nombre o el registro."),

    E("0377", "dumbbell rear delt row_shoulder", "standing", standing=True,
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
      why="El sufijo '_shoulder' en el nombre es basura de exportacion del "
           "dataset, no parte del ejercicio. El texto describe la misma "
           "elevacion posterior en bisagra que 2292 dumbbell rear delt "
           "raise y 0380, y recibe la misma clasificacion. Tres registros "
           "para un movimiento."),

    E("0380", "dumbbell rear lateral raise", "standing", standing=True,
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
      why="Tercer registro identico a 2292 y 0377. Los tres describen "
           "hinge mas elevacion lateral posterior con mancuernas. "
           "find_duplicates.py los agrupa junto a 0379 con umbral 0,90. "
           "Clasificados igual a proposito para que E3 los colapse."),

    E("0411", "dumbbell single leg squat", "standing", standing=True,
      bal="high", sl=True, grip="firm",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="high"),
      lat="unilateral", pat="squat", diff=5, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="high", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "vertigo", "visual_impairment",
              "osteoarthritis", "elderly_65plus", "multiple_sclerosis",
              "osteoporosis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "plantar_fasciitis", "dysautonomia", "obesity", "hypermobility",
            "pelvic_floor_dysfunction"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Sentadilla a una pierna con la otra extendida al frente, mas peso "
           "en las manos. Difficulty 5: la rodilla de apoyo absorbe todo el "
           "peso corporal mas la carga, y el tobillo necesita una "
           "dorsiflexion que mucha gente sana no tiene. Extremo superior de "
           "la familia de sentadilla, cuyo extremo inferior es 0291 "
           "dumbbell bench squat."),

    E("0415", "dumbbell standing alternate raise", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      lat="alternating", pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury", "wrist_injury"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "sciatica",
            "plantar_fasciitis", "carpal_tunnel", "osteoporosis",
            "one_arm_only"],
      why="Elevacion lateral alternada: 0334 dumbbell lateral raise brazo "
           "por brazo. Igual que en 0285, lo que cambia no es la carga sino "
           "la accesibilidad —one_arm_only entra en safe_for porque el gesto "
           "ya se hace de a un lado."),

    E("0416", "dumbbell standing biceps curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
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
            "sciatica"],
      why="Instrucciones identicas a 0294 dumbbell biceps curl. Se clasifica "
           "igual. Con 0294, 0285, 0416 y las variantes reverse y hammer, la "
           "familia de curl de pie con mancuerna tiene mas registros que "
           "movimientos distintos: es el grupo con mas redundancia del "
           "catalogo."),
]

CONFIDENCE_OVERRIDES = {
    "0370": 0.70,  # el nombre dice preacher, el texto describe 0313 de pie
    "0416": 0.70,  # duplicado de 0294
    "1628": 0.70,  # duplicado exacto de 0454
    "0380": 0.75,  # duplicado de 2292
    "0377": 0.75,  # duplicado de 2292, con sufijo espurio en el nombre
    "0309": 0.75,  # duplicado de 0310
    "0979": 0.80,  # solapa con 1015; uno de los dos sobra
    "3642": 0.80,  # el nombre dice "stretch lunge", el texto describe 0336
    "0498": 0.80,  # requiere suspension, listado como body weight
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
    print(f"lote 39: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
