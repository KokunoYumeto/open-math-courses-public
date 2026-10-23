# Torsors, co-Lie complexes and the Atiyah class

*Written by Claude Opus 5.5 (Anthropic) on 21 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(G\) be a group scheme over a scheme \(S\), flat and locally of finite presentation, and \(f\colon X\to Y\) a torsor under \(G\) over a scheme \(Y\). Locally for the fppf topology \(X\) is the trivial torsor \(G\times_SY\), and the nerve \(N(G,X)\) of the action is the Čech nerve of the covering \(X\to Y\). This lesson develops descent along \(f\) for the objects from which equivariant cotangent complexes are made. Equivariant modules on \(X\) are the same as modules on \(Y\). Bounded complexes on the nerve whose cohomology is cartesian come from \(Y\), on the big fppf sites and, for quasi-coherent cohomology, on the Zariski sites. The cotangent complex of the morphism of nerves \(N(G,X)\to N(G,Y)\) therefore descends to \(Y\): it is the *co-Lie complex* \(\ell_{X/Y}\), a perfect complex with tor amplitude in \([-1,0]\), compatible with base change. The transitivity triangle of \(N(G,X)\to N(G,Y)\to N(G)\) descends to a distinguished triangle \(t_{[n}L_{Y/S}\to\) \(\ell_n(X/S)\to\) \(\ell_{X/Y}\to\) \(t_{[n}L_{Y/S}[1]\), whose third map is the *Atiyah class* of the torsor, and which determines the equivariant Kodaira–Spencer class. When \(G\) is smooth, \(\ell_{X/Y}\) is the twist of the co-Lie algebra of \(G\) by \(X\) through the coadjoint action, and the Atiyah triangle is an exact sequence of differential forms, the algebraic form of the sequence introduced by Atiyah for principal bundles.

**Prerequisites.** [*Equivariant cotangent complexes*](equivariant-cotangent-complexes.md) (its notation throughout; Lemmas 1.3, 2.2, Propositions 1.5, 1.6, 2.3, 2.5, 3.3, Theorem 2.4); [*Flat group schemes are local complete intersections*](flat-group-schemes-are-local-complete-intersections.md) (Theorem 3.1 and its proof); [*Quasi-coherent and perfect complexes on big fppf sites*](quasi-coherent-and-perfect-complexes-on-big-fppf-sites.md) (Propositions 1.2 and 2.1, Corollary 2.2, Lemma 2.3, Construction 4.1, Lemma 4.2); [*Deformations of diagrams of schemes*](deformations-of-diagrams-of-schemes.md) (Conventions, Propositions 1.2–1.4); [*Equivariant sheaves on simplicial topoi*](equivariant-sheaves-on-simplicial-topoi.md) (Definition 1.1, Propositions 2.3 and 2.4, Section 6); [*Equivariant extensions and deformations*](equivariant-extensions-and-deformations.md) (Lemma 1.1 and Proposition 1.2, for Exercise 5.2). From the programme lesson [*The cotangent complex*](course:AG-HP/the-cotangent-complex#2-independence-of-the-resolution): Theorem 2.2, [Theorem 4.1](course:AG-HP/the-cotangent-complex#4-the-fundamental-triangle), Proposition 5.1, Theorem 6.1, Theorem 7.2 with formula (7.3), and [Proposition 10.1](course:AG-HP/the-cotangent-complex#10-morphisms-of-schemes). From the AI-integrated Stacks project: syntomic and smooth morphisms and their descent [[Stacks, Tag 01UI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-syntomic), [Tag 02VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-descending-property-syntomic), [Tag 02VL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-descending-property-smooth)]; differentials [[Tag 02G1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-omega-finite-locally-free), [Tag 01V0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-differentials)]; descent of perfect complexes and tor amplitude [[Tag 09UD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-tor-amplitude-descends), [Tag 09UG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-perfect-descends-fpqc), [Tag 08H5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-tor-amplitude-pullback)]; adequate modules [[Tag 06VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/adequate.html#adequate-lemma-adequate-characterize)]; derived pullback, direct images and base change maps [[Tag 07A6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-adjoint), [Tag 07A7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-remark-base-change), [Tag 0D6D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-pullback-composition), [Tag 0D6G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-restrict-direct-image-open)]; triangles and truncations [[Tag 05QT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-split), [Tag 06XS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-negative-exts), [Tag 0149](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-representable-homological), [Tag 014A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-third-isomorphism-triangle), [Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)].

## Conventions

The notation is that of [*Equivariant cotangent complexes*](equivariant-cotangent-complexes.md): \(T\) is the big fppf topos of \(S\), \(N(G,X)\) the nerve of the action category of a \(G\)-scheme \(X\), \(v_0\colon N_n(G,X)\to X\) the first vertex, \(B[G,X]^{\mathrm o}\) the classifying category of the opposite category, \(\operatorname{ner}\) the nerve functor of its Proposition 1.5, \(\varepsilon\) the comparison morphisms between big fppf and Zariski topoi, \(t_{[n}=\tau_{\geq n}\), and \(t_{[}L^G\) the equivariant cotangent complex. Here \(G\) is a group scheme over \(S\), flat and locally of finite presentation, with unit \(e\). A module of \(B[G,X]^{\mathrm o}\) is an \(\mathcal O\)-module \(M\) of \(T/X\) with a map \(m\colon\mathrm{act}^*M\to\mathrm{pr}^*M\) on \(G\times_SX\), where \(\mathrm{act}(g,x)=gx\) and \(\mathrm{pr}(g,x)=x\) (Proposition 1.5 (2) there). For a point \(x\) of \(X\) with values in a scheme \(U\), write \(M_x=x^*M\), a module on \((\mathrm{Sch}/U)_{\mathrm{fppf}}\), and \(m_{(g,x)}\colon M_{gx}\to M_x\) for the pullback of \(m\) along \((g,x)\). The two conditions of Definition 1.1 of [*Equivariant sheaves on simplicial topoi*](equivariant-sheaves-on-simplicial-topoi.md) read, for all points \(g,h\) of \(G\) and \(x\) of \(X\) with values in the same scheme,
\[
\begin{gathered}m_{(e,x)}=\mathrm{id},\\ m_{(h,x)}\circ m_{(g,hx)} =m_{(gh,x)}\\ \colon M_{ghx} \to M_x .\end{gathered} \tag{0.1}
\]
Indeed, two composable arrows of \([G,X]^{\mathrm o}\) are \(ghx\to hx\to x\), given by \((g,hx)\) and \((h,x)\), with composite \((gh,x)\). Equalities of maps of modules are checked on points with values in arbitrary schemes.

Every scheme \(Y\) over \(S\) has the trivial action of \(G\), and \(G_Y=G\times_SY\). By Lemma 1.3 of the lesson on equivariant cotangent complexes, \(N(G,Y)=N(G)\times_SY\), with the faces and degeneracies of \(N(G)=N(G,S)\) times the identity of \(Y\), and the projection \(q\colon N(G,Y)\to Y\) is a morphism to the constant simplicial scheme \(Y\). For a \(G\)-scheme \(X\) and a morphism \(f\colon X\to Y\) with \(f(gx)=f(x)\), the morphisms \(a_n=f\circ v_0\colon N_n(G,X)\to Y\) form a morphism \(a=q\circ N(G,f)\) from \(N(G,X)\) to the constant simplicial scheme \(Y\). It defines morphisms of ringed topoi \(a\colon\operatorname{Top}(N(G,X)_{\mathrm{Zar}})\to Y_{\mathrm{Zar}}\) and \(a\colon\operatorname{Top}(N(G,X)_{\mathrm{fppf}})\to T/Y\), as in the Conventions of [*Deformations of diagrams of schemes*](deformations-of-diagrams-of-schemes.md) and Construction 4.1 of the lesson on big fppf sites, with \((a^*E)_n=a_n^*E\). For a morphism of \(S\)-schemes \(V\to Y\), \(X_V=X\times_YV\).

## 1. Torsors

**Definition 1.1.** Let \(Y\) be a scheme over \(S\). A *torsor under \(G\) over \(Y\)*, or *\(G_Y\)-torsor*, is a \(G\)-scheme \(X\) with a morphism of \(S\)-schemes \(f\colon X\to Y\), \(f(gx)=f(x)\), such that

1. the morphism \(G\times_SX\to X\times_YX\), \((g,x)\mapsto(gx,x)\), is an isomorphism;
2. there is an fpqc covering \(\{Y_i\to Y\}\) such that every \(X_{Y_i}\to Y_i\) has a section.

A morphism of \(G_Y\)-torsors is a morphism of \(G\)-schemes over \(Y\). The *trivial torsor* is \(G_Y\to Y\), with \(G\) acting by left multiplication on the first factor.

**Lemma 1.2.** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor.

1. For every morphism \(Y'\to Y\), \(X_{Y'}\to Y'\) is a \(G_{Y'}\)-torsor.
2. If \(\sigma\colon Y\to X\) is a section of \(f\), then \(\psi_\sigma\colon G_Y\to X\), \((g,y)\mapsto g\sigma(y)\), is an isomorphism of \(G_Y\)-torsors.

**Proof.** (1) Both conditions are stable under base change, and fpqc coverings are stable under base change. (2) \(\psi_\sigma\) is a morphism of \(G\)-schemes over \(Y\). For a point \(x\) of \(X\), \((x,\sigma(f(x)))\) is a point of \(X\times_YX\), so condition 1 gives a unique point \(g\) of \(G\) with \(x=g\sigma(f(x))\), functorial in \(x\). Then \(x\mapsto(g,f(x))\) is inverse to \(\psi_\sigma\). \(\square\)

**Proposition 1.3.** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor.

1. \(f\) is syntomic and surjective, in particular faithfully flat and locally of finite presentation, so \(\{X\to Y\}\) is an fppf covering. The torsor \(X\times_YX\to X\) (first projection) has the diagonal as a section.
2. The morphisms \(\phi_n\colon N_n(G,X)\to X\times_Y\cdots\times_YX\) (\(n+1\) factors),
\[
\begin{aligned}&(g_1,\ldots,g_n;x)\longmapsto\\&\quad(x,\ g_1x,\ g_2g_1x,\ \ldots,\\&\qquad g_n\cdots g_1x),\end{aligned}
\]
form an isomorphism of simplicial schemes over \(Y\) from \(N(G,X)\) onto the *Čech nerve* of \(f\), whose map for \(\alpha\colon[m]\to[n]\) is \((x_0,\ldots,x_n)\mapsto(x_{\alpha(0)},\ldots,x_{\alpha(m)})\). In particular every face of \(N(G,X)\) is flat, being a base change of \(f\).

**Proof.** (1) Take a covering as in condition 2. By Lemma 1.2, \(X_{Y_i}\cong G_{Y_i}\), which is syntomic over \(Y_i\) by Theorem 3.1 of [*Flat group schemes are local complete intersections*](flat-group-schemes-are-local-complete-intersections.md) and [Tag 01UI], and surjective, as it has the unit section. Being syntomic is fpqc local on the base [Tag 02VK], so \(f\) is syntomic. Every point of \(Y\) comes from some \(Y_i\), hence from \(X\). The first projection \(X\times_YX\to X\) is the base change of \(f\) along \(f\), a torsor by Lemma 1.2 (1).

(2) By Lemma 1.3 of the lesson on equivariant cotangent complexes, the vertex \(k\) of \((g_1,\ldots,g_n;x)\) is \(g_k\cdots g_1x\), and \(N(G,X)(\alpha)\) keeps the vertices \(\alpha(0),\ldots,\alpha(m)\). This is the formula of the Čech nerve, and \(\phi\) is over \(Y\) because \(f\) is invariant. For a point \((x_0,\ldots,x_n)\), condition 1 gives unique points \(g_k\) of \(G\) with \(x_k=g_kx_{k-1}\), \(1\leq k\leq n\), and \((g_1,\ldots,g_n;x_0)\) is the inverse image. The faces of the Čech nerve omit one factor; they are base changes of \(f\). \(\square\)

## 2. Descent along a torsor

**Construction 2.1.** Let \(f\colon X\to Y\) be an invariant morphism from a \(G\)-scheme.

(a) For an \(\mathcal O\)-module \(E\) of \(T/Y\), \(f^*E\) is its restriction to \(T/X\). Since \(f\circ\mathrm{act}=f\circ\mathrm{pr}\), \(\mathrm{act}^*f^*E\) and \(\mathrm{pr}^*f^*E\) are both the restriction of \(E\) along this morphism, and the identity \(m_E\) between them satisfies (0.1). This defines an exact functor
\[
f^{G*}\colon\operatorname{Mod}(T/Y)\longrightarrow\operatorname{Mod}(B[G,X]^{\mathrm o}).
\]
The nerve of \(f^{G*}E\) has the levels \(v_0^*f^*E=a_n^*E\) with the canonical structure maps, so \(\operatorname{ner}\circ f^{G*}=a^*\).

(b) For a module \(M\) of \(B[G,X]^{\mathrm o}\) and a scheme \(V\) over \(Y\), let \(\mathrm{act}_V,\mathrm{pr}_V\colon G\times_SX_V\to X_V\) be the base changes of \(\mathrm{act}\) and \(\mathrm{pr}\), and put
\[
\begin{aligned}(f^G_*M)(V)=\bigl\{s\in M(X_V)\ :\ &m(\mathrm{act}_V^*s)\\&=\mathrm{pr}_V^*s\bigr\}.\end{aligned}
\]
Here \(M(X_V)\) is the module of sections over the object \(X_V\to X\) of \((\mathrm{Sch}/X)_{\mathrm{fppf}}\), \(\mathrm{act}_V^*s\) is a section of \(\mathrm{act}^*M\) and \(\mathrm{pr}_V^*s\) one of \(\mathrm{pr}^*M\) over \(G\times_SX_V\). On points, \(s\) lies in \(f^G_*M\) when \(m_{(g,x)}(s(gx))=s(x)\). Restrictions make \(f^G_*M\) a sheaf, because \(M\) is one and \(\{X_{V_k}\to X_V\}\) is a covering for a covering \(\{V_k\to V\}\). It is an \(\mathcal O\)-module: \(\mathcal O(V)\) acts through \(\mathcal O(V)\to\mathcal O(X_V)\), and the condition is linear because \(m\) is linear and a function on \(V\) has the same pullback along \(\mathrm{act}_V\) and \(\mathrm{pr}_V\).

(c) The map \(\eta_E\colon E\to f^G_*f^{G*}E\) sends \(s\in E(V)\) to its restriction to \(X_V\); this satisfies the condition of (b), since \(\mathrm{act}_V\) and \(\mathrm{pr}_V\) agree after composition with \(X_V\to V\). The map \(c_M\colon f^{G*}f^G_*M\to M\) sends, for a scheme \(w\colon W\to X\) over \(X\), viewed over \(Y\) through \(fw\), a section \(s\in(f^G_*M)(W)\subseteq M(X_W)\) to \(\sigma_w^*s\in M(W)\), where \(\sigma_w=(w,\mathrm{id}_W)\colon W\to X_W\) is a section of \(X_W\to W\) over \(X\).

**Proposition 2.2 (descent along a torsor).** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor.

1. \(\eta_E\) is an isomorphism for every \(\mathcal O\)-module \(E\) of \(T/Y\).
2. \(c_M\) is an isomorphism of modules of \(B[G,X]^{\mathrm o}\) for every module \(M\) of \(B[G,X]^{\mathrm o}\).
3. \(f^{G*}\) is an equivalence of abelian categories with quasi-inverse \(f^G_*\); both are exact, and \(f^{G*}\mathcal O=\mathcal O\).
4. Both functors commute with base change: for \(Y'\to Y\), \((f^G_*M)|_{Y'}=f'^G_*(M|_{X_{Y'}})\) and \((f^{G*}E)|_{X_{Y'}}=f'^{G*}(E|_{Y'})\), with \(f'\colon X_{Y'}\to Y'\).

**Proof.** (4) holds by construction, as \((X_{Y'})_V=X_V\) for \(V\) over \(Y'\).

(1) A section of \(f^G_*f^{G*}E\) over \(V\) is an \(s\in E(X_V)\) with \(\mathrm{act}_V^*s=\mathrm{pr}_V^*s\) in \(E(G\times_SX_V)\). By Lemma 1.2 (1) and condition 1, \((g,x)\mapsto(gx,x)\) is an isomorphism \(G\times_SX_V\to X_V\times_VX_V\) carrying \(\mathrm{act}_V\) and \(\mathrm{pr}_V\) to the two projections. By Proposition 1.3 (1), \(\{X_V\to V\}\) is an fppf covering, so the sheaf property of \(E\) says that restriction is a bijection from \(E(V)\) onto these sections.

(2) By (0.1), \(m_{(g,x)}\circ m_{(g^{-1},gx)}=m_{(e,gx)}=\mathrm{id}\) and \(m_{(g^{-1},gx)}\circ m_{(g,x)}=m_{(e,x)}=\mathrm{id}\), so \(m\) is invertible. Let \(w\colon W\to X\). By Lemma 1.2, \(\psi\colon G\times_SW\to X_W\), \((g,w')\mapsto(gw(w'),w')\), is an isomorphism. A section \(s\in(f^G_*M)(W)\) satisfies, at the points \((g\,w(w'),w')\),
\[
\begin{aligned}&s\bigl(g\,w(w'),w'\bigr)\\&\quad =m^{-1}_{(g,w(w'))}\bigl(s(w(w'),w')\bigr),\end{aligned}
\]
by its condition at the pair \((g,w(w'))\). Since \(\psi\) is an isomorphism, \(s\) is determined by \(\sigma_w^*s=c_M(s)\), and \(c_M\) is injective on sections over \(W\). Conversely, for \(t\in M(W)\), define \(s\in M(X_W)\) by \(s(gw(w'),w')=m^{-1}_{(g,w(w'))}(t(w'))\), that is, \(\psi^*s=j^*(m)^{-1}(q^*t)\) for \(j=\mathrm{id}_G\times w\colon G\times_SW\to G\times_SX\) and the projection \(q\colon G\times_SW\to W\). Then \(\sigma_w^*s=t\) by the first condition of (0.1), and \(s\) lies in \(f^G_*M\): for a point \(h\) of \(G\), writing \(w\) for \(w(w')\),
\[
\begin{aligned}&m_{(h,gw)}\bigl(s(hgw,w')\bigr)\\&\quad=m_{(h,gw)}\,m^{-1}_{(hg,w)}\bigl(t(w')\bigr)\\&\quad=m^{-1}_{(g,w)}\bigl(t(w')\bigr)=s(gw,w'),\end{aligned}
\]
because \(m_{(g,w)}\circ m_{(h,gw)}=m_{(hg,w)}\) by (0.1). So \(c_M\) is bijective on sections over every \(W\). It is compatible with the structures: for an invariant section \(s\), \(m_{(g,x)}(c_M(s)_{gx})=\) \(m_{(g,x)}(s(gx))=\) \(s(x)=\) \(c_M(s)_x\), while the structure of \(f^{G*}f^G_*M\) is the identity of (a).

(3) By (1) and (2), \(f^{G*}\) and \(f^G_*\) are quasi-inverse equivalences, hence exact. \(f^{G*}\mathcal O\) is \(\mathcal O\) with the identity structure, the ring of \(B[G,X]^{\mathrm o}\). \(\square\)

**Lemma 2.3.** For every module \(M\) of \(B[G,X]^{\mathrm o}\), \(m\) is invertible and \(\operatorname{ner}(M)\) is cartesian. A module of \(\operatorname{Top}(N(G,X)_{\mathrm{fppf}})\) is isomorphic to the nerve of a module of \(B[G,X]^{\mathrm o}\) if and only if it is cartesian.

**Proof.** The inverse of \(m\) was found in the proof of Proposition 2.2 (2), which used only (0.1). By Proposition 2.4 of the lesson on equivariant sheaves, in its module form (Section 6 there), the nerves of a sheaf with invertible structure are cartesian. Conversely, a cartesian module has invertible structure maps along every \(\alpha\) with \(\alpha(0)=0\), so it is isomorphic to a nerve by Proposition 2.3 of that lesson in its module form, as in the proof of Proposition 1.5 (3) of the lesson on equivariant cotangent complexes. \(\square\)

**Theorem 2.4 (descent on big sites).** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor. Then \(f^{G*}\colon D^b(T/Y)\to D^b(B[G,X]^{\mathrm o})\) is an equivalence, and
\[
\begin{aligned}&a^* =\operatorname{ner}\circ f^{G*} \colon D^b(T/Y)\\&\quad \longrightarrow D^b\bigl(\operatorname{Top}(N(G,X)_{\mathrm{fppf}})\bigr)\end{aligned}
\]
is fully faithful. Its essential image consists of the objects whose cohomology modules are cartesian; these are the quasi-cartesian objects of \(D^b\).

**Proof.** An exact equivalence of abelian categories induces an equivalence of bounded derived categories, so the first assertion follows from Proposition 2.2 (3). By Proposition 1.5 (3) of the lesson on equivariant cotangent complexes, \(\operatorname{ner}\) is fully faithful on \(D^b\), with essential image the objects whose cohomology modules have invertible structure maps along every \(\alpha\) with \(\alpha(0)=0\); by Lemma 2.3 these are the objects with cartesian cohomology modules. On big sites the inverse images along the levels are exact, so these are the quasi-cartesian objects (Lemma 4.2 (3) of the lesson on big fppf sites). \(\square\)

**Theorem 2.5 (descent on Zariski sites).** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor. The functor
\[
a^*\colon D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\longrightarrow D^b\bigl(N(G,X)_{\mathrm{Zar}}\bigr)
\]
is fully faithful. Its essential image consists of the quasi-cartesian objects with termwise quasi-coherent cohomology.

**Proof.** Every \(a_n=f\circ v_0\) is flat, \(v_0\colon G^n\times_SX\to X\) being a projection and \(G\) flat. So \(a^*\) is exact, and \(a^*E\) has the termwise quasi-coherent cohomology \(a^*H^i(E)\). It is quasi-cartesian: \(a_n=a_m\circ N(G,X)(\alpha)\), and its structure maps are the canonical isomorphisms \(LN(G,X)(\alpha)^*a_m^*E\cong a_n^*E\) [Tag 0D6D].

The comparison morphisms satisfy \(\varepsilon\circ a=a\circ\varepsilon\) as morphisms of ringed topoi from \(\operatorname{Top}(N(G,X)_{\mathrm{fppf}})\) to \(Y_{\mathrm{Zar}}\), levelwise by Construction 4.1 of the lesson on big fppf sites. Hence \(L\varepsilon^*a^*\cong a^*L\varepsilon^*\) [Tag 0D6D], and for \(F\in D^+(T/Y)\) there is a base change map \(a^*R\varepsilon_*F\to R\varepsilon_*a^*F\) [Tag 07A7]. Restriction to the levels commutes with these functors (Lemma 4.2 (1) of the lesson on big fppf sites), and at the level \(n\) this map is the base change map of Lemma 2.3 there for the flat morphism \(a_n\). So it is an isomorphism when \(F\) has adequate cohomology sheaves.

*Full faithfulness.* Let \(E,F\in D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\) and \(n\) with \(H^iE=H^iF=0\) for \(i<n\). There are bijections
\[
\begin{aligned}&\operatorname{Hom}(E,F)\\ &\quad \cong\operatorname{Hom}\bigl(L\varepsilon^*E,t_{[n}L\varepsilon^*F\bigr)\\ &\quad \cong\operatorname{Hom}\bigl(t_{[n}L\varepsilon^*E,t_{[n}L\varepsilon^*F\bigr)\\ &\quad \cong\operatorname{Hom}\bigl(a^*t_{[n}L\varepsilon^*E,a^*t_{[n}L\varepsilon^*F\bigr)\\ &\quad \cong\operatorname{Hom}\bigl(t_{[n}L\varepsilon^*a^*E,t_{[n}L\varepsilon^*a^*F\bigr)\\ &\quad \cong\operatorname{Hom}\bigl(L\varepsilon^*a^*E,t_{[n}L\varepsilon^*a^*F\bigr)\\ &\quad \cong\operatorname{Hom}(a^*E,a^*F).\end{aligned}
\]
The first is Corollary 2.2 (1) of the lesson on big fppf sites; the second and fifth hold because maps from an object to an object of \(D^{\geq n}\) factor uniquely through its truncation \(t_{[n}\) [Tag 06XS]; the third is Theorem 2.4, the objects being bounded; the fourth uses the exactness of \(a^*\) on big sites and \(L\varepsilon^*a^*\cong a^*L\varepsilon^*\); the last is Lemma 4.2 (2) of the lesson on big fppf sites for the diagram \(N(G,X)\), since \(H^i(a^*F)=0\) for \(i<n\). All maps are natural, and a map \(u\colon E\to F\) is sent through the first five to the image of \(a^*u\) under the last, because each step applies a functor to \(u\). So \(u\mapsto a^*u\) is bijective.

*Essential image.* Let \(K\in D^b(N(G,X)_{\mathrm{Zar}})\) be quasi-cartesian with termwise quasi-coherent cohomology, and \(H^iK=0\) for \(i<n\). By Lemma 4.2 (3) and Proposition 2.1 of the lesson on big fppf sites, applied levelwise, the cohomology modules of \(L\varepsilon^*K\) are cartesian and have adequate levels. So \(t_{[n}L\varepsilon^*K\) is bounded with cartesian cohomology, and Theorem 2.4 gives \(F\in D^b(T/Y)\) with \(a^*F\cong t_{[n}L\varepsilon^*K\). The cohomology sheaves of \(F\) are adequate: their restrictions to \(X\) are the levels \(0\) of the \(H^i(t_{[n}L\varepsilon^*K)\), \(\{X\to Y\}\) is an fppf covering, and adequacy is fppf local [Tag 06VK]. So \(E=R\varepsilon_*F\) lies in \(D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\) (Proposition 1.2 (1) of the lesson on big fppf sites), and
\[
\begin{aligned}a^*E&=a^*R\varepsilon_*F\cong R\varepsilon_*a^*F\\&\cong R\varepsilon_*t_{[n}L\varepsilon^*K\cong K\end{aligned}
\]
by the base change isomorphism and Lemma 4.2 (2) of the lesson on big fppf sites. \(\square\)

**Corollary 2.6.** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor, \(\ell\in D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\) and \(L=a^*\ell\), with the level \(L_0=f^*\ell\).

1. The adjunction map \(\ell\to Ra_*L\) is an isomorphism.
2. If \(s\colon Y\to X\) is a section of \(f\), then \(\ell=L(fs)^*\ell\cong Ls^*L_0\), naturally in \(\ell\).
3. \(L\varepsilon^*L\cong a^*L\varepsilon^*\ell=\operatorname{ner}\bigl(f^{G*}L\varepsilon^*\ell\bigr)\).
4. If \(H^i\ell=0\) for \(i<n\), then \(L^G=f^{G*}t_{[n}L\varepsilon^*\ell\in D^b(B[G,X]^{\mathrm o})\) satisfies \(\operatorname{ner}(L^G)\cong t_{[n}L\varepsilon^*L\) and \(R\varepsilon_*f^G_*L^G\cong\ell\).

**Proof.** (1) Let \(V\subseteq Y\) be an affine open. Then \(X_V\to V\) is a torsor whose nerve is the open simplicial subscheme \(a^{-1}(V)\) of \(N(G,X)\). By Theorem 2.5 over \(V\), the adjunction [Tag 07A6] and [Tag 0D6G],
\[
\begin{aligned}H^i(V,\ell)&=\operatorname{Hom}(\mathcal O_V,\ell|_V[i])\\&\cong\operatorname{Hom}(a^*\mathcal O_V,L|_{a^{-1}V}[i])\\&=H^i(V,Ra_*L),\end{aligned}
\]
and the composite is induced by the adjunction map. So its cone \(C\in D^+(Y_{\mathrm{Zar}})\) has \(H^i(V,C)=0\) for all \(i\) and all affine \(V\) [Tag 0149]. If \(C\neq0\) and \(H^m(C)\) is its first nonzero cohomology sheaf, then \(H^m(V,C)=\Gamma(V,H^m(C))\) [Tag 06XS] is nonzero for some affine \(V\), since affine opens form a basis. So \(C=0\).

(2) \(fs=\mathrm{id}_Y\), and \(Ls^*\circ Lf^*=L(fs)^*\) [Tag 0D6D], with \(Lf^*=f^*\) as \(f\) is flat.

(3) By Lemma 4.2 (1) of the lesson on big fppf sites and \(L\varepsilon^*a^*\cong a^*L\varepsilon^*\) (proof of Theorem 2.5), and Construction 2.1 (a).

(4) \(\operatorname{ner}(L^G)=a^*t_{[n}L\varepsilon^*\ell=t_{[n}a^*L\varepsilon^*\ell\), which is \(t_{[n}L\varepsilon^*L\) by (3). By Proposition 2.2 (3), \(f^G_*L^G\cong t_{[n}L\varepsilon^*\ell\), and \(R\varepsilon_*t_{[n}L\varepsilon^*\ell\cong\ell\) by Proposition 2.1 of the lesson on big fppf sites. \(\square\)

Applied to the truncations of an object one at a time, these statements hold for the projective systems \((t_{[n})_n\) of the lesson on equivariant cotangent complexes.

## 3. The co-Lie complex and the Atiyah class

In this section \(f\colon X\to Y\) is a \(G_Y\)-torsor and \(Y\to S\) a morphism of schemes. Put \(\varphi=N(G,f)\colon N(G,X)\to N(G,Y)\), and let \(\pi\colon N(G,Y)=N(G)\times_SY\to N(G)\) and \(q\colon N(G,Y)\to Y\) be the projections, so that \(a=q\varphi\).

**Lemma 3.1.**

1. For every \(\alpha\colon[m]\to[n]\), the squares formed by \(N(G,X)(\alpha)\), \(N(G,Y)(\alpha)\), \(\varphi_n\), \(\varphi_m\), and by \(N(G,Y)(\alpha)\), \(N(G)(\alpha)\), \(\pi_n\), \(\pi_m\), are cartesian. Every \(\varphi_n\) is flat, and \(N_m(G,Y)\) and \(N_n(G)\) are Tor independent over \(N_m(G)\).
2. \(L_{N(G,X)/N(G,Y)}\) is quasi-cartesian, with the levels \(Lv_0^*L_{X/Y}\), which have tor amplitude in \([-1,0]\). In particular it lies in \(D^{[-1,0]}\).
3. The functoriality map \(q^*L_{Y/S}\to L_{N(G,Y)/N(G)}\), of the commutative square formed by \(q\), \(\pi\) and the structure morphisms to \(S\), is an isomorphism. Hence \(a^*L_{Y/S}=\) \(L\varphi^*q^*L_{Y/S}\cong\) \(L\varphi^*L_{N(G,Y)/N(G)}\).
4. \(L_{N(G,X)/N(G)}\) is quasi-cartesian, and the three complexes of the transitivity triangle of \(N(G,X)\to N(G,Y)\to N(G)\) have termwise quasi-coherent cohomology.
5. An object \(K\) of \(D^-(N(G,X)_{\mathrm{Zar}})\) whose structure maps along the faces are isomorphisms is quasi-cartesian, and then every truncation \(t_{[r}K\) is quasi-cartesian.

**Proof.** (1) The second square is cartesian because \(N(G,Y)(\alpha)=N(G)(\alpha)\times\mathrm{id}_Y\). For the first, the morphism from \(N_n(G,X)\) to \(N_m(G,X)\times_{N_m(G,Y)}N_n(G,Y)\) sends \((g;x)\) to \(\bigl((N(G)(\alpha)(g);\,g_{\alpha(0)}\cdots g_1x),(g;f(x))\bigr)\), and a point \(\bigl((h;x'),(g;y)\bigr)\) of the target, with \(h=N(G)(\alpha)(g)\) and \(f(x')=y\), comes from the unique point \(\bigl(g;(g_{\alpha(0)}\cdots g_1)^{-1}x'\bigr)\), which lies over \((g;y)\) because \(f\) is invariant. \(\varphi_n=\mathrm{id}\times f\colon G^n\times_SX\to G^n\times_SY\) is flat. For the Tor independence apply Lemma 2.2 of the lesson on equivariant cotangent complexes to \(P=Y\to Q=S\), \(R=N_m(G)\to S\) and \(R'=N_n(G)\to R\): \(P\) and \(R\), and \(P\) and \(R'\), are Tor independent over \(S\) because \(N_m(G)\) and \(N_n(G)\) are flat over \(S\), and \(P\times_QR=N_m(G,Y)\).

(2) By (1) and Proposition 1.4 of the lesson on deformations of diagrams, \(L_{N(G,X)/N(G,Y)}\) is quasi-cartesian; its levels are \(Lv_0^*L_{X/Y}\) by Proposition 2.3 (1) of the lesson on equivariant cotangent complexes, \(f\) being flat. By Proposition 1.3 (1), \(f\) is syntomic, so \(L_{X/Y}\) is locally a complex of finite free modules in degrees \(-1\) and \(0\), as in the proof of Theorem 3.1 of [*Flat group schemes are local complete intersections*](flat-group-schemes-are-local-complete-intersections.md); pullbacks keep this property [Tag 08H5].

(3) The functoriality map is that of Theorem 2.2 of *The cotangent complex* for the map of ring pairs on \(\operatorname{Top}(N(G,Y)_{\mathrm{Zar}})\) given by \(q\) and \(\pi\); at the level \(n\) it is the functoriality map of the square formed by \(q_n\colon N_n(G)\times_SY\to Y\) and \(\pi_n\), which is cartesian with \(N_n(G)\) flat over \(S\). So its levels are isomorphisms by Proposition 1.4 of the lesson on deformations of diagrams, and a map whose levels are isomorphisms is an isomorphism, cohomology being computed levelwise. Finally \(a^*=L\varphi^*q^*\) [Tag 0D6D], all three being flat pullbacks.

(4) The transitivity triangle of Proposition 1.3 of the lesson on deformations of diagrams is natural, so the structure maps along \(\alpha\) of its three vertices form a morphism from \(LN(G,X)(\alpha)^*\) of the triangle at the level \(m\) to the triangle at the level \(n\). By (2) and (3) the maps on the first and the third vertices are isomorphisms, hence so is the middle one [Tag 014A]. The cohomology is termwise quasi-coherent by Proposition 1.2 (2) of the lesson on deformations of diagrams, and for \(a^*L_{Y/S}\) because \(a^*\) is exact.

(5) The faces are flat (Proposition 1.3 (2)). Represent \(K\) by a bounded above complex of modules with flat levels (proof of Lemma 4.2 (1) of the lesson on big fppf sites); its structure maps satisfy \(K_{\alpha\gamma}=K_\alpha\circ N(\alpha)^*(K_\gamma)\), writing \(N=N(G,X)\). For a degeneracy \(\sigma\colon[n+1]\to[n]\) choose a face \(\delta\colon[n]\to[n+1]\) with \(\sigma\delta=\mathrm{id}\); then \(K_\sigma\circ N(\sigma)^*(K_\delta)=\mathrm{id}\), so \(K_\sigma\) is invertible when \(K_\delta\) is. Every \(\alpha\) is a composite of faces and degeneracies, so all \(K_\alpha\) are invertible. Pullback along a face is exact and commutes with \(t_{[r}\), so \(t_{[r}K\) again has invertible structure maps along the faces. \(\square\)

**Lemma 3.2 (truncating a triangle).** Let \(A\xrightarrow{u}B\xrightarrow{v}C\xrightarrow{w}A[1]\) be a distinguished triangle in the derived category of an abelian category, and \(n\) an integer with \(C\in D^{\geq n}\). Then \(v\) factors uniquely as \(B\to t_{[n}B\xrightarrow{v'}C\), and
\[
t_{[n}A\xrightarrow{t_{[n}u}t_{[n}B\xrightarrow{v'}C\xrightarrow{w'}t_{[n}A[1]
\]
is distinguished, where \(w'\) is \(w\) followed by \(A[1]\to t_{[n}A[1]\).

**Proof.** In the triangle \(\tau_{\leq n-1}B\to B\to t_{[n}B\), the groups \(\operatorname{Hom}(\tau_{\leq n-1}B[i],C)\), \(i=0,1\), vanish [Tag 06XS], which gives the unique factorization. Choose a distinguished triangle \(t_{[n}A\to t_{[n}B\xrightarrow{v''}C''\xrightarrow{w''}t_{[n}A[1]\) on \(t_{[n}u\), and a morphism of triangles \((\mathrm{tr}_A,\mathrm{tr}_B,\gamma)\) to it from the given one, the truncation maps commuting with \(u\). In the long exact cohomology sequences, \(H^i(\mathrm{tr}_A)\) and \(H^i(\mathrm{tr}_B)\) are isomorphisms for \(i\geq n\), so \(H^i(\gamma)\) is an isomorphism for \(i\geq n\) by the five lemma. For \(i\leq n-2\), \(H^i(C'')=0\), and \(H^{n-1}(C'')\) is the kernel of \(H^n(A)\to H^n(B)\), the image of \(H^{n-1}(C)=0\). So \(\gamma\) is an isomorphism. Then \(\gamma^{-1}v''\) factors \(v\), hence equals \(v'\), and \(w''\gamma=\mathrm{tr}_A[1]\circ w=w'\). So \((\mathrm{id},\mathrm{id},\gamma)\) is an isomorphism from the stated triangle to a distinguished one. \(\square\)

**Theorem 3.3 (the co-Lie complex and the Atiyah triangle).** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor and \(Y\to S\) a morphism.

1. There is an object \(\ell_{X/Y}\) of \(D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\) with an isomorphism \(a^*\ell_{X/Y}\cong L_{N(G,X)/N(G,Y)}\), unique up to unique isomorphism: the *co-Lie complex* of \(X\) over \(Y\). It is perfect with tor amplitude in \([-1,0]\), \(\ell_{X/Y}\cong Ra_*L_{N(G,X)/N(G,Y)}\), \(f^*\ell_{X/Y}\cong L_{X/Y}\), and \(\ell_{X/Y}\cong Ls^*L_{X/Y}\) for every section \(s\) of \(f\).
2. For every integer \(n\) there is an object \(\ell_n(X/S)\) of \(D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\) with an isomorphism \(a^*\ell_n(X/S)\cong t_{[n}L_{N(G,X)/N(G)}\), and maps \(\ell_n(X/S)\to\ell_{n+1}(X/S)\) whose images under \(a^*\) are the truncation maps, all unique up to unique isomorphism. Moreover \(\ell_n(X/S)\cong Ra_*t_{[n}L_{N(G,X)/N(G)}\), \(f^*\ell_n(X/S)\cong t_{[n}L_{X/S}\), \(\ell_n(X/S)\cong Ls^*t_{[n}L_{X/S}\) for every section \(s\) of \(f\), and \(H^i(\ell_n(X/S))\) is quasi-coherent and independent of \(n\leq i\). The projective system \(\ell_{X/S}=(\ell_n(X/S))_n\) is the co-Lie complex of \(X\) over \(S\).
3. For every \(n\leq-1\) there are unique maps forming a distinguished triangle
\[
\begin{aligned}&\quad t_{[n}L_{Y/S}\\ &\quad \xrightarrow{\ \beta_n\ }\ell_n(X/S)\\ &\quad \xrightarrow{\ \gamma_n\ }\ell_{X/Y}\\ &\quad \quad \xrightarrow{\ \mathrm{at}_n\ }t_{[n}L_{Y/S}[1]\end{aligned} \tag{3.1}
\]
whose image under \(a^*\) is the triangle that Lemma 3.2 makes from the transitivity triangle of \(N(G,X)\to N(G,Y)\to N(G)\), through the isomorphisms of (1), (2) and Lemma 3.1 (3). These triangles are compatible with the transition maps. The family \(\mathrm{at}(X/Y/S)=(\mathrm{at}_n)_{n\leq-1}\) is the *Atiyah class* of the torsor, an element of
\[
\begin{aligned}&\operatorname{Ext}^1\bigl(\ell_{X/Y},t_{[}L_{Y/S}\bigr)\\&\quad=\varprojlim_n\operatorname{Hom}\bigl(\ell_{X/Y},t_{[n}L_{Y/S}[1]\bigr).\end{aligned}
\]
4. \(f^*(\mathrm{at}_n)\) is the Kodaira–Spencer class \(K(X/Y/S)\) followed by the truncation \(f^*L_{Y/S}[1]\to t_{[n}f^*L_{Y/S}[1]\).

**Proof.** (1) By Lemma 3.1 (2) and (4), \(L_{N(G,X)/N(G,Y)}\) is a bounded quasi-cartesian object with termwise quasi-coherent cohomology, so Theorem 2.5 gives \(\ell_{X/Y}\), unique up to unique isomorphism by full faithfulness. Its level \(0\) gives \(f^*\ell_{X/Y}\cong L_{X/Y}\) (Proposition 1.2 (1) of the lesson on deformations of diagrams). As \(f\) is flat and surjective, and \(f^*\ell_{X/Y}\) is perfect with tor amplitude in \([-1,0]\) (Lemma 3.1 (2)), so is \(\ell_{X/Y}\) [Tags 09UD, 09UG]. The last two assertions are Corollary 2.6 (1), (2).

(2) The object \(t_{[n}L_{N(G,X)/N(G)}\) is bounded, since the cotangent complex lies in \(D^{\leq0}\); it is quasi-cartesian by Lemma 3.1 (4), (5), with termwise quasi-coherent cohomology. Theorem 2.5 gives \(\ell_n(X/S)\) and the maps, and Corollary 2.6 the other formulas; the level \(0\) of \(t_{[n}L_{N(G,X)/N(G)}\) is \(t_{[n}L_{X/S}\). They are quasi-coherent, \(\ell_n(X/S)\) lying in \(D^b_{\mathrm{qc}}\). For \(n\leq n'\leq i\), the exact functor \(a^*\) carries \(H^i\) of the transition map \(\ell_n(X/S)\to\ell_{n'}(X/S)\) to \(H^i\) of \(t_{[n}L\to t_{[n'}L\), an isomorphism; a map of quasi-coherent modules on \(Y\) whose pullback by the faithfully flat \(f\) is an isomorphism is one, so \(H^i(\ell_n(X/S))\) does not depend on \(n\leq i\).

(3) By Lemma 3.1 (2), the third vertex \(L_{N(G,X)/N(G,Y)}\) of the transitivity triangle lies in \(D^{\geq-1}\subseteq D^{\geq n}\), so Lemma 3.2 gives a distinguished triangle on \(N(G,X)\) with vertices \(t_{[n}L\varphi^*L_{N(G,Y)/N(G)}\cong a^*t_{[n}L_{Y/S}\) (Lemma 3.1 (3) and exactness of \(a^*\)), \(a^*\ell_n(X/S)\) and \(a^*\ell_{X/Y}\). By Theorem 2.5 its three maps are \(a^*\) of unique maps \(\beta_n,\gamma_n,\mathrm{at}_n\). To see that (3.1) is distinguished, complete \(\beta_n\) to a distinguished triangle with third vertex \(Q\in D^b_{\mathrm{qc}}(Y_{\mathrm{Zar}})\). The exact functor \(a^*\) carries it to a distinguished triangle, so there is an isomorphism \(a^*Q\cong a^*\ell_{X/Y}\) compatible with the maps [Tag 014A]; by full faithfulness it is \(a^*\) of an isomorphism \(Q\cong\ell_{X/Y}\), compatible with the maps because \(a^*\) is faithful. So (3.1) is isomorphic to a distinguished triangle. The truncation maps commute with the maps of the truncated triangles on \(N(G,X)\), and by faithfulness the descended maps commute as well.

(4) The level \(0\) of the transitivity triangle of the nerves is that of \(X\to Y\to S\) (Proposition 1.3 of the lesson on deformations of diagrams), and \(f^*=a_0^*\). \(\square\)

**Proposition 3.4 (base change).** Let \(g\colon Y'\to Y\) be a morphism of \(S\)-schemes, \(X'=X_{Y'}\) and \(g_N\colon N(G,X')\to N(G,X)\) the induced morphism. There is a unique isomorphism \(Lg^*\ell_{X/Y}\cong\ell_{X'/Y'}\) whose image under \(a'^*\) is, through \(a'^*Lg^*=Lg_N^*a^*\) [Tag 0D6D] and the isomorphisms of Theorem 3.3 (1), the functoriality map \(Lg_N^*L_{N(G,X)/N(G,Y)}\to L_{N(G,X')/N(G,Y')}\).

**Proof.** At the level \(n\) the square formed by \(N_n(G,X')\to N_n(G,X)\), \(N_n(G,Y')\to N_n(G,Y)\) and the \(\varphi\)'s is cartesian, and \(\varphi_n\) is flat, so the functoriality map is an isomorphism at every level (Proposition 1.4 of the lesson on deformations of diagrams), hence an isomorphism. As \(\ell_{X/Y}\) is perfect, \(Lg^*\ell_{X/Y}\) lies in \(D^b_{\mathrm{qc}}\), and Theorem 2.5 over \(Y'\) gives the unique isomorphism. \(\square\)

**Proposition 3.5 (the equivariant cotangent complexes of a torsor).** Let \(n\leq-1\).

1. There are isomorphisms \(t_{[n}L^G_{X/Y}\cong f^{G*}t_{[n}L\varepsilon^*\ell_{X/Y}\) and \(t_{[n}L^G_{X/S}\cong f^{G*}t_{[n}L\varepsilon^*\ell_n(X/S)\) in \(D^b(B[G,X]^{\mathrm o})\), whose nerves are the isomorphisms (2.1) of the lesson on equivariant cotangent complexes composed with those of Theorem 3.3 and Corollary 2.6 (3). Moreover \(\ell_{X/Y}\cong R\varepsilon_*f^G_*t_{[n}L^G_{X/Y}\) and \(\ell_n(X/S)\cong R\varepsilon_*f^G_*t_{[n}L^G_{X/S}\).
2. Under these isomorphisms, the identification \(t_{[n}L^G_{Y/S}\cong t_{[n}p^*L\varepsilon^*L_{Y/S}\) of Proposition 2.5 (4) of that lesson, and \(Lf_B^*p^*=f^{G*}\), the equivariant Kodaira–Spencer map \(K_{G,n}\) of \(X\to Y\to S\) (Proposition 3.3 (2) there) is \(t_{[n}f^{G*}L\varepsilon^*(\mathrm{at}_n)\).

**Proof.** (1) Both sides have isomorphic nerves, by (2.1) there, Theorem 3.3, Corollary 2.6 (3) and, for \(X/S\), \(t_{[n}L\varepsilon^*t_{[n}L\cong t_{[n}L\varepsilon^*L\) ((0.2) there); \(\operatorname{ner}\) is fully faithful on \(D^b\) (Proposition 1.5 (3) there). The second formula is Corollary 2.6 (4), as \(H^i\ell_{X/Y}=0\) for \(i<-1\) and \(H^i\ell_n(X/S)=0\) for \(i<n\). (2) For a module \(E\) of \(T/Y\), \(f_B^*p^*E\) is \(f^*E\) with the structure pulled back from the identity, which is \(f^{G*}E\); since \(p^*\) and \(f^{G*}\) are exact, \(Lf_B^*p^*=f^{G*}\). Both maps have as nerve \(t_{[n}L\varepsilon^*\) of the third map of the transitivity triangle of \(N(G,X)\to N(G,Y)\to N(G)\), up to the isomorphisms (0.2) of the lesson on equivariant cotangent complexes: \(K_{G,n}\) by definition, and \(t_{[n}f^{G*}L\varepsilon^*(\mathrm{at}_n)\) by Construction 2.1 (a) and Theorem 3.3 (3). As \(\operatorname{ner}\) is faithful, they agree. \(\square\)

## 4. Smooth group schemes

Suppose that \(G\) is smooth over \(S\). Its co-Lie module is \(\omega_G=e^*\Omega_{G/S}\), a finite locally free \(\mathcal O_S\)-module [Tag 02G1]. For a scheme \(V\) over \(S\), \(e_V^*\Omega_{G_V/V}=\omega_G\otimes_{\mathcal O_S}\mathcal O_V\) [Tag 01V0]. For a morphism \(\rho\colon G_V\to G_V\) of \(V\)-schemes, \(d\rho\colon\rho^*\Omega_{G_V/V}\to\Omega_{G_V/V}\) is the map on differentials, and \(d(\rho\circ\rho')=d\rho'\circ\rho'^*d\rho\). If \(\rho\) fixes \(e_V\), put
\[
c(\rho)=e_V^*(d\rho)\colon\omega_G\otimes\mathcal O_V\longrightarrow\omega_G\otimes\mathcal O_V,
\]
using \(e_V^*\rho^*=(\rho e_V)^*=e_V^*\). Then \(c(\rho\rho')=c(\rho')c(\rho)\). For \(g\in G(V)\), the inner automorphism \(\operatorname{int}(g^{-1})\colon h\mapsto g^{-1}hg\) fixes \(e_V\), and \(g\mapsto c(\operatorname{int}(g^{-1}))\) is an action of the group \(G(V)\) on \(\omega_G\otimes\mathcal O_V\), the *coadjoint action*, since \(\operatorname{int}((gh)^{-1})=\operatorname{int}(h^{-1})\circ\operatorname{int}(g^{-1})\).

**Proposition 4.1 (the co-Lie complex of a smooth group).** Let \(G\) be smooth over \(S\) and \(f\colon X\to Y\) a \(G_Y\)-torsor.

1. \(f\) is smooth, \(L_{X/Y}\cong\Omega_{X/Y}\) in degree \(0\), and \(\ell_{X/Y}\) is a finite locally free \(\mathcal O_Y\)-module with \(f^*\ell_{X/Y}\cong\Omega_{X/Y}\).
2. For an open \(V\subseteq Y\) and a section \(s\) of \(f\) over \(V\), the composite
\[
\begin{aligned}\tau_s\colon\ell_{X/Y}|_V&\cong s^*\Omega_{X/Y}=e_V^*\psi_s^*\Omega_{X_V/V}\\&\xrightarrow{\ e_V^*(d\psi_s)\ }\omega_G\otimes\mathcal O_V\end{aligned}
\]
is an isomorphism, where the first map is that of Theorem 3.3 (1) over \(V\) and \(\psi_s\colon G_V\to X_V\), \(h\mapsto hs\), is the isomorphism of Lemma 1.2.
3. For \(g\in G(V)\), \(\tau_{gs}=c(\operatorname{int}(g^{-1}))\circ\tau_s\).

So \(\ell_{X/Y}\) is \(\omega_G\) twisted by \(X\) through the coadjoint action: on each open where \(X\) has a section it is \(\omega_G\otimes\mathcal O_V\), and the changes of section act by \(c(\operatorname{int}(g^{-1}))\).

**Proof.** (1) Over a covering as in Definition 1.1, \(X\) becomes \(G_{Y_i}\), which is smooth, and smoothness is fpqc local on the base [Tag 02VL]. So \(L_{X/Y}\cong\Omega_{X/Y}[0]\) (Propositions 5.1 and 10.1 of *The cotangent complex*), finite locally free [Tag 02G1]. By Theorem 3.3 (1), \(f^*H^{-1}(\ell_{X/Y})=H^{-1}(L_{X/Y})=0\), so \(H^{-1}(\ell_{X/Y})=0\), \(f\) being faithfully flat. Thus \(\ell_{X/Y}\) is a module, perfect with tor amplitude in \([0,0]\), that is, finite locally free.

(2) Each map is an isomorphism, \(\psi_s\) being an isomorphism with \(\psi_se_V=s\).

(3) Let \(\theta\colon f^*\ell_{X/Y}\to\Omega_{X/Y}\) be the level \(0\) of the isomorphism of Theorem 3.3 (1), so that the first map of \(\tau_s\) is \(s^*\theta\), through \(s^*f^*=\mathrm{id}\). For \(g\in G(V)\) let \(\lambda_g\colon X_V\to X_V\), \(x\mapsto gx\), and \(j_g\colon X_V\to G\times_SX_V\), \(x\mapsto(g,x)\), so that \(\mathrm{act}\circ j_g=\lambda_g\) and \(\mathrm{pr}\circ j_g=\mathrm{id}\). The isomorphism of Theorem 3.3 (1) commutes with the structure maps along the two faces \(\mathrm{act},\mathrm{pr}\colon N_1(G,X)\to N_0(G,X)\). Those of \(a^*\ell_{X/Y}\) are the canonical identifications, and those of \(L_{N(G,X)/N(G,Y)}\) are functoriality maps (Proposition 1.2 (1) of the lesson on deformations of diagrams). Pull back along \(j_g\) and compose with the functoriality map of \(j_g\). Since functoriality maps compose (Theorem 2.2 of *The cotangent complex*), this gives
\[
\begin{aligned}&\theta =d\lambda_g\circ\lambda_g^*\theta \colon f^*\ell_{X/Y}\\&\quad =\lambda_g^*f^*\ell_{X/Y} \to\Omega_{X/Y}.\end{aligned} \tag{4.1}
\]
Let \(s'=gs=\lambda_gs\). Then \(\psi_{s'}=\psi_s\circ\rho_g\) and \(\lambda_g\circ\psi_s=\psi_s\circ L_g\), with \(\rho_g(h)=hg\) and \(L_g(h)=gh\). By (4.1), \(s'^*\theta=s^*\lambda_g^*\theta=s^*(d\lambda_g)^{-1}\circ s^*\theta\), so
\[
\begin{aligned}\tau_{s'}\circ\tau_s^{-1}&=e_V^*(d\psi_{s'})\circ s^*(d\lambda_g)^{-1}\\&\qquad\circ e_V^*(d\psi_s)^{-1}.\end{aligned}
\]
The chain rule for \(\lambda_g\psi_s=\psi_sL_g\), pulled back along \(e_V\), gives \(e_V^*(d\psi_s)\circ s^*(d\lambda_g)=e_V^*(dL_g)\circ g^*(d\psi_s)\), and for \(\psi_{s'}=\psi_s\rho_g\) it gives \(e_V^*(d\psi_{s'})=e_V^*(d\rho_g)\circ g^*(d\psi_s)\); here \(g^*=e_V^*L_g^*=e_V^*\rho_g^*\). Substituting,
\[
\tau_{s'}\circ\tau_s^{-1}=e_V^*(d\rho_g)\circ e_V^*(dL_g)^{-1}.
\]
From \(L_{g^{-1}}L_g=\mathrm{id}\), \(e_V^*(dL_g)\circ g^*(dL_{g^{-1}})=\mathrm{id}\), so \(e_V^*(dL_g)^{-1}=g^*(dL_{g^{-1}})\), and the right side is \(e_V^*\bigl(d(L_{g^{-1}}\rho_g)\bigr)=c(\operatorname{int}(g^{-1}))\). \(\square\)

**Proposition 4.2 (the Atiyah sequence).** Let \(G\) be smooth over \(S\) and \(f\colon X\to Y\) a \(G_Y\)-torsor. Put \(\omega^1_{X/S}=H^0(\ell_n(X/S))\) for any \(n\leq0\).

1. The sequence
\[
\begin{gathered}0\to\Omega_{Y/S}\\ \xrightarrow{H^0(\beta_n)}\omega^1_{X/S}\\ \xrightarrow{H^0(\gamma_n)}\ell_{X/Y}\to0\end{gathered}
\tag{4.2}
\]
is exact, and its pullback by \(f\) is the exact sequence \(0\to f^*\Omega_{Y/S}\to\Omega_{X/S}\to\Omega_{X/Y}\to0\).
2. If moreover \(Y\) is smooth over \(S\), then \(\ell_n(X/S)\cong\omega^1_{X/S}\) in degree \(0\) for every \(n\leq0\), and for \(n\leq-1\) the triangle (3.1) is the triangle of the short exact sequence (4.2) [Tag 0152]: \(\mathrm{at}_n\) is the class of the extension (4.2), the same for all \(n\).

**Proof.** (1) The long exact sequence of (3.1), with \(H^{-1}(\ell_{X/Y})=0\) (Proposition 4.1 (1)), \(H^0(t_{[n}L_{Y/S})=\Omega_{Y/S}\) and \(H^1(t_{[n}L_{Y/S})=0\), gives the exactness. Its pullback is \(H^0\) of the level \(0\) of the transitivity triangle of the nerves, that is, of the triangle of \(X\to Y\to S\), whose maps on \(H^0\) are the maps of differentials (Theorem 6.1 of *The cotangent complex*).

(2) Then \(L_{Y/S}\cong\Omega_{Y/S}[0]\), so \(t_{[n}L_{Y/S}=\Omega_{Y/S}[0]\), and by (3.1) \(\ell_n(X/S)\) has cohomology only in degree \(0\). The triangle of (4.2) has the same first two maps as (3.1), so there is an isomorphism of triangles \((\mathrm{id},\mathrm{id},\chi)\) between them [Tag 014A], with \(\chi\colon\ell_{X/Y}\to\ell_{X/Y}\) and \(\chi\circ H^0(\gamma_n)=H^0(\gamma_n)\). Maps between modules in degree \(0\) are module maps [Tag 06XS], and \(H^0(\gamma_n)\) is surjective, so \(\chi=\mathrm{id}\), and the third maps agree. \(\square\)

## 5. Exercises

**5.1.** Let \(f\colon X\to Y\) be a \(G_Y\)-torsor with a section. Show that \(\mathrm{at}(X/Y/S)=0\).

**5.2.** Let \(k\) be a field of characteristic \(p>0\), \(S=\operatorname{Spec}k\), \(\mu_p=\operatorname{Spec}k[z]/(z^p-1)\), \(A\) a smooth \(k\)-algebra, \(u\in A^\times\), \(Y=\operatorname{Spec}A\), and \(X=\operatorname{Spec}B\), \(B=A[t]/(t^p-u)\), with \(\mu_p\) acting by \(t\mapsto zt\). Show that \(X\) is a \(\mu_{p,Y}\)-torsor; that \(H^{-1}(\ell_{X/Y})\) and \(H^0(\ell_{X/Y})\) are free of rank one over \(A\), on the class \(\bar e\) of \(t^p-u\) and on the class of \(t^{p-1}dt\); and that the map \(H^{-1}(\ell_{X/Y})\to H^0(L_{Y/k})=\Omega_{A/k}\) induced by \(\mathrm{at}_n(X/Y/k)\) sends \(\bar e\) to \(-du\). Deduce that \(\mathrm{at}(X/Y/k)\neq0\) for \(A=k[u,u^{-1}]\).

**5.3.** Let \(S\) be a scheme, \(Y\) smooth over \(S\), \(Y=\bigcup U_i\) an open covering and \(g_{ij}\in\mathcal O(U_i\cap U_j)^\times\) with \(g_{ik}=g_{ij}g_{jk}\) on triple intersections. Let \(X\) be the \(\mathbf G_m\)-torsor obtained by glueing the trivial torsors \(\mathbf G_m\times U_i\), with coordinates \(t_i\), along \(t_i=g_{ij}t_j\). Show that \(\ell_{X/Y}\cong\mathcal O_Y\), with generator \(\eta\) given by \(dt/t\) in every \(\tau_{s_i}\), \(s_i\) the section \(t_i=1\); that \(\sigma_i(\eta)=dt_i/t_i\) defines a splitting of (4.2) over \(U_i\); that \(\sigma_i-\sigma_j\) is \(\eta\mapsto dg_{ij}/g_{ij}\); and deduce that (4.2) splits if and only if there are \(\omega_i\in\Omega_{Y/S}(U_i)\) with \(dg_{ij}/g_{ij}=\omega_i-\omega_j\).

## 6. Complete solutions

**5.1.** By Lemma 1.2, \(X\cong G_Y\) as torsors, and all constructions are transported by isomorphisms of torsors, so let \(X=G\times_SY\). The square formed by \(\mathrm{pr}_G\colon X\to G\), \(f\) and \(G\to S\leftarrow Y\) is cartesian with \(G\) flat over \(S\), so its functoriality map \(\mathrm{pr}_G^*L_{G/S}\to L_{X/Y}\) is an isomorphism (Proposition 1.4 of the lesson on deformations of diagrams). Functoriality maps compose (Theorem 2.2 of *The cotangent complex*), so it is the composite of \(\mathrm{pr}_G^*L_{G/S}\to L_{X/S}\) and the map \(L_{X/S}\to L_{X/Y}\) of the transitivity triangle. So this map has a right inverse \(\rho\), and \(K(X/Y/S)=\) \(K(X/Y/S)\circ(L_{X/S}\to L_{X/Y})\circ\rho=\) \(0\), consecutive maps of a distinguished triangle composing to zero. By Theorem 3.3 (4), \(f^*(\mathrm{at}_n)=0\). With a section \(s\), Corollary 2.6 (2) identifies \(\mathrm{at}_n\) with \(Ls^*f^*(\mathrm{at}_n)\), naturally, so \(\mathrm{at}_n=0\).

**5.2.** *Torsor.* \(B\) is free over \(A\) with basis \(1,t,\ldots,t^{p-1}\), and \(t\) is a unit, as \(t^p=u\). The morphism \(\mu_p\times_kX\to X\times_YX\), \((z,x)\mapsto(zx,x)\), is given by \(B\otimes_AB\to B[z]/(z^p-1)\), \(t\otimes1\mapsto zt\), \(1\otimes t\mapsto t\), with inverse \(z\mapsto(t\otimes1)(1\otimes t)^{-1}\), \(t\mapsto1\otimes t\): indeed \(\bigl((t\otimes1)(1\otimes t)^{-1}\bigr)^p=u\cdot u^{-1}=1\), and both composites are the identity on generators. \(X\to Y\) is finite, faithfully flat and of finite presentation, an fppf covering, and \(X\times_YX\to X\) has the diagonal section; so condition 2 holds with the covering \(\{X\to Y\}\).

*Co-Lie complex.* As \(t^p-u\) is a nonzerodivisor of \(A[t]\), formula (7.3) of *The cotangent complex* gives \(L_{B/A}=[B\bar e\to B\,dt]\), \(\bar e\mapsto pt^{p-1}dt=0\). So \(H^{-1}(L_{X/Y})=B\bar e\) and \(H^0(L_{X/Y})=B\,dt\). For a quasi-coherent module \(H\) on the affine \(Y\), \(\Gamma(Y,H)=\) \(\operatorname{Hom}(\mathcal O_Y,H)\cong\) \(\operatorname{Hom}(a^*\mathcal O_Y,a^*H)\) (Theorem 2.5), the sections over \(N(G,X)\) of \(a^*H\): the sections \(\sigma\) of \(f^*H\) over \(X\) whose pullbacks along \(\mathrm{act}\) and \(\mathrm{pr}\) agree through the structure map. For \(H=H^i(\ell_{X/Y})\), \(f^*H=H^i(L_{X/Y})\), and the structure maps are induced by the functoriality maps along \(\mathrm{act}\): on conormal classes and differentials (Theorem 6.1 of *The cotangent complex*), \(\mathrm{act}^*\) sends \(\bar e\) to the class of \((zt)^p-u=t^p-u\), and \(dt\) to \(z\,dt\). Grade \(B\bar e\) and \(B\,dt\) by \(\deg t=1\), \(\deg\bar e=0\), \(\deg dt=1\), modulo \(p\); an element of degree \(j\) is sent to \(z^j\) times itself, and since \(1,z,\ldots,z^{p-1}\) are linearly independent, the invariant elements are those of degree \(0\). So \(\Gamma(Y,H^{-1})=A\bar e\) and \(\Gamma(Y,H^0)=A\,t^{p-1}dt\), both free of rank one.

*Atiyah class.* By Theorem 3.3 (4), \(f^*H^{-1}(\mathrm{at}_n)=H^{-1}(K(X/Y/k))\), truncation not changing \(H^0\) of \(L_{Y/k}\) for \(n\leq-1\). Let \(P=\operatorname{Spec}A[t]\), smooth over \(k\), with the closed immersion \(X\to P\). The transitivity triangle of \(X\to P\to Y\) gives \(H^{-1}(L_{X/Y})\cong\) \(H^{-1}(L_{X/P})=\) \((t^p-u)/(t^p-u)^2\), because the map to \(\Omega_{P/Y}|_X\) is \(d\) (Proposition 1.2 (2) of the lesson on equivariant extensions and deformations) and \(d(t^p-u)=pt^{p-1}dt=0\) relative to \(A\). The map of triples \((k\to A\to B)\to(k\to A[t]\to B)\) and the naturality of transitivity triangles (Proposition 1.3 of the lesson on deformations of diagrams) give \(H^{-1}(K(X/P/k))(\bar e)=\) \(\iota\bigl(H^{-1}(K(X/Y/k))(\bar e)\bigr)\), with \(\iota\colon\Omega_{A/k}\otimes B\to\Omega_{A[t]/k}\otimes B\) the injective natural map. By that Proposition 1.2 (2), \(H^{-1}(K(X/P/k))(\bar e)=\) \(d(t^p-u)=\) \(-du\). So \(H^{-1}(K(X/Y/k))(\bar e)=-du\), and, \(f^*\) being faithful on quasi-coherent modules, \(H^{-1}(\mathrm{at}_n)(\bar e)=-du\). For \(A=k[u,u^{-1}]\), \(du\neq0\) in \(\Omega_{A/k}=A\,du\), so \(\mathrm{at}_n\neq0\).

**5.3.** \(\mathbf G_m\) is commutative, so \(\operatorname{int}(g^{-1})=\mathrm{id}\) and \(c(\operatorname{int}(g^{-1}))=\mathrm{id}\); by Proposition 4.1 (3) the isomorphisms \(\tau_{s_i}\) glue to \(\ell_{X/Y}\cong\omega_{\mathbf G_m}\otimes\mathcal O_Y=\mathcal O_Y\,dt\), with \(\eta\) corresponding to \(dt\), the value of \(dt/t\) at \(t=1\). As in Exercise 5.2, sections of \(\omega^1_{X/S}\) over \(U_i\) are the \(\mathbf G_m\)-invariant sections of \(\Omega_{X/S}\) over \(X_{U_i}\). The form \(dt_i/t_i\) is invariant: its pullback along the action is \(d(zt_i)/(zt_i)=dt_i/t_i\) in \(\Omega_{\mathbf G_m\times X/\mathbf G_m}\), where \(dz=0\), the structure maps of \(L_{N(G,X)/N(G)}\) being taken relative to \(N(G)\). Its image in \(\ell_{X/Y}|_{U_i}\) is \(\eta\): under \(\psi_{s_i}\) the coordinate \(t_i\) becomes the coordinate of \(\mathbf G_m\), and \(e^*(dt/t)=dt\). So \(\sigma_i\) is a splitting of (4.2) over \(U_i\). On \(U_i\cap U_j\), \(t_i=g_{ij}t_j\) gives \(dt_i/t_i=dt_j/t_j+dg_{ij}/g_{ij}\), so \(\sigma_i-\sigma_j\) sends \(\eta\) to \(dg_{ij}/g_{ij}\in\Omega_{Y/S}(U_i\cap U_j)\). If \(\sigma\) is a global splitting, \(\omega_i=(\sigma_i-\sigma)(\eta)\) satisfy \(\omega_i-\omega_j=dg_{ij}/g_{ij}\). Conversely, given such \(\omega_i\), the splittings \(\eta\mapsto\sigma_i(\eta)-\omega_i\) agree on the overlaps and glue. By Proposition 4.2 (2), \(\mathrm{at}(X/Y/S)\) is the third map of the triangle of (4.2), which vanishes if and only if (4.2) splits [Tag 05QT]; so \(\mathrm{at}(X/Y/S)=0\) exactly in this case.

## Sources

Torsors under flat group schemes, descent along them for the equivariant cotangent complex, the co-Lie complex, the Atiyah class of a torsor and its relation with the equivariant Kodaira–Spencer class are due to Illusie, in his work on the cotangent complex. The exact sequence (4.2) is the algebraic form of the sequence introduced by Atiyah for principal bundles.
