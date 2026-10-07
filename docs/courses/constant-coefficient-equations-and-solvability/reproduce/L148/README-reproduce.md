# Reproduce the complex Fourier estimates lesson

This packet contains the original formal proof CF1–CF12, four worked examples,
ten complete exercise solutions, two original figure pairs and independent
calculations for AN02-L148.

The formal proof reconstructs all three estimates of Hörmander II, Lemma 15.2.2
(printed pp. 280–281), and the complete weak representation of Theorem 15.2.4
(printed pp. 286–287). It uses the negative-exponential Fourier convention and
the bilinear reflected reciprocal weight. It does not assert completion of the
four-condition weight construction, the neighboring topology discussion, or
the entire course.

Run from this folder with Python, NumPy, SciPy and Matplotlib:

    python -B -X utf8 check_examples157.py
    python -B -X utf8 make_figures157.py

The figures use exact mathematical formulas and physical quadrature samples.
Their editable geometry and constants are recorded in figures/geometry.json.
No external TeX program or Blender scene is needed for these one-dimensional
functions and two-dimensional measure geometry.

The first figure depicts an interval indicator, its exponentially weighted
physical function, the exact support-damped complex transform on four planes,
and its normalized plane energy. Its ceiling one is specific to the interval
model, not a stronger general weighted theorem.

The second depicts real-axis measure, the intersection of an open unit disk
centered at 1/4+i/2 with that axis, and its mass sqrt(3). It compares truncated
absolute and squared-data integrals for V(xi)=(1+xi^2)^(-3/8). The actual data
norm has the explicitly identified constant multiplier exp(4); the figure
omits that multiplier. The divergence lower bound is proved, and the finite
squared integral's horizontal line is a physical quadrature value. The
truncation range starts at T=1.05 so every plotted lower-bound value is positive
on its logarithmic axis.

Fifty-three independent checks evaluate actual physical transforms and
pairings, norm identities, Fourier truncation errors with rigorous tails,
reflected dual weights, measure-data tails, divergent absolute integrals and
lattice shell counts. These computations supplement the complete arguments;
they do not prove general statements by sampling.

All original prose, scripts and figures use CC0. The font license is separate.
No protected book pages, extracted text or media are included. Ordinary
scholarly attribution appears in the formal proof.
