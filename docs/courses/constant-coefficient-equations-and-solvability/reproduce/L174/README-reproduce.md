# Reproducing the illustrations and supplementary checks

The formal and learner chapters contain the full arguments. These programs reproduce two original mathematical illustrations and supplement the examples with exact and numerical checks.

With Python, Matplotlib, NumPy and mpmath installed, run:

    python -B -X utf8 make_figures237.py
    python -B -X utf8 check_numerics237.py

The figure program writes two PNG/SVG pairs and a coordinate-and-formula description. The first plots exact base-two logarithms of large point masses, shrinking smoothing radii and their summable test-error products. The second plots exact isolated singular-point coordinates and the derivative orders of a datum and its primitive. Neither draws a fictitious height for a Dirac distribution. Both use six indicated samples; the chapters prove the full infinite-series statements.

The check program uses exact fractions for support margins, geometric sums, jet scaling, tail bands, receiver distances and sequence norms. It uses 65-digit arithmetic for the actual normalized smooth bump's moments and mollifier errors, complex bilinear transposes, distributional primitives and componentwise smooth correction. The private local report is a supplementary check log, not part of the reading edition or a substitute for proofs.

Original chapters, programs and illustrations are public domain under CC0. The DejaVu font retains its separate licence. SVG text is editable. The temporary private Matplotlib configuration is removed when the figure program finishes.
