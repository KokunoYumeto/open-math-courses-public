# SH02-PREREQ-OPEN — Open prerequisites and exact import contracts

Local identifier: `SH02-PREREQ-OPEN`.

Let $k$ be a commutative ring with identity and let $k_X$ be its constant sheaf on a topological space $X$. The foundations below apply to all $k_X$-modules. They impose no constructibility, rank, field, compactness, or finite global-dimension condition. A later theorem may impose additional hypotheses; its statement must retain them. We use cohomological grading, so $H^i(K[n])=H^{i+n}(K)$.

The assigned advanced theory has its own baseline: the coefficient ring has finite global dimension, manifolds are finite dimensional and countable at infinity, and submanifolds may be locally closed. Individual constructions can have more general ambient spaces or derived-category ranges; their own statements govern their use.

Each statement records the hypotheses under which its comparison map or derived operation is used. The supporting proofs include finite-sum and scalar-germ calculations, the full bounded-below hypercohomology construction and its natural edge, proper-fibre comparisons and proper base change for arbitrary topological spaces, ordinary internal Hom and projection/base-change diagrams. Each contract below links its programme proof at the stated scope. The external references remain as mathematical credit and further reading; they do not replace those proofs.

## Sheaves and derived operations

### SH02-IMP-ABELIAN — Exactness of module sheaves

For a ringed space, its module sheaves form an abelian category; exactness is detected on all stalks. Apply this with structure sheaf $k_X$. [Stacks, Tag 01AG](https://stacks.math.columbia.edu/tag/01AG)

The programme proof is *Sheaves of modules on a ringed space*, Theorem 2.1, using the sheafification and stalk arguments in Lemmas 1.1–1.3. It works for arbitrary topological spaces and sheaves of associative unital rings, so it applies in particular to the constant-ring case here.

### SH02-IMP-COLIMITS — Limits, colimits and stalks

Limits and colimits of module sheaves exist; stalks preserve colimits and filtered colimits are exact. Infinite coproduct sections need not be the coproduct of sections. [Tag 01AH](https://stacks.math.columbia.edu/tag/01AH)

For the full construction, use *Sheaves of modules on a ringed space*, Theorem 3.1: it constructs all small limits and colimits, identifies stalks and proves filtered exactness. Its Exercise 5 with solution exhibits the failure of infinite coproduct sections to commute over every nonzero coefficient ring. No finite-rank or field hypothesis enters this contract.

### SH02-IMP-INVERSE — Exact inverse image

For every continuous $f:X\to Y$, inverse image on $k$-module sheaves is exact and $(f^{-1}F)_x=F_{f(x)}$. [Tags 01AJ](https://stacks.math.columbia.edu/tag/01AJ), [008O](https://stacks.math.columbia.edu/tag/008O)

The canonical stalk and scalar identifications, exactness and composition are proved in *Sheaves of modules on a ringed space*, Theorem 4.1(1)–(3). This is the exact inverse-image functor for constant coefficients; pullback between unrelated structure sheaves can also require extension of scalars.

### SH02-IMP-INJECTIVE — Injective resolutions

Module sheaves on any ringed space have enough injectives, with functorial injective embeddings. [Tag 01DI](https://stacks.math.columbia.edu/tag/01DI)

A complete construction is *Injective modules and bounded-below derived functors*, Lemmas 2.1–2.2 and Theorem 2.3. The proof constructs character-module injectives, embeds each module into their product, and uses the skyscraper adjunction, Lemma 5.2, at all points, to embed a module sheaf into a product of injectives. The points need not be closed. Functoriality here means functorial embeddings; it does not assert that the embedding functor is additive or that these embeddings are injective hulls.

### SH02-IMP-DERIVE — Right derived functors

For an abelian category $\mathcal B$, a left exact additive functor from module sheaves to $\mathcal B$ has a right derived functor on $D^+$. In particular this constructs $Rf_*$ and $R\Gamma$. [Section 20.3, Tag 0716](https://stacks.math.columbia.edu/tag/0716)

The programme construction is *Injective modules and bounded-below derived functors*, Theorem 4.1. It applies to an abelian source with enough injectives and any abelian target, with no enough-injectives condition on the target. The finite-stage construction and homotopy comparison produce the right derived functor on bounded-below complexes and its natural degree-zero identification for a left exact functor. Direct image and sections are left exact because their kernels are computed on sections; thus the theorem applies to both operations displayed here.

### SH02-IMP-KINJECTIVE — Unbounded right derived constructions

On a ringed space, every complex admits a functorial quasi-isomorphism to a K-injective complex with injective terms, and that map is injective in each degree. K-injective resolutions define $Rf_*$ and $R\Gamma$ on unbounded derived categories. This is [Tag 079P](https://stacks.math.columbia.edu/tag/079P) applied through [Section 20.28, Tag 079V](https://stacks.math.columbia.edu/tag/079V).

The category hypothesis is explicit: module sheaves are abelian, have exact filtered colimits, and have generator $\bigoplus_{U\subset X}j_{U!}\mathcal O_U$, where $U$ runs through the set of open subsets. A nonzero morphism is detected by a local section, which is a morphism out of one such open generator. This is the same K-injective import used in `SH02-UR-IMPORTS` of the unbounded range bridge. An unbounded complex of injectives need not itself be K-injective, and this existence statement asserts no bounded output.

The programme construction is *K-injective resolutions in Grothendieck abelian categories*, Theorem 4.1, with the sheaf-category hypotheses proved in its Proposition 1.1 and the size and extension lemmas proved in §§2–3. Theorem 5.1 constructs the unbounded right derived functors. The resolution is functorial and termwise monic, and its terms are injective.

### SH02-IMP-KFLAT — Flat resolutions

Every complex of module sheaves has a termwise surjective quasi-isomorphism from a K-flat complex with flat terms. [Tag 06YF](https://stacks.math.columbia.edu/tag/06YF)

See *Flat modules and K-flat resolutions*, Theorem 3.1. Its local cycle-attachment construction produces both the degreewise epimorphism and the K-flat resolution with flat terms, on arbitrary topological spaces with commutative unital coefficient sheaves.

### SH02-IMP-TENSOR — Derived tensor

Derived tensor exists on the unbounded derived category of module sheaves. Bounded output is a separate question. [Tag 06YH](https://stacks.math.columbia.edu/tag/06YH)

The unbounded bifunctor, its action on morphisms and its resolution independence are proved in *The derived tensor product and Tor sheaves*, §§1–2, especially Theorem 2.2. The proof uses K-flat models and direct-sum totalization, without a finite global-dimension or bounded-output hypothesis.

### SH02-IMP-PULLBACK-TENSOR — Pullback and tensor

Derived pullback exists, respects composition and derived tensor. For the constant-ring morphism it is $f^{-1}$. [Tags 06YJ](https://stacks.math.columbia.edu/tag/06YJ), [0D5S](https://stacks.math.columbia.edu/tag/0D5S), [079U](https://stacks.math.columbia.edu/tag/079U)

See *Derived pullback and pushforward*, Theorem 1.1 and Proposition 1.2 for the unbounded construction, coherent composition and tensor compatibility on arbitrary commutative ringed spaces. For $k_X\simeq f^{-1}k_Y$, exactness of $f^{-1}$ carries a K-flat resolution $P\to G$ to a quasi-isomorphism $f^{-1}P\to f^{-1}G$, giving the natural identification $Lf^*G\simeq f^{-1}G$.

### SH02-IMP-ADJUNCTION — Pullback adjunction

On arbitrary ringed spaces, $Lf^*$ is left adjoint to $Rf_*$, including unbounded derived categories. [Tag 079W](https://stacks.math.columbia.edu/tag/079W)

The full unbounded adjunction is proved in *Derived pullback and pushforward*, Lemma 2.1 and Theorem 2.2. The proof compares maps from a K-flat model to the pushforward of a K-injective model, without assuming that this pushforward is itself K-injective. It constructs the natural adjunction on all derived morphisms and verifies its unit and counit. The spaces are arbitrary; no flatness or boundedness is imposed. Corollary 2.3 gives the exact unchanged-coefficient specialization \(f^{-1}\dashv Rf_*\).

### SH02-IMP-RHOM — Internal derived Hom

Internal derived Hom exists, satisfies tensor–Hom adjunction, and commutes with open restriction. [Tags 08DH](https://stacks.math.columbia.edu/tag/08DH), [08DJ](https://stacks.math.columbia.edu/tag/08DJ), [08DL](https://stacks.math.columbia.edu/tag/08DL)

The specialization for inverse image uses the canonical isomorphism $f^{-1}k_Y\simeq k_X$, detected on stalks. The stalk identification is $k$-linear because it takes a represented germ to the same germ and thus commutes with addition and scalar multiplication. Consequently the additional extension of scalars in ringed-space pullback is an identity. This is why the exactness statement applies to arbitrary $k$-modules; general pullback between unrelated structure sheaves is only right exact.

The construction is *Hom complexes, internal derived Hom and Ext sheaves*, Lemma 2.1 and Theorem 2.2, and its Theorem 3.1 proves the internal and external tensor–Hom adjunctions. These proofs apply to unbounded complexes on any commutative ringed space. Hom totalization uses products; tensor totalization uses direct sums. Open restriction preserves the K-injective models used for the construction, giving the stated restriction isomorphism.

## Localization and morphisms

### SH02-IMP-FLABBY — Acyclic injective resolutions

Injective module sheaves on a ringed space are flabby, and flabby module sheaves have zero higher direct images for every morphism of ringed spaces. This combines the exact statements of [Tag 09SX](https://stacks.math.columbia.edu/tag/09SX) and [Tag 09T0](https://stacks.math.columbia.edu/tag/09T0). Apply them to the constant structure sheaves $k_X$ and $k_Y$. No condition on the coefficient ring or the topology is added. This does not say that restriction of an injective sheaf to an arbitrary closed subset is injective.

For a complete proof use *Injective modules, flasque sheaves and bounded-below derived functors*, Lemmas 1.1–1.2 and Proposition 1.3. The extension-by-zero adjunction proves that injectives are flabby, and gluing lifts across a flabby kernel proves acyclicity for sections on every open and for every direct image. The proof permits arbitrary topology and sheaves of associative unital rings. It proves acyclicity of the individual sheaves asserted here; it does not say that every unbounded complex of flabby sheaves computes a derived functor without an additional argument.

### SH02-IMP-HYPERCOH — Bounded-below hypercohomology

For $K\in D^+(k_X)$ there is a convergent spectral sequence

\[
E_2^{p,q}=H^p(X;H^q(K))\Longrightarrow H^{p+q}R\Gamma(X;K).
\]

The bounded-below hypercohomology proof constructs this spectral sequence from good truncations and proves finite convergence in each total degree. It applies to any topological space and arbitrary $k$-module sheaves. If the cohomology sheaves are acyclic for global sections, its canonical truncation edge is an isomorphism from hypercohomology to sections of the cohomology sheaf. The same proof checks compatibility with the section-to-germ map used on open stars. For further reading, this is the constant-ring instance of [Stacks, Tag 0BKM](https://stacks.math.columbia.edu/tag/0BKM).

### SH02-IMP-OPEN-ZERO — Extension by zero

For an open inclusion $j:U\hookrightarrow X$, extension by zero is exact. The stalk formula underlying [Tag 01AK](https://stacks.math.columbia.edu/tag/01AK) also applies to $k$-module sheaves: the stalk is the original stalk on $U$, and zero elsewhere. This is `SH02-IMP-OPEN-ZERO`.

The sheaf construction, stalk formula, exactness and adjunction are proved in *Sheaves of modules on a ringed space*, Lemma 5.1. Sections over an open \(V\) are sections on \(U\cap V\) whose support is closed in \(V\). This gives the original stalk on \(U\) and zero outside \(U\), on arbitrary topological spaces and for arbitrary associative unital coefficient sheaves.

### SH02-IMP-LOCALIZATION — Closed supports

For a closed subset $Z\subset X$ with complement $j:U\hookrightarrow X$, [Tag 0G72](https://stacks.math.columbia.edu/tag/0G72) gives, for arbitrary $F\in D(k_X)$, the functorial triangle

\[
R\Gamma_ZF\longrightarrow F\longrightarrow Rj_*j^{-1}F
\longrightarrow (R\Gamma_ZF)[1].
\]

Here $R\Gamma_ZF$ means the **sheaf** of derived sections supported in $Z$, namely the object denoted $i_*R\mathcal H_Z(F)$ in that reference. This is `SH02-IMP-LOCALIZATION`; it is distinct from global cohomology with support.

The fully unbounded triangle, including its canonical maps and connecting sign, is *Sections with support and the localization triangle*, Theorem 2.1. Its Proposition 1.1 identifies the sheaf support functor as \(i_*R\mathcal H_Z\). A K-injective resolution with injective terms gives a termwise exact localization sequence; open restriction preserves K-injectives, so its third term computes \(Rj_*j^{-1}F\). The proof works on arbitrary spaces with associative unital coefficient sheaves and unchanged coefficients on the closed subset.

### SH02-IMP-HOM-COMPOSITION — Composition

For $A,B,C\in D(\mathcal O_X)$, the internal derived Hom composition is

\[
R\mathcal{H}om(B,C)\otimes^L R\mathcal{H}om(A,B)
\longrightarrow R\mathcal{H}om(A,C).
\]

This is the map of [Tag 0A8V](https://stacks.math.columbia.edu/tag/0A8V): it is the transpose of evaluating first into $B$ and then into $C$. Threefold composition is associative, the transpose of the identity is the unit, and the middle-variable compatibility is dinatural. The supporting verification identifies this actual map on complexes, checks the signs and variance, and proves its compatibility with the pullback comparison below. These are ordinary internal-Hom identities; microlocal composition remains separate.

The evaluation transpose, associativity, unit and middle-variable dinaturality are proved in *Hom complexes, internal derived Hom and Ext sheaves*, Proposition 4.1, with the chain signs established in Lemma 1.1 and the unbounded closed structure in Theorem 3.1. DF-E and DF-F of the supporting proofs identify the same map and its compatibility with pullback. No microlocal composition theorem is used.

### SH02-IMP-HOM-PULLBACK — Pullback comparison

We import the comparison

\[
Lf^*R\mathcal{H}om(K,L)\longrightarrow
R\mathcal{H}om(Lf^*K,Lf^*L)
\]

from [Tag 08I3](https://stacks.math.columbia.edu/tag/08I3). This is a morphism, without an unconditional isomorphism claim. Neither it nor the composition import constructs microlocal Hom.

The supporting proof DF-F constructs this morphism as the unique transpose of pulled-back evaluation, using the unbounded tensor–Hom adjunction and the monoidal pullback comparison. Equations DF-PULL-COMP, DF-PULL-UNIT and DF-PULL-ITERATE prove compatibility with composition, identities and iterated pullback. The comparison is an isomorphism for open restriction; DF-F also gives a one-point ring example showing why a general isomorphism cannot be claimed.

## Properness and the projection formula

### SH02-IMP-PROPERNESS — The topological convention

For a continuous map of topological spaces, proper means separated and universally closed. Universal closedness is equivalent to being closed with quasi-compact fibres, by [Section 5.17, Tag 005M](https://stacks.math.columbia.edu/tag/005M) and [Tag 005R](https://stacks.math.columbia.edu/tag/005R). For locally compact Hausdorff spaces this agrees with compact inverse images of compact subsets. The programme proof, Lemmas 2–3, proves the equivalence with a closed map and quasi-compact fibres, proves preservation of quasi-compactness under inverse image, and checks the locally compact Hausdorff convention. Compact fibres alone do not establish properness.

### SH02-IMP-PROPER-BASECHANGE — Proper base change

This contract concerns a cartesian square with maps $f:X\to Y$, $g:Y'\to Y$, $f':X'\to Y'$, and $g':X'\to X$. If $f$ is proper and $E\in D^+(k_X)$, the canonical map is

\[
g^{-1}Rf_*E\longrightarrow Rf'_*(g')^{-1}E,
\]

and it is an isomorphism. [Tag 09V6](https://stacks.math.columbia.edu/tag/09V6) states this for abelian sheaves, with the comparison constructed in [Tag 02N7](https://stacks.math.columbia.edu/tag/02N7). The topological convention is `SH02-IMP-PROPERNESS`. Tag 02N7 requires both horizontal ringed-space maps to be flat; here each local structure-ring map is the identity $k\to k$, so both flatness hypotheses hold.

The coefficient specialization has a short verification. Forgetting the $k$-action is exact and detects quasi-isomorphisms. A bounded-below injective resolution in $k_X$-modules is a complex of flasque abelian sheaves by [Tag 09SX](https://stacks.math.columbia.edu/tag/09SX); its terms are acyclic for direct image by [Tag 09T0](https://stacks.math.columbia.edu/tag/09T0). It therefore computes the same $Rf_*$ after forgetting scalars, and similarly for $f'$. Inverse image and the adjunction maps retain their underlying abelian-sheaf maps. Thus the $k$-linear base-change morphism forgets to the isomorphism in Tag 09V6 and is itself an isomorphism. No flatness of $k$ over the integers is needed.

The general topological proper-base-change proof, GP1–GP13, supplies a complete programme route for the full statement above. It proves compactness and ambient point separation of fibres, gluing of section germs around compact subsets, acyclicity of restricted injectives, and the fibre formula with its canonical restriction map. The chain identity GP13 identifies the resulting isomorphism with the canonical derived adjunction comparison. Fibres need not be closed in their source, and no Hausdorff or local compactness assumption on the ambient spaces is used. The locally compact Hausdorff proof remains an alternative route for compact convex spaces and manifolds.

### SH02-IMP-PROJECTION-PERFECT — The perfect projection formula

The contract is the isomorphism

\[
Rf_*E\otimes^{L}K\longrightarrow
Rf_*(E\otimes^{L}Lf^*K)
\]

for a morphism of ringed spaces, $E\in D(\mathcal O_X)$, and **perfect** $K\in D(\mathcal O_Y)$, from [Tag 0B54](https://stacks.math.columbia.edu/tag/0B54). 

The map and its invertibility are proved in *The projection formula and the base change map*, Theorem 2.1. The proof defines projection by the derived counit, proves the finite locally free case, and passes to local strictly perfect models by finite filtrations and direct summands. It allows unbounded \(E\), arbitrary topological spaces and arbitrary commutative unital structure sheaves. Perfection is local; no single global degree bound on its local models is required.

### SH02-IMP-PROJECTION-CLOSED — A closed embedding

This contract permits arbitrary $K$ when $f$ is a homeomorphism onto a closed subset, by [Tag 0B55](https://stacks.math.columbia.edu/tag/0B55). The general comparison exists without these assumptions, but its invertibility requires justification.

See *The projection formula and the base change map*, Theorem 3.1. For a homeomorphism onto a closed subset, direct image is exact and commutes with arbitrary coproducts by its stalk formula. The stalkwise scalar-extension identity, applied to a K-flat model, gives the projection isomorphism for arbitrary unbounded \(E\) and \(K\). The proof identifies it with the counit-defined projection map; it requires no flatness or isomorphism of the structure-ring map.

### SH02-IMP-BASECHANGE-MORPHISM — The general comparison map

For any commutative square of ringed spaces with the labels above and $E\in D(\mathcal O_X)$, there is a canonical morphism

\[
Lg^*Rf_*E\longrightarrow Rf'_*L(g')^*E.
\]

It is the mate, under $L(f')^*\dashv Rf'_*$, of $L(g')^*$ applied to the counit $Lf^*Rf_*E\to E$, using $L(f')^*Lg^*\simeq L(g')^*Lf^*$. This is [Tag 08HY](https://stacks.math.columbia.edu/tag/08HY). Its existence requires neither a cartesian square, flatness nor properness, and gives no general isomorphism.

The mate construction, its naturality and its compatibility with pasting are proved in *The projection formula and the base change map*, Theorem 4.1. Equations (4.2)–(4.3) give the canonical comparison for any commutative square of ringed spaces and all unbounded inputs. Flatness is imposed only in the separate calculation with ordinary horizontal pullbacks, not in the construction of the general derived comparison.

### SH02-IMP-PROJECTION-COMPATIBILITY — The comparison diagram

For the same square, $E\in D(\mathcal O_X)$ and $K\in D(\mathcal O_Y)$, projection and base-change maps give two morphisms from

\[
Lg^*(Rf_*E\otimes^L K)
\quad\hbox{to}\quad
Rf'_*(L(g')^*E\otimes^L L(f')^*Lg^*K).
\]

They are equal. The first applies projection before base change, then the pullback tensor and composition isomorphisms. The second first distributes $Lg^*$ over tensor, applies base change to the first factor, and finally applies the projection map for $f'$. Tensor products inside $Rf'_*$ are over $\mathcal O_{X'}$. This is the compatibility in [Section 20.54, Tag 01E6, Remark 20.54.5](https://stacks.math.columbia.edu/tag/01E6). The supporting proof applies the adjunction bijection to both routes: each mate is pulled-back counit $L(g')^*Lf^*Rf_*E\to L(g')^*E$, tensored with the identity of the other factor. It thereby supplies the verification omitted in that remark. Invertibility of the comparison maps is unnecessary for this equality.

A complete verification is *The projection formula and the base change map*, Theorem 4.1, projection compatibility, also given in supporting proof E7. Transposing both routes under \(L(f')^*\dashv Rf'_*\) gives the same pulled-back counit tensored with the identity, with the coefficient and pullback-composition identifications retained. This proves equality for unbounded \(E,K\) and any commutative square, without requiring either comparison to be invertible.

The full $Rf_!$ base-change and projection formulas for nonproper manifold maps, composition with proper support, $f^!$, orientation and duality, conic descent, Fourier–Sato inversion, specialization, and microlocal Hom are separate SH-02 obligations. Their proofs cannot invoke the preceding $Rf_*$ statements after merely replacing a star with an exclamation mark. Likewise the existence of operations on $D$ does not prove preservation of $D^b$.

## Antecedents and reuse

The Stacks Project's [license notice](https://raw.githubusercontent.com/stacks/stacks-project/a04446e57ec1fbc252a871afcec7752fb2807b14/introduction.tex) grants GFDL version 1.2 or any later version, with no invariant sections and no cover texts; its [license text](https://raw.githubusercontent.com/stacks/stacks-project/a04446e57ec1fbc252a871afcec7752fb2807b14/COPYING) is version 1.2. The linked references were checked on 2026-09-07. The [cited repository edition](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14) identifies the exact source and licence; individual live tag pages may reflect later revisions. This prerequisite text is dedicated under CC0 1.0 Universal.

The bounded supplementary comparison includes Pierre Schapira's [A short review on microlocal sheaf theory](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), especially its Fourier–Sato discussion, and Schnürer–Soergel's [Proper base change for separated locally proper maps](https://arxiv.org/abs/1404.7630). The first supplies relevant mathematical statements but omits the Fourier–Sato inversion proof; no adaptation license was identified on the checked note and landing page. The second has an arXiv nonexclusive distribution license, which is not an identified permission to adapt its exposition. We cite these as antecedents and do not import their text. Within these checked sources no adequate reusable complete conic unit has been identified; this is a bounded comparison, not a claim about all open literature.

