#!/usr/bin/env python3
"""
Lote 1 de clasificacion manual en chat — 18 ejercicios.
Taxonomia v1.2 (30 campos, incluidos los 10 fisiologicos).

Se anexa a output/manual_classified.json.
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "output", "manual_classified.json")


def js(knee="none", hip="none", lumbar="none", cerv="none",
       sh="none", el="none", wr="none", ank="none"):
    return {"knee": knee, "hip": hip, "lumbar_spine": lumbar,
            "cervical_spine": cerv, "shoulder": sh, "elbow": el,
            "wrist": wr, "ankle": ank}


def E(eid, name, pos, *, floor=False, standing=False, bal="none", sl=False,
      oh=False, grip="none", axial="none", flex="none", ext="none", rot="none",
      impact="none", stress=None, lat="bilateral", pat="isolation", diff=3,
      rom="moderate",
      ortho="low", change="none", headdown=False, valsalva="none",
      iso="none", metab="low", laxity="none", pelvic="none", temp="low",
      gripdur="none",
      contra=(), caut=(), safe=(), why=""):
    return {
        "exercise_id": eid, "_name": name,
        "start_position": pos,
        "requires_floor_transition": floor,
        "requires_standing": standing,
        "requires_balance": bal,
        "single_leg_support": sl,
        "overhead_position": oh,
        "grip_required": grip,
        "axial_spinal_load": axial,
        "spinal_flexion": flex,
        "spinal_extension": ext,
        "spinal_rotation": rot,
        "impact_level": impact,
        "joint_stress": stress or js(),
        "laterality": lat,
        "movement_pattern": pat,
        "difficulty": diff,
        "rom_demand": rom,
        # --- v1.2 fisiologicos ---
        "orthostatic_load": ortho,
        "position_change": change,
        "head_below_heart": headdown,
        "valsalva_risk": valsalva,
        "sustained_isometric": iso,
        "metabolic_intensity": metab,
        "joint_laxity_risk": laxity,
        "pelvic_floor_load": pelvic,
        "temperature_load": temp,
        "grip_duration": gripdur,
        # --- seguridad ---
        "contraindications": list(contra),
        "cautions": list(caut),
        "safe_for": list(safe),
        "_reasoning": why,
        "enrichment_source": "manual_chat",
        "confidence": 0.95,
    }


BATCH = [
    E("0438", "dumbbell w-press", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low", wr="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", gripdur="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury",
            "knee_pain", "hip_replacement", "dysautonomia"],
      why="Press vertical sentado: el respaldo elimina la compensacion lumbar. "
           "Sentado y sin impacto lo hace apto para disautonomia, pero el brazo "
           "sobre la cabeza sigue siendo contraindicacion de hombro."),

    E("0687", "russian twist", "seated", floor=True, bal="moderate",
      flex="moderate", rot="high",
      stress=js(lumbar="high", hip="moderate", cerv="low"),
      lat="alternating", pat="core_rotation", diff=3, rom="moderate",
      ortho="low", change="high", valsalva="low", iso="moderate",
      metab="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_get_on_floor", "lumbar_disc", "sciatica", "si_joint_pain",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd",
              "recent_abdominal_surgery"],
      caut=["lumbar_pain", "osteoporosis", "postpartum",
            "pelvic_floor_dysfunction", "cervical_injury"],
      why="Rotacion lumbar con los pies en el aire y la columna en flexion: "
           "la peor combinacion posible para disco. Muy popular y muy sobrevalorado."),

    E("0817", "triceps stretch", "seated", oh=True, lat="unilateral",
      stress=js(sh="moderate", el="low"), pat="isolation", diff=1, rom="high",
      ortho="low", iso="moderate", metab="none", laxity="moderate", temp="none",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["hypermobility", "elbow_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "dysautonomia", "chronic_fatigue",
            "hip_replacement"],
      why="Estiramiento pasivo: difficulty 1 pero rom alto. Excelente safe_for "
           "para casi todo perfil restringido - salvo hombro, que es justo lo que estira."),

    E("1363", "spine stretch", "seated", floor=True, ext="moderate",
      stress=js(lumbar="moderate", sh="moderate", wr="moderate"),
      pat="isolation", diff=1, rom="moderate",
      ortho="low", change="high", metab="none", laxity="moderate",
      gripdur="low", temp="none",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel"],
      caut=["lumbar_disc", "shoulder_impingement", "hypermobility",
            "rheumatoid_arthritis"],
      safe=["cannot_stand", "knee_pain", "dysautonomia", "chronic_fatigue"],
      why="Se apoya en las manos detras del cuerpo: la muneca en extension "
           "carga mas de lo que sugiere un 'estiramiento de columna'."),

    E("1368", "ankle circles", "seated", floor=True, lat="unilateral",
      stress=js(ank="low"), pat="isolation", diff=1, rom="low",
      ortho="low", change="high", metab="none", temp="none",
      contra=["cannot_get_on_floor", "ankle_injury"],
      caut=["hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "lumbar_disc", "dysautonomia", "chronic_fatigue", "fibromyalgia",
            "hip_replacement", "elderly_65plus", "hypertension"],
      why="El ejercicio mas accesible del lote. Movilidad de tobillo sin carga: "
           "seguro incluso en fatiga cronica. Se puede adaptar a silla facilmente."),

    E("3119", "potty squat", "standing", standing=True, bal="moderate",
      axial="low", stress=js(knee="high", hip="high", ank="moderate", lumbar="low"),
      pat="squat", diff=2, rom="high",
      ortho="moderate", change="moderate", valsalva="low", metab="moderate",
      laxity="moderate", pelvic="moderate", temp="moderate",
      contra=["cannot_stand", "knee_injury", "knee_replacement", "hip_replacement"],
      caut=["knee_pain", "limited_balance", "osteoarthritis", "elderly_65plus",
            "dysautonomia", "hypermobility", "pregnancy_3rd"],
      safe=["shoulder_impingement", "no_overhead", "limited_grip", "wrist_injury"],
      why="CORRECCION A E1: lo marco 'seated' porque el nombre dice squat, pero "
           "el texto empieza con 'Stand with your feet shoulder-width apart'. "
           "Es de pie. Sentadilla profunda: rom alto exige movilidad de tobillo y cadera."),

    E("0130", "bench hip extension", "seated", bal="low",
      ext="moderate", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="hinge", diff=2, rom="moderate",
      ortho="low", change="low", valsalva="low", iso="low",
      metab="low", pelvic="moderate", temp="low",
      contra=["lumbar_disc"],
      caut=["si_joint_pain", "hip_pain", "hip_replacement", "pelvic_floor_dysfunction",
            "postpartum", "hernia_abdominal", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_pain", "shoulder_impingement",
            "no_overhead", "limited_grip", "wrist_injury", "dysautonomia"],
      why="Empuje de cadera con la espalda apoyada: glúteo sin carga axial ni "
           "equilibrio. De los mejores ejercicios de cadena posterior para "
           "movilidad reducida."),

    E("0391", "dumbbell seated curl", "seated", grip="firm",
      stress=js(el="moderate", wr="low", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["carpal_tunnel", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus"],
      why="Curl sentado: seguro para todo lo que no sea codo o agarre. "
           "El respaldo evita el balanceo lumbar que hace el curl de pie."),

    E("0555", "kick out sit", "seated", bal="low",
      flex="low", stress=js(hip="moderate", lumbar="moderate", knee="low"),
      pat="core_flexion", diff=2, rom="moderate",
      ortho="low", valsalva="low", iso="moderate", metab="low",
      pelvic="moderate", temp="low",
      contra=["lumbar_disc"],
      caut=["sciatica", "hip_pain", "hernia_abdominal", "postpartum",
            "pelvic_floor_dysfunction", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "cannot_get_on_floor", "limited_balance",
            "knee_pain", "ankle_injury", "shoulder_impingement", "dysautonomia"],
      why="Core en silla, sin bajar al suelo: raro y valioso. Cubre el hueco "
           "de abdominales para quien no puede acostarse. El psoas tracciona "
           "la lumbar, por eso no es safe_for lumbar."),

    E("1753", "three bench dip", "seated", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="low", change="low", valsalva="low", metab="moderate",
      gripdur="moderate", temp="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "limited_grip", "tendinitis_elbow"],
      caut=["wrist_injury", "carpal_tunnel", "hypermobility"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "lumbar_disc"],
      why="Fondo en banco con pies elevados: version mas dura del bench dip. "
           "Hombro en extension bajo carga = maximo riesgo de pinzamiento."),

    E("3419", "l-sit on floor", "seated", floor=True, bal="moderate",
      grip="firm", flex="moderate",
      stress=js(sh="high", wr="high", lumbar="moderate", hip="high", el="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      ortho="low", change="high", valsalva="moderate", iso="high",
      metab="moderate", laxity="moderate", pelvic="high", temp="moderate",
      gripdur="high",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel",
              "limited_grip", "shoulder_impingement", "hernia_abdominal",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd",
              "recent_abdominal_surgery", "pelvic_floor_dysfunction"],
      caut=["lumbar_disc", "hypertension", "postpartum", "hypermobility"],
      why="Isometrica maxima sobre munecas y core. difficulty 5. "
           "pelvic_floor_load alto: la presion intraabdominal sostenida es "
           "el riesgo que casi nunca se menciona en este ejercicio."),

    E("0392", "dumbbell seated front raise", "seated", grip="firm",
      stress=js(sh="high", el="low", cerv="low"),
      pat="isolation", diff=2, rom="moderate",
      ortho="low", metab="low", gripdur="moderate", temp="low",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["no_overhead", "cervical_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "dysautonomia"],
      why="Elevacion frontal: el brazo extendido a 90 grados es la posicion "
           "clasica de pinzamiento subacromial, aunque no pase de la cabeza."),

    E("0402", "dumbbell seated preacher curl", "seated_machine", grip="firm",
      lat="unilateral", stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="high",
      ortho="low", metab="low", gripdur="moderate", laxity="moderate", temp="low",
      contra=["limited_grip", "elbow_injury", "tendinitis_elbow"],
      caut=["carpal_tunnel", "hypermobility", "rheumatoid_arthritis"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "lumbar_disc", "hip_replacement", "no_overhead",
            "dysautonomia", "elderly_65plus", "chronic_fatigue"],
      why="Banco predicador: brazo fijo, cero compensacion. El codo llega a "
           "extension completa bajo carga - de ahi el estres alto pese a ser "
           "un ejercicio 'facil'."),

    E("0405", "dumbbell seated shoulder press", "seated", grip="firm", oh=True,
      axial="low", stress=js(sh="high", el="moderate", cerv="low", lumbar="low"),
      pat="vertical_push", diff=3, rom="high",
      ortho="low", valsalva="moderate", metab="low", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["cervical_injury", "hypertension", "elbow_injury", "hypermobility"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "knee_pain",
            "ankle_injury", "hip_replacement", "dysautonomia"],
      why="Casi identico al w-press (0438): ambos deben caer en el mismo "
           "substitute_group. Sentado con respaldo lo hace apto para POTS."),

    E("0691", "seated side crunch (wall)", "seated", floor=True,
      flex="moderate", rot="moderate",
      stress=js(lumbar="moderate", cerv="moderate", hip="low"),
      lat="alternating", pat="core_rotation", diff=2, rom="moderate",
      ortho="low", change="high", iso="low", metab="low", pelvic="moderate",
      temp="low",
      contra=["cannot_get_on_floor", "lumbar_disc", "cervical_injury",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["sciatica", "si_joint_pain", "postpartum", "osteoporosis"],
      safe=["cannot_stand", "knee_pain", "ankle_injury", "shoulder_impingement",
            "limited_grip", "no_overhead"],
      why="Manos detras de la cabeza otra vez: cervical moderate por la "
           "traccion del cuello. La pared da soporte, lo que baja la exigencia "
           "de equilibrio frente al russian twist."),

    E("0277", "decline crunch", "bench_supine", flex="high",
      stress=js(lumbar="moderate", cerv="high", hip="moderate"),
      pat="core_flexion", diff=3, rom="moderate",
      ortho="none", change="moderate", headdown=True, valsalva="moderate",
      metab="low", pelvic="moderate", temp="low",
      contra=["cannot_lie_supine", "cannot_transfer_to_bench", "lumbar_disc",
              "cervical_injury", "hernia_abdominal", "glaucoma",
              "retinal_detachment_risk", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["hypertension", "dysautonomia", "vertigo", "osteoporosis",
            "postpartum", "migraine"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance"],
      why="Banco declinado: la cabeza queda por debajo del corazon. "
           "head_below_heart=true activa glaucoma, hipertension y disautonomia. "
           "Es el unico eje que distingue este crunch de uno plano."),

    E("0279", "decline push-up", "plank", floor=True, bal="low",
      ext="low", stress=js(sh="high", el="moderate", wr="high", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      ortho="none", change="high", valsalva="low", iso="moderate",
      metab="moderate", pelvic="low", temp="moderate", gripdur="low",
      contra=["cannot_get_on_floor", "wrist_injury", "carpal_tunnel"],
      caut=["shoulder_impingement", "elbow_injury", "hypertension",
            "pregnancy_2nd", "pregnancy_3rd", "obesity"],
      safe=["cannot_stand", "knee_injury", "knee_pain", "ankle_injury",
            "hip_replacement", "limited_balance"],
      why="CORRECCION A E1: lo marco 'bench_supine' por la palabra decline, "
           "pero es una plancha con los PIES elevados, no el torso. "
           "Los pies arriba desplazan peso a las munecas: wrist high."),

    E("0375", "dumbbell pullover", "bench_supine", grip="firm", oh=True,
      ext="moderate", stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=3, rom="high",
      ortho="none", change="low", valsalva="moderate", metab="low",
      laxity="high", gripdur="moderate", temp="low",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff",
              "limited_grip", "cannot_lie_supine", "cannot_transfer_to_bench",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "elbow_injury", "hypermobility", "hypertension"],
      safe=["cannot_stand", "cannot_get_on_floor", "knee_injury", "knee_pain",
            "ankle_injury", "limited_balance", "hip_replacement", "dysautonomia"],
      why="joint_laxity_risk alto: el hombro llega a flexion maxima con carga. "
           "En hipermovilidad es donde mas facil se subluxa. Version con "
           "mancuerna del 0073 - mismo substitute_group."),
]


def main():
    existing = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else []
    have = {r["exercise_id"] for r in existing}
    added = [e for e in BATCH if e["exercise_id"] not in have]
    existing.extend(added)
    json.dump(existing, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"lote 1: +{len(added)}   total manual: {len(existing)}")


if __name__ == "__main__":
    main()
