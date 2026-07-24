#!/usr/bin/env python3
"""Lote 16 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0398", "dumbbell seated one arm kickback", "seated", grip="firm",
      flex="moderate", lat="unilateral",
      stress=js(el="moderate", sh="moderate", lumbar="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", change="low", headdown=True, metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "glaucoma",
              "retinal_detachment_risk"],
      caut=["lumbar_disc", "shoulder_impingement", "hypertension",
            "dysautonomia", "tendinitis_elbow"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead"],
      why="DUPLICADO unilateral de 0394. Torso paralelo al suelo: quinto caso "
           "de head_below_heart en un ejercicio que nadie llamaria inversion."),

    E("1620", "dumbbell incline one arm hammer press on exercise ball",
      "bench_supine", bal="moderate", grip="firm", lat="unilateral",
      stress=js(sh="moderate", el="high", lumbar="moderate", cerv="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", gripdur="moderate", temp="low",
      contra=["limited_balance", "limited_grip", "vertigo", "cannot_lie_supine",
              "elbow_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility",
            "multiple_sclerosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead"],
      why="CORRECCION A E1: dice 'sit on an exercise ball' pero rueda hasta "
           "apoyar cabeza y espalda alta. Es bench_supine. Version unilateral "
           "de 1618 - undecimo caso del mismo error de E1."),

    E("1729", "dumbbell lying alternate extension", "bench_supine", grip="firm",
      lat="alternating", stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Sexta entrada del rompecraneos. Al alternar, el brazo extendido "
           "sostiene la mancuerna en isometrico: gripdur high."),

    E("0322", "dumbbell incline inner biceps curl", "bench_incline", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="CUARTA entrada del curl inclinado (0315/0317/0318/0322). "
           "Arranca neutro y termina supinado - diferencia mínima."),

    E("1276", "dumbbell decline one arm fly", "bench_supine", grip="firm",
      lat="unilateral", stress=js(sh="high", el="moderate", wr="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="moderate", headdown=True, valsalva="low",
      metab="low", laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "elbow_injury", "hypertension", "dysautonomia",
            "vertigo", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "no_overhead"],
      why="Apertura declinada unilateral. Completa el cuadro de aperturas: "
           "plano, inclinado, declinado x bilateral, unilateral, pelota."),

    E("0459", "flutter kicks", "supine", floor=True,
      flex="moderate", stress=js(hip="high", lumbar="high", cerv="none"),
      lat="alternating", pat="core_flexion", diff=2, rom="low",
      ortho="none", change="high", valsalva="low", iso="high",
      metab="moderate", pelvic="high", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "postpartum", "osteoporosis"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury", "cervical_injury"],
      why="Piernas rectas suspendidas de forma sostenida: el psoas tracciona "
           "la lumbar en isometrico continuo. iso high y lumbar high pese a "
           "rom_demand bajo. Brazos a los costados: apto con lesion cervical."),

    E("0634", "negative crunch", "supine", floor=True,
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Ultimo miembro del grupo de 10 abdominales con texto identico. "
           "El grupo queda completo y colapsa en un solo substitute_group."),

    E("1412", "barbell palms up wrist curl over a bench", "seated", grip="firm",
      stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="DUODECIMA entrada de la familia de muneca. Version con barra de "
           "0401, antebrazos en banco."),

    E("2432", "ez-bar close-grip bench press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Version EZ de 0055. Confirma la regla: la barra EZ baja la muneca "
           "de high a moderate frente a la barra recta con agarre cerrado. "
           "Progresion de muneca: mancuerna -> EZ -> barra recta."),

    E("2705", "dumbbell lying pronation on floor", "prone", floor=True,
      grip="firm", stress=js(wr="moderate", el="moderate", sh="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="high", metab="none", gripdur="moderate", temp="none",
      contra=["cannot_get_on_floor", "cannot_lie_prone", "wrist_injury",
              "carpal_tunnel", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["tendinitis_elbow", "rheumatoid_arthritis", "shoulder_impingement"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "chronic_fatigue"],
      why="CORRECCION A E1: lo marco supine pero dice 'face down'. Es prone. "
           "Version en suelo de 0347: pierde el safe_for cannot_get_on_floor "
           "que si tiene la version en banco. Buen par para E4."),

    E("3293", "archer pull up", "hanging", grip="hanging_bodyweight", oh=True,
      lat="alternating",
      stress=js(sh="high", el="high", wr="high", lumbar="low"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", valsalva="moderate", metab="moderate", laxity="high",
      gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "hypermobility"],
      caut=["hypertension", "obesity", "cardiac", "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement"],
      why="Sexta dominada. El brazo que queda extendido llega a abduccion "
           "casi completa bajo carga: laxity high e hipermovilidad como "
           "contraindicacion, a diferencia de la dominada estandar."),

    E("3299", "full planche", "plank", floor=True, bal="high", grip="none",
      ext="moderate",
      stress=js(sh="high", el="high", wr="high", lumbar="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="none", change="high", valsalva="high", iso="high",
      metab="high", laxity="high", pelvic="moderate", temp="moderate",
      gripdur="low",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_balance", "hypermobility", "hypertension", "cardiac",
              "osteoporosis", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "obesity", "chronic_fatigue"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement", "hip_replacement"],
      why="Progresion de frog planche (3301). Todo el peso sobre munecas en "
           "extension maxima con el cuerpo horizontal. 14 contraindicaciones "
           "duras, difficulty 5."),

    E("3304", "skin the cat", "hanging", grip="hanging_bodyweight",
      ext="high", flex="high",
      stress=js(sh="high", el="high", wr="high", lumbar="high", cerv="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="moderate", change="high", headdown=True, valsalva="high",
      iso="high", metab="moderate", laxity="high", pelvic="moderate",
      gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "cervical_injury", "lumbar_disc", "osteoporosis", "hypermobility",
              "glaucoma", "retinal_detachment_risk", "hypertension", "cardiac",
              "vertigo", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["dysautonomia", "migraine", "chronic_fatigue", "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement"],
      why="NUEVO MAXIMO: 19 contraindicaciones duras, supera a handstand (18). "
           "El cuerpo pasa invertido entre los brazos: rotacion de hombro en "
           "rango extremo mas inversion completa. Techo absoluto de riesgo "
           "del catalogo."),

    E("3433", "swimmer kicks", "prone", floor=True, oh=True,
      ext="high", stress=js(lumbar="high", sh="moderate", hip="moderate",
      cerv="moderate"),
      lat="alternating", pat="isolation", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="high",
      metab="moderate", pelvic="low", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_prone", "no_overhead",
              "osteoporosis", "shoulder_impingement",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "cervical_injury", "hypermobility",
            "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "limited_grip", "wrist_injury",
            "carpal_tunnel", "dysautonomia"],
      why="Superman con aleteo: extension lumbar sostenida con brazos "
           "overhead. iso high. Como sphinx y hyperextension, la extension "
           "es precaucion en disco pero contraindicacion en osteoporosis."),

    E("3637", "wheel run", "plank", floor=True, bal="moderate", oh=True,
      ext="high", stress=js(sh="high", lumbar="high", wr="high", el="moderate"),
      pat="core_antiextension", diff=4, rom="high",
      ortho="none", change="high", valsalva="moderate", iso="high",
      metab="high", laxity="moderate", pelvic="moderate", temp="high",
      gripdur="moderate",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "no_overhead", "shoulder_impingement", "rotator_cuff",
              "lumbar_disc", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cardiac", "hypertension", "obesity", "chronic_fatigue",
            "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Rueda abdominal con desplazamiento continuo: anti-extension "
           "sostenida mas demanda metabolica alta. Une el perfil del rollout "
           "(0084) con el de un ejercicio de cardio."),

    E("3639", "bent knee lying twist", "supine", floor=True,
      rot="high", stress=js(lumbar="moderate", hip="low", cerv="none"),
      lat="alternating", pat="core_rotation", diff=1, rom="moderate",
      ortho="none", change="high", valsalva="none", metab="none",
      laxity="moderate", pelvic="low", temp="none",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "sciatica", "hypermobility",
            "hip_replacement", "postpartum"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "dysautonomia", "chronic_fatigue", "fibromyalgia", "elderly_65plus",
            "hypertension", "osteoporosis"],
      why="Rotacion lumbar PASIVA con rodillas flexionadas y brazos a los "
           "costados: 17 safe_for y lumbar_disc como precaucion, frente a "
           "las diez rotaciones activas donde es contraindicacion dura. "
           "NOTA: con lumbar_disc en severidad 'lesion' el motor igual lo "
           "excluye por el umbral de joint_stress (lumbar=moderate). Solo "
           "sobrevive en severidad 'molestia'. El comportamiento es "
           "conservador y correcto: en hernia activa la rotacion se evita."),

    E("0300", "dumbbell deadlift", "standing", standing=True, grip="firm",
      axial="high", flex="moderate",
      stress=js(knee="moderate", hip="high", lumbar="high", sh="low", wr="low",
                ank="low"),
      pat="hinge", diff=3, rom="high",
      ortho="moderate", change="moderate", headdown=True, valsalva="high",
      metab="moderate", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "lumbar_disc", "sciatica", "limited_grip",
              "osteoporosis", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "glaucoma", "retinal_detachment_risk",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hypertension", "cardiac", "knee_injury",
            "hip_replacement", "elderly_65plus", "dysautonomia", "postpartum"],
      safe=["shoulder_impingement", "no_overhead", "cervical_injury"],
      why="Peso muerto con mancuernas: menos carga axial que con barra (0032) "
           "porque el peso queda a los costados en vez de adelante, pero sigue "
           "siendo axial high. valsalva high y pelvic_floor high."),

    E("0341", "dumbbell lying one arm deltoid rear", "bench_prone", grip="firm",
      lat="unilateral", stress=js(sh="moderate", el="low", cerv="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "hypermobility",
            "cervical_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Version unilateral de 0348/0326. La familia de deltoides posterior "
           "en prono llega a cinco entradas, todas aptas para hernia discal."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 16: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
