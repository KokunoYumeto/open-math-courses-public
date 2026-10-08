# Reproduce the near-variety solution lesson

The original sources give the full weak near-characteristic-variety representation and complex characteristic-weight transfer, four worked examples and ten exercises with complete solutions. The formal proof includes the polynomial jet correction, nonsmooth strict weighted estimate, compact-support check, legitimate transpose annihilation and fixed-weight Hilbert limit.

Run the scripts with Python, NumPy, mpmath and Matplotlib:

    python -B check_examples163.py
    python -B make_figures163.py

The first script integrates the actual disk exponentials and densities, differentiates the defining jet norm in real coordinates at high precision, and checks physical differential solutions, characteristic vectors, tube bounds and radial extrema. These calculations supplement the full proofs; they do not establish recursive prerequisite closure.

The second script writes two PNG/SVG figure pairs and exact geometry JSON. It uses the DejaVu font family and needs no TeX installation. SVG dates are omitted and a fixed hash salt is used. The retained font license has its own terms. The diagrams are original; no protected book pixels or body text are included.

Figure NV-A keeps the reflected repair center, indicator and convolution radii, derivative-support annulus, original tube and exact disk-density phases. Figure NV-B keeps the complete polynomial jet formula and exact scalar curvature comparison, including analytic maximum coordinates. The displayed sample scales are not asserted sufficient for every weight.

Classical sources: Lars Hörmander, The Analysis of Linear Partial Differential Operators II, §15.3, Theorem 15.3.1 and Corollary 15.3.2, printed pp. 287–291, 1983 edition, second revised printing 1990, reprint 2005. The original proofs and their earlier freely readable course inputs are linked in the formal source.

The real regularity equivalence exercise and subsequent surface representation, discriminant, multiplicity and topology targets require separate arguments.
