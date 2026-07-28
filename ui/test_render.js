/**
 * Harness de render. Carga el index.html YA CONSTRUIDO en jsdom y deja que
 * ejecute sus propios scripts, igual que un navegador. Comprueba que las dos
 * pantallas montan, que el mapa se dibuja y que la ficha abre.
 *
 *   npm install jsdom
 *   node ui/build.js && node ui/test_render.js
 *
 * Existe porque un fallo al arrancar deja la pagina en blanco sin escribir
 * nada util, y eso es indistinguible de un problema de CSS o de red.
 */
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");

const HTML = path.join(__dirname, "index.html");
if (!fs.existsSync(HTML)) {
  console.error("Falta ui/index.html. Generalo con: node ui/build.js");
  process.exit(1);
}

const fallos = [];
const ok = (cond, msg) => { if (!cond) fallos.push(msg); };
const espera = ms => new Promise(r => setTimeout(r, ms));

const dom = new JSDOM(fs.readFileSync(HTML, "utf8"), {
  runScripts: "dangerously",
  pretendToBeVisual: true,
  url: "http://localhost/",
});
const { window } = dom;
const d = window.document;

window.addEventListener("error", e => fallos.push("error en pagina: " + e.message));
const click = el => el.dispatchEvent(new window.MouseEvent("click", { bubbles: true }));

(async () => {
  await espera(700);

  const externos = [...d.querySelectorAll("script[src], link[rel=stylesheet]")];
  ok(externos.length === 0,
     `hay ${externos.length} recurso(s) externo(s); el archivo debe ser autocontenido`);

  let out = d.getElementById("root").innerHTML;
  ok(out.length > 1000, "la pantalla de perfil no monto (root vacio)");
  ok(out.indexOf("Como te mueves") >= 0 || out.indexOf("mueves") >= 0,
     "faltan los grupos de condiciones");
  const chips = [...d.querySelectorAll(".chip")];
  ok(chips.length > 60, `se esperaban mas de 60 chips, hay ${chips.length}`);

  const antes = d.querySelector(".cuenta-num");
  ok(antes && Number(antes.textContent) > 500,
     "el contador inicial deberia mostrar el catalogo entero");

  ["No puedo bajar al suelo", "Equilibrio limitado", "Dolor de rodilla"].forEach(t => {
    const c = chips.find(x => x.textContent.trim() === t);
    ok(c, `no existe el chip "${t}"`);
    if (c) click(c);
  });
  await espera(200);

  const despues = Number(d.querySelector(".cuenta-num").textContent);
  ok(despues > 0 && despues < 694, `el filtro no redujo el catalogo (${despues})`);

  const btn = [...d.querySelectorAll("button")].find(b => b.textContent.indexOf("Ver resultados") >= 0);
  ok(btn, "no hay boton para pasar a resultados");
  if (btn) click(btn);
  await espera(250);

  out = d.getElementById("root").innerHTML;
  ok(out.indexOf("<svg") >= 0, "el mapa corporal no se dibujo");
  ok(d.querySelectorAll(".zona").length >= 6, "faltan zonas en el mapa");
  ok(d.querySelectorAll(".ej").length > 0, "no hay tarjetas de ejercicio");

  const nAntes = d.querySelectorAll(".ej").length;
  const zona = d.querySelector(".zona");
  if (zona) click(zona);
  await espera(200);
  ok(d.querySelectorAll(".ej").length !== nAntes || d.querySelector(".vacio"),
     "tocar una zona del mapa no filtro la lista");
  if (zona) click(zona);
  await espera(200);

  const card = d.querySelector(".ej");
  if (card) click(card);
  await espera(250);
  ok(d.querySelector('[role="dialog"]'), "la ficha de ejercicio no abre");
  ok(d.querySelector(".pie-tecnico"), "la ficha no muestra id ni confianza");

  if (fallos.length) {
    console.error("FALLOS:");
    fallos.forEach(f => console.error("  - " + f));
    process.exit(1);
  }
  console.log("render OK - autocontenido, perfil, filtro, mapa, zona y ficha");
  process.exit(0);
})();
