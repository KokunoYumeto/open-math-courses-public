# Component terms and reproduction

The original diagram, data and renderer in this directory are dedicated to CC0-1.0 to the extent of rights held. Mathematical antecedent: Takesaki, *Theory of Operator Algebras II*, XII.3.7(iii), printed pp.394–397. The figure is newly specified from the corrected proof in OA-FLOW-IC, IC7–12, IC41–46 and IC50–60; it reproduces no source page, source drawing or other image.

The six unmodified font files used by the rendered glyphs provide reproducible typography: DejaVuSans.ttf, DejaVuSans-Bold.ttf, DejaVuSans-Oblique.ttf, DejaVuSansDisplay.ttf, STIXNonUniIta.ttf and cmsy10.ttf. Complete DejaVu/Bitstream/Arev, STIX/SIL Open Font License and BaKoMa component notices are retained in FONT-LICENSE.txt. These fonts are not included in the CC0 dedication. DejaVuSans.ttf and DejaVuSans-Bold.ttf are reused from the adjacent typeiii-zero-decomposition asset directory; the remaining four files are included here. The renderer registers those exact local files. Matplotlib and FreeType version information is recorded below.

Run `python render.py` in a Python environment with Matplotlib. The renderer reads only local data and font files and writes induced-corners.svg and induced-corners.png. It uses no image editing, network request, PowerShell script, policy change or source-page image. PNG and SVG metadata are fixed or omit timestamps; the SVG identifier salt is fixed.

The exact integer-coordinate checks execute before drawing. Equal widths of the central bands encode no trace or probability. The orbit panels are finite windows, with no periodic closure. The commuting square is for the unsheared product map; the height-aligned map is used only to extract its action on constant coefficient fields. These qualifications are mathematical parts of the diagram.


Typography build details: Python 3.13.9, Matplotlib 3.10.9, FreeType 2.6.1.
