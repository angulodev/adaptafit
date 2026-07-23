#!/usr/bin/env python3
"""
Anotacion manual de 45 ejercicios, hecha en conversacion (no por API).
Seleccionados para cubrir el espacio start_position x movement_pattern.

Se fusionan con gold_examples.json. Marcados con _annotated_in: "chat".
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOLD = os.path.join(BASE, "gold", "gold_examples.json")

L = ["none", "low", "moderate", "high"]


def js(knee="none", hip="none", lumbar="none", cerv="none",
       sh="none", el="none", wr="none", ank="none"):
    return {"knee": knee, "hip": hip, "lumbar_spine": lumbar,
            "cervical_spine": cerv, "shoulder": sh, "elbow": el,
            "wrist": wr, "ankle": ank}


def E(eid, name, pos, *, floor=False, standing=False, bal="none", sl=False,
      oh=False, grip="none", axial="none", flex="none", ext="none", rot="none",
      impact="none", stress=None, lat="bilateral", pat="isolation", diff=3,
      rom="moderate", contra=(), caut=(), safe=(), why=""):
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
        "contraindications": list(contra),
        "cautions": list(caut),
        "safe_for": list(safe),
        "_reasoning": why,
        "_annotated_in": "chat",
    }


NEW = [
    # ---------------- DE PIE · aislamiento ----------------
    E("1018", "band shrug", "standing", standing=True, bal="low", grip="light",
      axial="low", stress=js(cerv="moderate", sh="moderate", lumbar="low"),
      pat="isolation", diff=1, rom="low",
      contra=["cannot_stand", "cervical_injury"],
      caut=["shoulder_impingement", "hypertension"],
      safe=["knee_injury", "ankle_injury", "hip_injury"] and ["knee_injury", "ankle_injury"],
      why="Encogimiento de hombros: carga directa sobre trapecio y cervical. "
           "Banda bajo los pies = carga axial baja pero real."),

    E("1017", "band y-raise", "standing", standing=True, bal="low", grip="light",
      oh=True, axial="low", stress=js(sh="high", cerv="low", lumbar="low"),
      pat="isolation", diff=2, rom="moderate",
      contra=["cannot_stand", "no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["hypertension"], safe=["knee_injury", "ankle_injury"],
      why="La Y termina por encima de la cabeza: no_overhead es contraindicacion dura. "
           "Elevacion con brazo extendido es la posicion clasica de pinzamiento."),

    E("3292", "elevator", "standing", standing=True, bal="moderate", grip="none",
      axial="moderate", flex="moderate",
      stress=js(lumbar="high", hip="moderate", knee="low"),
      pat="hinge", diff=2, rom="moderate",
      contra=["cannot_stand", "lumbar_disc", "limited_balance"],
      caut=["lumbar_pain", "hypertension", "vertigo", "elderly_65plus", "glaucoma"],
      why="Flexion de tronco sin apoyo. Aunque no hay peso externo, la columna "
           "sostiene el torso en voladizo: lumbar alto. Cabeza abajo => glaucoma e hipertension."),

    E("1471", "inchworm", "standing", floor=True, standing=True, bal="moderate",
      grip="none", flex="moderate", stress=js(sh="moderate", lumbar="moderate",
      wr="moderate", hip="moderate"),
      pat="core_antiextension", diff=3, rom="high",
      contra=["cannot_stand", "cannot_get_on_floor", "wrist_injury", "lumbar_disc"],
      caut=["shoulder_impingement", "pregnancy_2nd", "pregnancy_3rd", "elderly_65plus", "obesity"],
      why="Transita de pie a plancha con las manos: exige bajar al suelo y "
           "cargar munecas. Doble restriccion de Capa A."),

    # ---------------- SENTADO ----------------
    E("1016", "band wrist curl", "seated", bal="none", grip="light",
      stress=js(wr="moderate", el="low"), pat="isolation", diff=1, rom="low",
      caut=["wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury",
            "hip_replacement", "lumbar_disc", "elderly_65plus"],
      why="Sentado, sin carga axial, sin equilibrio. Candidato ideal para "
           "perfil con movilidad muy reducida. Solo la muneca es relevante."),

    E("0126", "barbell wrist curl", "seated", bal="none", grip="firm",
      stress=js(wr="high", el="low"), pat="isolation", diff=2, rom="low",
      contra=["wrist_injury", "limited_grip"], caut=["elbow_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury"],
      why="Identico al anterior pero con barra: la muneca pasa de moderate a high "
           "y limited_grip se vuelve contraindicacion. Buen ejemplo de como el "
           "equipamiento cambia el perfil de riesgo del mismo movimiento."),

    E("3533", "quads (bodyweight squat)", "standing", standing=True, bal="moderate",
      grip="none", axial="low", stress=js(knee="high", hip="moderate", lumbar="low",
      ank="moderate"), pat="squat", diff=2, rom="moderate",
      contra=["cannot_stand", "knee_injury", "knee_replacement"],
      caut=["limited_balance", "hip_replacement", "elderly_65plus", "obesity"],
      safe=["shoulder_impingement", "wrist_injury", "limited_grip", "no_overhead"],
      why="Sentadilla sin peso: la regresion natural de la sentadilla con barra. "
           "Sin carga axial ni agarre, por eso es safe_for para todo el tren superior."),

    E("3287", "elbow dips (bench dip)", "seated", bal="low", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury", "limited_grip"],
      caut=["wrist_injury"], safe=["knee_injury", "ankle_injury", "lumbar_disc"],
      why="El fondo en banco pone el hombro en extension e rotacion interna bajo "
           "carga: es la posicion de mayor riesgo de pinzamiento del catalogo."),

    E("0814", "triceps dip", "seated", bal="low", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=2, rom="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury", "limited_grip"],
      caut=["wrist_injury"], safe=["knee_injury", "ankle_injury"],
      why="Mismo patron que elbow dips. Se anotan los dos a proposito: son "
           "duplicados funcionales y deben caer en el mismo substitute_group."),

    E("0639", "one arm dip", "seated", bal="moderate", grip="firm",
      stress=js(sh="high", el="high", wr="high"),
      lat="unilateral", pat="horizontal_push", diff=4, rom="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury",
              "wrist_injury", "limited_grip"],
      caut=["hypertension"],
      why="Version a un brazo: todo el peso en una articulacion. Sube a difficulty 4 "
           "y la muneca pasa a high. E1 lo marco 'standing' por error - se corrige aca."),

    E("2329", "spine twist", "seated", floor=True, bal="low", grip="none",
      flex="low", rot="high", stress=js(lumbar="moderate", cerv="moderate"),
      pat="core_rotation", diff=2, rom="moderate",
      contra=["cannot_get_on_floor", "lumbar_disc", "cervical_injury"],
      caut=["lumbar_pain", "osteoporosis", "hernia_abdominal",
            "pregnancy_2nd", "pregnancy_3rd"],
      why="Rotacion lumbar bajo flexion: combinacion desaconsejada con disco. "
           "Sentado en el suelo, no en silla: exige bajar al suelo."),

    E("0689", "seated leg raise", "seated", bal="low", grip="light",
      flex="low", stress=js(hip="moderate", lumbar="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      contra=["lumbar_disc"],
      caut=["lumbar_pain", "hip_replacement", "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury",
            "shoulder_impingement", "no_overhead"],
      why="En banco, tren superior libre. Muy buen candidato para silla de ruedas "
           "si hay control de tronco. El psoas tracciona la lumbar: por eso no es safe_for lumbar."),

    E("0372", "dumbbell preacher curl", "seated_machine", bal="none", grip="firm",
      stress=js(el="high", wr="moderate", sh="low"),
      pat="isolation", diff=2, rom="moderate",
      contra=["elbow_injury", "limited_grip"], caut=["wrist_injury"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury",
            "lumbar_disc", "hip_replacement", "elderly_65plus"],
      why="Banco predicador: el brazo queda fijo, cero compensacion de tronco. "
           "Uno de los ejercicios mas seguros del catalogo para movilidad reducida. "
           "El codo en extension completa bajo carga es el unico riesgo real."),

    # ---------------- DE PIE · fuerza ----------------
    E("1004", "band squat", "standing", standing=True, bal="moderate", grip="none",
      axial="low", stress=js(knee="moderate", hip="moderate", lumbar="low", ank="moderate"),
      pat="squat", diff=2, rom="moderate",
      contra=["cannot_stand", "knee_injury", "knee_replacement"],
      caut=["limited_balance", "hip_replacement", "elderly_65plus"],
      safe=["shoulder_impingement", "wrist_injury", "no_overhead", "limited_grip"],
      why="La banda sobre las rodillas agrega resistencia lateral sin carga axial: "
           "por eso rodilla queda moderate y no high como en la sentadilla con barra."),

    E("0514", "jump squat", "standing", standing=True, bal="high", grip="none",
      axial="low", impact="high",
      stress=js(knee="high", hip="high", lumbar="moderate", ank="high"),
      pat="squat", diff=4, rom="moderate",
      contra=["cannot_stand", "limited_balance", "knee_injury", "knee_replacement",
              "ankle_injury", "hip_replacement", "osteoporosis",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cardiac", "hypertension", "obesity", "elderly_65plus", "lumbar_disc"],
      why="Pliometrico: el aterrizaje multiplica la carga articular. impact high "
           "activa casi todas las contraindicaciones de tren inferior a la vez."),

    E("0032", "barbell deadlift", "standing", standing=True, bal="moderate", grip="firm",
      axial="high", flex="moderate",
      stress=js(knee="moderate", hip="high", lumbar="high", sh="low", wr="moderate", ank="low"),
      pat="hinge", diff=4, rom="high",
      contra=["cannot_stand", "lumbar_disc", "limited_grip", "osteoporosis",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "hypertension", "cardiac", "knee_injury",
            "hip_replacement", "elderly_65plus"],
      why="Maxima carga axial del catalogo junto con la sentadilla. Bisagra de cadera "
           "con la columna en voladizo: cualquier patologia lumbar lo descarta."),

    E("0499", "inverted row", "hanging", bal="low", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=2, rom="moderate",
      contra=["limited_grip", "wrist_injury"],
      caut=["shoulder_impingement", "elbow_injury", "cannot_stand"],
      safe=["knee_injury", "hip_replacement", "lumbar_disc", "no_overhead"],
      why="E1 lo marco standing: en realidad el cuerpo cuelga de la barra con los "
           "talones apoyados. Es la regresion accesible de la dominada - tiron "
           "horizontal sin carga sobre la columna."),

    E("0808", "suspended row", "hanging", bal="moderate", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      contra=["limited_grip", "wrist_injury"],
      caut=["shoulder_impingement", "elbow_injury", "limited_balance"],
      safe=["knee_injury", "hip_replacement", "lumbar_disc", "no_overhead"],
      why="Igual al inverted row pero con anclaje inestable: sube equilibrio y dificultad."),

    E("1008", "band step-up", "standing", standing=True, bal="high", sl=True,
      grip="none", axial="low", impact="low",
      stress=js(knee="high", hip="moderate", ank="moderate", lumbar="low"),
      lat="alternating", pat="lunge", diff=3, rom="moderate",
      contra=["cannot_stand", "limited_balance", "knee_injury", "knee_replacement"],
      caut=["hip_replacement", "vertigo", "elderly_65plus", "obesity", "pregnancy_3rd"],
      safe=["shoulder_impingement", "wrist_injury", "no_overhead", "limited_grip"],
      why="Apoyo unipodal sobre plataforma elevada: equilibrio alto y riesgo de caida. "
           "limited_balance es contraindicacion dura, no precaucion."),

    E("0685", "run / jog in place", "standing", standing=True, bal="moderate",
      grip="none", impact="moderate",
      stress=js(knee="moderate", hip="moderate", ank="high", lumbar="low"),
      lat="alternating", pat="cardio_steady", diff=2, rom="low",
      contra=["cannot_stand", "limited_balance", "ankle_injury",
              "knee_replacement", "hip_replacement"],
      caut=["cardiac", "hypertension", "knee_injury", "obesity", "osteoporosis",
            "elderly_65plus", "pregnancy_3rd"],
      why="Impacto repetitivo. cardiac e hypertension son Capa C: advierten, no excluyen. "
           "Las protesis si excluyen: el impacto ciclico las compromete."),

    E("0997", "band shoulder press", "standing", standing=True, bal="low", grip="light",
      oh=True, axial="moderate",
      stress=js(sh="high", el="moderate", cerv="low", lumbar="moderate", wr="low"),
      pat="vertical_push", diff=2, rom="high",
      contra=["cannot_stand", "no_overhead", "shoulder_impingement", "rotator_cuff"],
      caut=["hypertension", "cervical_injury", "lumbar_pain", "elbow_injury"],
      safe=["knee_injury", "ankle_injury", "hip_replacement"],
      why="Press vertical de pie: el brazo sobre la cabeza transmite carga a la lumbar "
           "por compensacion. rom_demand alto - mucha gente no llega sin arquear la espalda."),

    # ---------------- PLANCHA ----------------
    E("0662", "push-up", "plank", floor=True, bal="low", grip="none",
      ext="low", stress=js(sh="moderate", el="moderate", wr="high", lumbar="low"),
      pat="horizontal_push", diff=2, rom="moderate",
      contra=["cannot_get_on_floor", "wrist_injury"],
      caut=["shoulder_impingement", "elbow_injury", "lumbar_pain",
            "pregnancy_3rd", "obesity"],
      safe=["knee_injury", "ankle_injury", "hip_replacement", "limited_balance"],
      why="La muneca en extension de 90 grados soportando peso corporal es el "
           "limitante real, mas que el hombro. Exige bajar al suelo."),

    E("1273", "clap push up", "plank", floor=True, bal="moderate", grip="none",
      impact="high", stress=js(sh="high", el="high", wr="high", lumbar="low"),
      pat="horizontal_push", diff=5, rom="moderate",
      contra=["cannot_get_on_floor", "wrist_injury", "elbow_injury",
              "shoulder_impingement", "rotator_cuff", "osteoporosis"],
      caut=["cardiac", "hypertension", "obesity"],
      why="Pliometrico de tren superior: el aterrizaje sobre las manos es impacto "
           "directo sobre muneca y codo. Progresion del push-up estandar."),

    E("0493", "incline push-up", "bench_incline", bal="low", grip="none",
      stress=js(sh="low", el="low", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=1, rom="low",
      caut=["wrist_injury", "shoulder_impingement"],
      safe=["cannot_get_on_floor", "knee_injury", "ankle_injury",
            "hip_replacement", "limited_balance", "obesity", "elderly_65plus"],
      why="Regresion clave del push-up: al elevar las manos baja la carga y NO exige "
           "bajar al suelo. Es la sustitucion natural para cannot_get_on_floor."),

    E("3301", "frog planche", "plank", floor=True, bal="high", grip="none",
      ext="moderate", stress=js(sh="high", el="high", wr="high", lumbar="moderate"),
      pat="core_antiextension", diff=5, rom="high",
      contra=["cannot_get_on_floor", "wrist_injury", "elbow_injury",
              "shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["hypertension", "hernia_abdominal"],
      why="Calistenia avanzada. Todo el peso sobre munecas en maxima extension. "
           "difficulty 5: sirve como techo de la escala."),

    # ---------------- SUPINO ----------------
    E("1014", "band v-up", "supine", floor=True, bal="none", grip="light", oh=True,
      flex="high", stress=js(lumbar="high", cerv="moderate", hip="moderate", sh="low"),
      pat="core_flexion", diff=3, rom="high",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cervical_injury", "lumbar_pain", "osteoporosis", "no_overhead"],
      why="Flexion espinal completa bajo tension: contraindicado en disco y hernia. "
           "Supino desde 2do trimestre comprime la vena cava."),

    E("0001", "3/4 sit-up", "supine", floor=True, bal="none", grip="none",
      flex="high", stress=js(lumbar="moderate", cerv="high", hip="moderate"),
      pat="core_flexion", diff=2, rom="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "cervical_injury", "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "osteoporosis", "elderly_65plus"],
      why="Manos detras de la cabeza => la gente tracciona el cuello: cervical high. "
           "Es el error de ejecucion mas comun del catalogo."),

    E("0260", "cocoons", "supine", floor=True, bal="none", grip="none",
      flex="high", stress=js(lumbar="moderate", cerv="moderate", hip="high"),
      pat="core_flexion", diff=3, rom="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "osteoporosis"],
      why="ATENCION: el dataset le puso a este ejercicio el mismo texto que a "
           "3/4 sit-up. La clasificacion se corrige segun el nombre real "
           "(cocoon = rodillas al pecho + elevacion de tronco), no segun el texto."),

    E("0641", "otis up", "supine", floor=True, bal="none", grip="light",
      flex="high", stress=js(lumbar="high", cerv="moderate", hip="moderate", sh="low"),
      pat="core_flexion", diff=3, rom="moderate",
      contra=["cannot_get_on_floor", "cannot_lie_supine", "lumbar_disc",
              "hernia_abdominal", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "cervical_injury", "osteoporosis"],
      why="Sit-up con peso sostenido: la carga en las manos aumenta el brazo de "
           "palanca sobre la lumbar. Mismo problema de texto duplicado."),

    E("3016", "curl-up", "supine", floor=True, bal="none", grip="none",
      flex="moderate", stress=js(lumbar="low", cerv="moderate", hip="low"),
      pat="core_flexion", diff=1, rom="low",
      contra=["cannot_get_on_floor", "cannot_lie_supine",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["cervical_injury", "lumbar_disc", "hernia_abdominal"],
      why="Recorrido corto: es la regresion segura del sit-up. Lumbar baja de "
           "moderate a low precisamente porque no despega la zona lumbar del suelo."),

    E("0073", "barbell pullover", "bench_supine", bal="low", grip="firm", oh=True,
      ext="moderate", stress=js(sh="high", lumbar="moderate", el="moderate", wr="moderate"),
      pat="vertical_pull", diff=3, rom="high",
      contra=["no_overhead", "shoulder_impingement", "rotator_cuff", "limited_grip",
              "pregnancy_2nd", "pregnancy_3rd"],
      caut=["lumbar_pain", "elbow_injury", "hypertension"],
      safe=["knee_injury", "ankle_injury", "cannot_stand", "limited_balance"],
      why="Flexion de hombro maxima con carga: rom_demand alto. La caja toracica "
           "se abre y arquea la lumbar. Cero demanda de tren inferior."),

    E("0308", "dumbbell fly", "bench_supine", bal="low", grip="firm",
      stress=js(sh="high", el="moderate", wr="low", lumbar="low"),
      pat="horizontal_push", diff=3, rom="high",
      contra=["shoulder_impingement", "rotator_cuff", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["elbow_injury", "limited_grip"],
      safe=["knee_injury", "ankle_injury", "cannot_stand", "limited_balance",
            "hip_replacement", "lumbar_disc"],
      why="Apertura: el hombro llega a rotacion externa maxima bajo carga. "
           "rom_demand alto pese a ser un movimiento simple."),

    E("0057", "barbell lying extension", "bench_supine", bal="low", grip="firm",
      stress=js(el="high", sh="moderate", wr="moderate"),
      pat="isolation", diff=3, rom="moderate",
      contra=["elbow_injury", "limited_grip", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["shoulder_impingement", "wrist_injury"],
      safe=["knee_injury", "ankle_injury", "cannot_stand", "limited_balance", "lumbar_disc"],
      why="Rompecraneos: el codo es la articulacion critica, no el hombro. "
           "Ejemplo de que el estres no siempre cae donde esta el musculo objetivo."),

    # ---------------- BANCO INCLINADO ----------------
    E("0318", "dumbbell incline curl", "bench_incline", bal="none", grip="firm",
      stress=js(el="moderate", sh="moderate", wr="low"),
      pat="isolation", diff=2, rom="high",
      contra=["limited_grip", "elbow_injury"],
      caut=["shoulder_impingement"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury",
            "hip_replacement", "lumbar_disc", "elderly_65plus"],
      why="El brazo colgando detras del cuerpo estira el biceps al maximo: "
           "rom_demand alto. Muy seguro para todo lo que no sea codo u hombro."),

    E("0316", "dumbbell incline press", "bench_incline", bal="low", grip="firm",
      stress=js(sh="high", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_push", diff=3, rom="moderate",
      contra=["shoulder_impingement", "rotator_cuff", "limited_grip"],
      caut=["elbow_injury", "wrist_injury", "pregnancy_3rd"],
      safe=["knee_injury", "ankle_injury", "cannot_stand", "limited_balance", "lumbar_disc"],
      why="Inclinado, no supino: la cabeza queda elevada, por eso el embarazo "
           "es solo precaucion en 3er trimestre y no contraindicacion desde el 2do."),

    E("0049", "barbell incline row", "bench_prone", bal="none", grip="firm",
      stress=js(sh="moderate", el="moderate", wr="moderate", lumbar="low"),
      pat="horizontal_pull", diff=3, rom="moderate",
      contra=["cannot_lie_prone", "limited_grip"],
      caut=["shoulder_impingement", "elbow_injury", "wrist_injury",
            "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["knee_injury", "ankle_injury", "cannot_stand", "lumbar_disc",
            "limited_balance", "hip_replacement"],
      why="E1 lo marco bench_incline: en realidad va boca abajo sobre el banco. "
           "Es bench_prone. El pecho apoyado elimina toda carga lumbar - "
           "excelente remo para quien no puede cargar la columna."),

    E("1665", "dumbbell one arm prone curl", "bench_prone", bal="none", grip="firm",
      stress=js(el="moderate", sh="low", wr="low"),
      lat="unilateral", pat="isolation", diff=2, rom="moderate",
      contra=["cannot_lie_prone", "limited_grip"],
      caut=["elbow_injury", "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      safe=["cannot_stand", "limited_balance", "knee_injury", "ankle_injury",
            "lumbar_disc", "hip_replacement"],
      why="Boca abajo: cero carga axial y cero equilibrio. cannot_lie_prone "
           "es la unica restriccion de Capa A que aplica."),

    # ---------------- COLGADO ----------------
    E("1326", "chin-up", "hanging", bal="none", grip="hanging_bodyweight", oh=True,
      stress=js(sh="high", el="high", wr="high", lumbar="low"),
      pat="vertical_pull", diff=4, rom="high",
      contra=["limited_grip", "no_overhead", "shoulder_impingement",
              "rotator_cuff", "elbow_injury", "wrist_injury"],
      caut=["hypertension", "obesity", "elderly_65plus"],
      safe=["knee_injury", "ankle_injury", "hip_replacement", "cannot_stand",
            "limited_balance", "knee_replacement"],
      why="Supinado carga mas el biceps y el codo que la dominada pronada. "
           "Cero demanda de tren inferior: opcion potente para lesion de rodilla o cadera."),

    E("0631", "muscle up", "hanging", bal="moderate", grip="hanging_bodyweight", oh=True,
      stress=js(sh="high", el="high", wr="high", lumbar="moderate"),
      pat="vertical_pull", diff=5, rom="high",
      contra=["limited_grip", "no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "wrist_injury", "cervical_injury"],
      caut=["hypertension", "cardiac", "obesity"],
      why="La transicion sobre la barra es el momento de mayor riesgo de hombro "
           "del catalogo entero. difficulty 5."),

    E("0638", "one arm chin-up", "hanging", bal="moderate", grip="hanging_bodyweight",
      oh=True, stress=js(sh="high", el="high", wr="high", lumbar="moderate"),
      lat="unilateral", pat="vertical_pull", diff=5, rom="high",
      contra=["limited_grip", "no_overhead", "shoulder_impingement", "rotator_cuff",
              "elbow_injury", "wrist_injury"],
      caut=["hypertension", "obesity"],
      why="E1 lo marco standing por la primera oracion ('Stand facing a pull-up bar'). "
           "Es hanging. Ejemplo de por que la ventana de texto puede enganar."),

    E("0251", "chest dip", "hanging", bal="moderate", grip="firm",
      stress=js(sh="high", el="high", wr="moderate"),
      pat="horizontal_push", diff=4, rom="high",
      contra=["shoulder_impingement", "rotator_cuff", "elbow_injury", "limited_grip"],
      caut=["wrist_injury", "hypertension", "obesity"],
      safe=["knee_injury", "ankle_injury", "hip_replacement", "cannot_stand"],
      why="Fondos en paralelas: hombro por debajo del codo en maxima flexion. "
           "Mucho mas exigente que el fondo en banco. E1 no resolvio la postura."),

    E("3303", "flag (human flag)", "hanging", bal="high", grip="hanging_bodyweight",
      rot="high", stress=js(sh="high", el="moderate", wr="high", lumbar="high"),
      lat="unilateral", pat="core_rotation", diff=5, rom="high",
      contra=["limited_grip", "no_overhead", "shoulder_impingement", "rotator_cuff",
              "wrist_injury", "lumbar_disc", "osteoporosis"],
      caut=["hypertension", "cardiac"],
      why="Ejercicio de exhibicion. Se anota para fijar el extremo superior de "
           "la escala: si algo llega a difficulty 5, se parece a esto."),

    # ---------------- POSTURAS RARAS (Capa A) ----------------
    E("0084", "barbell rollerout", "kneeling", floor=True, bal="moderate", grip="firm",
      ext="high", stress=js(lumbar="high", sh="high", knee="moderate",
      el="moderate", wr="moderate"),
      pat="core_antiextension", diff=4, rom="moderate",
      contra=["cannot_kneel", "cannot_get_on_floor", "lumbar_disc", "limited_grip",
              "shoulder_impingement", "hernia_abdominal",
              "pregnancy_1st", "pregnancy_2nd", "pregnancy_3rd"],
      caut=["knee_injury", "knee_replacement", "elderly_65plus"],
      why="Anti-extension: el riesgo es que la lumbar ceda a hiperextension si el "
           "core falla. Doble restriccion de Capa A: arrodillarse y bajar al suelo."),

    E("3360", "bear crawl", "quadruped", floor=True, bal="moderate", grip="none",
      impact="low", stress=js(sh="high", wr="high", knee="low", lumbar="moderate", hip="moderate"),
      lat="alternating", pat="cardio_steady", diff=3, rom="moderate",
      contra=["cannot_get_on_floor", "wrist_injury", "shoulder_impingement"],
      caut=["cardiac", "hypertension", "knee_injury", "obesity",
            "pregnancy_2nd", "pregnancy_3rd", "elderly_65plus"],
      why="Cuadrupedia con rodillas suspendidas: carga sostenida sobre munecas "
           "mientras se desplaza. Unico ejemplo de quadruped + cardio del gold set."),

    E("1604", "world's greatest stretch", "half_kneeling", floor=True, bal="moderate",
      grip="none", rot="high", ext="moderate",
      stress=js(hip="moderate", knee="moderate", lumbar="low", sh="low"),
      lat="unilateral", pat="isolation", diff=2, rom="high",
      contra=["cannot_kneel", "cannot_get_on_floor", "knee_replacement"],
      caut=["hip_replacement", "knee_injury", "lumbar_disc", "vertigo",
            "elderly_65plus", "pregnancy_3rd"],
      why="Movilidad, no fuerza: difficulty 2 pero rom_demand high. La distincion "
           "clave que el modelo suele confundir. Unico half_kneeling del gold set."),
]


def main():
    gold = json.load(open(GOLD, encoding="utf-8"))
    have = {e["exercise_id"] for e in gold["examples"]}
    added = [e for e in NEW if e["exercise_id"] not in have]
    gold["examples"].extend(added)
    gold["_note"] = gold.get("_note", "") + (
        " | v1.2: +45 ejemplos anotados en conversacion, cubriendo el espacio "
        "start_position x movement_pattern y las posturas de Capa A "
        "(kneeling, half_kneeling, quadruped, prone, hanging).")
    json.dump(gold, open(GOLD, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    from collections import Counter
    print(f"agregados: {len(added)}   total gold: {len(gold['examples'])}\n")
    print("cobertura de start_position:")
    for k, v in Counter(e["start_position"] for e in gold["examples"]).most_common():
        print(f"  {k:16s} {v}")
    print("\ncobertura de movement_pattern:")
    for k, v in Counter(e.get("movement_pattern") for e in gold["examples"]).most_common():
        print(f"  {str(k):22s} {v}")


if __name__ == "__main__":
    main()
