# Reproducing the support-distance diagrams and examples

The formal and learner texts contain the geometric criterion, all domain
consequences, four worked examples and ten exercises with complete solutions.

With Python, Matplotlib and mpmath installed, run in this directory:

    python -B make_figures225.py
    python -B check_numerics225.py

The two PNG/SVG figure pairs show exact reflected support intervals,
equal boundary margins, compact confinement and a cancelled atom before
and after mollification. Their coordinate ledger distinguishes open domain
endpoints, closed compact endpoints, actual supports and convex hulls.
A temporary font cache is removed when the script exits.

The checker uses exact rational arithmetic for interval and rectangle
distances, compact confinement, component selection and translating supports.
Finite signed and complex atomic convolutions check cancellation and
reflection. Physical mollifier transforms and moments use 65 decimal digits.
These checks supplement the full written proofs and do not constitute an
independent mathematical review.

Original exposition, solutions, geometry and code use CC0 1.0.
The DejaVu font retains its own license. The cited internal ordinary-support
theorem and its earlier dependencies retain their existing attribution and
terms; their prose is not copied into this original packet. Referenced books
are credited in the lessons and are not included.
