# Read and reproduce the density of entire logarithms

This original lesson proves all three exact targets: the local-integral
density of normalized logarithms of nonzero entire scalar functions,
dense-set convergence below a continuous subharmonic comparison, and the
bounded-Cauchy–Riemann point estimate with its continuous representative.

Read `entire-logarithm-density-learner.md` for four worked examples and ten
graded exercises with complete solutions. The formal companion supplies the
whole construction: exact Newtonian kernel sign and factors, continuity,
quadratic Taylor gaps, disjoint cutoff errors, strict weighted correction,
the one-third interpolation margin, expanding-ball qualification, smoothing
of proper singular weights, two diagonal selections and the reverse closure.
Scalar-log PSH and local-integrability properties are proved explicitly.

The actual earlier written inputs are L143 HC1–HC9 compactness and PSH
closure, L131 NP2/NP4 local integrability and the fundamental solution for
`Delta`, L140 UE2 positive PSH smoothing, L144 W1 strict weighted existence,
and L145 E3 joint holomorphic regularity. The curvature-weighted data
hypothesis is used exactly, with weight `2N*phi`.

With Python containing SciPy, Matplotlib and NumPy, run:

```text
python check_examples154.py
python make_figures154.py
```

The check script writes `independent-example-checks154.json`: 41 independent
physical quadratures evaluate actual polynomial logarithms over circles
and disks, compare the two-dimensional weighted seed error with its radial
integral, integrate the Newtonian derivative kernel, verify shrinking-bump
norm scaling and integrate the affine antiholomorphic example. Tiny seed
errors are rescaled before integration. No correction solution is numerically
claimed, and no general density or compactness theorem is inferred from
the numerical checks.

The figure script writes two PNG/SVG pairs and `figures/geometry.json`.
The first figure shows the exact centers, disjoint smooth cutoff annuli,
quadratic weight gap and actual normalized closed error. It does not plot
the correction supplied by the existence theorem. Positive errors below
the stated logarithmic plot floor are omitted from the plotted curve.
The second figure shows the actual 13 polynomial zeros, the fixed point
at which pointwise convergence fails, and the exact disk integral error
`pi*R^2*log(2)/N`, with independent physical quadrature points.
Every figure has proof locators and a human scholarly-source credit.
SVG identifiers have a fixed salt and no generated date.

Human source: Lars Hörmander, *The Analysis of Linear Partial Differential
Operators II*, §15.1, Theorem 15.1.6 and Lemmas 15.1.7–15.1.8, printed
pp. 277–278; 1983 edition, second revised printing 1990, reprint 2005.
The source's density theorem is not used in its later arguments, but remains
an assigned target here. The comparison in the dense-set lemma is `phi_j <=
phi`, not a nonpositive-sequence condition.

Original exposition, examples, solutions, scripts and artwork use CC0 1.0;
see `LICENSE.txt`. DejaVu Sans retains its separately included font license.
Protected native book text, page images, private reading scripts and task
state are absent from the distributable original packet. No TeX process,
worker, outgoing session message or backup copy is required. The remaining
assigned course targets still require their own complete proofs and audit.
