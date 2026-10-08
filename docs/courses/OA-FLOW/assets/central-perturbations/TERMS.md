# Original figure components and external font

The original diagram, renderer and rational model data in this directory are dedicated to CC0-1.0 to the extent of rights held. No source figure or source prose is reproduced.

The mathematical antecedent is Masamichi Takesaki, Theory of Operator Algebras II, XII.4.7–4.9, printed 407–410, DOI10.1007/978-3-662-10451-4. Exact proof locators in the independently written lesson are CPB4, CPB11, CPB13–15 and CPB31–32.

The renderer reads existing DejaVuSans.ttf and DejaVuSans-Bold.ttf from the public OA-FLOW assets/typeiii-zero-decomposition directory. Its existing FONT-LICENSE.txt remains authoritative for those fonts. Font and font-license files are not copied into this output. SVG uses outlined glyphs; no font file is embedded.

Run python render.py. In another checkout supply --font-dir PATH to the existing font directory; optionally use --output-dir PATH. The default uses the sibling assets/typeiii-zero-decomposition directory in this course checkout. Rational assertions check all 16 matrix-unit frequencies, both centralizers, the missing annulus and the perturbation sign before drawing. Neither shaded bands nor arrows represent numerically sampled spectra.

The image is an original finite-dimensional mechanism illustration, not a type III construction. The upper panel gives proved spectral containments. The lower panel gives exact model frequencies.
