# Reproduce the labelled-kernel diagram

Section 11AC of *K-theory of the leaf space* proves the labelled source-pair kernel interface and its converse, compact-fibre spectrum, continuous affine Hilbert field, and actual discrete action cases. Exercises 183–190 have complete solutions (56 points). Section 11AF proves the general eligible-holonomy kernel in GK.9.

Use Python 3.13.9 and the versions in requirements.txt, with the included unchanged fonts and full notices. Run `python -B finite_checks.py` and `python -B draw_kernel.py`. The first command performs 30 exact finite checks and writes finite-checks.json. The second writes the PNG, SVG and sample data in figures/. It reads only the drawing script, finite checks, fonts and notice. The pinned runtime gives deterministic outputs.

The Fibonacci identity is checked exactly in Q[alpha], alpha²=1−alpha. Circle and chord values are declared numerical samples; the label kernel is exactly n². The lower panel is a typed schematic of the proved conditional construction. These computations supplement the complete argument and do not prove GK.9. Proof locators: GK.2, GK.4–GK.10.
