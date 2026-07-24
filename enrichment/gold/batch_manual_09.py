#!/usr/bin/env python3
"""Lote 9 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0296", "dumbbell close-grip press", "bench_supine", grip="firm",
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
      why="DUPLICADO de 1731: texto identico, solo cambia el guion del nombre "
           "('close-grip' vs 'close grip'). Decimo par duplicado."),

    E("0385", "dumbbell reverse wrist curl", "seated", grip="firm",
      stress=js(wr="moderate", el="moderate"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="Version con mancuernas del 0082. El codo queda moderate: la extension "
           "de muneca cargada es el mecanismo de la epicondilitis lateral."),

    E("1678", "dumbbell seated hammer curl", "seated", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "elderly_65plus"],
      why="Agarre neutro: descarga la muneca respecto del curl supinado (0391). "
           "Es la variante preferible cuando hay molestia de muneca sin llegar "
           "a lesion."),

    E("0288", "dumbbell around pullover", "bench_supine", grip="firm", oh=True,
      ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "elbow_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance", "dysautonomia"],
      why="DUPLICADO funcional de 0375 (dumbbell pullover). Mismo grupo."),

    E("0302", "dumbbell decline fly", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="low"),
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
      why="Apertura en declinado: suma head_below_heart al rango maximo de "
           "hombro. Combina los dos riesgos - articular y de presion craneal."),

    E("0400", "dumbbell seated one leg calf raise", "seated", grip="firm",
      axial="low", lat="unilateral",
      stress=js(ank="moderate", knee="low", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="none", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["ankle_injury", "plantar_fasciitis"],
      caut=["knee_pain", "osteoarthritis", "hypermobility", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "lumbar_disc", "hip_replacement",
            "shoulder_impingement", "no_overhead", "dysautonomia",
            "cervical_injury", "elderly_65plus"],
      why="Version unilateral del 1379. Al trabajar una pierna por vez duplica "
           "la carga relativa sin necesidad de mas peso: progresion util para "
           "quien entrena sentado y no puede aumentar mucho la mancuerna."),

    E("0404", "dumbbell seated shoulder press (parallel grip)", "seated",
      grip="firm", oh=True, axial="low",
      stress=js(sh="moderate", el="moderate", cerv="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "rotator_cuff"],
      caut=["shoulder_impingement", "cervical_injury", "hypertension",
            "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="IMPORTANTE: agarre paralelo (neutro). La rotacion interna del hombro "
           "es mucho menor que en el press pronado, por eso el hombro baja a "
           "moderate y el pinzamiento pasa de contraindicacion a PRECAUCION. "
           "Es el unico vertical_push del catalogo que sobrevive al filtro de "
           "pinzamiento leve - resuelve parcialmente el hueco detectado en el lote 8."),

    E("1282", "dumbbell incline one arm press on exercise ball", "bench_incline",
      bal="moderate", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate"),
      lat="unilateral", pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="moderate", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "limited_balance", "limited_grip",
              "vertigo", "cannot_lie_supine", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["rotator_cuff", "hypermobility", "lumbar_pain", "multiple_sclerosis",
            "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Press a un brazo sobre pelota: la asimetria obliga a anti-rotacion "
           "constante del tronco sobre superficie inestable."),

    E("3545", "dumbbell incline alternate press", "bench_incline", grip="firm",
      stress=js(sh="high", el="moderate", wr="low", lumbar="low"),
      lat="alternating", pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", metab="low",
      gripdur="high", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["elbow_injury", "hypermobility", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Al alternar, el brazo que espera sostiene la mancuerna arriba en "
           "isometrico: grip_duration high. Mas exigente de lo que parece."),

    E("3147", "pelvic tilt", "supine", floor=True,
      flex="low", stress=js(lumbar="low", hip="low"),
      pat="core_antiextension", diff=1, rom="low",
      ortho="none", change="high", valsalva="none", iso="moderate",
      metab="none", pelvic="low", temp="none",
      contra=["cannot_get_on_floor", "cannot_lie_supine"],
      caut=["pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "lumbar_disc", "sciatica", "hernia_abdominal", "postpartum",
            "pelvic_floor_dysfunction", "dysautonomia", "chronic_fatigue",
            "fibromyalgia", "elderly_65plus", "hypertension", "osteoporosis"],
      why="HALLAZGO: el unico ejercicio de core que es safe_for lumbar_disc, "
           "sciatica, hernia_abdominal, postpartum Y suelo pelvico a la vez. "
           "22 safe_for - el mas alto del catalogo. Es la base de cualquier "
           "progresion de core en rehabilitacion: activa transverso sin "
           "flexion espinal ni presion intraabdominal."),

    E("0735", "sit-up v. 2", "supine", floor=True,
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="DUPLICADO del grupo de 10 abdominales con texto identico "
           "(3/4 sit-up, cocoons, curl-up, janda sit-up, negative crunch...). "
           "Undecimo par duplicado."),

    E("0850", "weighted side bend (on stability ball)", "seated", bal="moderate",
      grip="firm", rot="moderate",
      stress=js(lumbar="high", sh="low", hip="low"),
      lat="unilateral", pat="core_rotation", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", pelvic="moderate", gripdur="moderate", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "osteoporosis",
              "limited_balance", "vertigo", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hernia_abdominal", "postpartum",
            "multiple_sclerosis", "elderly_65plus"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead"],
      why="Flexion lateral cargada sobre pelota: la carga asimetrica lateral es "
           "de las peores para el disco. osteoporosis contraindicada por riesgo "
           "de fractura vertebral por compresion lateral."),

    E("1352", "lower back curl", "prone", floor=True,
      ext="high", stress=js(lumbar="moderate", cerv="moderate", hip="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", pelvic="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_prone",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "osteoporosis", "cervical_injury",
            "hypermobility", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "dysautonomia"],
      why="CORRECCION A E1: lo marco supine pero el texto dice 'lie flat on "
           "your stomach'. Es prone. Extension lumbar activa - como sphinx, "
           "en hernia discal suele aliviar (McKenzie), de ahi precaucion y no "
           "contraindicacion. En osteoporosis si es riesgoso por la extension "
           "forzada."),

    E("1366", "upward facing dog", "prone", floor=True,
      ext="high", stress=js(lumbar="high", sh="moderate", wr="high", cerv="moderate"),
      pat="isolation", diff=2, rom="high",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", laxity="high", pelvic="low", temp="low", gripdur="low",
      contra=["cannot_get_on_floor", "cannot_lie_prone", "wrist_injury",
              "carpal_tunnel", "osteoporosis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "cervical_injury", "hypermobility",
            "shoulder_impingement", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="Extension lumbar maxima con las munecas cargadas en extension. "
           "Mas agresivo que sphinx (1362), que es su regresion natural: "
           "sphinx apoya antebrazos y no carga muneca. Buen par para E4."),

    E("1466", "twist hip lift", "supine", floor=True,
      ext="moderate", rot="high",
      stress=js(lumbar="high", hip="moderate", knee="low"),
      lat="alternating", pat="core_rotation", diff=3, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "si_joint_pain", "sciatica",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "osteoporosis", "postpartum",
            "hernia_abdominal"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Puente de gluteo con rotacion: la torsion con la cadera elevada "
           "carga la sacroiliaca de forma asimetrica. si_joint_pain como "
           "contraindicacion dura."),

    E("1627", "ez barbell close grip preacher curl", "seated_machine", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypermobility",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia"],
      why="Barra EZ en banco predicador con agarre cerrado. El agarre cerrado "
           "aumenta la supinacion forzada: muneca a moderate. Progresion "
           "intermedia entre 0372 (mancuerna) y 0070 (barra recta)."),

    E("2800", "barbell sitted alternate leg raise (female)", "seated", grip="light",
      flex="low", stress=js(hip="high", lumbar="moderate"),
      lat="alternating", pat="core_flexion", diff=2, rom="moderate",
      ortho="low", change="none", valsalva="low", metab="low",
      pelvic="moderate", gripdur="low", temp="low",
      contra=["lumbar_disc", "sciatica", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hip_pain", "lumbar_pain", "hernia_abdominal", "postpartum",
            "si_joint_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_pain", "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "dysautonomia"],
      why="DUPLICADO de 2799 con sufijo '(female)'. Diferencia real minima: "
           "aca las manos se apoyan en el banco en vez de sostener la barra, "
           "por eso grip baja a light y limited_grip pasa a safe_for."),

    E("3302", "handstand", "plank", floor=True, bal="high", oh=True,
      ext="moderate",
      stress=js(sh="high", wr="high", el="high", cerv="moderate", lumbar="moderate"),
      pat="vertical_push", diff=5, rom="high",
      ortho="high", change="high", headdown=True, valsalva="high",
      iso="high", metab="high", laxity="moderate", pelvic="low",
      temp="moderate", gripdur="low",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "shoulder_impingement", "rotator_cuff", "no_overhead",
              "limited_balance", "vertigo", "glaucoma", "retinal_detachment_risk",
              "hypertension", "cardiac", "cervical_injury", "osteoporosis",
              "epilepsy", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "dysautonomia", "migraine", "elderly_65plus",
            "obesity", "multiple_sclerosis"],
      why="El ejercicio MAS contraindicado del catalogo: 18 contraindicaciones "
           "duras. Inversion completa con todo el peso sobre munecas. "
           "Combina head_below_heart, valsalva high, equilibrio alto y "
           "orthostatic_load high. Sirve como techo absoluto de la escala de "
           "riesgo, util para calibrar el resto."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 9: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
