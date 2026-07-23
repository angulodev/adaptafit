#!/usr/bin/env python3
"""Lote 4 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1437", "dumbbell finger curls", "seated", grip="firm", lat="unilateral",
      stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["carpal_tunnel", "wrist_injury", "limited_grip",
              "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="Version unilateral con mancuerna del 0455. Mismo perfil: "
           "grip_duration high es el eje que lo descarta en tunel carpiano."),

    E("2567", "seated piriformis stretch", "seated", floor=True,
      rot="moderate", stress=js(hip="moderate", lumbar="low", knee="low"),
      lat="unilateral", pat="isolation", diff=1, rom="high",
      ortho="low", change="high", metab="none", laxity="moderate", temp="none",
      contra=["cannot_get_on_floor", "hip_replacement"],
      caut=["sciatica", "si_joint_pain", "hip_pain", "lumbar_disc",
            "hypermobility", "pregnancy_3rd"],
      safe=["cannot_stand", "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "dysautonomia", "chronic_fatigue", "hypertension",
            "elderly_65plus"],
      why="Estiramiento de piriforme: paradojico con ciatica. Alivia cuando el "
           "sindrome es piriforme, empeora cuando la causa es discal. "
           "Por eso ciatica es precaucion y no safe_for."),

    E("1468", "crab twist toe touch", "seated", floor=True, bal="moderate",
      grip="none", rot="high", ext="moderate",
      stress=js(sh="high", wr="high", lumbar="moderate", hip="moderate"),
      lat="alternating", pat="core_rotation", diff=3, rom="high",
      ortho="low", change="high", valsalva="low", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", temp="moderate",
      gripdur="low",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "shoulder_impingement", "limited_balance",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "hypermobility", "rotator_cuff",
            "postpartum", "elderly_65plus"],
      why="CORRECCION A E1: dice 'sitting on the ground' pero se levanta la "
           "cadera y se sostiene en manos y pies - posicion de cangrejo. "
           "La muneca en extension con el hombro en rotacion interna es la "
           "combinacion mas agresiva del lote."),

    E("0287", "dumbbell arnold press v. 2", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low", wr="moderate"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility",
            "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="DUPLICADO de 2137: texto practicamente identico. Otro 'v. 2' sin "
           "diferencia real. Mismo substitute_group."),

    E("0387", "dumbbell seated alternate front raise", "seated", grip="firm",
      stress=js(sh="high", el="low", cerv="low"),
      lat="alternating", pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["no_overhead", "cervical_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia",
            "elderly_65plus"],
      why="Version alternada del 0392. Al trabajar un brazo por vez baja la "
           "demanda global pero no cambia el estres de hombro."),

    E("0976", "band concentration curl", "seated", grip="light", lat="unilateral",
      flex="low", stress=js(el="moderate", wr="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", metab="none", gripdur="moderate", temp="none",
      contra=["elbow_injury", "tendinitis_elbow"],
      caut=["lumbar_disc", "carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "shoulder_impingement", "limited_grip", "dysautonomia",
            "chronic_fatigue", "elderly_65plus"],
      why="Curl de concentracion con banda: agarre ligero y codo apoyado en el "
           "muslo. De los pocos ejercicios de biceps aptos con agarre limitado."),

    E("1622", "dumbbell one arm reverse grip press", "bench_supine", grip="firm",
      lat="unilateral", stress=js(sh="high", el="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["wrist_injury", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="CORRECCION A E1: dice 'sit on a flat bench' pero el press unilateral "
           "de pecho se ejecuta acostado. Es bench_supine. El agarre invertido "
           "carga mas la muneca que el press normal."),

    E("0321", "dumbbell incline hammer press", "bench_incline", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "elbow_injury", "hypermobility",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Agarre neutro (martillo): la rotacion interna del hombro es menor que "
           "en el press pronado, por eso el pinzamiento pasa de contraindicacion "
           "a precaucion. Es la regresion correcta del press inclinado."),

    E("0338", "dumbbell lying elbow press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Extension de triceps acostado con mancuernas. Mismo grupo que "
           "0057 (barra) y 0436 (tate press): tres formas del mismo patron."),

    E("0374", "dumbbell prone incline curl", "bench_prone", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury"],
      caut=["tendinitis_elbow", "hypermobility", "shoulder_impingement",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Curl boca abajo: el brazo cuelga libre, rom alto y cero posibilidad "
           "de balancear el tronco. Version prona del incline curl (0318)."),

    E("0830", "weighted bench dip", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="moderate", metab="moderate",
      gripdur="moderate", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypertension", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc"],
      why="Quinto duplicado funcional del fondo en banco, ahora con lastre. "
           "Progresion de 0814/3287/1399/0815. Todos al mismo substitute_group."),

    E("0996", "band seated hip internal rotation", "seated", grip="none",
      stress=js(hip="moderate", knee="low"),
      lat="bilateral", pat="isolation", diff=1, rom="low",
      ortho="low", metab="low", laxity="low", temp="none",
      contra=["hip_replacement"],
      caut=["hip_pain", "si_joint_pain", "osteoarthritis"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "dysautonomia", "chronic_fatigue",
            "elderly_65plus", "hypertension"],
      why="El safe_for mas amplio del lote: en silla, sin agarre, sin carga "
           "axial, sin demanda cardiaca. Activacion de gluteo medio para quien "
           "casi no puede hacer nada mas. Solo la protesis de cadera lo excluye."),

    E("1662", "dumbbell lying wide curl", "bench_supine", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="none", change="low", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_lie_supine",
              "cannot_transfer_to_bench", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["tendinitis_elbow", "shoulder_impingement", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Curl acostado con agarre ancho: el hombro queda en abduccion durante "
           "todo el recorrido, de ahi el estres moderado pese a ser un curl."),

    E("1755", "weighted tricep dips", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="moderate", metab="moderate",
      gripdur="moderate", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc"],
      why="Sexto duplicado del fondo en banco. El dataset tiene una redundancia "
           "seria en este movimiento: seis entradas para un solo ejercicio."),

    E("3011", "incline scapula push up", "plank", bal="low",
      stress=js(sh="moderate", wr="moderate", el="low", lumbar="low"),
      pat="horizontal_push", diff=1, rom="low",
      ortho="none", change="moderate", valsalva="none", iso="moderate",
      metab="low", pelvic="low", gripdur="low", temp="low",
      contra=["wrist_injury", "carpal_tunnel"],
      caut=["shoulder_impingement", "rotator_cuff", "pregnancy_3rd"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "limited_balance", "no_overhead",
            "dysautonomia", "chronic_fatigue", "elderly_65plus"],
      why="Solo retraccion escapular, sin flexion de codo: difficulty 1 y "
           "recorrido minimo. Manos elevadas, no exige bajar al suelo. "
           "Excelente entrada al patron de empuje para principiantes absolutos."),

    E("3122", "resistance band seated shoulder press", "seated", grip="light",
      oh=True, axial="low", stress=js(sh="high", el="moderate", cerv="low"),
      pat="vertical_push", diff=2, rom="high",
      ortho="low", valsalva="low", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "limited_grip", "dysautonomia",
            "elderly_65plus", "chronic_fatigue"],
      why="Press vertical con banda sentado: agarre ligero lo vuelve safe_for "
           "limited_grip, cosa que la version con mancuernas (0405) no es. "
           "Regresion correcta del press de hombro."),

    E("3124", "resistance band seated chest press", "seated", grip="light",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=1, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      caut=["shoulder_impingement", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "limited_grip", "wrist_injury",
            "dysautonomia", "chronic_fatigue", "elderly_65plus", "hypertension"],
      why="Sin contraindicaciones duras: sentado, banda, sin carga axial, sin "
           "brazo sobre la cabeza. Junto con 0996 es el nucleo de una rutina "
           "para movilidad muy reducida."),

    E("3544", "bodyweight incline side plank", "side_lying", floor=True,
      bal="moderate", grip="none",
      stress=js(sh="high", lumbar="moderate", hip="moderate", el="moderate"),
      lat="unilateral", pat="core_antiextension", diff=3, rom="low",
      ortho="none", change="high", valsalva="low", iso="high",
      metab="moderate", laxity="low", pelvic="low", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_on_side",
              "shoulder_impingement", "rotator_cuff"],
      caut=["lumbar_disc", "si_joint_pain", "hip_pain", "hypertension",
            "elbow_injury", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "limited_grip", "no_overhead", "wrist_injury"],
      why="CORRECCION A E1: lo marco bench_incline por el nombre, pero el texto "
           "dice 'lying on your side' con el antebrazo en el suelo. Es "
           "side_lying. Isometrica alta sobre el hombro de apoyo."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 4: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
