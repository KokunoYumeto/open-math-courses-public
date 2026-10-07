# Read and reproduce analytic-functional Fourier transforms

This original lesson proves the exact Fourier criterion for analytic
functionals carried by a nonempty compact convex real set: every positive
exponential loss is allowed, with a different finite constant for each loss.
The source definition uses linear forms on entire holomorphic tests. The proof
also constructs and uniquely identifies their action on holomorphic germs for
this convex carrier.

Read `analytic-functional-fourier-learner.md` for four worked examples and ten
graded exercises with complete solutions. The formal companion supplies the
full necessity, uniqueness and converse, including the exact diagonal graph,
support function, global oscillation check, holomorphic-moment compatibility
and every-neighborhood Cauchy estimate. Its local-test argument is explicitly
qualified to the convex carrier here; it does not claim the more general
nonconvex real-carrier approximation proposition.

The actual earlier inputs are L145 E2, holomorphic extension with its proved
growth exponent, and L122 CF2.1, the full compact-distribution Fourier theorem.
The construction uses the former in complex dimension `2n` and the latter in
real dimension `2n`. An explicit infinite-order point functional demonstrates
why a real point-supported distribution is not supplied in general.

With Python containing Matplotlib, NumPy and SciPy, run:

```text
python make_figures151.py
python check_examples151.py
```

The figure script produces two PNG/SVG pairs and `figures/geometry.json`.
The first figure shows the exact closed complex thickening of `[-1,1]` and
the parameter plane of the diagonal graph, with all four real graph
coordinates displayed. It does not present a spatial projection as the
full graph. The second figure plots the positive real series of the
infinite-order example. Its upper bounds, one-term lower bound and
loss-dependent constants are individually labeled. A finite plot is not
the proof of failure of every polynomial bound; that proof is written.
Figures include exact proof locators and human scholarly-source citations.
SVG identifiers use a fixed salt and have no generated date.

The check script writes `independent-example-checks151.json`. Seventeen
physical quadratures compare 75-digit positive series summation against an
independent exact real-circle integral, integrate the actual carrier area,
and check example circle means. The report also records exact point moments
and the diagonal sample. These calculations supplement the proofs; they do
not prove the general Fourier criterion, germ compatibility or finite-jet
obstruction by sampling.

Human sources: Lars Hörmander, *The Analysis of Linear Partial Differential
Operators II*, §15.1, Theorem 15.1.5, printed p. 276, 1983 edition, second
revised printing 1990, reprint 2005; volume I, Definition 9.1.1 and the
local-test discussion following Proposition 9.1.2, printed pp. 326–328,
1983 edition, second edition 1990, reprint 2003.

Original exposition, examples, solutions and artwork use CC0 1.0; see
`LICENSE.txt`. DejaVu Sans retains its separate included font license.
Native protected book pages, private reading scripts and task state are
excluded from the distributable original packet. No TeX process, browser
profile, worker or backup copy is required. Remaining Chapter 15 and 16
targets and the entire assigned course retain their own unfinished scope.
