# Compact multipliers and exponential solutions of convolution systems

The two Markdown chapters give the complete six-kernel counterexample in every dimension at least two, four worked examples and eight exercises with full solutions totaling 100 points. The compact-support Fourier theorem and weighted Cauchy–Riemann theorem are reused from the exact linked preceding lessons with their complete proofs.

Run python -B make_figure256.py to regenerate the PNG, SVG and figures/geometry256.json. This needs Matplotlib and mpmath. Its temporary Matplotlib configuration is removed on exit. The drawing shows every multiplier zero in its stated window and carrier inclusions, rather than unproved exact support equalities.

Run python -B check_multipliers256.py, python -B check_graph256.py and python -B check_learner256.py for 1442 supplementary comparisons at 90 decimal digits with tolerance 1e-65. These checks verify finite factor bounds, rigorous product-tail enclosures, sector signs, the all-type envelope, Levi eigenvalues and worked-example constants. They do not replace the complete proofs or numerically construct the weighted solutions.

Original text, programs and illustration are released under CC0 1.0. DejaVu font components retain the accompanying font licence. Credit for the counterexample, entire graph and six-generator idea belongs to D. I. Gurevich; all necessary arguments are supplied here or in the exact internal proofs.
