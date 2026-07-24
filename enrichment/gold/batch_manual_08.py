#!/usr/bin/env python3
"""Lote 8 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0297", "dumbbell concentration curl", "seated", grip="firm",
      flex="low", lat="unilateral",
      stress=js(el="moderate", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["lumbar_disc", "carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "elderly_65plus"],
      why="Version con mancuerna del 0976 (banda). El codo apoyado en el muslo "
           "elimina toda compensacion de hombro: por eso es safe_for pinzamiento."),

    E("1390", "seated calf stretch", "seated",
      stress=js(ank="low", knee="low", hip="low"),
      lat="unilateral", pat="isolation", diff=1, rom="moderate",
      ortho="low", change="none", headdown=True, metab="none",
      laxity="moderate", temp="none",
      contra=["glaucoma", "retinal_detachment_risk"],
      caut=["plantar_fasciitis", "sciatica", "hypermobility", "hypertension",
            "dysautonomia", "lumbar_disc"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "chronic_fatigue", "elderly_65plus"],
      why="DUPLICADO funcional de 1548 (chair leg extended stretch): mismo "
           "texto, distinto musculo declarado. El dataset dice cuadriceps en uno "
           "y pantorrilla en otro para el mismo movimiento - ninguno es exacto, "
           "estira isquiotibiales y gemelo."),

    E("1731", "dumbbell close grip press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="CORRECCION A E1: dice 'sit on a flat bench' pero el press se ejecuta "
           "acostado. Es bench_supine. Octavo caso del mismo patron de error."),

    E("0364", "dumbbell one arm wrist curl", "seated", grip="firm",
      lat="unilateral", stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue",
            "elderly_65plus"],
      why="Version unilateral con mancuerna de la flexion de muneca. Mas ligera "
           "que la de barra (0126): limited_grip baja a precaucion."),

    E("0289", "dumbbell bench press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Press de banca con mancuernas: mas rom que con barra (0025) porque "
           "las manos bajan mas alla del torso. Peor para el hombro comprometido, "
           "mejor para movilidad. El eje rom_demand captura esa diferencia."),

    E("1280", "dumbbell incline one arm fly on exercise ball", "bench_supine",
      bal="high", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate"),
      lat="unilateral", pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_balance",
              "limited_grip", "vertigo", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "lumbar_pain", "multiple_sclerosis", "dysautonomia",
            "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury"],
      why="DUPLICADO de 1288 y 1286. Tres entradas para la apertura a un brazo "
           "sobre pelota."),

    E("1291", "dumbbell one arm pullover on exercise ball", "seated",
      bal="moderate", grip="firm", oh=True, ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate"),
      lat="unilateral", pat="vertical_pull", diff=3, rom="high",
      ortho="low", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="high", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "limited_balance", "vertigo"],
      caut=["hypermobility", "lumbar_pain", "hypertension", "multiple_sclerosis",
            "dysautonomia"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Sentado ERGUIDO sobre pelota, no reclinado: el tronco queda sin apoyo "
           "mientras el brazo va detras de la cabeza. Distinto de 1295 pese al "
           "nombre parecido."),

    E("3523", "glute bridge two legs on bench", "seated", bal="low",
      ext="moderate", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", pelvic="moderate", temp="low",
      contra=["lumbar_disc"],
      caut=["si_joint_pain", "hip_pain", "hip_replacement",
            "pelvic_floor_dysfunction", "postpartum", "hernia_abdominal",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_pain", "ankle_injury",
            "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "dysautonomia"],
      why="DUPLICADO de 0130 (bench hip extension): texto identico. "
           "Importante igual: es uno de los DOS unicos hinge disponibles para "
           "movilidad reducida. El hueco de tren inferior sigue abierto."),

    E("0331", "dumbbell incline twisted flyes", "bench_incline", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="low", change="low", metab="low", laxity="high",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["hypermobility", "elbow_injury", "wrist_injury", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Apertura inclinada con rotacion de muneca al final: suma componente "
           "rotacional al rango maximo de hombro. laxity high."),

    E("0138", "bottoms-up", "supine", floor=True,
      flex="high", stress=js(lumbar="high", cerv="moderate", hip="moderate"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="none", change="high", valsalva="moderate", metab="low",
      pelvic="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "cervical_injury"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="DUPLICADO funcional de 0870 (butt-ups): misma elevacion de cadera "
           "con rodillas al pecho."),

    E("0087", "barbell seated bradford rocky press", "seated", grip="firm",
      oh=True, axial="moderate",
      stress=js(sh="high", cerv="moderate", el="moderate", lumbar="low"),
      pat="vertical_push", diff=4, rom="high",
      ortho="low", valsalva="moderate", metab="moderate", laxity="moderate",
      gripdur="high", temp="moderate",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "cervical_injury", "limited_grip"],
      caut=["hypertension", "elbow_injury", "hypermobility", "osteoporosis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement"],
      why="La barra pasa alternando por delante y por DETRAS de la cabeza. "
           "cervical_injury es contraindicacion dura: obliga a proyectar el "
           "cuello adelante en cada repeticion. La barra no baja del todo, "
           "por eso el hombro nunca sale de tension - gripdur high."),

    E("0845", "weighted russian twist (legs up)", "seated", floor=True,
      bal="high", grip="firm", flex="moderate", rot="high",
      stress=js(lumbar="high", hip="high", sh="moderate", cerv="low"),
      lat="alternating", pat="core_rotation", diff=4, rom="moderate",
      ortho="low", change="high", valsalva="moderate", iso="high",
      metab="moderate", pelvic="high", gripdur="moderate", temp="moderate",
      contra=["cannot_get_on_floor", "lumbar_disc", "sciatica", "si_joint_pain",
              "hernia_abdominal", "osteoporosis", "limited_grip",
              "limited_balance", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "postpartum", "hypertension", "shoulder_impingement",
            "hip_pain"],
      why="Version mas dura de 0846: pies en el aire suma equilibrio alto y "
           "flexion de cadera sostenida. Doce contraindicaciones duras - "
           "de los mas restrictivos del catalogo."),

    E("2429", "frog crunch", "supine", floor=True,
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "hip_pain"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Manos detras de la cabeza otra vez: cervical high. Es el patron mas "
           "repetido del catalogo y la causa mas comun de dolor de cuello al "
           "hacer abdominales."),

    E("2799", "barbell sitted alternate leg raise", "seated", grip="firm",
      flex="low", stress=js(hip="high", lumbar="moderate", wr="low"),
      lat="alternating", pat="core_flexion", diff=2, rom="moderate",
      ortho="low", change="none", valsalva="low", metab="low",
      pelvic="moderate", gripdur="moderate", temp="low",
      contra=["lumbar_disc", "sciatica", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "hernia_abdominal", "postpartum",
            "si_joint_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_pain", "ankle_injury", "shoulder_impingement", "no_overhead",
            "dysautonomia"],
      why="Elevacion alternada sentado con barra en los muslos. Al alternar, "
           "cada pierna trabaja sola y la lumbar baja de high (0620, ambas "
           "piernas) a moderate. Regresion util."),

    E("0086", "barbell seated behind head military press", "seated", grip="firm",
      oh=True, axial="moderate",
      stress=js(sh="high", cerv="high", el="moderate", lumbar="low"),
      pat="vertical_push", diff=4, rom="high",
      ortho="low", valsalva="moderate", metab="low", laxity="high",
      gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "cervical_injury", "limited_grip", "hypermobility"],
      caut=["hypertension", "elbow_injury", "osteoporosis", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement"],
      why="Press por detras de la nuca: rotacion externa maxima con abduccion "
           "completa, la posicion de mayor riesgo de pinzamiento y de "
           "inestabilidad anterior del hombro. laxity high e hipermovilidad "
           "como contraindicacion dura. Es el press de hombro MENOS recomendable "
           "del catalogo - contraste util frente a los nueve presses sentados "
           "seguros ya clasificados."),

    E("0137", "body-up", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia"],
      why="DECIMO duplicado del fondo en banco. E1 no resolvio la postura "
           "porque el texto arranca con 'placing your hands', sin verbo de "
           "posicion. Diez entradas para el mismo movimiento."),

    E("0865", "lying leg-hip raise", "supine", floor=True,
      flex="moderate", stress=js(hip="high", lumbar="high", cerv="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="moderate", iso="moderate",
      metab="low", pelvic="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "postpartum", "osteoporosis"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Version en suelo del 0620. Las manos bajo los gluteos reducen la "
           "anteversion pelvica, pero el psoas sigue traccionando: lumbar high."),

    E("1255", "barbell decline pullover", "bench_supine", grip="firm", oh=True,
      ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="none", change="moderate", headdown=True, valsalva="high",
      metab="low", laxity="high", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "glaucoma", "retinal_detachment_risk",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "dysautonomia", "vertigo", "migraine",
            "hypermobility", "lumbar_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance"],
      why="Combinacion mas riesgosa del lote para presion craneal: cabeza por "
           "debajo del corazon + barra sobre la cabeza + valsalva high. "
           "Glaucoma y riesgo retinal como contraindicaciones duras."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 8: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
