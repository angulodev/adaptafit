#!/usr/bin/env python3
"""Lote 18 de clasificacion manual en chat — 18 ejercicios. Taxonomia v1.2."""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_manual_01 import E, js


BATCH = [
    E("2188", "dumbbell seated triceps extension", "seated", oh=True,
      grip="firm", axial="low",
      stress=js(sh="high", el="high", cerv="low", wr="low", lumbar="low"),
      pat="isolation", diff=3, rom="high",
      ortho="moderate", change="low", valsalva="moderate", metab="low",
      laxity="moderate", gripdur="high", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "limited_grip", "cannot_transfer_to_bench",
              "cannot_sit_unsupported"],
      caut=["tendinitis_elbow", "cervical_injury", "neck_pain", "hypertension",
            "hypermobility", "osteoporosis", "dysautonomia", "lumbar_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "plantar_fasciitis"],
      why="Extension overhead sentado SIN respaldo ('back straight', no "
           "'against the backrest'): ortho moderate y cannot_sit_unsupported a "
           "contra. La mancuerna sostenida con las dos manos detras de la nuca "
           "toda la serie: gripdur high."),

    E("1415", "dumbbell one arm seated neutral wrist curl", "seated",
      grip="firm", flex="low", lat="unilateral",
      stress=js(wr="high", el="low", lumbar="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="moderate", change="low", valsalva="none", metab="low",
      laxity="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip",
              "cannot_transfer_to_bench", "cannot_sit_unsupported"],
      caut=["rheumatoid_arthritis", "osteoarthritis", "tendinitis_elbow",
            "elbow_injury", "lumbar_pain", "dysautonomia"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "one_arm_only",
            "plantar_fasciitis"],
      why="CONFLICTO NOMBRE vs TEXTO: el nombre dice 'neutral' (agarre martillo) "
           "pero el texto dice 'palm facing up' — es un curl de muneca supinado, "
           "flexores. Mandan las instrucciones. Confianza 0.70. Unilateral y de "
           "carga minima: entra en safe_for de one_arm_only, raro en el dataset."),

    E("0337", "dumbbell lying extension (across face)", "bench_supine",
      oh=True, grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate", cerv="low"),
      pat="isolation", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "no_overhead",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury", "carpal_tunnel",
            "hypermobility", "cervical_injury", "hypertension"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "dysautonomia",
            "plantar_fasciitis"],
      why="Variante 'across face' del rompecraneos: el arco pasa por detras de "
           "la cabeza, o sea flexion de hombro a rango final. no_overhead a "
           "contra aunque el ejercicio sea acostado — el criterio es la "
           "posicion del brazo, no la del cuerpo."),

    E("0352", "dumbbell neutral grip bench press", "bench_supine", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", metab="moderate",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
            "elbow_injury", "wrist_injury", "hypertension", "carpal_tunnel"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis", "osteoporosis"],
      why="EL CONTRASTE DEL LOTE. Mismo patron que 1624 (reverse bench press) "
           "pero con agarre neutro y 'elbows close to your body': el hombro "
           "baja de high a moderate y el pinzamiento pasa de contraindicacion a "
           "precaucion. La posicion del codo, no el implemento, decide. Esto es "
           "una arista directa del grafo de sustitucion de E4."),

    E("1733", "dumbbell incline two arm extension", "bench_incline",
      grip="firm", stress=js(sh="moderate", el="moderate", wr="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      ortho="low", change="moderate", valsalva="low", metab="low",
      laxity="low", pelvic="low", gripdur="moderate", temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "limited_grip",
              "pregnancy_3rd"],
      caut=["shoulder_impingement", "elbow_injury", "wrist_injury",
            "hypermobility", "dysautonomia", "vertigo", "lumbar_pain"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "no_overhead", "lumbar_disc",
            "plantar_fasciitis"],
      why="El texto no describe una extension de triceps: dice extender los "
           "brazos hacia el techo y bajarlos, o sea un press. Clasificado por "
           "lo que se ejecuta. Confianza 0.65. Unico del lote que describe "
           "explicitamente la transicion sentado→acostado: change moderate."),

    E("1419", "iron cross stretch", "supine", floor=True, grip="none",
      rot="high", flex="moderate", lat="alternating",
      stress=js(lumbar="high", hip="high", sh="moderate", knee="low"),
      pat="mobility_stretch", diff=3, rom="high",
      ortho="none", change="low", valsalva="low", iso="low", metab="low",
      laxity="high", pelvic="moderate", gripdur="none", temp="low",
      contra=["lumbar_disc", "sciatica", "si_joint_pain", "cannot_get_on_floor",
              "cannot_lie_supine", "hip_replacement", "osteoporosis",
              "pregnancy_2nd", "pregnancy_3rd", "recent_abdominal_surgery"],
      caut=["lumbar_pain", "hip_pain", "hypermobility", "shoulder_impingement",
            "hernia_abdominal", "postpartum", "pelvic_floor_dysfunction",
            "obesity"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "elbow_injury", "knee_injury", "ankle_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="Se llama 'stretch' y el motor no debe creerle. Piernas rectas "
           "cruzando al lado contrario = rotacion lumbar cargada con brazo de "
           "palanca maximo, ademas de flexion de cadera. rot high, laxity high. "
           "Osteoporosis a contra: rotacion + flexion es la combinacion que "
           "fractura vertebras por compresion."),

    E("0045", "barbell guillotine bench press", "bench_supine", grip="firm",
      stress=js(sh="high", cerv="high", el="moderate", wr="moderate"),
      pat="horizontal_push", diff=5, rom="high",
      ortho="none", change="low", valsalva="high", metab="moderate",
      laxity="high", pelvic="low", gripdur="high", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "shoulder_pain",
              "cervical_injury", "neck_pain", "hypermobility", "limited_grip",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "elderly_65plus", "osteoporosis", "epilepsy", "vertigo",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "cardiac", "elbow_injury", "wrist_injury",
            "carpal_tunnel", "glaucoma", "retinal_detachment_risk", "obesity",
            "multiple_sclerosis", "chronic_fatigue"],
      safe=[],
      why="safe_for VACIO. Barra descendiendo sobre el CUELLO con los codos "
           "abiertos a 90: abduccion + rotacion externa maxima, el arco exacto "
           "del pinzamiento, y sin margen de error mecanico. epilepsy y vertigo "
           "a contra por consecuencia catastrofica de una perdida de control, "
           "no por carga. Tercer safe_for vacio del proyecto."),

    E("3699", "shoulder tap", "plank", floor=True, bal="moderate", grip="none",
      lat="alternating",
      stress=js(wr="high", sh="moderate", lumbar="moderate", el="low"),
      pat="core_antiextension", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="moderate", pelvic="moderate", gripdur="none",
      temp="low",
      contra=["wrist_injury", "carpal_tunnel", "cannot_get_on_floor",
              "cannot_lie_prone", "shoulder_impingement",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["rotator_cuff", "elbow_injury", "lumbar_pain", "lumbar_disc",
            "hypertension", "obesity", "pelvic_floor_dysfunction", "postpartum",
            "hernia_abdominal", "elderly_65plus", "rheumatoid_arthritis",
            "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "knee_injury", "knee_pain",
            "hip_replacement", "limited_grip", "ankle_injury"],
      why="Antiextension con antirrotacion: cada vez que se levanta una mano el "
           "peso pasa a un solo brazo. Muneca en extension bajo carga asimetrica "
           "= wrist_injury y tunel carpiano a contra. limited_grip en safe_for: "
           "la mano se apoya abierta, no agarra nada."),

    E("0035", "barbell decline close grip to skull press", "bench_supine",
      grip="firm", stress=js(el="high", sh="moderate", wr="high", cerv="low"),
      pat="isolation", diff=4, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="high",
      metab="low", laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["elbow_injury", "tendinitis_elbow", "wrist_injury",
              "carpal_tunnel", "limited_grip", "cannot_lie_supine",
              "cannot_transfer_to_bench", "glaucoma", "retinal_detachment_risk",
              "hernia_abdominal", "one_arm_only", "pregnancy_1st",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "hypertension", "cardiac", "dysautonomia",
            "vertigo", "migraine", "osteoporosis", "elderly_65plus"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "no_overhead", "plantar_fasciitis"],
      why="Cuarto declinado de la familia rompecraneos, y el peor: barra recta "
           "(no EZ) obliga a la muneca a pronacion fija — wr high, contra. "
           "Ademas valsalva high por la carga y headdown por el declinado: "
           "acumula los dos disparadores de presion intracraneal a la vez."),

    E("0705", "side bridge v. 2", "side_lying", floor=True, grip="none",
      lat="unilateral",
      stress=js(sh="moderate", lumbar="low", hip="moderate", el="moderate"),
      pat="core_antiextension", diff=3, rom="low",
      ortho="none", change="moderate", valsalva="low", iso="high",
      metab="moderate", laxity="moderate", pelvic="low", gripdur="none",
      temp="low",
      contra=["cannot_lie_on_side", "cannot_get_on_floor",
              "shoulder_impingement", "rotator_cuff", "elbow_injury"],
      caut=["si_joint_pain", "hip_pain", "shoulder_pain", "obesity",
            "hypermobility", "elderly_65plus", "chronic_fatigue",
            "fibromyalgia", "hypertension", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_grip", "no_overhead", "wrist_injury",
            "carpal_tunnel", "knee_injury", "knee_pain", "ankle_injury",
            "plantar_fasciitis", "lumbar_disc", "lumbar_pain"],
      why="HALLAZGO: primer ejercicio de core con lumbar_disc en safe_for. El "
           "puente lateral es parte del Big-3 de McGill, prescrito justamente "
           "en hernia discal porque estabiliza sin flexionar ni rotar la "
           "columna. joint_stress lumbar low a proposito, para que el motor no "
           "lo corte por umbral. Contrasta con 0832 en este mismo lote."),

    E("0806", "suspended push-up", "standing", standing=True, bal="high",
      grip="firm", stress=js(sh="high", el="moderate", wr="moderate",
                             lumbar="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="moderate", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="low", gripdur="high",
      temp="moderate",
      contra=["cannot_stand", "limited_balance", "wheelchair", "limited_grip",
              "shoulder_impingement", "rotator_cuff", "hypermobility",
              "vertigo", "visual_impairment"],
      caut=["elbow_injury", "wrist_injury", "carpal_tunnel", "lumbar_pain",
            "shoulder_pain", "elderly_65plus", "obesity", "chronic_fatigue",
            "multiple_sclerosis", "dysautonomia", "hypertension"],
      safe=["cannot_get_on_floor", "cannot_kneel", "cannot_lie_supine",
            "cannot_lie_prone", "cannot_transfer_to_bench", "no_overhead",
            "knee_injury", "knee_pain", "lumbar_disc"],
      why="Empuje horizontal sin suelo ni banco: cubre el mismo hueco que "
           "push-up (wall) del lote 17, pero por arriba en dificultad. La "
           "inestabilidad de las cintas dispara laxity high — util para "
           "progresion, veneno para hipermovilidad."),

    E("0832", "weighted crunch", "supine", floor=True, grip="light",
      flex="high", stress=js(lumbar="high", cerv="moderate", hip="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="none", change="low", valsalva="moderate", iso="low",
      metab="moderate", laxity="low", pelvic="high", gripdur="low", temp="low",
      contra=["lumbar_disc", "sciatica", "osteoporosis", "hernia_abdominal",
              "recent_abdominal_surgery", "cannot_get_on_floor",
              "cannot_lie_supine", "pelvic_floor_dysfunction", "postpartum",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "neck_pain", "hypertension",
            "obesity", "si_joint_pain", "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "no_overhead", "knee_injury",
            "knee_pain", "ankle_injury", "hip_replacement", "wrist_injury",
            "plantar_fasciitis", "dysautonomia"],
      why="EL CONTRASTE DE 0705. Mismo objetivo (abdomen), mismo suelo, pero "
           "flexion espinal cargada y repetida: pelvic high, lumbar high, y la "
           "lista completa de embarazo, posparto, hernia y osteoporosis a "
           "contra. Dos ejercicios de core, resultados opuestos — es la mejor "
           "demostracion de por que la taxonomia no clasifica por musculo."),

    E("1257", "barbell reverse grip incline bench press", "bench_incline",
      grip="firm", stress=js(sh="moderate", el="moderate", wr="high"),
      pat="horizontal_push", diff=4, rom="moderate",
      ortho="low", change="low", valsalva="high", metab="moderate",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["wrist_injury", "carpal_tunnel", "limited_grip", "elbow_injury",
              "cannot_lie_supine", "cannot_transfer_to_bench", "one_arm_only",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "hypertension", "cardiac",
            "tendinitis_elbow", "hypermobility", "glaucoma", "osteoporosis",
            "elderly_65plus"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "dysautonomia", "plantar_fasciitis"],
      why="El agarre invertido reduce el pinzamiento (por eso hombro queda en "
           "cautions y no contra) pero traslada todo a la muneca en supinacion "
           "bajo barra pesada: wr high. Ademas desenganchar en supinado es el "
           "momento de mayor riesgo — valsalva high y one_arm_only a contra."),

    E("1274", "deep push up", "plank", floor=True, grip="firm",
      stress=js(sh="high", wr="moderate", el="moderate", lumbar="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      ortho="none", change="moderate", valsalva="moderate", iso="moderate",
      metab="moderate", laxity="high", pelvic="moderate", gripdur="moderate",
      temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "cannot_get_on_floor",
              "cannot_lie_prone", "hypermobility", "limited_grip",
              "recent_abdominal_surgery", "pregnancy_3rd"],
      caut=["shoulder_pain", "elbow_injury", "wrist_injury", "carpal_tunnel",
            "lumbar_pain", "lumbar_disc", "obesity", "elderly_65plus",
            "hernia_abdominal", "pelvic_floor_dysfunction", "postpartum",
            "pregnancy_2nd"],
      safe=["cannot_stand", "no_overhead", "knee_injury", "knee_pain",
            "hip_replacement", "ankle_injury", "plantar_fasciitis"],
      why="El equipamiento dice 'dumbbell' y el nombre dice 'deep': se hace con "
           "las manos sobre mancuernas para bajar el pecho por debajo de ellas. "
           "El texto no lo menciona pero es la unica lectura coherente con "
           "'deep'. Esa profundidad extra es extension de hombro mas alla del "
           "neutro: sh high, laxity high. Confianza 0.65."),

    E("1317", "barbell reverse grip incline bench row", "bench_prone",
      grip="firm", stress=js(sh="moderate", el="moderate", wr="moderate",
                             lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      ortho="low", change="moderate", valsalva="low", metab="moderate",
      laxity="low", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "one_arm_only", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "rotator_cuff", "wrist_injury",
            "carpal_tunnel", "tendinitis_elbow", "shoulder_pain",
            "hypertension"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "lumbar_pain",
            "no_overhead", "sciatica", "dysautonomia", "plantar_fasciitis",
            "osteoporosis"],
      why="CORRECCION A E1: E1 dijo bench_incline, pero el texto dice 'sit "
           "facing the backrest with your chest against it' — el pecho apoyado "
           "boca abajo es bench_prone. Remo con pecho apoyado: la columna no "
           "sostiene nada, por eso lumbar_disc Y sciatica en safe_for. Es el "
           "remo mas seguro del catalogo para espalda lesionada."),

    E("1346", "kneeling lat stretch", "kneeling", floor=True, oh=True,
      grip="none", rot="low", ext="low", lat="alternating",
      stress=js(sh="moderate", knee="moderate", lumbar="low", ank="moderate"),
      pat="mobility_stretch", diff=1, rom="high",
      ortho="low", change="moderate", valsalva="none", iso="low", metab="low",
      laxity="moderate", pelvic="none", gripdur="none", temp="low",
      contra=["cannot_kneel", "cannot_get_on_floor", "no_overhead",
              "shoulder_impingement", "knee_replacement", "knee_injury"],
      caut=["rotator_cuff", "knee_pain", "ankle_injury", "plantar_fasciitis",
            "hypermobility", "lumbar_pain", "elderly_65plus", "osteoarthritis"],
      safe=["limited_grip", "wrist_injury", "carpal_tunnel", "elbow_injury",
            "dysautonomia", "cannot_stand", "hypertension", "cardiac"],
      why="Estiramiento suave (diff 1, valsalva none) pero con tres filtros "
           "duros de Capa A encadenados: arrodillarse, bajar al suelo y brazos "
           "sobre la cabeza. Buen ejemplo de que la intensidad baja no implica "
           "accesibilidad alta. 'toes pointing back' carga el empeine: ank "
           "moderate."),

    E("1397", "standing calves", "standing", standing=True, bal="moderate",
      grip="none", axial="low",
      stress=js(ank="moderate", knee="low", hip="low"),
      pat="isolation", diff=1, rom="moderate",
      ortho="high", change="low", valsalva="low", iso="low", metab="low",
      laxity="low", pelvic="low", gripdur="none", temp="low",
      contra=["cannot_stand", "wheelchair", "ankle_injury"],
      caut=["plantar_fasciitis", "limited_balance", "knee_pain",
            "dysautonomia", "vertigo", "osteoarthritis", "varicose_veins",
            "elderly_65plus", "hip_replacement"],
      safe=["no_overhead", "limited_grip", "wrist_injury", "carpal_tunnel",
            "elbow_injury", "shoulder_impingement", "rotator_cuff",
            "lumbar_disc", "cannot_get_on_floor", "cannot_kneel",
            "cannot_lie_supine", "cannot_lie_prone", "cannot_transfer_to_bench",
            "one_arm_only", "hernia_abdominal", "osteoporosis"],
      why="16 en safe_for, nuevo maximo del proyecto — supera a push-up (wall). "
           "Sin agarre, sin brazos, sin columna cargada, sin suelo. Todo el "
           "peso del filtro cae en un solo eje: hay que poder pararse. "
           "ortho high igual, es de pie sostenido: disautonomia a cautions "
           "pese a lo benigno del movimiento."),

    E("1666", "dumbbell one arm prone hammer curl", "bench_prone", grip="firm",
      lat="unilateral", stress=js(el="moderate", sh="moderate", wr="low",
                                  cerv="moderate"),
      pat="isolation", diff=2, rom="moderate",
      ortho="none", change="moderate", valsalva="low", metab="low",
      laxity="moderate", pelvic="low", gripdur="high", temp="low",
      contra=["cannot_lie_prone", "cannot_transfer_to_bench", "limited_grip",
              "elbow_injury", "pregnancy_1st", "pregnancy_2nd",
              "pregnancy_3rd"],
      caut=["tendinitis_elbow", "shoulder_impingement", "cervical_injury",
            "neck_pain", "hypermobility", "wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "lumbar_disc", "no_overhead",
            "one_arm_only", "dysautonomia", "plantar_fasciitis"],
      why="Prono con el brazo colgando: el hombro queda en distraccion pasiva "
           "sosteniendo la mancuerna entre repeticiones — laxity moderate. "
           "Cervical moderate por la misma razon que 1423: en prono el cuello "
           "se rota o extiende toda la serie. Unilateral puro: one_arm_only "
           "en safe_for."),
]

# La taxonomia pide confidence < 0.7 cuando el texto fuente es ambiguo.
CONFIDENCE_OVERRIDES = {
    "1415": 0.70,  # nombre dice neutral, texto dice supinado
    "1733": 0.65,  # el texto describe un press, no una extension
    "1274": 0.65,  # el texto omite las mancuernas que definen el ejercicio
}

for _e in BATCH:
    _e.pop("safe_note", None)
    if _e["exercise_id"] in CONFIDENCE_OVERRIDES:
        _e["confidence"] = CONFIDENCE_OVERRIDES[_e["exercise_id"]]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 18: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
