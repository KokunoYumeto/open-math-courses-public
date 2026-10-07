# Reproduce the L142 illustrations

The full proof is `compact-measure-indicators-formal.md`; the learner lesson is `compact-measure-indicators-learner.md`. They include the complete hypotheses, original proof exposition, examples and full exercise solutions. Earlier-proof links are relative to an installed course reproduction directory `reproduce/L142/`.

With Python 3, NumPy and Matplotlib available, run:

```sh
python make_figures141.py
```

The program writes two native PNG images, two editable SVG images and `figures/geometry.json`. It uses the exact geometry and formulas described below and does not require an external typesetting engine.

- `complex-triangle-envelope` uses atoms at `(-1,0)`, `(1,0)`, `(0,2)` with coefficients `1`, `i`, `-1-i`. The support panel has equal Euclidean coordinate scales. In direction `(1,1)`, its support value is 2. The real frequency `(pi/4,-pi/2)` aligns the three terms, giving the exact envelope `log(exp(-y1)+exp(y1)+sqrt(2)*exp(2*y2))`. The shaded strip is the proved bound between the support function and that function plus `log(2+sqrt(2))`. Formal locators: MI4–MI5, MI7, equations MI22–MI24.
- `signed-density-growth` uses Lebesgue density `1_[-1,0]-1_[0,1]`, total mass zero, variation two and no endpoint atoms. The exact imaginary-ray quotient is `1-log(t)/t+2*log(1-exp(-t))/t`, evaluated with a stable exponential formula. The plotted interval is `1/2<=t<=32`; the proved limiting slope is one. Formal locators: MI2, MI5, MI7, equations MI25–MI27.

PNG dimensions are 2144×928 and 2144×880 pixels, respectively. SVG text remains editable. Labels use DejaVu Sans, whose separate notice is in `DejaVu-font-license.txt`. Original proof exposition, examples, solutions, figure geometry, drawing program and diagrams use CC0 1.0; see `LICENSE.txt`.

Classical source credit: Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (1983 edition; second revised printing 1990; reprint 2005), §16.3, Lemma 16.3.1, printed p. 319 (PDF p. 332). The illustrations show the original arguments and examples.
