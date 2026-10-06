# Studying class field theory

The question behind reciprocity is concrete: which arithmetic elements are norms, and how do the remaining classes act on an extension? Begin with a calculation, then identify the hypotheses that make it work in general. Lesson numbers provide stable references. The paths below select sections when a later application needs a proof developed elsewhere in the course.

## From concrete norms to local reciprocity

Start with automorphisms and norm-one elements; inspect the local cyclic calculation before constructing the abstract map.

- **Lesson 1.** [Profinite groups and infinite Galois theory](src/profinite-groups-and-infinite-galois-theory.md) — all.
- **Lesson 3.** [Hilbert's Theorem 90 and Kummer theory](src/hilberts-theorem-90-and-kummer-theory.md) — all.
- **Lesson 2.** [Cohomology of cyclic groups and the Herbrand quotient](src/cohomology-of-cyclic-groups-and-the-herbrand-quotient.md) — all.
- **Lesson 6.** [Local reciprocity and norm groups](src/local-reciprocity-and-norm-groups.md) — 1–3: arithmetic data and cyclic axiom.
- **Lesson 4.** [Frobenius lifts and abstract reciprocity](src/frobenius-lifts-and-abstract-reciprocity.md) — all: norm-class construction.
- **Lesson 5.** [The reciprocity law and the class field correspondence](src/the-reciprocity-law-and-the-class-field-correspondence.md) — all: isomorphism and correspondence.
- **Lesson 6.** [Local reciprocity and norm groups](src/local-reciprocity-and-norm-groups.md) — 4–6: arithmetic reciprocity and norms.
- **Lesson 7.** [Formal groups and Lubin–Tate modules](src/formal-groups-and-lubin-tate-modules.md) — all.
- **Lesson 8.** [Lubin–Tate division fields](src/lubin-tate-division-fields.md) — all.
- **Lesson 9.** [Explicit local reciprocity and the existence theorem](src/explicit-local-reciprocity-and-existence.md) — all.
- **Lesson 10.** [Abelian ramification, conductors and Hasse–Arf](src/abelian-ramification-conductors-and-hasse-arf.md) — all.
- **Lesson 11.** [Hilbert symbols and local conics](src/hilbert-symbols-and-local-conics.md) — all.
- **Lesson 12.** [Weil groups and one-dimensional representations](src/weil-groups-and-one-dimensional-representations.md) — 1–6: local Weil groups and factors.

## From local obstructions to global classes

See a complete constant-field calculation, then prove its finite-place and lattice mechanism before proving principal-symbol cancellation.

- **Lesson 13.** [Idèles in extensions and their cohomology](src/ideles-in-extensions-and-their-cohomology.md) — all.
- **Lesson 14.** [The Herbrand quotient of the idèle class group](src/the-herbrand-quotient-of-the-idele-class-group.md) — 1–2: explicit calculation and three modules.
- **Lesson 14.** [The Herbrand quotient of the idèle class group](src/the-herbrand-quotient-of-the-idele-class-group.md) — 3–8: general proof and splitting applications.
- **Lesson 15.** [The norm index bound and Hasse's norm theorem](src/the-norm-index-bound-and-hasses-norm-theorem.md) — 1–8: norm bound and cyclic axiom.
- **Lesson 16.** [The global reciprocity law](src/the-global-reciprocity-law.md) — 1: cyclotomic and constant-field cancellation.
- **Lesson 16.** [The global reciprocity law](src/the-global-reciprocity-law.md) — 2–8: map on classes and local comparison.
- **Lesson 17.** [Global existence and the idèlic class field correspondence](src/global-existence-and-the-idelic-class-field-correspondence.md) — all: existence and function-field Weil groups.
- **Lesson 18.** [Ray class fields, conductors and ideal reciprocity](src/ray-class-fields-conductors-and-ideal-reciprocity.md) — all: ray conditions.

## Applications of reciprocity

Choose the arithmetic question after the local and global core.

- **Lesson 20.** [Kronecker–Weber and the maximal abelian extension of the rationals](src/kronecker-weber-and-the-maximal-abelian-extension-of-the-rationals.md) — rational ray fields and cyclotomic action.
- **Lesson 19.** [Hilbert and ring class fields, and quadratic prime forms](src/hilbert-and-ring-class-fields-and-quadratic-prime-forms.md) — Hilbert and ring class fields, quadratic prime forms.
- **Lesson 23.** [Power residue symbols and reciprocity laws](src/power-residue-symbols-and-reciprocity-laws.md) — power symbols and primary reciprocity laws.
- **Lesson 21.** [Artin L-functions, conductors and discriminants](src/artin-l-functions-conductors-and-discriminants.md) — Artin factors and functional equations.
- **Lesson 22.** [The Chebotarev density theorem](src/the-chebotarev-density-theorem.md) — Dirichlet density and ray primes.
- **Lesson 22.** [The Chebotarev density theorem](src/the-chebotarev-density-theorem.md) — 6A: full Hasse–Minkowski, using the conic theorem of lesson 15 and the ray-prime theorem.

## Cohomology, Weil extensions and towers

Follow the final proofs back to the earlier applications they complete.

- **Lesson 24.** [Brauer groups of local and global fields](src/brauer-groups-of-local-and-global-fields.md) — all: Brauer invariants, fundamental classes, Weil extensions and tower bounds.
- **Lesson 12.** [Weil groups and one-dimensional representations](src/weil-groups-and-one-dimensional-representations.md) — 7: global compatibility, with lesson 17 in function fields and lesson 24 in number fields.
- **Lesson 19.** [Hilbert and ring class fields, and quadratic prime forms](src/hilbert-and-ring-class-fields-and-quadratic-prime-forms.md) — 9: iteration of the Hilbert field, pointing to the full infinite-tower theorem in lesson 24.
- **Lesson 21.** [Artin L-functions, conductors and discriminants](src/artin-l-functions-conductors-and-discriminants.md) — 8: global orthogonal consequence, with its separately stated external prerequisite.

## Tracking hypotheses

The abstract proof uses a discrete Galois module, a degree map and a compatible valuation. Its value group can be the integers or their profinite completion. The local and global lessons verify these hypotheses before applying the abstract isomorphism. In global function fields, the characteristic-p arguments use additive duality as well as radicals; the Weil group keeps integer constant-field degree. In number fields, the profinite degree construction and the later Weil extension have distinct roles.

The cyclic norm axiom in lesson 15 precedes reciprocity and existence. The general quadratic-form theorem is proved in lesson 22 after its ray-prime prerequisite. Likewise, the number-field Weil construction and infinite-tower theorem follow their cohomological proofs in lesson 24. The separately owned higher-dimensional local epsilon and orthogonal prerequisites retain the proof status explicitly stated in lessons 12 and 21.

All four exercises in each lesson have solutions. Work through the explicit norm or symbol calculation before reading its solution; then check exactly which hypotheses are used when the lesson passes from that example to the general theorem.
