#!/usr/bin/env python3
"""Lote 12 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0384", "dumbbell reverse preacher curl", "bench_prone", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "tendinitis_elbow",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["wrist_injury", "carpal_tunnel", "hypermobility",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia"],
      why="CORRECCION A E1: 'chest against the support' es prono. Decimo caso "
           "del mismo error. Version con mancuernas de 0081; al no fijar el "
           "agarre, la muneca baja de high a moderate."),

    E("0358", "dumbbell one arm reverse wrist curl", "seated", grip="firm",
      lat="unilateral", stress=js(wr="moderate", el="moderate"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="Version unilateral de 0385. La familia de flexo-extension de muneca "
           "ya tiene ocho entradas: es el segundo patron mas duplicado del "
           "catalogo despues del fondo en banco."),

    E("0303", "dumbbell decline hammer press", "bench_supine", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="low",
      metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "glaucoma", "retinal_detachment_risk",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "elbow_injury", "hypermobility",
            "hypertension", "dysautonomia", "vertigo", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead"],
      why="Agarre neutro en declinado: el hombro queda en moderate (buena "
           "noticia) pero head_below_heart activa glaucoma y presion craneal. "
           "Dos ejes independientes tirando en direcciones opuestas."),

    E("0307", "dumbbell decline twist fly", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate"),
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
      why="Apertura declinada con rotacion: suma componente rotacional al "
           "rango maximo de hombro, mas cabeza bajo el corazon. "
           "Variante de 0302 con un riesgo mas."),

    E("1735", "dumbbell lying single extension", "bench_supine", grip="firm",
      lat="unilateral", stress=js(el="high", sh="moderate", wr="moderate"),
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
      why="Rompecraneos unilateral. Al trabajar un brazo por vez la carga "
           "absoluta baja: es la regresion de 0057/0061 para codo sensible."),

    E("0317", "dumbbell incline curl v. 2", "bench_incline", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="DUPLICADO de 0318. Decimocuarto par 'v. 2' con texto equivalente."),

    E("1279", "dumbbell incline one arm fly", "bench_incline", grip="firm",
      lat="unilateral", stress=js(sh="high", el="moderate", wr="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="low", change="low", valsalva="low", iso="low", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["hypermobility", "elbow_injury", "si_joint_pain", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Apertura inclinada a un brazo en banco firme. Frente a las versiones "
           "sobre pelota (1280, 1286, 1288), esta no exige equilibrio: es su "
           "regresion natural y sirve para quien tiene vertigo o EM."),

    E("0469", "groin crunch", "supine", floor=True,
      flex="high", stress=js(lumbar="high", cerv="high", hip="high"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "sciatica", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "osteoporosis", "postpartum"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="Otro del grupo de abdominales con manos detras de la cabeza. "
           "Suma elevacion de piernas: cadera y suelo pelvico a high."),

    E("1747", "ez bar french press on exercise ball", "seated", bal="moderate",
      grip="firm", oh=True,
      stress=js(el="high", sh="high", wr="moderate", lumbar="moderate"),
      pat="isolation", diff=3, rom="high",
      ortho="low", change="low", valsalva="moderate", iso="moderate",
      metab="low", laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "tendinitis_elbow", "limited_grip",
              "limited_balance", "vertigo"],
      caut=["hypermobility", "lumbar_pain", "hypertension", "cervical_injury",
            "multiple_sclerosis", "dysautonomia"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement"],
      why="Extension de triceps sobre la cabeza en pelota inestable: combina "
           "restriccion de hombro, codo y equilibrio. Ocho contraindicaciones "
           "duras para un ejercicio de aislamiento - poco eficiente en "
           "relacion riesgo/beneficio."),

    E("0717", "side push-up", "side_lying", floor=True, bal="moderate",
      stress=js(sh="high", el="high", wr="high", lumbar="low"),
      lat="unilateral", pat="horizontal_push", diff=4, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="low", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_on_side", "wrist_injury",
              "carpal_tunnel", "shoulder_impingement", "rotator_cuff",
              "elbow_injury"],
      caut=["hypermobility", "hypertension", "obesity",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "limited_grip"],
      why="Empuje unilateral desde decubito lateral: todo el peso sobre un "
           "brazo con la muneca en extension. Segundo side_lying del catalogo "
           "tras 3544 y 1712 - postura rara y valiosa para cobertura."),

    E("1316", "barbell bent arm pullover", "bench_supine", grip="firm", oh=True,
      ext="moderate",
      stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "elbow_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "dysautonomia"],
      why="Pullover con codo flexionado: acorta el brazo de palanca, por eso "
           "laxity baja de high (0073, brazo recto) a moderate. Es la "
           "regresion correcta del pullover para hombro sensible."),

    E("1358", "side lying floor stretch", "side_lying", floor=True, oh=True,
      rot="moderate",
      stress=js(sh="moderate", lumbar="moderate", hip="moderate"),
      lat="unilateral", pat="isolation", diff=1, rom="high",
      ortho="none", change="high", metab="none", laxity="high", temp="none",
      contra=["cannot_get_on_floor", "cannot_lie_on_side", "no_overhead",
              "shoulder_impingement"],
      caut=["lumbar_disc", "si_joint_pain", "hip_pain", "hypermobility",
            "rotator_cuff", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "limited_grip", "wrist_injury", "carpal_tunnel",
            "dysautonomia", "chronic_fatigue", "elderly_65plus"],
      why="CORRECCION A E1: lo marco supine pero dice 'lie on your side'. "
           "Es side_lying. Estiramiento de dorsal con rotacion: laxity high, "
           "cuidado en hipermovilidad."),

    E("1428", "wrist circles", "standing", standing=True,
      stress=js(wr="low", el="low", sh="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="none", metab="none", laxity="low",
      gripdur="low", temp="none",
      contra=["cannot_stand"],
      caut=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis",
            "dysautonomia"],
      safe=["limited_balance", "knee_injury", "knee_pain", "ankle_injury",
            "lumbar_disc", "hip_replacement", "no_overhead", "limited_grip",
            "chronic_fatigue", "elderly_65plus", "hypertension", "osteoporosis",
            "cervical_injury"],
      why="Movilidad de muneca sin carga. Se hace de pie segun el texto, pero "
           "es trivialmente adaptable a sentado - candidato claro para que E4 "
           "lo marque como variante postural libre. 13 safe_for."),

    E("1721", "barbell reverse grip skullcrusher", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="high"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "limited_grip", "cannot_lie_supine",
              "cannot_transfer_to_bench", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypermobility", "rheumatoid_arthritis"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Rompecraneos con agarre invertido: la muneca en supinacion "
           "sosteniendo carga sobre la cara sube a high. Es la version MENOS "
           "apta para muneca de toda la familia de extensiones de triceps."),

    E("2312", "lying elbow to knee", "supine", floor=True,
      flex="high", rot="high",
      stress=js(lumbar="high", cerv="high", hip="moderate"),
      lat="alternating", pat="core_rotation", diff=2, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="moderate",
      pelvic="moderate", temp="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "sciatica", "si_joint_pain",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum",
            "pelvic_floor_dysfunction"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="DUPLICADO de 0443 y 0003. Tercera entrada de la bicicleta abdominal. "
           "Decimoquinto par duplicado del catalogo."),

    E("3019", "bench pull-ups", "hanging", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", valsalva="low", metab="moderate",
      gripdur="high", temp="low",
      contra=["limited_grip", "wrist_injury", "carpal_tunnel"],
      caut=["shoulder_impingement", "elbow_injury", "cannot_stand"],
      safe=["knee_injury", "knee_pain", "hip_replacement", "lumbar_disc",
            "no_overhead", "ankle_injury"],
      why="DUPLICADO funcional de 0499 (inverted row). E1 no resolvio la "
           "postura porque el texto abre con 'Position yourself under a bar'. "
           "Es la regresion clave de la dominada."),

    E("3193", "glute-ham raise", "bench_prone", ext="moderate",
      stress=js(knee="high", lumbar="moderate", hip="high"),
      pat="hinge", diff=4, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
              "knee_replacement", "lumbar_disc",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_pain", "si_joint_pain", "hip_pain", "osteoarthritis",
            "hypertension", "hamstring" if False else "hypermobility"],
      safe=["cannot_stand", "limited_balance", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "dysautonomia", "cervical_injury"],
      why="Elevacion de gluteo-femoral: quinto hinge del catalogo y el mas "
           "exigente. La rodilla soporta casi todo el torque - por eso "
           "knee_injury es contraindicacion dura pese a ser un ejercicio de "
           "isquiotibiales."),

    E("3288", "korean dips", "hanging", grip="firm", bal="moderate",
      ext="moderate", stress=js(sh="high", el="high", wr="high", lumbar="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", laxity="high", gripdur="high", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "wrist_injury", "carpal_tunnel", "tendinitis_elbow",
              "hypermobility", "lumbar_disc"],
      caut=["hypertension", "cardiac", "obesity", "cervical_injury"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement"],
      why="Fondos coreanos: el cuerpo pasa por detras de las barras, llevando "
           "el hombro a extension extrema. laxity high y difficulty 5. "
           "Duodecimo miembro de la familia del fondo y su version mas "
           "agresiva para el hombro."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 12: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
