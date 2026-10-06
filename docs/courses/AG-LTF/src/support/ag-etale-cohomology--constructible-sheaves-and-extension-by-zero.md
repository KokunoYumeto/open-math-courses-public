# Constructible sheaves and extension by zero

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0.*

A sheaf can have one finite local system on an open part of a scheme and different data on its boundary. Extension by zero places the open data on the whole scheme. Constructibility means that finitely many such locally constant descriptions suffice. We prove the exactness and permanence statements needed for subsequent base-change theorems, then use a finite étale trace to reduce finite monodromy to an \(\ell\)-group.

We use geometric stalks, finite direct images and their base change from Pushforward, pullback and finite morphisms, and effective descent for affine schemes from Topologies on schemes. Where the fundamental group occurs, the classification of finite étale covers is cited from the Stacks project.

For abelian sheaves, **constructible** will mean finite underlying stalks on finitely many locally constant pieces; such sheaves are torsion. We also prove the usual module version over a commutative Noetherian ring \(\Lambda\), where the constant modules are finitely generated. These are distinct finiteness conditions when \(\Lambda\) is infinite. For example the constant \(\mathbf Z\)-module is finitely generated, but its underlying abelian sheaf is not constructible in the finite-stalk convention. For a finite coefficient ring the two conditions coincide.

## 1. Extension by zero for an étale morphism

Let \(j:U\to X\) be étale, without assuming it finite, separated or an open immersion. For an abelian sheaf \(\mathcal F\) on \(U_{\mathrm{ét}}\), define a presheaf on \(X_{\mathrm{ét}}\) by

\[
(j_{p!}\mathcal F)(V)
 =\bigoplus_{\varphi:V\to U\ {\rm over}\ X}\mathcal F(V,\varphi).
\tag{1.1}
\]

Here \((V,\varphi)\) is an object of \(U_{\mathrm{ét}}\). Under \(a:V'\to V\), restrict a summand along \(a\) and put it in the summand indexed by \(\varphi a\); if indices coincide, add their contributions. Let \(j_!\mathcal F\) be its associated sheaf. The same construction is \(\Lambda\)-linear for module sheaves. For sheaves of sets one instead uses a coproduct and sheafification; its underlying set functor is different from the abelian \(j_!\).

**Proposition 1.1.** The functor \(j_!\) is left adjoint to \(j^{-1}\), is exact, and has geometric stalks

\[
(j_!\mathcal F)_{\bar x}
 =\bigoplus_{\bar u:\,j\bar u=\bar x}\mathcal F_{\bar u}.
\tag{1.2}
\]

**Proof.** A map from the presheaf (1.1) to a sheaf \(\mathcal G\) is a compatible family of maps from each \(\mathcal F(V,\varphi)\) to \(\mathcal G(V)\). This is exactly a map \(\mathcal F\to j^{-1}\mathcal G\), since restriction to the localized étale site gives \((j^{-1}\mathcal G)(V,\varphi)=\mathcal G(V)\). Conversely use that map on each summand and add. These constructions are inverse and natural. The universal property of sheafification proves the adjunction.

For (1.2), send a germ represented by \((V,\bar v,\varphi,s)\) to the germ of \(s\) at \(\bar u=\varphi\bar v\). Every such germ on \(U\) has a representative on an étale neighborhood of \(\bar u\), which is also an étale neighborhood of \(\bar x\). A finite list of representatives can be placed on one common pointed refinement by fiber products over \(X\). This proves surjectivity.

For injectivity, consider a finite sum mapping to zero. Any two indexing maps with the same lift \(\bar u\) agree on a pointed refinement: their equalizer is the inverse image of the open diagonal of the étale map \(U\to X\), and contains the chosen point. Refine so these maps agree, and combine their summands. Each resulting section has zero germ in its \(\mathcal F_{\bar u}\), hence vanishes after a further pointed refinement. A common refinement kills all of them. Sheafification does not change stalks, proving (1.2).

Direct sums of abelian groups or modules are exact. Applying the stalk formula to a short exact sequence, and using enough geometric points, proves exactness of \(j_!\). \(\square\)

**Proposition 1.2 (base change).** In a cartesian square

\[
\begin{array}{ccc}
U'=U\times_XY&\xrightarrow{g'}&U\\
j'\downarrow&&\downarrow j\\
Y&\xrightarrow{g}&X,
\end{array}
\]

there is a natural isomorphism
\(j'_!g'^{-1}\mathcal F\simeq g^{-1}j_!\mathcal F\), for arbitrary \(g\).

**Proof.** Pull back the unit \(\mathcal F\to j^{-1}j_!\mathcal F\); commuting inverse images and adjunction give the comparison from the left side to the right side. At \(\bar y\), lifts to \(U'\) are precisely lifts of \(g\bar y\) to \(U\), with the same geometric field. The inverse-image stalk formula and (1.2) identify the comparison with the identity on each corresponding summand. It is an isomorphism on all stalks. \(\square\)

If \(j\) is an open immersion, there is one lift over its image and none outside. Thus \(j_!\mathcal F\) restricts to \(\mathcal F\) on \(U\), and has zero stalks outside. These properties characterize it: adjunction supplies a map to any sheaf with those properties, and stalks make that map an isomorphism.

If \(i:Z\to X\) is the complementary closed immersion, the adjunction maps give

\[
0\longrightarrow j_!j^{-1}\mathcal G
 \longrightarrow\mathcal G
 \longrightarrow i_*i^{-1}\mathcal G
 \longrightarrow0.
\tag{1.3}
\]

At a point of \(U\) the left map is the identity and the right-hand stalk is zero; at a point of \(Z\) the right map is the identity and the left-hand stalk is zero. Finite-pushforward stalks apply to \(i\), proving exactness. Finally \((j_1j_2)_!=j_{1!}j_{2!}\) for composable étale maps, since both sides are left adjoint to the same restriction functor.

## 2. Finite local systems and monodromy

A constant set sheaf \(\underline S\) is the sheafification of the constant presheaf, so its sections are locally constant choices of elements of \(S\). A sheaf is **finite locally constant** if it becomes such a sheaf with finite \(S\) on an étale cover.

**Theorem 2.1.** A set sheaf is finite locally constant if and only if it is represented by a finite étale \(X\)-scheme. This is an equivalence of categories.

**Proof.** First a degree-\(d\) finite étale cover becomes a disjoint union of \(d\) copies of the base étale locally. One explicit splitting cover is its ordering cover: in \(Y^d_X\), remove all pairwise diagonals. Those diagonals are open and closed for a finite étale map. The resulting scheme is finite étale, and its geometric fiber is the set of orderings of the \(d\)-element fiber, hence nonempty. Over it the \(d\) tautological sections give a map \(\coprod_1^d V\to Y_V\) which is a bijection on every geometric fiber, and hence an isomorphism of finite étale covers. The degree is locally constant, so this argument applies on its degree loci; the degree-zero case is the empty cover. Thus the represented sheaf is finite locally constant.

Conversely choose an étale cover \(X_a\to X\) trivializing a finite locally constant sheaf \(\mathcal F\). Represent it there by \(\coprod_{S_a}X_a\). On \(X_a\times_XX_b\), the two identifications with \(\mathcal F\) give an isomorphism of represented sheaves. Yoneda gives a unique isomorphism of the representing schemes. On triple overlaps these isomorphisms satisfy the cocycle condition because their sheaf maps do. Effective affine descent glues the finite affine schemes. Their finite locally free algebras descend, and étaleness descends under the faithfully flat cover, so the resulting \(Y\to X\) is finite étale. Its represented sheaf agrees locally with \(\mathcal F\), hence globally. The same Yoneda-and-descent argument identifies all morphisms, proving the categorical assertion. \(\square\)

For a connected scheme with geometric point \(\bar x\), the precise fundamental-group foundation is the equivalence

\[
\mathrm{FÉt}_X\simeq
 \{\text{finite continuous left }\pi_1(X,\bar x)\text{-sets}\}.
\tag{2.1}
\]

Here \(\pi_1\) is the profinite automorphism group of the geometric fiber functor. The foundational proof is [Stacks, Tag 0BND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-fundamental-group), part (1), using the finite-étale Galois category and its equivalence theorem [Tag 0BN4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-galois). This same exact input was used for the character exercise in The multiplicative group on a curve. Combining it with our full representability proof proves the claimed finite-local-system classification.

The equivalence preserves finite products. Thus additions, zero, inverse and scalar-action maps on a finite locally constant set sheaf correspond exactly to those operations on its fiber, commuting with monodromy. Their identities hold on the sheaf if and only if they hold on its fiber. This proves the abelian-group and finite-underlying-module versions, including all morphisms and inverse constructions. For a finite ring \(\Lambda\), it classifies all finitely generated locally constant \(\Lambda\)-modules. We make no such unrestricted assertion for an infinite coefficient ring on an arbitrary connected scheme.

Pullback of a local system is locally constant: pull back its trivializing étale cover and its constant sheaf. For a finite étale map, pushforward of a local system is locally constant as well: on a splitting cover it is the finite product of the local systems on the individual sheets. The same computation gives

\[
f_!\mathcal F=f_*\mathcal F\quad\text{for }f\text{ finite étale}.
\tag{2.2}
\]

Indeed the stalk sum defining \(f_!\) and the finite product defining \(f_*\) agree, and locally their comparison is the finite direct-sum-to-product identity. It is invariant under permutations of sheets, so glues canonically.

## 3. Constructible pieces and basic permanence

On a qcqs scheme \(X\), a **constructible locally closed subset** is a locally closed subset which is constructible in the spectral-space sense: locally a finite Boolean combination of quasi-compact opens. A sheaf is constructible if there is a finite partition by such subsets on which it is finite locally constant. Use a locally closed subscheme with that underlying set; the choice of nilpotents does not affect its étale topos, by the topological invariance proved earlier. In the module version replace finite underlying values by finitely generated \(\Lambda\)-modules. On an arbitrary scheme the definition is applied on every affine open.

Finite constructible partitions have common refinements of the same kind: intersect the parts, then refine the finite Boolean combinations into intersections of an open and a closed subset. Constructible locally closed parts of a qcqs scheme are qcqs. For example on an affine they can be covered by finitely many sets \(D(g)\cap V(f_1,\ldots,f_s)\); their rings and finite intersections are affine. These observations also prove the equivalence between the global finite-partition definition and the affine-local definition on a qcqs scheme. A finite affine cover suffices, and all its finitely many partitions admit such a refinement.

**Lemma 3.1.** Maps between finitely generated locally constant module sheaves become maps of constant modules étale locally. These sheaves form an abelian subcategory closed under extensions and tensor products when \(\Lambda\) is Noetherian.

**Proof.** Trivialize source \(M\) and target \(N\). The images of finitely many generators of \(M\) are locally constant sections of \(\underline N\); refine the cover until they are constant. They determine a module homomorphism \(M\to N\), since all relations already hold as sheaf relations. Kernel and cokernel are the corresponding constant modules. The kernel is finitely generated because \(\Lambda\) is Noetherian and \(M\) is finitely generated; the cokernel is finitely generated as a quotient.

For an extension \(0\to\underline M\to\mathcal E\to\underline N\to0\), choose a finite presentation \(\Lambda^s\to\Lambda^r\to N\to0\). Étale locally lift the \(r\) generators to \(\mathcal E\). Their finitely many relation images lie in \(\underline M\); refine until those images are constant elements \(m_1,\ldots,m_s\). Then \(\mathcal E\) is the constant module

\[
(M\oplus\Lambda^r)/
 \langle(-m_a,r_a):1\leq a\leq s\rangle.
\tag{3.1}
\]

The natural map is surjective because the lifted generators generate the quotient \(N\); its kernel is generated by the displayed relations because every relation in \(\Lambda^r\to N\) is their linear combination. This checks the isomorphism on stalks and proves local constancy and finite generation. Tensor products are the constant tensor products on a common trivializing cover, and are finitely generated. \(\square\)

For finite abelian values, use a ring \(\mathbf Z/N\): in an extension of groups killed by \(a\) and \(b\), the middle group is killed by \(ab\). The preceding proof therefore also proves all these assertions with finite underlying values. Finite set maps can be treated by listing the finitely many source elements; on a common refinement their maps, finite limits and finite colimits are constant.

**Proposition 3.2.** Constructible abelian sheaves, and constructible \(\Lambda\)-modules in the module convention, form an abelian subcategory closed under extensions and tensor products. They are preserved by arbitrary scheme pullback.

**Proof.** Choose a common finite partition for the sheaves at the endpoints of a map or extension. Restriction to every stratum is exact and commutes with tensor product, so Lemma 3.1 applies there. This supplies a finite constructible partition for the kernel, cokernel, extension or tensor product.

For pullback, work on affine opens of source and target. The inverse images of the target's strata form a finite constructible locally closed partition, since inverse images of \(D(g)\) and \(V(f_1,\ldots,f_s)\) are defined by the pulled-back elements. Pullback of the local systems on those pieces is locally constant with the same finite values or finite generators. \(\square\)

The **support** of a constructible module or abelian sheaf is constructible: on a stratum the zero/nonzero stalk locus is open and closed. More generally the failure locus of surjectivity of a map between constructible modules is the support of its constructible cokernel. These facts will control finite choices below.

## 4. Finite data: the generators

For an affine étale object \(a:V\to X\) of finite presentation, put
\(P_V=a_!\underline\Lambda_V\). Adjunction gives

\[
\operatorname{Hom}(P_V,\mathcal F)=\mathcal F(V).
\tag{4.1}
\]

For finite abelian coefficients use \(a_!\mathbf Z/N\), whose Hom group consists of the \(N\)-torsion sections.

**Lemma 4.1.** The sheaves \(P_V\) are constructible, as are \(a_!\underline M\) for a finitely generated \(\Lambda\)-module \(M\). For finite abelian \(M\), the underlying abelian sheaf is constructible.

**Proof.** First consider an affine étale morphism of finite presentation \(\operatorname{Spec}B\to\operatorname{Spec}A\). Suppose \(A\) Noetherian. Over each generic point of its reduction, this algebra has a finite étale generic fiber. On an integral component, flatness makes \(B\) torsion free, so it embeds into its generic algebra. Choose a field basis from elements of \(B\). The products of basis elements, the identity and the given finite algebra generators involve finitely many coefficients in the fraction field. Clearing their denominators makes the span of that basis a finite algebra containing all the generators, hence equal to the localized \(B\). Remove the intersections with the other components to perform this argument separately on their generic open parts. If the base has nilpotents, its nilradical \(J\) is nilpotent. Finiteness modulo \(J\) implies finiteness here: a monic relation for any algebra generator modulo \(J\) lifts to \(p(b)\in JB\), and \(p(b)^e=0\) for \(J^e=0\) is a monic relation over \(A\). The algebra is finitely generated and integral, hence finite. Thus the same generic open argument applies to the original base.

The complementary closed subset is strictly smaller. Noetherian induction gives a finite locally closed partition on which the map is finite étale. This induction terminates because closed subsets satisfy the descending chain condition. All these subsets are constructible.

For general \(A\), write it as the filtered union of its finitely generated \(\mathbf Z\)-subalgebras. Finite-presentation algebra data, and the étale property, descend to one such Noetherian algebra \(A_0\). The exact finite-data foundations are [Stacks, Tags 01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation) and [07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale): finitely many equations and maps descend, their finitely many identities hold at a later stage, and étale Jacobian presentations descend after further refinement. Pull back the just-constructed partition of \(\operatorname{Spec}A_0\). Its strata remain constructible locally closed, and on them the map is finite étale.

This stratification argument also applies to a qcqs étale source over an affine base, even if the source is nonseparated. Choose a finite affine covering \(V_i\) of the source, and finite affine covers of all \(V_i\cap V_j\). Apply the affine result to every one of these finitely many affine maps and take a common partition of the base. On any resulting stratum, the \(V_i\)'s and the affine pieces of their intersections are finite étale. Each such intersection piece is an open immersion into \(V_i\) which is also finite over the stratum, hence is closed in \(V_i\). The overlaps are therefore clopen. After refining these finitely many clopen subsets, the gluing is a finite disjoint union of clopen pieces of the finite \(V_i\)'s, so the entire source over the stratum is finite étale. In particular this handles the possibly nonaffine inverse image of an affine base open.

Now work Zariski locally on \(X\) and use that stratification. By base change for \(a_!\), on a stratum our sheaf is the finite-étale direct image of \(\underline M\), by (2.2). On an étale splitting cover this is a finite direct sum of copies of \(M\). It is locally constant and has the required finite generation or finite underlying values. \(\square\)

We will also use the following finite-cover observation for all qcqs schemes, without a Noetherian hypothesis:

\[
\left(\mathop{\mathrm{colim}}_\alpha\mathcal F_\alpha\right)(V)
 =\mathop{\mathrm{colim}}_\alpha\mathcal F_\alpha(V)
\quad\text{for a qcqs étale basis object }V.
\tag{4.2}
\]

Indeed every covering family of \(V\) has a finite basis subcover. Matching on such a cover is a finite equalizer of finite products, which commutes with a filtered colimit. Hence the presheaf colimit on this finite-cover basis is already a sheaf. Fiber products remain qcqs, so the same argument applies to the overlaps. This proves (4.2). By (4.1), each \(P_V\) is compact for filtered colimits.

## 5. Filtered approximation, not always a union

**Theorem 5.1.** Every sheaf of \(\Lambda\)-modules on a qcqs scheme is a filtered colimit of constructible module sheaves. Every torsion abelian sheaf is a filtered colimit of constructible abelian sheaves. On a general qcqs scheme the transition and structure maps need not be injective.

**Proof.** The \(P_V\)'s generate all module sheaves. For every section over every affine étale basis object, (4.1) gives a map \(P_V\to\mathcal F\); their sum is surjective, because every geometric germ is represented by such a section. Do the same for its kernel. This gives a presentation

\[
\bigoplus_{b\in B}P_{V_b}
 \longrightarrow\bigoplus_{a\in A}P_{U_a}
 \longrightarrow\mathcal F\longrightarrow0.
\tag{5.1}
\]

Each single relation \(P_{V_b}\to\bigoplus_AP_{U_a}\) factors through a finite partial sum by (4.2) and compactness. Take finite sets of generators and finite sets of relations whose images use only those generators. Ordered by inclusion, these finite presentations form a filtered system. Every generator and relation occurs at some stage, so exactness of filtered sheaf colimits identifies its colimit with (5.1)'s cokernel. Each finite cokernel is constructible by Lemma 4.1 and Proposition 3.2. This proves the module assertion.

For a torsion sheaf, \(\mathcal F=\mathop{\mathrm{colim}}_{N\mid N'}\mathcal F[N]\); the order is divisibility, so the system is filtered. Apply the module assertion to each \(\mathbf Z/N\)-module \(\mathcal F[N]\). To verify that the combined approximation can be filtered, use the category of all constructible abelian sheaves equipped with a map to \(\mathcal F\). Two objects map to their direct sum; parallel maps are equalized by their cokernel, which is constructible and still maps to \(\mathcal F\). Thus this category is filtered.

Its colimit maps surjectively onto \(\mathcal F\) on stalks because any torsion germ is represented, after shrinking a neighborhood, by an \(N\)-torsion section, hence by a map \(a_!\mathbf Z/N\to\mathcal F\). For injectivity, if a germ in one constructible source maps to zero, represent it by a section on an affine pointed neighborhood where its image is zero. The source is killed by some \(N\), since its finite partition has finitely many finite abelian values. The section defines \(a_!\mathbf Z/N\to\mathcal C\); its composite to \(\mathcal F\) is zero. Passing to its constructible cokernel kills the germ in the filtered system. This proves stalk injectivity and the second assertion. \(\square\)

Here is why “constructible subsheaves” would be a false strengthening. Let \(A=\prod_{m\geq1}\mathbf F_2\), \(X=\operatorname{Spec}A\), and \(e_m\) the coordinate idempotents. This is an affine, hence qcqs, scheme. The points \(D(e_m)\) are isolated singletons. Their union \(U\) is a dense open which is not quasi-compact: its singleton cover has no finite subcover. It is not all of the compact space \(X\). Density follows because any nonempty \(D(a)\) contains a coordinate where \(a_m=1\). Put

\[
\mathcal Q=\operatorname{Coker}
   (j_!\mathbf F_{2,U}\longrightarrow\mathbf F_{2,X}).
\tag{5.2}
\]

Its stalks are zero on \(U\) and \(\mathbf F_2\) on the nonempty complement \(Z\). Every basic open in this Boolean-ring spectrum is clopen, so every constructible subset is clopen. A constructible subsheaf of \(\mathcal Q\) would have constructible support contained in \(Z\), hence clopen support disjoint from the dense \(U\). That support is empty, so the subsheaf is zero. The nonzero torsion sheaf \(\mathcal Q\) is therefore not a union of constructible subsheaves. Theorem 5.1 still applies to it.

**Lemma 5.2 (finite presentation and detection).** A constructible module sheaf has a finite presentation by the \(P_V\)'s and is compact for filtered colimits. If \(h:T\to X\) is a surjective morphism of qcqs schemes, a module sheaf \(\mathcal F\) is constructible if and only if \(h^{-1}\mathcal F\) is constructible. The same statements hold for torsion abelian sheaves using the finite-coefficient generators.

**Proof.** A qcqs scheme is compact in its constructible topology. On an affine, one proof takes an ultrafilter of constructible conditions and defines the prime ideal \(\mathfrak p=\{a:V(a)\text{ belongs to the ultrafilter}\}\); the identities for \(V(ab)\) and the containment \(V(a)\cap V(b)\subset V(a+b)\) prove primality and the ideal axioms. Its point satisfies all the selected basic conditions. This proves compactness, and a finite affine cover proves the qcqs version.

For a constructible \(\mathcal C\), consider all finite partial sums of its generating surjection (5.1). Their cokernels are constructible, hence have constructible supports. These supports decrease and have empty intersection: each finitely generated stalk is generated by some finite partial sum. Compactness makes one support empty. Thus a finite sum \(P_0\to\mathcal C\) is surjective. Its kernel is constructible by Proposition 3.2 and has a similar finite generating surjection \(P_1\to\ker(P_0\to\mathcal C)\). This is the desired finite presentation. Hom from its cokernel is the equalizer of Hom from the two finite sums. Formula (4.2) and commutation of filtered colimits with finite limits prove compactness. The finite-abelian case uses a common annihilator and the identical argument.

For detection, one implication is pullback permanence. For the converse write \(\mathcal F\) as the filtered colimit from Theorem 5.1. Upstairs the cokernels of maps \(h^{-1}\mathcal C_\alpha\to h^{-1}\mathcal F\) are constructible. Their supports decrease to the empty set, so compactness gives an epimorphism for some \(\alpha\). Surjectivity of \(h\) and geometric stalks imply that \(\mathcal C_\alpha\to\mathcal F\) itself is an epimorphism.

Let \(\mathcal K\) be its kernel. Exact pullback makes \(h^{-1}\mathcal K\) constructible upstairs. Repeat the argument for \(\mathcal K\), obtaining an epimorphism \(\mathcal D\to\mathcal K\) from a constructible sheaf. Then \(\mathcal K\) is the image of the map \(\mathcal D\to\mathcal C_\alpha\) between constructible sheaves, so is constructible. Its cokernel \(\mathcal F\) is constructible as well. This last two-step argument is needed: an arbitrary quotient of a constructible sheaf need not be constructible on a non-Noetherian scheme. \(\square\)

## 6. Extension by zero and finite pushforward preserve constructibility

**Theorem 6.1.** Let \(X\) be qcqs. Extension by zero along an étale morphism \(j:U\to X\) of finite presentation preserves constructible abelian sheaves and constructible \(\Lambda\)-modules. So does pushforward along a finite morphism \(f:Y\to X\) of finite presentation.

**Proof for \(j_!\).** The scheme \(U\) is qcqs. Present \(\mathcal F\) by finitely many generators \(P_V\) on \(U\), using affine étale \(V\to U\). Exactness and transitivity of extension by zero give

\[
j_!\mathcal F=
\operatorname{Coker}\!\left(
\bigoplus_b(jb)_!\underline\Lambda_{V_b}
\longrightarrow
\bigoplus_a(ja)_!\underline\Lambda_{U_a}\right).
\tag{6.1}
\]

Each composed map is étale of finite presentation. Its inverse images of affine base opens are qcqs; the full stratification argument of Lemma 4.1 makes these finitely many generators constructible. Proposition 3.2 makes their cokernel constructible. Finite abelian coefficients give the same proof. This also covers nonseparated \(j\); no embedding interpretation of \(j_!\) was used. \(\square\)

We give the finite-pushforward proof, including its non-Noetherian step, rather than invoke a finiteness theorem intended for a later lesson.

**Finite algebra splitting lemma 6.2.** For a finite morphism over an integral Noetherian affine \(X\), there is a nonempty affine open \(W\subset X\) and a finite faithfully flat affine \(T\to W\) such that \((Y\times_XT)_{\mathrm{ét}}\) is equivalent, over \(T_{\mathrm{ét}}\), to the étale topos of a finite disjoint union of copies of \(T\).

**Proof.** Let \(A\) be the base domain, \(K\) its fraction field and \(B\) the finite algebra. Its generic fiber is an Artinian \(K\)-algebra. After a finite field extension \(L/K\), including any needed inseparable extensions, the reduction of \(B_K\otimes_KL\) is \(L^r\) for some \(r\). This follows by taking the finitely many residue fields of the Artinian algebra, adjoining all their algebraic generators in an algebraic closure, and then splitting the separable embeddings. Thus there is a surjection

\[
B_K\otimes_KL\longrightarrow L^r
\tag{6.2}
\]

with nilpotent kernel.

Choose an \(A\)-subalgebra \(C\subset L\) with fraction field \(L\), generated by finitely many field generators. After localizing \(A\), their monic equations have coefficients in \(A\), so \(C\) is finite. Choose a \(K\)-basis of \(L\) from \(C\), and clear denominators expressing a finite set of module generators of \(C\) in that basis. A further localization makes \(C\) free over \(A\) of rank \([L:K]\), hence faithfully flat.

The map (6.2) extends to an algebra map \(B\otimes_AC\to C^r\) after another localization of \(A\). Its finitely many images and identities have coefficients in \(L=C\otimes_AK\); clearing their \(A\)-denominators suffices. Its cokernel is a finite \(A\)-module with zero generic fiber, so a nonzero element of \(A\) annihilates it. Localize to make the map surjective. Its kernel \(J\) is a finite \(A\)-module because \(A\) is Noetherian and both algebras are finite. Some power \(J^e\) has zero generic fiber, and is again a finite \(A\)-module, so another localization makes \(J^e=0\).

For \(T=\operatorname{Spec}C\), we now have a closed immersion \(\coprod_1^rT\to Y_T\) defined by a nilpotent ideal. Topological invariance of the étale site identifies their étale topoi over \(T\). All localizations were by finitely many nonzero base elements, so their common open \(W\) is nonempty. If \(r=0\), the same clearing argument makes \(Y_W\) empty, and the assertion uses the empty disjoint union. \(\square\)

**Proof for finite \(f_*\), Noetherian base.** Work on an affine base. Use Noetherian induction on closed subsets. Nilpotents in the base can be removed by topological invariance and finite-pushforward base change. There are finitely many irreducible components; remove their intersections and work on their generic integral open parts. On each such part apply Lemma 6.2.

Finite-pushforward base change gives

\[
(f_*\mathcal F)|_T=(f_T)_*(\mathcal F|_{Y_T}).
\tag{6.3}
\]

Under the splitting lemma, the right side is the finite product of the restrictions of \(\mathcal F\) to the copies of \(T\). Those restrictions are constructible by pullback permanence, so their finite product is constructible. Lemma 5.2 detects constructibility along the finite surjection \(T\to W\). We have therefore found a constructible generic open part of the base. On its closed complement, finite base change identifies the restricted pushforward with pushforward for the restricted finite morphism; Noetherian induction applies. Combining the finitely many resulting partitions proves constructibility on the original base.

**Proof for finite \(f_*\), general base.** Again work on an affine base \(\operatorname{Spec}A\), so \(Y=\operatorname{Spec}B\). Write \(A=\mathop{\mathrm{colim}}A_i\) with \(A_i\) finitely generated over \(\mathbf Z\). The finite-presentation algebra \(B\) descends to some \(B_i\), and after increasing \(i\) the map is finite. Explicitly its finitely many generators satisfy monic relations over \(A\); those coefficients and relations descend at one stage, making the descended algebra integral and finitely generated, hence finite. The exact finite-data locator for this step is [Stacks, Tag 01ZO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-finite-presentation).

Present \(\mathcal F\) by finitely many generators from Lemma 5.2. The affine étale algebras defining those generators descend over \(B_i\). Base change for extension by zero identifies their pullbacks with the original generators. Each of the finitely many entries of the relation map is a section on a qcqs étale object, by (4.1). The degree-zero continuity theorem for affine inverse systems, proved in the earlier direct-image lesson, makes it the pullback of a section at a sufficiently late stage. Thus the finite presentation descends to a constructible \(\mathcal F_i\) on \(\operatorname{Spec}B_i\). This does not assume a constructible-sheaf descent theorem: the finite presentation and the actual section-continuity statement prove precisely the descent needed.

The Noetherian case makes \(f_{i*}\mathcal F_i\) constructible. Finite base change identifies \(f_*\mathcal F\) with its inverse image over \(A\), which is constructible by Proposition 3.2. The same argument with a common finite annihilator handles finite abelian sheaves. This completes Theorem 6.1. \(\square\)

Finite presentation is substantive here. In the Boolean example (5.2), let \(I=\bigoplus_m\mathbf F_2e_m\subset A\), the ideal of sequences of finite support. Then \(Z=V(I)\), and the closed immersion \(i:\operatorname{Spec}(A/I)\to X\) is finite but is not of finite presentation: finitely many elements of \(I\) involve only finitely many coordinates, so cannot generate it. The constant finite sheaf on \(Z\) is constructible, whereas its pushforward is \(\mathcal Q\) by (1.3), with nonconstructible support \(Z\). Thus the finite-presentation restriction cannot simply be dropped.

## 7. What improves on a Noetherian scheme

**Proposition 7.1.** On a Noetherian scheme, every subobject or quotient of a constructible \(\Lambda\)-module is constructible. The same holds for constructible abelian sheaves. The Noetherian objects of the category of all \(\Lambda\)-module sheaves are exactly its constructible objects in the finite-generation convention; the Noetherian objects of the category of torsion abelian sheaves are exactly its finite-stalk constructible objects. Every torsion abelian sheaf is consequently the filtered union of its constructible subsheaves.

**Proof.** We first prove the subobject assertion for \(\mathcal G\subset\underline M\), where \(M\) is a finitely generated module and the base is irreducible Noetherian. At a geometric generic point the submodule \(M'\subset M\) is finitely generated, since \(\Lambda\) is Noetherian. Lift finitely many generators of \(M'\) to sections of \(\mathcal G\) on a common pointed étale neighborhood, and shrink it until their images in \(\underline M\) are the constant generators.

These sections descend to the open image of that neighborhood: their two pullbacks agree in \(\underline M\), hence in its subsheaf \(\mathcal G\). On that nonempty open we have \(\underline{M'}\subset\mathcal G\). There can be no further section values. A nonempty étale open with any additional constant value maps onto an open of the irreducible base containing its generic point, contradicting \(\mathcal G_{\bar\eta}=M'\). Thus \(\mathcal G=\underline{M'}\) on a nonempty open. Isolate the finitely many generic components for a reducible base, and apply Noetherian induction to the closed remainder. This proves that a subsheaf of a constant finitely generated module on any Noetherian scheme is constructible.

For a general constructible module, take its finite locally constant partition. On each piece choose a finite qc étale trivializing cover. Each member is Noetherian; the preceding argument makes the pulled-back subobject constructible. Detection in Lemma 5.2 then makes it constructible on that piece, hence on the whole scheme. A quotient is now the cokernel of a map between constructible modules. For finite abelian sheaves choose a common annihilator and apply this argument over its finite coefficient ring.

Let \(\mathcal G_1\subset\mathcal G_2\subset\cdots\subset\mathcal C\) be an increasing chain with \(\mathcal C\) constructible. Its union is a subobject of \(\mathcal C\), hence constructible and compact by Lemma 5.2. Its identity factors through some \(\mathcal G_m\), so that subobject is the whole union and the chain stabilizes. This proves the ascending chain condition.

Conversely a module sheaf, or a torsion abelian sheaf in the torsion category, is the filtered colimit from Theorem 5.1. The images of its constructible sources are constructible by the quotient assertion just proved. Their finite sums form a directed union equal to the sheaf. The ascending chain condition forces some finite sum to be the entire sheaf: otherwise successively adjoining an image not already contained would produce an infinite strict ascending chain. It is therefore constructible.

Finally, for any torsion abelian sheaf, its constructible source images form the asserted filtered union. This last union statement uses the Noetherian hypothesis; (5.2) shows precisely why it cannot be extended to every qcqs scheme. \(\square\)

In the general \(\Lambda\)-module assertion, “constructible” uses finite generation. In the torsion-abelian assertion it uses finite underlying values. This keeps the Noetherian-object statement consistent even when the ring is infinite.

## 8. Trace and reduction to an \(\ell\)-group

**Theorem 8.1 (finite étale trace).** If \(f:Y\to X\) is finite étale of constant degree \(d\), there is a natural map

\[
\operatorname{Tr}_f:f_*f^{-1}\mathcal F\longrightarrow\mathcal F
\quad\text{with}\quad
\operatorname{Tr}_f\circ\mathrm{unit}=d\,\mathrm{id}_{\mathcal F}.
\tag{8.1}
\]

If multiplication by \(d\) on \(\mathcal F\) is invertible, restriction
\(H^q(X,\mathcal F)\to H^q(Y,f^{-1}\mathcal F)\) is split injective for every \(q\).

**Proof.** On an étale cover splitting \(Y\) into \(d\) sheets, \(f_*f^{-1}\mathcal F\) is \(\mathcal F^d\). Define trace as the sum of its coordinates. Permuting the sheets preserves the sum, so these local maps agree on overlaps and glue. The adjunction unit is the diagonal map, whose composite with summation is \(d\). This proves naturality and (8.1); it also identifies trace with the counit of \(f_!=f_*\).

Finite direct image is exact, and the earlier finite-morphism comparison gives

\[
H^q(Y,f^{-1}\mathcal F)
 =H^q(X,f_*f^{-1}\mathcal F).
\tag{8.2}
\]

Apply cohomology to (8.1). The restriction followed by trace is multiplication by \(d\). Its inverse, if it exists on the sheaf, induces the inverse on cohomology; composing it with trace gives a left inverse to restriction. In particular the conclusion holds for \(\mathbf Z/n\)-modules if \(\gcd(d,n)=1\), with an explicit inverse scalar \(a\) satisfying \(ad\equiv1\pmod n\). \(\square\)

**Proposition 8.2 (Sylow reduction).** On a connected scheme \(X\), a finite locally constant \(\mathbf F_\ell\)-sheaf \(\mathcal L\) becomes a successive extension of constant \(\mathbf F_\ell\)-sheaves after a connected finite étale cover of degree prime to \(\ell\).

**Proof.** Its monodromy representation has finite image \(G\subset\mathrm{GL}(M)\). Choose an \(\ell\)-Sylow subgroup \(H\). The transitive \(\pi_1\)-set \(G/H\) defines a connected finite étale cover \(T\to X\) of degree \([G:H]\), prime to \(\ell\). Its monodromy subgroup is the inverse image of \(H\): the category of covers over a pointed transitive cover is the slice of finite \(\pi_1\)-sets over \(G/H\), equivalently finite sets for the stabilizer of that point. Thus the pulled-back representation factors through \(H\).

For a nonzero finite-dimensional \(\mathbf F_\ell\)-space \(V\) with an \(H\)-action, count the \(H\)-orbits of its underlying finite set. Nonfixed orbits have sizes divisible by \(\ell\); hence \(|V^H|\equiv|V|=0\pmod\ell\). Since zero is fixed, there are at least \(\ell\) fixed vectors, including a nonzero one. Its line is a trivial subrepresentation. Repeat on the quotient by that line. Induction on dimension constructs a full \(H\)-stable flag with trivial one-dimensional quotients. Finite-local-system classification turns it into the required sheaf filtration. \(\square\)

This is an actual trace application: if constant \(\mathbf F_\ell\)-coefficients have zero \(H^q(T,-)\), every successive extension in the filtration also has zero \(H^q\), by the long exact sequences in that fixed degree. Trace then injects \(H^q(X,\mathcal L)\) into zero. A vanishing theorem for constants on the chosen covers therefore yields the same vanishing for these local systems.

There is a useful \(\ell^a\)-coefficient variant. For a finite \(\ell\)-group \(H\), the augmentation ideal \(I\) of \(\mathbf F_\ell[H]\) is nilpotent. To prove it, choose a central element \(z\) of order \(\ell\), supplied by the class equation and Cauchy's theorem. The central element \(z-1\) has \((z-1)^\ell=0\). Modulo it the algebra is \(\mathbf F_\ell[H/\langle z\rangle]\). By induction its augmentation ideal has zero \(N\)-th power, so \(I^N\subset(z-1)\), and \(I^{N\ell}=0\). The trivial group starts the induction. In \((\mathbf Z/\ell^a)[H]\), reduction modulo \(\ell\) gives \(J^N\subset\ell R\), hence \(J^{Na}=0\). The filtration by the \(J^bM\)'s of an \(\ell^a\)-torsion module has quotients on which \(H\) acts trivially. If a coefficient ring acts and commutes with \(H\), these are coefficient submodules; over a Noetherian ring their subquotients remain finitely generated. For a local system with finite underlying values, the same Sylow cover and trace construction apply.

## 9. Examples of the open part and its boundary

For \(j:\mathbf A^1-\{0\}\to\mathbf A^1\), \(j_!\mathbf Z/n\) has stalk \(\mathbf Z/n\) at every geometric point of the open and zero at \(0\). It is constructible on the two pieces. Its global sections on \(\mathbf A^1\) are zero: the counit \(j_!\mathbf Z/n\to\mathbf Z/n\) is injective on stalks, and any global section of the constant sheaf on the connected affine line is constant. Its value at \(0\) must be zero, so it is zero everywhere. The localization sequence

\[
0\to j_!\mathbf Z/n\to\mathbf Z/n
  \to i_*\mathbf Z/n\to0
\tag{9.1}
\]

also shows that the open and closed data need not give a direct sum. For \(n>1\) this sequence is nonsplit: a section of the constant sheaf supported only at \(0\) must be zero on every connected étale neighborhood meeting the puncture, so a map \(i_*\mathbf Z/n\to\mathbf Z/n\) is zero.

**Kummer local systems.** Over an algebraically closed field with \(n\) invertible, the cover \(z^n=t\) of \(\mathbf G_m\) is a finite étale right \(\mu_n\)-torsor. Given a character \(\chi:\mu_n(k)\to\Lambda^\times\) for a finite coefficient ring, form the associated sheaf using
\((z\epsilon,v)\sim(z,\chi(\epsilon)v)\). Its local trivializations are free rank-one \(\Lambda\)-modules, with transitions given by \(\chi\) applied to the torsor transitions. It is finite locally constant. Extending by zero to \(\mathbf A^1\) gives a constructible sheaf with zero stalk at the boundary, whether or not its monodromy is trivial.

**Artin–Schreier local systems.** In characteristic \(p\), \(y^p-y=t\) is monic of degree \(p\), with derivative \(-1\). It is therefore a finite étale \(\mathbf F_p\)-torsor on \(\mathbf A^1\), with right action by translations \(y\mapsto y+a\). A character \(\psi:\mathbf F_p\to\Lambda^\times\), for a finite coefficient field of characteristic different from \(p\) containing the needed roots, gives a rank-one locally constant sheaf by the same associated-sheaf construction. This is the sheaf behind additive-character sums; later trace-formula lessons study its arithmetic values.

**A constructible curve sheaf.** On a smooth curve over an algebraically closed field, choose a dense open \(U\) on which a constructible sheaf is finite locally constant, and let \(S=X-U\) be finite. Such a \(U\) exists by its finite partition, after retaining a generic open piece; one-dimensional closed proper subsets are finite. Formula (1.3) becomes

\[
0\to j_!\mathcal L\to\mathcal F
 \to\bigoplus_{x\in S}i_{x*}M_x\to0.
\tag{9.2}
\]

Thus local systems and skyscrapers describe the pieces, while the extension records their gluing. Sequence (9.1) demonstrates why “local system plus skyscrapers” need not mean a split sum.

## 10. The inertia stalk for one puncture

**Proposition 10.1.** Let \(X\) be a smooth integral curve, separated and of finite type over a field, \(x\) a closed point, \(j\colon X-\{x\}\to X\), and \(\mathcal L\) a finite locally constant sheaf. Then \(j_*\mathcal L\) is constructible. At a geometric point \(\bar x\),

\[
(j_*\mathcal L)_{\bar x}=M^{I_x}.
\tag{10.1}
\]

Here \(M\) is its geometric generic fiber and \(I_x\) is the image of the absolute Galois group of
\(F_x=\operatorname{Frac}\mathcal O_{X,x}^{\mathrm{sh}}\) in the punctured curve's fundamental group, after compatible basepoint choices. This is the local inertia image.

**Proof.** The strict henselization is a discrete valuation ring: the common-uniformizer proof in the preceding curve lesson applies with the separable residue closure in place of \(k\). Its inverse image of the punctured curve is \(\operatorname{Spec}F_x\). Degree-zero strict-local continuity and the direct-image stalk formula identify the left side with sections of \(\mathcal L\) over this field. Field-topos comparison says these are exactly the fixed elements of its geometric generic fiber under \(G_{F_x}\), or under its image \(I_x\). This proves (10.1); changing compatible basepoints conjugates the image and transports the invariant fiber accordingly.

The stalk is finite, as a subset of finite \(M\). On the open, the pushforward restricts to \(\mathcal L\). On the closed stratum \(\operatorname{Spec}\kappa(x)\), its inverse image is the finite set or finite module in (10.1) with its residual continuous Galois action. Any finite continuous Galois action is killed by an open normal subgroup, so this is a finite locally constant sheaf on that field. The two strata are constructible on the Noetherian curve, proving the assertion. \(\square\)

This is a direct curve computation. It supplies no general theorem that arbitrary open pushforward preserves constructibility.

## 11. Exercises and complete solutions

1. For an open immersion \(j:U\to X\), compute the stalks of \(j_!\mathcal F\). Prove the characterization by restriction and zero boundary stalks.
2. For a smooth integral curve and one puncture, prove the inertia-invariant stalk formula for a finite local system and deduce constructibility of its open pushforward.
3. Give an infinite sum of constructible torsion sheaves which is not constructible. Prove the correct filtered-colimit approximation on qcqs schemes, and distinguish it from the Noetherian union statement.
4. Prove that the affine-local definition of constructibility is equivalent, on a qcqs scheme, to a finite partition into constructible locally closed pieces with finite locally constant restrictions.
5. If \(f:Y\to X\) is finite étale of degree prime to \(n\), prove that restriction on \(H^q(-,\mathcal F)\) is injective for every \(\mathbf Z/n\)-module sheaf and every \(q\). Identify a left inverse.

**Solution 1.** A geometric point of an open subscheme has exactly one lift; a geometric point outside it has none. The direct-sum formula (1.2) therefore gives \(\mathcal F_{\bar x}\) inside \(U\) and zero outside. The adjunction unit \(\mathcal F\to j^{-1}j_!\mathcal F\) is the identity on those inside stalks, hence an isomorphism. If \(\mathcal G|_U\simeq\mathcal F\) and \(\mathcal G\) has zero outside stalks, adjunction gives \(j_!\mathcal F\to\mathcal G\). It is an isomorphism on inside stalks and a map \(0\to0\) outside, hence an isomorphism. This proves both existence and uniqueness, with the specified restriction identification.

**Solution 2.** Put \(R=\mathcal O_{X,x}^{\mathrm{sh}}\) and \(F=\operatorname{Frac}R\). Étale local rings over the original discrete valuation ring have the same uniformizer; the filtered-union argument proves \(R\) is a discrete valuation ring. The punctured strict-local scheme is \(\operatorname{Spec}F\). The stalk formula and degree-zero continuity give
\((j_*\mathcal L)_{\bar x}=\Gamma(\operatorname{Spec}F,\mathcal L)\). Field-topos comparison identifies this with \(M^{G_F}=M^{I_x}\), where the action is the restricted monodromy. It is finite. The sheaf is locally constant on the punctured open and finite locally constant on the closed point, with its residual Galois action. These two locally closed pieces are constructible, so they provide the required finite partition. This proof works over a non-algebraically-closed ground field as well.

**Solution 3.** On the spectrum of an algebraically closed field the étale topos is sets. The sheaf \(\bigoplus_{m\geq1}\mathbf F_\ell\) has an infinite stalk, and hence is not constructible; every finite partial sum is constructible.

For the general approximation, generate a \(\mathbf Z/N\)-module sheaf by all maps \(a_!\mathbf Z/N\) indexed by its sections over affine étale basis objects. Generate the kernel in the same way. Each relation uses finitely many generators because sections on a qcqs basis object commute with filtered colimits of finite partial sums. Finite sets of generators and relations therefore give a filtered system of finite presentations, all constructible by Lemma 4.1 and cokernel permanence, with the desired sheaf as colimit. A torsion sheaf is the filtered colimit of its \(N\)-torsion parts. The category of all constructible sheaves mapping to it is filtered by finite sums and cokernels of parallel maps; the stalk argument in Theorem 5.1 verifies that its colimit is exactly the sheaf.

Over a Noetherian scheme, replace the constructible sources by their images; those images are constructible by Proposition 7.1, so they give a union. Over a general qcqs scheme this replacement can fail: the Boolean-spectrum sheaf (5.2) is nonzero but has no nonzero constructible subsheaf. Thus the approximation assertion remains true, while the asserted union would be false.

**Solution 4.** A global finite partition restricts to a finite constructible locally closed partition on every affine open, and its finite local systems restrict to finite local systems. This proves one direction.

Conversely choose a finite affine cover of the qcqs scheme and a finite partition on each member. Quasi-separatedness makes each affine inclusion quasi-compact, so each of those constructible subsets is constructible in the whole scheme. Intersect the finitely many pieces and their complements and refine their Boolean combinations into locally closed parts. One can choose the refinement so every part lies in one of the original affine pieces: first partition by the finite affine covering, then by the partitions of the covering members. Each refined part is constructible and locally closed, and on it the sheaf is a restriction of a finite local system. This supplies a global finite partition. The same proof works for finitely generated constant modules. On a Noetherian scheme every locally closed subset is constructible; on a general qcqs scheme that extra word cannot be discarded.

**Solution 5.** Split \(f\) étale locally into \(d\) copies of the base. The unit is the diagonal and trace is their sum, so their composite is \(d\). These maps glue because the sum is invariant under all sheet permutations. Exact finite direct image and its cohomology comparison identify \(H^q(Y,f^{-1}\mathcal F)\) with \(H^q(X,f_*f^{-1}\mathcal F)\). Choose an integer \(a\) with \(ad\equiv1\pmod n\). Since \(\mathcal F\) is a \(\mathbf Z/n\)-module, multiplication by \(ad\) on all its cohomology is the identity. Hence

\[
a\,H^q(\operatorname{Tr}_f):
H^q(Y,f^{-1}\mathcal F)\longrightarrow H^q(X,\mathcal F)
\tag{11.1}
\]

is a left inverse to restriction for every \(q\). This proves split injectivity without any constructibility assumption on \(\mathcal F\).

## 12. Sources and scope

The corresponding results of the Stacks project are [Stacks, Tag 03S2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-extension-by-zero) for extension by zero, [Tag 09Y8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-locally-constant) for locally constant sheaves, [Tag 05BE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-constructible) for constructibility, [Tag 03SA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-torsion-colimit-constructible) for filtered approximation, [Tag 095R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-finite-pushforward-constructible) for finite pushforward of finite presentation, and [Tag 03SH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-trace-method) for the trace method. The Noetherian subobject theorem is [Tag 09BH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-proposition-constructible-over-noetherian); the ascending-chain assertion has the additional locator [Tag 09YV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-constructible-over-noetherian-noetherian).

[SGA 4](https://www.normalesup.org/~forgogozo/SGA4/), Exposé XVII, §§5.1.1–5.1.2, treats open extension by zero and its base change; the presheaf, stalk and base-change proofs above are self-contained. The finite trace and the group-theoretic filtration are fully supplied here.

Constructible and perverse sheaves in the real and complex analytic setting use related stratification language, but different sites and coefficient conventions; they are a separate subject. The next lessons study the cohomological finiteness and base-change assertions for which this étale constructibility formalism is the input.
