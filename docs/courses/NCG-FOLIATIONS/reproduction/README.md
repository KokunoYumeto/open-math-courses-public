# Reproducing the Section 11B figures

The three scripts independently draw the mathematical objects, exact formulas and typed proof maps in Section 11B. They incorporate no image of a human source page. Their text and original diagrams are dedicated to CC0 1.0. The DejaVu fonts in `fonts/` have their separate licence in [LICENSE_DEJAVU.txt](fonts/LICENSE_DEJAVU.txt); retain that file with the fonts.

Preserve this layout, with the scripts in `reproduction/` and a sibling `figures/` directory. Python 3, Pillow, NumPy and Matplotlib are required. The scripts use the supplied font files directly, without installing fonts or depending on a machine font path. Create the sibling output directory if it is absent, then run:

```text
python reproduction/render_witten_product.py
python reproduction/render_restriction_projector.py
python reproduction/render_boundary_factorization.py
```

Each script writes a PNG and an SVG with the corresponding `kt-hyperbolic-…` filename. Preserve the original supplied PNGs for the reader: their exact bytes were inspected. Library versions, SVG identifiers and SVG creation metadata can affect newly reproduced byte hashes; the formulas, coordinate layout and proof mechanisms are determined by the scripts. The two editable text diagrams embed the exact bundled condensed regular/bold fonts and their complete licence in the SVG itself. The Matplotlib SVG retains its generated vector paths. The accompanying fonts and licence remain part of the reproduction bundle.

The Witten plot samples the explicit functions `(1+r²)^(-3/2)` and `r coth(r)/sqrt(1+r²)`, with their smooth value 1 at the origin. The analytical bounds and whole compact-subgroup product are proved in WP.20–WP.42. Samples do not prove the bounds. The projector and boundary diagrams give the complete module types and constructions at RP.0–RP.8, CL.1–CL.28, HF.1–HF.7, RR.2–RR.3 and RR.6–RR.8. The rejected bounded local formula in the projector's first panel is supported by the adjacent high-frequency counterexample and is excluded from the accepted induction argument.


The fixed-chart Dirichlet-input figure has its own complete [reproduction instructions](plaque-dirichlet-README.md) and [font notice](FONT-NOTICE.txt). Its standalone source is `draw_plaque_dirichlet_input.py`; retain the same reproduction/figures directory layout.
