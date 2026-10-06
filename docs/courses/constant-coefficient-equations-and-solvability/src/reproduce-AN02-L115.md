# Reproduce the Support cones force reciprocal bounds

These original drawings accompany Support cones force reciprocal bounds. The complete mathematical proof, all worked examples and complete solutions remain in that reader.

## Download the unchanged original files

Keep `make_figures.py` at the root of an empty scratch directory and the remaining files in `figures/`. The renderer creates `figures/` during a fresh run.

- [make_figures.py](../reproduce/L115/make_figures.py) — 4912 bytes; SHA-256 `2BC333EED0FBD68D0550B21749764AAE3435A4760ABD443974CC5503A5728AF8`.
- [finite-truncation-error.png](../reproduce/L115/figures/finite-truncation-error.png) — 53606 bytes; SHA-256 `B5A8CF0FE0F305EA6D2B2F15BDF1384EC9879101DFAB0E4E21260243CB480178`.
- [finite-truncation-error.svg](../reproduce/L115/figures/finite-truncation-error.svg) — 27989 bytes; SHA-256 `CB05558AF18FD1842472B0C290C06033F4DED4F69EB0125A4BFEB522779586FC`.
- [scene.json](../reproduce/L115/figures/scene.json) — 1147 bytes; SHA-256 `953667A77C37346DC4CC1005647B1B83679F1069C5D6C3BC245F95B062EC0F0B`.
- [translated-cone-and-kernel.png](../reproduce/L115/figures/translated-cone-and-kernel.png) — 61788 bytes; SHA-256 `364EC3F86F117521CC5943BABBE4001972B8FBD485A07A9B64862C0F092CF5E9`.
- [translated-cone-and-kernel.svg](../reproduce/L115/figures/translated-cone-and-kernel.svg) — 35118 bytes; SHA-256 `8D4C9FC5CA647DB38562CDFBEAE441CB34C8EA124FEECE4E115AF69EED64C178`.

## Run the renderer

The unchanged program requires Python, NumPy and Matplotlib. In the scratch directory run:

```text
python -X utf8 make_figures.py
```

It writes the supplied PNG, SVG and exact geometry files. A fresh replay with Python 3.13.9, NumPy 2.4.4 and Matplotlib 3.10.9, using Matplotlib’s bundled DejaVu Sans font, matched every supplied file byte for byte and all decoded PNG RGBA pixels. No SVG date or identifier normalization was performed. Byte identity is qualified by that observed software and font environment; different versions may change rendering bytes. The geometry files specify the mathematical objects independently of rendering.

## Check the mathematics and credits

Figure 1 has exact vertex −a=(−1,1), directions v₁=(1,1), v₂=(1,−1), compact kernel coefficients 1, −2, −3, 6, and inverse hull x+1≥|y−1|. The displayed lattice is finite; the full inverse is unbounded. Figure 2 displays the exact three error atoms (3,3,−8), (3,−3,−27), (6,0,216) of F₂, with supporting line x=3. See Theorem 1.1, Example 6.1 and both complete captions. The theorem proves the general forward implication; the general converse remains separate.

The original renderer, scene/geometry and diagrams are GPT-6.1 Sol (OpenAI), Ultra work, October 2026, dedicated under CC0. Matplotlib and the bundled DejaVu Sans font retain their own component terms already included with this course. The native geometry is explanatory; the full proof establishes the theorem.
