#!/usr/bin/env python3
"""Lote 22 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1669", "dumbbell one arm seated hammer curl", "seated", grip="firm",
      flex="low", lat="unilateral",
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
      why="Curl de concentracion: el codo apoyado en el muslo elimina toda "
           "compensacion de hombro y tronco. diff 1. Apoyar el codo obliga a "
           "inclinarse hacia adelante, pero sin carga espinal — lumbar_disc "
           "queda en safe_for, a diferencia de 0393 donde los dos antebrazos "
           "sobre los muslos flexionan mas el tronco."),

    E("0344", "dumbbell lying one arm pronated triceps extension",
      "bench_supine", oh=True, grip="firm", lat="unilateral",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="high",
      ortho="none", change="low", valsalva="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "no_overhead",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypermobility", "cervical_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "one_arm_only", "plantar_fasciitis"],
      why="Version unilateral del rompecraneos con pronacion. El texto aclara "
           "'back and head supported': el cuello no trabaja, por eso "
           "cervical_injury queda en cautions y no sube. La mancuerna baja "
           "detras de la cabeza, asi que no_overhead sigue siendo contra."),

    E("3640", "knee touch crunch", "supine", floor=True, grip="none",
      flex="high", rot="moderate", lat="alternating",
      stress=js(lumbar="high", cerv="high", hip="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="moderate", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "cervical_injury", "neck_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "pelvic_floor_dysfunction",
            "postpartum", "obesity", "elderly_65plus", "migraine"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "hip_replacement",
            "wrist_injury", "carpal_tunnel", "plantar_fasciitis",
            "dysautonomia"],
      why="Crunch con rotacion Y manos detras de la cabeza: cerv high, porque "
           "la gente se tracciona el cuello con las manos. cervical_injury y "
           "neck_pain a contra — es el primer core del proyecto donde el cuello "
           "pesa tanto como la lumbar."),

    E("0037", "barbell decline wide-grip pullover", "bench_supine", oh=True,
      grip="firm", ext="moderate",
      stress=js(sh="high", el="moderate", lumbar="moderate", wr="moderate"),
      pat="isolation", diff=4, rom="high",
      ortho="none", change="moderate", headdown=True, valsalva="high",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "no_overhead", "hypermobility", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "hernia_abdominal", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "lumbar_disc", "elbow_injury", "hypertension",
            "cardiac", "dysautonomia", "vertigo", "migraine", "elderly_65plus",
            "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="El peor caso de hombro del lote: flexion completa sobre la cabeza "
           "con barra ancha, brazos rectos y a rango final, en declinado. "
           "laxity high, valsalva high y head_below_heart al mismo tiempo. "
           "Los brazos rectos maximizan el brazo de palanca sobre la lumbar, "
           "que se arquea para compensar."),

    E("0258", "clock push-up", "plank", floor=True, bal="moderate",
      grip="none", rot="high", lat="alternating",
      stress=js(wr="high", sh="high", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "cannot_get_on_floor", "cannot_lie_prone",
              "lumbar_disc", "sciatica", "hypermobility", "one_arm_only",
              "recent_abdominal_surgery",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "lumbar_pain", "si_joint_pain", "shoulder_pain",
            "obesity", "elderly_65plus", "hernia_abdominal", "limited_balance",
            "chronic_fatigue"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis"],
      why="Flexion que rota el cuerpo y extiende un brazo al costado: en el "
           "momento de la rotacion todo el peso queda sobre una muneca y un "
           "hombro. rot high con carga corporal — lumbar_disc a contra. "
           "one_arm_only a contra: el ejercicio ES el brazo que se extiende."),

    E("3318", "swing 360", "standing", standing=True, bal="moderate",
      grip="none", rot="moderate",
      stress=js(lumbar="moderate", sh="moderate", cerv="low"),
      pat="cardio_steady", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="moderate",
      laxity="moderate", pelvic="low", gripdur="none", temp="moderate",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "shoulder_impingement", "vertigo"],
      caut=["lumbar_pain", "si_joint_pain", "limited_balance", "rotator_cuff",
            "dysautonomia", "hypertension", "migraine", "elderly_65plus",
            "multiple_sclerosis", "chronic_fatigue", "osteoporosis"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis", "hip_replacement"],
      why="Cardio sin impacto ni equipamiento, apto para rodilla y tobillo — "
           "raro y valioso. Pero rota el tronco de pie y sin apoyo: "
           "lumbar_disc a contra. vertigo tambien, porque el giro repetido del "
           "torso con la cabeza siguiendo el movimiento es un disparador "
           "vestibular directo."),

    E("0407", "dumbbell side bend", "standing", standing=True, bal="low",
      grip="firm", flex="moderate", rot="low", lat="unilateral",
      stress=js(lumbar="high", hip="low", sh="low", wr="low"),
      pat="core_rotation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="moderate", iso="low", metab="low",
      laxity="moderate", pelvic="moderate", gripdur="high", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "cannot_stand", "wheelchair", "limited_grip", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "shoulder_impingement", "hypertension",
            "obesity", "elderly_65plus", "dysautonomia", "hypermobility",
            "pelvic_floor_dysfunction", "postpartum"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="LIMITACION DEL ENUM: esto es flexion LATERAL de columna, plano "
           "frontal, y la taxonomia solo tiene flexion sagital y rotacion "
           "transversal. Quedo como core_rotation (lo mas cercano, igual que "
           "E1) con spinal_flexion moderate, pero ninguno de los dos campos lo "
           "describe. Candidato firme para v1.3: agregar spinal_lateral_flexion."),

    E("0664", "push-up to side plank", "plank", floor=True, bal="high",
      grip="none", rot="high", lat="alternating",
      stress=js(wr="high", sh="high", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="high", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "shoulder_impingement",
              "rotator_cuff", "cannot_get_on_floor", "cannot_lie_prone",
              "cannot_lie_on_side", "limited_balance", "hypermobility",
              "one_arm_only", "recent_abdominal_surgery",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "elbow_injury",
            "shoulder_pain", "obesity", "elderly_65plus", "vertigo",
            "chronic_fatigue", "hernia_abdominal", "dysautonomia"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis"],
      why="Combina flexion, rotacion y plancha lateral: position_change high "
           "por el giro completo del cuerpo en cada repeticion. Suma tres "
           "requisitos de Capa A a la vez — prono, lateral y suelo — algo poco "
           "habitual. A diferencia de 0258, aca la lumbar queda en cautions: "
           "la rotacion pasa por la plancha lateral, que es espinal-neutra."),

    E("0678", "rocky pull-up pulldown", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True,
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
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
      why="CORRECCION A E1: E1 dijo standing porque el texto arranca 'stand in "
           "front of a pull-up bar'. El ejercicio se ejecuta colgado: "
           "start_position hanging, igual que se resolvio 0688 en el lote 17. "
           "El nombre promete una variante alterna que el texto no describe: "
           "es una dominada comun."),

    E("0778", "spider crawl push up", "plank", floor=True, bal="moderate",
      grip="none", flex="low", lat="alternating",
      stress=js(wr="high", sh="moderate", hip="high", lumbar="moderate",
                knee="low"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="high", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "hip_replacement", "hip_pain",
              "shoulder_impingement", "hypermobility", "si_joint_pain",
              "recent_abdominal_surgery",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "sciatica", "elbow_injury",
            "rotator_cuff", "obesity", "elderly_65plus", "chronic_fatigue",
            "fibromyalgia", "hernia_abdominal", "knee_pain"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "ankle_injury", "plantar_fasciitis"],
      why="La rodilla al codo lleva la cadera a flexion profunda CON abduccion "
           "y rotacion externa: hip high, y hip_replacement a contra por la "
           "misma logica que 3561. metab high — es el unico push-up del lote "
           "que es tambien acondicionamiento."),

    E("0970", "band assisted pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, bal="moderate",
      stress=js(sh="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=2, rom="high",
      ortho="moderate", change="high", valsalva="low", iso="low",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="high",
      temp="low",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "cannot_stand", "limited_balance",
              "wrist_injury", "one_arm_only"],
      caut=["carpal_tunnel", "elbow_injury", "tendinitis_elbow",
            "hypermobility", "elderly_65plus", "obesity", "vertigo",
            "rheumatoid_arthritis", "osteoporosis"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "lumbar_disc",
            "dysautonomia"],
      why="Regresion de la dominada: la banda baja diff de 4 a 2 y saca "
           "elbow_injury de contra. Pero AGREGA una restriccion que la "
           "dominada no tiene — hay que pararse sobre la banda y meter el pie "
           "en ella con el cuerpo colgando: limited_balance a contra y "
           "position_change high. Una regresion de fuerza puede ser una "
           "progresion de equilibrio."),

    E("0984", "band lying hip internal rotation", "supine", floor=True,
      grip="light", stress=js(hip="moderate", knee="low", lumbar="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="none", change="low", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="low", temp="low",
      contra=["hip_replacement", "cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_3rd"],
      caut=["hip_pain", "si_joint_pain", "lumbar_disc", "lumbar_pain",
            "sciatica", "hypermobility", "osteoarthritis", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "ankle_injury", "plantar_fasciitis", "dysautonomia",
            "osteoporosis"],
      why="CONFLICTO NOMBRE vs TEXTO: se llama 'internal rotation' pero el "
           "texto dice 'rotate your knees outwards' — es rotacion EXTERNA con "
           "abduccion. Mandan las instrucciones, confianza 0.65. Y esa "
           "diferencia decide: abduccion con rotacion externa y cadera "
           "flexionada es exactamente la posicion que luxa una protesis. "
           "hip_replacement a contra."),

    E("1403", "neck side stretch", "seated", grip="none", rot="low",
      lat="unilateral", stress=js(cerv="moderate"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="low", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="none", temp="low",
      contra=["cervical_injury"],
      caut=["neck_pain", "hypermobility", "vertigo", "migraine",
            "osteoarthritis", "rheumatoid_arthritis", "osteoporosis"],
      safe=["cannot_stand", "wheelchair", "limited_balance", "limited_grip",
            "cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "one_arm_only", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "sciatica", "plantar_fasciitis", "dysautonomia",
            "hernia_abdominal", "pregnancy_1st", "pregnancy_2nd",
            "pregnancy_3rd"],
      why="NUEVO MAXIMO ABSOLUTO: 28 en safe_for y una sola contraindicacion. "
           "El texto dice 'stand OR sit', asi que requires_standing es false y "
           "quedo como seated para que llegue a usuarios de silla de ruedas — "
           "es el primer ejercicio del proyecto con wheelchair en safe_for "
           "junto con embarazo completo. Es literalmente inclinar la cabeza."),

    E("1405", "back pec stretch", "standing", standing=True, bal="low",
      grip="none", stress=js(sh="moderate", cerv="low", el="low"),
      pat="mobility_stretch", diff=1, rom="moderate",
      ortho="moderate", change="none", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement"],
      caut=["rotator_cuff", "shoulder_pain", "hypermobility", "elbow_injury",
            "cervical_injury", "dysautonomia", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
            "wrist_injury", "carpal_tunnel", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "sciatica",
            "plantar_fasciitis", "osteoporosis", "hernia_abdominal"],
      why="Estiramiento de pie, 17 en safe_for. El unico filtro real ademas de "
           "pararse es el hombro: cruzar los brazos y elevarlos es aduccion "
           "horizontal, la maniobra que se usa para PROVOCAR el pinzamiento en "
           "el examen clinico. Por eso shoulder_impingement a contra pese a ser "
           "un estiramiento suave."),

    E("1409", "barbell glute bridge", "supine", floor=True, grip="firm",
      ext="moderate", axial="low",
      stress=js(hip="moderate", lumbar="moderate", knee="low", wr="low"),
      pat="hinge", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="high", iso="moderate",
      metab="moderate", laxity="low", pelvic="high", gripdur="moderate",
      temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "limited_grip", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "sciatica",
            "postpartum", "hypertension", "cardiac", "hip_replacement",
            "hip_pain", "obesity", "osteoporosis", "elderly_65plus",
            "knee_pain"],
      safe=["cannot_stand", "no_overhead", "shoulder_impingement",
            "rotator_cuff", "knee_injury", "ankle_injury", "plantar_fasciitis",
            "dysautonomia"],
      why="TERCERA entrada de la familia del puente (0668, 3561, 1409) y la "
           "unica cargada. La barra sobre la cadera dispara pelvic_floor_load "
           "a high y valsalva a high: hernia, suelo pelvico y embarazo pasan de "
           "no figurar en 0668 a contraindicacion aca. hip_replacement baja de "
           "safe_for a cautions solo por la carga, no por el movimiento."),

    E("1427", "straight leg outer hip abductor", "side_lying", floor=True,
      grip="none", lat="unilateral", sl=True,
      stress=js(hip="moderate", lumbar="low", knee="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_lie_on_side", "cannot_get_on_floor", "hip_replacement"],
      caut=["hip_pain", "si_joint_pain", "lumbar_pain", "osteoarthritis",
            "sciatica", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "no_overhead",
            "wrist_injury", "carpal_tunnel", "elbow_injury",
            "shoulder_impingement", "rotator_cuff", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis", "dysautonomia",
            "lumbar_disc", "osteoporosis", "one_arm_only"],
      why="Abduccion pura tumbado de lado, sin plancha: 17 en safe_for, y a "
           "diferencia de 1774 (lote 19) no hay que sostener el cuerpo — el "
           "hombro y la sacroiliaca salen del cuadro. Es la version accesible "
           "del mismo objetivo muscular. hip_replacement a contra igual: la "
           "abduccion resistida es precaucion estandar post-artroplastia."),

    E("1467", "push-up on lower arms", "plank", floor=True, grip="none",
      stress=js(el="high", sh="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["elbow_injury", "cannot_get_on_floor", "cannot_lie_prone",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["tendinitis_elbow", "shoulder_impingement", "rotator_cuff",
            "lumbar_pain", "lumbar_disc", "obesity", "elderly_65plus",
            "hernia_abdominal", "pelvic_floor_dysfunction", "postpartum",
            "osteoarthritis", "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "dysautonomia"],
      why="HALLAZGO: empuje horizontal SIN carga de muneca. Al apoyar en los "
           "antebrazos, wrist_injury y carpal_tunnel pasan de contraindicacion "
           "—que es lo habitual en toda la familia de flexiones— a safe_for. "
           "Es la sustitucion directa de cualquier push-up para quien tiene "
           "problemas de muneca. Todo el costo se traslada al codo, que pasa a "
           "high."),

    E("1512", "all fours squad stretch", "quadruped", floor=True, bal="low",
      grip="none", ext="low", lat="unilateral",
      stress=js(knee="high", wr="moderate", hip="moderate", lumbar="low",
                ank="moderate"),
      pat="mobility_stretch", diff=2, rom="high",
      ortho="none", change="moderate", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "wrist_injury", "carpal_tunnel",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "osteoarthritis", "hip_pain", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "lumbar_pain",
            "hypermobility", "rheumatoid_arthritis", "elderly_65plus"],
      safe=["cannot_stand", "no_overhead", "shoulder_impingement",
            "rotator_cuff", "lumbar_disc", "dysautonomia", "one_arm_only"],
      why="Cuadrupedia: la rotula soporta el peso contra el suelo Y la rodilla "
           "va a flexion maxima para estirar el cuadriceps. knee high, "
           "knee_injury a contra. Segunda cuadrupedia del proyecto. La muneca "
           "en extension bajo peso la saca tambien para tunel carpiano, algo "
           "que un 'estiramiento de cuadriceps' no sugiere."),
]

CONFIDENCE_OVERRIDES = {
    "0984": 0.65,  # el nombre dice rotacion interna, el texto describe externa
    "0678": 0.70,  # el nombre promete una variante que el texto no describe
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
    print(f"lote 22: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
