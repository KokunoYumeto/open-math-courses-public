# Hydrodynamics of the vacuum: gravity, thermodynamics and fluids

Two companion lessons develop exact mathematical connections between fluid data and vacuum gravity. The first constructs nonlinear gravitational initial data from a complete compactly supported incompressible velocity field and recovers the velocity with an explicit decoder. The second derives the linear gravitational shear response in a Rindler region, its Navier–Stokes limit, its positive wave energy, and the first nonlinear backreaction term.

Each lesson contains complete arguments, a reproducible diagram and five exercises with full solutions. The cosmological constant, physical units, coordinate maps, boundary conditions and domains of the two constructions are specified separately.

- [Read both lessons](reader.html).
- Download the reader, editable sources and figures for offline use.
- [Lesson V6a: Exact vacuum constraint data from a velocity field](velocity-fields-and-vacuum-constraints.html) · [editable source](src/velocity-fields-and-vacuum-constraints.md).
- [Lesson V6b: The gravitational shear response and its fluid limit](gravitational-shear-and-the-fluid-limit.html) · [editable source](src/gravitational-shear-and-the-fluid-limit.md).

The lessons supply the analysis and geometric calculations their proofs use. Familiarity with multivariable calculus, Fourier transforms and basic metric notation is helpful. The forced Navier–Stokes construction gives the related fluid theorem and its complete proof.

The first lesson proves an injective map into a space of marked gravitational constraint data. Its exact time-evolution residual specifies the limits of identifying the two evolutions. The second gives a linear shear-sector theorem with its full source response. These conclusions do not assert an Einstein regularization of the nonlinear Navier–Stokes blowup.

The mathematical sources include work by Choquet-Bruhat, Isenberg and Pollack; Bredberg, Keeler, Lysov and Strominger; Compère, McFadden, Skenderis and Taylor; and Marolf and Rangamani, together with the [vacuum-hydrodynamics workbench manuscripts](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/0a320572884e6f6aaac0e6652fa45ce75ceaaec4/navier-stokes/continuations/20260919-vacuum-hydrodynamics/manuscripts). Each lesson cites its precise source passages. Lessons and diagrams written with GPT-6 Astra.

To rebuild the HTML readers from the Markdown sources, install Python and `markdown-it-py`, then run `python build.py` in this folder. Mathematical rendering works offline with the included MathJax runtime and its licence notices. The figure scripts require Matplotlib. External scholarly references remain online links.
