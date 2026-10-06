# Reproduce the full-isotropy diagram

Use Python with the dependencies in requirements.txt. From this component's directory in the course, run `python draw_isotropy.py --output-dir ../../figures`. For a standalone copy, choose any output directory with `--output-dir`. The script loads only the bundled unmodified DejaVu Sans typeface and writes the PNG and SVG there. The SVG contains the full font notice. The four panels show three proper infinite-group functors and the infinite-kernel failure; the displayed integers are only a window in the full action space.

The proofs are Theorem 5.26 and Propositions 5.27–5.28 of the transverse-measure lesson. All constants, cutoff values, multiplicities and image factors in the diagram are exact.
