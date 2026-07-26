#!/usr/bin/env python3
"""Lote 42 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("3635", "dumbbell contralateral forward lunge", "standing",
      standing=True, bal="high", sl=True, grip="firm", impact="low",
      lat="alternating",
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
      why="'Contralateral' implicaria cargar solo el lado opuesto a la "
           "pierna que avanza, lo que cambiaria por completo la demanda "
           "antirrotacion del tronco. El texto dice mancuerna en cada mano y "
           "describe 0336 dumbbell lunge. Se clasifica como 0336 y se marca "
           "para E3."),

    E("0335", "dumbbell lateral to front raise", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
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
      why="Encadena elevacion lateral y frontal sin soltar el peso, asi que "
           "el hombro sostiene carga mientras recorre dos planos: "
           "joint_laxity_risk high y sustained_isometric moderate, ambos por "
           "encima de 0334 o 0310 por separado. Version reducida del "
           "problema de 2143 around world."),

    E("1687", "posterior step to overhead reach", "standing", standing=True,
      bal="high", sl=True, oh=True, impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", sh="moderate", lumbar="moderate",
                ank="moderate"),
      pat="lunge", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "vertigo", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "shoulder_pain", "osteoarthritis", "plantar_fasciitis",
            "dysautonomia", "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "elbow_injury", "sciatica",
            "one_arm_only"],
      why="Tercer combinado que arrastra el hombro a un ejercicio de pierna, "
           "despues de 1685 y 3644. Zancada hacia atras mas alcance sobre la "
           "cabeza: sin carga externa, pero no_overhead y "
           "shoulder_impingement quedan en contraindicacion y bloquean todo "
           "el movimiento. 3470 forward lunge da el patron de pierna sin "
           "tocar el hombro."),

    E("0042", "barbell front squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="moderate", lumbar="moderate", wr="high",
                sh="moderate", ank="high", cerv="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip", "wrist_injury",
              "shoulder_impingement", "osteoporosis", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["carpal_tunnel", "rotator_cuff", "shoulder_pain", "lumbar_pain",
            "lumbar_disc", "ankle_injury", "plantar_fasciitis",
            "limited_balance", "dysautonomia", "hypertension", "cardiac",
            "glaucoma", "elderly_65plus", "obesity", "osteoarthritis",
            "hip_pain", "cervical_injury"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "elbow_injury", "sciatica"],
      why="Mismo intercambio que 3194 frankenstein squat pero con la barra "
           "apoyada en clavicula: el peso adelante obliga a torso vertical y "
           "lumbar queda en moderate, con sciatica en safe_for, contra high "
           "en 0124 y 0026 con barra atras. El costo se muda a la muneca "
           "—el front rack exige extension forzada— y al hombro. Para "
           "columna sensible es la mejor sentadilla con barra; para muneca "
           "sensible, la peor."),

    E("0028", "barbell clean and press", "standing", standing=True,
      bal="high", oh=True, grip="firm", axial="high", flex="moderate",
      impact="moderate",
      stress=js(knee="high", hip="high", lumbar="high", sh="high",
                el="moderate", wr="high", cerv="moderate", ank="moderate"),
      pat="hinge", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "si_joint_pain", "osteoporosis",
              "knee_injury", "knee_replacement", "knee_pain",
              "hip_replacement", "ankle_injury", "wrist_injury",
              "carpal_tunnel", "limited_grip", "one_arm_only", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "cervical_injury", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "cardiac", "hypertension", "elderly_65plus", "hypermobility",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "multiple_sclerosis",
            "vertigo", "hip_pain", "osteoarthritis", "epilepsy",
            "elbow_injury", "visual_impairment"],
      safe=[],
      why="Segundo levantamiento olimpico completo del catalogo junto a 0067 "
           "barbell one arm snatch: tiron desde el suelo, recepcion en "
           "clavicula y press sobre la cabeza. safe_for vacio. Treinta y dos "
           "contraindicaciones, el registro con mas restricciones de todo el "
           "pipeline hasta ahora."),

    E("0105", "barbell standing bradford press", "standing", standing=True,
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
      why="El bradford press real alterna adelante y detras de la nuca sin "
           "bloquear el codo; el texto solo describe un press frontal. Por "
           "D-019 se toma la lectura mas restrictiva y se clasifica como "
           "0788 standing behind neck press: cervical_injury y neck_pain en "
           "contraindicacion. Si E3 confirma que es solo frontal, se "
           "reclasifica como 1457."),

    E("0446", "ez barbell close-grip curl", "standing", standing=True,
      bal="low", grip="firm", axial="low",
      stress=js(el="moderate", wr="moderate", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "limited_balance", "hypertension",
            "elderly_65plus", "varicose_veins", "rheumatoid_arthritis",
            "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "sciatica", "osteoporosis"],
      why="0447 ez barbell curl con las manos mas juntas. El agarre estrecho "
           "en barra Z fuerza algo mas de desviacion de muneca que el agarre "
           "estandar, pero el angulo de la barra sigue amortiguando: "
           "wrist_injury queda en precaucion, no en contraindicacion como en "
           "0439 zottman. Diferencia menor; el par 0446/0447 es colapsable."),

    E("1023", "band straight back stiff leg deadlift", "standing",
      standing=True, bal="low", grip="light", flex="moderate",
      stress=js(hip="high", lumbar="moderate", knee="low"),
      pat="hinge", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hip_replacement",
            "osteoporosis", "hernia_abdominal", "limited_grip",
            "dysautonomia", "elderly_65plus", "obesity",
            "pelvic_floor_dysfunction", "hypertension", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Equivalente a 1009 band stiff leg deadlift. La banda tensa recien "
           "al final del recorrido, asi que la parte baja —donde la columna "
           "esta mas flexionada— es la de menos carga, al reves de la "
           "mancuerna en 0432 y de la barra en 0116. Por eso lumbar queda en "
           "moderate y osteoporosis en precaucion."),

    E("0108", "barbell standing leg calf raise", "standing", standing=True,
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
      why="Texto identico a 1372 barbell standing calf raise. Se clasifica "
           "igual. Octavo par duplicado del pipeline y el segundo dentro de "
           "la familia de gemelo."),

    E("0064", "barbell one arm bent over row", "standing", standing=True,
      bal="low", grip="firm", flex="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate",
                wr="moderate"),
      lat="unilateral", pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "lumbar_pain",
              "sciatica", "si_joint_pain", "osteoporosis", "limited_grip",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "hip_replacement", "shoulder_impingement",
            "shoulder_pain", "elbow_injury", "wrist_injury",
            "cervical_injury", "neck_pain", "hypertension", "glaucoma",
            "dysautonomia", "elderly_65plus", "obesity",
            "pelvic_floor_dysfunction"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "one_arm_only"],
      why="Barra larga sostenida con una sola mano desde posicion inclinada: "
           "ademas del isometrico lumbar de 0293, la carga queda "
           "descentrada y la columna resiste flexion lateral. si_joint_pain "
           "entra a contraindicacion, igual que en 0066 barbell one arm side "
           "deadlift. Con mancuerna, 0292 hace lo mismo sin barra "
           "descentrada."),

    E("3888", "dumbbell one arm snatch", "standing", standing=True,
      bal="high", oh=True, grip="firm", flex="moderate", impact="moderate",
      stress=js(knee="moderate", hip="high", lumbar="high", sh="high",
                el="moderate", wr="moderate", ank="moderate"),
      lat="unilateral", pat="hinge", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "si_joint_pain", "osteoporosis",
              "hip_replacement", "knee_injury", "knee_pain", "ankle_injury",
              "limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "hernia_abdominal",
              "pelvic_floor_dysfunction", "cardiac", "elderly_65plus",
              "hypermobility", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "glaucoma", "obesity", "chronic_fatigue",
            "dysautonomia", "multiple_sclerosis", "vertigo", "hip_pain",
            "osteoarthritis", "wrist_injury", "cervical_injury",
            "visual_impairment", "elbow_injury"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_replacement", "plantar_fasciitis"],
      why="Snatch con mancuerna en vez de barra. Frente a 0067 barbell one "
           "arm snatch la carga es mucho menor y el implemento no obliga a "
           "esquivar las rodillas: difficulty baja de 5 a 4 y aparece "
           "safe_for, que en 0067 estaba vacio. one_arm_only sale de "
           "contraindicacion —con mancuerna el brazo libre no hace falta "
           "para estabilizar."),

    E("5201", "dumbbell waiter biceps curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="moderate", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis",
            "hypermobility", "shoulder_pain", "lumbar_pain", "dysautonomia",
            "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica"],
      why="El waiter curl real sostiene una sola mancuerna en vertical sobre "
           "las palmas, lo que carga la muneca en extension; el texto "
           "describe un curl comun con mancuerna en cada mano. Por D-019 se "
           "sube wrist a moderate y wrist_injury queda en precaucion, en vez "
           "de tratarlo como 0294."),

    E("0292", "dumbbell one arm bent-over row", "standing", standing=True,
      bal="low", grip="firm", flex="low",
      stress=js(lumbar="high", hip="moderate", sh="moderate", el="moderate"),
      lat="unilateral", pat="horizontal_pull", diff=3, rom="moderate",
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
            "wrist_injury", "one_arm_only"],
      why="Version a un brazo de 0293 dumbbell bent over row, sin apoyar la "
           "mano libre en un banco: el tronco se sostiene solo. Ese detalle "
           "es lo que mantiene lumbar en high — los remos a un brazo "
           "apoyados en banco resuelven el mismo patron sin isometrico "
           "lumbar y son la sustitucion obvia."),

    E("0298", "dumbbell cross body hammer curl", "standing", standing=True,
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
      why="Curl martillo llevando la mancuerna hacia el hombro contrario. La "
           "aduccion horizontal es minima y ocurre a la altura del pecho, no "
           "del hombro, asi que shoulder_impingement se queda en safe_for a "
           "diferencia de 0669 rear deltoid stretch, donde el brazo cruza "
           "estirado. Por lo demas, identico a 0313."),

    E("0382", "dumbbell revers grip biceps curl", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="high", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel"],
      caut=["rheumatoid_arthritis", "hypermobility", "shoulder_pain",
            "lumbar_pain", "dysautonomia", "hypertension", "osteoarthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica"],
      why="Nombre con error de tipeo ('revers') pero texto coherente: palmas "
           "hacia abajo, pronado real. Identico a 1654 dumbbell biceps curl "
           "reverse. Junto con 0429 y 1675 son cuatro registros para el mismo "
           "curl invertido de pie."),

    E("0410", "dumbbell single leg split squat", "standing", standing=True,
      bal="high", sl=True, grip="firm",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="moderate"),
      lat="unilateral", pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "vertigo", "osteoarthritis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "plantar_fasciitis", "hypermobility", "dysautonomia",
            "elderly_65plus", "multiple_sclerosis", "obesity",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "no_overhead", "wrist_injury",
            "carpal_tunnel", "shoulder_impingement", "rotator_cuff",
            "elbow_injury"],
      why="Split squat bulgaro: pie trasero elevado sobre un banco fijo. "
           "Frente a 0809 suspended split squat la superficie no se mueve, "
           "asi que visual_impairment sale de contraindicacion y "
           "osteoarthritis se mantiene por la rodilla de adelante. "
           "cannot_transfer_to_bench no va a safe_for ni a contraindicacion: "
           "apoyar el empeine no es transferirse, pero el registro no "
           "alcanza para afirmarlo."),

    E("0423", "dumbbell standing one arm extension", "standing",
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
      why="Texto equivalente a 0430 dumbbell standing triceps extension. Se "
           "clasifica igual. Noveno par duplicado del pipeline."),

    E("0427", "dumbbell standing palms in press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low",
      stress=js(sh="moderate", el="moderate", wr="low", lumbar="moderate"),
      pat="vertical_push", diff=2, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead", "limited_grip",
              "shoulder_pain"],
      caut=["shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "cervical_injury", "lumbar_disc",
            "lumbar_pain", "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus", "osteoporosis", "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Hallazgo del lote, y el mismo mecanismo que 0311 full can lateral "
           "raise. Palmas enfrentadas significa agarre neutro: el humero se "
           "queda en rotacion externa y el espacio subacromial no se cierra. "
           "Todos los demas press de pie del catalogo —1456, 1457, 0445, "
           "0414, 0361, 0286, 2136— son pronados y contraindican "
           "pinzamiento; este lo baja a precaucion. no_overhead sigue "
           "contraindicado: el brazo igual va arriba. Es el press que se le "
           "puede ofrecer a un hombro sensible, no uno seguro."),
]

CONFIDENCE_OVERRIDES = {
    "0105": 0.65,  # bradford real alterna detras de nuca; texto solo describe frontal
    "5201": 0.65,  # waiter curl real carga la muneca; texto describe curl comun
    "3635": 0.70,  # "contralateral" no aparece en el texto
    "0108": 0.70,  # duplicado de 1372
    "0423": 0.70,  # duplicado de 0430
    "0446": 0.80,  # diferencia minima con 0447
    "0410": 0.80,  # cannot_transfer_to_bench sin resolver
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
    print(f"lote 42: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
