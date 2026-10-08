# Reproduce the nonconvex logarithmic-carrier lesson

The formal source proves the closed-union singular-carrier theorem for compact distributions. Its partition is constructed from finite convolutions of interval probability densities and a smooth final factor. A directional finite Taylor identity supplies the contour correction with its exact sign. The low-frequency term, the empty-profile case, and changes of partition with the derivative budget are included.

The learner source contains four worked examples and ten fully solved graded exercises totaling 100 points. The disconnected two-segment example identifies its entire closed carrier union without claiming to classify every individual profile.

Run the original figure renderer and numerical probes with Python:

    python -B -X utf8 make_figures192.py
    python -B -X utf8 check_numerics192.py

The figures require NumPy and Matplotlib. The numerical probes require NumPy and mpmath. They cover 72 independent real/top/correction contour integrals, factorial integrals, explicit finite-convolution lattice cutoffs, derivative probes, exact support-function geometry and the stated derivative budget.

The contour probes use an auxiliary compact polynomial cutoff with sufficient finite smoothness. The actual smooth partition and its growing controlled derivative range are proved in the formal source. Numerical probes supplement the mathematical proofs; they do not certify the theorem or constitute independent mathematical review.

The figure geometry is recorded in figures/geometry192.json. The complex-cell drawing uses real and imaginary displacement coordinates in units of its stated cell length. The two plotted summation factors omit the shared unspecified estimate constant. PNG and SVG pairs are included.

Original prose, solutions, scripts and artwork use CC0 1.0. The DejaVu font keeps its separate terms. Human scholarly references retain their rights. Protected book pages, source text and images are not included.
