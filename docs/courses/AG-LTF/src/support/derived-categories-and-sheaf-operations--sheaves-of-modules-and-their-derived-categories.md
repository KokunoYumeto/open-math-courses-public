# Sheaves of modules and their derived categories

*Written by Claude Opus 5.5 (Anthropic), September 2026. Spot-checked by Claude Opus 5.5 in a separate session. Public domain (CC0).*

This lesson sets up the homological algebra of sheaves of modules on a topological space, in the generality that microlocal sheaf theory needs. It shows that sheaves of left modules over any sheaf of rings, commutative or not, form an abelian category with exact filtered colimits, a generator and functorial injective embeddings. From this it obtains right derived functors, first on bounded-below complexes and then, through K-injective resolutions, on all complexes. For a commutative sheaf of rings it then treats K-flat resolutions, the derived tensor product, the adjunction between derived pullback and pushforward, the internal derived Hom and its composition map. It ends with the localization triangle for a locally closed set and a closed part of it, and with the two sign conventions for distinguished triangles that are in use.

Every result that needs no tensor product is proved for left modules over an arbitrary sheaf of rings, so it also applies to constant sheaves of noncommutative rings. The worked examples show which hypotheses cannot be dropped: an unbounded complex of injectives need not be K-injective, sections need not commute with infinite direct sums, products of sheaves need not be exact, and derived functors of bounded complexes need not be bounded.

The lesson assumes the basic language of sheaves on a topological space (sections, restriction maps, stalks and germs) and of homological algebra: abelian categories, complexes and their cohomology, the homotopy category, the derived category and triangulated categories. It has no prerequisite lessons. The facts it uses without proof are listed in Section 1, each with a reference.

Basic references are [Stacks] and the lessons of the course [*Derived categories and sheaf operations*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/), which treat these results in a reorganized form. Resolutions of unbounded complexes by K-injective and K-flat complexes go back to [Spaltenstein 1988].

## 1. Conventions and background

### Conventions

- \(X\) is a topological space. \(\mathcal O\) is a sheaf of rings on \(X\): associative, with \(1\), not necessarily commutative. \(\operatorname{Mod}(\mathcal O)\) is the category of sheaves of left \(\mathcal O\)-modules. For a ring \(A\), \(\operatorname{Mod}(A)\) is the category of left \(A\)-modules. When a result needs \(\mathcal O\) commutative we say so; then \((X,\mathcal O)\) is a ringed space.
- For a unital ring \(k\), \(k_X\) is the constant sheaf, and \(\operatorname{Mod}(k_X)\) is the category of sheaves of left \(k\)-modules. The ring \(k\) need not be commutative.
- \(F_x\) is the stalk at \(x\), a left module over the stalk ring \(\mathcal O_x\); \(s_x\) is the germ of a section \(s\). For an open \(j:U\hookrightarrow X\), \(j^{-1}\) is restriction, \(j_*\) is direct image, and \(j_!\) is extension by zero ([Lemma 5.2](#sh-fnd-dc-05)). \(x_*J\) is a skyscraper sheaf ([Lemma 5.3](#sh-fnd-dc-05)).
- Complexes are cohomological. The shift is \((K[1])^n=K^{n+1}\) with \(d_{K[1]}=-d_K\). The Hom complex is
\[
\operatorname{Hom}^n(K,L)=\prod_{p\in\mathbb Z}\operatorname{Hom}(K^p,L^{p+n}),\qquad df=d_L\circ f-(-1)^nf\circ d_K ,
\]
and the total complex of a tensor product has the differential \(d(a\otimes b)=da\otimes b+(-1)^{|a|}a\otimes db\).
- \(K(\mathcal A)\) is the homotopy category and \(D(\mathcal A)\) the derived category of an abelian category \(\mathcal A\). A complex is *acyclic* if all its cohomology vanishes. "Qis" means quasi-isomorphism.
- A complex \(I\) is *K-injective*, or *homotopically injective*, if \(\operatorname{Hom}_{K(\mathcal A)}(M,I)=0\) for every acyclic \(M\). For commutative \(\mathcal O\), a complex \(P\) of \(\mathcal O\)-modules is *K-flat* if \(\operatorname{Tot}(M\otimes_{\mathcal O}P)\) is acyclic for every acyclic \(M\).
- A sheaf \(F\) is *flabby* if \(F(X)\to F(V)\) is onto for every open \(V\). Then \(F(W)\to F(V)\) is onto for all opens \(V\subset W\), because \(F(X)\to F(V)\) factors through \(F(W)\).
- *Sections with support.* Let \(W\subset X\) be locally closed, and choose an open set \(\Omega\supset W\) in which \(W\) is closed. For a sheaf \(F\), the sheaf \(\Gamma_WF\) of sections supported in \(W\) is given by \((\Gamma_WF)(V)=\{s\in F(V\cap\Omega):\operatorname{supp}s\subset W\}\) for \(V\) open. It does not depend on \(\Omega\). The intersection of two choices is again a choice, so it is enough to compare \(\Omega\) with a choice \(\Omega'\subset\Omega\). A section over \(V\cap\Omega\) supported in \(W\) vanishes on the open set \(V\cap(\Omega\setminus W)\), and \(V\cap\Omega\) is covered by \(V\cap\Omega'\) and \(V\cap(\Omega\setminus W)\); so restriction to \(V\cap\Omega'\) is injective on such sections. A section over \(V\cap\Omega'\) supported in \(W\) glues with \(0\) on \(V\cap(\Omega\setminus W)\); so restriction is also onto. For closed \(W\) one can take \(\Omega=X\). For open \(W=U\) one can take \(\Omega=U\), so \(\Gamma_U=j_*j^{-1}\) for \(j:U\hookrightarrow X\).

### Background used without proof

The following standard facts are used without proof. A few further results that are needed in one section only are stated there, each followed by a reference: part (4) of Theorem 4.1; parts (1), (3) and (4) of Theorem 6.1; and, for commutative \(\mathcal O\), Theorems 8.1, 9.1, 10.1, 11.1 and 12.1, with the facts (a)–(c) of Section 8.

*Sheaves and modules.*

- **(S) Sheafification.** For a presheaf \(P\) of left \(\mathcal O\)-modules there are a sheaf \(P^+\) of left \(\mathcal O\)-modules and a map \(\theta:P\to P^+\) such that every map from \(P\) to a sheaf factors uniquely through \(\theta\), and \(\theta\) is bijective on stalks. Two consequences are used often. Every section of \(P^+\) is, near each point, the image of a section of \(P\), since germs agree. And if \(P\) is *separated* (a section with all germs zero is zero), \(\theta\) is injective on sections. *Reference:* [Stacks, Tags 007Z, 0080 and 0089].
- **(I) Stalks detect isomorphisms.** A morphism of sheaves that is bijective on every stalk is an isomorphism. *Reference:* [Stacks, Tag 007T].
- **(F) Filtered colimits are exact.** Filtered colimits of modules over a ring are exact. The index category must be filtered: colimits of pushout diagrams, for instance, are not left exact. *Reference:* [*Sheaves of modules on a ringed space*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sheaves-of-modules-on-a-ringed-space.html), Lemma 1.1, followed by a pushout counterexample.
- **(B) Baer's criterion.** A left module \(E\) over a ring \(A\) is injective if every \(A\)-linear map from a left ideal of \(A\) to \(E\) extends to \(A\). *Reference:* [*Injective modules, flasque sheaves and bounded-below derived functors*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html), Lemma 2.1.
- **(Γ) Supports.** Let \(Z\subset X\) be locally closed and \(Z'\subset Z\) closed in \(Z\). For every sheaf \(F\) of abelian groups, the sequence \(0\to\Gamma_{Z'}F\to\Gamma_ZF\to\Gamma_{Z\setminus Z'}F\), given by the inclusion of supports and by restriction, is exact. If \(F\) is flabby, the last map is onto. *Reference:* the proof of Proposition 3.1 in [*Sections with support and the localization triangle*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sections-with-support-and-the-localization-triangle.html).

*Complexes.* Let \(\mathcal A\) and \(\mathcal B\) be abelian categories.

- **(H) Maps into K-injective complexes.** If \(I\) is K-injective, then for every complex \(L\) the map \(\operatorname{Hom}_{K(\mathcal A)}(L,I)\to\operatorname{Hom}_{D(\mathcal A)}(L,I)\) is bijective. *Reference:* [Stacks, Tag 070I].
- **(K) K-injective resolutions.** Call \(\mathcal A\) a *Grothendieck* abelian category if it has all small colimits, its filtered colimits are exact, and it has a *generator*: an object \(G\) such that \(\operatorname{Hom}(G,-)\) is faithful. In such a category every complex \(K\) has a qis \(K\to I(K)\), functorial in \(K\) and injective in each degree, into a K-injective complex whose terms are injective objects. *Reference:* [Stacks, Tag 079P].
- **(D) Derived functors.** Suppose that every complex of \(\mathcal A\) has a qis into a K-injective complex. Then every additive functor \(\Phi:\mathcal A\to\mathcal B\) has a right derived functor \(R\Phi:D(\mathcal A)\to D(\mathcal B)\), and \(R\Phi(K)=\Phi(I)\) for every qis \(K\to I\) into a K-injective complex. *Reference:* [Stacks, Tag 070K].
- **(T) The triangle of a short exact sequence.** A termwise exact sequence \(0\to A\to B\to C\to0\) of complexes gives a distinguished triangle \(A\to B\to C\to A[1]\) in \(D(\mathcal A)\), and a morphism of such sequences gives a morphism of triangles. The third arrow and its sign are made explicit in Lemma 13.3. *Reference:* [Stacks, Tag 0152].

## 2. Module sheaves form an abelian category

**Theorem 2.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\).

1. \(\operatorname{Mod}(\mathcal O)\) is additive. A morphism \(\varphi:F\to G\) has a kernel, computed on sections: \((\operatorname{Ker}\varphi)(U)=\ker\varphi_U\). It has a cokernel: the sheafification of \(U\mapsto\operatorname{coker}\varphi_U\).
2. For each \(x\), the stalk functor \(F\mapsto F_x\), from \(\operatorname{Mod}(\mathcal O)\) to \(\operatorname{Mod}(\mathcal O_x)\), is additive, and \((\operatorname{Ker}\varphi)_x=\ker\varphi_x\), \((\operatorname{Coker}\varphi)_x=\operatorname{coker}\varphi_x\).
3. \(\operatorname{Mod}(\mathcal O)\) is abelian, and each stalk functor is exact.
4. A sequence \(F\to G\to H\) with zero composite is exact at \(G\) if and only if \(F_x\to G_x\to H_x\) is exact at \(G_x\) for every \(x\). A morphism \(\varphi\) is a monomorphism (epimorphism, isomorphism) if and only if every \(\varphi_x\) is one.

*Reference:* [Stacks, Tag 01AG] proves (3) and (4) for commutative \(\mathcal O\); [*Sheaves of modules on a ringed space*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sheaves-of-modules-on-a-ringed-space.html), Theorem 2.1, proves the general case.

**Proof.** (1) Morphisms add on sections, and composition is bilinear. The zero sheaf is a zero object. Finite direct sums are formed on sections: \(U\mapsto F(U)\oplus G(U)\) is a sheaf, because sections glue coordinatewise. Let \(\varphi:F\to G\). The presheaf \(U\mapsto\ker\varphi_U\) is a sheaf. Indeed, let a section \(s\) of \(F\) lie in the kernel on each set of an open cover. Then \(\varphi(s)\) vanishes on that cover, so \(\varphi(s)=0\), since \(G\) is a sheaf. Sections of the kernel that agree on overlaps glue in \(F\), and by this remark the glued section lies in the kernel. Each \(\varphi_U\) is \(\mathcal O(U)\)-linear, so the kernel is a subpresheaf of left modules. A morphism \(E\to F\) whose composite with \(\varphi\) is zero lands in it on every open set. So it is the kernel. For the cokernel, let \(P(U)=\operatorname{coker}\varphi_U\), a presheaf of left \(\mathcal O\)-modules. By (S), morphisms \(P^+\to H\) into a sheaf \(H\) correspond to morphisms of presheaves \(P\to H\). These are the morphisms \(G\to H\) that vanish after \(\varphi\). So \(P^+\) is the cokernel.

(2) The stalk \(F_x=\varinjlim_{U\ni x}F(U)\) is a left module over \(\mathcal O_x=\varinjlim_{U\ni x}\mathcal O(U)\), and the functor is additive. The open neighbourhoods of \(x\) form a filtered system, and filtered colimits are exact (F). Hence \((\operatorname{Ker}\varphi)_x=\varinjlim_U\ker\varphi_U=\ker\varphi_x\). By (S), \(\theta\) is bijective on stalks, so \((P^+)_x=P_x\); and by (F) again, \(P_x=\varinjlim_U\operatorname{coker}\varphi_U=\operatorname{coker}\varphi_x\).

(3) The coimage of \(\varphi\) is the cokernel of \(\operatorname{Ker}\varphi\to F\). The image is the kernel of \(G\to\operatorname{Coker}\varphi\). By (2), at each \(x\) the canonical map \(\operatorname{Coim}\varphi\to\operatorname{Im}\varphi\) becomes the canonical map \(\operatorname{Coim}\varphi_x\to\operatorname{Im}\varphi_x\) of \(\mathcal O_x\)-modules. That map is an isomorphism, because modules over a ring form an abelian category. By (I) the map of sheaves is an isomorphism. Its inverse is \(\mathcal O\)-linear, as the map is. So \(\operatorname{Mod}(\mathcal O)\) is abelian. The stalk functor preserves kernels and cokernels by (2), so it is exact.

(4) Exactness at \(G\) means that \(\operatorname{Im}(F\to G)\to\operatorname{Ker}(G\to H)\) is an isomorphism. Both sides are built from kernels and cokernels. By (2), the map at \(x\) is the same map for the stalk sequence. If every stalk sequence is exact, (I) gives exactness. Conversely, exact functors preserve exactness. A sheaf whose stalks all vanish is zero, since each section then vanishes on an open cover. Hence \(\varphi\) is a monomorphism iff \(\operatorname{Ker}\varphi=0\) iff every \(\ker\varphi_x=0\). The same holds with cokernels. An isomorphism is a morphism that is both. \(\square\)

The proof never uses commutativity of \(\mathcal O\). In particular, Theorem 2.1 holds for the constant sheaf \(k_X\) of any unital ring \(k\), commutative or not.

## 3. Limits, colimits, stalks, and sections of sums

**Theorem 3.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\).

1. Every small diagram \((F_i)\) in \(\operatorname{Mod}(\mathcal O)\) has a limit, computed on sections. So \(\Gamma(U,-)\) commutes with limits.
2. Every small diagram has a colimit: the sheafification of the presheaf colimit. Stalks commute with colimits: \((\varinjlim_iF_i)_x=\varinjlim_i(F_i)_x\).
3. Filtered colimits are exact.
4. Finite direct sums are computed on sections.
5. If \(U\) is a quasi-compact open set, the canonical map \(\bigoplus_i\Gamma(U,F_i)\to\Gamma(U,\bigoplus_iF_i)\) is bijective for every family. Without quasi-compactness it can fail to be onto (Example 2).
6. Products exist and are computed on sections, but they need not be exact (Example 3).

*Reference:* [Stacks, Tag 01AH], for parts (1)–(4) and commutative \(\mathcal O\).

**Proof.** (1) Let \(L(U)=\varprojlim_iF_i(U)\), with coordinatewise restriction and module structure. It is a sheaf. A local section on a cover is a compatible family on each piece. Glue each coordinate in \(F_i\). The glued coordinates again form a compatible family, because the transition maps are morphisms of sheaves and sections of a sheaf are determined locally. A morphism \(E\to L\) is the same as a compatible family of morphisms \(E\to F_i\), open set by open set. So \(L\) is the limit, and \(\Gamma(U,L)=\varprojlim_i\Gamma(U,F_i)\).

(2) Let \(P(U)=\varinjlim_iF_i(U)\). By (S), morphisms \(P^+\to H\) into a sheaf correspond to compatible families of morphisms \(F_i\to H\). So \(P^+\) is the colimit. At \(x\),
\[
(P^+)_x=P_x=\varinjlim_{U\ni x}\varinjlim_iF_i(U)=\varinjlim_i\varinjlim_{U\ni x}F_i(U)=\varinjlim_i(F_i)_x ,
\]
since colimits commute with colimits.

(3) Let \(0\to A_i\to B_i\to C_i\to0\) be exact, naturally in \(i\) over a filtered category. At each \(x\), by (2), the stalk sequence of the colimits is the filtered colimit of the exact sequences \(0\to(A_i)_x\to(B_i)_x\to(C_i)_x\to0\). It is exact by (F). Since exactness is checked on stalks ([Theorem 2.1](#sh-fnd-dc-02)(4)), the colimit sequence is exact.

(4) This was shown in the proof of [Theorem 2.1](#sh-fnd-dc-02)(1).

(5) Let \(S=\bigoplus_iF_i\), the sheafification of \(P(V)=\bigoplus_iF_i(V)\). The germ at \(x\) of \(p=(p_i)\in P(V)\) is \((p_{i,x})_i\in\bigoplus_i(F_i)_x\). If all germs of \(p\) vanish, each \(p_i\) has zero germs and is zero. So \(P\) is separated, and \(\theta:P(V)\to S(V)\) is injective for every \(V\). For \(V=U\) this is the injectivity of the canonical map. For surjectivity, let \(t\in S(U)\). By (S), every point of \(U\) has an open neighbourhood \(V\subset U\) and some \(p\in P(V)\) with \(\theta(p)=t|_V\). As \(U\) is quasi-compact, finitely many such pairs \((V_1,p_1),\ldots,(V_m,p_m)\) cover \(U\). Each \(p_k\) has finitely many nonzero coordinates. Let \(J\) be the finite set of indices that occur, and \(S_J=\bigoplus_{i\in J}F_i\). By (4), \(S_J\) is a sheaf. It is also a subpresheaf of \(P\) that contains all \(p_k\). On \(V_k\cap V_l\), the restrictions of \(p_k\) and \(p_l\) have the same image under the injective map \(\theta\), so they are equal. Glue them to \(s\in S_J(U)=\bigoplus_{i\in J}F_i(U)\). Then \(\theta(s)\) and \(t\) agree on each \(V_k\), so \(\theta(s)=t\).

(6) Products are limits, so (1) applies. Example 3 shows that a product of epimorphisms need not be an epimorphism. \(\square\)

The proofs use no commutativity of \(\mathcal O\). A related fact, not used here, is the analogue of (5) for filtered colimits: on a compact Hausdorff space \(X\), global sections commute with filtered colimits of sheaves. (Injectivity holds on every quasi-compact space [Stacks, Tag 009F]. For surjectivity, represent a global section of the colimit on a finite open cover \(U_1,\dots,U_n\) by sections \(t_j\in F_i(U_j)\) of one \(F_i\), and choose closed sets \(K_j\subset U_j\) covering \(X\). The germs of \(t_j\) and \(t_k\) agree in the colimit at each point of the compact set \(K_j\cap K_k\), so after enlarging \(i\) they agree on an open neighbourhood of it. The gluing in the proof of [Schapira SHV, Proposition 3.1.3(ii)], by induction on \(n\), then gives a global section of that \(F_i\) representing the given one.)

## 4. Exact inverse image

**Theorem 4.1.** Let \(f:X\to Y\) be continuous and \(\mathcal O_Y\) a sheaf of rings on \(Y\).

1. On \(X\), \(f^{-1}\mathcal O_Y\) is a sheaf of rings, with stalks \((f^{-1}\mathcal O_Y)_x=\mathcal O_{Y,f(x)}\). For \(G\in\operatorname{Mod}(\mathcal O_Y)\), \(f^{-1}G\) is a sheaf of left \(f^{-1}\mathcal O_Y\)-modules, and the canonical map \(G_{f(x)}\to(f^{-1}G)_x\) is an isomorphism of \(\mathcal O_{Y,f(x)}\)-modules.
2. \(f^{-1}:\operatorname{Mod}(\mathcal O_Y)\to\operatorname{Mod}(f^{-1}\mathcal O_Y)\) is exact and commutes with colimits.
3. For a unital ring \(k\), \(f^{-1}k_Y=k_X\) as sheaves of rings. So \(f^{-1}:\operatorname{Mod}(k_Y)\to\operatorname{Mod}(k_X)\) is exact, and \((f^{-1}G)_x=G_{f(x)}\) as \(k\)-modules. This holds for every unital ring \(k\), commutative or not.
4. \(f^{-1}\) is left adjoint to \(f_*:\operatorname{Mod}(f^{-1}\mathcal O_Y)\to\operatorname{Mod}(\mathcal O_Y)\).

Part (4) is used here without proof; [*Sheaves of modules on a ringed space*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sheaves-of-modules-on-a-ringed-space.html), Theorem 4.1(4), proves it. [Stacks, Tag 01AJ] proves the exactness in (2) for sheaves of abelian groups.

**Proof of (1)–(3).** Recall that \(f^{-1}G\) is the sheafification of the presheaf \(V\mapsto\varinjlim_{W\supset f(V)}G(W)\), where \(W\) runs over the open sets containing \(f(V)\). We use its description by germs. For \(V\subset X\) open, \(f^{-1}G(V)\) is the set of maps \(s\) that give each \(x\in V\) an element \(s(x)\in G_{f(x)}\), such that each point of \(V\) has an open neighbourhood \(V'\subset V\), an open \(W\supset f(V')\) and a section \(g\in G(W)\) with \(s(x')=g_{f(x')}\) for all \(x'\in V'\). The condition is local, so this is a sheaf of sets. Take \(G=\mathcal O_Y\) to get \(f^{-1}\mathcal O_Y\). Sum, product and the action are defined pointwise, through the ring \(\mathcal O_{Y,f(x)}\) and its module \(G_{f(x)}\). They preserve the local condition: if near a point \(s\) is represented by \(g\in G(W)\) and \(a\) by \(h\in\mathcal O_Y(W')\), then near that point \(as\) is represented by \(h|_{W\cap W'}\,g|_{W\cap W'}\). This gives the ring and module structures. Evaluation at \(x\) is a ring map, and a module map over it.

Evaluation \((f^{-1}G)_x\to G_{f(x)}\) is onto: \(g\in G(W)\) with \(W\ni f(x)\) defines a section over \(f^{-1}(W)\). It is one-to-one: if \(s(x)=0\), represent \(s\) near \(x\) by \(g\in G(W)\). Then \(g_{f(x)}=0\), so \(g\) vanishes on an open \(W_0\ni f(x)\), and \(s\) vanishes on \(V'\cap f^{-1}(W_0)\). The canonical map \(G_{f(x)}\to(f^{-1}G)_x\) sends the germ of \(g\) to the germ of the section defined by \(g\). It is inverse to evaluation. This proves (1).

(2) Exactness can be checked on stalks ([Theorem 2.1](#sh-fnd-dc-02)(4)). By (1), the stalk of \(f^{-1}G\) at \(x\) is \(G_{f(x)}\), so on stalks \(f^{-1}\) acts as the identity, and \(f^{-1}\) is exact. For a colimit, the canonical map \(\varinjlim_if^{-1}G_i\to f^{-1}\varinjlim_iG_i\) is, at \(x\), the map \(\varinjlim_i(G_i)_{f(x)}\to(\varinjlim_iG_i)_{f(x)}\). This map is bijective, because stalks commute with colimits ([Theorem 3.1](#sh-fnd-dc-03)(2)). So the canonical map is an isomorphism by (I).

(3) A germ of a section of \(k_Y\) is the germ of a locally constant function. So the sections of \(f^{-1}k_Y\) over \(V\) are the maps \(V\to k\) that are constant near each point, that is, the sections of \(k_X\). The ring operations agree pointwise. The argument never uses commutativity of \(k\). \(\square\)

**Remark 4.2.** For a morphism of ringed spaces \(f:(X,\mathcal O_X)\to(Y,\mathcal O_Y)\), the module pullback \(f^*=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}(-)\) is only right exact, and Example 5 shows that it can fail to be exact. It agrees with the exact functor \(f^{-1}\) of Theorem 4.1 exactly when \(\mathcal O_X=f^{-1}\mathcal O_Y\).

## 5. Enough injectives, functorially

Theorem 5.4 embeds every sheaf of modules into a product of skyscraper sheaves, one at each point, built from injective modules that contain the stalks. Choosing such an injective module separately for each stalk would already give enough injectives. The explicit construction of Lemma 5.1 makes the embedding a functor, for modules over any ring.

**Lemma 5.1 (functorial injective embeddings of modules).** Let \(A\) be a ring. Put \(E_A=\operatorname{Hom}_{\mathbb Z}(A,\mathbb Q/\mathbb Z)\), a left \(A\)-module by \((a\varphi)(b)=\varphi(ba)\). For a left \(A\)-module \(M\) put
\[
I_A(M)=\prod_{\varphi\in\operatorname{Hom}_A(M,E_A)}E_A,\qquad \iota_M(m)=(\varphi(m))_\varphi .
\tag{5.1}
\]
Then \(I_A(M)\) is injective and \(\iota_M\) is injective. For \(u:M\to N\), the formula \(I_A(u)\bigl((y_\varphi)_\varphi\bigr)=(y_{\chi\circ u})_{\chi}\), with \(\chi\) running over \(\operatorname{Hom}_A(N,E_A)\), makes \(I_A\) a functor and \(\iota\) a natural transformation.

**Proof.** \(E_A\) is a left module: \(((aa')\varphi)(b)=\varphi(baa')=(a(a'\varphi))(b)\). The maps
\[
\Phi(\varphi)=\bigl(m\mapsto\varphi(m)(1)\bigr),\qquad \Psi(\psi)=\bigl(m\mapsto(b\mapsto\psi(bm))\bigr)
\]
are inverse bijections between \(\operatorname{Hom}_A(M,E_A)\) and \(\operatorname{Hom}_{\mathbb Z}(M,\mathbb Q/\mathbb Z)\), natural in \(M\). Here \(\Psi(\psi)\) is \(A\)-linear, since \(\Psi(\psi)(am)(b)=\psi(bam)=(a\,\Psi(\psi)(m))(b)\). The group \(\mathbb Q/\mathbb Z\) is an injective \(\mathbb Z\)-module. To see this, use Baer's criterion (B): the ideals of \(\mathbb Z\) are the \(n\mathbb Z\). For \(n=0\) there is nothing to extend. For \(n\geq1\), a map \(n\mathbb Z\to\mathbb Q/\mathbb Z\) sending \(n\) to \(q\) extends to \(\mathbb Z\) by sending \(1\) to any \(q'\) with \(nq'=q\), which exists since \(\mathbb Q/\mathbb Z\) is divisible. Exact sequences of \(A\)-modules are exact as groups. So \(\operatorname{Hom}_A(-,E_A)\cong\operatorname{Hom}_{\mathbb Z}(-,\mathbb Q/\mathbb Z)\) is exact, and \(E_A\) is injective. A product of injectives is injective, because \(\operatorname{Hom}(-,\prod E)=\prod\operatorname{Hom}(-,E)\) and products of exact sequences of groups are exact. So \(I_A(M)\) is injective. If \(m\neq0\), define \(\psi\) on the subgroup \(\mathbb Zm\) by \(\psi(m)=1/n+\mathbb Z\) if \(m\) has finite order \(n\geq2\), and \(\psi(m)=1/2+\mathbb Z\) if \(m\) has infinite order. Extend \(\psi\) to \(M\), as \(\mathbb Q/\mathbb Z\) is injective. Then \(\varphi=\Psi(\psi)\) has \(\varphi(m)(1)=\psi(m)\neq0\), so \(\iota_M(m)\neq0\). Finally \(I_A(u)(\iota_M(m))=(\chi(u(m)))_\chi=\iota_N(u(m))\), and the displayed formula gives \(I_A(vu)=I_A(v)I_A(u)\) and \(I_A(\mathrm{id})=\mathrm{id}\). \(\square\)

**Lemma 5.2 (extension by zero from an open set).** Let \(j:U\hookrightarrow X\) be open and \(B\) a sheaf of left \(\mathcal O|_U\)-modules. For \(V\subset X\) open put
\[
j_!B(V)=\{\,s\in B(U\cap V):\ \operatorname{supp}s\text{ is closed in }V\,\}.
\]
1. \(j_!B\) is a sheaf of left \(\mathcal O\)-modules, with \((j_!B)_x=B_x\) for \(x\in U\) and \((j_!B)_x=0\) for \(x\notin U\). So \(j_!\) is exact.
2. \(\operatorname{Hom}_{\mathcal O}(j_!B,G)\cong\operatorname{Hom}_{\mathcal O|_U}(B,G|_U)\), naturally in \(B\) and \(G\).
3. \(\operatorname{Hom}_{\mathcal O}(j_!\mathcal O_U,G)\cong G(U)\) by \(\varphi\mapsto\varphi(1)\). For opens \(V\subset W\), the morphism \(j_{V!}\mathcal O_V\to j_{W!}\mathcal O_W\) that corresponds to \(1\in\mathcal O(V)=(j_{W!}\mathcal O_W)(V)\) is a monomorphism, and under these identifications it induces restriction \(G(W)\to G(V)\).

**Proof.** (1) Supports of sections are closed in their domains. Closedness of a support in \(V\) is a local condition on \(V\), so sections of \(B\) glue within \(j_!B\), and \(j_!B\) is a sheaf. Module operations do not enlarge supports. If \(x\in U\), the opens inside \(U\) are cofinal among neighbourhoods of \(x\), and there \(j_!B=B\); so \((j_!B)_x=B_x\). If \(x\notin U\) and \(s\in j_!B(V)\) with \(x\in V\), then \(x\notin\operatorname{supp}s\), and this support is closed in \(V\); so \(s\) vanishes near \(x\) and the stalk is \(0\). Exactness is checked on stalks ([Theorem 2.1](#sh-fnd-dc-02)(4)), and on each stalk \(j_!\) acts as the identity or as zero; so \(j_!\) is exact.

(2) A morphism \(j_!B\to G\) restricts over \(U\) to a morphism \(B\to G|_U\). Conversely, let \(\alpha:B\to G|_U\) and \(s\in j_!B(V)\). The section \(\alpha(s)\) on \(U\cap V\) and the section \(0\) on \(V\setminus\operatorname{supp}s\) agree on the overlap. The two open sets cover \(V\), because \(\operatorname{supp}s\subset U\cap V\). Glue them to a section of \(G\) over \(V\). This defines the inverse bijection; linearity and naturality are checked on the two pieces.

(3) By (2), a morphism \(j_!\mathcal O_U\to G\) is a left-linear map \(\mathcal O_U\to G|_U\), and such a map is \(a\mapsto as\) with \(s\) the image of \(1\in\mathcal O(U)\). For \(V\subset W\), \((j_{W!}\mathcal O_W)(V)=\mathcal O(V)\). At \(x\in V\) the morphism is the identity of \(\mathcal O_x\); at other points its source stalk is \(0\). So it is injective on every stalk, hence a monomorphism by [Theorem 2.1](#sh-fnd-dc-02)(4). Composing with it sends the morphism with \(\varphi(1)=s\in G(W)\) to the one with value \(s|_V\) at \(1\). \(\square\)

**Lemma 5.3 (skyscrapers).** Let \(x\in X\) and let \(J\) be a left \(\mathcal O_x\)-module. Put \(x_*J(V)=J\) if \(x\in V\) and \(0\) otherwise, with identity restrictions between opens containing \(x\), and let \(\mathcal O(V)\) act through \(\mathcal O(V)\to\mathcal O_x\). Then \(x_*J\) is a sheaf of left \(\mathcal O\)-modules, and
\[
\operatorname{Hom}_{\mathcal O}(F,x_*J)\cong\operatorname{Hom}_{\mathcal O_x}(F_x,J),
\tag{5.2}
\]
naturally in \(F\) and \(J\). If \(J\) is injective, then \(x_*J\) is injective.

**Proof.** Let \(x\in V\) and let \((V_i)\) cover \(V\). Some \(V_i\) contains \(x\). Compatible sections agree on all \(V_i\) that contain \(x\), since their pairwise overlaps contain \(x\); this common value is the glued section, and it is unique. If \(x\notin V\), all sections are \(0\). A morphism \(\varphi:F\to x_*J\) has components \(\varphi_V\), for \(x\in V\), that are compatible with restriction. So they define an \(\mathcal O_x\)-linear map \(F_x\to J\). Conversely, given \(g:F_x\to J\), put \(\varphi_V(s)=g(s_x)\) if \(x\in V\) and \(0\) otherwise. These constructions are inverse. If \(J\) is injective, \(\operatorname{Hom}_{\mathcal O}(-,x_*J)\cong\operatorname{Hom}_{\mathcal O_x}((-)_x,J)\) is exact, because the stalk functor is exact ([Theorem 2.1](#sh-fnd-dc-02)(3)). \(\square\)

**Theorem 5.4 (functorial injective embeddings).** Let \(\mathcal O\) be any sheaf of rings on \(X\). Put
\[
E(F)=\prod_{x\in X}x_*\bigl(I_{\mathcal O_x}(F_x)\bigr),
\]
where \(I_{\mathcal O_x}\) is the functor (5.1) for the ring \(\mathcal O_x\), and let \(\iota_F:F\to E(F)\) have \(x\)-component the morphism that corresponds under (5.2) to \(\iota_{F_x}:F_x\to I_{\mathcal O_x}(F_x)\). Then \(E(F)\) is injective, \(\iota_F\) is a monomorphism, and \(E\) is a functor with \(\iota\) natural. So \(\operatorname{Mod}(\mathcal O)\) has enough injectives, with functorial injective embeddings.

*Reference:* [Stacks, Tag 01DI] gives functorial injective embeddings for commutative \(\mathcal O\).

**Proof.** Products exist and are computed on sections ([Theorem 3.1](#sh-fnd-dc-03)(1)), and a product of injectives is injective, as in the proof of Lemma 5.1. Each factor is injective by Lemmas 5.1 and 5.3. Explicitly, \(\iota_F\) sends \(s\in F(V)\) to \((\iota_{F_x}(s_x))_{x\in V}\). If this is zero, each \(s_x=0\), as \(\iota_{F_x}\) is injective, so \(s=0\). Kernels are computed on sections ([Theorem 2.1](#sh-fnd-dc-02)(1)), so \(\iota_F\) is a monomorphism. For \(u:F\to G\) put \(E(u)=\prod_xx_*(I_{\mathcal O_x}(u_x))\). Naturality of \(\iota\) holds factor by factor, by Lemma 5.1. \(\square\)

**Corollary 5.5.** (1) Every injective \(\mathcal O\)-module is flabby. (2) For \(U\) open, the restriction of an injective \(\mathcal O\)-module \(I\) to \(U\) is an injective \(\mathcal O|_U\)-module.

**Proof.** (1) For \(V\subset W\), Lemma 5.2(3) gives a monomorphism \(j_{V!}\mathcal O_V\to j_{W!}\mathcal O_W\). Applying the exact functor \(\operatorname{Hom}(-,I)\) turns it into the restriction \(I(W)\to I(V)\), which is therefore onto. Take \(W=X\). (2) By Lemma 5.2(2), \(\operatorname{Hom}_{\mathcal O|_U}(-,I|_U)\cong\operatorname{Hom}_{\mathcal O}(j_!(-),I)\). This is a composite of exact functors. \(\square\)

## 6. Right derived functors on bounded-below complexes

**Theorem 6.1.** Let \(\mathcal A\) and \(\mathcal B\) be abelian, and assume that every object of \(\mathcal A\) embeds in an injective object. Let \(\Phi:\mathcal A\to\mathcal B\) be additive.

1. Every bounded-below complex \(K\) has a qis \(K\to I\) into a bounded-below complex of injectives. If \(K^n=0\) for \(n<a\), it can be chosen injective in each degree, with \(I^n=0\) for \(n<a\).
2. Such an \(I\) is K-injective (Lemma 6.2). Hence \(\operatorname{Hom}_{K(\mathcal A)}(L,I)=\operatorname{Hom}_{D(\mathcal A)}(L,I)\) for every \(L\). A morphism into \(I\) extends along a qis, uniquely up to homotopy.
3. The rule \(R\Phi(K)=\Phi(I)\) gives a triangulated functor \(D^+(\mathcal A)\to D^+(\mathcal B)\), and this functor is the right derived functor \(R\Phi\). If \(\Phi\) is left exact, \(R^0\Phi=\Phi\) and \((R^i\Phi)_i\) is a universal \(\delta\)-functor.
4. (Leray) If \(\Phi\) is left exact and \(J\) is a bounded-below complex with \(R^i\Phi(J^n)=0\) for all \(i>0\) and all \(n\), then \(\Phi(J)\to R\Phi(J)\) is an isomorphism. Left exactness cannot be dropped. For a general additive \(\Phi\), the terms must also satisfy \(\Phi(J^n)\cong R^0\Phi(J^n)\), which holds by (3) when \(\Phi\) is left exact. For \(\Phi=-\otimes_{\mathbb Z}\mathbb Z/2\) on \(\operatorname{Mod}(\mathbb Z)\) and \(J=\mathbb Z\) in degree \(0\), the injective resolution \(\mathbb Q\to\mathbb Q/\mathbb Z\) gives \(R\Phi(\mathbb Z)=0\), because \(\mathbb Q\) and \(\mathbb Q/\mathbb Z\) are divisible, while \(\Phi(\mathbb Z)=\mathbb Z/2\).
5. For \(\mathcal A=\operatorname{Mod}(\mathcal O)\), with \(\mathcal O\) any sheaf of rings, (1)–(4) hold by Theorem 5.4. This gives \(Rf_*\), \(R\Gamma(U,-)\), the sheaf \(R\Gamma_Z\) of sections with support (Section 1) and \(R\operatorname{Hom}_{\mathcal O}(G,-)\) on \(D^+\).

Parts (1), (3) and (4) are standard facts about abelian categories in which every object embeds in an injective object, and we use them without proof. Part (2) follows from Lemma 6.2 and (H), and part (5) from Theorem 5.4. So the only input about sheaves is Theorem 5.4. *Reference:* [Stacks, Tags 013K, 013P, 05TN and 015E]; [Stacks, Tag 0716] states (5) for commutative \(\mathcal O\).

**Lemma 6.2 (bounded-below complexes of injectives are K-injective).** Let \(I\) be a complex of injectives with \(I^n=0\) for \(n<a\), and let \(A\) be acyclic. Then every chain map \(f:A\to I\) is null-homotopic.

**Proof.** We build maps \(s^n:A^n\to I^{n-1}\) with
\[
f^n=d\,s^n+s^{n+1}d\qquad\text{for all }n .
\tag{6.1}
\]
Put \(s^n=0\) for \(n\leq a\). Then (6.1) holds for \(n<a\), where both sides are \(0\). Suppose \(s^k\) is built for \(k\leq n\) and (6.1) holds for all indices below \(n\). Put \(g=f^n-d\,s^n:A^n\to I^n\). Using (6.1) at \(n-1\), and \(d^2=0\),
\[
g\,d=f^nd-d\,s^nd=d\,f^{n-1}-d\bigl(f^{n-1}-d\,s^{n-1}\bigr)=0 .
\]
So \(g\) vanishes on the image of \(d:A^{n-1}\to A^n\). As \(A\) is acyclic, that image is the kernel of \(d:A^n\to A^{n+1}\). Hence \(h(da)=g(a)\) is a well-defined map from the image of \(d\) in \(A^{n+1}\) to \(I^n\). Since \(I^n\) is injective, \(h\) extends to \(s^{n+1}:A^{n+1}\to I^n\). Then \(s^{n+1}d=g\), which is (6.1) at \(n\). \(\square\)

The induction needs a place to start. Example 1 shows that without a lower bound the conclusion fails. A special case has a second proof: if \(I\) is itself acyclic, it splits and is contractible, so every chain map into it is null-homotopic.

## 7. K-injective resolutions of unbounded complexes

**Proposition 7.1 (a generator).** Let \(\mathcal O\) be any sheaf of rings on \(X\), and \(G=\bigoplus_{U}j_{U!}\mathcal O_U\), the sum over all open sets \(U\). Then:

- (a) for every subsheaf \(N\subsetneq M\) there is a morphism \(G\to M\) that does not factor through \(N\);
- (b) \(\operatorname{Hom}_{\mathcal O}(G,-)\) is faithful: a nonzero morphism \(M\to M'\) stays nonzero after composing with some \(G\to M\);
- (c) every \(M\) receives an epimorphism from a direct sum of copies of \(G\).

Together with [Theorem 3.1](#sh-fnd-dc-03)(2)–(3), which give all colimits and exact filtered colimits, this makes \(\operatorname{Mod}(\mathcal O)\) a Grothendieck abelian category in the sense of (K).

*Reference:* [Stacks, Tag 079V] states the generator for commutative \(\mathcal O\).

**Proof.** A section \(s\in M(U)\) gives \(e_s:j_{U!}\mathcal O_U\to M\) with \(e_s(1)=s\) (Lemma 5.2(3)). Composing with the projection \(G\to j_{U!}\mathcal O_U\) gives \(\tilde e_s:G\to M\). (a) A subobject of \(M\) in \(\operatorname{Mod}(\mathcal O)\) is a subsheaf, since kernels are computed on sections. If \(N\neq M\), there are \(U\) and \(s\in M(U)\setminus N(U)\). If \(\tilde e_s\) factored through \(N\), then \(s=e_s(1)\) would lie in \(N(U)\). (b) If \(\varphi:M\to M'\) is nonzero, then \(\varphi(s)\neq0\) for some section \(s\in M(U)\). So \(\varphi\circ\tilde e_s\neq0\): on the summand \(j_{U!}\mathcal O_U\) it sends \(1\) to \(\varphi(s)\). (c) The sum of all \(\tilde e_s\), over all pairs \((U,s)\), is a morphism \(\bigoplus_{(U,s)}G\to M\) whose image contains every section. So it is onto on stalks, hence an epimorphism. \(\square\)

The three forms of "generator" are equivalent in any abelian category with direct sums (Exercise 2). The definition in (K) uses form (b).

**Theorem 7.2.** For every complex \(K\) of left \(\mathcal O\)-modules there is a qis \(K\to I(K)\), functorial in \(K\) and injective in each degree, into a K-injective complex whose terms are injective. Consequently, every additive functor \(\Phi:\operatorname{Mod}(\mathcal O)\to\mathcal B\) into an abelian category has a right derived functor \(R\Phi:D(\mathcal O)\to D(\mathcal B)\), with \(R\Phi(K)=\Phi(I(K))\). In particular \(Rf_*\), \(R\Gamma(U,-)\) and the sheaf \(R\Gamma_Z\) are defined on the unbounded derived category.

*Reference:* [Stacks, Tag 079P].

**Proof.** By Proposition 7.1, \(\operatorname{Mod}(\mathcal O)\) is a Grothendieck abelian category. In every such category, complexes have functorial K-injective resolutions of the stated kind, by (K). The second statement then follows from (D), which applies in every abelian category in which each complex has a qis to a K-injective complex. \(\square\)

**Corollary 7.3.** (1) If \(I\) is a K-injective complex of \(\mathcal O\)-modules and \(U\) is open, \(I|_U\) is K-injective. (2) If \(f:X\to Y\) is continuous, \(\mathcal O_X=f^{-1}\mathcal O_Y\), and \(I\) is a K-injective complex of \(\mathcal O_X\)-modules, then \(f_*I\) is K-injective. (3) On bounded-below complexes, the derived functors of Theorem 7.2 agree with those of [Theorem 6.1](#sh-fnd-dc-06).

**Proof.** (1) and (2): a functor \(u\) with an exact left adjoint \(v\) preserves K-injectivity. Indeed, the adjunction on modules gives one on complexes, compatible with homotopies. So for acyclic \(A\), \(\operatorname{Hom}_K(A,uI)\cong\operatorname{Hom}_K(vA,I)=0\), since \(vA\) is acyclic. Apply this to \(j_!\dashv j^{-1}\), where \(j_!\) is exact and left adjoint to restriction by Lemma 5.2, and to \(f^{-1}\dashv f_*\), where \(f^{-1}\) is exact and left adjoint to \(f_*\) by [Theorem 4.1](#sh-fnd-dc-04)(2) and (4). (3) A bounded-below injective resolution is K-injective by Lemma 6.2, and two K-injective resolutions of the same complex are homotopy equivalent. \(\square\)

**Remark 7.4 (complexes of injectives).** An unbounded complex of injectives need not be K-injective (Example 1). If \(\operatorname{Mod}(\mathcal O)\) has finite homological dimension \(d\), every complex \(J\) of injectives is K-injective. (Theorem 7.2 gives a qis \(J\to I(J)\) into a K-injective complex of injectives; its cone \(C\) is an acyclic complex of injectives. For its cycles \(Z^n\), the sequences \(0\to Z^{n-1}\to C^{n-1}\to Z^n\to0\) give \(\operatorname{Ext}^1(-,Z^n)\cong\operatorname{Ext}^{d+1}(-,Z^{n-d})=0\), so every \(Z^n\) is injective, these sequences split and \(C\) is contractible. Hence \(J\to I(J)\) is a homotopy equivalence, and \(J\) is K-injective.) This is not used.

**Remark 7.5 (why a Grothendieck category).** Products in \(\operatorname{Mod}(\mathbb Z_{\mathbb R})\) are not exact (Example 3). So a criterion for K-injective resolutions that needs exact products does not apply to sheaves in general. Constructions by inverse limits of resolutions of truncations work for modules over a ring, where products are exact; for sheaves they need extra care. This is why Theorem 7.2 goes through the Grothendieck property.

**Remark 7.6 (no bounded output).** Theorem 7.2 asserts no bounded output. Exercise 4 gives a bounded input with unbounded \(R\operatorname{Hom}\).

## 8. K-flat resolutions

In this section \(\mathcal O\) is commutative.

**Theorem 8.1 (K-flat resolutions).** Every complex \(G\) of \(\mathcal O\)-modules has a qis \(K\to G\), surjective in each degree, from a K-flat complex \(K\) with flat terms.

*Reference:* [Stacks, Tag 06YF].

We use Theorem 8.1 without proof, together with three related facts:

- (a) bounded-above complexes of flat modules are K-flat;
- (b) a module is flat if and only if all its stalks are flat;
- (c) every module is a quotient of a flat module of the form \(\bigoplus j_{U!}\mathcal O_U\).

*Reference:* [Stacks, Tags 06YD, 05NE and 05NI].

**Lemma 8.2 (making a K-flat resolution termwise surjective).** Let \(P\to G\) be a qis with \(P\) K-flat with flat terms. For a module \(M\) let \(\lambda_M:L(M)=\bigoplus_{(U,s)}j_{U!}\mathcal O_U\to M\), with \(s\) running over \(M(U)\), be the sum of the morphisms \(e_s\) from the proof of Proposition 7.1. It is an epimorphism, since its image contains every section. For \(n\in\mathbb Z\) let \(D_n(M)\) be the complex with \(M\) in degrees \(n\) and \(n+1\) and differential \(\mathrm{id}_M\). Put \(T=\bigoplus_nD_n(L(G^n))\), mapped to \(G\) by \(\lambda_{G^n}\) in degree \(n\) on the summand \(D_n(L(G^n))\). Then \(P\oplus T\to G\) is a qis, surjective in each degree, from a K-flat complex with flat terms.

**Proof.** A chain map \(D_n(M)\to G\) is the same as a map \(\alpha:M\to G^n\): its degree-\((n+1)\) part must be \(d\alpha\), and then the chain condition holds. So \(T\to G\) is a chain map, and it is onto in each degree. The complex \(D_n(M)\) is contractible: the identity from degree \(n+1\) to degree \(n\) is a contracting homotopy. Hence \(T\) is contractible and acyclic. For every complex \(F\), \(\operatorname{Tot}(F\otimes T)\) is contractible, so \(T\) is K-flat. Each module \(L(G^n)\) has free stalks by Lemma 5.2(1), so it is flat by (b). A direct sum of K-flat complexes is K-flat, since \(\operatorname{Tot}\) commutes with direct sums and direct sums of acyclic complexes are acyclic: a direct sum is the filtered colimit of its finite partial sums, and filtered colimits are exact ([Theorem 3.1](#sh-fnd-dc-03)(3)). Finally \(H(P\oplus T)=H(P)\). \(\square\)

**Remark 8.3 (a second route to Theorem 8.1).** Resolve the truncations \(\tau_{\le n}G\) compatibly by bounded-above complexes whose terms are direct sums of the flat modules \(j_{U!}\mathcal O_U\). These are K-flat by (a), and their colimit maps to \(G\) by a qis, surjective in each degree, from a K-flat complex with flat terms, since filtered colimits are exact and preserve K-flatness. [*Flat modules and K-flat resolutions*](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/flat-modules-and-k-flat-resolutions.html), Proposition 4.3, carries out this construction. Flat terms alone do not suffice: Example 1 is an acyclic complex of free modules that is not K-flat.

## 9. The derived tensor product

In this section \(\mathcal O\) is commutative.

**Theorem 9.1 (the derived tensor product).** Let \(F\in D(\mathcal O)\) and choose a K-flat resolution \(P\to F\) (Theorem 8.1). The functor \(G\mapsto\operatorname{Tot}(G\otimes_{\mathcal O}P)\) induces a well-defined exact functor \(-\otimes^L_{\mathcal O}F:D(\mathcal O)\to D(\mathcal O)\) on the unbounded derived category: it preserves quasi-isomorphisms, and it does not depend on \(P\) up to isomorphism. One may instead resolve the variable: for a K-flat resolution \(Q\to G\), both \(\operatorname{Tot}(Q\otimes P)\to\operatorname{Tot}(G\otimes P)\) and \(\operatorname{Tot}(Q\otimes P)\to\operatorname{Tot}(Q\otimes F)\) are quasi-isomorphisms.

*Reference:* [Stacks, Tags 06YA, 06YG and 06YH].

We use Theorem 9.1 without proof. The associativity and symmetry isomorphisms of \(\otimes^L\), with their signs, are checked in the lesson Supporting verifications for open prerequisites.

**Bounded output is a separate question.** Example 4 gives two bounded objects whose derived tensor product has cohomology in every degree \(\leq0\). A finite weak global dimension of \(\mathcal O\) rules this out. Later lessons that need bounded outputs assume that the coefficient ring has finite global dimension.

## 10. Pullback and pushforward are adjoint on unbounded complexes

**Theorem 10.1.** For every morphism \(f:(X,\mathcal O_X)\to(Y,\mathcal O_Y)\) of commutative ringed spaces, \(Lf^*:D(\mathcal O_Y)\to D(\mathcal O_X)\) is left adjoint to \(Rf_*\), bifunctorially.

*Reference:* [Stacks, Tag 079W].

We use Theorem 10.1 without proof. For constant commutative coefficients, the unbounded adjunction is also proved directly in the lesson Supporting verifications for open prerequisites. The next proposition removes commutativity whenever \(\mathcal O_X=f^{-1}\mathcal O_Y\), in particular for constant coefficients.

**Proposition 10.2.** Let \(f:X\to Y\) be continuous, \(\mathcal O_Y\) any sheaf of rings, and \(\mathcal O_X=f^{-1}\mathcal O_Y\). Then \(Rf_*:D(\mathcal O_X)\to D(\mathcal O_Y)\) exists, and there are isomorphisms
\[
\operatorname{Hom}_{D(\mathcal O_X)}(f^{-1}B,E)\cong\operatorname{Hom}_{D(\mathcal O_Y)}(B,Rf_*E),
\tag{10.1}
\]
natural in \(B\in D(\mathcal O_Y)\) and \(E\in D(\mathcal O_X)\). This includes every constant sheaf of a unital ring \(k\), commutative or not.

*Reference:* [Stacks, Tag 079W] needs commutative rings.

**Proof.** Choose a K-injective resolution \(E\to I\) (Theorem 7.2). Then \(Rf_*E=f_*I\), and \(f_*I\) is K-injective by Corollary 7.3(2). Since \(f^{-1}\) is exact ([Theorem 4.1](#sh-fnd-dc-04)(2)), \(f^{-1}B\) represents the derived pullback of \(B\). Maps in the derived category into the K-injective complexes \(I\) and \(f_*I\) are homotopy classes of chain maps, by (H). The adjunction \(f^{-1}\dashv f_*\) of [Theorem 4.1](#sh-fnd-dc-04)(4) holds for complexes and respects homotopies. Together these give
\[
\operatorname{Hom}_D(f^{-1}B,E)=\operatorname{Hom}_K(f^{-1}B,I)\cong\operatorname{Hom}_K(B,f_*I)=\operatorname{Hom}_D(B,Rf_*E).
\]
Naturality in \(B\) and in \(E\) holds because the chain-level adjunction is natural for maps of complexes, and a change of K-injective model is a homotopy equivalence. This proves (10.1). \(\square\)

## 11. Internal derived Hom

In this section \(\mathcal O\) is commutative.

**Theorem 11.1.** (a) For \(L,M\in D(\mathcal O)\), \(R\mathcal Hom(L,M)=\mathcal Hom^\bullet(L,I)\), with \(M\to I\) K-injective, is well defined. (b) \(R\mathcal Hom(K,R\mathcal Hom(L,M))\cong R\mathcal Hom(K\otimes^L L,M)\), functorially. (c) \(R\mathcal Hom(L,M)|_U\cong R\mathcal Hom(L|_U,M|_U)\) for \(U\) open.

*Reference:* [Stacks, Tags 08DH, 08DJ, 08DL and 0A8S].

We use Theorem 11.1 without proof. The chain-level proofs that later lessons rely on are given in the lesson Supporting verifications for open prerequisites: currying, the K-injectivity of \(\mathcal Hom^\bullet(P,I)\) for K-flat \(P\), the adjunction \(\operatorname{Hom}_D(T,R\mathcal Hom(B,C))\cong\operatorname{Hom}_D(T\otimes^LB,C)\), and open restriction.

Two warnings. The output can be unbounded above for bounded inputs (Exercise 4). And for a continuous map that is not an open embedding, the comparison between internal derived Hom and inverse image need not be an isomorphism; see the closing example of Supporting verifications for open prerequisites.

## 12. The composition map

In this section \(\mathcal O\) is commutative.

**Theorem 12.1.** For \(K,L,M\in D(\mathcal O)\) there is a canonical morphism
\[
c_{K,L,M}:R\mathcal Hom(L,M)\otimes^L R\mathcal Hom(K,L)\longrightarrow R\mathcal Hom(K,M).
\]

*Reference:* [Stacks, Tag 0A8V], which calls \(c\) functorial in \(K,L,M\) and leaves out the proof of functoriality; in \(L\) this can only mean dinaturality, as explained below.

The morphism \(c\) is induced by the composition of Hom complexes. Its properties are proved in the lesson Supporting verifications for open prerequisites: \(c\) is the transpose of evaluating into \(L\) and then into \(M\); it is associative and unital; and it is natural in \(K\) and \(M\).

In \(L\) the right notion is dinaturality, which is also proved there. The object \(L\) occurs covariantly in one factor and contravariantly in the other, so the domain of \(c\) is not a functor of \(L\), and "natural in \(L\)" has no meaning.

## 13. The localization triangle, and signs

For a locally closed \(W\subset X\), \(\Gamma_W:\operatorname{Mod}(\mathcal O)\to\operatorname{Mod}(\mathcal O)\) is the sheaf of sections supported in \(W\) (Section 1). It is a left exact additive functor, and \(R\Gamma_W\) denotes its right derived functor on \(D(\mathcal O)\) (Theorem 7.2).

**Theorem 13.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\), \(Z\subset X\) locally closed, and \(Z'\subset Z\) closed in \(Z\). For \(K\in D(\mathcal O)\) there is a distinguished triangle
\[
R\Gamma_{Z'}K\longrightarrow R\Gamma_ZK\longrightarrow R\Gamma_{Z\setminus Z'}K\longrightarrow R\Gamma_{Z'}K[1],
\tag{13.1}
\]
functorial in \(K\). The first two arrows come from the inclusion of supports and from restriction. The third is the connecting morphism of the triangle (T) attached to the termwise exact sequence (13.2) below.

*Reference:* [Stacks, Tag 0G72] proves Corollary 13.2 for commutative \(\mathcal O\).

**Proof.** Let \(K\to I\) be as in Theorem 7.2: \(I\) is K-injective with injective terms. Each \(I^n\) is flabby (Corollary 5.5(1)). For a flabby sheaf \(F\), the sequence
\[
0\to\Gamma_{Z'}F\to\Gamma_ZF\to\Gamma_{Z\setminus Z'}F\to0
\tag{13.2}
\]
is exact by (Γ), a statement about sheaves of abelian groups. Here all terms are \(\mathcal O\)-modules (a section of \(\Gamma_WF\) is a section of \(F\) over an open set, supported in \(W\), and \(\mathcal O\) acts through restriction), and the maps are \(\mathcal O\)-linear. Exactness in \(\operatorname{Mod}(\mathcal O)\) is checked on stalks, as for abelian sheaves ([Theorem 2.1](#sh-fnd-dc-02)(4)), so (13.2) is exact in \(\operatorname{Mod}(\mathcal O)\). Applying (13.2) to each \(I^n\) gives a termwise exact sequence of complexes. By (T) it yields a distinguished triangle in \(D(\mathcal O)\). By Theorem 7.2, \(R\Gamma_W K=\Gamma_W(I)\) for each \(W\). This gives (13.1).

For functoriality, let \(u:K\to K'\) in \(D(\mathcal O)\), with resolution \(K'\to I'\). Since \(I'\) is K-injective, \(\operatorname{Hom}_D(I,I')=\operatorname{Hom}_K(I,I')\) by (H). So \(u\) is represented by a chain map \(\tilde u:I\to I'\), unique up to homotopy. Applying the three functors to \(\tilde u\) gives a morphism of termwise exact sequences, hence a morphism of the triangles; the triangle of (T) is natural for such morphisms. Homotopic chain maps give equal maps in \(D\) on each term. The same argument shows that another choice of \(I\) gives an isomorphic triangle. \(\square\)

**Corollary 13.2 (a closed set and its open complement).** Let \(Z\) be closed and \(j:U=X\setminus Z\hookrightarrow X\). For \(K\in D(\mathcal O)\) there is a distinguished triangle
\[
R\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^{-1}K\longrightarrow R\Gamma_ZK[1],
\tag{13.3}
\]
functorial in \(K\).

**Proof.** Apply Theorem 13.1 to the pair \((X,Z)\). Here \(\Gamma_X=\mathrm{id}\), \(X\setminus Z=U\), and \(\Gamma_U=j_*j^{-1}\) (Section 1). With \(I\) as in the proof, \(\Gamma_U(I)=j_*(I|_U)\). By Corollary 7.3(1), \(I|_U\) is K-injective, and it is a resolution of \(j^{-1}K\) because \(j^{-1}\) is exact. So \(j_*(I|_U)=Rj_*(j^{-1}K)\). \(\square\)

For bounded-below \(K\), Corollary 7.3(3) shows that (13.1) can also be computed with a bounded-below injective resolution. The sign of its third arrow depends on a convention, discussed next.

**Lemma 13.3 (the sign of the connecting morphism).** Let \(0\to A\xrightarrow{a}B\xrightarrow{b}C\to0\) be a termwise exact sequence of complexes in an abelian category. Let \(\operatorname{Cone}(a)^n=B^n\oplus A^{n+1}\) with \(d(y,x)=(dy+a(x),-dx)\), and let \(p(y,x)=x\) and \(q(y,x)=b(y)\), so that \(p:\operatorname{Cone}(a)\to A[1]\) and \(q:\operatorname{Cone}(a)\to C\) is a qis. Let \(\delta:H^n(C)\to H^{n+1}(A)\) be the connecting map: for a cycle \(z\), choose \(y\) with \(b(y)=z\) and the \(x\) with \(a(x)=dy\), and set \(\delta[z]=[x]\). Then
\[
H^n(p)\circ H^n(q)^{-1}=-\delta .
\tag{13.4}
\]
Two conventions for distinguished triangles are in use. For a chain map \(f:A\to B\), form \(\operatorname{Cone}(f)\) in the same way, with the inclusion \(i:B\to\operatorname{Cone}(f)\) and the projection \(p:\operatorname{Cone}(f)\to A[1]\). The *first convention* declares distinguished the triangles isomorphic to some \((f,i,p)\); the *second convention* declares distinguished those isomorphic to some \((f,i,-p)\). [Schapira HA, Definition 6.3.1] uses the first; [Stacks] and this lesson use the second. Under the second convention, the triangle attached to the sequence has third arrow \(-p\circ q^{-1}\), which by (13.4) induces \(+\delta\) on cohomology. Under the first, it has third arrow \(p\circ q^{-1}\), which induces \(-\delta\). More generally, the distinguished triangles of the first convention are exactly those of the second with the third arrow negated. Equivalently, by Exercise 5(i), the triangles of the second convention are the *antidistinguished* triangles of the first: those that become distinguished for the first convention when all three arrows are negated.

**Proof.** Let \(z\), \(y\), \(x\) be as stated. Then \(a(dx)=d\,dy=0\), so \(dx=0\), because \(a\) is injective. The element \((y,-x)\) is a cycle of \(\operatorname{Cone}(a)\), since \(d(y,-x)=(dy-a(x),dx)=(0,0)\). Also \(q(y,-x)=z\) and \(p(y,-x)=-x\). So \(H^n(p)H^n(q)^{-1}[z]=[-x]=-\delta[z]\). For the comparison of the two conventions, let \((\varphi_1,\varphi_2,\varphi_3)\) be an isomorphism of triangles from \((f,i,p)\) to \((u,v,w)\). Then the same maps give an isomorphism from \((f,i,-p)\) to \((u,v,-w)\). So the two classes differ exactly by the sign of the third arrow, in \(K(\mathcal A)\) and hence in \(D(\mathcal A)\). \(\square\)

**Remark 13.4 (working with both conventions).** When a formula taken from a text that uses the first convention contains the third arrow of a triangle, for instance a connecting morphism of a triangle of derived functors, negate that arrow before combining it with (13.3). Negating two arrows of a triangle gives an isomorphic triangle, so it is enough to track one sign per triangle (Exercise 5).

## 14. Worked examples

**Example 1 (a two-periodic complex: injective and free terms, acyclic, yet neither K-injective nor K-flat).** Let \(R=\mathbb Z/4\) and let \(C\) be the complex with \(C^n=R\) for all \(n\) and every differential equal to multiplication by \(2\).

- *\(C\) is acyclic.* The kernel of multiplication by \(2\) is \(\{0,2\}\), which is also its image.
- *Its terms are free and injective.* \(R\) is free over itself. It is injective by Baer's criterion (B): its ideals are \(0\), \((2)\) and \(R\), and a linear map \((2)\to R\) sends \(2\) to some \(c\) with \(2c=0\), that is \(c\in\{0,2\}\); it extends to \(R\) by \(1\mapsto0\) or \(1\mapsto1\).
- *\(C\) is not contractible.* A homotopy \(s\) is multiplication by elements \(s_n\in R\) in each degree, and \((ds+sd)^n=2s_n+2s_{n+1}\) lies in \(2R\). It is never \(1\). So \(\mathrm{id}_C\neq0\) in \(K(R)\).
- *\(C\) is not K-injective.* \(C\) is acyclic, but \(\operatorname{Hom}_{K(R)}(C,C)\ni\mathrm{id}_C\neq0\). So the lower bound in Lemma 6.2 cannot be dropped, and neither can the finite-dimension hypothesis in Remark 7.4: \(R\) has infinite global dimension (Exercise 4).
- *\(C\) is not K-flat.* Suppose it were. Let \(M\) be any complex and \(P\to M\) a K-flat resolution. The cone of \(P\to M\) is acyclic, so its tensor product with the K-flat \(C\) is acyclic, and \(\operatorname{Tot}(P\otimes C)\to\operatorname{Tot}(M\otimes C)\) is a qis. And \(\operatorname{Tot}(P\otimes C)\) is acyclic, since \(P\) is K-flat and \(C\) is acyclic. So \(M\otimes C\) would be acyclic for every \(M\). But for \(M=\mathbb Z/2\) in degree \(0\), \(M\otimes C\) has \(\mathbb Z/2\) in each degree and zero differentials, so its cohomology is \(\mathbb Z/2\) in every degree. So flat, even free, terms do not make a complex K-flat.

*Sheaf versions.* On any nonempty space \(X\) with \(\mathcal O=R_X\), the complex of constant sheaves \(C_X\) is acyclic with flat terms, and \((\mathbb Z/2)_X\otimes C_X\) has cohomology sheaves \((\mathbb Z/2)_X\) in every degree; so it is not K-flat. For \(x\in X\), the skyscraper complex \(x_*C\) has injective terms (Lemma 5.3) and is acyclic, since \(x_*\) is exact on sections. If \(\mathrm{id}_{x_*C}\) were null-homotopic, taking stalks at \(x\) would make \(\mathrm{id}_C\) null-homotopic. So \(x_*C\) is an acyclic complex of injective sheaves that is not K-injective: an unbounded complex of injectives need not be K-injective.

**Example 2 (sections do not commute with infinite sums).** Let \(X=\mathbb N\) with the discrete topology, \(k\neq0\) a ring, and \(F_n=n_*k\), the skyscraper at the point \(n\). On a discrete space, a sheaf is determined by its stalks, and its global sections are the families of stalk elements. The stalk of \(\bigoplus_nF_n\) at \(m\) is \(k\), coming from \(F_m\) alone. So
\[
\Gamma\Bigl(X,\bigoplus_nF_n\Bigr)=\prod_{m\in\mathbb N}k,\qquad \bigoplus_n\Gamma(X,F_n)=\bigoplus_{n\in\mathbb N}k ,
\]
and the canonical map is the inclusion of finitely supported sequences, which is not onto. \(X\) is not quasi-compact. On a finite discrete space the map is bijective, as [Theorem 3.1](#sh-fnd-dc-03)(5) predicts.

**Example 3 (products of sheaves are not exact).** Let \(X=\mathbb R\), \(k\neq0\), \(U_n=(-1/n,1/n)\) for \(n\geq1\), \(A_n=j_{U_n!}k_{U_n}\), and \(B=0_*k\), the skyscraper at \(0\). Let \(\varphi_n:A_n\to B\) correspond under Lemma 5.2(2) to evaluation at \(0\) of locally constant functions on open sets of \(U_n\). At \(0\) it is the identity of \(k\); at other points the target stalk is \(0\). So each \(\varphi_n\) is an epimorphism. Now look at \(\prod_n\varphi_n\) at \(0\). The target stalk is \(\prod_nk\), because \((\prod_nB)(V)=\prod_nk\) when \(0\in V\). A germ of the domain is represented on some \(V=(-\varepsilon,\varepsilon)\) by a family \((s_n)\) with \(s_n\in A_n(V)\). If \(n>1/\varepsilon\), then \(U_n\subsetneq V\), and \(s_n\) is a constant \(c\) on the connected set \(U_n\) whose support must be closed in \(V\). The support \(U_n\) is not closed in \(V\), so \(c=0\). Hence the image of the germ has only finitely many nonzero coordinates. The stalk map lands in \(\bigoplus_nk\subsetneq\prod_nk\), so \(\prod_n\varphi_n\) is not an epimorphism.

**Example 4 (a derived tensor product with unbounded output).** Let \(R=\mathbb Z/4\). The complex \(P:\ \cdots\to R\xrightarrow{2}R\xrightarrow{2}R\to0\), with the last \(R\) in degree \(0\), maps to \(\mathbb Z/2\) (in degree \(0\)) by reduction mod \(2\). This is a qis: the kernel of reduction is \(\{0,2\}=2R\), which is the image of the last map, and each other kernel equals the next image, as in Example 1. \(P\) is a bounded-above complex of free modules, so it is K-flat by fact (a) of Section 8. Hence \(\mathbb Z/2\otimes^L_R\mathbb Z/2=\mathbb Z/2\otimes_RP\), the complex \(\cdots\to\mathbb Z/2\xrightarrow{0}\mathbb Z/2\to0\). Its cohomology is \(\mathbb Z/2\) in every degree \(\leq0\). Both inputs are bounded, and the output is not. With constant sheaves on any nonempty \(X\), the same computation holds for \(\mathcal O=R_X\).

**Example 5 (inverse image versus module pullback).** Let \(X=Y\) be a point, \(\mathcal O_Y=\mathbb Z\) and \(\mathcal O_X=\mathbb Z/2\), with the ring map \(\mathbb Z\to\mathbb Z/2\). Then \(f^{-1}\) is the identity on abelian groups, but the module pullback is \(f^*M=\mathbb Z/2\otimes_{\mathbb Z}M\). It sends the exact sequence \(0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z/2\to0\) to \(\mathbb Z/2\xrightarrow{0}\mathbb Z/2\to\mathbb Z/2\to0\), whose first map is not injective. For constant sheaves of rings, \(\mathcal O_X=f^{-1}\mathcal O_Y\), so \(f^*=f^{-1}\) is exact (Theorem 4.1).

**Example 6 (the localization triangle on the Sierpiński space).** Let \(S=\{o,c\}\) with open sets \(\emptyset\), \(\{o\}\) and \(S\). The point \(c\) is closed and \(o\) is open. Let \(k\) be a ring and \(\mathcal O=k_S\).

- *Sheaves.* An open cover of \(S\) contains \(S\) itself, and an open cover of \(\{o\}\) contains \(\{o\}\). So every presheaf with \(F(\emptyset)=0\) is a sheaf. A sheaf is a \(k\)-linear map \(r:M\to N\), with \(M=F(S)\) and \(N=F(\{o\})\), and a morphism is a commuting square. The stalks are \(F_c=M\) and \(F_o=N\), because the smallest open neighbourhoods are \(S\) and \(\{o\}\).
- *Operations.* Let \(Z=\{c\}\), \(U=\{o\}\) and \(j:U\hookrightarrow S\). Then \(j^{-1}F=N\), \(j_*N=(N\xrightarrow{\mathrm{id}}N)\), and \(\Gamma_ZF=(\ker r\to0)\), since a section over \(\{o\}\) supported in \(Z\) is zero. The map \(F\to j_*j^{-1}F\) is \((r,\mathrm{id}_N)\). The functor \(j_*\) is exact, so \(Rj_*j^{-1}F=j_*j^{-1}F\).
- *Flabbiness.* \(F\) is flabby if and only if \(r\) is onto. The sequence \(0\to\Gamma_ZF\to F\to j_*j^{-1}F\to0\) is \(0\to\ker r\to M\xrightarrow{r}N\) over \(S\) and \(0\to0\to N\to N\to0\) over \(\{o\}\). It is exact on the right exactly when \(r\) is onto, as (13.2) predicts for flabby sheaves.
- *The triangle.* By (13.3) and its long exact sequence of cohomology sheaves,
\[
0\to H^0R\Gamma_ZF\to F\xrightarrow{(r,\mathrm{id})}j_*j^{-1}F\to H^1R\Gamma_ZF\to0,
\]
and \(H^qR\Gamma_ZF=0\) for \(q\neq0,1\). So \(H^0R\Gamma_ZF=(\ker r\to0)\) and \(H^1R\Gamma_ZF=(\operatorname{coker}r\to0)\), both concentrated at the closed point. With the second sign convention of Section 13, the map \(j_*j^{-1}F\to H^1R\Gamma_ZF\) is the connecting map \(\delta\) of Lemma 13.3 for (13.2) applied to a resolution \(I\) of \(F\); with the first convention it is \(-\delta\).

## Exercises

**Exercise 1 (stalks as left adjoints).** Let \(x\in X\). Show that \(F\mapsto F_x\) is left adjoint to \(J\mapsto x_*J\), and deduce that stalks commute with all colimits in \(\operatorname{Mod}(\mathcal O)\).

*Solution.* The adjunction is (5.2), natural in both variables (Lemma 5.3). For a diagram \((F_i)\) and every \(\mathcal O_x\)-module \(J\),
\[
\operatorname{Hom}\bigl((\varinjlim F_i)_x,J\bigr)\cong\operatorname{Hom}\bigl(\varinjlim F_i,x_*J\bigr)\cong\varprojlim\operatorname{Hom}(F_i,x_*J)\cong\varprojlim\operatorname{Hom}((F_i)_x,J)\cong\operatorname{Hom}\bigl(\varinjlim(F_i)_x,J\bigr),
\]
naturally in \(J\). By the Yoneda lemma, \((\varinjlim F_i)_x\cong\varinjlim(F_i)_x\). Tracing the identity of \(\varinjlim(F_i)_x\) through the chain shows that this isomorphism is inverse to the canonical map \(\varinjlim(F_i)_x\to(\varinjlim F_i)_x\). This is a second proof of the stalk formula in [Theorem 3.1](#sh-fnd-dc-03)(2).

**Exercise 2 (three forms of a generator).** Let \(\mathcal C\) be an abelian category with direct sums and \(G\) an object. Show that these are equivalent: (a) for every \(N\subsetneq M\) some morphism \(G\to M\) does not factor through \(N\); (b) \(\operatorname{Hom}(G,-)\) is faithful; (c) every object receives an epimorphism from a direct sum of copies of \(G\).

*Solution.* (c)\(\Rightarrow\)(a): let \(\pi:G^{(I)}\to M\) be an epimorphism. If every \(G\to M\) factored through \(N\), so would every component of \(\pi\), hence \(\pi\) itself. Then \(M=\operatorname{Im}\pi\subset N\), so \(N=M\). (a)\(\Rightarrow\)(b): if \(\varphi:M\to M'\) is nonzero, then \(\operatorname{Ker}\varphi\subsetneq M\). So some \(g:G\to M\) does not factor through \(\operatorname{Ker}\varphi\), that is, \(\varphi g\neq0\). (b)\(\Rightarrow\)(c): let \(\pi:\bigoplus_{g\in\operatorname{Hom}(G,M)}G\to M\) be the sum of all \(g\), and \(q:M\to\operatorname{Coker}\pi\). Every \(g\) factors through \(\pi\), so \(qg=0\) for all \(g\). By (b), \(q=0\). So \(\pi\) is an epimorphism. For \(\mathcal C=\operatorname{Mod}(\mathcal O)\) and \(G=\bigoplus_Uj_{U!}\mathcal O_U\), Proposition 7.1 checks all three directly.

**Exercise 3 (injectives on the Sierpiński space).** In Example 6, let \(k\) be a field. Show that \((r:M\to N)\) is injective in \(\operatorname{Mod}(k_S)\) if and only if \(r\) is onto. Show that \(j_!k\) is not injective.

*Solution.* If the sheaf is injective, it is flabby (Corollary 5.5(1)), so \(r\) is onto. Conversely let \(r\) be onto and \(K=\ker r\). Over a field, \(M\cong K\oplus N\) compatibly with \(r\). So the sheaf is the sum of \((K\to0)=c_*K\) and \((N\xrightarrow{\mathrm{id}}N)=j_*N\). A sum of two injectives is injective. The first is injective by Lemma 5.3, as every vector space is injective. For the second, a morphism \((s:A\to B)\to(N\xrightarrow{\mathrm{id}}N)\) is a pair \((\alpha,\beta)\) with \(\beta s=\alpha\), so it is determined by \(\beta:B\to N\). Hence \(\operatorname{Hom}(-,j_*N)\cong\operatorname{Hom}_k((-)_o,N)\), which is exact because stalks are exact and \(N\) is injective over \(k\). Finally \(j_!k=(0\to k)\) by Lemma 5.2: a section over \(S\) would need support closed in \(S\) and contained in \(\{o\}\), and \(\{o\}\) is not closed. Its \(r\) is not onto, so \(j_!k\) is not injective. Extension by zero does not preserve injectives.

**Exercise 4 (unbounded \(R\operatorname{Hom}\)).** Let \(R=\mathbb Z/4\). Compute \(\operatorname{Ext}^i_R(\mathbb Z/2,\mathbb Z/2)\) for all \(i\).

*Solution.* Embed \(\mathbb Z/2\) in \(R\) by \(1\mapsto2\). The sequence \(0\to\mathbb Z/2\to R\xrightarrow{2}R\xrightarrow{2}R\to\cdots\) is exact, as in Example 1, and its terms are injective (Example 1). So it is an injective resolution, bounded below, hence K-injective (Lemma 6.2), and it computes \(R\operatorname{Hom}_R(\mathbb Z/2,\mathbb Z/2)\). A linear map \(\mathbb Z/2\to R\) sends \(1\) to an element killed by \(2\), that is to \(0\) or \(2\). So \(\operatorname{Hom}_R(\mathbb Z/2,R)\cong\mathbb Z/2\), and multiplication by \(2\) acts on it as \(0\), since \(2\cdot2=0\). The Hom complex is \(\mathbb Z/2\xrightarrow{0}\mathbb Z/2\xrightarrow{0}\cdots\) in degrees \(0,1,2,\ldots\). Hence \(\operatorname{Ext}^i_R(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2\) for every \(i\geq0\), and \(0\) for \(i<0\). Two bounded inputs give an output that is unbounded above, and \(R\) has infinite global dimension. On a one-point space the same computation is a statement about sheaves.

**Exercise 5 (signs of triangles).** Let \((u,v,w)\) be a distinguished triangle \(X\to Y\to Z\to X[1]\) in a triangulated category. (i) Show that \((u,-v,-w)\), \((-u,v,-w)\) and \((-u,-v,w)\) are isomorphic to \((u,v,w)\), hence distinguished. (ii) Show that the identity functor of \(K(\mathcal A)\), with the natural isomorphism \(-\mathrm{id}\) between the shift and itself, is a triangulated equivalence from the structure of the first sign convention of Section 13 to that of the second.

*Solution.* (i) An isomorphism of triangles \((a,b,c)\) from \((u,v,w)\) produces the triangle \((bua^{-1},cvb^{-1},a[1]wc^{-1})\). Taking \((a,b,c)=(1,1,-1)\), \((-1,1,1)\) and \((1,-1,1)\) gives the three triangles, in this order. (ii) A triangulated functor is a pair \((\Phi,\xi)\) with \(\xi:\Phi\circ[1]\cong[1]\circ\Phi\), and it sends \((u,v,w)\) to \((\Phi u,\Phi v,\xi\circ\Phi w)\). With \(\Phi=\mathrm{id}\) and \(\xi=-\mathrm{id}\), it sends \((u,v,w)\) to \((u,v,-w)\). By Lemma 13.3 this maps the distinguished triangles of the first convention exactly onto those of the second. The same pair also maps the triangles of the second convention onto those of the first, so it is a triangulated equivalence whose inverse has the same form. Negating one arrow is not the same as negating two. For example, in \(D(\mathbb Z/9)\) let \((u,v,w)\) be the triangle of the exact sequence \(0\to\mathbb Z/3\to\mathbb Z/9\to\mathbb Z/3\to0\). If \((u,v,-w)\) were distinguished for the same structure, a morphism of triangles \((1,1,c)\) from \((u,v,w)\) would exist. Then \(cv=v\) forces \(c=1\), since \(v\) is onto and \(\operatorname{End}(\mathbb Z/3)=\mathbb Z/3\); and then \(-w=w\), so \(2w=0\). But \(w\neq0\) in \(\operatorname{Ext}^1(\mathbb Z/3,\mathbb Z/3)\cong\mathbb Z/3\), because the sequence does not split, and \(2\) is invertible modulo \(3\).

## Where this leads

- *Noncommutative coefficients.* The lesson Continuing cohomology through a moving boundary uses Theorems 2.1 and 6.1 for sheaves of modules over a noncommutative ring \(k\).
- *Acyclic resolutions.* The lesson Comparing sheaves through local support tests computes derived functors with acyclic resolutions, as in Theorem 6.1(4).
- *Unique lifts.* The lesson Proper-support composition through a change of base uses the lifts of Theorem 6.1(2), unique up to homotopy.
- *The unbounded layer.* The course *Microlocal Sheaves* uses the unbounded constructions of Sections 7–13 as its ordinary categorical layer: K-injective resolutions, the derived tensor product and Hom, the composition map, and the localization triangle with the second sign convention.

## References

- [Stacks] The Stacks project authors, *The Stacks project*, 2026, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
- [Spaltenstein 1988] N. Spaltenstein, Resolutions of unbounded complexes, *Compositio Mathematica* 65 (1988), no. 2, 121–154, open at [numdam.org](https://www.numdam.org/item/CM_1988__65_2_121_0/).
- [Schapira HA] P. Schapira, *An Introduction to Categories and Homological Algebra*, lecture notes, 2026, [author's notes](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/HA.pdf).
- [Schapira SHV] P. Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, lecture notes, 2026, [author's notes](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf).
