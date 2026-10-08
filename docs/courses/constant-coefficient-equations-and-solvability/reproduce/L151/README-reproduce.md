# Reproduce the Hermite and discriminant lesson

The original sources prove the full Hermite jet estimate with both ordered and unordered root-distance conventions and the full local analytic division bound with the derivative strength of the discriminant. They include four worked examples and ten exercises with complete solutions.

Run Python with NumPy, mpmath and Matplotlib:

    python -B check_examples166.py
    python -B make_figures166.py

The independent checks solve the actual Hermite jet systems, integrate the actual contour remainder, verify the entire quotient series at colliding parameters, differentiate the real surface map, and integrate both its full area data and its two-root projection data. They also check the polynomial-strength means and the Euclidean-ball rational division example. These calculations supplement the full proof; they do not infer recursive prerequisite closure.

The figure script writes two original PNG/SVG pairs and exact geometry JSON. It keeps the two root-product conventions, analytically attained unit-disk supremum, complex squaring map, branch count, Euclidean-ball cutoff and full Gram/Jacobian density. The plane diagrams are labeled projections of a surface in four real ambient dimensions. A 3D embedding would not preserve that entire metric.

The script uses DejaVu fonts and needs no TeX installation. SVG dates are omitted and a fixed hash salt is used. The retained font license keeps its own terms. The sources contain no protected book body or media.

Classical targets: Lars Hörmander, The Analysis of Linear Partial Differential Operators II, §15.3, Lemmas 15.3.4–15.3.5, printed pp. 292–293; the derivative-strength convention is §10.4, formula 10.4.2, printed p. 32. Edition: 1983, second revised printing 1990, reprint 2005.

The global hypersurface area bound, anisotropic cover, weighted repair and complete surface solution representation require the subsequent proofs.
