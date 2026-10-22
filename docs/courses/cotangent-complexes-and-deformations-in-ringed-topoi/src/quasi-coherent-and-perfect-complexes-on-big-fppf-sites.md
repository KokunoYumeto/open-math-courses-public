# Quasi-coherent and perfect complexes on big fppf sites

*Written by Claude Opus 5.5 (Anthropic) on 21 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A scheme \(S\) has two natural topoi: the topos of sheaves on its Zariski site, where quasi-coherent sheaves and their cohomology live, and the big fppf topos of all schemes over \(S\), where group schemes act and torsors are locally trivial. Deformation problems for schemes with a group action are posed on the big topos and solved with cotangent complexes, which are made on the Zariski side. This lesson compares the two sides. Quasi-coherent sheaves are the same on both, with the same cohomology. A bounded complex with quasi-coherent cohomology on \(S\) has the same derived Hom groups after pullback to the big site, once the pullback is truncated from below. Complexes of perfect amplitude in \([a,b]\) on the big site all come from \(S\).

The pullback of a complex of flat quasi-coherent sheaves to the big site need not have quasi-coherent cohomology: for \(\mathbb Z\xrightarrow{p}\mathbb Z\) on \(\operatorname{Spec}\mathbb Z\) the cohomology in degree \(-1\) is the sheaf of \(p\)-torsion functions, which vanishes on flat \(\mathbb Z\)-schemes and not on \(\mathbb F_p\)-schemes. Its cohomology is adequate in the sense of the Stacks project, and adequate modules have all the properties of quasi-coherent ones that the comparison needs: they have no higher direct images to \(S\), and their direct images commute with flat base change. The last section extends everything to diagrams of schemes.

**Prerequisites.** [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) (Definition 1.1, Examples 1.2, Theorem 4.2, Proposition 5.1); [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md) (Definition 1.1, Proposition 2.1, Proposition 4.2); [*Cohomology of total topoi*](cohomology-of-total-topoi.md) (Proposition 4.1, Remark 4.2). From the AI-integrated Stacks project: big fppf sites and their localizations [[Stacks, Tag 021R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-definition-big-fppf-site), [Tag 021S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-definition-big-small-fppf), [Tag 021W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topologies.html#topologies-lemma-morphism-big-fppf)]; the structure sheaf of the big site and the comparison morphism with the Zariski site [[Tag 03DU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-definition-structure-sheaf), [Tag 070R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-remark-change-topologies-ringed), [Tag 070S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-compare-sites), [Tag 03FH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-remark-change-topologies-ringed-sites)]; quasi-coherent modules on the big site [[Tag 03DT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-sheaf-condition-holds), [Tag 03DX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-equivalence-quasi-coherent), [Tag 03DW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-proposition-same-cohomology-quasi-coherent)]; adequate modules [[Tag 06VG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/adequate.html#adequate-definition-adequate), [Tag 06VK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/adequate.html#adequate-lemma-adequate-characterize), [Tag 06VM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/adequate.html#adequate-lemma-same-cohomology-adequate), [Tag 06VQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/adequate.html#adequate-lemma-abelian-adequate)]; higher direct images [[Tag 0D6I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-unbounded-describe-higher-direct-images)]; derived pullback and its adjunction [[Tag 06YY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-base-change), [Tag 07A6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-adjoint)]; bounded above complexes of flat modules are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)]; complexes with quasi-coherent cohomology on affine schemes [[Tag 06Z0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-affine-compare-bounded)]; vanishing of higher cohomology of quasi-coherent sheaves on affine schemes [[Tag 01XB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-quasi-coherent-affine-cohomology-zero)]; perfect complexes and tor amplitude [[Tag 08G5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-perfect), [Tag 0658](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-perfect)] and their descent along flat coverings [[Tag 09UD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-tor-amplitude-descends), [Tag 09UG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-perfect-descends-fpqc)].

## Conventions

\(S\) is a scheme, \((\mathrm{Sch}/S)_{\mathrm{fppf}}\) a big fppf site of \(S\) [Tags 021R, 021S], and \(\mathcal O\) its structure sheaf, \(U\mapsto\Gamma(U,\mathcal O_U)\) [Tag 03DU]. The fppf topology is used rather than the fpqc topology: fpqc coverings of a ring cannot be bounded by a set, so big fpqc sites need an additional choice of a universe [Stacks, Section 022A]. Let
\[
\varepsilon\colon\bigl((\mathrm{Sch}/S)_{\mathrm{fppf}},\mathcal O\bigr)\longrightarrow(S_{\mathrm{Zar}},\mathcal O_S)
\]
be the morphism of ringed sites of [Tag 070R]: \(\varepsilon_*F\) is the restriction of \(F\) to the open subschemes of \(S\), and for an \(\mathcal O_S\)-module \(M\), \(\varepsilon^*M\) is the fppf sheafification of \((f\colon T\to S)\mapsto\Gamma(T,f^*M)\) [Tag 070S]. For a morphism \(g\colon S'\to S\), the morphism \(g_{\mathrm{big}}\colon(\mathrm{Sch}/S')_{\mathrm{fppf}}\to(\mathrm{Sch}/S)_{\mathrm{fppf}}\) is the localization at \(S'\): its inverse image is the restriction to schemes over \(S'\), which is exact and preserves \(\mathcal O\) [Tag 021W], and \(g_{\mathrm{big}}^*\varepsilon^*\cong\varepsilon'^*g^*\) for the comparison morphism \(\varepsilon'\) of \(S'\) [Tag 03FH]. All rings are commutative.

\(D(S_{\mathrm{Zar}})\) is the derived category of \(\mathcal O_S\)-modules and \(D_{\mathrm{qc}}(S_{\mathrm{Zar}})\) its full subcategory of objects with quasi-coherent cohomology; \(D(S_{\mathrm{fppf}})\) is the derived category of \(\mathcal O\)-modules on the big site. For an object \(L\) of a derived category and an integer \(n\), \(t_{[n}L=\tau_{\geq n}L\) is its truncation killing the cohomology in degrees \(<n\), with the canonical map \(L\to t_{[n}L\). An object \(E\) of the derived category of modules on a ringed site has *perfect amplitude in \([a,b]\)* if every object \(U\) of the site has a covering \(\{U_k\to U\}\) such that every \(E|_{U_k}\) is represented by a complex of finite free modules concentrated in degrees \([a,b]\). These objects form a full subcategory \(\operatorname{Parf}^{[a,b]}\). On \(S_{\mathrm{Zar}}\) they are the perfect objects of tor amplitude in \([a,b]\): one direction is clear, and conversely such an object is, over an affine open \(\operatorname{Spec}A\), a complex of finite projective \(A\)-modules in degrees \([a,b]\) [Tags 06Z0, 0658], and finite projective modules are free locally on \(\operatorname{Spec}A\).

## 1. Quasi-coherent and adequate modules

**Proposition 1.1.** Let \(M\) be a quasi-coherent \(\mathcal O_S\)-module.

1. \(\varepsilon^*M\) is the sheaf \(M^a\colon(f\colon T\to S)\mapsto\Gamma(T,f^*M)\), and the unit \(M\to\varepsilon_*\varepsilon^*M\) is an isomorphism.
2. The functor \(\varepsilon^*\) is an equivalence from quasi-coherent \(\mathcal O_S\)-modules to quasi-coherent \(\mathcal O\)-modules on the big site, with quasi-inverse \(\varepsilon_*\). It is right exact on quasi-coherent modules, and it carries short exact sequences of flat quasi-coherent modules to short exact sequences.
3. \(R^q\varepsilon_*\varepsilon^*M=0\) for \(q>0\), so \(M\to R\varepsilon_*\varepsilon^*M\) is an isomorphism.

**Proof.** (1) The presheaf \(T\mapsto\Gamma(T,f^*M)\) is already an fppf sheaf [Tag 03DT], so it is \(\varepsilon^*M\) by [Tag 070S]. On an open subscheme \(U\) of \(S\) its value is \(\Gamma(U,M)\), so \(\varepsilon_*\varepsilon^*M=M\). (2) The equivalence is [Tag 03DX], and its quasi-inverse is \(\varepsilon_*\) by (1). For an affine \(T=\operatorname{Spec}B\) over \(S\), \(\Gamma(T,f^*-)\) is \(-\otimes_AB\) on the modules of an affine open \(\operatorname{Spec}A\subseteq S\) through which \(f\) factors; it is right exact, and exact on sequences \(0\to M'\to M\to M''\to0\) with \(M''\) flat. Exactness of a sequence of sheaves on the big site can be checked on affine objects, which have a covering by such \(T\). (3) By [Tag 0D6I], \(R^q\varepsilon_*\varepsilon^*M\) is the sheaf associated with \(U\mapsto\) \(H^q((\mathrm{Sch}/U)_{\mathrm{fppf}},M^a)=\) \(H^q(U,M)\) [Tag 03DW], on open subschemes \(U\) of \(S\). For affine \(U\) this vanishes when \(q>0\) [Tag 01XB], and affine opens form a basis, so the associated sheaf is zero. \(\square\)

The kernel of a map of quasi-coherent modules on the big site need not be quasi-coherent (Exercise 5.1). An \(\mathcal O\)-module \(F\) on the big site is *adequate* [Tag 06VG] if \(S\) has an affine open covering \(S=\bigcup S_k\) with maps \(G_k\to H_k\) of quasi-coherent \(\mathcal O_{S_k}\)-modules such that \(F|_{(\mathrm{Sch}/S_k)_{\mathrm{fppf}}}\) is the kernel of \(G_k^a\to H_k^a\); the same then holds over every affine scheme over \(S\), and adequacy is local for the fppf topology [Tag 06VK]. The adequate modules form an abelian subcategory closed under kernels, cokernels and extensions [Tag 06VQ].

**Proposition 1.2.** Let \(F\) be an adequate \(\mathcal O\)-module.

1. \(\varepsilon_*F\) is quasi-coherent, \(R^q\varepsilon_*F=0\) for \(q>0\), and \(\varepsilon_*\) is exact on adequate modules.
2. For a flat morphism \(g\colon S'\to S\) the base change map \(g^*\varepsilon_*F\to\varepsilon'_*g_{\mathrm{big}}^*F\) is an isomorphism.

**Proof.** (1) The first two assertions are [Tag 06VM] (1) and (3), with [Tag 0D6I] as in Proposition 1.1 (3). The second makes \(\varepsilon_*\) exact on adequate modules, by the long exact sequence. (2) The question is local on \(S\) and \(S'\), so we may assume that \(F\) is the kernel of \(G^a\to H^a\) for quasi-coherent \(G\to H\) on \(S\). Then \(\varepsilon_*F=\operatorname{Ker}(G\to H)\) by (1) of Proposition 1.1, and \(\varepsilon'_*g_{\mathrm{big}}^*F\) is the kernel of \(g^*G\to g^*H\), because \(g_{\mathrm{big}}^*\) is the restriction and \(g_{\mathrm{big}}^*G^a=(g^*G)^a\). Since \(g\) is flat, \(g^*\) commutes with the kernel. \(\square\)

## 2. Bounded complexes with quasi-coherent cohomology

**Proposition 2.1.** Let \(M\in D^b_{\mathrm{qc}}(S_{\mathrm{Zar}})\) and \(a\) an integer with \(H^iM=0\) for \(i<a\). The cohomology sheaves of \(L\varepsilon^*M\) are adequate, and for every \(n\leq a\) the map
\[
M\longrightarrow R\varepsilon_*t_{[n}L\varepsilon^*M,
\]
adjoint to \(L\varepsilon^*M\to t_{[n}L\varepsilon^*M\), is an isomorphism.

**Proof.** Both assertions are local on \(S\): adequacy is local, and \(R\varepsilon_*\) commutes with restriction to open subschemes. So let \(S=\operatorname{Spec}A\). Then \(M\) is represented by a bounded above complex \(P\) of free quasi-coherent modules [Tag 06Z0]. Such a complex is K-flat [Tag 06YQ], so \(L\varepsilon^*M=\varepsilon^*P\) [Tag 06YY], a complex of quasi-coherent modules on the big site, whose cohomology sheaves are adequate because adequate modules form an abelian subcategory containing the quasi-coherent ones. Since \(\varepsilon^*\) is right exact (Proposition 1.1 (2)), it carries \(P^{n-1}\to P^n\to P^n/\operatorname{Im}P^{n-1}\to0\) to an exact sequence, so \(t_{[n}\varepsilon^*P=\varepsilon^*t_{[n}P\) as complexes, where \(t_{[n}P\) is the complex \(P^n/\operatorname{Im}P^{n-1}\to P^{n+1}\to\cdots\). This is a bounded complex of quasi-coherent modules, and \(n\leq a\) makes \(P\to t_{[n}P\) a quasi-isomorphism. By Proposition 1.1 (3) its terms \(Q\) satisfy \(R\varepsilon_*\varepsilon^*Q=Q\), so for the bounded complex, \(R\varepsilon_*\varepsilon^*t_{[n}P=t_{[n}P\cong M\), and the map of the statement is this identification composed with \(M\cong P\to t_{[n}P\). \(\square\)

The truncation cannot be omitted in general: \(L\varepsilon^*M\) may have cohomology in degrees \(<a\) (Exercise 5.1), and it may be unbounded below.

**Corollary 2.2.**

1. For \(E\in D^-(S_{\mathrm{Zar}})\) and \(F\in D^b_{\mathrm{qc}}(S_{\mathrm{Zar}})\) with \(H^iF=0\) for \(i<n\), there is an isomorphism, natural in \(E\) and \(F\),
\[
\begin{aligned}&\operatorname{RHom}(E,F)\\&\quad \xrightarrow{\ \sim\ }\operatorname{RHom}\bigl(L\varepsilon^*E,t_{[n}L\varepsilon^*F\bigr).\end{aligned}
\]
2. For \(E\in D^-(S_{\mathrm{Zar}})\) and \(F\in D^-_{\mathrm{qc}}(S_{\mathrm{Zar}})\), the maps of (1) induce a bijection, natural in \(E\) and \(F\),
\[
\begin{aligned}&\varprojlim_n\operatorname{Hom}(E,t_{[n}F)\\&\quad \xrightarrow{\ \sim\ }\varprojlim_n\operatorname{Hom}\bigl(L\varepsilon^*E,t_{[n}L\varepsilon^*F\bigr),\end{aligned}
\]
the limits being over \(n\to-\infty\). In the language of pro-objects, with \(t_[L\) the projective system \((t_{[n}L)_n\), this is an isomorphism \(\operatorname{Hom}(E,t_[F)\) \(\cong\operatorname{Hom}(L\varepsilon^*E,t_[L\varepsilon^*F)\).

**Proof.** (1) Adjunction [Tag 07A6] gives \(\operatorname{RHom}(L\varepsilon^*E,G)\cong\operatorname{RHom}(E,R\varepsilon_*G)\) for \(G=t_{[n}L\varepsilon^*F\), and \(R\varepsilon_*G\cong F\) by Proposition 2.1. (2) For each \(n\), apply (1) to \(t_{[n}F\in D^b_{\mathrm{qc}}\). The triangle \(\tau_{<n}F\to F\to t_{[n}F\) gives the triangle \(L\varepsilon^*\tau_{<n}F\to L\varepsilon^*F\to L\varepsilon^*t_{[n}F\), and \(L\varepsilon^*\tau_{<n}F\) has no cohomology in degrees \(\geq n\): it is computed by a complex of flat modules in degrees \(<n\) [Stacks, Tags 05T7, 06YQ, 06YY], and \(\varepsilon^*\) of such a complex vanishes in degrees \(\geq n\). So \(t_{[n}L\varepsilon^*F=t_{[n}L\varepsilon^*t_{[n}F\), and the isomorphisms for the various \(n\) are compatible with the transition maps. \(\square\)

**Lemma 2.3 (flat base change).** Let \(g\colon S'\to S\) be flat, \(\varepsilon'\) the comparison morphism of \(S'\), and \(F\in D^+(S_{\mathrm{fppf}})\) with adequate cohomology sheaves. Then the base change map
\[
g^*R\varepsilon_*F\longrightarrow R\varepsilon'_*g_{\mathrm{big}}^*F
\]
is an isomorphism.

**Proof.** The inverse image \(g_{\mathrm{big}}^*\) is exact and preserves adequacy [Tag 06VK]. By Proposition 1.2 (1), applied over \(S\) and over \(S'\), both sides have the cohomology sheaves \(g^*\varepsilon_*H^iF\) and \(\varepsilon'_*g_{\mathrm{big}}^*H^iF\): for a complex with \(\varepsilon_*\)-acyclic cohomology in \(D^+\), the spectral sequence of \(R\varepsilon_*\) degenerates, and \(g^*\) is exact. The base change map is compatible with these identifications, and on each \(H^i\) it is the isomorphism of Proposition 1.2 (2). \(\square\)

## 3. Perfect complexes

**Theorem 3.1.** For every interval \([a,b]\), the functor \(L\varepsilon^*\) induces an equivalence
\[
\operatorname{Parf}^{[a,b]}(S_{\mathrm{Zar}})\xrightarrow{\ \sim\ }\operatorname{Parf}^{[a,b]}(S_{\mathrm{fppf}}),
\]
with quasi-inverse \(R\varepsilon_*\).

**Proof.** *The functor.* On an open \(U\subseteq S\) where \(E\) is a complex of finite free modules in degrees \([a,b]\), \(L\varepsilon^*E\) is the same complex of free \(\mathcal O\)-modules on \((\mathrm{Sch}/U)_{\mathrm{fppf}}\), so \(L\varepsilon^*E\) has perfect amplitude in \([a,b]\); in particular \(L\varepsilon^*E\in D^{[a,b]}\).

*Full faithfulness.* For \(E,E'\in\operatorname{Parf}^{[a,b]}(S_{\mathrm{Zar}})\), Corollary 2.2 (1) with \(n=a\) gives \(\operatorname{Hom}(E,E')\cong\) \(\operatorname{Hom}(L\varepsilon^*E,t_{[a}L\varepsilon^*E')=\) \(\operatorname{Hom}(L\varepsilon^*E,L\varepsilon^*E')\), and this bijection is induced by \(L\varepsilon^*\).

*Essential surjectivity.* Let \(F\in\operatorname{Parf}^{[a,b]}(S_{\mathrm{fppf}})\). Choose an fppf covering \(\{g_k\colon S_k\to S\}\) and complexes \(P_k\) of finite free \(\mathcal O_{S_k}\)-modules in degrees \([a,b]\) with \(g_{k,\mathrm{big}}^*F\cong\varepsilon_k^*P_k\); a complex of finite free \(\mathcal O\)-modules on the big site of \(S_k\) is \(\varepsilon_k^*\) of the complex of free \(\mathcal O_{S_k}\)-modules given by the same matrices of global functions. The cohomology sheaves of \(F\) are adequate: those of \(\varepsilon_k^*P_k\) are, and adequacy is fppf local. So Lemma 2.3 and Proposition 2.1 give
\[
g_k^*R\varepsilon_*F\cong R\varepsilon_{k*}\varepsilon_k^*P_k\cong P_k .
\]
The morphism \(\coprod_kS_k\to S\) is flat and surjective, so \(R\varepsilon_*F\) is perfect of tor amplitude in \([a,b]\) [Tags 09UD, 09UG], that is, it has perfect amplitude in \([a,b]\). The counit \(L\varepsilon^*R\varepsilon_*F\to F\) becomes, after restriction to \(S_k\) and the identifications above, the counit \(L\varepsilon_k^*R\varepsilon_{k*}\varepsilon_k^*P_k\to\varepsilon_k^*P_k\), which is an isomorphism because the unit \(P_k\to R\varepsilon_{k*}\varepsilon_k^*P_k\) is one. An isomorphism is detected on a covering, so the counit is an isomorphism, and \(F\cong L\varepsilon^*R\varepsilon_*F\). \(\square\)

**Remark 3.2 (non-flat base change).** For an arbitrary morphism \(g\colon S'\to S\) and \(F\in D^b(S_{\mathrm{fppf}})\) there is a base change map \(Lg^*R\varepsilon_*F\to R\varepsilon'_*g_{\mathrm{big}}^*F\). If \(F\) has perfect amplitude in \([a,b]\), it is an isomorphism: by Theorem 3.1, \(F\cong L\varepsilon^*E\) with \(E\) perfect, so the source is \(Lg^*E\), and the target is \(R\varepsilon'_*L\varepsilon'^*Lg^*E\cong Lg^*E\) by Theorem 3.1 over \(S'\), since \(Lg^*E\) is perfect of the same amplitude. In general it is not an isomorphism (Exercise 5.2).

## 4. Diagrams of schemes

Let \(I\) be a small category and \(X\colon I\to(\mathrm{Sch}/S)\) a diagram of schemes over \(S\), with the morphisms \(X_\alpha\colon X_i\to X_j\) for the arrows \(\alpha\colon i\to j\).

**Construction 4.1.** The Zariski topoi \((X_i)_{\mathrm{Zar}}\), with the morphisms of topoi defined by the \(X_\alpha\), form a topos fibred over \(I\) (Definition 1.1 of the lesson on fibred topoi), ringed by the \(\mathcal O_{X_i}\). Its total topos is the *Zariski topos* \(\operatorname{Top}(X_{\mathrm{Zar}})\) of \(X\), ringed by \(\mathcal O\). Representable functors are fppf sheaves [Stacks, Tag 023Q], so by the Yoneda embedding \(X\) is a diagram in the topos of sheaves on \((\mathrm{Sch}/S)_{\mathrm{fppf}}\), and it defines a topos fibred over \(I\) with levels \(\operatorname{Sh}((\mathrm{Sch}/X_i)_{\mathrm{fppf}})\) (Examples 1.2 (c) of that lesson and [Tag 021W]); its total topoi are the *fppf topoi* \(\operatorname{Top}(X_{\mathrm{fppf}})\) and \(\operatorname{Top}^{\mathrm o}(X_{\mathrm{fppf}})\) of \(X\). The comparison morphisms \(\varepsilon_i\) of the \(X_i\) are compatible with the transition morphisms, through the isomorphisms \(X_{\alpha,\mathrm{big}}^*\varepsilon_j^*\cong\varepsilon_i^*X_\alpha^*\) [Tag 03FH], so they form a morphism of fibred topoi over the identity of \(I\), and a morphism of ringed topoi
\[
\varepsilon\colon\operatorname{Top}(X_{\mathrm{fppf}})\longrightarrow\operatorname{Top}(X_{\mathrm{Zar}})
\]
(Proposition 2.1 of the lesson on morphisms of fibred topoi).

A module \(M\) on \(\operatorname{Top}(X_{\mathrm{Zar}})\) is a family of \(\mathcal O_{X_i}\)-modules \(M_i\) with maps \(M_\alpha\colon X_\alpha^*M_j\to M_i\) (Proposition 4.2 of the lesson on morphisms of fibred topoi). It is *termwise quasi-coherent* if every \(M_i\) is quasi-coherent, and *cartesian* if every \(M_\alpha\) is an isomorphism; the same terms are used on the fppf side. \(D_{\mathrm{qc}}(X_{\mathrm{Zar}})\) is the full subcategory of \(D(X_{\mathrm{Zar}})\) of objects with termwise quasi-coherent cohomology. An object \(E\) of \(D^-(X_{\mathrm{Zar}})\) or of \(D^-(X_{\mathrm{fppf}})\) is *quasi-cartesian* if for every arrow \(\alpha\) the map \(LX_\alpha^*E_j\to E_i\) is an isomorphism.

**Lemma 4.2.**

1. For \(E\in D^-(X_{\mathrm{Zar}})\) and every \(i\), \((L\varepsilon^*E)_i\cong L\varepsilon_i^*(E_i)\), and for \(G\in D^+(X_{\mathrm{fppf}})\), \((R\varepsilon_*G)_i\cong R\varepsilon_{i*}(G_i)\).
2. Proposition 2.1 and Corollary 2.2 hold with \(S\) replaced by \(X\): for \(M\in D^b_{\mathrm{qc}}(X_{\mathrm{Zar}})\) with \(H^iM=0\) for \(i<a\) and \(n\leq a\), \(M\cong R\varepsilon_*t_{[n}L\varepsilon^*M\), and for \(E\in D^-(X_{\mathrm{Zar}})\) the corresponding isomorphisms of \(\operatorname{RHom}\) and of \(\varprojlim_n\operatorname{Hom}\) hold.
3. \(L\varepsilon^*\) carries quasi-cartesian objects to quasi-cartesian objects. An object \(E\) of \(D^-(X_{\mathrm{fppf}})\) is quasi-cartesian if and only if every cohomology module \(H^nE\) is cartesian.

**Proof.** (1) The restriction to the level \(i\) has the left adjoint \(i_!\) with \(i_!(L)_j=\bigoplus_{\beta\colon j\to i}X_\beta^*L\), and tensor products are computed levelwise (Proposition 4.2 (b), (c) of the lesson on morphisms of fibred topoi). A free module \(\mathcal O_{X_i}^{(U)}\) on an object \(U\) of \((X_i)_{\mathrm{Zar}}\) has flat inverse images, so \(i_!\mathcal O_{X_i}^{(U)}\) has flat components; every module on \(\operatorname{Top}(X_{\mathrm{Zar}})\) is a quotient of a sum of such modules, since maps out of \(i_!\mathcal O_{X_i}^{(U)}\) are sections over \(U\) at the level \(i\). So every \(E\in D^-(X_{\mathrm{Zar}})\) is represented by a bounded above complex \(P\) of modules with flat components [Stacks, Tag 05T7]. A module with flat components is flat, tensor products being levelwise, so \(P\) is K-flat [Tag 06YQ] and \(L\varepsilon^*E=\varepsilon^*P\) [Tag 06YY]. The inverse image is computed levelwise, so \((\varepsilon^*P)_i=\varepsilon_i^*P_i\), and \(P_i\) is a bounded above complex of flat modules, which computes \(L\varepsilon_i^*E_i\). The second assertion is Proposition 4.1 and Remark 4.2 of the lesson on cohomology of total topoi.

(2) By (1), the map \(M\to R\varepsilon_*t_{[n}L\varepsilon^*M\) is, at the level \(i\), the map of Proposition 2.1 for \(M_i\) on \(X_i\), truncations being levelwise; an isomorphism of modules on the total topos is detected levelwise. The rest follows as in Corollary 2.2, with the adjunction [Tag 07A6] for the ringed total topoi (topoi by Theorem 4.2 of the lesson on fibred topoi).

(3) For an arrow \(\alpha\colon i\to j\), \(LX_\alpha^*\) and \(L\varepsilon^*\) commute up to isomorphism, by the isomorphism \(X_{\alpha,\mathrm{big}}^*\varepsilon_j^*\cong\varepsilon_i^*X_\alpha^*\) applied to complexes of flat modules; the map \(LX_\alpha^*(L\varepsilon^*E)_j\to(L\varepsilon^*E)_i\) is \(L\varepsilon_i^*\) of \(LX_\alpha^*E_j\to E_i\), by (1). On the fppf side \(X_{\alpha,\mathrm{big}}^*\) is the restriction to the localization, an exact functor, so \(LX_{\alpha,\mathrm{big}}^*=X_{\alpha,\mathrm{big}}^*\) commutes with cohomology sheaves, and \(X_{\alpha,\mathrm{big}}^*E_j\to E_i\) is an isomorphism if and only if it is on every \(H^n\). \(\square\)

On the Zariski side the second statement of (3) fails: a quasi-cartesian object can have cohomology modules that are not cartesian (Exercise 5.3).

## 5. Exercises

**5.1.** Let \(S=\operatorname{Spec}\mathbb Z\), \(p\) a prime, and \(K\) the kernel of multiplication by \(p\) on \(\mathcal O\) on the big site. Show that \(K(T)=0\) for every flat \(\mathbb Z\)-scheme \(T\) and \(K(T)=\Gamma(T,\mathcal O_T)\) for every \(\mathbb F_p\)-scheme \(T\). Deduce that \(K\) is adequate but not quasi-coherent, and that \(L\varepsilon^*(\mathcal O_S/p)\) has the nonzero cohomology sheaf \(K\) in degree \(-1\), although \(\mathcal O_S/p\) is a quasi-coherent module in degree \(0\).

**5.2.** Let \(S=\operatorname{Spec}\mathbb Z\), \(S'=\operatorname{Spec}\mathbb F_p\) with \(g\colon S'\to S\), and \(F=\varepsilon^*(\mathcal O_S/p)\), a quasi-coherent module in degree \(0\). Compute both sides of the base change map of Remark 3.2 and show that it is not an isomorphism.

**5.3.** Let \(I=\{0\to1\}\) and \(X\) the diagram \(X_\alpha\colon\operatorname{Spec}\mathbb F_p\to\operatorname{Spec}\mathbb Z\). Let \(P\) be the complex \(\mathcal O\xrightarrow{p}\mathcal O\) on \(\operatorname{Spec}\mathbb Z\), in degrees \(-1\) and \(0\), and \(E\) the complex of modules on \(\operatorname{Top}(X_{\mathrm{Zar}})\) with \(E_1=P\), \(E_0=X_\alpha^*P\) and the identity as structure map. Show that \(E\) is quasi-cartesian but that \(H^{-1}E\) is not cartesian.

## 6. Complete solutions

**5.1.** For an affine \(T=\operatorname{Spec}B\), \(K(T)=\{x\in B:px=0\}\). If \(B\) is flat over \(\mathbb Z\) it is torsion free, so \(K(T)=0\); if \(pB=0\), \(K(T)=B\). Both properties pass to non-affine \(T\) by the sheaf property. \(K\) is the kernel of \(p\colon\mathcal O_S^a\to\mathcal O_S^a\), hence adequate. If \(K\) were quasi-coherent, \(K=N^a\) with \(N=\varepsilon_*K\) (Proposition 1.1 (2)), and \(N(S)=K(\operatorname{Spec}\mathbb Z)=0\), so \(N=0\) and \(K=0\); but \(K(\operatorname{Spec}\mathbb F_p)=\mathbb F_p\). The complex \(\mathbb Z\xrightarrow{p}\mathbb Z\) in degrees \(-1,0\) is a flat resolution of \(\mathcal O_S/p\), so \(L\varepsilon^*(\mathcal O_S/p)\) is \(\mathcal O\xrightarrow{p}\mathcal O\), whose \(H^{-1}\) is \(K\).

**5.2.** By Proposition 1.1, \(R\varepsilon_*F=\mathcal O_S/p\), so the source is \(Lg^*(\mathbb Z/p)=\mathbb Z/p\otimes^{\mathbf L}_{\mathbb Z}\mathbb F_p\), computed by \(\mathbb F_p\xrightarrow{0}\mathbb F_p\): it has \(\mathbb F_p\) in degrees \(-1\) and \(0\). The target is \(R\varepsilon'_*g_{\mathrm{big}}^*F\), and \(g_{\mathrm{big}}^*F=(g^*(\mathcal O_S/p))^a=\mathcal O_{S'}^a\), whose \(R\varepsilon'_*\) is \(\mathbb F_p\) in degree \(0\) (Proposition 1.1 (3)). The map cannot be an isomorphism, since the source has \(H^{-1}\neq0\).

**5.3.** \(P\) is a complex of flat modules, so \(LX_\alpha^*E_1=X_\alpha^*P=E_0\) and \(E\) is quasi-cartesian. \(H^{-1}E_1=0\), since multiplication by \(p\) is injective on \(\mathbb Z\), while \(E_0\) is \(\mathbb F_p\xrightarrow{0}\mathbb F_p\), with \(H^{-1}E_0=\mathbb F_p\). The map \(X_\alpha^*H^{-1}E_1=0\to H^{-1}E_0=\mathbb F_p\) is not an isomorphism, so \(H^{-1}E\) is not cartesian.

## Sources

The comparison of the Zariski and the big flat topoi of a scheme for complexes with quasi-coherent cohomology and for perfect complexes, and its use for diagrams of schemes, are due to Illusie, in his work on the cotangent complex. Adequate modules and their properties are taken from the Stacks project.
