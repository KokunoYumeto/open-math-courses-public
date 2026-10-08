# Terms and reproducibility

The original diagram, exact data, and renderer are offered under CC0-1.0 to the extent of rights held. No book figure, source-page image, or existing course illustration was copied. Human-source context and exact proof locators are recorded in the lesson caption and `data.json`.

Run `python render.py` with Python 3, NumPy and Matplotlib. The script reads its neighboring `data.json` and writes `oes-models.png` and `oes-models.svg` in the same directory. No network access or external image asset is required. The reference rendering uses NumPy 2.4.4 and Matplotlib 3.10.9. The PNG is 2560 by 2048 pixels. A fixed SVG hash salt and omitted date field make both outputs reproducible with the same dependency versions.

The normalization path and weight bars are exact calculations in the fully proved infinite-multiplicity translation model. The phase plot displays the real phases before exponentiation on `[-pi, pi]`; it does not identify a real line with the unit circle. Its marked values at `s=pi/2` are the complex scalars `i`, `-i`, and `1`. The quotient diagram is explicitly conditional on a given properly infinite trace-scaling factor coefficient system. Diagram positions are not metric data. Its conclusion concerns the failure of a specified representative-lift prescription, not nonsplitting of all extensions.

The SVG embeds outlines from Matplotlib's bundled DejaVu fonts. Those components retain the separate terms in `FONT-LICENSE.txt`; CC0 does not replace their license. No account name or local filesystem identity is included in image metadata or visual credits. The complete mathematical arguments accompany the figure in the lesson; numerical renderer checks are implementation checks rather than theorem proofs.
