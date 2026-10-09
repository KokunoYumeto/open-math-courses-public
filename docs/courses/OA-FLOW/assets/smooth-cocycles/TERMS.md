# Smooth-cocycle figure: terms and reproduction

The original renderer, model data, caption and generated SVG/PNG are dedicated under **CC0 1.0**, to the extent of rights held. The renderer uses the unchanged DejaVu fonts and font license already included in this course. Their original terms remain in force.

The three roof lengths are 5/4, 1 and 3/2, with phase increments pi/4, pi/2 and -pi/3. The phase starts at -pi/4 on the preceding roof and is zero at the middle roof's lower endpoint. The graphs sample the exact flat interpolation in [SMC17–20](../../src/OA-FLOW-SMC.md#smc-4). The shaded intervals are constant neighborhoods. The derivative bounds are proved symbolic bounds, not numerical maxima inferred from the plot. Signed products are [SMC15](../../src/OA-FLOW-SMC.md#smc-3), and the norm remainder is SMC23–25.

Run `python render.py` with Python 3, NumPy and Matplotlib from this course directory. The default font path is the adjacent typeiii-zero-decomposition asset directory. For a separate copy, use `python render.py --font-dir PATH` with those two fonts. The script reads data.json and the fonts, then writes smooth-cocycles.svg and smooth-cocycles.png. The inspected outputs used Matplotlib 3.10.9 and NumPy 2.4.4. SVG identifiers are fixed and date metadata is omitted.

M. Takesaki, *Theory of Operator Algebras II*, Exercise XII.3.1, printed p. 402, supplies the smoothing question. This drawing was constructed directly from the accompanying proof's explicit formulas; it does not reproduce a source illustration.
