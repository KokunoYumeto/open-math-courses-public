# Reproduce the angular Fourier checks and figures

Run the following with Python, mpmath, NumPy and Matplotlib:

    python -B -X utf8 angular-Fourier-check-and-figures.py

It computes independent one-dimensional Fourier pairings and anisotropic hyperplane averages at 90 decimal digits, then renders two exact support/test diagrams as PNG and SVG. The complete proof and all eight full solutions remain the mathematical authority; numerical checks supplement them.

The first diagram is the exact cubic source on the line through (3/5,4/5) and its whole transverse delta-derivative spectrum. The second is the standard two-dimensional Gaussian and its exact Radon average. The geometry JSON records coordinates, formulas and proof locators. SVG dates are omitted and the hash salt is fixed.

All original materials are CC0. The font licence is retained. The lesson links the exact parity-preserving extension, symmetric finite-part and Schwartz Fourier proofs from the preceding distribution course. General analytic-wavefront operation theorems are separate prerequisites.
