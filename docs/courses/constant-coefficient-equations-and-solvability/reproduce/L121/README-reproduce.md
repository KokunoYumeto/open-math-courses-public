# Reproduce the rational-period diagrams

Keep make_figures.py beside an empty figures directory, or let the program create it. With Python, NumPy and Matplotlib available, run:

    python make_figures.py

The program writes three PNG diagrams, the corresponding SVG files, and geometry.json. To replay into a separate directory, use:

    python make_figures.py --output-dir replay

The source contains no machine-specific paths and imports no image media. It fixes the SVG identifier salt and omits SVG dates. A fresh replay in the observed Python/NumPy/Matplotlib environment matched all seven delivered outputs byte for byte and all decoded PNG RGBA pixels. Other library or font versions can change rendering bytes; geometry.json records the mathematical data independently.

The cover diagram shows an exact slice of the explicitly defined slit-plane cover. The phase diagram is an unwrapped coordinate map modulo \(2\pi\), with the normal circle first. The matrix diagram shows exact normalized periods and the actual primitive tube vector for the stated two-dimensional example. Full captions and proof locators are in projective-rational-periods-learner.md. Every figure is an original diagram for this candidate; free human mathematical-method credits are retained in the learner's bibliography.
