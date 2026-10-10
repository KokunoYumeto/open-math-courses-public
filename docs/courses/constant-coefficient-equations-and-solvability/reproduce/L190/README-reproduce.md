# Reproduce the derivative-class checks and figures

Run with Python, mpmath, NumPy and Matplotlib:

    python -B -X utf8 class-check-and-figures.py

Exact checks retain fixed-index-shift exponents, full class bounds and covector signs. Independent 90-digit integrals compare the positive spectral moments with exact factorials, the rotated boundary contour with a completed-square Gaussian expression, and the original Gaussian packet with its rationalized scaled form. The complete normalization of the limiting Gaussian integral, complex Euler derivative and proper kernel polynomial input are checked as well. Every comparison records its tolerance. Finite samples supplement the full all-index proofs and all eight complete solutions.

The two editable scientific PNG/SVG figures show exact angular class covectors and the derivative moments beside the proved positive packet rate. Geometry JSON records the complete class ranges, exact points, covectors, display scale, integer derivative orders and 90-digit scaled packet values. SVG dates are omitted and hash salt is fixed.

The sequence is increasing, L0=1, k<=Lk and L(k+1)<=C*Lk. It is a derivative sequence, not a Sobolev index. The class localization is fixed before estimating its Fourier transform. Ordinary normal continuity, hypocontinuity and uniform class estimates are distinguished; smooth convergence alone can lose Gevrey absence. Both origins remain excluded from homogeneous interchange, with full point and polynomial anomaly identities retained. Original content is CC0; all linked proofs, references and fonts retain their actual terms.
