# Sources, contributors and terms

The exposition is by OpenAI Codex (AI), with contributions and component terms identified below and in the course notices. The mathematical references accompany the proofs and exact prerequisite links in the lessons.

## Bounded-operator foundations

The bounded-operator lesson contains ten sections and three solved problems. Jacob Lurie, [*Math 261y: von Neumann Algebras*, Lecture 5](https://people.math.harvard.edu/~lurie/261ynotes/lecture5.pdf), 9 September 2011, Theorem 4 and Proposition 5, pp. 1–2, gives the finite-vector bicommutant argument. The course proof assumes that the algebra contains the identity, as required by its projection argument.

[The Hilbert-space lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html), Sections 1–3, and [the continuous-calculus lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), Theorem 5.1 and Section 8, give the prerequisite proofs. Their authors and component terms are identified on those pages.

## Spectral calculus and scalar inputs

The twelve-section spectral lesson constructs bounded and unbounded spectral integration and includes four solved problems. Its scalar inputs are Haar Theorem 2.2 and Proposition 2.3 and measure-tools Theorems 1.1, 2.1–2.2 and 3.1–3.2, together with the topology used in the Riesz–Markov–Kakutani theorem. [The scalar companion](spectral-scalar-foundations.md) links these proofs and gives the compact-space, complexification, L2, measure, Borel-representative and approximation arguments. In particular it explains how complex RMK gives the real version used in SK. The construction uses the earlier bounded Hilbert-space and continuous-calculus results and the maximal principle, without assuming an unbounded spectral or polar theorem.

The spectral lesson and scalar companion are CC0-1.0. The referenced mathlib components are Apache-2.0; their human contributors and precise declarations are identified in the companion. Mathematical explanation and presentation include contributions by GPT-6.1 Sol (OpenAI).

## Concrete preduals

The fourteen-section lesson develops projective tensors, Banach quotients, vector series and continuous duality, with four solved models. Its programme inputs are arbitrary-Hilbert Riesz representation, bounded forms and adjoints (HS Sections 2–3), real and complex norm-preserving Hahn–Banach extension (HB Section 2), real locally convex separation (HB Section 6), and the bounded positive-functional support and ideal argument (UE, State support and continuity tools; BI Lemma 8.1 and Theorem 8.3(1,3)). These lessons include AI contributions by Claude Opus 5.5 (Anthropic) and GPT-6.1 Sol (OpenAI), under their stated CC0 terms.

The cited mathlib Hilbert-dual, adjoint and Hahn–Banach components are Apache-2.0. Their contributors are, respectively, Frédéric Dupuis; Frédéric Dupuis and Heather Macbeth; and Yury Kudryashov and Heather Macbeth. The CP lesson supplies exact declaration locators at mathlib commit `71a80585ee495fc24472fd0eaffc89d94e4fd8d6`.

## Closed positive forms

The eleven-section lesson gives representation, exact-domain and directed convergence proofs, three worked models and five solved problems. Mathematical references are Zoltán Sebestyén and Zsigmond Tarcsay, [*Basic representation theorems of forms*, arXiv:2505.09588v1, Lemma 2.1 and Corollary 2.7](https://arxiv.org/pdf/2505.09588v1), and Barry Simon, [*A canonical decomposition for quadratic forms with applications to monotone convergence theorems*, Theorems 3.1 and 4.1](https://math.caltech.edu/SimonPapers/81.pdf). The first reference uses a closed-operator argument; the course construction instead starts from the bounded prerequisites in QF01. Simon's convergence theorems concern sequences; QF treats directed limits and their exact finite-energy domains.

The exposition is by OpenAI Codex, with mathematical explanations by GPT-6 Astra and reading presentation by GPT-6.1 Sol (OpenAI), under CC0-1.0. The HS, BK, SK and scalar prerequisite proofs have their own author and component notices.

## Tomita graph closure and polar data

The thirteen-section lesson proves the adjoint, graph and polar statements, with two matrix models and five solved problems. Its inputs are the Hilbert-space, bounded-operator, closed-form, spectral and scalar proofs linked in TC01.

The exposition is by OpenAI Codex, with mathematical correspondence and matrix-model contributions by GPT-6.1 Sol and reading presentation by GPT-6 Astra (OpenAI), under CC0-1.0. Programme prerequisite texts carry their own credits and component terms.

## Real coercive equations

The supporting proof, matrix calculations, diagram and reproducible figure source are by OpenAI Codex (GPT-6 Astra), CC0-1.0. The mathematical source is Marc A. Rieffel and Alfons Van Daele, *A bounded operator approach to Tomita–Takesaki theory*, Pacific Journal of Mathematics 69 (1977), 187–221; [publisher PDF](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf), Lemma 5.6. The lesson proves the initial real coercive equation; bounded multiplication is treated in the linked continuation.
