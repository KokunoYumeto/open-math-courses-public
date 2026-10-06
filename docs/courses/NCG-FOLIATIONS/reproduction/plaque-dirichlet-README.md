# Reproduce Figure 6.8c

Use Python 3 with NumPy and Matplotlib installed. Run:

```sh
python draw_plaque_dirichlet_input.py
```

The script writes `kt-plaque-dirichlet-input.png` and `.svg` into the sibling `figures` directory. It uses the DejaVu Sans fonts bundled with Matplotlib, and the Agg backend requires no graphical desktop. The reproduction used NumPy 2.4.4 and Matplotlib 3.10.9; the mathematical geometry and curves are explicit in the source.

The circle has radius 2/pi and physical circumference four. Panel B samples exact relative bump formulae at epsilon=1/16; the exact maxima are used rather than numerical normalization. Panels C and D draw proved formula bounds. They do not calculate operator norms or supply the proof. The theorem retains 0<epsilon<1/12; the plotted right endpoint is the continuous extension of its formulae. The complete proof is Proposition 6.8f, equations DD.1–DD.11.

The independently authored mathematical diagram and generator are dedicated to CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/. Matplotlib, NumPy and the bundled fonts retain their own licences; `FONT-NOTICE.txt` records the font terms. The SVG uses Matplotlib's ordinary outlined glyphs.
