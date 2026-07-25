# Plan maestro — AdaptaFit

Documento de seguimiento. Se actualiza con cada lote ejecutado.

**Última actualización:** 2026-07-23 · lote 16 completado

---

## Estado global

```
Clasificación manual   ██████████████████░░░░░░░░░░░░   540 / 895   (60,3%)
```

| Fase | Estado |
|---|---|
| Especificación | ✅ |
| Taxonomía v1.2 (30 atributos · 62 condiciones) | ✅ |
| E1 — pre-seed heurístico | ✅ 94,6% `start_position` |
| Motor de filtrado | ✅ funcionando |
| Cola de trabajo priorizada | ✅ |
| **Clasificación manual** | 🔄 **en curso — lote 27** |
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
| **12** | 2026-07-24 | 18 | 270 | 30,2% | 2 | `batch_manual_12.py` |
| **13** | 2026-07-24 | 18 | 288 | 32,2% | — | `batch_manual_13.py` |
| **14** | 2026-07-24 | 18 | 306 | 34,2% | — | `batch_manual_14.py` |
| **15** | 2026-07-24 | 18 | 324 | 36,2% | — | `batch_manual_15.py` |
| **16** | 2026-07-24 | 18 | 342 | 38,2% | — | `batch_manual_16.py` |
| **17** | 2026-07-24 | 18 | 360 | 40,2% | 1 | `batch_manual_17.py` |
| **18** | 2026-07-24 | 18 | 378 | 42,2% | 1 | `batch_manual_18.py` |
| **19** | 2026-07-24 | 18 | 396 | 44,2% | 1 | `batch_manual_19.py` |
| **20** | 2026-07-24 | 18 | 414 | 46,3% | 2 | `batch_manual_20.py` |
| **21** | 2026-07-24 | 18 | 432 | 48,3% | 2 | `batch_manual_21.py` |
| **22** | 2026-07-24 | 18 | 450 | 50,3% | 1 | `batch_manual_22.py` |
| **23** | 2026-07-24 | 18 | 468 | 52,3% | 2 | `batch_manual_23.py` |
| **24** | 2026-07-24 | 18 | 486 | 54,3% | 1 | `batch_manual_24.py` |
| **25** | 2026-07-24 | 18 | 504 | 56,3% | 2 | `batch_manual_25.py` |
| **26** | 2026-07-24 | 18 | 522 | 58,3% | 2 | `batch_manual_26.py` |
| **27** | 2026-07-24 | 18 | 540 | 60,3% | 3 | `batch_manual_27.py` |

**Meta realista:** ~200-250 clasificados (lote 10-12) antes de que el contexto
de conversación se agote. Con eso la app es plenamente funcional para uso
familiar. Los 895 completos requieren correr E2.

---

## Cobertura del motor por lote

Ejercicios disponibles según perfil, a medida que crece el catálogo:

| Perfil | gold (54) | L01 (72) | L02 (90) | L03 (108) | L04 (126) | L05 (144) | L06 (162) | L07 (180) | L08 (198) | L09 (216) | L10 (234) | L11 (252) | L12 (270) | L13 (288) | L14 (306) | L15 (324) | L16 (342) | L17 (360) | L18 (378) | L19 (396) | L20 (414) | L21 (432) | L22 (450) | L23 (468) | L24 (486) | L25 (504) | L26 (522) | L27 (540) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Movilidad reducida | 15 | 26 | 39 | 50 | 62 | 73 | 80 | 90 | 98 | 106 | 110 | 119 | 127 | 138 | 147 | 156 | 163 | 167 | 173 | 176 | 179 | 181 | 184 | 186 | 188 | 189 | 193 | **194** |
| Silla de ruedas | 21 | — | 47 | 60 | 72 | 86 | 95 | 108 | 118 | 127 | 131 | 143 | 153 | 166 | 176 | 188 | 196 | 200 | 206 | 209 | 212 | 214 | 217 | 219 | 221 | 225 | 230 | **235** |
| Disautonomía (sin advertencia) | 11 | — | 28 | 35 | 46 | 53 | 59 | 69 | 76 | 83 | 86 | 93 | 97 | 103 | 108 | 112 | 114 | 121 | 124 | 125 | 126 | 127 | 131 | 134 | 138 | 140 | 143 | **144** |

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
| dumbbell reverse preacher curl | seated | bench_prone | 12 |
| side lying floor stretch | supine | side_lying | 12 |
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


---

## Regla confirmada: flexionar el codo es una regresión (lote 12)

Tercera aparición del mismo principio, ya con evidencia suficiente para tratarlo
como regla general del grafo E4:

| Ejercicio (brazo recto) | Regresión (brazo flexionado) | Efecto |
|---|---|---|
| `dumbbell fly` | — | `laxity` alto |
| elevación lateral (`0396`) | `bent arm lateral raise` (`2317`) | hombro high → moderate |
| `barbell pullover` (`0073`) | `bent arm pullover` (`1316`) | `laxity` high → moderate |

Acortar el brazo de palanca reduce el torque sobre la articulación sin cambiar el
patrón de movimiento. Junto con el eje del agarre (lote 10), son las dos
transformaciones mecánicas que E4 puede aplicar de forma sistemática para generar
sustituciones válidas en vez de buscarlas caso por caso.

**Confirmación del eje de agarre:** `barbell reverse grip skullcrusher` repite
exactamente el patrón del lote 10 — el agarre invertido desplaza carga del hombro
hacia muñeca y codo. Ya son cuatro casos independientes.


---

## Reglas mecánicas de sustitución — consolidado tras lote 13

Tres transformaciones con evidencia repetida. Son la base algorítmica de E4:
en vez de un catálogo de excepciones caso por caso, E4 puede *derivar*
sustituciones aplicando estas reglas.

**1. Cambio de agarre** (5 casos confirmados)

| Agarre | Hombro | Muñeca / codo |
|---|---|---|
| Pronado | alto | moderado |
| Neutro / martillo | **moderado** | bajo |
| Invertido / supinado | moderado | **alto** |
| Cerrado / diamante | moderado | **alto** |

**2. Flexionar el codo = regresión** (3 casos)
`straight arm pullover` → `bent arm pullover` (laxity high → moderate).
El par `0433`/`1316` es el caso más limpio: el propio dataset los nombra
"straight arm" y "bent arm".

**3. Elevar las manos = quitar la transición al suelo** (4 casos)
`push-up` → `incline push-up`. Convierte `cannot_get_on_floor` de
contraindicación a `safe_for` sin cambiar el patrón.

**Regla negativa, igual de importante:** hay transformaciones que *no* son
regresiones aunque lo parezcan. `reverse grip push-up` es más fácil para el
pecho pero lleva la muñeca a `high`. E4 no debe asumir que "variante menos
popular" equivale a "más accesible".

## Extremos actualizados

| | Ejercicio | Contraindic. duras |
|---|---|---|
| 1º | `handstand` | 18 |
| 2º | `back lever` | 16 |
| 3º | `front lever` | 15 |

Los tres comparten el mismo perfil: isométrica máxima colgado o invertido,
con `valsalva` alto. Confirma que el eje `sustained_isometric` × `valsalva_risk`
identifica bien el extremo de riesgo cardiovascular.


---

## Cadena completa de elevación de piernas (lote 14)

Segundo patrón con progresión cerrada de punta a punta, y el más útil para la app
porque la accesibilidad varía en cada peldaño:

| Dif. | Ejercicio | Postura | Accesible para |
|---|---|---|---|
| 5 | `hanging pike` | colgado | — |
| 4 | `hanging leg raise` | colgado | sin uso de piernas |
| 3 | `captains chair straight leg raise` | vertical con apoyo | sin uso de piernas |
| 2 | `lying leg raise flat bench` | banco supino | no puede pararse |
| 2 | `seated leg raise` | sentado | no puede bajar al suelo |
| 2 | `barbell sitted alternate leg raise` | sentado | + agarre limitado |

Cada escalón no solo baja la dificultad: **cambia el conjunto de restricciones que
tolera**. Eso es lo que E4 debe explotar — no basta ordenar por `difficulty`, hay
que elegir el peldaño según el perfil.

## El filtro cervical funciona (verificado en lote 14)

Con lesión cervical, el motor deja 37 ejercicios de core disponibles y excluye
exactamente la familia de "manos detrás de la cabeza" — crunches, sit-ups,
`air bike`, `elbow-to-knee`, `oblique crunches`. Es el error de ejecución más común
del catálogo y el motor lo aísla correctamente.

**Hallazgo del lote:** `alternate heel touchers` es el primer abdominal con rotación
donde los brazos van a los costados en vez de detrás de la cabeza. `cervical` baja
de `high` a `low`. Es la regresión correcta de `oblique crunches` y de toda la
familia de rotación en suelo.


---

## El burpee justifica la taxonomía entera (lote 15)

`burpee` es el ejercicio con más ejes en rojo simultáneos del catálogo:
`impact_level` alto · `metabolic_intensity` alto · `orthostatic_load` alto ·
`temperature_load` alto · `position_change` alto · `pelvic_floor_load` alto.
Resultado: **14 contraindicaciones duras y 10 precauciones.**

Es el mejor argumento para los ejes fisiológicos de v1.2. Con solo
`start_position`, un burpee es "un ejercicio de pie" — indistinguible de un curl
de bíceps parado. Las seis dimensiones en rojo son las que hacen que el motor lo
excluya para disautonomía, fatiga crónica, suelo pélvico y osteoporosis a la vez.

## Nuevos abdominales aptos con lesión cervical

`reverse crunch` tiene `cervical` en **none** — brazos a los costados, la flexión
viene de la pelvis y no del cuello. Junto con `alternate heel touchers` (lote 14),
`pelvic tilt`, `dead bug` y `curl-up`, ya son cinco opciones de core para lesión
cervical. La familia "manos detrás de la cabeza" queda completamente sustituible.

## Segundo error de nomenclatura en la misma familia

`self assisted inverse leg curl` aparece **dos veces con textos distintos**:
`0697` describe rodillas al pecho (core), `1766` describe curl femoral en máquina.
Mismo nombre, ejercicios diferentes. Clasificados por texto, no por nombre.
Ambos a la cola prioritaria de E3.


---

## Nuevo máximo de riesgo: `skin the cat` (lote 16)

**19 contraindicaciones duras**, supera a `handstand` (18). El cuerpo pasa invertido
entre los brazos: rotación de hombro en rango extremo más inversión completa. Es el
techo absoluto de la escala de riesgo del catálogo.

## Rotación con hernia discal — el motor es más estricto que mi clasificación

Clasifiqué `bent knee lying twist` (rotación pasiva, rodillas flexionadas, brazos a
los costados) con `lumbar_disc` como *precaución* y 17 `safe_for`, esperando que
fuera la única rotación disponible para hernia discal. **El motor lo excluye igual**,
porque `joint_stress.lumbar_spine` es `moderate` y la severidad `lesión` corta en ese
umbral.

Comportamiento verificado:

| Severidad | Rotaciones aptas |
|---|---|
| molestia | `crab twist toe touch`, `alternate heel touchers`, `bent knee lying twist` |
| lesión | **ninguna** |

Es el resultado correcto: con hernia activa la rotación lumbar se evita, punto. Pero
importa registrar que **el umbral de `joint_stress` es más restrictivo que la lista
de contraindicaciones**, y que las dos vías de exclusión pueden discrepar. La lección
para E4: no alcanza con marcar `cautions` para que algo sobreviva — hay que revisar
que el `joint_stress` sea coherente con esa intención.

---

## `push-up (wall)` — el mejor caso de degradación del dataset (lote 17)

`0659 push-up (wall)` salió con **2 contraindicaciones de 62** y **15 `safe_for`**,
el array más largo clasificado hasta ahora. Es un empuje horizontal que no exige
suelo, ni banco, ni agarre, ni carga espinal, ni posición overhead.

Importa porque resuelve un hueco conocido: cuando el filtro deja sin pecho a un
perfil que no puede bajar al suelo ni transferirse a un banco, **este es el
ejercicio que queda**. Debe entrar en la cadena de sustitución de E4 como el
piso absoluto del patrón `horizontal_push`:

```
barbell bench press → dumbbell press → incline push-up → push-up (wall)
```

Segundo caso del mismo tipo en el lote: `2706 dumbbell lying supination on floor`,
con 13 `safe_for` y `difficulty` 1. El único filtro real es llegar al suelo.

---

## Dos `safe_for` vacíos en el mismo lote

`0558 kipping muscle up` y `0471 handstand push-up` quedaron con `safe_for = []`,
aplicando la regla de dejar el array vacío ante duda. Son los dos primeros del
proyecto en no tener **ni una sola** condición para la que se pueda afirmar
seguridad con certeza alta.

No es una clasificación floja: es el resultado esperado de un catálogo que se
diseñó para excluir. Sirven como el extremo superior de la escala de riesgo,
contra el que calibrar el resto.

---

## Limitación del enum `start_position` detectada en `handstand push-up`

`0471` es una **inversión completa bajo carga**: `head_below_heart`,
`position_change: high`, `valsalva_risk: high`, `cervical_spine: high`. La
taxonomía no tiene un valor de `start_position` que lo represente. Quedó como
`standing` (el texto arranca de pie) con `requires_floor_transition: true`.

Es una limitación del enum, no de la anotación. **Candidato concreto para v1.3:**
agregar `inverted` a `start_position`. Afecta a handstands, headstands y
variantes de pino contra pared.

---

## Conflicto nombre vs. texto: `scapular pull-up`

Tercer caso de nomenclatura rota en el dataset. Un scapular pull-up real es solo
retracción y depresión escapular, sin flexión de codo. El texto fuente describe
una dominada completa.

Se aplicó la regla de la taxonomía —mandan las instrucciones— y se clasificó como
`vertical_pull`, **con `confidence` bajada a 0.60**. Es el primer uso del
mecanismo de confianza baja para señalar ambigüedad de la fuente, no del
anotador. Debe entrar en la cola de E3 como revisión prioritaria.

Confianzas reducidas en este lote:

| id | ejercicio | confidence | motivo |
|---|---|---|---|
| 0688 | scapular pull-up | 0,60 | nombre y descripción son ejercicios distintos |
| 0696 | self assisted inverse leg curl | 0,70 | descripción anatómicamente incoherente |
| 0471 | handstand push-up | 0,75 | `start_position` sin enum adecuado |

---

## Corrección a E1 en el lote 17

| id | ejercicio | E1 dijo | Correcto | Motivo |
|---|---|---|---|---|
| 0408 | dumbbell side lying one hand raise | `supine` | `side_lying` | el texto dice literalmente *"lie on your side"* |

Es el mismo patrón de error que E1 viene cometiendo: colapsa cualquier posición
horizontal a `supine`. Primer `side_lying` clasificado del proyecto.

---

## Nota de mantenimiento

La barra de progreso en *Estado global* estaba descalibrada (16/30 de bloques
llenos para un 38,2%). Se recalibró a proporción real: 12/30 para 40,2%. El
número siempre fue correcto; la barra no.

---

## Dos pares que demuestran por qué no se clasifica por músculo (lote 18)

El lote trajo dos comparaciones directas que conviene dejar registradas como
casos de referencia para E4.

**Par 1 — el codo decide, no el implemento.**

| id | ejercicio | codo | `joint_stress.shoulder` | pinzamiento |
|---|---|---|---|---|
| 1624 | dumbbell reverse bench press (L17) | abierto a los lados | `high` | contraindicación |
| 0352 | dumbbell neutral grip bench press | pegado al cuerpo | `moderate` | precaución |

Mismo patrón, mismo implemento, misma posición del cuerpo. Lo único que cambia
es la trayectoria del codo, y eso mueve el ejercicio de excluido a disponible
para un perfil con pinzamiento. **`0352` es la sustitución directa de `1624`** y
debe entrar como arista del grafo.

**Par 2 — mismo músculo, resultados opuestos.**

| id | ejercicio | `spinal_flexion` | `pelvic_floor_load` | hernia discal |
|---|---|---|---|---|
| 0705 | side bridge v. 2 | `none` | `low` | **`safe_for`** |
| 0832 | weighted crunch | `high` | `high` | contraindicación |

Los dos son abdomen, los dos en el suelo. El puente lateral estabiliza sin
flexionar ni rotar; el crunch cargado hace exactamente lo contrario.

---

## Primer core con `lumbar_disc` en `safe_for`

`0705 side bridge v. 2` es el primer ejercicio de core del proyecto que entra en
`safe_for` de hernia discal. No es una concesión: el puente lateral es parte del
*Big-3* de McGill, prescrito en rehabilitación lumbar precisamente porque genera
rigidez sin cargar el disco.

Se clasificó `joint_stress.lumbar_spine` en `low` de forma deliberada, para que
el motor no lo corte por umbral. Es la aplicación práctica de la lección
registrada en el lote 16: **no alcanza con la lista de condiciones, el
`joint_stress` tiene que ser coherente con la intención**.

---

## `standing calves` — nuevo máximo de accesibilidad

`1397 standing calves` cerró con **16 `safe_for` y 3 contraindicaciones**,
superando a `push-up (wall)` del lote 17. Sin agarre, sin brazos, sin carga
espinal, sin suelo.

Todo el filtro cae sobre un único eje: hay que poder pararse. Es el caso más
limpio del dataset de un ejercicio que un solo atributo de Capa A elimina por
completo — y para quien sí puede pararse, es casi universalmente apto.

Ranking de accesibilidad hasta ahora:

| id | ejercicio | `safe_for` | contra |
|---|---|---|---|
| 1397 | standing calves | 16 | 3 |
| 0659 | push-up (wall) | 15 | 2 |
| 2706 | dumbbell lying supination on floor | 13 | 6 |

---

## Tercer `safe_for` vacío: `barbell guillotine bench press`

`0045` baja la barra sobre el **cuello** con los codos abiertos a 90°: abducción
y rotación externa máximas, el arco exacto del pinzamiento, sin margen de error
mecánico.

Novedad en el criterio: `epilepsy` y `vertigo` entraron como **contraindicación
por consecuencia**, no por carga. El ejercicio no exige nada del sistema
vestibular — pero una pérdida momentánea de control con una barra sobre la
tráquea es catastrófica. Es el primer uso de este razonamiento en el proyecto y
debería aplicarse hacia atrás a cualquier ejercicio con carga sobre cabeza o
cuello.

---

## Corrección a E1 en el lote 18

| id | ejercicio | E1 dijo | Correcto | Motivo |
|---|---|---|---|---|
| 1317 | barbell reverse grip incline bench row | `bench_incline` | `bench_prone` | *"sit facing the backrest with your chest against it"* |

Con el pecho apoyado la columna no sostiene carga, por eso `1317` quedó con
`lumbar_disc` **y** `sciatica` en `safe_for`: es el remo más seguro del catálogo
para espalda lesionada. La corrección no era cosmética — con `bench_incline` el
motor lo habría tratado como un remo con torso libre.

Confianzas reducidas en este lote:

| id | ejercicio | confidence | motivo |
|---|---|---|---|
| 1415 | dumbbell one arm seated neutral wrist curl | 0,70 | el nombre dice neutro, el texto dice supinado |
| 1733 | dumbbell incline two arm extension | 0,65 | el texto describe un press, no una extensión |
| 1274 | deep push up | 0,65 | el texto omite las mancuernas que definen el ejercicio |

---

## `drop push up` — el hallazgo que justifica no clasificar por músculo objetivo

`1275 drop push up` está catalogado como ejercicio de **pectorales**. Quedó
**contraindicado para rodilla**: `knee_injury`, `knee_replacement`, `knee_pain`,
`cannot_kneel` y `osteoarthritis`, con `joint_stress.knee` en `high` e
`impact_level` en `moderate`.

El motivo está en una sola frase del texto: *"quickly drop your knees to the
ground"*. Es un impacto directo de rótula contra el suelo, repetido cada
repetición.

Ningún sistema que filtre por grupo muscular habría detectado esto. Es la
demostración más limpia hasta ahora de por qué la taxonomía clasifica
**mecánica**, no anatomía de destino.

---

## Progresiones que invierten el veredicto (lote 19)

Dos pares más donde agregar un solo elemento cambia la clasificación de seguridad.
Van directo al grafo de E4 como aristas dirigidas.

**Par 3 — el puente de glúteo.**

| id | ejercicio | flexión de cadera | prótesis de cadera |
|---|---|---|---|
| 0668 | rear decline bridge | extensión pura | **`safe_for`** |
| 3561 | glute bridge march (L17) | rodilla al pecho, >90° | contraindicación |

El puente simple se prescribe en rehabilitación post-artroplastia. Agregarle la
marcha viola la precaución posterior.

**Par 4 — el puente lateral.**

| id | ejercicio | `joint_stress.hip` | hernia discal | sacroilíaca |
|---|---|---|---|---|
| 0705 | side bridge v. 2 (L18) | `moderate` | `safe_for` | precaución |
| 1774 | side bridge hip abduction | `high` | precaución | **contraindicación** |

La abducción en carga mete torque frontal sobre la sacroilíaca. La base sigue
siendo espinal-neutra, pero deja de ser el ejercicio de rehabilitación que es el
puente lateral simple.

**Par 5 — la suspensión.**

`1764 hanging leg hip raise` es `1761 hanging oblique knee raise` sin rotación.
Eso devuelve `lumbar_pain` y `si_joint_pain` de contraindicación a precaución.
Sustitución directa para quien tolera flexión pero no torsión.

---

## `inverted row on bench` — piso de accesibilidad del patrón `horizontal_pull`

`2298` cerró con **13 `safe_for`**, incluidos `lumbar_disc` y `sciatica`. Tracción
horizontal tumbado boca arriba en el suelo: no exige pararse, no carga la columna,
no requiere transferencia a banco.

Es la contraparte de tirón de `push-up (wall)`. Con los dos, el catálogo ya tiene
suelo de accesibilidad para empuje **y** tracción horizontal:

```
horizontal_push → push-up (wall)         [no requiere suelo]
horizontal_pull → inverted row on bench  [requiere bajar al suelo]
```

Queda pendiente un tirón horizontal que **no** requiera bajar al suelo. Para un
perfil con `cannot_get_on_floor` + `cannot_stand`, el patrón sigue sin piso.
Es un hueco concreto a buscar en los lotes restantes.

Segundo hallazgo de accesibilidad del lote: `2470 dumbbell lying on floor rear
delt raise`, con 14 `safe_for` — la versión sin banco de toda la familia de
deltoides posterior.

---

## Primer patrón `carry` del proyecto

`2133 farmers walk` es el primer `movement_pattern: carry` clasificado. Perfil
poco habitual: `axial_spinal_load` moderado, `sustained_isometric` alto,
`grip_duration` alto y `metabolic_intensity` alta, todo de pie y en movimiento.

Salió con **19 `cautions`**, la lista más larga del proyecto, y sólo 8
contraindicaciones. Es el patrón donde casi todos los sistemas participan un poco
sin que ninguno llegue a crítico — exactamente el caso que la Capa C fue diseñada
para manejar: no se oculta, se advierte.

---

## Corrección a E1 en el lote 19

| id | ejercicio | E1 dijo | Correcto | Motivo |
|---|---|---|---|---|
| 1330 | dumbbell reverse grip incline bench one arm row | `bench_incline` | `standing` | *"stand facing the bench... bend at the waist and place your knee and hand on the bench"* |

**Esta corrección no era cosmética.** Con `bench_incline` el motor lo habría
tratado como un remo con el torso apoyado y lo habría ofrecido a perfiles con
hernia discal. Es el remo clásico a una mano: de pie, con el torso en voladizo.
Quedó con `lumbar_disc` y `sciatica` en contraindicaciones.

Contrasta directamente con `1317` del lote 18, donde la corrección fue en sentido
opuesto (`bench_incline` → `bench_prone`) y **habilitó** el ejercicio para hernia
discal. Los dos son remos con barra/mancuerna y bench en el nombre; el apoyo del
torso decide.

Confianzas reducidas en este lote:

| id | ejercicio | confidence | motivo |
|---|---|---|---|
| 0397 | dumbbell seated neutral wrist curl | 0,65 | tercer conflicto nombre/texto de la familia de muñeca |
| 3298 | straddle planche | 0,65 | el texto no describe una planche real |

---

## Auditoría del prompt de E2 (tras el lote 19)

Se revisó `e2_classify.py` contra la taxonomía v1.2. El prompt se **arma dinámico**
desde el JSON, así que enums, `field_definitions` y `classification_rules` ya
seguían la versión actual. La preocupación registrada al inicio era infundada.

Pero aparecieron dos huecos reales:

**1. Las capas no llegaban al prompt.** `condition_layers` y `layer_semantics`
existían en la taxonomía y `build_system_prompt` nunca los incluía. El modelo iba
a clasificar 895 ejercicios sin saber que la Capa A es filtro duro y la C sólo
advierte — precisamente lo que determina cuán conservador debe ser al asignar
contraindicaciones. **Corregido.**

**2. Los 342 registros manuales con `_reasoning` no se usaban.** El few-shot salía
sólo del gold de 54. Todas las reglas aprendidas entre los lotes 12 y 19 quedaban
fuera. Se agregó `MANUAL_FEWSHOT_IDS` con seis casos elegidos por poder didáctico,
no por cobertura de posturas:

| id | qué enseña |
|---|---|
| 1275 | clasificar mecánica, no músculo objetivo |
| 0352 | los codos pegados bajan el pinzamiento a precaución |
| 1330 | *"bend at the waist"* → torso en voladizo, contra para hernia |
| 1317 | mismo patrón con pecho apoyado → apto para hernia |
| 0045 | `safe_for` vacío + contraindicación por consecuencia |
| 0659 | máxima accesibilidad (15 `safe_for`) |

Y un bloque de **nueve reglas destiladas** de los 396 ejercicios anotados.

Costo: el system prompt pasó de ~8.700 a ~11.700 tokens. Va con `cache_control`,
así que el aumento se paga una vez por sesión, no por lote.

---

## `e2_validate.py` — decidir con números si E2 sirve

Los 396 clasificados a mano dejan de ser sólo catálogo: son un **set de validación**.
El script mide el acuerdo entre `e2_output.json` y la clasificación manual,
excluyendo los ejercicios que el modelo vio como few-shot.

Umbrales de decisión:

| Métrica | Umbral | Por qué |
|---|---|---|
| Campos estructurales | ≥ 90 % | acuerdo global aceptable |
| Recall de contraindicaciones | ≥ 95 % | cada una perdida es un ejercicio peligroso ofrecido |
| Falsos «seguro» | ≤ 2 % | el único error que puede lesionar a alguien |

El tercero es el que manda. Un falso *seguro* —`safe_for` sobre una condición que
el manual contraindica— se reporta ejercicio por ejercicio y va a E3 sin excepción.

Probado en las dos direcciones: 100 % con datos idénticos, y rechaza correctamente
una salida degradada a propósito (recall 94,1 %, 10,1 % de falsos seguro).

**Flujo que queda disponible:**

```bash
export ANTHROPIC_API_KEY=...
python3 enrichment/scripts/e2_classify.py --dry-run   # auditar el prompt, gratis
python3 enrichment/scripts/e2_classify.py             # ~USD 8, o la mitad con Batch
python3 enrichment/scripts/e2_validate.py             # medir contra los 396
```

---

## `resistance band seated biceps curl` — nuevo máximo de accesibilidad (lote 21)

`3123` cerró con **17 `safe_for` y 2 contraindicaciones**, superando a
`standing calves` del lote 18.

Tres cosas lo explican, y las tres son replicables:

1. **Banda elástica**: la resistencia desaparece en el punto de menor tensión, así
   que no hay carga excéntrica de golpe. `valsalva_risk: none`, `difficulty: 1`.
2. **El texto dice *"sit on a chair or bench"***. Eso saca
   `cannot_transfer_to_bench` de las contraindicaciones — no exige un banco de
   gimnasio. Es un detalle de redacción con consecuencia real en el filtrado.
3. No hay columna cargada, ni brazos sobre la cabeza, ni agarre firme.

Ranking de accesibilidad actualizado:

| id | ejercicio | `safe_for` | contra |
|---|---|---|---|
| 3123 | resistance band seated biceps curl | 17 | 2 |
| 1397 | standing calves | 16 | 3 |
| 0002 | 45° side bend | 16 | 4 |
| 0284 | donkey calf raise | 15 | 3 |
| 0659 | push-up (wall) | 15 | 2 |

**Lección para E2 y E4:** el equipamiento con banda es sistemáticamente el más
accesible del catálogo. Vale priorizar esas entradas en la cola restante.

---

## `push-up plus` — la única excepción de la familia de flexiones

`3145` es el **único push-up del proyecto con `shoulder_impingement` y
`rotator_cuff` en `safe_for`**.

El "plus" es protracción escapular al final del empuje, que activa el serrato
anterior. Es un ejercicio prescrito en rehabilitación de discinesia escapular —
justamente la causa mecánica de buena parte de los pinzamientos. El agregado no
lo hace más duro: lo hace terapéutico.

Segundo caso del proyecto donde un ejercicio entra en `safe_for` de la condición
que su familia contraindica, después de `side bridge v. 2` con hernia discal.
**Ambos son ejercicios de rehabilitación reconocidos.** Vale revisar la cola
restante buscando específicamente este patrón: son los que más valor aportan a un
catálogo adaptativo.

---

## Un centímetro de trayectoria cambia la capa de filtrado

| id | ejercicio | la barra baja hacia | `no_overhead` |
|---|---|---|---|
| 0060 | barbell lying triceps extension | la frente | precaución |
| 1720 | barbell lying back of the head extension | detrás de la cabeza | **contraindicación** |

Mismo implemento, misma postura, mismo músculo. La diferencia es hacia dónde baja
la barra, y eso mueve el ejercicio de una capa a otra. `joint_stress.shoulder`
sube de `moderate` a `high`.

---

## Espejo de impacto: `plyo push up` vs `ski step`

| id | ejercicio | `impact_level` | apto para | contraindicado para |
|---|---|---|---|---|
| 1306 | plyo push up | `high` | rodilla, tobillo | muñeca, codo, hombro |
| 3671 | ski step | `high` | hombro, muñeca, codo | rodilla, tobillo |

Los dos son pliométricos de impacto alto y sus listas son casi complementarias.
Para un perfil con lesión de miembro superior, `ski step` es la sustitución
directa de `plyo push up` manteniendo el estímulo — y al revés.

---

## Hallazgo sistémico: descripciones inventadas en calistenia avanzada

Se acumularon seis entradas cuyo texto **no describe el ejercicio que nombran**:

| id | ejercicio | qué dice el texto |
|---|---|---|
| 3298 | straddle planche | una flexión inclinada con piernas abiertas |
| 3291 | stalder press | una sentadilla con brazos arriba |
| 3315 | full maltese | una bisagra de pie con brazos en cruz |
| 3012 | scapula dips | una bisagra de pie con empuje |
| 0816 | triceps press | mecánicamente incoherente |
| 3211 | kneeling push-up | una flexión completa, no de rodillas |

Todas quedaron con `confidence` entre 0,50 y 0,55 y van a E3 como bloque.

**`3211` es el más importante de los seis.** Si el nombre es el correcto y el
texto está mal, el catálogo está perdiendo la regresión accesible del push-up —
la que necesita cualquier principiante o persona con poca fuerza de tren
superior. Vale verificarlo a mano contra otra fuente antes de E4.

---

## Duplicados detectados en los lotes 20 y 21

Para colapsar en E4:

- `2188` ≡ `2189` (extensión de tríceps sentada) — clasificación idéntica
- `1680` ≡ `0422` (curl de pie apoyado en banco) — clasificación idéntica
- `0474` ≡ `0475` (elevación de piernas colgado) — difieren sólo en el límite del recorrido
- `2298` ≈ `2300` (remo invertido) — banco vs barra, mismo perfil

---

## Correcciones a E1 en los lotes 20 y 21

| id | ejercicio | E1 dijo | Correcto |
|---|---|---|---|
| 1331 | dumbbell reverse grip incline bench two arm row | `bench_incline` | `bench_prone` |
| 1680 | dumbbell standing one arm curl over incline bench | `bench_incline` | `standing` |
| 0422 | dumbbell standing one arm curl (over incline bench) | `bench_incline` | `standing` |
| 0467 | gorilla chin | `standing` | `hanging` |

**Patrón confirmado de E1:** si aparece la palabra *bench* en el nombre, asume
postura de banco sin leer el texto. Ya son cinco casos contando `1330` del lote 19
y `1317` del 18. Es la corrección más frecuente del proyecto y ya está reflejada
como regla explícita en el prompt de E2.

---

## Cruzamos el 50 % (lote 22)

450 de 895. Es el umbral que se venía señalando como punto razonable para
congelar el dataset y arrancar la UI: el motor ya entrega 184 ejercicios al
perfil de movilidad reducida y 217 al de silla de ruedas.

---

## `neck side stretch` — nuevo máximo absoluto de accesibilidad

`1403` cerró con **28 `safe_for` y una sola contraindicación** (`cervical_injury`).
Supera ampliamente a `standing calves` (16) del lote 18.

Es el **primer ejercicio del proyecto con `wheelchair` en `safe_for`**, y también
el primero apto en los tres trimestres de embarazo. El texto dice *"stand **or**
sit"*, así que `requires_standing` es `false` y quedó como `seated` para que
llegue a usuarios de silla de ruedas.

Ranking de accesibilidad actualizado:

| id | ejercicio | `safe_for` | contra |
|---|---|---|---|
| 1403 | neck side stretch | 28 | 1 |
| 1427 | straight leg outer hip abductor | 17 | 3 |
| 1405 | back pec stretch | 17 | 3 |
| 1397 | standing calves | 16 | 3 |
| 0659 | push-up (wall) | 15 | 2 |

---

## `push-up on lower arms` — empuje horizontal sin carga de muñeca

`1467` apoya en los antebrazos en vez de las manos. Eso mueve `wrist_injury` y
`carpal_tunnel` de contraindicación —lo habitual en **toda** la familia de
flexiones— a `safe_for`. Todo el costo se traslada al codo, que sube a `high`.

Es la sustitución directa de cualquier push-up para quien tiene problemas de
muñeca, y completa un hueco que venía abierto: hasta ahora el patrón
`horizontal_push` no tenía ninguna variante compatible con túnel carpiano.

---

## Segunda limitación del enum: la flexión lateral

`0407 dumbbell side bend` es **flexión lateral de columna**, plano frontal. La
taxonomía sólo tiene `spinal_flexion` (sagital) y `spinal_rotation` (transversal).
Quedó como `core_rotation` con `spinal_flexion: moderate`, pero **ninguno de los
dos campos describe lo que hace el ejercicio**.

Es la segunda limitación estructural detectada, después de `inverted` para
inversiones (lote 17). Ambas van juntas a la propuesta de v1.3:

| propuesta | campo | motivo |
|---|---|---|
| `inverted` | valor de `start_position` | handstands, headstands, pino contra pared |
| `spinal_lateral_flexion` | campo nuevo, escala `none..high` | side bends, molinos, inclinaciones cargadas |

---

## La familia del puente, completa

Tercera y última entrada: `1409 barbell glute bridge`.

| id | ejercicio | carga | `pelvic_floor_load` | prótesis de cadera | embarazo |
|---|---|---|---|---|---|
| 0668 | rear decline bridge | ninguna | `moderate` | `safe_for` | sólo 3er trim. |
| 3561 | glute bridge march | ninguna | `moderate` | contraindicado | 2º y 3er trim. |
| 1409 | barbell glute bridge | barra | `high` | precaución | los tres |

Tres ejercicios del mismo patrón con tres perfiles de seguridad distintos. En
`3561` lo que cambia es el **movimiento** (rodilla al pecho); en `1409` lo que
cambia es la **carga**. Son ejes independientes, y el grafo de E4 los necesita
separados.

---

## Corrección a E1 en el lote 22

| id | ejercicio | E1 dijo | Correcto | Motivo |
|---|---|---|---|---|
| 0678 | rocky pull-up pulldown | `standing` | `hanging` | el texto arranca de pie pero el ejercicio se ejecuta colgado |

Mismo criterio que se aplicó a `0688` en el lote 17: `start_position` es la
posición **de ejecución**, no la de partida. Vale revisar si E1 comete este error
de forma sistemática en toda la familia de suspensión.

Confianzas reducidas:

| id | ejercicio | confidence | motivo |
|---|---|---|---|
| 0984 | band lying hip internal rotation | 0,65 | el nombre dice rotación interna, el texto describe externa |
| 0678 | rocky pull-up pulldown | 0,70 | el nombre promete una variante que el texto no describe |

---

## Cadenas de progresión completas (lotes 23-24)

Dos familias quedaron cerradas de punta a punta. Son aristas listas para el grafo
de sustitución de E4.

**Dominadas — cuatro escalones.**

| id | variante | diff | cambio clave |
|---|---|---|---|
| 0970 | con banda | 2 | añade `limited_balance` (hay que pararse sobre la banda) |
| 1763 / 0678 / 0720 | libre | 4 | tres nombres distintos, **mismo ejercicio** |
| 0841 | lastrada | 5 | `valsalva` a `high` → arrastra glaucoma y retina |

**Elevación de piernas colgado — tres escalones.**

| id | variante | diff | cambio clave |
|---|---|---|---|
| 1761 | con rotación | 4 | añade `si_joint_pain` y `lumbar_pain` a contra |
| 1764 | rodillas flexionadas | 4 | punto medio |
| 2333 | piernas rectas | 5 | `pelvic_floor_load` a `high` |
| 0826 | en barras paralelas | 4 | **`no_overhead` en `safe_for`** |

`0826` es el hallazgo de la familia: apoyado en barras paralelas el hombro
sostiene por debajo en vez de estar en suspensión, así que deja de exigir
posición overhead. Es la sustitución para hombros que no toleran los brazos
sobre la cabeza.

---

## El criterio que ordena toda la familia rompecráneos

Con `1748` quedó explícito: lo que decide la contraindicación de hombro es
**a dónde baja la barra**.

| destino | ejemplo | `shoulder_impingement` |
|---|---|---|
| a la frente | `0056` | precaución |
| detrás de la cabeza | `1748`, `0337` | contraindicación |

La frase a buscar en el texto es *"to the forehead"* frente a *"behind the head"*.
Aplica a las nueve entradas de la familia clasificadas hasta ahora.

---

## `pelvic tilt into bridge` — primer `lumbar_pain` en `safe_for`

`1422` es la quinta y más suave entrada de la familia del puente: `difficulty` 1,
`rom_demand` `low`, sin carga, sólo dos contraindicaciones (ambas de acceso al
suelo).

Es el **primer ejercicio del proyecto con `lumbar_pain` en `safe_for`**. La
basculación pélvica es el ejercicio de rehabilitación lumbar más prescrito que
existe; excluirlo por dolor lumbar sería exactamente al revés. `lumbar_disc` queda
en precauciones por sesgo conservador.

Familia del puente, completa:

| id | variante | diff | carga | prótesis cadera | lumbar |
|---|---|---|---|---|---|
| 1422 | basculación pélvica | 1 | — | `safe_for` | **`lumbar_pain` safe** |
| 0668 | puente simple | 2 | — | `safe_for` | precaución |
| 3561 | con marcha | 3 | — | **contra** | precaución |
| 1409 | con barra | 3 | barra | precaución | precaución |

---

## Duplicados funcionales detectados

El dataset trae el mismo ejercicio con nombres distintos. Se clasificaron
idénticos a propósito, pero **E4 no debe ofrecerlos como opciones separadas**:

| grupo | ids | ejercicio real |
|---|---|---|
| flexión contra la pared | `0659`, `0658` | idénticos palabra por palabra en mecánica |
| dominada estándar | `1763`, `0678`, `0720` | los tres describen una dominada común |
| puente lateral con pierna | `1774`, `1775` | uno dice «abduction», otro «adduction»; el texto describe lo mismo |

El riesgo es concreto: ofrecer tres veces la flexión contra la pared a un perfil
muy restringido da **falsa sensación de variedad justo donde el catálogo es más
pobre**. Hace falta un campo `duplicate_of` o un agrupador en E4.

---

## `dumbbell biceps curl squat` — la corrección más importante del lote

`1655` se llama *curl squat* y E1 lo clasificó como patrón `squat`. **El texto no
menciona sentadilla en ningún momento**: es un curl de bíceps de pie y nada más.

Si se hubiera aceptado a E1, el motor habría excluido el ejercicio para lesión de
rodilla y prótesis de cadera sin ningún motivo. Quedó con `knee_injury`,
`knee_pain` y `hip_replacement` en `safe_for`.

Es el mejor ejemplo hasta ahora de que **un error de E1 puede quitar opciones, no
sólo agregar riesgo**. Las dos direcciones importan.

---

## Correcciones a E1 en los lotes 23-24

| id | ejercicio | E1 dijo | Correcto | Motivo |
|---|---|---|---|---|
| 0720 | side-to-side chin | `standing` | `hanging` | tercer caso del sesgo de suspensión |
| 1771 | bodyweight kneeling triceps extension | `kneeling` | `plank` | *"extend your legs straight behind you"* |
| 1775 | side plank hip adduction | `plank` | `side_lying` | *"lying on your side"* |
| 2135 | weighted front plank | `prone` | `plank` | el cuerpo se levanta y se sostiene |
| 1655 | dumbbell biceps curl squat | `squat` | `isolation` | el texto no describe sentadilla |

**El sesgo de suspensión de E1 ya es sistemático** (`0688`, `0678`, `0720`): lee la
frase de aproximación —*"stand in front of the bar"*— como posición de ejecución.
Conviene revisar de oficio todas las entradas de `hanging` que E1 marcó como
`standing`.

Confianzas reducidas:

| id | ejercicio | confidence | motivo |
|---|---|---|---|
| 0339 | dumbbell lying femoral | **0,55** | texto mecánicamente incoherente — la más baja del proyecto |
| 1689 | push and pull bodyweight | 0,60 | describe la misma fase dos veces |
| 0458 | floor fly (with barbell) | 0,60 | una apertura con barra recta es imposible |
| 1655 | dumbbell biceps curl squat | 0,60 | el nombre dice squat, el texto es sólo curl |
| 1775 | side plank hip adduction | 0,65 | el nombre dice aducción, el texto describe abducción |
| 3021 | scapula push-up | 0,65 | misma ambigüedad que `0688 scapular pull-up` |
| 0720 | side-to-side chin | 0,70 | el nombre promete un movimiento que el texto no describe |

---

## `jack burpee` — quinto `safe_for` vacío y récord de exclusiones

`0501` cerró con **23 contraindicaciones**, récord del dataset, y `safe_for` vacío.
Es el único ejercicio del proyecto que satura cinco ejes fisiológicos a la vez:
`impact` `high`, `metabolic_intensity` `high`, `temperature_load` `high`,
`position_change` `high` y `orthostatic_load` `high`.

Sirve como extremo superior de la escala. En el otro extremo, `1403 neck side
stretch` con 28 `safe_for` y una sola contraindicación. Entre esos dos puntos cabe
todo el catálogo.

---

## Nuevo eje de restricción: la superficie inestable (lote 25)

Aparecieron las tres primeras entradas sobre pelota de estabilidad —`1659`,
`1746`, `0353`— y traen un tipo de restricción que el catálogo no tenía.

El par más limpio: `0353` es **el mismo curl de concentración que `1669`**, sólo
que sentado en pelota en vez de banco.

| | `1669` (banco) | `0353` (pelota) |
|---|---|---|
| `difficulty` | 1 | 2 |
| `requires_balance` | — | `moderate` |
| `sustained_isometric` | — | `moderate` |
| `lumbar_disc` | `safe_for` | precaución |
| contraindicaciones nuevas | — | `limited_balance`, `vertigo`, `multiple_sclerosis`, `cannot_sit_unsupported` |

Lo relevante: **el riesgo no viene del ejercicio sino del asiento**. `vertigo` y
`multiple_sclerosis` entran por riesgo de caída, no por demanda del movimiento.
Es el mismo razonamiento de «contraindicación por consecuencia» que se fijó con
el guillotine press en el lote 18.

`1746` es el peor de los tres: peso **sobre la cabeza** en superficie inestable,
con la caída hacia atrás y una mancuerna detrás de la nuca.

---

## Dos soluciones excluyentes para el problema de muñeca

`0660 push-up close-grip off dumbbell` agarra las mancuernas apoyadas en el suelo,
lo que mantiene la muñeca **neutra** en vez de extendida.

| id | cómo resuelve la muñeca | `wrist_injury` | `carpal_tunnel` | `limited_grip` |
|---|---|---|---|---|
| 1467 | apoyo en antebrazos | `safe_for` | `safe_for` | `safe_for` |
| 0660 | agarre neutro sobre mancuernas | precaución | **`safe_for`** | **contra** |

Las dos rutas sirven, pero son **mutuamente excluyentes**: `1467` no exige agarre
y `0660` sí. Para un perfil con túnel carpiano *y* fuerza de agarre reducida, la
única salida sigue siendo `1467` o `0659 push-up (wall)`.

---

## `leg up hamstring stretch` es la maniobra de Lasègue

`1576` parece inofensivo —`difficulty` 1, estiramiento en el suelo— pero elevar la
pierna recta con la cadera flexionada **es literalmente la prueba clínica que se
usa para provocar el dolor ciático**. `sciatica` quedó en contraindicaciones.

Es el segundo caso del proyecto donde un estiramiento suave contraindica algo
importante, después de `1405 back pec stretch` (aducción horizontal = maniobra de
pinzamiento). Regla que se consolida: **los estiramientos reproducen maniobras de
provocación clínica**; la intensidad baja no implica seguridad.

---

## Tercera limitación del enum: la plancha invertida

`3663 reverse plank with leg lift` es boca arriba, con el cuerpo suspendido entre
manos y talones. No hay valor de `start_position` que lo describa; quedó `supine`
por orientación.

Propuestas acumuladas para **v1.3**:

| propuesta | tipo | disparador |
|---|---|---|
| `inverted` | valor de `start_position` | `0471` handstand push-up (L17) |
| `spinal_lateral_flexion` | campo nuevo | `0407` dumbbell side bend (L22) |
| `reverse_plank` | valor de `start_position` | `3663` (L25) |

---

## Duplicados funcionales — grupos 4 y 5

| grupo | ids | nota |
|---|---|---|
| flexión con patada lateral | `0661`, `0642` | «inside» y «outside leg kick» describen el mismo gesto |
| elevación de rodillas colgado | `1764`, `2355` | idénticos |
| plancha con toque de hombro | `3699`, `3239` | idénticos |

Ya son **siete grupos** de duplicados detectados. La cadena de suspensión, una vez
deduplicada, tiene sólo tres niveles reales:

```
1764 = 2355  (rodillas)  →  2333 (piernas rectas)  →  1761 (con rotación)
                          ↘  0826 (barras paralelas, sin overhead)
```

---

## `dumbbell burpee` — nuevo récord de exclusiones

`1201` cerró con **28 contraindicaciones** y `safe_for` vacío (el sexto). Es
`0501 jack burpee` más carga, más press sobre la cabeza y más agarre.

Curiosidad que vale como referencia de escala: **empata exactamente en 28 con el
`safe_for` de `1403 neck side stretch`**. Los dos extremos del catálogo tienen el
mismo tamaño, en direcciones opuestas.

---

## Corrección a E1 en el lote 25

| id | ejercicio | E1 dijo | Correcto | Motivo |
|---|---|---|---|---|
| 0466 | gironda sternum chin | `standing` | `hanging` | **cuarto caso** del sesgo de suspensión |
| 3239 | kneeling plank tap shoulder | `kneeling` | `plank` | *"extend your legs behind you… into a plank position"* |

Con `0688`, `0678`, `0720` y ahora `0466`, el sesgo de suspensión de E1 está
confirmado como sistemático. **Acción pendiente para E3:** revisar de oficio todas
las entradas donde E1 puso `standing` y el texto contiene *"hang"* o *"grab the
bar"*.

`0466` además es la única dominada del catálogo con `lumbar_disc` y
`cervical_injury` en contraindicaciones: llevar el **esternón** a la barra obliga
a arquear la columna en el aire.

Confianzas reducidas: `0065` (0,60 — sostener una barra recta con una mano en
supinación), `1746` (0,70 — el nombre dice *supine*, el texto dice sentado).

---

## `band underhand pulldown` — el hallazgo más importante hasta ahora (lote 26)

Hasta este lote, **las nueve entradas de `vertical_pull` del proyecto eran
dominadas**. Todas con `grip_required: hanging_bodyweight`, todas contraindicadas
para agarre limitado, muñeca y túnel carpiano, todas exigiendo poder colgar el
peso corporal entero.

`1013 band underhand pulldown` rompe eso: tracción vertical con banda, de pie,
agarre ligero.

| | familia de dominadas | `1013` |
|---|---|---|
| `difficulty` | 4-5 | **1** |
| `grip_required` | `hanging_bodyweight` | `light` |
| `wrist_injury` | contraindicación | **`safe_for`** |
| `carpal_tunnel` | contraindicación | **`safe_for`** |
| `lumbar_disc` | `safe_for` | `safe_for` |
| `safe_for` total | 10 | **17** |

Es el piso de accesibilidad del patrón y la sustitución obligada de toda la
familia. **Con esto, los cuatro patrones principales tienen suelo:**

```
horizontal_push → 0659 push-up (wall)         · sin suelo, sin agarre
horizontal_pull → 0497 inverted row v.2       · sin suelo, requiere estar de pie
                → 2298 inverted row on bench  · sin estar de pie, requiere suelo
vertical_pull   → 1013 band underhand pulldown · sin colgarse
vertical_push   → (pendiente)
```

Queda `vertical_push` sin piso identificado. Es el hueco a buscar en los lotes
restantes.

---

## La banda como eje de accesibilidad

Seis entradas con banda en este lote muestran un patrón consistente: **la banda
convierte `grip_required` de `firm` a `light`**, y eso mueve `wrist_injury` y
`carpal_tunnel` de contraindicación a `safe_for`.

| ejercicio con banda | equivalente con peso | qué cambia |
|---|---|---|
| `0978` band front raise | `0376` dumbbell raise | muñeca y túnel a `safe_for`, 16 `safe_for` |
| `0993` band reverse fly | familia de remos | 18 `safe_for`, columna fuera del cuadro |
| `1013` band underhand pulldown | familia de dominadas | ver arriba |

Contraejemplo importante: `0971 band assisted wheel rollerout` y `0985 band
kneeling twisting crunch` son de los más restrictivos del lote. **La banda no hace
seguro un ejercicio; sólo elimina la demanda de agarre.** Si el patrón ya es
agresivo, sigue siéndolo.

---

## `band standing crunch` — primer `core_flexion` sin suelo

Los seis ejercicios de flexión de tronco clasificados hasta ahora (`0832`, `0992`,
`3640`, `3202`, `0972`, `1495`) exigían tumbarse. `1005` es el primero de pie.

Segundo detalle: al no llevar las manos detrás de la cabeza, `cervical_injury` y
`neck_pain` entran en `safe_for` — único del grupo. Sigue contraindicado para
hernia discal, porque la flexión cargada es flexión cargada de pie o en el suelo.

---

## Una opción en el texto cambia una contraindicación

`1495 oblique crunch v.2` dice *"place your hands behind your head **or** cross
them over your chest"*.

Esa alternativa evita la tracción manual del cuello, así que `cervical_spine` baja
a `moderate` y `cervical_injury` queda en precauciones — mientras que en `3640`,
`3202` y `0972`, donde las manos detrás de la cabeza son obligatorias, el cuello
sale a contraindicación.

**Criterio para E2/E3:** cuando el texto ofrece una variante más segura como
opción explícita, se clasifica por la variante segura y se anota. Es la única
excepción razonable al sesgo conservador.

---

## `close grip chin-up` — la dominada más amable con el hombro

`1327` es la única variante de la familia donde `shoulder_impingement` baja de
contraindicación a precaución. El agarre supinado y cerrado rota el húmero
externamente y mantiene los codos pegados.

El precio se traslada al codo: `elbow` a `high` y epicondilitis a
contraindicación. Es la sustitución directa de `1429 wide grip pull-up` para
hombros sensibles.

El ancho de agarre se comporta igual en empuje y en tracción:

| ancho | tracción | empuje |
|---|---|---|
| cerrado | `1327` chin-up · hombro `moderate` | `2398`, `0660` · hombro `moderate` |
| ancho | `1429` wide pull-up · hombro `high` | `1311` wide push-up · hombro `high` |

---

## `one arm against wall` — 19 `safe_for`

`1355` es un isométrico de dorsal empujando la pared: sin carga, sin agarre, sin
suelo, sin recorrido articular. Tres contraindicaciones.

Es al patrón de tracción lo que `0659 push-up (wall)` es al de empuje, con la
salvedad de que aquí la activación es isométrica y no hay rango de movimiento.

---

## Correcciones a E1 en el lote 26

| id | ejercicio | E1 dijo | Correcto | Impacto |
|---|---|---|---|---|
| 0993 | band reverse fly | `horizontal_push` | `horizontal_pull` | como *push* habría competido con las flexiones en vez de complementarlas |
| 0864 | dumbbell upright shoulder external rotation | `core_rotation` | `isolation` | no rota la columna, rota el hombro |

Son los dos primeros errores de E1 en **`movement_pattern`** y no en
`start_position`. Ambos habrían roto el grafo de sustitución de E4 sin afectar la
seguridad — el mismo tipo de fallo silencioso que `1655 curl squat` en el lote 24.

---

## Duplicados — grupos 8 y 9

| grupo | ids | nota |
|---|---|---|
| puente de glúteo simple | `0668`, `3013` | idénticos |
| curl de concentración en banco | `1669`, `0403` | `0403` dice «reverse grip», el texto describe supinado normal |
| curl en pelota | `1659`, `0390` | martillo vs supinado, sin diferencia de restricciones |

Y la familia de curls de muñeca acumula **cinco entradas con nombre que no
coincide con la descripción** (`0393`, `1415`, `0397`, `0365`, `0366`). Ya no son
casos sueltos: es un problema sistemático de la fuente que E3 debe revisar en
bloque.

---

## Cruzamos el 60 % (lote 27)

540 de 895. El motor entrega 194 ejercicios al perfil de movilidad reducida y 235
al de silla de ruedas.

---

## `standing pelvic tilt` — segundo del ranking absoluto

`1364` cerró con **25 `safe_for` y dos contraindicaciones**, sólo por detrás de
`1403 neck side stretch`.

Es la versión de pie de `1422 pelvic tilt into bridge`, y comparte con él lo más
valioso: `lumbar_pain` en `safe_for`, por ser rehabilitación lumbar estándar. Pero
**sin exigir bajar al suelo**, así que alcanza un perfil que `1422` no puede.

Ranking de accesibilidad actualizado:

| id | ejercicio | `safe_for` | contra |
|---|---|---|---|
| 1403 | neck side stretch | 28 | 1 |
| 1364 | standing pelvic tilt | 25 | 2 |
| 0716 | side push neck stretch | 23 | 3 |
| 1355 | one arm against wall | 19 | 3 |
| 0993 | band reverse fly | 18 | 3 |

Los cinco primeros son estiramientos, isométricos o movilidad. **El catálogo
accesible se sostiene sobre movimiento de baja carga, no sobre versiones fáciles
de ejercicios de fuerza.** Es un dato a tener en cuenta al diseñar rutinas: para
un perfil muy restringido, una sesión honesta se parece más a fisioterapia que a
gimnasio.

---

## El mismo implemento en distinto rol invierte el perfil

La familia pelota llegó a ocho entradas, y `1660` rompe el patrón:

| id | rol de la pelota | `limited_balance` | `vertigo` | rodilla |
|---|---|---|---|---|
| 1659, 0390, 1650, 1656, 1668 | asiento | contra | contra | `safe_for` |
| 1652 | asiento + una pierna | contra | contra | `safe_for` |
| **1660** | **apoyo de codos** | **`safe_for`** | — | **contra** |

En `1660` la pelota deja de ser superficie inestable y pasa a ser soporte. Eso
elimina todo el bloque de inestabilidad y a cambio mete el filtro de rodilla por
arrodillarse. **El equipamiento no determina el perfil de restricción; el rol que
cumple, sí.**

`1652` merece nota aparte: es el único de la familia donde `elderly_65plus` y
`osteoporosis` suben a contraindicación. No por el peso —mínimo— sino porque una
caída desde sentado, con mancuernas en las manos y sin poder amortiguar, es
fractura de cadera. Contraindicación por consecuencia otra vez.

---

## `modified push up to lower arms` no es la versión fácil de `1467`

Parece la progresión suave de `1467 push-up on lower arms`. Es lo contrario.

| | `1467` | `1421` |
|---|---|---|
| mecánica | se apoya en antebrazos | baja de manos a antebrazos **y vuelve a subir** |
| `wrist_injury` | **`safe_for`** | contraindicación |
| `elbow` | `high` | `high` |
| `position_change` | `moderate` | `high` |
| artritis / artrosis | precaución | **contraindicación** |

`1467` protege la muñeca; `1421` la castiga igual que una flexión normal **y
además** suma el impacto del codo contra el suelo. Nombres parecidos, perfiles
opuestos. Es exactamente el tipo de par que E4 no debe tratar como progresión.

---

## Correcciones a E1 en el lote 27

| id | ejercicio | E1 dijo | Correcto | Impacto |
|---|---|---|---|---|
| 0378 | dumbbell rear fly | `horizontal_push` | `horizontal_pull` | **segunda vez** que E1 confunde apertura posterior con empuje |
| 1430 | chest dip (on cage) | `overhead_position: true` | `false` | habría excluido el ejercicio para todo perfil sin rango overhead |
| 0613 | lying (side) quads stretch | `supine` | `side_lying` | mismo error que `0408` en el lote 17 |

El de `1430` es el más costoso: en los fondos los brazos están **abajo**,
sosteniendo el cuerpo. Marcarlo como overhead habría quitado uno de los pocos
empujes disponibles justo al perfil que menos opciones tiene.

Con `0993` (L26) y `0378`, la confusión **apertura posterior → empuje** ya es un
patrón de E1, igual que el sesgo de suspensión. Acción para E3: revisar todo lo
que E1 marcó `horizontal_push` cuyo texto contenga *"squeeze your shoulder blades
together"*.

---

## Duplicados — el grupo más grande hasta ahora

**Cinco** curls sentado en pelota que difieren sólo en agarre y lateralidad, sin
una sola diferencia de restricción: `1659`, `0390`, `1650`, `1656`, `1668`.

Otros grupos nuevos de este lote:

| grupo | ids |
|---|---|
| chin-up | `1327`, `0627` |
| flexión a un brazo / arquero | `3294`, `0725` |
| fondos en paralelas | `2462`, `1430` |
| pulldown con banda | `1013`, `0974` |
| curl predicador | `1646`, `1663`, `0452`, `1414` |

Van **quince grupos** de duplicados detectados. El dataset tiene bastante menos
variedad real de la que sugiere su tamaño, y eso afecta directamente al diseño de
E4: sin deduplicar, una rutina puede ofrecer cinco veces el mismo curl.

**Recomendación concreta:** añadir un campo `duplicate_of` en la fase E3 y
resolverlo antes de construir el grafo de sustitución.
