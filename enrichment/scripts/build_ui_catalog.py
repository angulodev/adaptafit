#!/usr/bin/env python3
"""
Prepara el catalogo para la UI.

Hace tres cosas:
  1. Deduplica: colapsa fichas con firma de clasificacion identica.
  2. Traduce los nombres al espanol con un glosario por tokens.
  3. Exporta un JSON compacto (condiciones indexadas por entero).

Uso:  python3 build_ui_catalog.py
Sale: ui/catalog.json
"""

import json
import os
import re
import collections

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "source", "exercises.json")
MANUAL = os.path.join(BASE, "output", "manual_classified.json")
TAX = os.path.join(BASE, "taxonomy", "taxonomy_v1.json")
OUTDIR = os.path.join(os.path.dirname(BASE), "ui")

# --- Zonas del mapa corporal -------------------------------------------------
TARGET_ZONA = {
    "pectorals": "pecho", "serratus anterior": "pecho",
    "delts": "hombros", "levator scapulae": "hombros", "traps": "hombros",
    "biceps": "biceps", "triceps": "triceps", "forearms": "antebrazos",
    "abs": "core", "spine": "lumbar",
    "upper back": "espalda", "lats": "espalda",
    "glutes": "gluteos", "quads": "cuadriceps",
    "hamstrings": "isquios", "calves": "gemelos",
    "abductors": "caderas", "adductors": "caderas",
    "cardiovascular system": "cardio",
}
# cara del cuerpo en la que se dibuja cada zona
ZONA_CARA = {
    "pecho": "frente", "hombros": "frente", "biceps": "frente",
    "antebrazos": "frente", "core": "frente", "cuadriceps": "frente",
    "caderas": "frente", "gemelos": "espalda", "espalda": "espalda",
    "triceps": "espalda", "lumbar": "espalda", "gluteos": "espalda",
    "isquios": "espalda", "cardio": "frente",
}

EQUIPO_ES = {
    "body weight": "Peso corporal", "dumbbell": "Mancuernas",
    "barbell": "Barra", "band": "Banda elástica",
    "resistance band": "Banda elástica", "weighted": "Peso libre",
    "ez barbell": "Barra EZ", "olympic barbell": "Barra olímpica",
}

COND_ES = {
    # Capa A — movilidad
    "cannot_stand": "No puedo estar de pie",
    "cannot_get_on_floor": "No puedo bajar al suelo",
    "cannot_kneel": "No puedo arrodillarme",
    "cannot_lie_prone": "No puedo tumbarme boca abajo",
    "cannot_lie_supine": "No puedo tumbarme boca arriba",
    "cannot_lie_on_side": "No puedo tumbarme de lado",
    "no_overhead": "No puedo levantar los brazos por encima de la cabeza",
    "limited_grip": "Agarre limitado",
    "limited_balance": "Equilibrio limitado",
    "wheelchair": "Uso silla de ruedas",
    "cannot_sit_unsupported": "No puedo sentarme sin respaldo",
    "cannot_transfer_to_bench": "No puedo pasarme a un banco",
    "one_arm_only": "Solo tengo un brazo funcional",
    "visual_impairment": "Discapacidad visual",
    # Capa B — lesión articular
    "lumbar_disc": "Hernia discal lumbar",
    "lumbar_pain": "Dolor lumbar",
    "cervical_injury": "Lesión cervical",
    "shoulder_impingement": "Pinzamiento de hombro",
    "rotator_cuff": "Manguito rotador",
    "knee_injury": "Lesión de rodilla",
    "knee_replacement": "Prótesis de rodilla",
    "hip_replacement": "Prótesis de cadera",
    "ankle_injury": "Lesión de tobillo",
    "wrist_injury": "Lesión de muñeca",
    "elbow_injury": "Lesión de codo",
    "knee_pain": "Dolor de rodilla",
    "shoulder_pain": "Dolor de hombro",
    "neck_pain": "Dolor de cuello",
    "hip_pain": "Dolor de cadera",
    "sciatica": "Ciática",
    "si_joint_pain": "Dolor sacroilíaco",
    "plantar_fasciitis": "Fascitis plantar",
    "tendinitis_elbow": "Epicondilitis",
    "carpal_tunnel": "Túnel carpiano",
    "osteoarthritis": "Artrosis",
    "rheumatoid_arthritis": "Artritis reumatoide",
    # Capa C — sistémica
    "hypertension": "Hipertensión",
    "cardiac": "Cardiopatía",
    "osteoporosis": "Osteoporosis",
    "hernia_abdominal": "Hernia abdominal",
    "pregnancy_1st": "Embarazo, primer trimestre",
    "pregnancy_2nd": "Embarazo, segundo trimestre",
    "pregnancy_3rd": "Embarazo, tercer trimestre",
    "vertigo": "Vértigo",
    "glaucoma": "Glaucoma",
    "obesity": "Obesidad",
    "elderly_65plus": "Más de 65 años",
    "dysautonomia": "Disautonomía",
    "chronic_fatigue": "Fatiga crónica",
    "fibromyalgia": "Fibromialgia",
    "hypermobility": "Hipermovilidad",
    "multiple_sclerosis": "Esclerosis múltiple",
    "asthma": "Asma",
    "diabetes": "Diabetes",
    "epilepsy": "Epilepsia",
    "migraine": "Migraña",
    "anemia": "Anemia",
    "varicose_veins": "Varices",
    "postpartum": "Posparto",
    "pelvic_floor_dysfunction": "Disfunción del suelo pélvico",
    "recent_abdominal_surgery": "Cirugía abdominal reciente",
    "retinal_detachment_risk": "Riesgo de desprendimiento de retina",
}

POS_ES = {
    "standing": "De pie", "seated": "Sentado", "supine": "Boca arriba",
    "prone": "Boca abajo", "side_lying": "De lado", "kneeling": "De rodillas",
    "quadruped": "Cuadrupedia", "plank": "Plancha",
    "bench_supine": "Banco, boca arriba", "bench_prone": "Banco, boca abajo",
    "bench_seated": "Banco, sentado", "hanging": "Suspendido",
    "wall_supported": "Apoyado en pared",
}

# --- Traduccion de nombres --------------------------------------------------
# El ingles pone el sustantivo del movimiento al final ("band reverse wrist
# curl"); el espanol lo pone al principio ("curl de muneca invertido con
# banda"). Por eso no basta un glosario token a token: hay que clasificar cada
# fragmento en un rol y reensamblar la frase. Traduccion mecanica y
# provisional, pendiente de revision editorial.

# Se buscan primero las expresiones de varias palabras.
FRASES = [
    ("bent over",         "pos", "inclinado"),
    ("bent-over",         "pos", "inclinado"),
    ("close grip",        "mod", "agarre cerrado"),
    ("close-grip",        "mod", "agarre cerrado"),
    ("wide grip",         "mod", "agarre abierto"),
    ("wide-grip",         "mod", "agarre abierto"),
    ("narrow stance",     "mod", "postura estrecha"),
    ("reverse grip",      "mod", "agarre invertido"),
    ("underhand grip",    "mod", "agarre supino"),
    ("overhand grip",     "mod", "agarre prono"),
    ("neutral grip",      "mod", "agarre neutro"),
    ("cross body",        "mod", "cruzado"),
    ("cross-body",        "mod", "cruzado"),
    ("one arm",           "lat", "a un brazo"),
    ("one-arm",           "lat", "a un brazo"),
    ("two arm",           "lat", "a dos brazos"),
    ("single leg",        "lat", "a una pierna"),
    ("one leg",           "lat", "a una pierna"),
    ("two legs",          "lat", "a dos piernas"),
    ("single arm",        "lat", "a un brazo"),
    ("split squat",       "mov", "Zancada"),
    ("side split squat",  "mov", "Zancada lateral"),
    ("squat jump",        "mov", "Sentadilla con salto"),
    ("calf raise",        "mov", "Elevación de talon"),
    ("lateral raise",     "mov", "Elevación lateral"),
    ("front raise",       "mov", "Elevación frontal"),
    ("rear lateral raise", "mov", "Elevación posterior"),
    ("leg raise",         "mov", "Elevación de piernas"),
    ("hip thrust",        "mov", "Empuje de cadera"),
    ("toe touch",         "mov", "Toque de punta"),
    ("wrist curl",        "mov", "Curl de muñeca"),
    ("hammer curl",       "mov", "Curl martillo"),
    ("preacher curl",     "mov", "Curl predicador"),
    ("concentration curl", "mov", "Curl de concentración"),
    ("spider curl",       "mov", "Curl spider"),
    ("biceps curl",       "mov", "Curl de bíceps"),
    ("bicep curl",        "mov", "Curl de bíceps"),
    ("triceps extension", "mov", "Extensión de triceps"),
    ("tricep extension",  "mov", "Extensión de triceps"),
    ("triceps kickback",  "mov", "Patada de tríceps"),
    ("tricep kickback",   "mov", "Patada de tríceps"),
    ("triceps dip",       "mov", "Fondo de tríceps"),
    ("bench press",       "mov", "Press de banca"),
    ("chest dip",         "mov", "Fondo de pecho"),
    ("pelvic tilt",       "mov", "Báscula pélvica"),
    ("shoulder press",    "mov", "Press de hombro"),
    ("chest press",       "mov", "Press de pecho"),
    ("leg press",         "mov", "Prensa de piernas"),
    ("push up",           "mov", "Flexión"),
    ("push-up",           "mov", "Flexión"),
    ("pull up",           "mov", "Dominada"),
    ("pull-up",           "mov", "Dominada"),
    ("chin up",           "mov", "Dominada supina"),
    ("sit up",            "mov", "Abdominal"),
    ("sit-up",            "mov", "Abdominal"),
    ("clean and press",   "mov", "Cargada y press"),
    ("power clean",       "mov", "Cargada de potencia"),
    ("rear delt",         "part", "de deltoides posterior"),
    ("upper back",        "part", "de espalda alta"),
    ("lower back",        "part", "lumbar"),
    ("stork stance",      "mod", "en postura stork"),
    ("with towel",        "mod", "con toalla"),
    ("with arm blaster",  "mod", "con arm blaster"),
    ("exercise ball",     "eq",  "con pelota de pilates"),
    ("stability ball",    "eq",  "con pelota de estabilidad"),
    ("medicine ball",     "eq",  "con balon medicinal"),
    ("ez barbell",        "eq",  "con barra EZ"),
    ("ez bar",            "eq",  "con barra EZ"),
    ("ez-bar",            "eq",  "con barra EZ"),
    ("ez-barbell",        "eq",  "con barra EZ"),
    ("olympic barbell",   "eq",  "con barra olímpica"),
    ("body weight",       "eq",  ""),
    ("resistance band",   "eq",  "con banda elástica"),
]

PALABRAS = {
    # movimiento (sustantivo principal)
    "squat": ("mov", "Sentadilla"), "squats": ("mov", "Sentadillas"),
    "lunge": ("mov", "Zancada"), "lunges": ("mov", "Zancadas"),
    "deadlift": ("mov", "Peso muerto"), "press": ("mov", "Press"),
    "row": ("mov", "Remo"), "curl": ("mov", "Curl"),
    "curls": ("mov", "Curls"), "extension": ("mov", "Extensión"),
    "extensions": ("mov", "Extensiónes"), "raise": ("mov", "Elevación"),
    "raises": ("mov", "Elevaciónes"), "fly": ("mov", "Apertura"),
    "flyes": ("mov", "Aperturas"), "flys": ("mov", "Aperturas"),
    "pulldown": ("mov", "Jalón"), "pullover": ("mov", "Pullover"),
    "pushup": ("mov", "Flexión"), "pushups": ("mov", "Flexiónes"),
    "pullup": ("mov", "Dominada"), "crunch": ("mov", "Encogimiento"),
    "crunches": ("mov", "Encogimientos"), "plank": ("mov", "Plancha"),
    "bridge": ("mov", "Puente"), "shrug": ("mov", "Encogimiento de hombros"),
    "kickback": ("mov", "Patada"), "dip": ("mov", "Fondo"),
    "dips": ("mov", "Fondos"), "twist": ("mov", "Giro"),
    "stretch": ("mov", "Estiramiento"), "jump": ("mov", "Salto"),
    "jumps": ("mov", "Saltos"), "clean": ("mov", "Cargada"),
    "snatch": ("mov", "Arrancada"), "jerk": ("mov", "Envión"),
    "burpee": ("mov", "Burpee"), "swing": ("mov", "Swing"),
    "thrust": ("mov", "Empuje"), "pull": ("mov", "Tirón"),
    "walk": ("mov", "Caminata"), "hold": ("mov", "Isométrico"),
    "circles": ("mov", "Círculos"), "rotation": ("mov", "Rotación"),
    # parte del cuerpo
    "wrist": ("part", "de muñeca"), "chest": ("part", "de pecho"),
    "shoulder": ("part", "de hombro"), "shoulders": ("part", "de hombros"),
    "biceps": ("part", "de bíceps"), "bicep": ("part", "de bíceps"),
    "triceps": ("part", "de tríceps"), "tricep": ("part", "de tríceps"),
    "calf": ("part", "de gemelo"), "leg": ("part", "de pierna"),
    "legs": ("part", "de piernas"), "hip": ("part", "de cadera"),
    "glute": ("part", "de glúteo"), "abs": ("part", "abdominal"),
    "neck": ("part", "de cuello"), "back": ("part", "de espalda"),
    "forearm": ("part", "de antebrazo"), "finger": ("part", "de dedos"),
    "adductor": ("part", "de aductores"), "abductor": ("part", "de abductores"),
    # posicion
    "standing": ("pos", "de pie"), "seated": ("pos", "sentado"),
    "sitting": ("pos", "sentado"), "lying": ("pos", "tumbado"),
    "kneeling": ("pos", "de rodillas"), "prone": ("pos", "boca abajo"),
    "supine": ("pos", "boca arriba"), "incline": ("pos", "inclinado"),
    "decline": ("pos", "declinado"), "squatting": ("pos", "en sentadilla"),
    "hanging": ("pos", "suspendido"),
    # lateralidad
    "alternate": ("lat", "alterno"), "alternating": ("lat", "alterno"),
    "unilateral": ("lat", "unilateral"),
    # modificadores
    "reverse": ("mod", "invertido"), "side": ("mod", "lateral"),
    "lateral": ("mod", "lateral"), "front": ("mod", "frontal"),
    "rear": ("mod", "posterior"), "overhead": ("mod", "sobre la cabeza"),
    "wide": ("mod", "abierto"), "close": ("mod", "cerrado"),
    "narrow": ("mod", "estrecho"), "neutral": ("mod", "neutro"),
    "hammer": ("mod", "martillo"), "sumo": ("mod", "sumo"),
    "goblet": ("mod", "goblet"), "zercher": ("mod", "zercher"),
    "pistol": ("mod", "pistol"), "cossack": ("mod", "cossack"),
    "zottman": ("mod", "zottman"), "isometric": ("mod", "isométrico"),
    "full": ("mod", "completa"), "half": ("mod", "media"),
    "single": ("mod", "unilateral"), "weighted": ("mod", "con peso"),
    "assisted": ("mod", "asistido"), "explosive": ("mod", "explosivo"),
    "static": ("mod", "estático"), "dynamic": ("mod", "dinámico"),
    "rotational": ("mod", "rotacional"), "circular": ("mod", "circular"),
    "clasped": ("mod", "manos entrelazadas"),
    "supported": ("mod", "con apoyo"), "support": ("mod", "con apoyo"),
    "wall": ("mod", "en pared"), "floor": ("mod", "en suelo"),
    "bench": ("mod", "en banco"), "chair": ("mod", "en silla"),
    "staircase": ("mod", "en escalera"), "stepbox": ("mod", "en cajón"),
    "towel": ("mod", "con toalla"), "high": ("mod", "alto"),
    "low": ("mod", "bajo"), "underhand": ("mod", "agarre supino"),
    "overhand": ("mod", "agarre prono"), "palm": ("mod", "de palma"),
    "grip": ("mod", ""), "stance": ("mod", ""),
    "straight": ("mod", "con barra recta"), "twisting": ("mod", "con giro"),
    "upright": ("mod", "vertical"), "behind": ("mod", "por detrás"),
    "stiff": ("mod", "piernas rígidas"), "parallel": ("mod", "en paralelas"),
    "planche": ("mod", "planche"), "suspended": ("mod", "suspendido"),
    "plyo": ("mod", "pliométrico"), "forward": ("mod", "al frente"),
    "lift": ("mov", "Elevación"), "rotate": ("mov", "Rotación"),
    "knee": ("part", "de rodilla"), "knees": ("part", "de rodillas"),
    "hand": ("mod", ""), "hands": ("mod", ""), "arms": ("mod", ""),
    "head": ("part", "de cabeza"), "lat": ("part", "de dorsal"),
    "lats": ("part", "de dorsal"), "step": ("mod", "con paso"),
    "bent": ("pos", "inclinado"), "over": ("mod", ""), "push": ("mod", ""),
    "bench": ("mod", "en banco"), "ez": ("eq", "con barra EZ"),
    "tilt": ("mov", "Báscula"), "pelvic": ("part", "pélvica"),
    "hyght": ("mod", "Hyght"), "chest": ("part", "de pecho"),
    # equipo
    "barbell": ("eq", "con barra"), "dumbbell": ("eq", "con mancuerna"),
    "dumbbells": ("eq", "con mancuernas"), "band": ("eq", "con banda"),
    "cable": ("eq", "en polea"), "lever": ("eq", "en máquina"),
    "smith": ("eq", "en multipower"), "machine": ("eq", "en máquina"),
    "kettlebell": ("eq", "con pesa rusa"), "bodyweight": ("eq", ""),
    "sled": ("eq", "en trineo"), "roller": ("eq", "con rueda"),
    "rope": ("eq", "con cuerda"),
}

RUIDO = {"the", "a", "an", "of", "in", "on", "to", "and", "for", "with",
         "your", "up", "down", "v", "pov", "male", "female", "bar"}


def traducir(nombre):
    txt = re.sub(r"\((male|female|[^)]*pov[^)]*)\)", " ", nombre, flags=re.I)
    txt = re.sub(r"\bv\.? ?\d\b", " ", txt, flags=re.I)
    txt = txt.replace("(", " ").replace(")", " ").lower()
    txt = " " + re.sub(r"\s+", " ", txt).strip() + " "

    partes = {"mov": [], "part": [], "mod": [], "pos": [], "lat": [], "eq": []}

    for frase, rol, es in FRASES:
        if f" {frase} " in txt:
            txt = txt.replace(f" {frase} ", " ")
            txt = " " + re.sub(r"\s+", " ", txt).strip() + " "
            if es and es not in partes[rol]:
                partes[rol].append(es)

    for tok in txt.split():
        tok = tok.strip(".,-")
        if not tok or tok in RUIDO:
            continue
        if tok in PALABRAS:
            rol, es = PALABRAS[tok]
            if es and es not in partes[rol]:
                partes[rol].append(es)
        else:
            if tok not in partes["mod"]:
                partes["mod"].append(tok)

    if not partes["mov"]:
        partes["mov"] = [(partes["mod"].pop(0).capitalize())
                         if partes["mod"] else "Ejercicio"]

    orden = (partes["mov"][:1] + partes["part"][:1] + partes["mod"]
             + partes["pos"] + partes["lat"] + partes["eq"][:1])
    out = re.sub(r"\s+", " ", " ".join(orden)).strip()
    return out[:1].upper() + out[1:] if out else nombre


def firma(r):
    """Dos fichas con esta misma firma son el mismo ejercicio para el motor."""
    return (r["start_position"], r["movement_pattern"], r["laterality"],
            r["overhead_position"], r["requires_standing"],
            tuple(sorted(r["contraindications"])),
            tuple(sorted(r["cautions"])),
            tuple(sorted(r["safe_for"])))


def main():
    src = {x["id"]: x for x in json.load(open(SRC, encoding="utf-8"))}
    recs = json.load(open(MANUAL, encoding="utf-8"))
    tax = json.load(open(TAX, encoding="utf-8"))

    # --- 1. dedup ---
    grupos = collections.defaultdict(list)
    for r in recs:
        grupos[firma(r)].append(r)

    representantes = []
    for g in grupos.values():
        # se queda el de mayor confianza; a igualdad, el de nombre mas corto
        # (los nombres largos suelen ser los que llevan marcador de duplicado)
        g.sort(key=lambda r: (-r.get("confidence", 0), len(r["_name"])))
        elegido = dict(g[0])
        elegido["_variantes"] = len(g)
        elegido["_ids_variantes"] = [x["exercise_id"] for x in g[1:]]
        representantes.append(elegido)

    print(f"dedup: {len(recs)} fichas -> {len(representantes)} ejercicios "
          f"({len(recs) - len(representantes)} colapsados)")

    # --- 2. indexar condiciones ---
    conds, capas = [], {}
    for capa, items in tax["condition_layers"].items():
        ks = list(items) if isinstance(items, dict) else items
        capas[capa] = []
        for c in ks:
            capas[capa].append(len(conds))
            conds.append(c)
    idx = {c: n for n, c in enumerate(conds)}

    # --- 3. exportar ---
    ejercicios = []
    for r in representantes:
        x = src[r["exercise_id"]]
        target = x.get("target") or ""
        ejercicios.append({
            "i": r["exercise_id"],
            "n": traducir(r["_name"]),
            "en": r["_name"],
            "eq": EQUIPO_ES.get(x.get("equipment"), x.get("equipment")),
            "z": TARGET_ZONA.get(target, "otros"),
            "p": POS_ES.get(r["start_position"], r["start_position"]),
            "d": r["difficulty"],
            "c": sorted(idx[c] for c in r["contraindications"] if c in idx),
            "w": sorted(idx[c] for c in r["cautions"] if c in idx),
            "s": sorted(idx[c] for c in r["safe_for"] if c in idx),
            "cf": round(r.get("confidence", 1), 2),
            "v": r["_variantes"],
        })
    ejercicios.sort(key=lambda e: (e["z"], e["d"], e["n"]))

    salida = {
        "generado": "lote 47 · catálogo deduplicado",
        "conditions": conds,
        "labels": [COND_ES.get(c, c) for c in conds],
        "layers": capas,
        "zonaCara": ZONA_CARA,
        "equipos": sorted({e["eq"] for e in ejercicios}),
        "exercises": ejercicios,
    }
    os.makedirs(OUTDIR, exist_ok=True)
    ruta = os.path.join(OUTDIR, "catalog.json")
    json.dump(salida, open(ruta, "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))
    kb = os.path.getsize(ruta) / 1024
    print(f"escrito {ruta}  ({kb:.0f} KB, {len(ejercicios)} ejercicios)")

    zc = collections.Counter(e["z"] for e in ejercicios)
    print("por zona:", dict(zc.most_common()))


if __name__ == "__main__":
    main()
