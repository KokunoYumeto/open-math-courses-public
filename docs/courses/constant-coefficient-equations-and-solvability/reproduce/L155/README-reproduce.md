# Reproduce the arbitrary-distribution representation lesson

The formal and learner sources, exact geometry, figure program and actual independent-check results are original course material under CC0 1.0. The retained DejaVu font license keeps its own terms. The classical human source is Lars Hörmander, The Analysis of Linear Partial Differential Operators II, the two unnumbered representation exercises on printed page300.

Use Python with NumPy, Matplotlib and mpmath:

    python -B -X utf8 check_examples178.py
    python -B -X utf8 make_figures178.py

The figure program writes two PNG/SVG pairs and their exact geometry description. SVG date metadata is omitted and its identifier salt is fixed. The images display exact scalar energy profiles, the actual repeated-characteristic solution kernels and explicitly sampled positions of an infinite locally finite distribution. Read the geometry for metric, measure, normalizations and exact proof locators.

The checks independently differentiate actual kernels, integrate rational norm moments and imaginary Gaussian profiles, compute the strict seed's complex Hessian from its defining real function, test compact triangle transforms and the triple triangle's distributional derivative, and check isolated point-mass phases. Auxiliary noncompact Gaussian contour probes are labeled as such; they supplement sign checks. A compact cutoff equal to one on the spline carrier makes its derivative probe an actual compact test.

These finite computations do not prove the arbitrary-distribution results. Their full proofs include finite-exhaustion weighted envelopes, local exterior derivative regularity identified by tested logarithmic contours, uniform physical mollifier neighborhood membership, compact entire division, legitimate smooth equation tests, final weighted surface limits and Hilbert densities.

No TeX compilation, book body, book-page image, protected source dependency or network access is needed to reproduce this original packet.
