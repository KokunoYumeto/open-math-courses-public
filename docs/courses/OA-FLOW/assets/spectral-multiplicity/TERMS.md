# Terms and reproduction

The original lesson, mathematical models, figure data, renderer and resulting SVG/PNG figures in this directory are dedicated to CC0-1.0. No figure reproduces or edits a source-page image.

Run the renderer with normal Python:

    python render.py --font-dir PATH/TO/OA-FLOW/assets/typeiii-zero-decomposition

The renderer reads the existing DejaVuSans.ttf and DejaVuSans-Bold.ttf in that public asset directory. Their existing FONT-LICENSE.txt governs those fonts. No font or font-license copy is supplied here. The SVG uses glyph outlines from those fonts; the PNG is the rendered figure. DejaVu/Bitstream font terms remain applicable as stated in that existing license; the CC0 dedication does not relicense the fonts.

Python, Matplotlib and their dependencies retain their own licenses. The figures were verified with Python 3.13.9, Matplotlib 3.10.9, NumPy 2.4.4 and Pillow 12.2.0. There are no network inputs.

data.json specifies every measure, multiplicity, coordinate map and scalar graph. The Cantor bands are the exact fifth-stage support cover, not a density. The point-projection graph contains an isolated value at zero and is not joined to the zero-valued rest of the graph. The other graph is the exact overlap-length formula on the Lebesgue sector. Captions and proof locators appear in ../../src/OA-FLOW-SMULT.md, Section 9.

render.py writes only figures/measure-multiplicity.svg, figures/measure-multiplicity.png, figures/carrier-scaling.svg and figures/carrier-scaling.png beside the supplied inputs. A fixed SVG hash salt and omitted timestamp make repeated rendering deterministic in the recorded environment.

