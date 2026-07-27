# AdaptaFit — slice vertical

Primera interfaz. Un solo archivo, sin build. Abrir `index.html` servido por
HTTP (no `file://`, porque hace `fetch` de `catalog.json`).

```bash
cd ui && python3 -m http.server 8000
```

Alcance deliberado: perfil → mapa corporal → lista filtrada. **Sin rutinas, sin
progresión, sin persistencia.** Sirve para responder una sola pregunta: ¿el
modelo de tres capas produce resultados coherentes cuando se le presentan a una
persona?

- `index.html` — React UMD + Babel, Tailwind CDN, sin build.
- `catalog.json` — generado por `enrichment/scripts/build_ui_catalog.py`.

Los nombres están traducidos mecánicamente por reglas gramaticales. Es
provisional y se nota: pendiente de revisión editorial.
