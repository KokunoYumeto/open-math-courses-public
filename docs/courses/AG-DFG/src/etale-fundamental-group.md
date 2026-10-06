# The étale fundamental group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The étale fundamental group records every finite étale covering of a connected scheme. Its definition uses a geometric fibre, but its content is the entire category of covers and their maps. The categorical theorem of *Galois categories* will do the reconstruction once we verify the geometric axioms. We then compute examples, explain the function-field description for normal schemes, and prove the exact sequence separating geometric covers from arithmetic ones.

Throughout, schemes called connected are nonempty. A geometric point \(\bar x\) is a morphism \(\operatorname{Spec}\Omega\to X\) from an algebraically closed field. No Noetherian, separation or quasi-compactness assumption is implicit in the first four sections. The arithmetic exact sequence will explicitly require quasi-compactness and quasi-separatedness.

## 1. The category of finite étale covers

Write \(\operatorname{F\acute Et}(X)\) for finite étale \(X\)-schemes, including the empty scheme, with all \(X\)-morphisms. We use the étale-local splitting theorem from the étale-neighbourhood prerequisite: every finite étale map becomes a finite disjoint union of copies of its base on an étale covering [Stacks, Tag 04HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-etale-etale-local). The number of copies can vary between covering members.

A map between two finite étale \(X\)-schemes is itself finite étale. Étaleness is the cancellation property for two schemes étale over the same base [Stacks, Tag 02GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-permanence). Finiteness can be checked locally after splitting both objects: a map between finite sets of copies is a finite map. More directly its graph is a closed immersion into their fibre product, since the target is separated over \(X\), and the projection of that product to the target is finite. This observation applies even when \(X\) is not separated.

**Proposition 1.1.** The category \(\operatorname{F\acute Et}(X)\) has finite limits and finite colimits. Base change along every morphism \(X'\to X\) preserves all of them. [Stacks, Tag 0BN9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-covers-limits-colimits)

*Proof.* The terminal object is \(X\), and fibre products are finite étale. Terminal objects and fibre products construct all finite limits; their formation commutes with base change. Finite coproducts are disjoint unions, including the empty union.

It remains to construct a coequalizer of \(a,b: Z\rightrightarrows Y\). Write \(Y=\underline{\operatorname{Spec}}_X\mathcal B\) and \(Z=\underline{\operatorname{Spec}}_X\mathcal C\), for finite locally free algebras. Set

\[
\mathcal A=\ker(a^\sharp-b^\sharp:\mathcal B\to\mathcal C).
\tag{1.1}
\]

This is an algebra containing the unit and a quasi-coherent module. The latter assertion follows by computing kernels of quasi-coherent modules on affines; multiplication restricts because the two maps are algebra maps. On an étale cover splitting \(Y,Z\), further split the base into open pieces on which the maps between their finite sets of labels are fixed. Such pieces exist because the inverse images of the open-and-closed summands are open and closed. The number of possible label maps is finite.

On one such piece, let the maps of labels be \(a_0,b_0:J\rightrightarrows I\), and let \(I\to T\) be their finite-set coequalizer. The two algebra maps are coordinate pullbacks, and (1.1) becomes

\[
\{(r_i)\in\mathcal O^I:r_{a_0(j)}=r_{b_0(j)}\text{ for all }j\}
=\mathcal O^T.
\tag{1.2}
\]

Thus \(\mathcal A\) is locally a finite product of copies of the structure sheaf. Finite local freeness and étaleness descend by the previous two lessons. Hence \(Q=\underline{\operatorname{Spec}}_X\mathcal A\) is finite étale. The algebra equalizer property is exactly the coequalizer universal property in the opposite category of affine \(X\)-schemes, and every finite étale \(X\)-scheme is affine over \(X\). Thus \(Y\to Q\) is the required coequalizer.

We must also check arbitrary base change; tensor products need not preserve an arbitrary kernel. There is a canonical comparison from the pullback of (1.1) to the equalizer for the pulled-back maps. On the same split covering, formula (1.2) identifies both with the structure sheaf of the new base raised to the finite power \(T\). The comparison is an isomorphism there. The pulled-back covering is still étale and surjective, so faithful flatness detects that it is an isomorphism globally. Thus these particular equalizers commute with every base change, including nonflat ones. This proves right exactness and finishes the proof. \(\square\)

The constructed finite colimits also have their universal property among all schemes [Stacks, Tag 0BNA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-remark-colimits-commute-forgetful). For the only additional case, take a map \(Y\to T\) to an arbitrary scheme equalizing \(a,b\). On the split covering used in (1.2), the maps from copies of the base agree whenever their labels lie in one equivalence class, so give a unique map from the copies indexed by the finite quotient set in (1.2). These factorizations agree on overlaps by uniqueness. Faithfully flat descent of morphisms from *Faithfully flat descent* glues them to a unique map \(Q\to T\). Thus the coequalizer is also a scheme coequalizer. The forgetful functor to schemes over \(X\) preserves all finite limits; the functor to schemes preserves equalizers and fibre products, and hence connected finite limits. Its terminal object need not be a terminal scheme.

**Proposition 1.2 (internal Hom).** For finite étale \(U,V\) over \(X\), there is a finite étale \(X\)-scheme \(\mathcal H\) with natural bijections

\[
\operatorname{Hom}_X(T,\mathcal H)
\simeq\operatorname{Hom}_T(U_T,V_T)
\tag{1.3}
\]

for every \(X\)-scheme \(T\). [Stacks, Tag 0BL7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-internal-hom-finite-etale)

*Proof.* On a covering splitting \(U\) and \(V\) with label sets \(I,J\), take the disjoint union of copies of the base indexed by the finite set \(J^I\). Over any base change \(T\), a map from \(I\) copies of \(T\) to \(J\) copies is specified by a locally constant choice of a label in \(J\) for each element of \(I\). This is exactly a map to the scheme of label functions \(J^I\), so it represents (1.3), even when \(T\) is disconnected.

On overlaps, changing the labels of \(U\) and \(V\) induces the corresponding relabelling of their functions. Equivalently the representing property supplies unique transition isomorphisms. Uniqueness gives the cocycle. Affine descent from *Faithfully flat descent* glues these schemes; finite étale permanence gives a finite étale result. The local bijections (1.3) glue because morphisms of schemes are sheaves for faithfully flat coverings, also proved in that lesson. This proves representability and compatibility with all base change. \(\square\)

A monomorphism in \(\operatorname{F\acute Et}(X)\) is precisely an inclusion of an open-and-closed subscheme. Indeed its diagonal is an isomorphism, since the category has the scheme fibre products. It is therefore a scheme monomorphism. After étale-local splitting its label map is injective, so it is an open-and-closed inclusion locally and hence globally. Conversely such an inclusion is monic and remains finite étale over \(X\).

**Theorem 1.3.** If \(X\) is connected, then

\[
F_{\bar x}:\operatorname{F\acute Et}(X)\longrightarrow\operatorname{FinSets},
\qquad Y\longmapsto |Y_{\bar x}|
\tag{1.4}
\]

makes this category a Galois category. [Stacks, Tag 0BNB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-connected-galois-category)

*Proof.* Proposition 1.1 supplies finite limits and colimits. A finite étale scheme over an algebraically closed field is a finite disjoint union of points, so (1.4) is the base-change functor followed by its identification with finite sets. Proposition 1.1 proves exactness.

The categorical connected objects are precisely the nonempty connected schemes, by the subobject description above. We verify that each cover is a finite coproduct of such objects without assuming local Noetherianness. Its locally free degree over the connected base \(X\) is a fixed finite integer \(n\). A nonempty open-and-closed piece is again finite étale; its image is open, by étaleness, and closed, by finiteness. That image is therefore all of \(X\). Its degree is a positive constant. If a piece is disconnected, split it into two nonempty open-and-closed pieces. Repeating this cannot produce more than \(n\) pieces, since their positive degrees sum to \(n\). Thus it terminates in connected pieces. For degree zero the cover is empty. This also shows these pieces are exactly its connected components.

Finally suppose \(f:Y\to Z\) is bijective on the chosen geometric fibres. Decompose \(Z\) into its connected components \(Z_i\). Each maps onto \(X\), as just proved. The finite étale map \(Y\times_ZZ_i\to Z_i\) has degree one at every point over \(\bar x\); such points exist. Degree is locally constant, so it is one throughout connected \(Z_i\). A finite locally free algebra of rank one is its base ring: its unit generates every residue-field fibre, so Nakayama makes the unit map an isomorphism locally, and hence globally. Thus each restriction of \(f\) is an isomorphism. So \(F_{\bar x}\) reflects isomorphisms. All four axioms of *Galois categories*, Section 2, are verified. \(\square\)

## 2. Definition, base points and Galois covers

For connected \(X\), define

\[
\pi_1(X,\bar x)=\operatorname{Aut}(F_{\bar x})
\tag{2.1}
\]

with the profinite topology of pointwise agreement on finitely many finite fibres [Stacks, Tag 0BNC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-definition-fundamental-group). Applying the reconstruction theorem of *Galois categories* to Theorem 1.3 gives

\[
\operatorname{F\acute Et}(X)\simeq
\operatorname{Fin}(\pi_1(X,\bar x)).
\tag{2.2}
\]

This equivalence includes all morphisms, finite limits and finite colimits [Stacks, Tag 0BND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-fundamental-group).

For another geometric point \(\bar x'\), the exact fibre-functor uniqueness theorem gives an isomorphism \(t:F_{\bar x}\simeq F_{\bar x'}\). Conjugating natural automorphisms by \(t\) identifies the groups topologically and preserves (2.2). Two choices of \(t\) differ by a natural automorphism, so the group isomorphisms differ by an inner conjugation. This is why a base-point-free assertion normally specifies the group only up to inner automorphism; it does not supply a preferred identification of two fibres.

For \(f:X\to S\) between connected schemes and \(\bar s=f\bar x\), base change is exact and has the canonical identification
\(F_{\bar x}(Y_X)=F_{\bar s}(Y)\). The functoriality theorem of *Galois categories* therefore gives a canonical continuous homomorphism

\[
f_*:\pi_1(X,\bar x)\longrightarrow\pi_1(S,\bar s).
\tag{2.3}
\]

Pulling back a cover means restricting its group action along (2.3). Successive pullbacks compose their canonical fibre identifications, so \((gf)_*=g_*f_*\). Other choices of base-point identifications introduce precisely the already described inner conjugations.

A **Galois cover** is a connected finite étale \(Y\to X\) whose group \(\operatorname{Aut}_X(Y)\) acts simply transitively on a geometric fibre. Connected-object one-point uniqueness from *Galois categories* makes this automorphism action free. Thus transitivity, simple transitivity and equality of its order with the degree of the cover are equivalent. They hold at one geometric fibre exactly when they hold at all, because the categorical characterization does not depend on the fibre functor.

Under (2.2), connected covers correspond to transitive sets \(\Pi/H\), with \(\Pi=\pi_1(X,\bar x)\) and \(H\) open. Pointing a cover selects a point of its fibre and hence a particular \(H\); forgetting it replaces \(H\) by its conjugacy class. Galois covers correspond to open normal subgroups \(N\). Their deck group is \((\Pi/N)^{\mathrm{op}}\) for the right-translation convention; inversion identifies this with \(\Pi/N\). Every connected cover is dominated by a Galois cover, by Galois domination in the preceding lesson. Two Galois covers have a common Galois dominator with quotient group the image of \(\Pi\) in the product of their finite quotients [Stacks, Section 03SF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-section-finite-etale-under-galois).

## 3. Fields and the generic point

For a field \(K\), fix an algebraic closure \(\bar K\) and its separable subclosure \(K^s\). A map from a finite separable extension into \(\bar K\) lands in \(K^s\). The field equivalence proved in *Galois categories*, Theorem 5.1, therefore identifies its fibre with (1.4) and gives the topological isomorphism

\[
\pi_1(\operatorname{Spec}K,\operatorname{Spec}\bar K)
\simeq\operatorname{Gal}(K^s/K).
\tag{3.1}
\]

The action on embeddings is \(g\cdot e=g\circ e\). In terms of geometric points it is precomposition by \(\operatorname{Spec}(g)\), whose contravariance gives the same left action [Stacks, Tags [0BNE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-fundamental-group-Galois-group), [0BQ9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-remark-variance)]. Hence finite fields give \(\widehat{\mathbf Z}\), topologically generated by arithmetic Frobenius, and separably closed fields give the trivial group.

Let \(X\) be irreducible and \(\eta\) its generic point, with residue field \(K=\kappa(\eta)\). Choosing a geometric point over \(\eta\), (2.3) gives

\[
\operatorname{Gal}(K^s/K)\longrightarrow\pi_1(X,\bar\eta).
\tag{3.2}
\]

We need a hypothesis on the branches of \(X\) before asserting that this map is surjective.

A local ring is **geometrically unibranch** if its strict henselization has a unique minimal prime. This is equivalent to the usual normalization-based definition [Stacks, Tag 06DM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-geometrically-unibranch). A scheme is geometrically unibranch when all its local rings are. A normal scheme has this property [Stacks, Tag 0BQ3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-normal-geometrically-unibranch). We use two strict-henselization facts from the étale-neighbourhood prerequisite: a strict henselization is faithfully flat over its local ring, and finite étale algebras over it split into copies of it.

**Proposition 3.1.** If \(X\) is irreducible and geometrically unibranch, every connected finite étale cover of \(X\) is irreducible. Consequently, for every nonempty open \(U\subset X\), both

\[
\pi_1(U,\bar u)\longrightarrow\pi_1(X,\bar u),
\qquad
\pi_1(\eta,\bar\eta)\longrightarrow\pi_1(X,\bar\eta)
\tag{3.3}
\]

are surjective. [Stacks, Tag 0BQI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-irreducible-geometrically-unibranch)

*Proof.* Let \(Y\to X\) be finite étale. Every generic point of \(Y\) maps to \(\eta\): if its image had a proper generalization, flat going down would lift that generalization, contradicting genericity [Stacks, Tag 03HV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-generalizations-lift-flat). There are finitely many such points because the fibre over \(\eta\) is finite. Thus \(Y\) has finitely many irreducible components.

At a point \(y\) over \(x\), put \(A=\mathcal O_{X,x}\), and take \(A^{sh}\). The finite étale algebra for \(Y\) over \(\operatorname{Spec}A\) becomes a product of copies of \(A^{sh}\). Choose a point in this product lying over \(y\); localizing there gives a faithfully flat map from \(\mathcal O_{Y,y}\) to \(A^{sh}\). Since the latter has a unique minimal prime, so does the former: every minimal prime lifts under faithful flatness and contracts from a minimal prime by going down. Hence two distinct irreducible components of \(Y\) cannot meet at \(y\). With only finitely many components, they are therefore pairwise disjoint closed subsets, and each is open. Connected \(Y\) has just one of them, so is irreducible.

For nonempty \(U\), its inverse image in any nonempty connected \(Y\) is nonempty, since \(Y\to X\) is surjective. It is an open subset of an irreducible space, hence connected. The surjectivity criterion of *Galois categories*, Theorem 4.2, proves the first map in (3.3) is surjective. Similarly \(Y_\eta\) has a single point: its points are precisely the generic points of \(Y\). To check the reverse inclusion, a generalization of a point over \(\eta\) must still lie over \(\eta\); the finite fibre has no proper specializations, so that point has no proper generalization. It is nonempty and hence a connected finite étale \(K\)-scheme. The same criterion proves the second assertion. This proof also applies when \(X\) is nonreduced; no replacement of a nonreduced generic local ring by a field is made except in the explicitly defined residue-field fibre. \(\square\)

For comparison, if a morphism has dense image, pullback of finite étale covers is always faithful, even without the branch hypothesis [Stacks, Tag 0BQE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-dense-faithful). To prove this, two maps are sections of the internal Hom in Proposition 1.2. Their equalizer is open and closed in the base, since the diagonal of a finite étale scheme is open and closed. If they become equal on a dense image, that equalizer is the whole base. Full faithfulness, and thus the surjectivity in (3.3), is a stronger assertion.

## 4. Normal schemes and unramified function-field extensions

Let \(X\) be normal integral with function field \(K\). For finite separable \(L/K\), let \(X_L\) be the normalization of \(X\) in \(L\): over \(\operatorname{Spec}A\subset X\) its algebra is the integral closure of \(A\) in \(L\). Say \(L\) is **unramified over \(X\)** when \(X_L\to X\) is unramified as a morphism of schemes. This includes local finite type; it is not merely a condition at codimension-one points. For arbitrary normal schemes we do not assume all these normalizations are finite.

**Lemma 4.1.** The normalization \(X_L\to X\) is unramified if and only if it is finite étale. [Stacks, Tag 0BQK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-unramified-in-L)

*Proof.* Finite étale implies unramified. Conversely a normalization is integral, and an integral locally finite type morphism is finite [Stacks, Tag 01WJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-integral). Work near a point of an affine normal domain \(A\), and let \(B\subset L\) be its now finite integral closure. For \(x\in\operatorname{Spec}A\), let \(R=\mathcal O_{X,x}^{sh}\). It is a normal domain [Stacks, Tag 06DI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-normal), and is flat over \(A\). Thus

\[
B\otimes_A R\ \subset\ L\otimes_A R.
\tag{4.1}
\]

Writing \(S=A\setminus\{0\}\), the right side is
\(L\otimes_K S^{-1}R\), free of rank \([L:K]\) over the domain \(S^{-1}R\). Therefore \(B\otimes_A R\) is torsion-free as an \(R\)-module.

The local structure theorem for finite unramified morphisms makes this algebra a finite product of quotients \(R/I_j\) [Stacks, Tag 04HJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-unramified-etale-local). To pass from that theorem's étale neighbourhood to \(R\), choose its point over the closed point with the fixed separable residue embedding; strict henselianity gives the corresponding section after base change to \(R\). Remove any empty factors. Each remaining quotient is torsion-free over the domain \(R\), by (4.1). If a nonzero element of \(I_j\) existed, it would annihilate its nonzero unit, a contradiction. Thus every \(I_j=0\). The normalization is a finite disjoint union of copies over \(R\), and hence étale there. Faithfully flat descent of étaleness over the local rings proves it is étale over \(X\). \(\square\)

**Lemma 4.2.** A connected finite étale \(Y\to X\) is normal integral and is the normalization of \(X\) in its finite separable function-field extension \(L/K\). [Stacks, Tag 0BQL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-covering-normal-unramified)

*Proof.* Normality ascends along étale maps, as stated in *Descending properties of schemes and morphisms*. Proposition 3.1 makes connected \(Y\) irreducible. Normal schemes are reduced, so \(Y\) is integral. Its generic fibre is finite étale and connected, giving a finite separable field \(L/K\).

On \(\operatorname{Spec}A\subset X\), its inverse image is \(\operatorname{Spec}B\) for a finite normal domain \(B\subset L\). It is contained in the integral closure of \(A\) in \(L\). Conversely if \(z\in L\) is integral over \(A\), its monic equation also has coefficients in \(B\), so it is integral over \(B\). Normality of \(B\) gives \(z\in B\). Thus \(B\) is exactly that integral closure. These identifications agree on overlaps, proving the normalization assertion. \(\square\)

The same reasoning includes all morphisms. A \(K\)-embedding between the generic fields of two connected covers carries elements integral over an affine base ring to elements integral over that ring; it therefore restricts to a map of their integral closures. These maps glue uniquely. Finite disjoint unions give the full morphism correspondence for arbitrary finite étale covers. In particular generic restriction is fully faithful.

**Theorem 4.3.** Let \(M\subset K^s\) be the union of all finite extensions unramified over \(X\). It is a Galois extension of \(K\), and (3.2) is the quotient map

\[
\operatorname{Gal}(K^s/K)\longrightarrow
\operatorname{Gal}(M/K)\simeq\pi_1(X,\bar\eta).
\tag{4.2}
\]

Its kernel is \(\operatorname{Gal}(K^s/M)\). [Stacks, Tag 0BQM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-normal)

*Proof.* Proposition 3.1 makes (3.2) surjective. Lemmas 4.1–4.2 and the morphism calculation identify the essential image of generic restriction with finite disjoint unions of the embedding sets
\(\operatorname{Hom}_K(L,K^s)\) for extensions unramified over \(X\).

These extensions are closed under composita. Given two, take the product of their connected covers. Its generic algebra is \(L_1\otimes_KL_2\); the map to the compositum in \(K^s\) selects one of its field factors. The corresponding connected component of the product has that generic field, and Lemma 4.2 realizes its normalization as a finite étale cover. They are also closed under conjugation by \(\operatorname{Gal}(K^s/K)\), because conjugating the field embedding carries its integral closure to the conjugate integral closure. Thus their union \(M\) is a field stable under all these automorphisms, and is a normal separable, hence Galois, extension of \(K\).

An element of \(\operatorname{Gal}(K^s/K)\) acts trivially on all the displayed embedding sets exactly when it fixes every conjugate of every such \(L\). By their conjugation closure, this is exactly when it fixes \(M\). On the other hand the action on all these sets is the restriction of every finite \(\pi_1(X,\bar\eta)\)-action, and finite regular quotients separate the latter group. Therefore the kernel of (3.2) is \(\operatorname{Gal}(K^s/M)\).

Finally restriction identifies the corresponding quotient with \(\operatorname{Gal}(M/K)\). Surjectivity of restriction can be seen by extending each automorphism on finite Galois subextensions and applying compactness; equivalently it is infinite Galois theory [Stacks, Tag 0BML](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-inifinite-galois-theory). The quotient identification is topological, since these are compact groups with their finite-quotient topologies. \(\square\)

The normality assumption governs the extension of generic-field maps across the whole scheme. The nodal example below shows that even surjectivity of (3.2) can fail without it.


## 5. Curves and arithmetic examples

### 5.1. The projective line in every characteristic

**Proposition 5.1.** For every algebraically closed field \(k\),
\(\pi_1(\mathbf P^1_k)=1\).

*Proof.* Let \(Y\to\mathbf P^1_k\) be a connected finite étale cover of degree \(n\ge1\). It is a smooth proper connected curve. Its connectedness and smoothness make it integral, and its global constant field is \(k\), since \(k\) is algebraically closed. Étaleness identifies

\[
\Omega_{Y/k}\simeq f^*\Omega_{\mathbf P^1/k}.
\]

The canonical degree formula for a smooth proper curve gives

\[
2g(Y)-2=\deg\Omega_{Y/k}=-2n
\tag{5.1}
\]

[Stacks, Tag 0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth). Since \(g(Y)\ge0\), we have \(n\le1\), and thus \(n=1\). A finite locally free map of degree one is an isomorphism, as in Theorem 1.3. Every finite étale cover is consequently a finite disjoint union of copies of \(\mathbf P^1_k\). By (2.2) its fundamental group is trivial. This proof uses no characteristic-zero ramification formula; it is the argument already used in *Descending properties of schemes and morphisms*, Lemma 7.1. \(\square\)

### 5.2. Kummer and Artin–Schreier covers

For \(n\) invertible in \(k\), the map

\[
\mathbf G_{m,k}\longrightarrow\mathbf G_{m,k},
\qquad z\longmapsto z^n
\tag{5.2}
\]

is finite étale of degree \(n\). Its algebra is
\(k[t,t^{-1}][z]/(z^n-t)\); it is free with basis \(1,z,\ldots,z^{n-1}\), and the derivative \(nz^{n-1}\) is a unit. Here \(z\) is automatically invertible. Over algebraically closed \(k\) its source is connected and multiplication by \(n\)th roots of unity gives all \(n\) deck transformations. It is a Galois cover with group \(\mu_n(k)\). If the characteristic divides \(n\), the same derivative vanishes and the map is not étale.

In characteristic \(p>0\), a polynomial \(f(x)\in k[x]\) gives the finite étale algebra

\[
k[x,y]/(y^p-y-f(x)).
\tag{5.3}
\]

It is free of rank \(p\), and the derivative with respect to \(y\) is \(-1\). Translations \(y\mapsto y+c\), \(c\in\mathbf F_p\), act on it. Over any geometric point the roots differ by these translations, so this is a \(\mathbf Z/p\mathbf Z\)-torsor.

For algebraically closed \(k\), (5.3) is connected exactly when \(f\) cannot be written \(h^p-h\) with \(h\in k[x]\). To verify this, over \(k(x)\) the field generated by one root contains every root, since the others are its translates by \(\mathbf F_p\). Its Galois group is a subgroup of the group of order \(p\). Thus the polynomial is either irreducible of degree \(p\), or has a root in \(k(x)\) and splits. A rational function \(h\) with \(h^p-h\) polynomial cannot have a finite pole: at a pole of order \(m>0\) the difference has pole order \(pm\). Hence such an \(h\) is polynomial. In the irreducible case the algebra (5.3) injects into its generic field, since it is free over \(k[x]\), and is a domain. In the split case its linear factors differ by units, so it is a product of \(p\) copies of \(k[x]\). This proves the criterion.

In particular \(f=x\) cannot equal \(h^p-h\): a nonconstant polynomial on the right has degree divisible by \(p\), while a constant has degree zero. More concretely, (5.3) is then just \(k[y]\), with \(x=y^p-y\). Therefore

\[
\pi_1(\mathbf A^1_k)\twoheadrightarrow\mathbf Z/p\mathbf Z,
\qquad\operatorname{char}k=p,
\tag{5.4}
\]

so the affine line is not étale simply connected. This explicit torsor supplies the nontriviality without a cohomology computation; it is the geometric form of the Artin–Schreier sequence [Stacks, Section 0A3J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-artin-schreier).

### 5.3. The affine line and multiplicative group in characteristic zero

We use the smooth projective model of a function field of transcendence degree one, and extension of maps between such models [Stacks, Tags [0BY1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-theorem-curves-rational-maps), [0BY3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-nonsingular-model-smooth)]. Thus a connected finite étale cover of an open subset of \(\mathbf P^1_k\), with \(k\) algebraically closed, extends to a finite map
\(\bar f:C\to\mathbf P^1_k\) from a smooth projective connected curve. Its restriction over the original open is the original cover, by Lemma 4.2 and uniqueness of normalization. All ramification is at the deleted points.

For clarity, we derive the characteristic-zero Riemann–Hurwitz formula used here. For a finite separable map \(f:C\to D\) of smooth projective connected curves over algebraically closed \(k\), the differential map
\(f^*\Omega_{D/k}\to\Omega_{C/k}\) is generically an isomorphism of line bundles. It is injective because its source is torsion-free. Its torsion cokernel has finite length. Taking degrees and using the canonical degree formula yields

\[
2g(C)-2=n(2g(D)-2)+\sum_{P\in C}d_P,
\tag{5.5}
\]

where \(d_P\) is the order of vanishing of the differential map at \(P\). In completed local coordinates, if \(t=u s^{e_P}\), with \(u\) a unit, then

\[
dt=s^{e_P-1}(e_Pu+s u')\,ds.
\]

In characteristic zero the bracket is a unit, so \(d_P=e_P-1\). This proves the formula in the precise case used below; compare Vakil, *The Rising Sea*, §21.4, Theorem 21.4.3. In positive characteristic the order \(d_P\) can exceed \(e_P-1\). The ramification index remains the valuation exponent \(e_P\); one must keep it distinct from the differential order.

For a degree-\(n\) map of these curves, the sum of the indices over each target point is \(n\): the local fibre length is the locally free rank, and all residue fields are \(k\). If there are \(r_q\) points over a target point \(q\), characteristic-zero ramification there contributes \(n-r_q\) to (5.5).

**Proposition 5.2.** Over algebraically closed \(k\) of characteristic zero,

\[
\pi_1(\mathbf A^1_k)=1,
\qquad
\pi_1(\mathbf G_{m,k},1)\simeq\varprojlim_n\mu_n(k)
\simeq\widehat{\mathbf Z}.
\tag{5.6}
\]

Every connected finite étale cover of \(\mathbf G_{m,k}\) is isomorphic over the target to \(z\mapsto z^n\).

*Proof.* For an affine-line cover, the completion can ramify only over \(\infty\). Put \(r=|\bar f^{-1}(\infty)|\ge1\). Formula (5.5) gives

\[
2g(C)-2=-2n+(n-r)=-n-r.
\]

Since the left side is at least \(-2\), we have \(n+r\le2\). Thus \(n=1\), so the finite étale cover is an isomorphism. This proves the first assertion.

For a multiplicative-group cover, put \(r_0,r_\infty\ge1\) for the fibre cardinalities of its completion over \(0,\infty\). Formula (5.5) gives

\[
2g(C)-2=-2n+(n-r_0)+(n-r_\infty)
=-(r_0+r_\infty).
\tag{5.7}
\]

Hence \(r_0+r_\infty\le2\), so both are one and \(g(C)=0\). A smooth proper genus-zero curve with a rational point is \(\mathbf P^1_k\) [Stacks, Tag 0C6U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-proposition-projective-line); over algebraically closed \(k\) it has such points. Choose a coordinate \(z\) whose zero is the sole point over \(0\) and whose pole is the sole point over \(\infty\). The target coordinate has divisor \(n(0)-n(\infty)\) in this source coordinate, so is \(c z^n\) for some \(c\in k^\times\). Taking an \(n\)th root of \(c\) and changing \(z\) puts it in the form \(z^n\). Removing these two points gives the asserted cover of \(\mathbf G_m\).

All these covers are Galois, with deck group \(\mu_n(k)\), and they dominate every connected finite étale cover. Point them by \(z=1\) over the target point \(1\); for \(n\mid m\), the pointed domination map is \(z\mapsto z^{m/n}\). Its group transition is \(\zeta\mapsto\zeta^{m/n}\). The inverse-limit reconstruction from *Galois categories*, Lemma 3.1, therefore identifies the fundamental group with the displayed inverse limit of roots of unity. The groups are abelian, so the opposite convention makes no difference here.

Choose compatible primitive roots \(\zeta_n\). Such a choice exists: the finite sets of primitive roots have surjective transition maps, as follows by lifting a unit modulo \(n\) to a unit modulo \(m\) when \(n\mid m\), using the Chinese remainder theorem. Compactness gives a compatible family. Sending \(1\bmod n\) to \(\zeta_n\) gives the last isomorphism in (5.6). That last isomorphism depends on this choice; the root-of-unity inverse limit is the natural form of the answer. \(\square\)

### 5.4. The nodal cubic

Let \(k\) be algebraically closed of any characteristic, and let

\[
C:\quad y^2z+xyz=x^3\ \subset\mathbf P^2_k.
\tag{5.8}
\]

The normalization and its reduced double and triple relations were computed in *Descending properties of schemes and morphisms*, Section 7. They give the equivalence

\[
\operatorname{F\acute Et}(C)
\simeq\{\text{finite sets equipped with one permutation}\}.
\tag{5.9}
\]

To recall its mechanism, pullback of a cover to the normalization \(\mathbf P^1_k\) is trivial by Proposition 5.1, with a finite label set \(E\). The two points over the node are glued by one permutation \(\sigma\) of \(E\). The reverse ordered pair uses \(\sigma^{-1}\), and the triple-relation cocycle supplies the consistency. Integral descent proves effectivity and the complete morphism correspondence. Thus a morphism in (5.9) is exactly a function commuting with the permutations. The calculation includes characteristic two.

Take the geometric base point at a smooth \(k\)-point of \(C\). Under (5.9) its fibre is the underlying finite set, so *Galois categories*, Lemma 1.1, gives

\[
\pi_1(C)\simeq\widehat{\mathbf Z}.
\tag{5.10}
\]

A connected cover corresponds to one cycle of length \(n\). Its normalization consists of \(n\) copies of \(\mathbf P^1_k\), with one branch of the node on each copy glued to the other branch on the next. These form a cycle, and every such cover is Galois with cyclic deck group of order \(n\).

Yet the map from the absolute Galois group of \(K=k(C)\) is trivial. The normalization is an isomorphism at the generic point, and every pulled-back cover is already trivial on the normalization. Thus the generic algebra of a degree-\(n\) cover is \(K^n\). The group \(\operatorname{Gal}(K^s/K)\) acts trivially on every one of these generic fibres. Formula (3.2) therefore acts trivially on every finite \(\pi_1(C)\)-set; finite regular quotients separate points, so the homomorphism itself is trivial. It is not surjective onto (5.10). The connected covers here are reducible, and the nodal curve is not geometrically unibranch.

### 5.5. The spectrum of the integers

We use the following named arithmetic input: every number field strictly larger than \(\mathbf Q\) has a ramified finite prime. This consequence of Minkowski's bound is stated as Theorem 4.9 in Milne, *Algebraic Number Theory*, version 3.08, p. 72 ([author's notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf)). It is an input from number theory.

A connected finite étale cover of \(\operatorname{Spec}\mathbf Z\) is, by Lemma 4.2, the normalization in a number field \(L\). Its ring is the integral closure \(\mathcal O_L\). Finite étaleness says its local extensions at every finite prime are unramified; equivalently their fibres are reduced with separable residue fields and no ramification multiplicity. Thus no finite prime ramifies in \(L/\mathbf Q\). Minkowski's consequence forces \(L=\mathbf Q\), whose integral closure is \(\mathbf Z\). Every connected cover is the identity, and hence

\[
\pi_1(\operatorname{Spec}\mathbf Z)=1.
\tag{5.11}
\]

Removing primes changes the allowed ramification and can change this answer; the calculation is for the full spectrum.

## 6. Geometric and arithmetic fundamental groups

### 6.1. Finite presentation and purely inseparable change of field

We first state the approximation input already used in *Descending properties of schemes and morphisms*: for a filtered inverse system of quasi-compact quasi-separated schemes with affine transition maps, finite-presentation objects, maps and equalities descend to a finite stage; if a descended object is finite étale at the limit, it is finite étale after increasing the stage [Stacks, Tags [01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation), [01ZO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-finite-presentation), [07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale)]. It implies

\[
\operatorname{F\acute Et}(\varprojlim_i X_i)
\simeq\varinjlim_i\operatorname{F\acute Et}(X_i).
\tag{6.1}
\]

Indeed objects descend by the finite and étale parts of that input, maps descend by its morphism part, and equality of maps is eventually true by its equality part. Inverses and their two identities descend in the same way. This proves the category equivalence, including isomorphisms and diagrams [Stacks, Tag 0BTV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-limit). When the stages are eventually connected, a natural automorphism of the limit fibre functor is precisely a compatible family of natural automorphisms at all stages. The finite-coordinate topologies give the corresponding inverse-limit formula for fundamental groups. We will use (6.1) with \(X_i=X_{k_i}\), for a fixed quasi-compact quasi-separated \(X\) and a filtered union of fields.

**Lemma 6.1.** For an arbitrary connected \(k\)-scheme \(X\), passage to the perfection \(k^{\mathrm{perf}}\) preserves connectedness and gives an equivalence of finite étale categories, hence an isomorphism
\(\pi_1(X_{k^{\mathrm{perf}}})\simeq\pi_1(X)\). [Stacks, Tag 0BTW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-perfection)

*Proof.* In characteristic zero the assertion is the identity. Suppose \(\operatorname{char}k=p\). First, absolute Frobenius pullback acts as the identity on finite étale objects, by the relative Frobenius isomorphism

\[
F_{Y/X}:Y\longrightarrow Y\times_{X,F_X}X.
\tag{6.2}
\]

Here is a proof in the finite case. The two schemes in (6.2) are finite étale over \(X\), so (6.2) is finite étale by the observation preceding Proposition 1.1. Over a geometric point \(\operatorname{Spec}\Omega\to X\), its fibre points correspond on one side to algebra maps with the given scalar embedding into \(\Omega\), and on the other to maps with its Frobenius-twisted embedding. Frobenius on algebraically closed \(\Omega\) is an automorphism. Composing with it bijects these two sets of embeddings, exactly as the formula \(b\otimes a\mapsto b^pa\) for relative Frobenius requires. Thus (6.2) is bijective on every geometric fibre. Its locally free degree over the target is one everywhere, so it is an isomorphism by the rank-one argument in Theorem 1.3. This isomorphism is natural in \(Y\) [Stacks, Tag 0EBS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-relative-frobenius-etale). The same holds for every iterate of Frobenius.

Let \(k'/k\) be finite purely inseparable, with \((k')^{p^r}\subset k\). For \(f:X_{k'}\to X\), define a morphism \(g:X\to X_{k'}\) on each affine by

\[
\mathcal O_X(U)\otimes_k k'\longrightarrow\mathcal O_X(U),
\qquad a\otimes c\longmapsto a^{p^r}c^{p^r}.
\tag{6.3}
\]

The scalar \(c^{p^r}\) lies in \(k\), and the formula respects tensor relations, sums, products and localizations, so glues. These are morphisms of schemes; \(g\) need not be a \(k\)-morphism. The composites \(fg\) and \(gf\) are the respective \(r\)th absolute Frobenius iterates. By (6.2), their pullback functors on finite étale categories are naturally the identity. Thus \(f^*\) and \(g^*\) are inverse equivalences.

The perfection is the filtered union of finite purely inseparable subextensions. For affine \(X\), apply (6.1) to their affine base changes. Every transition equivalence just proved identifies this colimit category with \(\operatorname{F\acute Et}(X)\). For arbitrary \(X\), apply that affine result on an affine open cover and on affine covers of its intersections. Full faithfulness gives unique lifted transition maps and their cocycle; Zariski gluing produces the finite étale object on \(X\). The local result also glues all maps. Hence the equivalence needs no global quasi-compactness assumption.

Finally \(X_{k^{\mathrm{perf}}}\to X\) is a universal homeomorphism. For a finite purely inseparable extension its scalar generators satisfy purely inseparable monic equations, and after any field base change its spectrum has one point over each base point, with purely inseparable residue extension. It is integral and universally bijective, hence a universal homeomorphism. The same is true for the union, by integrality and the unique extensions of primes. Thus it preserves connectedness. Applying the equivalence and fibre identification proves the group assertion. \(\square\)

### 6.2. The exact sequence

**Theorem 6.2.** Let \(X\) be quasi-compact and quasi-separated over a field \(k\), and suppose \(X_{\bar k}\) is connected, for an algebraic closure \(\bar k\). Choose a geometric point of \(X_{\bar k}\) and its image in \(X\). There is a short exact sequence of profinite groups

\[
1\longrightarrow\pi_1(X_{\bar k})
\xrightarrow{b}\pi_1(X)
\xrightarrow{a}\operatorname{Gal}(k^s/k)
\longrightarrow1.
\tag{6.4}
\]

[Stacks, Tag 0BTX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-ses-field)

*Proof.* The projection \(X_{\bar k}\to X\) is surjective, so \(X\) is connected. By Lemma 6.1, replacing \(k\) with its perfection changes neither \(\pi_1(X)\) nor the arithmetic group; \(\bar k\) is unchanged. Indeed every automorphism of \(\bar k/k\) fixes the uniquely specified purely inseparable roots, so the groups over \(k\) and its perfection agree with the same finite-quotient topology. We may therefore assume \(k\) perfect, so \(\bar k\) is the union of its finite separable extensions.

The exact functors producing the arrows are

\[
\operatorname{F\acute Et}(k)
\xrightarrow{T}\operatorname{F\acute Et}(X)
\xrightarrow{U}\operatorname{F\acute Et}(X_{\bar k}).
\tag{6.5}
\]

We verify the complete categorical tests from *Galois categories*, Section 4.

**Surjectivity on the right.** A connected finite étale \(k\)-scheme is \(\operatorname{Spec}k'\) for a finite separable extension. Its pullback \(X_{k'}\) is connected: it is a surjective image of connected \(X_{\bar k}\), using any embedding \(k'\to\bar k\). Thus \(T\) preserves connected objects, and the surjectivity criterion proves \(a\) is surjective. It also proves \(T\) fully faithful. Clearly \(U\circ T\) sends every object to a disjoint union of copies of \(X_{\bar k}\), so \(ab\) is trivial.

**Injectivity on the left.** Let \(V\to X_{\bar k}\) be any connected finite étale cover. By (6.1), it descends to a finite étale \(V'\to X_{k'}\) for some finite separable \(k'/k\). The composite \(V'\to X\) is finite étale. After base change to \(\bar k\), its decomposition according to the embeddings of \(k'\) into \(\bar k\) contains \(V\) as an open-and-closed summand. Thus \(V\) is a subobject of the pullback of an object of \(\operatorname{F\acute Et}(X)\). With the identity epimorphism from \(V\) to itself, this is the diagram in the injectivity criterion, which proves \(b\) injective.

**Normality of its image.** Suppose \(Y\to X\) is connected finite étale and \(Y_{\bar k}\to X_{\bar k}\) has a section. Descend the section to some finite Galois \(L/k\), using (6.1) for its map and identities. The scheme \(X_L\) is connected, again as a surjective image of \(X_{\bar k}\). Its section image is therefore one connected open-and-closed summand of \(Y_L\), isomorphic to \(X_L\). Take the union of all its conjugate section images under \(\operatorname{Gal}(L/k)\). Each is a connected summand, so any two are equal or disjoint. Their union \(W_L\) is open and closed and stable under the Galois descent datum.

This union descends to an open-and-closed \(W\subset Y\). One can see the descent directly on its algebra: the idempotent selecting \(W_L\) is invariant under the datum and hence descends by faithfully flat algebra descent. It is nonempty, so connectedness of \(Y\) forces \(W=Y\). Consequently \(Y_L\), and then \(Y_{\bar k}\), is a disjoint union of copies of the base. The normality criterion therefore proves \(b(\pi_1(X_{\bar k}))\) normal in \(\pi_1(X)\).

**The entire kernel.** Suppose a finite étale \(Y\to X\) becomes trivial over \(\bar k\). Descend an isomorphism with a finite disjoint union of the base, including its inverse, to a finite separable \(k'/k\), using (6.1). If the degree is \(n\), it gives

\[
Y_{k'}\simeq\coprod_{i=1}^n X_{k'}.
\]

Put \(V=\coprod_{i=1}^n\operatorname{Spec}k'\). The displayed isomorphism followed by \(Y_{k'}\to Y\) gives a surjection \(T(V)\to Y\). It is an epimorphism in the finite étale category, since it is surjective on geometric fibres. Thus \(T\) is fully faithful, \(U\circ T\) is trivial on objects, and every object trivialized by \(U\) has an epic image from \(T\). The closed-normal-kernel test identifies \(\ker a\) with the smallest closed normal subgroup containing the image of \(b\). That image is already normal and closed, by the preceding step and compactness. Hence \(\ker a=\operatorname{im}b\). Together with both end conditions this proves (6.4). \(\square\)

The proof identifies exactly where quasi-compactness and quasi-separatedness are used: descending covers, sections and trivializing isomorphisms from the algebraic closure to a finite extension. Geometric connectedness proves surjectivity on the right and is essential to the normality argument. A rational point \(x\in X(k)\), with compatible geometric base point, supplies a section of \(a\), since the composite \(\operatorname{Spec}k\xrightarrow{x}X\to\operatorname{Spec}k\) is the identity. Different geometric base-point identifications change this splitting by conjugation.


## 7. Exercises and complete solutions

**Exercise 7.1 (easy).** Compute \(\pi_1(\operatorname{Spec}\mathbf F_q)\) and \(\pi_1(\operatorname{Spec}k)\) for separably closed \(k\).

*Solution.* Equation (3.1) identifies these groups with their absolute Galois groups in the Krull topology. For \(\mathbf F_q\), the unique extension of degree \(n\) is the root field of \(T^{q^n}-T\), and its automorphism group is cyclic of order \(n\), generated by \(u\mapsto u^q\). This calculation, including uniqueness and the exact order of Frobenius, was proved in *Galois categories*, Example 5.2. The restriction maps preserve Frobenius, so the inverse limit is \(\widehat{\mathbf Z}\). For separably closed \(k\), there are no nontrivial finite separable extensions, so every finite étale scheme is a finite disjoint union of copies of \(\operatorname{Spec}k\). Its fibre functor is the forgetful functor on finite sets and has trivial natural automorphism group. An algebraic closure used as a geometric point adds only purely inseparable elements and does not add finite étale covers.

**Exercise 7.2 (medium).** Prove \(\pi_1(\mathbf P^1_k)=1\) over any algebraically closed field, using degrees of differentials.

*Solution.* Let \(f:Y\to\mathbf P^1_k\) be a connected finite étale cover. Smoothness and properness of the base ascend through this map, so \(Y\) is a smooth proper connected curve; it is integral and its constant field is \(k\). Let \(n\ge1\) be its degree. The étale differential sequence identifies \(\Omega_{Y/k}\) with \(f^*\Omega_{\mathbf P^1/k}\). The latter has degree \(-2n\), since \(\Omega_{\mathbf P^1/k}\) has degree \(-2\) and pullback multiplies line-bundle degree by \(n\). The canonical degree formula therefore gives \(2g(Y)-2=-2n\). Nonnegative genus forces \(n=1\). The cover is an isomorphism by the finite rank-one algebra argument. Every cover decomposes into connected covers by Theorem 1.3, so all finite covers are trivial. Equation (2.2), tested on finite regular quotients, makes the group trivial. No step uses a characteristic-zero assumption.

**Exercise 7.3 (medium).** Over \(k=\overline{\mathbf F}_p\), show that \(y^p-y=x\) defines a connected Galois cover of \(\mathbf A^1_k\) with group \(\mathbf Z/p\mathbf Z\). Deduce that the affine line has nontrivial étale fundamental group.

*Solution.* Eliminating \(x\) identifies the source algebra with \(k[y]\), so the source is \(\mathbf A^1_k\) and is integral, hence connected. As an algebra over \(k[x]\) it is free of rank \(p\), by reduction modulo the monic polynomial \(y^p-y-x\). Its derivative is \(-1\), a unit, so the map is étale. Thus it is finite étale of degree \(p\).

For each \(c\in\mathbf F_p\), translation \(y\mapsto y+c\) preserves \(y^p-y\). These \(p\) automorphisms are distinct. In every geometric fibre any two roots differ by a root of \(T^p-T\), exactly an element of \(\mathbf F_p\), so the translations act simply transitively. It is a Galois cover with the asserted group. Under (2.2) it gives a continuous surjection of \(\pi_1(\mathbf A^1_k)\) onto that group. Hence the fundamental group is nontrivial.

**Exercise 7.4 (medium).** Compute the fundamental group of the nodal cubic (5.8), and show that its function-field Galois map is trivial.

*Solution.* The normalization is \(\nu:\mathbf P^1_k\to C\); in the parameter \(t\) used in *Descending properties of schemes and morphisms*, Section 7, the node has preimages \(a=0\) and \(b=-1\). A finite étale cover pulled back along \(\nu\) is \(E\) copies of \(\mathbf P^1_k\), by Exercise 7.2. The reduced double relation is the diagonal together with the two ordered off-diagonal pairs \((a,b),(b,a)\). A descent isomorphism is the identity on the diagonal and gives a permutation \(\sigma\) on one pair. The triple relation forces the permutation on the reverse pair to be \(\sigma^{-1}\); there is no other independent permutation. The integral effectivity theorem from that lesson makes every such datum an actual finite étale cover.

All maps descend as well, so the finite-cover category is equivalent to finite sets with a permutation and equivariant functions. Its fibre at a smooth point is the underlying set. *Galois categories*, Lemma 1.1, computes the automorphism group of this functor as \(\widehat{\mathbf Z}\).

For a cycle of length \(n\), the normalized cover has \(n\) copies, with the point over \(a\) on one copy identified with the point over \(b\) on the next, according to the chosen orientation of \(\sigma\). It is connected exactly when the permutation has one orbit: an open-and-closed piece pulls back to a union of these connected copies, and descends exactly when that label subset is \(\sigma\)-stable. Thus the connected covers are cycles of rational components.

At the generic point \(\nu\) is an isomorphism. The generic algebra of every degree-\(n\) cover is therefore \(K^n\), where \(K=k(C)\). Its embedding set has trivial absolute Galois action. Consequently the map \(\operatorname{Gal}(K^s/K)\to\pi_1(C)\) acts trivially on all finite actions; since finite regular quotients separate points, it is the trivial homomorphism. This proves both assertions and displays why normality matters in Theorem 4.3.

**Exercise 7.5 (hard).** Over algebraically closed \(k\) of characteristic zero, classify connected finite étale covers of \(\mathbf G_m\) and compute its fundamental group using Riemann–Hurwitz.

*Solution.* Let \(Y\to\mathbf G_m\) have degree \(n\). It is integral by Lemma 4.2. Its smooth projective model \(C\) gives a finite map to \(\mathbf P^1_k\) extending the cover, ramified only over \(0,\infty\). Let \(r_0,r_\infty\) be the numbers of points in these fibres. All residue fields are \(k\), and the sums of their ramification indices are \(n\). In characteristic zero the ramification divisor consequently has degree
\((n-r_0)+(n-r_\infty)\). Formula (5.5) gives

\[
2g(C)-2=-(r_0+r_\infty).
\]

Both cardinalities are positive, so their sum is at least two; nonnegative genus makes it at most two. Therefore \(g(C)=0\) and \(r_0=r_\infty=1\). The curve is \(\mathbf P^1_k\). Choose a coordinate \(z\) vanishing at the unique point over zero and having a pole at the unique point over infinity. The target coordinate has divisor \(n\) times their difference, so it is \(c z^n\). Absorb \(c\) by an \(n\)th root in \(k\). Restriction to the complement of these points identifies the original cover over its target with \(z\mapsto z^n\).

These covers are all Galois with group \(\mu_n(k)\). Pointed domination for \(n\mid m\) has transition \(\mu_m(k)\to\mu_n(k)\), \(\zeta\mapsto\zeta^{m/n}\). Since these covers include every connected finite cover, the reconstruction theorem gives \(\pi_1(\mathbf G_m,1)=\varprojlim_n\mu_n(k)\). Compatible primitive roots identify this limit with \(\widehat{\mathbf Z}\), as proved in Proposition 5.2. The choice is needed for that final identification; the cover classification itself uses no such choice.

## 8. What this lesson does not prove

The geometric Galois-category axioms, internal Hom, normal-scheme description, unibranch surjectivity, all listed computations and the complete arithmetic exact sequence are proved here, using the preceding course proofs as indicated. We use the following precise prerequisite results.

- Finite étale local splitting, and the local decomposition of finite unramified maps into closed immersions [Stacks, Tags [04HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-etale-etale-local), [04HJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-unramified-etale-local)]; faithfully flat strict henselization and splitting of finite étale algebras over a strictly henselian local ring belong to the étale-neighbourhood prerequisite.
- Étale cancellation [Stacks, Tag 02GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-permanence), flat going down [Stacks, Tag 03HV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-generalizations-lift-flat), and normality of a strict henselization of a local normal domain [Stacks, Tag 06DI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-normal). The equivalence of the strict-henselization and usual definitions of geometric unibranchness is [Stacks, Tag 06DM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-geometrically-unibranch). Normality ascent along étale maps was stated precisely in the preceding descent lesson.
- Finite-presentation descent of objects, maps and equality along affine inverse systems of quasi-compact quasi-separated schemes, and eventual finiteness and étaleness [Stacks, Tags [01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation), [01ZO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-finite-presentation), [07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale)]. Equation (6.1) spells out the consequence used here.
- The canonical degree formula for a smooth proper curve with constant field \(k\) [Stacks, Tag 0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth), multiplicativity of line-bundle degree under nonconstant finite pullback [Stacks, Tag 0AYZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-pullback-map-proper-curves), smooth projective models and extension of function-field maps [Stacks, Tags [0BY1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-theorem-curves-rational-maps), [0BY3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-nonsingular-model-smooth)], and the genus-zero characterization with a rational point [Stacks, Tag 0C6U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-proposition-projective-line). A nonconstant map between these proper curves is finite: its fibres are zero-dimensional, so proper quasi-finite finiteness applies, a consequence of Zariski Main in the quasi-finite-morphism prerequisite. These are the curve-theory inputs behind Proposition 5.2. The characteristic-zero form of Riemann–Hurwitz needed there was derived in (5.5); Vakil, *The Rising Sea*, §21.4, is a reference for the general formula.
- Minkowski's consequence that every nontrivial number field has a ramified finite prime [Milne, *Algebraic Number Theory*, version 3.08, Theorem 4.9, p. 72](https://www.jmilne.org/math/CourseNotes/ANT.pdf). The standard interpretation of finite étaleness of rings of integers as absence of finite-prime ramification is the accompanying number-theory prerequisite.
- The elementary finite Galois theory used in the preceding lesson, and its infinite fixed-field/closed-subgroup consequence [Stacks, Tag 0BML](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-inifinite-galois-theory). The latter also follows by applying finite Galois theory on finite normal subextensions and intersecting closed subgroups.

The next lesson studies proper families, including invariance under universal homeomorphisms, covers over henselian bases, and the homotopy exact sequence. Its hypotheses will control which geometric covers persist through a family; the group tests proved in *Galois categories* will again turn those geometric statements into exactness.
