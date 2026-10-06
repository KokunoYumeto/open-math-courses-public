# Reproduce the finite-chain Morse diagrams

The original portable source is make_figures.py. With Python, NumPy and Matplotlib available, run:

    python make_figures.py

It writes three PNGs, their three SVG counterparts and geometry.json in figures/. To keep a replay separate, use:

    python make_figures.py --output-dir replay

The program imports no image media or machine-specific paths. It fixes the SVG identifier salt, omits SVG dates and uses DejaVu Sans. The bundled DejaVu font notice is retained separately; independently authored text and diagrams are CC0-1.0. Different rendering-library or font versions can alter bytes, while geometry.json retains the exact mathematical data independently.

The first figure shows an explicitly rescaled local saddle chart, its lower lobes and exact stopped trajectory. It is not a global proper exhaustion. The second shows negative-disc **relative** pairs, including the disjoint basepoint required in index zero; it does not assert that every core is an absolute cycle. The third shows the actual cylinder function t²−cos θ, its identified parameter edges and actual sublevels. Its marked edge points are one saddle. The full learner captions contain proof locators and programme-method credits. The complete formal proof is retained verbatim in the learner and supplied as a separate source.
