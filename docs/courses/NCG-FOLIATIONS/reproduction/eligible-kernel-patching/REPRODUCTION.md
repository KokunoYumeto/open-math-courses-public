# Reproduce the exact labelled-kernel diagram and finite checks

Run `python -B reproduce.py --output-dir out` in this directory. Compare the PNG/SVG with the lesson figures in `../../figures/` and the two JSON outputs with the copies in this directory. It writes
`finite-checks.json`, `eligible-kernel-patching-data.json`, and the PNG/SVG
diagram. `python reproduce.py --checks-only` runs the same finite algebra
checks using only the Python standard library. `--output-dir PATH` selects
another output directory. The public input besides the script is the
component notice in this directory; no proof files or private files are read.

The inspected rendering used Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4
and Pillow 12.2.0, pinned in requirements.txt. The script explicitly selects
Matplotlib's installed DejaVu Sans regular/bold files. SVG keeps its text as text and includes
the complete font notice in metadata; the PNG description includes it too.
No runtime or font binary is bundled. A fixed SVG salt and absent date metadata
make the outputs repeatable in this pinned environment.

Twenty finite checks verify rational feature Gram matrices, convex midpoint
coordinates, three zero-sum CND identities, invariant weighted Gram sums,
36 exact noncommutative free-word cancellations, the direction of right
cosets in S3, all 63 principal minors of its extended rational Gram matrix,
the normalization constants, lower-series bounds and finite probability
witness examples. Floating arithmetic is used only for the normalized sample
and 25 close-feature pairs; those checks are labelled accordingly.

The geometric panels are typed schematics. The normalized vectors have the
exact listed coordinates; their plotted positions are numerical samples.
Finite algebra does not establish the local Lie lemma, germ extension,
finite-label compactness, continuity of the infinite kernel, or compact-fibre
Haar properness. Those are the complete proofs EG.1–EG.9 and EK.1–EK.6,
with solved exercises EH.1–EH.4. The illustration identifies their objects,
maps and bounds without replacing the arguments.
