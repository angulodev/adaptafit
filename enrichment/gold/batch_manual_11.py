#!/usr/bin/env python3
"""Lote 11 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("1770", "biceps leg concentration curl", "seated", grip="firm",
      flex="low", lat="unilateral",
      stress=js(el="moderate", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["lumbar_disc", "carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "elderly_65plus"],
      why="DUPLICADO de 0297 (concentration curl). El dataset lo lista como "
           "'body weight' pero el texto pide mancuerna: error de equipamiento "
           "del upstream, no de E1. Decimotercer par duplicado."),

    E("0369", "dumbbell over bench wrist curl", "seated", grip="firm",
      stress=js(wr="moderate", el="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="Antebrazos apoyados en el banco en vez de en los muslos: mas "
           "estable y con rango algo mayor. Diferencia real frente a 0126, "
           "aunque menor."),

    E("1734", "dumbbell kickbacks on exercise ball", "seated", bal="moderate",
      grip="firm", flex="low",
      stress=js(el="moderate", sh="moderate", lumbar="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", gripdur="moderate", temp="low",
      contra=["limited_balance", "vertigo", "limited_grip", "elbow_injury"],
      caut=["lumbar_disc", "shoulder_impingement", "multiple_sclerosis",
            "dysautonomia", "elderly_65plus", "tendinitis_elbow"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead"],
      why="Patada de triceps sentado erguido sobre pelota. Sin apoyo de "
           "respaldo, el tronco sostiene la posicion: iso moderate y equilibrio "
           "como contraindicacion dura."),

    E("1380", "dumbbell seated one leg calf raise - hammer grip", "seated",
      grip="firm", axial="low", lat="unilateral",
      stress=js(ank="moderate", knee="low", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="none", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["ankle_injury", "plantar_fasciitis"],
      caut=["knee_pain", "osteoarthritis", "hypermobility", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "lumbar_disc", "hip_replacement",
            "shoulder_impingement", "no_overhead", "dysautonomia",
            "cervical_injury", "elderly_65plus"],
      why="Trilogia de pantorrilla sentada unilateral: 0400 (neutro), "
           "1381 (palma arriba, muneca moderate), 1380 (martillo, muneca low). "
           "El agarre martillo es el mas amable con la muneca de los tres."),

    E("0314", "dumbbell incline bench press", "bench_incline", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="low", change="low", valsalva="low", metab="low",
      laxity="moderate", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["elbow_injury", "wrist_injury", "hypermobility", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="DUPLICADO funcional de 0316. Version pronada del press inclinado; "
           "la neutra (0321/0324) es su alternativa para hombro comprometido."),

    E("0328", "dumbbell incline shoulder raise", "bench_incline", grip="firm",
      oh=True, stress=js(sh="high", cerv="low", el="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", valsalva="low", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_transfer_to_bench"],
      caut=["cervical_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="Version con mancuernas de 0050. Elevacion escapular: trabaja "
           "serrato anterior, util para discinesia escapular si el hombro "
           "tolera la posicion overhead."),

    E("0343", "dumbbell lying one arm press", "bench_supine", grip="firm",
      lat="unilateral", stress=js(sh="high", el="moderate", wr="low", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "hypermobility", "si_joint_pain"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="Press plano a un brazo. La carga asimetrica exige anti-rotacion "
           "del tronco aunque el banco sostenga la espalda."),

    E("0274", "crunch floor", "supine", floor=True,
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="low"),
      pat="core_flexion", diff=1, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "postpartum", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury"],
      why="El crunch clasico. Duodecimo miembro del grupo de abdominales con "
           "manos detras de la cabeza: cervical high es el sello del grupo. "
           "Su regresion segura sigue siendo curl-up (3016) o pelvic tilt (3147)."),

    E("1619", "dumbbell incline one arm hammer press", "bench_incline",
      grip="firm", lat="unilateral",
      stress=js(sh="moderate", el="high", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "hypermobility", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Agarre martillo unilateral: el hombro queda en moderate y el "
           "pinzamiento es precaucion. Otra pieza del eje de sustitucion por "
           "agarre detectado en el lote 10."),

    E("0061", "barbell lying triceps extension", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="DUPLICADO de 0057 (barbell lying extension). Rompecraneos: "
           "el codo es la articulacion critica, no el hombro."),

    E("0072", "barbell prone incline curl", "bench_prone", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="moderate"),
      pat="isolation", diff=2, rom="high",
      ortho="low", change="moderate", metab="low", laxity="moderate",
      gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury"],
      caut=["tendinitis_elbow", "wrist_injury", "hypermobility",
            "shoulder_impingement", "pregnancy_1st", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Version con barra de 0374. La barra recta fija la supinacion: "
           "muneca sube a moderate frente a la version con mancuernas."),

    E("0122", "barbell wide bench press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "hypertension", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia"],
      why="El agarre ancho aumenta la abduccion del hombro en el punto bajo: "
           "laxity high. Es la variante del press de banca MENOS recomendable "
           "para hombro, frente al agarre cerrado (0055) que descarga el hombro "
           "pero carga codo y muneca."),

    E("0140", "biceps pull-up", "hanging", grip="hanging_bodyweight", oh=True,
      stress=js(sh="high", el="high", wr="high", lumbar="low"),
      pat="vertical_pull", diff=4, rom="high",
      ortho="moderate", valsalva="moderate", metab="moderate", laxity="moderate",
      gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "tendinitis_elbow"],
      caut=["hypertension", "obesity", "elderly_65plus", "hypermobility"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement", "limited_balance"],
      why="DUPLICADO funcional de 1326 (chin-up) y 0651. Cuarta dominada del "
           "catalogo. Todas comparten: cero demanda de tren inferior, agarre "
           "y hombro como limitantes."),

    E("0248", "cambered bar lying row", "bench_prone", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="low", change="moderate", valsalva="low", metab="moderate",
      gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "elbow_injury", "wrist_injury",
            "carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="Remo con pecho apoyado y barra: cero carga lumbar. Junto con 0049 "
           "y 0327, uno de los pocos remos pesados aptos para hernia discal."),

    E("0484", "hip raise (bent knee)", "supine", floor=True,
      ext="moderate", stress=js(hip="moderate", lumbar="low", knee="low"),
      pat="hinge", diff=1, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="low", pelvic="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_3rd"],
      caut=["si_joint_pain", "hip_pain", "hip_replacement", "lumbar_disc",
            "postpartum"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "dysautonomia", "chronic_fatigue", "elderly_65plus", "osteoporosis"],
      why="HALLAZGO: el puente de gluteo en suelo es el unico hinge del "
           "catalogo con lumbar low y 15 safe_for. Cuarto patron de cadera "
           "disponible, y de lejos el mas accesible. Base de progresion de "
           "cadena posterior en rehabilitacion."),

    E("0670", "rear pull-up", "hanging", grip="hanging_bodyweight", oh=True,
      stress=js(sh="high", el="high", wr="high", cerv="moderate", lumbar="low"),
      pat="vertical_pull", diff=5, rom="high",
      ortho="moderate", valsalva="moderate", metab="moderate", laxity="high",
      gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury", "carpal_tunnel",
              "cervical_injury", "hypermobility"],
      caut=["hypertension", "obesity", "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement"],
      why="Dominada tras nuca: mismo problema que el press tras nuca (0086). "
           "Rotacion externa maxima con abduccion completa mas proyeccion "
           "cervical. laxity high, hipermovilidad y lesion cervical como "
           "contraindicaciones duras. Es la dominada menos recomendable."),

    E("0672", "reverse dip", "hanging", grip="firm", bal="moderate",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", metab="moderate",
      laxity="moderate", gripdur="high", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypertension", "obesity",
            "hypermobility"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement"],
      why="Fondos en paralelas: E1 no resolvio la postura. Es el peldano "
           "superior de la familia del fondo - los once fondos en banco son "
           "sus regresiones. Cadena completa lista para E4."),

    E("0677", "ring dips", "hanging", grip="hanging_bodyweight", bal="high",
      stress=js(sh="high", el="high", wr="high"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="high", laxity="high", gripdur="high", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "wrist_injury", "carpal_tunnel", "tendinitis_elbow",
              "hypermobility", "limited_balance"],
      caut=["hypertension", "cardiac", "obesity"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "knee_replacement"],
      why="Fondos en anillas: superficie inestable con todo el peso corporal. "
           "laxity high - las anillas permiten que el hombro se vaya a rangos "
           "que una barra fija impide. difficulty 5, techo de la familia."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 11: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
