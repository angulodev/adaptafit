#!/usr/bin/env python3
"""Lote 2 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js  # reutiliza los helpers


BATCH = [
    E("0815", "triceps dips floor", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia"],
      why="Fondo desde silla con piernas extendidas. Mismo substitute_group que "
           "0814, 3287 y 1399: son el mismo movimiento con nombres distintos."),

    E("1494", "butterfly yoga pose", "seated", floor=True,
      stress=js(hip="moderate", knee="moderate", lumbar="low"),
      pat="isolation", diff=1, rom="high",
      ortho="low", change="high", metab="none", laxity="high", temp="none",
      contra=["cannot_get_on_floor", "hip_replacement", "hip_pain"],
      caut=["knee_pain", "si_joint_pain", "hypermobility", "osteoarthritis",
            "pregnancy_3rd", "elderly_65plus"],
      safe=["cannot_stand", "shoulder_impingement", "no_overhead", "limited_grip",
            "wrist_injury", "dysautonomia", "chronic_fatigue", "hypertension"],
      why="joint_laxity_risk alto: rotacion externa maxima de cadera sin carga. "
           "En hipermovilidad es donde mas facil se pasa de rango. "
           "Contraindicado con protesis de cadera por la posicion."),

    E("2397", "dumbbell scott press", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="CORRECCION A E1: no marco overhead_position, pero 'press upward until "
           "arms are fully extended' desde altura de hombro es sobre la cabeza. "
           "Mismo substitute_group que 0405 y 0438."),

    E("3420", "v-sit on floor", "seated", floor=True, bal="moderate",
      flex="high", stress=js(lumbar="high", hip="high", cerv="low"),
      pat="core_flexion", diff=4, rom="high",
      ortho="low", change="high", valsalva="moderate", iso="high",
      metab="moderate", pelvic="high", temp="moderate",
      contra=["cannot_get_on_floor", "lumbar_disc", "sciatica", "hernia_abdominal",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hip_pain", "postpartum", "osteoporosis",
            "hypertension", "chronic_fatigue"],
      safe=["cannot_stand", "shoulder_impingement", "no_overhead", "limited_grip"],
      why="Isometrica de core con flexion de cadera sostenida: pelvic_floor_load "
           "alto. La combinacion isometrico + presion intraabdominal es el perfil "
           "clasico de riesgo para suelo pelvico y hernia."),

    E("0396", "dumbbell seated lateral raise", "seated", grip="firm",
      stress=js(sh="high", el="low", cerv="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["cervical_injury", "hypermobility", "tendinitis_elbow"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Abduccion a 90 grados: el arco doloroso del pinzamiento subacromial "
           "esta justo ahi. No pasa de la cabeza, por eso es safe_for no_overhead."),

    E("0690", "seated lower back stretch", "seated", flex="moderate",
      stress=js(lumbar="low", hip="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="low", headdown=True, metab="none",
      laxity="low", temp="none",
      contra=["glaucoma", "retinal_detachment_risk"],
      caut=["lumbar_disc", "hypertension", "dysautonomia", "vertigo",
            "hypermobility", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "limited_grip", "chronic_fatigue", "elderly_65plus"],
      why="Se hace en silla, sin bajar al suelo: safe_for muy amplio. "
           "Pero al inclinarse hacia adelante la cabeza baja del corazon, "
           "y eso activa glaucoma y disautonomia. Detalle facil de pasar por alto."),

    E("1399", "bench dip on floor", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia"],
      why="Cuarto duplicado funcional del fondo en banco. Cuando E4 arme el grafo "
           "de sustituciones, estos cuatro colapsan en uno."),

    E("0282", "decline sit-up", "bench_supine", flex="high",
      stress=js(lumbar="high", cerv="high", hip="high"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "lumbar_disc",
              "cervical_injury", "sciatica", "hernia_abdominal", "glaucoma",
              "retinal_detachment_risk", "recent_abdominal_surgery",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "dysautonomia", "vertigo", "osteoporosis",
            "postpartum", "migraine", "pelvic_floor_dysfunction"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance"],
      why="Sit-up completo en declinado: mas lumbar que el decline crunch (0277) "
           "porque despega toda la espalda. Cabeza bajo el corazon ademas."),

    E("1011", "band seated twist", "seated", floor=True, grip="light",
      rot="high", stress=js(lumbar="moderate", cerv="low", sh="low"),
      lat="alternating", pat="core_rotation", diff=2, rom="moderate",
      ortho="low", change="high", iso="low", metab="low",
      pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_get_on_floor", "lumbar_disc", "si_joint_pain",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["sciatica", "lumbar_pain", "osteoporosis", "hernia_abdominal",
            "postpartum"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "no_overhead", "dysautonomia"],
      why="Rotacion con banda sentado en el suelo. Menos agresivo que el russian "
           "twist (0687) porque no levanta los pies: la lumbar baja de high a moderate."),

    E("1277", "dumbbell fly on exercise ball", "bench_supine", bal="moderate",
      grip="firm", stress=js(sh="high", el="moderate", lumbar="moderate", wr="low"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_balance",
              "limited_grip", "cannot_lie_supine", "vertigo",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "lumbar_pain", "elbow_injury", "multiple_sclerosis",
            "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury"],
      why="Apertura sobre pelota: superficie inestable + rango maximo de hombro. "
           "limited_balance pasa a contraindicacion dura - rodar y caer con "
           "mancuernas en las manos es un accidente serio."),

    E("1293", "dumbbell press on exercise ball", "bench_supine", bal="moderate",
      grip="firm", stress=js(sh="high", el="moderate", lumbar="moderate", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="moderate", temp="low",
      contra=["limited_balance", "limited_grip", "cannot_lie_supine", "vertigo",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypermobility", "lumbar_pain",
            "multiple_sclerosis", "dysautonomia", "elderly_65plus"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "hip_replacement"],
      why="Press sobre pelota. Menos rom que la apertura, por eso el hombro no "
           "es contraindicacion sino precaucion. La inestabilidad sigue mandando."),

    E("2963", "captains chair straight leg raise", "seated", grip="firm",
      flex="moderate", stress=js(sh="moderate", lumbar="moderate", hip="high", el="low"),
      pat="core_flexion", diff=3, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="high",
      metab="moderate", pelvic="high", gripdur="high", temp="moderate",
      contra=["lumbar_disc", "sciatica", "hernia_abdominal", "limited_grip",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hip_pain", "postpartum", "hypertension",
            "carpal_tunnel", "dysautonomia"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury"],
      why="Silla romana: el torso queda vertical sostenido por los antebrazos, "
           "por eso orthostatic_load es moderate pese a decir 'sit'. "
           "Elevacion de piernas rectas = maxima traccion del psoas sobre la lumbar."),

    E("0305", "dumbbell decline shrug", "bench_prone", grip="firm",
      stress=js(cerv="moderate", sh="moderate", el="low"),
      pat="isolation", diff=2, rom="low",
      ortho="none", change="moderate", headdown=True, metab="low",
      gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "cervical_injury", "glaucoma", "retinal_detachment_risk",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "dysautonomia", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "limited_balance", "hip_replacement"],
      why="Boca abajo en declinado: cero carga axial pero la cabeza queda abajo. "
           "Buen ejemplo de que head_below_heart no siempre viene de una inversion."),

    E("0319", "dumbbell incline fly", "bench_incline", grip="firm",
      stress=js(sh="high", el="moderate", wr="low"),
      pat="horizontal_push", diff=3, rom="high",
      ortho="low", metab="low", laxity="high", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip",
              "cannot_transfer_to_bench"],
      caut=["hypermobility", "elbow_injury", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="Apertura inclinada: rotacion externa maxima bajo carga. "
           "laxity high - es de los ejercicios donde la hipermovilidad mas "
           "expone la articulacion."),

    E("0325", "dumbbell incline raise", "bench_incline", grip="firm", oh=True,
      stress=js(sh="high", el="low", cerv="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="low", metab="low", laxity="moderate",
      gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_transfer_to_bench"],
      caut=["cervical_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="Elevacion por encima de la cabeza desde banco inclinado. El respaldo "
           "impide compensar arqueando la lumbar, lo que lo hace mas exigente "
           "para el hombro que la version de pie."),

    E("0327", "dumbbell incline row", "bench_prone", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", metab="low", gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip"],
      caut=["shoulder_impingement", "elbow_injury", "carpal_tunnel",
            "rheumatoid_arthritis", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia"],
      why="CORRECCION A E1: lo marco bench_incline, pero 'sit on the bench with "
           "your chest against the incline' es boca abajo. Es bench_prone. "
           "Remo con pecho apoyado: cero carga lumbar, ideal para hernia discal."),

    E("0329", "dumbbell incline shrug", "bench_incline", grip="firm",
      stress=js(cerv="moderate", sh="moderate"),
      pat="isolation", diff=1, rom="low",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "cervical_injury", "cannot_transfer_to_bench"],
      caut=["shoulder_impingement", "carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Encogimiento con respaldo: elimina la carga axial que tiene la version "
           "de pie (1018). Es su regresion natural para quien no puede pararse."),

    E("0347", "dumbbell lying pronation", "bench_prone", grip="firm",
      stress=js(wr="moderate", el="moderate", sh="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="none", change="moderate", metab="none", gripdur="moderate", temp="none",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "wrist_injury",
              "carpal_tunnel", "limited_grip"],
      caut=["tendinitis_elbow", "rheumatoid_arthritis",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_injury", "knee_pain", "ankle_injury", "lumbar_disc",
            "hip_replacement", "no_overhead", "dysautonomia", "chronic_fatigue"],
      why="CORRECCION A E1: lo marco bench_supine, pero dice 'chest facing down'. "
           "Es bench_prone. Rotacion de antebrazo: minima demanda sistemica, "
           "apto incluso en fatiga cronica."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 2: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
