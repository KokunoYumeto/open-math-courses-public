# Reproducing the illustrations and supplementary checks

The formal and learner chapters contain the full mathematical arguments. These programs reproduce the two original illustrations and supplement the examples with exact geometry and numerical checks.

With Python, Matplotlib, NumPy and mpmath installed, run:

    python -B -X utf8 make_figures231.py
    python -B -X utf8 check_numerics231.py

The figure program writes PNG/SVG pairs and a formula-and-coordinate description in the figures directory. The first figure is a support-set diagram: its vertical placement is schematic, while all horizontal intervals, point locations and open endpoints are exact. It does not graph the height of a Dirac distribution or of the smooth tail. The second plots exact samples of the singular-point and boundary-distance formulas; the infinite distribution and its extension obstruction are proved in the learner chapter.

The check program uses exact fractions for domain margins, translated supports, cutoff tails and scaled-jet powers, and 65-digit arithmetic for complex bilinear transposes and translated solutions. It writes a supplementary local report. That report is a check log, not part of the mathematical reading edition or a substitute for its proofs.

Original chapters, programs and illustrations are public domain under CC0. The DejaVu font retains its separate licence. SVG text is editable. The private temporary Matplotlib configuration is removed when the figure program finishes.
