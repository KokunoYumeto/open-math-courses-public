# Simplicial groups and right fractions

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

When the topos has enough points, the quasi-isomorphisms of simplicial sheaves admit a calculus of left fractions in the homotopy category; between Kan simplicial sheaves they also admit a calculus of right fractions. That is, the quasi-isomorphisms between Kan simplicial sheaves, taken up to homotopy, form a right multiplicative system: every morphism \(X\to Y\) of the simplicial derived category between Kan objects is a homotopy class of maps \(X'\to Y\) composed with the inverse of a quasi-isomorphism \(X'\to X\), which may be taken to be a fibration. The proof uses path objects instead of the cylinders of the left calculus: a map between Kan simplicial sheaves factors as a homotopy equivalence followed by a fibration, and mapping objects of fibrations relative to finite simplicial sets are fibrations. In every topos, localizing the Kan simplicial sheaves gives the whole simplicial derived category, through Kan's functor \(\operatorname{Ex}^\infty\). For the topos of sets this recovers the homotopy category of Kan complexes. The same holds over a fixed simplicial sheaf \(B\), for the simplicial sheaves whose map to \(B\) is a fibration.

The lesson begins with simplicial groups, which are Kan. Their homotopy sheaves are the homology sheaves of the normalized (Moore) complex, also in the non-abelian case, and a homomorphism of simplicial groups is a fibration exactly when it is an epimorphism on the normalized complex in positive degrees.

**Prerequisites.** [*The simplicial derived category of a topos*](the-simplicial-derived-category-of-a-topos.md) (Conventions, Lemmas 1.1–1.2, Proposition 1.3, Section 2, Corollary 3.3, Corollary 4.3, Section 6); [*Local fibrations and Kan's subdivision functor*](local-fibrations-and-kan-s-subdivision-functor.md) (Sections 1, 2 and 4, Theorem 3.7); [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md), Sections 1 and 2; [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes), Sections 4.4 and 5.3 (the relations (4.14) and (5.12), the product (4.16), Lemma 5.3b, Theorem 5.3f); [*The cotangent complex*](course:AG-HP/the-cotangent-complex), Proposition 1.4 (simplicial groups are Kan); [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md), Section 2.1 (the opposite \(K^{\mathrm{op}}\) of a simplicial set). From the AI-integrated Stacks project: right multiplicative systems and right fractions [[Stacks, Tag 04VC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-multiplicative-system), [Tag 04VI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-morphisms-right-localization), [Tag 04VJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-equality-morphisms-right-localization), [Tag 04VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-properties-right-localization)].

## Conventions

As in the lessons on the simplicial derived category and on local fibrations: \(T=\operatorname{Sh}(\mathcal C)\), \(e\) is the final simplicial sheaf, \(\underline{\operatorname{Homs}}\) are mapping objects, fibrations are the local fibrations, Kan simplicial sheaves are those whose map to \(e\) is a fibration, and quasi-isomorphisms are those of Definition 2.1 of the lesson on homotopy sheaves. A *fibrant quasi-isomorphism* is a map that is both. Simplicial sets are constant simplicial sheaves. For a sheaf \(F\), the constant simplicial sheaf with value \(F\) is written \(F\) again.

## 1. Simplicial groups

A *simplicial group* of \(T\) is a simplicial object of the category of sheaves of groups. Its *normalized complex* \(NG\) has \(N_0G=G_0\) and, for \(n\geq1\),
\[
N_nG=\bigcap_{i=1}^n\ker\bigl(d_i\colon G_n\to G_{n-1}\bigr),
\]
with the differential \(d_0\colon N_nG\to N_{n-1}G\). Put \(Z_n=N_nG\cap\ker d_0\) for \(n\geq1\), \(Z_0=G_0\), and \(B_n=d_0(N_{n+1}G)\).

**Lemma 1.1.** \(d_0\) maps \(N_nG\) into \(N_{n-1}G\), \(B_n\subset Z_n\), and \(B_n\) is a normal subgroup of \(G_n\). So \(H_n(NG)=Z_n/B_n\) is a sheaf of groups.

**Proof.** For \(i\geq1\), \(d_id_0=d_0d_{i+1}\), so \(d_0\) maps \(N_nG\) into \(N_{n-1}G\); and \(d_0d_0=d_0d_1\) vanishes on \(N_{n+1}G\). For \(y\in N_{n+1}G\) and \(g\in G_n\), the element \(s_0(g)\,y\,s_0(g)^{-1}\) lies in \(N_{n+1}G\): \(d_1s_0=1\) gives \(d_1\)-face \(gg^{-1}=1\), and for \(i\geq2\), \(d_is_0=s_0d_{i-1}\) and \(d_iy=1\). Its image under \(d_0\) is \(g\,d_0(y)\,g^{-1}\). \(\square\)

**Proposition 1.2 (Moore).** Let \(G\) be a simplicial group of \(T\). Then \(G\) is a Kan simplicial sheaf; \(\pi_0(G)=G_0/B_0\) as sheaves of groups; and for \(n\geq1\) and \(U\in\mathcal C\),
\[
\pi_n(G|U,1)\cong H_n(NG)|U,
\]
an isomorphism of sheaves of groups, which are abelian. Right translation by \(x^{-1}\) identifies \(\pi_n(G|U,x)\) with \(\pi_n(G|U,1)\) for every base point \(x\).

**Proof.** The sections of \(G\) over \(U\) form a simplicial group \(G(U)\), and a horn of \(G\) over \(U\) is a horn of \(G(U)\) (Lemma 1.1 (3) of the lesson on the simplicial derived category). Simplicial groups of sets are Kan (Proposition 1.4 of the lesson on the cotangent complex), so horns of \(G\) are filled over \(U\) itself. The homotopy sheaves are associated with the presheaves of homotopy groups of sections, and sheafification commutes with kernels, images and quotients by normal subgroups. So it suffices to treat a simplicial group \(G\) of sets. Translation is Lemma 1.2 (4) of the lesson on homotopy sheaves.

*Components.* If \(e\) is an edge from \(a\) to \(b\) (\(d_1e=a\), \(d_0e=b\)), then \(e\,s_0(a)^{-1}\in N_1G\) has \(d_0\)-image \(ba^{-1}\). Conversely, if \(ba^{-1}=d_0y\) with \(y\in N_1G\), then \(y\,s_0(a)\) is an edge from \(a\) to \(b\). So "joined by an edge" is the relation \(ba^{-1}\in B_0\), which is an equivalence relation, and \(\pi_0(G)=G_0/B_0\).

*Cycles and the relation.* Let \(n\geq1\). The cycles at \(1\) in the sense of (4.13) of the lesson on Kan complexes are the elements with all faces \(1\): the group \(Z_n\). By Lemma 5.3b there, two cycles are related by (4.14), restated there as (5.12), exactly when, as maps \(\Delta[n]\to G\), they are homotopic by a homotopy constant on \(\partial\Delta[n]\). The opposite \(G^{\mathrm{op}}\), with \(d_i\) and \(s_i\) replaced by \(d_{n-i}\) and \(s_{n-i}\), is a simplicial group with the same cycles. A map \(L\to G^{\mathrm{op}}\) is a map \(L^{\mathrm{op}}\to G\), and the order-reversing isomorphisms of \([n]\) and \([1]\) give \((\Delta[n]\times\Delta[1])^{\mathrm{op}}\cong\Delta[n]\times\Delta[1]\), carrying \(\partial\Delta[n]\times\Delta[1]\) to itself, exchanging the two ends and carrying the simplex of a cycle to the simplex of the same element. So homotopy relative to the boundary, and hence the relation (4.14), is the same in \(G\) and in \(G^{\mathrm{op}}\). In \(G^{\mathrm{op}}\), (4.14) for cycles \(z,z'\) asks for \(H\in G_{n+1}\) with \(d_0H=z\), \(d_1H=z'\) and \(d_iH=1\) for \(i\geq2\). For such \(H\), \(H\,s_0(z')^{-1}\) lies in \(N_{n+1}G\), since \(d_1s_0=1\) and \(d_is_0=s_0d_{i-1}\) for \(i\geq2\), and its \(d_0\)-image is \(zz'^{-1}\). Conversely, if \(zz'^{-1}=d_0y\) with \(y\in N_{n+1}G\), then \(H=y\,s_0(z')\) has these faces. So \(z\) and \(z'\) have the same class exactly when \(zz'^{-1}\in B_n\).

*Group law.* The product \([b][a]\) of (4.16) there is the class of the face \(d_n\) of a simplex with \(d_{n-1}=b\), \(d_{n+1}=a\) and all lower faces \(1\). The simplex \(s_{n-1}(b)\,s_n(a)\) is one: \(d_{n-1}\) gives \(b\cdot s_{n-1}d_{n-1}a=b\), \(d_{n+1}\) gives \(s_{n-1}d_nb\cdot a=a\), lower faces give \(1\), and \(d_n\) gives \(ba\). So \([b][a]=[ba]\), and \(\pi_n(G,1)=Z_n/B_n\) as groups.

*Commutativity.* For \(z,w\in Z_n\), the simplex \(y=s_{n-1}(z)s_n(w)s_{n-1}(z)^{-1}s_n(w)^{-1}\) has \(d_ny=zwz^{-1}w^{-1}\) and all other faces \(1\), by the same face identities. By (4.14), \(zwz^{-1}w^{-1}\) has the class of \(1\). \(\square\)

**Lemma 1.3.** Let \(G\) be a simplicial group of sets and \(n\geq1\). Every \(u\in G_n\) whose vertex \(0\) is \(1\) is a finite product of elements \(\sigma(z)\), with \(z\in N_kG\), \(1\leq k\leq n\), and \(\sigma\colon G_k\to G_n\) an iterated degeneracy; the factors are given by a formula in \(u\), its faces and degeneracies, and the group operations, the same for all simplicial groups. Every \(x\in G_n\) is \(u\cdot s_0^n(x_0)\), where \(x_0\) is the vertex \(0\) of \(x\), \(s_0^n\) the iterated degeneracy \(G_0\to G_n\), and \(u\) has vertex \(0\) equal to \(1\).

**Proof.** The last assertion holds with \(u=x\,s_0^n(x_0)^{-1}\). For the first, let \(u^{(n)}=u\), and for \(m=n,\ldots,1\) put \(w_m=d_mu^{(m)}\) and \(u^{(m-1)}=u^{(m)}s_{m-1}(w_m)^{-1}\). Suppose \(d_iu^{(m)}=1\) for \(i>m\). Then \(d_mu^{(m-1)}=w_mw_m^{-1}=1\), because \(d_ms_{m-1}=1\); and for \(i>m\), \(d_is_{m-1}=s_{m-1}d_{i-1}\) and \(d_{i-1}w_m=d_{i-1}d_mu^{(m)}=d_md_iu^{(m)}=1\). So \(d_iu^{(m-1)}=1\) for \(i\geq m\). Hence \(u^{(0)}\in N_nG\) and
\[
u=u^{(0)}\,s_0(w_1)\,s_1(w_2)\cdots s_{n-1}(w_n).
\]
Each \(w_m\in G_{n-1}\) has vertex \(0\) equal to \(1\), since faces \(d_m\) with \(m\geq1\) keep the vertex \(0\), and so does every \(u^{(m)}\). By induction on \(n\) each \(w_m\) is such a product in degree \(n-1\) (for \(n-1=0\), \(w_1=1\)), and the degeneracies \(s_{m-1}\) are homomorphisms. \(\square\)

**Proposition 1.4.** Let \(f\colon G\to H\) be a homomorphism of simplicial groups of \(T\), with kernel \(K\). The following are equivalent:

1. \(f\) is a fibration;
2. \(N_nf\colon N_nG\to N_nH\) is an epimorphism for every \(n\geq1\);
3. the map \(G\to H\times_{\pi_0(H)}\pi_0(G)\), to the fibre product of \(H\to\pi_0(H)\) and \(\pi_0(f)\), is an epimorphism in every degree.

**Proof.** We first show that an epimorphism \(f\) in every degree is a fibration. Let \(x\) be a horn of \(G\) over \(U\) and \(y\) a simplex of \(H\) over \(U\) with \(f(x)=y|_{\text{horn}}\). Locally \(y=f(g)\). The horn \(x\cdot(g|_{\text{horn}})^{-1}\), a product in the group of horns, lies in \(K\), a simplicial group; fill it by \(k\) over the same object. Then \(kg\) fills \(x\) and lies over \(y\).

(1)\(\Rightarrow\)(2). Let \(z\in N_nH\) over \(U\). The horn \(\Lambda^0[n]\to G\) with all faces \(1\) lies over the faces \(d_1z,\ldots,d_nz\), which are \(1\). A local filler \(g\) over \(z\) lies in \(N_nG\).

(2)\(\Rightarrow\)(3). Work with local sections. Let \(h\in H_n\) and \(c\in\pi_0(G)\) with \(\pi_0(f)(c)=[h]\), the class of the vertices of \(h\). Write \(h=u\,s_0^n(h_0)\) as in Lemma 1.3. Lift the factors \(z\in N_kH\) of \(u\) through (2), and form \(\tilde u\) from the lifts by the same formula; then \(f(\tilde u)=u\), and \(\tilde u\) has vertex \(0\) equal to \(1\), since every element of \(N_kG\), \(k\geq1\), has vertex \(0\) equal to \(1\). Locally \(c=[g_0]\) with \(g_0\in G_0\); as \([f(g_0)]=[h_0]\), \(h_0f(g_0)^{-1}=d_0(\epsilon)\) locally, with \(\epsilon\in N_1H\) (Proposition 1.2). Lift \(\epsilon\) to \(\tilde\epsilon\in N_1G\) and put \(g_v=d_0(\tilde\epsilon)g_0\). Then \(f(g_v)=h_0\) and \([g_v]=[g_0]=c\). The element \(g=\tilde u\,s_0^n(g_v)\) satisfies \(f(g)=h\), and its vertex \(0\) is \(g_v\), so its class is \(c\).

(3)\(\Rightarrow\)(1). The map \(G\to H'=H\times_{\pi_0(H)}\pi_0(G)\) is a homomorphism of simplicial groups that is an epimorphism in every degree, hence a fibration. The map \(H'\to H\) is a base change of the map of constant simplicial sheaves \(\pi_0(G)\to\pi_0(H)\), which is a fibration (Proposition 2.5 (4) of the lesson on local fibrations). Composites of fibrations are fibrations. \(\square\)

**Proposition 1.5.** A homomorphism \(f\colon G\to H\) of simplicial groups of \(T\) is a fibrant quasi-isomorphism if and only if it is an epimorphism in every degree and its kernel \(K\) has \(\pi_n(K)=1\) for every \(n\geq0\). Consequently the base change of a fibrant quasi-isomorphism of simplicial groups along any homomorphism is a fibrant quasi-isomorphism.

**Proof.** By Proposition 1.2 and translation, \(f\) is a quasi-isomorphism if and only if \(H_n(Nf)\) is an isomorphism for every \(n\geq0\). We use local sections throughout; \(Z_n\), \(B_n\) refer to the group indicated.

Suppose that \(f\) is an epimorphism in every degree with \(\pi_*(K)=1\). It is a fibration (proof of Proposition 1.4), so \(N_nf\) is an epimorphism for \(n\geq1\), and \(N_nK\) is its kernel. *Surjectivity of \(H_n(Nf)\).* For \(n=0\) it holds since \(f_0\) is an epimorphism. For \(n\geq1\), lift \(z\in Z_n(NH)\) to \(g\in N_nG\); then \(d_0g\in Z_{n-1}(NK)\), so locally \(d_0g=d_0k\) with \(k\in N_nK\), and \(gk^{-1}\in Z_n(NG)\) maps to \(z\). *Injectivity.* Let \(g\in Z_n(NG)\) with \(f(g)=d_0(c)\), \(c\in N_{n+1}H\). Lift \(c\) to \(c'\in N_{n+1}G\). Then \(g\,d_0(c')^{-1}\in Z_n(NK)=B_n(NK)\), so \(g\in B_n(NG)\).

Conversely let \(f\) be a fibrant quasi-isomorphism. Since \(\pi_0(f)\) is an isomorphism, \(H\times_{\pi_0(H)}\pi_0(G)=H\), and \(f\) is an epimorphism in every degree by Proposition 1.4. Let \(k\in Z_n(NK)\), \(n\geq0\). Its class in \(H_n(NG)\) maps to \(1\), so \(k=d_0(g)\) with \(g\in N_{n+1}G\). Then \(f(g)\in Z_{n+1}(NH)\), and by surjectivity of \(H_{n+1}(Nf)\), \(f(g)=f(g'')d_0(c)\) with \(g''\in Z_{n+1}(NG)\) and \(c\in N_{n+2}H\). Lift \(c\) to \(c'\in N_{n+2}G\) and put \(g'''=g''d_0(c')\in Z_{n+1}(NG)\). Then \(g\,g'''^{-1}\in N_{n+1}K\) and \(d_0(g\,g'''^{-1})=k\). So \(Z_n(NK)=B_n(NK)\).

For the last assertion: a base change of \(f\) along \(H'\to H\) is an epimorphism in every degree with the same kernel. \(\square\)

## 2. Mapping objects relative to maps

For maps \(f\colon X'\to X\) and \(g\colon Y'\to Y\) of simplicial sheaves, put
\[
\begin{aligned}&\underline{\operatorname{Homs}}(X'/X,Y'/Y)\\&\quad=\underline{\operatorname{Homs}}(X,Y)\\&\qquad\times_{\underline{\operatorname{Homs}}(X',Y)}\underline{\operatorname{Homs}}(X',Y'),\end{aligned}
\]
the fibre product of \(f^*\) and \(g_*\). By Lemma 1.1 (1) of the lesson on the simplicial derived category, maps \(W\to\underline{\operatorname{Homs}}(X'/X,Y'/Y)\) are pairs of maps \(W\times X\to Y\), \(W\times X'\to Y'\) forming a commutative square with \(W\times f\) and \(g\).

For a simplicial set \(K\) and a map \(Y\to Z\), put
\[
\begin{aligned}&\underline{\operatorname{Homs}}(K,Y/Z)\\&\quad=\underline{\operatorname{Homs}}(K,Y)\times_{\underline{\operatorname{Homs}}(K,Z)}Z,\end{aligned}
\]
where \(Z\to\underline{\operatorname{Homs}}(K,Z)\) is the constant-map morphism. Its maps from \(W\) are the maps \(K\times W\to Y\) whose composite with \(Y\to Z\) factors through the projection to \(W\). So for \(W\) and \(Y\) over \(Z\), maps \(W\to\underline{\operatorname{Homs}}(K,Y/Z)\) over \(Z\) are the maps \(K\times W\to Y\) over \(Z\). For an inclusion of simplicial sets \(Y\subset X\) and maps \(E\to F\to B\), put
\[
\begin{aligned}&\underline{\operatorname{Homs}}(Y/X,E/F/B)\\&\quad=\underline{\operatorname{Homs}}(Y/X,E/F)\times_{\underline{\operatorname{Homs}}(X,B)}B,\end{aligned}
\]
through the maps \(\underline{\operatorname{Homs}}(Y/X,E/F)\to\underline{\operatorname{Homs}}(X,F)\) and \(\underline{\operatorname{Homs}}(X,F)\to\underline{\operatorname{Homs}}(X,B)\) and the constant maps. Its maps from \(W\) are the squares from \(W\times(Y\subset X)\) to \(E\to F\) whose composite with \(F\to B\) factors through the projection \(W\times X\to W\). In particular
\[
\begin{aligned}&\underline{\operatorname{Homs}}(X,E/B)\\&\quad=\underline{\operatorname{Homs}}(X,E)\times_{\underline{\operatorname{Homs}}(X,B)}B.\end{aligned}
\]

**Proposition 2.1.** Let \(j\colon Y\subset X\) be a monomorphism of simplicial sets with \(X\) finite, and \(p\colon E\to F\) a fibration of simplicial sheaves. Then the map
\[
\underline{\operatorname{Homs}}(X,E)\to\underline{\operatorname{Homs}}(Y/X,E/F)
\]
is a fibration. If moreover \(E\) and \(F\) lie over \(B\) and \(p\) is a map over \(B\), then the map from \(\underline{\operatorname{Homs}}(X,E/B)\) to \(\underline{\operatorname{Homs}}(Y/X,E/F/B)\) is a fibration.

**Proof.** Let \(h\colon K\subset L\) be a horn. By the description of maps into these objects, a lifting problem of \(h\) over \(U\) against the first map is a lifting problem of \(h\mathbin\square j\) over \(U\) against \(p\), and local solutions correspond. By Lemma 1.2 (2) of the lesson on local fibrations, \(h\mathbin\square j\) is strict anodyne, and \(p\) has the local lifting property relative to strict anodyne extensions. The second map is the base change of the first along the projection of \(\underline{\operatorname{Homs}}(Y/X,E/F/B)\) to \(\underline{\operatorname{Homs}}(Y/X,E/F)\): both sides are the fibre products with \(B\) over \(\underline{\operatorname{Homs}}(X,B)\). Base changes of fibrations are fibrations. \(\square\)

**Corollary 2.2.** Let \(Y\subset X\) be a monomorphism of finite simplicial sets.

1. If \(E\to F\) is a fibration, so is \(\underline{\operatorname{Homs}}(X,E)\to\underline{\operatorname{Homs}}(X,F)\).
2. If \(E\) is Kan, \(\underline{\operatorname{Homs}}(X,E)\to\underline{\operatorname{Homs}}(Y,E)\) is a fibration, and \(\underline{\operatorname{Homs}}(X,E)\) is Kan.
3. If \(E\to B\) is a fibration, the restriction from \(\underline{\operatorname{Homs}}(X,E/B)\) to the fibre product of \(\underline{\operatorname{Homs}}(Y,E)\) and \(B\) over \(\underline{\operatorname{Homs}}(Y,B)\) is a fibration. In particular the endpoint map \(\underline{\operatorname{Homs}}(\Delta[1],E/B)\to E\times_BE\) is a fibration.

**Proof.** Apply Proposition 2.1 to \(\varnothing\subset X\); to \(E\to e\), whose mapping objects \(\underline{\operatorname{Homs}}(Y,e)\) are \(e\), and then to \(\varnothing\subset X\); and to the map \(E\to B\) over \(B\), for which \(\underline{\operatorname{Homs}}(Y/X,E/B/B)\) is \(\underline{\operatorname{Homs}}(Y,E)\times_{\underline{\operatorname{Homs}}(Y,B)}B\), with \(Y=\partial\Delta[1]\) for the last assertion. \(\square\)

## 3. Path factorization

**Proposition 3.1.** Let \(f\colon E\to F\) be a map of simplicial sheaves over \(B\) such that \(E\to B\) and \(F\to B\) are fibrations. Put \(\operatorname{Path}_B(F)=\underline{\operatorname{Homs}}(\Delta[1],F/B)\), with the evaluations \(\operatorname{ev}_0,\operatorname{ev}_1\) at the two vertices and the constant-path map \(c\colon F\to\operatorname{Path}_B(F)\), and let \(P_f=E\times_F\operatorname{Path}_B(F)\) be the fibre product of \(f\) and \(\operatorname{ev}_0\). Let \(i=(1,cf)\colon E\to P_f\), \(q\colon P_f\to E\) the projection, and \(f'=\operatorname{ev}_1\circ\operatorname{pr}_2\colon P_f\to F\). Then \(f=f'i\), \(qi=1\), \(iq\) is homotopic to the identity by a homotopy over \(B\), and \(f'\) is a fibration. For \(B=e\) this applies to every map between Kan simplicial sheaves, with \(\operatorname{Path}_e(F)=\underline{\operatorname{Homs}}(\Delta[1],F)\).

**Proof.** The identities \(f'i=\operatorname{ev}_1cf=f\) and \(qi=1\) hold by construction. The map \(\operatorname{Path}_B(F)\times\Delta[1]\to\operatorname{Path}_B(F)\) adjoint to \((\omega,s,t)\mapsto\omega(\min(s,t))\) keeps paths over constant paths of \(B\) and fixes \(\operatorname{ev}_0\). So it induces an elementary homotopy on \(P_f\), from \(iq\) at \(s=0\) to the identity at \(s=1\), over \(B\).

The map \((q,f')\colon P_f\to E\times_BF\) is the base change of the endpoint map \(\operatorname{Path}_B(F)\to F\times_BF\) along \(f\times_B1\); the endpoint map is a fibration by Corollary 2.2 (3). The projection \(E\times_BF\to F\) is the base change of the fibration \(E\to B\). So \(f'\), their composite, is a fibration. \(\square\)

## 4. Right fractions

Let \(\operatorname{Hot}_\bullet(T)_{\mathrm{kan}}\) be the full subcategory of \(\operatorname{Hot}_\bullet(T)\) on the Kan simplicial sheaves, and \(D_\bullet(T)_{\mathrm{kan}}\) its localization with respect to the quasi-isomorphisms.

**Theorem 4.1.** Suppose that \(T\) has enough points. In \(\operatorname{Hot}_\bullet(T)_{\mathrm{kan}}\), the quasi-isomorphisms form a right multiplicative system [[Stacks, Tag 04VC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-multiplicative-system)].

**Proof.** *RMS1.* Identities and composites of quasi-isomorphisms are quasi-isomorphisms.

*RMS2.* Let \(s\colon Y\to Z\) be a quasi-isomorphism and \(u\colon X\to Z\) a map between Kan simplicial sheaves. By Proposition 3.1, \(s=s'i\) with \(i\colon Y\to P\), \(qi=1\), \(iq\simeq1\), and \(s'\colon P\to Z\) a fibration, a quasi-isomorphism by two out of three. Let \(t\colon W=X\times_ZP\to X\) be the base change of \(s'\) along \(u\). By Proposition 4.3 of the lesson on local fibrations, \(t\) is a fibration and a quasi-isomorphism, so \(W\) is Kan. Put \(g=q\circ\operatorname{pr}_P\colon W\to Y\). Then \(sg=s'iq\operatorname{pr}_P\simeq s'\operatorname{pr}_P=ut\).

*RMS3.* Let \(f,g\colon X\to Y\) and a quasi-isomorphism \(s\colon Y\to Z\) between Kan simplicial sheaves satisfy \(sf\simeq sg\). With \(s=s'i\) as above, \(s'(if)=sf\simeq sg=s'(ig)\); and if \((if)t\simeq(ig)t\), then \(ft=qift\simeq qigt=gt\). So we may assume that \(s\) is a fibration. Choose a chain of homotopies \(H\colon I\times X\to Z\) from \(sf\) to \(sg\), for a zigzag interval \(I\). Consider
\[
\begin{aligned}u\colon&\underline{\operatorname{Homs}}(I,Y)\\&\to Q=\underline{\operatorname{Homs}}(\partial I/I,Y/Z),\\
v\colon&Q\to\underline{\operatorname{Homs}}(I,Z),\end{aligned}
\]
the canonical map and the projection; \(vu=\underline{\operatorname{Homs}}(I,s)\). By Proposition 2.1, \(u\) is a fibration. The constant-map inclusions \(Y\to\underline{\operatorname{Homs}}(I,Y)\) and \(Z\to\underline{\operatorname{Homs}}(I,Z)\) are homotopy equivalences (Lemma 1.2 (3) of the lesson on the simplicial derived category), so \(\underline{\operatorname{Homs}}(I,s)\) is a quasi-isomorphism by two out of three. The map \(v\) is the base change of \(s\times s\colon Y\times Y\to Z\times Z\) along the restriction to the ends \(\underline{\operatorname{Homs}}(I,Z)\to Z\times Z\); and \(s\times s=(s\times1)(1\times s)\) is a composite of base changes of \(s\). By Proposition 4.3 of the lesson on local fibrations, \(v\) is a fibrant quasi-isomorphism, and so \(u\) is a quasi-isomorphism by two out of three. The maps \((f,g)\colon X\to Y\times Y\) and the adjoint of \(H\) define \(k\colon X\to Q\). Let \(t\colon W=X\times_Q\underline{\operatorname{Homs}}(I,Y)\to X\) be the base change of \(u\) along \(k\). It is a fibrant quasi-isomorphism, so \(W\) is Kan, and the projection \(W\to\underline{\operatorname{Homs}}(I,Y)\) is adjoint to a chain of homotopies from \(ft\) to \(gt\). \(\square\)

**Corollary 4.2.** If \(T\) has enough points, then for Kan simplicial sheaves \(X\) and \(Y\), every morphism \(X\to Y\) of \(D_\bullet(T)_{\mathrm{kan}}\) is \(us^{-1}\) for a fibrant quasi-isomorphism \(s\colon X'\to X\) and a map \(u\colon X'\to Y\), and \(us^{-1}=u's^{-1}\) if and only if \(ut\simeq u't\) for some fibrant quasi-isomorphism \(t\colon X''\to X'\).

**Proof.** By Theorem 4.1 and [[Stacks, Tag 04VI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-morphisms-right-localization), [Tag 04VJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-equality-morphisms-right-localization), [Tag 04VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-properties-right-localization)], the morphisms are right fractions \(us^{-1}\) with \(s\) a quasi-isomorphism, and equality is detected after composing with a quasi-isomorphism. By Proposition 3.1 every quasi-isomorphism \(s\) between Kan simplicial sheaves is \(s'i\) with \(i\) a homotopy equivalence, invertible in the homotopy category, and \(s'\) a fibrant quasi-isomorphism; then \(us^{-1}=(uq)s'^{-1}\). \(\square\)

**Theorem 4.3.** For every topos \(T\), the functor \(D_\bullet(T)_{\mathrm{kan}}\to D_\bullet(T)\) induced by the inclusion is an equivalence of categories, with a quasi-inverse induced by \(\operatorname{Ex}^\infty\).

**Proof.** By Remark 4.2 of the lesson on local fibrations, \(\operatorname{Ex}^\infty\) is a functor \(\operatorname{Hot}_\bullet(T)\to\operatorname{Hot}_\bullet(T)_{\mathrm{kan}}\), and it carries quasi-isomorphisms to quasi-isomorphisms (Proposition 4.1 there and two out of three). Since \(D_\bullet(T)\) is the localization of \(\operatorname{Hot}_\bullet(T)\) with respect to quasi-isomorphisms (Corollary 4.3 of the lesson on the simplicial derived category), it induces a functor \(G\colon D_\bullet(T)\to D_\bullet(T)_{\mathrm{kan}}\). Let \(J\) be the functor of the statement. The maps \(e^\infty_X\colon X\to\operatorname{Ex}^\infty(X)\) are natural quasi-isomorphisms, so they give natural isomorphisms from the identity of \(D_\bullet(T)\) to \(JG\), and from the identity of \(D_\bullet(T)_{\mathrm{kan}}\) to \(GJ\); natural transformations defined on the homotopy categories extend to the localizations. \(\square\)

**Corollary 4.4.** For the topos of sets, \(D_\bullet(\mathrm{Sets})\) is equivalent to the homotopy category \(\operatorname{Ho}(\mathrm{Kan})\) of Kan complexes.

**Proof.** In \(\operatorname{Hot}_\bullet(\mathrm{Sets})_{\mathrm{kan}}=\operatorname{Ho}(\mathrm{Kan})\), every quasi-isomorphism is already invertible: a quasi-isomorphism between Kan complexes is a homotopy equivalence (Theorem 5.3f of the lesson on Kan complexes). So \(D_\bullet(\mathrm{Sets})_{\mathrm{kan}}=\operatorname{Ho}(\mathrm{Kan})\), and Theorem 4.3 applies. \(\square\)

**Remark 4.5.** As for the left fractions, Illusie remarks that the hypothesis of enough points in Theorem 4.1 is probably unnecessary. Theorem 4.3 holds without it.

## 5. Over a fixed simplicial sheaf

Fix a simplicial sheaf \(B\). Let \(\operatorname{Hotfib}_\bullet(T,B)\) be the full subcategory of \(\operatorname{Hot}_\bullet(T,B)\) (Section 6 of the lesson on the simplicial derived category) on the objects \(E\to B\) that are fibrations, and \(D'_\bullet(T,B)\) its localization with respect to the quasi-isomorphisms.

**Proposition 5.1.** For every topos \(T\) there are a functor \(R_B\) on \(\operatorname{Simpl}(T)_{/B}\) and a natural monomorphism and quasi-isomorphism \(\eta_X\colon X\to R_B(X)\) over \(B\) such that \(R_B(X)\to B\) is a fibration.

**Proof.** Put \(X^{(0)}=X\). Given \(X^{(r)}\) over \(B\), let \(A_{m,k}\) be the sheaf of horn squares
\[
\begin{aligned}A_{m,k}={}&\operatorname{Hom}(\Lambda^k[m],X^{(r)})\\&\times_{\operatorname{Hom}(\Lambda^k[m],B)}\operatorname{Hom}(\Delta[m],B)\end{aligned}
\]
for \(m\geq1\), \(0\leq k\leq m\), and let \(X^{(r+1)}\) be the pushout of
\[
\begin{aligned}X^{(r)}&\leftarrow\textstyle\coprod A_{m,k}\times\Lambda^k[m]\\&\to\textstyle\coprod A_{m,k}\times\Delta[m],\end{aligned}
\]
the first map given by evaluation, with the map to \(B\) given by evaluation on the second term. Let \(R_B(X)\) be the colimit of the \(X^{(r)}\). The construction is natural in \(X\) over \(B\).

The maps \(A\times\Lambda^k[m]\to A\times\Delta[m]\) are monomorphisms, so are their pushouts in the topos \(\operatorname{Simpl}(T)\) and the colimit map \(\eta_X\). A lifting problem of a horn over \(U\) against \(R_B(X)\to B\) is a section over \(U\) of the corresponding sheaf of horn squares for \(R_B(X)\), the colimit of those for the \(X^{(r)}\), since horns are finite; locally it comes from some \(A_{m,k}\) at a stage \(r\), and the attached simplex at the stage \(r+1\) solves it. So \(R_B(X)\to B\) is a fibration.

The sheaf \(X^{(r+1)}\) is associated with the presheaf pushout \(P\) formed with the sets of sections \(A_{m,k}(V)\). For every \(V\), \(X^{(r)}(V)\to P(V)\) is a pushout of a coproduct of horn inclusions, hence anodyne, hence a quasi-isomorphism of simplicial sets. As at the start of Section 3 of the lesson on the simplicial derived category, the homotopy sheaves of \(X^{(r)}\) and \(X^{(r+1)}\) are associated with the presheaves of homotopy groups of \(V\mapsto X^{(r)}(V)\) and of \(P\); so \(X^{(r)}\to X^{(r+1)}\) is a quasi-isomorphism. Homotopy sheaves commute with filtered colimits (Proposition 1.5 (1) of the lesson on homotopy sheaves), so \(\eta_X\) is a quasi-isomorphism. \(\square\)

**Theorem 5.2.**

1. If \(T\) has enough points, the quasi-isomorphisms of \(\operatorname{Hotfib}_\bullet(T,B)\) form a right multiplicative system.
2. For every topos \(T\), the functor \(D'_\bullet(T,B)\to D_\bullet(T,B)\) induced by the inclusion is an equivalence of categories.

**Proof.** (1) The proof of Theorem 4.1 applies over \(B\), with Proposition 3.1 over \(B\) and relative mapping objects. In RMS2, \(W=X\times_ZP\to X\) is a fibrant quasi-isomorphism and \(X\to B\) a fibration, so \(W\to B\) is a fibration; the homotopy \(iq\simeq1\) is over \(B\). In RMS3, after replacing \(s\) by a fibration \(s\colon Y\to Z\) over \(B\), use the map \(u\) from \(\underline{\operatorname{Homs}}(I,Y/B)\) to \(Q_B=\underline{\operatorname{Homs}}(\partial I/I,Y/Z/B)\), a fibration by Proposition 2.1, and the projection \(v\colon Q_B\to\underline{\operatorname{Homs}}(I,Z/B)\), the base change of \(s\times_Bs\colon Y\times_BY\to Z\times_BZ\), a composite of base changes of \(s\). The contracting homotopies of \(I\) (Lemma 1.2 (3) of the lesson on the simplicial derived category) preserve paths over constant paths of \(B\), so \(Y\to\underline{\operatorname{Homs}}(I,Y/B)\) and \(Z\to\underline{\operatorname{Homs}}(I,Z/B)\) are homotopy equivalences, and \(u\) is a quasi-isomorphism by two out of three. A chain of \(B\)-homotopies \(I\times X\to Z\) from \(sf\) to \(sg\) defines \(X\to Q_B\), and the base change of \(u\) along it gives \(t\colon W\to X\), a fibrant quasi-isomorphism with \(W\to B\) a fibration, and a chain of \(B\)-homotopies from \(ft\) to \(gt\).

(2) The functor \(X\mapsto R_B(X)\) from \(\operatorname{Simpl}(T)_{/B}\) to \(D'_\bullet(T,B)\) carries quasi-isomorphisms to isomorphisms, because \(R_B(f)\) is a quasi-isomorphism between fibrant objects by two out of three with \(\eta\). So it factors through \(D_\bullet(T,B)\), the localization of \(\operatorname{Simpl}(T)_{/B}\), and gives \(G\colon D_\bullet(T,B)\to D'_\bullet(T,B)\). Let \(J\) be the functor of the statement, induced by the inclusion of \(\operatorname{Hotfib}_\bullet(T,B)\) into \(\operatorname{Hot}_\bullet(T,B)\) followed by the localization functor to \(D_\bullet(T,B)\) (Proposition 6.1 of the lesson on the simplicial derived category). The maps \(\eta\) are natural quasi-isomorphisms over \(B\). They give a natural isomorphism from the identity of \(D_\bullet(T,B)\) to \(JG\), natural on \(\operatorname{Simpl}(T)_{/B}\) and hence on its localization. On \(\operatorname{Hotfib}_\bullet(T,B)\), the composite \(GJ\) sends the class of a map \(f\) to the class of \(R_B(f)\), and \(\eta\) is natural with respect to maps; its components are quasi-isomorphisms between fibrant objects, hence isomorphisms of \(D'_\bullet(T,B)\). So \(\eta\) is a natural isomorphism from the identity to \(GJ\). \(\square\)

## 6. Exercises

**Exercise 6.1** (easy). Let \(\phi\colon A\to A'\) be a homomorphism of sheaves of groups, regarded as a map of constant simplicial groups. Show that \(\phi\) is a fibration, compute \(N\phi\), and show that \(\phi\) is a quasi-isomorphism if and only if it is an isomorphism.

**Exercise 6.2** (medium). Let \(H\subset G\) be a simplicial subgroup of a simplicial group of \(T\). Show that the inclusion is a fibration if and only if \(H_n=G_n\times_{\pi_0(G)}\pi_0(H)\) for every \(n\), that is, \(H\) consists of the simplices of \(G\) whose class in \(\pi_0(G)\) lies in the image of \(\pi_0(H)\).

**Exercise 6.3** (medium). Suppose that \(T\) has enough points. Let \(p\colon E\to F\) be a fibrant quasi-isomorphism and \(K\) a finite simplicial set. Show that \(\underline{\operatorname{Homs}}(K,E)\to\underline{\operatorname{Homs}}(K,F)\) is a fibrant quasi-isomorphism.

**Exercise 6.4** (hard). Let \(f\colon G\to H\) be a homomorphism of simplicial groups of \(T\) that is an epimorphism in every degree, with kernel \(K\). Construct homomorphisms \(\delta\colon\pi_n(H)\to\pi_{n-1}(K)\), \(n\geq1\), such that the sequence
\[
\begin{aligned}\cdots&\to\pi_n(K)\to\pi_n(G)\to\pi_n(H)\\&\xrightarrow{\delta}\pi_{n-1}(K)\to\cdots\to\pi_0(K)\\&\to\pi_0(G)\to\pi_0(H)\to1\end{aligned}
\]
of sheaves of groups is exact.

## 7. Complete solutions

**Solution 6.1.** By Proposition 2.5 (4) of the lesson on local fibrations, a map of constant simplicial sheaves is a fibration. For a constant simplicial group all faces are the identity, so \(N_0=A\) and \(N_n=1\) for \(n\geq1\); \(N\phi\) is \(\phi\) in degree \(0\). By Proposition 1.2, \(\pi_0=A\) and \(\pi_n=1\) for \(n\geq1\), so \(\phi\) is a quasi-isomorphism exactly when \(\phi\) is an isomorphism of sheaves.

**Solution 6.2.** Apply Proposition 1.4 to the inclusion \(f\). Condition (3) says that the monomorphism \(H\to G\times_{\pi_0(G)}\pi_0(H)\) is an epimorphism in every degree, that is, an isomorphism.

**Solution 6.3.** By Corollary 2.2 (1), the map is a fibration. At a point \(x\), \(p_x\) is a trivial fibration (Theorem 3.7 of the lesson on local fibrations), and \(\underline{\operatorname{Homs}}(K,p)_x=\underline{\operatorname{Homs}}(K,p_x)\) (Lemma 1.1 (2) of the lesson on the simplicial derived category). A lifting problem of a monomorphism \(i\) against \(\underline{\operatorname{Homs}}(K,p_x)\) is one of the monomorphism \(i\mathbin\square(\varnothing\subset K)=i\times K\) against \(p_x\), which has a solution. So \(\underline{\operatorname{Homs}}(K,p_x)\) is a trivial fibration, hence a quasi-isomorphism, and the map is a quasi-isomorphism by Corollary 3.3 (3) of the lesson on the simplicial derived category.

**Solution 6.4.** By Proposition 1.4, \(f\) is a fibration and \(N_nf\) is an epimorphism with kernel \(N_nK\) for every \(n\geq0\). By Proposition 1.2 it suffices to construct the exact sequence of the homology sheaves of \(NK\), \(NG\), \(NH\); we argue with local sections. For \(z\in Z_n(NH)\), \(n\geq1\), lift it to \(g\in N_nG\); then \(d_0g\in Z_{n-1}(NK)\). Another lift is \(gk\) with \(k\in N_nK\), changing \(d_0g\) by \(d_0k\in B_{n-1}(NK)\); if \(z=d_0(c)\), lifting \(c\) to \(c'\in N_{n+1}G\) gives the lift \(g=d_0c'\) with \(d_0g=1\). So \(\delta[z]=[d_0g]\) is well defined, and it is a homomorphism because \(d_0\) is one.

*Exactness at \(\pi_n(G)\).* A class from \(K\) maps to \(1\). If \(g\in Z_n(NG)\) has \(f(g)=d_0(c)\), lift \(c\) to \(c'\); then \(g\,d_0(c')^{-1}\in Z_n(NK)\) has the class of \(g\).

*Exactness at \(\pi_n(H)\).* The boundary of \(f(g)\), \(g\) a cycle, is computed with the lift \(g\) and is \(1\). If \(\delta[z]=1\), then \(d_0g=d_0k\) with \(k\in N_nK\), and \(gk^{-1}\) is a cycle of \(NG\) over \(z\).

*Exactness at \(\pi_{n-1}(K)\).* The class \([d_0g]\) becomes \(1\) in \(\pi_{n-1}(G)\). If \(k\in Z_{n-1}(NK)\) becomes \(1\) in \(\pi_{n-1}(G)\), then \(k=d_0(g)\) with \(g\in N_nG\), and \(f(g)\) is a cycle with \(\delta[f(g)]=[k]\).

*The end.* \(\pi_0(G)\to\pi_0(H)\) is an epimorphism because \(f_0\) is one.

## Sources

The calculus of right fractions for Kan simplicial sheaves, the path factorization, the mapping objects relative to maps and their fibrations, the description of fibrations of simplicial groups through the normalized complex, the equivalence of the Kan derived category with the simplicial derived category and the relative versions over a simplicial sheaf are due to Illusie, in his work on the cotangent complex; the relative fibrant replacement follows the functorial construction of Gabriel and Zisman. The identification of the homotopy groups of a simplicial group with the homology of its normalized complex is due to Moore. Right multiplicative systems are taken from the AI-integrated Stacks project [[Stacks, Tag 04VB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-section-localization)].
