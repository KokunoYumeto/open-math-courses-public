# Reproducing the convex approximation diagrams and examples

The formal and learner texts contain the full arguments and ten solved exercises.
The two diagrams use the exact coordinates and contour bounds in those texts.
Run from this directory with Python, NumPy, Matplotlib and mpmath installed:

    python -B make_figures216.py
    python -B check_numerics216.py

The figure script produces the PNG/SVG pairs and the editable geometry data.
Its temporary Matplotlib cache is removed when the script exits.
The example checker compares transverse Cauchy quotients through colliding roots,
finite jets of an exponential divisor with a physical derivative distribution,
Minkowski support functions with all physical vertex sums, exact rational contour
bounds, and compact analytic-germ Gaussian integrals at 65 decimal digits.
The finite Gaussian average of the quadratic example has bias \(1/(2j)\);
that is an approximation effect, not integration error.
The generated probe report is supplementary and does not replace the proofs or
claim an independent mathematical review.

Original exposition, code and mathematical figure geometry are CC0 1.0.
The DejaVu font used for figure text has its separate retained license.
References are identified in the lessons; their copyrighted expression is not
included in this original material.
