# Cohomology of total topoi

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A sheaf on the total topos of a fibred topos is a family of sheaves on the levels, tied together by transition maps. Its cohomology is built from the cohomology of the levels. Restriction to all levels at once is a morphism of topoi from the product of the levels to the total topos. Its adjunction gives the standard resolutions, and it supplies enough sheaves that are acyclic on every level. A second resolution, indexed by the strings of composable arrows of the index category, identifies the derived direct image to a topos with an explicit complex: in degree \(n\), it is the product, over the strings of \(n\) arrows, of the direct images from the first level of the string. For the punctual topos, this is the classical complex computing the derived functors of an inverse limit. Three consequences follow: a spectral sequence from derived limits of the cohomology of the levels to the cohomology of the total topos; the cohomology of a total topos over a category with a final object is that of the final level; and derived direct images under a morphism of fibred topoi over a fixed index category are computed level by level.

**Prerequisites.** [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) and [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); Lemma 2.2 of [*Strict simplicial objects and Deligne's contractibility theorem*](strict-simplicial-objects-and-deligne-s-contractibility-theorem.md); totally acyclic sheaves [[Stacks, Tag 072Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-limp)]; standard resolutions of an adjunction [[Stacks, Tag 08N8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-standard)]; spectral sequences of double complexes [[Stacks, Tag 0132](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-first-quadrant-ss)].

Notation is that of the lesson on fibred topoi. \(X\) is a topos fibred over a small category \(I\), with morphisms of topoi \(X_f=(f^*,f_*)\colon X_i\to X_j\) for \(f\colon i\to j\). The transitivity isomorphisms are not written. An *abelian sheaf* on \(\operatorname{Top}(X)\) is an abelian group object: a family of abelian sheaves \(E_i\) on the levels with additive maps \(E_f\colon f^*E_j\to E_i\). Kernels and cokernels are computed levelwise (Proposition 2.2 of the lesson on fibred topoi). So the abelian sheaves form an abelian category \(\operatorname{Ab}(\operatorname{Top}(X))\), and a sequence is exact if and only if it is exact at every level. For a topos \(T\), \(\operatorname{Ab}(T)\) is the category of abelian sheaves on \(T\).

## 1. The discrete topos and totally acyclic sheaves

Let \(X^{\mathrm{dis}}=\prod_{i\in\operatorname{Ob}I}X_i\) be the product of the levels. Its objects are the families \(L=(L_i)\) with \(L_i\in X_i\). It is the total topos of the restriction of \(X\) to the discrete category on \(\operatorname{Ob}I\), hence a topos by Theorem 4.2 of the lesson on fibred topoi.

**Lemma 1.1.** For \(E\in\operatorname{Top}(X)\) and \(L\in X^{\mathrm{dis}}\), put \(e^*E=(E_i)_i\) and
\[
\begin{gathered}e_*L=\prod_i i_*(L_i),\\ e_!L=\coprod_i i_!(L_i).\end{gathered}
\]

1. \(e_!\) is left adjoint and \(e_*\) is right adjoint to \(e^*\). So \(e=(e^*,e_*)\) is a morphism of topoi \(X^{\mathrm{dis}}\to\operatorname{Top}(X)\), and
\[
(e_*L)_j=\prod_i\prod_{f\colon i\to j}f_*L_i .
\]
2. On abelian sheaves, \(e^*\) is exact and conservative, and it has an exact left adjoint \(e^{\mathrm{ab}}_!\), with
\[
(e^{\mathrm{ab}}_!L)_j=\bigoplus_i\bigoplus_{f\colon j\to i}f^*L_i .
\]
Hence \(e^*\) and every level functor \(i^*\) carry injective abelian sheaves to injective abelian sheaves.

**Proof.** (1) By Proposition 3.1 of the lesson on fibred topoi, \(\operatorname{Hom}(i_!L_i,E)=\operatorname{Hom}(L_i,E_i)\) and \(\operatorname{Hom}(E,i_*L_i)=\operatorname{Hom}(E_i,L_i)\). Taking the product over \(i\) gives the two adjunctions. A functor with a left and a right adjoint preserves limits and colimits, so \(e^*\) is exact and \((e^*,e_*)\) is a morphism of topoi. Products in \(\operatorname{Top}(X)\) are computed levelwise, so the formula for the levels of \(e_*L\) is the formula for \(i_*\) in Proposition 3.1.

(2) Exactness of \(e^*\) is the levelwise computation of kernels and cokernels. If every component \(u_i\) of a morphism \(u\colon E\to E'\) is an isomorphism, the inverses \(u_i^{-1}\) are compatible with the maps \(E_f\) and \(E'_f\), so \(u\) is an isomorphism. The proof of Proposition 3.1 (1) of the lesson on fibred topoi, with direct sums of abelian sheaves in place of coproducts, shows that
\[
i^{\mathrm{ab}}_!(L)_j=\bigoplus_{f\colon j\to i}f^*L
\]
defines a left adjoint of \(i^*\) on abelian sheaves. It is exact, because every \(f^*\) is exact and direct sums of abelian sheaves are exact. Summing over \(i\) gives \(e^{\mathrm{ab}}_!\). A functor with an exact left adjoint carries injectives to injectives [Stacks, Tag 015Z]. \(\square\)

**Definition 1.2.** Let \(T\) be a topos. For \(K\in T\) and \(F\in\operatorname{Ab}(T)\), write \(F(K)=\operatorname{Hom}_T(K,F)\), and let \(H^p(K,F)\) be the right derived functors of \(F\mapsto F(K)\). An abelian sheaf \(F\) is *totally acyclic* if \(H^p(K,F)=0\) for every object \(K\) of \(T\) and every \(p\geq1\) [Stacks, Tag 072Y].

In SGA 4, Exposé V, totally acyclic sheaves are called flasque.

**Lemma 1.3.** Let \(T\) be a topos.

1. Injective abelian sheaves are totally acyclic.
2. Let \(g\colon T\to T'\) be a morphism of topoi and \(F\) a totally acyclic sheaf on \(T\). Then \(R^qg_*F=0\) for \(q\geq1\), and \(g_*F\) is totally acyclic.
3. A product \(\prod_\alpha F_\alpha\) of totally acyclic sheaves is totally acyclic, and \(H^p(K,\prod_\alpha F_\alpha)=\prod_\alpha H^p(K,F_\alpha)\) for every \(K\) and \(p\).
4. In an exact sequence \(0\to F'\to F\to F''\to0\) with \(F'\) and \(F\) totally acyclic, \(F''\) is totally acyclic. A product of exact sequences \(0\to F'_\alpha\to F_\alpha\to F''_\alpha\to0\) in which every \(F'_\alpha\) is totally acyclic is exact.
5. Let \((C_\alpha)\) be a family of exact complexes of totally acyclic sheaves, all zero below a fixed degree. Then \(\prod_\alpha C_\alpha\) is exact, and \(g_*C_\alpha\) is exact for every morphism of topoi \(g\) with source \(T\).

**Proof.** (1) The derived functors of \(F\mapsto F(K)\) vanish on injectives in positive degrees.

(2) The vanishing of \(R^qg_*F\) is [Stacks, Tag 0731]. For \(K\in T'\), adjunction gives \((g_*F)(K)=F(g^*K)\). So \(F\mapsto F(g^*K)\) is the composite of \(g_*\) with the sections over \(K\). The functor \(g_*\) carries injectives to injectives, its left adjoint \(g^*\) being exact. By [Stacks, Tag 015M], the derived functor of the composite is the composite of the derived functors. Since \(Rg_*F=g_*F\), this gives \(H^p(K,g_*F)=H^p(g^*K,F)=0\) for \(p\geq1\).

(3) Choose injective resolutions \(F_\alpha\to I^\bullet_\alpha\) and put \(I^\bullet=\prod_\alpha I^\bullet_\alpha\), a complex of injectives. For every \(K\), \(I^\bullet(K)=\prod_\alpha I^\bullet_\alpha(K)\), so \(H^p(I^\bullet(K))=\prod_\alpha H^p(K,F_\alpha)\), which vanishes for \(p\geq1\). Let \(p\geq1\). A section over \(K\) of the kernel of \(I^p\to I^{p+1}\) is a cycle of \(I^\bullet(K)\), hence the image of a section of \(I^{p-1}\) over \(K\). So \(I^\bullet\) is exact in positive degrees. Its kernel in degree \(0\) is \(\prod_\alpha F_\alpha\). Therefore \(I^\bullet\) is an injective resolution of \(\prod_\alpha F_\alpha\), and \(H^p(K,\prod_\alpha F_\alpha)\) is \(H^p(I^\bullet(K))=\prod_\alpha H^p(K,F_\alpha)\).

(4) The first assertion follows from the exact sequences
\[
\begin{gathered}H^p(K,F)\to H^p(K,F'')\\ \to H^{p+1}(K,F').\end{gathered}
\] The product of the sequences is exact at its first two places, since products are left exact. For every \(K\), the map \(F_\alpha(K)\to F''_\alpha(K)\) is surjective, as \(H^1(K,F'_\alpha)=0\). So every section of \(\prod_\alpha F''_\alpha\) over every \(K\) lifts to \(\prod_\alpha F_\alpha\), and the last map is an epimorphism.

(5) Let every \(C_\alpha\) vanish below degree \(a\), and let \(Z^q_\alpha\) be the kernel of \(C^q_\alpha\to C^{q+1}_\alpha\). The sequences \(0\to Z^q_\alpha\to C^q_\alpha\to Z^{q+1}_\alpha\to0\) are exact, and \(Z^a_\alpha=0\). By the first part of (4) and induction on \(q\), every \(Z^q_\alpha\) is totally acyclic. By the second part of (4), the products of these sequences are exact, and this is the exactness of \(\prod_\alpha C_\alpha\). By (2), \(R^1g_*Z^q_\alpha=0\), so the sequences stay exact after applying \(g_*\), and \(g_*C_\alpha\) is exact. \(\square\)

**Proposition 1.4.**

1. Let \(L\in\operatorname{Ab}(X^{\mathrm{dis}})\) have totally acyclic components \(L_i\). Then \(e_*L\) is totally acyclic, and so is every level \((e_*L)_j\).
2. Every abelian sheaf on \(\operatorname{Top}(X)\) is a subsheaf of a sheaf \(e_*L\) with \(L\) injective. Such a sheaf \(e_*L\) is injective, and its levels are totally acyclic.
3. Let \(A\) be a ring of \(\operatorname{Top}(X)\) (Section 4 of the lesson on morphisms of fibred topoi), so that every \(X_f\) underlies a morphism of ringed topoi \((X_i,A_i)\to(X_j,A_j)\). If all these morphisms are flat, every \(A\)-module is a submodule of an injective \(A\)-module whose levels are injective modules.

**Proof.** (1) By Lemma 1.1, the levels are products of sheaves \(f_*L_i\), which are totally acyclic by Lemma 1.3 (2), (3). Next we show \(R^qe_*L=0\) for \(q\geq1\). Choose an injective resolution \(L\to J^\bullet\) in \(X^{\mathrm{dis}}\), that is, a family of injective resolutions \(L_i\to J^\bullet_i\). Since every level functor is exact, the level \(j\) of the cohomology of \(e_*J^\bullet\) is the cohomology of
\[
(e_*J^\bullet)_j=\prod_i\prod_{f\colon i\to j}f_*J^\bullet_i .
\]
The augmented complexes \(0\to L_i\to J^\bullet_i\) are exact complexes of totally acyclic sheaves. By Lemma 1.3 (5), the complexes \(0\to f_*L_i\to f_*J^\bullet_i\) and their product are exact. Hence \(R^qe_*L=0\) for \(q\geq1\). As in the proof of Lemma 1.3 (2), it follows that \(H^p(K,e_*L)=H^p(e^*K,L)\) for every \(K\in\operatorname{Top}(X)\). In the product topos, \(\operatorname{Hom}(M,N)=\prod_i\operatorname{Hom}(M_i,N_i)\), and injective resolutions are taken componentwise. So \(H^p(e^*K,L)=\prod_iH^p(K_i,L_i)=0\) for \(p\geq1\).

(2) The unit \(E\to e_*e^*E\) is a monomorphism: at the level \(j\), its component at \((i,f)=(j,\mathrm{id}_j)\) is the identity of \(E_j\). Choose a monomorphism \(e^*E\to L\) with \(L\) injective. Since \(e_*\) is left exact, the composite \(E\to e_*L\) is a monomorphism. The sheaf \(e_*L\) is injective because \(e^*\) is exact [Stacks, Tag 015Z], and its levels are totally acyclic by (1) and Lemma 1.3 (1).

(3) The restriction \(e^*\) from \(A\)-modules to modules over the ring \(e^*A\) of \(X^{\mathrm{dis}}\) is exact, with right adjoint \(e_*\). So \(e_*\) carries injective modules to injective modules. If \(J\) is injective, the levels \(\prod_{i,f}f_*J_i\) of \(e_*J\) are injective: \(f_*\) carries injective modules to injective modules because \(X_f\) is flat [Stacks, Tag 0730], and a product of injective modules is injective. The embedding is constructed as in (2). \(\square\)

## 2. Standard resolutions

The construction of [Stacks, Tag 08N8], applied to the adjunction between \(e^{\mathrm{ab}}_!\) and \(e^*\), gives an augmented simplicial object
\[
(e^{\mathrm{ab}}_!e^*)^{\bullet+1}E\longrightarrow E,
\]
whose faces are built from the counit of the adjunction. Applied to the opposite categories, in which \((e_*)^{\mathrm{op}}\) is left adjoint to \((e^*)^{\mathrm{op}}\), it gives an augmented cosimplicial object
\[
E\longrightarrow(e_*e^*)^{\bullet+1}E,
\]
whose cofaces are built from the unit of the adjunction. Both are functorial in \(E\in\operatorname{Ab}(\operatorname{Top}(X))\). They are the *standard resolutions* of \(E\).

**Proposition 2.1.** For every abelian sheaf \(E\) on \(\operatorname{Top}(X)\), the complexes
\[
\begin{gathered}0\to E\to e_*e^*E\to(e_*e^*)^2E\to\cdots,\\ \cdots\to(e^{\mathrm{ab}}_!e^*)^2E\to e^{\mathrm{ab}}_!e^*E\to E\to0,\end{gathered}
\]
whose differentials are the alternating sums of the cofaces, respectively of the faces, are exact. They become contractible after applying \(e^*\). If the levels of \(E\) are totally acyclic, every \((e_*e^*)^{n+1}E\) is totally acyclic and has totally acyclic levels.

**Proof.** By [Stacks, Tag 08ND], applied to \(e^*\) and its left adjoint \(e^{\mathrm{ab}}_!\), the augmentation from \(e^*(e^{\mathrm{ab}}_!e^*)^{\bullet+1}E\) to the constant simplicial object \(e^*E\) is a homotopy equivalence of simplicial objects. By [Stacks, Tag 019T], the associated chain complexes are homotopy equivalent. The augmented complex is the cone of this homotopy equivalence, up to a shift, so it is contractible. The same lemma, applied to the opposite categories, gives a homotopy equivalence of cosimplicial objects from the constant object \(e^*E\) to \(e^*(e_*e^*)^{\bullet+1}E\). By [Stacks, Tag 01A0], the associated cochain complexes are homotopy equivalent, and \(e^*\) of the first augmented complex is contractible. A complex of abelian sheaves on \(\operatorname{Top}(X)\) is exact when its image under \(e^*\) is exact (Lemma 1.1).

For the last assertion, \((e_*e^*)^{n+1}E=e_*\bigl(e^*(e_*e^*)^nE\bigr)\). By induction on \(n\) and Proposition 1.4 (1), the levels of \((e_*e^*)^nE\) are totally acyclic. Then \(e_*\) of their family is totally acyclic with totally acyclic levels, again by Proposition 1.4 (1). \(\square\)

## 3. The cosimplicial complex of a total topos

**3.1. Setting.** Let \(Y\) be a topos and \(p\colon X\to Y\) a morphism of fibred topoi, where \(Y\) is fibred over the category with one object and one arrow (Definition 1.1 of the lesson on morphisms of fibred topoi). It consists of morphisms of topoi \(p_i\colon X_i\to Y\) and isomorphisms \(\theta_f\colon f^*p_j^*\to p_i^*\) for \(f\colon i\to j\), compatible with composites. By Proposition 2.1 and Corollary 2.2 of that lesson, the induced morphism of topoi \(p\colon\operatorname{Top}(X)\to Y\) has
\[
\begin{gathered}p^*(G)_i=p_i^*G,\\ p_*E=\varprojlim_{i\in I}p_{i*}E_i .\end{gathered}
\]
Here \(i\mapsto p_{i*}E_i\) is a functor \(\underline{p}_*E\colon I^{\mathrm{op}}\to\operatorname{Ab}(Y)\). For \(f\colon i\to j\), its map \(p_{j*}E_j\to p_{i*}E_i\) is \(p_{j*}\) applied to the adjoint \(E_j\to f_*E_i\) of \(E_f\), followed by the isomorphism \(p_{j*}f_*\cong p_{i*}\) adjoint to \(\theta_f\).

**Definition 3.2.** Let \(\mathcal A\) be an abelian category with products and \(G\colon I^{\mathrm{op}}\to\mathcal A\) a functor. Let \(N_n(I)\) be the set of strings
\[
\sigma=(i_0\xrightarrow{f_1}i_1\to\cdots\xrightarrow{f_n}i_n)
\]
of \(n\) composable arrows, and \(d_k\sigma\in N_{n-1}(I)\) the string with \(i_k\) omitted. For \(0<k<n\), the arrows \(f_k\) and \(f_{k+1}\) are replaced by \(f_{k+1}f_k\). The *cosimplicial complex* \(C^\bullet(G)\) has
\[
C^n(G)=\prod_{\sigma\in N_n(I)}G(i_0(\sigma)),
\]
where \(i_0(\sigma)\) is the first object of \(\sigma\), and the differential \(\delta\colon C^{n-1}(G)\to C^n(G)\) given by
\[
(\delta x)_\sigma=G(f_1)\bigl(x_{d_0\sigma}\bigr)+\sum_{k=1}^n(-1)^kx_{d_k\sigma}.
\]

The maps \(x\mapsto(G(f_1)x_{d_0\sigma})_\sigma\) and \(x\mapsto(x_{d_k\sigma})_\sigma\), \(k\geq1\), are the cofaces of a cosimplicial object of \(\mathcal A\). The cosimplicial identities follow from the simplicial identities of the nerve of \(I\) and from the functoriality of \(G\), so \(\delta\circ\delta=0\). A cocycle of degree \(0\) is a family \(x_i\in G(i)\) with \(G(f)(x_j)=x_i\) for every \(f\colon i\to j\). So \(H^0(C^\bullet(G))=\varprojlim_{I^{\mathrm{op}}}G\).

**Lemma 3.3.** Let \(G\in\operatorname{Ab}(Y)\). For \(n\geq0\), put
\[
B_n(G)=\bigoplus_{\sigma\in N_n(I)}(i_0)^{\mathrm{ab}}_!\bigl(p_{i_0}^*G\bigr),
\]
where \(i_0=i_0(\sigma)\) and \(i^{\mathrm{ab}}_!\) is the left adjoint of \(i^*\) on abelian sheaves (Lemma 1.1). For \(k\geq1\), let \(\partial_k\colon B_n(G)\to B_{n-1}(G)\) map the summand of \(\sigma\) identically to the summand of \(d_k\sigma\), which has the same first object. Let \(\partial_0\) map the summand of \(\sigma\) to that of \(d_0\sigma\) by the map
\[
(i_0)^{\mathrm{ab}}_!p_{i_0}^*G\longrightarrow(i_1)^{\mathrm{ab}}_!p_{i_1}^*G
\]
adjoint to the inclusion of \(p_{i_0}^*G\cong f_1^*p_{i_1}^*G\) (by \(\theta_{f_1}\)) as the summand of \(f_1\) in
\[
\begin{aligned}&\bigl((i_1)^{\mathrm{ab}}_!p_{i_1}^*G\bigr)_{i_0}\\&\quad=\bigoplus_{g\colon i_0\to i_1}g^*p_{i_1}^*G .\end{aligned}
\]
Let \(\varepsilon\colon B_0(G)\to p^*G\) be adjoint to the identity of \(p_i^*G\) on the summand of each object \(i\). Then the complex
\[
\cdots\to B_1(G)\to B_0(G)\xrightarrow{\ \varepsilon\ }p^*G\to0,
\]
with differential \(\sum_k(-1)^k\partial_k\), is exact.

**Proof.** Fix an object \(m\) of \(I\) and evaluate at the level \(m\). By Lemma 1.1,
\[
\begin{aligned}B_n(G)_m&=\bigoplus_{\sigma}\ \bigoplus_{h\colon m\to i_0}h^*p_{i_0}^*G\\&\cong\bigoplus_{(h,\sigma)}p_m^*G,\end{aligned}
\]
using the isomorphisms \(\theta_h\colon h^*p_{i_0}^*G\to p_m^*G\). The pairs \((h,\sigma)\) are exactly the strings of \(n\) composable arrows in the comma category \(m/I\). Its objects are the arrows \(m\to i\), and its morphisms \((m\to i)\to(m\to i')\) are the arrows \(i\to i'\) compatible with the arrows from \(m\). The string of \((h,\sigma)\) starts at \(h\), and its \(k\)-th object is \(f_k\cdots f_1h\). Under this identification, \(\partial_k\) is the \(k\)-th face of the nerve \(N(m/I)\). For \(k\geq1\) this is clear. The map \(\partial_0\) carries the summand of \((h,\sigma)\) to that of \((f_1h,d_0\sigma)\) by the identity of \(p_m^*G\), because \(\theta\) is compatible with composites. Likewise \(\varepsilon\) becomes the augmentation \(\mathbb Z[N_0(m/I)]\to\mathbb Z\). So the augmented complex at the level \(m\) is the augmented chain complex
\[
\mathbb Z[N_\bullet(m/I)]\longrightarrow\mathbb Z
\]
of the nerve of \(m/I\), with every copy of \(\mathbb Z\) replaced by \(p_m^*G\). The category \(m/I\) has the initial object \(\mathrm{id}_m\), so this augmented complex of free abelian groups is contractible (Lemma 2.2 of the lesson on strict simplicial objects). A contracting homotopy, given by integer matrices, induces a contracting homotopy after the replacement. So the complex is exact at every level. \(\square\)

**Proposition 3.4.** Let \(F\) be an injective abelian sheaf on \(\operatorname{Top}(X)\). Then the complex
\[
\begin{gathered}0\to p_*F\to C^0(\underline{p}_*F)\\ \to C^1(\underline{p}_*F)\to\cdots\end{gathered}
\]
is exact. Here \(p_*F\to C^0(\underline{p}_*F)=\prod_ip_{i*}F_i\) is the inclusion of the limit.

**Proof.** For \(G\in\operatorname{Ab}(Y)\), the adjunctions give
\[
\begin{aligned}\operatorname{Hom}(B_n(G),F)&=\prod_{\sigma}\operatorname{Hom}\bigl(p_{i_0}^*G,F_{i_0}\bigr)\\&=\operatorname{Hom}\bigl(G,C^n(\underline{p}_*F)\bigr),\end{aligned}
\]
and \(\operatorname{Hom}(p^*G,F)=\operatorname{Hom}(G,p_*F)\). Under these identifications, \(\operatorname{Hom}(\partial_k,F)\) is composition with the \(k\)-th coface of Definition 3.2. For \(k\geq1\) this is clear. For \(k=0\), the component of a map \(\varphi\colon(i_1)^{\mathrm{ab}}_!p_{i_1}^*G\to F\) on the summand of \(f_1\) at the level \(i_0\) is \(F_{f_1}\circ f_1^*(\varphi^\flat)\), where \(\varphi^\flat\colon p_{i_1}^*G\to F_{i_1}\) is the adjoint of \(\varphi\) (proof of Proposition 3.1 of the lesson on fibred topoi). Its adjoint \(G\to p_{i_0*}F_{i_0}\) is the adjoint of \(\varphi^\flat\) followed by the map \(p_{i_1*}F_{i_1}\to p_{i_0*}F_{i_0}\) of \(\underline{p}_*F\). Similarly, \(\operatorname{Hom}(\varepsilon,F)\) is composition with the inclusion of the limit. Since \(F\) is injective, \(\operatorname{Hom}(-,F)\) carries the exact complex of Lemma 3.3 to an exact complex. So
\[
\begin{gathered}0\to\operatorname{Hom}(G,p_*F)\to\operatorname{Hom}(G,C^0)\\ \to\operatorname{Hom}(G,C^1)\to\cdots\end{gathered}
\]
is exact for every \(G\), where \(C^n=C^n(\underline{p}_*F)\). Take \(G=\mathbb Z_K\), the free abelian sheaf on an object \(K\) of \(Y\). Then \(\operatorname{Hom}(\mathbb Z_K,-)\) is the functor of sections over \(K\), and the complex is exact on sections over every object. The sections of a kernel are the kernel of the sections, so the complex of sheaves is exact. \(\square\)

**Theorem 3.5.** Let \(E\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\).

1. If \(I^\bullet\) is a bounded below complex of injectives representing \(E\), the total complex of the double complex \(C^n(\underline{p}_*I^q)\) represents \(Rp_*E\).
2. If \(E\) is represented by a bounded below complex \(E^\bullet\) whose terms have totally acyclic levels, the total complex of \(C^n(\underline{p}_*E^q)\) represents \(Rp_*E\). In particular, if \(E\) is an abelian sheaf with totally acyclic levels, then, for \(q\geq0\),
\[
R^qp_*E=H^q\bigl(C^\bullet(\underline{p}_*E)\bigr).
\]

**Proof.** (1) Let \(A^{n,q}=C^n(\underline{p}_*I^q)\), with \(n\geq0\) and \(q\) bounded below. By Proposition 3.4, each row \(A^{\bullet,q}\) is a resolution of \(p_*I^q\). Hence the map from \(p_*I^\bullet\) to the total complex of \(A\) is a quasi-isomorphism [Stacks, Tag 0133]. And \(p_*I^\bullet\) represents \(Rp_*E\).

(2) Choose a quasi-isomorphism \(E^\bullet\to I^\bullet\) to a bounded below complex of injectives. Fix \(n\). The cone of the map of columns
\[
C^n(\underline{p}_*E^\bullet)\longrightarrow C^n(\underline{p}_*I^\bullet)
\]
is the product, over \(\sigma\in N_n(I)\), of \(p_{i_0*}\) of the cone of \(E^\bullet_{i_0}\to I^\bullet_{i_0}\). These cones are exact complexes of totally acyclic sheaves, all zero below a fixed degree: the levels of an injective are injective (Lemma 1.1), hence totally acyclic. By Lemma 1.3 (2), (5), \(p_{i_0*}\) of each cone is an exact complex of totally acyclic sheaves, and so is their product. So the map of double complexes is a quasi-isomorphism on every column. Both double complexes vanish for \(n<0\) and for \(q\) below a fixed bound, so the filtrations by \(n\) are finite in each total degree. Comparing the spectral sequences of these filtrations [Stacks, Tag 0132], the map of total complexes is a quasi-isomorphism. Now apply (1). For a single sheaf, the double complex has a single row. \(\square\)

**Corollary 3.6.** Let \(G\colon I^{\mathrm{op}}\to\operatorname{Ab}\) be a functor. The right derived functors of \(\varprojlim_{I^{\mathrm{op}}}\colon\operatorname{Fun}(I^{\mathrm{op}},\operatorname{Ab})\to\operatorname{Ab}\) are
\[
R^n\!\varprojlim_{I^{\mathrm{op}}}G=H^n\bigl(C^\bullet(G)\bigr).
\]

**Proof.** Let \(X\) be the constant fibred topos over \(I\) with value the punctual topos, and \(p\) its morphism to the punctual topos. Then \(\operatorname{Top}(X)\) is the category of presheaves of sets on \(I\), its abelian sheaves are the functors \(I^{\mathrm{op}}\to\operatorname{Ab}\), and \(p_*=\Gamma(\operatorname{Top}(X),-)=\varprojlim_{I^{\mathrm{op}}}\) (Corollary 2.2 of the lesson on morphisms of fibred topoi). Every abelian group is totally acyclic on the punctual topos: for a set \(K\), the functor \(F\mapsto F(K)=\prod_KF\) is exact. Since \(\underline{p}_*G=G\), Theorem 3.5 (2) gives the claim. \(\square\)

**Corollary 3.7.** Let \(E\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\). There is a spectral sequence
\[
\begin{aligned}E_2^{n,q}&=R^n\!\varprojlim_{i\in I^{\mathrm{op}}}H^q(X_i,E_i)\\&\Longrightarrow H^{n+q}(\operatorname{Top}(X),E),\end{aligned}
\]
functorial in \(E\). Here \(i\mapsto H^q(X_i,E_i)\) is the functor \(I^{\mathrm{op}}\to\operatorname{Ab}\) induced by the maps \(E_f\).

**Proof.** Apply Theorem 3.5 (1) with \(Y\) the punctual topos, and filter the total complex of \(A\) by \(n\). The column \(n\) is \(\prod_\sigma\Gamma(X_{i_0},I^\bullet_{i_0})\). Each \(I^\bullet_i\) is a bounded below complex of injectives representing \(E_i\) (Lemma 1.1), and products of abelian groups are exact. So
\[
\begin{aligned}E_1^{n,q}&=\prod_\sigma H^q(X_{i_0},E_{i_0})\\&=C^n\bigl(H^q(X_\bullet,E_\bullet)\bigr),\end{aligned}
\]
and \(d_1\) is the differential of Definition 3.2. By Corollary 3.6, \(E_2^{n,q}=R^n\varprojlim H^q(X_\bullet,E_\bullet)\). The filtration is finite in each degree, so the spectral sequence converges [Stacks, Tag 0132]. \(\square\)

**Lemma 3.8.** Suppose \(I\) has a final object \(t\). Let \(\mathcal A\) be an abelian category with products and \(G\colon I^{\mathrm{op}}\to\mathcal A\) a functor. For \(\sigma\in N_{n-1}(I)\), let \((\sigma,t)\in N_n(I)\) be \(\sigma\) followed by the unique arrow from its last object to \(t\). For \(n\geq1\), define \(h\colon C^n(G)\to C^{n-1}(G)\) by
\[
(hx)_\sigma=(-1)^nx_{(\sigma,t)}.
\]
Then \(\delta h+h\delta=\mathrm{id}\) on \(C^n(G)\) for \(n\geq1\), and on \(C^0(G)\)
\[
(h\delta x)_i=x_i-G(i\to t)(x_t).
\]
Consequently \(H^n(C^\bullet(G))=0\) for \(n\geq1\), and the projection \(C^0(G)\to G(t)\) induces an isomorphism \(\varprojlim_{I^{\mathrm{op}}}G\cong G(t)\).

**Proof.** Let \(n\geq1\), \(x\in C^n(G)\), and \(\sigma\in N_n(I)\) with first arrow \(f_1\). The faces of \((\sigma,t)\) are \(d_k(\sigma,t)=(d_k\sigma,t)\) for \(k\leq n\), and \(d_{n+1}(\sigma,t)=\sigma\). Put
\[
\begin{aligned}S&=G(f_1)\bigl(x_{(d_0\sigma,t)}\bigr)\\&\quad+\sum_{k=1}^n(-1)^kx_{(d_k\sigma,t)}.\end{aligned}
\]
Then \((\delta x)_{(\sigma,t)}=S+(-1)^{n+1}x_\sigma\), so \((h\delta x)_\sigma=(-1)^{n+1}S+x_\sigma\), while \((\delta hx)_\sigma=(-1)^nS\). The sum is \(x_\sigma\). For \(n=0\) and \(\sigma=(i)\), \((h\delta x)_i=-(\delta x)_{(i\to t)}\), which is \(x_i-G(i\to t)(x_t)\).

If \(x\) is a cocycle of degree \(n\geq1\), then \(x=\delta hx\). A cocycle \(x\) of degree \(0\) satisfies \(x_i=G(i\to t)(x_t)\), so it is determined by \(x_t\). Conversely, for \(y\in G(t)\), the family \(x_i=G(i\to t)(y)\) is a cocycle, because the arrow to \(t\) is unique. \(\square\)

**Corollary 3.9.** Suppose \(I\) has a final object \(t\). For every \(E\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\), restriction to the level \(t\) induces an isomorphism
\[
Rp_*E\xrightarrow{\ \sim\ }Rp_{t*}E_t .
\]
In particular \(H^n(\operatorname{Top}(X),E)=H^n(X_t,E_t)\) for every \(n\).

**Proof.** Represent \(E\) by a bounded below complex of injectives \(I^\bullet\), and let \(A\) be the double complex of Theorem 3.5 (1). The projections \(C^0(\underline{p}_*I^q)\to p_{t*}I^q_t\) define a map from \(A\) to the double complex with the single column \(p_{t*}I^\bullet_t\) in degree \(n=0\). By Lemma 3.8, it is a quasi-isomorphism on every row. Since the filtrations by \(q\) are finite in each total degree, the map of total complexes is a quasi-isomorphism. Composed with the quasi-isomorphism \(p_*I^\bullet\to\operatorname{Tot}(A)\), it is the restriction map \(\varprojlim_ip_{i*}I^\bullet_i\to p_{t*}I^\bullet_t\). As \(I^\bullet_t\) is a complex of injectives representing \(E_t\) (Lemma 1.1), \(p_{t*}I^\bullet_t\) represents \(Rp_{t*}E_t\). \(\square\)

**Examples 3.10.** (a) Let \(I=\{0\to1\}\), so that \(X\) is a morphism of topoi \(f\colon X_0\to X_1\) (Examples 1.2 (a) of the lesson on fibred topoi). The object \(1\) is final, so \(H^n(\operatorname{Top}(X),E)=H^n(X_1,E_1)\) for every \(E\): the level \(X_0\) does not contribute. In degree \(0\) this can be seen directly. A global section of \(E\) is a pair of global sections \(s_1\) of \(E_1\) and \(s_0\) of \(E_0\) with \(s_0=E_f(f^*s_1)\), so it is determined by \(s_1\).

(b) Let \(X\) be the constant fibred topos over \(I\) with value a topos \(T\), and \(p\colon X\to T\) the identity on every level. Then \(\operatorname{Top}(X)\) is the category of functors \(I^{\mathrm{op}}\to T\) (Examples 5.2 (c) of the lesson on fibred topoi), and \(p_*=\varprojlim_{I^{\mathrm{op}}}\). Theorem 3.5 computes the derived functors of
\[
\begin{aligned}\varprojlim_{I^{\mathrm{op}}}\colon\ &\operatorname{Fun}(I^{\mathrm{op}},\operatorname{Ab}(T))\\&\longrightarrow\operatorname{Ab}(T).\end{aligned}
\]
For a functor \(E\) with totally acyclic values, \(R^n\varprojlim E=H^n(C^\bullet(E))\), the complex being formed in \(\operatorname{Ab}(T)\).

## 4. Morphisms over a fixed index category

**Proposition 4.1.** Let \(u\colon X\to Y\) be an \(I\)-morphism of topoi fibred over \(I\) (Definition 1.1 of the lesson on morphisms of fibred topoi), and \(i\) an object of \(I\). There is a canonical isomorphism of functors on \(D^+(\operatorname{Ab}(\operatorname{Top}(X)))\)
\[
i^*\circ Ru_*\cong Ru_{i*}\circ i^* .
\]

**Proof.** By Corollary 2.2 (b) of the lesson on morphisms of fibred topoi, \(i^*u_*F=u_{i*}F_i\) for every abelian sheaf \(F\), so \(i^*\circ u_*=u_{i*}\circ i^*\) as functors to \(\operatorname{Ab}(Y_i)\). The functor \(i^*\) is exact, so \(i^*\circ Ru_*\) is the derived functor of \(i^*\circ u_*\). The functor \(i^*\) is exact and carries injectives to injectives (Lemma 1.1), so \(Ru_{i*}\circ i^*\) is the derived functor of \(u_{i*}\circ i^*\) [Stacks, Tag 015M]. \(\square\)

For the second total category, direct images are not computed levelwise (Section 3 of the lesson on morphisms of fibred topoi), and Proposition 4.1 has no analogue in general.

**Remark 4.2.** Let \(A\) be a ring of \(\operatorname{Top}(X)\). The derived direct image of a complex of \(A\)-modules agrees with the derived direct image of the underlying complex of abelian sheaves [Stacks, Tag 0D6J]; the total topos is the topos of sheaves on a site by Theorem 4.2 of the lesson on fibred topoi. So Theorem 3.5, Corollary 3.9 and Proposition 4.1 also compute derived direct images of complexes of modules.

## 5. Exercises

**Exercise 5.1.** Let \(I\) be the category with two objects \(0,1\) and, besides the identities, two arrows \(a,b\colon0\to1\).

1. Show that for every functor \(G\colon I^{\mathrm{op}}\to\operatorname{Ab}\), \(R^n\varprojlim G\) is the cohomology of the two-term complex
\[
G(1)\xrightarrow{\ G(a)-G(b)\ }G(0)
\]
in degrees \(0\) and \(1\). In particular \(R^n\varprojlim G=0\) for \(n\geq2\).
2. A topos fibred over \(I\) is a pair of morphisms of topoi \(a,b\colon X_0\to X_1\). Deduce a long exact sequence
\[
\begin{gathered}\cdots\to H^q(\operatorname{Top}(X),E)\\ \to H^q(X_1,E_1)\to H^q(X_0,E_0)\\ \to H^{q+1}(\operatorname{Top}(X),E)\to\cdots\end{gathered}
\]
for every abelian sheaf \(E\) on \(\operatorname{Top}(X)\), whose middle map is the difference of the maps induced by \(E_a\) and \(E_b\).

**Exercise 5.2.** Let \(\Gamma\) be a group, viewed as a category \(B\Gamma\) with one object \(\ast\), with the elements of \(\Gamma\) as arrows and composition \(g\circ h=gh\). Let \(X\) be the constant fibred topos over \(B\Gamma\) with value the punctual topos.

1. Show that an abelian sheaf on \(\operatorname{Top}(X)\) is an abelian group \(M\) with a right action of \(\Gamma\), and that \(\Gamma(\operatorname{Top}(X),M)=M^\Gamma\).
2. Show that \(C^n(M)\) is the group of maps \(\Gamma^n\to M\), with
\[
\begin{aligned}&(\delta x)(g_1,\ldots,g_n)\\&\quad=x(g_2,\ldots,g_n)\cdot g_1\\&\qquad+\sum_{k=1}^{n-1}(-1)^kx(\ldots,g_{k+1}g_k,\ldots)\\&\qquad+(-1)^nx(g_1,\ldots,g_{n-1}),\end{aligned}
\]
where the middle terms replace \(g_k,g_{k+1}\) by \(g_{k+1}g_k\). Deduce that \(H^n(\operatorname{Top}(X),M)\) is the cohomology of \(\Gamma\) with coefficients in \(M\), that is, the \(n\)-th derived functor of \(M\mapsto M^\Gamma\).

**Exercise 5.3.** Let \(I=\{0\to1\}\). Let both levels be the punctual topos, with rings \(A_0=\mathbb Z/2\mathbb Z\) and \(A_1=\mathbb Z\), and let the arrow act by the ring map \(\mathbb Z\to\mathbb Z/2\mathbb Z\).

1. Let \(J\) be the module of \(X^{\mathrm{dis}}\) with \(J_0=\mathbb Z/2\mathbb Z\) and \(J_1=0\). Show that \(e_*J\) is an injective module whose level \(1\) is not an injective \(\mathbb Z\)-module.
2. Which hypothesis of Proposition 1.4 (3) fails?

## 6. Complete solutions

**5.1.** (1) Let \(\Phi(G)\) be the two-term complex. The functor \(\Phi\) is exact, so the cohomology of \(\Phi\) is a \(\delta\)-functor. In degree \(0\) it is \(\varprojlim G\): a compatible family is a pair \(y\in G(1)\), \(x\in G(0)\) with \(x=G(a)y=G(b)y\), and it is determined by \(y\). For an object \(k\) of \(I\) and an abelian group \(Q\), let \(R_k(Q)\) be the functor
\[
j\longmapsto\prod_{\operatorname{Hom}_I(k,j)}Q,
\]
whose map for \(g\colon j\to j'\) sends \((q_\varphi)_{\varphi\colon k\to j'}\) to \((q_{g\psi})_{\psi\colon k\to j}\). Then \(\operatorname{Hom}(G,R_k(Q))=\operatorname{Hom}(G(k),Q)\), and \(R_k(Q)\) is injective when \(Q\) is. For \(R_0(Q)\), the map \(G(a)-G(b)\colon Q\times Q\to Q\) is \((q_a,q_b)\mapsto q_a-q_b\), which is surjective. For \(R_1(Q)\), it is the map \(Q\to0\). Choose embeddings \(G(k)\to Q_k\) into injective abelian groups. The map \(G\to R_0(Q_0)\times R_1(Q_1)\), adjoint to these embeddings, is a monomorphism, and its target has \(H^1\Phi=0\), since the map \(G(a)-G(b)\) of a product is the product of the maps. So \(H^1\Phi\) is effaceable, \(H^\bullet\Phi\) is a universal \(\delta\)-functor [Stacks, Tag 010T], and it coincides with \(R^\bullet\varprojlim\). As \(\Phi\) has length two, \(R^n\varprojlim=0\) for \(n\geq2\).

(2) In the spectral sequence of Corollary 3.7, \(E_2^{n,q}=0\) unless \(n\in\{0,1\}\). So all differentials from \(E_2\) on vanish, and there are exact sequences
\[
\begin{gathered}0\to E_2^{1,q-1}\to H^q(\operatorname{Top}(X),E)\\ \to E_2^{0,q}\to0 .\end{gathered}
\]
By (1), \(E_2^{0,q}\) and \(E_2^{1,q}\) are the kernel and the cokernel of
\[
H^q(X_1,E_1)\longrightarrow H^q(X_0,E_0),
\]
the difference of the two composites
\[
\begin{gathered}H^q(X_1,E_1)\to H^q(X_0,c^*E_1)\\ \to H^q(X_0,E_0)\end{gathered}
\]
given by \(c^*\) and \(E_c\), for \(c=a,b\). Splicing the short exact sequences gives the long exact sequence.

**5.2.** (1) An abelian sheaf is a functor \(M\colon B\Gamma^{\mathrm{op}}\to\operatorname{Ab}\) (proof of Corollary 3.6). Put \(m\cdot g=M(g)(m)\). Then
\[
\begin{aligned}m\cdot(gh)&=M(g\circ h)(m)\\&=M(h)\bigl(M(g)(m)\bigr)\\&=(m\cdot g)\cdot h,\end{aligned}
\]
a right action. Conversely, a right action defines such a functor. Global sections are \(\varprojlim_{B\Gamma^{\mathrm{op}}}M\), the elements fixed by every \(M(g)\), that is, \(M^\Gamma\).

(2) A string \(\sigma\in N_n(B\Gamma)\) is a sequence \((g_1,\ldots,g_n)\) of arrows, and \(G(i_0)=M\) for every \(\sigma\). So \(C^n(M)\) is the group of maps \(\Gamma^n\to M\). The face \(d_0\) removes \(g_1\), the face \(d_n\) removes \(g_n\), and \(d_k\) for \(0<k<n\) replaces \(g_k,g_{k+1}\) by their composite \(g_{k+1}\circ g_k=g_{k+1}g_k\). The term \(G(f_1)(x_{d_0\sigma})\) is \(x(g_2,\ldots,g_n)\cdot g_1\). This gives the formula. By Corollary 3.6, \(H^n(C^\bullet(M))=R^n\varprojlim M\), the derived functor of \(M\mapsto M^\Gamma\) on right \(\Gamma\)-modules. Since \(\Gamma(\operatorname{Top}(X),-)\) is this functor on \(\operatorname{Ab}(\operatorname{Top}(X))\), \(H^n(\operatorname{Top}(X),M)\) is the same derived functor.

**5.3.** (1) The arrows with target \(1\) are \(\mathrm{id}_1\) and the arrow \(f\colon0\to1\). By Lemma 1.1,
\[
(e_*J)_1=J_1\times f_*J_0=\mathbb Z/2\mathbb Z,
\]
where \(f_*\) is restriction of scalars along \(\mathbb Z\to\mathbb Z/2\mathbb Z\). An injective \(\mathbb Z\)-module is divisible, and \(\mathbb Z/2\mathbb Z\) is not, since \(1\) is not twice an element. The module \(J\) is injective over the ring of \(X^{\mathrm{dis}}\): \(\mathbb Z/2\mathbb Z\) is a field, and \(0\) is injective. Since \(e^*\) is exact, \(e_*J\) is injective, as in the proof of Proposition 1.4 (3).

(2) The morphism of ringed topoi \(X_f\) is not flat: \(\mathbb Z/2\mathbb Z\) is not a flat \(\mathbb Z\)-module, since multiplication by \(2\) on \(\mathbb Z\) is injective but becomes zero after tensoring with \(\mathbb Z/2\mathbb Z\).

## Sources

The cohomology of total topoi, with the standard resolutions, the cosimplicial computation of derived direct images and the commutation of direct images with the levels, is due to Illusie, in his work on the cotangent complex and the cohomology of diagrams. The complex computing the derived functors of an inverse limit is due to J.-E. Roos. The resolution of Lemma 3.3 extends to any index category the resolution used in the Stacks project for simplicial sites [Stacks, Tags 09WI and 0D78]. Totally acyclic sheaves are the flasque sheaves of SGA 4, Exposé V; the Stacks project treats them in [Stacks, Tag 079X]. Standard resolutions go back to Godement's book on sheaf theory.
