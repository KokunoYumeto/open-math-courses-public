# The Riemann existence theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that for every scheme \(X\) locally of finite type over \(\mathbf C\), the functor \(Y\mapsto Y(\mathbf C)\) from finite étale covers of \(X\) to finite coverings of \(X(\mathbf C)\) is an equivalence of categories. Two steps are proved in earlier lessons of the course: the functor is fully faithful for every \(X\) ([Connectedness and full faithfulness](connectedness-and-full-faithfulness.md)), and essentially surjective for smooth \(X\) ([Covers of smooth varieties](covers-of-smooth-varieties.md)). For a singular \(X\) we pull a covering back to the resolution \(R(X)\), which is smooth, find a finite étale cover there, and bring it down to \(X\) by descent along the proper surjective morphism \(R(X)\to X\). The last sections translate the theorem into a statement about fundamental groups and work out examples.

We use [Finite étale covers and their analytification](finite-etale-covers-and-their-analytification.md), [Connectedness and full faithfulness](connectedness-and-full-faithfulness.md), [Covers of smooth varieties](covers-of-smooth-varieties.md), [Descent along proper surjective morphisms](descent-along-proper-surjective-morphisms.md), [Principalization and resolution](course:resolution-of-singularities-in-characteristic-zero/principalization-and-resolution#4-resolution-of-singularities) from the course on resolution of singularities, and, for fundamental groups, the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) and the chapter on fundamental groups of schemes of the Stacks project. Throughout, \(\Phi_X:\operatorname{F\acute Et}(X)\to\operatorname{Cov}(X(\mathbf C))\) denotes the functor \(Y\mapsto Y(\mathbf C)\) of the first lesson.

## 1. Separated schemes and projective morphisms

The descent of coverings in the previous lesson needs a proper map between locally compact Hausdorff spaces. We check that the resolution of an affine scheme provides one.

**Lemma 1.1.** Let \(X\) be a scheme locally of finite type over \(\mathbf C\).

1. If \(i:Z\to X\) is a closed immersion, then \(i(\mathbf C)\) is a homeomorphism of \(Z(\mathbf C)\) onto a closed subset of \(X(\mathbf C)\).
2. If \(X\) is separated, then \(X(\mathbf C)\) is Hausdorff.
3. The space \(\mathbf P^N(\mathbf C)\) is compact and Hausdorff.

**Proof.** (1) Let \(U\subset X\) be an affine open subset with a closed immersion \(U\to\mathbf A^n\). Then \(Z\cap U=i^{-1}(U)\) is an affine open subset of \(Z\), and the composite \(Z\cap U\to U\to\mathbf A^n\) is a closed immersion. By Definition 1.1 and Lemma 1.2(1) of [the first lesson](finite-etale-covers-and-their-analytification.md#1-the-space-of-complex-points), \((Z\cap U)(\mathbf C)\) carries the subspace topology of \(U(\mathbf C)\subset\mathbf C^n\), and it is the set of common zeros in \(U(\mathbf C)\) of generators of the ideal of \(Z\cap U\), so it is closed in \(U(\mathbf C)\). The sets \(U(\mathbf C)\) form an open cover of \(X(\mathbf C)\), and the sets \((Z\cap U)(\mathbf C)\) an open cover of \(Z(\mathbf C)\) (Lemma 1.2(3) there). Hence \(i(\mathbf C)\) is a homeomorphism onto a closed subset.

(2) The diagonal \(X\to X\times_{\mathbf C}X\) is a closed immersion. By Lemma 1.2(6) of the first lesson, applied over \(\operatorname{Spec}\mathbf C\), whose space of complex points is a single point, \((X\times_{\mathbf C}X)(\mathbf C)\) is \(X(\mathbf C)\times X(\mathbf C)\) with the product topology. By (1) the diagonal of \(X(\mathbf C)\) is closed in it, and a space whose diagonal is closed in its square is Hausdorff.

(3) The scheme \(\mathbf P^N\) is separated ([Stacks, Tag 01NH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-lemma-projective-space-separated)), so \(\mathbf P^N(\mathbf C)\) is Hausdorff by (2). The standard open subset \(U_i=D_+(x_i)\) is the affine space with coordinates \(x_j/x_i\), \(j\ne i\). The map \(\mathbf C^{N+1}\setminus\{0\}\to\mathbf P^N(\mathbf C)\), \(x\mapsto[x_0:\cdots:x_N]\), is continuous, because on the open set \(\{x_i\ne0\}\) it is \(x\mapsto(x_j/x_i)_{j\ne i}\in\mathbf C^N=U_i(\mathbf C)\). Its restriction to the unit sphere of \(\mathbf C^{N+1}\) is surjective, and the sphere is compact, so \(\mathbf P^N(\mathbf C)\) is compact. \(\square\)

**Lemma 1.2 (projective morphisms are proper on complex points).** Let \(g:X'\to X\) be a projective morphism of schemes of finite type over \(\mathbf C\), with \(X\) affine. Then the inverse image under \(g(\mathbf C)\) of every compact subset of \(X(\mathbf C)\) is compact, and \(g(\mathbf C)\) is a closed map.

**Proof.** Since \(X\) is affine, \(\mathcal O_X\) is an ample invertible sheaf, so \(g\) factors as a closed immersion \(X'\to\mathbf P^N_X\) followed by the projection ([Stacks, Tag 087S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-projective-over-quasi-projective-is-H-projective)). As \(\mathbf P^N_X=\mathbf P^N\times_{\mathbf C}X\), Lemma 1.2(6) of the first lesson identifies \(\mathbf P^N_X(\mathbf C)\) with \(\mathbf P^N(\mathbf C)\times X(\mathbf C)\), with the product topology, and \(g(\mathbf C)\) with the restriction of the second projection; by Lemma 1.1(1), \(X'(\mathbf C)\) is a closed subset. For a compact \(K\subset X(\mathbf C)\), the set \(g(\mathbf C)^{-1}(K)=X'(\mathbf C)\cap(\mathbf P^N(\mathbf C)\times K)\) is closed in the compact space \(\mathbf P^N(\mathbf C)\times K\), hence compact.

The space \(X(\mathbf C)\) is Hausdorff and locally compact, by Lemma 1.2(3) of the first lesson. Let \(F\subset X'(\mathbf C)\) be closed and \(y\notin g(F)\), and let \(K\) be a compact neighbourhood of \(y\). Then \(g(F)\cap K=g\bigl(F\cap g(\mathbf C)^{-1}(K)\bigr)\) is compact, hence closed, and the interior of \(K\) minus this set is an open neighbourhood of \(y\) disjoint from \(g(F)\). So \(g(F)\) is closed. \(\square\)

## 2. The theorem

**Theorem 2.1 (Riemann existence theorem).** Let \(X\) be a scheme locally of finite type over \(\mathbf C\). The functor \(\Phi_X:\operatorname{F\acute Et}(X)\to\operatorname{Cov}(X(\mathbf C))\), \(Y\mapsto Y(\mathbf C)\), is an equivalence of categories.

**Proof.** *Reductions.* The functor is fully faithful by [Connectedness and full faithfulness, Corollary 3.1](connectedness-and-full-faithfulness.md#3-full-faithfulness). Essential surjectivity is local on \(X\), by Proposition 3.2 of the same lesson, so we may assume \(X\) affine. By [Finite étale covers and their analytification, Proposition 4.1](finite-etale-covers-and-their-analytification.md#4-nonreduced-schemes) we may replace \(X\) by \(X_{\rm red}\). So let \(X\) be a reduced affine scheme of finite type over \(\mathbf C\), and let \(p:E\to X(\mathbf C)\) be a finite covering.

*The resolution.* Let \(g=\rho_X:S'=R(X)\to X\) be the resolution of [Principalization and resolution, Theorem 4.8](course:resolution-of-singularities-in-characteristic-zero/principalization-and-resolution#4-resolution-of-singularities). The scheme \(S'\) is smooth of finite type over \(\mathbf C\). Since \(X\) is affine, it embeds into an affine space, so \(g\) is projective by part (4) of that theorem; in particular \(S'\) is separated. The image of \(g\) is closed and contains the smooth locus, which is dense because \(X\) is reduced; so \(g\) is surjective. Every closed point of \(X\) has a nonempty fibre, a scheme of finite type over \(\mathbf C\), which has a closed point; that point is closed in \(S'\). Hence \(g(\mathbf C)\) is surjective. By Lemmas 1.1 and 1.2, \(g(\mathbf C):S'(\mathbf C)\to X(\mathbf C)\) is a proper surjective continuous map of locally compact Hausdorff spaces.

Put \(S''=S'\times_XS'\) and \(S'''=S'\times_XS'\times_XS'\), with projections \(p_1,p_2:S''\to S'\) and \(p_{12},p_{13},p_{23}:S'''\to S''\). These schemes are of finite type over \(\mathbf C\), but in general not smooth. By Lemma 1.2(6) of the first lesson, \(S''(\mathbf C)=S'(\mathbf C)\times_{X(\mathbf C)}S'(\mathbf C)\) and \(S'''(\mathbf C)\) is the triple fibre product, compatibly with the projections; and for every finite étale \(Z\to S'\), \((p_i^*Z)(\mathbf C)=p_i(\mathbf C)^*\bigl(Z(\mathbf C)\bigr)\), and similarly over \(S'''\). In other words, \(\Phi\) commutes with these pull-backs.

*Step 1: a cover upstairs.* The pull-back \(E'=S'(\mathbf C)\times_{X(\mathbf C)}E\) is a finite covering of \(S'(\mathbf C)\). By [Covers of smooth varieties, Corollary 2.2](covers-of-smooth-varieties.md#2-the-smooth-quasi-projective-case) there are a finite étale \(Y'\to S'\) and an isomorphism of coverings \(\beta:Y'(\mathbf C)\to E'\).

*Step 2: a descent datum.* The covering \(p_i^*E'\) of \(S''(\mathbf C)\) consists of the pairs \(\bigl((s_1,s_2),(s_i,e)\bigr)\) with \(g(s_i)=p(e)\). Since \(g(s_1)=g(s_2)\), the map

\[
c_E:p_1^*E'\longrightarrow p_2^*E',\qquad \bigl((s_1,s_2),(s_1,e)\bigr)\longmapsto\bigl((s_1,s_2),(s_2,e)\bigr),
\]

is an isomorphism of coverings of \(S''(\mathbf C)\). Over \(S'''(\mathbf C)\) both \(p_{13}^*c_E\) and \(p_{23}^*c_E\circ p_{12}^*c_E\) send \(\bigl((s_1,s_2,s_3),(s_1,e)\bigr)\) to \(\bigl((s_1,s_2,s_3),(s_3,e)\bigr)\), so they are equal. Now consider the isomorphism of coverings of \(S''(\mathbf C)\)

\[
\theta=(p_2^*\beta)^{-1}\circ c_E\circ p_1^*\beta:\ (p_1^*Y')(\mathbf C)\longrightarrow(p_2^*Y')(\mathbf C).
\]

By full faithfulness of \(\Phi_{S''}\) (Corollary 3.1 of the second lesson, which holds for every scheme locally of finite type over \(\mathbf C\)), \(\theta=\Phi(\varphi)\) for a unique isomorphism \(\varphi:p_1^*Y'\to p_2^*Y'\) over \(S''\). In the composite \(p_{23}^*\theta\circ p_{12}^*\theta\) the middle factors of \(\beta\) cancel, so the cocycle identity for \(c_E\) gives \(p_{13}^*\theta=p_{23}^*\theta\circ p_{12}^*\theta\). Since \(\Phi\) commutes with pull-back, this says \(\Phi(p_{13}^*\varphi)=\Phi(p_{23}^*\varphi\circ p_{12}^*\varphi)\), and faithfulness of \(\Phi_{S'''}\) gives \(p_{13}^*\varphi=p_{23}^*\varphi\circ p_{12}^*\varphi\). So \((Y',\varphi)\) is a descent datum relative to \(g\).

*Step 3: descent.* The scheme \(X\) is noetherian and \(g\) is proper and surjective. By [Descent along proper surjective morphisms, Theorem 3.4](descent-along-proper-surjective-morphisms.md#3-reduction-to-a-henselian-base) there are a finite étale \(Y\to X\) and an isomorphism \(\psi:g^*Y\to Y'\) compatible with the descent data:

\[
\varphi\circ p_1^*\psi=p_2^*\psi\circ\mathrm{can}_Y,
\]

where \(\mathrm{can}_Y:p_1^*g^*Y\to p_2^*g^*Y\) identifies both sides with the pull-back of \(Y\) to \(S''\).

*Step 4: comparison.* Let \(\alpha'=\beta\circ\Phi(\psi):g(\mathbf C)^*\bigl(Y(\mathbf C)\bigr)\to E'=g(\mathbf C)^*E\), an isomorphism of coverings of \(S'(\mathbf C)\). On complex points, \(\mathrm{can}_Y\) becomes the map \(c_{Y(\mathbf C)}\) defined by the same formula as \(c_E\). Applying \(\Phi_{S''}\) to the compatibility of \(\psi\) and substituting \(\Phi(\varphi)=\theta\) gives

\[
(p_2^*\beta)^{-1}\circ c_E\circ p_1^*\beta\circ p_1^*\Phi(\psi)=p_2^*\Phi(\psi)\circ c_{Y(\mathbf C)},\qquad\text{that is,}\qquad c_E\circ p_1^*\alpha'=p_2^*\alpha'\circ c_{Y(\mathbf C)}.
\]

So the two pull-backs of \(\alpha'\) to \(S''(\mathbf C)\) agree under the canonical identifications. By [Descent along proper surjective morphisms, Proposition 4.1](descent-along-proper-surjective-morphisms.md#4-covering-spaces), applied to the proper surjective map \(g(\mathbf C)\) and the coverings \(Y(\mathbf C)\) and \(E\), there is an isomorphism \(\alpha:Y(\mathbf C)\to E\) over \(X(\mathbf C)\) with \(g(\mathbf C)^*\alpha=\alpha'\). Thus \(E\) is isomorphic to \(\Phi_X(Y)\). \(\square\)

**Remark 2.2.** The proof shows more generally: if \(g:S'\to S\) is a projective surjective morphism of schemes of finite type over \(\mathbf C\) with \(S\) affine, and every finite covering of \(S'(\mathbf C)\) comes from a finite étale cover of \(S'\), then the same holds for \(S\). Grothendieck's proof in SGA 1 first descends along the normalization, which reduces the theorem to normal schemes, and then extends covers across subsets of codimension at least two. The proof above uses resolution to reduce the theorem to smooth schemes in one step. Example 5.3 of the first lesson shows why some descent step is unavoidable: finite étale covers of a nonnormal scheme are not normal.

The theorem has an analytic form. For a variety \(X\), let \(\operatorname{F\acute Et}(X^{\rm an})\) be the category of analytic spaces \(E\) with a morphism \(p:E\to X^{\rm an}\) that is a local isomorphism of analytic spaces and whose underlying map is a finite covering, with morphisms over \(X^{\rm an}\); analytic spaces are as in [Complex analytic spaces and analytification](course:AG-QC/complex-analytic-spaces-and-analytification).

**Corollary 2.3 (analytic form).** Let \(X\) be a variety. The functor \(Y\mapsto Y^{\rm an}\) is an equivalence \(\operatorname{F\acute Et}(X)\to\operatorname{F\acute Et}(X^{\rm an})\).

**Proof.** The degree of a finite étale \(q:Y\to X\) is locally constant, so \(X\) is the disjoint union of open and closed subvarieties over which it is constant. By [Finite étale covers and their analytification, Proposition 3.1](finite-etale-covers-and-their-analytification.md#3-the-analytic-structure-of-a-cover) on each of them, \(q^{\rm an}\) is a local isomorphism, and its underlying map \(Y(\mathbf C)\to X(\mathbf C)\) is a finite covering. So the functor is defined.

Forgetting the analytic structure is an equivalence \(\operatorname{F\acute Et}(X^{\rm an})\to\operatorname{Cov}(X(\mathbf C))\). Indeed, for a finite covering \(p:E\to X(\mathbf C)\), the sheaf \(p^{-1}\mathcal O_{X^{\rm an}}\) makes \(E\) an analytic space for which \(p\) is a local isomorphism: over an open set \(O\subset E\) that \(p\) maps homeomorphically onto an open \(W\), the ringed space \((O,p^{-1}\mathcal O_{X^{\rm an}}|_O)\) is isomorphic to \((W,\mathcal O_{X^{\rm an}}|_W)\). If \(\mathcal O_E\) is any structure for which \(p\) is a local isomorphism, then \(p^\#:p^{-1}\mathcal O_{X^{\rm an}}\to\mathcal O_E\) is an isomorphism, because it is one over each such \(O\). For a continuous map \(f:E_1\to E_2\) over \(X(\mathbf C)\), we have \(f^{-1}p_2^{-1}\mathcal O_{X^{\rm an}}=p_1^{-1}\mathcal O_{X^{\rm an}}\), which makes \(f\) a morphism of analytic spaces over \(X^{\rm an}\), and it is the only one with underlying map \(f\), since its comorphism must be compatible with the isomorphisms \(p_1^\#\) and \(p_2^\#\). The composite of \(Y\mapsto Y^{\rm an}\) with the forgetful functor is \(\Phi_X\), because \(Y^{\rm an}\) has underlying space \(Y(\mathbf C)\) (Lemma 1.2(4) of the first lesson). Since \(\Phi_X\) is an equivalence by Theorem 2.1, so is \(Y\mapsto Y^{\rm an}\). \(\square\)

## 3. Fundamental groups

Let \(X\) be a connected scheme, \(\overline x\) a geometric point and \(F_{\overline x}:\operatorname{F\acute Et}(X)\to\mathrm{Sets}\), \(Y\mapsto|Y\times_X\overline x|\), the fibre functor. The pair \((\operatorname{F\acute Et}(X),F_{\overline x})\) is a Galois category ([Stacks, Tag 0BNB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-connected-galois-category); the axioms are in [Tag 0BMY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-definition-galois-category)). The *étale fundamental group* \(\pi_1(X,\overline x)\) is the group of automorphisms of \(F_{\overline x}\) ([Tag 0BNC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-definition-fundamental-group)). It is a profinite group, as a closed subgroup of \(\prod_Y\operatorname{Aut}(F_{\overline x}(Y))\) ([Tag 0BMR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-aut-inverse-limit)), and \(F_{\overline x}\) is an equivalence from \(\operatorname{F\acute Et}(X)\) to the category of finite sets with a continuous action of \(\pi_1(X,\overline x)\) ([Tag 0BND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-fundamental-group)). Under this equivalence the connected finite étale covers correspond to the transitive actions, and the automorphisms of a cover to the automorphisms of the corresponding finite set with its action.

Now let \(X\) be locally of finite type over \(\mathbf C\) and connected, \(x\in X(\mathbf C)\) a closed point, and \(\overline x:\operatorname{Spec}\mathbf C\to X\) the corresponding geometric point. For a finite étale \(q:Y\to X\), the scheme \(Y\times_X\overline x\) is the spectrum of a finite étale \(\mathbf C\)-algebra, a finite disjoint union of copies of \(\operatorname{Spec}\mathbf C\), whose points are the complex points of \(Y\) over \(x\). So

\[
F_{\overline x}=F_x\circ\Phi_X,\qquad F_x:\operatorname{Cov}(X(\mathbf C))\to\mathrm{Sets},\quad(E\xrightarrow{p}X(\mathbf C))\mapsto p^{-1}(x).
\]

**Theorem 3.1.** Let \(X\) be connected and locally of finite type over \(\mathbf C\), and \(x\in X(\mathbf C)\). Then \((\operatorname{Cov}(X(\mathbf C)),F_x)\) is a Galois category, and restriction along \(\Phi_X\) is an isomorphism of profinite groups

\[
\operatorname{Aut}(F_x)\longrightarrow\operatorname{Aut}(F_x\circ\Phi_X)=\pi_1(X,\overline x),\qquad u\longmapsto u\Phi_X .
\]

**Proof.** By Theorem 2.1, \(\Phi_X\) is an equivalence. Composition with an equivalence is an equivalence of functor categories, so it induces a bijection on automorphism groups of functors, which is a group isomorphism. The topologies of Tag 0BMR are defined by the actions on the finite sets \(F_x(E)\) and \(F_{\overline x}(Y)\), and these sets correspond, because every covering is isomorphic to some \(\Phi_X(Y)\). So the isomorphism is a homeomorphism. The axioms of a Galois category are stated in terms of finite limits and colimits, connected objects, and properties of the functor, all of which are preserved by an equivalence compatible with the functors. \(\square\)

To compare with the topological fundamental group we need the classification of covering spaces. In the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), a space is *semilocally simply connected* if every point has a basis of open neighbourhoods \(N\) that are path-connected and such that any two paths in \(N\) with the same end points are homotopic in the whole space relative to their end points (Definition 6.2). Every manifold has this property (Example 6.2). For such a space, the monodromy functor from coverings to functors on the fundamental groupoid is an equivalence of categories (Theorem 17.1).

**Theorem 3.2 (comparison of fundamental groups).** Let \(X\) be connected and locally of finite type over \(\mathbf C\), and \(x\in X(\mathbf C)\). Assume that \(X(\mathbf C)\) is semilocally simply connected; this holds if \(X\) is smooth. Then the monodromy action of \(\pi_1(X(\mathbf C),x)\) on the fibres \(q(\mathbf C)^{-1}(x)\) of finite étale covers \(q:Y\to X\) induces an isomorphism of profinite groups

\[
\pi_1(X(\mathbf C),x)^\wedge\longrightarrow\pi_1(X,\overline x)
\]

from the profinite completion of the topological fundamental group.

**Proof.** The space \(M=X(\mathbf C)\) is connected by [Connectedness and full faithfulness, Theorem 2.1](connectedness-and-full-faithfulness.md#2-open-and-closed-subsets). By hypothesis it has a basis of path-connected open sets, so its path components are open; being connected, \(M\) is path-connected. Let \(G=\pi_1(M,x)\). By Theorem 17.1 of the core course, the monodromy functor is an equivalence from coverings of \(M\) to functors on the fundamental groupoid of \(M\), and since \(M\) is path-connected, evaluation at \(x\) is an equivalence from such functors to sets with an action of \(G\). The composite sends a covering to its fibre over \(x\) with the monodromy action. A covering of the connected space \(M\) has fibres of constant cardinality, so finite coverings correspond to finite \(G\)-sets, and we obtain an equivalence \(\operatorname{Cov}(M)\to\textit{Finite-}G\textit{-Sets}\) under which \(F_x\) becomes the forgetful functor. (If loops are made to act on fibres from the right, replace each action by the left action through \(g\mapsto g^{-1}\).) The automorphism group of the forgetful functor on finite \(G\)-sets, for the discrete group \(G\), is the profinite completion \(G^\wedge\) ([Stacks, Tag 0BMU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-single-out-profinite)). So \(\operatorname{Aut}(F_x)\cong G^\wedge\), and Theorem 3.1 gives the isomorphism with \(\pi_1(X,\overline x)\). It sends the class of a loop \(\gamma\) to the automorphism of \(F_{\overline x}\) that acts on each fibre \(q(\mathbf C)^{-1}(x)\) by monodromy along \(\gamma\).

If \(X\) is smooth, then by [Connectedness and full faithfulness, Lemma 1.1](connectedness-and-full-faithfulness.md#1-smooth-points-and-divisors-with-normal-crossings) every point of \(X(\mathbf C)\) has an open neighbourhood homeomorphic to an open subset of \(\mathbf C^n\). Small balls in these charts are convex, so straight-line homotopies show that \(X(\mathbf C)\) is semilocally simply connected, as in Example 6.2 of the core course. \(\square\)

**Remark 3.3.** For a singular \(X\) the space \(X(\mathbf C)\) is also semilocally simply connected: it is locally contractible, because the set of complex points of an affine scheme of finite type is a real semi-algebraic subset of some \(\mathbf R^{2n}\), and such sets can be triangulated (Łojasiewicz). Hence Theorem 3.2 holds for every connected \(X\) locally of finite type over \(\mathbf C\). The triangulation theorem is not proved in this collection, and nothing else in the course depends on this remark. Theorem 3.1 holds without any hypothesis on \(X(\mathbf C)\).

## 4. Examples

**Example 4.1 (affine space has no nontrivial covers).** The space \(\mathbf C^n\) is convex, so every loop is homotopic to a constant loop by a straight-line homotopy, and \(\pi_1(\mathbf C^n,0)\) is trivial. By Theorem 3.2, \(\pi_1(\mathbf A^n_{\mathbf C},\overline 0)\) is trivial. Under the equivalence of Tag 0BND, finite sets with the trivial action correspond to trivial covers, so every finite étale cover of \(\mathbf A^n_{\mathbf C}\) is a finite disjoint union of copies of \(\mathbf A^n_{\mathbf C}\). This purely algebraic statement fails in positive characteristic (Exercise 5.1).

**Example 4.2 (the multiplicative group).** The map \((t,s)\mapsto\bigl((1-s)+s/|t|\bigr)t\) deformation retracts \(\mathbf C^*\) onto the unit circle, so \(\pi_1(\mathbf C^*,1)\cong\mathbf Z\) by Theorem 10.1 of the core course. By Theorem 3.2, \(\pi_1(\mathbf G_m,\overline 1)\) is the profinite completion \(\widehat{\mathbf Z}=\lim_n\mathbf Z/n\mathbf Z\). The group \(\mathbf Z\) has exactly one subgroup of index \(n\), and it is normal with quotient \(\mathbf Z/n\mathbf Z\). Hence \(\mathbf G_m\) has, up to isomorphism, exactly one connected finite étale cover of degree \(n\). It is the cover \(w\mapsto w^n\) of [Example 5.1 of the first lesson](finite-etale-covers-and-their-analytification.md#5-examples), whose automorphism group is \(\mu_n\), acting by \(w\mapsto\zeta w\).

**Example 4.3 (the line minus two points).** Let \(X=\mathbf A^1\setminus\{0,1\}\), so \(X(\mathbf C)=\mathbf C\setminus\{0,1\}\). Put \(U=\{\operatorname{Re}z<2/3\}\setminus\{0\}\) and \(V=\{\operatorname{Re}z>1/3\}\setminus\{1\}\). The intersection \(U\cap V\) is the strip \(1/3<\operatorname{Re}z<2/3\), which is convex, hence simply connected. The half-plane \(\{\operatorname{Re}z<2/3\}\) is convex and contains \(0\), so moving each point of \(U\) along its ray from \(0\) onto the circle of radius \(1/3\) about \(0\) is a deformation retraction of \(U\) onto that circle, and \(\pi_1(U)\cong\mathbf Z\); likewise \(\pi_1(V)\cong\mathbf Z\). By the Seifert–van Kampen theorem (Corollary 12.1 of the core course), \(\pi_1(\mathbf C\setminus\{0,1\})\) is the free product \(\mathbf Z*\mathbf Z\), the free group \(F_2\) on two generators. By Theorem 3.2, \(\pi_1(X,\overline x)\cong\widehat{F_2}\).

Consequently every finite group \(G\) generated by two elements is the automorphism group of a connected finite étale cover of \(X\) of degree \(|G|\) on which it acts simply transitively on fibres. Indeed, a surjection \(F_2\to G\) makes \(G\) a transitive finite \(F_2\)-set by left multiplication, which corresponds to a connected cover \(Y\); its automorphisms are the automorphisms of this \(F_2\)-set, namely the right multiplications by elements of \(G\).

**Example 4.4 (the nodal cubic).** Let \(X\) be the nodal cubic \(y^2=x^2(x+1)\) and \(\nu:\mathbf A^1\to X\) its normalization, \(t\mapsto(t^2-1,t(t^2-1))\), which identifies \(t=1\) and \(t=-1\) and is injective elsewhere. We show that \(X\) has, up to isomorphism, exactly one connected finite étale cover of each degree \(d\ge1\).

Let \(p:E\to X(\mathbf C)\) be a finite covering of degree \(d\). Its pull-back \(\nu(\mathbf C)^*E\) is a covering of \(\mathbf C\), which is simply connected and semilocally simply connected, so it is trivial by the classification theorem: choose an isomorphism \(\nu(\mathbf C)^*E\cong\mathbf C\times F\) with \(|F|=d\). The projection \(\mathbf C\times F\to E\) is surjective, and it is proper, being a base change of \(\nu(\mathbf C)\), which is proper because \(\nu\) is finite ([Lemma 2.1 of the first lesson](finite-etale-covers-and-their-analytification.md#2-finite-morphisms-and-étale-morphisms)). As \(E\) is Hausdorff and locally compact, the projection is closed, hence a quotient map. It is injective over \(\mathbf C\setminus\{\pm1\}\), and the fibre of \(E\) over the node is identified with \(F\) both through \(t=1\) and through \(t=-1\). Comparing the two identifications gives a permutation \(\sigma\) of \(F\), and

\[
E\cong(\mathbf C\times F)/\bigl((1,\phi)\sim(-1,\sigma(\phi))\bigr).
\]

A different trivialization changes \(\sigma\) to a conjugate, because two trivializations of a covering of the connected space \(\mathbf C\) differ by a constant permutation; conversely every \(\sigma\) occurs, and conjugate permutations give isomorphic coverings. The quotient is connected if and only if the powers of \(\sigma\) act transitively on \(F\), that is, if \(\sigma\) is a \(d\)-cycle, and all \(d\)-cycles are conjugate. So \(X(\mathbf C)\) has exactly one connected covering of degree \(d\). By Theorem 2.1 the same holds for finite étale covers of \(X\). The cover is the cycle of \(d\) copies of \(\mathbf A^1\) in which \(t=1\) on the \(k\)-th copy is identified with \(t=-1\) on the \((k+1)\)-st, indices modulo \(d\); for \(d=2\) it is the cover of Example 5.3 of the first lesson. Its automorphisms are the permutations of \(F\) commuting with \(\sigma\), the cyclic group generated by \(\sigma\), which acts simply transitively on \(F\).

Translated through Tag 0BND: \(\pi_1(X,\overline x)\) has exactly one open subgroup \(U_d\) of each index \(d\), it is normal, and \(\pi_1(X,\overline x)/U_d\) is cyclic of order \(d\). If \(d\) divides \(m\), the preimage of the subgroup of index \(d\) of the cyclic group \(\pi_1(X,\overline x)/U_m\) is an open subgroup of index \(d\), so \(U_m\subset U_d\). Every open normal subgroup is some \(U_d\), so \(\pi_1(X,\overline x)\) is the inverse limit of the cyclic groups \(\pi_1(X,\overline x)/U_d\) along surjections, ordered by divisibility. Choosing compatible generators, which is possible because each transition map \(\mathbf Z/m\to\mathbf Z/d\) is surjective and the sets of generators are finite and nonempty, identifies this limit with \(\widehat{\mathbf Z}=\lim_d\mathbf Z/d\mathbf Z\).

## 5. Exercises

**Exercise 5.1.** Let \(k\) be an algebraically closed field of characteristic \(p>0\). Show that \(Y=\operatorname{Spec}k[x,y]/(y^p-y-x)\to\mathbf A^1_k\) is a connected finite étale cover of degree \(p\). Conclude that Example 4.1 has no analogue in characteristic \(p\).

*Solution.* The algebra \(B=k[x][y]/(y^p-y-x)\) is free over \(k[x]\) with basis \(1,y,\ldots,y^{p-1}\), because the polynomial is monic of degree \(p\) in \(y\). Its derivative in \(y\) is \(py^{p-1}-1=-1\), a unit, so \(k[x]\to B\) is standard étale, hence étale ([Stacks, Tag 00UC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-etale)). Since \(x=y^p-y\) in \(B\), the map \(k[y]\to B\) is an isomorphism, so \(Y\cong\mathbf A^1_k\) is connected. A connected cover of degree \(p>1\) is not a disjoint union of copies of \(\mathbf A^1_k\).

**Exercise 5.2.** Show that the connected finite étale covers of degree \(2\) of \(\mathbf G_m\times\mathbf G_m\) over \(\mathbf C\) correspond to the subgroups of index \(2\) of \(\mathbf Z^2\), and find them.

*Solution.* By Lemma 2.2(1) of [Finite covers of punctured polydiscs](finite-covers-of-punctured-polydiscs.md#2-monodromy) and Example 4.2, \(\pi_1(\mathbf C^*\times\mathbf C^*)\cong\mathbf Z^2\), and the space is a manifold. By Theorem 3.2 and Tag 0BND, connected covers of degree \(2\) correspond to transitive \(\mathbf Z^2\)-sets with two elements, up to isomorphism, that is, to the subgroups of index \(2\), which are the stabilizers; conjugation is trivial because \(\mathbf Z^2\) is abelian. These are the kernels of the three nonzero homomorphisms \(\mathbf Z^2\to\mathbf Z/2\). The corresponding covers are \(w^2=z_1\), \(w^2=z_2\) and \(w^2=z_1z_2\): going once around \(z_1=0\) changes the sign of \(w\) for the first and third, and going around \(z_2=0\) for the second and third.

**Exercise 5.3.** Show that \(\mathbf A^1_{\mathbf C}\setminus\{0,1\}\) has a connected finite étale cover of degree \(6\) whose automorphism group is the symmetric group \(S_3\).

*Solution.* The group \(S_3\) is generated by the transposition \((12)\) and the \(3\)-cycle \((123)\), so there is a surjection \(F_2\to S_3\). Example 4.3 gives a connected cover of degree \(|S_3|=6\) with automorphism group \(S_3\).

**Exercise 5.4.** In the proof of Theorem 2.1, where is it used that \(X\) is affine and that the resolution is projective rather than merely proper?

*Solution.* Over an affine \(X\) the projective morphism \(g\) factors through \(\mathbf P^N_X\) (Tag 087S), and the compactness of \(\mathbf P^N(\mathbf C)\) makes \(g(\mathbf C)\) proper (Lemma 1.2). The affine \(X\) is also separated, so \(X(\mathbf C)\) and \(S'(\mathbf C)\) are Hausdorff. Both properties are needed to descend the isomorphism \(\alpha'\) by Proposition 4.1 of the previous lesson. The reduction to affine \(X\) is harmless, because existence is local by Proposition 3.2 of the second lesson.

## References

- [SGA 1] A. Grothendieck et al., *Revêtements étales et groupe fondamental (SGA 1)*, Exposé XII, Theorem 5.1 (the Riemann existence theorem) and Corollary 5.2 (fundamental groups), and Exposé V (Galois categories); free re-edition arXiv:math/0206203. The proof in this lesson descends along a resolution of singularities, where SGA 1 descends along the normalization and extends covers across subsets of codimension two. <https://arxiv.org/abs/math/0206203>
- [Łojasiewicz] S. Łojasiewicz, *Triangulation of semi-analytic sets*, Ann. Scuola Norm. Sup. Pisa (3) 18 (1964), 449–474, free from Numdam. <https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0/>
