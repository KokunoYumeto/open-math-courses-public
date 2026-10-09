# Proper morphisms and the valuative criterion of properness

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A closed map sends closed subsets to closed subsets. Universal closedness asks for that behaviour after every change of base. Valuation rings turn this apparently unlimited topological test into an extension problem: can a point defined over a fraction field acquire a compatible limit over the valuation ring? Properness combines existence of these limits with uniqueness and finite type.

We use the specialization witnesses, domination theorem, value groups, and separatedness criteria proved in Valuation rings and separatedness, and the integral and finite morphisms of Affine and finite morphisms. Quasi-compactness and finite type have the conventions of Finiteness of morphisms. No separation or Noetherian hypothesis is implicit. A valuation ring may have arbitrary rank; its fraction field is always the field occurring in its valuation diagram.

## 1. Closedness after changing the base

A morphism \(f:X\to S\) is **universally closed** if, for every \(S'\to S\), the projection \(X\times_S S'\to S'\) is a closed map of underlying spaces. It need not be a closed immersion. For example, an integral morphism is universally closed, even when many points lie over a point of the base.

We write \(s'\leadsto s\) when \(s\) lies in the closure of \(\{s'\}\). We say that **specializations lift** along \(f\) if, for every such specialization and every specified \(x'\) over \(s'\), there is a specialization \(x'\leadsto x\) with \(f(x)=s\). Specifying \(x'\) matters: merely finding some point over \(s\) is a weaker assertion.

**Lemma 1.1.** A closed morphism lifts specializations. Conversely, a quasi-compact morphism that lifts specializations is closed.

**Proof.** If \(f\) is closed, the image of \(\overline{\{x'\}}\) is closed and contains \(s'\). It therefore contains \(s\), giving the required \(x\).

For the converse, let \(Z\subset X\) be any closed subset, endowed with its reduced closed subscheme structure. The map \(Z\to S\) is quasi-compact. Its image is stable under specialization: a point of \(Z\) can be specialized as required in \(X\), and every such specialization stays in \(Z\). The quasi-compact image criterion of Theorem 1.2 in *Finiteness of morphisms* says that this image is closed. This applies to every \(Z\). \(\square\)

A **valuation diagram** for \(f\) consists of compatible maps

\[
u:\operatorname{Spec}K\longrightarrow X,
\qquad a:\operatorname{Spec}R\longrightarrow S,
\qquad K=\operatorname{Frac}(R),
\tag{1.1}
\]

where \(R\) is a valuation ring and compatibility means \(fu=a|_{\operatorname{Spec}K}\). An extension is an \(S\)-morphism \(\widetilde u:\operatorname{Spec}R\to X\) restricting to \(u\). The **existence part** asks for at least one extension in every diagram; the **uniqueness part** asks for at most one.

**Theorem 1.2 (universal closedness).** The existence part is equivalent to lifting specializations after every base change. In particular, if \(f\) is quasi-compact, then

\[
f\text{ is universally closed}
\quad\Longleftrightarrow\quad
f\text{ satisfies the existence part.}
\tag{1.2}
\]

**Proof.** First suppose specializations lift after every base change. For (1.1), replace the base by \(\operatorname{Spec}R\). The resulting generic point \(x'\) of the diagram in \(X_R\) specializes to a point \(x\) over the closed point of \(\operatorname{Spec}R\). The given generic map identifies \(\kappa(x')\) with a subfield of \(K\). We have maps

\[
R\longrightarrow \mathcal O_{X_R,x}
\longrightarrow\kappa(x')\longrightarrow K,
\tag{1.3}
\]

whose composite is the given inclusion \(R\subset K\). The first map is local. The image \(C\) of the middle local ring in \(K\) is a local subring containing and dominating \(R\): its maximal ideal contracts to the maximal ideal of \(R\). A valuation ring is maximal among local subrings of its fraction field that dominate it, by the domination characterization in the valuation lesson. Thus \(C=R\). The resulting local map \(\mathcal O_{X_R,x}\to R\) defines \(\operatorname{Spec}R\to X_R\). Its generic restriction is the originally specified map, since all maps in (1.3) used that same embedding into \(K\). Projection to \(X\) gives the extension.

Conversely, existence survives arbitrary base change. An extension into \(X\), together with the prescribed map to the new base, defines the extension into the fibre product. It is therefore enough to lift one specialization \(s'\leadsto s\) along \(f\). Given \(x'\) over \(s'\), apply the specialization-witness theorem of the valuation lesson with the specified field extension \(\kappa(x')/\kappa(s')\). It supplies a valuation ring \(R\subset K=\kappa(x')\) and a map \(\operatorname{Spec}R\to S\) whose generic point maps to \(s'\) and whose closed point maps to \(s\). The canonical map \(\operatorname{Spec}\kappa(x')\to X\) completes a valuation diagram. Any extension sends the closed point to the desired specialization of \(x'\).

If \(f\) is universally closed, Lemma 1.1 gives lifting after every base change, hence existence. If \(f\) is quasi-compact and satisfies existence, its base changes are quasi-compact and lift specializations, so Lemma 1.1 makes all of them closed. \(\square\)

These are [Stacks, Tags 01KC, 01KE and 01KF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-proposition-characterize-universally-closed). The domination argument explains why the extension uses the original valuation ring, rather than an unspecified larger valuation ring.

## 2. Properness and its permanence properties

A morphism is **proper** if it is separated, of finite type, and universally closed. Each requirement has a distinct role. Finite type controls how much algebra is needed; separatedness controls uniqueness; universal closedness controls existence. An infinite integral algebra can be universally closed and separated without being of finite type.

**Theorem 2.1.** Properness is local on the target for open covers and is stable under arbitrary base change and composition. Closed immersions and finite morphisms are proper. If

\[
X\xrightarrow{f}Y\xrightarrow{g}S
\]

has \(gf\) proper and \(g\) separated, then \(f\) is proper. Consequently, every \(S\)-morphism from a proper \(S\)-scheme to a separated \(S\)-scheme is proper and has closed image.

**Proof.** Universal closedness is target-local: after any base change, the inverse images of a target open cover form an open cover, and the images of a closed subset are closed on all those opens exactly when its full image is closed. Separatedness and finite type are target-local by the first two lessons. Their conjunction is therefore target-local.

Base changes of universally closed maps remain universally closed by associativity of fibre products. A composite of universally closed maps is universally closed because every base change of the composite is a composite of closed maps. Separatedness and finite type have the same permanence properties, proving the corresponding assertions for properness.

A closed immersion is separated, of finite type, and remains a closed immersion after base change. It is therefore proper, even when its ideal is not finitely generated. A finite morphism is affine and hence separated; its finite module algebra is finitely generated as an algebra. It is integral, so universally closed by the integral-morphism theorem. This proves properness of finite morphisms without a Noetherian assumption.

For cancellation, factor \(f\) as

\[
X\xrightarrow{\Gamma_f}X\times_S Y
\xrightarrow{\operatorname{pr}_Y}Y.
\tag{2.1}
\]

The graph \(\Gamma_f\) is a closed immersion because \(Y\to S\) is separated. The projection is the base change of the proper map \(X\to S\). Both arrows are proper, hence so is \(f\). The final assertion is this factorization applied to the structure maps. A proper map is closed, and the image of its entire source is thus closed. No finite-type hypothesis on \(Y\to S\) is needed. \(\square\)

The target-local, composition, base-change, closed-immersion, image, and finite assertions are [Stacks, Tags 01W2–01W6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-image-proper-scheme-closed) and [Tag 01WN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-proper).

**Corollary 2.2.** If \(p:X'\to X\) is surjective and universally closed and \(fp:X'\to S\) is universally closed, then \(f\) is universally closed.

**Proof.** Every base change of a surjective scheme morphism is surjective: over a point, a pair of nonempty fibres gives a point of the fibre product because the tensor product of two field extensions of the residue field is nonzero. Given a closed subset \(Z\subset X_T\), its inverse image in \(X'_T\) is closed, and its image in \(T\) equals the image of \(Z\). That image is closed by universal closedness of \((fp)_T\). \(\square\)

In fact the proof only needs universal surjectivity of \(p\); the stated form is the one we will use.

## 3. The general valuative criterion

**Theorem 3.1.** Let \(f:X\to S\) be quasi-separated and of finite type. Then \(f\) is proper if and only if every valuation diagram has exactly one extension.

**Proof.** A proper morphism is quasi-compact and universally closed, so Theorem 1.2 supplies existence. Its separatedness supplies uniqueness by the valuation lesson. Conversely, finite type includes quasi-compactness, so existence gives universal closedness. Quasi-separatedness and uniqueness give separatedness by the general separatedness criterion of that lesson. Finite type was already assumed. These are precisely the three properness conditions. \(\square\)

This is [Stacks, Tag 0BX5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-characterize-proper). Notice where quasi-separatedness enters: it is needed for the converse uniqueness criterion. Notice also that the valuation test alone does not impose finite type.

For a concrete failure of the latter inference, let \(L/k\) be an infinite algebraic field extension. The map \(\operatorname{Spec}L\to\operatorname{Spec}k\) is integral and separated, hence satisfies existence and uniqueness. It is not of finite type: a field generated by finitely many algebraic elements has finite degree. Thus it is not proper.

## 4. Projective space supplies limits

**Theorem 4.1.** For every scheme \(S\) and every \(n\geq0\), the projection \(\mathbf P^n_S\to S\) is proper.

**Proof.** Separatedness was proved using chart intersections in the diagonal lesson. The standard charts are affine spaces over the base, and there are \(n+1\) of them, so the morphism is of finite type. It remains to prove existence.

After pulling back a valuation diagram, the base is \(\operatorname{Spec}R\). A \(K\)-point of \(\mathbf P^n_R\) has homogeneous coordinates \([a_0:\cdots:a_n]\), not all zero. Among the nonzero coordinates choose \(a_j\) of least value in the totally ordered value group of \(R\). Then

\[
b_i=a_i/a_j\in R\quad\text{for every }i,
\qquad b_j=1.
\tag{4.1}
\]

Zero coordinates cause no problem. These ratios define a map into the standard chart \(D_+(T_j)\cong\mathbf A^n_R\), giving the required extension. Separatedness gives its uniqueness. Theorem 3.1 now proves properness. Since the argument works on every base change, it proves the assertion for arbitrary \(S\). \(\square\)

In a DVR one often multiplies the coordinates by a power of a uniformizer. Formula (4.1) is the version that also works when the valuation is not discrete and has higher rank: only the minimum of a finite set of values is used.

The same mechanism works for positive weights, although one must compare values after taking their degrees into account.

**Theorem 4.2 (finitely generated graded algebras).** Let \(G=\bigoplus_{d\geq0}G_d\) be a graded ring generated by finitely many homogeneous elements of positive degree as a \(G_0\)-algebra. Then \(\operatorname{Proj}G\to\operatorname{Spec}G_0\) is proper. In particular it satisfies both parts of the valuative criterion, without assuming that the generators have degree one.

**Proof.** Choose generators \(x_1,\ldots,x_m\) of degrees \(d_1,\ldots,d_m>0\). If there are none, Proj is empty and the assertion holds. Otherwise the \(D_+(x_j)\) form a finite cover. Each degree-zero chart ring \(G_{(x_j)}\) is a finite-type \(G_0\)-algebra. To verify this last point, write a degree-zero monomial with powers of \(x_j\) cancelled from its numerator. For every other exponent write \(e_i=q_i d_j+r_i\), with \(0\leq r_i<d_j\). Peel off the powers of \(x_i^{d_j}/x_j^{d_i}\). The remaining numerator has bounded exponents \(r_i\); its degree is divisible by \(d_j\), so its denominator is the corresponding integral power of \(x_j\). There are only finitely many such residual monomials. They and the displayed powers generate the chart ring. Thus Proj is of finite type; it is separated by the diagonal lesson.

Consider a valuation diagram and write \(v:K^*\to\Gamma\) for its value group. The generic point lands in some \(D_+(h)\), where \(h\) is homogeneous of degree \(e>0\). Let \(\varphi:G_{(h)}\to K\) be its ring map and put

\[
q_i=\varphi(x_i^e/h^{d_i}).
\]

At least one \(q_i\) is nonzero, since the \(D_+(x_i)\) cover Proj. Set \(D=\operatorname{lcm}(d_1,\ldots,d_m)\). Among the nonzero \(q_i\), choose \(q_j\) minimizing

\[
\gamma_i=(D/d_i)v(q_i).
\tag{4.2}
\]

The point lies in \(D_+(x_j)\), so it determines a map \(\psi:G_{(x_j)}\to K\). Every generating degree-zero monomial has the form

\[
M=\frac{\prod_i x_i^{a_i}}{x_j^b},
\qquad\sum_i a_i d_i=b d_j.
\]

If a factor with positive exponent has \(q_i=0\), its image under \(\psi\) is zero. Otherwise raising the monomial to the \(e\)-th power and using the degree equality gives

\[
De\,v(\psi(M))
=\sum_i a_i d_i\gamma_i-bd_j\gamma_j
\geq\left(\sum_i a_i d_i-bd_j\right)\gamma_j=0.
\tag{4.3}
\]

A totally ordered abelian group has no torsion and positive integer multiplication detects the sign. Hence \(v(\psi(M))\geq0\). The coefficients from \(G_0\) already map into \(R\), so the whole chart ring maps into \(R\). This defines an extension through \(D_+(x_j)\). Its generic restriction is the prescribed point, and uniqueness follows from separatedness. Theorem 3.1 finishes the proof. \(\square\)

The weighted valuative statement is [Stacks, Tag 01MF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-lemma-proj-valuative-criterion). The value comparison avoids dividing in \(\Gamma\), where division by degrees need not exist. Finite homogeneous generation is essential to the finite-type conclusion; arbitrary graded algebras need not produce proper morphisms.

## 5. Why discrete valuation rings suffice over a Noetherian base

**Theorem 5.1 (Noetherian valuative criterion).** Suppose \(S\) is locally Noetherian and \(f:X\to S\) is of finite type. Then \(f\) is proper if and only if every valuation diagram with \(R\) a DVR has exactly one extension.

We first record how schematic closures retain information that a reduced closure would discard. For a quasi-compact immersion \(U\to T\) into a Noetherian scheme, its **scheme-theoretic closure** is defined by

\[
\mathcal I=\ker(\mathcal O_T\to j_*\mathcal O_U).
\tag{5A.1}
\]

The ideal is quasi-coherent by the qcqs pushforward fact. Its closed subscheme has underlying space \(\overline{U}\), and \(U\) is open in it: inside an open where the immersion is closed, (5A.1) recovers that closed subscheme. The map from the closure's structure sheaf into \(j_*\mathcal O_U\) is injective. We call this **scheme-theoretic density** of \(U\). The construction commutes with restriction to opens, directly from (5A.1).

If two \(S\)-morphisms from such a closure to a scheme \(Q\) separated over \(S\) agree on \(U\), they agree everywhere. Their equalizer is the pullback of the closed relative diagonal \(\Delta_{Q/S}\), hence a closed subscheme; its defining ideal vanishes on \(U\), so injectivity of the structure-sheaf map makes that ideal zero. This is the version of the equalizer argument appropriate to possibly nonreduced schemes.

**Lemma 5.0 (Noetherian Chow construction).** Let \(S\) be Noetherian and \(X\to S\) separated and of finite type. There exist a proper surjection \(\pi:X'\to X\), a quasi-compact immersion \(X'\to\mathbf P^N_S\), and a dense open \(U\subset X\) such that \(\pi^{-1}(U)\to U\) is an isomorphism.

**Proof.** All schemes in the construction are Noetherian. The finitely many irreducible components of \(X\) have generic points \(\eta_1,\ldots,\eta_r\). Every point \(x\) has an affine neighbourhood containing all these generic points. Indeed, choose an affine neighbourhood \(W\) avoiding the components that do not contain \(x\); it contains the generic points of all components through \(x\). For each remaining component choose an affine neighbourhood of its generic point avoiding every other component. These extra opens are disjoint from \(W\) and from one another. Their finite disjoint union with \(W\) is affine and has the required points. Quasi-compactness now gives a finite affine cover \(U_1,\ldots,U_m\) with every generic point in every member. Their intersection \(U\) is dense and open.

Replace \(X\) temporarily by the scheme-theoretic closure \(X^*\) of \(U\) in \(X\). Its map to \(X\) is a surjective closed immersion and is an isomorphism on \(U\). The intersections \(U_i\cap X^*\) remain affine and cover it. Thus a solution for \(X^*\) gives one for \(X\), and we may assume \(U\) scheme-theoretically dense in \(X\).

Each affine \(U_i=\operatorname{Spec}B\) admits a quasi-compact immersion into a finite projective space over \(S\). Choose a finite principal cover \(D(f_a)\) of \(U_i\) such that each member maps into an affine \(S_a=\operatorname{Spec}A_a\subset S\). Each \(B_{f_a}\) is a finite-type \(A_a\)-algebra by the affine-chart finite-type theorem. Write a finite generating list as \(b_{aj}/f_a^{e_{aj}}\), with \(b_{aj}\in B\). Choose \(M_a\geq1\) at least all these exponents. Use, for every \(a\), the global functions
\[
f_a^{M_a},\quad f_a^{M_a-1},\quad
f_a^{M_a-e_{aj}}b_{aj}
\]
as one finite homogeneous coordinate tuple. They generate the unit ideal: no maximal ideal can contain all \(f_a^{M_a}\), because the \(D(f_a)\) cover. The projective-coordinate theorem in Projective space, relative Proj and maps to projective space, Theorem 1.1 therefore defines a map to \(\mathbf P^{n_i}_S\).

In the target chart for the coordinate \(f_a^{M_a}\), restricted over \(S_a\), the inverse image is precisely \(D(f_a)\). Its coordinate ratios include \(f_a^{-1}\) and every \(b_{aj}/f_a^{e_{aj}}\), so the homomorphism from that target affine chart to \(B_{f_a}\) is surjective. Thus the map is a closed immersion on every one of these charts. Their union is an open target neighbourhood of its whole image, since the \(D(f_a)\) cover its source. It is a closed immersion into that union and hence an immersion into the full projective space. Quasi-compactness follows from the finite source cover. This proof works with a nonaffine \(S\), arbitrary fields and nilpotents.

Let \(Z_i\subset\mathbf P^{n_i}_S\) be the scheme-theoretic closure of \(U_i\), so \(U_i\subset Z_i\) is a scheme-theoretically dense open. Each \(Z_i\) is proper over \(S\). The combined maps on \(U\) give an immersion

\[
U\longrightarrow\prod_{i=1}^m\mathbf P^{n_i}_S.
\]

It is an immersion because one component is an immersion and the remaining separated factors permit the closed-graph factorization. Let \(Z\) be its scheme-theoretic closure in this product. It is proper over \(S\), contains \(U\) as a scheme-theoretically dense open, and has projections \(p_i:Z\to Z_i\). The projections factor through \(Z_i\) because their defining ideals vanish on \(U\), hence on \(Z\) by schematic density. Each \(p_i\) is proper: it is a map from a proper \(S\)-scheme to a separated \(S\)-scheme.

Set \(V_i=p_i^{-1}(U_i)\), and \(X'=\bigcup_iV_i\subset Z\). The maps \(V_i\to U_i\subset X\) are proper over \(U_i\). On \(V_i\cap V_j\) these \(S\)-morphisms agree on \(U\). Pulling back the closed diagonal \(\Delta_{X/S}\), schematic density makes their equalizer the whole overlap. They glue to \(\pi:X'\to X\).

We verify that \(\pi^{-1}(U_i)=V_i\). There is an open inclusion \(V_i\subset\pi^{-1}(U_i)\) over \(U_i\). Its source is proper over \(U_i\), and its target is separated over \(U_i\): \(X'\) is separated over \(S\), so its morphism to \(X\) is separated by separatedness cancellation. Therefore the inclusion is proper and has closed image. It contains \(U\), which is dense in \(\pi^{-1}(U_i)\), so its image is the whole target. The two open subschemes are equal. Thus \(\pi\) is proper on the target cover \((U_i)\), hence proper globally. Its image on each \(U_i\) is closed and contains the dense \(U\); hence it is surjective.

The same argument, replacing \(V_i\to U_i\) by the identity \(U\to U\), proves \(\pi^{-1}(U)=U\). Finally \(X'\) is open in the closed subscheme \(Z\) of the product of projective spaces. The iterated Segre embedding places that product in a single finite projective space. Its full chart proof over an arbitrary base is in the prerequisite Projective space, relative Proj and maps to projective space, Section 2. Properness of projective space and its permanence properties have already been proved in Sections 2 and 4 here. Thus \(X'\) has the required immersion; it is quasi-compact because it is Noetherian. Compose with \(X^*\to X\) if the earlier replacement was necessary. Properness, surjectivity and the isomorphism on \(U\) are preserved. \(\square\)

This is [Stacks, Tag 0200](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-chow-Noetherian). The scheme-theoretic closure step is essential for nonreduced sources. Ordinary topological density alone would not make the maps on overlaps equal.


**Proof of Theorem 5.1.** Properness implies existence and uniqueness for all valuation rings, hence for DVRs. Assume conversely the DVR test. Properness is target-local, so restrict to an affine open of \(S\). Its inverse image is Noetherian because \(f\) is of finite type. The Noetherian separatedness criterion in the valuation lesson shows first that \(f\) is separated: every DVR diagram has at most one extension. We may therefore apply Lemma 5.0.

We claim that the immersion \(j:X'\to\mathbf P^N_S\) is closed. Otherwise its image has a point \(y\) in its closure outside the image. The Noetherian space \(X'\) has finitely many irreducible components, so \(y\) lies in the closure of the image of one of them. Give that closure its reduced structure and call it \(Z\). It is an integral Noetherian scheme; the component's generic point has residue field \(K=K(Z)\), and \(y\) is not its generic point. The local domain \(\mathcal O_{Z,y}\) is not a field. The full discrete-domination proof in Valuation rings and separatedness, Lemma 5.1, applies to \(\mathcal O_{Z,y}\). It gives a DVR \(R\subset K\), with fraction field exactly \(K\), dominating \(\mathcal O_{Z,y}\). It defines a map

\[
c:\operatorname{Spec}R\longrightarrow Z\longrightarrow\mathbf P^N_S
\]

whose closed point goes to \(y\), while its generic point has its specified lift \(u:\operatorname{Spec}K\to X'\).

Apply the assumed DVR existence test to \(pu:\operatorname{Spec}K\to X\) and the base map supplied by \(c\). It yields \(a:\operatorname{Spec}R\to X\). Since \(p\) is proper, the general existence criterion lifts this diagram to \(b:\operatorname{Spec}R\to X'\). The two \(S\)-maps \(jb\) and \(c\) into projective space agree on \(\operatorname{Spec}K\). Projective space is separated and \(\operatorname{Spec}R\) is integral, so the reduced-source uniqueness lemma gives \(jb=c\). Its closed point would then map both into \(j(X')\) and to \(y\), a contradiction.

An immersion with closed image is a closed immersion: near the image its closed-immersion descriptions give the ideal sheaf, and the open complement has empty inverse image. Thus \(j\) is closed. Theorem 4.1 and composition make \(X'\to S\) proper. Corollary 2.2 then makes \(X\to S\) universally closed. It is already separated and of finite type, hence proper. \(\square\)

The theorem and the boundary-point argument are [Stacks, Tag 0208](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-Noetherian-dvr-valuative-proper). Discrete domination uses the complete programme proof in Valuation rings and separatedness, Lemma 5.1, including the one-dimensional reduction, the full Krull–Akizuki length argument and the normal one-dimensional local-ring characterization proved there. This proof tests the boundary of a finite-type projective model; it does not assert that an arbitrary higher-rank valuation can itself be replaced by a DVR.

## 6. Missing limits, duplicated limits, and closed subspaces

**The affine line misses limits.** In \(\mathbf A^1_k\times_k\mathbf A^1_k\), with base coordinate \(x\) and other coordinate \(y\), the closed subscheme \(V(xy-1)\) has coordinate ring \(k[x,x^{-1}]\). Its image on the \(x\)-line is \(D(x)\), which is not closed. Thus \(\mathbf A^1_k\to\operatorname{Spec}k\) is not universally closed. The map itself is closed: its target has one point. Universal closedness detects the failure only after a base change.

The same failure appears in a DVR diagram. Take \(R=k[[t]]\), \(K=k((t))\), and the point with affine coordinate \(y=t^{-1}\). An extension would require a ring map \(k[y]\to R\) sending \(y\) to \(t^{-1}\), which is impossible.

**The doubled affine line duplicates some limits but still misses others.** Glue two copies of \(\mathbf A^1_k\) along \(D(z)\) by the identity. The generic point \(z=t\) extends through either chart over \(k[[t]]\), with distinct closed-point images at the two origins. This proves failure of uniqueness. However, \(z=t^{-1}\) has no extension. Any proposed extension has a closed-point image in one affine chart. The inverse image of that chart is an open neighbourhood of the closed point of a local spectrum and hence the whole spectrum. It would supply the impossible ring map just described. Therefore the doubled affine line is not an example of existence in every diagram.

**A doubled projective line has existence without uniqueness.** Instead glue two copies of \(\mathbf P^1_k\) along \(\mathbf P^1_k\setminus\{0\}\) by the identity, retaining distinct origins \(0_1,0_2\). Every field-valued point lies in one copy of \(\mathbf P^1\), and its valuation diagram extends in that copy by Theorem 4.1. Thus existence holds for every valuation ring. The generic point with local coordinate \(z=t\) again has two extensions, one to each origin. The scheme is quasi-compact and of finite type, and so Theorem 1.2 makes its structure map universally closed. It fails separatedness and therefore fails properness.

**Closed subspaces of projective space keep limits.** If \(Z\hookrightarrow\mathbf P^n_S\) is any closed immersion, then \(Z\to S\) is proper by Theorem 2.1. Alternatively, extend a generic point in projective space. Every local equation of \(Z\) vanishes in \(K\), and hence in \(R\subset K\); the extension factors through \(Z\). This works even when the defining ideal is not of finite type.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Show that \(\mathbf A^1_k\to\operatorname{Spec}k\) is closed but not universally closed. Identify a specialization that fails to lift in a base change.

**Solution.** Every subset image in the one-point target is closed. Base change by \(\mathbf A^1_k\) gives the projection of the affine plane to the \(x\)-line. The closed hyperbola \(H=V(xy-1)\) maps to \(D(x)\). Its generic point maps to the generic point of the line, which specializes to the origin; \(H\) has no point over that origin. Equivalently, the image \(D(x)\) contains the generic point but omits one of its specializations. If the plane projection were closed, the image of \(H\) would be closed. Hence the original line map is not universally closed. This does not contradict the fact that specializations can lift along the plane projection itself: the obstruction is a specialization that must stay inside the specified closed subset \(H\).

**Exercise 7.2 (easy).** Prove that every closed subscheme \(Z\subset\mathbf P^n_S\) is proper over \(S\). Explain why no coherence assumption on its ideal is required.

**Solution.** Its inclusion is a closed immersion, hence separated, universally closed, and of finite type. The finite-type assertion follows on affine charts from the quotient map \(A\to A/I\): the target is generated as an \(A\)-algebra without adjoining any elements, regardless of the size of \(I\). The projective-space map is proper by Theorem 4.1. Composition proves the assertion. Finite presentation of the inclusion would require local finite generation of \(I\), but properness uses finite type, so that stronger requirement is unnecessary.

**Exercise 7.3 (medium).** Let \(R\) be any valuation ring with fraction field \(K\). Extend a point \([a_0:\cdots:a_n]\in\mathbf P^n(K)\) to \(\mathbf P^n(R)\), and prove uniqueness. Do not assume that \(R\) has a uniformizer.

**Solution.** Choose a nonzero coordinate \(a_j\) of least value among the finitely many nonzero coordinates. For each \(i\), the ratio \(b_i=a_i/a_j\) belongs to \(R\), and \(b_j=1\). The tuple defines a surjection \(R^{n+1}\to R\) and, concretely, the chart map \(R[T_i/T_j]_{i\ne j}\to R\) with ratios \(b_i\). It gives the desired extension over \(\operatorname{Spec}R\). Choosing a different minimum coordinate produces a tuple differing by a unit, because the ratio of two equal-value coordinates is a unit of \(R\); hence the corresponding chart maps glue to the same point. More generally any two extensions agree on the generic point. Their equalizer is closed because projective space is separated, and it contains the schematically dense generic point of the integral scheme \(\operatorname{Spec}R\). They are therefore equal, by the reduced-source lemma. This also covers possible extensions described in different charts.

**Exercise 7.4 (medium).** Let \(X\xrightarrow fY\xrightarrow gS\) have \(gf\) proper and \(g\) separated. Prove that \(f\) is proper, without assuming that \(g\) is of finite type.

**Solution.** The graph is the pullback of \(\Delta_g:Y\to Y\times_S Y\) along the map \(X\times_S Y\to Y\times_S Y\) given by \((x,y)\mapsto(f(x),y)\). Thus \(\Gamma_f:X\to X\times_S Y\) is a closed immersion. The projection to \(Y\) is the base change of \(gf:X\to S\), hence proper. Their composite is \(f\). Closed immersions and compositions are proper, so the assertion follows. This proof establishes finite type of \(f\) as part of properness and does not try to infer finite type of \(g\).

**Exercise 7.5 (medium).** If \(X\to S\) is proper and \(Y\to S\) is separated, prove that every \(S\)-morphism \(h:X\to Y\) is proper and has closed image. Show also that the image remains closed after arbitrary base change on \(Y\).

**Solution.** Apply Exercise 7.4 to \(X\xrightarrow hY\to S\). The composite is the proper structure map of \(X\), and the second map is separated. Hence \(h\) is proper, in particular universally closed. For any \(Y'\to Y\), the base change \(X\times_Y Y'\to Y'\) is proper and closed. Its full source is a closed subset of itself, so its image is closed. Taking \(Y'=Y\) gives the original assertion. Moreover this image is the inverse image of \(h(X)\) as a set: a point over \(h(x)\) has a nonempty fibre after residue-field extension, by the nonzero field tensor-product argument in Corollary 2.2.

## References and proof providers

The Stacks project, read in the AI Integrated Stacks Project edition, supplies the exact tagged treatments of universal closedness, properness permanence, general valuative criteria, weighted Proj, and the Noetherian DVR criterion cited above. The complete Noetherian Chow construction needed by Theorem 5.1 is proved here in Lemma 5.0; Tag 0200 identifies a free comparison source. Discrete domination uses the complete programme proof in Valuation rings and separatedness, Lemma 5.1, including the one-dimensional reduction, the full Krull–Akizuki length argument and the normal one-dimensional local-ring characterization proved there. These linked works retain GNU FDL 1.2. No source text is reproduced here.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §§11.4 and 13.7, was consulted for alternative exposition of properness and valuation diagrams. Its expression is not reproduced. All four assigned result groups and all five exercises have their proofs here or in the precisely named prerequisite programme lessons. External references provide freely accessible comparison material.
