# Plan maestro — AdaptaFit

Documento de seguimiento. Se actualiza con cada lote ejecutado.

**Última actualización:** 2026-07-23 · lote 4 completado

---

## Estado global

```
Clasificación manual   ████░░░░░░░░░░░░░░░░░░░░░░░░░░   126 / 895   (14,1%)
```

| Fase | Estado |
|---|---|
| Especificación | ✅ |
| Taxonomía v1.2 (30 atributos · 62 condiciones) | ✅ |
| E1 — pre-seed heurístico | ✅ 94,6% `start_position` |
| Motor de filtrado | ✅ funcionando |
| Cola de trabajo priorizada | ✅ |
| **Clasificación manual** | 🔄 **en curso — lote 4 de ~12** |
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
| 05 | — | — | — | — | — | pendiente |
| 06 | — | — | — | — | — | pendiente |
| 07 | — | — | — | — | — | pendiente |
| 08 | — | — | — | — | — | pendiente |
| 09 | — | — | — | — | — | pendiente |
| 10 | — | — | — | — | — | pendiente |
| 11 | — | — | — | — | — | pendiente |
| 12 | — | — | — | — | — | pendiente |

**Meta realista:** ~200-250 clasificados (lote 10-12) antes de que el contexto
de conversación se agote. Con eso la app es plenamente funcional para uso
familiar. Los 895 completos requieren correr E2.

---

## Cobertura del motor por lote

Ejercicios disponibles según perfil, a medida que crece el catálogo:

| Perfil | gold (54) | L01 (72) | L02 (90) | L03 (108) | L04 (126) |
|---|---|---|---|---|---|
| Movilidad reducida | 15 | 26 | 39 | 50 | **62** |
| Silla de ruedas | 21 | — | 47 | 60 | **72** |
| Disautonomía (sin advertencia) | 11 | — | 28 | 35 | **46** |

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

**Patrón:** `bench_incline` vs `bench_prone` es el error más frecuente. Cuando el
pecho queda apoyado contra el respaldo inclinado, la posición es prona, no
inclinada. Importa porque `bench_prone` excluye a quien no puede ponerse boca abajo.

---

## Hallazgos acumulados

**`head_below_heart` aparece donde no se espera.** No solo en inversiones:
`seated lower back stretch` se hace en una silla y parece inocuo, pero al
inclinarse la cabeza baja del corazón. Activa glaucoma, riesgo retinal y
disautonomía. Igual en `dumbbell one arm reverse fly` y `decline shrug`.

**Duplicados funcionales — el problema es peor de lo estimado.** Ya van **seis**
variantes del mismo fondo en banco (`triceps dip`, `elbow dips`, `bench dip on
floor`, `triceps dips floor`, `weighted bench dip`, `weighted tricep dips`), dos
elevaciones laterales idénticas (`0396`/`0395`) y dos Arnold press idénticos
(`2137`/`0287`). El sufijo `v. 2` del dataset casi nunca implica una diferencia
real. E4 los colapsa en `substitute_group`.

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
