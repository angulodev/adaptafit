# Bitácora de decisiones

Registro de decisiones tomadas y su motivo. Sirve para no re-discutir lo cerrado
y para entender por qué algo está como está.

---

### D-001 · El dataset original es inmutable
**2026-07-18**

`enrichment/source/` no se modifica nunca. El enriquecimiento vive en archivos paralelos
vinculados por `exercise_id`.

*Por qué:* permite re-sincronizar si el upstream se actualiza, versionar el enriquecimiento
por separado, y auditar qué fue generado por IA vs revisado a mano.

---

### D-002 · La media licenciada queda fuera del repo
**2026-07-18**

Imágenes y GIFs son © Gym visual. `media/` está en `.gitignore`.

*Por qué:* el permiso de redistribución del repo upstream no se transfiere al clonar.
Uso privado local: OK. Repo público o bucket público: no. Ver `LICENCIAS.md`.

---

### D-003 · Repo propio, separado de `copilot-gym`
**2026-07-18**

El proyecto vive en `adaptafit`, no en el clone del dataset.

*Por qué:* el clone arrastra 138 MB de media ajena y 16 MB de un `index.html` que no usamos.
Repo propio = liviano, publicable, sin licencias heredadas. `copilot-gym` queda como
fuente externa de datos.

---

### D-004 · Los campos de seguridad no se infieren por heurística
**2026-07-18**

E1 deja `joint_stress`, `contraindications`, `cautions`, `safe_for`, `spinal_*`,
`rom_demand` y `difficulty` explícitamente en `null`.

*Por qué:* se podían inferir con regex, pero una regla tipo *"si dice squat → rodilla alto"*
produce falsos negativos que lesionan gente. Ese material lo resuelve E2 con contexto real
y pasa obligatoriamente por revisión humana en E3.

---

### D-005 · Taxonomía en 3 capas con semántica de filtrado distinta
**2026-07-18** · taxonomy v1.1

- **Capa A (movilidad):** filtro duro, excluye.
- **Capa B (lesión articular):** filtro por umbral según severidad.
- **Capa C (sistémica):** no filtra — advierte y degrada ranking.

*Por qué:* la Capa A es objetiva y sin ambigüedad médica ("no me puedo parar" es un hecho).
La Capa C es territorio médico: ocultar ejercicios en silencio por hipertensión o embarazo
es donde la app pierde confianza. Mejor mostrar con advertencia y que la persona decida.

---

### D-006 · La Capa A se agregó en v1.1, faltaba en v1.0
**2026-07-18**

La taxonomía v1.0 tenía 24 condiciones, casi todas médicas. Le faltaban
`cannot_stand`, `cannot_get_on_floor`, `cannot_kneel`, `no_overhead`, `limited_grip`.

*Por qué importa:* sin esa capa el diferenciador del producto no se puede implementar.
El ejemplo original del proyecto era literalmente *"este ejercicio se hace parado, pero si
alguien no se puede parar no se lo muestro"*. Eso es Capa A.

---

### D-007 · Lotes de 8 en E2, no 16
**2026-07-18**

*Por qué:* con ~25 campos por ejercicio, 16 respuestas en una sola salida rozaban el
truncado. El parser de rescate existe, pero mejor no depender de él.

---

### D-008 · Enriquecer solo el equipo disponible en casa
**2026-07-18**

E2 procesa 895 de 1.324 ejercicios (peso corporal, mancuernas, barra, banco, bandas).

*Por qué:* reduce el costo de E2 un tercio, hace realista la revisión manual de E3,
y la app queda más útil — nadie quiere navegar 1.324 ejercicios de los que puede hacer 200.
Para procesar todo existe `--all-equipment`.

---

### D-009 · Uso privado familiar
**2026-07-18**

Sin distribución pública, sin venta, sin validación por kinesiólogo externo.

*Por qué:* simplifica auth, monetización, CDN y licencias.
**No relaja el criterio de seguridad:** los datos malos ya no lesionan a un usuario
anónimo, lesionan a alguien de la familia. El sesgo conservador se mantiene.

---

## Decisiones abiertas

| # | Pregunta | Bloquea |
|---|---|---|
| A-01 | ¿Stack definitivo? Propuesto: Vite + React + Supabase | esquema y app |
| A-02 | ¿Cuántos perfiles familiares y con qué condiciones reales? | onboarding |
| A-03 | ¿Onboarding largo o mínimo (3 preguntas) + refinamiento por uso? | UX |
| A-04 | ¿El índice de filtrado va en cliente (bitmask) o en Supabase? | motor |
| A-05 | ¿Nombre definitivo? "AdaptaFit" es provisorio | — |

---

### D-010 · El gold set se expandió en chat, no por API
**2026-07-23**

Se anotaron 45 ejercicios adicionales en conversación (total: 54), cubriendo el espacio
`start_position × movement_pattern` y todas las posturas de Capa A.

*Por qué:* clasificar los 895 en chat no es viable (~500K tokens de salida). Pero el
cuello de botella de E2 no es el modelo, son los ejemplos. Pasar de 9 a 54 ejemplos
de calidad humana mejora los 895 de forma pareja. Mismo esfuerzo, aplicado donde rinde.

Correcciones de E1 detectadas al anotar:
- `0499 inverted row` y `0638 one arm chin-up`: E1 los marcó `standing`, son `hanging`
- `0049 barbell incline row`: E1 lo marcó `bench_incline`, es `bench_prone`
- `0639 one arm dip`: E1 lo marcó `standing`, es `seated`
- `0251 chest dip`: E1 no lo resolvió, es `hanging`

Estas correcciones ahora están en el gold, así que E2 aprende a no repetirlas.

---

### D-011 · 43 ejercicios comparten texto de instrucciones
**2026-07-23**

17 grupos con instrucciones idénticas, 43 ejercicios afectados (3,2%). El peor caso:
10 ejercicios abdominales distintos con el mismo texto (`3/4 sit-up`, `cocoons`,
`curl-up`, `half sit-up`, `janda sit-up`, `negative crunch`...).

*Implicancia:* E2 los va a clasificar idénticos porque no tiene con qué distinguirlos.
Cuatro de ellos se anotaron a mano en el gold usando el nombre real del ejercicio,
no el texto. El resto queda como cola prioritaria de E3.

---

### D-012 · El gold se divide en few-shot y validación
**2026-07-23**

14 ejemplos van dentro del prompt de E2 (`FEWSHOT_IDS`); los otros 40 quedan
reservados para `--validate`.

*Por qué:* medir el acuerdo del modelo contra los mismos ejemplos que le diste
no mide nada. Además el prompt bajó de 16.800 a 5.500 tokens, y con eso la
corrida completa de USD 9,13 a USD 5,50 (USD 2,75 si se usa Batch API).

---

### D-013 · Motor de filtrado construido y validado sobre el gold
**2026-07-23** · `enrichment/scripts/engine.py`

El motor corre antes de que exista E2, usando los 54 ejemplos anotados a mano
como catálogo. Cuando `e2_output.json` exista, lo detecta y lo usa sin cambios.

*Por qué:* es el hito que valida el producto. Si el motor no produce resultados
sensatos sobre datos reales, ninguna UI lo salva. Probarlo con 54 alcanza para
verificar la lógica.

Resultados sobre los 54:

| Perfil | Disponibles |
|---|---|
| Sin restricciones | 53 (98%) |
| Hernia discal lumbar | 31 (57%) |
| Silla de ruedas | 21 (39%) |
| Pinzamiento de hombro | 20 (37%) |
| Movilidad reducida | 15 (28%) |
| Embarazo 2do trimestre | 42 (78%) + 12 con advertencia |

---

### D-014 · La degradación nunca afloja la Capa A
**2026-07-23**

Si el perfil deja el catálogo vacío, el motor relaja en orden: primero
equipamiento, después umbral de lesión. **Nunca la Capa A.**

*Por qué:* si alguien no se puede parar, no se puede parar. Eso no se negocia
por falta de opciones. El equipamiento se puede conseguir y el umbral de lesión
se puede revisar con criterio; la restricción de movilidad es un hecho físico.

Toda relajación se informa explícitamente al usuario.

---

## Decisiones abiertas (actualizado)

| # | Pregunta | Bloquea |
|---|---|---|
| A-01 | ¿Stack definitivo? Propuesto: Vite + React + Supabase | esquema y app |
| A-02 | ¿Cuántos perfiles familiares y con qué condiciones reales? | onboarding |
| A-03 | ¿Onboarding largo o mínimo (3 preguntas) + refinamiento por uso? | UX |
| A-04 | ¿El índice de filtrado va en cliente (bitmask) o en Supabase? | motor |
| A-05 | ¿Nombre definitivo? "AdaptaFit" es provisorio | — |
| **A-06** | **¿`wheelchair` debe excluir las posiciones de banco?** Hoy no las excluye: se asume que la persona puede transferirse a un banco. Puede ser optimista. | taxonomía |

---

### D-015 · Taxonomía v1.2 — atributos fisiológicos antes que condiciones
**2026-07-23**

Se agregaron **10 atributos** y **30 condiciones** (total: 30 campos, 62 condiciones).

*Por qué los atributos primero:* agregar `dysautonomia` al enum no hace nada si el
motor no tiene contra qué compararlo. La disautonomía no se filtra por articulación
ni por postura inicial: se filtra por **carga ortostática**, cambios de posición y
maniobra de Valsalva. Ninguno de esos ejes existía.

Atributos nuevos: `orthostatic_load`, `position_change`, `head_below_heart`,
`valsalva_risk`, `sustained_isometric`, `metabolic_intensity`, `joint_laxity_risk`,
`pelvic_floor_load`, `temperature_load`, `grip_duration`.

Condiciones nuevas destacadas: disautonomía/POTS, fatiga crónica (EM/SFC),
hipermovilidad, esclerosis múltiple, dolor rotuliano, ciática, túnel carpiano,
artrosis, artritis reumatoide, posparto, suelo pélvico.

`PHYSIOLOGIC_RULES` en `engine.py` mapea 18 condiciones a umbrales sobre estos ejes.

---

### D-016 · Una advertencia en todo es una advertencia en nada
**2026-07-23**

La primera derivación de `orthostatic_load` marcaba `moderate` a casi todo, y el perfil
de disautonomía terminaba con **36 de 42 ejercicios advertidos**. Inútil.

*Corrección:* la carga ortostática es cuestión de **verticalidad del torso**, no de
"no estar acostado". En cuadrupedia o en plancha la cabeza queda a la altura del
corazón: eso no es carga ortostática. Ahora: reclinado y cuadrupedia = `none`,
sentado y arrodillado = `low`, colgado = `moderate`, de pie = `moderate`/`high`.

Resultado: 31 advertidos, **11 limpios** — y los 11 son exactamente los sentados y
reclinados. La señal ahora discrimina.

*Regla general para el proyecto:* si un filtro marca más del ~60% del catálogo,
el filtro está mal calibrado, no el catálogo.

---

### D-017 · `cannot_transfer_to_bench` resuelve la decisión abierta A-06
**2026-07-23**

En vez de decidir si `wheelchair` excluye o no las posiciones de banco, se agregó una
restricción de Capa A separada. La persona declara si puede transferirse o no.

*Por qué:* asumir por ella era paternalista en un sentido u otro. Muchos usuarios de
silla transfieren sin problema; otros no. Es un dato, no una inferencia.
