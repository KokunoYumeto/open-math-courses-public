# Elliptic boundary reduction

The compact-cylinder calculation identifies exactly how a tangential measurement loses regularity, smooth-error solvability and closed range. The general lesson retains the full reference inverse and derives the comparison system for arbitrary boundary rows.

[Read the lesson](arbitrary-boundary-data-reduction.html) · [PDF](pdf/arbitrary-boundary-data-reduction.pdf) · [TeX](tex/arbitrary-boundary-data-reduction.tex) · [Credits and terms](credits.html)

The lesson's supporting arguments and reference routes belong to the same selected reading package.

Rebuild HTML with Python 3, Beautiful Soup and Pandoc:

```text
python build/build_reader.py
```

The `--pandoc` option accepts a specific executable path. The mathematical reader uses native MathML and contains its own CSS. No remote rendering service is required.

The existing TeX file uses the sibling figure directory. To build its PDF, start from `tex/` and compile `arbitrary-boundary-data-reduction.tex` with a standard LaTeX installation. Regenerate the PNG and SVG with Python and Matplotlib by running `figures/arbitrary_boundary_data_reduction.py`.

Read offline by serving this directory with a local HTTP server. Human source identities and use roles are in [sources.json](sources.json). The lesson and independent operator-flow figure are dedicated under CC0 1.0. Supporting inherited readings retain their own GFDL 1.2 only terms and notices.
