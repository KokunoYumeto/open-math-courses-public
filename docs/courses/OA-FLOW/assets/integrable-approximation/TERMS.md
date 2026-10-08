# Terms and reproducibility

The original drawing script, illustration, mathematical model data and explanatory text in this directory are dedicated to CC0-1.0 to the extent of rights held. They were independently produced for this lesson. No source-publication illustration, page, extraction, screenshot or font file is included.

Run `python generate_model.py` in this directory to regenerate the SVG, PNG and JSON. The script requires NumPy and Matplotlib and reads an existing installed DejaVu Sans font; its package-relative reference and SHA256 are recorded in `model-data.json`. It does not copy that font. SVG text refers to font families, with `svg.fonttype=none`; the raster output contains the rendered drawing. Installed fonts and plotting software retain their own licenses.

The four panels illustrate the exact objects and constants proved in ../../src/OA-FLOW-IAP.md, equations (IA13)–(IA18) and (IA24). Numerical curve samples are rendering data, not substitutes for those proofs. The first six matrix coordinates are explicitly schematic; the actual factor is infinite-dimensional. No type III factor is claimed to be constructed by the diagram.

Human-source context: M. Takesaki, *Theory of Operator Algebras II*, XII.5.9–5.11, printed pp.426–427. The drawing and its arrangement are original and contain no source assets.
