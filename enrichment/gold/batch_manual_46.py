#!/usr/bin/env python3
"""Lote 46 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


# Perfil compartido por las sentadillas con barra cargada. Todas comparten el
# mismo nucleo de riesgo (axial high + valsalva high + rodilla/cadera/lumbar
# high); lo que las diferencia es donde se apoya la barra.
SQUAT_CAUT = ["osteoporosis", "hypertension", "cardiac", "hernia_abdominal",
              "glaucoma", "retinal_detachment_risk", "osteoarthritis",
              "pelvic_floor_dysfunction", "postpartum", "varicose_veins",
              "dysautonomia", "vertigo", "elderly_65plus", "obesity",
              "pregnancy_2nd", "pregnancy_3rd"]
SQUAT_SAFE = ["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
              "cannot_lie_prone", "cannot_transfer_to_bench"]
SQUAT_CONTRA = ["cannot_stand", "wheelchair", "limited_balance",
                "knee_injury", "knee_replacement", "knee_pain",
                "hip_replacement", "hip_pain", "lumbar_disc", "lumbar_pain",
                "sciatica", "ankle_injury", "limited_grip"]


BATCH = [
    E("0023", "barbell alternate biceps curl", "standing", standing=True,
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
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="El texto es fisicamente imposible: 'hold a barbell in each hand' y "
           "despues alternar brazos. Una barra no se sostiene con una mano ni "
           "se alterna. Se clasifica como curl con barra bilateral, que es la "
           "unica lectura ejecutable. confidence 0,60."),

    E("0068", "barbell one leg squat", "standing", standing=True, bal="high",
      sl=True, grip="firm", axial="high", lat="unilateral",
      stress=js(knee="high", hip="high", lumbar="high", ank="high",
                sh="moderate", wr="moderate"),
      pat="squat", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=SQUAT_CONTRA + ["visual_impairment", "plantar_fasciitis",
                             "shoulder_impingement", "rotator_cuff"],
      caut=SQUAT_CAUT + ["si_joint_pain", "hypermobility", "wrist_injury",
                         "multiple_sclerosis"],
      safe=SQUAT_SAFE + ["no_overhead"],
      why="Pistol con barra cargada en la espalda. Diecisiete "
           "contraindicaciones y difficulty 5: combina lo peor de 1759 "
           "(unipodal, equilibrio, rango) con lo peor de 0101 (axial high, "
           "valsalva high). No hay perfil con ninguna restriccion que lo "
           "tolere."),

    E("1369", "band two legs calf raise - (band under both legs) v. 2",
      "standing", standing=True, bal="moderate", grip="light",
      stress=js(ank="high", knee="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury",
              "plantar_fasciitis", "limited_grip"],
      caut=["limited_balance", "knee_pain", "osteoarthritis", "dysautonomia",
            "vertigo", "elderly_65plus", "varicose_veins", "obesity",
            "multiple_sclerosis"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "shoulder_impingement",
            "rotator_cuff", "elbow_injury", "carpal_tunnel", "lumbar_disc",
            "sciatica", "hip_replacement", "knee_replacement",
            "osteoporosis"],
      why="Septima elevacion de talon del catalogo. Se ubica en el medio del "
           "espectro: sin apoyo de pared como 1382, pero sin carga axial ni "
           "riesgo de borde como 0111 o 1490. La banda ocupa las dos manos, "
           "por eso limited_grip pasa a contraindicacion y queda fuera de "
           "one_arm_only."),

    E("0051", "barbell jefferson squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", rot="moderate",
      lat="alternating",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                sh="moderate", wr="moderate", el="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=SQUAT_CONTRA + ["si_joint_pain"],
      caut=SQUAT_CAUT + ["shoulder_impingement", "wrist_injury"],
      safe=SQUAT_SAFE + ["no_overhead", "rotator_cuff", "elbow_injury",
                         "carpal_tunnel"],
      why="Unica sentadilla del catalogo con carga asimetrica: pies "
           "escalonados y barra por delante, lo que genera torsion mantenida "
           "bajo carga axial alta. Por eso spinal_rotation moderate y "
           "si_joint_pain sube a contraindicacion, cosa que ninguna otra "
           "sentadilla con barra tiene. El nombre sugiere ademas montar a "
           "horcajadas sobre la barra, que el texto no describe."),

    E("0069", "barbell overhead squat", "standing", standing=True, bal="high",
      grip="firm", oh=True, axial="high",
      stress=js(knee="high", hip="high", lumbar="high", sh="high", ank="high",
                wr="high", cerv="moderate", el="moderate"),
      pat="squat", diff=5, rom="high",
      ortho="high", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="high", pelvic="high", gripdur="high",
      temp="moderate",
      contra=SQUAT_CONTRA + ["no_overhead", "shoulder_impingement",
                             "rotator_cuff", "shoulder_pain", "wrist_injury"],
      caut=SQUAT_CAUT + ["cervical_injury", "neck_pain", "hypermobility",
                         "carpal_tunnel", "si_joint_pain"],
      safe=SQUAT_SAFE,
      why="Dieciocho contraindicaciones y solo cinco safe_for, todas de posturas que el ejercicio no usa. Las ocho articulaciones quedan en moderate o high — algo que solo comparte con los levantamientos olimpicos (power clean, squat jerk, snatch). La diferencia es que aquellos son explosivos y este es lento y sostenido: sostener una barra sobre la cabeza en el fondo de una sentadilla profunda no tiene ninguna via de adaptacion."),

    E("0127", "barbell zercher squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", flex="low",
      stress=js(knee="high", hip="high", lumbar="high", el="high",
                sh="moderate", ank="moderate", wr="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=SQUAT_CONTRA + ["elbow_injury", "tendinitis_elbow"],
      caut=SQUAT_CAUT + ["si_joint_pain", "rheumatoid_arthritis",
                         "shoulder_impingement"],
      safe=SQUAT_SAFE + ["no_overhead", "rotator_cuff", "wrist_injury",
                         "carpal_tunnel"],
      why="La barra descansa en el pliegue de los codos. Unico squat del "
           "catalogo con elbow high, y a la vez el unico que es safe_for de "
           "wrist_injury y carpal_tunnel, porque la muneca no soporta nada. "
           "Es un intercambio limpio: quien tiene la muneca comprometida "
           "puede hacer zercher y no puede hacer front squat."),

    E("1545", "barbell full zercher squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high", flex="low",
      stress=js(knee="high", hip="high", lumbar="high", el="high",
                sh="moderate", ank="moderate", wr="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="moderate",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=SQUAT_CONTRA + ["elbow_injury", "tendinitis_elbow"],
      caut=SQUAT_CAUT + ["si_joint_pain", "rheumatoid_arthritis",
                         "shoulder_impingement"],
      safe=SQUAT_SAFE + ["no_overhead", "rotator_cuff", "wrist_injury",
                         "carpal_tunnel"],
      why="Duplicado de 0127. Los dos textos son practicamente identicos "
           "palabra por palabra; el unico anadido de 'full' es bajar hasta "
           "los muslos paralelos, que 0127 tambien describe. Clasificacion "
           "identica a proposito para que E4 los colapse."),

    E("1001", "band single leg split squat", "standing", standing=True,
      bal="high", grip="none", lat="unilateral",
      stress=js(knee="high", hip="high", ank="moderate", lumbar="moderate"),
      pat="squat", diff=3, rom="high",
      ortho="high", change="high", valsalva="low", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_balance", "knee_injury",
              "knee_replacement", "knee_pain", "hip_replacement", "hip_pain",
              "ankle_injury"],
      caut=["lumbar_pain", "lumbar_disc", "sciatica", "si_joint_pain",
            "plantar_fasciitis", "osteoarthritis", "osteoporosis",
            "hypermobility", "dysautonomia", "vertigo", "elderly_65plus",
            "obesity", "multiple_sclerosis", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "limited_grip", "one_arm_only",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel"],
      why="Los dos pies quedan en el suelo, asi que single_leg_support es "
           "False pese al nombre; el equilibrio sigue alto por la base "
           "estrecha. Sin manos involucradas entra en one_arm_only y "
           "limited_grip — es la sentadilla mas accesible para tren superior "
           "de todo el lote, y la unica sin barra."),

    E("0024", "barbell bench front squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", sh="high", wr="high",
                ank="moderate", el="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA + ["wrist_injury", "carpal_tunnel",
                             "shoulder_impingement", "rotator_cuff"],
      caut=SQUAT_CAUT + ["si_joint_pain", "elbow_injury", "shoulder_pain"],
      safe=SQUAT_SAFE + ["no_overhead"],
      why="El nombre menciona un banco que el texto no usa en ningun momento. "
           "Se clasifica como front squat normal. La posicion de rack frontal "
           "exige extension de muneca extrema con carga encima: wrist y "
           "shoulder en high, y carpal_tunnel pasa a contraindicacion, cosa "
           "que la sentadilla trasera no hace."),

    E("0029", "barbell clean-grip front squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", sh="high", wr="high",
                ank="moderate", el="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA + ["wrist_injury", "carpal_tunnel",
                             "shoulder_impingement", "rotator_cuff"],
      caut=SQUAT_CAUT + ["si_joint_pain", "elbow_injury", "shoulder_pain"],
      safe=SQUAT_SAFE + ["no_overhead"],
      why="Front squat con agarre de cargada. Duplicado funcional de 0024 y "
           "0039: los tres textos describen la misma barra apoyada en el "
           "pecho con los codos al frente. El agarre de cargada es el que "
           "mas extension de muneca exige de los tres, pero la diferencia no "
           "alcanza para cambiar ninguna contraindicacion."),

    E("0039", "barbell front chest squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", sh="high", wr="high",
                ank="moderate", el="moderate", cerv="low"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA + ["wrist_injury", "carpal_tunnel",
                             "shoulder_impingement", "rotator_cuff"],
      caut=SQUAT_CAUT + ["si_joint_pain", "elbow_injury", "shoulder_pain"],
      safe=SQUAT_SAFE + ["no_overhead"],
      why="Tercera ficha del mismo front squat, tras 0024 y 0029. El catalogo "
           "tiene tres entradas distintas para un ejercicio que no varia en "
           "nada relevante para accesibilidad."),

    E("0063", "barbell narrow stance squat", "standing", standing=True,
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
      why="El nombre dice postura estrecha y el texto dice ancho de hombros, "
           "que es la postura estandar. Se clasifica el texto: queda como una "
           "sentadilla trasera comun, identica a 1436."),

    E("0098", "barbell side split squat", "standing", standing=True,
      bal="moderate", grip="firm", axial="high",
      stress=js(knee="high", hip="high", lumbar="high", ank="moderate",
                sh="moderate", wr="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="high", iso="low", metab="high",
      laxity="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=SQUAT_CONTRA,
      caut=SQUAT_CAUT + ["si_joint_pain", "hypermobility",
                         "shoulder_impingement", "rotator_cuff",
                         "wrist_injury", "carpal_tunnel"],
      safe=SQUAT_SAFE + ["no_overhead", "elbow_injury"],
      why="El nombre promete una sentadilla lateral escalonada; el texto "
           "describe una sentadilla sumo con pies anchos y rodillas hacia "
           "fuera. Se clasifica el texto. La apertura de cadera bajo carga "
           "justifica hypermobility en cautions respecto de la sentadilla "
           "trasera normal."),

    E("0113", "barbell standing wide-grip curl", "standing", standing=True,
      bal="low", grip="firm", ext="low",
      stress=js(el="high", wr="high", lumbar="moderate", sh="low"),
      pat="isolation", diff=3, rom="moderate",
      ortho="high", change="none", valsalva="moderate", iso="low",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "wrist_injury",
              "carpal_tunnel", "tendinitis_elbow", "elbow_injury"],
      caut=["shoulder_pain", "lumbar_pain", "rheumatoid_arthritis",
            "osteoarthritis", "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="El texto dice palmas hacia fuera del cuerpo, o sea agarre prono: "
           "es un curl invertido, no el curl ancho que anuncia el nombre. "
           "Perfil identico a 0636 del lote 44 — barra recta mas pronacion "
           "pone codo y muneca en high."),

    E("0986", "band one arm overhead biceps curl", "standing", standing=True,
      bal="low", grip="light", oh=True, lat="unilateral",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="high", metab="low",
      laxity="moderate", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "no_overhead",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["shoulder_pain", "cervical_injury", "neck_pain", "lumbar_pain",
            "elbow_injury", "tendinitis_elbow", "hypermobility",
            "hypertension", "osteoporosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "one_arm_only",
            "knee_injury", "knee_pain", "knee_replacement", "hip_replacement",
            "ankle_injury", "plantar_fasciitis", "sciatica", "lumbar_disc",
            "wrist_injury", "carpal_tunnel"],
      why="El brazo se mantiene extendido sobre la cabeza durante toda la "
           "serie mientras solo se mueve el antebrazo: sustained_isometric "
           "high por el hombro, igual que 0998. La banda bajo el pie deja la "
           "otra mano libre, asi que entra en one_arm_only pese a ser "
           "overhead."),

    E("0987", "band one arm single leg split squat", "standing",
      standing=True, bal="moderate", sl=True, grip="light", lat="unilateral",
      stress=js(knee="high", hip="high", ank="moderate", lumbar="moderate"),
      pat="squat", diff=4, rom="high",
      ortho="high", change="high", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="moderate",
      gripdur="moderate", temp="moderate",
      contra=["cannot_stand", "wheelchair", "knee_injury", "knee_replacement",
              "knee_pain", "hip_replacement", "hip_pain", "ankle_injury"],
      caut=["limited_balance", "visual_impairment", "limited_grip",
            "lumbar_pain", "lumbar_disc", "sciatica", "si_joint_pain",
            "plantar_fasciitis", "osteoarthritis", "osteoporosis",
            "hypermobility", "dysautonomia", "vertigo", "elderly_65plus",
            "obesity", "multiple_sclerosis", "pregnancy_2nd",
            "pregnancy_3rd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "one_arm_only",
            "shoulder_impingement", "rotator_cuff", "elbow_injury",
            "wrist_injury", "carpal_tunnel"],
      why="Bulgara con banda y una mano en un apoyo. Aplica la regla del "
           "apoyo: pese a ser unipodal con pie trasero elevado, el agarre "
           "baja el balance a moderate y limited_balance queda en cautions. "
           "El apoyo se toma con una sola mano, asi que sigue siendo apto "
           "para one_arm_only — la diferencia con 0356, donde el apoyo "
           "consumia la segunda mano."),

    E("1436", "barbell high bar squat", "standing", standing=True,
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
      why="El par 1435/1436 es la comparacion mas util del lote: misma "
           "sentadilla, misma carga, misma profundidad. La barra alta apoya "
           "en los trapecios y deja el hombro en moderate; la barra baja "
           "exige rotacion externa extrema y lo pone en high. Resultado: "
           "trece contraindicaciones contra diecisiete. Cuatro condiciones de "
           "hombro y muneca dependen unicamente de donde se apoya la barra."),

    E("2414", "barbell standing concentration curl", "standing",
      standing=True, bal="low", grip="firm", lat="unilateral",
      stress=js(el="moderate", wr="moderate", sh="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="high", change="none", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="none", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip",
              "tendinitis_elbow"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "hypermobility", "hypertension", "dysautonomia",
            "elderly_65plus"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone",
            "cannot_transfer_to_bench", "knee_injury", "knee_pain",
            "knee_replacement", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "sciatica", "lumbar_disc",
            "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      why="Segundo texto imposible del lote: sostener una barra con una sola "
           "mano. Ademas manda apoyar la mano contraria en el muslo, asi que "
           "por D-020 queda fuera de one_arm_only — el mismo caso que 0421 y "
           "0418. confidence 0,60."),
]


CONFIDENCE_OVERRIDES = {
    "0023": 0.60,  # "una barra en cada mano" y alternar: imposible
    "2414": 0.60,  # barra sostenida con una sola mano: imposible
    "0063": 0.70,  # nombre postura estrecha, texto ancho de hombros
    "0113": 0.70,  # nombre wide-grip curl, texto describe agarre prono
    "0024": 0.75,  # "bench" en el nombre, ausente del texto
    "0051": 0.75,  # jefferson normalmente monta a horcajadas sobre la barra
    "0098": 0.75,  # nombre side split squat, texto describe sumo
    "0039": 0.80,  # tercer duplicado del front squat
    "1545": 0.85,  # duplicado de 0127
    "1369": 0.85,  # marca v. 2
    "0987": 0.85,  # regla del apoyo aplicada sobre unipodal elevado
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
    print(f"lote 46: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
