# Reproducing the partition-of-unity illustration

Run `python draw_partition.py`. It writes the PNG, SVG and numerical-component record to `../../figures`. `--output DIRECTORY` chooses a different output directory. No mathematical source pixels, scans, or source extracts are included.

The rendering uses Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. Both unmodified bundled fonts are selected explicitly by filename; the component record lists the actual loaded font files. SVG glyphs are stored as outlines. The curves sample the exact quotient in Theorem 3.E using the constants in Figure 3.1; the generator documents the floating-point evaluation. The mathematical proof is in the lesson, not inferred from numerical sampling.

Original proof, exercise, figure geometry, caption and generator expression are dedicated under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The dedication preserves the following component terms.

The unmodified `fonts/DejaVuSans.ttf` and `fonts/DejaVuSans-Bold.ttf`, and their glyph outlines in the SVG, retain the complete Bitstream Vera/DejaVu terms in `fonts/LICENSE_DEJAVU.txt`. Retain that notice alongside the figure and reproduction files. No font glyph was modified.

Matplotlib, NumPy and Pillow are rendering dependencies. Their complete notices are retained as `MATPLOTLIB-LICENSE.txt`, `NUMPY-LICENSE.txt` and `PILLOW-LICENSE.txt`. They are not relicensed by the original-expression dedication. This generator uses no STIX fonts.
