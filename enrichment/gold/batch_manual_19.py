#!/usr/bin/env python3
"""Lote 19 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("0397", "dumbbell seated neutral wrist curl", "seated", grip="firm",
      flex="low", stress=js(el="moderate", wr="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="moderate", change="low", valsalva="low", metab="low",
      laxity="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "dysautonomia", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis"],
      why="TERCER conflicto nombre/texto seguido en la familia de muneca: se "
           "llama 'wrist curl' pero el texto describe un curl de martillo "
           "('curl the dumbbells up towards your shoulders'), y el target del "
           "dataset dice biceps. Ademas es mecanicamente imposible con los "
           "antebrazos sobre los muslos. Clasificado como curl de codo. "
           "Confianza 0.65."),

    E("1441", "dumbbell over bench one arm reverse wrist curl", "seated",
      grip="firm", flex="low", lat="unilateral",
      stress=js(wr="high", el="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="none", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "tendinitis_elbow",
              "limited_grip", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "elbow_injury",
            "lumbar_pain", "dysautonomia"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis"],
      why="Version unilateral y con apoyo en banco de 1411. Palma abajo = "
           "extensores, el tendon de la epicondilitis: tendinitis_elbow a "
           "contra igual que en 1411. El antebrazo apoyado en el banco y no en "
           "el muslo reduce la flexion de tronco, pero sigue siendo sentado sin "
           "respaldo."),

    E("1287", "dumbbell one arm decline chest press", "bench_supine",
      grip="firm", lat="unilateral", rot="low",
      stress=js(sh="moderate", el="moderate", wr="low", lumbar="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", laxity="moderate", pelvic="low", gripdur="moderate",
      temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "limited_grip",
              "glaucoma", "retinal_detachment_risk", "hernia_abdominal",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "elbow_injury",
            "hypertension", "dysautonomia", "vertigo", "migraine",
            "lumbar_pain", "cardiac"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead",
            "plantar_fasciitis", "one_arm_only"],
      why="Press unilateral en declinado: la carga asimetrica obliga al tronco "
           "a resistir rotacion — lumbar moderate, rot low. head_below_heart "
           "por el banco declinado, con toda la familia ocular a contra. "
           "one_arm_only en safe_for: es literalmente de a un brazo."),

    E("1330", "dumbbell reverse grip incline bench one arm row", "standing",
      standing=True, bal="moderate", grip="firm", lat="unilateral",
      flex="moderate",
      stress=js(lumbar="moderate", sh="moderate", el="moderate", wr="moderate",
                knee="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      ortho="high", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_stand", "wheelchair", "limited_grip", "lumbar_disc",
              "sciatica", "wrist_injury", "elbow_injury",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "shoulder_impingement",
            "carpal_tunnel", "tendinitis_elbow", "limited_balance",
            "hypertension", "obesity", "elderly_65plus", "knee_pain",
            "dysautonomia"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "one_arm_only",
            "ankle_injury", "plantar_fasciitis"],
      why="CORRECCION A E1: E1 dijo bench_incline, pero el texto dice 'stand "
           "facing the bench... bend at the waist and place your knee and hand "
           "on the bench'. Es el remo clasico a una mano: de pie, inclinado, con "
           "apoyo. start_position standing. La diferencia importa mucho — como "
           "bench_incline el motor lo daria por apto para hernia discal, y con "
           "el torso en voladizo es exactamente lo contrario."),

    E("0668", "rear decline bridge", "supine", floor=True, grip="none",
      ext="moderate", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="low", iso="moderate",
      metab="low", laxity="low", pelvic="moderate", gripdur="none", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "si_joint_pain", "sciatica",
            "postpartum", "pelvic_floor_dysfunction", "hernia_abdominal",
            "knee_pain", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "shoulder_impingement",
            "rotator_cuff", "hip_replacement", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "one_arm_only"],
      why="PAR CON 3561 (lote 17). El puente simple es extension pura de "
           "cadera: prescrito en rehabilitacion post-artroplastia, por eso "
           "hip_replacement va en safe_for. La version con marcha (3561) lleva "
           "la rodilla al pecho, supera los 90 grados de flexion y viola la "
           "precaucion posterior — ahi hip_replacement es contraindicacion. "
           "Un solo movimiento agregado invierte el veredicto."),

    E("0056", "barbell lying close-grip triceps extension", "bench_supine",
      oh=True, grip="firm",
      stress=js(el="high", wr="high", sh="moderate"),
      pat="isolation", diff=3, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "limited_grip", "cannot_lie_supine",
              "cannot_transfer_to_bench", "one_arm_only",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "hypermobility",
            "osteoporosis", "no_overhead"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis"],
      why="Rompecraneos con barra recta y agarre SUPINADO ('palms facing up') "
           "cerrado: la combinacion peor para la muneca — wr high. La barra baja "
           "a la frente, no detras de la cabeza, asi que no_overhead queda en "
           "cautions y no en contra, a diferencia de 0337."),

    E("0449", "ez barbell incline triceps extension", "bench_incline", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="low", wr="low"),
      pat="isolation", diff=3, rom="high",
      ortho="low", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench"],
      caut=["tendinitis_elbow", "cervical_injury", "hypertension",
            "hypermobility", "osteoporosis", "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis", "cannot_sit_unsupported"],
      why="Gemelo de 0330 con barra EZ. Diferencia unica pero real: el texto "
           "dice explicitamente 'back against the pad', asi que "
           "cannot_sit_unsupported entra en safe_for. La barra EZ ademas baja "
           "el estres de muneca de moderate a low frente a la barra recta."),

    E("0992", "band push sit-up", "supine", floor=True, grip="light",
      flex="high", stress=js(lumbar="high", hip="moderate", cerv="moderate"),
      pat="core_flexion", diff=3, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="low",
      metab="moderate", laxity="low", pelvic="high", gripdur="moderate",
      temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "cannot_get_on_floor",
              "cannot_lie_supine", "pelvic_floor_dysfunction", "postpartum",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "neck_pain", "si_joint_pain",
            "hypertension", "obesity", "elderly_65plus", "limited_grip",
            "shoulder_impingement"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "wrist_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="Sit-up completo (torso a 45 grados), no crunch: suma flexores de "
           "cadera traccionando sobre la lumbar. Mismo perfil de exclusion que "
           "0832 del lote 18 pero con mas rango. La banda no lo hace mas suave: "
           "agrega resistencia justo en la parte alta del recorrido."),

    E("2187", "barbell reverse close-grip bench press", "bench_supine",
      grip="firm", stress=js(wr="high", el="moderate", sh="low"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="none", change="low", valsalva="high", metab="moderate",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip", "elbow_injury",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "tendinitis_elbow", "hypertension",
            "cardiac", "glaucoma", "osteoporosis", "elderly_65plus",
            "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis"],
      why="Agarre invertido + codos pegados: el hombro baja a low, el mejor "
           "valor de toda la familia de press con barra. Todo el riesgo se "
           "traslada a la muneca en supinacion bajo carga. Es la version plana "
           "de 1257 y comparte el mismo problema: desenganchar en supinado."),

    E("3298", "straddle planche", "plank", floor=True, grip="none",
      stress=js(wr="high", sh="high", el="moderate", lumbar="moderate",
                hip="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="none", change="moderate", valsalva="high", iso="high",
      metab="high", laxity="high", pelvic="moderate", gripdur="none",
      temp="moderate",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement", "rotator_cuff",
              "hypermobility", "hernia_abdominal", "recent_abdominal_surgery",
              "hip_replacement", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["elbow_injury", "lumbar_pain", "lumbar_disc", "hypertension",
            "cardiac", "obesity", "elderly_65plus", "chronic_fatigue",
            "fibromyalgia", "si_joint_pain", "pelvic_floor_dysfunction"],
      safe=[],
      why="CUARTO safe_for vacio. El texto no describe una planche real (no "
           "despega los pies) sino una flexion muy inclinada con piernas "
           "abiertas — confianza 0.65. Aun asi la clasificacion es dura: "
           "hombros por delante de las manos con muneca en extension maxima e "
           "isometrico alto. hip_replacement a contra por la abduccion "
           "extrema mantenida."),

    E("1275", "drop push up", "plank", floor=True, grip="none",
      impact="moderate",
      stress=js(knee="high", wr="moderate", sh="moderate", el="moderate",
                lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="low",
      metab="moderate", laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["knee_injury", "knee_replacement", "knee_pain", "cannot_kneel",
              "cannot_get_on_floor", "cannot_lie_prone", "osteoarthritis",
              "wrist_injury", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "carpal_tunnel", "elbow_injury",
            "rheumatoid_arthritis", "obesity", "elderly_65plus",
            "hernia_abdominal", "lumbar_pain"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "limited_grip",
            "hip_replacement", "ankle_injury", "lumbar_disc",
            "plantar_fasciitis", "dysautonomia"],
      why="HALLAZGO CONTRAINTUITIVO: es un ejercicio de pecho contraindicado "
           "para la RODILLA. 'Quickly drop your knees to the ground' es un "
           "impacto directo de rotula contra el suelo, repetido. knee high e "
           "impact moderate en un push-up. cannot_kneel a contra por la misma "
           "razon. El motor jamas lo habria filtrado clasificando por musculo "
           "objetivo."),

    E("1719", "barbell incline close grip bench press", "bench_incline",
      grip="firm", stress=js(el="high", sh="moderate", wr="moderate"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="low", change="low", valsalva="high", metab="moderate",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "wrist_injury", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "hypertension", "cardiac",
            "carpal_tunnel", "glaucoma", "retinal_detachment_risk",
            "osteoporosis", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis"],
      why="Version inclinada de 0030. El respaldo a 45 grados sube la "
           "participacion del hombro respecto del plano, pero mantiene los "
           "codos pegados: hombro queda en moderate. valsalva high por barra "
           "pesada con desenganche, igual que su gemelo plano."),

    E("1761", "hanging oblique knee raise", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high", rot="high",
      lat="alternating",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate",
                hip="moderate"),
      pat="core_rotation", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "lumbar_disc", "lumbar_pain", "sciatica", "si_joint_pain",
              "cannot_stand", "one_arm_only", "hernia_abdominal",
              "recent_abdominal_surgery", "osteoporosis",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "hypertension", "pelvic_floor_dysfunction", "postpartum",
            "rheumatoid_arthritis", "shoulder_pain"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "plantar_fasciitis"],
      why="Suspension + flexion + rotacion lumbar bajo el peso de las piernas. "
           "Acumula los tres factores que la taxonomia trata como criticos para "
           "la columna. Ironia util: es apto para rodilla y tobillo, porque los "
           "pies nunca tocan el suelo."),

    E("1764", "hanging leg hip raise", "hanging", oh=True,
      grip="hanging_bodyweight", standing=True, flex="high",
      stress=js(sh="high", lumbar="high", el="moderate", wr="moderate",
                hip="moderate"),
      pat="core_flexion", diff=4, rom="moderate",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "wrist_injury", "carpal_tunnel", "elbow_injury",
              "lumbar_disc", "sciatica", "cannot_stand", "one_arm_only",
              "hernia_abdominal", "recent_abdominal_surgery",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "si_joint_pain", "hypermobility", "osteoporosis",
            "obesity", "elderly_65plus", "chronic_fatigue", "hypertension",
            "pelvic_floor_dysfunction", "postpartum", "hip_pain"],
      safe=["cannot_kneel", "cannot_get_on_floor", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "knee_injury",
            "knee_pain", "ankle_injury", "plantar_fasciitis"],
      why="Version sin rotacion de 1761: sale rot high y baja de core_rotation "
           "a core_flexion, lo que devuelve lumbar_pain y si_joint_pain de "
           "contra a cautions. Es la sustitucion directa de 1761 para quien "
           "tolera flexion pero no torsion."),

    E("1774", "side bridge hip abduction", "side_lying", floor=True,
      bal="moderate", grip="none", lat="unilateral", sl=True,
      stress=js(sh="moderate", hip="high", lumbar="low", el="moderate",
                knee="low"),
      pat="core_antiextension", diff=4, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="none",
      temp="moderate",
      contra=["cannot_lie_on_side", "cannot_get_on_floor",
              "shoulder_impingement", "rotator_cuff", "elbow_injury",
              "hip_replacement", "si_joint_pain"],
      caut=["hip_pain", "lumbar_disc", "lumbar_pain", "shoulder_pain",
            "hypermobility", "obesity", "elderly_65plus", "chronic_fatigue",
            "fibromyalgia", "limited_balance", "osteoarthritis",
            "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis"],
      why="Progresion de 0705 (lote 18) y ejemplo de que una progresion cambia "
           "el veredicto. La abduccion en carga mete torque frontal sobre la "
           "sacroiliaca: si_joint_pain y hip_replacement pasan a contra, y "
           "lumbar_disc baja de safe_for a cautions. La base sigue siendo "
           "espinal-neutra, pero ya no es el ejercicio de rehabilitacion que "
           "es el puente lateral simple."),

    E("2133", "farmers walk", "standing", standing=True, bal="moderate",
      grip="firm", axial="moderate",
      stress=js(lumbar="moderate", sh="moderate", wr="moderate", knee="low",
                ank="low", hip="low"),
      pat="carry", diff=2, rom="low",
      ortho="high", change="low", valsalva="moderate", iso="high",
      metab="high", laxity="low", pelvic="moderate", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "wheelchair", "limited_grip", "limited_balance",
              "carpal_tunnel", "osteoporosis", "hernia_abdominal",
              "pregnancy_3rd"],
      caut=["lumbar_disc", "lumbar_pain", "shoulder_impingement",
            "wrist_injury", "knee_pain", "hip_pain", "ankle_injury",
            "plantar_fasciitis", "dysautonomia", "hypertension", "cardiac",
            "obesity", "elderly_65plus", "chronic_fatigue", "varicose_veins",
            "multiple_sclerosis", "pelvic_floor_dysfunction", "postpartum",
            "pregnancy_2nd"],
      safe=["no_overhead", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench"],
      why="Primer patron 'carry' del proyecto. Perfil raro: carga axial "
           "moderada, isometrico alto y agarre alto sostenido durante minutos, "
           "todo de pie y caminando — ortho high y metab high. Es el ejercicio "
           "con la lista de cautions mas larga hasta ahora (19), porque casi "
           "todo sistema participa un poco sin que nada llegue a critico."),

    E("2298", "inverted row on bench", "supine", floor=True, grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", iso="moderate",
      metab="moderate", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "limited_grip",
              "elbow_injury", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "tendinitis_elbow", "obesity", "elderly_65plus",
            "hypertension", "pregnancy_2nd"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "lumbar_disc",
            "lumbar_pain", "sciatica", "plantar_fasciitis", "dysautonomia",
            "osteoporosis"],
      why="E1 no le asigno start_position; el texto dice 'lie face up on the "
           "ground', o sea supine. Traccion horizontal sin necesidad de "
           "pararse ni de sostener el peso con la columna: 13 en safe_for, "
           "incluidos lumbar_disc y sciatica. Es la contraparte de tiron del "
           "push-up (wall) — el suelo de accesibilidad del patron "
           "horizontal_pull para quien puede bajar al piso."),

    E("2470", "dumbbell lying on floor rear delt raise", "prone", floor=True,
      grip="firm", stress=js(sh="high", cerv="moderate", el="low", wr="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="moderate", temp="low",
      contra=["cannot_lie_prone", "cannot_get_on_floor", "limited_grip",
              "shoulder_impingement", "rotator_cuff",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cervical_injury", "neck_pain", "hypermobility", "shoulder_pain",
            "elbow_injury", "hernia_abdominal"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "lumbar_pain",
            "no_overhead", "sciatica", "dysautonomia", "plantar_fasciitis",
            "wrist_injury", "osteoporosis"],
      why="Deltoides posterior en prono sobre el suelo, sin banco: 14 en "
           "safe_for. Es la version accesible de toda la familia de deltoides "
           "posterior del dataset — misma mecanica que 0348/0326 pero sin "
           "requerir transferencia a banco. Cervical moderate por la misma "
           "razon de siempre en prono: el cuello queda rotado o extendido."),
]

# La taxonomia pide confidence < 0.7 cuando el texto fuente es ambiguo.
CONFIDENCE_OVERRIDES = {
    "0397": 0.65,  # el nombre dice wrist curl, el texto describe curl de codo
    "3298": 0.65,  # el texto no describe una planche real
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
    print(f"lote 19: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
