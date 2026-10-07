# Reproduce the L140 illustrations

The formal proof is `constant-upper-envelopes-formal.md`; the learner lesson is `constant-upper-envelopes-learner.md`. Both include the full hypotheses, original arguments, examples and complete exercise solutions. Their earlier-proof links are relative to an installed course reproduction directory `reproduce/L140/`.

Run the figure program from this directory with Python 3, NumPy and Matplotlib available:

```sh
python make_figures134.py
```

The program writes two native PNG images, two editable SVG images and `figures/geometry.json`. It uses the mathematical formulas directly and does not use an external typesetting engine.

- `logarithmic-tail-envelopes` samples `log(r)/j` and draws the exact regularized tail `max(0,log(r))/k`. The original logarithmic samples omit `r=0`; the caption states its actual minus-infinite value. The separate regularized center value is zero. Formal proof locators: UE3–UE5, UE8, equations UE26–UE27.
- `scaled-translation-averages` draws the exact complex translation rectangle, the absolute-value profiles and their exact piecewise integrals. It uses `q(zeta)=abs(Im zeta)`, `y=1`, rectangle `[-1,1]+i[0,1]`, and `t=1,2,4,8`. The fixed-center limit is one. Formal proof locators: UE7–UE8, equations UE23, UE28–UE29.

PNG dimensions are 2144×880 and 2880×928 pixels, respectively. SVG labels remain editable text. Matplotlib renders labels with DejaVu Sans; `DejaVu-font-license.txt` retains the font's separate terms. Original figure geometry, code, proof exposition, examples and solutions use CC0 1.0; see `LICENSE.txt`.

Classical source credit: Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (1983 edition; second revised printing 1990; reprint 2005), §16.2, Lemma 16.2.3 and the following real-parameter remark, printed p. 316 (PDF p. 329). The illustrations visualize the original proof and examples; no book page image is included.
