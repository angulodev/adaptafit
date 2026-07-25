#!/usr/bin/env python3
"""Lote 26 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1663", "dumbbell one arm hammer preacher curl", "seated", grip="firm",
      lat="unilateral", stress=js(el="high", wr="low", sh="low"),
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
            "cannot_sit_unsupported", "one_arm_only"],
      why="Version unilateral de 1646 (lote 24), identica salvo que suma "
           "one_arm_only en safe_for. Mantiene el rasgo distintivo del banco "
           "predicador: el apoyo impide encoger el hombro, el codo queda en "
           "extension completa bajo carga y por eso hypermobility esta en "
           "contra — unico curl del proyecto con esa exclusion, junto a 1646."),

    E("1495", "oblique crunch v. 2", "supine", floor=True, grip="none",
      flex="high", rot="moderate", lat="alternating",
      stress=js(lumbar="high", cerv="moderate", hip="low"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="moderate", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "hernia_abdominal", "recent_abdominal_surgery",
              "cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "neck_pain",
            "pelvic_floor_dysfunction", "postpartum", "obesity",
            "elderly_65plus", "migraine"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "dysautonomia"],
      why="DETALLE QUE IMPORTA: el texto ofrece 'hands behind your head OR "
           "cross them over your chest'. Esa alternativa evita la traccion "
           "manual del cuello, asi que cerv baja a moderate y cervical_injury "
           "queda en cautions — a diferencia de 3640, 3202 y 0972, donde las "
           "manos detras de la cabeza son obligatorias y el cuello sale a "
           "contra. Una opcion en el texto cambia una contraindicacion."),

    E("1327", "close grip chin-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "cannot_stand", "one_arm_only"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "hypermobility", "osteoporosis", "obesity", "elderly_65plus",
            "rheumatoid_arthritis", "cervical_injury", "chronic_fatigue"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc"],
      why="LA DOMINADA MAS AMABLE CON EL HOMBRO. Agarre supinado y cerrado: "
           "el humero rota externamente y los codos van pegados, lo que reduce "
           "el pinzamiento. sh baja a moderate y shoulder_impingement pasa de "
           "contra a cautions — unica variante de la familia donde ocurre. El "
           "precio va al codo: el high y epicondilitis a contra. Es la "
           "sustitucion de 1429 wide grip para hombros sensibles."),

    E("3013", "low glute bridge on floor", "supine", floor=True, grip="none",
      ext="moderate", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="low", pelvic="moderate", gripdur="none", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "sciatica",
            "postpartum", "pelvic_floor_dysfunction", "hernia_abdominal",
            "knee_pain", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "one_arm_only"],
      why="DUPLICADO FUNCIONAL DE 0668 rear decline bridge (lote 19). Octavo "
           "grupo de duplicados. La familia del puente ya tiene cinco entradas "
           "para tres ejercicios reales: 1422 (basculacion) < 0668=3013 "
           "(simple) < 3561 (marcha) y 1409 (con barra)."),

    E("0684", "run (equipment)", "standing", standing=True, bal="moderate",
      grip="none", impact="high", lat="alternating",
      stress=js(knee="high", ank="high", hip="moderate", lumbar="moderate"),
      pat="cardio_steady", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="high",
      laxity="low", pelvic="high", gripdur="none", temp="high",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "ankle_injury", "hip_replacement",
              "osteoporosis", "plantar_fasciitis", "pelvic_floor_dysfunction",
              "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "osteoarthritis", "lumbar_disc",
            "lumbar_pain", "si_joint_pain", "dysautonomia", "hypertension",
            "cardiac", "obesity", "elderly_65plus", "chronic_fatigue",
            "asthma", "varicose_veins", "multiple_sclerosis", "postpartum",
            "vertigo", "pregnancy_2nd"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "no_overhead", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "one_arm_only"],
      why="Trote en el lugar: impact high y pelvic high por el impacto "
           "repetido, temp high por duracion sostenida. Igual que 3361 y 1688, "
           "no pide nada del tren superior — 13 en safe_for de brazos y "
           "hombros. El cardio es el patron que mas claramente separa "
           "restricciones de tren inferior y superior."),

    E("1311", "wide hand push up", "plank", floor=True, grip="none",
      stress=js(sh="high", wr="high", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "cannot_get_on_floor",
              "cannot_lie_prone", "recent_abdominal_surgery",
              "pregnancy_3rd"],
      caut=["elbow_injury", "hypermobility", "lumbar_pain", "lumbar_disc",
            "obesity", "elderly_65plus", "hernia_abdominal",
            "pelvic_floor_dysfunction", "postpartum", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "knee_injury", "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="El texto se contradice —'hands wider than shoulder-width' pero "
           "'elbows close to your sides'— y manda la posicion de las manos, "
           "que es lo que da nombre al ejercicio. Manos anchas = mas abduccion "
           "de hombro: sh high y shoulder_pain a contra, igual que en 1429 wide "
           "grip pull-up. El ancho de agarre se comporta igual en empuje y en "
           "traccion."),

    E("1355", "one arm against wall", "standing", standing=True, bal="low",
      grip="none", lat="unilateral",
      stress=js(sh="moderate", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="low",
      ortho="moderate", change="none", valsalva="low", iso="high", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement"],
      caut=["rotator_cuff", "shoulder_pain", "elbow_injury", "wrist_injury",
            "dysautonomia", "hypertension", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_lie_on_side",
            "cannot_transfer_to_bench", "limited_grip", "carpal_tunnel",
            "no_overhead", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "lumbar_disc", "lumbar_pain", "sciatica",
            "plantar_fasciitis", "osteoporosis", "one_arm_only"],
      why="Isometrico de dorsal empujando la pared: 19 en safe_for y solo tres "
           "contraindicaciones. Sin carga, sin agarre, sin suelo, sin rango. "
           "iso high es todo el estimulo. Es al patron de traccion lo que "
           "0659 push-up (wall) es al de empuje — aunque aca la activacion es "
           "isometrica y no hay recorrido articular."),

    E("0365", "dumbbell over bench neutral wrist curl", "seated", grip="firm",
      flex="low", stress=js(wr="high", el="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="none", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "cannot_transfer_to_bench", "cannot_sit_unsupported"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "tendinitis_elbow",
            "elbow_injury", "lumbar_pain", "dysautonomia"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis"],
      why="CUARTO conflicto nombre/texto de la familia de muneca. El texto "
           "dice a la vez 'rest your forearms on the bench, allowing your "
           "wrists to hang off the edge' (curl de muneca) y 'curl the "
           "dumbbells up towards your shoulders' (curl de codo). Con los "
           "antebrazos apoyados lo segundo es imposible, asi que manda el "
           "apoyo. Confianza 0.65."),

    E("0366", "dumbbell over bench one arm neutral wrist curl", "seated",
      grip="firm", flex="low", lat="unilateral",
      stress=js(wr="high", el="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="none", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "cannot_transfer_to_bench", "cannot_sit_unsupported"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "tendinitis_elbow",
            "elbow_injury", "lumbar_pain", "dysautonomia"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis"],
      why="Version unilateral de 0365, con el mismo texto contradictorio. "
           "Confianza 0.65. La familia de curls de muneca acumula ya cinco "
           "entradas con nombres que no coinciden con la descripcion (0393, "
           "1415, 0397, 0365, 0366): es un problema sistematico de la fuente, "
           "no casos sueltos."),

    E("0390", "dumbbell seated biceps curl (on stability ball)", "seated",
      bal="moderate", grip="firm",
      stress=js(el="moderate", lumbar="moderate", wr="low"),
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
      why="Cuarta entrada de la familia pelota y duplicado funcional de 1659 "
           "(la unica diferencia es agarre supinado en vez de martillo, que no "
           "cambia ninguna restriccion). Mismo bloque de contraindicaciones "
           "por inestabilidad."),

    E("0403", "dumbbell seated revers grip concentration curl", "seated",
      grip="firm", flex="low", lat="unilateral",
      stress=js(el="moderate", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "dysautonomia",
            "rheumatoid_arthritis", "hip_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis", "lumbar_disc"],
      why="El nombre dice 'reverse grip' pero el texto dice 'palm facing up', "
           "que es agarre supinado normal. Duplicado funcional de 1669 (lote "
           "22): mismo curl de concentracion en banco firme, mismo perfil, "
           "lumbar_disc en safe_for. Noveno grupo de duplicados."),

    E("0864", "dumbbell upright shoulder external rotation", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(sh="high", el="moderate", wr="low", cerv="low"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "limited_grip",
              "hypermobility"],
      caut=["elbow_injury", "cervical_injury", "neck_pain", "dysautonomia",
            "hypertension", "elderly_65plus", "chronic_fatigue",
            "osteoporosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "sciatica", "plantar_fasciitis"],
      why="CORRECCION A E1: E1 lo puso como core_rotation, pero no rota la "
           "columna — rota el HOMBRO. Es isolation. La posicion final (brazos "
           "en cruz a 90 grados y rotacion externa) es la del lanzador, la de "
           "mayor tension capsular anterior del hombro: laxity high y "
           "hypermobility a contra. Curioso: no_overhead en safe_for, porque "
           "las manos nunca pasan de la altura de la cabeza."),

    E("0971", "band assisted wheel rollerout", "kneeling", floor=True,
      grip="light", ext="high", stress=js(lumbar="high", sh="high",
                                          wr="moderate", knee="moderate",
                                          el="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "shoulder_impingement", "rotator_cuff",
              "no_overhead", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "osteoporosis", "hypermobility",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "obesity", "elderly_65plus", "chronic_fatigue", "postpartum",
            "limited_grip", "hypertension"],
      safe=["cannot_stand", "limited_balance", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="La rueda abdominal es el ejercicio de antiextension mas exigente que "
           "existe: en el punto lejano la lumbar aguanta todo el peso del "
           "cuerpo en extension con brazos sobre la cabeza. lumbar high, "
           "ext high, iso high y laxity high a la vez. La banda asiste pero no "
           "cambia el pico de carga, solo permite volver."),

    E("0978", "band front raise", "standing", standing=True, bal="low",
      grip="light", stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury", "limited_grip"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "sciatica", "plantar_fasciitis", "wrist_injury",
            "carpal_tunnel", "osteoporosis"],
      why="Equivalente con banda de 0376 dumbbell raise (lote 17), y mas "
           "accesible: la banda exige agarre ligero, asi que wrist_injury y "
           "carpal_tunnel entran en safe_for y limited_grip baja a cautions. "
           "16 en safe_for. Sube solo a paralelo — no_overhead sigue siendo "
           "apto, pero el arco de 60-120 grados es el del pinzamiento."),

    E("0985", "band kneeling twisting crunch", "kneeling", floor=True,
      grip="light", flex="moderate", rot="high", lat="alternating",
      stress=js(lumbar="high", knee="moderate", sh="moderate", hip="low"),
      pat="core_rotation", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "cannot_kneel",
              "cannot_get_on_floor", "knee_injury", "knee_replacement",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "knee_pain", "osteoarthritis", "hip_pain",
            "shoulder_impingement", "pelvic_floor_dysfunction", "postpartum",
            "obesity", "elderly_65plus", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "hip_replacement"],
      why="Rotacion lumbar resistida de rodillas. Suma dos filtros duros "
           "independientes: arrodillarse (rodilla, Capa A) y rotar la columna "
           "bajo carga (disco). rot high con banda es peor que sin ella — la "
           "resistencia es maxima justo en el final del giro, que es donde el "
           "disco esta mas comprometido."),

    E("0993", "band reverse fly", "standing", standing=True, bal="low",
      grip="light", stress=js(sh="moderate", el="low", wr="low",
                              lumbar="low"),
      pat="horizontal_pull", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement"],
      caut=["rotator_cuff", "shoulder_pain", "elbow_injury", "dysautonomia",
            "hypertension", "elderly_65plus", "limited_grip", "hypermobility"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "lumbar_disc", "lumbar_pain", "sciatica", "plantar_fasciitis",
            "wrist_injury", "carpal_tunnel", "osteoporosis",
            "hernia_abdominal"],
      why="CORRECCION A E1: E1 lo puso como horizontal_push. Es traccion — los "
           "brazos se separan tirando de la banda y las escapulas se juntan. "
           "El error importa para E4: como push habria competido con las "
           "flexiones en vez de complementarlas. 18 en safe_for, con la "
           "columna completamente fuera del cuadro."),

    E("1005", "band standing crunch", "standing", standing=True, bal="low",
      grip="light", flex="high",
      stress=js(lumbar="high", sh="moderate", hip="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="moderate", gripdur="moderate",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "pelvic_floor_dysfunction",
            "postpartum", "shoulder_impingement", "dysautonomia",
            "hypertension", "obesity", "elderly_65plus", "limited_grip"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "cervical_injury", "neck_pain"],
      why="PRIMER core_flexion QUE NO REQUIERE SUELO. Cubre un hueco real: "
           "hasta ahora los seis ejercicios de flexion de tronco (0832, 0992, "
           "3640, 3202, 0972, 1495) exigian tumbarse. Ademas, sin manos detras "
           "de la cabeza, cervical_injury y neck_pain entran en safe_for — "
           "unico del grupo. Sigue contraindicado para disco: la flexion "
           "cargada es flexion cargada, de pie o en el suelo."),

    E("1013", "band underhand pulldown", "standing", standing=True, bal="low",
      oh=True, grip="light",
      stress=js(sh="moderate", el="moderate", wr="low", lumbar="low"),
      pat="vertical_pull", diff=1, rom="high",
      ortho="moderate", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff"],
      caut=["shoulder_pain", "elbow_injury", "tendinitis_elbow",
            "dysautonomia", "hypertension", "elderly_65plus", "limited_grip",
            "cervical_injury", "hypermobility"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "wrist_injury",
            "carpal_tunnel", "osteoporosis", "one_arm_only"],
      why="HALLAZGO MAYOR: traccion vertical SIN suspender el peso corporal. "
           "Hasta ahora las nueve entradas de vertical_pull eran dominadas — "
           "todas con grip hanging_bodyweight, todas contraindicadas para "
           "agarre limitado, muneca y tunel carpiano. Esta pide agarre ligero: "
           "diff 1, 17 en safe_for, apta para muneca y hernia discal. Es el "
           "piso de accesibilidad del patron vertical_pull y la sustitucion "
           "obligada de toda la familia de dominadas."),
]

CONFIDENCE_OVERRIDES = {
    "0365": 0.65,  # texto contradictorio: apoyo de antebrazo vs curl al hombro
    "0366": 0.65,  # idem 0365
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
    print(f"lote 26: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
