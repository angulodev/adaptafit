#!/usr/bin/env python3
"""Lote 23 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0346", "dumbbell lying one arm supinated triceps extension",
      "bench_supine", oh=True, grip="firm", lat="unilateral",
      stress=js(el="high", sh="moderate", wr="high"),
      pat="isolation", diff=3, rom="high",
      ortho="none", change="low", valsalva="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "limited_grip", "cannot_lie_supine",
              "cannot_transfer_to_bench", "no_overhead",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypermobility", "cervical_injury",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "one_arm_only", "plantar_fasciitis"],
      why="Gemelo supinado de 0344 (lote 22). Unica diferencia real: el agarre "
           "invertido sostiene la mancuerna con el antebrazo en supinacion "
           "sobre la cara, lo que sube wr de moderate a high y mueve "
           "carpal_tunnel de cautions a contra. El resto es identico."),

    E("0453", "ez barbell seated triceps extension", "seated", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="low", wr="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "cervical_injury", "neck_pain", "hypertension",
            "hypermobility", "osteoporosis", "dysautonomia", "lumbar_pain",
            "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="Version con barra EZ de 2188. El texto dice 'back straight' y no "
           "menciona respaldo: cannot_sit_unsupported a contra y ortho "
           "moderate, igual que su gemelo con mancuerna. La barra EZ mantiene "
           "wr en low, a diferencia de la barra recta."),

    E("0339", "dumbbell lying femoral", "supine", floor=True, grip="light",
      stress=js(knee="moderate", hip="moderate", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="moderate", gripdur="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "knee_injury",
              "knee_replacement", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "lumbar_disc", "lumbar_pain", "hip_pain",
            "osteoarthritis", "hernia_abdominal", "sciatica"],
      safe=["cannot_stand", "limited_balance", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "elbow_injury", "ankle_injury", "dysautonomia",
            "plantar_fasciitis"],
      why="TEXTO INCOHERENTE: dice que la mancuerna descansa sobre el abdomen y "
           "que al flexionar las rodillas se la lleva hacia los gluteos, con "
           "los pies planos en el suelo. Mecanicamente no se sostiene — la "
           "mancuerna no se mueve con las rodillas. Clasificado de forma "
           "conservadora como flexion de rodilla en decubito. Confianza 0.55, "
           "la mas baja del proyecto. Prioridad alta para revision en E3."),

    E("2802", "twisted leg raise", "supine", floor=True, grip="none",
      flex="high", rot="high", lat="alternating",
      stress=js(lumbar="high", hip="high", cerv="low"),
      pat="core_rotation", diff=4, rom="high",
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
      why="Piernas rectas elevadas MAS torsion de cadera: el peor caso lumbar "
           "de los ejercicios de suelo. flex high y rot high a la vez, con el "
           "brazo de palanca completo de las piernas. Las manos bajo los "
           "gluteos son justamente la senal de que la lumbar no aguanta sola."),

    E("1763", "shoulder grip pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "cannot_stand", "one_arm_only"],
      caut=["hypermobility", "osteoporosis", "obesity", "elderly_65plus",
            "shoulder_pain", "tendinitis_elbow", "rheumatoid_arthritis",
            "chronic_fatigue", "cervical_injury"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="Dominada estandar con agarre al ancho de hombros. Tercera entrada "
           "identica de la familia (0678, 0720, 1763): el dataset tiene varios "
           "nombres distintos para el mismo ejercicio. Vale marcarlos como "
           "duplicados funcionales para que E4 no ofrezca tres veces lo mismo."),

    E("3662", "pike-to-cobra push-up", "plank", floor=True, oh=True,
      grip="none", ext="high", bal="moderate",
      stress=js(sh="high", wr="high", lumbar="high", el="moderate",
                cerv="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="none", change="high", headdown=True, valsalva="moderate",
      iso="moderate", metab="high", laxity="high", pelvic="moderate",
      gripdur="none", temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "no_overhead", "lumbar_disc", "lumbar_pain",
              "sciatica", "cannot_get_on_floor", "cannot_lie_prone",
              "hypermobility", "osteoporosis", "glaucoma",
              "retinal_detachment_risk", "hernia_abdominal",
              "recent_abdominal_surgery", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["elbow_injury", "cervical_injury", "neck_pain", "si_joint_pain",
            "obesity", "elderly_65plus", "chronic_fatigue", "vertigo",
            "dysautonomia", "hypertension", "shoulder_pain"],
      safe=["cannot_stand", "limited_grip", "knee_injury", "knee_pain",
            "hip_replacement", "ankle_injury"],
      why="Flujo completo: pike (cadera arriba, cabeza abajo, hombro en flexion "
           "maxima) → flexion → cobra (extension lumbar maxima). "
           "position_change high y head_below_heart por la fase de pike. "
           "spinal_extension high por la cobra — es el unico del lote donde la "
           "lumbar se lesiona por EXTENSION y no por flexion."),

    E("0501", "jack burpee", "standing", floor=True, standing=True,
      bal="moderate", oh=True, grip="none", impact="high",
      stress=js(knee="high", ank="high", wr="high", sh="moderate",
                lumbar="moderate", hip="moderate"),
      pat="cardio_interval", diff=5, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", gripdur="none",
      temp="high",
      contra=["cannot_stand", "wheelchair", "cannot_get_on_floor",
              "cannot_lie_prone", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "wrist_injury", "carpal_tunnel", "osteoporosis", "hip_replacement",
              "cardiac", "no_overhead", "shoulder_impingement",
              "pelvic_floor_dysfunction", "hernia_abdominal",
              "recent_abdominal_surgery", "plantar_fasciitis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "dysautonomia", "obesity", "elderly_65plus",
            "chronic_fatigue", "fibromyalgia", "multiple_sclerosis",
            "lumbar_disc", "lumbar_pain", "postpartum", "asthma", "epilepsy",
            "migraine"],
      safe=[],
      why="QUINTO safe_for vacio. Burpee con salto: impact high, metab high, "
           "temp high, position_change high y ortho high — el unico ejercicio "
           "del proyecto que satura cinco ejes fisiologicos a la vez. 23 "
           "contraindicaciones, record del dataset. Es el extremo opuesto de "
           "neck side stretch."),

    E("0720", "side-to-side chin", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "cannot_stand", "one_arm_only"],
      caut=["hypermobility", "osteoporosis", "obesity", "elderly_65plus",
            "shoulder_pain", "tendinitis_elbow", "rheumatoid_arthritis",
            "cervical_injury", "chronic_fatigue"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="CORRECCION A E1: E1 dijo standing por 'stand with your feet...' en "
           "la primera frase, pero el texto sigue con 'hang from the bar'. "
           "Tercer caso identico en la familia de suspension (0688, 0678, "
           "0720): E1 tiene un sesgo sistematico y lee la frase de "
           "aproximacion como posicion de ejecucion. El nombre promete "
           "desplazamiento lateral que el texto no describe."),

    E("3294", "archer push up", "plank", floor=True, bal="moderate",
      grip="none", lat="alternating",
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
      why="Con un brazo extendido al costado, casi todo el peso cae sobre el "
           "otro: es una flexion a una mano encubierta. El brazo extendido "
           "queda en abduccion de 90 grados soportando carga — laxity high. "
           "one_arm_only a contra: paradojicamente, un ejercicio que carga un "
           "solo brazo necesita los dos."),

    E("1688", "lunge with twist", "standing", standing=True, bal="high",
      sl=True, grip="none", rot="moderate", impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="moderate", ank="moderate"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "lumbar_disc", "sciatica",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "obesity", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff"],
      why="Zancada con rotacion de torso sobre una pierna en apoyo: bal high y "
           "ortho high. La rotacion cargada de pie sin apoyo saca lumbar_disc, "
           "igual que en swing 360. Util para quien tiene problemas de brazos: "
           "no requiere agarre, ni hombro, ni bajar al suelo."),

    E("1689", "push and pull bodyweight", "plank", floor=True, grip="none",
      stress=js(wr="high", sh="moderate", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["rotator_cuff", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "obesity", "elderly_65plus", "hernia_abdominal",
            "pelvic_floor_dysfunction", "postpartum", "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="TEXTO REDUNDANTE: describe bajar el pecho flexionando los codos, "
           "subir, y despues 'tirar el pecho hacia el suelo flexionando los "
           "codos' — que es exactamente lo mismo. No hay fase de traccion "
           "posible en apoyo sobre el suelo. Clasificado como flexion comun. "
           "Confianza 0.60."),

    E("1700", "dumbbell push press", "standing", standing=True, bal="moderate",
      oh=True, grip="firm", axial="moderate", impact="low",
      stress=js(sh="high", el="moderate", lumbar="moderate", knee="moderate",
                wr="moderate"),
      pat="vertical_push", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="high", iso="low",
      metab="high", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "limited_grip",
              "cervical_injury", "osteoporosis", "hernia_abdominal",
              "knee_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "hypertension", "cardiac",
            "glaucoma", "retinal_detachment_risk", "dysautonomia", "vertigo",
            "elbow_injury", "wrist_injury", "knee_pain", "elderly_65plus",
            "limited_balance", "obesity", "pelvic_floor_dysfunction"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "ankle_injury",
            "plantar_fasciitis"],
      why="El impulso de piernas es lo que lo diferencia de un press militar: "
           "suma knee moderate y valsalva high, porque el gesto explosivo casi "
           "obliga a la apnea. Sobre la cabeza, de pie y con carga axial: "
           "ortho high y toda la familia ocular en cautions."),

    E("1771", "bodyweight kneeling triceps extension", "plank", floor=True,
      grip="none", stress=js(el="high", sh="moderate", wr="high",
                             lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "cannot_get_on_floor", "cannot_lie_prone",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "lumbar_pain",
            "lumbar_disc", "obesity", "elderly_65plus", "hernia_abdominal",
            "pelvic_floor_dysfunction", "postpartum", "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "cannot_kneel"],
      why="CORRECCION A E1: E1 dijo kneeling porque el texto arranca "
           "'kneel down', pero sigue con 'extend your legs straight behind "
           "you' — termina en plancha. Es una flexion con codos pegados. "
           "cannot_kneel queda en safe_for justamente porque las rodillas se "
           "despegan del suelo. El nombre no describe el ejercicio."),

    E("1775", "side plank hip adduction", "side_lying", floor=True,
      bal="moderate", grip="none", lat="unilateral", sl=True,
      stress=js(sh="moderate", hip="high", lumbar="low", el="moderate",
                knee="low"),
      pat="core_antiextension", diff=4, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="none",
      temp="moderate",
      contra=["cannot_lie_on_side", "cannot_get_on_floor",
              "shoulder_impingement", "rotator_cuff", "elbow_injury",
              "hip_replacement", "si_joint_pain"],
      caut=["hip_pain", "lumbar_disc", "lumbar_pain", "shoulder_pain",
            "hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "fibromyalgia", "limited_balance", "osteoarthritis",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis"],
      why="DUPLICADO FUNCIONAL DE 1774 (lote 19). El nombre dice 'adduction' "
           "pero el texto dice 'lift your top leg towards the ceiling' — es "
           "ABduccion, exactamente el mismo movimiento que 1774. Clasificado "
           "identico a proposito, para que el motor los trate igual. Ademas "
           "corrige a E1, que dijo plank donde el texto dice 'lying on your "
           "side'. Confianza 0.65 por el conflicto de nombre."),

    E("2135", "weighted front plank", "plank", floor=True, grip="none",
      axial="low",
      stress=js(lumbar="moderate", sh="moderate", el="moderate"),
      pat="core_antiextension", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_prone", "elbow_injury",
              "recent_abdominal_surgery", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "lumbar_pain",
            "lumbar_disc", "obesity", "elderly_65plus", "osteoporosis",
            "pelvic_floor_dysfunction", "postpartum", "hypertension",
            "chronic_fatigue"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "dysautonomia"],
      why="CORRECCION A E1: E1 dijo prone, pero el texto describe levantar el "
           "cuerpo y sostenerlo — es plank, no prono estatico. Como 1467, "
           "apoya en antebrazos: wrist_injury y carpal_tunnel en safe_for. "
           "El disco (peso) sobre la espalda sube pelvic y valsalva pero no "
           "cambia el perfil articular."),

    E("2333", "arm slingers hanging straight legs", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high",
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
      why="Version con piernas RECTAS de 1764: el brazo de palanca completo "
           "sube diff de 4 a 5, pelvic de moderate a high, y saca lumbar_pain "
           "de cautions a contra. Tercer eslabon de la cadena de suspension "
           "(2333 recto → 1764 flexionado → 1761 con rotacion) que E4 puede "
           "usar como progresion ordenada."),

    E("2398", "close-grip push-up (on knees)", "quadruped", floor=True,
      grip="none", stress=js(wr="high", el="high", sh="moderate",
                             knee="moderate", lumbar="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_replacement",
              "wrist_injury", "carpal_tunnel", "elbow_injury",
              "tendinitis_elbow", "pregnancy_3rd"],
      caut=["knee_pain", "knee_injury", "osteoarthritis",
            "shoulder_impingement", "rotator_cuff", "lumbar_pain",
            "rheumatoid_arthritis", "obesity", "elderly_65plus",
            "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "hip_replacement", "ankle_injury", "plantar_fasciitis",
            "lumbar_disc", "sciatica", "dysautonomia", "osteoporosis"],
      why="La regresion clasica de la flexion: apoyo en rodillas baja diff a 2 "
           "y saca la lumbar del cuadro (lumbar_disc y sciatica en safe_for). "
           "Pero cambia una restriccion por otra — cannot_kneel pasa a "
           "contraindicacion, y el agarre cerrado sube el codo a high. Para "
           "quien no puede arrodillarse, la sustitucion correcta es 0659 "
           "push-up (wall) o 1467 sobre antebrazos."),

    E("2462", "chest dip on straight bar", "standing", standing=True,
      grip="firm", stress=js(sh="high", el="high", wr="moderate",
                             cerv="low"),
      pat="vertical_push", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "wrist_injury", "elbow_injury",
              "tendinitis_elbow", "hypermobility", "cannot_stand",
              "one_arm_only", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["carpal_tunnel", "cervical_injury", "obesity", "elderly_65plus",
            "osteoporosis", "hypertension", "chronic_fatigue",
            "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "plantar_fasciitis"],
      why="Los fondos llevan el hombro a extension profunda con el peso "
           "corporal colgando: laxity high y la peor posicion posible para "
           "pinzamiento. Curiosidad util: no_overhead queda en safe_for porque "
           "los brazos nunca pasan por encima de la cabeza — el hombro sufre "
           "por abajo, no por arriba. El nombre dice 'straight bar' pero el "
           "texto dice 'parallel bars'."),
]

CONFIDENCE_OVERRIDES = {
    "0339": 0.55,  # texto mecanicamente incoherente
    "1689": 0.60,  # el texto describe la misma fase dos veces
    "1775": 0.65,  # el nombre dice aduccion, el texto describe abduccion
    "0720": 0.70,  # el nombre promete un movimiento que el texto no describe
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
    print(f"lote 23: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
