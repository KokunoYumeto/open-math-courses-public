# Hom complexes, internal derived Hom and Ext sheaves

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original text: public domain (CC0). Authorship and sources are listed in the [course notice](../LICENCE.md).*

The tensor product combines two inputs, whereas internal Hom records maps from one input to another as an object on the space. Derived internal Hom must detect extensions as well as ordinary maps. Its degree-zero global cohomology recovers maps in the derived category; its other cohomology sheaves record local extensions. These statements involve derived sections, which cannot generally be replaced by ordinary sections of a cohomology sheaf.

The prerequisites are [Derived pullback and pushforward](derived-pullback-and-pushforward.md), Proposition 3.2 and Theorem 4.1, for restriction and local cohomology; [The derived tensor product and Tor sheaves](derived-tensor-products-and-tor-sheaves.md), Lemma 1.1, Lemma 2.1 and Theorem 2.2, for K-flat models and their localization; and [K-injective resolutions in Grothendieck categories](k-injective-resolutions-in-grothendieck-categories.md), Theorems 4.1 and 5.1. We also use maps into K-injectives and their cone closure from Theorem 3.3 and Lemma 3.1 of [Injective modules and bounded-below derived functors](injective-modules-and-bounded-below-derived-functors.md). The common reading's Theorems 3.1 and 4.2 supply cone triangles and roof cancellation.

Throughout, \(\mathcal O=\mathcal O_X\) is a sheaf of commutative unital rings on an arbitrary topological space. Complexes are cohomologically indexed and may be unbounded in both directions. Tensor totalization uses sums, Hom totalization uses products, and a cone triangle ends in the negative projection. Write \(\mathsf H(A,B)\) for the sheaf Hom complex, reserving \(\operatorname{Hom}\) for a group of maps.

The construction follows the Stacks project authors’ *Cohomology of Sheaves*, “Hom complexes”, “Internal hom”, “Ext sheaves” and “Global derived hom”, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex). Composition is natural in its outer variables and dinatural in the repeated middle variable; Section 4 proves the precise identities. Source attribution appears in the [course notice](../LICENCE.md).
## 1. The sheaf Hom complex

For two module sheaves define the internal Hom by

\[
\begin{gathered}
\mathcal Hom(A,B)(U)\\
=\operatorname{Hom}_{\mathcal O_U}(A|_U,B|_U).
\end{gathered}
\tag{1.1}
\]

Restriction means restricting a map. Compatible maps on an open cover glue: for each local section of \(A\), their images agree and glue in \(B\). The glued assignment respects restriction, addition and scalar multiplication because these properties can be checked on the cover. This proves the sheaf condition. Commutativity gives it its \(\mathcal O\)-module action by multiplying the output.

For complexes set

\[
\begin{aligned}
\mathsf H^n(A,B)&=\prod_i\mathcal Hom(A^i,B^{i+n}),\\
(d\phi)^i&=d_B\phi^i\\
&\quad-(-1)^n\phi^{i+1}d_A.
\end{aligned}
\tag{1.2}
\]

The product is the sheaf product; on every open it is the product of the section groups. Applying the differential twice leaves two mixed terms with coefficients \(-(-1)^n\) and \(-(-1)^{n+1}\), which cancel. The remaining terms contain \(d_B^2\) or \(d_A^2\). Thus this is a complex. A degree-zero cycle is a chain map, and a degree-zero boundary is a null-homotopic map. With the usual shifted differential this proves

\[
\begin{gathered}
H^n\Gamma(U,\mathsf H(A,B))\\
=\operatorname{Hom}_{K(\mathcal O_U)}(A|_U,B|_U[n]).
\end{gathered}
\tag{1.3}
\]

Restriction to an open commutes with (1.1) and (1.2): their values on each smaller open are identical. This observation concerns restriction, not passage to a stalk. An infinite product need not commute with stalks, and a germ of a module map need not be an arbitrary map of stalk modules.

**Lemma 1.1 (chain identities).** Hom complexes respect homotopies. There is a natural currying isomorphism

\[
\begin{gathered}
\mathsf H(K,\mathsf H(L,M))\\
\cong\mathsf H(K\otimes L,M).
\end{gathered}
\tag{1.4}
\]

Evaluation and composition are chain maps, given on homogeneous elements by

\[
\begin{aligned}
\phi\otimes l&\longmapsto\phi(l),\\
\phi\otimes\psi&\longmapsto\phi\psi.
\end{aligned}
\tag{1.5}
\]

**Proof.** If \(h:B\to B'[-1]\) is a homotopy between two target maps, the induced Hom homotopy is \(\phi\mapsto h\phi\). If \(h:A'\to A[-1]\) is a homotopy between two source maps, it is \(\phi\mapsto(-1)^n\phi h\) on degree \(n\). Substitution into (1.2) gives respectively postcomposition and precomposition with \(dh+hd\); the mixed terms cancel. Hence both variables descend to homotopy categories.

Currying sends \(\phi\) to the map \(k\otimes l\mapsto\phi(k)(l)\), with no additional sign. The tensor relation is exactly the linearity in each variable. In degree \(n\), both sides are the product over pairs of degrees \((i,j)\) of
\(\mathcal Hom(K^i\otimes L^j,M^{i+j+n})\). This uses the universal property that Hom out of a sum is a product, followed by reindexing a product. It uses no exactness assertion about products. For homogeneous \(k\), their common differential evaluated at \(k,l\) is

\[
\begin{aligned}
d_M\phi(k)(l)&-(-1)^n\phi(d_Kk)(l)\\
&-(-1)^{n+|k|}\phi(k)(d_Ll).
\end{aligned}
\]

Finally \(d(\phi(l))=(d\phi)(l)+(-1)^{|\phi|}\phi(dl)\) and
\(d(\phi\psi)=(d\phi)\psi+(-1)^{|\phi|}\phi(d\psi)\). These are precisely the tensor differentials, proving (1.5). All constructions are sectionwise and therefore commute with restriction. \(\square\)

We also need the cone signs. For \(g:B\to B'\), the two finite blocks give
\(\mathsf H(A,C(g))=C(\mathsf H(A,g))\); the identity identification preserves the differential and negative projection. For \(f:K\to L\), put \(h=\mathsf H(f,I)\). In degree \(n\), an element of \(\mathsf H(C(f),I)\) is a pair \((b,a)\), where \(b\) has Hom degree \(n\) on \(L\) and \(a\) has degree \(n-1\) on \(K\). The isomorphism to \(C(h)[-1]\) is

\[
(b,a)\longmapsto\bigl((-1)^{n+1}a,b\bigr).
\tag{1.6}
\]

Indeed the source differential is \((db,da-(-1)^nbf)\), and the shifted cone differential on \((x,y)\) is \((-dx-hy,dy)\). Formula (1.6) intertwines them. The source-shift identification
\(\mathsf H(K[1],I)\cong\mathsf H(K,I)[-1]\) multiplies degree \(n\) by \((-1)^n\). Together these formulas turn a source cone triangle into the reversed distinguished Hom triangle, with its connecting map determined by the negative original projection. This verifies exactness in the contravariant variable, including its shift sign.

## 2. Constructing internal derived Hom

**Lemma 2.1.** Let \(I\) be K-injective. A quasi-isomorphism \(s:A\to B\) induces a quasi-isomorphism
\(\mathsf H(B,I)\to\mathsf H(A,I)\).

**Proof.** On every open \(U\), the restriction of \(I\) is K-injective, by the preceding lesson's Proposition 3.2. Maps into it are unchanged by localization. Thus precomposition by \(s|_U\) is a bijection on
\(\operatorname{Hom}_{K(\mathcal O_U)}(-,I|_U[n])\) for every integer \(n\). Formula (1.3) gives a quasi-isomorphism of the section Hom complexes on every open. The cohomology sheaf is the sheafification of section-complex cohomology, as proved in that proposition; sheafifying these isomorphisms proves the claim. Applying the argument to every shift is essential: degree zero alone would not prove a quasi-isomorphism. \(\square\)

**Theorem 2.2.** For any \(L,M\), choose a K-injective resolution \(M\to I\). Then

\[
\begin{aligned}
{}[L,M]&:=R\mathcal Hom(L,M)\\
&=\mathsf H(L,I).
\end{aligned}
\tag{2.1}
\]

defines an object of \(D(\mathcal O)\) and a canonical bifunctor, contravariant in \(L\), covariant in \(M\), exact in each variable. It commutes with restriction to opens.

**Proof.** Resolutions exist for every unbounded complex by the earlier K-injective theorem. The map from \(M\) to another resolution determines a unique homotopy class \(I\to I'\) under the maps from \(M\): maps into a K-injective are the same in the homotopy and derived categories. Such a comparison is a quasi-isomorphism between K-injectives, hence a homotopy equivalence. Lemma 1.1 carries its two homotopy inverses to inverse Hom maps. Comparisons are unique in the homotopy category, so their composites obey the required identity and cocycle laws.

In the source variable Lemma 2.1 inverts every quasi-isomorphism. A roof acts by its numerator and the inverse of its denominator; common refinements give the same action because Hom respects homotopies. In the target variable represent a derived map by the unique homotopy class between K-injective models. Composition of these classes, and commutation with source precomposition, prove bifunctoriality and natural independence of resolutions.

Source cone triangles give reversed Hom triangles by (1.6). A target map between K-injectives has K-injective cone by the earlier cone-closure lemma, so it supplies a model for the entire target triangle. The target cone identity proves exactness there. Shift identifications are those checked after (1.6). Finally restricting \(M\to I\) gives a K-injective resolution on each open, and the sectionwise identity for Hom gives the asserted restriction isomorphism, natural in all roofs. \(\square\)

**Lemma 2.3.** If \(P\) is K-flat and \(I\) K-injective, then \(\mathsf H(P,I)\) is K-injective.

**Proof.** For an acyclic complex \(A\), Lemma 1.1 and degree-zero homotopy classes give

\[
\operatorname{Hom}_K(A,\mathsf H(P,I))
=\operatorname{Hom}_K(A\otimes P,I)=0.
\]

The tensor is acyclic by K-flatness, and the last group vanishes by K-injectivity. This is the defining test for K-injectivity. No injectivity of the individual terms of \(\mathsf H(P,I)\) is required. \(\square\)

## 3. Adjunction, local maps and Ext

**Theorem 3.1.** There are natural isomorphisms

\[
\begin{gathered}
{}[K,[L,M]]\cong[K\otimes^{\mathbf L}L,M],\\
\operatorname{Hom}_D(K,[L,M])\\
\cong\operatorname{Hom}_D(K\otimes^{\mathbf L}L,M).
\end{gathered}
\tag{3.1}
\]

For every open \(U\) and integer \(n\),

\[
\begin{gathered}
H^n(U,[L,M])\\
\cong\operatorname{Hom}_{D(\mathcal O_U)}(L|_U,M|_U[n]).
\end{gathered}
\tag{3.2}
\]

**Proof.** Resolve \(L\) by a K-flat \(P\) and \(M\) by a K-injective \(I\). Lemma 2.1 permits the model \(\mathsf H(P,I)\) for \([L,M]\); Lemma 2.3 makes this model K-injective. Therefore (1.4) is an actual complex isomorphism computing both sides of the first line of (3.1). The complex \(K\otimes P\) computes the derived tensor even when \(K\) is not K-flat, by Lemma 1.1 of the tensor lesson. Taking homotopy classes and using maps into K-injectives gives the second line.

Naturality holds first for chain maps by currying. For source maps represented by roofs, Lemma 2.1 inverts the source denominators, and tensor invariance inverts the denominators on the other side. Comparison maps between K-flat models can be represented in their localized homotopy category, by the tensor lesson's Lemma 2.1. Target comparisons are homotopy classes between K-injectives. Thus the same commuting chain squares and their inverse denominator squares prove naturality for every derived morphism, not only actual chain maps on fixed resolutions.

For (3.2), restrict these models to \(U\). Restriction preserves K-flatness and K-injectivity. The K-injective model \(\mathsf H(P,I)|_U\) computes derived sections, so (1.3) identifies its cohomology with the stated group of derived maps. \(\square\)

Define the Ext sheaves and global derived Hom by

\[
\begin{gathered}
\mathcal Ext^n(L,M)=\mathcal H^n([L,M]),\\
R\operatorname{Hom}_X(L,M)\\
=R\Gamma(X,[L,M]).
\end{gathered}
\tag{3.3}
\]

The global object is a complex over \(\Gamma(X,\mathcal O)\). Its underlying abelian cohomology can equally be computed by the preceding lesson's coefficient comparison. Formula (3.2) identifies its \(n\)-th cohomology with \(\operatorname{Hom}_D(L,M[n])\).

In particular, a derived morphism is represented locally by a degree-zero cycle in a Hom complex into a K-injective target, modulo its degree-zero boundaries. Composition in Proposition 4.1 below induces the usual composition of these classes. For a triangle in either input, Theorem 2.2 gives a triangle of internal Hom objects, and derived sections give the resulting long exact sequence of groups of maps. The source-variable connecting map includes the shift sign in (1.6); the target-variable map includes the negative cone projection. Thus the local extension groups and their boundary operations come from the same proved triangle conventions as the global ones. No choice of an unrelated connecting-homomorphism sign is needed.

The Ext sheaf is the sheafification of the presheaf sending \(U\) to the right side of (3.2). To see this directly, use the model \(\mathsf H(P,I)\); sheafifying its section-complex cohomology gives its cohomology sheaf. This does not identify ordinary sections of \(\mathcal Ext^n\) with that derived-map group on an arbitrary open. Sheafification may change sections.

There is also a convenient formula with an arbitrary representative \(L\): the complex \(\Gamma(X,\mathsf H(L,I))\) computes global derived Hom. Although \(\mathsf H(L,I)\) need not be K-injective, its comparison to \(\mathsf H(P,I)\) is a quasi-isomorphism on sections by (1.3) and the K-injective map test. The latter is a K-injective sheaf complex, so its sections compute the derived sections. For module sheaves \(F,G\) in degree zero choose a bounded-below injective resolution \(G\to I^{\geq0}\). Its Hom complex from \(F\) has no negative degrees and degree-zero kernel \(\mathcal Hom(F,G)\). Hence
\(\mathcal Ext^n(F,G)=0\) for \(n<0\), and \(\mathcal Ext^0(F,G)=\mathcal Hom(F,G)\).

### Internal Hom into a skyscraper

**Proposition 3.2.** For every point \(x\), every unbounded \(L\in D(\mathcal O_X)\), and every unbounded \(M\in D(\mathcal O_x)\), there is a natural isomorphism
\[
R\mathcal Hom_X(L,x_*M)
\simeq x_*\operatorname{RHom}_{\mathcal O_x}(L_x,M).
\]
No closed-point or finite-presentation hypothesis is required.

**Proof.** On an open \(U\) containing \(x\), the stalk–skyscraper adjunction of the first lesson identifies
\[
\operatorname{Hom}_{\mathcal O_U}(L|_U,x_*M|_U)
=\operatorname{Hom}_{\mathcal O_x}(L_x,M).
\]
On an open not containing \(x\), the target is zero. These identifications respect restriction and scalar action, so they give the ordinary sheaf-Hom isomorphism. For complexes, apply the identification to each pair of degrees and form the Hom products. The skyscraper preserves products by Proposition 5.3 of the first lesson, and the component identifications commute with the differential \(d_M\phi-(-1)^{|\phi|}\phi d_L\). Thus the same identity holds for Hom complexes.

Resolve \(M\) by a K-injective \(J\) over \(\mathcal O_x\). The exact stalk functor is left adjoint to \(x_*\), so \(x_*J\) is K-injective by the exact-left-adjoint criterion. Exactness of \(x_*\) also makes \(x_*M\to x_*J\) a quasi-isomorphism. The preceding Hom-complex identity now computes both sides of the derived statement. Functoriality of the ordinary adjunction and the K-injective comparison establish naturality and independence of the choice of \(J\). \(\square\)

This is the useful special case developed by Daniel Murfet in [*Derived Categories of Sheaves*, §7.2, Lemma 104 and Proposition 106](https://therisingsea.org/notes/DerivedCategoriesOfSheaves.pdf). It coexists with the warning after (1.3): for an arbitrary target, passage to stalks need not commute with internal derived Hom. The special target and its two adjunctions are what justify the formula here.

## 4. Evaluation, composition and their variances

The adjunction gives a safe way to construct canonical maps without asserting that an arbitrary ordinary tensor of Hom complexes computes a derived tensor. Its counit is evaluation

\[
e_{L,M}:[L,M]\otimes^{\mathbf L}L\longrightarrow M.
\tag{4.1}
\]

It is the transpose of the identity of \([L,M]\). On models it is (1.5), after any K-flat replacement needed for its tensor factors. Currying and its naturality show that this construction is independent of those replacements.

**Proposition 4.1 (composition).** There is a canonical associative, unital composition map

\[
\begin{gathered}
c_{K,L,M}:[L,M]\otimes^{\mathbf L}[K,L]\\
\longrightarrow[K,M].
\end{gathered}
\tag{4.2}
\]

It is natural contravariantly in \(K\), covariantly in \(M\), and dinatural in \(L\): for \(u:L\to L'\), the two maps from \([L',M]\otimes^{\mathbf L}[K,L]\) to \([K,M]\) satisfy

\[
\begin{aligned}
c_{K,L,M}\circ([u,M]\otimes1)&\\
\quad=c_{K,L',M}\circ(1\otimes[K,u]).&
\end{aligned}
\tag{4.3}
\]

**Proof.** Put \(A=[L,M]\), \(B=[K,L]\). Define (4.2) to be the transpose of successive evaluations

\[
\begin{aligned}
(A\otimes^{\mathbf L}B)\otimes^{\mathbf L}K
&\longrightarrow A\otimes^{\mathbf L}L\\
&\longrightarrow M.
\end{aligned}
\tag{4.4}
\]

Here and below association maps are the coherent tensor isomorphisms proved in the tensor lesson. Evaluation is natural in its target. For a source map \(u\), its defining adjunction gives the identity that evaluating \(u,M\) on \(l\) equals evaluating \(a\) on \(u(l)\). This is an identity of morphisms in the derived category: transpose either side by (3.1), and both are precomposition of the same identity map by \(u\). It therefore holds for roofs as well as chain maps.

Postcomposing (4.4) by a map \(M\to M'\) proves target naturality. Precomposing its last tensor factor by a map \(K'\to K\), and applying the source evaluation identity, proves source naturality. For (4.3), transpose both sides and apply that identity once. Both become successive evaluation with \(u\) inserted between the two evaluations. Symbolically both give \(a(u(b(k)))\). The adjunction is a bijection of map groups, so equality of the transposes proves equality of the maps.

For four objects, either order of composition transposes to the same three successive evaluations. The tensor associator satisfies the pentagon, so this proves associativity. The identity of \(L\) corresponds by (3.2) to a morphism \(\mathbf1=\mathcal O\to[L,L]\). Evaluation with this morphism is the identity on \(L\), by its transpose; inserting it on either side of (4.4) proves both unit laws. These arguments prove all assertions without changing resolutions in the middle of an unverified diagram. \(\square\)

The word *dinatural* records the opposing variances of the two occurrences of \(L\). A map \(L\to L'\) induces \([L',M]\to[L,M]\) but \([K,L]\to[K,L']\). Thus the source of composition is not a covariant or contravariant one-variable functor of \(L\). Formula (4.3) is the well-typed compatibility statement. It does not require \(u\) to be invertible.

**Proposition 4.2 (other canonical maps).** Put \(L^\vee=[L,\mathbf1]\). There are canonical maps

\[
\begin{aligned}
K&\longrightarrow[L,K\otimes^{\mathbf L}L],\\
K\otimes^{\mathbf L}[M,L]
&\longrightarrow[M,K\otimes^{\mathbf L}L],\\
M\otimes^{\mathbf L}L^\vee&\longrightarrow[L,M],\\
[L,M]\otimes^{\mathbf L}K&\longrightarrow[[K,L],M].
\end{aligned}
\tag{4.5}
\]

The first is the adjunction unit, natural in \(K\) and dinatural in \(L\). The second is natural covariantly in \(K,L\) and contravariantly in \(M\). The third is natural covariantly in \(M\), contravariantly in \(L\). The last is natural covariantly in \(K,M\), contravariantly in \(L\).

**Proof.** Transpose the identity of \(K\otimes^{\mathbf L}L\) to obtain the first. If \(\eta_{K,L}\) denotes it and \(u:L\to L'\), both sides of

\[
\begin{gathered}
{}[u,K\otimes^{\mathbf L}L']\eta_{K,L'}\\
=[L,K\otimes^{\mathbf L}u]\eta_{K,L}.
\end{gathered}
\tag{4.6}
\]

transpose to \(1_K\otimes u\). This proves its middle-variable dinaturality; ordinary target naturality proves its \(K\) naturality.

For the second map, transpose \(1_K\otimes e_{M,L}\). For the third, transpose \(1_M\otimes e_{L,\mathbf1}\), followed by the unit isomorphism. For the last, its transpose has domain
\(([L,M]\otimes^{\mathbf L}K)\otimes^{\mathbf L}[K,L]\). Move \(K\) past \([K,L]\) using the Koszul symmetry, evaluate \([K,L]\) on \(K\), and then evaluate \([L,M]\) on the result. Each stated naturality follows from the evaluation identities already proved, followed by the naturality of transposition. On homogeneous chain representatives of degrees \(p,q,r\), this last construction is

\[
(\phi\otimes k)(h)=(-1)^{qr}\phi(h(k)).
\tag{4.7}
\]

The sign comes from moving \(k\) past \(h\), not past \(\phi\). Lemma 1.1 and the tensor symmetry prove it is a chain map whenever the chosen models compute these derived constructions. \(\square\)

These are maps, with no general claim of invertibility. The perfect-complex lesson proves that the third is an isomorphism when \(L\) is perfect. The final exercise below shows a concrete failure without this hypothesis. The unit in (4.5), just like composition, has a repeated variable with opposite variances; writing its compatibility as (4.6) prevents a second misleading blanket functoriality claim.

## 5. Worked examples

First, \([\mathcal O,M]\cong M\). Evaluation at \(1\) identifies \(\mathsf H(\mathcal O,I)\) with \(I\), including its differential. The K-injective resolution identifies this with \(M\). The corresponding global statement is
\(R\operatorname{Hom}_X(\mathcal O,M)=R\Gamma(X,M)\), which may have higher cohomology even when \(M\) is a sheaf.

Let \(j:U\hookrightarrow X\) be open. For any K-injective resolution \(F\to I\), the extension-by-zero adjunction on every open \(V\) gives

\[
\mathsf H(j_!\mathcal O_U,I)(V)
=\Gamma(V\cap U,I).
\]

These identities respect differentials and restrictions. The right side is \(j_*(I|_U)(V)\), and \(I|_U\) is K-injective. Consequently

\[
[j_!\mathcal O_U,F]\cong Rj_*(F|_U).
\tag{5.1}
\]

The ordinary Hom sheaf in degree zero is \(j_*F|_U\), not extension by zero. It can have a nonzero boundary stalk. Higher Ext sheaves describe the higher local cohomology of intersections with \(U\), through the local pushforward formula of the preceding lesson.

For a second example take \(X=\mathbf C\) with holomorphic functions and let \(k_a\) be the skyscraper residue module at \(a\). The tensor lesson's [holomorphic coordinate germ lemma](derived-tensor-products-and-tor-sheaves.md#holomorphic-coordinate-germs) gives the parameter resolution

\[
P_a=(\mathcal O\xrightarrow{z-a}\mathcal O).
\tag{5.2}
\]

It lies in degrees minus one and zero, with augmentation given by evaluation at \(a\). At \(a\), the lemma proves that multiplication by \(z-a\) is injective and that its image is the evaluation kernel. At every other point \(z-a\) is a holomorphic unit and the residue stalk is zero. Exactness on stalks therefore proves \(P_a\to k_a\) is a quasi-isomorphism. This finite free complex can be used in the source of derived Hom. Indeed \(\mathsf H(\mathcal O,-)\) is the identity, so a finite filtration by its two terms shows \(\mathsf H(P_a,-)\) preserves quasi-isomorphisms. Thus comparison with any K-injective resolution of \(k_b\) proves that \(\mathsf H(P_a,k_b)\) computes \([k_a,k_b]\). It has \(k_b\) in degrees zero and one, with differential multiplication by \(-(b-a)\). If \(b\ne a\), this is invertible and the Hom object is zero. If \(b=a\), the differential is zero and

\[
[k_a,k_a]\cong k_a\oplus k_a[-1].
\tag{5.3}
\]

In particular, the sheaf Ext in degree one is \(k_a\); all other positive Ext sheaves vanish. These objects describe the derived Hom of modules over the holomorphic structure sheaf, not Hom of arbitrary skyscraper abelian sheaves. Changing the coefficient ring changes the calculation.

Here is an explicit reason for the stalk warning after (1.3). Let \(X=\{0\}\cup\{1,1/2,1/3,\ldots\}\) with its subspace topology, and use the constant ring sheaf \(k_X\) for a field. Set \(A=\bigoplus_{j\geq1}k_X\) and \(B=k_X\). The sum's universal property gives
\(\mathcal Hom(A,B)=\prod_{j\geq1}k_X\): specifying a map on an open means specifying the image of the unit in each summand. For each \(j\), let \(f_j\) be the locally constant function which is one at \(1/j\) and zero at every other point. It is locally constant at zero too, since a sufficiently small neighborhood excludes that particular point. Hence \((f_j)_j\) is a section of this product on all of \(X\).

Every individual \(f_j\) has zero germ at zero. The induced map of stalk modules \(A_0=\bigoplus_j k\to B_0=k\) is therefore zero, since an element of the direct sum uses only finitely many coordinates. But the germ of the section \((f_j)_j\) of the Hom sheaf is nonzero: every neighborhood of zero contains some \(1/j\), where its \(j\)-th coordinate is one. Thus the canonical comparison
\(\mathcal Hom(A,B)_0\to\operatorname{Hom}_k(A_0,B_0)\) is not even injective. The issue already appears for ordinary Hom, before any derived construction. Restriction to a fixed open is valid because it preserves the whole sectionwise product; moving to a germ cannot uniformly discard the infinitely many shrinking exceptional points.

## 6. Exercises with checked solutions

**Exercise 1 (easy: the unit).** Prove \([\mathcal O,M]=M\), and determine the unit \(K\to[\mathcal O,K\otimes^{\mathbf L}\mathcal O]\) under the tensor and Hom unit identifications.

**Solution.** A map \(\mathcal O|_V\to I^n|_V\) is determined by the image of \(1\), with every section \(a\) sent to \(a\) times that image. These identifications commute with restriction and the differential, so \(\mathsf H(\mathcal O,I)=I\). For the unit, the adjunction transpose of the identity of \(K\otimes^{\mathbf L}\mathcal O\) is the map in question. Evaluation at \(1\) and the tensor unit both send that identity back to \(1_K\). Hence the unit becomes the identity of \(K\), in every degree and for every unbounded complex.

**Exercise 2 (medium: currying without boundedness).** Explain why (3.1) holds without a finiteness condition on any complex. In particular, identify the step where products are needed and distinguish it from an assertion that products of exact sequences are exact.

**Solution.** Choose a K-flat \(P\to L\) and K-injective \(M\to I\). In Hom degree \(n\), currying identifies the product indexed by \(i,j\) of maps \(K^i\otimes P^j\to I^{i+j+n}\) on both sides. On the tensor side the source in each degree is a direct sum, so specifying a map means independently specifying a map on every summand. Rearranging the resulting products gives exactly the Hom product on the iterated side. Formula (1.4)'s differential calculation proves the identification is a complex isomorphism.

K-flatness makes \(K\otimes P\) a model for the derived tensor; Lemma 2.3 makes \(\mathsf H(P,I)\) an admissible K-injective target. Consequently both Hom complexes compute the stated derived Hom objects. Quasi-isomorphisms in the first variable are handled on every open by Lemma 2.1, and target comparisons by homotopy equivalences. No step applies a product to an arbitrary exact sequence of sheaves. The product's universal property and the two resolution properties are sufficient.

**Exercise 3 (medium: a middle-variable example).** Over a field, take \(K=M=k\), \(L=k^2\), \(L'=k\), and \(u(x,y)=x\), all in degree zero. Verify (4.3) and explain why it is the appropriate replacement for one-variable naturality.

**Solution.** Write \(a:L'\to M\) as multiplication by \(\alpha\), and \(b:K\to L\) as \(t\mapsto(\beta t,\gamma t)\). Precomposing \(a\) by \(u\) gives the row \((\alpha,0)\). Its product with the column \((\beta,\gamma)\) is multiplication by \(\alpha\beta\). Postcomposing \(b\) by \(u\) gives multiplication by \(\beta\), so composing with \(a\) gives the same answer. Bilinearity proves equality on the tensor product. All these vector spaces are flat and injective, so the calculation is also the derived one.

The map on the first factor goes from \(\operatorname{Hom}(L',M)\) to \(\operatorname{Hom}(L,M)\), whereas the map on the second goes from \(\operatorname{Hom}(K,L)\) to \(\operatorname{Hom}(K,L')\). Their directions oppose each other. Since \(u\) is a noninvertible projection, reversing one direction cannot be done by an inverse. Dinaturality compares the two composites on their common mixed source and does exactly what the calculation verifies.

**Exercise 4 (hard: the K-injective target test).** Let \(P\) be K-flat and \(I\) K-injective. Prove that \(\mathsf H(P,I)\) is K-injective using an explicit correspondence between maps and homotopies. Explain why termwise flatness alone does not justify this argument.

**Solution.** A chain map \(A\to\mathsf H(P,I)\) curries to a chain map \(A\otimes P\to I\) by (1.4). A homotopy is a degree-minus-one element whose Hom differential is the difference of the two maps. Since (1.4) is an isomorphism of complexes, it carries exactly such homotopies in either direction. Thus it gives a bijection on homotopy classes. If \(A\) is acyclic, K-flatness makes \(A\otimes P\) acyclic, and K-injectivity of \(I\) says every resulting chain map is null-homotopic. Uncurrying that null-homotopy proves the defining condition for \(\mathsf H(P,I)\).

The flat-resolution lesson, Section 5, gives an unbounded termwise-free complex over the dual numbers whose tensor with an acyclic complex is not acyclic. Termwise flatness therefore cannot supply the crucial implication for an unbounded \(P\). Bounded-above termwise-flat complexes do supply it, by that lesson's Lemma 2.3; the distinction is between that proved bounded case and the general K-flat condition.

**Exercise 5 (hard: a dual map that fails).** Let \(R=k[\varepsilon]/(\varepsilon^2)\) on a one-point space and \(N=R/(\varepsilon)\). Compute \(N^\vee\), compare \(N\otimes_R^{\mathbf L}N^\vee\) with \([N,N]\), and show the canonical degree-zero map is zero.

**Solution.** The only ideals of \(R\) are \(0,(\varepsilon),R\). A map from \((\varepsilon)\) to \(R\) sends \(\varepsilon\) to an element killed by \(\varepsilon\), necessarily \(c\varepsilon\), and extends by multiplication by \(c\). Maps from the other two ideals extend immediately. Baer's criterion, proved in the bounded-derived lesson's Lemma 2.1, makes \(R\) injective. It is therefore K-injective concentrated in degree zero. Consequently

\[
N^\vee=\operatorname{Hom}_R(N,R)
=(\varepsilon)\cong N,
\]

concentrated in degree zero. A free resolution of \(N\) has one copy of \(R\) in every nonpositive degree, all negative differentials multiplication by \(\varepsilon\), and the quotient augmentation in degree zero. It is exact in negative degrees because the image and kernel of multiplication by \(\varepsilon\) both equal \((\varepsilon)\).

Tensoring this bounded-above free resolution with \(N^\vee\cong N\) makes all differentials zero. Thus the left object has cohomology \(N\) in every nonpositive degree and zero in positive degrees. Hom from that resolution to \(N\) likewise has zero differential but lies in nonnegative degrees. It computes \([N,N]\): a map \(a:P\to C\) to any acyclic complex has a null-homotopy constructed downwards. In degree zero, \(a^0\) lands in the cycles of \(C^0\), and projectivity lifts it through \(d:C^{-1}\to Z^0C\) to \(h^0\). Having chosen \(h^{n+1}\), the map \(a^n-h^{n+1}d_P\) lands in \(Z^nC\) by the chain-map equation and the preceding homotopy equation. Lift it to \(h^n:P^n\to C^{n-1}\). This constructs \(a=dh+hd\) in every nonpositive degree, with no infinite summation. Applying the same argument to every shift proves \(\operatorname{Hom}^\bullet(P,C)\) acyclic. Cone compatibility then proves invariance under every target quasi-isomorphism, including \(N\to I\). The right object therefore has cohomology \(N\) in every nonnegative degree, and zero in negative degrees.

Finally degree-zero evaluation sends \(m\otimes\phi\) to the map \(n\mapsto\phi(n)m\). Every \(\phi(n)\) lies in \((\varepsilon)\), which acts by zero on \(N\). Hence this induced map on degree-zero cohomology is zero. The canonical dual map is far from an isomorphism in this example. Finite duality in the perfect-complex lesson will require a hypothesis this residue module does not satisfy.
