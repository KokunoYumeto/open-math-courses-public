# From actions to orbit algebras

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text is public domain (CC0).*

## Introduction

An action records both where a point moves and which group element moves it. Its orbit relation records only the two endpoints. These records coincide for a free action. With isotropy, they can give different algebras even when the action is faithful and ergodic.

This lesson connects the constructions, type criteria and approximation theorems proved earlier. It also explains the historical notes in Takesaki III, Chapter XIII, with precise proof routes and corrected bibliographic pointers. The finite example in Section 2 can be read using matrix algebra alone. Sections 3–4 use the complete earlier proofs named there; no external research citation supplies a missing proof.

The measured relations below are principal, standard Borel and countable, with a nonzero sigma-finite measure and nonsingular presenting maps. Equalities and isomorphisms of measured relations are on invariant conull Borel sets. A locally compact crossed product has the separately stated hypotheses of the free-action lessons. These two scopes should be checked before applying a conclusion.

## 1. What passes from an action to its orbit relation

For a countable group \(\Gamma\) acting on \(X\), the transformation groupoid has arrows \((g,x):x\to gx\). The principal relation has arrows \((gx,x)\). The endpoint map is
\[
q:\Gamma\ltimes X\longrightarrow R,\qquad
q(g,x)=(gx,x).
\tag{1.1}
\]
It preserves composition because
\[
q(h,gx)q(g,x)=(hgx,gx)(gx,x)=(hgx,x)=q(hg,x).
\tag{1.2}
\]
For fixed endpoints \((y,x)\), choose \(g_0x=y\). All arrows above those endpoints are \(g_0\Gamma_x\), where \(\Gamma_x\) is the stabilizer. Thus \(q\) is bijective precisely when every stabilizer is trivial. This includes the loops above \((x,x)\), which are erased by the endpoint map. [Orbits, stabilizers, and relation algebras](orbits-stabilizers-and-relation-algebras.md), Proposition 1.1, gives the full groupoid statement.

**Proposition 1.1 (the diagonal remembers the relation).** The principal relation algebra has maximal abelian diagonal \(\mathcal A=L^\infty(X,\mu)\), with
\[
Z(\mathcal M(R,\mu))
=\{M_f:f(x)=f(y)\text{ for almost every }(x,y)\in R\}.
\tag{1.3}
\]
Consequently it is a factor exactly when \(R\) is ergodic. An orbit equivalence preserving the measure class induces a spatial isomorphism carrying diagonal onto diagonal.

*Proof.* The full cyclic/separating-vector and two-coordinate commutant proof is [Orbits, stabilizers, and relation algebras](orbits-stabilizers-and-relation-algebras.md), Theorem 4.2 and Corollary 4.3. Maximal abelianness puts a central operator in the diagonal. Commutation with each partial orbit transport then makes its multiplier constant along that transport; a countable presentation gives (1.3) on one conull set. Conversely every such multiplier commutes with the diagonal and all the generating transports, hence is central. In an ergodic relation, rational level sets of the real and imaginary parts of an invariant multiplier are null or conull. They force the multiplier to be constant almost everywhere. A nontrivial invariant set instead gives a nontrivial central projection.

For the last assertion, the complete measure-change unitary and orbit-coordinate transport are the same lesson's Proposition 5.1 and Theorem 5.2. They intertwine each diagonal multiplier and each partial orbit map, so they intertwine the generated von Neumann algebras. This preserves the diagonal pair, not just the abstract factor. \(\square\)

For a free locally compact action, [Free actions and the crossed-product diagonal](free-actions-and-the-crossed-product-diagonal.md), Theorems 3.1–3.3, supplies the corresponding maximal-abelian and centre results at the exact separable locally compact group scope. The general crossed-product construction and dual-weight machinery belong to the separate flow course. For a nonfree action, Proposition 1.1 concerns the principal relation construction; it does not discard isotropy from the crossed product.

## 2. A faithful finite action with two different algebras

Let \(G=S_3\) act on \(X=\{1,2,3\}\) by permutations, with uniform probability. The action is faithful, transitive and measure preserving. It is not free: the transposition \((23)\) fixes \(1\). Its orbit relation is the complete relation \(X\times X\).

**Proposition 2.1.** For this action,
\[
\begin{aligned}
\mathcal M(R,\mu)&\cong M_3(\mathbb C),\\
\ell^\infty(X)\rtimes S_3
&\cong M_3(\mathbb C)\oplus M_3(\mathbb C).
\end{aligned}
\tag{2.1}
\]
The first centre is \(\mathbb C\); the second is \(\mathbb C\oplus\mathbb C\).

*Proof.* In the relation algebra the nine endpoint arrows give the ordinary matrix units \(e_{ij}\). They satisfy \(e_{ij}e_{kl}=\delta_{jk}e_{il}\), \(e_{ij}^*=e_{ji}\), and \(\sum_i e_{ii}=1\). They span the entire algebra of the finite complete relation, proving the first assertion.

Write \(N=\ell^\infty(X)\rtimes S_3\), with diagonal projections \(p_i\) and regular group unitaries \(u_g\). Its covariance relation is \(u_gp_i u_g^*=p_{gi}\). The elements \(p_i u_g\), \(i\in X,g\in S_3\), span \(N\) and are linearly independent. Indeed, in the regular covariant representation, applying a sum \(\sum_g a_g u_g\) to a vector in the identity group-coordinate separates its distinct \(g\)-coordinates and forces every \(a_g\) to vanish. Therefore \(\dim_{\mathbb C}N=18\).

Choose \(r_1=e,r_2=(12),r_3=(13)\) and put
\[
v_i=u_{r_i}p_1,\qquad
v_i^*v_j=\delta_{ij}p_1,\qquad
v_iv_i^*=p_i.
\tag{2.2}
\]
The middle equality follows by inserting the disjoint range projections \(p_i,p_j\). The corner \(p_1Np_1\) is spanned by \(p_1u_h\) for \(h\) in the stabilizer \(H=\{e,(23)\}\): \(p_1u_gp_1=0\) if \(g1\ne1\). Its two spanning elements are independent by the same regular representation. With
\[
w=p_1u_{(23)},\qquad w=w^*,\qquad w^2=p_1,
\tag{2.3}
\]
the corner is the two-dimensional group algebra of \(H\), hence \(\mathbb C\oplus\mathbb C\).

The maps
\[
[a_{ij}]\longmapsto\sum_{i,j}v_i a_{ij}v_j^*,
\qquad
b\longmapsto[v_i^*bv_j]
\tag{2.4}
\]
are inverse star isomorphisms between \(M_3(p_1Np_1)\) and \(N\). Matrix-unit multiplication (2.2) proves multiplicativity; \(\sum_i v_iv_i^*=1\) proves the two inverse identities. This gives the second algebra in (2.1). Its two central projections are
\[
z_\pm=\sum_i v_i\frac{p_1\pm w}{2}v_i^*.
\tag{2.5}
\]
Both are nonzero, are orthogonal, and sum to one. Each associated summand is \(M_3(\mathbb C)\). The claimed centres follow. \(\square\)

Faithfulness only says that no group element fixes every point. Freeness says that no nonidentity group element fixes any point in the relevant conull space. The action above satisfies the first assertion and fails the second. Ergodicity forces factoriality of its principal relation algebra; it does not force factoriality of its crossed product.

## 3. Measure classes determine the factor type

Suppose \(R\) is ergodic in the countable standard scope stated above. The full proofs are in [Diagonal expectations and invariant measures](diagonal-expectations-and-invariant-measures.md), Theorems 3.4, 4.1, 5.1, 5.2 and 5.4. They give:

| Measured orbit structure | Algebra |
|---|---|
| The measure is concentrated on one countable orbit \(O\) | \(B(\ell^2(O))\), type I |
| No conull orbit; an equivalent finite invariant measure exists | Type \(II_1\) |
| No conull orbit; an equivalent infinite sigma-finite invariant measure exists | Type \(II_\infty\) |
| No equivalent sigma-finite invariant measure exists | Type III |

Here “invariant” concerns every partial orbit bijection, and “equivalent” preserves exactly the null sets. The presenting measure need not itself be invariant. In the type I row its positive atomic weights may be replaced by counting weights. In the finite row normalization changes the trace by a positive scalar.

**Proposition 3.1 (transport of the invariant measure).** Let \(\Phi:(X,R,\mu)\to(Y,S,\nu)\) be a measure-class orbit isomorphism. If \(m\sim\mu\) is invariant, then \(\Phi_*m\sim\nu\) is invariant and has the same total mass, finite or infinite.

*Proof.* Equivalent measures have the same null sets, and a measure-class isomorphism transports that property to \(Y\). For a partial \(S\)-bijection \(\theta\), the map \(\Phi^{-1}\theta\Phi\) is a partial \(R\)-bijection. For each measurable \(B\) in its range of definition,
\[
\begin{aligned}
(\Phi_*m)(\theta B)&=m(\Phi^{-1}\theta B)\\
&=m(\Phi^{-1}B)\\
&=(\Phi_*m)(B).
\end{aligned}
\tag{3.1}
\]
Total mass is unchanged by pushforward. The inverse map gives the converse. The factor type table is therefore intrinsic to the measured relation. \(\square\)

For a free locally compact action, the relevant Haar/modulus criterion is instead [Type criteria for locally compact free actions](type-criteria-for-locally-compact-free-actions.md), Theorems 4.2 and 5.1. An invariant measure condition from the countable relation table must not be substituted for that separately proved formula.

## 4. Finite approximation and orbit classification

**Proposition 4.1 (the finite-measure classification).** Any two ergodic hyperfinite principal relations on standard nonatomic probability spaces, preserving their probabilities, are isomorphic as measured relations. Their relation algebras are isomorphic by an isomorphism carrying diagonal onto diagonal.

*Proof.* [Balanced arrays and the hyperfinite finite factor](balanced-arrays-and-the-hyperfinite-finite-factor.md), Theorem 4.1, constructs for each relation a conull Borel orbit isomorphism onto the fair binary tail relation on \(\{0,1\}^{\mathbb N}\). Its proof includes equal-measure matching, balancing, exact array refinement, approximation of every measurable generator, and realization of the address map. An array cell with prefix of length \(m\) has measure \(2^{-m}\); its compatible transports change the prefix and preserve every later digit. Thus both the probability and the entire relation are transported, not merely a selected generating transformation.

Let these two maps be \(\Phi_1,\Phi_2\). Intersect their conull ranges, then take the intersection of all their images under finite-prefix replacements. There are countably many such maps and each preserves fair product measure, so the resulting tail-invariant Borel set \(C\) is conull. The map
\[
\begin{gathered}
\Psi=\Phi_2^{-1}\Phi_1,\\
\Psi:\Phi_1^{-1}(C)\longrightarrow\Phi_2^{-1}(C).
\end{gathered}
\tag{4.1}
\]
is a probability-preserving Borel isomorphism. Two points are related exactly when their addresses are tail equivalent, so \(\Psi\) is an orbit isomorphism. Proposition 1.1 transports the diagonal pair. The full compatible matrix-algebra conclusion is the balanced-array lesson's Theorem 5.1. \(\square\)

This is the finite, nonatomic, invariant-measure classification discussed in the source notes in connection with H. A. Dye. Infinite sigma-finite invariant measure is handled by the same lesson's Proposition 6.1, with the complete relation on \(\mathbb N\) as the amplification. In the nonsingular case the binary address measure need not be fair. The general flow classification referred forward to Chapter XVIII is a later theorem, not a conclusion of Proposition 4.1.

[Invariant means on measured relations](invariant-means-on-measured-relations.md), Theorem 6.1 and Proposition 6.3, proves that amenability, hyperfiniteness and the source's constant-size AF exhaustion agree for ergodic standard countable principal measured groupoids, including atomic cases. The full matching, finite-approximation and tail-intersection proofs are there. [Towers and odometer orbits](towers-and-odometer-orbits.md), Corollary 3.2, also proves finite exhaustion directly for a nonsingular transformation.

For example, \(\mathbb Z\) is amenable, using the intervals \([-n,n]\): translating by a fixed \(k\) changes at most \(2|k|\) points, while the interval has \(2n+1\) points. The invariant-mean construction from these estimates is proved in [Means, Følner sets, and regular representations](means-folner-sets-and-regular-representations.md), Section 2. Yet \(\mathbb Z\) has no nontrivial finite subgroup: a nonzero integer has infinitely many distinct multiples. Finite subgroupoids approximating an orbit relation are finite equivalence classes inside that relation. They need not come from finite subgroups of the presenting group.

## 5. Historical sources and exact boundaries

The chapter introduction announces the passage from group actions to principal measured relations, the factor-type question and amenable approximation. Sections 1–4 explain those connections with the precise freeness, standardness, measure and atomic qualifications. The introduction's forward mention of approximation of general amenable factors in Chapter XVI belongs to that later factor theory; it is distinct from the principal-relation theorem proved here.

The closing notes begin with Murray and von Neumann's constructions, recalled in Chapter V, and then credit Dye, Krieger, Mackey, Ramsay, Renault, Feldman and Moore, Hahn, Zimmer, and Connes, Feldman and Weiss. The following reading routes retain that credit:

| Historical subject | Source pointer | Treatment in this course |
|---|---|---|
| Early group-measure-space factors | Murray and von Neumann; the notes refer back to Chapter V | Historical attribution; the present construction, Bernoulli type \(II_1\) example and affine type III example have the full owned proofs cited above |
| Finite invariant-measure orbit classification | Dye, *On groups of measure preserving transformations*, I (1959), II (1963); Takesaki bibliography [507] | Balanced-array Theorems 4.1 and 5.1; Proposition 4.1 above |
| A single nonsingular generator for an AF relation | Krieger, *On non-singular transformations of a measure space*, I–II (1969); [619] | The full dyadic/atomic generator constructions in [Matching sets and nonsingular dyadic arrays](matching-sets-and-nonsingular-dyadic-arrays.md), Sections 3–4 |
| Classification involving ergodic flows | Krieger, *On ergodic flows and the isomorphism of factors*, Math. Ann. 223 (1976), 19–70; [621] | A forward reference to Chapter XVIII; the countable associated-flow construction is proved in [Lifted relations and the associated flow](lifted-relations-and-the-associated-flow.md) |
| Virtual and measured groupoids | Mackey (1966), [633]; Ramsay (1971), [674]; Renault (1980), [676]; Hahn (1978), [556]; Feldman–Hahn–Moore, *Orbit Structure and Countable Sections for Actions of Continuous Groups*, [521] | The owned groupoid constructions and exact programme prerequisites; general Ramsay/disintegration obligations remain separately identified |
| Cartan algebras and measured relations | Feldman–Moore I–II (1977), [522] | The maximal-abelian, expectation and normalizer proofs named in Sections 1 and 3 |
| Rigidity and its broader setting | Fisher, *Groups acting on manifolds: around the Zimmer program* (2008), Section 1 | Freely accessible historical survey of the Zimmer programme; no rigidity theorem is asserted or proved here |
| Amenability and AF relations | Connes–Feldman–Weiss (1981), [482] | The complete principal-relation invariant-mean and finite-exhaustion proof cited in Section 4 |
| Foliations and index theory | Connes, the works referenced by [474], [475] and *Noncommutative Geometry* (1994), [480] | Historical context beyond this ergodic-relation assignment |

Two bibliographic details need care. The notes' 1973 wording should not be used as the publication date of [621]: the book's own bibliography gives 1976. This observation does not determine the date of every earlier announcement. The notes' Zimmer pointer [749] instead names G. Zeller-Meier; the Zimmer book is [750]. Also, the author of [674] is Arlan Ramsay, despite the notes' spelling “Ramsey.” The corrected identities follow the actual bibliography.

These historical pointers do not certify the contents of whole external papers. They identify attribution and boundaries; every mathematical conclusion used here has its complete proof here or at an exact earlier written course locator. [Borel group measures and isotropy topologies](borel-group-measures-and-isotropy-topologies.md), Sections 4–6, proves the supported fixed-range-fibre disintegration and Haar product; [Orbit averaging and the modular weight bridge](orbit-averaging-and-the-modular-weight-bridge.md), Corollary 5.2, completes its standing standard Borel source route. Broader countably generated assertions retain their proved counterexamples or unresolved existential scope. The separate AF08 continuous product-model book-notation correspondence remains with the flow course and is not inferred from the owned countable construction.

## 6. Exercises with complete solutions

**Exercise 6.1 (faithful and free).** *Level 1.* For the \(S_3\) action in Section 2, compute all stabilizers and the number of transformation-groupoid arrows above each principal arrow.

*Solution.* The stabilizer of \(1\) is \(\{e,(23)\}\), that of \(2\) is \(\{e,(13)\}\), and that of \(3\) is \(\{e,(12)\}\). Each has order two. For any endpoints \(i,j\), the permutations sending \(j\) to \(i\) are one coset of the stabilizer of \(j\), so exactly two transformation arrows lie above \((i,j)\). There are nine principal arrows and eighteen transformation arrows. A permutation fixing all three points is the identity, so the action is faithful, while these nontrivial stabilizers show that it is not free.

**Exercise 6.2 (the two central projections).** *Level 2.* Prove directly that the operators \(z_\pm\) in (2.5) are nonzero central orthogonal projections, and identify the diagonal in the two matrix summands.

*Solution.* In the corner, \(c_\pm=(p_1\pm w)/2\) satisfy \(c_\pm^*=c_\pm\), \(c_\pm^2=c_\pm\), \(c_+c_-=0\) and \(c_++c_-=p_1\). Neither is zero, because \(w\) and \(p_1\) are independent. The corner is spanned by those two commuting elements, so both \(c_\pm\) are central there. Under the star isomorphism (2.4), \(z_\pm\) correspond to diagonal matrices with constant entry \(c_\pm\). They are therefore central, nonzero and orthogonal, and sum to one. Each \(p_i=v_i p_1v_i^*\) corresponds to the \(i\)-th diagonal matrix unit tensored with the corner identity. Hence the original diagonal becomes \(\{(d,d):d\in D_3\}\) in \(M_3\oplus M_3\). Its dimension is three, and it is not maximal abelian there; its commutant contains \(D_3\oplus D_3\).

**Exercise 6.3 (changing the presenting measure).** *Level 2.* Let a complete relation on a finite set \(X=\{1,\ldots,n\}\) have probabilities \(a_i>0\), \(\sum_i a_i=1\). Find an equivalent invariant measure and determine its relation algebra and trace.

*Solution.* Set \(m(\{i\})=1/n\). Both measures give positive mass to every singleton, so have exactly the same null sets. Every partial orbit bijection between finite subsets preserves their cardinalities, hence preserves \(m\). The complete relation has one orbit containing all mass. Its matrix units give \(M_n(\mathbb C)\), independent of the original \(a_i\). With the invariant probability, diagonal integration gives \(\tau(e_{ii})=1/n\), and therefore the normalized matrix trace. The original diagonal state instead gives \(\varphi(e_{ii})=a_i\), which is tracial only when all \(a_i\) are equal: matrix-unit cyclicity requires \(\varphi(e_{ij}e_{ji})=\varphi(e_{ji}e_{ij})\), or \(a_i=a_j\).

**Exercise 6.4 (composing conull orbit isomorphisms).** *Level 3.* Complete the common-range construction in Proposition 4.1, including exact invariance and preservation of measure.

*Solution.* Let \(C_0\) be the intersection of the two conull Borel ranges. Let \(\mathcal F\) be the countable group of flips of finite sets of binary coordinates; its orbits are exactly tail classes. Put \(C=\bigcap_{T\in\mathcal F}T(C_0)\). Every \(T\) preserves fair probability, so \(C\) is Borel and conull. Applying any \(S\in\mathcal F\) permutes the indexing group, giving \(S(C)=C\) exactly. The preimages of \(C\) under the two orbit isomorphisms are invariant conull Borel sets. On them (4.1) is a Borel bijection, preserves probability, and preserves and reflects related pairs because both intermediate addresses lie in \(C\) and both maps identify related pairs with tail equivalence. This verifies all parts of the claimed measured relation isomorphism.

**Exercise 6.5 (finite classes do not require finite subgroups).** *Level 2.* For the binary tail relation, show that agreement after the first \(n\) digits defines classes of size \(2^n\), and explain why this is compatible with an odometer presentation by \(\mathbb Z\).

*Solution.* Once the infinite tail is fixed, each of the \(2^n\) binary prefixes is allowed, giving exactly \(2^n\) points. These relations increase, and their union is tail equivalence because two tail-equivalent sequences differ in finitely many coordinates. The odometer's orbit computation in [Towers and odometer orbits](towers-and-odometer-orbits.md), Section 4, identifies its orbits with tail classes on an invariant conull Borel set. A finite stage retains only selected arrows of that orbit relation. It is not the orbit relation of a finite subgroup of \(\mathbb Z\), since the only such subgroup is \(\{0\}\), whose classes are singletons. Finite-prefix classes and finite subgroups are different approximation objects.

**Exercise 6.6 (a publication date and a theorem boundary).** *Level 2.* State what the source comparison proves about the references [621] and [749], and what it does not prove about nonsingular flow classification.

*Solution.* The actual bibliography dates [621], Krieger's *On ergodic flows and the isomorphism of factors*, to 1976. Thus 1973 in the notes is not the publication date of that cited paper; it might refer to earlier history, which this comparison does not determine. Bibliography [749] is a work of Zeller-Meier, while Zimmer's book is [750], so the notes' Zimmer number needs correction. Proposition 4.1 proves classification of ergodic hyperfinite nonatomic probability-preserving relations by the fair tail relation, using complete written coding proofs. It does not prove the nonsingular type III classification by flows, which the notes explicitly refer forward to Chapter XVIII. The associated-flow construction already proved in the flow lesson and the separate remaining AF08 correspondence retain their exact respective scopes.

## References and source scope

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Springer, 2003. Chapter XIII, introduction; closing notes, pages 79–80. Bibliography [507], [619], [621], [633], [674], [676], [521]–[522], [556], [749]–[750], [474]–[475], [482] and [480] supplies the historical identities above. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).

[Fisher] David Fisher, *Groups acting on manifolds: around the Zimmer program*, arXiv:0809.4849v2, 5 December 2008, Section 1 (Prologue). [Read the survey](https://arxiv.org/html/0809.4849v2#S1). Its opening section discusses actions of higher rank groups and lattices on compact manifolds and the motivation from cocycle superrigidity. This 2008 survey provides supplementary historical context for Section 5. The proofs used in this lesson remain at the course locators above.

The new finite action calculation and the connective arguments are original course exposition. The finite classification, type, normalizer and amenability proofs are at the exact owned lesson locators identified above. Scholarly sources are credited at the cited lesson locators; the course-wide comparison of wording and distinctive arrangement remains in progress. This lesson does not mark the remaining general Connes or continuous-flow dependencies complete.
