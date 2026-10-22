# Reproduce the joint convolution-carrier lesson

The formal source proves both directions of the full joint-family identity for compact convolution. It includes proper local integral limits, collapsed coordinates, the exact Fourier normalization, indicator addition and empty Minkowski sums. The learner source has four worked examples and ten fully solved exercises totaling 100 points.

Run the original illustrations and direct numerical probes with Python:

    python -B -X utf8 make_figures195.py
    python -B -X utf8 check_numerics195.py

The figures require NumPy, Matplotlib and mpmath. The probes require NumPy and mpmath. The program integrates a physical trapezoidal convolution, computes signed atomic convolutions independently of their Fourier products, compares nested distributional derivatives, tests exact proper-profile bounds, and checks the smooth two-dimensional convolution with independent quadrature.

The numerical program reports finite checks of compactness and indicator identities. The general statements are established by the mathematical proofs.

The figure geometry is in figures/geometry195.json. Signed masses, support intervals, the smooth probability density and the three shared-frequency rays are specified there. The crossed-factor diagram shows actual ordinary and singular supports. It does not classify every individual proper profile carrier. PNG and SVG pairs are supplied.

Original exposition, solutions, scripts and artwork use CC0 1.0. DejaVu retains its separate font terms. Human scholarly references retain their own rights.
