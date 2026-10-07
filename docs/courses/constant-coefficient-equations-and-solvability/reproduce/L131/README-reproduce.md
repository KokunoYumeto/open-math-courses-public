# Reproduce the lesson diagrams

The lesson proves local integrability and a convolution continuity criterion for subharmonic functions, using the explicit Laplacian kernel, a compact local cutoff and harmonic smoothing. The learner exposition is in `newtonian-potentials-learner.md`; the complete argument is in `newtonian-potentials-formal.md`.

The script `make_figures107.py` needs Python, NumPy and Matplotlib. Run:

```text
python make_figures107.py
```

It writes the two PNG/SVG figure pairs and `figures/geometry.json`. The JSON retains the exact coordinates, masses, radii, analytic formulas and proof locators. The blue/orange bubble areas show retained/remaining mass. The integrability curves are samples of the exact formulas in NP4 and NP10.

The potential formulas use the convention `Delta E = delta_0`. The planar kernel is `log(r)/(2*pi)`; in dimension greater than two it is `-r^(2-n)/((n-2)*area(S^(n-1)))`. The unit-ball density has integral one. Neither an excluded critical exponent nor a one-dimensional interpretation of `n/(n-2)` is asserted.

Original exposition, examples and diagrams: CC0-1.0. Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Classical source: Hörmander, *The Analysis of Linear Partial Differential Operators II*, Chapter 16, Proposition 16.1.1, printed page 304 (PDF page 317). See `LICENSE.txt` and the retained DejaVu font notice.
