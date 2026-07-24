#!/usr/bin/env python3
"""Lote 21 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("3123", "resistance band seated biceps curl", "seated", grip="light",
      stress=js(el="low", sh="low", wr="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", valsalva="none", metab="low", laxity="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel",
            "rheumatoid_arthritis", "cannot_sit_unsupported"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "lumbar_pain", "sciatica", "dysautonomia", "plantar_fasciitis",
            "osteoporosis", "cannot_get_on_floor", "cannot_kneel",
            "cannot_transfer_to_bench", "elderly_65plus"],
      why="NUEVO MAXIMO DE ACCESIBILIDAD: 17 en safe_for y solo 2 "
           "contraindicaciones, supera a standing calves (16). El texto dice "
           "'sit on a chair OR bench': no exige transferencia a banco de gimnasio, "
           "por eso cannot_transfer_to_bench entra en safe_for. Banda elastica = "
           "sin carga excentrica de golpe, valsalva none, diff 1. Es el ejercicio "
           "de bicep que el motor debe ofrecer cuando todo lo demas se filtro."),

    E("0422", "dumbbell standing one arm curl (over incline bench)", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", metab="low", laxity="low",
      gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury"],
      caut=["tendinitis_elbow", "limited_balance", "dysautonomia",
            "hypertension", "wrist_injury", "elderly_65plus", "lumbar_pain",
            "chronic_fatigue"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "one_arm_only", "knee_pain", "lumbar_disc", "ankle_injury",
            "plantar_fasciitis"],
      why="DUPLICADO de 1680 (lote 20): mismo texto salvo 'palm facing forward'. "
           "Clasificacion identica. Y E1 volvio a cometer el mismo error — "
           "bench_incline por la palabra 'bench' en el nombre, cuando el texto "
           "arranca con 'stand'. Tercera vez en dos lotes."),

    E("0262", "cross body crunch", "supine", floor=True, grip="none",
      flex="high", rot="moderate", lat="alternating",
      stress=js(lumbar="high", cerv="moderate", hip="low"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "cannot_get_on_floor",
              "cannot_lie_supine", "si_joint_pain",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "neck_pain", "hypertension",
            "obesity", "elderly_65plus", "pelvic_floor_dysfunction",
            "postpartum", "shoulder_impingement"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "dysautonomia"],
      why="Flexion + rotacion combinadas, la peor pareja para el disco. Las "
           "manos detras de la cabeza con codos abiertos invitan a traccionar el "
           "cuello: cervical moderate y cervical_injury en cautions. Contrasta "
           "con 0705 (puente lateral) — mismo objetivo abdominal, veredicto "
           "opuesto para hernia discal."),

    E("0034", "barbell decline bent arm pullover", "bench_supine", oh=True,
      grip="firm", stress=js(sh="high", el="moderate", lumbar="moderate",
                             wr="low"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "hypermobility", "glaucoma", "retinal_detachment_risk",
              "hernia_abdominal", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["shoulder_pain", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "hypertension", "cardiac", "dysautonomia", "vertigo", "migraine",
            "osteoporosis", "cervical_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis",
            "wrist_injury"],
      why="El peor pullover posible: suma el declinado (head_below_heart, toda "
           "la familia ocular) al rango final de hombro de 3010. La barra recta "
           "ademas fija la rotacion del hombro, quitando el margen que da la EZ. "
           "laxity high."),

    E("0630", "mountain climber", "plank", floor=True, grip="none",
      bal="low", impact="low", flex="moderate", lat="alternating",
      stress=js(wr="high", sh="moderate", hip="moderate", lumbar="moderate",
                knee="low"),
      pat="cardio_steady", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="high", laxity="low", pelvic="moderate", gripdur="none",
      temp="high",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement",
              "recent_abdominal_surgery", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cardiac", "hypertension", "asthma", "chronic_fatigue",
            "fibromyalgia", "multiple_sclerosis", "dysautonomia", "obesity",
            "elderly_65plus", "anemia", "diabetes", "rotator_cuff",
            "elbow_injury", "lumbar_pain", "hip_pain",
            "pelvic_floor_dysfunction", "postpartum", "epilepsy"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "hip_replacement", "ankle_injury", "plantar_fasciitis"],
      why="Version sin flexion de 3638 (lote 20): mismo perfil metabolico y "
           "termico, sin la carga de empuje. Es la sustitucion natural de 3638 "
           "para quien tolera el cardio pero no el push-up. Notable: sigue "
           "siendo apto para rodilla y tobillo, porque los pies se deslizan "
           "en vez de impactar."),

    E("3145", "push-up plus", "plank", floor=True, grip="none",
      stress=js(wr="high", sh="moderate", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["elbow_injury", "lumbar_pain", "lumbar_disc", "obesity",
            "elderly_65plus", "hernia_abdominal", "pelvic_floor_dysfunction",
            "postpartum", "plantar_fasciitis", "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "shoulder_impingement", "rotator_cuff"],
      why="EXCEPCION A LA REGLA DE LA FAMILIA: es el unico push-up del proyecto "
           "con shoulder_impingement y rotator_cuff en safe_for. El 'plus' es "
           "protraccion escapular, que activa el serrato anterior — ejercicio "
           "prescrito en rehabilitacion de discinesia escapular, la causa mecanica "
           "de muchos pinzamientos. El agregado no lo hace mas duro: lo hace "
           "terapeutico."),

    E("0467", "gorilla chin", "hanging", oh=True, grip="hanging_bodyweight",
      standing=True, stress=js(sh="high", el="high", wr="moderate",
                               lumbar="low"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "tendinitis_elbow", "cannot_stand", "one_arm_only"],
      caut=["hypermobility", "osteoporosis", "cervical_injury", "obesity",
            "rheumatoid_arthritis", "elderly_65plus", "shoulder_pain",
            "lumbar_pain", "hypertension"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="CORRECCION A E1: dijo standing, pero el texto termina en 'hang from "
           "the bar with your arms fully extended'. Es hanging. El nombre alude "
           "a una dominada con rodillas al pecho, pero el texto describe una "
           "dominada comun — clasificado por el texto, confianza 0.65."),

    E("0816", "triceps press", "standing", standing=True, bal="low",
      grip="none", flex="low",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "elbow_injury",
              "tendinitis_elbow"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "limited_balance", "dysautonomia", "hypertension", "lumbar_pain",
            "elderly_65plus"],
      safe=["no_overhead", "limited_grip", "cannot_get_on_floor",
            "cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "plantar_fasciitis"],
      why="Texto incoherente: 'extend your arms straight out in front' y despues "
           "'lower your body towards the ground' — no se sostiene "
           "mecanicamente sin decir contra que se empuja. Interpretado como "
           "empuje contra pared o superficie a la altura del pecho, que es la "
           "unica lectura viable de pie. Confianza 0.55, revision en E3."),

    E("1256", "barbell reverse grip decline bench press", "bench_supine",
      grip="firm", stress=js(wr="high", sh="moderate", el="moderate"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="high",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip", "elbow_injury",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "glaucoma", "retinal_detachment_risk", "hernia_abdominal",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "cardiac", "dysautonomia",
            "vertigo", "migraine", "tendinitis_elbow", "osteoporosis",
            "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "lumbar_disc", "no_overhead",
            "plantar_fasciitis"],
      why="Cuarta variante de press invertido: plano (2187), inclinado (1257), "
           "ancho (1258) y ahora declinado. Este suma head_below_heart y "
           "valsalva high a la muneca en supinacion. El eje que ordena la "
           "familia es la inclinacion del banco; el agarre es constante."),

    E("1720", "barbell lying back of the head tricep extension", "bench_supine",
      oh=True, grip="firm",
      stress=js(el="high", sh="high", wr="moderate", cerv="low"),
      pat="isolation", diff=4, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "hypermobility", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["wrist_injury", "carpal_tunnel", "hypertension", "osteoporosis",
            "cervical_injury", "shoulder_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis"],
      why="La barra baja DETRAS de la cabeza, no a la frente: eso lo saca de la "
           "familia rompecraneos y lo mete en la de extension overhead. sh sube "
           "de moderate a high y no_overhead pasa de caution (0060) a "
           "contraindicacion. Un centimetro de trayectoria cambia la capa de "
           "filtrado."),

    E("3669", "standing archer", "standing", standing=True, bal="low",
      grip="none", rot="moderate", lat="alternating",
      stress=js(lumbar="moderate", sh="moderate", hip="low"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "rotator_cuff", "limited_balance", "dysautonomia", "hypertension",
            "elderly_65plus", "osteoporosis", "hypermobility"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Rotacion de pie sin carga externa. Confirma la leccion del lote 16: "
           "aunque la rotacion sea suave, con hernia discal el motor corta por "
           "umbral de joint_stress. lumbar moderate y lumbar_disc a contra, "
           "coherente con esa regla. Para todo lo demas es muy accesible: 14 en "
           "safe_for."),

    E("3671", "ski step", "standing", standing=True, bal="high", sl=True,
      grip="none", impact="high",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="low"),
      pat="cardio_interval", diff=4, rom="moderate",
      ortho="high", change="moderate", valsalva="low", iso="low",
      metab="high", laxity="moderate", pelvic="high", gripdur="none",
      temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "plantar_fasciitis", "hip_replacement", "osteoporosis",
              "vertigo", "visual_impairment", "pelvic_floor_dysfunction",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cardiac", "hypertension", "asthma", "chronic_fatigue",
            "fibromyalgia", "multiple_sclerosis", "dysautonomia", "obesity",
            "elderly_65plus", "osteoarthritis", "hypermobility", "postpartum",
            "varicose_veins", "epilepsy", "si_joint_pain", "diabetes"],
      safe=["limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "no_overhead", "shoulder_impingement", "rotator_cuff",
            "cannot_get_on_floor", "cannot_kneel"],
      why="Saltos laterales con aterrizaje unipodal: el unico del lote con "
           "impact high, single_leg_support y balance high a la vez. Espejo de "
           "1306 (plyo push-up): alli el impacto era todo de miembro superior y "
           "quedaba apto para rodilla; aca es todo de miembro inferior y queda "
           "apto para hombro y muneca."),

    E("0002", "45° side bend", "standing", standing=True, bal="low",
      grip="none", rot="low",
      stress=js(lumbar="moderate", hip="low"),
      pat="core_rotation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica"],
      caut=["lumbar_pain", "si_joint_pain", "osteoporosis", "limited_balance",
            "dysautonomia", "hypertension", "elderly_65plus", "hypermobility",
            "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Flexion lateral de pie, diff 1, sin implemento. 16 en safe_for pero "
           "lumbar_disc a contra: la flexion lateral cargada por el propio "
           "torso comprime el disco de forma asimetrica. Es el caso donde "
           "'ejercicio suave' y 'apto para hernia' no coinciden."),

    E("0257", "circles knee stretch", "standing", standing=True, bal="high",
      grip="none", rot="low",
      stress=js(knee="high", ank="high", hip="low"),
      pat="mobility_stretch", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="none", iso="moderate", metab="low",
      laxity="high", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "vertigo",
              "visual_impairment"],
      caut=["knee_pain", "osteoarthritis", "hypermobility", "plantar_fasciitis",
            "elderly_65plus", "dysautonomia", "multiple_sclerosis",
            "diabetes", "varicose_veins"],
      safe=["limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "no_overhead", "shoulder_impingement", "rotator_cuff",
            "lumbar_disc", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone"],
      why="Se llama 'stretch' pero es rotacion de rodilla en carga, con las "
           "rodillas flexionadas y en puntas de pie. La rodilla no es una "
           "articulacion de rotacion: knee high y laxity high. balance high por "
           "el apoyo en el antepie sin sujecion. Segundo caso del proyecto de un "
           "'stretch' mas riesgoso que su nombre (el primero: iron cross "
           "stretch, lote 19)."),

    E("0284", "donkey calf raise", "standing", standing=True, bal="low",
      grip="light", flex="low",
      stress=js(ank="moderate", knee="low", lumbar="low", hip="low"),
      pat="isolation", diff=1, rom="high",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="low", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain", "hip_pain",
            "dysautonomia", "vertigo", "osteoarthritis", "varicose_veins",
            "elderly_65plus", "lumbar_pain", "hypermobility"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "one_arm_only",
            "hernia_abdominal", "osteoporosis"],
      why="El nombre dice 'donkey' (inclinado sobre un soporte) pero el texto "
           "describe una elevacion de talon de pie con las manos apoyadas para "
           "equilibrio. Clasificado por el texto. Comparado con 1397 (lote 18): "
           "el apoyo de manos baja el balance de moderate a low, y el escalon "
           "sube el rom_demand a high. Mejor opcion que 1397 para equilibrio "
           "limitado, peor para tobillo rigido."),

    E("0373", "dumbbell pronate-grip triceps extension", "seated", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="low", wr="moderate", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel",
            "cervical_injury", "hypertension", "hypermobility", "osteoporosis",
            "dysautonomia", "cannot_transfer_to_bench"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="Tercera entrada de la extension overhead sentada (2188, 2189, 0373). "
           "Diferencia real: 'palms facing down' con 'elbows pointing forward' "
           "fuerza pronacion mantenida — wr sube a moderate. Y el texto dice "
           "'bench OR chair', asi que cannot_transfer_to_bench baja de contra a "
           "caution, al reves que sus dos gemelas."),

    E("0464", "front plank with twist", "plank", floor=True, bal="moderate",
      grip="none", rot="moderate", lat="alternating", oh=True,
      stress=js(wr="high", sh="high", lumbar="moderate", el="moderate"),
      pat="core_rotation", diff=4, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement", "rotator_cuff",
              "no_overhead", "recent_abdominal_surgery", "lumbar_disc",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "lumbar_pain", "si_joint_pain", "hypermobility",
            "obesity", "elderly_65plus", "hernia_abdominal",
            "pelvic_floor_dysfunction", "postpartum", "shoulder_pain",
            "limited_balance"],
      safe=["cannot_stand", "limited_grip", "knee_injury", "knee_pain",
            "hip_replacement", "ankle_injury", "plantar_fasciitis"],
      why="Plancha que rota y abre el brazo al techo: al levantar una mano todo "
           "el peso pasa a la muneca contraria (wr high) y el brazo que sube "
           "termina por encima de la cabeza (oh true, no_overhead a contra). "
           "Es mucho mas que una plancha — comparar con 3699 (shoulder tap, "
           "lote 18), que es la version sin rotacion ni apertura."),

    E("0474", "hanging straight leg hip raise", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate",
                hip="high"),
      pat="core_flexion", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "cannot_stand", "one_arm_only", "hernia_abdominal",
              "recent_abdominal_surgery", "osteoporosis",
              "pelvic_floor_dysfunction", "postpartum",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "hypertension", "hip_pain", "rheumatoid_arthritis",
            "shoulder_pain"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="DUPLICADO funcional de 0475 (lote 20): mismo texto salvo el limite "
           "explicito 'until parallel to the ground'. Clasificacion identica. "
           "La familia colgada del dataset tiene al menos cuatro entradas casi "
           "iguales (0474, 0475, 1761, 1764) — candidata a colapso en E4."),
]

# La taxonomia pide confidence < 0.7 cuando el texto fuente es ambiguo.
CONFIDENCE_OVERRIDES = {
    "0816": 0.55,  # el texto no se sostiene mecanicamente
    "0467": 0.65,  # el nombre alude a rodillas al pecho, el texto no
    "0284": 0.70,  # el nombre dice donkey, el texto describe de pie
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
    print(f"lote 21: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
