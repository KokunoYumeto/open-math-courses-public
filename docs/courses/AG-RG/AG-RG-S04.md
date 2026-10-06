# Affine descent, Zariski Main and recognition of spaces

This supporting lesson puts the actual arguments before the group-theoretic applications. Every base and test scheme is arbitrary unless the statement gives an additional hypothesis. A finite algebra is finite as a module; finite presentation is never silently imposed. A quasi-finite morphism is quasi-compact and locally quasi-finite. Locally quasi-finite spaces in block E need not be quasi-compact.

The proof order is P: elementary integral algebra; A: faithfully flat and quasi-affine descent; B: polynomial normality; C: the conductor argument and affine completion; D: the étale structural lemmas and general scheme Zariski Main; E: locally quasi-finite effectivity, finite quotients and scheme recognition. Labels retain their source section number with the block letter, so Lemma C3.2 and Theorem D5.2 have unambiguous positions. The recognition theorem never supplies an input to its own scheme-descent proof.

The earlier programme inputs are the full elementary field, integral-extension, affine/relative-Spec, quasi-finite-fibre and scheme-limit proofs, together with [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md).

*Copyright (C) 2005–2025 Johan de Jong. Adapted Stacks Project arguments retain the GNU Free Documentation License, version 1.2 or later, with no Invariant Sections, Front-Cover Texts or Back-Cover Texts. The complete [GNU Free Documentation License](assets/GFDL-1.2.txt) accompanies this edition. Original explanations retain their CC0 dedication. Source citations identify freely accessible writing and comparison material; none substitutes for a programme proof.*

## P. Elementary integral algebra before descent and completion

This block reconstructs the consumed elementary arguments from freely readable Stacks material. It supplies the proof itself; earlier private bibliography entries are not its mathematical sources. Localization, filtered colimits, Nakayama and the Noetherian polynomial argument have already been proved in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Section 1.

**Lemma P0.1 (prime separation and radicals).** If an ideal $I$ avoids a multiplicative set $S$, it is contained in a prime avoiding $S$. The radical of $I$ is the intersection of primes containing $I$.

**Proof.** A chain of ideals containing $I$ and avoiding $S$ has its union as an upper bound still avoiding $S$. Choose a maximal such ideal $J$ by Zorn. If $ab\in J$ with $a,b\notin J$, both larger ideals $J+(a)$ and $J+(b)$ meet $S$. Multiplying one chosen element from each gives an element of $S$ in $J$, a contradiction. Thus $J$ is prime. A power in $I$ lies in every prime over $I$. Conversely, if no power of $a$ lies in $I$, apply separation to $S=\{1,a,a^2,\ldots\}$ to obtain a prime over $I$ missing $a$. This proves the radical statement. Primes of a quotient correspond to primes containing its kernel; primes of a localization correspond to primes avoiding its denominators, since extension and contraction are inverse by the fraction equality test. These identifications preserve inclusion. $\square$

**Lemma P0.2 (finite integral control).** An element is integral over $R$ exactly when its generated algebra is finite as an $R$-module. Integral elements form a subalgebra, integrality is transitive, and an integral finite-type algebra is finite.

**Proof.** A monic degree-$d$ relation bounds all powers by $1,b,\ldots,b^{d-1}$. Conversely, on any finite module subalgebra containing $1$, write multiplication by $b$ on module generators as a matrix with coefficients in $R$. Its adjugate makes its monic characteristic polynomial annihilate every generator, hence $1$, so it annihilates $b$ in the algebra. For finitely many integral elements, the monomials whose exponents are below their relation degrees span their algebra. The preceding determinant argument makes every element of that algebra integral, proving closure under sums and products. For a monic relation over an integral intermediate ring, collect its finitely many coefficients. Their subalgebra is finite over the original ring; adjoining the element is finite over that subalgebra. Products of the two finite generating lists give finiteness over the original ring and hence integrality. This proves transitivity and the last assertion. A finite module algebra is of finite type and integral by the same argument. $\square$

**Lemma P0.3 (localization of integral closure).** For any $R$-algebra $B$, its integral subalgebra $C$ satisfies

$$
S^{-1}C=\{z\in S^{-1}B:z\text{ integral over }S^{-1}R\}.
$$

**Proof.** Divide a monic equation for $c$ by its leading denominator power to prove the forward inclusion. Conversely, take a monic equation for $z=b/s$. Choose a common product $v\in S$ of all coefficient denominators and $s$, so $c=vz$ is the image of an element of $B$ and has a monic equation $c^d+r_1c^{d-1}+\cdots+r_d=0$ with $r_i\in R$ in the localization. Some $h\in S$ kills its error in $B$. Then $hc$ satisfies the genuine monic equation

$$
(hc)^d+hr_1(hc)^{d-1}+\cdots+h^dr_d=0
$$

in $B$, since the left side is $h^d$ times that error. Thus $hc\in C$ and $z=(hc)/(hv)$. Exact localization identifies $S^{-1}C$ with its image in $S^{-1}B$. The zero localization is included. $\square$

**Lemma P0.4 (prime lifting and closed images).** An integral inclusion $R\subset B$ has lying over and going up. Distinct primes with equal contraction are incomparable. Integral maps of spectra are closed, also after every base change.

**Proof.** First, for integral domains $A\subset D$, one is a field exactly when the other is. If $A$ is a field, each nonzero $d$ acts injectively and hence surjectively on the finite-dimensional domain $A[d]$, so has an inverse. If $D$ is a field, a monic relation for $a^{-1}$, multiplied by $a^{d-1}$, puts $a^{-1}$ in $A$.

Localize an integral inclusion at $R\setminus\mathfrak p$ and choose a maximal ideal upstairs. Its contraction is maximal by the field assertion, so is the local base's unique maximal ideal. Contracting before localization gives lying over. Quotient by a prescribed prime upstairs and apply lying over to the quotient inclusion to obtain going up. A residue-field fibre algebra is integral over its field: monic equations survive quotient and localization. Every prime quotient is consequently a field. Its primes are all maximal, proving incomparability. For an arbitrary ideal $J\subset B$, apply lying over to $R/(J\cap R)\subset B/J$. Its image is $V(J\cap R)$, proving closedness. After any base change, elements from $B$ remain integral, and each tensor expression uses finitely many of them; Lemma P0.2 proves integrality of the new algebra. The same closed-image proof therefore applies. $\square$

**Lemma P0.5 (factorial and polynomial field rings).** A factorial domain is normal. If $k$ is a field, $k[T_1,\ldots,T_n]$ is factorial.

**Proof.** A fraction $a/b$ with no common irreducible factor satisfying a monic equation has $b\mid a^d$ after clearing denominators. Thus $b$ is a unit and the fraction belongs to the domain. For a factorial $R$, a product of primitive polynomials is primitive: reduction modulo an irreducible divisor of all product coefficients would contradict the domain property of $R/(p)$. Hence contents multiply. Clear denominators in a factorization over $\operatorname{Frac}R[T]$ and divide out contents. Two primitive polynomials differing by a fraction scalar differ by a unit: a reduced denominator must divide all coefficients, and then the numerator would divide the other content. The Euclidean factorization over the fraction field therefore gives existence and uniqueness of primitive factorization over $R[T]$, together with factorization of contents. This proves $R[T]$ factorial. Starting with a field and iterating proves the assertion. Euclidean factorization itself follows by dividing repeatedly into irreducibles; degrees decrease, and Bezout makes each irreducible prime, giving uniqueness. $\square$

**Lemma P0.6 (monic factors over a normal domain).** Let $R$ be normal with fraction field $K$. A monic factor $Q\in K[T]$ of a monic $F\in R[T]$ lies in $R[T]$. If all nonleading coefficients of $F$ lie in $I$, those of $Q$ lie in $\sqrt I$.

**Proof.** Adjoin the finitely many roots of $F$ to a splitting field. Every root is integral over $R$. The coefficients of $Q$ are elementary symmetric expressions in a sublist of those roots, counting repetitions. Lemma P0.2 makes them integral; they already lie in $K$, so normality puts them in $R$. Monic division puts the complementary factor in $R[T]$ too. Modulo each prime over $I$, their product is $T^{\deg F}$. Over that residue domain's fraction field its monic factors are powers of $T$. Thus every nonleading coefficient of $Q$ vanishes modulo every prime over $I$, and Lemma P0.1 gives membership in $\sqrt I$. In particular the minimal polynomial of an integral element over $K$ has coefficients in $R$. $\square$

**Lemma P0.7 (integral elements of an extended ideal).** In an integral algebra $B/R$, every $y\in IB$ satisfies a monic equation whose coefficient of degree $d-i$ belongs to $I^i$.

**Proof.** Express $y=\sum_j a_jb_j$ with $a_j\in I$. The algebra generated by the finitely many integral $b_j$ is finite over $R$ by Lemma P0.2. Multiplication by $y$ carries it into $I$ times itself. On finite module generators this multiplication is therefore expressed by a matrix with entries in $I$. In its monic characteristic polynomial the coefficient $i$ places below the leading term is a sum of products of $i$ entries, hence lies in $I^i$. The adjugate kills the module generators, and then its unit, giving the required equation for $y$ in $B$. $\square$

**Theorem P0.8 (going down over a normal domain).** For an integral inclusion of domains $R\subset B$ with $R$ normal, if $\mathfrak p\subset\mathfrak p'$ and $\mathfrak q'$ lies over $\mathfrak p'$, there is $\mathfrak q\subset\mathfrak q'$ lying over $\mathfrak p$.

**Proof.** We prove $\mathfrak pB_{\mathfrak q'}\cap R=\mathfrak p$. Write an element of the left side as $z=y/g$, with $y\in\mathfrak pB$ and $g\notin\mathfrak q'$. In the domain $B$, $zg=y$. Suppose $z\ne0$. The minimal polynomial of $g$ is $T^n+a_1T^{n-1}+\cdots+a_n$ with $a_i\in R$ by Lemma P0.6. Some $a_i$ misses $\mathfrak p$, since otherwise its equation puts $g^n$ in $\mathfrak q'$. The minimal polynomial of $zg$ is $T^n+za_1T^{n-1}+\cdots+z^na_n$, by invertible scaling in $K$. It divides a monic polynomial for $y$ with nonleading coefficients in $\mathfrak p$, supplied by Lemma P0.7. Lemma P0.6 gives $z^ia_i\in\mathfrak p$. The chosen $a_i$ forces $z\in\mathfrak p$. The case $z=0$ is immediate. Thus $\mathfrak pB_{\mathfrak q'}$ avoids $R\setminus\mathfrak p$. Prime separation, Lemma P0.1, gives a prime containing it and avoiding that set. Contracting from $B_{\mathfrak q'}$ gives the required prime inside $\mathfrak q'$. $\square$

**Lemma P0.9 (the field-algebra and zero-dimensional tests).** A field finitely generated as an algebra over $k$ is finite over $k$. A zero-dimensional Noetherian ring is Artinian, with finitely many local factors. In particular a finite-type zero-dimensional fibre algebra has finitely many points and finite residue fields.

**Proof.** In a field algebra choose a maximal algebraically independent sublist of its algebra generators. The other generators are algebraic over its rational function field. Invert one nonzero polynomial $g$ clearing their monic-equation denominators. The field is then finite integral over $k[t_1,\ldots,t_r,1/g]$, which must be a field by Lemma P0.4's field test. If $r>0$, choose an irreducible polynomial in $k[t_1]$ not dividing $g$. Such polynomials are infinite by the product-plus-one argument and factorization by degree; only finitely many divide the finitely many coefficients of $g$. Its principal prime remains proper after inverting $g$, a contradiction. Thus $r=0$, proving the field assertion.

A Noetherian ring has finitely many minimal primes. To prove this, choose by ACC an ideal maximal among those whose closed set is not a finite union of irreducible closed sets. That closed set is reducible, so is a union of two proper closed subsets, each a finite union by maximality, a contradiction. An irreducible closed set has prime radical: if $ab$ vanishes on it, its cover by $V(a)$ and $V(b)$ forces one of them to contain it. Thus the finite irreducible components give the finite minimal primes. In dimension zero these are all maximal and all primes. The nilradical is generated by finitely many nilpotents, so a sufficiently high power is zero by expanding monomials. Modulo it, the Chinese remainder map gives the product of the finitely many residue fields. Each successive nilradical-power quotient is a finite module over that field product, hence has finite length. The ring therefore has finite length and is Artinian. The same Chinese remainder argument using sufficiently high powers of the maximal ideals gives its finite product of local Artinian factors. Hilbert's basis theorem in S01 makes a finite-type fibre algebra Noetherian; the two assertions just proved finish the statement. $\square$

<a id="finite-torsion-free-lattices"></a>

**Lemma P0.10 (finite torsion-free lattices).** Every finitely generated torsion-free abelian group is isomorphic to \(\mathbb Z^r\) for a finite \(r\geq0\). Every subgroup of \(\mathbb Z^n\) is free of rank at most \(n\).

**Proof.** A nonzero subgroup \(J\subseteq\mathbb Z\) has a least positive element \(a\). Integer division of \(x\in J\) by \(a\) leaves a remainder in \(J\) between \(0\) and \(a-1\), so that remainder is zero. Hence \(J=a\mathbb Z\); the zero subgroup has rank zero.

Induct on \(n\), starting with \(\mathbb Z^0=0\). Project a subgroup \(H\subseteq\mathbb Z^n\) onto its last coordinate. If its image is zero, use induction inside \(\mathbb Z^{n-1}\). Otherwise its image is \(a\mathbb Z\) with \(a>0\); choose \(v\in H\) projecting to \(a\). For each \(h\in H\), subtract the unique multiple of \(v\) with the same last coordinate. Thus
\[
H=\mathbb Z v\oplus H_0,\qquad H_0=H\cap(\mathbb Z^{n-1}\times\{0\}).
\]
The sum is direct because a nonzero multiple of \(v\) has nonzero last coordinate. Induction gives a basis of \(H_0\), and adjoining \(v\) gives a basis of \(H\) with at most \(n\) elements.

Let now \(M\) be finitely generated and torsion-free. The localization obtained by inverting nonzero integers is \(\mathbb Q\otimes_{\mathbb Z}M\): the maps \((a/b)\otimes m\mapsto am/b\) and \(m/b\mapsto(1/b)\otimes m\) are inverse by the fraction and bilinear relations. The fraction equality test says that \(m/1=0\) precisely when a nonzero integer kills \(m\). Consequently \(M\) embeds in this rational vector space. A finite generating set spans it; discarding each vector in the span of its predecessors gives a finite basis, say of size \(s\). In these coordinates the finitely many generators have rational entries. Multiplying all coordinates by one common positive denominator embeds \(M\) in \(\mathbb Z^s\). The subgroup assertion just proved makes its image finite free. This also includes \(M=0\). \(\square\)

Freely readable proof material: the Stacks Project, [embedding finite torsion-free modules in free modules](https://stacks.math.columbia.edu/tag/0AUU) and [finite torsion-free modules over a principal ideal domain](https://stacks.math.columbia.edu/tag/0AUW), part (3). The complete integer case, including the splitting and fraction calculations used for character lattices, is proved above.

Freely readable comparison sources: the Stacks Project's [finite and integral extensions](https://stacks.math.columbia.edu/tag/00GH), [localization of integral closure](https://stacks.math.columbia.edu/tag/0307), [monic factors over a normal domain](https://stacks.math.columbia.edu/tag/00H6), [minimal polynomials](https://stacks.math.columbia.edu/tag/00H7), [integrality over an ideal](https://stacks.math.columbia.edu/tag/00H5), [going down](https://stacks.math.columbia.edu/tag/00H8), [finite-type field algebras](https://stacks.math.columbia.edu/tag/00FV), and [Noetherian zero-dimensional rings](https://stacks.math.columbia.edu/tag/00KH). These are writing and comparison sources; the complete arguments used by blocks A–E are supplied above.

## A. Faithfully flat and quasi-affine descent

### A1. Faithfully flat algebra, topology and maps

<a id="scheme-open-gluing"></a>
**Lemma A1.0 (gluing schemes along opens).** Let \((X_i)_{i\in I}\) be a set-indexed family of schemes. For every pair let \(X_{ij}\subset X_i\) be open, with isomorphisms \(\phi_{ij}:X_{ij}\to X_{ji}\). Assume \(X_{ii}=X_i\), \(\phi_{ii}=1\), \(\phi_{ji}=\phi_{ij}^{-1}\), and the precise triple conditions

\[
\phi_{ij}(X_{ij}\cap X_{ik})=X_{ji}\cap X_{jk},\qquad
\phi_{jk}\phi_{ij}=\phi_{ik}\quad\text{on }X_{ij}\cap X_{ik}.
\]

There is a scheme \(X\), with open embeddings \(X_i\to X\), having precisely these overlaps and identifications. Maps from \(X\) to any scheme are exactly compatible maps from the \(X_i\). The construction is unique up to its unique compatible isomorphism. Empty overlaps give arbitrary set-indexed disjoint unions.

**Proof.** Form the disjoint union of the underlying spaces and identify \(x\in X_{ij}\) with \(\phi_{ij}(x)\). The inverse and triple conditions make this an equivalence relation; a chain of identifications between two chosen pieces reduces to their specified direct identification. No two distinct points of one piece become identified. Give the quotient the quotient topology. The saturation of an open subset of one piece is a union of its images under the open identifications, hence is open in every piece. Thus each \(X_i\) embeds openly with its original topology, and its intersection with the image of \(X_j\) is exactly \(X_{ij}\).

For an open \(W\subset X\), define \(\mathcal O_X(W)\) to consist of tuples \((s_i)\), with \(s_i\in\mathcal O_{X_i}(W\cap X_i)\), whose restrictions agree under every \(\phi_{ij}\). Restrict tuples componentwise. A compatible family of these tuples on an open covering of \(W\) glues uniquely in each \(\mathcal O_{X_i}\); their overlap equalities persist by the sheaf uniqueness axiom. Hence \(\mathcal O_X\) is a sheaf of rings. On \(X_i\) the restriction is \(\mathcal O_{X_i}\): a section on that piece determines all its restrictions to the other pieces by the specified identifications. Therefore the stalk at a point of \(X_i\) is its original local ring. The quotient is a locally ringed space covered by open subspaces which are schemes, and the affine charts in the pieces make it a scheme by the definition of a scheme. Compatible morphisms on the pieces glue their continuous maps and sheaf maps, remain local on stalks, and give the asserted unique morphism. Applying this universal property in both directions proves uniqueness of the constructed scheme. \(\square\)

**Lemma A1.1 (the equalizer).** If $R\to A$ is faithfully flat, then for every $R$-module $M$ the sequence

$$
0\longrightarrow M\longrightarrow A\otimes_R M
\rightrightarrows A\otimes_R A\otimes_R M
$$

is exact, with the two arrows inserting a unit in the first or second $A$ position.

**Proof.** Tensor the augmented alternating unit-insertion complex with $A$. Regard the added factor as the coefficient ring. The new covering algebra is $A\otimes_R A$, and its multiplication map to $A$ is a retraction of its structure map. Applying that retraction to the first covering-algebra factor is a contracting homotopy: the term inserting a unit in that position gives the identity; every other insertion cancels the corresponding insertion after the homotopy, with opposite sign. The same formula in augmentation degree is a left inverse of the augmentation. Thus the tensored complex is exact. Flatness commutes with the kernels and cokernels computing its cohomology, and faithful flatness detects their vanishing. The original complex, and in particular the displayed beginning, is exact. Taking $M=R$ gives $R=\operatorname{Eq}(A\rightrightarrows A\otimes_R A)$. $\square$

**Lemma A1.2 (module and algebra effectivity).** An $A$-module with descent datum for a faithfully flat map $R\to A$ is uniquely the scalar extension of its invariant $R$-module. The same holds for algebras and compatible morphisms, without finite generation assumptions.

**Proof.** Use the convention that the datum is an $(A\otimes_R A)$-linear isomorphism

$$
\phi:N\otimes_R A\xrightarrow{\sim}A\otimes_R N.
$$

Put $\rho(n)=\phi(n\otimes1)$ and $M=\{n:\rho(n)=1\otimes n\}$. The cocycle and its diagonal restriction give

$$
\rho(an)=(a\otimes1)\rho(n),\qquad
\mu\rho(n)=n,\qquad
(1\otimes\rho)\rho(n)=\sum_i a_i\otimes1\otimes n_i
$$

when $\rho(n)=\sum_i a_i\otimes n_i$ and $\mu(a\otimes n)=an$. For diagonal normalization, the cocycle on the triple diagonal says that an invertible endomorphism is idempotent, hence is the identity. The last formula is the triple cocycle on $n\otimes1\otimes1$.

Flatness identifies $A\otimes_R M$ with the kernel of $1\otimes(\rho-\eta)$ in $A\otimes_R N$, where $\eta(n)=1\otimes n$. The last formula says that $\rho$ lands in this kernel. Hence it defines $\beta:N\to A\otimes_R M$. Multiplication defines $\alpha:A\otimes_R M\to N$. The second formula gives $\alpha\beta=1$, and the first, applied to invariant $m$, gives $\beta\alpha(a\otimes m)=a\otimes m$. Thus $\alpha$ is an isomorphism. Its compatibility with the datum is the equation $\phi((am)\otimes b)=a\otimes bm$. Compatible morphisms preserve invariants and are the scalar extensions of their restrictions. For the canonical datum on $A\otimes_R M_0$, Lemma A1.1 identifies its invariants with $M_0$. This proves the equivalence, including recovery and uniqueness. If $N$ is an algebra and $\phi$ is multiplicative, invariants form a subalgebra containing the unit, and $\alpha$ is an algebra isomorphism. $\square$

**Lemma A1.3 (finite modules descend).** For faithfully flat $R\to A$, finite generation, finite presentation, flatness and finite local freeness of an $R$-module $M$ are equivalent to the respective property of $A\otimes_R M$.

**Proof.** From finitely many generators of $A\otimes_R M$ collect their finitely many $M$ components. Their span has cokernel with zero scalar extension, so generates $M$. To descend finite presentation choose a finite free surjection $R^n\to M$. Its kernel becomes finitely generated after tensoring: for a finitely presented target, the kernel of any finite free surjection is finitely generated, as one sees by comparing with a finite presentation using the pullback of the two surjections and splitting its projections. Descend generation of this kernel by the first argument. To descend flatness, tensor any injection with $M$; its kernel vanishes after flat extension to $A$, because $A\otimes_R M$ is flat, and therefore vanishes. Ascent follows by tensoring presentations and injections. Finally, a finitely presented flat module is finite locally free: locally lift a basis of its residue-field fibre, use finite presentation for the kernel of the resulting free surjection, use flatness to inject that kernel's fibre, and use Nakayama to kill it. Finite presentation spreads the resulting basis to a neighbourhood. The converse is immediate from local bases. $\square$

**Lemma A1.4 (quotient topology).** A surjective flat morphism of affine schemes is a quotient map on underlying topological spaces, universally after base change.

**Proof.** Write $q:\operatorname{Spec}A\to\operatorname{Spec}R$ and suppose $q^{-1}(C)$ is closed. Give spectra their constructible topology, generated by the clopen sets $D(f)$ and $V(f)$. This topology is compact and Hausdorff: an ultrafilter determines the prime of $f$ for which $V(f)$ belongs to it; closure under sums and products follows from the vanishing-set identities, primality from $V(fg)=V(f)\cup V(g)$, and properness from $V(1)=\varnothing$. This gives convergence of every ultrafilter. If a family of closed sets has the finite-intersection property, its generated proper filter extends to an ultrafilter by Zorn's lemma. A limit point lies in each closed member: otherwise its open complement is a neighbourhood belonging to the same filter, a contradiction. Taking complements proves that every open cover has a finite subcover. Distinct primes are separated by $D(f),V(f)$, so the topology is Hausdorff. Ring-induced maps are continuous for this topology. A closed subset of a compact space is compact, since adjoining its open complement to a cover gives a cover of the whole space. Pulling back open covers proves that a continuous image of a compact space is compact. A compact subset $K$ of a Hausdorff space is closed: for a point outside $K$, choose disjoint neighbourhoods separating it from each point of $K$; finitely many of the latter neighbourhoods cover $K$, and the intersection of the corresponding former neighbourhoods avoids $K$. The closed inverse image is therefore constructibly compact; its image $C$, by surjectivity, is constructibly compact and closed.

It is also stable under specialization. If $\mathfrak p\subset\mathfrak p'$ with $\mathfrak p\in C$, choose $\mathfrak q'$ above $\mathfrak p'$. The map $R_{\mathfrak p'}\to A_{\mathfrak q'}$ is flat and local, hence faithfully flat. Indeed a proper ideal of the local source extends inside the maximal ideal of the local target; a nonzero cyclic submodule remains nonzero, and flatness preserves its injection into an arbitrary module. Its spectrum is therefore surjective, by applying this to each residue-field fibre. A prime above $\mathfrak p$ gives $\mathfrak q\subset\mathfrak q'$. Closedness of the inverse image puts $\mathfrak q'$ in it and hence $\mathfrak p'$ in $C$.

A constructibly compact specialization-stable subset is Zariski closed. If a point $\mathfrak p$ outside it had every $D(f)$, $f\notin\mathfrak p$, meeting it, compactness would supply $\mathfrak r\in C$ avoiding all such $f$. Then $\mathfrak r\subset\mathfrak p$, contradicting specialization stability. Thus some principal neighbourhood avoids $C$. Applying complements proves the quotient assertion for opens. After base change, use affine opens of the new base; the same proof applies and glues. $\square$

**Lemma A1.5 (maps and refinement).** Morphisms of schemes satisfy fpqc descent and are uniquely recovered from their compatible pullbacks. This includes morphisms between scheme-valued descent data after refining an fpqc covering.

**Proof.** First take a surjective flat affine cover $\operatorname{Spec}A\to\operatorname{Spec}R$ and a compatible map $u:\operatorname{Spec}A\to Z$. Two points above the same base point have a common point above them on the fibre product: their residue fields have nonzero tensor product over the base residue field, and a prime of that product gives the point. Compatibility therefore defines a set map from $\operatorname{Spec}R$ to $Z$, and Lemma A1.4 makes it continuous. Around a base point choose a principal neighbourhood mapping into an affine open of $Z$. The coefficient map into the corresponding localization of $A$ has equal two pullbacks, and Lemma A1.1 factors it uniquely through the localization of $R$. These maps agree on overlaps, since equality can be checked after the faithfully flat extension on a common affine target chart. They glue to the unique descended map.

For an arbitrary fpqc family, each affine base open has a finite affine refinement; their finite disjoint union is a faithfully flat affine cover. The preceding construction gives a map there. On every original member it recovers the prescribed map after pulling back the refinement, and uniqueness gives recovery before that pullback. The local maps consequently agree on intersections and glue. This works after any base change, so also applies to compatible maps on the pullbacks of any source scheme.

For refinement full faithfulness, let $U_i\to V_{a(i)}\to S$ refine a cover $\{V_j\to S\}$. Given compatible maps between two data on $U_i$, transport them to $U_i\times_S V_j$ using the original transition isomorphisms. The transported maps agree on $U_i\times_S U_k\times_S V_j$ by the two cocycles and their compatibility. The already proved morphism descent gives a unique map over $V_j$. Its compatibility on the original overlaps is checked after the refinement and then follows by uniqueness. This gives full faithfulness; it does not assert effectivity of arbitrary object data. $\square$

**Lemma A1.6 (invariant opens and gluing).** An open of the pullback of a scheme along an fpqc covering descends to an open if its two inverse images agree on overlaps. Invariant open subobjects of an effective scheme datum descend, even when they are not quasi-compact.

**Proof.** On a standard affine refinement, take the image of the invariant open under the surjective flat affine projection. The common-residue-field argument in Lemma A1.5 says that saturation is exactly being the full inverse image of this image. Lemma A1.4 says that the image is open. Give it its open subscheme structure; equality of underlying opens is equality of open subschemes. Uniqueness makes these constructions agree on original covering members and affine base overlaps. The result glues. An open-immersion map compatible with effective data therefore descends to this open immersion. Descended overlaps of a covering by invariant effective opens have unique compatible identifications by Lemma A1.5, satisfy the cocycle by faithfulness, and glue by ordinary scheme gluing. $\square$

<a id="quotient-local-coordinates"></a>
**Lemma A1.7 (local quotient coordinates and unique arrows).** Let \(R\rightrightarrows U\) be an equivalence relation of fppf sheaves on every scheme test, with endpoint map a monomorphism. In particular this applies when \(U,R\) are schemes. On the big fppf site, the associated quotient sheaf \(F\) has local representatives in \(U\), and

\[
U\times_F U=R.
\]

These assertions require no flatness or finite-presentation hypothesis on the projections of \(R\).

**Proof.** If \(U,R\) are schemes, morphism descent in Lemma A1.5 makes them fppf sheaves. In the general case this is already a hypothesis. Construct \(F(T)\) explicitly as follows. A representative is an fppf covering \(\{T_i\to T\}\), together with sections \(u_i\in U(T_i)\), such that on each \(T_i\times_TT_j\) the two maps are endpoints of an arrow to \(R\). Such an arrow is unique by the endpoint monomorphism. The equivalence-relation identities therefore make the arrows obey the triple equation. Two representatives are equivalent when their coordinates are joined by arrows on the mixed overlaps, after a common fppf refinement if necessary. A locally existing arrow glues uniquely by the sheaf property of \(R\), so the phrase “after a refinement” can be removed once the endpoints have been fixed on an overlap. Common refinements are fibre products of coverings. Reflexivity, symmetry and transitivity of the resulting identification follow respectively from the identity, inverse and composition of the arrows. Pullback of coverings and coordinates defines restriction to every test scheme.

This presheaf is a sheaf. Given compatible classes on an fppf covering \(\{T_a\to T\}\), choose coordinate coverings of each \(T_a\). Their composites form a covering of \(T\). Compatibility of the classes means that on every mixed overlap the coordinates are locally joined by an arrow. The unique arrows glue there as just proved. Hence the combined coordinate family is a representative over \(T\), giving existence of the glued class. If two classes restrict equally on the covering, the same mixed-overlap test and uniqueness of arrows make their representatives equivalent, giving uniqueness.

The map from the presheaf \(U(T)/R(T)\) sends a global coordinate to its one-member covering. If a map from this presheaf to an fppf sheaf \(H\) is given, apply it to each coordinate \(u_i\). The images agree on overlaps, since the arrows relate their coordinates, so they glue uniquely to a section of \(H(T)\). Equivalent representatives give the same section, and the construction commutes with pullback. This is the unique extension of the original map. Thus the constructed \(F\) has exactly the universal property of the associated quotient sheaf. Its construction immediately provides local representatives in \(U\).

Finally two maps \(a,b:T\to U\) have the same class precisely when they are locally joined by an arrow. Those local arrows have the fixed endpoints \(a,b\); uniqueness makes them agree on overlaps, and the sheaf property of \(R\) glues them to one arrow over \(T\). Conversely an arrow gives equal classes. This identifies \(U\times_FU\) with \(R\) naturally on every test, proving the displayed identity. \(\square\)

### A2. The affine hull under flat base change

**Lemma A2.1.** If $V$ is quasi-compact and separated over $\operatorname{Spec}R$, then, for every flat $R$-algebra $A$,

$$
A\otimes_R\Gamma(V,\mathcal O_V)
\simeq\Gamma(V_A,\mathcal O_{V_A}).
$$

**Proof.** First make the closed-subscheme calculation explicit. A closed immersion into $\operatorname{Spec}D$ is defined by a quasi-coherent ideal, which is $\widetilde J$ for an ideal $J\subset D$ by S01, Proposition 2.2. The primes of $D/J$ are exactly the primes containing $J$, with the same distinguished-open topology. On these opens, and then on stalks, its structure sheaf is the quotient of the structure sheaf of $\operatorname{Spec}D$, since $(D/J)_f=D_f/JD_f$. Thus the closed subscheme is $\operatorname{Spec}(D/J)$ and is affine. After a ring base change $D\to D'$, the maps $d'\otimes(d+J)\mapsto d'd+JD'$ and $d'+JD'\mapsto d'\otimes1$ identify $D'\otimes_D(D/J)$ with $D'/JD'$. The tensor relations make these maps well defined and inverse. The affine-map correspondence in S01, Proposition 2.3, identifies fibre products of affines with spectra of tensor products: ring maps out of the tensor product are exactly the pairs agreeing on the base, on every locally ringed test space. These calculations prove the affine closed-immersion base-change assertion; restricting to affine charts proves it for arbitrary base changes. Now choose a finite affine open cover $V_i$. The product $V_i\times_R V_j$ is affine by the same tensor calculation. The inverse image of this product under the closed diagonal is $V_i\cap V_j$, which is therefore a closed subscheme of that affine product and hence affine. Global sections are the kernel of the differences of restrictions from $\prod_i\Gamma(V_i,\mathcal O)$ to $\prod_{i,j}\Gamma(V_i\cap V_j,\mathcal O)$, by the sheaf axiom. Flat tensor preserves this kernel and the finite products, as proved in S01, Section 1. On each affine chart and intersection, scalar extension replaces its ring by its tensor product with $A$. The resulting diagram is consequently the same sections diagram for the base-changed cover. $\square$

**Lemma A2.2.** For a quasi-compact open $V\subset\operatorname{Spec}C$, the canonical map $V\to\operatorname{Spec}\Gamma(V,\mathcal O_V)$ is a quasi-compact open immersion.

**Proof.** Choose finitely many principal opens $D_C(f_i)$ contained in $V$ and covering it, and put $B=\Gamma(V,\mathcal O_V)$. Lemma A2.1 with $C\to C_{f_i}$ gives $B_{f_i}=C_{f_i}$, because $V_{f_i}=D_C(f_i)$. Thus the canonical map is an isomorphism from each $D_C(f_i)$ to $D_B(f_i)$. These identifications agree on the principal intersections and glue. The image is the finite union of the $D_B(f_i)$, hence is quasi-compact. $\square$

### A3. Effective quasi-affine descent

**Theorem A3.1.** Quasi-affine scheme morphisms with data for an fpqc covering descend effectively to quasi-affine scheme morphisms, with all compatible morphisms descending uniquely.

**Proof for an affine faithfully flat cover.** Let $R\to A$ be faithfully flat and let $V/A$ be quasi-affine with a datum. Put $B=\Gamma(V,\mathcal O_V)$. The two projections from $\operatorname{Spec}(A\otimes_R A)$ are flat. Lemma A2.1 therefore turns the original datum into algebra descent data on $B$, compatibly with multiplication, unit and the triple cocycle. Lemma A1.2 gives an $R$-algebra $B_0$ with $A\otimes_R B_0=B$. Lemma A2.2 embeds $V$ as a quasi-compact open of $W_A$, where $W=\operatorname{Spec}B_0$, and this embedding respects the datum. Its two pulled-back opens agree. Lemma A1.6 descends it to an open $U\subset W$ with $U_A=V$ and precisely the given datum. Its topology is quasi-compact, since it is the continuous image of $V$. Thus $U$ is quasi-affine over $R$. Morphisms descend by Lemma A1.5.

**Passage to arbitrary fpqc coverings.** Over an affine base open choose a finite affine refinement of the covering, and combine its members into one affine scheme. Finite disjoint unions of quasi-affine schemes over an affine base are quasi-affine: take the product of their affine hull algebras and the union of the corresponding component opens. Apply the affine construction. Its comparison with every original member descends uniquely after pulling back the refinement, by Lemma A1.5; the cocycle supplies the requisite compatibility. Construct the result on each affine base open. The uniquely descended comparisons on their intersections satisfy the cocycle and glue to a scheme $U\to S$.

The resulting morphism is globally quasi-affine, and not merely quasi-affine separately on these pieces. On an affine base open, localization and Lemma A2.1 show that $f_*\mathcal O_U$ is the quasi-coherent algebra associated to its section algebra. These algebras agree under restriction, so form a quasi-coherent algebra on $S$. The canonical map $U\to\operatorname{Spec}_S(f_*\mathcal O_U)$ is a quasi-compact open immersion on every affine base open, by Lemma A2.2, hence globally. This proves the asserted type and effectivity. $\square$

**Corollary A3.2.** Affineness, closed immersions and open immersions of existing scheme morphisms descend under fpqc coverings. Quasi-affineness of an existing scheme morphism is fpqc-local on the target.

**Proof.** Affine objects descend by Lemma A1.2 on the affine refinements; their comparison isomorphisms with an existing scheme and their inverses descend by Lemma A1.5. For closed immersions descend the quotient algebra and its defining ideal using the same module construction; the surjectivity of its algebra map is detected by faithfully flat tensoring. This constructs a closed immersion with the given data, hence identifies it with the existing map. For open immersions use Lemma A1.6. Finally apply Theorem A3.1 to the canonical datum of an existing morphism and descend its comparison and inverse. $\square$

## B. Polynomial normality before the conductor

### B1. A preliminary coefficient proof for polynomial normality

**Lemma B1.1 (integral polynomial coefficients).** Let $R\to B$ be any ring map. A polynomial $b(T)=\sum_{j<d}b_jT^j$ in $B[T]$ is integral over $R[T]$ if and only if every $b_j$ is integral over $R$.

**Proof.** Integral elements form a ring, so the reverse implication follows from finite integral generators and the fact that $T$ already belongs to the base.

Here is an interpolation argument valid in every characteristic and with nilpotents. First supply the integer arithmetic. Lemma P0.10 proves that every nonzero integer ideal has a positive generator. Applied to $(a,b)$ this gives $\gcd(a,b)=ua+vb$ for integers $u,v$. If $\gcd(a,b)=1$ and $a\mid bc$, multiplication of that identity by $c$ shows $a\mid c$. A prime integer is therefore a prime element. Induction factors every integer $n>1$ into primes, by splitting a composite into smaller positive factors; prime divisibility and cancellation give uniqueness. Thus $\mathbf Z$ is factorial. A prime divisor of the product of any finite prime list plus one is absent from that list, so prime integers are arbitrarily large. Distinct prime powers have greatest common divisor one and satisfy the same Bezout identity. Choose a prime integer $p>d$ and put

$$
R_p=R[1/p],\qquad
C_p=R_p[Z]/(1+Z+\cdots+Z^{p-1}).
$$

Monic division gives a unique remainder of degree below $p-1$ in this quotient: subtract the leading coefficient times the appropriate monomial multiple of the monic divisor until the degree drops. Uniqueness follows because a nonzero multiple of a monic degree-$p-1$ polynomial has degree at least $p-1$, even over a ring with zero divisors. Thus $C_p$ is finite free over $R_p$ with basis $1,Z,\ldots,Z^{p-2}$. The coefficient-of-one projection is an $R_p$-linear retraction of its unit inclusion. Tensoring that retraction with $B_p$ splits $B_p\to B_p\otimes_{R_p}C_p$, so this map is injective without a flatness hypothesis. Zero rings are included.

In $\mathbf Z[Z]/(1+\cdots+Z^{p-1})$ there is the identity

$$
T^p-1=\prod_{i=0}^{p-1}(T-Z^i).                                      \tag{1.1}
$$

To justify it before arbitrary base change, write $\Phi(Z)=1+\cdots+Z^{p-1}$. After replacing $Z$ by $V+1$, it becomes $((V+1)^p-1)/V$; every nonleading coefficient is divisible by $p$, since $p\mid\binom pi$ for $0<i<p$ (the denominator $i!$ has no factor $p$), and its constant term is $p$, not divisible by $p^2$. If it had two nonconstant monic integral factors, reduction modulo $p$ would make both powers of $V$, so both constant terms would be divisible by $p$, a contradiction. The primitive polynomial argument of Lemma P0.5, using the factoriality of $\mathbf Z$ proved above, converts a rational factorization to such an integral one. Thus $\Phi$ is irreducible over $\mathbf Q$. Put $E=\mathbf Q[Z]/(\Phi)$ and let $z$ be the image of $Z$. This quotient is a field: for a nonzero remainder, Euclidean Bezout with the irreducible $\Phi$ supplies its inverse. The identity $(Z-1)\Phi(Z)=Z^p-1$ gives $z^p=1$, whereas $z\ne1$ since $\Phi(1)=p\ne0$ in $E$. If $z^n=1$ for $0<n<p$, the integer Bezout identity for $n,p$ would give $z=1$. Hence $1,z,\ldots,z^{p-1}$ are distinct. Division by $T-a$ leaves remainder $f(a)$; after dividing off one root, evaluation at each other distinct root still vanishes, because their differences are nonzero in the field. Repeating division and comparing degrees proves (1.1) in $E[T]$. Monic division by $\Phi$ shows $\mathbf Z[Z]/(\Phi)\to E$ injective: its unique integer remainder of degree below $p-1$ can vanish in the rational quotient only if every coefficient is zero. Therefore (1.1) holds already in that integral quotient.

Differentiate (1.1) and evaluate at $T=Z^i$. The product $\prod_{j\ne i}(Z^i-Z^j)$ equals $pZ^{i(p-1)}$. It is a unit in $C_p$ because $p$ is inverted and $Z^p=1$. Each of its factors is consequently a unit. The $d$ elements $\alpha_i=Z^i$, $0\le i<d$, have pairwise invertible differences.

In $B_p\otimes C_p$, evaluation of a monic integral equation for $b(T)$ at $\alpha_i$ makes $b(\alpha_i)$ integral over $C_p$. Since $C_p$ is finite over $R_p$, these values are integral over $R_p$. Lagrange interpolation gives

$$
b(T)=\sum_{i<d}b(\alpha_i)
\frac{\prod_{j\ne i}(T-\alpha_j)}
{\prod_{j\ne i}(\alpha_i-\alpha_j)}.                                  \tag{1.2}
$$

For completeness, prove the determinant identity used here. In independent variables $X_0,\ldots,X_{d-1}$, the determinant of $(X_i^j)_{0\le i,j<d}$, viewed as a polynomial in $X_{d-1}$ over $\mathbf Q(X_0,\ldots,X_{d-2})$, has degree at most $d-1$ and vanishes at each $X_i$ with $i<d-1$, because two rows then coincide. Its leading coefficient is the preceding Vandermonde determinant by expansion in the last row. Division by those distinct linear factors and induction, starting with the empty determinant $1$, give $\det(X_i^j)=\prod_{i<j}(X_j-X_i)$. Both expressions are integer polynomials; their embedding in the rational-function polynomial ring is injective, so this is an integer-polynomial identity and remains true after substitution into every commutative ring. The difference of the two sides of (1.2) has degree below $d$ and vanishes at all $\alpha_i$; its coefficient vector is killed by this Vandermonde matrix. Its determinant is a unit, and the adjugate gives an inverse, so the difference is zero. Formula (1.2) makes each coefficient integral over $C_p$, and hence over $R_p$. Its monic equation holds already in $B_p$, by the displayed injectivity.

Repeat with a distinct prime $q>d$. If $A\subset B$ is the integral closure of the image of $R$, localization of integral closure, proved in Lemma P0.3, gives $b_j/1\in A[1/p]$ and $b_j/1\in A[1/q]$. Hence powers $p^a$ and $q^c$ kill the class of $b_j$ in the $R$-module $B/A$. Bezout's identity for those two coprime integers kills the class itself. Thus $b_j\in A$, as required. The degree-zero and zero-polynomial cases are included. $\square$

**Corollary B1.2 (polynomial normality).** If $R$ is a normal domain, then $R[T]$ is a normal domain.

**Proof.** Put $K=\operatorname{Frac}R$. An element $z\in K(T)$ integral over $R[T]$ is integral over $K[T]$. The Euclidean ring $K[T]$ is factorial and therefore normal, by Lemma P0.5. Thus $z\in K[T]$. Lemma B1.1 applied to $R\subset K$ makes all its coefficients integral over $R$. Normality of $R$ puts them in $R$. Therefore $z\in R[T]$. $\square$

This is the precise preliminary input consumed by Lemma C3.2 below. The earlier proof of normality of polynomial rings over a field alone would not suffice.

## C. Conductor and affine Zariski Main

### C1. Extracting an integral remainder

**Lemma C1.1.** Let $A[X]\to B$ be a ring map and let $v\in B$ be integral over the image of $A[X]$. If $vP(X)$ belongs to that image for a monic $P\in A[X]$, then there is $Q\in A[X]$ such that $v-Q(X)$ is integral over $A$.

**Proof.** Write $vP=R$ in $B$ for $R\in A[X]$. Divide $R$ by the monic $P$ to obtain $R=QP+R_0$, with $\deg R_0<\deg P$. Replace $v$ by $v-Q(X)$, which is still integral over $A[X]$ and now satisfies $vP=R_0$.

In $B_v$ the element $X$ satisfies the monic equation $P(X)-v^{-1}R_0(X)=0$ over the image of $A[v^{-1}]$. It is therefore integral over that ring. Transitivity makes $v$ integral over the same ring. Write the coefficients of its monic equation as finite sums $\sum_j a_{ij}v^{-j}$. Choose $N$ large enough to make all exponents nonnegative when the equation is multiplied by $v^N$, and, if necessary, enlarge $N$ to kill its localization error in $B$. The equation becomes

$$
v^{d+N}+\sum_{i<d,j}a_{ij}v^{i+N-j}=0
$$

in $B$. Every exponent in the sum is nonnegative and strictly less than $d+N$. This is a monic equation over $A$, proving the claim. If $P=1$, the remainder is zero and the conclusion follows immediately. $\square$

**Lemma C1.2.** With the same integral $v$, suppose $vP(X)$ belongs to the image for an arbitrary polynomial $P=a_0+\cdots+a_dX^d$. Then $a_d^Nv-Q(X)$ is integral over $A$ for some $N\ge0$ and $Q\in A[X]$.

**Proof.** Localize at $a_d$. The polynomial $P/a_d$ is monic there, so Lemma C1.1 gives an integral remainder $v-Q_0(X)$, with $Q_0\in A_{a_d}[X]$. Multiply by a power of $a_d$ to clear the coefficients of $Q_0$. The resulting element $w=a_d^nv-Q(X)$ is integral after localization. In its localized monic equation, multiplying $w$ by a sufficiently high power of $a_d$ clears every coefficient denominator. A further power kills the error if that equation initially holds only after localization. The monic equation is then valid before localization. Thus a further multiple $a_d^mw$ is integral over $A$, as asserted. This argument also covers a nilpotent $a_d$: its localization is zero, and sufficiently high powers make the required element zero. $\square$

### C2. The conductor and all coefficients

Let $A\subset B$ be an inclusion such that $A$ is integrally closed **in $B$**, and suppose $B$ is finite over the subalgebra $A[x]$. The latter phrase does not require $x$ to be transcendental. Define

$$
J=\{u\in B:uB\subset A[x]\}.
$$

This is an ideal of $B$, is contained in $A[x]$, and is called the conductor. For every $u\in J$, localization gives $B_u=A[x]_u$: write $b=(ub)/u$. Choose $A[x]$-module generators $b_1,\ldots,b_s$ for $B$.

**Lemma C2.1.** If $u(a_0+a_1x+\cdots+a_dx^d)\in J$, then $ua_d^N\in J$ for some $N\ge0$.

**Proof.** For each $i$ the element $ub_i$ is integral over $A[x]$, since $B$ is finite over it, and its product with the displayed polynomial lies in $A[x]$ by the conductor condition. Lemma C1.2 gives $a_d^{N_i}ub_i-Q_i(x)$ integral over $A$. This element belongs to $B$, so integral closedness puts it in $A\subset A[x]$. Hence $a_d^{N_i}ub_i\in A[x]$. With $N=\max_iN_i$, all $a_d^Nub_i$ belong to $A[x]$; module generation then gives $ua_d^NB\subset A[x]$, which is the assertion. $\square$

**Lemma C2.2.** If $u(a_0+a_1x+\cdots+a_dx^d)\in\sqrt J$, then $ua_i\in\sqrt J$ for every $i$.

**Proof.** Choose $r>0$ such that $u^r(a_0+\cdots+a_dx^d)^r\in J$. Applying Lemma C2.1 to this polynomial gives $u^ra_d^{rN}\in J$ for some $N$. If $N=0$, then $u\in\sqrt J$ and the required assertion is immediate. If $N>0$, multiplying by a sufficiently high power of $u$ shows that a power of $ua_d$ lies in $J$, so $ua_d\in\sqrt J$. Subtract the term $ua_dx^d$ from the original expression. The result is still in $\sqrt J$. Repeat with its lower-degree polynomial until every coefficient has been treated. $\square$

An element $x$ of a reduced algebra $B$ is **strongly transcendental over $A$** if

$$
u(a_0+a_1x+\cdots+a_dx^d)=0
\quad\Longrightarrow\quad ua_i=0\text{ for every }i
$$

for all $u\in B$ and all coefficients $a_i\in A$. Lemma C2.2 says that the image of $x$ in $B/\sqrt J$ has this property over the embedded reduced ring $A/(A\cap\sqrt J)$.

### C3. Why a strongly transcendental finite extension has no isolated fibre point

We use the fibre criterion proved in the earlier quasi-finite-morphism lesson: for a finite-type ring map, a point is quasi-finite exactly when it is isolated in its fibre and its residue field is finite over the base residue field. Base change and passage to a closed source subscheme preserve quasi-finiteness. In particular a finite extension is quasi-finite. These are substantive earlier proofs to be bound to this lesson, not external proof substitutes.

**Lemma C3.1.** If reduced $A\subset B$ has a strongly transcendental $x\in B$, then for every minimal prime $\mathfrak q$ of $B$ the image of $x$ is transcendental over $A/(A\cap\mathfrak q)$ in the domain $B/\mathfrak q$.

**Proof.** The localization $B_{\mathfrak q}$ is a field: it is reduced, its only prime is its maximal ideal, and its nilradical, the intersection of all primes, is zero; thus its maximal ideal is zero. If $u\sum_i a_ix^i\in\mathfrak q$, it vanishes there, so some $v\notin\mathfrak q$ makes $vu\sum_i a_ix^i=0$ in $B$. Strong transcendence gives $vua_i=0$, so $ua_i\in\mathfrak q$ for all $i$. Taking $u=1$ proves that no nonzero polynomial over the embedded $A/(A\cap\mathfrak q)$ can annihilate the image of $x$. $\square$

**Lemma C3.2.** Suppose $A\subset B$ are domains, $x$ is transcendental over $A$, and $B$ is finite over $A[x]$. Then $\operatorname{Spec}B\to\operatorname{Spec}A$ is quasi-finite at no point.

**Proof.** First let $A$ be normal. Corollary B1.2 above makes $A[x]$ normal. At a prime $\mathfrak q$ put $\mathfrak p=\mathfrak q\cap A$ and $\mathfrak r=\mathfrak q\cap A[x]$. If $\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is not finite, the fibre criterion already excludes quasi-finiteness. Otherwise $\kappa(\mathfrak r)/\kappa(\mathfrak p)$ is finite, and $\mathfrak r$ strictly contains $\mathfrak pA[x]$: the latter prime has residue field $\kappa(\mathfrak p)(x)$, which is transcendental. Going down for the integral domain extension $A[x]\subset B$ supplies $\mathfrak q'\subsetneq\mathfrak q$ over $\mathfrak pA[x]$. Both primes are in the fibre over $\mathfrak p$. Thus $\mathfrak q$ has a distinct generalization in that fibre, and cannot be isolated.

For general $A$, let $A'$ be its integral closure in $\operatorname{Frac}(A)$ and let $B'$ be the subring of $\operatorname{Frac}(B)$ generated by $A'$ and $B$. The ring $B'$ is integral over $B$ and finite over $A'[x]$: it is a quotient of $B\otimes_A A'$, with the same finite module generating list. The element $x$ is still transcendental over $A'$, since $A'$ lies in $\operatorname{Frac}(A)$. If $\mathfrak q$ were quasi-finite over $A$, its base changes to $\operatorname{Spec}(B\otimes_A A')$ would be quasi-finite over $A'$, and so would their restrictions to $\operatorname{Spec}B'$. Lying over for $B\subset B'$ gives a prime of $B'$ above $\mathfrak q$. The normal-base case contradicts quasi-finiteness at that prime. $\square$

**Corollary C3.3.** If reduced $A\subset B$ contains a strongly transcendental $x$, and $B$ is finite over $A[x]$, then no point is quasi-finite over $A$.

**Proof.** At a prime $\mathfrak q$ choose a minimal prime $\mathfrak q_0\subset\mathfrak q$. Lemma C3.1 and Lemma C3.2 apply to $A/(A\cap\mathfrak q_0)\subset B/\mathfrak q_0$. A quasi-finite point would remain quasi-finite on this closed source subscheme, a contradiction. $\square$

### C4. Algebraic Zariski Main

**Lemma C4.1 (one generator).** If $B=A[b]$ and $C$ is the integral closure of the image of $A$ in $B$, every quasi-finite point $\mathfrak q$ admits $g\in C\setminus\mathfrak q$ with $C_g=B_g$.

**Proof.** Put $\mathfrak p=\mathfrak q\cap A$ and present $B=A[T]/I$. Some polynomial of $I$ has a coefficient outside $\mathfrak p$: otherwise the fibre is $\kappa(\mathfrak p)[T]$, whose points are not isolated with finite residue field. Thus there is an equation $a_mb^m+\cdots+a_0=0$ in $B$, with coefficients in the image of $A$, and some coefficient outside $\mathfrak q$.

Its leading multiple $a_mb$ is integral: multiply the equation by $a_m^{m-1}$ to give a monic equation for that multiple. Hence $a_mb\in C$. If $a_m\notin\mathfrak q$, localizing at $g=a_m$ puts $b$ in $C_g$ and proves equality. Otherwise combine the first two terms as $(a_mb+a_{m-1})b^{m-1}$ and keep the lower terms. This is a shorter equation with coefficients in $C$ and at least one coefficient outside $\mathfrak q$, since $a_mb\in\mathfrak q$. The same argument applies: transitivity puts every new integral leading multiple in $C$. Repetition must find a leading coefficient outside $\mathfrak q$, since a degree-zero equation with its coefficient outside that prime is impossible. This coefficient gives the required $g$. $\square$

**Lemma C4.2 (finite over one generator).** Suppose $A\subset B$ is integrally closed in $B$, $B$ is finite over $A[b]$, and $\mathfrak q$ is quasi-finite over $A$. Then $A_h=B_h$ for some $h\in A\setminus\mathfrak q$.

**Proof.** Use the conductor $J$ of $A[b]\subset B$. If $J\subset\mathfrak q$, Lemma C2.2 makes the quotient extension

$$
A/(A\cap\sqrt J)\subset B/\sqrt J
$$

strongly transcendental and finite over its single polynomial generator. Corollary C3.3 says it has no quasi-finite point. But the point from $\mathfrak q$ remains quasi-finite on that closed fibre subscheme, a contradiction. Choose $u\in J\setminus\mathfrak q$. Then $A[b]_u=B_u$. Its corresponding point is quasi-finite over $A$, since the local fibre agrees with the fibre of $B$ there. Apply Lemma C4.1 to $A[b]$, whose relative integral closure is $A$, to obtain $a\in A\setminus\mathfrak q$ with $A_a=A[b]_a$. In this ring express $u=c/a^N$ with $c\in A\setminus\mathfrak q$. Localizing at $h=ac$ makes $a$ and $u$ invertible and gives $A_h=B_h$. $\square$

**Theorem C4.3 (algebraic Zariski Main).** For a finite-type map $R\to B$, let $C\subset B$ be the integral closure of its image. At every quasi-finite prime $\mathfrak q$ there is $g\in C\setminus\mathfrak q$ with $C_g=B_g$.

**Proof.** Replace $R$ by its image. Induct on the least $n$ for which $B$ is finite over $R[b_1,\ldots,b_n]$. For $n=0$, $C=B$. For $n=1$, replace $R$ by $C$ and use Lemma C4.2: relative integrality is unchanged by transitivity, the same list generates $B$ as a finite module over $C[b_1]$, and its fibre at the point is a subspace of the original fibre with the same finite residue-field condition.

For $n>1$, take the relative integral closure $D$ of $R[b_1,\ldots,b_{n-1}]$ in $B$. Lemma C4.2 supplies $v\in D\setminus\mathfrak q$ with $D_v=B_v$. Choose finitely many numerators in $D$ for a finite algebra generating list of $B_v$ over $R$. Let $E\subset D$ be generated by those numerators, $v$, and $b_1,\ldots,b_{n-1}$. Then $E_v=B_v$. It is finite over $R[b_1,\ldots,b_{n-1}]$, because its finitely many added generators are integral over that ring. The contracted point is quasi-finite over $R$, by equality of the localized rings and fibres.

Induction applied to the finite-type $E$ gives its relative integral closure $F$ and $w\in F\setminus\mathfrak q$ such that $F_w=E_w$. Write $v=c/w^M$ there, with $c\in F\setminus\mathfrak q$. Put $g=wc$. Then $F_g=E_g=B_g$. Since $F\subset C\subset B$, also $C_g=B_g$. The finite intermediate $E$ is essential: no finiteness of the entire integral closure $D$ has been assumed. $\square$

### C5. Affine completion and the open quasi-finite locus

**Theorem C5.1.** The quasi-finite locus of a locally finite-type scheme morphism is open. A quasi-finite affine morphism $\operatorname{Spec}B\to\operatorname{Spec}R$ factors as a quasi-compact open immersion into a finite affine $R$-scheme.

**Proof.** On an affine chart Theorem C4.3 gives $C_g=B_g$ near a chosen quasi-finite point. Select finitely many integral numerators that, together with $g^{-1}$, generate $B_g$ over $R$, and let $D\subset C$ be generated by them and $g$. Its generators are integral, so $D$ is a finite $R$-module algebra. Since $D_g=B_g$, the open $D_B(g)$ is quasi-finite over $R$, being the open part of a finite map. These neighbourhoods prove openness.

If every point is quasi-finite, choose finitely many such $g_i$ whose opens cover $\operatorname{Spec}B$. Take the finite $R$-subalgebra generated by all the selected numerators and all $g_i$. Its localizations at $g_i$ are $B_{g_i}$. Thus $\operatorname{Spec}B$ identifies with the finite union of opens $D_D(g_i)$ in $\operatorname{Spec}D$, giving the stated quasi-compact open immersion. The construction allows extra points in the finite completion. $\square$

## D. Étale structure and general scheme Zariski Main

### D2. The structural étale inputs, with proofs

**Lemma D2.1 (maps between étale algebras).** Every $R$-algebra map $P\to Q$ between étale $R$-algebras is étale. A surjective such map is a principal localization, equivalently the projection onto an open-and-closed component.

**Proof.** Write finite presentations of $P$ and $Q$ over $R$, and express the images of the finitely many generators of $P$ as polynomials in the generators of $Q$. Over $P$, the presentation of $Q$ consists of its finitely many old relations together with the equations identifying those images with the generators of $P$. Hence $Q$ is finitely presented over $P$.

In a square-zero lifting problem over $P$, formal étaleness of $Q/R$ gives a unique $R$-lift. Its restriction to $P$ and the specified $P$-structure are two $R$-lifts of the same residue map. Formal unramifiedness of $P/R$ makes them equal. The lift is therefore a $P$-lift and is unique. This proves étaleness using its finite-presentation and formal-lifting definition.

If $Q=P/I$, finite presentation makes $I$ a finite ideal. One direct justification is to present the quotient over $P$ using finitely many variables and relations, choose lifts of their images in $P$, and substitute those lifts into the finitely many relations; their values generate the kernel. Formal smoothness over $P$ applied to $P/I^2\to P/I$ gives a $P$-algebra section. For $a\in I$, its image in $P/I^2$ must then be the image of zero, so $I/I^2=0$.

Write finite generators $a_i$ as $a_i=\sum_jc_{ij}a_j$ with $c_{ij}\in I$. The adjugate of $(\delta_{ij}-c_{ij})$ shows that its determinant annihilates $I$. That determinant is $1-e$ for an $e\in I$. Thus $(1-e)I=0$, and in particular $(1-e)e=0$. Consequently $e^2=e$ and $I=Pe$. The quotient $P/I$ is $P_{1-e}$, proving the final assertion. $\square$

**Lemma D2.2 (one monic étale equation near a point).** If $R\to S$ is étale and $\mathfrak q\in\operatorname{Spec}S$, a principal neighbourhood of $\mathfrak q$ is isomorphic over $R$ to

$$
(R[T]/(F))_h,\qquad F\text{ monic},\quad F'\text{ invertible}.          \tag{2.1}
$$

**Proof.** Étale field fibres are finite products of finite separable fields, by the full field proof in the earlier étale lesson. Hence $S/R$ is quasi-finite. Theorem C4.3 gives a finite $R$-subalgebra $D\subset S$ and $v\in D\setminus\mathfrak q$ with $D_v=S_v$. Let $\mathfrak r=\mathfrak q\cap D$ and $\mathfrak p=\mathfrak q\cap R$. The selected local factor of $D\otimes_R\kappa(\mathfrak p)$ is $\kappa(\mathfrak q)$, because localization at $v$ is the étale fibre. The other finitely many factors are local Artinian rings.

Choose a nonzero primitive element $\alpha$ of $\kappa(\mathfrak q)/\kappa(\mathfrak p)$. The elementary primitive-element proof is as follows. Over an infinite base field, for a separable extension generated by $a,b$, finitely many embeddings into a splitting field forbid only finitely many values of $c$ for which two embeddings agree on $a+cb$. A value outside that list gives an element with the full number of distinct conjugates and hence the full degree. Induct on the finite generating list. Over a finite base field, the multiplicative group of the finite extension is cyclic: in a finite abelian subgroup of a field's units, choose an element whose order contains the largest prime-power order occurring for each prime, multiply these prime-power components, and obtain order equal to the group's exponent. Every group element is a root of $T^e-1$, so the field root bound gives the group's size at most $e$, forcing equality. Its generator generates the field. For a trivial extension choose $\alpha=1$.

In the fibre of $D$, choose $\bar t=(\alpha,0,\ldots,0)$. Clearing a base denominator gives $t\in D$ with residue $(c\alpha,0,\ldots,0)$ for a nonzero $c\in\kappa(\mathfrak p)$; scaling preserves primitivity and nonzeroness. Put $E=R[t]\subset D$. This is finite over $R$, since $t$ is integral. The prime $\mathfrak r'=\mathfrak r\cap E$ has exactly one prime of $D$ above it: all other fibre points have $t=0$, whereas the chosen one has $t=c\alpha\ne0$.

The finite algebra $D_{\mathfrak r'}$ over the local ring $E_{\mathfrak r'}$ is therefore local, with localization $D_{\mathfrak r}$. To see this, maximal ideals of a finite algebra contract to the maximal ideal, so the unique prime above $\mathfrak r'$ is its unique maximal ideal; localizing further at that ideal changes nothing. Its quotient by $\mathfrak p$ is the field $\kappa(\mathfrak q)$. The residue field of $E_{\mathfrak r'}$ also equals that field, because it contains $c\alpha$ and $\kappa(\mathfrak p)$. Nakayama applied to the finite module $D_{\mathfrak r'}/E_{\mathfrak r'}$ gives

$$
E_{\mathfrak r'}=D_{\mathfrak r'}=D_{\mathfrak r}.
$$

The modules $D/E$ and $D/vD$ are finite over $E$ and vanish after localization at $\mathfrak r'$. A common element $u\in E\setminus\mathfrak r'$ kills their chosen finite generators. Thus $E_u=D_u$, $v$ is invertible there, and $E_u=D_u=S_{uv}$ is étale over $R$.

Present $E=R[T]/I$ by $T\mapsto t$. Choose a monic $M\in I$ using integrality of $t$. The fibre ideal $I\kappa(\mathfrak p)[T]$ is principal. Its factor belonging to the selected point is the separable minimal polynomial $H_1$ of $c\alpha$ with multiplicity one, because $(E\otimes\kappa(\mathfrak p))_{\mathfrak r'}$ is the field $\kappa(\mathfrak q)$. Choose $H\in I$ whose reduction is a nonzero scalar multiple of a generator of that fibre ideal. This is possible by expressing that generator as a finite combination of images of elements of $I$ and clearing the finitely many denominators outside $\mathfrak p$.

For $N\ge2$ with $N\deg M>\deg H$, put $F=M^N+H\in I$. It is monic. Modulo $\mathfrak p$, the term $M^N$ is divisible by $H_1^2$, whereas $H$ is divisible by $H_1$ exactly once. Therefore $F'$ is nonzero at $c\alpha$. Choose a polynomial lift of $u$ and localize at its product with $F'$. We get a surjection from the standard étale algebra $(R[T]/F)_{uF'}$ onto the étale algebra $E_{uF'}$. Lemma D2.1 makes this surjection a principal localization. Its target is a principal neighbourhood of our original point in $S$, and its source and all principal localizations have the form (2.1). $\square$

No Noetherian reduction was used here. Finiteness of $D/E$ is sufficient for the localization step; no finiteness of the full relative integral closure was assumed.

**Lemma D2.3 (flatness and openness).** Étale morphisms are flat and open.

**Proof.** The algebra $R[T]/F$ for monic $F$ is finite free over $R$. Localization at an element of this algebra is a filtered colimit of copies of that free $R$-module with multiplication transition maps. Tensoring an injection with every copy is injective, and exactness of filtered colimits proves flatness of the localization. Lemma D2.2 covers an étale algebra by such principal neighbourhoods. A kernel of a tensor map which vanishes on that principal cover is zero, so the entire algebra is flat.

For openness, let $C=R[T]/F$, of rank $d$, and let $a\in C$. A prime $\mathfrak p$ belongs to the image of $D_C(a)$ exactly when $a$ is not nilpotent in the finite-dimensional algebra $C\otimes_R\kappa(\mathfrak p)$. Multiplication by $a$ has characteristic polynomial $T^d+c_1T^{d-1}+\cdots+c_d$. Over a field it is nilpotent exactly when this polynomial is $T^d$: one direction is elementary nilpotent linear algebra, and the other is Cayley–Hamilton, obtained by the polynomial adjugate identity. Thus the image is $\bigcup_iD_R(c_i)$, an open.

A principal open of a localization $C_g$ is $D_C(ga)$ for a suitable numerator $a$. Its image is open by the same calculation. Principal opens form a basis, and Lemma D2.2 covers arbitrary étale morphisms by these charts. Taking unions proves openness. $\square$

### D3. Finite pieces after an elementary étale neighbourhood

An **elementary étale neighbourhood** of $(S,s)$ is an étale morphism $T\to S$ with a chosen $t\mapsto s$ inducing $\kappa(t)=\kappa(s)$.

**Lemma D3.1 (the universal coprime-factor construction).** Suppose $F\in R[T]$ is monic and its reduction at $\mathfrak p\subset R$ factors into coprime monic polynomials $\bar G\bar H$ of degrees $r,s$. There is an elementary étale neighbourhood $(\operatorname{Spec}R',\mathfrak p')$ of $\mathfrak p$ on which $F=GH$ with those degrees and residues, and $G,H$ generate the unit ideal of $R'[T]$.

**Proof.** Introduce $r+s$ variables for the nonleading coefficients of monic $G,H$, impose the $r+s$ coefficient equations $GH=F$, and invert their Jacobian determinant $\Delta$. At the prescribed residue point the Jacobian is the matrix of

$$
\kappa(\mathfrak p)[T]_{<r}\oplus\kappa(\mathfrak p)[T]_{<s}
\longrightarrow\kappa(\mathfrak p)[T]_{<r+s},
\qquad (U,V)\longmapsto\bar H U+\bar G V.
$$

Its kernel is zero: coprimality forces $\bar G\mid U$, then the degree bound gives $U=0$ and $V=0$. Equal dimensions make $\Delta$ nonzero at that point. The square Jacobian lifting proof in the earlier étale lesson proves that this finitely presented localized coefficient algebra $R'$ is étale. Evaluation at the prescribed coefficients gives the point with residue field exactly $\kappa(\mathfrak p)$.

Over $R'$ the same coefficient matrix is invertible. Apply its inverse to the constant polynomial $1$. This gives $U,V$ with $HU+GV=1$, proving the last assertion. Degree-zero factors are included, with the evident empty coefficient lists. $\square$

The construction below uses this coprime-factor matrix at an actual finite neighbourhood; it requires no henselization theorem.

**Lemma D3.2 (one finite open piece).** Let $f:X\to S$ be locally of finite type and let $x$ be isolated in $X_s$, $s=f(x)$. There is an elementary étale neighbourhood $(T,t)$ of $(S,s)$ and an open $V\subset X_T$ finite over $T$, whose fibre over $t$ has exactly one point $v$ mapping to $x$, with $\kappa(v)=\kappa(x)$. A further elementary étale base change preserves these properties.

**Proof.** Choose compatible affine neighbourhoods of $x$ and $s$. Openness of the quasi-finite locus from Theorem C5.1 lets us choose a smaller affine principal neighbourhood $Y$ of $x$ on which the map is quasi-finite. Its affine completion embeds $Y$ openly into $\operatorname{Spec}D$, with $D$ finite over the chosen base ring $R$.

The finite fibre $D\otimes_R\kappa(s)$ is a product of local Artinian rings. Let $e_0$ be the component idempotent for the point $x$ in this completion. Work first over $R_{\mathfrak p}$, where $\mathfrak p$ is the prime of $s$, and lift $e_0$ to $b\in D_{\mathfrak p}$. There is a monic $F\in R_{\mathfrak p}[T]$ with $F(b)=0$ by the finite-module determinant argument. If the fibre has just this one component, take $e=1$ and skip the next splitting paragraph.

Otherwise $e_0$ and $1-e_0$ are nonzero. The identity

$$
\bar F(e_0)=\bar F(0)(1-e_0)+\bar F(1)e_0=0
$$

forces $\bar F(0)=\bar F(1)=0$, since a nonzero scalar cannot annihilate a nonzero idempotent. Factor $\bar F=(T-1)^a\bar H$, with $a\ge1$, $\bar H(1)\ne0$ and $\bar H(0)=0$. Lemma D3.1 lifts this coprime factorization after an elementary étale extension. Bezout gives an idempotent in the quotient by $F$, equal to one in the factor for $(T-1)^a$ and zero in the other. Evaluation at $b$ gives an idempotent $e$ of $D\otimes_RR'$ whose special-fibre image is $e_0$: its residue polynomial takes value one at $1$ and zero at $0$.

All the data used so far are finite: the coefficients of $F$, the lift $b$, the equality $F(b)=0$, and the coefficient equations and Jacobian. Clear their finitely many denominators outside $\mathfrak p$, and one further denominator to kill any equality error. The construction is then defined over $R_a$ for one $a\notin\mathfrak p$. Its coefficient algebra, including its inverted Jacobian, is étale over $R_a$ and therefore over $R$, and the chosen point has residue $\kappa(s)$. Thus it is an actual elementary étale neighbourhood of the original affine base, not only a ring over $R_{\mathfrak p}$.

The component $\operatorname{Spec}(e(D\otimes_RR'))$ is finite over $R'$ and its special fibre is precisely the local Artinian factor for $x$. Its complement of $Y_{R'}$ is closed. Its image in $\operatorname{Spec}R'$ is closed, by the full closed-image proof for finite morphisms, and avoids the selected base point. Shrink to a principal base neighbourhood avoiding that image. The whole finite component now lies in $Y_{R'}$. Call it $V$. It is open in the completion and hence in $Y_{R'}$ and $X_{R'}$, finite over the shrunk base, with the required unique point and unchanged residue field.

Under a further elementary neighbourhood the selected fibre is identified with its old fibre, since the base residue field is unchanged. Finiteness and openness survive base change. This proves the final assertion. $\square$

**Proposition D3.3 (several finite pieces and the separated decomposition).** For distinct isolated points $x_1,\ldots,x_n$ in $X_s$, a single elementary étale neighbourhood admits finite open pieces $V_i$ with the properties of Lemma D3.2 for all $i$. If $f$ is separated, after shrinking that neighbourhood there is a decomposition

$$
X_T=W\amalg V_1\amalg\cdots\amalg V_n                                  \tag{3.1}
$$

into open-and-closed subschemes, and $W_t$ has no point mapping to any $x_i$.

**Proof.** Construct the pieces successively. At each elementary neighbourhood the fibre is the original fibre, so the next point is uniquely identified and still isolated; Lemma D3.2's final assertion preserves all earlier pieces. Finite induction gives a common neighbourhood.

For a separated map, each finite $T$-scheme $V_i$ is also closed in $X_T$. Indeed its graph into $V_i\times_TX_T$ is closed by separatedness of $X_T/T$, and the projection of this graph to $X_T$ is finite, being a closed immersion followed by the base change of the finite map $V_i\to T$. Its image, which is $V_i$, is closed.

The intersections $V_i\cap V_j$ are closed in the finite $T$-scheme $V_i$ and have empty fibre at the chosen base point, because the original $x_i$ are distinct. Their finitely many closed images in $T$ can all be avoided by a further principal shrink. The pieces are then disjoint and open-and-closed. Their complementary open-and-closed scheme is $W$. Each original $x_i$ has exactly one point above it in the elementary fibre and that point belongs to $V_i$, so none belongs to $W_t$. $\square$

**Proposition D3.4 (separable residue extension before the finite splitting).** Without separatedness, one can instead choose an étale neighbourhood $(T,t)$ with finite separable residue extension so that, above each $x_i$, all points $y_{ij}$ have finite purely inseparable residue extension over $\kappa(t)$ and each has a finite open piece over $T$.

**Proof.** Put $k=\kappa(s)$ and $K_i=\kappa(x_i)$, finite over $k$ by the isolated fibre criterion. In characteristic $p>0$, for each generator of $K_i/k$ its minimal polynomial is a separable polynomial in $T^{p^a}$. Thus a sufficiently high $p$-power of each generator is separable over $k$. These powers generate a finite separable subextension over which $K_i$ is purely inseparable. In characteristic zero take $K_i$ itself. Let $L/k$ be a finite Galois extension containing the separable subextensions for all $i$; construct it by successively adjoining all roots of their finitely many separable minimal polynomials.

Lift the monic minimal polynomial of a primitive generator of $L/k$ to coefficients over a principal neighbourhood of $s$. Invert its derivative and select the point evaluating the generator to that element of $L$. This gives an étale neighbourhood with residue field $L$. The fibre above $x_i$ is the spectrum of $K_i\otimes_kL$. The separable intermediate algebra splits as a product of copies of $L$: its distinct embeddings supply the factorization of the separable minimal polynomials and the Chinese remainder isomorphism. In each resulting factor the remaining equations are purely inseparable power equations. Each has a unique root in an algebraic closure, so every factor has exactly one prime and its residue is finite purely inseparable over $L$. Nilpotents in these tensor products are allowed.

The finitely many resulting points are isolated: base change of a finite-dimensional open fibre algebra is still finite-dimensional. Apply the multiple-piece part of Proposition D3.3 to all of them, using a further elementary neighbourhood with unchanged residue $L$. Its finite pieces have the stated residues, and their points exhaust all points above the selected $x_i$. $\square$

### D4. Relative integral closure through étale base change

**Lemma D4.1 (the derivative coefficient identity).** Let $F\in R[T]$ be monic of degree $d$, let $R\to B$ be a ring map, and let $h\in B[T]/F$ be integral over $R$. The unique degree-below-$d$ representative of $F'h$ has all coefficients integral over $R$.

**Proof.** Construct a splitting extension of $B$ by adjoining one root of $F$, dividing by its monic linear factor, adjoining a root of the remaining monic polynomial, and continuing. At every step the quotient by a monic polynomial is finite free with a basis containing $1$. Thus the composite $B\subset B'$ is an injective finite free extension and

$$
F(T)=\prod_{i=1}^d(T-\alpha_i)\quad\text{in }B'[T].
$$

Every $\alpha_i$ satisfies $F$, so is integral over $R$. Write $h=\sum_{j<d}h_jT^j$. In $B'[T]/F$ the identity is

$$
F'h=\sum_{i=1}^dh(\alpha_i)\prod_{j\ne i}(T-\alpha_j).                 \tag{4.1}
$$

Here is a proof covering repeated roots and nilpotents. First put independent variables $\alpha_i,h_j$ in the domain $\mathbf Z[\alpha_1,\ldots,\alpha_d,h_0,\ldots,h_{d-1}]$. Reduce the left side by the monic $F$; both sides then have degree below $d$. Their difference evaluates to zero at every $\alpha_i$, because $F'(\alpha_i)=\prod_{j\ne i}(\alpha_i-\alpha_j)$. The Vandermonde determinant is a nonzero polynomial in this domain. In its fraction field it is invertible, forcing the difference to be zero. Injectivity into that field proves the polynomial identity over the universal domain. Specialization gives (4.1) over every ring, including when that determinant becomes zero.

A monic equation for $h$ over $R$ evaluates to the same monic equation for each $h(\alpha_i)$ over $R$. Hence each is integral over $R$. Integral elements form a ring, so the coefficients on the right side of (4.1) are integral over $R$. They are the coefficients of the monic remainder on the left, which already belong to $B$. A monic equation for such a coefficient in $B'$ holds in $B$ by the displayed injection. $\square$

**Theorem D4.2 (étale base change for integral closure).** Let $R\to P$ be étale, let $R\to B$ be any ring map, and let $A\subset B$ be the integral closure of the image of $R$. Then

$$
P\otimes_RA\ \cong\
\{\text{elements of }P\otimes_RB\text{ integral over }P\}.             \tag{4.2}
$$

**Proof.** The left side injects into $P\otimes_RB$ by flatness from Lemma D2.3. Every element of the left side is integral over $P$, since it is built from finitely many base changes of integral elements.

It remains to prove surjectivity, which may be checked on the principal cover of $\operatorname{Spec}P$ from Lemma D2.2. Indeed integral closure commutes with localization, and a module whose localizations on that cover vanish is zero. Thus assume $P=(R[T]/F)_g$, with $F$ monic and $F'$ invertible there.

Put $C=R[T]/F$ and $D=B[T]/F$. If $A''$ is the integral closure of $C$ in $D$, localization of integral closure says that the right side of (4.2) is $(A'')_g$. An element $a\in A''$ is integral over $R$, by transitivity, since $C$ is finite over $R$. Lemma D4.1 writes the monic remainder of $F'a$ with coefficients in $A$. Consequently $F'a$ belongs to the image of $A[T]/F$. After localization, $F'$ is a unit from $P$, so $a$ belongs to $P\otimes_RA$. Dividing by powers of $g$ gives the same assertion for all elements of $(A'')_g$. $\square$

Let now $f:X\to S$ be quasi-compact and quasi-separated. On $V=\operatorname{Spec}R\subset S$, its inverse image is qcqs. The finite-cover localization proof in the earlier quasi-coherent-sheaf lesson gives

$$
\Gamma(f^{-1}V,\mathcal O_X)_a
=\Gamma(f^{-1}D(a),\mathcal O_X).
$$

Thus $f_*\mathcal O_X$ is quasi-coherent. Taking the integral closure of $R$ in these section algebras commutes with localization, by the full algebraic localization theorem. The closures therefore form a quasi-coherent integral $\mathcal O_S$-algebra $\mathcal A$. Define

$$
Z=\operatorname{Spec}_S\mathcal A,\qquad
X\xrightarrow{j}Z\xrightarrow{\nu}S.                                 \tag{4.3}
$$

The map $j$ is induced by $\mathcal A\subset f_*\mathcal O_X$ and evaluation, using the proved relative-Spec universal property. The map $\nu$ is integral. This is **relative integral closure**; it retains nilpotents and is not a reduced normalization.

**Corollary D4.3 (the scheme compatibility).** For an étale morphism $S_1\to S$, the base change $Z_{S_1}$ in (4.3) is the relative integral closure of $S_1$ in $X_{S_1}$.

**Proof.** Work on compatible affine base charts $R\to P$. Since $P$ is flat, the finite-cover equalizer for sections on the qcqs scheme $f^{-1}V$ stays exact after tensoring by $P$. Its chart and overlap terms become the corresponding section modules after base change. Hence

$$
P\otimes_R\Gamma(f^{-1}V,\mathcal O_X)
=\Gamma((f^{-1}V)_P,\mathcal O).
$$

This is also the degree-zero case of the full flat cohomology base-change proof already in [Algebra and sheaf cohomology before reductive groups](AG-RG-S01.md), Section 6. Theorem D4.2 identifies the integral subalgebra after this base change with $P\otimes_RA$. Relative Spec commutes with base change by its earlier construction. These canonical chart identifications agree on all restrictions and glue to the asserted identification. $\square$

### D5. Descending the local isomorphism

**Lemma D5.1 (isomorphisms descend along an étale cover).** If $g:Y\to Z$ becomes an isomorphism after a surjective étale base change $P\to Z$, then $g$ is an isomorphism.

**Proof.** The inverse of the base-changed isomorphism gives a map $\sigma_P:P\to Y$ over $Z$. Its two pullbacks to $P\times_ZP$ coincide: they are both inverses to the same base-changed isomorphism. We describe the descent of this compatible map using only faithfully flat affine algebra.

First, if $R\to A$ is faithfully flat, then

$$
0\longrightarrow M\longrightarrow A\otimes_RM
\longrightarrow A\otimes_RA\otimes_RM,\quad
a\otimes m\longmapsto1\otimes a\otimes m-a\otimes1\otimes m             \tag{5.1}
$$

is exact for every $R$-module $M$. After tensoring by $A$, multiplication of the first two $A$ factors retracts the first map. For a tensor in the kernel of the second map, multiplication of those first two factors in its kernel equation expresses that tensor as the first-map image of its retraction. Thus the tensored sequence is exact. Flatness and faithfulness detect its kernels and quotient, proving (5.1).

Every affine open $W=\operatorname{Spec}R$ of $Z$ has a finite affine refinement of its étale cover: affine source neighbourhoods have open images by Lemma D2.3, and quasi-compactness of $W$ selects finitely many of them. Their disjoint union is $\operatorname{Spec}A$, flat and surjective over $W$, hence faithfully flat. For the last assertion, any nonzero module contains a nonzero cyclic submodule $R/I$; a point above a maximal ideal containing $I$ makes $IA$ proper, and flatness preserves the cyclic submodule's injection.

Points of this cover above the same point of $W$ have a common point on their fibre product, because the tensor product of their two residue fields over the base residue field is nonzero. Compatibility therefore gives a well-defined set map $\sigma:W\to Y$. The cover is open and surjective, so it is a quotient map; the compatibility makes the inverse image of an open of $Y$ invariant, and its image is the inverse image under $\sigma$. This proves continuity.

Around any point of $W$ choose a principal neighbourhood $D(r)$ whose image under $\sigma$ lies in an affine open $\operatorname{Spec}B$ of $Y$. The coefficient map $B\to A_r$ has equal two pullbacks to $A_r\otimes_{R_r}A_r$. Formula (5.1), with $M=R_r$, factors it uniquely through $R_r$. It defines the desired local scheme map. The local maps agree on overlaps by the same faithful equalizer and glue. On each affine base open the map recovers $\sigma_P$ after pullback, so those descended maps also agree on overlaps of the base opens.

We obtain $\sigma:Z\to Y$ with $g\sigma=\mathrm{id}_Z$. Its composite $\sigma g$ becomes $\mathrm{id}_Y$ after the surjective étale cover pulled back to $Y$. Equality of scheme maps can be checked there by the same affine equalizer and open-target argument just used. Hence $\sigma g=\mathrm{id}_Y$. $\square$

This is the earlier affine descent block in block A above, Lemmas A1.1 and A1.5, specialized with its proof to étale covers. It does not use effectivity of separated locally quasi-finite descent or any algebraic space.

**Theorem D5.2 (relative Zariski Main).** Let $f:X\to S$ be finite type and separated, and let (4.3) be its relative integral closure. If $U\subset X$ is its quasi-finite locus, then $U'=j(U)$ is open in $Z$,

$$
j^{-1}(U')=U,\qquad U\xrightarrow{\sim}U'.                            \tag{5.2}
$$

**Proof.** Theorem C5.1 proves that $U$ is open. Fix $x\in U$, with image $s$. Proposition D3.3 gives an elementary étale neighbourhood $T\to S$ and a decomposition

$$
X_T=V\amalg W,\qquad V\to T\text{ finite},\quad (x,t)\in V.
$$

The relative integral closure of $T$ in $X_T$ is $V\amalg W'$, where $W'$ is the relative integral closure of $T$ in $W$. On an affine base chart its section algebra is a product $D\times B$, with $D$ finite over the base ring. The integral subalgebra is exactly $D\times C$, where $C$ is the integral subalgebra of $B$. Membership implies componentwise integrality by projection. Conversely the product of two monic annihilating polynomials annihilates the pair, proving membership. Since every element of $D$ is integral, its component is unchanged. Taking relative spectra gives the asserted disjoint union.

Corollary D4.3 identifies this closure with $Z_T$. Thus the clopen target component $V\subset Z_T$ has full inverse image $V\subset X_T$, mapping isomorphically onto it. The image $O\subset Z$ of that component is open by étale openness, and contains $j(x)$. Its map $V\to O$ is a surjective étale cover. The pullback of $j^{-1}(O)\to O$ along this cover is precisely the isomorphism just obtained. Lemma D5.1 makes $j^{-1}(O)\to O$ an isomorphism.

Every point of $j^{-1}(O)$ is quasi-finite over $S$. Indeed $O$ is locally finite type over $S$ by this isomorphism with an open of $X$, and it is open in the integral $S$-scheme $Z$. Integral fibre algebras are integral over a field, so all their prime quotients are algebraic fields and all primes are maximal, by Lemma P0.4. An affine locally finite-type chart in such a fibre is a zero-dimensional Noetherian algebra, hence Artinian and discrete by Lemma P0.9. Its residue fields are finite by Lemma P0.9. The isolated fibre criterion therefore gives quasi-finiteness.

The opens $O$ constructed for all $x\in U$ consequently have full inverse images contained in $U$; they cover $j(U)$ and their inverse images cover $U$. Their isomorphisms are restrictions of the same map $j$ and agree on overlaps. Taking their union proves all three assertions in (5.2). $\square$

**The scope of quasi-compactness.** Let $A=k[t_1,t_2,\ldots]$, $I=(t_1,t_2,\ldots)$ and $B=A[z]/(Iz)$. Over a prime not containing $I$, the fibre of $\operatorname{Spec}B\to\operatorname{Spec}A$ is the single reduced point $z=0$. Over a prime containing $I$, the fibre is an affine line, with no isolated point. Hence its quasi-finite locus is the copy of $D(I)=\bigcup_iD(t_i)$ at $z=0$. This is not quasi-compact: given finitely many indices, the prime generated by those variables avoids an unselected variable and belongs to none of the selected opens. This finite-type separated affine example shows why Theorem D5.2 asserts an open immersion without adding quasi-compactness.

### D6. Finite integral subalgebras and finite-stage immersions

We first reproduce the exact finite-submodule argument already proved in *Quasi-coherent sheaves on schemes*, Sections D3–D4, so its arbitrary qcqs scope is explicit.

**Lemma D6.1 (finite submodules on a qcqs scheme).** Let $S$ be qcqs, let $\mathcal F$ be quasi-coherent, let $Q\subset S$ be a quasi-compact open, and let $\mathcal G\subset\mathcal F|_Q$ be a finite-type quasi-coherent submodule. It extends to a finite-type quasi-coherent submodule of $\mathcal F$. Every $\mathcal F$ is the directed union of its finite-type quasi-coherent submodules.

**Proof.** Pushforward by the quasi-compact open immersion $i:Q\hookrightarrow S$ preserves quasi-coherence. This follows from the finite-cover localization calculation: over an affine chart of $S$, its intersection with $Q$ is qcqs; finite affine covers of that intersection and its overlaps identify sections on a principal subopen with localization. The affine module–sheaf correspondence then identifies the pushforward with the sheaf of its section module.

If $S=\operatorname{Spec}R$, the kernel

$$
\mathcal H=\ker\bigl(\mathcal F\longrightarrow
i_*(\mathcal F|_Q/\mathcal G)\bigr)
$$

is quasi-coherent, lies in $\mathcal F$ and restricts to $\mathcal G$. Write $\mathcal H=\widetilde N$. Cover $Q$ by finitely many principal opens $D(a_j)$. Each $N_{a_j}$ is finite because its associated sheaf there is finite type; this affine implication follows by selecting finitely many principal local generating sets and testing the quotient by their numerators. Choose numerators for finite generating sets of all $N_{a_j}$ and let $N_0\subset N$ be their finite span. Then $(N_0)_{a_j}=N_{a_j}$, so $\widetilde{N_0}$ is the required extension.

For general $S$, add finitely many affine opens to $Q$. At each step the intersection with the already treated quasi-compact open is quasi-compact by quasi-separatedness. Apply the affine construction on the newly added affine, and glue along equality of the two submodules inside $\mathcal F$. Finite induction gives the extension.

Finally any germ of $\mathcal F$ is represented on an affine neighbourhood. Its cyclic submodule there is finite type and extends by the assertion just proved. Thus these submodules exhaust every stalk. Their family is directed under sums, since the image of a finite direct sum remains quasi-coherent and finite type. Stalkwise exhaustion proves their directed union is $\mathcal F$. $\square$

**Lemma D6.2 (the finite subalgebras actually needed).** An integral quasi-coherent $\mathcal O_S$-algebra $\mathcal A$ on a qcqs scheme is the directed union of its finite quasi-coherent subalgebras.

**Proof.** For a finite-type quasi-coherent submodule $\mathcal N\subset\mathcal A$, form the image $\mathcal A_{\mathcal N}$ of $\operatorname{Sym}(\mathcal N)\to\mathcal A$. Images, sums, tensor powers and their direct sums are quasi-coherent by their affine module descriptions. Hence this image is a quasi-coherent subalgebra of finite algebra type. On any affine chart, finitely many generators of $\mathcal N$ are integral over the base. Their finitely many monic equations bound their powers, so their bounded monomials span $\mathcal A_{\mathcal N}$ as a module. It is therefore finite on every affine chart.

By Lemma D6.1 each local section lies in one such $\mathcal N$, and hence in one finite subalgebra. Two finite subalgebras lie in the finite subalgebra generated by their sum: their sum is a finite-type submodule, and the same integral-generator argument applies. This proves the directed union. $\square$

This proves the entire part of the finite integral approximation theorem consumed here. No approximation by finitely presented **algebras**, and no assumption of finite presentation of $X/S$, is used.

**Lemma D6.3 (finite-stage closed immersions and immersions).** Let $Z=\varprojlim_i Z_i$ be a directed limit over a scheme $S$, with affine transition maps, and let $Y\to Z$ be an $S$-map.

1. If it is a closed immersion, all $Z_i$ are quasi-compact, and $Y$ is locally finite type over $S$, then $Y\to Z_i$ is a closed immersion eventually.
2. If it is an immersion, all $Z_i$ are quasi-separated, $Y$ is quasi-compact and locally finite type over $S$, then $Y\to Z_i$ is an immersion eventually.

**Proof.** For the first assertion choose one stage and a finite affine cover whose members map into affine opens $\operatorname{Spec}R$ of $S$. Their inverse images at later stages and the limit are affine, since the transitions and projections are affine. The inverse image $V\subset Y$ of each such chart is closed in its affine limit, hence affine and quasi-compact. It is locally finite type over $\operatorname{Spec}R$, hence its ring $B$ is a finitely generated $R$-algebra, by the proved affine finite-type criterion.

Writing the coordinate rings of the chart system as $C_i$ and its limit as $C=\varinjlim_iC_i$, the closed immersion gives a surjection $C\to B$. A finite $R$-algebra generating list of $B$ has preimages represented in one common $C_i$. Thus $C_i\to B$ is surjective at that stage and at all later stages. Applying this to finitely many charts at once proves the eventual closed immersion. No finite relation list for $B$ was required.

For the second assertion fix a stage $i_0$. Quasi-compactness of $Y$ lets us choose a quasi-compact open $Z'_{i_0}\subset Z_{i_0}$ containing its image. Replace later stages by its inverse images. They are now qcqs, and the map still factors through their limit $Z'$. An immersion is closed in some open of its target. Choose a quasi-compact open $O\subset Z'$ containing $Y$ inside that open, using finitely many affine neighbourhoods of its image. The immersion $Y\to O$ is closed.

The full finite-open-data proof in the earlier limits lesson, Lemma D2.1, gives a quasi-compact stage open $O_i\subset Z_i'$ whose inverse image is $O$. Its later inverse images have affine transition maps. The first part applied to $Y\to O$ gives a closed immersion $Y\to O_i$ eventually. Composing with the open immersion $O_i\hookrightarrow Z_i$ proves the assertion. $\square$

The finite-open-data proof just used needs no Noetherian hypothesis: on a finite affine cover of a qcqs stage, a quasi-compact limit open is a finite union of principal opens with finitely many defining elements. Represent these at a common stage. Equal inverse-image opens eventually agree, since their finitely generated ideals have the same radical in the colimit and the finitely many power-membership equations hold at a common stage. This also proves that a finite stage-open covering at the limit eventually covers the stage. These are exactly the local calculations in the earlier complete proof.

### D7. The finite completion over a qcqs base

**Theorem D7.1 (general finite factorization).** If $S$ is qcqs and $f:X\to S$ is quasi-finite and separated, then

$$
X\ \lhook\joinrel\longrightarrow\ \overline X\ \longrightarrow S
$$

factors $f$ as a quasi-compact open immersion followed by a finite morphism. The scheme $S$ is arbitrary qcqs; $X/S$ need not be finitely presented.

**Proof.** Theorem D5.2 identifies all of $X$ with an open subscheme of $Z=\operatorname{Spec}_S\mathcal A$, since every point is quasi-finite. The algebra $\mathcal A$ is integral. By Lemma D6.2 write

$$
\mathcal A=\varinjlim_i\mathcal A_i,\qquad
Z_i=\operatorname{Spec}_S\mathcal A_i,
$$

where each $\mathcal A_i\subset\mathcal A$ is a finite quasi-coherent subalgebra. Each $Z_i$ is finite over $S$, hence qcqs. Their transition morphisms are affine. On affine base charts, the elementary spectrum-of-a-ring-colimit construction gives $Z=\varprojlim_iZ_i$; the chart identifications glue by relative Spec.

The source $X$ is quasi-compact because $f$ is quasi-compact and $S$ is quasi-compact, and it is locally finite type by quasi-finiteness. Lemma D6.3 makes the induced map $j_i:X\to Z_i$ an immersion at some stage. We now show it is open, a step not supplied by the limit lemma alone.

By definition of immersion there is an open $O\subset Z_i$ in which $X$ is closed. Work over an affine base chart $\operatorname{Spec}R\subset S$, and put $C=\mathcal A_i(\operatorname{Spec}R)$ and $B=\Gamma(X_R,\mathcal O)$. The map $C\to B$ is injective, since $\mathcal A_i$ is an actual subalgebra of $\mathcal A\subset f_*\mathcal O_X$. Cover $O\cap\operatorname{Spec}C$ by principal opens $D_C(c)$ contained in it. The qcqs localization formula gives

$$
\Gamma((X_R)_c,\mathcal O)=B_c,
$$

and exact localization preserves the injection $C_c\hookrightarrow B_c$. But the closed immersion into $O$ makes this same ring map a surjection, with kernel its defining ideal on $D_C(c)$. Hence that ideal is zero and the map is an isomorphism. These principal charts cover $O$ over all base affines. Therefore the closed immersion $X\to O$ is an isomorphism, and $j_i$ is an open immersion. Take $\overline X=Z_i$.

Finally this open immersion is quasi-compact. The scheme $\overline X$ is quasi-separated, and its open image is homeomorphic to the quasi-compact scheme $X$. Its intersection with every affine open of $\overline X$ is therefore quasi-compact. This is exactly quasi-compactness of the open immersion. $\square$

**Corollary D7.2 (the relative quasi-affine conclusion).** Every quasi-finite separated morphism of schemes is quasi-affine, without a quasi-compactness assumption on the base.

**Proof.** The relative integral closure $Z\to S$ is affine, and Theorem D5.2 embeds $X$ openly in $Z$. This open immersion is quasi-compact locally on $S$: over an affine base chart, $X$ is quasi-compact by quasi-finiteness, and the target $Z$ is affine, hence quasi-separated. Thus the open immersion is quasi-compact. It is a quasi-compact open immersion into an affine $S$-scheme, which is the relative quasi-affine assertion. If $S$ is qcqs, Theorem D7.1 strengthens the affine target to a finite one. $\square$

**Corollary D7.3 (proper quasi-finite morphisms).** A proper quasi-finite scheme morphism is finite over an arbitrary base.

**Proof.** The claim is local on the target, so take an affine target. Theorem D7.1 gives an open immersion $j:X\hookrightarrow Z$ with $Z$ finite over the target $S$. The map $j$ is proper: its graph into $X\times_SZ$ is closed because $Z/S$ is separated, and the projection to $Z$ is proper by base change of $X/S$. Thus its open image is also closed, by the closed-image part of properness. An open immersion with closed image identifies $X$ with a clopen subscheme of $Z$, hence with a direct factor of its finite coordinate algebra. That factor is finite over the base. These affine target conclusions glue to finiteness. $\square$

**Corollary D7.4 (normal birational target).** A quasi-finite separated birational morphism of integral schemes with normal target is an open immersion.

**Proof.** Restrict to an affine normal target $S=\operatorname{Spec}R$, and put $K=\operatorname{Frac}R$. Birationality identifies the function field of $X$ with $K$. Every regular section on $X$ injects into $K$: on each nonempty affine open its coordinate domain injects into the common function field, and restrictions agree there. The relative integral algebra is therefore an $R$-subalgebra of $K$. Its elements integral over $R$ are precisely $R$, by normality; the pullback inclusion supplies all of $R$. The relative integral closure is thus $S$ itself. Every point of $X$ is quasi-finite, so Theorem D5.2 identifies $X$ with an open of $S$. This argument applies on every affine target open, and the canonical open immersions agree on overlaps, proving the assertion. $\square$

## Free sources and the proof order

The freely accessible writing material is the Stacks Project's [maps between étale algebras, Tag 00U7](https://stacks.math.columbia.edu/tag/00U7), [monic étale neighbourhoods, Tag 00UE](https://stacks.math.columbia.edu/tag/00UE), [finite elementary étale pieces, Tags 02LK–02LN](https://stacks.math.columbia.edu/tag/02LN), [integral-closure derivative identity, Tag 03GD](https://stacks.math.columbia.edu/tag/03GD), [étale integral-closure base change, Tag 03GE](https://stacks.math.columbia.edu/tag/03GE), [polynomial coefficient argument, Tag 03GG](https://stacks.math.columbia.edu/tag/03GG), [scheme base change, Tag 03GV](https://stacks.math.columbia.edu/tag/03GV), [relative Zariski Main, Tag 03GW](https://stacks.math.columbia.edu/tag/03GW), [finite integral subalgebras, Tag 0817](https://stacks.math.columbia.edu/tag/0817), and [finite-stage immersions, Tag 081B](https://stacks.math.columbia.edu/tag/081B). Full local source texts and the GFDL accompany the draft. These references identify sources for writing and comparison; the proofs consumed above are in this lesson or the exact earlier programme texts.

The logical order of the proofs is: the elementary ring, affine-sheaf, field-algebra and integral-extension proofs; Section B1 of this lesson; Theorem C4.3; Section D2 here; the earlier complete henselian splitting proof, if used; Sections D3–D4 here; the earlier affine faithfully flat descent block; Sections D5–D7 here; and only then separated locally quasi-finite scheme effectivity, algebraic-space recognition and normalized space factorization. In particular the latter three results never justify a step in this lesson.

## E. Locally quasi-finite effectivity and space recognition

### E4. Two finite scheme facts and the étale finite piece

**Lemma E4.1.** A finite monomorphism of schemes is a closed immersion, without a Noetherian or finite-presentation assumption.

**Proof.** Over an affine target write $R\to B$, with $B$ a finite $R$-module. The monomorphism says that multiplication $B\otimes_R B\to B$ is an isomorphism. For every residue field $k$ of $R$, the finite-dimensional $k$-algebra $E=B\otimes_R k$ therefore satisfies $E\otimes_k E=E$. Its vector-space dimension $d$ satisfies $d^2=d$, so it is either zero or one. In the latter case its unit identifies it with $k$. In either case $k\to E$ is surjective. The finite cokernel of $R\to B$ consequently has zero fibre at every maximal ideal. Nakayama kills its localization at each maximal ideal, and a module with all such localizations zero is zero. Hence $R\to B$ is surjective, proving the closed immersion. $\square$

**Lemma E4.2.** A finite étale scheme morphism is finite locally free.

**Proof.** On affine charts let $R\to B$ be finite, flat and finitely presented as an algebra. Pick algebra generators $b_i$. Each is integral by the finite-module determinant argument. Choose monic equations $P_i(b_i)=0$. The algebra $C=R[T_i]/(P_i(T_i))$ is finite free, with basis the bounded monomials. A finite presentation of $B$ as an algebra says that the kernel of $C\to B$ is a finitely generated ideal: lift its finite defining relations to the polynomial algebra and add the finitely many $P_i$. The products of its ideal generators with the bounded monomial basis generate it as an $R$-module. Thus $B$ is finitely presented as an $R$-module. Flatness and Lemma A1.3 make it finite locally free. $\square$

**Lemma E4.3 (finite piece without flatness).** Let $T$ and $U$ be affine schemes and let $U\to T$ be quasi-finite. For $u\in U$, with image $p\in T$, there are an affine elementary étale neighbourhood $(T',p')\to(T,p)$ and a clopen subscheme $U'\subset U_{T'}$, finite over $T'$, having a point above $u$. One may arrange that $U'_{p'}=U_p$ under $\kappa(p')=\kappa(p)$.

**Proof.** The fibre $U_p$ is a finite scheme over $\kappa(p)$: its coordinate algebra is finite type of dimension zero, hence Artinian, and its residue fields are finite, by the earlier field-algebra and quasi-finite fibre proofs. List all its finitely many points as $u_1,\ldots,u_n$. Proposition D3.3 applies to the separated affine morphism $U\to T$ and all these isolated fibre points. It supplies a single elementary étale neighbourhood with disjoint clopen finite pieces $V_i\subset U_{T'}$, each containing the unique point above $u_i$, and complementary clopen piece $W$ whose selected fibre has no point above any $u_i$. Thus $W_{p'}$ is empty. Take $U'=\coprod_iV_i$. It is finite, clopen and has the whole selected fibre. Shrink the elementary neighbourhood to an affine principal neighbourhood of its marked point; all these properties persist. Its residue field equals $\kappa(p)$ by the elementary-neighbourhood construction, giving the claimed equality of fibres and a point above the original $u$. No flatness or finite presentation of the finite completion is used. $\square$

### E5. Effective separated locally quasi-finite scheme descent

Theorems D5.2 and D7.1, and Corollary D7.2, have already proved the **general scheme Zariski Main theorem**: a quasi-finite separated morphism to a qcqs scheme is an open subscheme of a finite scheme over that base, and consequently is quasi-affine. Their proofs appear in block D above and use no theorem on algebraic spaces or separated locally quasi-finite scheme effectivity.

**Theorem E5.1.** Let $\{X_i\to S\}$ be an fppf covering. A scheme datum $(V_i/X_i,\phi_{ij})$ whose structure maps are separated and locally quasi-finite is effective as a scheme. The descended morphism is separated and locally quasi-finite. No quasi-compactness of the local objects or the result is assumed.

**Proof for a single affine cover.** First take $S=\operatorname{Spec}R$ and $X=\operatorname{Spec}A$, with $X\to S$ faithfully flat and finitely presented. Let $V\to X$ be separated and locally quasi-finite, with datum $\phi:V\times_S X\to X\times_S V$. For each affine open $W^1\subset V$ put

$$
W=\operatorname{pr}_V\bigl(\phi(W^1\times_S X)\bigr)\subset V.
$$

The projection is a base change of the flat finitely presented cover, hence is open; its image $W$ is open. It is quasi-compact, being the image of the affine scheme $W^1\times_S X$. Diagonal normalization of the datum gives $W^1\subset W$.

The cocycle makes $W$ invariant. One can check this on points after common residue-field extensions: membership in $W$ means being joined by the descent relation to a point of $W^1$; a further relation arrow composes with that arrow. Conversely use the inverse arrow. Equivalently, on every test scheme local lifts of such arrows can be refined and composed, giving the equality of opens

$$
\phi(W\times_S X)=X\times_S W.
$$

Thus $W$ carries the restricted datum. Its map to the affine scheme $X$ is quasi-compact, separated and locally quasi-finite, hence quasi-finite and separated. Scheme Zariski Main makes $W/X$ quasi-affine. Theorem A3.1 descends $W$ effectively to a quasi-affine scheme $U_W/S$.

These invariant $W$ cover $V$, because the original affine $W^1$ do. For two of them, $W\cap\widetilde W$ is an invariant open of each. Lemma A1.6 descends this open inside $U_W$ and $U_{\widetilde W}$; Lemma A1.5 descends the comparison isomorphism and its inverse. The comparisons satisfy the triple equation after the cover and hence before it. Ordinary open gluing produces a scheme whose pullback is $V$, with its original datum. This step does not require the intersections to be affine, nor invoke Theorem E5.1 recursively.

**General fppf families and arbitrary bases.** On an affine open of $S$, affine pieces of covering members have open images, because their maps are flat and locally finitely presented. Finitely many such images cover this quasi-compact affine open. Their finite disjoint union is an affine faithfully flat finitely presented cover. Pullback preserves separatedness and local quasi-finiteness, and the disjoint union retains them. The preceding construction applies. On every original member the comparison isomorphisms descend after this refinement by Lemma A1.5; their inverses descend too. Repeat on affine base opens, compare on affine opens of intersections using the original data, and glue. This constructs the effective scheme datum over any $S$.

For completeness its stated properties also descend. Closedness of the diagonal follows from Corollary A3.2 after the covering. Local finite type descends by the following affine argument: if $A\otimes_R B$ is generated by finitely many elements as an $A$-algebra, collect their finitely many $B$ components; the algebra they generate in $B$ has quotient module killed by faithfully flat tensoring, so is all of $B$. Apply this to affine charts of the existing descended scheme. On a residue-field fibre over $k$, choose a field extension $L/k$ induced by a point of the covering. The whole pulled-back fibre is locally quasi-finite over $L$. Let $\operatorname{Spec}B$ be an affine open in the original fibre; $B$ is a finite-type $k$-algebra. If $B$ had a strict prime chain $\mathfrak q\subsetneq\mathfrak q'$, faithful flatness of $B\to B\otimes_kL$ would give a prime above $\mathfrak q'$, and the flat local going-down argument of Lemma A1.4 would give a smaller prime above $\mathfrak q$. This would be a strict chain in the pulled-back fibre. Such a chain is impossible there: local quasi-finiteness makes every point isolated in that fibre, and a distinct generalization belongs to every neighbourhood of a point. Thus $B$ has dimension zero. Hilbert basis makes $B$ Noetherian, and Lemma P0.9 makes its spectrum a finite discrete set with finite residue fields over $k$. Each original fibre point is consequently isolated with finite residue extension. The finite-type fibre criterion stated before Lemma C3.1 proves local quasi-finiteness of the descended morphism. $\square$

### E6. The finite affine quotient used in recognition

**Theorem E6.1.** Let $P\rightrightarrows U=\operatorname{Spec}A$ be a scheme equivalence relation, with both projections finite locally free. Write $P=\operatorname{Spec}B$, let $s,t:A\to B$ be its endpoint maps, and set

$$
C=\{a\in A:s(a)=t(a)\}.
$$

Then $A$ is faithfully flat finite locally free over $C$, $B=A\otimes_C A$ through the endpoint maps, and $\operatorname{Spec}C$ represents the fppf quotient $U/P$ on all test schemes.

**Proof.** The empty object has the empty quotient, so suppose $U\ne\varnothing$. The identity section makes each source fibre nonempty. The rank of $B$ over $A$ through $s$ is therefore positive, locally constant, and invariant under the relation. Invariance follows because composition with an arrow identifies the two source fibres, after base change to the scheme of arrows. The rank strata are finitely many clopen subsets of the affine quasi-compact $U$. Their idempotents have equal pullbacks under $s,t$ (equality of the clopen subsets is equality of their idempotents), so lie in $C$. Decompose by them and assume the rank is $r>0$.

For $a\in A$, multiplication by $t(a)$ on the finite locally free $s(A)$-module $B$ has a characteristic polynomial. All its coefficients lie in $C$. Indeed composition gives an isomorphism, over the entire arrow scheme, between the two pulled-back source-fibre bundles, preserving target evaluations. It conjugates their multiplication operators. Characteristic polynomials commute with base change and conjugation, so the two coefficient pullbacks agree as functions, including nilpotents. Cayley–Hamilton follows on local free charts from the adjugate identity and hence globally. Apply the identity section to its equation: $a$ satisfies a monic polynomial over $C$. Thus $C\subset A$ is integral and has surjective spectrum by lying over. The same conjugation proves that

$$
N(a)=\det_s(\text{multiplication by }t(a)\text{ on }B)\in C.
$$

The endpoint map $P\to U\times_{\mathbf Z}U$ is finite: factor it as the closed graph of the second endpoint, followed by the base change of the finite first projection. The graph is closed because an affine scheme is separated over $\mathbf Z$. This endpoint map is also a monomorphism: it factors through the equivalence-relation monomorphism into $U\times_S U$ and then the monomorphism to $U\times_{\mathbf Z}U$. Lemma E4.1 makes it a closed immersion. Consequently the endpoint map gives a surjection

$$
\theta:A\otimes_C A\longrightarrow B,\qquad
a\otimes a'\longmapsto s(a)t(a').
$$

This works for a base $S$ which is neither separated nor affine.

Invariant rings commute with flat base changes of $C$: tensor the kernel sequence $0\to C\to A\xrightarrow{s-t}B$. Fix a prime $\mathfrak p$ of $C$, and extend $C_{\mathfrak p}$ faithfully flat to the local ring

$$
D=(C_{\mathfrak p}[z])_{\mathfrak p C_{\mathfrak p}[z]}.
$$

Polynomial extension and localization are flat; the map is local, hence faithful. Its residue field is the infinite field $\kappa(\mathfrak p)(z)$. It is enough to prove the claimed algebra statements after these extensions at every prime. By the kernel observation the new base is still the invariant ring. We may therefore assume $C$ is local with maximal ideal $\mathfrak m$ and infinite residue field $k$.

The ring $A$ is semilocal. Integrality makes every maximal ideal lie over $\mathfrak m$. Each topological orbit of maximal ideals is finite: its targets occur in the finite source fibre over one of its objects. Inversion and composition give equivalence and transitivity; common residue-field extensions allow composition when only the underlying endpoints initially agree. Suppose there were two such orbits. By the Chinese remainder theorem choose $f\in A$ having residue zero at every ideal of the first orbit and residue one at every ideal of the second. On the finite Artinian source fibre at an object of the first orbit, $t(f)$ is nilpotent, and its determinant is zero. On the corresponding fibre of the second orbit, $t(f)-1$ is nilpotent, and its determinant is one. But $N(f)\in C$ has a single residue in $k$, which cannot become zero in one field extension and one in another. Hence there is only one orbit, containing all maximal ideals, so there are finitely many.

The surjection $\theta$ says that $B$ is generated over $s(A)$ by elements of $t(A)$. Choose a finite list $t(f_1),\ldots,t(f_m)$ generating the finite module $B$. At each of the finitely many maximal ideals of $A$, there is an $r$-tuple of linear combinations of this list giving a basis of the fibre. Its determinant is a nonzero polynomial in the combination coefficients over that residue field. It cannot vanish on all tuples from the infinite common subfield $k$: expand its finitely many coefficients in a basis of their span over $k$ and retain a nonzero coordinate polynomial over $k$. The product of finitely many such nonzero polynomials is nonzero. A nonzero polynomial over an infinite field has a nonvanishing field-valued tuple, by induction on the number of variables, choosing nonzero coefficient values first and then avoiding the finitely many roots in the last variable. Avoid the chosen coordinate polynomials simultaneously, and lift the resulting coefficients to $C$. We get $x_1,\ldots,x_r\in A$ with $t(x_i)$ a basis at all maximal ideals. Nakayama makes $A^r\to B$ surjective; localizing shows it is an isomorphism between free modules of the same rank. Hence

$$
B=\bigoplus_i s(A)t(x_i).
$$

Write uniquely $t(a)=\sum_i s(a_i)t(x_i)$. In the composable-pair algebra $E=B\otimes_{s,A,t}B$, where an arrow in the left factor follows one in the right factor, composition satisfies

$$
c^*t(a)=t(a)\otimes1,\qquad c^*s(a)=1\otimes s(a).
$$

Apply composition to the expansion, and also include the expansion in the left factor. The elements $t(x_i)\otimes1$ are a basis over the right factor. Its tensor relation identifies $s(a_i)\otimes1$ with $1\otimes t(a_i)$. Comparing the two expansions gives $s(a_i)=t(a_i)$ for every $i$, so $a_i\in C$. Applying the identity section gives $a=\sum_i a_i x_i$. Applying $t$ and the basis just constructed gives linear independence over $C$. Thus $A=\bigoplus_i Cx_i$ and $\theta$ is an isomorphism, since it carries the $A$-basis $1\otimes x_i$ to $t(x_i)$.

Return to the original $C$. At each prime, faithfully flat detection over the chosen local extension shows that the kernel of $\theta$ vanishes and that $A$ is flat over $C$. To verify the latter explicitly, tensor any injection with $A$, localize its kernel at the prime and extend to $D$; the computed free $D$-algebra makes this kernel zero, so faithfulness kills it. Vanishing at every prime kills the original kernel. Lying over gives surjectivity, hence faithful flatness. Now $A\otimes_C A=B$ is finite locally free over $A$. Lemma A1.3 descends this property of the module $A$ through the faithfully flat $C\to A$. Thus $A/C$ is finite locally free, and its relation is exactly $P$.

Finally, $q:\operatorname{Spec}A\to\operatorname{Spec}C$ is an fppf covering. On every scheme test of its target, its base change is again a finite locally free surjective cover, and its double overlap is the pullback of $P$. Sections therefore locally lift to $U$, and two such sections have equal image exactly when they are related by $P$. This local-lifting and equality description, followed by the sheaf condition, identifies the represented target with the fppf sheaf quotient. This is an identity on all test schemes, not just on geometric points. $\square$

### E7. Descending an affine neighbourhood of a space

**Lemma E7.0 (the étale diagonal).** The diagonal of an étale scheme morphism is an open immersion.

**Proof.** Around a diagonal point use the earlier proved local standard form $E=(R[T]/(f))_g$, with $f$ monic and $f'$ invertible in $E$. In the self-overlap, write the two coordinate classes $t_0,t_1$. The divided difference $h$ defined by $f(t_0)-f(t_1)=(t_0-t_1)h(t_0,t_1)$ restricts on the diagonal to the unit $f'(t_0)$. On $D(h)$ the two equations $f(t_0)=f(t_1)=0$ force $t_0=t_1$. The self-overlap localized at $h$ is therefore exactly the diagonal algebra $E$, giving an open neighbourhood which is the diagonal. These local charts cover the diagonal and prove it is an open immersion. $\square$

We use algebraic spaces as fppf sheaves with scheme-representable diagonal and a representable surjective étale scheme atlas. For an open in an atlas, its image defines an open subspace: on every scheme test the pulled-back atlas is a scheme étale cover, and the image of its selected open is an open subset of the test scheme. These images commute with base change, since two points above the same point can be joined after a common residue-field extension. Thus their open subscheme structures agree on overlaps and define the open subfunctor. This description also proves the following fact without a bootstrap theorem.

**Lemma E7.1 (an open atlas quotient).** If $U\to X$ is a surjective étale scheme atlas of an algebraic space, and $U_0\subset U$ is open, then $U_0/(U_0\times_X U_0)$ is the open image of $U_0$ in $X$ as an fppf sheaf.

**Proof.** On every scheme test of the image, its section locally lifts through $U_0$ after an étale, hence fppf, refinement. Two local lifts have the same image exactly when their pair factors through $U_0\times_X U_0$. Local lifts and this equality description identify the sheaf quotient with the open image. All arrows with given endpoints are unique because this is an equivalence relation. Consequently the equality arrows, as well as the object sections, descend on refinements. $\square$

**Lemma E7.2.** Let $X\to T$ be a separated locally quasi-finite morphism of algebraic spaces, with $T$ affine. Let $T'\to T$ be an étale map with $T'$ affine, and let $V'\subset X\times_T T'$ be an affine open subspace. Then its image $W\subset X$ is an open subspace represented by a scheme.

**Proof.** Its image is open because the map to $X$ is étale. It is quasi-compact as the image of the affine $V'$. There is a uniform finite bound $n$ on the cardinalities of the geometric fibres of $T'\to T$: this is an affine quasi-finite morphism, so Theorem C5.1 embeds $T'$ in a finite scheme over $T$. A finite list of module generators of that completion bounds every fibre algebra's dimension and hence its number of geometric points. We induct on such a bound; no boundedness of the fibres of $X\to T$ is required.

For $n=0$ the image is empty. For $n=1$, the étale map $T'\to T$ is an open immersion. To recall the precise reason, its diagonal is an open immersion by Lemma E7.0; the fibre bound makes its image all of $T'\times_T T'$, because there is at most one geometric point in each fibre. Thus the diagonal is an isomorphism and the map is a monomorphism. An étale monomorphism is an open immersion: its open image $O$ is a scheme open, and the map to $O$ is a surjective étale cover. Its double overlap is its diagonal, hence is the source itself. The identity map of the source is consequently compatible on that overlap. Lemma A1.5 descends it to an inverse $O$-map; both inverse equations hold after the cover and hence before it by the same uniqueness. Thus the map is an isomorphism onto $O$. In this case $X\times_T T'$ is an open subspace of $X$, and $W=V'$ is a scheme.

For $n>1$, the diagonal of $T'\to T$ is both open, by étaleness, and closed, since a map of affines is separated. Thus

$$
T'\times_T T'=\Delta(T')\amalg T^*
$$

is a decomposition into affine clopen schemes. Each projection $T^*\to T'$ is étale and has geometric fibre bound $n-1$, because the diagonal removes exactly one point from the corresponding full base-changed fibre.

Write $X'=X\times_T T'$ and $X^*=X\times_T T^*$. In $X'\times_X X'$ use projections $p_0,p_1$, with its part over $T^*$ identified with $X^*$. The open

$$
V^*=p_0^{-1}(V')\cap X^*
=T^*\times_{\operatorname{pr}_0,T'}V'
$$

is affine, since both displayed factors and their base $T'$ are affine. It is an open in $X'\times_{T',\operatorname{pr}_1}T^*$. Apply the induction hypothesis with base $T'$, cover $\operatorname{pr}_1:T^*\to T'$, ambient space $X'$, and selected affine open $V^*$. Its image $p_1(V^*)$ is a scheme open in $X'$. The diagonal part contributes $V'$, so the saturation is

$$
p_1(p_0^{-1}(V'))=V'\cup p_1(V^*).
$$

It is a scheme by gluing these two scheme opens over their intersection, which is an open subscheme in each. It is also exactly $X'\times_X W=T'\times_T W$ as an open subspace. Indeed, over every test scheme a point in this pullback locally has one lift in $V'$ and its chosen lift in $X'$; these two lifts give the required overlap point. Conversely every overlap point with its first endpoint in $V'$ has image in $W$. This proves equality of the open subfunctors and includes infinitesimal test schemes.

Let $O\subset T$ be the open image of $T'$. The morphism $W\to T$ factors through $O$, and $T'\to O$ is a surjective étale, hence fppf, cover. Its pullback of $W$ is the scheme just constructed, separated and locally quasi-finite over $T'$ by base change. Its canonical scheme datum is effective by Theorem E5.1. Let $W_0/O$ be the descended scheme. For an arbitrary scheme $Z\to O$, pull back the cover $T'\to O$. The sections of $W_0$ and $W$ are respectively the compatible sections of exactly the same pulled-back scheme with the same equality datum. Both are fppf sheaves, so their functors on $Z$ agree naturally. Thus $W=W_0$ as a sheaf and is a scheme. This completes the induction. $\square$

### E8. Recognition and representability on every test scheme

**Theorem E8.1 (scheme recognition).** If $X\to T$ is a separated locally quasi-finite morphism of algebraic spaces and $T$ is a scheme, then $X$ is a scheme. The source need not be quasi-compact.

**Proof.** Restrict to affine target opens; the inverse images cover $X$ and will glue as schemes once recognized. Over an affine $T$, choose a scheme atlas of $X$ and cover it by affine opens. Each has an open image by the preceding construction. It suffices to recognize each such image, because they cover $X$ and their scheme opens then glue. We may therefore suppose an affine scheme $U$ maps étale surjectively to $X$.

The composite $U\to T$ is locally quasi-finite, by composition with the étale atlas and the definition on scheme coordinates. Since source and target are affine it is quasi-compact and separated, hence quasi-finite. The scheme relation $R=U\times_X U$ is a closed subscheme of $U\times_T U$, because $X/T$ is separated. Thus $R$ is affine, and its two projections are étale.

Fix $u\in U$ with image $p\in T$. Lemma E4.3 gives an affine elementary étale neighbourhood $(T',p')$ and a clopen finite $U'\subset U_{T'}$ containing a point above $u$. Let

$$
R'=U'\times_{X_{T'}}U'.
$$

Its endpoint map is closed in $U'\times_{T'}U'$ by separatedness. Since $U'/T'$ is finite, each projection $R'\to U'$ is finite. It is also étale, being the restriction to an open of a base-changed projection of $R$. Lemma E4.2 makes these projections finite locally free. In particular $U'$ and $R'$ are affine, and Theorem E6.1 constructs an affine quotient $V'=U'/R'$.

Lemma E7.1 identifies this quotient with the open image of $U'$ in $X_{T'}$. It contains the image of the selected point above $u$. Lemma E7.2 makes its image in $X$ a scheme open containing the image of $u$. Repeating for every point of $U$ gives scheme opens covering $X$. Their intersections are opens in each scheme; the identifications and their cocycle are the original identifications as subfunctors of $X$. Ordinary scheme gluing therefore represents $X$. The argument applies over every affine target open and gives the asserted result over any scheme $T$. $\square$

**Corollary E8.2.** A separated locally quasi-finite morphism $f:X\to Y$ of algebraic spaces is representable by schemes.

**Proof.** For every scheme $T\to Y$, the fibre product $X_T$ is an algebraic space separated and locally quasi-finite over $T$, by base change. Theorem E8.1 recognizes it as a scheme. These are all scheme tests, including non-Noetherian and non-quasi-compact ones, which is the definition of representability by schemes. $\square$

### E9. The normalization factorization consumed by AG-RG-03

The scheme input needed in this section is stronger than the quasi-affineness consequence used in Section E5. It is the **representable finite-type separated normalization theorem**: for a finite-type separated scheme morphism, the quasi-finite locus maps isomorphically onto an open of the relative integral closure; formation of that integral closure commutes with étale base change. Theorem D5.2 and Corollary D4.3 above prove these two scheme inputs. The present section explains every additional space descent step, so no separate algebraic-space normalization theorem is being invoked without proof.

**Theorem E9.1 (normalization factorization).** Let $f:X\to Y$ be quasi-finite and separated between algebraic spaces. Let $Y'$ be the relative integral closure of $Y$ in $X$. Then $X\to Y'$ is a quasi-compact open immersion and $Y'\to Y$ is integral. In particular $f$ is quasi-affine. If $Y$ is a scheme, then $X$ is a scheme.

**Proof.** Corollary E8.2 makes $f$ representable by schemes. Choose an étale scheme atlas $U\to Y$, and cover $U$ by affine opens $U_i$. Each $X_i=X\times_Y U_i$ is a scheme, and $X_i\to U_i$ is quasi-finite separated. On these schemes form the relative integral closure $U_i'$ and the scheme Zariski Main factorization. Over $U_i\times_Y U_j$ the two constructions agree: this overlap is a scheme étale over both atlas members, and the scheme integral-closure base-change theorem gives the same algebra. Its functoriality gives the triple cocycle. Consequently the integral, hence affine, $U_i'/U_i$ have affine algebra descent data.

Here is the space construction explicitly. For every scheme test $y:T\to Y$, the atlas pullbacks $T\times_Y U_i$ form an étale scheme covering of $T$. Apply effective affine descent from Lemma A1.2 and its finite affine refinement argument to these pulled-back integral algebras. The result is an affine $T$-scheme $T'_y$. It is independent of the refinement and compatible with every further scheme test, by uniqueness of algebra descent. Integrality descends as well. On a faithfully flat affine refinement $R\to A$, if $b\in B$ becomes integral in $A\otimes_R B$, the injection

$$
A\otimes_R R[b]\hookrightarrow A\otimes_R B
$$

identifies its image with $A[b]$, a finite $A$-module. Lemma A1.3 descends finite generation of $R[b]$, and the finite-module determinant argument makes $b$ integral over $R$. Thus every such $T'_y/T$ is integral.

Define $Y'(T)$ to consist of pairs of a section $y\in Y(T)$ and a section of the affine scheme $T'_y/T$. Compatibility with base change defines pullbacks. This is an fppf sheaf: the $y$ sections glue because $Y$ is a sheaf, and the sections of the resulting fixed affine pullback glue by Lemma A1.5. Its pullback over each fixed $y:T\to Y$ is represented by $T'_y$, so $Y'\to Y$ is affine and integral. The $U_i'$ give a surjective étale scheme atlas: on a test pair $(y,s)$ the pullback of its $i$th member is identified with the scheme $T\times_Y U_i$, using the base-change identification of the integral algebra and the section $s$. These schemes form an étale cover of $T$.

Its diagonal is scheme-representable. On a pair of scheme tests, first impose equality of their underlying $Y$ sections, obtaining a scheme by the diagonal of $Y$. Over that scheme the two chosen sections lie in one affine integral pullback, and their equality is a closed subscheme, because an affine scheme is separated over its base. Thus the tested equality functor is a scheme. This proves the algebraic-space conditions, and the tested affine construction proves integrality. By construction this space is precisely the relative integral closure.

The canonical maps $X_i\to U_i'$ agree on overlaps by the same scheme construction, and glue as sheaf maps to $g:X\to Y'$. Each is an open immersion. To justify descent on all tests, first note that $g$ is representable by schemes. For a scheme $Z\to Y'$, its pullback of $X$ over $Y$ is a scheme by Corollary E8.2. The desired $X\times_{Y'}Z$ is the inverse image of the diagonal of $Y'/Y$ in that scheme; that diagonal is a closed immersion because $Y'/Y$ is affine. Hence it too is a scheme. After the étale scheme cover of $Z$ induced by the $U_i'$, this morphism to $Z$ is an open immersion. Its local open images agree on overlaps; Lemma A1.6 descends them to an open subscheme of $Z$, and their comparison isomorphisms descend by Lemma A1.5. Thus the tested morphism is an open immersion. Since this holds for every $Z$, $g$ is an open immersion of spaces.

It is quasi-compact. Its graph $X\to X\times_Y Y'$ is a closed immersion, since $Y'/Y$ is separated. The projection $X\times_Y Y'\to Y'$ is a base change of the quasi-compact $f$. Their composite is $g$, so it is quasi-compact. For every affine scheme $T\to Y$, the integral $T\times_Y Y'$ is affine, and $X\times_Y T$ is a quasi-compact open subscheme of it. This is quasi-affineness on all affine scheme tests, equivalently the quasi-affine morphism property. The final scheme assertion also follows directly from Theorem E8.1. $\square$

For the monomorphism from the reductive quotient to its Grassmannian, Theorem E8.1 already supplies the essential assertion that the quotient is a scheme. Quasi-affineness needs scheme Zariski Main, and the claimed specific integral-normalization factorization needs its full normalization and étale-base-change version. These three conclusions must not be collapsed into a source citation.

## Freely accessible sources and exact proof use

The complete proofs appear above or in the specified earlier programme lessons. Comparison material is freely readable: the Stacks Project's [conductor argument, Tags 00PT–00Q9](https://stacks.math.columbia.edu/tag/00Q9), [polynomial coefficients, Tag 03GG](https://stacks.math.columbia.edu/tag/03GG), [étale local structure, Tags 00U7 and 00UE](https://stacks.math.columbia.edu/tag/00UE), [finite étale-local pieces, Tag 02LN](https://stacks.math.columbia.edu/tag/02LN), [relative integral closure and Zariski Main, Tags 03GE and 03GW](https://stacks.math.columbia.edu/tag/03GW), [finite integral subalgebras, Tag 0817](https://stacks.math.columbia.edu/tag/0817), [finite-stage immersions, Tag 081B](https://stacks.math.columbia.edu/tag/081B), [quasi-affine descent, Tag 0247](https://stacks.math.columbia.edu/tag/0247), [locally quasi-finite effectivity, Tag 02W8](https://stacks.math.columbia.edu/tag/02W8), [finite affine quotients, Tag 03BM](https://stacks.math.columbia.edu/tag/03BM), [scheme recognition, Tag 03XX](https://stacks.math.columbia.edu/tag/03XX), and [normalized factorization for spaces, Tag 0ABS](https://stacks.math.columbia.edu/tag/0ABS). The editable comparison sources and copying notices are retained with the reconstruction records.

## History

Source: *The Stacks Project*, the Stacks Project authors, copyright (C) 2005–2025 Johan de Jong, published openly by the Stacks Project under the GNU Free Documentation License, version 1.2 or later. Exact freely readable source tags are identified in this lesson.

Modified edition: *Affine descent, Zariski Main and recognition of spaces*, 5 October 2026. Author and publisher of the modified edition: GPT-6.1 Sol (OpenAI), Codex, Ultra setting, for Open mathematics courses. Faithfully flat descent, polynomial coefficients, conductor and affine completion, general scheme Zariski Main, finite quotients and space recognition; proofs reordered before consumption, finite-piece and open-immersion arguments expanded. Self-checked by the writing AI. Original contributions retain their separate CC0 dedication, and adapted Stacks expression retains its GNU FDL terms.
