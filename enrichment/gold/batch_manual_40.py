#!/usr/bin/env python3
"""Lote 40 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0417", "dumbbell standing calf raise", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(ank="high", knee="low", hip="low", lumbar="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury", "limited_grip"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain", "hip_pain",
            "hip_replacement", "osteoarthritis", "dysautonomia", "vertigo",
            "varicose_veins", "elderly_65plus", "osteoporosis",
            "lumbar_pain"],
      safe=["no_overhead", "shoulder_impingement", "rotator_cuff",
            "wrist_injury", "carpal_tunnel", "elbow_injury", "lumbar_disc",
            "sciatica", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "hernia_abdominal"],
      why="Comparacion directa con 1372 barbell standing calf raise: mismo "
           "trabajo de gemelo, misma carga externa, pero el peso cuelga de "
           "las manos en vez de apoyarse en la columna. axial_spinal_load "
           "pasa de high a none y osteoporosis y lumbar_disc salen de "
           "contraindicacion. Si hay que cargar un gemelo y la columna "
           "importa, se carga asi."),

    E("1418", "hug keens to chest", "standing", standing=True, bal="moderate",
      grip="light", flex="moderate",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="high"),
      pat="squat", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="moderate", pelvic="moderate", gripdur="low",
      temp="low",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "ankle_injury"],
      caut=["hip_pain", "osteoarthritis", "lumbar_pain", "lumbar_disc",
            "sciatica", "si_joint_pain", "plantar_fasciitis",
            "limited_balance", "dysautonomia", "vertigo", "elderly_65plus",
            "obesity", "osteoporosis", "hernia_abdominal", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff"],
      why="El nombre trae un error de tipeo ('keens' por 'knees'). Es una "
           "sentadilla profunda abrazando las rodillas: no es trabajo de "
           "fuerza sino de rango, y exige flexion maxima simultanea de "
           "tobillo, rodilla y cadera. Difficulty 2 por la carga, pero "
           "rom_demand high — la barrera real es la movilidad, no la fuerza."),

    E("0355", "dumbbell one arm lateral raise", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      lat="unilateral", pat="isolation", diff=2, rom="moderate",
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
      why="Cuarta entrada de la familia elevacion lateral con mancuerna, "
           "junto a 0334, 0415 y 0376. Unilateral estricta, asi que "
           "one_arm_only queda en safe_for. Fuera de eso, identica a 0334."),

    E("1765", "dumbbell upright row (back pov)", "standing", standing=True,
      bal="low", grip="firm", axial="low",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low",
                cerv="low"),
      pat="vertical_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip"],
      caut=["wrist_injury", "carpal_tunnel", "elbow_injury",
            "tendinitis_elbow", "neck_pain", "cervical_injury", "lumbar_pain",
            "lumbar_disc", "hypermobility", "dysautonomia", "hypertension",
            "elderly_65plus", "osteoporosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "sciatica"],
      why="'(back pov)' es metadato de angulo de camara, igual que en "
           "1461/1462 — no describe el ejercicio. Con mancuernas las manos "
           "se mueven libres y no hay desviacion cubital forzada: "
           "wrist_injury baja de contraindicacion —como en 0120 y 0121 con "
           "barra— a precaucion. El arco de hombro no cambia, asi que el "
           "pinzamiento sigue fuera."),

    E("3194", "frankenstein squat", "standing", standing=True, bal="moderate",
      grip="firm", axial="high",
      stress=js(knee="high", hip="moderate", lumbar="moderate", sh="high",
                ank="high", wr="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "osteoporosis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["osteoarthritis", "hip_pain", "lumbar_pain", "lumbar_disc",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "dysautonomia", "hypertension", "cardiac", "glaucoma",
            "elderly_65plus", "obesity", "cervical_injury", "wrist_injury",
            "hypermobility"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "elbow_injury", "sciatica",
            "carpal_tunnel"],
      why="Barra al frente con los brazos estirados hacia adelante. El peso "
           "adelantado obliga a un torso vertical, y eso baja lumbar a "
           "moderate frente a high en 0124 barbell wide squat — pero el "
           "precio es sostener los brazos extendidos toda la serie, asi que "
           "el hombro pasa a ser el limitante en vez de la espalda. Ademas "
           "exige mas dorsiflexion de tobillo que cualquier sentadilla con "
           "barra atras."),

    E("0853", "weighted standing curl", "standing", standing=True, bal="low",
      grip="firm",
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
      why="Catalogado como equipo 'weighted' pero las instrucciones dicen "
           "mancuerna en cada mano: es 0294 dumbbell biceps curl otra vez. "
           "Quinta entrada de la familia curl de pie. Se clasifica identico."),

    E("0103", "barbell standing ab rollerout", "standing", standing=True,
      bal="high", oh=True, grip="firm", ext="high",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="moderate", change="high", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "limited_grip",
              "no_overhead", "shoulder_impingement", "rotator_cuff",
              "shoulder_pain", "lumbar_disc", "lumbar_pain", "sciatica",
              "si_joint_pain", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "hypermobility", "osteoporosis",
              "elderly_65plus", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "obesity", "chronic_fatigue", "hypertension",
            "dysautonomia", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Rollout de pie hasta extension completa del cuerpo. Es el "
           "anti-extension mas duro del catalogo: difficulty 5, un escalon "
           "por encima de 0805 suspended abdominal fallout, porque desde de "
           "pie el recorrido termina con el cuerpo casi horizontal sostenido "
           "solo por los brazos. Veintiun contraindicaciones. Para casi "
           "cualquier perfil el sustituto es 0979 band horizontal pallof "
           "press, que entrena lo mismo con dos."),

    E("0116", "barbell straight leg deadlift", "standing", standing=True,
      bal="low", grip="firm", flex="high",
      stress=js(hip="high", lumbar="high", knee="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "hernia_abdominal",
              "hip_replacement", "limited_grip", "si_joint_pain",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "hypermobility", "knee_pain", "dysautonomia",
            "vertigo", "limited_balance", "elderly_65plus", "obesity",
            "pelvic_floor_dysfunction", "glaucoma", "hypertension",
            "cardiac", "retinal_detachment_risk"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "ankle_injury", "plantar_fasciitis"],
      why="Version con barra de 0432 dumbbell stiff leg deadlift. La barra "
           "obliga a mantener el peso por delante del cuerpo en vez de a los "
           "costados, lo que alarga el brazo de palanca sobre la columna: "
           "difficulty sube de 3 a 4, valsalva de moderate a high y "
           "si_joint_pain entra a contraindicacion. Progresion de la familia: "
           "1009 banda, 0432 mancuerna, 0116 barra."),

    E("0077", "barbell rear lunge v. 2", "standing", standing=True,
      bal="high", sl=True, grip="firm", axial="high", impact="low",
      stress=js(knee="high", hip="moderate", lumbar="high", cerv="moderate",
                ank="moderate"),
      lat="unilateral", pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "lumbar_disc", "sciatica", "osteoporosis",
              "cervical_injury", "limited_grip", "pregnancy_1st",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "obesity", "hypertension", "cardiac",
            "hernia_abdominal", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff"],
      why="Instrucciones equivalentes a 0078 barbell rear lunge. Se clasifica "
           "identico. La barra al hombro es lo que mete cervical_injury en "
           "contraindicacion: hay que sostenerla sobre el trapecio con el "
           "cuello estable mientras el cuerpo se desplaza hacia atras."),

    E("0445", "ez barbell anti gravity press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="moderate",
      stress=js(sh="high", el="moderate", wr="low", lumbar="high",
                cerv="low"),
      pat="vertical_push", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "lumbar_disc", "osteoporosis"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "lumbar_pain", "sciatica", "hypertension",
            "cardiac", "glaucoma", "retinal_detachment_risk", "dysautonomia",
            "elderly_65plus", "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Press militar de pie con barra Z. El agarre angulado deja la "
           "muneca en semipronacion en vez de pronacion completa: wrist baja "
           "de moderate —como en 1456 y 1457 con barra recta— a low. Es la "
           "unica diferencia; todo lo demas, incluido lumbar_disc en "
           "contraindicacion por la hiperextension compensatoria, se "
           "mantiene."),

    E("0589", "lever one arm bent over row", "standing", standing=True,
      bal="low", grip="firm", flex="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="high",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "limited_grip", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hip_replacement",
            "shoulder_impingement", "elbow_injury", "cervical_injury",
            "neck_pain", "hypertension", "glaucoma", "dysautonomia",
            "elderly_65plus", "obesity", "pelvic_floor_dysfunction"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "wrist_injury"],
      why="El nombre dice 'lever one arm' pero el equipo catalogado es barra "
           "y el texto describe un remo inclinado bilateral: es 0293 dumbbell "
           "bent over row con barra. Se clasifica por el texto. Mismo "
           "limitante que 0293 y 0075: el isometrico lumbar sostenido, no el "
           "musculo que se quiere entrenar."),

    E("0418", "dumbbell standing concentration curl", "standing",
      standing=True, bal="low", grip="firm", flex="low",
      stress=js(el="moderate", lumbar="moderate", wr="low", sh="low"),
      lat="unilateral", pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["carpal_tunnel", "wrist_injury", "rheumatoid_arthritis",
            "lumbar_pain", "lumbar_disc", "shoulder_pain", "dysautonomia",
            "hypertension", "hip_pain"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica", "one_arm_only"],
      why="La mano libre apoyada en el muslo sostiene parte del peso del "
           "tronco inclinado. Ese detalle es lo que separa este curl de un "
           "kickback tipo 0333: lumbar queda en moderate en vez de high y "
           "lumbar_disc baja a precaucion. Curioso que one_arm_only siga en "
           "safe_for aunque la otra mano se use —solo sirve de apoyo, no "
           "carga."),

    E("0429", "dumbbell standing reverse curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="moderate", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury"],
      caut=["carpal_tunnel", "rheumatoid_arthritis", "hypermobility",
            "shoulder_pain", "lumbar_pain", "dysautonomia", "hypertension",
            "osteoarthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica"],
      why="Nombre e instrucciones no coinciden: 'reverse curl' implica agarre "
           "pronado, pero el texto dice palmas hacia el cuerpo, que es agarre "
           "neutro. Ante la discrepancia se toma la lectura MAS restrictiva "
           "—pronado, wrist moderate y wrist_injury contraindicado— porque en "
           "un dataset de seguridad el costo de advertir de mas es mucho "
           "menor que el de advertir de menos. Criterio a fijar en E3 para "
           "todos los casos de nombre contra texto."),

    E("0430", "dumbbell standing triceps extension", "standing",
      standing=True, bal="low", oh=True, grip="firm", axial="low",
      stress=js(sh="high", el="high", wr="moderate", lumbar="moderate"),
      lat="unilateral", pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "elbow_injury",
              "tendinitis_elbow", "limited_grip"],
      caut=["shoulder_pain", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "neck_pain", "lumbar_pain", "lumbar_disc",
            "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus", "osteoporosis", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "one_arm_only"],
      why="Extension de triceps sobre la cabeza a un brazo: 1749 ez bar "
           "standing french press con mancuerna. Al ser unilateral, "
           "one_arm_only entra en safe_for y la carga sobre la columna es "
           "menor —lumbar moderate en vez de la compensacion bilateral con "
           "barra. El hombro sigue siendo el filtro."),

    E("0434", "dumbbell straight leg deadlift", "standing", standing=True,
      bal="low", grip="firm", flex="high",
      stress=js(hip="high", lumbar="high", knee="moderate"),
      pat="hinge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "osteoporosis", "hernia_abdominal",
              "hip_replacement", "limited_grip", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hypermobility", "knee_pain",
            "dysautonomia", "vertigo", "limited_balance", "elderly_65plus",
            "obesity", "pelvic_floor_dysfunction", "glaucoma",
            "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "ankle_injury", "plantar_fasciitis"],
      why="Instrucciones equivalentes a 0432 dumbbell stiff leg deadlift "
           "—'straight leg' y 'stiff leg' son el mismo ejercicio con dos "
           "nombres. Se clasifica identico. Septimo par duplicado "
           "identificado en el pipeline."),

    E("0730", "single leg platform slide", "standing", standing=True,
      bal="high", sl=True,
      stress=js(hip="high", knee="moderate", lumbar="moderate", ank="low"),
      lat="unilateral", pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement", "vertigo"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "ankle_injury", "plantar_fasciitis", "osteoarthritis",
            "dysautonomia", "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis", "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="El pie no se despega nunca de la superficie: impact_level none, "
           "sin aterrizaje ni fase de vuelo, a diferencia de toda la familia "
           "de zancada. Eso lo hace la via mas suave al patron unipodal para "
           "articulaciones sensibles. El costo es que la superficie desliza "
           "de forma poco predecible, asi que el equilibrio sigue en high. "
           "Requiere tabla deslizante: fuera del filtro de equipo de casa."),

    E("1373", "bodyweight standing calf raise", "standing", standing=True,
      bal="low",
      stress=js(ank="high", knee="low", hip="low"),
      pat="isolation", diff=1, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["plantar_fasciitis", "knee_pain", "hip_pain", "osteoarthritis",
            "limited_balance", "dysautonomia", "vertigo", "varicose_veins",
            "elderly_65plus", "osteoporosis"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "lumbar_disc", "lumbar_pain", "sciatica", "cannot_get_on_floor",
            "cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "hernia_abdominal",
            "knee_injury", "hip_replacement"],
      why="La entrada de toda la familia de gemelo: manos en la pared, sin "
           "carga, difficulty 1, tres contraindicaciones. La progresion "
           "completa queda 1373 apoyado a dos piernas, 1386 apoyado a una, "
           "1387 sin apoyo a una, 0999 con banda, 0417 con mancuernas, "
           "0833 con talon colgando, 1372 con barra. Siete escalones para el "
           "mismo musculo — el catalogo tiene con que progresar sin saltar."),

    E("1398", "standing calves calf stretch", "standing", standing=True,
      bal="low",
      stress=js(ank="moderate", knee="low", hip="low"),
      lat="unilateral", pat="mobility_stretch", diff=1, rom="high",
      ortho="high", change="low", valsalva="none", iso="moderate",
      metab="none", laxity="moderate", pelvic="low", temp="none",
      contra=["cannot_stand", "wheelchair"],
      caut=["ankle_injury", "plantar_fasciitis", "knee_pain", "hip_pain",
            "osteoarthritis", "limited_balance", "dysautonomia", "vertigo",
            "elderly_65plus", "hypermobility", "varicose_veins"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "lumbar_pain", "sciatica", "knee_injury",
            "hip_replacement", "osteoporosis", "hernia_abdominal"],
      why="Dos contraindicaciones, las dos de Capa A. Manos en la pared, "
           "columna neutra y cabeza por encima del corazon: al reves de 1511 "
           "hamstring stretch, que se pliega hacia adelante y arrastra "
           "glaucoma, vertigo e hipertension a precaucion. Para perfil mayor "
           "o con disautonomia, este es el estiramiento de pierna que si "
           "funciona. 1390 seated calf stretch cubre el caso sentado."),
]

CONFIDENCE_OVERRIDES = {
    "0429": 0.65,  # nombre "reverse" contra texto neutro; se toma la lectura estricta
    "0589": 0.65,  # nombre "lever one arm" contra texto de remo bilateral con barra
    "0853": 0.70,  # duplicado de 0294, catalogado como "weighted"
    "0434": 0.70,  # duplicado de 0432
    "1765": 0.75,  # "(back pov)" es angulo de camara, no ejercicio
    "0077": 0.75,  # duplicado de 0078
    "1418": 0.80,  # error de tipeo en el nombre, intencion ambigua
    "0730": 0.80,  # requiere tabla deslizante, fuera del filtro de equipo
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
    print(f"lote 40: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
