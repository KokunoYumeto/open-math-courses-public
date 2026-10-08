# Reproducing the support diagrams and examples

The formal and learner texts contain both necessary-condition proofs,
four worked examples and ten exercises with complete solutions.

With Python, Matplotlib and mpmath installed, run in this directory:

    python -B make_figures222.py
    python -B check_numerics222.py

The figure script produces two PNG/SVG pairs and an exact coordinate ledger.
One diagram shows disconnected translated domains, a compact test support,
and its reflected transpose support. The other shows tests approaching an
excluded boundary while their transpose supports stay in a fixed compact
set of the larger solution domain. A temporary font cache is removed on exit.

The checker uses 65 decimal digits for physical averaging integrals,
slow-decrease window examples, asymmetric smooth-kernel forcing,
complex integration by parts, Fourier derivative signs and rescaled test jets.
Exact rational checks cover support intervals, translations and boundary
distances. Logarithmic checks compare the exponential forcing obstruction
with its polynomial lower bound. These are supplementary checks, not proofs
of the two general theorems or an independent mathematical review.

Original exposition, solutions, mathematical geometry and code use CC0 1.0.
The DejaVu font retains its separate license. Referenced copyrighted works
are credited in the lessons; their expression and media are not included.
