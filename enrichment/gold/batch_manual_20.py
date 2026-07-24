#!/usr/bin/env python3
"""Lote 20 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("2189", "dumbbells seated triceps extension", "seated", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="low", wr="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "cervical_injury", "neck_pain", "hypertension",
            "hypermobility", "osteoporosis", "dysautonomia", "lumbar_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="DUPLICADO exacto de 2188 (lote 18) salvo el plural del nombre y el "
           "agarre pronado explicito. Clasificacion identica a proposito: si dos "
           "entradas describen el mismo movimiento, deben filtrar igual. E4 "
           "debe colapsarlas."),

    E("0507", "jackknife sit-up", "supine", floor=True, oh=True, grip="none",
      flex="high", stress=js(lumbar="high", hip="high", cerv="moderate"),
      pat="core_flexion", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="none",
      temp="low",
      contra=["lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "postpartum", "cannot_get_on_floor",
              "cannot_lie_supine", "no_overhead", "shoulder_impingement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cervical_injury", "neck_pain", "hypertension", "obesity",
            "elderly_65plus", "hip_pain", "hypermobility", "chronic_fatigue"],
      safe=["cannot_stand", "limited_balance", "limited_grip", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="El V-up es la version mas agresiva de la familia de flexion: sube "
           "torso Y piernas a la vez, o sea maximo brazo de palanca en los dos "
           "extremos. Peor que 0832 y 0992. no_overhead a contra porque los "
           "brazos arrancan extendidos por encima de la cabeza."),

    E("1331", "dumbbell reverse grip incline bench two arm row", "bench_prone",
      grip="firm", stress=js(sh="moderate", el="moderate", wr="moderate",
                             lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", valsalva="low", metab="moderate",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "tendinitis_elbow", "shoulder_pain",
            "hypertension"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "lumbar_pain",
            "no_overhead", "sciatica", "dysautonomia", "plantar_fasciitis",
            "osteoporosis"],
      why="CORRECCION A E1, segunda vez con la misma frase: 'chest against the "
           "backrest'. Es bench_prone, no bench_incline. Version con mancuernas "
           "de 1317 (lote 18) y misma conclusion — el pecho apoyado saca la "
           "columna de la ecuacion: lumbar_disc y sciatica en safe_for."),

    E("1680", "dumbbell standing one arm curl over incline bench", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="moderate", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "elbow_injury"],
      caut=["tendinitis_elbow", "limited_balance", "dysautonomia",
            "hypertension", "wrist_injury", "elderly_65plus", "lumbar_pain",
            "chronic_fatigue"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "one_arm_only", "knee_pain", "lumbar_disc", "ankle_injury",
            "plantar_fasciitis"],
      why="CORRECCION A E1: dijo bench_incline pero el texto empieza con 'stand "
           "with your feet shoulder-width apart' — el banco es solo apoyo para "
           "la mano libre. Es standing. Mismo error de E1 que 1330 del lote 19: "
           "ve la palabra 'bench' en el nombre y asume postura de banco."),

    E("0060", "barbell lying triceps extension skull crusher", "bench_supine",
      grip="firm", stress=js(el="high", wr="moderate", sh="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypertension", "hypermobility", "osteoporosis", "no_overhead"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis"],
      why="El rompecraneos canonico, agarre pronado. Referencia de la familia: "
           "0056 (supinado) sube la muneca a high, 0035 (declinado) agrega "
           "head_below_heart, 0337 (across face) agrega no_overhead a contra. "
           "Este es la linea base contra la que se comparan todos."),

    E("0345", "dumbbell lying one arm rear lateral raise", "bench_prone",
      grip="firm", lat="unilateral",
      stress=js(sh="high", cerv="moderate", el="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "shoulder_impingement", "rotator_cuff",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cervical_injury", "neck_pain", "hypermobility", "shoulder_pain",
            "elbow_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "lumbar_pain",
            "no_overhead", "sciatica", "one_arm_only", "dysautonomia",
            "plantar_fasciitis", "wrist_injury"],
      why="Sexta entrada de la familia de deltoides posterior en prono. La "
           "version en banco de 2470 (lote 19): mismo perfil, 14 en safe_for, "
           "pero agrega cannot_transfer_to_bench como filtro. Para quien puede "
           "bajar al suelo, 2470 domina a esta."),

    E("0475", "hanging straight leg raise", "hanging", oh=True,
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
      why="Piernas RECTAS: brazo de palanca maximo sobre la lumbar, muy por "
           "encima de 1764 (rodillas flexionadas). diff 5. Confirma la regla "
           "del lote 12: flexionar la articulacion intermedia es una regresion. "
           "Cadena completa: 0475 → 1764 → 1761 segun que tolere la persona."),

    E("1258", "barbell wide reverse grip bench press", "bench_supine",
      grip="firm", stress=js(wr="high", sh="moderate", el="moderate"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="none", change="low", valsalva="high", metab="moderate",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip", "elbow_injury",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "hypertension", "cardiac",
            "tendinitis_elbow", "hypermobility", "glaucoma", "osteoporosis",
            "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis"],
      why="El texto se contradice solo: 'wide reverse grip' pero 'keeping your "
           "elbows tucked in'. Con agarre ancho los codos se abren por "
           "mecanica. Resuelto por sesgo conservador: hombro en moderate, no "
           "low como en 2187 (cerrado). Tercera variante de press invertido "
           "del proyecto — el ancho del agarre es el eje que las separa."),

    E("1306", "plyo push up", "plank", floor=True, grip="none", impact="high",
      stress=js(wr="high", sh="high", el="high", lumbar="moderate"),
      pat="horizontal_push", diff=5, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="low",
      metab="high", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "elbow_injury",
              "tendinitis_elbow", "shoulder_impingement", "rotator_cuff",
              "cannot_get_on_floor", "cannot_lie_prone", "osteoporosis",
              "osteoarthritis", "rheumatoid_arthritis", "hypermobility",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "postpartum",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "obesity", "elderly_65plus",
            "chronic_fatigue", "fibromyalgia", "multiple_sclerosis",
            "lumbar_pain", "varicose_veins", "asthma"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "hip_replacement",
            "knee_injury", "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Unico impact high del lote. El aterrizaje sobre las manos convierte "
           "toda la familia de muneca y codo en contraindicacion dura, y suma "
           "osteoporosis y artritis por el impacto repetido. Curiosidad util: "
           "sigue siendo apto para rodilla y tobillo, porque el impacto es "
           "todo de miembro superior."),

    E("2300", "inverted row bent knees", "supine", floor=True, grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "limited_grip",
              "elbow_injury", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "tendinitis_elbow", "obesity", "elderly_65plus",
            "hypertension", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "dysautonomia",
            "osteoporosis"],
      why="Gemelo de 2298 (lote 19) con barra en vez de banco. El nombre dice "
           "'bent knees' pero el texto dice 'your body is straight': la version "
           "con rodillas flexionadas seria mas facil. Clasificado por el texto, "
           "mismo perfil que 2298. Refuerza el piso de accesibilidad del patron "
           "horizontal_pull."),

    E("2571", "rocking frog stretch", "quadruped", floor=True, grip="none",
      ext="low", stress=js(knee="high", hip="high", wr="moderate", sh="low",
                           ank="moderate"),
      pat="mobility_stretch", diff=2, rom="high",
      ortho="none", change="moderate", valsalva="none", iso="low", metab="low",
      laxity="high", pelvic="moderate", gripdur="none", temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_injury",
              "knee_replacement", "hip_replacement", "wrist_injury",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "hip_pain", "si_joint_pain", "osteoarthritis",
            "hypermobility", "carpal_tunnel", "ankle_injury",
            "plantar_fasciitis", "obesity", "elderly_65plus", "lumbar_pain"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "dysautonomia", "cervical_injury"],
      why="El texto mezcla arrodillado y plancha de forma incoherente; "
           "clasificado como quadruped, que es lo que sostiene el peso en la "
           "posicion descripta. Abduccion de cadera en rango final con la "
           "rodilla apoyada: knee y hip high, laxity high. hip_replacement a "
           "contra — la abduccion forzada es precaucion post-artroplastia."),

    E("3010", "ez bar lying bent arms pullover", "bench_supine", oh=True,
      grip="firm", stress=js(sh="high", el="moderate", lumbar="moderate",
                             wr="low"),
      pat="vertical_pull", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "hypermobility", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_pain", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "hypertension", "osteoporosis", "cervical_injury",
            "hernia_abdominal"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia",
            "plantar_fasciitis", "wrist_injury"],
      why="El pullover lleva el hombro a flexion maxima con carga y el brazo de "
           "palanca mas largo del catalogo: laxity high. Ademas la barra detras "
           "de la cabeza tiende a arquear la lumbar contra el banco — por eso "
           "lumbar_disc queda en cautions y no en safe_for, a diferencia del "
           "resto de los ejercicios en banco supino."),

    E("3012", "scapula dips", "standing", standing=True, bal="low",
      grip="none", flex="low",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=2, rom="low",
      ortho="high", change="low", valsalva="low", iso="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "shoulder_impingement",
              "rotator_cuff"],
      caut=["shoulder_pain", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "limited_balance", "lumbar_pain", "dysautonomia", "hypertension",
            "elderly_65plus", "hypermobility"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "limited_grip", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis"],
      why="El texto no describe un dip escapular real (que se hace suspendido "
           "en paralelas): describe una bisagra de pie con empuje de brazos. "
           "Clasificado por el texto, confianza 0.55. Es la cuarta entrada de "
           "calistenia avanzada del dataset con descripcion inventada."),

    E("3211", "kneeling push-up (male)", "plank", floor=True, grip="none",
      stress=js(wr="high", sh="moderate", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "elbow_injury",
            "lumbar_pain", "lumbar_disc", "obesity", "elderly_65plus",
            "hernia_abdominal", "pelvic_floor_dysfunction", "postpartum",
            "plantar_fasciitis", "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury"],
      why="PROBLEMA IMPORTANTE: el nombre dice 'kneeling push-up', que es LA "
           "regresion accesible del push-up, pero el texto dice 'extend your "
           "legs behind you, resting on the balls of your feet' — o sea una "
           "flexion completa. Mandan las instrucciones, confianza 0.55, pero "
           "esto merece revision humana prioritaria en E3: si el nombre es "
           "correcto, el catalogo esta perdiendo una regresion valiosa para "
           "principiantes y personas con poca fuerza de tren superior."),

    E("3291", "stalder press", "standing", standing=True, floor=False,
      bal="moderate", oh=True, grip="none",
      stress=js(knee="moderate", hip="moderate", sh="moderate", ank="low",
                lumbar="low"),
      pat="squat", diff=3, rom="high",
      ortho="high", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "knee_replacement", "knee_injury",
              "hip_replacement"],
      caut=["knee_pain", "hip_pain", "rotator_cuff", "limited_balance",
            "ankle_injury", "plantar_fasciitis", "dysautonomia", "hypertension",
            "obesity", "elderly_65plus", "osteoarthritis", "lumbar_pain",
            "pelvic_floor_dysfunction", "pregnancy_3rd"],
      safe=["limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench"],
      why="Un stalder press real es una habilidad de gimnasia en el suelo, con "
           "las manos apoyadas. El texto describe una sentadilla con brazos "
           "sobre la cabeza. Clasificado por el texto, confianza 0.50 — la mas "
           "baja del proyecto. Quinta entrada de calistenia con descripcion "
           "generica."),

    E("3315", "full maltese", "standing", standing=True, bal="moderate",
      grip="none", flex="moderate",
      stress=js(lumbar="high", hip="moderate", sh="moderate", knee="low"),
      pat="hinge", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["cannot_stand", "wheelchair", "lumbar_disc", "sciatica",
              "osteoporosis", "shoulder_impingement",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hip_pain", "limited_balance",
            "rotator_cuff", "dysautonomia", "hypertension", "vertigo",
            "obesity", "elderly_65plus", "chronic_fatigue"],
      safe=["limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "knee_injury", "knee_pain"],
      why="Un maltese real es un sostenimiento en anillas. El texto describe una "
           "bisagra de pie con brazos en cruz, tipo 'buenos dias' isometrico. "
           "Clasificado por el texto, confianza 0.50. El torso en voladizo con "
           "brazos abiertos carga la lumbar sin ninguna asistencia: lumbar high "
           "e iso high, por eso lumbar_disc a contra."),

    E("3638", "push to run", "plank", floor=True, grip="none", bal="low",
      impact="moderate", flex="moderate", lat="alternating",
      stress=js(wr="high", sh="moderate", hip="moderate", lumbar="moderate",
                knee="low", el="moderate"),
      pat="cardio_interval", diff=4, rom="moderate",
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
            "pelvic_floor_dysfunction", "postpartum"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "hip_replacement", "ankle_injury", "plantar_fasciitis"],
      why="Flexion + escaladores en continuo: unico temperature_load high del "
           "lote. Eso arrastra esclerosis multiple (fenomeno de Uhthoff) y "
           "disautonomia a cautions por calor, no por carga articular. metab "
           "high hace lo propio con EM/SFC. Es el caso donde los campos "
           "fisiologicos de v1.2 hacen todo el trabajo."),

    E("3665", "power point plank", "plank", floor=True, grip="none",
      lat="alternating",
      stress=js(wr="high", sh="moderate", el="high", lumbar="moderate"),
      pat="core_antiextension", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "elbow_injury",
              "cannot_get_on_floor", "cannot_lie_prone",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "tendinitis_elbow",
            "lumbar_pain", "lumbar_disc", "obesity", "elderly_65plus",
            "hernia_abdominal", "pelvic_floor_dysfunction", "postpartum",
            "osteoarthritis", "rheumatoid_arthritis", "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "limited_grip", "knee_injury",
            "knee_pain", "hip_replacement", "ankle_injury",
            "plantar_fasciitis"],
      why="Plancha con transicion mano-antebrazo alternada. El codo apoyado "
           "recibe el peso corporal de golpe en cada bajada: el a high, mas "
           "alto que en la plancha estatica. iso high por el sosten continuo. "
           "limited_grip en safe_for: nunca se agarra nada."),
]

# La taxonomia pide confidence < 0.7 cuando el texto fuente es ambiguo.
CONFIDENCE_OVERRIDES = {
    "3211": 0.55,  # el nombre dice de rodillas, el texto describe flexion completa
    "3012": 0.55,  # el texto no describe un dip escapular
    "3291": 0.50,  # el texto no describe un stalder press
    "3315": 0.50,  # el texto no describe un maltese
    "2571": 0.65,  # el texto mezcla arrodillado y plancha
    "1258": 0.70,  # el texto se contradice sobre la posicion del codo
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
    print(f"lote 20: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
