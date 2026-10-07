# Read and reproduce weighted Cauchy–Riemann existence

This lesson proves weighted solvability of the inhomogeneous Cauchy–Riemann
equations on complex Euclidean space. Strict positive Levi curvature gives the
exact data-divided-by-curvature square norm bound. A general PSH weight gives
the exact factor 2 estimate with `(1+|z|^2)^(-2)`.

Read `weighted-dbar-existence-learner.md` for four worked examples and nine
graded exercises with complete solutions. Read
`weighted-dbar-existence-formal.md` for the full W1–W28 argument: adjoint
identity, joint graph-domain approximation, closed-form projection, Hilbert
representation, explicit auxiliary convex weight, local weak extraction and
monotone PSH regularization. The graph-domain approximation and weak limiting
steps are part of the proof.

Earlier written inputs are L043 Lemma 1.1 on Hilbert representation, the linked
Lebesgue foundations, L140 UE2 on PSH smoothing, and L141 D5 on ball-mean
monotonicity. Later weighted extension theorems remain separate work.

Run with Python containing Matplotlib, NumPy and SciPy:

```text
python make_figures144.py
python check_examples144.py
```

The figure script makes two PNG/SVG pairs and `figures/geometry.json`.
`levi-curvature` plots the exact eigenvalues of the Hessian of
`2 log(1+|z|^2)` and an explicitly identified real test-vector section at
`z=(2,0)` in complex dimension 2. `disk-solution-budget` plots the exact
piecewise disk solution, its radial weighted norm density and its accumulated
norm ratio. The finite integration radius is labelled; its exact full limit
is `4 log(2)-2`. Both figures include proof locators and a human-source credit.
The SVG output uses a fixed identifier salt and omits generated dates.

The check script writes `independent-example-checks144.json`. Its24 Gaussian,
disk, Levi eigenvalue, ellipse and finite-data checks supplement the complete
exact arguments. Numerical quadrature is not used to establish existence or
replace a proof. No TeX process, browser profile or worker is required.

Human scholarly source: Lars Hörmander, *The Analysis of Linear Partial
Differential Operators II*, §15.1, Theorems 15.1.1–15.1.2, printed pp. 271–274,
1983 edition, second revised printing 1990, reprint 2005. All accompanying
expositions and artwork are original. Protected source pages, procurement
records, private reading scripts and private task state are excluded.

Original material is CC0 1.0; see `LICENSE.txt`. DejaVu Sans is used under the
separately retained font license. This lesson does not assert that the entire
AN-02 course or all of its proof prerequisites are closed.
