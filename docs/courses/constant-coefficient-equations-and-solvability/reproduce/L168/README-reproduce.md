# Reproducing the analytic-forcing illustrations and examples

The formal and learner texts contain the full general proof, four worked
examples and ten exercises with complete solutions.

With Python, NumPy, Matplotlib and mpmath installed, run in this directory:

    python -B make_figures219.py
    python -B check_numerics219.py

The first script produces two PNG/SVG figure pairs and their coordinate ledger.
The illustrations show the exact resonant averaging identity and strict
compact margins of nested source and equation intervals. Open circles mark
excluded endpoints. A temporary Matplotlib font cache is removed on exit.

The supplementary checker uses 65 decimal digits for physical convolution
integrals, resonant multiplier derivatives, translated derivative kernels,
point-carrier moments, the boundary telescoping solution, Cauchy-circle
quotients through a multiplier zero, and asymmetric smoothing reflections.
Exact rational checks cover the interval erosion, strict margins and geometric
tails. These checks supplement the written arguments. They are not proofs of
the full theorem and do not constitute an independent mathematical review.

The original exposition, solutions, geometry and code use CC0 1.0.
The DejaVu font has its separately retained license. Referenced works are
credited in the lessons; their copyrighted expression and media are not included.
