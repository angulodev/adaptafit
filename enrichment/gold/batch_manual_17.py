#!/usr/bin/env python3
"""Lote 17 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0393", "dumbbell seated inner biceps curl", "seated", grip="firm",
      flex="low", stress=js(el="moderate", sh="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "wrist_injury", "lumbar_pain", "dysautonomia",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis"],
      why="Banco sin respaldo con antebrazos sobre los muslos: ortho moderate, "
           "no low. El torso inclinado sobre las piernas es flexion lumbar "
           "sentada — saco lumbar_disc de safe_for y lo dejo en cautions."),

    E("0330", "dumbbell incline triceps extension", "bench_incline", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="low", wr="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench"],
      caut=["tendinitis_elbow", "cervical_injury", "hypertension",
            "hypermobility", "osteoporosis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia",
            "plantar_fasciitis"],
      why="Extension sobre la cabeza en banco inclinado: el respaldo baja el "
           "ortho a low pero la posicion overhead con flexion de hombro a rango "
           "final es contraindicacion dura de hombro. laxity moderate por el "
           "rango final."),

    E("1624", "dumbbell reverse bench press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "cannot_lie_supine",
              "cannot_transfer_to_bench", "limited_grip", "wrist_injury",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "hypertension", "hypermobility", "carpal_tunnel",
            "shoulder_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia"],
      why="El texto dice 'elbows flare out to the sides': ese codo abierto es "
           "justo el arco de pinzamiento. Contraindicacion de hombro pese a ser "
           "un press acostado. La muneca en pronacion carga bajo peso: "
           "wrist_injury a contra, carpal_tunnel a cautions."),

    E("1411", "barbell palms down wrist curl over a bench", "seated",
      grip="firm", flex="low",
      stress=js(wr="high", el="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "tendinitis_elbow", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "elbow_injury",
            "lumbar_pain", "dysautonomia"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis"],
      why="Palmas abajo = curl inverso: extensores de muneca, el tendon que "
           "duele en epicondilitis. gripdur high porque la barra se sostiene "
           "toda la serie — es el caso de manual que separa grip_required de "
           "grip_duration."),

    E("3561", "glute bridge march", "supine", floor=True, bal="low",
      grip="none", ext="moderate", lat="alternating",
      stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="hinge", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "hip_replacement",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "sciatica",
            "postpartum", "pelvic_floor_dysfunction", "hernia_abdominal",
            "knee_pain"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "carpal_tunnel", "ankle_injury", "dysautonomia"],
      why="El puente solo seria apto para protesis de cadera, pero la marcha "
           "lleva la rodilla al pecho: flexion de cadera >90, viola la "
           "precaucion posterior. hip_replacement a contra. iso moderate: el "
           "puente se sostiene durante toda la serie."),

    E("0030", "barbell close-grip bench press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="high", metab="moderate",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "one_arm_only", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "cardiac", "carpal_tunnel",
            "hernia_abdominal", "glaucoma", "retinal_detachment_risk",
            "osteoporosis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis"],
      why="Barra pesada con desenganche: valsalva high, el unico del lote junto "
           "al handstand. Eso arrastra glaucoma y desprendimiento de retina a "
           "cautions aunque la cabeza nunca baje del corazon — el pico de "
           "presion intraocular viene de la apnea, no de la inversion. "
           "one_arm_only a contra: la barra no se desengancha con un brazo."),

    E("0688", "scapular pull-up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, impact="low",
      stress=js(sh="high", el="moderate", wr="moderate", cerv="low"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="low",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "cannot_stand", "one_arm_only"],
      caut=["hypermobility", "osteoporosis", "cervical_injury", "obesity",
            "rheumatoid_arthritis", "elderly_65plus", "tendinitis_elbow",
            "shoulder_pain"],
      safe=["cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_get_on_floor", "cannot_transfer_to_bench"],
      why="CONFLICTO NOMBRE vs TEXTO: un scapular pull-up real es solo "
           "retraccion escapular sin flexion de codo, pero el texto describe "
           "una dominada completa. Regla de la taxonomia: mandan las "
           "instrucciones. Clasificado como vertical_pull. Confianza bajada a "
           "0.60. laxity high: la suspension muerta distrae el hombro, lo peor "
           "para hipermovilidad."),

    E("0558", "kipping muscle up", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, bal="moderate",
      impact="moderate", ext="high", flex="moderate",
      stress=js(sh="high", el="high", wr="high", lumbar="high",
                cerv="moderate"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="low",
      metab="high", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "shoulder_pain", "elbow_injury",
              "tendinitis_elbow", "wrist_injury", "carpal_tunnel",
              "lumbar_disc", "lumbar_pain", "cervical_injury", "neck_pain",
              "sciatica", "cannot_stand", "one_arm_only", "limited_balance",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "osteoporosis", "hypertension", "cardiac",
            "obesity", "elderly_65plus", "chronic_fatigue", "fibromyalgia",
            "multiple_sclerosis", "hernia_abdominal", "epilepsy"],
      safe=[],
      why="safe_for VACIO a proposito. Es el ejercicio mas agresivo del lote: "
           "balistico, latigazo lumbar en el kip, transicion de traccion a fondo "
           "en el punto mas debil del hombro. La regla dice dejar el array vacio "
           "ante duda, y aca no hay un solo perfil adaptado al que se lo "
           "ofreceria. Embarazo a contra por riesgo de caida, no por carga."),

    E("1423", "reverse hyper on flat bench", "bench_prone", grip="light",
      ext="high",
      stress=js(lumbar="high", hip="moderate", cerv="moderate", knee="low"),
      pat="hinge", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "lumbar_disc",
              "sciatica", "si_joint_pain", "hernia_abdominal",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "cervical_injury", "neck_pain",
            "hip_pain", "hypertension", "obesity", "pelvic_floor_dysfunction",
            "postpartum"],
      safe=["cannot_stand", "no_overhead", "knee_injury", "knee_pain",
            "ankle_injury", "plantar_fasciitis", "dysautonomia"],
      why="El reverse hyper de maquina se usa en rehabilitacion lumbar; sobre "
           "un banco plano, sin contrapeso y con las piernas rectas como "
           "palanca, no es lo mismo. Sesgo conservador: lumbar_disc a contra. "
           "Cuello en cautions porque el prono obliga a rotar o extender la "
           "cervical toda la serie."),

    E("2186", "ez barbell decline triceps extension", "bench_supine",
      grip="firm", stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "hernia_abdominal", "pregnancy_1st",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypertension", "dysautonomia", "vertigo", "migraine", "cardiac"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis"],
      why="Banco declinado con pies asegurados: head_below_heart true. Sexto o "
           "septimo caso del lote de rompecraneos, pero el declinado le suma "
           "toda la familia ocular y vestibular que el plano no tiene."),

    E("2706", "dumbbell lying supination on floor", "supine", floor=True,
      grip="firm", stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=1, rom="low",
      ortho="none", change="low", valsalva="none", metab="low", laxity="low",
      gripdur="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "limited_grip",
              "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "dysautonomia", "cannot_transfer_to_bench", "plantar_fasciitis",
            "cannot_kneel", "osteoporosis"],
      why="JOYA DE ACCESIBILIDAD. diff 1, valsalva none, ortho none, sin "
           "columna cargada. El unico filtro real es llegar al suelo. Para un "
           "perfil que no puede pararse pero si tumbarse, este entra casi "
           "siempre — safe_for de 13 condiciones, el mas largo del lote."),

    E("3300", "lean planche", "plank", floor=True, grip="none",
      stress=js(wr="high", sh="high", el="moderate", lumbar="moderate"),
      pat="core_antiextension", diff=4, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement", "rotator_cuff",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "hypertension", "cardiac", "pelvic_floor_dysfunction",
            "postpartum", "obesity", "elderly_65plus", "chronic_fatigue",
            "plantar_fasciitis"],
      safe=["cannot_stand", "no_overhead", "knee_injury", "knee_pain",
            "hip_replacement", "limited_grip"],
      why="iso high — el unico del lote. Llevar el hombro por delante de la "
           "mano lleva la muneca a extension extrema bajo casi todo el peso "
           "corporal: wrist_injury y tunel carpiano a contra sin discusion. "
           "plantar_fasciitis a cautions porque el antepie sostiene la plancha."),

    E("0376", "dumbbell raise", "standing", standing=True, bal="low",
      grip="firm", stress=js(sh="high", el="low", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "shoulder_impingement", "rotator_cuff",
              "shoulder_pain", "limited_grip", "wheelchair"],
      caut=["dysautonomia", "hypertension", "neck_pain", "cervical_injury",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "elbow_injury"],
      safe=["no_overhead", "lumbar_disc", "cannot_get_on_floor",
            "cannot_kneel", "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_pain"],
      why="Elevacion lateral: de pie con brazos elevados = ortho high por "
           "definicion, disparador clasico de POTS. Sube solo a paralelo, asi "
           "que no_overhead queda en safe_for — pero el arco de 60-120 grados "
           "es exactamente donde pinza el supraespinoso: hombro a contra. "
           "Valioso para quien no puede bajar al suelo."),

    E("0408", "dumbbell side lying one hand raise", "side_lying", floor=True,
      grip="firm", lat="unilateral",
      stress=js(sh="high", cerv="moderate", el="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["cannot_lie_on_side", "cannot_get_on_floor", "limited_grip",
              "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "neck_pain", "hypermobility", "shoulder_pain",
            "elbow_injury", "si_joint_pain", "hip_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "no_overhead", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis"],
      why="CORRECCION A E1: E1 puso 'supine' pero el texto dice literalmente "
           "'lie on your side'. Es side_lying. Primer side_lying del lote y de "
           "los pocos del dataset. La cabeza apoyada sobre el brazo toda la "
           "serie carga la cervical: cerv moderate."),

    E("0448", "ez barbell decline close grip face press", "bench_supine",
      grip="firm", stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "hernia_abdominal", "pregnancy_1st",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypertension", "dysautonomia", "vertigo", "migraine", "cardiac",
            "limited_balance"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "plantar_fasciitis"],
      why="Gemelo de 2186 con agarre neutro y sin 'feet secured' en el texto. "
           "Esa omision es la unica diferencia real: sin pies asegurados en "
           "declinado hay riesgo de deslizamiento, por eso limited_balance "
           "aparece en cautions y sale de safe_for, al reves que en 2186."),

    E("0471", "handstand push-up", "standing", floor=True, standing=True,
      bal="high", oh=True, grip="none", impact="moderate",
      stress=js(sh="high", wr="high", cerv="high", el="high", lumbar="moderate"),
      pat="vertical_push", diff=5, rom="high",
      ortho="none", change="high", headdown=True, valsalva="high",
      iso="moderate", metab="high", laxity="high", pelvic="moderate",
      gripdur="none", temp="moderate",
      contra=["cannot_stand", "cannot_get_on_floor", "limited_balance",
              "no_overhead", "shoulder_impingement", "rotator_cuff",
              "wrist_injury", "carpal_tunnel", "cervical_injury", "neck_pain",
              "elbow_injury", "glaucoma", "retinal_detachment_risk", "vertigo",
              "visual_impairment", "epilepsy", "wheelchair",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "osteoporosis", "dysautonomia",
            "migraine", "multiple_sclerosis", "obesity", "elderly_65plus",
            "hypermobility", "hernia_abdominal"],
      safe=[],
      why="Inversion completa con carga: position_change high, headdown true, "
           "valsalva high, cervical high. Segundo safe_for vacio del lote. "
           "Ojo con start_position: la taxonomia no tiene enum 'invertido', y "
           "el texto arranca de pie, asi que queda 'standing' con floor=true — "
           "es una limitacion del enum, no una clasificacion floja. "
           "Candidato a atributo nuevo en v1.3."),

    E("0659", "push-up (wall)", "standing", standing=True, bal="low",
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
      why="LA JOYA DEL LOTE. Empuje horizontal con solo dos contraindicaciones "
           "en las 62 condiciones. safe_for de 15, el mas largo hasta ahora. "
           "Es el ejercicio que el motor deberia proponer cuando la degradacion "
           "vacia el catalogo de pecho: quien no puede bajar al suelo ni "
           "transferirse a un banco todavia puede empujar una pared."),

    E("0696", "self assisted inverse leg curl (on floor)", "supine",
      floor=True, grip="none", ext="moderate",
      stress=js(knee="moderate", hip="moderate", lumbar="moderate"),
      pat="hinge", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "knee_injury",
              "knee_replacement", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "sciatica",
            "hip_pain", "hip_replacement", "postpartum",
            "pelvic_floor_dysfunction", "hernia_abdominal", "knee_pain",
            "fibromyalgia"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "carpal_tunnel", "dysautonomia"],
      why="El texto esta anatomicamente confundido: describe un puente y llama "
           "'curl' a deslizar los pies. Clasificado por lo que se ejecuta, no "
           "por el nombre. Flexion de rodilla cargada bajo el puente: "
           "knee_injury a contra. fibromyalgia en cautions por calambre de "
           "isquiotibial, que es el modo de fallo real de este ejercicio."),
]

# Confianza real por ejercicio cuando el texto fuente es ambiguo (regla de la
# taxonomia: usar < 0.7 cuando hay ambiguedad).
CONFIDENCE_OVERRIDES = {
    "0688": 0.60,  # nombre y descripcion describen ejercicios distintos
    "0696": 0.70,  # descripcion anatomicamente incoherente
    "0471": 0.75,  # start_position sin enum adecuado para inversiones
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
    print(f"lote 17: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
