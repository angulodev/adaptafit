# AdaptaFit — slice vertical

`index.html` es **autocontenido**: React, el JSX compilado, el CSS y el catálogo
van dentro del archivo. Se abre haciendo doble clic, desde `file://`, desde un
visor sin red o desde GitHub Pages. No pide nada por internet.

## Por qué hay un build, si el resto del stack no tiene

La primera versión cargaba React, ReactDOM, Babel Standalone, Tailwind y Google
Fonts por CDN. Si cualquiera de los cinco no llega, **la página queda en blanco
sin ningún error visible**, porque el fallo ocurre antes de que React monte.
Pasó dos veces seguidas: primero por el runtime automático de JSX en Babel
7.26, después al abrirla en un visor sin acceso a red.

Compilar de antemano elimina la clase entera de problemas y quita 3 MB de
descarga. El coste es un paso de build de un segundo.

## Uso

```bash
npm install react@18 react-dom@18 @babel/standalone@7.26.4 jsdom
node ui/build.js        # genera index.html
node ui/test_render.js  # comprueba que monta de verdad
```

## Archivos

| Archivo | Qué es |
|---|---|
| `app.jsx` | Fuente de la app. **Aquí se edita.** |
| `styles.css` | Estilos propios. **Aquí se edita.** |
| `catalog.json` | Generado por `enrichment/scripts/build_ui_catalog.py`. |
| `build.js` | Compila los tres anteriores en `index.html`. |
| `index.html` | **Artefacto generado. No editar a mano.** |
| `test_render.js` | Ejecuta el HTML real en jsdom. Correr antes de cada push. |

## Alcance

Perfil → mapa corporal → lista filtrada. Sin rutinas, sin progresión, sin
persistencia. Responde a una sola pregunta: ¿el modelo de tres capas produce
resultados coherentes cuando se le enseñan a una persona?

Los nombres de ejercicio están traducidos mecánicamente por reglas
gramaticales. Es provisional y se nota.
