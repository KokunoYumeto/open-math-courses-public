# Prerequisites and reading order

Read the supporting lessons below before the six main lessons: tori; centralizers; roots and rank one; root data and Bruhat cells; integral pinned classification; forms and parabolic flag schemes. Every mathematical result used requires its proof here or in an earlier programme lesson. Freely accessible references provide writing and comparison material; they never replace that programme proof.

Approximation, general flat quotients, Lie and group foundations have written supporting proofs, and concrete corrections across the six main lessons are integrated. The complete consumed-result inventory and full transitive proof validation remain active.

The relative Bruhat and Schubert arguments retain the integral scheme decompositions used for finite-field counting and torified varieties. A scheme stratification does not partition points over a general ring.

## Earlier supporting lessons

| Read first | Written proofs |
| --- | --- |
| [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md) | Localization, arbitrary-module Tor, finite algebra, modules and sheaves, derived cohomology, affine vanishing, flat base change, arbitrary-base projective properness and Serre arguments. |
| [Projective cohomology and smooth affine models](AG-RG-S02.md) | Completion, formal functions, Noetherian models, universal cohomology complexes and full curve duality. |
| [Completing a smooth affine curve and extending its group action](AG-RG-S03.md) | Finite normalization, proper smooth completion, regular extension of the translation family and the one-dimensional unipotent argument. |
| [Affine descent, Zariski Main and recognition of spaces](AG-RG-S04.md) | Integral algebra, full conductor, general scheme factorization, separated locally quasi-finite descent, finite affine quotient and space recognition, in dependency order. |
| [Artin approximation and desingularization](AG-RG-S05.md) | Pointed étale approximation, complete-local finite splitting covers and torus descent, finite coefficient systems, full desingularization and its consumed foundations. |
| [Lie proofs for the characteristic-zero group construction](AG-RG-S06.md) | Complete ordered-word proof, trace criterion and complete reducibility, rational Serre algebra, finite highest-weight presentations and polynomial rank-one integration. |
| [Flat quotient bootstrap over an arbitrary base](AG-RG-S07.md) | Fibre loci, regular cuts, finite-presentation descent, slices, finite parts and the general flat quotient with all test schemes. |
| [Supporting group-scheme proofs](AG-RG-S08.md) | Canonical flat components, field-group identity components with nilpotents, point dimension, field smoothness descent, Cartier, universal schematic density, closed orbits and semilinear Hopf descent. |

The supporting lessons are placed before their first main-course use. Their precise earlier algebra and geometry inputs remain part of the active proof review.

## Lie algebras and smoothness of group schemes

Lie algebras at the identity and invariant derivations, including their commutator bracket; Cartier smoothness for a locally finite-type group scheme over a characteristic-zero field. Used in main lesson 1 §4; 5 §6.

**Required programme proof.** AG-RG-S08 G.1.1–G.1.2 (point dimension), G.2.1 (field smoothness descent), G.3.1–G.3.4 (full Cartier chain); earlier GS02 Proposition 1.1, Lemma 2.1, Theorem 2.2 and Proposition 2.7 retain the tangent/bracket/cotangent proofs.

The argument is in [AG-RG-S08.md](AG-RG-S08.md).

## Group schemes over a field

For locally finite-type group schemes over any field, including nonreduced groups, the identity component is a normal geometrically irreducible quasi-compact subgroup, open and closed, and commutes with every field extension. For a smooth finite-type algebraic group acting on a nonempty separated finite-type reduced scheme over an algebraically closed field, orbits are locally closed and there is a closed orbit; schematic stabilizers and the associated scheme orbit use the separately proved G/H quotient. Also, a quasi-compact homomorphism of field group schemes has a closed schematic subgroup image; if its source is reduced, the factor onto that image is faithfully flat. Quasi-compact dominant homomorphisms into a reduced target are faithfully flat. These statements are applied to smooth finite-type geometric fibres in lesson 5 Section 9. Used in main lesson 1 §2; 2 §1; 5 §9 (Propositions 5.6 and 5.8 for schematic image and fibre affineness).

**Required programme proof.** AG-RG-S08 G.0.1 (canonical flat closed structure), G.0.2 (algebraic-extension connectedness), G.0.3 (locally finite-type field-group identity component with nilpotents); AG-RG-S08 G.4.1–G.4.2 (reduced products and full smooth closed-orbit proof); the separate schematic orbit proof retains earlier GS03 Lemma 7.12 and Theorem 7.13, with GS04 Theorem 11.1b and the flat quotient now proved in AG-RG-S07. The current earlier GS03 Propositions 5.6 and 5.8 supply the complete closed-image and flatness argument consumed in AG-RG-05 §9.

The argument is in [AG-RG-S08.md](AG-RG-S08.md).

## Quotients and torsors

Effective affine finite locally free free-action quotients, including nonconstant and nonreduced finite groups; effective affine-group torsors and nonabelian H1; Hilbert 90 over arbitrary fields and Gm torsors as line bundles; scheme quotients G/H for finite-type groups over a field and closed H. Used in main lesson 1 §§2,5; 3 §§5–6; 6 §§4–6.

**Required programme proof.** Faithfully flat affine descent (opening Module descent lemma/Affine descent corollary); §§1–4, especially Theorem 4.3 (general finite flat affine quotient) and Corollary 4.4 (constant finite étale special case); §§6–7.1 (torsors and cocycles); Theorem 8.1 (frames, Hilbert 90, line bundles); Lemma 11.1a/Theorem 11.1b (field G/H scheme quotient, through AS-02 bootstrap).

Earlier written programme proof: [quotients and torsors](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/src/quotients-and-torsors.md). That proof supplies this input.

## Diagonalizable groups and groups of multiplicative type

Over an arbitrary field, finite-type groups of multiplicative type are contravariantly equivalent to finitely generated character groups with continuous Galois action and split over a finite separable extension. Used in main lesson 1 introductory section and §§3–4.

**Required programme proof.** AG-RG-S08 G.5.1–G.5.3 (explicit arbitrary-characteristic semilinear Hopf descent); earlier GS05 Lemma 2.1/Theorem 2.2, Theorem 5.0 and Lemma 5.1 retain the monomial and separable-splitting proofs, and Theorem 3.1, Theorem 4.10/Corollary 4.11, Proposition 7.14, Theorem 7.15 and Proposition 8.1 retain the actual deformation proofs.

The argument is in [AG-RG-S08.md](AG-RG-S08.md).

## Faithfully flat descent

Effective faithfully flat descent of affine schemes over arbitrary bases, modules, algebras and equivariant morphisms, including group operations and their identities. Used in main lesson 1 §3; 3 §1 (central quotient group operations); 6 §§2,4,6.

**Required programme proof.** Earlier AG-GS-04, opening Faithfully flat affine descent: Module descent lemma (line 29) and Affine descent corollary (line 45), including arbitrary-base gluing and equivariant maps. Unit, multiplication, inverse and all group-law equalities descend as maps and equalities. Current provider commit 4034302e92d3ef07f10dde2d4bf9673a9917b996.

Earlier written programme proof: [quotients and torsors](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/src/quotients-and-torsors.md). That proof supplies this input.

## The bootstrap theorem

An equivalence relation of algebraic spaces with flat locally finitely presented projections has an algebraic-space fppf quotient; a free action of a flat locally finitely presented group gives a representable quotient map satisfying the torsor identity on all test schemes. Used in main lesson 1 §5; 3 §5; 5 §8.

**Required programme proof.** AG-RG-S07 §§2–8: Lemmas 2.1–2.4/Corollary 2.5, dimension and Cohen–Macaulay locus 3.1–3.4, regular cuts 4.1, descent 5.1–5.3, slicing 6.1–6.2, finite part 7.1, division 8.1, general flat quotient 8.2 and free actions 8.3; preceding scheme descent/recognition and finite affine quotient in AG-RG-S04 A/E5.1/E6.1/E8.1–E8.2.

The argument is in [AG-RG-S07.md](AG-RG-S07.md).

## Artin approximation for polynomial equations

Artin approximation for finite polynomial systems over an excellent Noetherian local ring essentially of finite type over Z: a formal solution can be approximated to each finite order in its henselization, hence in an étale neighbourhood with unchanged residue field. Used in main lesson 1 §3.

**Required programme proof.** AG-RG-S05 Theorem 1.1, Lemmas 1.2–1.3/Corollary 1.4, spreading Lemma 2.1 and full finite torus system §3; complete desingularization sequence D.1–D.38 including D.34A/D.35 global selection, foundation blocks F.1–F.138 including F.99A/F.102 and G-ring permanence F.132–F.135; exact elementary earlier programme proofs in §6.

The argument is in [AG-RG-S05.md](AG-RG-S05.md).

## Limits of schemes and Noetherian approximation

Finite-presentation objects, morphisms and finite diagrams of identities descend through filtered inverse limits with affine transitions and qcqs stages; affineness, closed immersion and smoothness hold eventually under their stated finite-presentation hypotheses. Used in main lesson 1 §3; 3 §§1,5; 4 §7; 5 §§8–9; 6 §2.

**Required programme proof.** Theorem 1.1; Lemmas 2.1–2.3; Lemma 3.1/Theorem 3.2; Theorems 4.1–4.2 (objects, maps, identities, affine/finite/closed/separated properties); Theorem 5.1 (affine Noetherian approximation). Smoothness is the separately read Stacks 0C0C/0C0B proof imported in §4. AG-RG's connected normalizer models additionally use the separately read 05FI/055I/05F4 proofs.

Earlier programme source: `AG-MO/src/limits-and-noetherian-approximation.md`. Its consumed proof and transitive inputs remain in the programme review.

## Zariski's Main Theorem

For a quasi-finite separated morphism to a qcqs scheme, Zariski Main gives an open immersion into a finite scheme; this form applies target-locally on arbitrary bases. A quasi-finite separated birational morphism of integral schemes with normal target is an open immersion. A proper quasi-finite morphism is finite over arbitrary bases. Used in main lesson 5 §§7,9.

**Required programme proof.** Blocks B–D: polynomial normality, conductor proof and affine completion (C4.3/C5.1); relative integral closure and étale base change (D4.2–D4.3); general relative Zariski Main and finite factorization (D5.2/D7.1); proper quasi-finite finiteness and normal birational open immersion (D7.3/D7.4). Space recognition and normalized space factorization are E8.1/E8.2/E9.1.

The argument is in [AG-RG-S04.md](AG-RG-S04.md).

## Flatness criteria, dimension and the flat locus

For a locally finitely presented X→S, locally finite-type Y→S and a morphism X→Y, with X and Y flat over S, flatness of X→Y is equivalent to flatness of its geometric fibre maps; the finite-presentation module form also works over arbitrary nonreduced bases. Used in main lesson 3 §1, Theorem 1.1; 4 §7.

**Required programme proof.** Theorem 2.1/Corollary 2.2 (Noetherian fibre criterion); Lemmas 6.1–6.2 and Theorem 6.3 (finite Tor obstruction and arbitrary-base criterion); Theorem 6.4/Corollary 6.5 (open relative flat locus and base change). Theorem 6.3 is the exact arbitrary-base input in AG-RG-04 §7.

Earlier programme source: `AG-FSE/src/flatness-criteria.md`. Its consumed proof and transitive inputs remain in the programme review.

## Étale morphisms and their local structure

A flat locally finitely presented morphism with étale geometric fibres is étale; an étale monomorphism is an open immersion. Used in main lesson 1 §3; 3 §§1,4–5; 4 §7; 6 §2.

**Required programme proof.** Lemmas 1.1–1.2 and Theorem 1.3 (standard Jacobian quotient, finite kernel/Nakayama and fibre criterion); Theorem 4.1 (open immersion equivalent to an étale monomorphism/universally injective étale map, with the faithfully flat local epimorphism proof).

Earlier programme source: `AG-FSE/src/etale-morphisms-and-their-local-structure.md`. Its consumed proof and transitive inputs remain in the programme review.

## Smooth morphisms

A locally finitely presented morphism is smooth exactly when flat with smooth geometric fibres; a smooth surjection admits sections on an étale covering, including over nonreduced bases. Used in main lesson 1 §3; 3 §§1,4; 4 §7; 6 §§2,6.

**Required programme proof.** Theorem 3.1 (fibrewise smoothness criterion), Theorem 4.1 (étale coordinates), and Theorem 5.2 (étale-local sections via a finite separable point in a nonempty smooth fibre).

Earlier programme source: `AG-FSE/src/smooth-morphisms.md`. Its consumed proof and transitive inputs remain in the programme review.

## Cohomology of sheaves on ringed spaces

Leray spectral sequence for higher direct images and sheaf cohomology Used in main lesson 5 §9.

**Required programme proof.** Section 3, Lemmas 3.1–3.3 and acyclic-resolution comparison; Section 4 filtered-complex construction; Theorem 4.1, including the full compatible injective double resolution and both filtrations.

The argument is in [AG-RG-S01.md](AG-RG-S01.md).

## Cohomology of affine schemes and Serre's criterion

Vanishing of positive quasi-coherent cohomology on affine schemes and Serre’s affine criterion for quasi-compact separated schemes Used in main lesson 1 §2; 5 §9; 6 §5.

**Required programme proof.** Theorem 5.1 and Corollary 5.2; Lemma 9.1 and Theorem 9.2, with the quasi-separatedness-free affine criterion proof.

The argument is in [AG-RG-S01.md](AG-RG-S01.md).

## Coherent sheaves on projective schemes: Serre's theorems

Finiteness of all coherent cohomology modules on a projective scheme over a Noetherian ring; eventual global generation and positive-cohomology vanishing for coherent ample twists. Used in main lesson 3 Section 5; 6 Section 2.

**Required programme proof.** Sections 7–8: all projective-space twists and perfect monomial pairing; Lemmas 8.1/8.3, Proposition 8.2, Theorem 8.4 and Corollary 8.5, including projective-scheme coherent finiteness and ample twists.

The argument is in [AG-RG-S01.md](AG-RG-S01.md).

## Base change and the Grothendieck complex

Flat base change for quasi-coherent cohomology on quasi-compact quasi-separated schemes, including localization Used in main lesson 5 §9, openly licensed affine-open proof.

**Required programme proof.** Section 6, full canonical flat base-change and localization proof for arbitrary quasi-compact quasi-separated schemes, including nonseparated intersections.

The argument is in [AG-RG-S01.md](AG-RG-S01.md).

## Semicontinuity and Grauert's theorem

Lemma (sections in a vanishing family). Let f: X -> S be a smooth projective morphism of finite presentation, and let L be an invertible O_X-module. Suppose H^q(X_s,L_s)=0 for every geometric point s of S and every q>0. Then f_*L is finite locally free, R^q f_*L=0 for q>0, and for every base change g: S′ -> S the canonical map g^*f_*L -> f′_*L′ is an isomorphism and R^q f′_*L′=0 for q>0. The base S may be arbitrary and nonreduced. Used in main lesson 3 §5; 6 §2.

**Required programme proof.** Lemma 5.1, full universally acyclic finite-projective replacement; Proposition 5.2, arbitrary-base and all-base-change sections in a vanishing smooth projective family.

The argument is in [AG-RG-S02.md](AG-RG-S02.md).

## The theorem on formal functions

For a Noetherian ring A, a projective scheme X over A, a coherent F and an ideal I, I-adic completion of H^q(X,F) equals the inverse limit of H^q(X,F/I^n F). For complete local A this turns a compatible formal idempotent in H0 into an actual idempotent. Used in main lesson 3 §5.

**Required programme proof.** Lemmas 1.1–1.4 and 2.1–2.2, Theorem 2.3 and Corollary 2.4: finite Rees images, kernel filtrations, exact inverse limits, projective formal functions and idempotents.

The argument is in [AG-RG-S02.md](AG-RG-S02.md).

## Serre duality for smooth projective curves

For a smooth projective pure one-dimensional curve C over any field and an invertible L, H^1(C,L) is naturally dual to H^0(C,Omega_(C/k) tensor L inverse). Used in main lesson 1 §2; 3 §2.

**Required programme proof.** AG-RG-S02 §6, Lemma 6.A and Theorem 6.B (complete ambient projective duality), Lemma 6.1 and Theorem 6.2 (local Ext and single-row local-to-global comparison), with projective finiteness and finite filtered complexes in AG-RG-S01 §§4,8.

The argument is in [AG-RG-S02.md](AG-RG-S02.md).

## Brauer groups and Tsen's theorem

Central simple algebras of degree n split over finite separable extensions; Brauer and matrix-algebra descent over fields Used in main lesson 6 §6.

**Required programme proof.** Lemma 6.1 and Theorem 6.2: finite-dimensional density proved, central simplicity under arbitrary field extension, algebraic-closure splitting, smooth isomorphism scheme and finite separable splitting; converse and matrix-algebra descent.

The argument is in [AG-RG-06.md](AG-RG-06.md).

## Complete reducibility: Casimir elements and Weyl's theorem

Complete reducibility and invariant complements for finite-dimensional semisimple Lie algebras over every characteristic-zero field. Used in main lesson 5 §6.

**Required programme proof.** AG-RG-S06, Sections 1–4; Proposition 4.1 and Theorem 4.2, including the invariant projection and finite-linear-system descent over every characteristic-zero field.

The argument is in [AG-RG-S06.md](AG-RG-S06.md).

## Representations of sl(2)

Finite-dimensional sl2 weight theory and explicit polynomial SL2 actions on symmetric powers Used in main lesson 5 §6.

**Required programme proof.** Section 6, Lemma 6.1

The argument is in [AG-RG-05.md](AG-RG-05.md).

## Inner derivations of semisimple Lie algebras

Every derivation of a finite-dimensional semisimple Lie algebra over a characteristic-zero field is inner, by the nondegenerate Killing form. Used in main lesson 5 §6, directly over Q.

**Required programme proof.** AG-RG-S06, Proposition 3.1 (Killing nondegeneracy) and Proposition 3.3 (all derivations inner over the given characteristic-zero field).

The argument is in [AG-RG-S06.md](AG-RG-S06.md).

## Root systems and their Weyl groups

Positive-root inversion length, simple-reflection length reduction and the complete Coxeter presentation for the Weyl groups of the pinned reductive groups used in lesson 5 Sections 2 and 5. Used in main lesson 5 §§2,5.

**Required programme proof.** Earlier chamber freeness Lemma 3.A; Proposition 3.1 and Lemmas 3.2–3.3, Theorem 3.4; rank-two table (3.2). The consumed presentation concerns the root data of the pinned groups in lesson 5 Sections 2 and 5.

The argument is in [AG-RG-04.md](AG-RG-04.md).

## The isomorphism theorem and Serre's theorem

Finite-type Cartan Serre presentation: finite-dimensional split semisimple Lie algebra with the specified roots over Q, compatible with characteristic-zero field extension. Used in main lesson 5 §6, directly over Q and every characteristic-zero extension.

**Required programme proof.** AG-RG-S06, Theorem 1.A, Section 5, Lemma 6.1 and Theorem 6.2: full rational Serre algebra, auxiliary relations, Serre ideal stability, finite root set and semisimplicity.

The argument is in [AG-RG-S06.md](AG-RG-S06.md).

## Weights, Verma modules and the theorem of the highest weight

Finite integrable highest-weight presentation for dominant integral weights, its irreducibility over C, and its rational form compatible with characteristic-zero extension. Used in main lesson 5 §6, rational finite highest-weight presentation and absolute irreducibility.

**Required programme proof.** AG-RG-S06, Section 7, equations (7.1)–(7.6) and the rational base-change paragraph; Section 8 for faithful fundamental modules and polynomial rank-one actions.

The argument is in [AG-RG-S06.md](AG-RG-S06.md).

## Sources and further reading

The source record identifies exact freely accessible editions and the passages compared. The component record preserves the terms of attributed adaptations. Independently authored contributions retain CC0; Stacks adaptations retain their GNU Free Documentation License obligations.
