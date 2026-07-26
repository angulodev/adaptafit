#!/usr/bin/env python3
"""Lote 41 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("2143", "dumbbell standing around world", "standing", standing=True,
      bal="low", oh=True, grip="firm",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "hypermobility"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "neck_pain", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "hypertension", "elderly_65plus",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "sciatica"],
      why="El brazo recorre el arco completo de abduccion en circulo "
           "continuo y con peso, sin pasar por ninguna posicion de descanso. "
           "joint_laxity_risk high: pasa por el arco doloroso en cada "
           "repeticion y ademas suma rotacion bajo carga. Para el mismo "
           "musculo, 0334 dumbbell lateral raise hace menos daño."),

    E("3212", "basic toe touch (male)", "standing", standing=True, bal="low",
      flex="high", headdown=True,
      stress=js(lumbar="high", hip="high", knee="low"),
      pat="mobility_stretch", diff=1, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="low", laxity="moderate", pelvic="low", temp="none",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "osteoporosis", "hip_replacement"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hypermobility",
            "knee_injury", "glaucoma", "retinal_detachment_risk",
            "hypertension", "dysautonomia", "vertigo", "elderly_65plus",
            "limited_balance", "varicose_veins", "obesity", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "ankle_injury", "plantar_fasciitis"],
      why="Flexion espinal completa de pie y sin apoyo: la posicion clasica "
           "de fractura vertebral por compresion, por eso osteoporosis entra "
           "a contraindicacion aunque no haya peso externo. Contraste con "
           "1511 hamstring stretch, que apoya la mano en el muslo y reparte "
           "el plegado en la cadera: mismo objetivo muscular, mucho menos "
           "riesgo espinal."),

    E("3213", "side-to-side toe touch (male)", "standing", standing=True,
      bal="low", flex="moderate", rot="moderate",
      stress=js(lumbar="high", hip="moderate", knee="low"),
      pat="core_rotation", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "osteoporosis", "si_joint_pain"],
      caut=["lumbar_pain", "hip_pain", "hypermobility", "limited_balance",
            "cervical_injury", "dysautonomia", "vertigo", "elderly_65plus",
            "hernia_abdominal", "obesity", "pelvic_floor_dysfunction",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Flexion lateral repetida con impulso. Para un disco es peor que "
           "3212 basic toe touch, no mejor: la carga cae asimetrica sobre un "
           "solo lado del anillo fibroso y el impulso quita el control "
           "excentrico. Se clasifica core_rotation porque la taxonomia no "
           "tiene flexion lateral —vacio a resolver en v1.3."),

    E("0311", "dumbbell full can lateral raise", "standing", standing=True,
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
      why="Aplicacion inversa del criterio de lectura estricta. 'Full can' "
           "designa la variante con pulgar arriba, que es la amable para el "
           "manguito —pero el texto no menciona rotacion externa en ningun "
           "lado y describe una elevacion lateral comun. No se concede el "
           "beneficio de seguridad que el nombre sugiere: se clasifica como "
           "0334 y shoulder_impingement queda contraindicado. Si E3 confirma "
           "el pulgar arriba, este registro mejora."),

    E("0312", "dumbbell hammer curl v. 2", "standing", standing=True,
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
      why="El nombre dice martillo pero el texto dice rotar las palmas hasta "
           "que miren al frente antes de flexionar: eso es un curl supinado, "
           "o sea 0294. Se toma la lectura estricta y carpal_tunnel queda en "
           "precaucion, no en safe_for como en 0313 dumbbell hammer curl. "
           "Sexta entrada de la familia de curl de pie."),

    E("0409", "dumbbell single leg calf raise", "standing", standing=True,
      bal="moderate", sl=True, grip="firm",
      stress=js(ank="high", knee="low", hip="low", lumbar="low"),
      lat="unilateral", pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis", "limited_grip"],
      caut=["limited_balance", "knee_pain", "hip_pain", "hip_replacement",
            "osteoarthritis", "dysautonomia", "vertigo", "varicose_veins",
            "elderly_65plus", "osteoporosis", "lumbar_pain"],
      safe=["no_overhead", "shoulder_impingement", "rotator_cuff",
            "wrist_injury", "carpal_tunnel", "elbow_injury", "lumbar_disc",
            "sciatica", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "hernia_abdominal"],
      why="Octavo y ultimo escalon de la familia de gemelo: una pierna, "
           "talon colgando del escalon y mancuerna en la mano libre. Junta "
           "las tres exigencias que los escalones anteriores tenian por "
           "separado —unipodal de 1387, dorsiflexion completa de 0833, carga "
           "externa de 0417— pero sin carga axial, asi que lumbar_disc sigue "
           "en safe_for. Es el techo de la escalera, no el atajo."),

    E("0026", "barbell bench squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                cerv="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="low",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip", "lumbar_disc",
              "lumbar_pain", "sciatica", "osteoporosis", "cervical_injury",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["osteoarthritis", "hip_pain", "si_joint_pain", "ankle_injury",
            "plantar_fasciitis", "limited_balance", "dysautonomia",
            "hypertension", "cardiac", "glaucoma", "elderly_65plus",
            "obesity", "hernia_abdominal", "multiple_sclerosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury"],
      why="El nombre promete banco —tope de profundidad y descanso por "
           "repeticion, como en 0291 dumbbell bench squat— pero el texto "
           "describe salir de un rack y hacer una sentadilla libre completa "
           "con barra. Lectura estricta: se clasifica como sentadilla con "
           "barra, difficulty 4, no como la regresion que el nombre sugiere. "
           "Es el caso donde equivocarse hacia el lado amable seria peor."),

    E("0988", "band one arm standing low row", "standing", standing=True,
      bal="low", grip="light", flex="low",
      stress=js(lumbar="moderate", hip="moderate", sh="moderate",
                el="moderate"),
      lat="unilateral", pat="horizontal_pull", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="high", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hip_replacement",
            "shoulder_impingement", "shoulder_pain", "elbow_injury",
            "limited_grip", "hypertension", "dysautonomia", "elderly_65plus",
            "obesity", "osteoporosis", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "wrist_injury", "carpal_tunnel", "one_arm_only"],
      why="Version a un brazo de 1022 band standing rear delt row: misma "
           "bisagra suave con banda, mismo isometrico lumbar moderado. Lo "
           "que cambia es que one_arm_only entra en safe_for. Sigue siendo "
           "de los pocos tirones horizontales ofrecibles a un perfil lumbar "
           "de riesgo medio."),

    E("3644", "weighted lunge with swing", "standing", standing=True,
      bal="high", sl=True, oh=True, grip="firm", impact="low",
      lat="alternating",
      stress=js(knee="high", hip="moderate", sh="high", lumbar="high",
                ank="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="high", laxity="high", pelvic="moderate", gripdur="high",
      temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "lumbar_disc",
              "sciatica", "osteoporosis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_pain", "lumbar_pain", "si_joint_pain", "hip_pain",
            "osteoarthritis", "plantar_fasciitis", "hypermobility",
            "dysautonomia", "vertigo", "elderly_65plus", "multiple_sclerosis",
            "obesity", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "wrist_injury",
            "carpal_tunnel", "elbow_injury"],
      why="Dos patrones exigentes al mismo tiempo: zancada mas swing "
           "balistico de brazos hasta arriba. El impulso de las mancuernas "
           "hacia adelante tira del tronco justo cuando el equilibrio esta "
           "en su punto mas fragil, y el hombro tiene que frenar el peso al "
           "final del arco. Es peor que la suma de 0336 y una elevacion "
           "frontal por separado."),

    E("0115", "barbell stiff leg good morning", "standing", standing=True,
      bal="low", grip="firm", axial="high", flex="moderate",
      stress=js(lumbar="high", hip="high", cerv="moderate", knee="low"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "hip_replacement",
              "hernia_abdominal", "cervical_injury", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "hypermobility", "knee_pain", "hypertension",
            "cardiac", "glaucoma", "retinal_detachment_risk", "dysautonomia",
            "elderly_65plus", "obesity", "pelvic_floor_dysfunction",
            "limited_balance", "vertigo"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "knee_injury", "ankle_injury",
            "plantar_fasciitis"],
      why="El brazo de palanca lumbar mas largo del catalogo. En 0116 "
           "barbell straight leg deadlift la barra cuelga de las manos y baja "
           "con el torso; aca va apoyada en el trapecio, o sea en el extremo "
           "opuesto de la palanca, y se queda ahi mientras el tronco llega a "
           "la horizontal. Mismo patron de bisagra, momento sobre la columna "
           "muy superior."),

    E("1654", "dumbbell biceps curl reverse", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="high", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel"],
      caut=["rheumatoid_arthritis", "hypermobility", "osteoarthritis",
            "shoulder_pain", "lumbar_pain", "dysautonomia", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica"],
      why="Curl invertido sin ambiguedad: el texto dice palmas hacia abajo. "
           "Agarre pronado bajo carga, con los extensores de muñeca "
           "trabajando en desventaja: wrist high y wrist_injury y "
           "carpal_tunnel contraindicados, igual que en 0439 dumbbell zottman "
           "curl. Este registro valida la lectura estricta que se aplico a "
           "0429, donde el texto era ambiguo."),

    E("1675", "dumbbell reverse spider curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="high", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel"],
      caut=["rheumatoid_arthritis", "hypermobility", "osteoarthritis",
            "shoulder_pain", "lumbar_pain", "dysautonomia", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica"],
      why="El peor caso de nombre contra texto del pipeline: el nombre "
           "promete dos cosas —invertido Y spider, o sea brazo apoyado en "
           "banco— y el texto no describe ninguna, solo un curl de pie con "
           "palmas al cuerpo. Se resuelve tomando lo mas restrictivo de cada "
           "eje: agarre pronado como 1654, sin apoyo de codo. Confianza 0,60, "
           "la mas baja del pipeline."),

    E("1685", "squat to overhead reach", "standing", standing=True,
      bal="low", oh=True,
      stress=js(knee="high", hip="moderate", sh="moderate", ank="moderate",
                lumbar="low"),
      pat="squat", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "no_overhead",
              "shoulder_impingement", "rotator_cuff"],
      caut=["osteoarthritis", "hip_pain", "ankle_injury", "plantar_fasciitis",
            "limited_balance", "lumbar_pain", "shoulder_pain",
            "dysautonomia", "elderly_65plus", "obesity", "osteoporosis",
            "hypertension", "vertigo"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "elbow_injury", "one_arm_only",
            "lumbar_disc", "sciatica"],
      why="Sentadilla sin carga mas alcance sobre la cabeza. Sin peso ni "
           "agarre, asi que muñeca y mano quedan libres —limited_grip y "
           "carpal_tunnel en safe_for— pero el alcance overhead mete al "
           "hombro en el filtro para algo que es un ejercicio de pierna. Si "
           "el hombro es el problema, 3132 potty squat with support entrega "
           "la sentadilla sin esa restriccion."),

    E("2808", "dumbbell sumo pull through", "standing", standing=True,
      bal="low", grip="firm", flex="moderate",
      stress=js(hip="high", knee="high", lumbar="moderate", ank="moderate"),
      pat="hinge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "hip_replacement", "hip_pain",
              "limited_grip", "lumbar_disc", "sciatica", "osteoporosis",
              "knee_replacement", "si_joint_pain", "pregnancy_3rd"],
      caut=["knee_injury", "knee_pain", "lumbar_pain", "osteoarthritis",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "dysautonomia", "hypertension", "elderly_65plus", "obesity",
            "pelvic_floor_dysfunction", "hernia_abdominal", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Comparten nombre con 0991 band pull through y son casi opuestos "
           "en riesgo. Alla la banda tiraba en horizontal y quedaban dos "
           "contraindicaciones; aca la mancuerna cuelga en vertical entre las "
           "piernas y la base sumo exige abduccion y rotacion externa de "
           "cadera, asi que hip_replacement y hip_pain suben a "
           "contraindicacion como en 0124 barbell wide squat. El nombre no "
           "predice el riesgo."),

    E("2812", "dumbbell step-up split squat", "standing", standing=True,
      bal="high", sl=True, grip="firm", impact="low", lat="alternating",
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
            "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Tercer registro de step-up con mancuernas junto a 0431 y 2796; el "
           "'split squat' del nombre no aparece en el texto, que describe "
           "subir al cajon con un pie. Se clasifica igual que 0431. "
           "visual_impairment contraindicado por tener que calcular la altura "
           "del escalon."),

    E("3132", "potty squat with support", "standing", standing=True,
      bal="low", grip="light",
      stress=js(knee="high", hip="high", ank="high", lumbar="low"),
      pat="squat", diff=1, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="moderate", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "knee_replacement",
              "hip_replacement"],
      caut=["knee_injury", "knee_pain", "osteoarthritis", "hip_pain",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "lumbar_pain", "si_joint_pain", "dysautonomia", "elderly_65plus",
            "obesity", "osteoporosis", "limited_grip", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "lumbar_disc",
            "sciatica"],
      why="Hallazgo del lote y caso raro en el catalogo: rom_demand high con "
           "difficulty 1. La silla se lleva el equilibrio y parte del peso, "
           "asi que se accede al rango completo de cadera y tobillo sin "
           "exigencia de fuerza. Para movilidad de cadera, suelo pelvico y "
           "recuperar la sentadilla profunda en perfil mayor, es de lo mas "
           "util que hay. Solo cuatro contraindicaciones, todas de Capa A."),

    E("3158", "bodyweight standing close-grip row", "standing",
      standing=True, bal="low", grip="firm", flex="low",
      stress=js(lumbar="moderate", sh="moderate", el="moderate",
                hip="moderate"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="high", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hip_replacement",
            "shoulder_impingement", "shoulder_pain", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "hypertension", "dysautonomia",
            "elderly_65plus", "obesity", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="E1 marco grip_required none pero el texto dice agarrar la barra o "
           "las manijas: se corrige a firm por lectura estricta, porque dar "
           "limited_grip por seguro cuando hace falta agarre es exactamente "
           "el error caro. A diferencia de 3166 bodyweight standing row, aca "
           "el tronco va inclinado, asi que aparece isometrico lumbar y "
           "lumbar_disc sale de safe_for."),

    E("3543", "bodyweight drop jump squat", "standing", standing=True,
      bal="moderate", impact="high",
      stress=js(knee="high", hip="moderate", lumbar="moderate", ank="high"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "osteoarthritis", "vertigo",
              "elderly_65plus", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "dysautonomia", "hypertension", "cardiac", "obesity",
            "chronic_fatigue", "asthma", "varicose_veins",
            "multiple_sclerosis", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Salto con aterrizaje y caida inmediata a la siguiente repeticion, "
           "sin pausa para absorber. La instruccion de caer sobre la punta y "
           "bajar de inmediato es lo que sube el tobillo a high y saca a "
           "elderly_65plus de precaucion a contraindicacion, cosa que en "
           "0513 jump squat v.2 no pasaba: alli cada repeticion empieza "
           "desde parado."),
]

CONFIDENCE_OVERRIDES = {
    "1675": 0.60,  # nombre promete "reverse" y "spider"; el texto no da ninguna
    "0026": 0.65,  # nombre dice banco, texto describe sentadilla libre con barra
    "0312": 0.65,  # nombre dice martillo, texto describe curl supinado
    "0311": 0.70,  # nombre dice "full can"; el texto no menciona rotacion externa
    "3158": 0.70,  # E1 dice grip none, el texto dice agarrar barra o manijas
    "2812": 0.75,  # nombre dice split squat, texto describe step-up (0431)
    "3213": 0.75,  # la taxonomia no tiene flexion lateral; se mapea a core_rotation
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
    print(f"lote 41: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
