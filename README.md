# AdaptaFit

App de entrenamiento **adaptativo**. Uso privado, familiar.

La premisa no es *"¿qué querés lograr?"* sino **"¿qué NO podés hacer?"**.
El valor está en la exclusión inteligente: si una persona no puede pararse,
los ejercicios de pie no aparecen. Nunca.

---

## Estado actual

**Fase:** clasificación manual en curso — **594 de 895 (66,4%)** · lote 30
**Última actualización:** 2026-07-24

📋 Plan detallado y registro de lotes: [`docs/PLAN.md`](docs/PLAN.md)

| Fase | Qué es | Estado |
|---|---|---|
| Especificación | Modelo de datos, motor adaptativo, arquitectura | ✅ `docs/ESPECIFICACION.md` |
| Taxonomía v1.2 | 30 atributos · 62 condiciones en 3 capas | ✅ `enrichment/taxonomy/` |
| Gold set | 54 ejercicios anotados a mano (14 few-shot + 40 validación) | ✅ `enrichment/gold/` |
| **E1** — pre-seed heurístico | Reglas sobre el texto. 94,6% de `start_position` | ✅ `enrichment/output/e1_output.json` |
| **Clasificación manual** | 594 de 895, lotes de 18, cola priorizada por valor | 🔄 **en curso** |
| **E2** — clasificación IA | Alternativa: 895 de una. USD 7,79 (3,89 con Batch API) | ⏸ listo, opcional |
| **Motor de filtrado** | Capas A/B/C + degradación. Probado sobre 594 | ✅ `engine.py` |
| **E3** — revisión humana | Baja confianza + todo lo que toque contraindicaciones | ⬜ |
| **E4** — grafo de sustituciones | Regresiones, progresiones, equivalencias | ⬜ |
| Esquema Supabase | Tablas `gym_*` | ⬜ |
| App | Vite + React | ⬜ |

**Siguiente acción concreta:** lote 31 de clasificación (`workqueue.py --next 18`).

---

## Estructura

```
adaptafit/
├── docs/
│   ├── ESPECIFICACION.md ....... spec funcional y técnica (documento madre)
│   ├── LICENCIAS.md ............ qué se puede usar y qué no
│   └── NOTICE-upstream.md ...... notice original del dataset
│
├── enrichment/ ................. el activo real del proyecto
│   ├── source/ ................. dataset original (MIT, no modificar)
│   ├── taxonomy/ ............... contrato de clasificación, versionado
│   ├── gold/ ................... anotaciones humanas de referencia
│   ├── scripts/ ................ pipeline E1 → E2 → E3 → E4
│   └── output/ ................. resultados de cada fase
│
├── app/ ........................ frontend (aún vacío)
├── supabase/migrations/ ........ esquema (aún vacío)
└── tools/ ...................... utilidades de build
```

### Por qué esta separación

`enrichment/source/` es **inmutable**. Todo lo que generamos vive en paralelo,
vinculado por `exercise_id`. Si el dataset upstream se actualiza, se re-sincroniza
sin perder el enriquecimiento.

El enriquecimiento **es** el producto. La app es la interfaz. Esos ~25 atributos
por ejercicio (postura, carga axial, estrés articular, contraindicaciones) no
existen en ningún dataset público — los fabricamos nosotros.

---

## Origen de los datos

Dataset base: [`angulodev/copilot-gym`](https://github.com/angulodev/copilot-gym) — 1.324 ejercicios.

- **Datos** (nombres, instrucciones, categorías): licencia MIT. Incluidos en este repo.
- **Media** (imágenes y GIFs): © Gym visual. **NO incluida.** Ver `docs/LICENCIAS.md`.

---

## Alcance

**Uso privado familiar.** Sin distribución pública, sin venta.

Esto simplifica el proyecto (no hace falta validación profesional externa, ni CDN,
ni monetización) pero **no relaja el criterio de seguridad**: los datos malos ya no
lesionan a un usuario anónimo, lesionan a alguien de la familia. El sesgo conservador
en contraindicaciones se mantiene igual.

> ⚠️ Esta app **no** es consejo médico. Filtra ejercicios según un perfil declarado,
> con criterio biomecánico general. No reemplaza a un kinesiólogo.
