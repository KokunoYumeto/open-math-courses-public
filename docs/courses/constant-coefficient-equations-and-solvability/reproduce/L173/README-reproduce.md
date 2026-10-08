# Reproducing the illustrations and supplementary checks

The formal and learner chapters contain the full proofs. These programs reproduce two original geometric illustrations and supplement the examples with exact arithmetic and numerical checks.

With Python, Matplotlib, NumPy and mpmath installed, run:

    python -B -X utf8 make_figures234.py
    python -B -X utf8 check_numerics234.py

The figure program writes two PNG/SVG pairs and a coordinate-and-formula description. The first shows the actual vertical singular hull, an established point carrier, the two open rectangular domains and a sampled escaping singularity sequence. It does not claim that the combined singular hull is itself a profile carrier or enumerate all the kernel's profiles. Dashed rectangle boundaries are excluded. The second draws the exact convex graph of absolute value plus a square and four regular tangents. The chapters prove that all regular tangents, not only those drawn, pass strictly below the excluded corner.

The check program uses exact fractions for containment, boundary margins, reflected support values, escaping-point coordinates, tangent gaps, subgradients and halfspace thresholds. It also uses 65-digit arithmetic for normal vectors, complex bilinear transposes, normalization of the positive bump and sampled real Fourier bounds. Its local report is a supplementary check log, not part of the reading edition or a substitute for the full proofs.

Original chapters, programs and illustrations are public domain under CC0. The DejaVu font retains its separate licence. SVG text remains editable. The figure program removes its private temporary Matplotlib configuration on completion.
