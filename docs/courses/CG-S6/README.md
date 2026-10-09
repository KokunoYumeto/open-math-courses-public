# Complex threefolds from marked torus families

This course develops the complex-geometry S6 construction through its original marked periods, finite fillings, cusp, integral topology, canonical sections and deformation. It preserves the mathematical contributions of the manuscript produced with Claude under Levent Alpöge's direction, Philip Engel's subsequent treatment, and the programme's retained exact calculations.

Start with [lesson 1: Two finite torus quotients and their line bundles](CG-S6-01.html). It proves the explicit product-cover degrees nine and eight, the complete finite group actions, and the smooth trivializations of line bundles of exact holomorphic orders three and four. Its [editable source](src/finite-quotients-and-line-bundles.md) contains every proof and four solved exercises. Continue with [lesson 2: Normal boundaries and their integral maps](CG-S6-02.html), which computes the entire attachment kernel, the explicit group product isomorphism and the integral cohomology covering maps. Its [editable source](src/normal-boundaries-and-integral-maps.md) contains the full proofs and three solved exercises.

Continue with [lesson 3: Varying finite fillings and every base-change branch](CG-S6-03.html). Its [editable source](src/varying-finite-fillings.md) constructs all local period germs with the original transformation laws, proves their exact real-analytic comparison with the normal bundles, computes every normalization branch, and gives the full punctured holomorphic conjugacy. Three further exercises have complete solutions.

The [series map](series.json) retains the full remaining assignment. The three finite-local lessons are available; the global period family, cusp, compact gluing and sphere recognition remain course work. Source reading and proof acceptance have separate records.

- [Course and result metadata](course.json)
- Finite-quotient calculations
- Normal-boundary calculations
- Varying-period and branch calculations
- Source identities and attribution
- Complete current source and offline reader

New mathematical exposition and diagrams are dedicated under CC0-1.0. Bundled rendering software and fonts retain their own notices in `assets/mathjax/`. Current authoring provenance: GPT-6 Astra (OpenAI), Codex, Ultra, 8 October 2026. Independent review is not claimed.

Run `python rebuild_course.py` with SymPy installed and Pandoc on PATH to reproduce all three exact checkers, regenerate the readers and rebuild the complete offline download. For individual operations, run the checkers above or `python rebuild_reader.py`. Each SVG figure is its editable source. Open `index.html` in the extracted archive to read offline; all equation-rendering assets and fonts are included.
