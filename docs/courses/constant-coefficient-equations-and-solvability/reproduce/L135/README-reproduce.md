# Boundary measures and Green potentials in a half-space

`half-space-green-riesz-learner.md` gives the learner exposition, examples and complete solutions. `half-space-green-riesz-formal.md` gives the complete representation argument at locators GR1–GR11. The domain is the upper half-space in dimension at least two. A ball Poisson formula and explicit inversion supply its harmonic representation.

To reproduce both PNG/SVG figure pairs with Python, NumPy and Matplotlib:

```text
python make_figures123.py
```

The script also writes `figures/geometry.json`, containing exact coordinates, masses, kernels, sampling domains, color cutoff and proof locators. The figures depict the reflected interior pole, the normalized boundary Poisson kernel, and the inversion which converts one sphere atom into a linear height term. The plotted harmonic slice is the explicit function `P(x,0)/2+P(x,1)+t/4` at height one; its negative supplies an example satisfying the theorem's upper bound. Samples illustrate analytic formulas; the written argument supplies their proofs.

The sign convention is `Delta E = delta_0`, so the half-space Green kernel is nonpositive. The point singularity in the potential plot has a stated color cutoff, with its true value tending to minus infinity.

Original exposition and diagrams: CC0 1.0. Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. The retained DejaVu notice gives the font terms.

Classical source: Hörmander, *The Analysis of Linear Partial Differential Operators II*, Theorem 16.1.7, printed pp. 310–312 (PDF pp. 323–325), 1983 edition, second revised printing 1990, reprint 2005. The lower written proof routes are identified in the full argument.
