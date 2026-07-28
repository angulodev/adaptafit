const {useState, useEffect, useMemo} = React;

/* ---------- textos ---------- */
const CAPA_INFO = {
  A_movilidad: {
    titulo: "Cómo te mueves",
    ayuda: "Descartan el ejercicio por completo. Si no puedes adoptar la postura, no hay forma de adaptarlo."
  },
  B_lesion_articular: {
    titulo: "Articulaciones",
    ayuda: "Descartan los ejercicios que cargan esa articulación por encima de tu umbral."
  },
  C_sistemica: {
    titulo: "Salud general",
    ayuda: "No descartan nada. Marcan con un aviso lo que conviene revisar antes."
  }
};

const ZONA_ES = {
  pecho:"Pecho", hombros:"Hombros", biceps:"Bíceps", triceps:"Tríceps",
  antebrazos:"Antebrazos", core:"Abdomen", espalda:"Espalda", lumbar:"Lumbar",
  gluteos:"Glúteos", cuadriceps:"Cuádriceps", isquios:"Isquios",
  gemelos:"Gemelos", caderas:"Caderas", cardio:"Cardio", otros:"Otros"
};

/* ---------- filtro ----------
   Replica engine.py: una contraindicación descarta, una precaución avisa. */
function filtrar(cat, sel, equipos) {
  const s = new Set(sel);
  const out = [];
  for (const e of cat.exercises) {
    if (equipos.length && !equipos.includes(e.eq)) continue;
    if (e.c.some(c => s.has(c))) continue;
    out.push({...e, avisos: e.w.filter(c => s.has(c))});
  }
  return out;
}

/* ---------- mapa corporal ----------
   Figura esquemática propia. No pretende ser anatómica: son zonas legibles. */
const FRENTE = {
  hombros:[["ellipse",{cx:63,cy:80,rx:17,ry:13}],["ellipse",{cx:137,cy:80,rx:17,ry:13}]],
  pecho:[["rect",{x:72,y:70,width:56,height:40,rx:14}]],
  core:[["rect",{x:76,y:114,width:48,height:52,rx:12}]],
  biceps:[["rect",{x:44,y:92,width:20,height:52,rx:10}],["rect",{x:136,y:92,width:20,height:52,rx:10}]],
  antebrazos:[["rect",{x:40,y:148,width:19,height:52,rx:9}],["rect",{x:141,y:148,width:19,height:52,rx:9}]],
  caderas:[["rect",{x:72,y:170,width:56,height:26,rx:12}]],
  cuadriceps:[["rect",{x:75,y:200,width:22,height:74,rx:11}],["rect",{x:103,y:200,width:22,height:74,rx:11}]]
};
const ESPALDA = {
  espalda:[["rect",{x:72,y:70,width:56,height:46,rx:14}]],
  triceps:[["rect",{x:44,y:92,width:20,height:52,rx:10}],["rect",{x:136,y:92,width:20,height:52,rx:10}]],
  lumbar:[["rect",{x:76,y:120,width:48,height:44,rx:12}]],
  gluteos:[["rect",{x:72,y:168,width:56,height:32,rx:14}]],
  isquios:[["rect",{x:75,y:204,width:22,height:70,rx:11}],["rect",{x:103,y:204,width:22,height:70,rx:11}]],
  gemelos:[["rect",{x:77,y:280,width:19,height:56,rx:9}],["rect",{x:104,y:280,width:19,height:56,rx:9}]]
};

function tono(n, max) {
  if (!n) return "var(--vacio)";
  const t = max ? n / max : 0;
  if (t > 0.66) return "var(--ink)";
  if (t > 0.33) return "var(--deep)";
  if (t > 0.12) return "var(--mid)";
  return "var(--soft)";
}

function MapaCuerpo({conteo, cara, setCara, zonaSel, setZona}) {
  const zonas = cara === "frente" ? FRENTE : ESPALDA;
  const max = Math.max(1, ...Object.values(conteo));
  return (
    <div className="mapa">
      <div className="mapa-toggle">
        {[["frente","Frente"],["espalda","Espalda"]].map(([k,l]) => (
          <button key={k} className="chip chip-sm" aria-pressed={cara===k}
                  onClick={() => setCara(k)}>{l}</button>
        ))}
      </div>

      <svg viewBox="0 0 200 360" className="mapa-svg" role="img"
           aria-label="Mapa del cuerpo. Cada zona se colorea según cuántos ejercicios tienes disponibles.">
        <g className="silueta">
          <circle cx="100" cy="36" r="19"/>
          <rect x="92" y="52" width="16" height="16" rx="5"/>
          <rect x="70" y="66" width="60" height="132" rx="18"/>
          <rect x="42" y="86" width="24" height="118" rx="12"/>
          <rect x="134" y="86" width="24" height="118" rx="12"/>
          <rect x="73" y="196" width="26" height="146" rx="13"/>
          <rect x="101" y="196" width="26" height="146" rx="13"/>
        </g>
        {Object.entries(zonas).map(([z, formas]) => {
          const n = conteo[z] || 0;
          const act = zonaSel === z;
          return (
            <g key={z} className={"zona" + (act ? " zona-sel" : "")} role="button" tabIndex="0"
               aria-pressed={act}
               aria-label={ZONA_ES[z] + ": " + n + (n === 1 ? " ejercicio" : " ejercicios")}
               onClick={() => setZona(act ? null : z)}
               onKeyDown={ev => {
                 if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); setZona(act ? null : z); }
               }}>
              {formas.map(([tag, at], i) => React.createElement(tag, {
                key: i, ...at, fill: tono(n, max),
                stroke: act ? "var(--ink)" : "none", strokeWidth: act ? 2.5 : 0
              }))}
            </g>
          );
        })}
      </svg>

      <ul className="leyenda">
        {[["var(--vacio)","nada"],["var(--soft)","poco"],["var(--deep)","bastante"],["var(--ink)","mucho"]]
          .map(([c,l]) => (
            <li key={l}><i style={{background:c}}/>{l}</li>
          ))}
      </ul>
    </div>
  );
}

/* ---------- perfil ---------- */
function Perfil({cat, sel, setSel, equipos, setEquipos, vivos, ir}) {
  const toggle = i => setSel(s => s.includes(i) ? s.filter(x => x !== i) : [...s, i]);
  const togEq = e => setEquipos(s => s.includes(e) ? s.filter(x => x !== e) : [...s, e]);

  return (
    <div className="pantalla pantalla-perfil">
      <header className="wrap cabecera">
        <p className="eyebrow">AdaptaFit</p>
        <h1 className="h1">Dinos qué evitar.<br/>Quitamos el resto.</h1>
        <p className="lede">
          Marca solo lo que te afecta. Puedes no marcar nada y ver el catálogo entero.
        </p>
      </header>

      {Object.entries(cat.layers).map(([capa, idxs]) => (
        <section key={capa} className="wrap seccion">
          <h2 className="h2">{CAPA_INFO[capa].titulo}</h2>
          <p className="ayuda">{CAPA_INFO[capa].ayuda}</p>
          <div className="chips">
            {idxs.map(i => (
              <button key={i} className="chip" aria-pressed={sel.includes(i)}
                      onClick={() => toggle(i)}>{cat.labels[i]}</button>
            ))}
          </div>
        </section>
      ))}

      <section className="wrap seccion">
        <h2 className="h2">Qué tienes a mano</h2>
        <p className="ayuda">Sin marcar nada se muestra todo el equipo.</p>
        <div className="chips">
          {cat.equipos.map(e => (
            <button key={e} className="chip" aria-pressed={equipos.includes(e)}
                    onClick={() => togEq(e)}>{e}</button>
          ))}
        </div>
      </section>

      <div className="barra-inf">
        <div className="wrap barra-inf-fila">
          <div className="cuenta">
            <p className="cuenta-num">{vivos.length}</p>
            <p className="cuenta-lbl">
              {vivos.length === 1 ? "ejercicio disponible" : "ejercicios disponibles"}
              {sel.length > 0 && " · " + sel.length + (sel.length === 1 ? " condición" : " condiciones")}
            </p>
          </div>
          <button className="btn" onClick={ir} disabled={!vivos.length}>Ver resultados</button>
        </div>
      </div>
    </div>
  );
}

/* ---------- ficha ---------- */
function Ficha({e, cat, cerrar}) {
  useEffect(() => {
    const esc = ev => { if (ev.key === "Escape") cerrar(); };
    window.addEventListener("keydown", esc);
    return () => window.removeEventListener("keydown", esc);
  }, [cerrar]);

  return (
    <div className="velo" onClick={cerrar}>
      <div className="hoja" role="dialog" aria-modal="true" aria-label={e.n}
           onClick={ev => ev.stopPropagation()}>
        <div className="asa"/>
        <p className="eyebrow">{ZONA_ES[e.z]} · {e.p}</p>
        <h2 className="h2 hoja-titulo">{e.n}</h2>
        <p className="ayuda">{e.eq} · dificultad {e.d} de 5</p>

        {e.avisos.length > 0 && (
          <div className="aviso">
            <p className="aviso-tit">Revísalo antes de hacerlo</p>
            <ul className="aviso-lista">
              {e.avisos.map(i => <li key={i}>{cat.labels[i]}</li>)}
            </ul>
            <p className="aviso-pie">
              No está descartado, pero tu situación aconseja consultarlo o empezar muy suave.
            </p>
          </div>
        )}

        {e.s.length > 0 && (
          <div className="bloque">
            <p className="bloque-tit">Sigue siendo seguro con</p>
            <div className="tags">
              {e.s.slice(0, 14).map(i => (
                <span key={i} className="tag">{cat.labels[i]}</span>
              ))}
            </div>
          </div>
        )}

        <p className="pie-tecnico">
          id {e.i} · confianza {e.cf.toFixed(2)}
          {e.v > 1 && " · agrupa " + e.v + " fichas equivalentes"}
        </p>
        <button className="btn btn-ancho" onClick={cerrar}>Cerrar</button>
      </div>
    </div>
  );
}

/* ---------- resultados ---------- */
function Resultados({cat, vivos, volver}) {
  const [cara, setCara] = useState("frente");
  const [zona, setZona] = useState(null);
  const [abierto, setAbierto] = useState(null);
  const [soloLimpios, setSolo] = useState(false);

  const conteo = useMemo(() => {
    const c = {};
    for (const e of vivos) c[e.z] = (c[e.z] || 0) + 1;
    return c;
  }, [vivos]);

  const lista = useMemo(() => {
    let l = zona ? vivos.filter(e => e.z === zona) : vivos;
    if (soloLimpios) l = l.filter(e => !e.avisos.length);
    return l.slice().sort((a, b) => a.d - b.d || a.n.localeCompare(b.n, "es"));
  }, [vivos, zona, soloLimpios]);

  const conAviso = vivos.filter(e => e.avisos.length).length;

  return (
    <div className="pantalla">
      <header className="wrap cabecera-res">
        <button className="chip chip-sm" onClick={volver}>← Perfil</button>
        <div className="cuenta">
          <p className="cuenta-num">{vivos.length}</p>
          <p className="cuenta-lbl">
            pasan tu filtro{conAviso > 0 && ", " + conAviso + " con aviso"}
          </p>
        </div>
      </header>

      <div className="wrap">
        <MapaCuerpo conteo={conteo} cara={cara} setCara={setCara}
                    zonaSel={zona} setZona={setZona}/>
      </div>

      <div className="wrap filtros">
        {zona && (
          <button className="chip chip-sm" aria-pressed="true"
                  onClick={() => setZona(null)}>{ZONA_ES[zona]} ✕</button>
        )}
        {conAviso > 0 && (
          <button className="chip chip-sm" aria-pressed={soloLimpios}
                  onClick={() => setSolo(v => !v)}>Ocultar los que tienen aviso</button>
        )}
        <span className="filtros-num">{lista.length}</span>
      </div>

      <ul className="wrap lista">
        {lista.length === 0 && (
          <li className="vacio">
            <p className="vacio-tit">Aquí no queda nada</p>
            <p className="ayuda">
              Ningún ejercicio de {zona ? ZONA_ES[zona].toLowerCase() : "esta selección"} pasa
              tu filtro. Toca otra zona del mapa.
            </p>
          </li>
        )}
        {lista.slice(0, 140).map(e => (
          <li key={e.i}>
            <button className="ej" onClick={() => setAbierto(e)}>
              <span className="ej-dif" aria-label={"dificultad " + e.d}>{e.d}</span>
              <span className="ej-txt">
                <span className="ej-nom">{e.n}</span>
                <span className="ej-meta">{e.eq} · {e.p}</span>
              </span>
              {e.avisos.length > 0 && <span className="ej-aviso">aviso</span>}
            </button>
          </li>
        ))}
        {lista.length > 140 && (
          <li className="mas">y {lista.length - 140} más. Toca una zona del mapa para acotar.</li>
        )}
      </ul>

      {abierto && <Ficha e={abierto} cat={cat} cerrar={() => setAbierto(null)}/>}
    </div>
  );
}

/* ---------- app ---------- */
function App() {
  const cat = window.CATALOGO;
  const [sel, setSel] = useState([]);
  const [equipos, setEquipos] = useState([]);
  const [vista, setVista] = useState("perfil");

  const vivos = useMemo(() => filtrar(cat, sel, equipos), [cat, sel, equipos]);

  return vista === "perfil"
    ? <Perfil cat={cat} sel={sel} setSel={setSel} equipos={equipos}
              setEquipos={setEquipos} vivos={vivos}
              ir={() => { setVista("resultados"); window.scrollTo(0, 0); }}/>
    : <Resultados cat={cat} vivos={vivos}
                  volver={() => { setVista("perfil"); window.scrollTo(0, 0); }}/>;
}

ReactDOM.createRoot(document.getElementById("root")).render(<App/>);
