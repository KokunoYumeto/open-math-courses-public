# Reproducing the illustrations and supplementary checks

The formal and learner chapters contain the full arguments. The programs reproduce two original mathematical illustrations and supplement the examples with exact and numerical checks.

With Python, Matplotlib, NumPy and mpmath installed, run:

    python -B -X utf8 make_figures240.py
    python -B -X utf8 check_numerics240.py

The figure program writes two PNG/SVG pairs and a coordinate-and-formula description. The first draws exact formulas for imaginary-axis logarithms of a sine transform at three real zeros, together with the proved canonical limit. The value at the omitted origin is minus infinity for each finite center; the limit includes its actual value zero. The second draws finite stages of explicit locally Lipschitz weights and the common derivative index. These weights illustrate local stabilization and are not asserted to solve unspecified forcing.

The check program uses exact fractions for two sparse convolution inverses and the stabilized weight recurrence. It uses 65-digit arithmetic for the complex sine identity, canonical-profile error bound, disk average, actual smooth probability bump and shifted complex distributional transpose. Its local report is supplementary evidence, rather than a replacement for the proofs.

Original chapters, programs and illustrations are public domain under CC0. The DejaVu font retains its separate licence. SVG paths preserve the rendered labels, and the complete figure program and formula description provide editable sources. The temporary private Matplotlib configuration is removed when the figure program finishes.
