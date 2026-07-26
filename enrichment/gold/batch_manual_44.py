#!/usr/bin/env python3
"""Lote 44 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1377", "calf stretch with hands against wall", "standing",
      standing=True, bal="low", grip="none", lat="alternating",
      stress=js(ank="moderate", knee="low", hip="low", sh="low", wr="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="none", iso="high", metab="low",
      laxity="low", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["limited_balance", "wrist_injury", "carpal_tunnel", "knee_pain",
            "osteoarthritis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip", "plantar_fasciitis",
            "lumbar_disc", "sciatica", "hip_replacement", "knee_replacement",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "osteoporosis"],
      why="Estiramiento de gemelo contra pared. Va a safe_for de "
           "plantar_fasciitis a proposito y en contra del sesgo conservador "
           "habitual: el estiramiento de gastrocnemio es tratamiento de "
           "primera linea para fascitis plantar, no un riesgo. Las manos "
           "planas en la pared no exigen agarre pero si extension de muneca, "
           "por eso wrist_injury queda en cautions. No entra one_arm_only "
           "(D-020): el texto asigna rol a ambas manos."),

    E("1407", "calf push stretch with hands against wall", "standing",
      standing=True, bal="low", grip="none", lat="alternating",
      stress=js(ank="moderate", knee="low", hip="low", sh="low", wr="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="none", iso="high", metab="low",
      laxity="low", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["limited_balance", "wrist_injury", "carpal_tunnel", "knee_pain",
            "osteoarthritis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip", "plantar_fasciitis",
            "lumbar_disc", "sciatica", "hip_replacement", "knee_replacement",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "osteoporosis"],
      why="Duplicado funcional exacto de 1377. La unica diferencia textual es "
           "'bend your front knee slightly' contra 'bend your left knee y "
           "lean forward'. Misma posicion, mismo musculo, mismo apoyo. "
           "Clasificacion identica deliberadamente para que E4 los colapse."),

    E("3214", "arms apart circular toe touch (male)", "standing",
      standing=True, bal="high", sl=True, grip="none", flex="high",
      rot="moderate", lat="alternating",
      stress=js(lumbar="high", hip="high", knee="moderate", ank="moderate",
                sh="low"),
      pat="hinge", diff=4, rom="high",
      ortho="high", change="high", headdown=True, valsalva="low",
      iso="moderate", metab="moderate", laxity="high", pelvic="moderate",
      gripdur="none", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "lumbar_disc", "lumbar_pain", "sciatica",
              "si_joint_pain", "hip_pain", "knee_injury", "knee_replacement",
              "hip_replacement", "ankle_injury"],
      caut=["osteoporosis", "hypermobility", "glaucoma",
            "retinal_detachment_risk", "migraine", "vertigo", "dysautonomia",
            "elderly_65plus", "obesity", "multiple_sclerosis", "hypertension",
            "osteoarthritis", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel"],
      why="El peor ejercicio del lote y candidato al peor del catalogo para "
           "columna: flexion completa con piernas rectas, mas rotacion, mas "
           "apoyo unipodal, mas cabeza por debajo del corazon. Trece "
           "contraindicaciones. Flexion mas rotacion bajo carga es "
           "exactamente el mecanismo de fractura vertebral por compresion en "
           "osteoporosis. Sufijo '(male)' — duplicado de genero probable."),

    E("0851", "weighted sissy squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="moderate",
      stress=js(knee="high", hip="moderate", lumbar="moderate",
                ank="moderate", sh="low", wr="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement", "hip_pain",
              "ankle_injury", "lumbar_disc", "limited_grip"],
      caut=["lumbar_pain", "sciatica", "si_joint_pain", "osteoarthritis",
            "osteoporosis", "hypertension", "hernia_abdominal",
            "pelvic_floor_dysfunction", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "carpal_tunnel"],
      why="La contradiccion mas grave del lote. Una sissy squat lleva las "
           "rodillas muy por delante de los pies con el torso inclinado "
           "hacia atras: es de los ejercicios de mayor cizalla rotuliana que "
           "existen. El texto describe una sentadilla goblet comun. Se aplica "
           "D-021 y se toma la lectura restrictiva en el campo de seguridad: "
           "knee high. confidence 0,60, prioridad alta en E3."),

    E("0636", "olympic barbell hammer curl", "standing", standing=True,
      bal="low", grip="firm", axial="low", ext="low",
      stress=js(el="high", wr="high", lumbar="moderate", sh="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="none", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "wrist_injury",
              "carpal_tunnel", "tendinitis_elbow", "elbow_injury"],
      caut=["shoulder_pain", "lumbar_pain", "lumbar_disc", "hypertension",
            "rheumatoid_arthritis", "osteoarthritis", "hypermobility",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "shoulder_impingement",
            "rotator_cuff", "osteoporosis"],
      why="El nombre es imposible: una barra olimpica no permite agarre "
           "neutro, que es lo que define un hammer curl. El texto confirma "
           "agarre prono, o sea un curl invertido. Barra recta mas pronacion "
           "mas 20 kg de barra vacia pone muneca y codo en high — la unica "
           "combinacion del lote donde el implemento, y no el musculo, define "
           "las contraindicaciones."),

    E("1344", "ez bar reverse grip bent over row", "standing", standing=True,
      bal="moderate", grip="firm", axial="moderate", ext="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="moderate", knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "limited_grip", "tendinitis_elbow"],
      caut=["si_joint_pain", "hip_pain", "osteoporosis", "hernia_abdominal",
            "shoulder_impingement", "elbow_injury", "wrist_injury",
            "carpal_tunnel", "hypertension", "dysautonomia", "vertigo",
            "elderly_65plus", "obesity", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis"],
      why="Remo inclinado con supinacion: la barra EZ queda en el medio de la "
           "escala de implemento para muneca, pero el agarre supino carga el "
           "tendon distal del biceps y el epicondilo medial durante todo el "
           "tiron. Por eso tendinitis_elbow es contraindicacion aqui y solo "
           "cautions en los remos pronos del lote 43."),

    E("0421", "dumbbell standing one arm concentration curl", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low", hip="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "lumbar_pain", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Segundo caso de prueba de D-020, y mas sutil que 0356: 'place your "
           "free hand on your thigh for support'. El apoyo es en el propio "
           "muslo, no en un objeto externo, y no afecta el equilibrio en "
           "absoluto — pero el texto le asigna un rol a la segunda mano, asi "
           "que one_arm_only queda fuera. Si E3 confirma que el apoyo es "
           "prescindible, este es el primero que deberia recuperarlo."),

    E("0425", "dumbbell standing one arm reverse curl", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip",
              "tendinitis_elbow"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel",
            "rheumatoid_arthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Control positivo de D-020: mismo patron que 0421 pero el texto no "
           "menciona la mano libre en ningun rol, asi que si entra en "
           "one_arm_only. El par 0421/0425 es la demostracion limpia de que "
           "la regla discrimina por texto y no por lateralidad."),

    E("0727", "single leg calf raise (on a dumbbell)", "standing",
      standing=True, bal="high", sl=True, grip="firm", lat="unilateral",
      stress=js(ank="high", knee="low", hip="low", wr="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "ankle_injury", "plantar_fasciitis"],
      caut=["limited_grip", "knee_pain", "osteoarthritis", "dysautonomia",
            "vertigo", "elderly_65plus", "multiple_sclerosis", "obesity",
            "varicose_veins"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "carpal_tunnel", "lumbar_disc", "sciatica", "hip_replacement",
            "osteoporosis"],
      why="El nombre sugiere pararse sobre la mancuerna; el texto dice "
           "sostenerla en una mano. Se clasifica el texto. Comparar con 1000 "
           "del lote 43: mismo gesto unipodal, pero alli el texto ofrece "
           "agarrarse de algo y limited_balance baja a cautions. Aqui no hay "
           "apoyo y queda contraindicado. Dos fichas separadas por una sola "
           "frase de apoyo."),

    E("0968", "band alternating biceps curl", "standing", standing=True,
      bal="low", grip="light", lat="alternating",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "carpal_tunnel", "hypermobility", "dysautonomia",
            "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Banda elastica, carga autolimitada, alternado, sin cambio de "
           "posicion. Empata con 1670 del lote 43 como suelo de accesibilidad "
           "para biceps de pie, con la ventaja de que la banda regula sola la "
           "intensidad. difficulty 1."),

    E("1329", "dumbbell palm rotational bent over row", "standing",
      standing=True, bal="moderate", grip="firm", axial="moderate", ext="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="moderate", knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "limited_grip"],
      caut=["si_joint_pain", "hip_pain", "osteoporosis", "hernia_abdominal",
            "shoulder_impingement", "elbow_injury", "tendinitis_elbow",
            "wrist_injury", "carpal_tunnel", "hypertension", "dysautonomia",
            "vertigo", "elderly_65plus", "obesity", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis"],
      why="Tercer remo inclinado del lote. La rotacion de palma bajo carga "
           "sube muneca a moderate respecto de un remo prono normal, pero el "
           "filtro dominante sigue siendo la bisagra sostenida. Los tres "
           "remos del lote comparten exactamente las mismas seis "
           "contraindicaciones de columna."),

    E("1382", "exercise ball on the wall calf raise", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(ank="high", knee="low", lumbar="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis"],
      caut=["limited_balance", "limited_grip", "knee_pain", "lumbar_pain",
            "osteoarthritis", "dysautonomia", "vertigo", "elderly_65plus",
            "varicose_veins", "obesity"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "sciatica", "hip_replacement", "knee_replacement",
            "osteoporosis"],
      why="Espalda contra la pared con pelota lumbar: el apoyo es el mas "
           "completo del lote y baja el balance a low pese a estar de pie. "
           "Es la elevacion de talon mas accesible de los cuatro que trae "
           "este lote. El equipo del dataset dice 'dumbbell' pero requiere "
           "ademas pelota y pared — corregir en E3."),

    E("1490", "standing calf raise (on a staircase)", "standing",
      standing=True, bal="moderate", grip="none",
      stress=js(ank="high", knee="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "visual_impairment",
              "ankle_injury", "plantar_fasciitis"],
      caut=["limited_balance", "knee_pain", "osteoarthritis", "dysautonomia",
            "vertigo", "elderly_65plus", "multiple_sclerosis", "obesity",
            "varicose_veins"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip", "one_arm_only",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "lumbar_disc", "sciatica",
            "hip_replacement", "knee_replacement", "osteoporosis"],
      why="Talones colgando del borde de un escalon: rom_demand high, el "
           "unico del lote entre las elevaciones de talon. visual_impairment "
           "pasa a contraindicacion y no a cautions — el riesgo no es el "
           "ejercicio sino el borde del escalon, y una caida por escalera es "
           "un desenlace de otra magnitud. El apoyo del texto es condicional "
           "('if needed'), por eso el balance queda moderate y no low."),

    E("1649", "dumbbell alternating bicep curl with leg raised on exercise ball",
      "standing", standing=True, bal="high", sl=True, grip="firm",
      lat="alternating",
      stress=js(el="moderate", ank="moderate", knee="moderate",
                hip="moderate", lumbar="moderate", wr="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "ankle_injury", "knee_injury",
              "hip_replacement", "limited_grip"],
      caut=["knee_pain", "hip_pain", "lumbar_pain", "si_joint_pain",
            "plantar_fasciitis", "elbow_injury", "tendinitis_elbow",
            "osteoarthritis", "osteoporosis", "hypermobility", "dysautonomia",
            "vertigo", "elderly_65plus", "multiple_sclerosis", "obesity"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "wrist_injury", "carpal_tunnel"],
      why="Un curl de biceps con ocho contraindicaciones, todas de tren "
           "inferior. El ejercicio de brazo no cambio; le agregaron un pie "
           "sobre una pelota inestable. Junto con 1653 forman una familia que "
           "conviene marcar en E4: el sustituto correcto no es otro curl mas "
           "facil, es el mismo curl sin el truco de equilibrio — 0968 o 1670."),

    E("1653", "dumbbell bicep curl with stork stance", "standing",
      standing=True, bal="high", sl=True, grip="firm",
      stress=js(el="moderate", ank="moderate", hip="moderate", knee="low",
                lumbar="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance",
              "visual_impairment", "ankle_injury", "limited_grip"],
      caut=["knee_pain", "hip_pain", "plantar_fasciitis", "elbow_injury",
            "tendinitis_elbow", "osteoarthritis", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "wrist_injury", "carpal_tunnel", "lumbar_disc",
            "sciatica", "osteoporosis"],
      why="Version mas benigna de 1649: la pierna trasera apoya la punta del "
           "pie en el suelo en vez de una pelota, asi que hay un tercer punto "
           "de contacto estable. Dos contraindicaciones menos y recupera "
           "lumbar_disc y sciatica en safe_for. La diferencia entre ambos "
           "mide exactamente lo que cuesta la superficie inestable."),

    E("1657", "dumbbell cross body hammer curl v. 2", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "wrist_injury",
            "hypermobility", "dysautonomia", "elderly_65plus",
            "hypertension"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "carpal_tunnel",
            "osteoporosis"],
      why="Agarre neutro cruzado al hombro contrario. El neutro mantiene la "
           "muneca en low y permite carpal_tunnel en safe_for, cosa que el "
           "curl invertido 0425 no consigue. Marca 'v. 2' — grupo de "
           "duplicados ya identificado en el catalogo."),

    E("1667", "dumbbell one arm reverse spider curl", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip",
              "tendinitis_elbow"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel",
            "rheumatoid_arthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Un spider curl real se hace en decubito prono sobre un banco "
           "inclinado — start_position bench_prone, no standing. El texto "
           "describe estar de pie y no menciona banco alguno. Clasificado de "
           "pie queda como duplicado exacto de 0425. La version real, si "
           "existe, seria bastante mas accesible para equilibrio y bastante "
           "menos para quien no puede tumbarse boca abajo."),

    E("1671", "dumbbell one arm standing hammer curl", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["elbow_injury", "tendinitis_elbow", "hypermobility",
            "dysautonomia", "elderly_65plus", "hypertension"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "osteoporosis"],
      why="El nombre dice 'one arm' y el texto dice 'a dumbbell in each hand'. "
           "laterality no es campo de seguridad, asi que aqui manda la regla "
           "5 y no D-021: se clasifica bilateral segun el texto, y en "
           "consecuencia one_arm_only queda fuera de safe_for. Duplicado "
           "funcional de 1657 sin el cruce al hombro contrario."),
]


CONFIDENCE_OVERRIDES = {
    "0851": 0.60,  # sissy squat: el texto describe una sentadilla comun
    "0636": 0.65,  # hammer curl imposible con barra olimpica
    "1667": 0.65,  # spider curl es bench_prone, el texto dice de pie
    "1671": 0.65,  # nombre one arm, texto dice mancuerna en cada mano
    "0727": 0.75,  # "on a dumbbell" sin resolver
    "1407": 0.85,  # duplicado funcional de 1377
    "1657": 0.85,  # marca v. 2
    "1382": 0.85,  # equipo mal declarado: requiere pelota y pared
    "3214": 0.90,  # sufijo (male), duplicado de genero probable
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
    print(f"lote 44: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
