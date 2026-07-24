#!/usr/bin/env python3
"""Lote 6 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0388", "dumbbell seated alternate press", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low", lumbar="low"),
      lat="alternating", pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="low", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility",
            "si_joint_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="Octavo press de hombro sentado. Al alternar, la carga asimetrica "
           "genera algo de torsion lumbar - por eso valsalva baja a low pero "
           "aparece si_joint_pain como precaucion."),

    E("0812", "triceps dip (bench leg)", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia"],
      why="OCTAVO duplicado del fondo en banco. Ya es un caso de estudio: "
           "el 0,9% del catalogo es el mismo ejercicio."),

    E("1677", "dumbbell seated bicep curl", "seated", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="DUPLICADO de 0391 (dumbbell seated curl): texto identico. "
           "Cuarto par duplicado del dataset."),

    E("1587", "seated wide angle pose sequence", "seated", floor=True,
      flex="moderate", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="isolation", diff=1, rom="high",
      ortho="low", change="high", headdown=True, metab="none",
      laxity="high", temp="none",
      contra=["cannot_get_on_floor", "hip_replacement", "glaucoma",
              "retinal_detachment_risk"],
      caut=["lumbar_disc", "sciatica", "si_joint_pain", "hip_pain",
            "hypermobility", "hypertension", "dysautonomia", "pregnancy_3rd"],
      safe=["cannot_stand", "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "chronic_fatigue", "elderly_65plus"],
      why="Apertura amplia de piernas con flexion de tronco: laxity high. "
           "En hipermovilidad es de los estiramientos que mas facil sobrepasa "
           "el rango seguro de cadera y aductores."),

    E("1290", "dumbbell one arm press on exercise ball", "seated", bal="moderate",
      grip="firm", oh=True, axial="low",
      stress=js(sh="high", el="moderate", lumbar="moderate", cerv="low"),
      lat="unilateral", pat="vertical_push", diff=3, rom="high",
      ortho="low", change="low", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_balance", "vertigo"],
      caut=["hypertension", "lumbar_pain", "multiple_sclerosis", "dysautonomia",
            "elderly_65plus", "hypermobility"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Sentado ERGUIDO sobre pelota (no reclinado): la inestabilidad obliga "
           "a estabilizar el tronco mientras el brazo va sobre la cabeza. "
           "Equilibrio como contraindicacion dura."),

    E("1292", "dumbbell one leg fly on exercise ball", "seated", bal="high",
      sl=True, grip="firm",
      stress=js(sh="high", el="moderate", lumbar="moderate", hip="moderate"),
      lat="unilateral", pat="horizontal_push", diff=4, rom="high",
      ortho="low", change="low", valsalva="low", iso="high",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate",
      temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "limited_balance",
              "limited_grip", "vertigo", "hip_replacement", "knee_injury"],
      caut=["hypermobility", "lumbar_pain", "multiple_sclerosis", "dysautonomia",
            "elderly_65plus", "knee_pain"],
      why="Apertura con una pierna levantada sobre pelota: combina inestabilidad, "
           "apoyo unipodal y rango maximo de hombro. difficulty 4 y equilibrio "
           "alto - de los mas exigentes del catalogo en estabilidad."),

    E("0492", "incline push up depth jump", "plank", bal="moderate",
      impact="high", stress=js(sh="high", el="high", wr="high", lumbar="low"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="low",
      metab="high", pelvic="low", temp="high", gripdur="low",
      contra=["wrist_injury", "carpal_tunnel", "elbow_injury",
              "shoulder_impingement", "rotator_cuff", "osteoporosis",
              "rheumatoid_arthritis"],
      caut=["cardiac", "hypertension", "obesity", "chronic_fatigue",
            "fibromyalgia", "dysautonomia", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury"],
      why="Pliometrico de tren superior sobre superficie elevada. impact high "
           "y metabolic high: interesante porque es exigente sin cargar nada "
           "de tren inferior - opcion cardiovascular para lesion de rodilla."),

    E("1254", "band bench press", "bench_supine", grip="light",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "limited_grip", "wrist_injury",
            "dysautonomia", "elderly_65plus"],
      why="Press de banca con banda: la resistencia progresiva descarga el "
           "hombro en el punto de mayor riesgo (abajo). Por eso el pinzamiento "
           "es precaucion y no contraindicacion, a diferencia del 0025 con barra. "
           "Es la regresion correcta del press de banca."),

    E("1281", "dumbbell incline one arm press", "bench_incline", grip="firm",
      stress=js(sh="high", el="moderate", lumbar="low", wr="low"),
      lat="unilateral", pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["elbow_injury", "hypermobility", "si_joint_pain", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Press inclinado a un brazo. La carga asimetrica exige anti-rotacion "
           "del tronco aunque el banco de soporte."),

    E("1362", "sphinx", "prone", floor=True,
      ext="moderate", stress=js(lumbar="moderate", sh="moderate", cerv="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="high", metab="none", laxity="moderate",
      pelvic="low", temp="none",
      contra=["cannot_get_on_floor", "cannot_lie_prone",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "hypermobility",
            "shoulder_impingement", "osteoporosis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "limited_grip",
            "wrist_injury", "carpal_tunnel", "chronic_fatigue", "dysautonomia"],
      why="Extension lumbar suave apoyado en antebrazos. OJO: en hernia discal "
           "la extension suele ALIVIAR (metodo McKenzie) mientras la flexion "
           "agrava - por eso lumbar_disc es precaucion aca y contraindicacion "
           "en los abdominales. La direccion del movimiento importa mas que la zona."),

    E("1371", "barbell seated calf raise v2", "seated", grip="firm",
      axial="low", stress=js(ank="moderate", knee="low", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="none", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["ankle_injury", "plantar_fasciitis", "limited_grip"],
      caut=["knee_pain", "osteoarthritis", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "lumbar_disc", "hip_replacement",
            "shoulder_impingement", "no_overhead", "dysautonomia",
            "cervical_injury"],
      why="DUPLICADO de 0088. Este describe el rango completo (baja el talon "
           "por debajo del escalon), de ahi rom high vs moderate. "
           "Diferencia minima pero real."),

    E("1458", "ez barbell seated curls", "seated", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="high", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["carpal_tunnel", "rheumatoid_arthritis", "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="La barra EZ tiene angulo: reduce el estres de muneca frente a la "
           "barra recta (0070). Progresion util: mancuerna -> EZ -> barra recta, "
           "en ese orden de tolerancia de muneca."),

    E("1674", "dumbbell prone incline hammer curl", "bench_prone", grip="firm",
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
      why="Version martillo del 0374. El agarre neutro descarga la muneca "
           "respecto del curl supinado."),

    E("3117", "band fixed back close grip pulldown", "seated", grip="light",
      oh=True, stress=js(sh="moderate", el="moderate", lumbar="low"),
      pat="vertical_pull", diff=2, rom="high",
      ortho="low", change="none", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement"],
      caut=["rotator_cuff", "elbow_injury", "cervical_injury", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "limited_grip", "dysautonomia", "elderly_65plus",
            "chronic_fatigue"],
      why="Jalon vertical sentado con banda: cubre el patron vertical_pull sin "
           "colgarse ni necesitar agarre firme. Es la unica alternativa real a "
           "la dominada para perfiles restringidos - hallazgo importante."),

    E("3144", "resistance band seated straight back row", "seated", floor=True,
      grip="light", stress=js(sh="moderate", el="moderate", lumbar="moderate"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="high", valsalva="low", iso="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["cannot_get_on_floor"],
      caut=["lumbar_disc", "shoulder_impingement", "elbow_injury",
            "hypermobility", "sciatica"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "limited_grip",
            "dysautonomia", "elderly_65plus", "chronic_fatigue"],
      why="Remo sentado en el suelo con banda. Requiere bajar al suelo, a "
           "diferencia del 0990 que se hace en silla - misma funcion, distinta "
           "accesibilidad. Buen par para el grafo de sustituciones."),

    E("0003", "air bike", "supine", floor=True,
      flex="high", rot="high",
      stress=js(lumbar="high", cerv="high", hip="moderate"),
      lat="alternating", pat="core_rotation", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="low",
      metab="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "sciatica", "hernia_abdominal",
              "recent_abdominal_surgery", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "osteoporosis", "postpartum",
            "pelvic_floor_dysfunction"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Bicicleta abdominal: manos detras de la cabeza (cervical high) mas "
           "flexion y rotacion lumbar simultaneas. Muy popular y de los peores "
           "para disco. La combinacion flexion+rotacion es la que mas presion "
           "genera sobre el anillo fibroso."),

    E("0125", "barbell wrist curl v. 2", "seated", grip="firm",
      stress=js(wr="high", el="low"), pat="isolation", diff=2, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="DUPLICADO de 0126. Quinto par 'v. 2' con texto identico."),

    E("0276", "dead bug", "supine", floor=True,
      ext="none", stress=js(lumbar="low", hip="moderate", sh="low"),
      lat="alternating", pat="core_antiextension", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", pelvic="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "hernia_abdominal", "postpartum", "hip_pain",
            "recent_abdominal_surgery"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "dysautonomia", "elderly_65plus"],
      why="CLAVE: es el abdominal seguro. Anti-extension con la lumbar pegada "
           "al piso, sin flexion espinal y sin manos detras de la cabeza. "
           "lumbar low y cervical none, contra el high de casi todos los demas "
           "abdominales. Es la sustitucion correcta cuando el motor excluye "
           "crunches y sit-ups por disco."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 6: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
