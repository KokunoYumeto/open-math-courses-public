# Reproduce the Gaussian packet checks and figures

Run with Python, mpmath, NumPy and Matplotlib:

    python -B -X utf8 packet-check-and-figures.py

Exact rational checks retain the covector rotation and the entire finite nilpotent matrix inverse. Independent 90-digit Gaussian integrals verify the full Fourier phase and constants, point-jet transforms and both origin anomaly errors. Separate spatial and time integrals verify the inverse heat remainder; principal-value and half-line integrals independently verify the positive ray. Complex degrees, finite logarithmic chains and the full resonant Fourier constants are checked as well. Each numerical comparison records its tolerance, including the explicit Laurent truncation tolerance. Finite checks supplement the complete all-index proofs.

The two editable PNG/SVG diagrams show exact ray covectors and Gaussian widths with inverse heat multiplier defects. The geometry JSON records all coordinates, display scales, supports, singular supports, cutoffs of the plotting window and proof locators. SVG dates are omitted and the hash salt is fixed.

Both physical and Fourier origins are excluded in the interchange theorem. Point terms and Fourier polynomials are retained in the full identities. The packet regularity proof fixes each compact analytic localization before estimating its transform. Original content is CC0; linked proofs, references and fonts retain their actual terms.
