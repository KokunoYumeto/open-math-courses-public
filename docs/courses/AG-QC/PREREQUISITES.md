# Prerequisites and proof providers

The links below identify the precise statements supplied by this edition, their hypotheses and their proofs. A proof using a stated input is complete only after that input has an exact available proof. The input record distinguishes those dependencies from the arguments written in each lesson.

## Programme foundations

- **SH-DC.injective-embeddings**: No commutativity or separation assumption; product is an injective embedding, not a hull. [Exact proof](../derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#2-functorial-injective-embeddings). Lemmas 2.1-2.2 and Theorem 2.3. Source SHA-256: `b2dc989efbc8d2d4004c8d24cbc3004a9e81da485cd702bb7d293a7f8af5edba`.
- **SH-DC.flasque-acyclic**: Arbitrary topological spaces and unital coefficient rings, without compactness or separation. [Exact proof](../derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#1-extending-maps-and-extending-sections). Lemmas 1.1-1.2 and Proposition 1.3. Source SHA-256: `b2dc989efbc8d2d4004c8d24cbc3004a9e81da485cd702bb7d293a7f8af5edba`.
- **SH-DC.bounded-derived**: Lower bound for complexes; no filtered-colimit or product exactness assumption on A. Left exactness, or degree-zero comparison as well as positive vanishing, is required in the acyclic-term assertion. [Exact proof](../derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#4-right-derived-functors-on-bounded-below-complexes). Theorem 4.1. Source SHA-256: `b2dc989efbc8d2d4004c8d24cbc3004a9e81da485cd702bb7d293a7f8af5edba`.
- **SH-DC.Leray-spectral-sequence**: First-quadrant sequence for sheaves in degree zero; no asserted unconditional convergence for arbitrary two-sided unbounded inputs. [Exact proof](../derived-categories-and-sheaf-operations/derived-pullback-and-pushforward.html#6-exercises-with-checked-solutions). Proposition 3.1 and Exercise 3 solution. Source SHA-256: `fece9386a64e3298cd133f9ed65d4d74aac82b9a8b266fb5ccc6363c8c063ab2`.
- **AG-ETALE.Noetherian-vanishing**: Noetherian topological space of finite dimension at most d; arbitrary abelian sheaf; H^q=0 for q>d. This is a Zariski topological result and does not require étale torsion hypotheses. [Exact proof](../ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula.html#7-the-bound-for-all-finite-type-schemes). Section 7, Lemma 7.1; proof lines 208–227, generator reduction and induction on dimension/irreducible components. Source SHA-256: `a79b0658b3888f6d6e9e92b62e2f180a7a756248afc76c5176d4ecc1c888f51c`.
- **AG-CA.completion**: Exact completion and completed-module tensor comparison require Noetherian R and finite modules. R→R-hat flat for Noetherian R; faithful flatness additionally I⊂Jac(R), in particular maximal-ideal completion of a Noetherian local ring. [Exact proof](../AG-CA/AG-CA-19.html#3-noetherian-exactness-tensoring-and-flatness). Theorems 3.1–3.3; finite-ideal quotient formula Proposition 2.2. Source SHA-256: `b26410bacd1cc68362c171189e0d2fe610d9c9a1a114965c1338bf49ccea67b8`.
- **AG-QC15.associated-zero-divisors**: R commutative Noetherian; M arbitrary; empty union for M=0. [Exact proof](../AG-CA/AG-CA-04.html#1-annihilators-that-are-prime). Lemma 1.1 and Theorem 1.2 with proofs. Source SHA-256: `a93661c9e37cb85586daac99604b6a1071ae56630a0c981e31fd141b8104e157`.
- **AG-QC15.associated-prime-finiteness**: R Noetherian; M finitely generated; zero module allowed with empty filtration. [Exact proof](../AG-CA/AG-CA-04.html#2-exact-sequences-and-finite-control). Theorem 2.2 with proof. Source SHA-256: `a93661c9e37cb85586daac99604b6a1071ae56630a0c981e31fd141b8104e157`.
- **AG-QC15.finite-prime-avoidance**: Arbitrary commutative ring, finite family of prime ideals; no infinite-field hypothesis. The zero-divisor application uses a nonzero Noetherian ring. [Exact proof](../AG-CA/AG-CA-04.html#9-solutions). Exercise 8.5, fully proved in Solution 8.5. Source SHA-256: `a93661c9e37cb85586daac99604b6a1071ae56630a0c981e31fd141b8104e157`.
- **AG-QC15.regular-implies-CM**: Nonzero commutative Noetherian local ring; regular means embedding dimension equals Krull dimension; includes the field case. [Exact proof](../AG-CA/AG-CA-12.html#6-regular-local-rings-and-complete-intersections). Theorem 6.1 with proof. Source SHA-256: `eeeff0205fcf94eb6421f1590970382145a6f0cfe1cc5e15de583068298c44c4`.
- **AG-QC15.regular-quotient-CM-dimension**: Nonzero Noetherian regular local ring; the list lies in the maximal ideal and final quotient is nonzero. No smoothness or reducedness of the quotient. [Exact proof](../AG-CA/AG-CA-12.html#6-regular-local-rings-and-complete-intersections). Lemma 2.1, Theorem 2.3 depth drop, Corollary 4.3 proof, and Corollary 6.2 with proof. Source SHA-256: `eeeff0205fcf94eb6421f1590970382145a6f0cfe1cc5e15de583068298c44c4`.
- **AG-QC15.CM-unmixedness**: Finite nonzero module over a Noetherian local ring; CM means depth equals support dimension. Equal heights in an arbitrary ambient ring are not asserted. [Exact proof](../AG-CA/AG-CA-12.html#4-when-dimension-detects-regularity). Theorem 4.1 and Corollary 5.2, each with proof. Source SHA-256: `eeeff0205fcf94eb6421f1590970382145a6f0cfe1cc5e15de583068298c44c4`.
- **AG-QC15.CM-localization**: Nonzero finite CM module over a Noetherian local ring; localization at a support prime, so the localized module is nonzero. [Exact proof](../AG-CA/AG-CA-12.html#5-localization-and-cohen-macaulay-rings). Theorem 5.1 and Corollary 5.2 with proofs. Source SHA-256: `eeeff0205fcf94eb6421f1590970382145a6f0cfe1cc5e15de583068298c44c4`.
- **AG-QC15.CM-height-dimension**: Noetherian CM local ring; p arbitrary prime. dim A_p is ht_A p. [Exact proof](../AG-CA/AG-CA-12.html#5-localization-and-cohen-macaulay-rings). Lemma 5.4 with proof. Source SHA-256: `eeeff0205fcf94eb6421f1590970382145a6f0cfe1cc5e15de583068298c44c4`.
- **AG-QC15.Auslander-Buchsbaum**: R commutative Noetherian local; M nonzero finitely generated with finite projective dimension. The zero module and modules of infinite projective dimension are excluded. [Exact proof](../AG-CA/AG-CA-13.html#3-the-auslander-buchsbaum-formula). Theorem 3.1 with full induction proof. Source SHA-256: `a98b84e8b9b1b60a2299c0e6592c8fd38515ac5de03d3ad5bcb75f49aeeecbbb`.
- **AG-QC15.regular-finite-free-resolutions**: R nonzero commutative Noetherian regular local; finite means finitely generated. Global dimension statement also covers arbitrary modules. [Exact proof](../AG-CA/AG-CA-14.html#2-the-homological-converse). Theorem 2.2 with proof; direct regular implication uses projective-dimension Corollary 4.3. Source SHA-256: `618df1c1404575a4acbbfac95323eb877d184e8d4650a860fc4a66bc00b890cd`.
- **AG-QC15.regularity-of-projective-space-stalks**: Arbitrary field, no perfection or algebraic-closure hypothesis. Noetherianity is essential for the regular-ring results. [Exact proof](../AG-CA/AG-CA-14.html#3-regularity-at-more-general-points). Theorem 3.2 and Proposition 3.3 with proofs, including polynomial iteration. Source SHA-256: `618df1c1404575a4acbbfac95323eb877d184e8d4650a860fc4a66bc00b890cd`.
- **AG-QC15.Koszul-resolution**: Regular means successive multiplication injective and final quotient nonzero; no Noetherian/local/field hypothesis. [Exact proof](../AG-CA/AG-CA-13.html#4-koszul-resolutions). Theorem 4.1 and Corollary 4.2 with proofs. Source SHA-256: `a98b84e8b9b1b60a2299c0e6592c8fd38515ac5de03d3ad5bcb75f49aeeecbbb`.
- **AG-QC15.finite-type-height-formula**: Arbitrary field; finite-type domain for the height formula, with separate componentwise application in general algebras. No perfection assumption. [Exact proof](../AG-CA/AG-CA-09.html#4-parameters-measure-dimension-and-height). Theorem 4.3 proof and Theorem 5.1 proof. Source SHA-256: `5b0969051396f29b75c0a7466acfdac4cc2457893a73fc4f3f312e3c0d434de4`.
- **AG-QC15.dimension-at-arbitrary-point**: Finite-type k-algebra; arbitrary point, possibly nonclosed; equidimensionality is required for using one fixed component dimension. [Exact proof](../AG-CA/AG-CA-09.html#6-dimension-at-a-point). Theorem 6.1 with full proof and following equidimensional consequence. Source SHA-256: `5b0969051396f29b75c0a7466acfdac4cc2457893a73fc4f3f312e3c0d434de4`.
- **AG-QC10.exact-finite-completion**: R Noetherian; every module in the short exact sequence finitely generated; arbitrary ideal I; neither I⊂Jac(R) nor prior completeness of R is required for this assertion. [Exact proof](../AG-CA/AG-CA-19.html#3-noetherian-exactness-tensoring-and-flatness). Theorem 3.1 with Artin–Rees and presentation proof. Source SHA-256: `b26410bacd1cc68362c171189e0d2fe610d9c9a1a114965c1338bf49ccea67b8`.
- **AG-QC10.faithfully-flat-local-completion**: R Noetherian. Faithful flatness requires I⊂Jac(R); an arbitrary ideal gives only flatness. [Exact proof](../AG-CA/AG-CA-19.html#3-noetherian-exactness-tensoring-and-flatness). Theorem 3.2 with full proof and local specialization. Source SHA-256: `b26410bacd1cc68362c171189e0d2fe610d9c9a1a114965c1338bf49ccea67b8`.
- **AG-QC10.completion-residue-quotient**: I finitely generated; no finiteness of M is needed. In the consumer R is Noetherian local, I=m and M is finite. [Exact proof](../AG-CA/AG-CA-19.html#2-topology-and-the-powers-of-the-ideal). Propositions 2.2 and 2.3 with proofs. Source SHA-256: `b26410bacd1cc68362c171189e0d2fe610d9c9a1a114965c1338bf49ccea67b8`.
- **AG-QC10.localization-is-flat**: Arbitrary commutative ring and module; no Noetherian or finite-presentation hypothesis. [Exact proof](../AG-CA/AG-CA-07.html#3-stability-and-localization). Theorem 3.3 with proof. Source SHA-256: `210b21719f7021478941153585e49e5e97f0d084b047cafe9049666435371336`.
- **AG-QC10.completion-flatness-provider-criterion**: Arbitrary commutative ring and module; no finite presentation of J or Noetherianity needed for the criterion itself. [Exact proof](../AG-CA/AG-CA-07.html#2-the-ideal-and-tor-criteria). Theorem 2.1 with full ideal-to-free-submodule-to-arbitrary-injection proof. Source SHA-256: `210b21719f7021478941153585e49e5e97f0d084b047cafe9049666435371336`.
- **AG-QC10.faithful-flatness-reflects-isomorphisms**: Arbitrary commutative rings; flat local map for Lemma 6.2. Reflection of isomorphisms applies to any module map once faithful flatness is established. [Exact proof](../AG-CA/AG-CA-07.html#6-exact-sequences-and-prime-lifting). Definition/argument preceding Lemma 6.2 and Lemma 6.2 with proof. Source SHA-256: `210b21719f7021478941153585e49e5e97f0d084b047cafe9049666435371336`.
- **AGQC17.local-completion-dimension-regularity**: Noetherian local ring, completed at its maximal ideal; equal residue field and cotangent-space dimension. [Exact proof](../AG-CA/AG-CA-19.html#4-local-dimension-and-regularity). Theorem 4.1; equality of lengths of the common residue quotients, Hilbert–Samuel dimension and the first graded piece.. Source SHA-256: `b26410bacd1cc68362c171189e0d2fe610d9c9a1a114965c1338bf49ccea67b8`.

## Hilbert-Samuel dimension: the proof route

This route supplies the dimension input used in local completion and analytification. It leads to the existing proofs, with the finite-module variant kept distinct from the ring statement.

1. [Hilbert-Serre polynomial](../AG-CA/AG-CA-10.html#3-hilbert-serre-by-multiplication). Start with a standard graded algebra over an Artinian ring and a finite graded module. The multiplication proof keeps the kernel.
2. [Hilbert-Samuel growth](../AG-CA/AG-CA-10.html#4-from-an-ideal-filtration-to-a-graded-module). Pass to the associated graded module. For a finite module over a Noetherian local ring, an m-primary ideal gives an eventual length polynomial.
3. [Exact sequences and degree](../AG-CA/AG-CA-10.html#6-exact-sequences-and-the-induced-filtration). Artin-Rees controls the induced filtration. Degrees and leading terms behave as stated; do not replace this by additivity of the whole polynomial.
4. [Growth bounds prime chains](../AG-CA/AG-CA-11.html#1-growth-bounds-every-prime-chain). Injective multiplication lowers degree; induction bounds prime-chain length without presupposing the dimension equality.
5. [Dimension equals degree and parameter count](../AG-CA/AG-CA-11.html#2-dimension-growth-and-parameter-count). Theorem 2.1 applies to every nonzero Noetherian local ring, including nonreduced rings and finite residue fields.
6. [The finite-module version](../AG-CA/AG-CA-11.html#2-dimension-growth-and-parameter-count). Corollary 2.2 identifies the degree with support dimension for every nonzero finite module, using a prime filtration.
7. [Apply the equality to completion](../AG-CA/AG-CA-19.html#4-local-dimension-and-regularity). The common finite residue quotients have the same lengths, and the first graded pieces agree. Thus maximal completion preserves dimension and regularity.

Earlier inputs: [length additivity](../AG-CA/AG-CA-03.html#3-measuring-a-module-by-simple-pieces), [Artin-Rees](../AG-CA/AG-CA-03.html#5-intersecting-a-filtration-with-a-submodule), [Nakayama](../AG-CA/AG-CA-02.html#4-finite-generators-near-a-point), [finite prime avoidance](../AG-CA/AG-CA-04.html#9-solutions), [prime filtrations](../AG-CA/AG-CA-04.html#2-exact-sequences-and-finite-control), [support of finite modules](../AG-CA/AG-CA-02.html#6-where-a-module-is-visible).

These are exact proof locations, not a certification that every prerequisite of the entire course has been checked. The machine-readable prerequisite record preserves source and reader identities and the directed dependencies.

## Normalization and dimension: exact proof inputs

Follow individual results here without searching an entire lesson. The algebraic normalization and point-dimension statements keep their full generality; the analytification application is specifically over the complex numbers.

1. [Make one equation monic](../AG-CA/AG-CA-09.html#2-making-one-equation-monic). The weighted substitution works over any field, including a finite field.
2. [Normalization respecting ideals](../AG-CA/AG-CA-09.html#3-normalization-that-respects-ideals). Theorem 3.1 and Corollary 3.2 preserve a finite chain of proper ideals. They do not require those ideals to be prime or radical, and do not assert normality or flatness of the finite algebra.
3. [The normal-base going-down input](../AG-CA/AG-CA-05.html#4-going-down-why-the-normal-base-matters). This supplies the reverse height inequality at a specified prime; lying over alone would not suffice.
4. [Dimension and height over an arbitrary field](../AG-CA/AG-CA-09.html#4-parameters-measure-dimension-and-height). The finite-type domain formula combines normalization, transcendence degree and integral dimension comparisons.
5. [Prime intervals and catenarity](../AG-CA/AG-CA-09.html#5-saturated-chains-and-catenarity). Pass to a domain quotient; do not impose equidimensionality on the whole algebra.
6. [Dimension at an arbitrary point](../AG-CA/AG-CA-09.html#6-dimension-at-a-point). Distinguish dimension of neighbourhoods from the local-ring dimension. Residue transcendence degree accounts for nonclosed points.
7. [Application to reduced complex completions](complex-analytic-spaces-and-analytification.html#3-constructing-analytification-with-the-full-ideal). The algebraic part of Lemma 3.1 uses separability, a torsion-free embedding, Artinian fibres and exact completion. It is not a claim about arbitrary Nagata rings.

Earlier inputs: [finite and integral algebras](../AG-CA/AG-CA-05.html#1-a-monic-equation-is-finite-control), [lying over and incomparability](../AG-CA/AG-CA-05.html#3-lifting-points-and-specializations), [the finite-type field lemma](../AG-CA/AG-CA-06.html#1-why-an-algebra-generated-field-is-finite), [finite exact completion](../AG-CA/AG-CA-19.html#3-noetherian-exactness-tensoring-and-flatness).

The analytic vanishing-ideal conclusion still uses its separate analytic Nullstellensatz input, and full-ideal chart coherence uses Oka. These links identify the checked algebraic route, not independent review or complete recursive certification of the course. The machine-readable prerequisite record gives exact content identities and directed dependencies.

## Oka coherence: exact proof inputs

This is a route through the existing proofs, not a replacement exposition or a claim that the whole course is complete. Follow individual results without searching entire lessons. The result records keep hypotheses, source identity and proof availability separate.

1. Start with the generic sheaf algebra. [Coherent kernels, cokernels and extensions (01BY)](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-coherent-abelian); [Finite generators on a neighbourhood (Lemma 1.3)](../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#1-coherent-modules-on-a-ringed-space). These statements apply to arbitrary ringed spaces; they do not assume holomorphic functions are already coherent.
2. Use the proof actually supplied. [Coherent versus finitely presented (Proposition 1.2(2))](../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#1-coherent-modules-on-a-ringed-space). The cited external tag 01BZ has an omitted proof in both checked editions. The complete argument is written here, assuming the structure sheaf coherent.
3. Choose one regular direction. [The convergent-germ domain](../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#1-the-ring-of-germs); Regular-coordinate choice (Lemma 4.1). Applying the coordinate lemma to the product handles finitely many nonzero germs at once.
4. Prepare and divide. [Preparation and division in AG-QC-17, Section 2](complex-analytic-spaces-and-analytification.html#2-local-analytic-algebra). This earlier argument does not use the later Oka application in the same lesson; there is no circular proof dependency.
5. Control all nearby polynomial relations. [Polynomial divisibility (Lemma 2.3)](../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#2-weierstrass-polynomials); [Nearby monic-factor splitting (Lemma 3.2)](../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#3-unique-factorization); [Bounded-degree relations (Lemma 2.2)](../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#2-oka-s-coherence-theorem). Keep the zero-order factor and the unit quotient. Nearby splitting does not require the surrounding unique-factorization theorem.
6. Finish the dimension induction. [Oka coherence (Theorem 2.1)](../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#2-oka-s-coherence-theorem). Coherence on the lower-dimensional base supplies finite generators for the coefficient system on a common neighbourhood. Noetherian stalks alone would not justify this step.
7. Pass from stalk data to one neighbourhood. [Stalk injectivity persists (01C0)](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/modules.html#modules-lemma-finite-type-to-coherent-injective-on-stalk); [Extension of a specified finite free resolution (Corollary 3.3)](../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#3-the-category-of-coherent-analytic-sheaves). The source must be of finite type and the target coherent. The existing direct finite-resolution proof and regular-local alternative are retained.

The external Stacks/AI Integrated Stacks text retains its own licence notices and human/AI provenance; it is cited, not included or relabelled CC0. Native source revision 29a05ca0 and English reader revision 00e21940 are distinct. Only the selected statements and used arguments were compared. The ordinary reader links are for navigation, not immutable edition identifiers.

[Exact native modules source](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/29a05ca0ba1328874b7aae53301e09c9bbbbaf7b/modules.tex) · [Exact English reader source](https://raw.githubusercontent.com/KokunoYumeto/stacks-zh-hans-cn/00e219403ad0d07f04fa6563fc39fc761e365c72/en/modules.html) · Machine-readable Oka input records.

## Cohomology, base change, formal functions and duality

### AG-QC-01: Leray spectral sequence

Any morphism of ringed spaces and any module sheaf in degree zero; first quadrant, finite filtration in every total degree. No finite dimension, separation or properness assumption.

[Read Theorem 4.1 and its proof](cohomology-of-sheaves-on-ringed-spaces.html#AG-QC-01-Leray). Section 4; current sheaf-operations course, derived pullback and pushforward, Proposition 3.1 and Exercise 3.

Editable source: [cohomology-of-sheaves-on-ringed-spaces.md](src/cohomology-of-sheaves-on-ringed-spaces.md). SHA-256: `90c34f08aa0b7cf16ac7ba2bf950f049a8458df6c45feff866231af50780b977`.

### AG-QC-03: Affine quasi-coherent vanishing

Every ring R and every R-module M; H^p(Spec R, tilde M)=0 for p>0. No Noetherian or finite-generation assumption.

[Read Theorem 2.2 and its proof](affine-cohomology-and-serres-criterion.html#AG-QC-03-affine-vanishing). Lemma 2.1 and Theorem 2.2; Čech lesson, Theorem 4.1.

Editable source: [affine-cohomology-and-serres-criterion.md](src/affine-cohomology-and-serres-criterion.md). SHA-256: `9113f6aa822a41c9f58e454bf0a86e0e440f71ccee048c2cf94cae34685af2db`.

### AG-QC-03: Serre’s affine criterion

X quasi-compact; affineness is equivalent to vanishing of all positive quasi-coherent cohomology, and to H^1(X,I)=0 for every quasi-coherent ideal. The statement does not require quasi-separatedness.

[Read Theorem 5.2 and its proof](affine-cohomology-and-serres-criterion.html#AG-QC-03-Serre-affineness). Lemma 5.1 and Theorem 5.2; affine vanishing in Theorem 2.2.

Editable source: [affine-cohomology-and-serres-criterion.md](src/affine-cohomology-and-serres-criterion.md). SHA-256: `9113f6aa822a41c9f58e454bf0a86e0e440f71ccee048c2cf94cae34685af2db`.

### AG-QC-05: Serre’s theorems on projective space

R Noetherian, F coherent on P_R^N; finite cohomology, eventual higher-twist vanishing and eventual global generation.

Read Theorem 2.1 and its proof. Proposition 1.2; descending induction in Theorem 2.1; preceding projective-space lesson, Theorem 2.2.

Editable source: serres-theorems-on-projective-schemes.md. SHA-256: `ddac40fd2bf24adfb7184702da4b3adcf5596f2739bbd9fb2d81bf9941f3f116`.

### AG-QC-05: Serre’s theorems for a proper scheme with an ample line bundle

X proper over a Noetherian affine base R, F coherent and L ample; finiteness, and vanishing and global generation for every sufficiently large integer twist. Thresholds on a merely locally Noetherian non-quasi-compact base are only local.

Read Theorem 2.2 and its proof. Lemma 1.3 proves the closed embedding; Theorems 2.1–2.2, with the finite residue-class argument.

Editable source: serres-theorems-on-projective-schemes.md. SHA-256: `ddac40fd2bf24adfb7184702da4b3adcf5596f2739bbd9fb2d81bf9941f3f116`.

### AG-QC-08: Flat base change

f quasi-compact and quasi-separated, F quasi-coherent, g flat; every higher direct-image comparison is an isomorphism. F need not be flat. Includes localization and nonseparated X.

[Read Theorem 2.1 and its proof](base-change-and-the-grothendieck-complex.html#AG-QC-08-flat-base-change). Section 1 constructs the canonical map; Section 2 proves the separated case and the finite spectral-sequence comparison for quasi-separated X.

Editable source: [base-change-and-the-grothendieck-complex.md](src/base-change-and-the-grothendieck-complex.md). SHA-256: `d74a9c8c4789238fb8bea05cf6de26f0b2fb1df88a357b74cffec1d14243dcf8`.

### AG-QC-09: Fiber vanishing gives locally free H^0 and arbitrary base change

Noetherian base: f proper, F coherent and base-flat. Arbitrary base: f proper of finite presentation, F finitely presented and base-flat. All positive fiber cohomology vanishes at every point. Then f_*F is finite locally free, all positive higher direct images vanish, and both assertions commute with arbitrary base change. No reducedness is required. A line bundle on a flat proper finitely presented family satisfies the sheaf conditions.

[Read Corollary 5.3 and its proof](semicontinuity-and-grauerts-theorem.html#AG-QC-09-vanishing-local-freeness). Lemma 2.1 and Corollary 5.3 prove the fiber-vanishing case. Corollary 5.1 proves the higher-direct-image-vanishing case. Lesson 8 proves the Noetherian finite model; Lemma 0.1 in that lesson writes the general-base finite model, using the actual earlier finite-presentation and flatness arguments. Constant fiber dimension alone on a nonreduced base is insufficient; Theorem 4.1 assumes a reduced base.

Editable source: [semicontinuity-and-grauerts-theorem.md](src/semicontinuity-and-grauerts-theorem.md). SHA-256: `b6fdd5f794d77aedb97b216b27a9cea4edb61538afcd59cd21c715c64c6afac1`.

### AG-QC-10: Formal functions

A Noetherian, I any ideal, X proper over Spec A, F coherent; the canonical I-adic completed cohomology is the inverse limit of cohomology on X_n. F need not be flat and A need not be complete.

[Read Theorem 4.1 and its proof](the-theorem-on-formal-functions.html#AG-QC-10-formal-functions). Sections 2–4, especially Lemma 2.2, Proposition 3.1 and Theorem 4.1. Corollary 4.2 gives the locally Noetherian stalk form using lesson 8 localization.

Editable source: [the-theorem-on-formal-functions.md](src/the-theorem-on-formal-functions.md). SHA-256: `76e9b47b2804b9be424b617db2ebdb84b769242e95a81b488c08e2c29e88ddb3`.

### AG-QC-15: Cohen–Macaulay projective Serre duality

X projective over a field k, Cohen–Macaulay and equidimensional of dimension n, F coherent; Ext_X^(n-i)(F,omega_X) is naturally dual to H^i(X,F), for every integer i. For a smooth projective equidimensional curve and invertible L this gives H^1(L)^vee=H^0(omega_X tensor L^-1). No non-Cohen–Macaulay sheaf-duality extension is asserted.

Read Theorem 4.2 and its proof. Sections 2–4; local Ext vanishing, ambient projective-space duality from lesson 14 and Theorem 4.2. Local algebra inputs are recorded separately.

Editable source: dualizing-sheaves-and-serre-duality-for-projective-schemes.md. SHA-256: `2eb5d75cf6789870a3868831c7e701c12ab4033a8f6122f3937cb945e1ad5223`.

## Analytic proof inputs

The analytic bridge, *Complex analytic spaces and coherent sheaves*, supplies the following programme proof locations. It was written and self-checked by Claude Opus 5.5. GPT-6 Astra (OpenAI), Codex, Ultra, compared the linked statements and their uses here and integrated the routes. This is not a certification of all prerequisites or a full independent review of either course.

- **Coherence of holomorphic functions on every complex manifold, including kernel coherence.** [Coherent sheaves and Oka's theorem, Theorem 2.1 and Section 3](../complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem.html#2-oka-s-coherence-theorem). Used in lesson 17, Sections 1 and 5, and throughout lesson 18.
- **The analytic Nullstellensatz for every ideal in a convergent local ring.** [Analytic germs, local parametrization and the Nullstellensatz, Theorem 5.1](../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#5-the-nullstellensatz-and-dimension). Used in lesson 17, Sections 1 and 3.
- **Coherence of analytic vanishing ideals, including singular subsets.** [Cartan's coherence theorem and complex spaces, Theorem 1.1](../complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces.html#1-the-ideal-sheaf-of-an-analytic-set). Used in lesson 17 and in the ideal-algebraization argument of lesson 18.
- **Vanishing in all positive degrees for every coherent analytic sheaf on a complex manifold with a smooth strictly plurisubharmonic exhaustion.** [Theorems A and B on Stein manifolds, Theorem 4.1](../complex-analytic-spaces-and-coherent-sheaves/theorems-a-and-b-on-stein-manifolds.html#4-theorem-b). Used for the projective affine-chart intersections in lesson 18, Sections 1–2. The scope is not limited to vector bundles.
- **Finite dimensionality in every degree for coherent cohomology on compact complex spaces.** [Finiteness on compact complex spaces, Theorem 2.1](../complex-analytic-spaces-and-coherent-sheaves/finiteness-on-compact-complex-spaces.html#2-the-finiteness-theorem). Used in lesson 18, Sections 1 and 5. Its proof is analytic and does not assume algebraization of the sheaf.

Two more local analytic tools have exact locations: [finite parametrization, Theorem 4.1, and dimension, Theorem 5.4](../complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz.html#4-the-local-parametrization-theorem), used in lesson 17; and [unique factorization of holomorphic germs, Theorem 3.1](../complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html#3-unique-factorization), used for hypersurfaces in lesson 18, Exercise 7.3.

### Reading order for the analytic comparison

1. Read the scalar [Cauchy integral theorem and formula, Theorems 2.2–2.3](../foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html#OA-FND-CT-02), its [compact-rectangle integration tools, Lemma 0.1](../foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html#OA-FND-CT-07), and its [power-series and isolated-zero proofs, Section 3](../foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html#OA-FND-CT-03). Then read the bridge's iterated Cauchy integrals and Taylor expansions, followed by preparation and division in [lesson 17, Section 2](complex-analytic-spaces-and-analytification.html#2-local-analytic-algebra). That section proves the parameter-dependent root count by finite Taylor factorization and Cauchy integration, including multiplicities. It does not use GAGA or the coherence results listed in lesson 17, Section 1.
2. Read the bridge's local-ring, coherence, finite-parametrization and Nullstellensatz proofs. Return to lesson 17, Sections 3–5, for analytification and faithful flatness.
3. Read Laurent series and homogeneous projections: the annulus theorem, product expansions, extension of specified negative-power parts, and the signed homogeneous complex. Its one-variable argument builds on the scalar Cauchy proof above. Lebl's adapted contribution and the identified AI extensions retain CC BY-SA 4.0 in that separate teaching unit.
4. With the earlier sheaf-cohomology lessons, read the bridge's differential and analytic estimates, Fréchet-space arguments, vanishing and finiteness. Then read lesson 18. Its comparison theorem is a consumer of those results, not a premise of their proofs.

The exact source identities, theorem scopes and consumer locations are recorded in the prerequisite record. The referenced courses retain their own authorship and component terms.

## Additional prerequisite boundaries

The dimension-sensitive results in lesson 1 and lesson 10 use the exact Noetherian topological proof linked above. The arbitrary-base finite-presentation extension in lesson 9 is proved in its Lemma 0.1, including properness descent and the finite-cover passage from pointwise eventual flatness to one stage. Local algebra providers and their hypotheses are bound in the prerequisite record. Basic scheme constructions are identified where used; a planned lesson does not count as an available proof.

The scalar Cauchy and power-series providers above supply the inputs to the bridge's iterated Cauchy and Taylor arguments. Lesson 17 gives the full contour root count used in preparation. The Laurent teaching unit supplies the full product convergence, coordinate-extension and contraction arguments used in lesson 18, Lemma 2.1. Other core inputs used later in the bridge, including one-variable extension and Arzelà–Ascoli, are not certified by this bounded integration; complete recursive proof closure is not asserted here. Lesson 17 now constructs full-ideal analytification for locally finite type schemes, proves the reducedness comparison and faithful flatness, and detects finite algebraic isomorphisms. Lesson 18 proves the three projective GAGA assertions with nilpotents, then gives projective direct-image comparison, proper cohomological comparison, Ext comparison, uniform support annihilation and coherent algebraization for every proper complex scheme in Lemma 6.4 through Theorem 6.11. Lesson 11 supplies the arbitrary-base Stein construction in Appendix A and Theorem6.1. Lesson 16 supplies compact generation, Brown, proper locality and compactification comparison. Its Appendix N writes the full Noetherian Nagata construction, including nilpotents and a nonaffine base; the affineness-descent support it uses has a written proof in earlier lessons, and the conductor support is given in lesson 10, Appendix Z; its lower algebraic prerequisites are not proved in this course. Lesson 10, Lemma 0.1, supplies its previously missing polynomial-normality proof for every normal domain. These are local written arguments whose recursive prerequisites still require clearance. The earlier analytic bridge also has unresolved recursive proof and exact-free-citation checks.

See [the machine-readable providers](PROVIDER_HANDOFF.json) and [result locations](RESULTS.json).

Lesson 10, Appendix Z, contains the full conductor-coefficient and strong-transcendence support used by the earlier algebraic Zariski Main proof. Its normal-domain step uses the locally proved Lemma 0.1. The lower regular-local, dimension and flatness-slicing prerequisites are not proved in this course.
