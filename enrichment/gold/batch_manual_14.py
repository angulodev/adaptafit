#!/usr/bin/env python3
"""Lote 14 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0389", "dumbbell seated bench extension", "seated", grip="firm", oh=True,
      stress=js(sh="high", el="high", cerv="low", wr="moderate"),
      pat="isolation", diff=2, rom="high",
      ortho="low", valsalva="low", metab="low", laxity="moderate",
      gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "tendinitis_elbow", "limited_grip"],
      caut=["cervical_injury", "hypertension", "wrist_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="Press frances sentado con respaldo: version estable de 1747 (sobre "
           "pelota). Sin el componente de equilibrio, cuatro contraindicaciones "
           "menos. Ejemplo limpio del efecto aislado de la superficie."),

    E("0368", "dumbbell over bench revers wrist curl", "seated", grip="firm",
      stress=js(wr="moderate", el="moderate"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", metab="none", gripdur="high", temp="none",
      contra=["wrist_injury", "carpal_tunnel", "rheumatoid_arthritis"],
      caut=["tendinitis_elbow", "osteoarthritis", "limited_grip"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "shoulder_impingement", "dysautonomia", "chronic_fatigue"],
      why="DECIMA entrada de la familia flexion/extension de muneca. "
           "Version invertida de 0369, antebrazos en banco."),

    E("1736", "dumbbell one arm french press on exercise ball", "seated",
      bal="moderate", grip="firm", oh=True, lat="unilateral",
      stress=js(sh="high", el="high", lumbar="moderate", wr="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", change="low", valsalva="low", iso="moderate",
      metab="low", laxity="moderate", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "tendinitis_elbow", "limited_balance", "vertigo"],
      caut=["lumbar_pain", "hypertension", "hypermobility", "limited_grip",
            "multiple_sclerosis", "dysautonomia"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement"],
      why="Version unilateral de 1747 sobre pelota. Con mancuerna en vez de "
           "barra EZ, limited_grip baja de contraindicacion a precaucion."),

    E("0320", "dumbbell incline hammer curl", "bench_incline", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", metab="low", laxity="moderate", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Version martillo del curl inclinado. Agarre neutro: muneca low, "
           "frente al supinado (0315/0317/0318). Sexto caso del eje de agarre."),

    E("1661", "dumbbell lying supine biceps curl", "bench_supine", grip="firm",
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
      why="DUPLICADO de 0350 y 1662. El curl acostado ya tiene tres entradas."),

    E("1289", "dumbbell one arm incline chest press", "bench_incline",
      grip="firm", lat="unilateral",
      stress=js(sh="high", el="moderate", wr="low", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="low", metab="low",
      gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["elbow_injury", "hypermobility", "si_joint_pain", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="DUPLICADO de 1281. Press inclinado unilateral en banco firme."),

    E("3201", "quarter sit-up", "supine", floor=True,
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
      why="Otro miembro del grupo de abdominales con texto identico. "
           "El nombre promete un cuarto de recorrido, pero el texto describe "
           "45 grados igual que janda sit-up y 3/4 sit-up. Cola de E3."),

    E("0006", "alternate heel touchers", "supine", floor=True,
      flex="moderate", rot="moderate",
      stress=js(lumbar="moderate", cerv="low", hip="low"),
      lat="alternating", pat="core_rotation", diff=1, rom="low",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="low", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "hernia_abdominal", "postpartum",
            "osteoporosis"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury", "cervical_injury",
            "dysautonomia", "elderly_65plus"],
      why="HALLAZGO: primer abdominal con rotacion donde los brazos van a los "
           "costados, NO detras de la cabeza. cervical baja de high a low. "
           "Es la regresion correcta de oblique crunches (0635) y de toda la "
           "familia de rotacion en suelo. Cuarto abdominal apto con lesion "
           "cervical, junto a pelvic tilt, dead bug y curl-up."),

    E("0033", "barbell decline bench press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "hypertension", "dysautonomia",
            "vertigo", "migraine", "hypermobility"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "no_overhead"],
      why="Press declinado con barra. El codo pegado al cuerpo reduce la "
           "abduccion respecto del agarre ancho (0036), su par directo."),

    E("0036", "barbell decline wide-grip press", "bench_supine", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "glaucoma",
              "retinal_detachment_risk", "hypermobility",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "wrist_injury", "hypertension", "dysautonomia",
            "vertigo", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "no_overhead"],
      why="Par de 0033 con agarre ancho: 'elbows out to the sides' aumenta la "
           "abduccion. laxity sube a high e hipermovilidad pasa a "
           "contraindicacion. Confirma el patron de 0122 vs 0055."),

    E("0473", "hanging pike", "hanging", grip="hanging_bodyweight",
      flex="high", stress=js(sh="high", el="moderate", wr="high",
      lumbar="high", hip="high"),
      pat="core_flexion", diff=5, rom="high",
      ortho="moderate", change="moderate", valsalva="high", iso="high",
      metab="high", laxity="moderate", pelvic="high", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "hypermobility", "chronic_fatigue",
            "obesity"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement", "hip_replacement"],
      why="Piernas rectas hasta la barra colgado: maxima flexion de cadera con "
           "traccion del psoas sobre la lumbar. difficulty 5. "
           "Progresion de hanging leg raise (0472)."),

    E("0259", "close-grip push-up", "plank", floor=True, bal="low",
      stress=js(sh="moderate", el="high", wr="high", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="moderate", pelvic="low", gripdur="low", temp="moderate",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "elbow_injury", "tendinitis_elbow"],
      caut=["shoulder_impingement", "rheumatoid_arthritis",
            "pregnancy_2nd", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "limited_balance", "no_overhead"],
      why="DUPLICADO funcional de 0283 (diamond push-up). Manos juntas: "
           "descarga hombro, carga codo y muneca. Su regresion elevada es 0490."),

    E("0348", "dumbbell lying rear lateral raise", "bench_prone", grip="firm",
      stress=js(sh="moderate", el="low", cerv="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="none", change="moderate", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "hypermobility",
            "cervical_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="DUPLICADO funcional de 0326. Deltoides posterior con pecho apoyado: "
           "cero carga lumbar, util para postura sin cargar la columna."),

    E("0450", "ez barbell jm bench press", "bench_supine", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=4, rom="moderate",
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
      why="Version con barra EZ de 0052. El angulo de la EZ reduce la "
           "desviacion cubital: muneca moderate en vez de high. Regresion "
           "correcta para muneca sensible."),

    E("0472", "hanging leg raise", "hanging", grip="hanging_bodyweight",
      flex="moderate", stress=js(sh="high", el="moderate", wr="high",
      lumbar="high", hip="high"),
      pat="core_flexion", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "lumbar_disc",
              "sciatica", "hernia_abdominal", "recent_abdominal_surgery",
              "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "hypermobility", "obesity", "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "knee_replacement", "hip_replacement"],
      why="Elevacion de piernas colgado. Su cadena de regresion queda completa: "
           "hanging pike (5) -> hanging leg raise (4) -> captains chair (3) -> "
           "lying leg raise (2) -> seated leg raise (2). Cinco niveles del "
           "mismo patron, con accesibilidad decreciente."),

    E("0488", "hyperextension (on bench)", "bench_prone", grip="none",
      ext="high", flex="moderate",
      stress=js(lumbar="high", hip="moderate", cerv="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      iso="moderate", metab="low", pelvic="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "osteoporosis",
              "glaucoma", "retinal_detachment_risk",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "si_joint_pain", "sciatica", "hypertension",
            "dysautonomia", "hypermobility", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel"],
      why="DUPLICADO de 0489. La unica diferencia textual es 'muslos' vs "
           "'caderas' sobre el pad - que en la practica si cambia el brazo de "
           "palanca, pero el resto del texto es identico."),

    E("0697", "self assisted inverse leg curl", "supine", floor=True,
      flex="low", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="core_flexion", diff=1, rom="moderate",
      ortho="none", change="high", valsalva="low", metab="low",
      pelvic="moderate", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_disc", "sciatica", "hip_pain", "hernia_abdominal",
            "postpartum"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "shoulder_impingement", "no_overhead",
            "limited_grip", "wrist_injury", "carpal_tunnel", "cervical_injury",
            "dysautonomia", "elderly_65plus"],
      why="El nombre dice curl femoral pero el texto describe rodillas al "
           "pecho: es core, no isquiotibiales. Error de nomenclatura del "
           "dataset. Clasificado por el texto - difficulty 1, muy accesible."),

    E("0863", "dumbbell lying external shoulder rotation", "side_lying",
      grip="firm", lat="unilateral",
      stress=js(sh="moderate", el="low", wr="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="moderate", metab="none", laxity="moderate",
      gripdur="moderate", temp="none",
      contra=["cannot_lie_on_side", "cannot_transfer_to_bench", "rotator_cuff"],
      caut=["shoulder_impingement", "limited_grip", "hypermobility",
            "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "chronic_fatigue", "elderly_65plus"],
      why="CORRECCION A E1: lo marco supine y core_rotation, pero dice 'lie on "
           "your side' y es rotacion de HOMBRO, no de tronco. Es side_lying + "
           "isolation. Ejercicio clave de rehabilitacion del manguito rotador: "
           "el codo pegado al cuerpo evita la posicion de pinzamiento. "
           "Par acostado de 0399 (sentado)."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 14: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
