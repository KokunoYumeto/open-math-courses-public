# Reproduce the invariant-null-sector diagrams

Figures 5.21 and 5.22 accompany Sections 5.21.1–5.21.7, Theorems 5.21–5.24 and equations BP.1–BP.13 in *Transverse measures of foliations*. Exercises 16–19 include four complete solutions and 44 points.

Install the external versions in [requirements.txt](requirements.txt), then run from this directory:

    python draw_boundary.py

The portable generator uses only the two exact unmodified DejaVu fonts in fonts/, guards their hashes and records both actual loads. It writes ../../figures/borel-null-sector-composition.png, its SVG, ../../figures/borel-finite-radon-boundary.png, its SVG, and [figure-bindings.json](figure-bindings.json). Both SVGs contain glyph outlines and embed the complete [font notice](FONT-NOTICE.txt).

The first diagram shows two genuine globally nonproper weak leaf maps whose restrictions to the full conull good sectors are proper. The full image agrees on every countable target presentation: m finite labels give m, an empty presentation gives zero and infinitely many labels give infinity. Boxes specify sectors, not charts or a standard Borel model of the irrational quotient.

The second diagram shows the same compact disjoint union of foliated tori with finite transverse Radon measures. Adding any positive irrational-sector mass excludes the normalized-cutoff construction, even though the total variation distance is exactly epsilon. It displays a proved admissibility boundary, not a numerical output at an excluded parameter and not an impossibility theorem for all finite-Radon output rules.

Reference reproduction uses Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. The two isolated reference runs have identical figure bytes and mathematical reports in that environment. Another environment may produce different bytes. A Python runtime and external software are not included.

The independent proof and explanatory diagram expression are CC0 1.0. The exact fonts, glyphs and external software retain their own full terms in [COMPONENT-TERMS.md](COMPONENT-TERMS.md), [COMPONENTS.json](COMPONENTS.json), [FONT-NOTICE.txt](FONT-NOTICE.txt) and notices/. No source-paper image, transcription or expression is included. The historical Borel-map interface, holonomy isotropy and nontrivial modules remain outside this measure-dependent principal/module-one result.
