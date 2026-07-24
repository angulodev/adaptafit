# Plan maestro — AdaptaFit

Documento de seguimiento. Se actualiza con cada lote ejecutado.

**Última actualización:** 2026-07-23 · lote 16 completado

---

## Estado global

```
Clasificación manual   █████████████░░░░░░░░░░░░░░░░░   378 / 895   (42,2%)
```

| Fase | Estado |
|---|---|
| Especificación | ✅ |
| Taxonomía v1.2 (30 atributos · 62 condiciones) | ✅ |
| E1 — pre-seed heurístico | ✅ 94,6% `start_position` |
| Motor de filtrado | ✅ funcionando |
| Cola de trabajo priorizada | ✅ |
| **Clasificación manual** | 🔄 **en curso — lote 18** |
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

**Meta realista:** ~200-250 clasificados (lote 10-12) antes de que el contexto
de conversación se agote. Con eso la app es plenamente funcional para uso
familiar. Los 895 completos requieren correr E2.

---

## Cobertura del motor por lote

Ejercicios disponibles según perfil, a medida que crece el catálogo:

| Perfil | gold (54) | L01 (72) | L02 (90) | L03 (108) | L04 (126) | L05 (144) | L06 (162) | L07 (180) | L08 (198) | L09 (216) | L10 (234) | L11 (252) | L12 (270) | L13 (288) | L14 (306) | L15 (324) | L16 (342) | L17 (360) | L18 (378) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Movilidad reducida | 15 | 26 | 39 | 50 | 62 | 73 | 80 | 90 | 98 | 106 | 110 | 119 | 127 | 138 | 147 | 156 | 163 | 167 | **173** |
| Silla de ruedas | 21 | — | 47 | 60 | 72 | 86 | 95 | 108 | 118 | 127 | 131 | 143 | 153 | 166 | 176 | 188 | 196 | 200 | **206** |
| Disautonomía (sin advertencia) | 11 | — | 28 | 35 | 46 | 53 | 59 | 69 | 76 | 83 | 86 | 93 | 97 | 103 | 108 | 112 | 114 | 121 | **124** |

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
