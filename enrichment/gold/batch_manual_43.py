#!/usr/bin/env python3
"""Lote 43 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("3162", "bodyweight standing one arm row", "standing", standing=True,
      bal="moderate", grip="firm", axial="moderate", ext="low", rot="low",
      lat="unilateral",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="low", knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="low", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "limited_grip"],
      caut=["si_joint_pain", "hip_pain", "osteoporosis", "hypertension",
            "shoulder_impingement", "elbow_injury", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "osteoarthritis", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "ankle_injury", "plantar_fasciitis", "carpal_tunnel"],
      why="El equipo dice 'body weight' pero el texto pide mancuerna en una "
           "mano. Se clasifica lo que describe el texto. Lo determinante no "
           "es el remo sino la bisagra sostenida sin apoyo: lumbar high e "
           "sustained_isometric high. Al ser unilateral entra en safe_for de "
           "one_arm_only, uno de los pocos tirones que lo consigue."),

    E("0424", "dumbbell standing one arm palm in press", "standing",
      standing=True, bal="moderate", grip="firm", oh=True, axial="moderate",
      ext="low", rot="low", lat="unilateral",
      stress=js(sh="moderate", el="moderate", lumbar="moderate", cerv="low",
                wr="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead", "limited_grip"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "cervical_injury", "neck_pain", "lumbar_pain", "hypertension",
            "elbow_injury", "hypermobility", "dysautonomia", "vertigo",
            "elderly_65plus", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "one_arm_only",
            "knee_injury", "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "carpal_tunnel"],
      why="'Palm in' es agarre neutro: aplica la regla de sustitucion "
           "confirmada en E4 — el neutro baja el estres de hombro de high a "
           "moderate. Por eso impingement y manguito quedan en cautions y no "
           "en contraindicaciones. no_overhead sigue siendo filtro duro de "
           "capa A: es geometria, no carga."),

    E("0998", "band side triceps extension", "standing", standing=True,
      bal="low", grip="light",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="high", metab="low",
      laxity="moderate", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "limited_grip"],
      caut=["shoulder_pain", "elbow_injury", "tendinitis_elbow",
            "chronic_fatigue", "fibromyalgia", "hypermobility",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "lumbar_disc", "sciatica", "plantar_fasciitis", "osteoporosis",
            "carpal_tunnel"],
      why="El triceps no es el problema: los brazos se sostienen abiertos y "
           "paralelos al suelo durante toda la serie. Eso es abduccion "
           "mantenida a 90 grados, el arco doloroso exacto del impingement. "
           "sustained_isometric high por el hombro, no por el codo."),

    E("2805", "dumbbell single leg deadlift with stepbox support", "standing",
      standing=True, bal="high", sl=True, grip="firm", axial="moderate",
      ext="low", rot="low", lat="unilateral",
      stress=js(hip="high", lumbar="high", knee="moderate", ank="moderate",
                sh="low", el="low", wr="low"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "lumbar_disc", "lumbar_pain", "sciatica",
              "hip_replacement", "hip_pain", "ankle_injury", "limited_grip"],
      caut=["knee_pain", "knee_injury", "si_joint_pain", "osteoarthritis",
            "plantar_fasciitis", "osteoporosis", "vertigo", "dysautonomia",
            "elderly_65plus", "obesity", "multiple_sclerosis", "hypertension",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "carpal_tunnel"],
      why="El texto se contradice: primero apoya el pie en el cajon y despues "
           "manda elevar esa misma pierna. Si el pie queda apoyado el apoyo "
           "baja el balance un escalon; si se eleva es un peso muerto "
           "unilateral puro. Ante duda en campo de seguridad se toma la "
           "lectura restrictiva: bal high y sl True. Marcado para E3."),

    E("0101", "barbell speed squat", "standing", standing=True, bal="moderate",
      grip="firm", axial="high", ext="low", impact="low",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                sh="moderate", wr="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement", "hip_pain",
              "lumbar_disc", "lumbar_pain", "sciatica", "ankle_injury",
              "limited_grip", "shoulder_impingement", "rotator_cuff"],
      caut=["osteoporosis", "hypertension", "cardiac", "hernia_abdominal",
            "pregnancy_2nd", "pregnancy_3rd", "glaucoma",
            "retinal_detachment_risk", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "si_joint_pain", "osteoarthritis",
            "pelvic_floor_dysfunction", "postpartum", "varicose_veins"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench"],
      why="El texto describe una sentadilla trasera comun; 'speed' no aparece "
           "en ninguna instruccion. Se clasifica el texto y se baja "
           "confidence. Barra en la espalda: axial high mas valsalva high mas "
           "pelvic_floor high, la combinacion mas restrictiva del catalogo "
           "junto a la sentadilla frontal. La posicion de rack tambien exige "
           "rotacion externa de hombro, por eso impingement es contra."),

    E("1000", "band single leg reverse calf raise", "standing", standing=True,
      bal="moderate", sl=True, grip="light",
      stress=js(ank="high", knee="low", hip="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="none", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis"],
      caut=["limited_balance", "limited_grip", "knee_pain", "osteoarthritis",
            "dysautonomia", "vertigo", "elderly_65plus", "varicose_veins",
            "multiple_sclerosis", "obesity"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "lumbar_disc", "sciatica",
            "hip_replacement", "osteoporosis"],
      why="Dos cosas. Primero, el nombre dice 'reverse' pero el texto describe "
           "una elevacion de talon normal, no una elevacion de punta. "
           "Segundo, el texto pide agarrarse de un objeto estable: aplica la "
           "regla del apoyo y limited_balance baja de contraindicacion a "
           "cautions pese a ser unipodal. Es el unico unipodal del lote que "
           "sobrevive a un perfil con equilibrio limitado."),

    E("3643", "weighted cossack squats (male)", "standing", standing=True,
      bal="high", grip="firm", axial="moderate", flex="low", rot="low",
      lat="alternating",
      stress=js(knee="high", hip="high", ank="high", lumbar="moderate",
                sh="low", el="low", wr="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement", "hip_pain",
              "ankle_injury", "lumbar_disc", "limited_grip"],
      caut=["lumbar_pain", "sciatica", "si_joint_pain", "osteoarthritis",
            "hypermobility", "plantar_fasciitis", "osteoporosis",
            "dysautonomia", "vertigo", "elderly_65plus", "obesity",
            "multiple_sclerosis", "hypertension", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "carpal_tunnel"],
      why="Sentadilla lateral profunda con la otra pierna en extension "
           "completa: joint_laxity_risk high por el rango de aductores y "
           "ankle high por la dorsiflexion exigida. Es de los pocos "
           "ejercicios donde el tobillo, no la rodilla, suele ser el limite "
           "real. Sufijo '(male)' — candidato a duplicado de genero."),

    E("0107", "barbell standing front raise over head", "standing",
      standing=True, bal="low", grip="firm", oh=True, axial="low", ext="low",
      stress=js(sh="high", wr="moderate", lumbar="moderate", el="low",
                cerv="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="none", valsalva="moderate", iso="moderate",
      metab="low", laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "wrist_injury"],
      caut=["cervical_injury", "neck_pain", "lumbar_pain", "hypertension",
            "hypermobility", "tendinitis_elbow", "carpal_tunnel",
            "dysautonomia", "elderly_65plus", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica"],
      why="Conflicto entre reglas de la taxonomia. El nombre dice 'over head' "
           "y el texto dice 'slightly above shoulder level'. La regla 5 manda "
           "priorizar instrucciones, pero la regla 1 manda el valor mas "
           "restrictivo en campo de seguridad, y overhead_position es filtro "
           "duro de capa A. Gana la regla 1: oh True. Barra recta ademas "
           "coloca la muneca en el extremo alto de la escala de implemento."),

    E("1670", "dumbbell one arm standing curl", "standing", standing=True,
      bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "lumbar_disc", "sciatica",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Solo tres contraindicaciones y dieciocho safe_for: es el "
           "ejercicio mas accesible del lote y el suelo de accesibilidad para "
           "biceps de pie. Unilateral, sin carga axial, sin cambio de "
           "posicion, sin overhead. Candidato claro a sustituto por defecto "
           "en E4 para cualquier curl mas exigente."),

    E("1739", "dumbbell standing alternating tricep kickback", "standing",
      standing=True, bal="moderate", grip="firm", axial="low", ext="low",
      rot="low", lat="alternating",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="low", knee="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="high",
      metab="low", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "limited_grip"],
      caut=["si_joint_pain", "hip_pain", "shoulder_impingement",
            "shoulder_pain", "elbow_injury", "tendinitis_elbow",
            "osteoporosis", "hypertension", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis", "carpal_tunnel"],
      why="Mismo patron que 3162: un ejercicio de brazo cuyo filtro real es "
           "la bisagra sostenida. Un aislado de triceps termina "
           "contraindicado para hernia discal no por el codo sino por la "
           "postura de partida. La extension de hombro por detras del cuerpo "
           "justifica impingement en cautions."),

    E("1759", "single leg squat (pistol) male", "standing", standing=True,
      bal="high", sl=True, grip="none", axial="low", flex="low",
      lat="unilateral",
      stress=js(knee="high", hip="high", ank="high", lumbar="moderate"),
      pat="squat", diff=5, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "hip_pain", "ankle_injury",
              "plantar_fasciitis"],
      caut=["lumbar_pain", "lumbar_disc", "sciatica", "si_joint_pain",
            "osteoarthritis", "hypermobility", "osteoporosis", "dysautonomia",
            "vertigo", "elderly_65plus", "obesity", "multiple_sclerosis",
            "hypertension", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip", "one_arm_only",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel"],
      why="Unico difficulty 5 del lote. Curiosidad util: al no necesitar "
           "agarre ni carga externa, el pistol es safe_for de todo el tren "
           "superior — limited_grip, one_arm_only, muneca, codo, hombro. Es "
           "el espejo exacto del curl 1670: cada uno es el suelo de "
           "accesibilidad del hemisferio opuesto."),

    E("2293", "dumbbell standing zottman preacher curl", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel"],
      caut=["shoulder_pain", "hypermobility", "rheumatoid_arthritis",
            "osteoarthritis", "dysautonomia", "elderly_65plus",
            "hypertension"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "lumbar_disc", "sciatica",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Nombre encadenado de tres tecnicas incompatibles: de pie, zottman "
           "y predicador. El texto resuelve pidiendo apoyar los brazos en el "
           "banco predicador estando de pie. La suma predicador mas rotacion "
           "bajo carga pone elbow en high, el unico high de codo del lote. "
           "Marcado para E3."),

    E("2327", "dumbbell reverse grip row (female)", "standing", standing=True,
      bal="moderate", grip="firm", axial="moderate", flex="low", ext="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="low", knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "limited_grip"],
      caut=["si_joint_pain", "hip_pain", "osteoporosis", "hernia_abdominal",
            "shoulder_impingement", "elbow_injury", "hypertension",
            "dysautonomia", "vertigo", "elderly_65plus", "obesity",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis", "carpal_tunnel"],
      why="El nombre dice agarre invertido y el texto dice 'overhand grip'. "
           "Se clasifica el texto. Detalle relevante para osteoporosis: el "
           "texto dice 'bend forward at the waist', no at the hips — flexion "
           "de columna bajo carga, no bisagra. Por eso spinal_flexion low en "
           "vez de none. Sufijo '(female)' — candidato a duplicado."),

    E("3165", "bodyweight standing row (with towel)", "standing",
      standing=True, bal="low", grip="light", axial="low", ext="low",
      stress=js(lumbar="moderate", hip="moderate", sh="low", el="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="high",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
            "hip_pain", "osteoporosis", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "wrist_injury", "carpal_tunnel", "elbow_injury"],
      why="Autorresistencia con toalla, sin ancla ni carga externa: el "
           "esfuerzo es isometrico y autolimitado. Eso cambia la lectura de "
           "la bisagra — sin peso en las manos, hernia discal y ciatica bajan "
           "de contraindicacion a cautions. Es el suelo de accesibilidad para "
           "traccion horizontal de pie sin equipo, el equivalente del "
           "isometric chest squeeze en empuje horizontal."),

    E("3167", "bodyweight squatting row (with towel)", "standing",
      standing=True, bal="moderate", grip="light", axial="low", flex="low",
      stress=js(knee="moderate", hip="moderate", lumbar="moderate",
                ank="moderate", sh="low", el="low"),
      pat="horizontal_pull", diff=3, rom="high",
      ortho="high", change="high", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip"],
      caut=["limited_balance", "lumbar_pain", "lumbar_disc", "sciatica",
            "hip_pain", "ankle_injury", "plantar_fasciitis", "osteoarthritis",
            "osteoporosis", "dysautonomia", "vertigo", "elderly_65plus",
            "obesity", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel"],
      why="Hibrido: el target es espalda alta pero el filtro real lo impone "
           "la sentadilla. Se mantiene horizontal_pull como patron por "
           "coherencia con el target y E1, pero las contraindicaciones son "
           "todas de rodilla y cadera. Comparado con 3165 pierde nueve "
           "safe_for solo por agregar el descenso."),

    E("0356", "dumbbell one arm lateral raise with support", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="moderate",
      metab="low", laxity="high", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip"],
      caut=["limited_balance", "cervical_injury", "neck_pain",
            "hypermobility", "elbow_injury", "chronic_fatigue",
            "hypertension", "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "lumbar_disc", "sciatica", "osteoporosis"],
      why="Apoyo explicito en banco o pared: la regla del apoyo baja el "
           "balance a low y limited_balance queda en cautions. Ojo con un "
           "detalle que no es obvio — aunque el ejercicio es unilateral, NO "
           "entra en safe_for de one_arm_only, porque el apoyo consume la "
           "otra mano. Es la excepcion a la equivalencia unilateral igual "
           "one_arm_only que veniamos aplicando."),

    E("0379", "dumbbell rear lateral raise (support head)", "standing",
      standing=True, bal="moderate", grip="firm", axial="low", ext="low",
      stress=js(lumbar="high", sh="high", hip="moderate", cerv="moderate",
                el="low", wr="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="high",
      metab="low", laxity="high", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "shoulder_impingement", "rotator_cuff",
              "cervical_injury", "limited_grip"],
      caut=["neck_pain", "shoulder_pain", "si_joint_pain", "hip_pain",
            "osteoporosis", "hypermobility", "hypertension", "dysautonomia",
            "vertigo", "elderly_65plus", "obesity", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis", "elbow_injury",
            "carpal_tunnel"],
      why="Caso costoso. El nombre promete '(support head)' — la version con "
           "la frente apoyada en un banco inclinado, que elimina la bisagra y "
           "es de las mas accesibles del catalogo. El texto no menciona "
           "ningun apoyo. Se clasifica sin apoyo y queda contraindicado para "
           "columna y cuello. La version real merece ficha propia en E3: es "
           "una perdida de accesibilidad importante."),

    E("0419", "dumbbell standing front raise above head", "standing",
      standing=True, bal="low", grip="firm", oh=True, axial="low",
      ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="low", wr="low", cerv="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="none", valsalva="moderate", iso="moderate",
      metab="low", laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip"],
      caut=["cervical_injury", "neck_pain", "lumbar_pain", "lumbar_disc",
            "elbow_injury", "hypertension", "hypermobility", "dysautonomia",
            "elderly_65plus", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica", "carpal_tunnel"],
      why="Version con mancuernas de 0107 y sin la ambiguedad: aqui el texto "
           "si dice 'above your head'. Comparados uno al lado del otro "
           "confirman la escala de implemento — misma mecanica, pero la "
           "muneca baja de moderate a low al cambiar barra recta por "
           "mancuernas. spinal_extension moderate por el arco lumbar "
           "compensatorio al llegar arriba."),
]


CONFIDENCE_OVERRIDES = {
    "0107": 0.65,  # nombre dice over head, texto dice slightly above shoulder
    "0379": 0.65,  # nombre promete apoyo de cabeza, texto no lo menciona
    "2293": 0.65,  # nombre encadena de pie + zottman + predicador
    "2805": 0.70,  # texto se contradice: pie en cajon y a la vez pierna elevada
    "2327": 0.70,  # nombre dice reverse grip, texto dice overhand
    "1000": 0.75,  # nombre dice reverse calf raise, texto describe una normal
    "0101": 0.75,  # 'speed' no aparece en las instrucciones
    "3162": 0.75,  # equipo body weight pero el texto pide mancuerna
    "3167": 0.80,  # patron hibrido squat/pull sin resolver
    "3643": 0.90,  # sufijo (male), duplicado de genero probable
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
    print(f"lote 43: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
