# Especificación funcional y técnica — App de entrenamiento adaptativo

**Versión:** 0.1 (borrador para revisión)
**Base de datos fuente:** `copilot-gym` (1.324 ejercicios, 10 idiomas, imagen + GIF por ejercicio)
**Estado:** en discusión — no escribir código hasta cerrar decisiones abiertas

---

## 1. Tesis del producto

La mayoría de las apps de fitness parten de la pregunta *"¿qué querés lograr?"*. Esta parte de una pregunta distinta:

> **"¿Qué NO podés hacer?"**

El objetivo del producto no es mostrar más ejercicios, es **mostrar menos, pero los correctos**. El valor está en la exclusión inteligente, no en el catálogo.

**Diferenciador central:** un motor de reglas que, dado un perfil de capacidades y restricciones de la persona, filtra el catálogo completo y devuelve solo lo ejecutable y seguro para ella — con una explicación transparente de por qué se excluyó lo demás.

---

## 2. Realidad del dataset (auditoría)

### 2.1 Lo que trae

| Campo | Tipo | Cardinalidad | Utilidad |
|---|---|---|---|
| `id` | string `^\d{4}$` | 1.324 | PK |
| `name` | string | 1.324 | Display |
| `body_part` | enum | 10 valores | Filtro grueso |
| `category` | string | espeja `body_part` | **Redundante — descartar** |
| `equipment` | string | 28 valores | Filtro de disponibilidad |
| `target` | string | 19 valores | Músculo primario |
| `muscle_group` | string | — | Sinergista principal |
| `secondary_muscles` | string[] | — | Cobertura muscular |
| `instructions` | mapa 10 idiomas | — | Texto corrido |
| `instruction_steps` | mapa 10 idiomas | — | Pasos ordenados |
| `image` / `gif_url` | path relativo | — | Media local (295 MB total) |
| `attribution` | string | — | **Obligación legal de mostrar** |

**Distribución `body_part`:** upper arms 292 · upper legs 227 · back 203 · waist 169 · chest 163 · shoulders 143 · lower legs 59 · lower arms 37 · cardio 29 · neck 2

**Distribución `equipment` (top):** body weight 325 · dumbbell 294 · cable 157 · barbell 154 · leverage machine 81 · band 54 · smith machine 48 · kettlebell 41

### 2.2 Lo que NO trae — y es exactamente lo que necesitamos

Nada en el schema permite responder *"¿este ejercicio se puede hacer sentado?"* o *"¿es seguro con hernia lumbar?"*. **Toda la capa adaptativa hay que fabricarla.**

Campos ausentes críticos:

- Postura inicial / posición corporal
- Carga axial sobre columna
- Impacto articular (rodilla, hombro, muñeca, cadera)
- Requerimiento de equilibrio
- Unilateral vs bilateral
- Rango de movimiento exigido
- Nivel de dificultad
- Contraindicaciones
- Prerequisitos de movilidad (ej. "requiere bajar al suelo")

### 2.3 Viabilidad del enriquecimiento (prueba ya ejecutada)

Corrí heurísticas regex sobre el texto en inglés de los 1.324 ejercicios buscando señales de postura:

| Señal | Coincidencias |
|---|---|
| standing | 568 |
| seated | 352 |
| bench | 325 |
| lying / supine / prone | 240 |
| hanging | 137 |
| kneeling | 26 |
| quadruped | 3 |
| **sin ninguna señal** | **113 (8,5%)** |

**Conclusión:** el enriquecimiento es viable. Hay solapamientos (un ejercicio menciona "stand" y "bench") que las regex no resuelven solas, pero sirven como *pre-seed* para un pase de clasificación con IA. No estamos ante un problema de anotación manual de 1.324 registros desde cero.

---

## 3. Modelo de datos enriquecido

### 3.1 Principio de diseño

El dataset original es **inmutable**. Creamos una tabla/archivo paralelo `exercise_attributes` vinculado por `exercise_id`. Esto permite:

- Re-sincronizar si el upstream se actualiza
- Versionar el enriquecimiento independientemente
- Auditar qué fue generado por IA y qué fue revisado por humano

### 3.2 Esquema propuesto — `exercise_attributes`

```jsonc
{
  "exercise_id": "0001",

  // ---------- POSTURA Y POSICIÓN ----------
  "start_position": "supine",
  // enum: standing | seated | seated_machine | supine | prone |
  //       side_lying | kneeling | half_kneeling | quadruped |
  //       hanging | plank | bench_supine | bench_incline | bench_prone

  "requires_floor_transition": true,
  // ¿Hay que bajar al suelo y volver a levantarse? Crítico para
  // adultos mayores, movilidad reducida, embarazo avanzado.

  "requires_standing": false,
  "requires_balance": "none",           // none | low | moderate | high
  "single_leg_support": false,
  "overhead_position": false,           // brazos por encima de la cabeza
  "grip_required": "light",             // none | light | firm | hanging_bodyweight

  // ---------- CARGA Y ARTICULACIONES ----------
  "axial_spinal_load": "none",          // none | low | moderate | high
  "spinal_flexion": "high",             // none | low | moderate | high
  "spinal_extension": "none",
  "spinal_rotation": "none",
  "impact_level": "none",               // none | low | moderate | high (pliométrico)

  "joint_stress": {
    "knee": "none",                     // none | low | moderate | high
    "hip": "low",
    "lumbar_spine": "moderate",
    "cervical_spine": "moderate",
    "shoulder": "none",
    "elbow": "none",
    "wrist": "none",
    "ankle": "none"
  },

  // ---------- EJECUCIÓN ----------
  "laterality": "bilateral",            // bilateral | unilateral | alternating
  "movement_pattern": "core_flexion",
  // enum: squat | hinge | lunge | horizontal_push | horizontal_pull |
  //       vertical_push | vertical_pull | core_flexion | core_antiextension |
  //       core_rotation | carry | isolation | cardio_steady | cardio_interval

  "chain": "closed",                    // open | closed
  "difficulty": 1,                      // 1..5
  "rom_demand": "moderate",             // low | moderate | high (exigencia de movilidad)
  "setup_complexity": "trivial",        // trivial | simple | complex

  // ---------- ADAPTABILIDAD ----------
  "regressions": ["0092", "0103"],      // versiones más fáciles
  "progressions": ["0007"],             // versiones más difíciles
  "seated_alternative_of": null,        // si es la variante sentada de otro
  "substitute_group": "abdominal_flexion_bodyweight",
  // clave de agrupación: ejercicios intercambiables entre sí

  // ---------- SEGURIDAD ----------
  "contraindications": ["lumbar_disc", "cervical_injury", "pregnancy_2nd_3rd"],
  "cautions": ["hypertension"],
  "safe_for": ["knee_injury", "ankle_injury"],

  // ---------- PROCEDENCIA ----------
  "enrichment_source": "ai_v1",         // heuristic | ai_v1 | human_reviewed
  "confidence": 0.86,                   // 0..1
  "reviewed_by": null,
  "reviewed_at": null
}
```

### 3.3 Taxonomía de condiciones del usuario

Esta es la pieza que hay que cerrar con más cuidado. Propuesta inicial en tres capas:

**Capa A — Restricciones de movilidad/postura** (objetivas, sin ambigüedad médica)

| Código | Etiqueta usuario | Efecto en el filtro |
|---|---|---|
| `cannot_stand` | No puedo estar de pie | excluye `requires_standing = true` |
| `cannot_get_on_floor` | No puedo bajar al suelo | excluye `requires_floor_transition = true` |
| `cannot_kneel` | No puedo arrodillarme | excluye `start_position ∈ {kneeling, half_kneeling, quadruped}` |
| `cannot_lie_prone` | No puedo acostarme boca abajo | excluye `prone`, `bench_prone` |
| `cannot_lie_supine` | No puedo acostarme boca arriba | excluye `supine` |
| `limited_balance` | Equilibrio limitado | excluye `requires_balance ∈ {moderate, high}`, `single_leg_support` |
| `wheelchair_user` | Uso silla de ruedas | preset: sentado + sin soporte de piernas |
| `no_overhead` | No puedo levantar brazos sobre la cabeza | excluye `overhead_position` |
| `limited_grip` | Agarre limitado | excluye `grip_required ∈ {firm, hanging_bodyweight}` |

**Capa B — Zonas de dolor / lesión** (mapea a `joint_stress` con umbral)

`knee` · `hip` · `lumbar_spine` · `cervical_spine` · `shoulder` · `elbow` · `wrist` · `ankle`

Cada una con severidad: `molestia` (excluye `high`) · `lesión activa` (excluye `moderate` + `high`) · `postoperatorio` (solo `none`, y muestra advertencia de consultar profesional).

**Capa C — Condiciones sistémicas** (banderas, no filtros duros)

`hipertensión` · `embarazo (trimestre)` · `osteoporosis` · `hernia discal` · `cardiopatía` · `adulto mayor 65+`

⚠️ **Decisión abierta:** ¿la Capa C filtra o solo advierte? Mi recomendación: **advierte + degrada** (baja el ranking, muestra alerta), nunca filtra silenciosamente. Filtrar en silencio sobre condiciones médicas es donde una app así se mete en problemas legales y de confianza.

**Capa D — Equipamiento disponible**

Checklist sobre los 28 valores de `equipment`, agrupados en presets: *Casa sin equipo* · *Casa básica (mancuernas + banda)* · *Gimnasio completo* · *Personalizado*.

---

## 4. Motor adaptativo

### 4.1 Pipeline de decisión

```
Catálogo (1.324)
   │
   ├─ [1] FILTRO DURO — restricciones de postura/movilidad (Capa A)
   │      → elimina. No negociable.
   │
   ├─ [2] FILTRO DURO — equipamiento no disponible (Capa D)
   │      → elimina.
   │
   ├─ [3] FILTRO POR LESIÓN — umbral de joint_stress (Capa B)
   │      → elimina o degrada según severidad.
   │
   ├─ [4] BANDERAS — condiciones sistémicas (Capa C)
   │      → NO elimina. Marca + baja ranking + muestra alerta.
   │
   ├─ [5] SUSTITUCIÓN — si un patrón de movimiento quedó sin cobertura,
   │      buscar en substitute_group una alternativa viable.
   │      "No podés hacer sentadilla de pie → prensa sentada / puente de glúteo"
   │
   ├─ [6] RANKING — por objetivo, dificultad vs nivel, variedad,
   │      cobertura muscular faltante
   │
   └─ Set elegible + rutina generada + registro de exclusiones
```

### 4.2 Transparencia como feature (clave del producto)

Toda exclusión debe ser **explicable y visible**:

> *"Ocultamos 340 ejercicios según tu perfil."*
> → **Ver por qué:**
> - 210 requieren estar de pie
> - 87 no tenés el equipo
> - 43 cargan la rodilla derecha
>
> [Ajustar mi perfil]

Esto genera confianza y a la vez es el mecanismo de corrección: si la persona ve que se excluyó algo que sí puede hacer, ajusta el perfil. **El usuario se vuelve el corrector del enriquecimiento por IA.**

### 4.3 Perfil dinámico (el "adaptativo" real)

El perfil no es estático. Debe evolucionar con dos señales:

1. **Feedback post-ejercicio:** ¿dolor? ¿demasiado fácil/difícil? → ajusta dificultad y agrega banderas por articulación.
2. **Estado del día:** un check-in rápido antes de entrenar (*"¿cómo está tu espalda hoy?"*) que aplica restricciones temporales sin tocar el perfil base.

Este segundo punto es lo que ninguna app mainstream hace bien y es donde está el diferenciador defendible.

---

## 5. Estrategia de enriquecimiento (proyecto previo al desarrollo)

**Esto es un proyecto en sí mismo y hay que tratarlo como tal.** Sin este dataset enriquecido, la app no existe.

### Fase E1 — Pre-seed heurístico
Script que aplica regex sobre `instructions.en` para pre-clasificar `start_position`, `equipment`-derivados, `laterality`, `overhead_position`. Cobertura estimada: ~70% con confianza media.

### Fase E2 — Clasificación asistida por IA
Pase por lotes contra la API de Anthropic. Por tu experiencia previa (KDP Book Studio): **lotes chicos, salida JSON estricta, parser de rescate para JSON parcial.**

- Lotes de 15–20 ejercicios por request
- Prompt con la taxonomía completa + few-shot de 5 ejemplos anotados a mano
- Salida: solo JSON, sin preámbulo
- Cada campo con `confidence`
- ~70–90 requests totales para los 1.324

### Fase E3 — Revisión humana priorizada
No revisar los 1.324. Revisar:
1. Todo lo que tenga `confidence < 0.7`
2. **Todo lo que toque `contraindications` y `joint_stress` alto** (es el material sensible)
3. Los 113 sin señal heurística
4. Muestra aleatoria del 10% para medir tasa de error

Estimado: ~300 registros a revisar.

### Fase E4 — Grafo de sustituciones
`substitute_group`, `regressions`, `progressions`. Se puede derivar semi-automáticamente agrupando por `movement_pattern` + `target` + `difficulty`, luego curar.

### Fase E5 — Validación externa ⚠️
**Recomendación fuerte:** conseguir que un kinesiólogo/fisioterapeuta revise al menos la matriz de contraindicaciones antes de publicar. No la lista completa de ejercicios — la **matriz de reglas** (condición → qué se excluye). Son ~50 reglas, revisables en un par de horas por un profesional. Esto convierte el producto de "app de fitness con IA" a "app con criterio clínico validado", que es un argumento de venta real y una cobertura de riesgo.

---

## 6. Arquitectura técnica

### 6.1 El problema del volumen (decide el stack)

El repo pesa **295 MB**: `exercises.json` 17 MB + 12 MB de imágenes + ~265 MB de GIFs.

Esto descarta tu patrón habitual de single-file PWA sin build. Un `exercises.json` de 17 MB no se carga en el arranque de una PWA móvil.

### 6.2 Recomendación de stack

| Capa | Elección | Por qué |
|---|---|---|
| **Frontend** | React 19 + Vite + PWA plugin | Necesitás code-splitting, lazy loading y service worker configurable. El volumen de datos lo exige. |
| **Estilos** | Tailwind (build, no CDN) | Consistente con leader_pro |
| **Backend/DB** | Supabase (proyecto nuevo, prefijo `gym_`) | Ya dominás el patrón: RLS, auth, RPC |
| **Media** | Supabase Storage o Cloudflare R2 + CDN | 277 MB no van en el repo de la app. **R2 gana: egress gratis.** |
| **Filtrado** | **Cliente**, sobre índice comprimido | Ver 6.3 |
| **Deploy** | GitHub Pages o Cloudflare Pages | |

### 6.3 Decisión clave — dónde vive el filtro

Propongo **filtrado en cliente sobre un índice liviano**:

- Se genera en build un `exercise_index.json`: solo los campos necesarios para filtrar (~1.324 × ~40 campos numéricos/enum ≈ **250–400 KB gzip**). Sin texto de instrucciones, sin multiidioma.
- El detalle completo de un ejercicio (instrucciones en 10 idiomas, media) se pide **on-demand** a Supabase cuando se abre la ficha.
- Ventaja: el motor adaptativo corre offline, instantáneo, sin round-trip. Y es lo que hace que la app se sienta rápida cuando el usuario ajusta su perfil y ve el catálogo recalcularse en vivo.

**Optimización adicional:** representar `joint_stress` y las banderas booleanas como **bitmask entero**. El filtrado se vuelve operaciones AND sobre enteros — recalcular 1.324 ejercicios toma <5 ms.

### 6.4 Esquema Supabase (borrador)

```
gym_exercises          -- espejo del dataset original (read-only, público)
gym_exercise_attrs     -- enriquecimiento (read-only público)
gym_conditions         -- catálogo de condiciones (Capas A/B/C)
gym_rules              -- matriz condición → filtro (editable sin deploy)
gym_profiles           -- perfil de usuario (RLS: solo dueño)
gym_profile_conditions -- N:N usuario ↔ condiciones
gym_routines           -- rutinas generadas/guardadas
gym_routine_items
gym_sessions           -- entrenamientos ejecutados
gym_session_logs       -- series, reps, peso, feedback de dolor
gym_daily_checkins     -- estado del día (restricciones temporales)
gym_exclusion_log      -- auditoría: qué se excluyó y por qué
```

**Nota de diseño:** `gym_rules` como tabla, no como código, es deliberado — permite corregir la matriz de contraindicaciones sin redeploy. Es el mismo patrón MDD que ya usás (reglas en datos, motor genérico).

---

## 7. Alcance del MVP

### Dentro
- Onboarding de perfil (Capas A, B, D — la C solo como banderas informativas)
- Catálogo filtrado con explicación de exclusiones
- Ficha de ejercicio (instrucciones ES + GIF + alternativas)
- Generador de rutina básico por objetivo + días disponibles
- Registro de sesión con feedback de dolor/dificultad
- Check-in del día
- PWA offline para el índice y las rutinas guardadas

### Fuera del MVP
- Video propio / detección de forma por cámara
- Comunidad, social, gamificación
- Planes de nutrición
- Wearables / HealthKit
- Multiidioma en UI (el dataset lo soporta, la UI arranca solo en español)
- Monetización

---

## 8. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| **Responsabilidad médica.** Filtrar ejercicios por lesión es cercano a consejo de salud. | Alto | Disclaimer explícito en onboarding; lenguaje de "sugerencia" no "prescripción"; validación por kinesiólogo; nunca ocultar en silencio por condición médica — siempre explicar. |
| **Calidad del enriquecimiento IA.** Un falso "seguro para rodilla" puede lesionar a alguien. | Alto | Revisión humana obligatoria de todo el material de contraindicaciones (Fase E3, prioridad 2). Sesgo conservador: ante duda, marcar como riesgoso. |
| **Licencia del dataset y de la media.** | Medio-alto | **Revisar `LICENSE` y `NOTICE.md` del repo antes de avanzar.** El campo `attribution` sugiere que la media tiene condiciones. Bloqueante para monetizar. |
| Sobre-filtrado: perfil muy restrictivo → catálogo vacío | Medio | Degradación gradual + fallback: "con este perfil quedan 12 ejercicios, acá van" en vez de pantalla vacía. |
| 295 MB de media | Medio | R2/CDN, lazy loading, GIF solo bajo demanda |
| Alcance excesivo | Alto | MVP acotado arriba. Enriquecimiento primero, app después. |

---

## 9. Decisiones abiertas — a resolver antes de codear

1. **¿La Capa C (condiciones sistémicas) filtra o solo advierte?** (mi voto: solo advierte)
2. **¿Buscamos validación de un kinesiólogo?** ¿Tenés acceso a alguno?
3. **¿Onboarding largo o progresivo?** Preguntar 15 cosas al inicio mata la conversión. Alternativa: perfil mínimo (3 preguntas) + refinamiento por uso.
4. **¿Nombre del producto?**
5. **¿Modelo de negocio desde el diseño?** Definir ahora si hay tier gratis/pago cambia el esquema de datos.
6. **¿Confirmamos Vite + Supabase + R2?**
7. **Licencia:** ¿qué permiten `LICENSE` y `NOTICE.md`?

---

## 10. Plan de trabajo propuesto

| # | Entregable | Bloquea a |
|---|---|---|
| 0 | Cerrar decisiones §9 + revisar licencia | todo |
| 1 | Taxonomía final de condiciones y atributos (v1.0 congelada) | 2 |
| 2 | Script E1 (pre-seed heurístico) | 3 |
| 3 | Pipeline E2 (clasificación IA por lotes) | 4 |
| 4 | Revisión E3 + matriz de reglas | 5 |
| 5 | Índice comprimido + motor de filtrado (probado en consola, sin UI) | 6 |
| 6 | Esquema Supabase + carga de datos | 7 |
| 7 | UI: onboarding + catálogo filtrado | 8 |
| 8 | Generador de rutinas + registro de sesión | — |

**El paso 5 es el hito que valida el producto.** Motor funcionando sobre datos reales, verificable desde consola, antes de invertir una hora en interfaz. Si el motor no produce resultados sensatos ahí, la UI no lo va a salvar.
