#!/usr/bin/env python3
"""Lote 37 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1585", "runners stretch", "standing", standing=True, bal="moderate",
      stress=js(hip="moderate", knee="moderate", ank="moderate",
                lumbar="low"),
      lat="unilateral", pat="mobility_stretch", diff=1, rom="high",
      ortho="high", change="moderate", valsalva="none", iso="moderate",
      metab="none", laxity="moderate", pelvic="low", temp="none",
      contra=["cannot_stand", "wheelchair", "knee_replacement",
              "limited_balance"],
      caut=["knee_injury", "knee_pain", "hip_pain", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "osteoarthritis",
            "si_joint_pain", "lumbar_pain", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "sciatica"],
      why="Zancada estatica sostenida con las manos apoyadas en el muslo. "
           "A diferencia de 1511 hamstring stretch la cadera se extiende en "
           "vez de plegarse: no hay head_below_heart, la columna se queda "
           "neutra y lumbar_disc y sciatica van a safe_for. El costo se "
           "traslada entero a la rodilla de adelante, que sostiene el peso "
           "flexionada durante 20-30 segundos."),

    E("0313", "dumbbell hammer curl", "standing", standing=True, bal="low",
      grip="firm",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["rheumatoid_arthritis", "wrist_injury", "shoulder_pain",
            "lumbar_pain", "dysautonomia", "hypertension", "varicose_veins"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica", "carpal_tunnel", "osteoporosis"],
      why="Agarre neutro: la muneca no supina en ningun momento del "
           "recorrido. Esa es toda la diferencia con 0294 dumbbell biceps "
           "curl, y alcanza para que carpal_tunnel pase de precaucion a "
           "safe_for. Para quien no puede estar de pie, 1678 dumbbell seated "
           "hammer curl es el sustituto exacto."),

    E("3166", "bodyweight standing row", "standing", standing=True, bal="low",
      grip="firm",
      stress=js(sh="moderate", el="moderate", lumbar="low", wr="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "elbow_injury", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "cervical_injury", "dysautonomia", "hypertension",
            "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "osteoporosis", "lumbar_disc", "sciatica"],
      why="Tiron horizontal de pie con el tronco erguido: es el unico remo "
           "del catalogo sin isometrico lumbar, al reves de 0293 dumbbell "
           "bent over row y 0075. Por eso lumbar_disc y osteoporosis quedan "
           "en safe_for. El texto no aclara contra que se tira —barra fija, "
           "anillas o banda— asi que la confianza baja; hay que resolverlo "
           "en E3 antes de ofrecerlo como sustituto lumbar."),

    E("0432", "dumbbell stiff leg deadlift", "standing", standing=True,
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
      why="Version con mancuernas de 1009 band stiff leg deadlift. Misma "
           "flexion lumbar alta, pero la mancuerna carga desde el primer "
           "grado de recorrido mientras la banda recien tensa al final: "
           "difficulty sube de 2 a 3 y limited_grip pasa de precaucion a "
           "contraindicacion. Frente a 1459 romanian deadlift la rodilla "
           "queda mas extendida, lo que traslada carga del gluteo al isquio "
           "y a la columna."),

    E("0709", "side hip (on parallel bars)", "hanging", standing=True,
      grip="firm", flex="low", rot="moderate",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="high",
                hip="moderate"),
      pat="core_rotation", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_grip", "one_arm_only",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "elbow_injury", "lumbar_disc", "sciatica", "si_joint_pain",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["lumbar_pain", "wrist_injury", "carpal_tunnel", "hip_pain",
            "hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "osteoporosis", "postpartum", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Mismo soporte que 0826 vertical leg raise (on parallel bars) pero "
           "elevando las piernas al costado: agrega componente lateral sobre "
           "una columna que ya esta en traccion. El dataset lo lista como "
           "body weight, aunque exige barras paralelas: candidato a marcarse "
           "como no disponible en casa durante el build del indice."),

    E("0977", "band front lateral raise", "standing", standing=True,
      bal="low", grip="light",
      stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury", "limited_grip"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "sciatica",
            "plantar_fasciitis", "wrist_injury", "carpal_tunnel",
            "osteoporosis"],
      why="El nombre dice 'front lateral' pero las instrucciones describen "
           "una elevacion frontal pura: se clasifica como 0978 band front "
           "raise, del que es equivalente. La banda mantiene el brazo bajo "
           "los 90 grados, asi que no_overhead sigue en safe_for pese a ser "
           "trabajo de deltoides."),

    E("2402", "dumbbell hammer curls (with arm blaster)", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="high", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow"],
      caut=["rheumatoid_arthritis", "wrist_injury", "shoulder_pain",
            "lumbar_pain", "dysautonomia", "hypertension", "osteoarthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica", "carpal_tunnel"],
      why="Instrucciones identicas a 0313 dumbbell hammer curl; lo unico que "
           "cambia es el arm blaster, que fija el codo e impide compensar "
           "con el hombro. Se refleja como elbow high en vez de moderate: "
           "mas estricto es mas carga articular, no menos. Confianza baja "
           "porque el accesorio no esta en el filtro de equipo y puede que "
           "haya que descartarlo del indice de casa."),

    E("0046", "barbell hack squat", "standing", standing=True, bal="moderate",
      grip="firm",
      stress=js(knee="high", hip="moderate", lumbar="moderate", sh="moderate",
                wr="moderate", ank="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "limited_grip",
              "shoulder_impingement", "rotator_cuff", "lumbar_disc",
              "osteoporosis", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_pain", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "sciatica", "hip_pain", "osteoarthritis", "ankle_injury",
            "plantar_fasciitis", "limited_balance", "dysautonomia",
            "hypertension", "glaucoma", "elderly_65plus", "obesity"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "elbow_injury"],
      why="La barra va DETRAS de las piernas, no sobre la espalda: obliga a "
           "sostener los hombros en extension con rotacion interna durante "
           "toda la serie, que es la postura que un hombro pinzado no "
           "tolera. Por eso shoulder_impingement entra a contraindicacion, "
           "cosa que no pasa en ninguna sentadilla con barra al hombro "
           "(0054, 0102). No es 'una sentadilla mas': el limite esta arriba, "
           "no en la pierna."),

    E("0999", "band single leg calf raise", "standing", standing=True,
      bal="moderate", sl=True, grip="light",
      stress=js(ank="high", knee="low", hip="low"),
      lat="unilateral", pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain",
            "hip_replacement", "hip_pain", "osteoarthritis", "dysautonomia",
            "vertigo", "elderly_65plus", "multiple_sclerosis",
            "varicose_veins", "osteoporosis", "limited_grip"],
      safe=["no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "lumbar_disc",
            "lumbar_pain", "sciatica", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "hernia_abdominal", "knee_injury"],
      why="Tercera variante unipodal de gemelo del pipeline, junto a 1387 "
           "sin apoyo y 1386 con apoyo de pared. Aca la banda agrega "
           "resistencia pero ocupa las manos: limited_grip baja de safe_for "
           "a precaucion, que es lo unico que la separa de 1386. Para perfil "
           "con equilibrio comprometido, 1386 sigue siendo la mejor."),

    E("1022", "band standing rear delt row", "standing", standing=True,
      bal="low", grip="light", flex="low",
      stress=js(lumbar="moderate", hip="moderate", sh="moderate",
                el="moderate"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="high", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hip_replacement",
            "shoulder_impingement", "shoulder_pain", "elbow_injury",
            "limited_grip", "cervical_injury", "hypertension", "glaucoma",
            "dysautonomia", "elderly_65plus", "obesity", "osteoporosis",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "wrist_injury", "carpal_tunnel"],
      why="Regresion directa de 0075 barbell rear delt raise. La banda pesa "
           "poco y se ancla bajo los pies, asi que el isometrico lumbar "
           "sigue existiendo pero con una fraccion de la carga: lumbar baja "
           "de high a moderate, y osteoporosis y lumbar_pain pasan de "
           "contraindicacion a precaucion. Es el escalon de entrada al "
           "trabajo de deltoides posterior en bisagra."),

    E("1410", "barbell lateral lunge", "standing", standing=True, bal="high",
      grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="moderate"),
      lat="unilateral", pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "limited_grip", "osteoporosis", "lumbar_disc",
              "si_joint_pain", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "sciatica", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "hypermobility", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "obesity",
            "pelvic_floor_dysfunction", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "rotator_cuff", "elbow_injury"],
      why="Unico patron de zancada en plano frontal del catalogo: el peso se "
           "desplaza al costado con la barra cargada sobre la espalda. Esa "
           "combinacion de carga axial y desplazamiento lateral es lo que "
           "mete si_joint_pain en contraindicacion, cosa que no ocurre en "
           "0054 barbell lunge ni en 0078 rear lunge. Mismo criterio de "
           "hombro que el resto de barra al hombro: no_overhead va a "
           "safe_for."),

    E("0067", "barbell one arm snatch", "standing", standing=True, bal="high",
      oh=True, grip="firm", axial="high", flex="moderate", impact="moderate",
      stress=js(knee="high", hip="high", lumbar="high", cerv="moderate",
                sh="high", el="moderate", wr="high", ank="moderate"),
      lat="unilateral", pat="hinge", diff=5, rom="high",
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
              "cardiac", "elderly_65plus", "hypermobility",
              "visual_impairment", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "glaucoma", "retinal_detachment_risk", "obesity",
            "chronic_fatigue", "dysautonomia", "multiple_sclerosis",
            "vertigo", "hip_pain", "osteoarthritis", "epilepsy",
            "elbow_injury"],
      safe=[],
      why="Levantamiento olimpico completo a un brazo: tiron desde el suelo, "
           "recepcion explosiva y bloqueo sobre la cabeza con una sola mano. "
           "safe_for vacio, igual que 0776 snatch pull. Peor que 0776 en dos "
           "cosas: la carga queda asimetrica sobre la columna y el bloqueo "
           "overhead unilateral exige un hombro perfecto. one_arm_only entra "
           "a contraindicacion aunque sea unilateral —hace falta el otro "
           "brazo para estabilizar el tiron."),

    E("1456", "barbell standing close grip military press", "standing",
      standing=True, bal="low", oh=True, grip="firm", axial="moderate",
      stress=js(lumbar="high", cerv="low", sh="high", el="high",
                wr="moderate"),
      pat="vertical_push", diff=4, rom="high",
      ortho="high", change="low", valsalva="high", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "limited_grip", "lumbar_disc", "osteoporosis", "elbow_injury",
              "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "cervical_injury", "lumbar_pain",
            "sciatica", "hypertension", "cardiac", "glaucoma",
            "retinal_detachment_risk", "dysautonomia", "elderly_65plus",
            "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis"],
      why="Hermano de 1457 barbell standing wide military press. El agarre "
           "cerrado reduce la abduccion del hombro pero traslada el trabajo "
           "al triceps con el codo muy flexionado bajo la barra: elbow sube "
           "de moderate a high y elbow_injury y tendinitis_elbow entran a "
           "contraindicacion, cosa que en 1457 no pasa. Menos hombro, mas "
           "codo — no es una version mas segura, es otra distribucion."),

    E("0291", "dumbbell bench squat", "standing", standing=True, bal="low",
      grip="firm",
      stress=js(knee="moderate", hip="moderate", lumbar="low", ank="low"),
      pat="squat", diff=1, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="low", pelvic="low", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip"],
      caut=["knee_injury", "knee_pain", "knee_replacement", "hip_replacement",
            "hip_pain", "osteoarthritis", "lumbar_pain", "lumbar_disc",
            "ankle_injury", "plantar_fasciitis", "limited_balance",
            "dysautonomia", "elderly_65plus", "obesity", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "no_overhead", "wrist_injury",
            "carpal_tunnel", "shoulder_impingement", "rotator_cuff",
            "elbow_injury", "sciatica", "osteoporosis"],
      why="Segundo hallazgo util del bloque de piernas: el banco pone un "
           "tope fisico a la profundidad y da un punto de descanso en cada "
           "repeticion. Es el patron sentarse-y-levantarse, el mas funcional "
           "que existe para perfil mayor o con rodilla sensible. Difficulty "
           "1 y knee moderate frente a high en 0413 dumbbell squat: es la "
           "regresion que le faltaba a toda la familia de sentadillas."),

    E("0371", "dumbbell plyo squat", "standing", standing=True, bal="high",
      grip="firm", impact="high", lat="alternating",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="high"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "osteoarthritis", "vertigo",
              "limited_grip", "lumbar_disc", "elderly_65plus",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "si_joint_pain", "dysautonomia",
            "hypertension", "cardiac", "obesity", "chronic_fatigue",
            "asthma", "varicose_veins", "multiple_sclerosis", "postpartum",
            "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff"],
      why="0513 jump squat con mancuernas en las manos y cambio de pierna en "
           "el aire. La carga extra multiplica la fuerza de aterrizaje y las "
           "manos ocupadas eliminan el reflejo de brazos para reequilibrar: "
           "limited_grip y lumbar_disc entran a contraindicacion, que en "
           "0513 no estaban. Techo de la familia de sentadilla pliometrica."),

    E("0420", "dumbbell standing kickback", "standing", standing=True,
      bal="moderate", grip="firm", flex="moderate",
      stress=js(lumbar="high", sh="moderate", el="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
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
            "wrist_injury", "carpal_tunnel"],
      why="Texto equivalente a 0333 dumbbell kickback: mismo bisagra de "
           "cadera sostenida y misma extension de codo. Se clasifica "
           "identico. Tercer posible duplicado del pipeline junto a "
           "0360/0361 y 0313/2402 — vale la pena que E3 resuelva los tres "
           "de una vez en lugar de arrastrarlos al indice."),

    E("0439", "dumbbell zottman curl", "standing", standing=True, bal="low",
      grip="firm",
      stress=js(el="high", wr="high", sh="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="low", iso="none", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "rheumatoid_arthritis"],
      caut=["hypermobility", "osteoarthritis", "shoulder_pain",
            "dysautonomia", "hypertension", "lumbar_pain"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "shoulder_impingement", "rotator_cuff",
            "sciatica", "osteoporosis"],
      why="Sube supinado y baja pronado: la muneca rota bajo carga en cada "
           "repeticion y la fase excentrica cae sobre el antebrazo en "
           "pronacion. Es el unico curl del catalogo donde wrist llega a "
           "high, y por eso wrist_injury y carpal_tunnel son "
           "contraindicacion —en 0294 y 0313 eran precaucion o safe_for. "
           "2294 zottman preacher curl da lo mismo sentado y con el codo "
           "fijo."),

    E("0624", "march sit (wall)", "standing", standing=True, bal="moderate",
      sl=True, lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="low", ank="low"),
      pat="squat", diff=3, rom="moderate",
      ortho="moderate", change="low", valsalva="moderate", iso="high",
      metab="high", laxity="low", pelvic="moderate", temp="high",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain"],
      caut=["hip_pain", "hip_replacement", "osteoarthritis", "lumbar_pain",
            "si_joint_pain", "limited_balance", "dysautonomia",
            "hypertension", "cardiac", "glaucoma", "obesity",
            "elderly_65plus", "chronic_fatigue", "fibromyalgia",
            "multiple_sclerosis", "varicose_veins",
            "pelvic_floor_dysfunction", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "sciatica", "ankle_injury", "plantar_fasciitis",
            "osteoporosis"],
      why="La pared sostiene la columna entera: es de los pocos ejercicios "
           "de pierna con carga real donde lumbar_disc, sciatica y "
           "osteoporosis van los tres a safe_for. El precio esta en otro "
           "lado: isometrico sostenido con la rodilla a 90 grados, que "
           "dispara presion arterial —de ahi hypertension, cardiac y "
           "glaucoma en precaucion pese a ser un ejercicio 'suave'. Ejemplo "
           "claro de por que la Capa C no puede deducirse del patron."),
]

CONFIDENCE_OVERRIDES = {
    "3166": 0.70,  # el texto no dice contra que se tira (barra, anillas, banda)
    "2402": 0.75,  # arm blaster fuera del filtro de equipo; posible duplicado de 0313
    "0420": 0.75,  # posible duplicado de 0333
    "0977": 0.85,  # el nombre dice "front lateral", las instrucciones son frontal
    "0709": 0.80,  # listado como body weight pero exige barras paralelas
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
    print(f"lote 37: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
