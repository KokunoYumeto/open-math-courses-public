# Rational top forms: reproducible illustrations

The formal exposition supplies the complete argument. The learner chapter has four worked examples and eight exercises with full solutions, totaling 100 points.

Run the included Python source with Python 3, NumPy, mpmath and Matplotlib:

    python -B -X utf8 rational-top-forms-check-and-figures.py

It regenerates both PNG/SVG figures and the exact geometry data. The graph drawing shows two coordinate projections of the oriented cycle in zw=1, rather than a spatial rendering of all four ambient coordinates. The Morse drawing shows radial height profiles in the chart z=r exp(i theta); the shaded band is the exact range over theta. The critical points are defined by their quartic equations, and the decimal labels are numerical samples.

The finite consistency checks supplement the full proof. They check exact exterior-algebra anticommutators, diagonal and Hermitian curvature spectra, positive homogeneous degrees, Morse roots and indices, Laurent periods, repeated denominators and Taylor remainders. They do not establish a general theorem by numerical testing.

Original exposition, code and diagrams: CC0 1.0. The font retains its own license. Historical references are linked, with their original rights retained.
