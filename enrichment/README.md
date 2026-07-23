# Pipeline de enriquecimiento

Genera los atributos adaptativos que el dataset original no trae.

```
source/exercises.json  (1.324, MIT, inmutable)
        │
        ▼
   E1  e1_preseed.py ........... reglas deterministas sobre el texto
        │                        → output/e1_output.json
        ▼
   E2  e2_classify.py .......... clasificación IA, capa de seguridad
        │                        → output/e2_output.json
        ▼
   E3  revisión humana .......... baja confianza + contraindicaciones
        │                        → output/e3_reviewed.json  ← CANÓNICO
        ▼
   E4  grafo de sustituciones ... regresiones / progresiones
        │                        → output/e4_substitutes.json
        ▼
   build índice para la app ..... ~300 KB, filtrable en cliente
```

---

## Contrato: `taxonomy/taxonomy_v1.json`

**v1.1 — congelada.** Define los enums válidos y las 32 condiciones en 3 capas.

| Capa | Qué es | Semántica de filtrado |
|---|---|---|
| **A — Movilidad** | `cannot_stand`, `cannot_get_on_floor`, `cannot_kneel`, `no_overhead`, `limited_grip`... | **Filtro duro.** Excluye. Sin ambigüedad médica. |
| **B — Lesión articular** | `lumbar_disc`, `knee_injury`, `rotator_cuff`... | Filtro por umbral según severidad. |
| **C — Sistémica** | `hypertension`, `pregnancy_*`, `osteoporosis`... | **No filtra.** Advierte y degrada ranking. |

> Cambiar la taxonomía invalida el enriquecimiento existente y obliga a re-correr E2.
> Si hay que cambiarla, subir la versión.

**Por qué la Capa C no filtra:** ocultar ejercicios en silencio por una condición médica
es donde una app así pierde la confianza del usuario. Mejor mostrar con advertencia
y dejar que la persona decida.

---

## E1 — pre-seed heurístico

```bash
python3 scripts/e1_preseed.py
```

Sin dependencias, sin costo. Cobertura sobre 1.324 ejercicios:

| Campo | Cobertura |
|---|---|
| `start_position` | 94,6% |
| `setup_complexity` | 94,5% |
| `grip_required` | 88,1% |
| `requires_balance` | 85,9% |
| `movement_pattern` | 73,3% |
| `laterality` | 44,0% |
| `axial_spinal_load` | 31,0% |
| `impact_level` | 2,6% |

**Deliberadamente vacío:** `joint_stress`, `contraindications`, `cautions`, `safe_for`,
`spinal_*`, `rom_demand`, `difficulty`.

Se podían inferir con regex, pero una regla tipo *"si dice squat → estrés de rodilla alto"*
produce falsos negativos que lesionan gente. Ese material lo resuelve E2 con contexto
real y pasa sí o sí por revisión humana en E3.

Reporte completo: `output/e1_report.md`.

---

## E2 — clasificación por IA

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pip install anthropic

python3 scripts/e2_classify.py --dry-run      # ver 1 prompt, sin gastar
python3 scripts/e2_classify.py --limit 32     # prueba: 4 lotes
python3 scripts/e2_classify.py --validate     # acuerdo contra el gold set
python3 scripts/e2_classify.py                # corrida completa
```

**Correr en ese orden.** Si `--validate` da acuerdo bajo, el problema está en el prompt
o en los ejemplos del gold — arreglarlo ahí cuesta centavos, después cuesta la corrida entera.

| | |
|---|---|
| Ejercicios objetivo | **895** (filtrados por equipo disponible en casa) |
| Lotes | 112 × 8 |
| System prompt | ~4.200 tokens, idéntico en cada lote |
| Costo estimado | ~USD 8–10 |

**Optimización pendiente:** activar prompt caching sobre el system prompt. Se repite
idéntico 112 veces.

### Decisiones de diseño del script

- **Lotes de 8**, no 16. Con ~25 campos por ejercicio, 16 respuestas rozaban el truncado.
- **Parser de rescate** para JSON parcial: si la respuesta viene cortada, recupera los
  objetos completos en vez de perder el lote.
- **Checkpoint incremental**: si se corta a mitad, retoma donde quedó.
- **E1 se pasa como pista, no como verdad.** El modelo puede corregirla si el texto
  la contradice.
- **Validación de enums** en cada registro: los que fallan quedan marcados, no se
  descartan en silencio.

### Filtro de equipo

`e2_classify.py` procesa solo el equipo disponible en casa:

```python
EQUIPMENT_FILTER = {"body weight", "dumbbell", "barbell", "band",
                    "resistance band", "ez barbell", "olympic barbell", "weighted"}
```

895 de 1.324. Descarta máquinas de gimnasio, cable, kettlebell.
Para procesar todo: `--all-equipment`.

---

## E3 — revisión humana (pendiente)

No revisar los 895. Priorizar:

1. Todo lo que tenga `confidence < 0.7`
2. **Todo lo que toque `contraindications` y `joint_stress` alto** — material sensible
3. Los que E1 no pudo resolver
4. Muestra aleatoria del 10% para medir tasa de error

Estimado: ~250 registros. La salida `e3_reviewed.json` es el archivo **canónico** que
consume la app.

---

## Gold set — `gold/gold_examples.json`

9 ejercicios anotados a mano. Cumplen doble función: few-shot dentro del prompt de E2,
y set de validación para medir el acuerdo del modelo.

**No regenerar con IA.** Es la única referencia humana del pipeline.

Cobertura: banco supino, sentadilla con barra, dominada, press militar sentado,
estiramiento lateral, front lever, zancada caminando, rollout arrodillado.
