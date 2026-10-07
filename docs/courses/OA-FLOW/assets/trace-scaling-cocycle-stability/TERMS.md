# Terms and reproducibility

The original exposition, exact data, renderer, and diagrams in this directory are offered under CC0-1.0 to the extent of rights held. No figure, scan, or source-page image has been copied from a book or article. Mathematical source context and exact proof locators are recorded in the lesson caption and `data.json`.

The diagrams are generated from exact formulas by `render.py`, with NumPy and Matplotlib. Run `python render.py` from any directory; the script reads its neighboring `data.json` and writes `cst-models.png` and `cst-models.svg` next to itself. It requires no network access and no external visual assets. Its printed checks verify the plotted matrix products, sample cocycle identities, linking orientation, and trace areas. The complete mathematical proofs remain in the lesson.

Panel A uses the exact shift `log(2)` and exact exponential curves; the displayed domain is `[-1.08, 1.24]`. Panel B records exact integer imaginary coefficients, with zero real part. Panel C rounds matrix entries to three decimal places for display; exact formulas and factor orders are retained in `data.json`. Panel D displays only indices 1 through 4 of a countably infinite product and explicitly shows the omitted continuation. None of these finite pictures asserts a finite-dimensional reduction of the general theorem.

The SVG embeds glyph outlines from Matplotlib's bundled DejaVu fonts. Those font components retain the separate license in `FONT-LICENSE.txt`; the CC0 statement does not replace it. The PNG is 2560 by 2048 pixels. The renderer uses a fixed SVG hash salt and omits the SVG date field to support reproducible output with the same dependency versions. Numerical matrix checks are diagnostics, not substitutes for the exact proofs.

Reference rendering environment: Python 3, NumPy 2.4.4, Matplotlib 3.10.9. No account name or local filesystem identity is included in image metadata or visual credits.
