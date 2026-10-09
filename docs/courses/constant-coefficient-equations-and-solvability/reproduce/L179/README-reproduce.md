# Radial boundary kernels and regularity of convolution

The two Markdown chapters contain the complete proofs in every dimension, four worked examples and eight exercises with full solutions totaling 100 points.

Run python -B make_figures252.py to regenerate the two PNG/SVG pairs and figures/geometry252.json. This needs Matplotlib, NumPy and mpmath. The temporary Matplotlib configuration is removed on exit.

Run python -B check_numerics252.py, python -B check_figures252.py and python -B check_learner252.py for supplementary comparisons. The mathematical checks use 90 decimal digits; the figures use 70 digits. The figure checker compares their samples with independently evaluated Gaussian integrals at 90 digits, using the stated 1e-40 figure tolerance. The full proofs remain in the chapters.

The two-dimensional Gaussian formula is derived in the proof. Hankel functions serve as an independent numerical comparison, rather than a missing proof dependency. The figure captions distinguish global model samples from the compact-transform theorem.

Original chapters, illustrations and programs are released under CC0 1.0. DejaVu font components retain the accompanying font licence. The preceding linked lesson supplies the exact one-dimensional Fourier calculation and full global-distribution regularity/parametrix criterion.
