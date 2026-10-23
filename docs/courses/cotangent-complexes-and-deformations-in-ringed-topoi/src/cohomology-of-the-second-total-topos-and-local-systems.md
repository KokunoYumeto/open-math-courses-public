# Cohomology of the second total topos and local systems

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The second total topos of a fibred topos has transition maps in the other direction: an object is a family of sheaves on the levels with maps from each level to the inverse images of the later ones. Its direct images are equalizers involving base change maps, not limits of the direct images of the levels, and they do not commute with restriction to the levels. This lesson computes its cohomology under an explicit acyclicity hypothesis. The direct image factors through the simplicial topos of the fibred topos, which pulls each sheaf back from the last level of a string to the first. A standard resolution then identifies the derived direct image with that of the associated simplicial object. Cartesian objects of the two total topoi correspond, and for them the two cohomologies agree. The same method gives a base change criterion for direct images under morphisms that fix the index category.

**Prerequisites.** [*Cohomology of total topoi*](cohomology-of-total-topoi.md) and [*Cohomology of simplicial topoi and cohomological descent*](cohomology-of-simplicial-topoi-and-cohomological-descent.md); Theorem 4.3, Proposition 5.1 and Proposition 3.1 of [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md); Sections 1 and 3 of [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); Leray's acyclicity lemma [[Stacks, Tag 015E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-leray-acyclicity)].

**Standing hypotheses.** \(X\) is a good topos fibred over a small category \(I\), every \(f^*\) having a left adjoint \(f_!\), and the second total category \(\operatorname{Top}^{\mathrm o}(X)\) is a topos. By Theorem 4.3 of the lesson on fibred topoi, this holds when every \(f_!\) preserves fibre products, in particular for diagrams in a topos (Proposition 5.1 there), and it holds for every good fibred topos by Corollary 4.1 of [*Giraud's characterization of topoi*](giraud-s-characterization-of-topoi.md). An abelian sheaf \(E\) on \(\operatorname{Top}^{\mathrm o}(X)\) is a family of abelian sheaves \(E_i\) with additive maps \(E_f\colon E_i\to f^*E_j\) for \(f\colon i\to j\). Colimits and finite limits are computed levelwise, so a sequence of abelian sheaves is exact if and only if it is exact at every level. Notation is otherwise that of the lessons on cohomology of total topoi and of simplicial topoi.

## 1. Standard resolutions

**Lemma 1.1.** For \(E\in\operatorname{Top}^{\mathrm o}(X)\) and \(L\in X^{\mathrm{dis}}\), put \(e^{\mathrm o*}E=(E_i)_i\) and \(e^{\mathrm o}_*L=\prod_ii^{\mathrm o}_*(L_i)\), so that
\[
(e^{\mathrm o}_*L)_j=\prod_i\prod_{f\colon j\to i}f^*L_i .
\]
Then \(e^{\mathrm o}_*\) is right adjoint to \(e^{\mathrm o*}\), and \(e^{\mathrm o}=(e^{\mathrm o*},e^{\mathrm o}_*)\) is a morphism of topoi \(X^{\mathrm{dis}}\to\operatorname{Top}^{\mathrm o}(X)\). On abelian sheaves, \(e^{\mathrm o*}\) is exact and conservative, and \(e^{\mathrm o}_*\) carries injectives to injectives.

**Proof.** By Proposition 3.1 (2) of the lesson on fibred topoi, \(i^{\mathrm o}_*\) is right adjoint to the level functor \(i^{\mathrm o*}\), with the stated levels; products are computed levelwise. So \(e^{\mathrm o}_*\) is right adjoint to \(e^{\mathrm o*}\). The functor \(e^{\mathrm o*}\) also has the left adjoint \(\coprod_ii^{\mathrm o}_!\), so it is exact, and \((e^{\mathrm o*},e^{\mathrm o}_*)\) is a morphism of topoi. It is conservative as in Lemma 1.1 of the lesson on cohomology of total topoi, and \(e^{\mathrm o}_*\) carries injectives to injectives because its left adjoint is exact [Stacks, Tag 015Z]. \(\square\)

For \(x\in N_n(I)\), a string \(x(0)\to x(1)\to\cdots\to x(n)\), write \(c(x)\colon x(0)\to x(n)\) for the composite arrow; for \(n=0\) it is the identity.

**Proposition 1.2.** Let \(E\) be an abelian sheaf on \(\operatorname{Top}^{\mathrm o}(X)\).

1. The standard resolution \(E\to(e^{\mathrm o}_*e^{\mathrm o*})^{\bullet+1}E\), built as in Section 2 of the lesson on cohomology of total topoi from the adjunction between \(e^{\mathrm o*}\) and \(e^{\mathrm o}_*\), is exact.
2. For \(n\geq0\) and every object \(k\),
\[
\begin{aligned}&\bigl((e^{\mathrm o}_*e^{\mathrm o*})^nE\bigr)_k\\&\quad=\prod_{x\in N_n(I),\ x(0)=k}c(x)^*E_{x(n)} .\end{aligned}
\]
3. If \(f^*E_j\) is totally acyclic for every arrow \(f\colon i\to j\) of \(I\), identities included, then every term \((e^{\mathrm o}_*e^{\mathrm o*})^{n+1}E\) is a totally acyclic sheaf on \(\operatorname{Top}^{\mathrm o}(X)\).
4. If every \(f^*\) carries injective abelian sheaves to injective abelian sheaves, every abelian sheaf on \(\operatorname{Top}^{\mathrm o}(X)\) is a subsheaf of an injective sheaf whose levels are injective.

**Proof.** (1) The proof of Proposition 2.1 of the lesson on cohomology of total topoi applies: by [Stacks, Tag 08ND] in the opposite categories and [Stacks, Tag 01A0], the complex becomes contractible after \(e^{\mathrm o*}\), and \(e^{\mathrm o*}\) detects exactness.

(2) For \(n=0\) both sides are \(E_k\). If the formula holds for \(n\), Lemma 1.1 gives
\[
\begin{aligned}&\bigl((e^{\mathrm o}_*e^{\mathrm o*})^{n+1}E\bigr)_k\\&\quad=\prod_{f\colon k\to i}f^*\prod_{x(0)=i}c(x)^*E_{x(n)}\\&\quad=\prod_{f,\,x}(c(x)f)^*E_{x(n)},\end{aligned}
\]
because \(f^*\) commutes with products, having the left adjoint \(f_!\). The pairs \((f,x)\) are the strings of \(n+1\) arrows starting at \(k\).

(3) By (2), \((e^{\mathrm o}_*e^{\mathrm o*})^{n+1}E=e^{\mathrm o}_*L\), where every component \(L_k\) is a product of sheaves \(g^*E_j\). These are totally acyclic by hypothesis, so \(L\) is totally acyclic (Lemma 1.3 (3) of the lesson on cohomology of total topoi; in the product topos, cohomology is computed componentwise). By Lemma 1.3 (2) of that lesson, applied to the morphism of topoi \(e^{\mathrm o}\), \(e^{\mathrm o}_*L\) is totally acyclic.

(4) The unit \(E\to e^{\mathrm o}_*e^{\mathrm o*}E\) is a monomorphism, its component at \((j,\mathrm{id}_j)\) on the level \(j\) being the identity. Choose a monomorphism \(e^{\mathrm o*}E\to J\) with \(J\) injective. Then \(E\to e^{\mathrm o}_*J\) is a monomorphism into an injective sheaf, whose levels \(\prod_{i,f}f^*J_i\) are injective by hypothesis. \(\square\)

## 2. Direct images and the simplicial topos

Let \(Y\) be a topos and \(p\colon X\to Y\) a morphism of fibred topoi to it. It induces the morphism of topoi \(p^{\mathrm o}\colon\operatorname{Top}^{\mathrm o}(X)\to Y\) of Section 3 of the lesson on morphisms of fibred topoi, and the morphism \(p\colon C_\bullet(X)\to Y\) from the simplicial topos of \(X\) (Definition 3.1 of the lesson on cohomology of simplicial topoi).

**Definition 2.1.** For an abelian sheaf \(E\) on \(\operatorname{Top}^{\mathrm o}(X)\), let \(C_\bullet(E)\) be the abelian sheaf on \(\operatorname{Top}(C_\bullet(X))\) with levels
\[
C_n(E)=\bigl(c(x)^*E_{x(n)}\bigr)_{x\in N_n(I)} .
\]
For \(\alpha\colon[m]\to[n]\), its map \(C_\alpha^*C_m(E)\to C_n(E)\) has at \(x\) the component
\[
\begin{aligned}&x(0\to\alpha(0))^*c(x\alpha)^*E_{x(\alpha(m))}\\&\quad\longrightarrow c(x)^*E_{x(n)}\end{aligned}
\]
obtained by applying \(x(0\to\alpha(m))^*\) to \(E_g\colon E_{x(\alpha(m))}\to g^*E_{x(n)}\), where \(g=x(\alpha(m)\to n)\), and using \(g\circ x(0\to\alpha(m))=c(x)\).

The conditions on composites hold because \(E_{hg}=g^*(E_h)\circ E_g\). Since every \(c(x)^*\) is exact, \(E\mapsto C_\bullet(E)\) is an exact functor.

**Lemma 2.2.** For every abelian sheaf \(E\) on \(\operatorname{Top}^{\mathrm o}(X)\), \(p^{\mathrm o}_*E=p_*C_\bullet(E)\), naturally in \(E\).

**Proof.** By Proposition 3.1 of the lesson on morphisms of fibred topoi, with the one-point category as target, \(p^{\mathrm o}_*E\) is the equalizer of the two maps
\[
\prod_ip_{i*}E_i\rightrightarrows\prod_{g\colon i_0\to i_1}p_{i_0*}g^*E_{i_1}
\]
whose components at \(g\) are \(p_{i_0*}(E_g)\) and the base change map \(p_{i_1*}E_{i_1}\to p_{i_0*}g^*E_{i_1}\). By the description of the cofaces in Theorem 2.1 of the lesson on cohomology of simplicial topoi, \(p_*C_\bullet(E)\) is the equalizer of the two cofaces \(p_{0*}C_0(E)\rightrightarrows p_{1*}C_1(E)\). These are the same products, and by Definition 2.1 the coface \(\delta^1\) has the component \(p_{i_0*}(E_g)\) at \(x=g\), while \(\delta^0\) has the base change map. \(\square\)

**Lemma 2.3.** For every abelian sheaf \(M\) on \(\operatorname{Top}^{\mathrm o}(X)\), applying \(p^{\mathrm o}_*\) to the standard resolution of \(M\) gives the cosimplicial sheaf \([n]\mapsto p_{n*}C_n(M)\) of the simplicial topos \(C_\bullet(X)\):
\[
\begin{aligned}&p^{\mathrm o}_*\bigl((e^{\mathrm o}_*e^{\mathrm o*})^{n+1}M\bigr)\\&\quad\cong\prod_{x\in N_n(I)}p_{x(0)*}c(x)^*M_{x(n)},\end{aligned}
\]
compatibly with the cofaces.

**Proof.** Since \(p^{\mathrm o}\circ e^{\mathrm o}\) has components \(p_i\), \(p^{\mathrm o}_*e^{\mathrm o}_*L=\prod_ip_{i*}L_i\). With \(L=e^{\mathrm o*}(e^{\mathrm o}_*e^{\mathrm o*})^nM\), Proposition 1.2 (2) gives the product formula. The coface \(d^k\) of the standard resolution inserts the unit of the adjunction at the depth \(k\). At depth \(0\), the unit of \(e^{\mathrm o}\) composed with \(p^{\mathrm o}_*\) is the inclusion of an equalizer as in Lemma 2.2; it carries the factor of \(y\) to the factor of each \(x\) with \(x\delta^0=y\) by the base change map along \(x(0\to1)\), which is the coface \(\delta^0\) of \(C_\bullet(M)\). At depth \(n\), the unit applied to \(M\) has the components \(M_f\colon M_k\to f^*M_l\); it carries the factor of \(x\delta^n\) to the factor of \(x\) by \(c(x\delta^n)^*(M_{x(n-1\to n)})\), the coface \(\delta^n\). At a depth \(0<k<n\), it carries the factor of \(x\delta^k\) to the factor of \(x\) by the transitivity isomorphism of \(X\), the coface \(\delta^k\). \(\square\)

**Theorem 2.4.** Let \(E\in D^+(\operatorname{Ab}(\operatorname{Top}^{\mathrm o}(X)))\) be represented by a bounded below complex \(E^\bullet\) such that \(f^*E^q_j\) is totally acyclic for every arrow \(f\colon i\to j\) of \(I\), identities included. Then there is a canonical isomorphism
\[
Rp^{\mathrm o}_*E\cong Rp_*C_\bullet(E).
\]

**Proof.** Let \(R^{n,q}=(e^{\mathrm o}_*e^{\mathrm o*})^{n+1}E^q\). By Proposition 1.2 (1), each column \(R^{\bullet,q}\) is a resolution of \(E^q\), so the total complex of \(R\) is a resolution of \(E^\bullet\) [Stacks, Tag 0133]. By Proposition 1.2 (3), its terms are totally acyclic, hence acyclic for \(p^{\mathrm o}_*\) [Stacks, Tag 0731]. By Leray's acyclicity lemma [Stacks, Tag 015E], \(Rp^{\mathrm o}_*E\) is represented by \(p^{\mathrm o}_*\) of this total complex. By Lemma 2.3, this is the total complex of the double complex \(p_{n*}C_n(E^q)\). The levels \(c(x)^*E^q_{x(n)}\) of \(C_\bullet(E^q)\) are totally acyclic by hypothesis, so by Theorem 2.1 (2) of the lesson on cohomology of simplicial topoi, the same total complex represents \(Rp_*C_\bullet(E)\). \(\square\)

## 3. Local systems

**Proposition 3.1.** Let \(\operatorname{Cart}\) denote the full subcategories of cartesian objects, those whose maps \(E_f\) are isomorphisms. The rule \(E\mapsto\overline E\), with \(\overline E_i=E_i\) and \(\overline E_f=(E_f)^{-1}\colon E_i\to f^*E_j\), is an equivalence
\[
\begin{aligned}&\operatorname{Cart}(\operatorname{Top}(X))\\&\quad\xrightarrow{\ \sim\ }\operatorname{Cart}(\operatorname{Top}^{\mathrm o}(X)),\end{aligned}
\]
with the inverse given by the same rule.

**Proof.** For \(i\xrightarrow{f}j\xrightarrow{g}k\), the condition \(E_{gf}=E_f\circ f^*(E_g)\) in \(\operatorname{Top}(X)\) is equivalent, after inverting all three isomorphisms, to \(\overline E_{gf}=f^*(\overline E_g)\circ\overline E_f\), the condition in \(\operatorname{Top}^{\mathrm o}(X)\). A family of maps \(u_i\) is compatible with the \(E_f\) exactly when it is compatible with their inverses. \(\square\)

**Lemma 3.2.** For a cartesian abelian sheaf \(E\) on \(\operatorname{Top}(X)\), there is an isomorphism, natural in \(E\),
\[
C_\bullet(E)\xrightarrow{\ \sim\ }C_\bullet(\overline E),
\]
where \(C_\bullet(E)\) is that of Definition 3.1 of the lesson on cohomology of simplicial topoi and \(C_\bullet(\overline E)\) that of Definition 2.1. On the level \(n\), its component at \(x\) is \(\overline E_{c(x)}=(E_{c(x)})^{-1}\colon E_{x(0)}\to c(x)^*E_{x(n)}\).

**Proof.** We check compatibility with the map for \(\alpha\colon[m]\to[n]\) at \(x\). Put \(a=x(0\to\alpha(0))\), \(b=c(x\alpha)\) and \(g=x(\alpha(m)\to n)\), so that \(c(x)=gba\). The map of \(C_\bullet(E)\) is \(E_a\colon a^*E_{x(\alpha(0))}\to E_{x(0)}\), and that of \(C_\bullet(\overline E)\) is \(a^*b^*(\overline E_g)\). The square to be checked says
\[
\overline E_{gba}\circ E_a=a^*b^*(\overline E_g)\circ a^*(\overline E_b)
\]
as maps \(a^*E_{x(\alpha(0))}\to c(x)^*E_{x(n)}\). By the conditions on composites, \(\overline E_{gba}=a^*(\overline E_{gb})\circ\overline E_a\) and \(\overline E_{gb}=b^*(\overline E_g)\circ\overline E_b\). Since \(\overline E_a\circ E_a=\mathrm{id}\), both sides agree. \(\square\)

**Theorem 3.3.** Let \(E\) be a cartesian abelian sheaf on \(\operatorname{Top}^{\mathrm o}(X)\) having a resolution \(F^\bullet\) by abelian sheaves such that \(f^*F^q_j\) is totally acyclic for every arrow \(f\colon i\to j\), identities included. Then there is a canonical isomorphism
\[
Rp^{\mathrm o}_*(E)\cong Rp_*(\overline E),
\]
the right side being computed on \(\operatorname{Top}(X)\).

**Proof.** By Theorem 2.4, \(Rp^{\mathrm o}_*E\cong Rp_*C_\bullet(F^\bullet)\). Since \(C_\bullet\) is exact, \(C_\bullet(F^\bullet)\) is a resolution of \(C_\bullet(E)\), so \(Rp_*C_\bullet(F^\bullet)\cong Rp_*C_\bullet(E)\). By Lemma 3.2 applied to the cartesian sheaf \(\overline E\) of \(\operatorname{Top}(X)\), whose image under the equivalence is \(E\), \(C_\bullet(E)\cong C_\bullet(\overline E)\), where now \(C_\bullet(\overline E)\) is formed in \(\operatorname{Top}(X)\). Finally \(Rp_*C_\bullet(\overline E)\cong Rp_*\overline E\) by Proposition 3.2 of the lesson on cohomology of simplicial topoi. \(\square\)

**Corollary 3.4.** Suppose that every abelian sheaf on \(Y\) is a subsheaf of a totally acyclic sheaf \(F\) such that every \(p_i^*F\) is totally acyclic. Then for \(F\in D^+(Y)\) there is a canonical isomorphism
\[
Rp_*p^*F\cong Rp^{\mathrm o}_*p^{\mathrm o*}F,
\]
where \(p\colon\operatorname{Top}(X)\to Y\) and \(p^{\mathrm o}\colon\operatorname{Top}^{\mathrm o}(X)\to Y\) are the morphisms defined by \(p\).

**Proof.** By the hypothesis, every abelian sheaf on \(Y\) embeds into a sheaf of the stated kind, so \(F\) is represented by a bounded below complex of such sheaves \(F^q\) [Stacks, Tag 05T6]. The sheaves \(p^{\mathrm o*}F^q\) are cartesian, and \(\overline{p^*F^q}=p^{\mathrm o*}F^q\), as the maps of both are the isomorphisms \(\theta\) and their inverses. For an arrow \(f\colon i\to j\), \(f^*p_j^*F^q\cong p_i^*F^q\) is totally acyclic. So Theorem 2.4 applies to \(p^{\mathrm o*}F^\bullet\) itself, and the proof of Theorem 3.3 gives \(Rp^{\mathrm o}_*p^{\mathrm o*}F\cong Rp_*p^*F\). \(\square\)

**Corollary 3.5.** Let \(T\) be a topos, \(X\) a simplicial object of \(T\), and \(p\) the morphism from the simplicial topos \([n]\mapsto T/X_n\) to \(T\). The second total topos is the topos of simplicial objects of \(T\) over \(X\), and for \(E\in D^+(T)\)
\[
Rp^{\mathrm o}_*p^{\mathrm o*}E\cong R\underline{\operatorname{Hom}}\bigl(\mathbb Z(X),E\bigr).
\]

**Proof.** The fibred topos of a diagram is good, its functors \(f_!\) preserve fibre products, and its second total topos is the category of diagrams over \(X\) (Proposition 5.1 of the lesson on fibred topoi). Injective sheaves on \(T\) are totally acyclic, and their restrictions to the \(T/X_n\) are injective (Lemma 5.1 of the lesson on cohomology of simplicial topoi). So Corollary 3.4 applies, and Proposition 5.2 of that lesson computes \(Rp_*p^*E\). \(\square\)

## 4. Base change for morphisms over a fixed index category

Let \(u\colon X\to Y\) be an \(I\)-morphism between fibred topoi satisfying the standing hypotheses, with morphisms of topoi \(u_i\colon X_i\to Y_i\). For an arrow \(f\colon i\to j\) and a sheaf \(G\) on \(X_j\), the isomorphism \(\theta_f\) gives a base change map \(f^*u_{j*}G\to u_{i*}f^*G\), and its derived version \(f^*Ru_{j*}\to Ru_{i*}f^*\). For an abelian sheaf \(G\) on \(\operatorname{Top}^{\mathrm o}(X)\), the projection of the equalizer of Proposition 3.1 of the lesson on morphisms of fibred topoi onto the factor of \((i,\mathrm{id}_i)\) is a map \(i^{\mathrm o*}u^{\mathrm o}_*G\to u_{i*}G_i\).

**Proposition 4.1.** Suppose that every \(X_f^*\) carries injective abelian sheaves to injective abelian sheaves, and that one of the following holds: every \(Y_f^*\) carries injective abelian sheaves to totally acyclic sheaves; or, for every \(n\), only finitely many strings of \(n\) arrows start at each object of \(I\). Let \(E\in D^+(\operatorname{Ab}(\operatorname{Top}^{\mathrm o}(X)))\), and suppose that for every arrow \(f\colon i\to j\) the base change map
\[
f^*Ru_{j*}(E_j)\longrightarrow Ru_{i*}(f^*E_j)
\]
is an isomorphism. Then for every object \(i\), the map \(i^{\mathrm o*}Ru^{\mathrm o}_*E\to Ru_{i*}(E_i)\) is an isomorphism.

**Proof.** By Proposition 1.2 (4), the injective sheaves with injective levels form a class into which every abelian sheaf embeds, so \(E\) is represented by a bounded below complex \(E^\bullet\) of such sheaves [Stacks, Tag 05T6]. By Proposition 1.2 (2) and the hypothesis on the \(f^*\), the terms of the standard resolutions of the \(E^q\) are of the form \(e^{\mathrm o}_*L\) with \(L\) injective, hence injective. So \(Ru^{\mathrm o}_*E\) is represented by the total complex of \(u^{\mathrm o}_*\) of the standard resolutions, and \(Ru_{i*}(E_i)\) by \(u_{i*}\) of their levels \(i\), which are resolutions of \(E^q_i\) by injectives. Let \(u^{\mathrm{dis}}\colon X^{\mathrm{dis}}\to Y^{\mathrm{dis}}\) have the components \(u_i\). Since \(e^{\mathrm o*}u^{\mathrm o*}=(u^{\mathrm{dis}})^*e^{\mathrm o*}\), the right adjoints satisfy \(u^{\mathrm o}_*e^{\mathrm o}_*=e^{\mathrm o}_*u^{\mathrm{dis}}_*\), and by Lemma 1.1 and Proposition 1.2 (2) the map in degree \(n\) at the level \(i\) is the product, over the strings \(x\) of \(n+1\) arrows starting at \(i\), of the base change maps
\[
\begin{aligned}&x(0\to1)^*u_{x(1)*}\bigl(c(x')^*E_{x(n+1)}\bigr)\\&\quad\longrightarrow u_{i*}\bigl(c(x)^*E_{x(n+1)}\bigr),\end{aligned}
\]
where \(x'\) is \(x\) without its first arrow. By the hypothesis applied to \(c(x')\) and to \(c(x)\), and the transitivity of base change maps, each of these is a quasi-isomorphism. If the products are finite, their product is a quasi-isomorphism. Otherwise, by the first alternative, the left sides consist of totally acyclic sheaves: \(u_{x(1)*}\) carries injectives to injectives, its left adjoint being exact, and \(Y_{x(0\to1)}^*\) carries these to totally acyclic sheaves. The right sides consist of injective sheaves. So the cone of each map is an exact complex of totally acyclic sheaves, all of them zero below a fixed degree, and the product of these cones is exact (Lemma 1.3 (5) of the lesson on cohomology of total topoi). So the map is a quasi-isomorphism in every degree \(n\), and, the filtrations being finite in each total degree, on the total complexes [Stacks, Tag 0132]. \(\square\)

Without an acyclicity or finiteness condition of this kind, a product of quasi-isomorphisms of abelian sheaves need not be a quasi-isomorphism, and the argument above does not apply.

## 5. Exercises

**Exercise 5.1.** Suppose \(I\) is a groupoid. Show that every object of \(\operatorname{Top}(X)\) and of \(\operatorname{Top}^{\mathrm o}(X)\) is cartesian, so that the two total topoi are equivalent. For \(I\) a group \(\Gamma\) and \(X\) constant with value the punctual topos, describe the equivalence in terms of right and left \(\Gamma\)-modules.

**Exercise 5.2.** Let \(E\) be a cartesian abelian sheaf on \(\operatorname{Top}(X)\). Show directly that \(\Gamma(\operatorname{Top}(X),E)=\Gamma(\operatorname{Top}^{\mathrm o}(X),\overline E)\).

**Exercise 5.3.** Let \(I=\{0\to1\}\). Let \(Y\) be the constant fibred topos over \(I\) with value the punctual topos, and \(X\) the fibred topos with \(X_0\) the punctual topos, \(X_1\) the topos of sets over \(\{1,2\}\), and \(X_f\) the point \(1\). Let \(u\colon X\to Y\) be the \(I\)-morphism given by global sections. For an abelian sheaf \(G\) on \(\operatorname{Top}^{\mathrm o}(X)\), given by abelian groups \(G_0\), \(G_1=(A,B)\) and a map \(G_f\colon G_0\to A\), show that the level \(0\) of \(u^{\mathrm o}_*G\) is isomorphic to \(G_0\oplus B\), and that the canonical map to \(u_{0*}G_0=G_0\) is the projection, which is not injective when \(B\neq0\). Which hypothesis of Proposition 4.1 fails?

## 6. Complete solutions

**5.1.** Let \(f\colon i\to j\) be invertible in \(I\). In \(\operatorname{Top}(X)\), the conditions on composites for \(f^{-1}f=\mathrm{id}_i\) and \(ff^{-1}=\mathrm{id}_j\) give
\[
\begin{gathered}\mathrm{id}=E_{f^{-1}f}=E_f\circ f^*(E_{f^{-1}}),\\ \mathrm{id}=E_{ff^{-1}}=E_{f^{-1}}\circ(f^{-1})^*(E_f).\end{gathered}
\]
The first identity says that \(f^*(E_{f^{-1}})\) is a right inverse of \(E_f\). Applying \(f^*\) to the second identity and using \(f^*(f^{-1})^*\cong\mathrm{id}\), which carries \(f^*(f^{-1})^*(E_f)\) to \(E_f\), shows that \(f^*(E_{f^{-1}})\) is also a left inverse of \(E_f\). So \(E_f\) is an isomorphism. The same argument applies in \(\operatorname{Top}^{\mathrm o}(X)\). Proposition 3.1 gives the equivalence. For \(I=B\Gamma\) and punctual levels, an object of \(\operatorname{Top}(X)\) is a right \(\Gamma\)-module \(M\) with \(m\cdot g=E_g(m)\) (Exercise 5.2 of the lesson on cohomology of total topoi), and an object of \(\operatorname{Top}^{\mathrm o}(X)\) is a functor \(B\Gamma\to\operatorname{Ab}\), a left \(\Gamma\)-module with \(g\cdot m=E_g(m)\). The equivalence sends the right module \(M\) to the left module with \(g\cdot m=m\cdot g^{-1}\).

**5.2.** A global section of \(E\) is a family \(s_i\in\Gamma(X_i,E_i)\) with \(s_i=E_f(f^*s_j)\) for every \(f\colon i\to j\), by Corollary 2.2 of the lesson on morphisms of fibred topoi. A global section of \(\overline E\) is a family with \(\overline E_f(s_i)=f^*s_j\), by Lemma 2.2 with \(Y\) the punctual topos. Since \(\overline E_f=E_f^{-1}\), the two conditions are equivalent.

**5.3.** By Proposition 3.1 of the lesson on morphisms of fibred topoi, the level \(0\) of \(u^{\mathrm o}_*G\) is the equalizer of two maps from \(u_{0*}G_0\times f^*u_{1*}G_1\) to \(u_{0*}f^*G_1\). Here \(u_{0*}G_0=G_0\), \(f^*u_{1*}G_1=\Gamma(\{1,2\},G_1)=A\oplus B\) (the inverse image along \(Y_f=\mathrm{id}\) is the identity), and \(u_{0*}f^*G_1=A\), the stalk at \(1\). The first map is \((c,(a,b))\mapsto G_f(c)\), the second \((c,(a,b))\mapsto a\). The equalizer is \(\{(c,(a,b)) : a=G_f(c)\}\cong G_0\oplus B\). The canonical map of Section 4 is the projection onto the factor of \((0,\mathrm{id})\), \((c,(a,b))\mapsto c\), whose kernel is \(B\). The other hypotheses of Proposition 4.1 hold: \(X_f^*\), the stalk at \(1\), carries injective sheaves to injective abelian groups, and \(Y_f^*\) is the identity. The base change hypothesis fails: for \(G_1=(A,B)\) injective, the base change map from \(f^*u_{1*}G_1=A\oplus B\) to \(u_{0*}f^*G_1=A\) is the projection, not an isomorphism when \(B\neq0\).

## Sources

The cohomology of the second total topos, the simplicial objects \(C_\bullet(E)\), the comparison of cartesian objects and the base change criterion are due to Illusie, in his work on the cotangent complex and the cohomology of diagrams. Standard resolutions go back to Godement's book on sheaf theory.
