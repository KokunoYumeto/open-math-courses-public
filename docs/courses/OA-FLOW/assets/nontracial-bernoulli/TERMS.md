# Original figure and model terms

The three figures, their code, numerical models and explanatory captions were independently authored for this lesson. They are CC0-1.0 to the extent of rights held. The motivating mathematical source is M. Takesaki, *Theory of Operator Algebras III*, Exercise XVII.3.4, printed p.293; the source comparison and convention correction appear in the lesson's Section 12. No source-book image is reproduced.

Run `python render_and_check.py` from this asset directory to recreate the six PNG/SVG outputs and the model/check JSON files. The renderer uses installed NumPy and Matplotlib, with the installed DejaVu Sans font. Those dependencies retain their own licenses; no font file is bundled.

The site figure is a support schematic, with no metric or ordering assigned to the group. The lattice figure uses lambda = 1/2 only for numerical eigenvalue labels; the theorem ranges over 0 < lambda <= 1 and treats the scalar endpoint separately. The corner figure depicts supports and the factor-contact mechanism; it asserts no finite rank, equal dimensions or isometry. Finite model checks verify coordinate identities and a nonzero support composition. The complete infinite-dimensional and all-weight arguments are in the lesson.
