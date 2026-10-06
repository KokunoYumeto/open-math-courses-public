# Reproducing the physical plaque diagram

Run `python draw_physical_plaque.py`. It writes `../../figures/plaque-physical-two-realizations.png` and the matching SVG. The SVG stores font outlines; the PNG stores rendered pixels. Use `--output DIRECTORY` to choose another destination. The reference package versions are in requirements.txt.

The recorded rendering used Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. The two bundled unmodified DejaVu fonts are explicitly selected by filename. The generator records the exact constants and defines the schematic support profiles. The diagram does not compute operator spectra. Panel C displays the proved bounds for the illustrative constant product one; the proof permits any positive finite constant product.

Original diagram geometry, generator code, mathematical proof and exercise expression are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). That dedication does not change the component terms below.

The unmodified `fonts/DejaVuSans.ttf` and `fonts/DejaVuSans-Bold.ttf`, and their glyph outlines embedded in the SVG, retain the complete Bitstream Vera/DejaVu terms in `fonts/LICENSE_DEJAVU.txt`. Preserve that notice with the figure and reproduction files. The font names have not been changed and no glyphs have been modified.

Matplotlib, NumPy and Pillow are rendering dependencies, not relicensed components of the original proof. Their complete software notices are retained as `MATPLOTLIB-LICENSE.txt`, `NUMPY-LICENSE.txt` and `PILLOW-LICENSE.txt`. The bundled fonts and these notices suffice for this figure's scoped component attribution; no STIX font or font notice is used by this generator.
