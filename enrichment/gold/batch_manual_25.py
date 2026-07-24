#!/usr/bin/env python3
"""Lote 25 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1659", "dumbbell hammer curl on exercise ball", "seated", bal="moderate",
      grip="firm", stress=js(el="moderate", lumbar="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["limited_balance", "cannot_sit_unsupported", "limited_grip",
              "elbow_injury", "vertigo", "multiple_sclerosis"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "elderly_65plus", "osteoporosis",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "plantar_fasciitis"],
      why="PRIMERA ENTRADA DE LA FAMILIA 'PELOTA'. Sentarse en una superficie "
           "inestable convierte un curl trivial en un ejercicio de equilibrio: "
           "bal moderate, iso moderate por el core que estabiliza, y "
           "limited_balance a contraindicacion. vertigo y multiple_sclerosis "
           "tambien — el riesgo real es caerse, no el peso. Compara con 1648, "
           "identico en banco firme y con diff 1."),

    E("1576", "leg up hamstring stretch", "supine", floor=True, grip="light",
      lat="unilateral", stress=js(hip="moderate", knee="low", lumbar="low"),
      pat="mobility_stretch", diff=1, rom="high",
      ortho="none", change="low", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="low", temp="low",
      contra=["sciatica", "hip_replacement", "cannot_get_on_floor",
              "cannot_lie_supine"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "hip_pain",
            "hypermobility", "knee_injury", "osteoarthritis",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "no_overhead",
            "shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "osteoporosis",
            "one_arm_only"],
      why="OJO CON ESTE: elevar la pierna recta con la cadera flexionada es "
           "literalmente la maniobra de Lasegue, la prueba clinica que se usa "
           "para PROVOCAR el dolor ciatico. sciatica a contraindicacion aunque "
           "sea un estiramiento suave de diff 1. Y llevar la rodilla al pecho "
           "supera los 90 grados: hip_replacement tambien."),

    E("0803", "superman push-up", "plank", floor=True, bal="high", grip="none",
      ext="moderate", lat="alternating",
      stress=js(wr="high", sh="high", lumbar="high", el="moderate",
                hip="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="high", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "lumbar_disc", "lumbar_pain", "sciatica",
              "cannot_get_on_floor", "cannot_lie_prone", "limited_balance",
              "hypermobility", "one_arm_only", "si_joint_pain",
              "recent_abdominal_surgery", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "shoulder_pain", "hip_pain", "obesity",
            "elderly_65plus", "chronic_fatigue", "hernia_abdominal",
            "fibromyalgia"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury"],
      why="Flexion sosteniendo el cuerpo sobre UNA mano y UN pie en diagonal, "
           "con extension lumbar simultanea. lumbar high por la extension bajo "
           "carga asimetrica, y laxity high por el hombro de apoyo unico. "
           "diff 5. La combinacion de antiextension y extension activa es "
           "contradictoria: por eso lumbar_pain sale a contra, no a cautions."),

    E("0972", "band bicycle crunch", "supine", floor=True, grip="light",
      flex="high", rot="high", lat="alternating",
      stress=js(lumbar="high", cerv="high", hip="moderate"),
      pat="core_rotation", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="low", pelvic="high", gripdur="low", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "cervical_injury",
              "neck_pain", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "cannot_get_on_floor", "cannot_lie_supine", "hip_replacement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "postpartum", "obesity", "elderly_65plus",
            "hypertension", "migraine", "fibromyalgia"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "knee_injury", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="Flexion MAS rotacion MAS manos detras de la cabeza, repetido y en "
           "ritmo: acumula los tres factores criticos de columna que la "
           "taxonomia separa. Peor que 3202 y 3640 juntos. hip_replacement a "
           "contra por la rodilla al pecho alternada."),

    E("1429", "wide grip pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "cannot_stand", "one_arm_only", "hypermobility"],
      caut=["osteoporosis", "obesity", "elderly_65plus", "tendinitis_elbow",
            "rheumatoid_arthritis", "cervical_injury", "chronic_fatigue"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="El agarre ancho abre el hombro y reduce el rango util: mas "
           "abduccion en el punto bajo, que es donde el manguito rotador sufre "
           "en suspension. Frente a 1763 (agarre al ancho de hombros), "
           "shoulder_pain e hypermobility suben de cautions a contra. Quinta "
           "variante de dominada del proyecto."),

    E("1201", "dumbbell burpee", "standing", floor=True, standing=True,
      bal="moderate", oh=True, grip="firm", impact="high", axial="moderate",
      stress=js(knee="high", ank="high", wr="high", sh="high",
                lumbar="high", hip="moderate", el="moderate"),
      pat="cardio_interval", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="high",
      contra=["cannot_stand", "wheelchair", "cannot_get_on_floor",
              "cannot_lie_prone", "limited_balance", "limited_grip",
              "knee_injury", "knee_replacement", "knee_pain", "ankle_injury",
              "wrist_injury", "carpal_tunnel", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "osteoporosis",
              "hip_replacement", "cardiac", "lumbar_disc", "lumbar_pain",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "plantar_fasciitis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "dysautonomia", "obesity", "elderly_65plus",
            "chronic_fatigue", "fibromyalgia", "multiple_sclerosis",
            "postpartum", "asthma", "epilepsy", "glaucoma",
            "retinal_detachment_risk", "elbow_injury"],
      safe=[],
      why="SEXTO safe_for vacio y NUEVO RECORD: 28 contraindicaciones. Es "
           "0501 jack burpee mas cargada, mas press sobre la cabeza y mas "
           "agarre. Satura los cinco ejes fisiologicos de 0501 y le suma "
           "valsalva high y overhead. Empata en 28 con el maximo de safe_for "
           "de 1403 neck side stretch — los dos extremos del catalogo tienen "
           "exactamente el mismo tamano, en direcciones opuestas."),

    E("0466", "gironda sternum chin", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, ext="moderate",
      stress=js(sh="high", el="moderate", lumbar="moderate", wr="moderate",
                cerv="moderate"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "cannot_stand", "one_arm_only", "hypermobility",
              "cervical_injury", "lumbar_disc"],
      caut=["osteoporosis", "obesity", "elderly_65plus", "neck_pain",
            "tendinitis_elbow", "rheumatoid_arthritis", "chronic_fatigue",
            "lumbar_pain"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="CORRECCION A E1, CUARTO CASO del sesgo de suspension (0688, 0678, "
           "0720, 0466): E1 leyo 'stand facing a high bar' como posicion de "
           "ejecucion. Es colgado. Ademas, llevar el ESTERNON a la barra "
           "obliga a arquear la columna en el aire — lumbar_disc a contra y "
           "cervical_injury tambien, algo que ninguna otra dominada tiene."),

    E("0642", "outside leg kick push-up", "plank", floor=True, bal="moderate",
      grip="none", lat="alternating",
      stress=js(wr="high", sh="moderate", hip="moderate", lumbar="moderate",
                el="moderate"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement", "hip_replacement",
              "si_joint_pain", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["rotator_cuff", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "hip_pain", "obesity", "elderly_65plus", "hernia_abdominal",
            "limited_balance", "chronic_fatigue"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "dysautonomia"],
      why="DUPLICADO FUNCIONAL DE 0661 (lote 24). 'inside leg kick' y 'outside "
           "leg kick' describen el mismo gesto: patada lateral con la pierna "
           "recta durante la flexion. Clasificado identico. Cuarto grupo de "
           "duplicados detectado en el dataset."),

    E("0660", "push-up close-grip off dumbbell", "plank", floor=True,
      grip="firm", stress=js(el="high", sh="moderate", wr="low",
                             lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_get_on_floor", "cannot_lie_prone",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "hypermobility", "lumbar_pain", "lumbar_disc", "obesity",
            "elderly_65plus", "hernia_abdominal", "pelvic_floor_dysfunction",
            "postpartum", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "carpal_tunnel"],
      why="SEGUNDA VIA para la muneca. Agarrar las mancuernas mantiene la "
           "muneca NEUTRA en vez de extendida: wr baja a low y carpal_tunnel "
           "entra en safe_for. Distinto de 1467, que lo resuelve apoyando en "
           "antebrazos. Pero el precio es opuesto: aca hace falta agarre firme, "
           "asi que limited_grip pasa a contra — en 1467 estaba en safe_for. "
           "Dos soluciones al mismo problema, excluyentes entre si."),

    E("1746", "exercise ball supine triceps extension", "seated",
      bal="moderate", oh=True, grip="firm",
      stress=js(sh="high", el="high", lumbar="moderate", cerv="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "limited_balance",
              "cannot_sit_unsupported", "vertigo", "multiple_sclerosis"],
      caut=["tendinitis_elbow", "cervical_injury", "hypertension",
            "hypermobility", "osteoporosis", "dysautonomia", "lumbar_pain",
            "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "plantar_fasciitis"],
      why="El nombre dice 'supine' pero el texto dice 'sit on an exercise "
           "ball': es sentado. Confianza 0.70. Segunda entrada de la familia "
           "pelota, y la peor combinacion posible — peso sobre la cabeza en "
           "una superficie inestable. La caida seria hacia atras con una "
           "mancuerna detras de la nuca."),

    E("1773", "one arm towel row", "standing", standing=True, bal="moderate",
      grip="firm", flex="moderate", lat="unilateral",
      stress=js(lumbar="high", sh="moderate", el="moderate", wr="moderate"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "rotator_cuff", "wrist_injury", "carpal_tunnel", "limited_balance",
            "hypertension", "obesity", "elderly_65plus", "osteoporosis",
            "dysautonomia"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "one_arm_only",
            "plantar_fasciitis", "hip_replacement"],
      why="Mismo perfil que 1330: 'bend forward at the waist' con el torso en "
           "voladizo y SIN apoyo — lumbar high, lumbar_disc y sciatica a "
           "contra. Aca es peor que 1330 porque no hay rodilla ni mano "
           "apoyada en un banco. Criterio ya fijado en el lote 19: el apoyo "
           "del torso decide la lumbar."),

    E("2355", "arm slingers hanging bent knee legs", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate",
                hip="moderate"),
      pat="core_flexion", diff=4, rom="moderate",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "lumbar_disc", "sciatica", "cannot_stand", "one_arm_only",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hypermobility", "osteoporosis",
            "obesity", "elderly_65plus", "chronic_fatigue", "hypertension",
            "pelvic_floor_dysfunction", "postpartum", "hip_pain"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="DUPLICADO FUNCIONAL DE 1764 (lote 19): elevacion de rodillas "
           "colgado. Quinto grupo de duplicados. La cadena de suspension queda "
           "entonces con tres niveles reales y dos nombres repetidos: "
           "1764=2355 (rodillas) → 2333 (piernas rectas) → 1761 (con "
           "rotacion)."),

    E("3239", "kneeling plank tap shoulder (male)", "plank", floor=True,
      bal="moderate", grip="none", lat="alternating",
      stress=js(wr="high", sh="moderate", lumbar="moderate", el="low"),
      pat="core_antiextension", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["rotator_cuff", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "hypertension", "obesity", "pelvic_floor_dysfunction", "postpartum",
            "hernia_abdominal", "elderly_65plus", "rheumatoid_arthritis",
            "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "knee_injury", "knee_pain",
            "hip_replacement", "limited_grip", "ankle_injury", "cannot_kneel"],
      why="CORRECCION A E1 y DUPLICADO. E1 dijo kneeling por la primera frase, "
           "pero el texto sigue con 'extend your legs behind you... into a "
           "plank position' — mismo patron que 1771 en el lote 23. Y es "
           "funcionalmente identico a 3699 shoulder tap (lote 17). "
           "cannot_kneel en safe_for: las rodillas se despegan."),

    E("3663", "reverse plank with leg lift", "supine", floor=True,
      bal="moderate", grip="none", ext="high", lat="alternating",
      stress=js(wr="high", sh="high", lumbar="moderate", hip="moderate",
                el="moderate"),
      pat="core_antiextension", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "cannot_get_on_floor", "cannot_lie_supine",
              "hypermobility", "lumbar_disc", "hip_replacement",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_pain", "elbow_injury", "lumbar_pain", "si_joint_pain",
            "obesity", "elderly_65plus", "chronic_fatigue", "osteoporosis",
            "hernia_abdominal", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "dysautonomia"],
      why="TERCERA LIMITACION DEL ENUM: la plancha invertida es boca arriba con "
           "el cuerpo suspendido entre manos y talones, y no hay valor que la "
           "describa. Quedo supine por ser la orientacion correcta. Los dedos "
           "apuntando a los pies llevan la muneca a extension EXTREMA bajo "
           "peso — wr high, peor que en cualquier plancha normal. Y el hombro "
           "queda en extension maxima, que es la posicion de fondos."),

    E("3664", "dumbbell side plank with rear fly", "side_lying", floor=True,
      bal="high", grip="firm", lat="unilateral", sl=True,
      stress=js(sh="high", el="moderate", hip="moderate", lumbar="low",
                wr="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["cannot_lie_on_side", "cannot_get_on_floor",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "elbow_injury", "limited_grip", "limited_balance",
              "hypermobility", "hip_replacement", "si_joint_pain",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["wrist_injury", "carpal_tunnel", "hip_pain", "lumbar_pain",
            "obesity", "elderly_65plus", "chronic_fatigue", "fibromyalgia",
            "osteoporosis", "rheumatoid_arthritis"],
      safe=["cannot_stand", "no_overhead", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis"],
      why="Tercer escalon de la familia del puente lateral: 0705 (simple) → "
           "1774/1775 (con pierna) → 3664 (con mancuerna). diff 5. El brazo de "
           "arriba deja de estabilizar para levantar peso, asi que el hombro de "
           "abajo sostiene todo — sh high y laxity high. lumbar sigue en low: "
           "la base espinal-neutra del puente lateral se mantiene incluso aca."),

    E("0065", "barbell one arm floor press", "supine", floor=True, grip="firm",
      lat="unilateral", stress=js(sh="moderate", el="high", wr="high",
                                  lumbar="low"),
      pat="horizontal_push", diff=4, rom="low",
      ortho="none", change="moderate", valsalva="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip", "elbow_injury",
              "cannot_get_on_floor", "cannot_lie_supine", "hypermobility",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "tendinitis_elbow",
            "hypertension", "osteoporosis", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis", "cannot_transfer_to_bench"],
      why="Sostener una BARRA con una sola mano y en supinacion es "
           "mecanicamente muy inestable — el desequilibrio de la barra es el "
           "riesgo real, no el peso. Confianza 0.60, el texto describe algo que "
           "casi nadie ejecuta asi. Dato util igual: el suelo frena el codo "
           "antes del rango final, por eso rom low y el hombro queda en "
           "cautions pese a ser un press."),

    E("0353", "dumbbell one arm concentration curl (on stability ball)",
      "seated", bal="moderate", grip="firm", flex="low", lat="unilateral",
      stress=js(el="moderate", lumbar="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["limited_balance", "cannot_sit_unsupported", "limited_grip",
              "elbow_injury", "vertigo", "multiple_sclerosis"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "lumbar_disc",
            "dysautonomia", "elderly_65plus", "osteoporosis", "hip_pain"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis"],
      why="Tercera entrada de la familia pelota, y el par exacto de 1669 (lote "
           "22) que es el mismo curl de concentracion en banco firme. La "
           "diferencia completa: 1669 tiene diff 1 y lumbar_disc en safe_for; "
           "este tiene diff 2, lumbar_disc en cautions y cuatro "
           "contraindicaciones nuevas por inestabilidad. El asiento es el "
           "unico cambio."),

    E("0362", "dumbbell one arm triceps extension (on bench)", "seated",
      oh=True, grip="firm", lat="unilateral",
      stress=js(sh="high", el="high", cerv="low", wr="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench",
              "one_arm_only"],
      caut=["tendinitis_elbow", "cervical_injury", "neck_pain",
            "hypermobility", "osteoporosis", "dysautonomia", "lumbar_pain",
            "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc",
            "plantar_fasciitis", "cannot_sit_unsupported"],
      why="Detalle que cambia dos campos: 'place your other hand on the bench "
           "for support'. Esa mano de apoyo hace que cannot_sit_unsupported "
           "entre en safe_for —a diferencia de 2188 y 0453, que exigen "
           "sostenerse solos— pero tambien que one_arm_only pase a "
           "contraindicacion, aunque el ejercicio sea unilateral. El brazo "
           "libre no descansa: trabaja."),
]

CONFIDENCE_OVERRIDES = {
    "0065": 0.60,  # sostener una barra recta con una mano en supinacion
    "1746": 0.70,  # el nombre dice supine, el texto dice sentado en pelota
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
    print(f"lote 25: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
