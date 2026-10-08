# Krieger-tower figure: terms and reproduction

The original renderer, model data, caption and generated SVG/PNG are dedicated under **CC0 1.0**, to the extent of rights held. The renderer uses the unchanged [DejaVu fonts](../typeiii-zero-decomposition/DejaVuSans.ttf) and [font license](../typeiii-zero-decomposition/FONT-LICENSE.txt) already included in this course. Their original terms remain in force.

Put b=(sqrt(5)-1)/2 and c=log(2). The torus point map is S_s(x,y)=(x+s/c,y+bs/c), while the center automorphism is theta_s(f)=f composed with S_{-s}. The curve samples normalized times from 0 to 11/2. The highlighted section has x=1/4, and the six marked heights are b(1/4+k) modulo 1 for k=0,...,5. The full section is countable, proving Haar-nullity of the full orbit by Fubini. The other panel plots exactly A_{[-R,R]}(1)=(R/pi)1, with paired Haar measures dt and dp/(2pi). See [KT23–26](../../src/OA-FLOW-KRT.md#kt-5) and the [exact immediate-stop model](../../src/OA-FLOW-KRT.md#kt-7). No general existence of prescribed stopping indices is inferred from the diagram.

Run `python render.py` with Python 3, NumPy and Matplotlib from this asset directory. Its default fonts are in the adjacent typeiii-zero-decomposition directory. For a separate copy, use `python render.py --font-dir PATH` with those two fonts. The renderer reads data.json and the fonts, then writes krieger-tower.svg and krieger-tower.png. The inspected outputs used Matplotlib 3.10.9 and NumPy 2.4.4. SVG identifiers are fixed and date metadata is omitted.

M. Takesaki, *Theory of Operator Algebras II*, Exercise XII.3.2, printed pp. 402–403, supplies the recursive-tower question. This diagram was constructed from the accompanying proof's explicit formulas and does not reproduce a source illustration.
