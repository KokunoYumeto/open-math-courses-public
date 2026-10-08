# Reproduce the singular-support hull examples

The original proof, learner material, complete solutions and figure programs use CC0 1.0. The DejaVu font license retains its own terms.

With Python 3, NumPy, SciPy, Matplotlib and mpmath installed, run:

    python -B make_figures188.py
    python -B check_contours188.py

The figure program writes PNG/SVG pairs and exact geometry. The strip boundary is the positive root of its actual implicit complex-frequency equation. The displayed contour is the specified second-frequency-zero slice of a two-dimensional contour. The distributional arrows show the signed coefficients of point masses.

The calculation program uses 65 decimal digits to evaluate actual logarithmic-cycle Gaussian inverses for a point mass and its first two derivatives, finite unregularized contour integrals, strip and Jacobian bounds, complex Gaussian moduli, bounded-displacement widths, and physical triangular-function Fourier integrals. Values too large for a machine float are retained in decimal scientific notation. These checks supplement the full all-dimensional proofs in the lesson.

The complete proof contains the logarithmic-strip criterion with a fixed growth order, Gaussian contour deformation and uniform removal of regularization, the hull theorem through all logarithmic profiles, and compact singular-hull preservation under any nonzero polynomial differential operator. Four worked examples and ten complete solutions accompany it.
