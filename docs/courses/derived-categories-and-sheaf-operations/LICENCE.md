# Sources and authorship

The thirteen main course readings are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

Many statements and proofs follow the Stacks project, whose authors are credited in each lesson. The lessons cite the AI Integrated Stacks Project edition at commit `565b10e987aba5969b21145a0833f42d69f96790`, with upstream Stacks commit `a04446e57ec1fbc252a871afcec7752fb2807b14`. The lesson texts are written independently; the Stacks project itself is distributed under the [GNU FDL 1.2](COPYING) or later. AI Integrated Stacks Project is an unofficial edition, not affiliated with, approved by or reviewed by the Stacks project's maintainers.

The edition records corrections by GPT-5.6 Sol (OpenAI), Ultra, integrated by GPT-6 Astra (OpenAI), Ultra, and additions principally by GPT-6 Astra, with some GPT-5.6 Sol contributions checked by GPT-6 Astra. The course's module-sheaf exposition includes Claude Opus 5.5 (Anthropic) contributions. Resolution and derived-functor proof contributions include GPT-6 Astra (OpenAI), Ultra. The model identity for one part of the K-flat construction is unverified. Course exposition, proof expansions and mathematical self-checking are by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Independent AI review, human review and formal verification are not claimed.

Independently authored programme explanations, examples, exercises and proofs dedicated under CC0 remain available under CC0 1.0. This includes the four prerequisite readings listed below.

## Mathematical sources and contributions

- **Sheaves of modules.** *Sheaves on Spaces* and *Sheaves of Modules* supply the sheaf and module constructions. The course develops germ-family sheafification, stalk bijections, associative-ring module structures and their full universal-property proofs.
- **Complexes and localization.** *Derived Categories* supplies cone and triangulation arguments; the course develops roofs, common refinements and localization checks. The diagram and elementary cohomology prerequisites are in Wen-Wei Li's *Methods of Algebra, Volume 2*, in the programme's English edition.
- **Injective and K-injective resolutions.** *Injectives*, *Derived Categories* and *Cohomology of Sheaves* supply the resolution methods. The course includes flasque-section arguments, large-cofinality and transfinite constructions. The Stacks chapter credits Christian Serpé and Nicolas Spaltenstein for the unbounded-resolution theory; *Sets* credits the large-cofinality method to Grothendieck.
- **Flat and K-flat resolutions.** *Modules on Ringed Spaces* and *Cohomology of Sheaves* supply flat-module and compatible-resolution methods. The course develops cycle attachments, complete flatness calculations and compatible resolutions.
- **Tensor, pullback and pushforward.** *Cohomology of Sheaves* supplies tensor, Tor, pullback and local-cohomology arguments. The course includes fibre-product comparisons, coherence, the general derived adjunction, coefficient comparisons and Leray exact-couple details.
- **Derived Hom and supports.** *Cohomology of Sheaves* and *Sheaves of Modules* supply Hom and closed-support arguments. The course includes sign calculations, functoriality, composition and dinaturality, locally closed supports, and singular-cochain comparison on Euclidean opens.
- **Perfect complexes, projection and base change.** *Cohomology of Sheaves* supplies finite-model, pseudo-coherence, Tor-amplitude, duality, projection and base-change methods. The course develops the finite-cell retract argument, local and pasting checks, coefficient-model comparisons, examples and exercises.
- **Inverse limits and unbounded resolutions.** This lesson follows and expands Dolors Herbera, Wolfgang Pitsch, Manuel Saorín and Simone Virili, [*A poisonous example to explicit resolutions of unbounded complexes*, version 3](https://arxiv.org/abs/2407.09741v3). Writing and mathematical self-check are by GPT-6.1 Sol (OpenAI), Ultra, October 2026. The lesson adds direct lifting and K-injectivity proofs, an explicit truncation calculation, totalization details and worked exercises. Roos and Spaltenstein are credited for the resolution methods; the related construction of Chachólski, Neeman, Pitsch and Scherer is linked in the lesson.
- **Quasi-coherent sheaves and concentrated scheme maps.** The Stacks project authors' *Schemes*, *Properties of Schemes*, *Cohomology of Schemes* and *Cohomology of Sheaves* supply affine, Gabber small-submodule and Čech methods. The lesson includes full affine and unbounded comparison arguments, precise cohomological bounds, and projection and flat-base-change proofs.
- **Additional mathematical reading.** The lessons cite Amnon Yekutieli, Daniel Murfet, Pierre Schapira, Bernhard Keller, Joseph Lipman and Nicolas Spaltenstein for their relevant expositions and methods, and Roman Bezrukavnikov's MIT notes by Serina Hu and Vasily Krylov for algebraic constructions. Each contribution and research route is identified where used. Joël Riou and the Mathlib community's derived-category code is a comparison reference, not a formal verification of these lessons.

The lesson texts identify individual sources and mathematical conditions. Proof expansions and exposition dated 1–3 October 2026 are by GPT-6.1 Sol (OpenAI), Ultra, with the contributions credited above.

[AI Integrated Stacks Project source edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790) · [Stacks project](https://stacks.math.columbia.edu/) · [Methods of Algebra, Volume 2](https://kokunoyumeto.github.io/methods-of-algebra-volume-2-en/) · [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)

## Earlier proofs for the holomorphic examples

Read these components in order before the holomorphic coordinate-germ lemma in the tensor lesson:

- [Real analysis on closed intervals](prerequisites/real-analysis-on-closed-intervals.html): CC0-1.0.
- [Complex exponential and the circle](prerequisites/complex-exponential-and-the-circle.html): CC0-1.0.
- [The scalar Cauchy formula and power series](prerequisites/scalar-cauchy.html): CC0-1.0.
- [Holomorphic functions and convergent power series](prerequisites/holomorphic-power-series.html): CC0-1.0.

The first two components follow Jiří Lebl, *Basic Analysis*, volumes I and II, version 6.3, in their own words. Their text is by GPT-6 Astra (OpenAI), Ultra; selection and prerequisite integration are by GPT-6.1 Sol (OpenAI), Ultra. Their [real-analysis source notice](prerequisites/assets/notices/real-analysis-source-notice.html) and [circle source notice](prerequisites/assets/notices/complex-exponential-source-notice.html) give the attribution and link the unmodified source passages, which keep Lebl's licence.

The scalar Cauchy and polydisc/Taylor readings retain independently authored programme proofs dedicated under CC0 1.0, with Claude Opus 5.5 (Anthropic) contributions and the earlier AI proof expansions identified in each reading. Their selection and scalar specialization do not import external textbook text. The course adds complete local proofs of the holomorphic germ quotients and the curve and surface residue resolutions. No independent AI review, human review or formal verification is claimed.
