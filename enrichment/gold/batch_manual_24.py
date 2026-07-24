#!/usr/bin/env python3
"""Lote 24 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1648", "dumbbell alternate seated hammer curl", "seated", grip="firm",
      lat="alternating", stress=js(el="moderate", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "dysautonomia",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "plantar_fasciitis", "sciatica"],
      why="Curl martillo alternado sentado, sin apoyo del codo. Torso erguido y "
           "codos pegados: la columna no participa, lumbar_disc y sciatica en "
           "safe_for. gripdur high porque la mancuerna del brazo que descansa "
           "se sigue sosteniendo — detalle que distingue el alternado del "
           "unilateral puro."),

    E("3202", "half sit-up (male)", "supine", floor=True, grip="none",
      flex="high", stress=js(lumbar="high", cerv="high", hip="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="low", pelvic="high", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "cervical_injury", "neck_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "cannot_get_on_floor",
              "cannot_lie_supine", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "postpartum", "obesity",
            "elderly_65plus", "migraine", "hypertension"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "dysautonomia"],
      why="Torso a 45 grados con manos detras de la cabeza: mismo perfil que "
           "0992 pero sin banda. cerv high por la traccion manual del cuello, "
           "criterio ya fijado en 3640. Cuarta entrada de la familia de "
           "flexion de tronco (0832, 0992, 3640, 3202), todas con el mismo "
           "bloque de exclusiones."),

    E("1422", "pelvic tilt into bridge", "supine", floor=True, grip="none",
      ext="low", stress=js(hip="moderate", lumbar="low", knee="low"),
      pat="hinge", diff=1, rom="low",
      ortho="none", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="moderate", gripdur="none", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine"],
      caut=["lumbar_disc", "si_joint_pain", "sciatica", "hip_pain",
            "pelvic_floor_dysfunction", "hernia_abdominal", "knee_pain",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "one_arm_only", "osteoporosis",
            "lumbar_pain", "elderly_65plus"],
      why="CUARTA entrada de la familia del puente y la mas suave de todas: "
           "diff 1, rom low, sin carga. La basculacion pelvica es el ejercicio "
           "de rehabilitacion lumbar mas prescrito que existe, por eso "
           "lumbar_pain entra en safe_for — primer caso del proyecto. "
           "lumbar_disc queda en cautions por sesgo conservador. Solo dos "
           "contraindicaciones, ambas de acceso al suelo."),

    E("3021", "scapula push-up", "plank", floor=True, grip="none",
      stress=js(wr="high", sh="moderate", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=2, rom="low",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="none",
      temp="low",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement"],
      caut=["rotator_cuff", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "obesity", "elderly_65plus", "hypermobility",
            "recent_abdominal_surgery", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "knee_injury", "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="Mismo problema de nomenclatura que 0688 scapular pull-up: un "
           "push-up escapular real es solo protraccion y retraccion sin "
           "flexionar el codo, pero el texto dice 'keeping your elbows close "
           "to your body' mientras se baja el pecho. Clasificado como flexion "
           "de rango corto. Confianza 0.65. Segundo caso de la familia "
           "'scapula' con la misma ambiguedad — vale revisarla entera en E3."),

    E("1748", "ez bar lying close grip triceps extension behind head",
      "bench_supine", oh=True, grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "no_overhead",
              "shoulder_impingement", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["rotator_cuff", "wrist_injury", "carpal_tunnel", "hypermobility",
            "cervical_injury", "hypertension", "osteoporosis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis"],
      why="La barra baja POR DETRAS de la cabeza, no a la frente: eso lleva el "
           "hombro a flexion completa y mueve shoulder_impingement de cautions "
           "a contra, a diferencia de 0056. Es el criterio que separa a toda la "
           "familia rompecraneos: 'to the forehead' vs 'behind the head'."),

    E("3361", "skater hops", "standing", standing=True, bal="high", sl=True,
      grip="none", impact="high", lat="alternating",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="low"),
      pat="cardio_interval", diff=4, rom="high",
      ortho="high", change="moderate", valsalva="low", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "ankle_injury",
              "hip_replacement", "osteoporosis", "plantar_fasciitis",
              "pelvic_floor_dysfunction", "vertigo", "multiple_sclerosis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "osteoarthritis", "lumbar_pain", "si_joint_pain",
            "dysautonomia", "hypertension", "cardiac", "obesity",
            "elderly_65plus", "chronic_fatigue", "postpartum", "asthma",
            "varicose_veins", "pregnancy_1st"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Saltos laterales con aterrizaje en una pierna: impact high con "
           "componente de corte lateral, el mecanismo tipico de lesion de "
           "ligamento cruzado y tobillo. bal high y sl true. Igual que "
           "1688, no exige nada de los brazos — util para quien tiene el tren "
           "superior comprometido pero el inferior sano."),

    E("0661", "push-up inside leg kick", "plank", floor=True, bal="moderate",
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
      why="Flexion con patada lateral: la pierna que se abre es abduccion en "
           "cadena cerrada, y al hacerlo el peso se desplaza a un lado del "
           "cuerpo. hip_replacement y si_joint_pain a contra por el mismo "
           "criterio que 0778, aunque aca la cadera no llegue a flexion "
           "profunda."),

    E("1365", "upper back stretch", "standing", standing=True, bal="low",
      oh=True, grip="none", stress=js(sh="moderate", cerv="low", el="low"),
      pat="mobility_stretch", diff=1, rom="high",
      ortho="high", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff"],
      caut=["shoulder_pain", "hypermobility", "elbow_injury",
            "cervical_injury", "dysautonomia", "elderly_65plus",
            "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "sciatica",
            "plantar_fasciitis", "osteoporosis", "hernia_abdominal"],
      why="Gemelo de 1405 con una diferencia decisiva: 1405 eleva los brazos "
           "al frente, este los lleva SOBRE la cabeza. Eso suma no_overhead a "
           "contraindicaciones y sube ortho a high (brazos elevados de pie). "
           "Mismo estiramiento, un escalon menos de accesibilidad."),

    E("0458", "floor fly (with barbell)", "supine", floor=True, grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel", "hypertension", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis", "cannot_transfer_to_bench",
            "osteoporosis"],
      why="TEXTO IMPOSIBLE: una apertura ('fly') separa las manos hacia los "
           "lados, y con una barra recta las manos estan unidas. Clasificado "
           "como press en el suelo, que es lo unico ejecutable. Confianza 0.60. "
           "Hallazgo util igual: el SUELO frena el codo antes del rango final, "
           "asi que el hombro queda en cautions y no en contra — la version en "
           "banco del mismo movimiento seria mas agresiva."),

    E("0497", "inverted row v. 2", "standing", standing=True, bal="moderate",
      grip="firm", stress=js(sh="moderate", el="moderate", wr="moderate",
                             lumbar="moderate"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="high",
      temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury",
              "limited_balance"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "tendinitis_elbow", "lumbar_pain", "obesity",
            "elderly_65plus", "dysautonomia", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "sciatica", "plantar_fasciitis"],
      why="CIERRA UN HUECO parcial anotado en el lote 19: traccion horizontal "
           "para quien NO puede bajar al suelo. Complementa a 2298 (que si "
           "exige suelo). Entre los dos, el patron horizontal_pull ya tiene "
           "salida tanto para cannot_get_on_floor como para cannot_stand — "
           "pero sigue sin haber uno para quien tiene las DOS restricciones."),

    E("0658", "push-up (wall) v. 2", "standing", standing=True, bal="low",
      grip="none", stress=js(wr="moderate", sh="low", el="low", lumbar="low"),
      pat="horizontal_push", diff=1, rom="low",
      ortho="moderate", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair"],
      caut=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
            "plantar_fasciitis", "dysautonomia"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side", "cannot_transfer_to_bench",
            "no_overhead", "limited_grip", "knee_injury", "knee_pain",
            "hip_replacement", "lumbar_disc", "elderly_65plus", "osteoporosis",
            "obesity"],
      why="DUPLICADO EXACTO de 0659 (lote 17). El texto describe el mismo "
           "movimiento con otras palabras. Clasificado identico a proposito "
           "para que el motor los trate igual, pero deben marcarse como "
           "duplicados funcionales: ofrecer dos veces la flexion contra la "
           "pared a un perfil muy restringido daria una falsa sensacion de "
           "variedad justo donde el catalogo es mas pobre."),

    E("0716", "side push neck stretch", "seated", grip="light", rot="low",
      lat="unilateral", stress=js(cerv="moderate", sh="low", el="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="low", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="low", temp="low",
      contra=["cervical_injury", "neck_pain", "osteoporosis"],
      caut=["hypermobility", "vertigo", "migraine", "osteoarthritis",
            "rheumatoid_arthritis", "shoulder_impingement", "limited_grip",
            "one_arm_only"],
      safe=["cannot_stand", "wheelchair", "limited_balance",
            "cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "sciatica",
            "plantar_fasciitis", "dysautonomia", "hernia_abdominal",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      why="Version asistida de 1403: la mano empuja la cabeza para forzar el "
           "rango. Esa presion externa es la diferencia — neck_pain y "
           "osteoporosis pasan de cautions a contra, porque el limite deja de "
           "ponerlo el propio musculo. 23 en safe_for, segundo del ranking "
           "detras de 1403. Regla general: si el texto dice 'apply pressure', "
           "sube un escalon de restriccion cervical."),

    E("0795", "standing single leg curl", "standing", standing=True,
      bal="moderate", sl=True, grip="none",
      stress=js(knee="moderate", hip="low", ank="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement"],
      caut=["knee_pain", "osteoarthritis", "hip_pain", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "vertigo", "elderly_65plus",
            "multiple_sclerosis", "pregnancy_3rd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only",
            "lumbar_disc", "sciatica", "hip_replacement"],
      why="Isquiotibiales de pie sin equipamiento ni agarre: 16 en safe_for. "
           "Apoyo unipodal con las manos en la cadera, asi que bal moderate y "
           "limited_balance a contra. Alternativa directa a 0696 y 0339 para "
           "quien no puede bajar al suelo."),

    E("0826", "vertical leg raise (on parallel bars)", "hanging", grip="firm",
      standing=True, flex="high",
      stress=js(sh="high", el="moderate", lumbar="high", wr="moderate",
                hip="moderate"),
      pat="core_flexion", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "lumbar_disc", "sciatica", "cannot_stand",
              "one_arm_only", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "wrist_injury", "carpal_tunnel",
            "hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "osteoporosis", "postpartum", "hypertension"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "no_overhead"],
      why="Elevacion de piernas apoyado en barras paralelas, no colgado de una "
           "barra alta: el hombro sostiene por DEBAJO en vez de estar en "
           "suspension. Eso baja laxity de high a moderate y —clave— pone "
           "no_overhead en safe_for, imposible en 2333 o 1764. Es la "
           "sustitucion de la elevacion colgada para hombros que no toleran "
           "posicion overhead."),

    E("0841", "weighted pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, axial="low",
      stress=js(sh="high", el="high", wr="moderate", lumbar="low"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="low",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "tendinitis_elbow", "cannot_stand",
              "one_arm_only", "hypermobility", "osteoporosis",
              "elderly_65plus", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["cervical_injury", "hypertension", "cardiac", "obesity",
            "chronic_fatigue", "rheumatoid_arthritis", "glaucoma",
            "retinal_detachment_risk"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="Cuarto eslabon de la cadena de dominadas y el mas duro: "
           "0970 (con banda, diff 2) → 1763/0678/0720 (libre, diff 4) → "
           "0841 (lastrada, diff 5). El lastre suma valsalva high, que arrastra "
           "glaucoma y desprendimiento de retina a cautions, y saca "
           "hypermobility y osteoporosis a contraindicacion."),

    E("0975", "band close-grip push-up", "plank", floor=True, grip="none",
      stress=js(wr="high", el="high", sh="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "elbow_injury",
              "tendinitis_elbow", "cannot_get_on_floor", "cannot_lie_prone",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "lumbar_pain",
            "lumbar_disc", "obesity", "elderly_65plus", "hernia_abdominal",
            "pelvic_floor_dysfunction", "postpartum", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "knee_injury", "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="La banda va alrededor de los brazos, no en las manos: grip_required "
           "sigue siendo none y limited_grip queda en safe_for pese a que el "
           "equipamiento sea 'band'. Buen recordatorio de que el implemento no "
           "determina el requisito de agarre — hay que leer donde se sujeta."),

    E("1646", "dumbbell alternate hammer preacher curl", "seated", grip="firm",
      lat="alternating", stress=js(el="high", wr="low", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_transfer_to_bench", "hypermobility"],
      caut=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis",
            "shoulder_impingement", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "lumbar_pain", "sciatica", "dysautonomia", "plantar_fasciitis",
            "cannot_sit_unsupported"],
      why="El banco predicador apoya el brazo entero y el pecho, asi que ortho "
           "baja a low y cannot_sit_unsupported entra en safe_for. Pero ese "
           "mismo apoyo impide encoger el hombro al final del descenso: el "
           "codo queda en extension completa bajo carga — el a high y "
           "hypermobility a contra, unico curl del proyecto con esa exclusion."),

    E("1655", "dumbbell biceps curl squat", "standing", standing=True,
      bal="low", grip="firm",
      stress=js(el="moderate", wr="low", lumbar="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury"],
      caut=["tendinitis_elbow", "wrist_injury", "dysautonomia", "limited_balance",
            "hypertension", "elderly_65plus", "varicose_veins",
            "rheumatoid_arthritis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "sciatica", "plantar_fasciitis"],
      why="CONFLICTO GRAVE NOMBRE vs TEXTO: se llama 'curl squat' y E1 lo "
           "clasifico como patron squat, pero el texto NO menciona sentadilla "
           "en ningun momento — es un curl de pie y nada mas. Clasificado como "
           "isolation. Si se hubiera aceptado a E1, el motor lo habria excluido "
           "para rodilla y protesis de cadera sin motivo: knee_injury y "
           "hip_replacement estan en safe_for. Confianza 0.60."),
]

CONFIDENCE_OVERRIDES = {
    "0458": 0.60,  # una apertura con barra recta es mecanicamente imposible
    "1655": 0.60,  # el nombre dice squat, el texto describe solo un curl
    "3021": 0.65,  # misma ambiguedad que la familia 'scapula'
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
    print(f"lote 24: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
