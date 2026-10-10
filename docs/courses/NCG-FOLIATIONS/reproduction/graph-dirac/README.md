# Reproduce the graph Dirac constraint diagram

Use Python 3.13 with the versions in [requirements.txt](requirements.txt), then run:

```console
python draw_graph_dirac.py
```

The complete generator uses the bundled exact DejaVu and STIX typefaces, creates `../../figures/kt-graph-dirac-constraints.png` and `.svg`, and writes [arithmetic-and-figure.json](arithmetic-and-figure.json). The SVG contains glyph outlines and the complete font notices. No external font service is needed. The reference run uses Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. Exact bytes are checked for two runs in that recorded environment; different renderer or dependency versions may produce different bytes without changing the formulas.

The 289 finite Pauli-matrix blocks check the illustrated squares and grading for -8 ≤ m,n ≤ 8. They support the diagram; Section 11C supplies the all-mode proof, the general coefficient argument, the exact domains, the scalar defects, the index-zero conclusion and the determinant-line obstruction. The diagram uses fixed formulas and schematics, with no spectral sampling or tree truncation as proof evidence.

Original programme text, source and diagram expression use CC0 1.0. The actual fonts and external numerical/rendering dependencies have separately scoped terms in COMPONENT-TERMS.md.
