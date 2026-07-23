# Licencias — qué se puede usar y qué no

## Resumen

| Activo | Licencia | ¿Se puede usar? | ¿Va en el repo? |
|---|---|---|---|
| Datos del dataset (nombres, instrucciones, categorías) | MIT | ✅ Sí, incluso comercial | ✅ Sí |
| Imágenes (`.jpg`) | © Gym visual | ⚠️ Solo uso privado | ❌ **No** |
| GIFs (`.gif`) | © Gym visual | ⚠️ Solo uso privado | ❌ **No** |
| Enriquecimiento propio (E1–E4) | Nuestro | ✅ Sí | ✅ Sí |
| Taxonomía y gold set | Nuestro | ✅ Sí | ✅ Sí |

---

## Los datos: MIT

Los 1.324 registros de `enrichment/source/exercises.json` están bajo MIT.
Se pueden copiar, modificar, redistribuir y usar comercialmente.

**Todo el enriquecimiento que generamos encima es trabajo original y es enteramente nuestro.**
Los ~25 atributos por ejercicio (postura, carga axial, estrés articular, contraindicaciones)
no vienen del dataset: los fabricamos.

## La media: NO

Las imágenes y GIFs son propiedad de **Gym visual** (gymvisual.com). El repo upstream
los redistribuye bajo un permiso escrito **específico para ese repo**.

Ese permiso **no se transfiere** al clonar. Está dicho explícitamente en el NOTICE
original (copia en `NOTICE-upstream.md`).

### Qué significa en la práctica

**Uso privado familiar** — usar los GIFs localmente, sin publicarlos ni distribuirlos:
riesgo muy bajo. Es el escenario de este proyecto.

**Lo que NO se puede hacer:**
- Subir la media a un repo público
- Subirla a un bucket público (Supabase Storage público, R2, CDN)
- Distribuir la app con la media incluida
- Vender la app o cobrar por acceso

### Cómo se maneja en este repo

`media/` está en `.gitignore`. Para poblarla localmente:

```bash
git clone https://github.com/angulodev/copilot-gym.git /tmp/cg
mkdir -p media
cp -r /tmp/cg/images media/
cp -r /tmp/cg/videos media/
```

**Si en algún momento esto deja de ser un proyecto familiar**, hay que reemplazar la media
o comprar licencia en gymvisual.com. Es lo primero que hay que resolver antes de publicar.

---

## Disclaimer médico

Independiente de las licencias: esta app filtra ejercicios según un perfil declarado,
usando criterio biomecánico general generado con asistencia de IA y revisado a mano.

**No es consejo médico y no reemplaza a un profesional de la salud.**

El disclaimer debe aparecer en el onboarding de la app, no solo en la documentación.
