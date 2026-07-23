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
