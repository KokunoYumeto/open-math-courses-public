# Normalized coefficient weights: figure terms and reproduction

The diagram, exact mathematical data, drawing code and generated PNG/SVG are original contributions dedicated to **CC0-1.0**, to the extent of rights held. No image, page rendering or graphic from a publication is included.

The mathematical model is [Normalized weights in a discrete coefficient algebra, Section 8](../../OA-FLOW-NCOEF.html#nc-models), equations NC54–NC58. The proof mechanisms are the [right-sided density identity](../../OA-FLOW-NCOEF.html#nc-density-cocycle), NC9; [normalized Fourier rigidity](../../OA-FLOW-NCOEF.html#nc-rigidity), NC20–NC27; the [complete centralizer and compression formulas](../../OA-FLOW-NCOEF.html#nc-centralizer), NC28–NC30; and the [infinite-multiplicity seed](../../OA-FLOW-NCOEF.html#nc-seed), NC44–NC50. Historical mathematical antecedents are M. Takesaki, *Theory of Operator Algebras II*, XII.4.10–4.11 and XII.4.13–4.14, printed pp.410–414. The alternating density and all plotted coordinates are the independent example proved in the lesson.

Panel A shows the exact integer shift and its phase: the arrow from delta_j to delta_(j-1) carries rho(j)^(it). Panel B shows half-open central bands [rho_n(j),rho_(n-1)(j)) on a logarithmic density axis; the filled and empty markers show the closed lower and open upper endpoint of the normalized band. Panel C samples the exact discrete density at the displayed integers, with straight segments only as visual guides; the value 1 is a limit, not an eigenvalue. Panel D displays four coordinates of an infinite multiplicity fiber and its actual rank-one compression. It is not a claim that a finite four-dimensional centralizer is properly infinite.

## Files

- `render.py`: reproducible drawing source and exact rational identity checks.
- `data.json`: exact rational weights, densities and band endpoints, model definitions, proof locators and external font hashes.
- `normalized-coefficients.svg`: vector rendering, with glyphs rendered as paths.
- `normalized-coefficients.png`: raster rendering, 2112 by 1664 pixels.
- `TERMS.md`: these terms and reproduction instructions.

## External fonts

The renderer reads **DejaVu Sans** and **DejaVu Sans Bold** from the existing sibling `typeiii-zero-decomposition` asset directory. Their files are not duplicated in this figure directory. Both original font components retain their terms, reproduced in the existing [FONT-LICENSE.txt](../typeiii-zero-decomposition/FONT-LICENSE.txt). The CC0 dedication above does not replace those font terms. SVG glyph outlines remain subject to the applicable font terms. `data.json` identifies both font files by SHA-256.

## Reproduction

Use Python with Matplotlib and NumPy. From this directory run:

```text
python render.py --font-dir ../typeiii-zero-decomposition
```

The required font-directory argument can instead be an explicit path to the same two existing font files. The renderer verifies the cocycle and right-sided phase identities using rational arithmetic before plotting. It writes the three outputs beside itself, uses a fixed SVG hash salt, and omits variable date metadata. The PNG and SVG are two formats of the same exact model.
