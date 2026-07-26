#!/usr/bin/env python3
"""
Lote 47 — ULTIMO de la clasificacion manual. 14 ejercicios. Taxonomia v1.2.

Reutiliza las constantes de perfil de sentadilla con barra definidas en el
lote 46, porque cinco de estos catorce vuelven a caer en el mismo nucleo.
"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js
from batch_manual_46 import SQUAT_CONTRA, SQUAT_CAUT, SQUAT_SAFE

# Perfil compartido por los curls de pie con barra: cambia el implemento y el
# agarre, no la mecanica.
CURL_SAFE = ["no_overhead", "cannot_get_on_floor", "cannot_kneel",
             "cannot_lie_supine", "cannot_lie_prone",
             "cannot_transfer_to_bench", "knee_injury", "knee_pain",
             "knee_replacement", "hip_replacement", "ankle_injury",
             "plantar_fasciitis", "sciatica", "lumbar_disc",
             "shoulder_impingement", "rotator_cuff", "osteoporosis"]


BATCH = [
    E("0106", "barbell standing close grip curl", "standing", standing=True,
      bal="low", grip="firm", ext="low",
      stress=js(el="moderate", wr="high", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "wrist_injury",
              "carpal_tunnel", "tendinitis_elbow"],
      caut=["elbow_injury", "lumbar_pain", "rheumatoid_arthritis",
            "osteoarthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=CURL_SAFE,
      why="Agarre cerrado y supino sobre barra recta: la muneca queda en "
           "desviacion cubital forzada bajo carga, el irritante clasico de "
           "esta variante. Unico curl del lote con wrist high junto a 2407, y "
           "por eso carpal_tunnel pasa a contraindicacion."),

    E("2810", "barbell split squat v. 2", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", lat="alternating",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                sh="moderate", wr="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA,
      caut=SQUAT_CAUT + ["si_joint_pain", "shoulder_impingement",
                         "rotator_cuff", "wrist_injury", "carpal_tunnel"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="Zancada con barra en la espalda, alternando pierna. Se clasifica "
           "como lunge y no squat pese a lo que dice E1: el texto manda dar "
           "un paso amplio al frente, que es el patron de zancada. Marca "
           "'v. 2', duplicado de 0099 salvo por la alternancia."),

    E("0099", "barbell single leg split squat", "standing", standing=True,
      bal="high", grip="firm", axial="high", lat="unilateral",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                sh="moderate", wr="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=SQUAT_CONTRA + ["visual_impairment"],
      caut=SQUAT_CAUT + ["si_joint_pain", "shoulder_impingement",
                         "rotator_cuff", "wrist_injury", "carpal_tunnel",
                         "multiple_sclerosis"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="Igual que 2810 pero completando todas las repeticiones de un lado "
           "antes de cambiar, con la pierna trasera recta. Eso sube el "
           "equilibrio a high y agrega visual_impairment. El par 2810/0099 "
           "mide lo que cuesta no alternar: una contraindicacion mas."),

    E("0109", "barbell standing overhead triceps extension", "standing",
      standing=True, bal="low", grip="firm", oh=True, axial="moderate",
      ext="moderate",
      stress=js(sh="high", el="high", wr="moderate", cerv="moderate",
                lumbar="moderate"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="none", valsalva="moderate", iso="moderate",
      metab="low", laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "elbow_injury", "tendinitis_elbow", "limited_grip"],
      caut=["cervical_injury", "neck_pain", "lumbar_pain", "lumbar_disc",
            "wrist_injury", "carpal_tunnel", "hypermobility", "hypertension",
            "osteoporosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica"],
      why="Barra por detras de la cabeza con los brazos sobre ella: hombro y "
           "codo en high a la vez, combinacion que ningun otro aislado del "
           "catalogo tiene. La barra pasa cerca de la columna cervical, de "
           "ahi cerv moderate. Nueve contraindicaciones para un ejercicio de "
           "triceps."),

    E("0637", "olympic barbell triceps extension", "standing", standing=True,
      bal="low", grip="firm", oh=True, axial="moderate", ext="moderate",
      stress=js(sh="high", el="high", wr="moderate", cerv="moderate",
                lumbar="moderate"),
      pat="isolation", diff=3, rom="high",
      ortho="high", change="none", valsalva="moderate", iso="moderate",
      metab="low", laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "elbow_injury", "tendinitis_elbow", "limited_grip"],
      caut=["cervical_injury", "neck_pain", "lumbar_pain", "lumbar_disc",
            "wrist_injury", "carpal_tunnel", "hypermobility", "hypertension",
            "osteoporosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica"],
      why="Duplicado de 0109. Los dos textos describen el mismo gesto casi "
           "palabra por palabra; la unica diferencia es que la barra olimpica "
           "pesa 20 kg vacia, lo que cambia la carga minima pero ninguna "
           "contraindicacion."),

    E("0110", "barbell standing reverse grip curl", "standing", standing=True,
      bal="low", grip="firm", ext="low",
      stress=js(el="moderate", wr="moderate", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "wrist_injury",
              "tendinitis_elbow"],
      caut=["elbow_injury", "carpal_tunnel", "lumbar_pain",
            "rheumatoid_arthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=CURL_SAFE,
      why="Tercer curl del proyecto cuyo nombre dice agarre invertido y cuyo "
           "texto describe agarre supino, tras 0451 y 0113. Se clasifica el "
           "texto: curl con barra normal."),

    E("1461", "barbell full squat (back pov)", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", sh="moderate",
                wr="moderate", ank="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA,
      caut=SQUAT_CAUT + ["si_joint_pain", "shoulder_impingement",
                         "rotator_cuff", "wrist_injury", "carpal_tunnel"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="Sentadilla trasera estandar, identica a 1436 y 0063. 'back pov' no "
           "es una variante del ejercicio: es el angulo de camara del video "
           "de origen."),

    E("1462", "barbell full squat (side pov)", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", sh="moderate",
                wr="moderate", ank="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA,
      caut=SQUAT_CAUT + ["si_joint_pain", "shoulder_impingement",
                         "rotator_cuff", "wrist_injury", "carpal_tunnel"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="El duplicado mas limpio de todo el catalogo: el texto de 1462 es "
           "identico caracter por caracter al de 1461. Dos fichas para el "
           "mismo ejercicio filmado desde otro angulo. Si algo justifica la "
           "deduplicacion en E4, es este par."),

    E("0097", "barbell side split squat v. 2", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", lat="alternating",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                sh="moderate", wr="moderate"),
      pat="lunge", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA,
      caut=SQUAT_CAUT + ["si_joint_pain", "hypermobility",
                         "shoulder_impingement", "rotator_cuff",
                         "wrist_injury", "carpal_tunnel"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="Zancada lateral con barra. A diferencia de 0098, que el texto "
           "describia como sumo estatico, aqui si hay paso lateral real, asi "
           "que el patron es lunge. La apertura de cadera bajo carga axial "
           "alta mantiene hypermobility en cautions."),

    E("1629", "barbell standing wide grip biceps curl", "standing",
      standing=True, bal="low", grip="firm", ext="low",
      stress=js(el="moderate", wr="high", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "wrist_injury",
              "tendinitis_elbow"],
      caut=["elbow_injury", "carpal_tunnel", "shoulder_pain", "lumbar_pain",
            "rheumatoid_arthritis", "osteoarthritis", "hypermobility",
            "hypertension", "dysautonomia", "elderly_65plus"],
      safe=CURL_SAFE,
      why="Agarre ancho y supino sobre barra recta. Junto con 0106 (agarre "
           "cerrado) delimitan el rango: cualquier desviacion del ancho "
           "natural sobre una barra fija fuerza la muneca, sea hacia dentro "
           "o hacia fuera. Los dos extremos dan wrist high."),

    E("2404", "ez-bar biceps curl (with arm blaster)", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="moderate", wr="moderate", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip",
              "tendinitis_elbow"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "shoulder_pain",
            "rheumatoid_arthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=CURL_SAFE,
      why="El curl con barra mas accesible del catalogo: cuatro "
           "contraindicaciones. La barra EZ permite semipronacion, que quita "
           "la torsion forzada de muneca, y el arm blaster fija el humero y "
           "elimina el balanceo lumbar. Sustituto por defecto en E4 para "
           "cualquier curl con barra recta."),

    E("2407", "barbell biceps curl (with arm blaster)", "standing",
      standing=True, bal="low", grip="firm",
      stress=js(el="moderate", wr="high", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "wrist_injury",
              "carpal_tunnel", "tendinitis_elbow"],
      caut=["elbow_injury", "shoulder_pain", "lumbar_pain",
            "rheumatoid_arthritis", "hypermobility", "hypertension",
            "dysautonomia", "elderly_65plus"],
      safe=CURL_SAFE,
      why="Mismo accesorio que 2404 pero con barra recta. El par aisla el "
           "efecto del implemento con todo lo demas constante: la barra recta "
           "sube la muneca de moderate a high y agrega dos "
           "contraindicaciones. Es la demostracion mas limpia de la escala de "
           "implemento que veniamos aplicando desde el lote 12."),

    E("2741", "ez-barbell standing wide grip biceps curl", "standing",
      standing=True, bal="low", grip="firm", ext="low",
      stress=js(el="moderate", wr="moderate", lumbar="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip",
              "tendinitis_elbow"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "shoulder_pain",
            "lumbar_pain", "rheumatoid_arthritis", "hypermobility",
            "hypertension", "dysautonomia", "elderly_65plus"],
      safe=CURL_SAFE,
      why="Version EZ de 1629. Mismo agarre ancho, misma mecanica, pero la "
           "curvatura de la barra baja la muneca de high a moderate y "
           "wrist_injury sale de contraindicaciones. Tercer par del lote que "
           "confirma la escala de implemento."),

    E("2798", "barbell squat jump step rear lunge", "standing", standing=True,
      bal="high", grip="firm", axial="high", impact="high",
      lat="alternating",
      stress=js(knee="high", hip="high", lumbar="high", ank="high",
                sh="moderate", wr="moderate", cerv="moderate"),
      pat="squat", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="high", pelvic="high", gripdur="high", temp="high",
      contra=SQUAT_CONTRA + ["visual_impairment", "si_joint_pain",
                             "plantar_fasciitis"],
      caut=SQUAT_CAUT + ["multiple_sclerosis", "hypermobility",
                         "shoulder_impingement", "rotator_cuff",
                         "wrist_injury", "carpal_tunnel", "chronic_fatigue",
                         "fibromyalgia"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="Salto pliometrico con barra cargada en la espalda, aterrizaje y "
           "zancada inversa encadenada. Unico ejercicio del catalogo que "
           "combina impact high con axial high y valsalva high. Nota sobre "
           "osteoporosis: se mantiene en cautions por coherencia con el "
           "contrato de la capa C, que advierte pero nunca excluye en "
           "silencio — aunque en este caso concreto la advertencia se queda "
           "corta y conviene revisarlo al definir la severidad de los avisos."),
]


CONFIDENCE_OVERRIDES = {
    "0110": 0.70,  # nombre reverse grip, texto describe agarre supino
    "1461": 0.85,  # "pov" es angulo de camara, no variante
    "1462": 0.85,  # texto identico a 1461
    "0637": 0.85,  # duplicado de 0109
    "2810": 0.85,  # marca v. 2
    "0097": 0.85,  # marca v. 2
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
    print(f"lote 47: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
