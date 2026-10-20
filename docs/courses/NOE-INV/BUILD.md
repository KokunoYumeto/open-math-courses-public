# Invariants and finiteness: editable sources

The five Markdown files in src/ contain the native lesson text. The matching LaTeX files contain the same mathematical exposition, proofs, exercises and solutions. Figures are supplied as PNG and editable SVG, with Python drawing sources. Historical German facsimiles and English PDF readings are in historical/noether/.

Convert a lesson with Pandoc: pandoc src/NOE-INV-01.md -f markdown+tex_math_single_backslash -t latex -s -o NOE-INV-01.tex. From this folder, a suitable LaTeX engine can compile that export. The HTML readers use MathJax from jsDelivr; an internet connection is needed to typeset formulas in the browser.

The exact calculations require Python, SymPy and python-flint. verify_quartic_certificate.py checks the parameter calculations of the fourth lesson, Section5; verify_quartic_generators.py checks the all-degree Hilbert identity and the secondary-monomial certificate of Section6. The two certificate directories contain the exact data. The smaller check programs reproduce the cubic, Hesse-group and Schmid calculations. These computations accompany the written mathematical proofs.

Original modern mathematical content and calculation programs are CC0. Noether’s original papers are public domain; the English translation layer is CC0, from the maintained edition at https://doi.org/10.5281/zenodo.21923146 . Historical PDFs may contain fonts under their own terms. Linked research sources and the external MathJax runtime retain their own terms.
