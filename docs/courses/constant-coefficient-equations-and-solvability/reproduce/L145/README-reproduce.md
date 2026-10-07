# Read and reproduce weighted holomorphic extension

This lesson proves extension of an entire function from a complex linear
subspace with the exact `(6 pi exp(C))^k` square norm bound and weight
`(1+|z|^2)^(-3k)`. It also proves the exact `n+2k+1` polynomial growth
transfer for exponentially bounded data.

Read `weighted-holomorphic-extension-learner.md` for four worked examples and
ten graded exercises with complete solutions. The formal source gives the
whole proof, including distributional holomorphic regularity, the annular
cutoff data, pointwise restriction recovery, preservation of the original
normal-comparison constant through all codimension steps, and the fixed-ball
growth estimate. The separate normal-monotone comparison has its own stronger
hypothesis and does not replace the general theorem.

Earlier written inputs are L144 general PSH weighted Cauchy–Riemann existence
and L131 NP5 on harmonic smoothing and the mean identity. The joint Cauchy
power-series step and every extension/iteration step are written here.

With Python containing Matplotlib, NumPy and SciPy, run:

```text
python make_figures147.py
python check_examples147.py
```

The figure script writes two PNG/SVG pairs and `figures/geometry.json`.
The normal-plane diagram shows the exact cutoff radii, annular coefficient
and the hypothetical normal-pole obstruction to a nonzero trace difference.
The obstruction is explicitly distinguished from a returned solution.
The codimension diagram tracks complex dimensions, inverse weight powers and
the fixed comparison constant. Its curves are proved upper bounds, with the
additional normal-monotone hypothesis labelled. They are not solution norms.
Both figures give exact proof locators and a human scholarly-source credit.
The SVG files use a fixed identifier salt and contain no generated dates.

The check script writes `independent-example-checks147.json`: 29 physical
radial quadratures verify the annular error norm, integer-dimensional radial
integrals, finite polynomial data, direct-extension bounds and the growth
example. These checks supplement the complete exact proofs; they do not
establish extension, replace the trace argument or close the whole course.
No TeX process, browser profile, worker or backup copy is required.

Human source: Lars Hörmander, *The Analysis of Linear Partial Differential
Operators II*, §15.1, Theorem 15.1.3 and Corollary 15.1.4, printed pp. 274–276;
1983 edition, second revised printing 1990, reprint 2005. All included exposition,
examples, solutions and artwork are original. Protected book pages, private
reading scripts, private task state and procurement records are excluded.

Original material is CC0 1.0; see `LICENSE.txt`. DejaVu Sans retains the
separately included font license. Remaining analytic-functional and weighted
Fourier targets and the entire assigned course retain their own proof scope.
