# Algebraic spaces

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

## Introduction

A quotient can have good local coordinates even when no affine neighbourhood exists at one of its points. Algebraic spaces let us retain those coordinates. The coordinates are allowed to be étale rather than Zariski local, and the object they describe is a sheaf of sets. Automorphisms of an object are not retained in this construction; retaining them will lead to stacks.

We will construct quotients before studying their geometry. The decisive question is whether the relation between two coordinate systems is itself represented by a scheme. After answering it, we will compare finite symmetry, an infinite translation action, and an identification that changes at one point.

We assume the functor of points, fibre products of schemes, the fppf topology, and descent of morphisms. The scheme descent theorem used below is proved at full locally quasi-finite scope in §2.0. We impose no quasi-separatedness condition in the definition of an algebraic space. All groups used in this lesson are abstract groups, acting through their constant group schemes; a profinite group is treated here as an abstract group unless expressly stated otherwise.

Basic references are [Stacks] and [Behrend]. The term algebraic space used here concerns étale presentations. Serre's earlier use of the same words, discussed in [EGA IV, §10.10], concerns a different construction with closed points of Jacobson schemes.

## 1. Local coordinates without an underlying scheme

Fix a scheme \(S\). Work on the big fppf site of \(S\)-schemes, within a fixed universe. A scheme \(V\) is identified with the sheaf

\[
h_V(T)=\operatorname{Hom}_S(T,V).
\]

A transformation \(a:F\to G\) of sheaves is **representable by schemes** if \(T\times_G F\) is represented by a scheme for every scheme \(T\) and every map \(T\to G\). This condition lets us ask geometric questions about \(a\): it is étale, an open immersion, or surjective if every such base change has that property. Here surjectivity is surjectivity of the resulting maps of schemes, not surjectivity of \(F(T)\to G(T)\) for every \(T\).

**Lemma 1.1.** Base change and composition preserve representability by schemes. If a property of scheme morphisms is stable under base change and local on the target for the fppf topology, then its definition for representable transformations can be checked after an fppf cover of any test scheme. If the property is also stable under composition, compositions of representable transformations with that property have the property.

**Proof.** For base change, the test fibre product is still a test fibre product of the original transformation. For \(F\to G\to H\) and \(T\to H\), first form the scheme \(V=T\times_H G\). Then

\[
T\times_H F=V\times_G F
\]

is a scheme. The map to \(T\) is the composition of the two tested morphisms. For the local assertion, pull \(T\times_G F\to T\) back to an fppf covering \(\{T_i\to T\}\) and use the stated locality of the property. These observations prove all the assertions. \(\square\)

The diagonal packages all tests involving a pair of objects. A sheaf \(X\) has representable diagonal if, for every scheme \(T\) and \(a,b\in X(T)\), the equality functor

\[
E_{a,b}(T')=\{f:T'\to T:a|_{T'}=b|_{T'}\}
\]

is represented by a scheme over \(T\). This is exactly the base change of \(X\to X\times_S X\) by \((a,b):T\to X\times_S X\).

**Definition 1.2.** An **algebraic space over \(S\)** is an fppf sheaf \(X\) whose diagonal is representable by schemes and which admits a representable, surjective étale morphism \(q:U\to X\) from a scheme. Such a morphism is an **étale presentation**.

If the diagonal is representable, every map from a scheme \(V\) to \(X\) is representable: \(T\times_X V\) is the base change of the diagonal by \(T\times_S V\to X\times_S X\). Thus the word representable in the last condition is redundant once the diagonal condition has been imposed.

Every scheme is an algebraic space. Its functor of points is an fppf sheaf; its diagonal is a scheme morphism; and its identity is an étale presentation.

For a presentation, the scheme

\[
R=U\times_X U
\]

records equal coordinates. Write \(s,t:R\to U\) for the projections. Both are étale. The map \(j=(s,t):R\to U\times_S U\) is a monomorphism, and for every test scheme its image is an equivalence relation. The relation includes an identity arrow, reversal of arrows, and composition. Because \(j\) is a monomorphism, these arrows, when they exist, are unique.

Conversely, an **étale equivalence relation** consists of schemes \(U,R\) and a monomorphism \(j=(s,t):R\to U\times_S U\) which gives an equivalence relation on every test scheme, with \(s,t\) étale. Its quotient \(U/R\) will always mean the fppf sheafification of the presheaf \(T\mapsto U(T)/R(T)\).

Sheafification matters. A point of \((U/R)(T)\) need not have one coordinate on \(T\). It has coordinates on an fppf cover of \(T\), related on overlaps.

## 2. Constructing the quotient

We prove the scheme descent theorem first. Its construction uses affine algebras and quasi-affine invariant neighbourhoods, then glues an arbitrary family of those neighbourhoods. This supplies the input to the quotient construction which follows.

### 2.0. Scheme descent before taking the quotient

**Theorem 2.0 (effective separated locally quasi-finite descent).** Let \(S\) be any scheme and \(\{S_i\to S\}_{i\in I}\) an fppf covering. Suppose that \(X_i\to S_i\) are separated locally quasi-finite morphisms of schemes, with isomorphisms
\[
\phi_{ij}:X_i\times_S S_j\xrightarrow{\sim}S_i\times_S X_j
\]
over \(S_i\times_S S_j\), satisfying the cocycle identity on every triple overlap. There exist a separated locally quasi-finite scheme \(X\to S\) and compatible isomorphisms \(X\times_S S_i\cong X_i\) recovering this datum. They are unique up to a unique compatible isomorphism. Every compatible family of morphisms between two such data descends uniquely.

There is no quasi-compactness hypothesis on \(X_i\), no Noetherian hypothesis on \(S\), and no local finite-presentation hypothesis on \(X_i\to S_i\). “Locally quasi-finite” includes local finite type and zero-dimensional fibres. The **covering maps** are locally finitely presented, as required in the definition of fppf; this will be essential for the invariant-open construction.

We first establish the scheme-theoretic descent tools used in the proof. The two other scheme inputs are stated exactly: flat locally finitely presented morphisms are universally open, and separated quasi-finite morphisms are quasi-affine. Their genuine programme homes and current transitive states are recorded at the end.

#### 2.0.1. Affine algebras, invariant opens and morphisms

**Affine algebra lemma.** Let \(R\to B\) be faithfully flat. A \(B\)-algebra \(C\) with an algebra descent datum is the base change of an \(R\)-algebra \(C_0\), uniquely with the prescribed comparison. Compatible algebra maps descend.

*Proof.* Choose the direction of the algebra datum as
\[
\theta:C\otimes_R B\xrightarrow{\sim}B\otimes_R C,
\]
an isomorphism of \(B\otimes_R B\)-algebras. For the scheme datum directed from \(X'\times_S S'\) to \(S'\times_S X'\), this is the inverse of its pullback on coordinate rings. Define
\[
\rho:C\longrightarrow B\otimes_R C,\qquad
\rho(c)=\theta(c\otimes1).
\]
This is an \(R\)-algebra homomorphism, and is \(B\)-linear when \(B\) acts on the first factor of its target:
\(\rho(bc)=(b\otimes1)\rho(c)\).
The diagonal and cocycle identities for \(\theta\) give
\[
\mu\rho=\operatorname{id}_C,\qquad
(\operatorname{id}_B\otimes\rho)\rho(c)
 =\sum_\nu b_\nu\otimes1\otimes c_\nu
 \quad\text{if }\rho(c)=\sum_\nu b_\nu\otimes c_\nu,              \tag{D.1}
\]
where \(\mu:B\otimes_R C\to C\) is multiplication by the structural \(B\)-action. The first identity follows by pulling \(\theta\) to the diagonal; the cocycle makes that invertible diagonal map idempotent, hence the identity. The second identity is the cocycle applied to \(c\otimes1\otimes1\): passage successively from the first to the second and third coordinates equals direct passage from the first to the third.

Put
\[
C_0=\{c\in C:\rho(c)=1\otimes c\}.
\]
It is an \(R\)-subalgebra because both maps in this equalizer are algebra homomorphisms. Flatness of \(B/R\), applied to the equalizer of the two \(R\)-linear maps \(\rho\) and \(c\mapsto1\otimes c\), identifies
\[
B\otimes_R C_0
=\ker\bigl(\operatorname{id}_B\otimes\rho
              -\operatorname{id}_B\otimes(c\mapsto1\otimes c)\bigr)
\subset B\otimes_R C .
\]
By (D.1), \(\rho(C)\) is contained in this kernel. Thus \(\rho\) gives an inverse to
\[
\lambda:B\otimes_R C_0\longrightarrow C,\qquad b\otimes c\longmapsto bc.
\]
Indeed \(\mu\rho=\operatorname{id}\), and, for \(c\in C_0\),
\(\rho(bc)=b\otimes c\). Hence \(\lambda\) is an isomorphism of \(B\)-algebras. It respects the full datum: the identity
\(\theta(c\otimes b)=(1\otimes b)\rho(c)\) shows that \(\rho\) determines \(\theta\), and on \(B\otimes_R C_0\) the resulting datum is the canonical one.

For completeness, the equalizer for a canonical object is its original algebra. For any \(R\)-module \(L\), the sequence
\[
0\longrightarrow L\longrightarrow B\otimes_R L
\rightrightarrows B\otimes_R B\otimes_R L                       \tag{D.2}
\]
is exact. After tensoring with \(B\), the injection has the retraction multiplying the first two \(B\)-factors. If
\(z=\sum a_\nu\otimes b_\nu\otimes l_\nu\) is in the equalizer in that tensored sequence, its equality is
\[
\sum a_\nu\otimes1\otimes b_\nu\otimes l_\nu
 =\sum a_\nu\otimes b_\nu\otimes1\otimes l_\nu.
\]
Multiplying the first two factors gives
\(z=\sum a_\nu b_\nu\otimes1\otimes l_\nu\), precisely the image of the previous term. Faithful flatness reflects exactness and proves (D.2).

A compatible map between two data commutes with their \(\rho\)'s and therefore restricts to a map between their equalizers. The base-change isomorphisms recover the original map. Conversely the pullback of an \(R\)-algebra map respects the canonical datum, and (D.2) proves uniqueness. Taking spectra proves affine scheme effectivity and full faithfulness. \(\square\)

**Invariant opens lemma.** Let \(q:T'\to T\) be a faithfully flat affine morphism. An open \(U'\subset T'\) whose two inverse images in \(T'\times_T T'\) agree is the pullback of a unique open \(U\subset T\).

*Proof.* It is saturated on underlying points. If two points \(t'_1,t'_2\) lie above the same \(t\), their residue fields have a nonzero tensor product over \(\kappa(t)\). A prime of that tensor product gives a point of the fibre product mapping to both. Invariance therefore says \(t'_1\in U'\) if and only if \(t'_2\in U'\). Thus \(U'=q^{-1}(q(U'))\).

A faithfully flat affine morphism is universally a quotient map on topological spaces. The actual proof is AG-FSE, *Flat morphisms*, Theorem 3.3, which applies after every base change: flatness lifts generizations, and the images of finitely many affine pieces of a closed inverse image are constructibly compact and specialization stable, hence closed. Consequently \(q(U')\) is open. Give it the open subscheme structure. Its pullback equals \(U'\) as an open subscheme, and surjectivity proves uniqueness. When \(q\) is fppf, one may instead use its openness directly. \(\square\)

The same statement holds for arbitrary fppf covering families. Each covering map is open; the union of the images of the invariant opens is open, and the residue-field argument gives equality of all its inverse images. No quasi-compactness is used here.

**Morphism descent lemma.** Morphisms between existing schemes descend uniquely along fppf coverings, without separation or quasi-compactness restrictions on those schemes.

*Proof.* Begin with \(S=\operatorname{Spec}R\), \(S'=\operatorname{Spec}B\), and \(R\to B\) faithfully flat. Let \(Y,Z\) be \(S\)-schemes, and let \(g':Y_{S'}\to Z_{S'}\) be compatible with their canonical data. Compose \(g'\) with \(Z_{S'}\to Z\).

For an affine open \(V\subset Z\), its inverse image \(U'\subset Y_{S'}\) is invariant and descends to an open \(U\subset Y\) by the preceding lemma, applied to \(Y_{S'}\to Y\). Cover \(U\) by affine opens \(U_\alpha=\operatorname{Spec}D_\alpha\). The map upstairs to \(V\) corresponds to a homomorphism
\[
\Gamma(V,\mathcal O_V)\longrightarrow D_\alpha\otimes_R B.
\]
Compatibility puts its values in the equalizer (D.2), which is \(D_\alpha\). It therefore determines a unique map \(U_\alpha\to V\). The maps agree on intersections: cover each intersection by affine opens and use the same faithful equalizer. They glue to \(U\to V\). The opens obtained from an affine cover of \(Z\) cover \(Y\), since their pullbacks cover \(Y_{S'}\) and the covering is surjective. Their maps glue, again by the equalizer and faithful checking, to the required \(Y\to Z\). The two structural maps \(Y\to S\) agree after the cover, hence agree by the same equalizer argument; thus the descended morphism is over \(S\). This proves both existence and uniqueness.

For an arbitrary fppf covering family over an affine base, take a finite affine refinement, combine its members into one faithfully flat affine covering, and apply this argument. Equality with the original maps on every unchosen member is checked after its base change by that refinement, and follows by the uniqueness just proved. For a general base, repeat on affine opens and glue. This is gluing morphisms between **existing schemes**, so it uses no object-effectivity theorem. \(\square\)

One consequence we will use is descent of closed immersions for an existing morphism. On an affine target, its pullback along an affine faithfully flat cover is an affine scheme with affine descent data. The affine algebra lemma produces an affine scheme over that target. The morphism descent lemma identifies it with the given source, by descending the comparison isomorphism and its inverse. Write the given morphism as \(R\to D\). Surjectivity after tensoring with the faithfully flat covering algebra forces \(\operatorname{coker}(R\to D)=0\), so it is a closed immersion. This is target-local and therefore proves the assertion for arbitrary schemes.

#### 2.0.2. Finite-presentation localization and covering refinements

We spell out the finite-presentation point needed in the preceding reduction and in the main proof. It concerns covering algebras, not the potentially non-finitely-presented schemes being descended.

**Localization lemma.** If \(\operatorname{Spec}D\) has a finite principal-open cover \(D(d_1),\ldots,D(d_m)\), with every \(D_{d_i}\) finitely presented over \(R\), then \(D\) is finitely presented over \(R\).

*Proof.* Choose \(e_i\in D\) with \(\sum e_id_i=1\). For each \(i\), choose finitely many generators of \(D_{d_i}\) over \(R\), and express them as fractions with numerators in \(D\). Let \(D_0\subset D\) be generated over \(R\) by all these numerators and by all \(d_i,e_i\). Then \((D_0)_{d_i}=D_{d_i}\). If \(d\in D\), at each \(i\) some \(d_i^{n_i}d\) belongs to \(D_0\). The powers \(d_i^{n_i}\) generate the unit ideal in \(D_0\): expand a sufficiently high power of \(\sum e_id_i=1\), so every term contains one of those powers. Hence \(d\in D_0\). Thus \(D\) is finitely generated over \(R\).

Write \(P=R[z_1,\ldots,z_n]\twoheadrightarrow D\), with kernel \(K\), and lift \(d_i,e_i\) to \(a_i,b_i\in P\). The kernels \(K_{a_i}\) of \(P_{a_i}\to D_{d_i}\) are finitely generated ideals. To justify this usual presentation fact without a Noetherian assumption, take a finite presentation \(R[y]/(r_j)\) of the target, express \(y\)'s in any chosen finite generating list \(z\), and express that list in the \(y\)'s. Substitution gives finitely many kernel generators \(r_j(h(z))\) and \(z_\ell-g_\ell(h(z))\); their quotient and the original presentation have inverse maps. The same argument includes a localization generator and its inverse relation.

Choose finitely many elements of \(K\) whose localizations generate each \(K_{a_i}\), and include
\[
1-\sum b_ia_i\in K.
\]
Let \(K_0\) be their generated ideal. The map \(P/K_0\to D\) is an isomorphism after localizing at each \(a_i\), and the \(a_i\) generate the unit ideal in \(P/K_0\). Therefore it is an isomorphism globally: every element of its kernel or cokernel is killed by a power of each \(a_i\), and the preceding unit-ideal argument kills that element. Thus \(K=K_0\) is finitely generated. \(\square\)

In particular, an affine locally finitely presented morphism between affine schemes is finitely presented. Around each source point choose an affine finite-presentation chart over a principal target open \(\operatorname{Spec}R_r\), then choose a principal open of the whole affine source contained in that chart. On the chart this is again a principal open, so its algebra is finitely presented over \(R_r\): adjoining the inverse of its function adds one generator and one relation. Since \(R_r=R[u]/(ru-1)\), the combined generators and relations also give a finite presentation over \(R\). Quasi-compactness selects a finite cover by these principal opens, and the localization lemma applies. Its first paragraph, without its kernel argument, proves the corresponding finite-generation assertion for affine locally finite-type morphisms.

Now let \(\{S_i\to S\}\) be fppf with \(S\) affine. The images of affine opens in the \(S_i\) are open in \(S\), by universal openness of flat locally finitely presented maps, and cover it. Quasi-compactness of \(S\) selects finitely many such affine pieces \(T_1,\ldots,T_m\). Their maps to \(S\) are flat and finitely presented by the preceding paragraph. The finite disjoint union
\[
S'=\coprod_{\nu=1}^m T_\nu
     =\operatorname{Spec}\Bigl(\prod_{\nu=1}^m\Gamma(T_\nu,\mathcal O)\Bigr)
 \longrightarrow S
\]
is affine, faithfully flat and finitely presented. It refines the original covering. The finite product is finitely presented: each factor has a finite presentation, and finite products can be presented by adjoining finitely many orthogonal idempotents summing to \(1\) together with those presentations on their idempotent factors.

This gives the promised finite refinement even when the original index set and the original covering schemes are not quasi-compact. It imposes no finiteness on the schemes \(X_i\).

#### 2.0.3. Descending quasi-affine neighbourhoods

**Quasi-affine lemma.** Let \(S'=\operatorname{Spec}B\to S=\operatorname{Spec}R\) be faithfully flat. A quasi-compact quasi-affine \(S'\)-scheme with descent datum descends effectively to a quasi-compact quasi-affine \(S\)-scheme, with the given datum.

*Proof.* Let \(V'\) be the scheme upstairs. It is separated and quasi-compact over the affine base. Write \(C=\Gamma(V',\mathcal O_{V'})\).

We need the actual flat base-change comparison for this ring. Choose a finite affine cover \(V'=\bigcup U_a\). The intersections \(U_a\cap U_b\) are affine, because \(V'/S'\) is separated: the intersection is the inverse image of its closed diagonal in the affine scheme \(U_a\times_{S'}U_b\). For every flat \(B\)-algebra \(B_1\), tensoring the finite sections equalizer by \(B_1\) gives
\[
B_1\otimes_B C
\xrightarrow{\sim}\Gamma(V'\times_{S'}\operatorname{Spec}B_1,\mathcal O).
                                                                    \tag{D.3}
\]
Flat tensor product preserves the kernel of the difference-of-restrictions map and finite products, so this is the specified natural ring homomorphism, not just an abstract module isomorphism. It is compatible with further flat base changes and with isomorphisms of the schemes.

We also need the canonical map
\[
c:V'\longrightarrow\operatorname{Spec}C
\]
to be a quasi-compact open immersion. Choose an affine embedding \(V'\subset\operatorname{Spec}E\), and finitely many principal opens \(D_E(f_a)\) contained in and covering \(V'\). Regard \(f_a\) as functions on \(V'\). Apply the same sections-equalizer argument to localization over \(E\); this is allowed because \(V'\) is a separated quasi-compact \(E\)-scheme. It gives
\[
C_{f_a}=\Gamma(D_E(f_a),\mathcal O)=E_{f_a}.
\]
Thus \(c\) identifies \(D_E(f_a)\) with \(D_C(f_a)\), by the actual restriction map. These identifications agree on the principal opens for \(f_af_b\). They identify \(V'\) with the finite union \(\bigcup D_C(f_a)\).

Both projections \(S'\times_S S'\to S'\) are flat. Equation (D.3) therefore carries the original descent isomorphism to an algebra descent datum on \(C\). The identities on triple overlaps follow functorially from the original cocycle and the compatible base-change maps. The affine algebra lemma gives an \(R\)-algebra \(C_0\), with a descent-compatible isomorphism \(B\otimes_R C_0\cong C\).

Put \(W=\operatorname{Spec}C_0\). The canonical embedding just proved identifies \(V'\) with an open subscheme of \(W_{S'}\). This open is invariant under the canonical datum: the canonical embedding is functorial, so the original descent isomorphism restricts the descended affine-hull isomorphism to the two copies of this open. The invariant opens lemma descends it to an open \(V\subset W\). It is quasi-compact, since it is the continuous image of quasi-compact \(V'\) under \(W_{S'}\to W\). Thus \(V/S\) is quasi-affine. Its pullback equals \(V'\) as an open subscheme of the identified affine hull, with exactly the prescribed datum. This proves effectivity and recovery. \(\square\)

The proofs of (D.3), the canonical embedding and this bridge also occur, with full local arguments, in AG-DFG Lesson 3, Lemmas 4.1–4.2 and Theorem 4.3. Their quasi-affine statement has the exact scope of the bridge just proved.

#### 2.0.4. Invariant source neighbourhoods and gluing

We first prove the main theorem for an affine fppf covering
\[
p:S'=\operatorname{Spec}B\longrightarrow S=\operatorname{Spec}R
\]
which is faithfully flat and finitely presented. Let \(X'\to S'\) be separated and locally quasi-finite with its given datum.

Write
\[
\mathcal R=X'\times_S S',\qquad
s:\mathcal R\to X',\quad
t:\mathcal R\xrightarrow{\phi}S'\times_S X'\to X' .
\]
Both \(s\) and \(t\) are base changes of \(p\), up to the specified isomorphism. In particular they are affine, flat, finitely presented and surjective. The diagonal base coordinates give the identity arrows. Inversion uses \(\phi^{-1}\), and the cocycle gives composition of arrows: two composable changes of base coordinates equal their direct change. These constructions give a scheme groupoid on \(X'\). They are just a way to express the specified datum; no quotient algebraic space is being assumed to exist.

Choose any affine open \(U\subset X'\), and form its saturation
\[
V'=t(s^{-1}(U))\subset X'.                                    \tag{D.4}
\]
It is open because \(s^{-1}(U)\) is open and \(t\) is open. It is quasi-compact: \(s^{-1}(U)\) is affine, since \(s\) is affine and \(U\) is affine; its continuous image is quasi-compact. Identity arrows show \(U\subset V'\).

The cocycle gives
\[
s^{-1}(V')=t^{-1}(V').                                       \tag{D.5}
\]
Here is the pointwise justification, including field comparisons. A point in the image (D.4) has an arrow from a point of \(U\), after extending its residue field. If it has another arrow to a point \(x\), extend both fields to a common field over the residue field of their common endpoint. The tensor product of the two extensions is nonzero, so such a common field exists. Composition in the groupoid gives an arrow from \(U\) to \(x\); hence \(x\in V'\). Inversion gives the reverse implication. This argument can be tested on geometric points, where compatible composable arrows are actual points after a common extension. Membership in an open is preserved by extension of residue fields, so it proves equality of the two underlying opens, and therefore equality as open subschemes. Equivalently, it is the cocycle restricted to a source-saturated open.

The restriction \(V'\to S'\) is separated and locally quasi-finite. It is also quasi-compact, since \(V'\) is quasi-compact and \(S'\) affine; preimages of principal opens are covered by finitely many affine principal opens in a finite affine cover of \(V'\). Thus it is separated and quasi-finite. The scheme Zariski Main consequence makes it quasi-affine: a separated quasi-finite scheme over an affine scheme is a quasi-compact open in an affine finite completion. The provider is *Zariski’s Main Theorem* (AG-MO-12), Theorem 4.1, at the prerequisite state recorded below.

By (D.5) the original datum restricts to \(V'\). The quasi-affine lemma descends it to a scheme \(V\to S\). Performing this construction for affine neighbourhoods of every point of \(X'\) gives an arbitrary open cover
\[
X'=\bigcup_{a\in A}V'_a
\]
by invariant quasi-compact opens, and descended schemes \(V_a/S\). The index set need not be finite.

We now give the gluing and recovery explicitly. For each pair \(a,b\), the intersection \(V'_a\cap V'_b\) is invariant. Under \(V_a\times_S S'\cong V'_a\), it descends by the invariant opens lemma to an open \(V_{ab}\subset V_a\). Under the other comparison it descends to \(V_{ba}\subset V_b\). The identity on \(V'_a\cap V'_b\) is a compatible morphism of their pullbacks, and the morphism descent lemma gives a unique isomorphism
\[
\psi_{ab}:V_{ab}\xrightarrow{\sim}V_{ba}.
\]
Its inverse is \(\psi_{ba}\), because that assertion becomes the identity after the faithfully flat cover.

On a triple overlap, \(V_{ab}\cap V_{ac}\) pulls back to \(V'_a\cap V'_b\cap V'_c\). The isomorphism \(\psi_{ab}\) takes it onto \(V_{ba}\cap V_{bc}\): the corresponding opens have equal inverse images, and the covering is surjective. On this open,
\(\psi_{bc}\psi_{ab}=\psi_{ac}\), since both pull back to the identity on the triple intersection and morphism descent is faithful. Likewise \(\psi_{aa}=\operatorname{id}\). Thus these are genuine scheme-gluing data. Ordinary gluing of schemes along open subschemes, for an arbitrary index set, produces \(X/S\).

After base change to \(S'\), its open pieces are \(V'_a\), and the gluing isomorphisms are their actual identities on intersections. The comparisons therefore glue to an isomorphism
\[
X\times_S S'\xrightarrow{\sim}X' .
\]
On \(S'\times_S S'\), it recovers \(\phi\) on every invariant open \(V'_a\); these opens cover the source, so it recovers \(\phi\) globally. This proves object effectivity, without any quasi-compactness assumption on \(X'\).

#### 2.0.5. Recovering the covering and the morphism properties

For an arbitrary fppf covering of an affine \(S\), choose the finite affine refinement constructed earlier. Pull the datum to that refinement and combine its finitely many schemes by disjoint union. A finite disjoint union of separated locally quasi-finite morphisms over the corresponding disjoint union of bases has the same properties, because each assertion is checked on an open-and-closed base component. The preceding construction gives \(X/S\).

Fix an original member \(S_i\). The refinement pulls back to an fppf covering of \(S_i\). On it, the isomorphisms of the original datum identify \(X_{S_i}\) with \(X_i\). The cocycle makes these comparisons compatible. The morphism descent lemma descends them and their inverses to an isomorphism \(X_{S_i}\cong X_i\). On double overlaps the resulting comparison is exactly \(\phi_{ij}\), because that equality holds after the refinement. This recovers also the members and overlaps not chosen in the finite refinement.

For an arbitrary base \(S\), do this on every affine open. On intersections, the local schemes represent the same restricted original datum; morphism descent supplies their unique compatible isomorphisms. On triple intersections those isomorphisms satisfy the cocycle, since the corresponding maps after the covering do. Ordinary Zariski gluing gives the global scheme and its morphism to \(S\), and the local comparisons glue to the required comparisons on every \(S_i\).

It remains to establish the asserted properties of this scheme; existence by itself would not establish them.

Separatedness descends from the given schemes: the base changes of
\(\Delta_{X/S}:X\to X\times_S X\) along the covering induced by the \(S_i\) are closed immersions. The closed-immersion descent consequence of the affine algebra and morphism lemmas makes this diagonal closed.

Local finite type descends as follows. Reduce the base to \(\operatorname{Spec}R\) with affine faithfully flat cover \(\operatorname{Spec}B\), and take an affine \(U=\operatorname{Spec}D\subset X\). Its base change is affine, and \(B\otimes_R D\) is finitely generated over \(B\), by the finite-generation assertion just established and local finite type upstairs. Expand a finite generating list into tensors, and collect the finitely many elements \(d_1,\ldots,d_n\in D\) occurring. The inclusion \(D_0=R[d_1,\ldots,d_n]\subset D\) becomes a surjection and an injection after tensoring with \(B\). Faithfulness applied to \(D/D_0\) gives \(D=D_0\). Hence \(X/S\) is locally of finite type.

Finally let \(U=\operatorname{Spec}D\) be such an affine source open over the affine base. Its pullback to \(\operatorname{Spec}B\) is quasi-compact and locally quasi-finite, hence quasi-finite. For \(s\in\operatorname{Spec}R\), choose \(s'\in\operatorname{Spec}B\) above it. The finite-type fibre \(U_s\) becomes zero-dimensional after the field extension \(\kappa(s)\to\kappa(s')\). Zero-dimensionality descends here directly: if the fibre ring had a strict chain of primes, choose a prime above its larger member after this faithfully flat field extension and apply flat going down to lift the smaller member. Their distinct contractions give a strict chain upstairs, a contradiction. Thus every fibre of \(U/S\) is zero-dimensional. A zero-dimensional finite-type algebra over a field is Noetherian and has finitely many irreducible components; each component has only its generic point, which is maximal. Its spectrum is consequently a finite set of closed points, and each singleton is open. All fibre points of \(U/S\) are therefore isolated. With local finite type this proves \(U/S\) quasi-finite, and these affine opens prove \(X/S\) locally quasi-finite. This proof never promotes the whole non-quasi-compact \(X/S\) to a quasi-finite morphism.

For two data, their compatible morphisms become compatible maps between the recovered schemes after the original covering, and the morphism descent lemma supplies the unique map over \(S\). In particular, two effectivity constructions are uniquely isomorphic, with the specified comparisons, by descending the identity of the original datum and its inverse. The stated equivalence of categories, including uniqueness, is now proved. \(\square\)

The scheme Zariski Main input is *Zariski’s Main Theorem* (AG-MO-12), Theorem 4.1: a separated quasi-finite morphism over an arbitrary affine scheme is quasi-affine and has a finite completion. Its full nonaffine proof and conductor foundations are genuinely assigned prerequisite repairs; the present course does not claim that they are already written. Universal openness, quotient topology and flat going down are *Flat morphisms* (AG-FSE-01), Theorem 2.2 and §3; openness retains that lesson’s finite-presentation Chevalley prerequisite. The local quasi-finiteness criterion is *Quasi-finite morphisms and Chevalley’s theorem* (AG-MO-06), Theorems 1.1–1.2. The affine equalizers, quasi-affine bridge, gluing and all original comparison maps needed here have been proved above.

The sources are the Stacks Project authors’ *More on Morphisms*, Tag 02W8, label `lemma-separated-locally-quasi-finite-morphisms-fppf-descend`, and *Descent*, labels `lemma-effective-for-fpqc-is-local-upstairs` and `lemma-quasi-affine` (Tag 0247), as read in the AI Integrated Stacks Project at revision `565b10e987aba5969b21145a0833f42d69f96790`. This proof is independently expressed eligible AI writing under CC0; the consulted source retains its human attribution and GFDL terms.

The elementary part of quotient sheafification is useful throughout the proof.

**Lemma 2.1.** Put \(F=U/R\). The map \(U\to F\) is an epimorphism of fppf sheaves, and

\[
U\times_F U\simeq R.
\]

**Proof.** Locally, a section of a sheafification comes from the presheaf being sheafified, and a presheaf quotient section has a representative in \(U\). This proves the first assertion. Two maps \(a,b:T\to U\) have equal images in \(F(T)\) precisely when they are related fppf locally. On a cover \(T_i\to T\), choose the corresponding maps \(r_i:T_i\to R\). Their endpoints agree on overlaps. The monomorphism \(j\) makes the \(r_i\) agree there, and the sheaf property of \(R\) glues them to a unique map \(T\to R\). Thus being related locally is equivalent to being related globally. This identifies the displayed fibre product as a sheaf, hence proves the assertion. \(\square\)

**Theorem 2.2 (étale quotient theorem).** For every étale equivalence relation \(R\rightrightarrows U\) over \(S\), the fppf quotient \(X=U/R\) is an algebraic space. The quotient map \(U\to X\) is representable, surjective and étale, and its relation is the original \(R\).

**Proof.** We first construct quotient neighbourhoods from affine pieces of \(U\), and then show that those neighbourhoods glue.

Suppose first that \(U\) is affine. The morphism \(U\times_S U\to U\times_{\operatorname{Spec}\mathbf Z}U\) is a monomorphism. Since the latter target is affine, \(U\times_S U\) is separated as an absolute scheme. A monomorphism is separated, so \(R\) is separated too. In particular \(s\) and \(t\) are separated. They are locally quasi-finite because they are étale.

Let \(a:T\to X\) be a map from a scheme. Lemma 2.1 gives an fppf cover \(T_i\to T\) and lifts \(a_i:T_i\to U\). On that cover, the sheaf \(V=T\times_X U\) is represented by

\[
V_i=T_i\times_{a_i,U,s}R.
\]

Each \(V_i\to T_i\) is separated and étale. The equality functor defining \(V\) supplies canonical identifications on overlaps, satisfying the cocycle condition. The scheme descent theorem produces a scheme representing \(V\). One can see the representation directly: maps into the descended scheme are compatible maps into the \(V_i\), and these are exactly sections of the sheaf \(V\). Since each \(V_i\to T_i\) is étale and surjective, the descended morphism has these properties. Surjectivity here follows because \(s\) has the identity section. We have proved representability and the presentation condition for \(U\to X\).

We must still prove representability of the diagonal. The morphism \(j:R\to U\times_S U\) is separated and locally quasi-finite. For local finite type, use that its composition with a projection is étale: a morphism whose composition is locally of finite type is locally of finite type. A monomorphism has at most one geometric point in each geometric fibre, so this local finite type morphism is locally quasi-finite.

Given \((a,b):T\to X\times_S X\), take an fppf cover on which both sections have lifts to \(U\). On this cover their equality scheme is the base change of \(j\). It is therefore separated and locally quasi-finite. Apply the same scheme descent theorem to these equality schemes. The descended scheme represents \(E_{a,b}\), by the same sheaf argument. This proves the diagonal condition when \(U\) is affine.

We now return to arbitrary \(U\). For any open subscheme \(A\subset U\), let \(R_A=R\times_{U\times_S U}(A\times_S A)\), and let \(X_A=A/R_A\). Its map to \(X\) is a monomorphism: if two coordinates in \(A\) are related in \(U\), their unique relation arrow lies in \(R_A\).

The map \(X_A\to X\) is represented by open immersions. To prove this without assuming \(X\) algebraic, form the saturation

\[
W_A=t(s^{-1}(A))\subset U.
\]

It is open because étale morphisms are open. Its points are precisely the points related, after a residue-field extension if necessary, to points of \(A\). The equivalence relation identities give \(s^{-1}(W_A)=t^{-1}(W_A)\) as open subschemes.

For \(T\to X\), choose lifts \(a_i:T_i\to U\) on an fppf cover. The opens \(a_i^{-1}(W_A)\) agree on overlaps: the lifts there are endpoints of an arrow in \(R\). They descend to an open \(T_A\subset T\). A section on a test scheme over \(T\) belongs to \(X_A\) exactly when it factors through this open. Indeed, membership in \(W_A\) can be lifted to \(s^{-1}(A)\) fppf locally using the surjective étale map \(s^{-1}(A)\to W_A\); its other endpoint is a coordinate in \(A\). Conversely, a coordinate in \(A\) makes any related coordinate lie in \(W_A\). Thus \(T_A=T\times_X X_A\).

Take an affine open cover \(\{A_\lambda\}\) of \(U\). The quotient opens \(X_{A_\lambda}\) cover \(X\) and, by the affine case, are algebraic spaces. Here they cover even in the Zariski sense appropriate to representable opens: after pulling back to any \(T\to X\), the opens \(T_{A_\lambda}\) cover \(T\).

For completeness, the diagonal of \(X\) is now represented as follows. For a pair of sections on \(T\), cover \(T\) by opens on which the first lies in some \(X_{A_\lambda}\). Its equality with the second is possible only on the open where the second also lies in that same \(X_{A_\lambda}\). There the equality functor is represented by the diagonal of this algebraic space. These schemes glue over their open intersections, since they represent the same equality functor. Thus \(\Delta_X\) is representable.

Finally the maps \(A_\lambda\to X_{A_\lambda}\to X\) are representable étale maps and together are surjective. Their disjoint union is a scheme presentation. Hence \(X\) is algebraic. The original map \(U\to X\) is representable by the diagonal observation in Section 1. On an fppf cover of any test scheme admitting coordinates in \(U\), its base change is a base change of \(s:R\to U\). It is therefore étale and surjective. Lemma 2.1 identifies its relation with \(R\). \(\square\)

*Reference:* [Stacks, Tag 02WW]. The affine neighbourhoods in the proof are used to make scheme descent effective. They do not assert that \(X_{A_\lambda}\) is an affine scheme.

**Corollary 2.3.** An algebraic space is the quotient of any of its étale presentations by the corresponding equivalence relation.

**Proof.** An étale surjection has local sections for the étale topology. Thus \(U\to X\) is an epimorphism of fppf sheaves. Its kernel relation is \(U\times_X U\). Lemma 2.1, or directly the gluing of local coordinates, identifies its quotient with \(X\). \(\square\)

## 3. Products and gluing

**Proposition 3.1.** If \(X\to Z\leftarrow Y\) are morphisms of algebraic spaces over \(S\), then \(X\times_Z Y\) is an algebraic space and has the expected fibre product universal property.

**Proof.** The fibre product \(H\) in sheaves exists. Choose presentations \(U\to X\), \(V\to Y\). Since \(Z\) has representable diagonal, \(W=U\times_Z V\) is a scheme. The map \(W\to H\) is the composition of base changes of the two presentations, so is representable, étale and surjective.

For two sections of \(H\) over a scheme \(T\), their equality is equivalent to the equality of their \(X\)-coordinates and of their \(Y\)-coordinates. The two equality schemes over \(T\) exist by the diagonal conditions of \(X\) and \(Y\). Their scheme fibre product over \(T\) represents the equality functor for \(H\). Thus \(H\) has representable diagonal. Its universal property is its universal property as a sheaf, since the category of algebraic spaces is a full subcategory of sheaves. \(\square\)

**Proposition 3.2.** Algebraic spaces can be glued along open subspaces with specified identifications satisfying the cocycle condition. A disjoint union indexed by a set is an algebraic space, subject to the fixed universe convention.

**Proof.** Construct the glued sheaf by identifying the specified open subfunctors. For any test scheme, membership in an open piece is an open condition and the pieces cover. As in the last part of Theorem 2.2, equality schemes can be built on these opens and glued, establishing the diagonal condition. Choose a scheme presentation of each piece. Their disjoint union is a scheme, and its map to the glued sheaf is representable étale and surjective, because each piece is a representable open. The disjoint union is the case of empty overlaps. \(\square\)

This argument is also why ordinary Zariski gluing remains available after passing from schemes to spaces.

## 4. Symmetry and separation

Suppose an abstract group \(G\) acts on an \(S\)-scheme \(U\). Use the action relation

\[
R=\coprod_{g\in G}U,
\qquad (g,u)\longmapsto (u,g(u)).
\]

This is an equivalence relation precisely when the action has no stabilizers on geometric points. One useful form of that condition is

\[
g(u)=u\text{ and }g|_{\kappa(u)}=\operatorname{id}
\quad\Longrightarrow\quad g=1.
\tag{4.1}
\]

It is possible for a group element to fix an ordinary point while moving its residue field. Condition (4.1) permits this. We call an action satisfying it **free**.

**Proposition 4.1.** Under condition (4.1), the action relation is an étale equivalence relation. Its quotient \(U/G\) is an algebraic space, and \(U\to U/G\) is a torsor for the constant group in the fppf topology. If \(G\) is finite, the quotient map is finite étale and surjective.

**Proof.** A map from a test scheme into \(R\) consists of a locally constant choice of \(g\) and a map to \(U\). Suppose two such maps have the same pair of endpoints. Locally on the test scheme their group labels are constant. At any point \(z\) of a nonempty such piece, equality of endpoints shows that \(g^{-1}h\) fixes the image \(u\) and acts trivially after the injective field map \(\kappa(u)\to\kappa(z)\). It acts trivially on \(\kappa(u)\), and (4.1) gives \(g=h\). The maps to \(U\) then agree too. This proves the monomorphism condition, including disconnected test schemes.

Identity, inversion and multiplication of labels provide reflexivity, symmetry and transitivity. Each projection is, on a component, either the identity of \(U\) or an automorphism, and is therefore étale. Theorem 2.2 applies. Lemma 2.1 gives the torsor identity

\[
G\times U\simeq U\times_{U/G}U.
\]

The quotient map has local sections, and this identity makes the action simply transitive on those local trivializations. If \(G\) is finite, a base change of the quotient map by itself is the finite disjoint union of identity maps on \(U\). It is finite étale. Finiteness and étaleness descend fppf locally on the target; the quotient map is therefore finite étale and surjective. \(\square\)

For an algebraic space \(X\) over \(S\), we use the following separation conditions:

| Condition | Condition on \(\Delta_{X/S}\) |
|---|---|
| Quasi-separated | Quasi-compact |
| Locally separated | An immersion |
| Separated | A closed immersion |

The conditions can be tested on the relation of a presentation. Indeed, \(j:R\to U\times_S U\) is the pullback of \(\Delta_{X/S}\) along the representable étale surjection \(U\times_S U\to X\times_S X\). After any test scheme mapping into the latter sheaf, this gives an étale cover by schemes. Quasi-compactness, immersion and closed immersion descend under these covers. Thus the test does not require that \(U\) itself be separated.

**Proposition 4.2.** For a free action of a finite group, \(U/G\) is quasi-separated over \(S\) if \(U\) is quasi-separated over \(S\), and separated over \(S\) if \(U\) is separated over \(S\).

**Proof.** Each graph of \(g:U\to U\) is obtained from \(\Delta_{U/S}\) by an automorphism of \(U\times_S U\). In the quasi-separated case all these graphs are quasi-compact morphisms, and their finite disjoint union is quasi-compact. This proves the first assertion by the relation test.

In the separated case the graphs are closed immersions. Distinct graphs have disjoint underlying images: a point in their intersection would give, over a common residue-field extension, a geometric point fixed by \(g^{-1}h\), contradicting (4.1). A finite family of disjoint closed subschemes has disjoint-union map a closed immersion. To check this on an affine open of the target, the corresponding ideals are pairwise comaximal, and the Chinese remainder theorem gives the required quotient algebra. Apply the relation test again. \(\square\)

*References:* [Stacks, Tags 02Z2 and 02Z4].

**Proposition 4.3.** A free action of a finite group on an affine scheme \(U=\operatorname{Spec}A\) has affine quotient \(\operatorname{Spec}(A^G)\). The algebra \(A\) is finite locally free over \(A^G\), and the quotient map is finite étale. More generally, if every orbit in a scheme \(U\) is contained in an affine open, then \(U/G\) is a scheme.

**Proof.** Set \(B=A^G\). The action graphs in the absolute affine product \(U\times U\) are pairwise disjoint closed subschemes by freeness. The Chinese remainder theorem therefore makes the map

\[
A\otimes_{\mathbf Z}A\longrightarrow\prod_{g\in G}A,
\qquad a\otimes b\longmapsto (a\,g(b))_g
\]

surjective. Choose a finite tensor sum mapping to the vector which is one in the identity component and zero elsewhere. Write its entries as \(a_i,b_i\in A\); thus

\[
\sum_i a_i g(b_i)=\begin{cases}1&g=1,\\0&g\ne1.\end{cases}
\tag{4.2}
\]

The sum \(\operatorname{tr}(c)=\sum_g g(c)\) belongs to \(B\). Equation (4.2) gives, for every \(c\in A\),

\[
\sum_i a_i\operatorname{tr}(b_i c)=c.
\tag{4.3}
\]

This is a finite dual basis: \(A\) is a direct summand of a finite free \(B\)-module, hence finite projective. Every \(c\in A\) satisfies the monic polynomial \(\prod_g(T-g(c))\) with coefficients in \(B\). The integral inclusion \(B\subset A\) is surjective on spectra by lying over. Consequently this finite projective algebra is faithfully flat.

The induced map

\[
\theta:A\otimes_B A\longrightarrow\prod_g A
\]

is still surjective. It is injective as well. If \(z=\sum_j c_j\otimes d_j\) has zero image, then \(\sum_j c_jg(d_j)=0\) for every \(g\). Expand each \(d_j\) with (4.3). The coefficient of \(1\otimes a_i\) in this expansion is

\[
\sum_j c_j\operatorname{tr}(b_i d_j)
=\sum_g g(b_i)\sum_j c_jg(d_j)=0.
\]

Thus \(z=0\). The faithfully flat map \(\operatorname{Spec}A\to\operatorname{Spec}B\) has the action relation as its fibre relation. Fppf descent of sections of a sheaf therefore identifies its quotient with \(\operatorname{Spec}B\). After base change by \(\operatorname{Spec}A\) it is a disjoint union of identity maps, so it is finite étale. This also identifies its rank as \(|G|\).

For the general assertion, first produce invariant affine neighbourhoods. Let an orbit \(E\) lie in an affine open \(A_0\subset U\). The intersection \(V=\bigcap_g g(A_0)\) is a \(G\)-invariant open containing \(E\), and is an open of \(A_0\). There is a function \(f\) on \(A_0\) such that \(E\subset D(f)\subset V\). Indeed, the ideal defining the closed complement of \(V\) is not contained in any of the finitely many primes in \(E\); finite prime avoidance gives such an \(f\). On \(V\), all translates \(g(f)\) are regular. Their product \(N=\prod_g g(f)\) is invariant and nonzero at every point of \(E\).

The invariant open \(D_V(N)\) is affine: it lies in \(D_{A_0}(f)\), and is the principal open of that affine scheme cut out by the restriction of \(N\). This construction does not assume that intersections of affine opens in \(U\) are affine.

These invariant affine opens cover \(U\). Their quotients are affine by the first part. Each quotient maps to \(U/G\) as a representable open immersion: its pullback to \(U\) is precisely the invariant open, or one can apply the saturation argument in Theorem 2.2. Thus the algebraic space \(U/G\) has a cover by open affine schemes. Gluing these schemes over their open overlaps represents it by a scheme. \(\square\)

Infinite groups behave differently even when every nonidentity element is a very simple automorphism.

## 5. Three quotients that distinguish the definitions

### 5.1. Identify opposite coordinates except at zero

Let \(k\) be a field with \(2\ne0\), and put \(U=\mathbf A^1_k\). Use the relation

\[
R=\mathbf A^1_k\amalg\mathbf G_{m,k},
\quad j|_{\mathbf A^1}(x)=(x,x),
\quad j|_{\mathbf G_m}(x)=(x,-x).
\]

Both projections are étale. The two components have disjoint images: their graphs meet only at zero, which has been removed from the second component. The equivalence relation identities follow from changing sign twice. Thus Theorem 2.2 produces \(X=U/R\).

The map \(j\) is quasi-compact. In fact both components are quasi-compact schemes, and every open subset of either is quasi-compact, because they are Noetherian. The inverse image of an affine open of \(\mathbf A^2_k\) is consequently quasi-compact. Thus \(X\) is quasi-separated.

It is not locally separated. Let \(D\) be the diagonal and \(L\) the line \(y=-x\) in \(\mathbf A^2_k\). The image of \(j\) is \(D\cup(L\setminus\{0\})\), whose underlying set is the closed set \(D\cup L\). Suppose \(j\) were an immersion. Its underlying space would then have the subspace topology of this union. But the diagonal component is open and closed in \(R\). Its image \(D\) is not open in \(D\cup L\): any open neighbourhood of the origin on the line \(L\) contains its generic point, which is in \(L\setminus\{0\}\) and outside \(D\). This contradicts the subspace topology. Hence \(j\) is not an immersion.

Every scheme over \(k\) is locally separated: on an affine neighbourhood of a point its diagonal is closed, and these neighbourhoods give the immersion property for the full diagonal. Therefore \(X\) is not a scheme. The obstruction is visible in the relation, without a search for a hypothetical coordinate ring.

Away from the image of zero, the quotient is \(\mathbf G_m\). The map \(x\mapsto x^2\) is finite étale on \(\mathbf G_m\), and its fibre relation is exactly the identity and sign-change graphs. It represents the quotient there. Every neighbourhood of the image of zero retains the failure of immersion just proved, so none is a scheme.

*Reference:* [Stacks, Tag 02Z1].

### 5.2. An algebraic closure with a discrete Galois action

Let \(U=\operatorname{Spec}\overline{\mathbf Q}\) and let \(G=\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)\) act as an abstract group. Its only ordinary point is fixed by every element, but a nonidentity element acts nontrivially on its residue field. Condition (4.1) holds, so \(X=U/G\) is an algebraic space over \(\mathbf Q\).

It is not \(\operatorname{Spec}\mathbf Q\). If it were, its presentation would make \(\operatorname{Spec}\overline{\mathbf Q}\to\operatorname{Spec}\mathbf Q\) étale. A field étale over \(\mathbf Q\) is a finite separable extension; the algebraic closure is infinite. This contradiction already distinguishes the two sheaves.

In fact \(X\) is not a scheme. Here is a useful argument that avoids a classification of finite subgroups of the Galois group. Suppose it were a scheme, and choose an affine open \(V\subset X\) containing the image \(x\) of the unique point of \(U\). The preimage of \(V\) is all of \(U\), so \(U\to V\) is étale. It is locally of finite presentation. Since its source and target are affine and its source has one point, it is also quasi-compact; its separatedness follows from affineness. It is therefore of finite presentation. Its fibre over \(x\) shows that \(\overline{\mathbf Q}\) is finite separable over \(\kappa(x)\).

The map \(U\to X\) is invariant under every element of \(G\), so the embedded field \(\kappa(x)\subset\overline{\mathbf Q}\) lies in the fixed field \(\mathbf Q\). As the map is over \(\mathbf Q\), this embedded field is exactly \(\mathbf Q\). That contradicts the finite-extension conclusion.

The distinction comes from the group used to form the relation. In this example it is the constant group indexed by the underlying set of \(G\), not a group object carrying the profinite topology.

*Reference:* [Stacks, Tag 02Z6].

### 5.3. Translation by integers

Let \(k\) have characteristic zero, and let \(\mathbf Z\) act on \(\mathbf A^1_k\) by \(x\mapsto x+n\). A nonzero translation has no fixed geometric point. At the generic ordinary point it acts nontrivially on \(k(x)\), so condition (4.1) still holds. Put

\[
X=\mathbf A^1_k/\mathbf Z.
\]

The relation is an infinite disjoint union of affine lines. Its entire inverse image over the affine scheme \(\mathbf A^2_k\) is not quasi-compact: the infinitely many nonempty open-and-closed components have no finite subcover. Thus the relation map is not quasi-compact, and \(X\) is not quasi-separated.

A further failure concerns residue fields. The generic point gives \(\gamma:\operatorname{Spec}k(x)\to X\). Unlike a point of a scheme, it cannot factor through a monomorphism from the spectrum of a field. We prove this next, so that the obstruction is explicit.

**Lemma 5.1.** Let a constant abstract group \(G\) act freely on \(U\), and let \(\operatorname{Spec}L\to U/G\) be any field-valued point. For each connected component \(\operatorname{Spec}L'\) of its pullback to \(U\), the extension \(L'/L\) is finite Galois and its Galois group is isomorphic to the subgroup of \(G\) preserving that component.

**Proof.** The pullback \(P\to\operatorname{Spec}L\) is a nonempty étale scheme. It is a disjoint union of spectra of finite separable extensions of \(L\), and \(P\) is a \(G\)-torsor by Proposition 4.1. Let \(H\) preserve the chosen component \(P_0=\operatorname{Spec}L'\). Restricting the torsor identity gives

\[
H\times P_0\simeq P_0\times_L P_0.
\]

The right side is finite over \(P_0\), of degree \([L':L]\), so \(H\) is finite with that cardinality. The isomorphism identifies its elements with all \(L\)-automorphisms of \(L'\). A finite separable extension with as many automorphisms as its degree is Galois. \(\square\)

Suppose \(\gamma\) factored as

\[
\operatorname{Spec}k(x)\longrightarrow\operatorname{Spec}L
\xrightarrow{m}X
\]

with \(m\) a monomorphism. Pull \(m\) back to \(\mathbf A^1_k\), obtaining a monomorphism \(P\to\mathbf A^1_k\) with a lift of the generic point. A component \(\operatorname{Spec}L'\subset P\) therefore receives \(\operatorname{Spec}k(x)\) and maps to the generic point of the affine line. The composite

\[
k(x)\longrightarrow L'\longrightarrow k(x)
\]

is the identity. Since a field map is injective, these maps force \(L'=k(x)\): the second map embeds \(L'\) into \(k(x)\) and its image already contains all of \(k(x)\). Lemma 5.1 says that \(L'/L\) has Galois group a finite subgroup of \(\mathbf Z\), hence is trivial. Thus \(L=L'=k(x)\).

However, restricting the relation to the generic point gives

\[
\operatorname{Spec}k(x)\times_X\operatorname{Spec}k(x)
\simeq\coprod_{n\in\mathbf Z}\operatorname{Spec}k(x).
\]

There is one component for each translation automorphism of the rational function field. The diagonal lands in the component indexed by zero and is not an isomorphism. Therefore \(\gamma\) is not a monomorphism, contradicting the factorization. This explains why the points of general algebraic spaces must be defined by equivalence classes of field-valued maps rather than by monomorphisms from spectra of fields.

*References:* [Stacks, Tags 02Z5 and 02Z7].

## 6. Exercises and solutions

The following exercises revisit the constructions through different tests: equality of coordinates, gluing, and the effect of changing the group. The final exercise develops the affine-neighbourhood question for finite quotients.

**Exercise 6.1 (first steps).** For a scheme \(V\), identify the equality scheme for two maps \(T\to V\). Then construct a presentation of \(\coprod_i X_i\) from presentations \(U_i\to X_i\).

**Solution.** The equality scheme is \(T\times_{V\times_S V}V\), using the diagonal of \(V\). Thus schemes satisfy the diagonal condition, and the identity gives their presentations. For the disjoint union, use \(\coprod_i U_i\). The equality functor between two sections splits over the open-and-closed parts of \(T\) on which both choose the same index. On each such part it is the equality scheme for \(X_i\); on parts with different indices it is empty. These schemes glue, and the disjoint-union presentation is representable étale and surjective.

**Exercise 6.2 (separation).** In the sign-identification example, replace the removed origin in the second graph by an arbitrary finite set of closed points invariant under sign. Require that the set contain zero. Describe the quotient off that set, and show that it is not locally separated at the image of zero when the second graph is nonempty.

**Solution.** On the invariant complement \(A\subset\mathbf A^1\), sign is a free action of the two-element group. The square map identifies \(A/\{\pm1\}\) with the open of \(\mathbf A^1\) obtained by removing the squares of the excluded points, and this open is contained in \(\mathbf G_m\). The restricted relation is its fibre relation. For the full quotient, the second graph remains dense in \(L:y=-x\), while its origin is absent. The image of the diagonal component is not open near the origin in the union of the two lines. The topology argument of Section 5.1 again proves that the relation is not an immersion. In the original example, the same argument also proves quasi-separatedness because both components are Noetherian and quasi-compact.

**Exercise 6.3 (finite torsors).** Let a finite group act freely on \(U\). Find the degree of \(U\to U/G\) and explain why a \((U/G)(T)\)-point need not lift to \(U(T)\).

**Solution.** Proposition 4.1 proves that the map is finite étale; its pullback by itself is \(|G|\) copies of \(U\). Therefore it is finite locally free of constant rank \(|G|\). A point of the quotient over \(T\) pulls back to a \(G\)-torsor on \(T\). It has a lift precisely when that torsor has a section. Such a section trivializes the torsor; a nontrivial torsor has local sections but no global section. For example, a nontrivial quadratic finite separable extension \(L/k\) defines the free Galois action on \(\operatorname{Spec}L\), whose quotient is \(\operatorname{Spec}k\). The latter's identity point does not lift to \(\operatorname{Spec}L(k)\).

**Exercise 6.4 (infinite symmetry).** Replace the integer translation action by translation by the additive group of a nonzero finitely generated subgroup \(\Lambda\subset k\), where \(k\) has characteristic zero. Show that the quotient is not quasi-separated and that its generic point has no factorization through a field-spectrum monomorphism.

**Solution.** The group \(\Lambda\) is infinite and torsion-free. Its action is free on geometric points, and its action on \(k(x)\) is faithful. The relation is the disjoint union of \(\mathbf A^1\) indexed by \(\Lambda\). Its inverse image over \(\mathbf A^2\) is not quasi-compact, proving the first assertion. For the second, the proof after Lemma 5.1 applies unchanged: a hypothetical factorization forces \(L'=k(x)\), and then the finite stabilizer subgroup is trivial. The restricted relation on \(\operatorname{Spec}k(x)\) still has one component for each \(\lambda\in\Lambda\), contradicting the monomorphism. Taking \(\Lambda=\mathbf Z\cdot1\) gives the original integer example.

**Exercise 6.5 (affine neighbourhoods).** Suppose a finite group acts freely on a scheme \(U\) quasi-projective over an affine scheme. Show that every orbit lies in an invariant affine open and that \(U/G\) is a scheme. Why would simply taking the intersection of all translates of an affine open require an extra argument?

**Solution.** A quasi-projective scheme over an affine base has an ample invertible sheaf, and every finite subset lies in an affine open. The precise scheme result is [Stacks, Tag 01ZY]. One way to obtain the affine neighbourhood is to embed \(U\) as a locally closed subscheme of a projective space over the base. Choose homogeneous functions whose standard opens cover the finite set and avoid the boundary of \(U\) in its closure. Homogeneous prime avoidance supplies one homogeneous function in their generated ideal avoiding every prime in the finite set. Its standard open avoids the boundary; its intersection with \(U\) is closed in an affine standard open and is therefore affine.

The homogeneous prime avoidance used here is [Stacks, Tag 00JS]. Apply the affine-neighbourhood result to the orbit, then apply the norm construction in Proposition 4.3 to obtain an invariant affine open. Its quotient is the spectrum of the invariant ring, and these affine quotients give an open scheme cover of \(U/G\). The intersection of the translates is invariant and open, but affineness of an open subscheme does not follow just from its being contained in an affine scheme. In the present quasi-projective case separatedness also gives affineness of finite intersections of affine opens. The norm construction proves the needed refinement even without that shortcut.

## Prerequisites and sources

The scheme effectiveness theorem for separated, locally quasi-finite descent data [Stacks, Tag 02W8] is proved in §2.0, including arbitrary non-quasi-compact sources and recovery of the complete original descent datum. Its genuine Zariski Main prerequisite state is recorded there. The scheme descent references for opens, étaleness, surjectivity, finiteness, quasi-compactness, immersion and closed immersion are respectively [Stacks, Tags 03N0, 02VN, 02KV, 02LA, 02KQ, 02YM and 02L6]. For immersions, the locality asserted here is for fppf coverings. We also use the ample finite-set lemma [Stacks, Tag 01ZY] and homogeneous prime avoidance [Stacks, Tag 00JS]. These are statements about schemes, not additional quotient assertions.

## References

- **[Stacks]** The Stacks project, *Algebraic Spaces* and *More on Morphisms*, especially Tags 02WW, 02W8, 02Z1, 02Z2, 02Z4, 02Z5, 02Z6 and 02Z7. The corresponding text is also available in [AI Integrated Stacks Project, Algebraic Spaces](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/spaces.html), an edition with AI-proposed corrections and AI-written additions which has not been reviewed by the Stacks project's maintainers. The [official Stacks project](https://stacks.math.columbia.edu/) retains its own publication and tags.
- **[Behrend]** K. Behrend, *Introduction to algebraic stacks*, lecture notes, 2012. [Author's lecture notes](https://personal.math.ubc.ca/~behrend/math615A/stacksintro.pdf).
- **[EGA IV]** A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique IV*, third part, Publications Mathématiques de l'IHÉS 28 (1966), §10.10, for the earlier terminology concerning Serre's algebraic spaces. [Original text](https://www.numdam.org/item/PMIHES_1966__28__5_0/).
