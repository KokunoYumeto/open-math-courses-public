# Figure terms and reproduction

The original drawing, mathematical coordinate data and `render.py` are dedicated to the public domain under CC0-1.0. The figure illustrates the exact pair choice, frequency addition and original-center obstruction proved in OA-FLOW-DS, Sections 3, 6 and 8, equations DSEL12–DSEL16, DSM7–DSM11 and DSM16–DSM17. No image or diagram is reproduced from another publication.

Mathematical background: M. Takesaki, *Theory of Operator Algebras II*, Theorem XII.4.18, Lemma XII.4.19 and Definition XII.4.20, printed pp. 417–418. The explicit coordinate and support models are given with complete proofs in the present lesson.

Run `python render.py` with Python 3, NumPy and Matplotlib. The script reads the exact rational constants in `data.json`, verifies the pair and power identities with rational arithmetic, and produces `ds-models.svg` and `ds-models.png`. The plot joins the exact piecewise-linear graphs; it is not a numerical approximation to an unknown object. The shaded cells represent the support in each original central summand, not finite-dimensional matrix sizes, dimensions, trace values or metric areas.

DejaVu Sans and its mathematical glyphs are supplied by Matplotlib. The SVG retains glyph outlines and the PNG retains their rasterization. Font components are not covered by the CC0 dedication: their complete retained terms are in `FONT-LICENSE.txt`, copied without alteration from Matplotlib's `LICENSE_DEJAVU`. No font files are modified or redistributed separately. Matplotlib and NumPy retain their own licenses; they are dependencies rather than bundled components.
