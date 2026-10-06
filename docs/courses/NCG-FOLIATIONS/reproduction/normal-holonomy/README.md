# Reproducing the affine oscillator and return-holonomy figure

Run `python draw_normal_holonomy.py` with Matplotlib installed. The generator writes the PNG and SVG to the course figures directory; `--output-dir DIRECTORY` chooses another destination. It explicitly selects the two bundled DejaVu fonts.

The square and edge directions show the exact Klein-bottle fundamental region. The Gaussian is the actual two-dimensional auxiliary kernel, sampled on a 101-by-101 grid in [-2.7, 2.7]^2. The return panel plots the exact values (3/2)^n and half those values on a logarithmic vertical scale. The complete proofs and limitations are in Section 11G and Exercises 125–127 of K-theory of the leaf space.

Original figure geometry, caption and generator expression are CC0 1.0. The unmodified fonts and their outlined SVG glyphs retain the full terms in FONT-NOTICE.txt. The complete software licence notices accompany this source. See COMPONENT-TERMS.md.
