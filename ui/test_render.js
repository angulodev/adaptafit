/**
 * Harness de render para el slice. Ejecuta index.html en jsdom, transforma el
 * JSX igual que el navegador y comprueba que las dos pantallas montan.
 *
 *   npm install jsdom react@18 react-dom@18 @babel/standalone@7.26.4
 *   node ui/test_render.js
 *
 * Existe porque un fallo de transformacion de Babel deja la pagina en blanco
 * sin escribir nada en consola, y eso es indistinguible de un error de CSS o
 * de red. Correr esto antes de cada push.
 */
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");
const Babel = require("@babel/standalone");

const UI = path.dirname(__filename);
const cat = JSON.parse(fs.readFileSync(path.join(UI, "catalog.json"), "utf8"));
const html = fs.readFileSync(path.join(UI, "index.html"), "utf8");

const dom = new JSDOM('<!doctype html><html><body><div id="root"></div></body></html>',
  { pretendToBeVisual: true, url: "http://localhost/" });
const { window } = dom;
global.window = window;
global.document = window.document;
global.self = window;
window.scrollTo = () => {};
window.fetch = global.fetch = () =>
  Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve(cat) });
window.React = global.React = require("react");
window.ReactDOM = global.ReactDOM = require("react-dom/client");
window.Babel = global.Babel = Babel;

// Mismo bootstrap que index.html: runtime clasico, si no Babel emite `import`.
Babel.registerPreset("react-clasico", {
  presets: [[Babel.availablePresets["react"], { runtime: "classic" }]],
});

const src = html.match(
  /<script type="text\/babel" data-presets="react-clasico">([\s\S]*?)<\/script>/)[1];

const fallos = [];
const ok = (cond, msg) => { if (!cond) fallos.push(msg); };

let code;
try {
  code = Babel.transform(src, { presets: ["react-clasico"] }).code;
} catch (e) {
  fallos.push("Babel no pudo transformar el JSX: " + e.message);
}
if (code) {
  ok(!/^\s*import\s/m.test(code), "el codigo transformado emite `import`, la pagina quedara en blanco");
  try { (0, eval)(code); } catch (e) { fallos.push("error al ejecutar: " + e.message); }
}

const click = (el) => el.dispatchEvent(new window.MouseEvent("click", { bubbles: true }));
const espera = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  await espera(600);
  const d = window.document;

  let out = d.getElementById("root").innerHTML;
  ok(out.length > 1000, "la pantalla de perfil no monto");
  ok(out.includes("Cómo te mueves"), "faltan los grupos de condiciones");
  const chips = [...d.querySelectorAll(".chip")];
  ok(chips.length > 60, `se esperaban mas de 60 chips, hay ${chips.length}`);

  ["No puedo bajar al suelo", "Equilibrio limitado", "Dolor de rodilla"]
    .forEach((t) => {
      const c = chips.find((x) => x.textContent.trim() === t);
      ok(c, `no existe el chip "${t}"`);
      if (c) click(c);
    });
  await espera(200);

  const btn = [...d.querySelectorAll("button")].find((b) => b.textContent.includes("Ver resultados"));
  ok(btn, "no hay boton para pasar a resultados");
  if (btn) click(btn);
  await espera(250);

  out = d.getElementById("root").innerHTML;
  ok(out.includes("<svg"), "el mapa corporal no se dibujo");
  ok((out.match(/class="zone/g) || []).length >= 6, "faltan zonas en el mapa");
  ok((out.match(/class="card w-full/g) || []).length > 0, "no hay tarjetas de ejercicio");

  const card = d.querySelector(".card.w-full");
  if (card) click(card);
  await espera(250);
  ok(d.getElementById("root").innerHTML.includes('role="dialog"'), "la ficha de ejercicio no abre");

  if (fallos.length) {
    console.error("FALLOS:");
    fallos.forEach((f) => console.error("  - " + f));
    process.exit(1);
  }
  console.log("render OK: perfil, resultados, mapa y ficha montan correctamente");
})();
