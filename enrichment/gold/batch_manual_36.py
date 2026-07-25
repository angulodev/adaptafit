#!/usr/bin/env python3
"""Lote 36 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0456", "flexion leg sit up (bent knee)", "supine", floor=True,
      flex="high",
      stress=js(lumbar="high", cerv="high", hip="high"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", pelvic="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "lumbar_pain", "sciatica", "cervical_injury", "neck_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "postpartum", "obesity",
            "elderly_65plus", "migraine", "hypertension", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "limited_grip",
            "no_overhead", "knee_injury", "knee_pain", "ankle_injury",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "dysautonomia", "shoulder_impingement", "rotator_cuff"],
      why="Sube tronco Y piernas a la vez con las manos detras de la nuca: "
           "suma flexion lumbar cargada, traccion cervical y flexion de cadera "
           "profunda. Mas exigente que 3202 half sit-up en las tres cosas. "
           "hip_replacement entra a contraindicacion —no estaba en 3202— "
           "porque las piernas suben mas alla de los 90 grados de cadera."),

    E("0294", "dumbbell biceps curl", "standing", standing=True, bal="low",
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
      why="Version de pie de 1677 dumbbell seated bicep curl. Mecanicamente "
           "identico en el codo; lo unico que cambia es que hay que estar de "
           "pie sostenido varios minutos: cannot_stand y wheelchair salen de "
           "safe_for y entran a contraindicacion, y aparece carga ortostatica. "
           "Si el perfil no puede estar de pie, 1677 es el sustituto directo."),

    E("0669", "rear deltoid stretch", "standing", standing=True, bal="low",
      stress=js(sh="moderate", el="low"),
      lat="unilateral", pat="mobility_stretch", diff=1, rom="high",
      ortho="high", iso="moderate", metab="none", laxity="moderate",
      temp="none",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain"],
      caut=["hypermobility", "elbow_injury", "limited_balance", "dysautonomia",
            "varicose_veins", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "osteoporosis", "one_arm_only",
            "plantar_fasciitis"],
      why="El brazo cruza el pecho y se queda a la altura del hombro: "
           "no_overhead va a safe_for, pero la aduccion horizontal es "
           "justamente la maniobra que provoca dolor en pinzamiento y en "
           "manguito rotador, asi que esos quedan en contraindicacion pese a "
           "ser 'solo un estiramiento'. Mismo criterio que 0817 triceps "
           "stretch: el estiramiento contraindica la articulacion que estira."),

    E("3470", "forward lunge (male)", "standing", standing=True, bal="high",
      sl=True, impact="low", lat="alternating",
      stress=js(knee="high", hip="moderate", lumbar="low", ank="moderate"),
      pat="lunge", diff=2, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "obesity", "osteoporosis", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "one_arm_only", "lumbar_disc"],
      why="Zancada sin carga, manos en la cadera. Es la version base de 0336 "
           "dumbbell lunge: mismo estres de rodilla, pero al soltar las "
           "mancuernas limited_grip pasa de contraindicacion a safe_for y "
           "lumbar_disc tambien, porque desaparece el peso colgando al "
           "costado. Buena regresion de 0336 y de 3582 lunge with jump."),

    E("0293", "dumbbell bent over row", "standing", standing=True, bal="low",
      grip="firm", flex="low",
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
      why="El costo real no esta en la espalda alta sino en el isometrico "
           "lumbar: el tronco queda inclinado sosteniendo el peso durante toda "
           "la serie. Por eso sustained_isometric high y lumbar_disc a "
           "contraindicacion. Los remos apoyados en banco (0327, 1330) "
           "entregan el mismo patron sin ese isometrico: son la sustitucion "
           "obvia para cualquier perfil lumbar."),

    E("0513", "jump squat v. 2", "standing", standing=True, bal="moderate",
      impact="high",
      stress=js(knee="high", hip="moderate", lumbar="moderate", ank="high"),
      pat="squat", diff=3, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "vertigo", "osteoarthritis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "dysautonomia", "hypertension", "cardiac", "obesity",
            "elderly_65plus", "chronic_fatigue", "asthma", "varicose_veins",
            "multiple_sclerosis", "postpartum", "pregnancy_1st"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Sentadilla completa mas salto, encadenada sin pausa. Se clasifica "
           "como squat y no como cardio_interval —a diferencia de 3222 semi "
           "squat jump— porque el rango es completo y la carga articular manda "
           "sobre el componente metabolico. Frente a 3222 suma knee_pain y "
           "osteoarthritis a contraindicacion por la profundidad."),

    E("3552", "quick feet v. 2", "standing", standing=True, bal="low",
      impact="moderate", lat="alternating",
      stress=js(ank="high", knee="moderate", hip="low"),
      pat="cardio_interval", diff=2, rom="low",
      ortho="high", change="low", valsalva="none", iso="low", metab="high",
      laxity="low", pelvic="moderate", temp="high",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis", "knee_replacement"],
      caut=["knee_injury", "knee_pain", "hip_replacement", "hip_pain",
            "osteoarthritis", "limited_balance", "dysautonomia",
            "hypertension", "cardiac", "obesity", "elderly_65plus",
            "chronic_fatigue", "asthma", "osteoporosis", "vertigo",
            "pelvic_floor_dysfunction", "multiple_sclerosis", "postpartum",
            "varicose_veins", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "lumbar_pain"],
      why="Amplitud minima pero frecuencia altisima sobre la punta del pie: "
           "todo el costo se concentra en tobillo y fascia plantar, no en "
           "rodilla ni columna. Por eso plantar_fasciitis y ankle_injury "
           "quedan en contraindicacion mientras lumbar_disc va a safe_for, "
           "al reves de casi todo el bloque de cardio de pie."),

    E("3655", "walking high knees lunge", "standing", standing=True,
      bal="high", sl=True, impact="moderate", lat="alternating",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="high", laxity="moderate", pelvic="high", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement",
              "ankle_injury", "vertigo", "pelvic_floor_dysfunction",
              "visual_impairment", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "lumbar_disc", "si_joint_pain",
            "osteoarthritis", "plantar_fasciitis", "dysautonomia",
            "hypertension", "cardiac", "obesity", "elderly_65plus",
            "chronic_fatigue", "asthma", "multiple_sclerosis", "postpartum",
            "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="E1 lo marco cardio_steady porque el dataset lo tiene en body_part "
           "cardio, pero mecanicamente es una zancada caminando con rodilla "
           "alta intercalada: se clasifica lunge. La rodilla alta obliga a "
           "un apoyo unipodal completo entre zancada y zancada —ahi esta la "
           "diferencia con 3582 lunge with jump— y por eso entra "
           "visual_impairment a contraindicacion: hay desplazamiento."),

    E("1386", "one leg donkey calf raise", "standing", standing=True,
      bal="moderate", sl=True, grip="light",
      stress=js(ank="high", knee="low", hip="low"),
      pat="isolation", diff=2, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="low", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain", "hip_pain",
            "hip_replacement", "osteoarthritis", "dysautonomia", "vertigo",
            "elderly_65plus", "multiple_sclerosis", "varicose_veins",
            "osteoporosis"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "lumbar_disc", "lumbar_pain", "sciatica", "cannot_get_on_floor",
            "cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "one_arm_only", "hernia_abdominal",
            "knee_injury"],
      why="Version apoyada de 1387 one leg floor calf raise: las manos van a "
           "la pared o a una barra. Ese apoyo es lo que la hace util —baja la "
           "exigencia de equilibrio sin bajar el trabajo de gemelo— y por eso "
           "limited_balance se queda en precaucion en vez de subir. Es el "
           "escalon intermedio entre 0284 donkey calf raise a dos piernas "
           "y 1387 sin apoyo."),

    E("0360", "dumbbell one arm shoulder press v. 2", "standing",
      standing=True, bal="low", oh=True, grip="firm", axial="low",
      stress=js(lumbar="moderate", sh="high", el="moderate", wr="moderate"),
      lat="unilateral", pat="vertical_push", diff=2, rom="high",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["shoulder_pain", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_disc", "lumbar_pain", "cervical_injury", "hypermobility",
            "dysautonomia", "hypertension", "elderly_65plus", "osteoporosis",
            "glaucoma"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement",
            "plantar_fasciitis", "one_arm_only"],
      why="Duplicado funcional de 0361 dumbbell one arm shoulder press: el "
           "texto de instrucciones es equivalente y no aparece ninguna "
           "diferencia de ejecucion. Se clasifica identico a proposito. Si "
           "en E3 se confirma que son el mismo movimiento, uno de los dos "
           "deberia colapsarse en el indice de la app."),

    E("1015", "band vertical pallof press", "standing", standing=True,
      bal="moderate", grip="light", rot="none",
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
      why="Hallazgo del lote: trabajo de core que RESISTE la rotacion en vez "
           "de producirla. Cero flexion lumbar, cero transicion al suelo, "
           "cero impacto —lo contrario de todo el bloque de sit-ups de este "
           "mismo lote. Es el ejercicio de abdomen que si se le puede ofrecer "
           "a lumbar_disc, osteoporosis y hernia abdominal. Prioridad alta "
           "para el catalogo accesible."),

    E("0075", "barbell rear delt raise", "standing", standing=True, bal="low",
      grip="firm", flex="low",
      stress=js(lumbar="high", sh="high", hip="moderate", wr="moderate",
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
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Elevacion posterior con barra desde posicion inclinada: combina lo "
           "peor de 0293 dumbbell bent over row —isometrico lumbar sostenido— "
           "con abduccion horizontal de hombro a brazo extendido, que es el "
           "arco donde el manguito se pinza. Doble contraindicacion, lumbar y "
           "hombro. 2470 dumbbell lying on floor rear delt raise da el mismo "
           "estimulo tumbado, sin el isometrico lumbar."),

    E("1756", "barbell single leg deadlift", "standing", standing=True,
      bal="high", sl=True, grip="firm", flex="moderate",
      stress=js(hip="high", lumbar="high", knee="moderate", ank="moderate"),
      lat="unilateral", pat="hinge", diff=5, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "lumbar_disc",
              "lumbar_pain", "sciatica", "osteoporosis", "hip_replacement",
              "ankle_injury", "limited_grip", "vertigo", "hernia_abdominal",
              "multiple_sclerosis", "visual_impairment", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "knee_pain", "knee_injury",
            "plantar_fasciitis", "hypertension", "glaucoma", "dysautonomia",
            "elderly_65plus", "obesity", "hypermobility", "osteoarthritis",
            "pelvic_floor_dysfunction", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "elbow_injury"],
      why="Difficulty 5: es el peso muerto de 1459 con la base de apoyo "
           "reducida a un pie y una barra larga que amplifica cualquier "
           "oscilacion. visual_impairment entra a contraindicacion —unico "
           "criterio de Capa A que lo separa del romanian deadlift bilateral— "
           "porque el equilibrio unipodal cargado depende de referencia "
           "visual. Progresion, no ejercicio de entrada."),

    E("0121", "barbell upright row v. 3", "standing", standing=True,
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
      why="Misma familia que 0120 barbell upright row pero con agarre mas "
           "ancho que los hombros. El agarre ancho reduce la desviacion "
           "cubital de la muneca y baja algo el pinzamiento: carpal_tunnel "
           "baja de contraindicacion a precaucion y wrist pasa de high a "
           "moderate. El hombro sigue contraindicado —el arco de elevacion "
           "interna es el mismo— asi que es una variante menos mala, "
           "no una variante segura."),

    E("1749", "ez bar standing french press", "standing", standing=True,
      bal="low", oh=True, grip="firm", axial="low",
      stress=js(sh="high", el="high", wr="moderate", lumbar="moderate",
                cerv="low"),
      pat="isolation", diff=3, rom="high",
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
            "plantar_fasciitis"],
      why="Frente a 1747 ez bar french press on exercise ball el cambio no es "
           "menor: al salir del balon desaparecen limited_balance y vertigo de "
           "la contraindicacion, pero entra cannot_stand y aparece "
           "hiperextension lumbar compensatoria al bajar la barra detras de la "
           "cabeza —lumbar sube a moderate. Un perfil gana y otro pierde; "
           "no es una progresion lineal."),

    E("3204", "arms overhead full sit-up (male)", "supine", floor=True,
      oh=True, flex="high",
      stress=js(lumbar="high", hip="high", cerv="moderate", sh="moderate"),
      pat="core_flexion", diff=3, rom="high",
      ortho="none", change="high", valsalva="moderate", iso="low",
      metab="moderate", pelvic="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "no_overhead",
              "lumbar_disc", "lumbar_pain", "sciatica", "osteoporosis",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "shoulder_impingement",
              "rotator_cuff", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["cervical_injury", "neck_pain", "si_joint_pain", "hip_pain",
            "hip_replacement", "postpartum", "obesity", "elderly_65plus",
            "migraine", "hypertension"],
      safe=["cannot_stand", "limited_balance", "limited_grip",
            "knee_injury", "knee_pain", "ankle_injury", "wrist_injury",
            "carpal_tunnel", "plantar_fasciitis", "dysautonomia"],
      why="Los brazos estirados sobre la cabeza alargan el brazo de palanca: "
           "es el sit-up mas caro en lumbar de todo el bloque a igual rango. "
           "Ademas no_overhead, shoulder_impingement y rotator_cuff entran a "
           "contraindicacion, cosa que no pasa en 3202 half sit-up ni en 0735 "
           "sit-up v.2. hip_replacement baja a precaucion —no contraindicado "
           "como en 0456— porque las piernas se quedan en el suelo."),

    E("0457", "flexion leg sit up (straight arm)", "supine", floor=True,
      oh=True, flex="high",
      stress=js(lumbar="high", hip="high", cerv="moderate", sh="moderate"),
      pat="core_flexion", diff=4, rom="high",
      ortho="none", change="high", valsalva="moderate", iso="moderate",
      metab="high", laxity="moderate", pelvic="high", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "no_overhead",
              "lumbar_disc", "lumbar_pain", "sciatica", "cervical_injury",
              "neck_pain", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "hip_replacement", "shoulder_impingement", "rotator_cuff",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "postpartum", "obesity",
            "elderly_65plus", "migraine", "hypertension", "chronic_fatigue",
            "fibromyalgia", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "limited_grip",
            "knee_injury", "knee_pain", "ankle_injury", "wrist_injury",
            "carpal_tunnel", "plantar_fasciitis", "dysautonomia"],
      why="El V-up: piernas rectas y brazos estirados subiendo a la vez. Es "
           "0456 con las dos palancas extendidas al maximo, difficulty 4 y el "
           "peor del grupo. Acumula la contraindicacion lumbar de 0456, la de "
           "hombro de 3204 y suma cervical_injury, porque el cuello sostiene "
           "la cabeza sin apoyo durante todo el recorrido."),

    E("1511", "hamstring stretch", "standing", standing=True, bal="moderate",
      flex="moderate", headdown=True,
      stress=js(hip="moderate", lumbar="moderate", knee="low", ank="low"),
      lat="unilateral", pat="mobility_stretch", diff=1, rom="high",
      ortho="high", change="moderate", valsalva="none", iso="moderate",
      metab="none", laxity="moderate", pelvic="low", temp="none",
      contra=["cannot_stand", "wheelchair", "sciatica", "lumbar_disc",
              "hip_replacement"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "hypermobility",
            "knee_injury", "osteoarthritis", "limited_balance",
            "dysautonomia", "vertigo", "glaucoma", "retinal_detachment_risk",
            "hypertension", "elderly_65plus", "osteoporosis",
            "varicose_veins", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Estiramiento facil de subestimar: al plegarse hacia el pie la "
           "cabeza queda bajo el corazon —head_below_heart True, mismo "
           "criterio que 1390 seated calf stretch— y la traccion del nervio "
           "ciatico es directa, por eso sciatica contraindicado. 1576 leg up "
           "hamstring stretch da el mismo estiramiento tumbado, sin carga "
           "ortostatica ni equilibrio: es la sustitucion para perfil mayor "
           "o con disautonomia."),
]

CONFIDENCE_OVERRIDES = {
    "3655": 0.75,  # E1 lo marca cardio_steady; se reclasifica a lunge
    "0360": 0.75,  # posible duplicado de 0361, a resolver en E3
    "1015": 0.80,  # el texto mezcla pallof "vertical" con la version clasica
    "3552": 0.80,  # sin patron en E1, se infiere del texto
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
    print(f"lote 36: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
