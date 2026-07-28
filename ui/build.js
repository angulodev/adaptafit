/**
 * Compila el slice a un index.html AUTOCONTENIDO.
 *
 *   node ui/build.js
 *
 * Por qué existe, si el resto del stack no tiene build:
 * la versión anterior dependía de cuatro CDNs (React, ReactDOM, Babel,
 * Tailwind) más Google Fonts. Si cualquiera de ellos no carga, la página
 * queda EN BLANCO y sin error visible, porque el fallo ocurre antes de que
 * React llegue a montar. Eso pasó al abrirla en un visor sin red.
 *
 * Este script incrusta React, el JSX ya transformado, el CSS y el catálogo
 * en un solo archivo. El resultado se abre desde file://, desde un visor sin
 * red o desde GitHub Pages, y no depende de nadie.
 *
 * Se edita `app.jsx` y `styles.css`; `index.html` es artefacto generado.
 */
const fs = require("fs");
const path = require("path");
const Babel = require("@babel/standalone");

const UI = __dirname;
const ROOT = path.dirname(UI);

function leer(...p) { return fs.readFileSync(path.join(...p), "utf8"); }

function reactUmd(nombre, rutaRel) {
  const candidatos = [
    path.join(ROOT, "node_modules", ...rutaRel),
    path.join(process.cwd(), "node_modules", ...rutaRel),
    path.join(require.resolve("react/package.json"), "..", "..", ...rutaRel),
  ];
  for (const c of candidatos) {
    if (fs.existsSync(c)) return fs.readFileSync(c, "utf8");
  }
  throw new Error(
    `No encuentro el UMD de ${nombre}. Instala las dependencias:\n` +
    `  npm install react@18 react-dom@18 @babel/standalone@7.26.4`
  );
}

const react = reactUmd("react", ["react", "umd", "react.production.min.js"]);
const reactDom = reactUmd("react-dom", ["react-dom", "umd", "react-dom.production.min.js"]);
const css = leer(UI, "styles.css");
const jsx = leer(UI, "app.jsx");
const catalogo = leer(UI, "catalog.json");

// Runtime clásico obligatorio: el automático emite `import`, que revienta
// dentro de un <script> normal.
const js = Babel.transform(jsx, {
  presets: [[Babel.availablePresets["react"], { runtime: "classic" }]],
}).code;

if (/^\s*import\s/m.test(js)) {
  console.error("El JSX transformado emite `import`. Revisa el runtime de Babel.");
  process.exit(1);
}

// El catálogo va como JSON parseado en tiempo de carga, no como literal de
// objeto: es más rápido de arrancar y evita problemas de escapado.
const catSeguro = JSON.stringify(catalogo)
  .replace(/</g, "\\u003c")
  .replace(/\u2028/g, "\\u2028")
  .replace(/\u2029/g, "\\u2029");

const html = `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>AdaptaFit — ejercicios que sí puedes hacer</title>
<meta name="description" content="Marca tus restricciones y mira qué queda disponible.">
<meta name="theme-color" content="#0F2A1D">
<!-- Archivo generado por ui/build.js. No editar a mano: edita app.jsx y styles.css. -->
<style>
${css}
</style>
</head>
<body>
<div id="root"><noscript>Esta página necesita JavaScript.</noscript></div>
<script>${react}</script>
<script>${reactDom}</script>
<script>window.CATALOGO = JSON.parse(${catSeguro});</script>
<script>${js}</script>
</body>
</html>
`;

const salida = path.join(UI, "index.html");
fs.writeFileSync(salida, html);
const kb = (Buffer.byteLength(html) / 1024).toFixed(0);
console.log(`index.html generado — ${kb} KB, sin dependencias externas`);
