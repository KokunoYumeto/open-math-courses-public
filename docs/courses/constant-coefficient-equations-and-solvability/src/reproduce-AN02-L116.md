# Reproduce the When zero smooth periods mean that a cycle bounds

These original drawings accompany When zero smooth periods mean that a cycle bounds. The complete mathematical proof, all worked examples and complete solutions remain in that reader.

## Download the unchanged original files

Keep `render_detection.py` at the root of an empty scratch directory and the remaining files in `figures/`. The renderer creates `figures/` during a fresh run.

- [render_detection.py](../reproduce/L116/render_detection.py) — 6418 bytes; SHA-256 `78A341BC9C6E182678D003E00CFE9668B8029634248089CCF2B976DFB35376AE`.
- [cycle-detection.geometry.json](../reproduce/L116/figures/cycle-detection.geometry.json) — 51787 bytes; SHA-256 `503A6B20CD4C26882222EF18EFC8126996678D8E20A435ED9CBFEADE7D483798`.
- [cycle-detection.png](../reproduce/L116/figures/cycle-detection.png) — 232421 bytes; SHA-256 `13641EA222BC41BBE23FEFB8B53FA4A96E218302918EF9E0F41E33661A6F6984`.
- [cycle-detection.svg](../reproduce/L116/figures/cycle-detection.svg) — 116328 bytes; SHA-256 `AA95739469C02F8C5B25659825C56D05E153D1D82EE9E601CB8DA5E794542F7D`.

## Run the renderer

The unchanged program requires Python, NumPy and Matplotlib. In the scratch directory run:

```text
python -X utf8 render_detection.py
```

It writes the supplied PNG, SVG and exact geometry files. A fresh replay with Python 3.13.9, NumPy 2.4.4 and Matplotlib 3.10.9, using Matplotlib’s bundled DejaVu Sans font, matched every supplied file byte for byte and all decoded PNG RGBA pixels. No SVG date or identifier normalization was performed. Byte identity is qualified by that observed software and font environment; different versions may change rendering bytes. The geometry files specify the mathematical objects independently of rendering.

## Check the mathematics and credits

The left panel has eight balls centered at exp(iπj/4), radius 3/5, and the positively oriented unit circle. The arc distance bound is 2 sin(π/16)<3/5. These balls cover the displayed cycle, not all of the punctured plane. The right panel records δ horizontally, (−1)ᵖdᵥ vertically, and finite elimination along (0,2)→(1,1)→(2,0). It is an algebraic grid, not a geometric circle deformation. See Figure L1, Worked example 1, CD2–CD5c and the full CD0–CD10 proof. Georges de Rham and Allen Hatcher receive exact historical and method credits in the reader.

The original renderer, scene/geometry and diagrams are GPT-6.1 Sol (OpenAI), Ultra work, October 2026, dedicated under CC0. Matplotlib and the bundled DejaVu Sans font retain their own component terms already included with this course. The native geometry is explanatory; the full proof establishes the theorem.
