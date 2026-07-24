# Plan maestro — AdaptaFit

Documento de seguimiento. Se actualiza con cada lote ejecutado.

**Última actualización:** 2026-07-23 · lote 11 completado

---

## Estado global

```
Clasificación manual   ███████████░░░░░░░░░░░░░░░░░░░   252 / 895   (28,2%)
```

| Fase | Estado |
|---|---|
| Especificación | ✅ |
| Taxonomía v1.2 (30 atributos · 62 condiciones) | ✅ |
| E1 — pre-seed heurístico | ✅ 94,6% `start_position` |
| Motor de filtrado | ✅ funcionando |
| Cola de trabajo priorizada | ✅ |
| **Clasificación manual** | 🔄 **en curso — lote 11 de ~14** |
| E2 — clasificación IA (opcional) | ⏸ listo, USD 7,79 |
| E3 — revisión humana | ⬜ |
| E4 — grafo de sustituciones | ⬜ |
| Índice comprimido | ⬜ |
| Esquema Supabase | ⬜ |
| App | ⬜ |

---

## Registro de lotes

Cada lote son ~18 ejercicios clasificados a mano con los 30 campos de v1.2.
La cola (`workqueue.py`) los ordena por **valor**, no por id: accesibilidad,
cobertura de espacio y fundamentalidad. Si el trabajo se corta en cualquier
punto, lo hecho es lo más útil.

| Lote | Fecha | N | Acumulado | % | Correcciones a E1 | Archivo |
|---|---|---|---|---|---|---|
| gold | 2026-07-23 | 54 | 54 | 6,0% | 5 | `gold_examples.json` |
| **01** | 2026-07-23 | 18 | 72 | 8,0% | 2 | `batch_manual_01.py` |
| **02** | 2026-07-23 | 18 | 90 | 10,1% | 4 | `batch_manual_02.py` |
| **03** | 2026-07-23 | 18 | 108 | 12,1% | 3 | `batch_manual_03.py` |
| **04** | 2026-07-23 | 18 | 126 | 14,1% | 3 | `batch_manual_04.py` |
| **05** | 2026-07-23 | 18 | 144 | 16,1% | 1 | `batch_manual_05.py` |
| **06** | 2026-07-23 | 18 | 162 | 18,1% | 0 | `batch_manual_06.py` |
| **07** | 2026-07-23 | 18 | 180 | 20,1% | 2 | `batch_manual_07.py` |
| **08** | 2026-07-23 | 18 | 198 | 22,1% | 1 | `batch_manual_08.py` |
| **09** | 2026-07-23 | 18 | 216 | 24,1% | 1 | `batch_manual_09.py` |
| **10** | 2026-07-23 | 18 | 234 | 26,1% | 1 | `batch_manual_10.py` |
| **11** | 2026-07-23 | 18 | 252 | 28,2% | 0 | `batch_manual_11.py` |
| 12 | — | — | — | — | — | pendiente |

**Meta realista:** ~200-250 clasificados (lote 10-12) antes de que el contexto
de conversación se agote. Con eso la app es plenamente funcional para uso
familiar. Los 895 completos requieren correr E2.

---

## Cobertura del motor por lote

Ejercicios disponibles según perfil, a medida que crece el catálogo:

| Perfil | gold (54) | L01 (72) | L02 (90) | L03 (108) | L04 (126) | L05 (144) | L06 (162) | L07 (180) | L08 (198) | L09 (216) | L10 (234) | L11 (252) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Movilidad reducida | 15 | 26 | 39 | 50 | 62 | 73 | 80 | 90 | 98 | 106 | 110 | **119** |
| Silla de ruedas | 21 | — | 47 | 60 | 72 | 86 | 95 | 108 | 118 | 127 | 131 | **143** |
| Disautonomía (sin advertencia) | 11 | — | 28 | 35 | 46 | 53 | 59 | 69 | 76 | 83 | 86 | **93** |

---

## Correcciones a E1 detectadas al anotar

El pre-seed heurístico acierta el 94,6% de `start_position`, pero falla de forma
sistemática cuando la primera oración describe el montaje en vez de la posición.

| Ejercicio | E1 dijo | Real | Lote |
|---|---|---|---|
| inverted row | standing | hanging | gold |
| one arm chin-up | standing | hanging | gold |
| barbell incline row | bench_incline | bench_prone | gold |
| one arm dip | standing | seated | gold |
| chest dip | *sin resolver* | hanging | gold |
| potty squat | seated | standing | 01 |
| decline push-up | bench_supine | plank | 01 |
| dumbbell scott press | *sin overhead* | overhead=true | 02 |
| dumbbell incline row | bench_incline | bench_prone | 02 |
| dumbbell lying pronation | bench_supine | bench_prone | 02 |
| captains chair | ortho low | ortho moderate | 02 |
| dumbbell tate press | seated | bench_supine | 03 |
| dumbbell incline y-raise | bench_incline | bench_prone | 03 |
| dumbbell incline t-raise | bench_incline | bench_prone | 03 |
| crab twist toe touch | seated | plank invertido (manos+pies) | 04 |
| dumbbell one arm reverse grip press | seated | bench_supine | 04 |
| bodyweight incline side plank | bench_incline | side_lying | 04 |
| dumbbell incline rear lateral raise | bench_incline | bench_prone | 05 |
| barbell lying preacher curl | seated | bench_prone | 07 |
| dumbbell close grip press | seated | bench_supine | 08 |
| lower back curl | supine | prone ('lie on your stomach') | 09 |
| barbell reverse preacher curl | seated | bench_prone | 10 |
| inverse leg curl (pull-up cable) | overhead + hanging grip | isolation prono | 07 |

**Patrón:** `bench_incline` vs `bench_prone` es el error más frecuente. Cuando el
pecho queda apoyado contra el respaldo inclinado, la posición es prona, no
inclinada. Importa porque `bench_prone` excluye a quien no puede ponerse boca abajo.

---

## Hallazgos acumulados

**`head_below_heart` aparece donde no se espera.** No solo en inversiones:
`seated lower back stretch` se hace en una silla y parece inocuo, pero al
inclinarse la cabeza baja del corazón. Activa glaucoma, riesgo retinal y
disautonomía. Igual en `dumbbell one arm reverse fly` y `decline shrug`.

**Duplicados funcionales — el problema es peor de lo estimado.** Ya van **siete**
variantes del mismo fondo en banco (`triceps dip`, `elbow dips`, `bench dip on
floor`, `triceps dips floor`, `weighted bench dip`, `weighted tricep dips`,
`bench dip (knees bent)`), siete presses de hombro sentado, tres pares `v. 2`
con texto idéntico, dos
elevaciones laterales idénticas (`0396`/`0395`) y dos Arnold press idénticos
(`2137`/`0287`). El sufijo `v. 2` del dataset casi nunca implica una diferencia
real. E4 los colapsa en `substitute_group`.

**"Sentado" no significa "seguro".** `barbell seated good morning` se hace sentado
pero tiene barra sobre la espalda, flexión de tronco, `axial_spinal_load` alto,
`valsalva_risk` alto y `head_below_heart`. Es el ejercicio más riesgoso del lote 5.
Confirma que filtrar solo por `start_position` sería insuficiente — que es
exactamente por lo que existen las otras 29 dimensiones.

**Validación fuerte del motor (lote 6).** Con 162 clasificados, al filtrar por
hernia discal lumbar sobreviven **exactamente dos** ejercicios de core:
`curl-up` y `dead bug`. Son precisamente los dos que la práctica clínica
recomienda para esa condición. El motor llegó ahí solo, por umbrales sobre
atributos — nadie codificó "para hernia usar dead bug".

**La dirección del movimiento importa más que la zona.** `sphinx` carga la
columna lumbar, pero en **extensión** — y en hernia discal la extensión suele
aliviar mientras la flexión agrava (principio del método McKenzie). Por eso
`lumbar_disc` es precaución en sphinx y contraindicación en los crunches,
aunque ambos "carguen la espalda baja". Un modelo que solo mirara
`joint_stress.lumbar_spine` no podría hacer esa distinción: hacen falta
`spinal_flexion` y `spinal_extension` por separado.

**Hueco estructural en tren inferior (lote 7).** Con 180 clasificados, el perfil
de movilidad reducida cubre bien empuje y tirón, pero de patrones de pierna solo
tiene `isolation` y **un** `hinge`. Cero `squat`, cero `lunge` — por definición
requieren estar de pie. No es un error del motor: es una limitación real del
catálogo. La app debe ser honesta al respecto en vez de fingir cobertura.

**`resistance band seated hip abduction` es el ejercicio más accesible
encontrado:** cero contraindicaciones duras y 17 `safe_for`. Nota clínica que
justifica la excepción: tras artroplastia de cadera la abducción es el
movimiento *seguro* — lo contraindicado es aducción y rotación interna.

**43 ejercicios comparten texto de instrucciones** (17 grupos, 3,2% del dataset).
El peor: 10 abdominales distintos con el mismo texto. Cola prioritaria de E3.

**`grip_required` y `grip_duration` son ejes distintos.** `finger curls` tiene
agarre firme y duración alta — el perfil exacto que el túnel carpiano no tolera.
Separarlos permitió detectarlo.

**`difficulty` y `rom_demand` son independientes.** Un estiramiento puede ser
dificultad 1 y exigencia de movilidad alta. Confundirlos haría que el motor
recomiende estiramientos profundos a alguien con movilidad limitada justamente
porque "son fáciles".

---

## Rutina de cada lote

1. `python3 enrichment/scripts/workqueue.py --next 18`
2. Clasificar → `enrichment/gold/batch_manual_NN.py`
3. Ejecutar el batch → se anexa a `output/manual_classified.json`
4. Validar contra `taxonomy_v1.json`
5. Correr el motor para ver cómo cambió la cobertura
6. Actualizar este documento y el README
7. Commit + push

---

## Después de la clasificación

| # | Entregable | Bloquea |
|---|---|---|
| 1 | **E4 — grafo de sustituciones** · regresiones, progresiones, equivalencias | recomendador |
| 2 | **Índice comprimido** · ~300 KB, bitmask, filtrable offline | app |
| 3 | **Esquema Supabase** · tablas `gym_*`, RLS, perfiles familiares | app |
| 4 | **App** · onboarding, catálogo filtrado, explicación de exclusiones | — |

**Decisión pendiente:** si en algún momento se quieren los 895 completos,
`e2_classify.py` está listo (USD 7,79 con caching, 3,89 con Batch API). Lo
clasificado a mano queda como referencia de calidad y set de validación.


---

## Comportamiento de la severidad (verificado en lote 8)

La severidad declarada en Capa B modula el umbral de `joint_stress`:

| Pinzamiento de hombro | Disponibles (de 198) |
|---|---|
| molestia | 116 |
| lesión | 73 |
| postoperatorio | 55 |

**Pero la lista explícita de `contraindications` es absoluta**, independiente de la
severidad. Consecuencia concreta: con pinzamiento de hombro, aunque sea leve,
**ningún ejercicio de `vertical_push` sobrevive** — los diez presses clasificados
listan `shoulder_impingement` como contraindicación.

Clínicamente es correcto: el press por encima de la cabeza con pinzamiento se evita
en cualquier grado. Pero deja un patrón de movimiento entero sin cubrir, y eso
**es exactamente el problema que E4 tiene que resolver**: ofrecer alternativas que
trabajen el hombro sin posición overhead, en vez de dejar la zona sin entrenar.

*Decisión abierta A-07:* ¿debería `molestia` degradar las contraindicaciones
explícitas a advertencia, en vez de bloquearlas? Argumento a favor: dar opciones con
alerta. Argumento en contra: una contraindicación explícita significa "no hagas esto
con esta condición", y relajarla por autodiagnóstico de gravedad es riesgoso.

**Hueco cerrado en el lote 9 — sin tocar el motor.** `dumbbell seated shoulder
press (parallel grip)` usa agarre neutro, lo que reduce mucho la rotación interna
del hombro. Clasificado con `shoulder_impingement` como *precaución* y no como
contraindicación, es el único `vertical_push` del catálogo que sobrevive al filtro
de pinzamiento leve. La solución vino de clasificar bien, no de relajar reglas —
que es la respuesta correcta a A-07 en la práctica.

**Extremos de la escala, ya anclados:**
- Más accesible: `pelvic tilt` — **22 `safe_for`**, cero contraindicaciones salvo
  las posturales. Único ejercicio de core seguro simultáneamente con hernia discal,
  ciática, hernia abdominal, posparto y disfunción de suelo pélvico. Base de
  cualquier progresión de core en rehabilitación.
- Más restringido: `handstand` — **18 contraindicaciones duras**. Inversión completa
  con todo el peso en muñecas: `head_below_heart`, `valsalva` alto, equilibrio alto
  y `orthostatic_load` alto a la vez.


---

## El agarre como eje de sustitución (lote 10)

Tres variantes del mismo movimiento, distinto agarre, distinto perfil de riesgo:

| Agarre | Hombro | Muñeca | Codo | Sirve para |
|---|---|---|---|---|
| Pronado (estándar) | **alto** | moderado | moderado | sin restricciones |
| Neutro / paralelo | moderado | bajo | moderado | **hombro comprometido** |
| Invertido / supinado | moderado | **alto** | **alto** | hombro comprometido, muñeca sana |

Esto no es cosmético: es la base de un eje de sustitución que E4 puede explotar.
Cuando el motor excluye un empuje por pinzamiento de hombro, la variante de agarre
neutro suele sobrevivir. Con 234 clasificados, un perfil con pinzamiento leve
conserva **17 empujes** — el hueco del lote 8 quedó cerrado del todo.

**Contraejemplo útil:** el curl zottman rota la muñeca bajo carga y la lleva a
`high`, siendo la versión *menos* apta para túnel carpiano — frente al curl
predicador con mancuerna, que es de las más seguras. Mismo músculo, extremos
opuestos del espectro de riesgo.

---

## Primer caso de `visual_impairment` (lote 10)

`balance board` es el primer ejercicio donde la discapacidad visual es
contraindicación dura: el equilibrio unipodal sobre superficie inestable depende de
referencia visual. Tiene una paradoja que conviene que la app maneje con cuidado —
es un ejercicio *de* equilibrio, así que quien más lo necesitaría es justamente
quien no puede hacerlo sin supervisión.


---

## Cadena completa del fondo (lote 11)

Con `reverse dip` y `ring dips` clasificados, la familia del fondo queda cerrada de
punta a punta — y es el primer patrón con progresión completa lista para E4:

| Nivel | Ejercicio | Dif. |
|---|---|---|
| Regresión | `incline scapula push up` | 1 |
| Base | `bench dip (knees bent)` y 10 duplicados | 2 |
| Progresión | `three bench dip` / `weighted bench dip` | 3 |
| Avanzado | `weighted three bench dips` / `reverse dip` | 4 |
| Techo | `ring dips` | 5 |

Los once duplicados del fondo en banco, que parecían ruido del dataset, resultan
ser el eslabón medio de una cadena real. Colapsarlos en `substitute_group` sigue
siendo correcto, pero la cadena de progresión sí tiene valor.

## Tren inferior: el hueco persiste (lote 11)

Con 252 clasificados, el perfil de movilidad reducida sigue teniendo **solo dos
`hinge`** y cero `squat` o `lunge`. `hip raise (bent knee)` fue el mejor hallazgo
del lote — único `hinge` con `lumbar_spine` en `low` y **15 `safe_for`** — pero el
patrón sigue siendo el punto débil estructural del catálogo para perfiles sentados.

Conclusión de producto: la app debe declarar la limitación explícitamente. Una
rutina de tren inferior para movilidad reducida se construye con aislamiento y
puente de glúteo, no con patrones compuestos, y eso hay que decirlo.
