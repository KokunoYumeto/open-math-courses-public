# Reproducing the convolution regularity examples

The two chapters give the full mathematical arguments, four worked examples and ten fully solved exercises. The diagrams show exact transform zeros, specified logarithmic windows, one exact elliptic zero branch, affine profiles and reflected singular sets. The captions distinguish samples, exact limiting profiles and proved statements.

Run the supplementary checks with Python and mpmath:

    python -B check_numerics243.py

The script uses 65 decimal digits and exact rational cancellation. It compares independent Fourier integrals, tests the distributional cutoff identity, and checks the complex contour determinant and harmonic kernel normalization. The 1,250 finite checks supplement the proofs.

Recreate the PNG and SVG figures with Python, NumPy and Matplotlib:

    python -B make_figures243.py

The script retains the exact diagram geometry in figures/geometry243.json. Its temporary font cache is removed automatically. The SVG metadata has no changing date.

The original chapters, examples, solutions, scripts and diagrams are dedicated to the public domain under CC0 1.0. The DejaVu font keeps the terms reproduced in DejaVu-font-license.txt. References are credited in the chapters; no source-book text or figures are reproduced.
