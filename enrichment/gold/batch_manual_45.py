#!/usr/bin/env python3
"""Lote 45 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("3218", "hands clasped circular toe touch (male)", "standing",
      standing=True, bal="moderate", grip="none", flex="high", rot="low",
      stress=js(lumbar="high", hip="high", knee="low", ank="low"),
      pat="hinge", diff=2, rom="high",
      ortho="high", change="high", headdown=True, valsalva="low", iso="low",
      metab="low", laxity="moderate", pelvic="low", gripdur="none",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain"],
      caut=["hip_pain", "knee_pain", "osteoporosis", "hypermobility",
            "glaucoma", "retinal_detachment_risk", "migraine", "vertigo",
            "dysautonomia", "hypertension", "elderly_65plus", "obesity",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "ankle_injury",
            "plantar_fasciitis"],
      why="El mas benigno de la familia toe touch: rodillas flexionadas, dos "
           "pies en el suelo, sin rotacion. Seis contraindicaciones frente a "
           "las trece de 3214. La flexion lumbar completa sigue siendo el "
           "filtro, pero sin la pierna en el aire ni las piernas rectas el "
           "perfil cambia por completo. No entra one_arm_only (D-020): manos "
           "entrelazadas."),

    E("1435", "barbell low bar squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", ext="low",
      stress=js(knee="high", hip="high", lumbar="high", sh="high",
                ank="moderate", wr="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement", "hip_pain",
              "lumbar_disc", "lumbar_pain", "sciatica", "ankle_injury",
              "limited_grip", "shoulder_impingement", "rotator_cuff",
              "shoulder_pain", "wrist_injury"],
      caut=["osteoporosis", "hypertension", "cardiac", "hernia_abdominal",
            "glaucoma", "retinal_detachment_risk", "carpal_tunnel",
            "dysautonomia", "vertigo", "elderly_65plus", "obesity",
            "si_joint_pain", "osteoarthritis", "pelvic_floor_dysfunction",
            "postpartum", "varicose_veins", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench"],
      why="Diecisiete contraindicaciones, el mas restringido del lote. La "
           "diferencia con 0101 no esta en la pierna sino en el hombro: la "
           "barra baja exige rotacion externa y extension de hombro "
           "extremas, por eso sh sube a high y impingement, manguito y "
           "muneca pasan a contraindicacion. El texto no confirma que sea "
           "barra baja — dice 'upper back' — pero el nombre es especifico y "
           "el campo afectado es de seguridad (D-021)."),

    E("0451", "ez barbell reverse grip curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="moderate", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip",
              "tendinitis_elbow"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "rheumatoid_arthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Nombre dice agarre invertido, texto dice underhand — o sea supino, "
           "que es un curl normal. Se clasifica el texto: laterality y grip "
           "no son campos de seguridad de capa A, asi que manda la regla 5. "
           "La barra EZ mantiene la muneca en moderate, entre la mancuerna y "
           "la barra recta."),

    E("0111", "barbell standing rocking leg calf raise", "standing",
      standing=True, bal="high", grip="firm", axial="high",
      stress=js(ank="high", lumbar="moderate", sh="moderate", wr="moderate",
                knee="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "ankle_injury", "plantar_fasciitis",
              "limited_grip", "lumbar_disc", "shoulder_impingement",
              "rotator_cuff"],
      caut=["lumbar_pain", "sciatica", "knee_pain", "hip_replacement",
            "wrist_injury", "osteoporosis", "osteoarthritis", "hypertension",
            "dysautonomia", "vertigo", "elderly_65plus", "obesity",
            "varicose_veins"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "elbow_injury", "carpal_tunnel"],
      why="Elevarse sobre las puntas de los pies con una barra cargada en la "
           "espalda y sin ningun apoyo. Es el extremo opuesto de 1382 dentro "
           "del mismo gesto: mismo musculo, diez contraindicaciones contra "
           "cuatro. El nombre habla de 'rocking leg' pero el texto describe "
           "una elevacion bilateral comun."),

    E("0118", "barbell reverse grip bent over row", "standing", standing=True,
      bal="moderate", grip="firm", axial="moderate", ext="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="moderate", knee="low"),
      pat="horizontal_pull", diff=4, rom="moderate",
      ortho="high", change="moderate", valsalva="high", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "limited_grip"],
      caut=["hip_pain", "osteoporosis", "hernia_abdominal",
            "shoulder_impingement", "elbow_injury", "tendinitis_elbow",
            "wrist_injury", "carpal_tunnel", "hypertension", "cardiac",
            "pelvic_floor_dysfunction", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis"],
      why="Cuarto remo inclinado de la serie (1344, 2327, 1329, 0118) y el "
           "mas pesado. Unico con valsalva_risk high: la barra permite cargas "
           "que la mancuerna no, y el bloqueo respiratorio en bisagra "
           "sostenida es lo que agrega cardiac y pelvic_floor_dysfunction a "
           "cautions. Mismo conflicto de agarre nombre/texto que 0451."),

    E("1686", "squat to overhead reach with twist", "standing", standing=True,
      bal="moderate", grip="none", oh=True, rot="moderate", flex="low",
      ext="low", lat="alternating",
      stress=js(knee="moderate", hip="moderate", lumbar="moderate",
                sh="moderate", ank="moderate"),
      pat="squat", diff=3, rom="high",
      ortho="high", change="high", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "knee_injury",
              "knee_replacement", "hip_replacement", "lumbar_disc"],
      caut=["limited_balance", "knee_pain", "hip_pain", "lumbar_pain",
            "sciatica", "si_joint_pain", "ankle_injury", "shoulder_pain",
            "cervical_injury", "neck_pain", "osteoporosis", "hypermobility",
            "osteoarthritis", "dysautonomia", "vertigo", "elderly_65plus",
            "obesity", "multiple_sclerosis", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "elbow_injury", "wrist_injury", "carpal_tunnel"],
      why="Sin carga externa y aun asi nueve contraindicaciones, porque "
           "apila tres vectores de riesgo en un solo gesto: sentadilla, "
           "brazos sobre la cabeza y rotacion de tronco. Es el ejemplo mas "
           "claro del lote de que la carga no es lo que decide la "
           "accesibilidad — la geometria si."),

    E("1740", "dumbbell standing bent over one arm triceps extension",
      "standing", standing=True, bal="moderate", grip="firm", axial="low",
      ext="low", lat="unilateral",
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
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis",
            "carpal_tunnel"],
      why="El texto pide el torso 'parallel to the ground', mas horizontal "
           "que el 1739 del lote 43, pero el brazo libre no recibe ningun "
           "rol, asi que si entra en one_arm_only. Es el unico aislado de "
           "triceps del catalogo que combina safe_for de un solo brazo con "
           "una postura sin transferencia al suelo."),

    E("1741", "dumbbell standing bent over two arm triceps extension",
      "standing", standing=True, bal="moderate", grip="firm", axial="low",
      ext="low",
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
      why="Version bilateral de 1740, identica salvo por perder "
           "one_arm_only. El par 1740/1741 es otro control limpio de D-020: "
           "la unica diferencia entre ambas fichas es la lateralidad "
           "declarada en el texto."),

    E("1742", "dumbbell tricep kickback with stork stance", "standing",
      standing=True, bal="high", sl=True, grip="firm", axial="low", ext="low",
      lat="unilateral",
      stress=js(lumbar="high", hip="moderate", ank="moderate", sh="moderate",
                el="moderate", knee="low", wr="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="high",
      metab="low", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "lumbar_disc", "lumbar_pain", "sciatica",
              "ankle_injury", "limited_grip"],
      caut=["si_joint_pain", "hip_pain", "knee_pain", "shoulder_impingement",
            "elbow_injury", "tendinitis_elbow", "plantar_fasciitis",
            "osteoporosis", "dysautonomia", "vertigo", "elderly_65plus",
            "obesity", "multiple_sclerosis", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "rotator_cuff",
            "carpal_tunnel"],
      why="Caso inverso a 0379. Aqui el nombre anuncia stork stance "
           "(unipodal) y el texto describe una bisagra normal con los dos "
           "pies apoyados. Se aplica D-021: requires_balance alimenta el "
           "filtro duro limited_balance, asi que gana la lectura restrictiva "
           "y queda bal high con sl True. Marcado para E3 — si el texto tiene "
           "razon, recupera bastante accesibilidad."),

    E("2321", "dumbbell standing inner biceps curl v. 2", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Curl con supinacion durante el recorrido. Marca 'v. 2', grupo de "
           "duplicados ya identificado. Perfil identico a 2401 y practicamente "
           "identico a 1657 del lote 44 — el catalogo tiene al menos cinco "
           "fichas distintas para el mismo curl de pie con mancuernas."),

    E("2401", "dumbbell biceps curl (with arm blaster)", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="El nombre promete arm blaster y el texto no lo menciona nunca: "
           "describe un curl de pie comun. Se clasifica el texto y por lo "
           "tanto no se declara equipo adicional. Comparar con 2403, donde el "
           "mismo accesorio si aparece en las instrucciones — el dataset es "
           "inconsistente consigo mismo dentro de la misma familia."),

    E("2403", "dumbbell alternate biceps curl (with arm blaster)", "standing",
      standing=True, bal="low", grip="firm", lat="alternating",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "shoulder_pain", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc", "rotator_cuff",
            "osteoporosis"],
      why="Aqui el arm blaster si aparece en el texto. El accesorio se apoya "
           "en la parte alta del torso y fija el humero, lo que anade "
           "shoulder_pain a cautions respecto de 2401. Tercer caso del "
           "proyecto donde el campo equipment del dataset esta incompleto "
           "(tras 1382 y 3240): dice 'dumbbell' y hacen falta dos cosas."),

    E("3156", "bodyweight standing close-grip one arm row", "standing",
      standing=True, bal="moderate", grip="firm", axial="moderate",
      ext="low", rot="low", lat="unilateral",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="low", knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="low", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "limited_grip"],
      caut=["si_joint_pain", "hip_pain", "osteoporosis", "hypertension",
            "shoulder_impingement", "elbow_injury", "osteoarthritis",
            "dysautonomia", "vertigo", "elderly_65plus", "obesity",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "ankle_injury", "plantar_fasciitis", "carpal_tunnel"],
      why="Mismo defecto que 3162 del lote 43: equipment dice 'body weight' "
           "pero el texto pide mancuerna. Clasificacion identica a 3162 salvo "
           "el agarre neutro declarado. Son duplicados funcionales y deberian "
           "colapsarse en E4."),

    E("3161", "bodyweight standing one arm row (with towel)", "standing",
      standing=True, bal="low", grip="light", axial="low", ext="low",
      lat="unilateral",
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
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "shoulder_impingement",
            "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury"],
      why="Hallazgo del lote. Version unilateral de 3165: sin carga externa, "
           "la bisagra deja de ser contraindicacion y baja a cautions, y al "
           "usar una sola mano entra ademas en one_arm_only. Es el unico "
           "tiron horizontal del catalogo que sirve simultaneamente a hernia "
           "discal, un solo brazo funcional y ausencia de equipo. Objecion "
           "pendiente para E3: con una sola mano y sin anclaje no queda claro "
           "que resiste la toalla."),

    E("3215", "hands reversed clasped circular toe touch (male)", "standing",
      standing=True, bal="moderate", grip="none", oh=True, flex="high",
      ext="moderate", rot="low",
      stress=js(lumbar="high", hip="high", sh="high", knee="moderate",
                cerv="moderate"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="high", headdown=True, valsalva="low", iso="low",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "knee_injury", "hip_pain"],
      caut=["knee_pain", "hip_replacement", "cervical_injury", "neck_pain",
            "osteoporosis", "hypermobility", "glaucoma",
            "retinal_detachment_risk", "migraine", "vertigo", "dysautonomia",
            "hypertension", "osteoarthritis", "elderly_65plus", "obesity",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "elbow_injury", "wrist_injury", "carpal_tunnel", "ankle_injury",
            "plantar_fasciitis"],
      why="El texto se contradice dos veces: dice rodillas ligeramente "
           "flexionadas y despues 'keeping your legs straight', y pide "
           "entrelazar las manos por detras de las piernas para luego "
           "subirlas por encima de la cabeza. Ese recorrido con las manos "
           "unidas es extension de hombro extrema, de ahi sh high y las tres "
           "contraindicaciones de hombro. Sumado a flexion lumbar completa y "
           "cabeza bajo el corazon, doce contraindicaciones."),

    E("3240", "exercise ball on the wall calf raise (tennis ball between knees)",
      "standing", standing=True, bal="low", grip="firm",
      stress=js(ank="high", knee="low", hip="low", lumbar="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis"],
      caut=["limited_balance", "limited_grip", "knee_pain", "hip_pain",
            "hip_replacement", "lumbar_pain", "osteoarthritis",
            "dysautonomia", "vertigo", "elderly_65plus", "varicose_veins",
            "obesity"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "sciatica", "knee_replacement", "osteoporosis"],
      why="1382 mas una pelota de tenis entre las rodillas. El apretón "
           "aductor es leve y hacia la linea media, no la cruza, pero como "
           "las precauciones tras protesis de cadera restringen aduccion se "
           "agrega hip_replacement a cautions — es la unica diferencia "
           "respecto de 1382. Empata con el como la elevacion de talon mas "
           "accesible del catalogo: cuatro contraindicaciones."),

    E("3241", "exercise ball on the wall calf raise (tennis ball between ankles)",
      "standing", standing=True, bal="low", grip="firm",
      stress=js(ank="high", knee="low", lumbar="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis"],
      caut=["limited_balance", "limited_grip", "knee_pain", "lumbar_pain",
            "osteoarthritis", "dysautonomia", "vertigo", "elderly_65plus",
            "varicose_veins", "obesity"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "sciatica", "knee_replacement", "hip_replacement",
            "osteoporosis"],
      why="Texto fisicamente imposible: manda ponerse 'facing a wall' y a "
           "continuacion colocar la pelota entre la pared y la zona lumbar. "
           "Se asume que es de espaldas, como en 3240 y 1382, porque es la "
           "unica lectura ejecutable. Con la pelota en los tobillos "
           "desaparece la aduccion de cadera y recupera hip_replacement en "
           "safe_for."),

    E("3560", "dumbbell standing alternate hammer curl and press", "standing",
      standing=True, bal="low", grip="firm", oh=True, axial="moderate",
      ext="low", lat="alternating",
      stress=js(sh="moderate", el="moderate", lumbar="moderate", wr="low",
                cerv="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead", "limited_grip"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "cervical_injury", "neck_pain", "lumbar_pain", "elbow_injury",
            "tendinitis_elbow", "osteoporosis", "hypertension",
            "hypermobility", "dysautonomia", "vertigo", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica", "lumbar_disc",
            "carpal_tunnel"],
      why="Combinado curl mas press. El patron se clasifica como "
           "vertical_push y no isolation porque el press es lo que define "
           "las restricciones. Agarre neutro en ambas fases, asi que aplica "
           "la misma regla que 0424: impingement y manguito quedan en "
           "cautions, y no_overhead sigue siendo contraindicacion dura."),
]


CONFIDENCE_OVERRIDES = {
    "1742": 0.65,  # nombre dice stork stance, texto describe dos pies apoyados
    "0451": 0.70,  # nombre reverse grip, texto underhand
    "0118": 0.70,  # nombre reverse grip, texto overhand
    "2401": 0.70,  # arm blaster en el nombre, ausente del texto
    "3241": 0.70,  # texto imposible: facing a wall con pelota lumbar
    "0111": 0.75,  # "rocking leg" no aparece en el texto
    "3156": 0.75,  # equipment body weight pero el texto pide mancuerna
    "3161": 0.75,  # toalla a una mano sin anclaje: que resiste?
    "3215": 0.75,  # texto contradictorio sobre rodillas rectas o flexionadas
    "1435": 0.85,  # el texto no confirma barra baja
    "2321": 0.85,  # marca v. 2
    "3240": 0.85,  # equipment incompleto: pelota y pelota de tenis
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
    print(f"lote 45: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
