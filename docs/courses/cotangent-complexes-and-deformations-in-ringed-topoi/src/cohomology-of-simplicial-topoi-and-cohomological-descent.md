# Cohomology of simplicial topoi and cohomological descent

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A simplicial topos is a topos fibred over the opposite of the category of finite ordinals. For such an index category, the cohomology of the total topos has a simpler description than for a general one: the derived direct image to a topos is computed by the cosimplicial object formed by the direct images of the levels themselves, with no products over strings of arrows. This gives a spectral sequence from the cohomology of the levels, and it applies to every fibred topos through an associated simplicial topos. Two applications follow. The décalage of a simplicial topos is cohomologically trivial over its augmentation. For a simplicial object \(X\) of a topos \(T\), the derived direct image of the inverse image of a complex \(E\) is \(R\underline{\operatorname{Hom}}(\mathbb Z(X),E)\); so a morphism of simplicial objects that induces a quasi-isomorphism of free abelian sheaves induces an isomorphism on cohomology. For hypercoverings this is cohomological descent, valid in every topos.

**Prerequisites.** [*Cohomology of total topoi*](cohomology-of-total-topoi.md), and the lessons on fibred topoi and their morphisms it uses; Lemma 2.2 of [*Strict simplicial objects and Deligne's contractibility theorem*](strict-simplicial-objects-and-deligne-s-contractibility-theorem.md); Theorems 4.1 and 7.1 of [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md); hypercoverings and the acyclicity of their free abelian sheaves [[Stacks, Tag 01GE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/hypercovering.html#hypercovering-lemma-acyclic-hypercover-sheaves)]; internal Hom in derived categories [[Stacks, Tag 08J7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-internal-hom)].

Notation is that of the lesson on cohomology of total topoi. A *simplicial topos* is a topos \(X\) fibred over \(\Delta^{\mathrm{op}}\). For an increasing map \(\alpha\colon[m]\to[n]\), the corresponding arrow \([n]\to[m]\) of \(\Delta^{\mathrm{op}}\) gives a morphism of topoi \(X(\alpha)\colon X_n\to X_m\). An abelian sheaf \(E\) on \(\operatorname{Top}(X)\) has levels \(E_n\) and maps \(E_\alpha\colon X(\alpha)^*E_m\to E_n\). The cofaces and codegeneracies of \(\Delta\) are written \(\delta^k\colon[n-1]\to[n]\) (the injection missing \(k\)) and \(\sigma^k\colon[n+1]\to[n]\) (the surjection repeating \(k\)).

## 1. A resolution indexed by the simplices

Let \(Y\) be a topos and \(p\colon X\to Y\) a morphism of fibred topoi, as in Section 3.1 of the lesson on cohomology of total topoi: morphisms of topoi \(p_n\colon X_n\to Y\) with isomorphisms \(\theta_\alpha\colon X(\alpha)^*p_m^*\to p_n^*\) compatible with composites. For an abelian sheaf \(E\) on \(\operatorname{Top}(X)\), the direct images \(p_{n*}E_n\) form a cosimplicial abelian sheaf \(\underline{p}_*E\) on \(Y\), and \(p_*E\) is the kernel of the two cofaces \(p_{0*}E_0\rightrightarrows p_{1*}E_1\). Write \(s(\underline{p}_*E)\) for the associated cochain complex, with the alternating sums of the cofaces as differentials.

**Lemma 1.1.** Let \(G\in\operatorname{Ab}(Y)\). Put \(B_n(G)=n^{\mathrm{ab}}_!(p_n^*G)\), where \(n^{\mathrm{ab}}_!\) is the left adjoint of the level functor \(n^*\) on abelian sheaves. For \(0\leq k\leq n\), let \(\partial_k\colon B_n(G)\to B_{n-1}(G)\) be adjoint to the inclusion of \(p_n^*G\cong X(\delta^k)^*p_{n-1}^*G\) (by \(\theta_{\delta^k}\)) as the summand of \(\delta^k\) in
\[
\begin{aligned}&\bigl((n-1)^{\mathrm{ab}}_!p_{n-1}^*G\bigr)_n\\&\quad=\bigoplus_{\beta\colon[n-1]\to[n]}X(\beta)^*p_{n-1}^*G .\end{aligned}
\]
Let \(\varepsilon\colon B_0(G)\to p^*G\) be adjoint to the identity of \(p_0^*G\). Then the complex
\[
\cdots\to B_1(G)\to B_0(G)\xrightarrow{\ \varepsilon\ }p^*G\to0,
\]
with differential \(\sum_k(-1)^k\partial_k\), is exact.

**Proof.** Evaluate at the level \(m\). By Lemma 1.1 of the lesson on cohomology of total topoi,
\[
\begin{aligned}B_n(G)_m&=\bigoplus_{\alpha\colon[n]\to[m]}X(\alpha)^*p_n^*G\\&\cong\bigoplus_{\alpha\in\Delta([n],[m])}p_m^*G,\end{aligned}
\]
using the isomorphisms \(\theta_\alpha\). The map \(\partial_k\) carries the summand of \(\alpha\) to the summand of \(\alpha\circ\delta^k\) by the identity of \(p_m^*G\), because \(\theta\) is compatible with composites. The set \(\Delta([n],[m])\) is the set of \(n\)-simplices of \(\Delta[m]\), and \(\alpha\mapsto\alpha\circ\delta^k\) is its \(k\)-th face. So the augmented complex at the level \(m\) is the augmented chain complex of the simplicial set \(\Delta[m]\), with every copy of \(\mathbb Z\) replaced by \(p_m^*G\). The simplicial set \(\Delta[m]\) is the nerve of the ordered set \([m]\), which has the initial object \(0\). By Lemma 2.2 of the lesson on strict simplicial objects, its augmented chain complex is contractible, and a contracting homotopy given by integer matrices remains one after the replacement. \(\square\)

**Proposition 1.2.** If \(F\) is an injective abelian sheaf on \(\operatorname{Top}(X)\), the complex
\[
\begin{gathered}0\to p_*F\to p_{0*}F_0\\ \to p_{1*}F_1\to p_{2*}F_2\to\cdots\end{gathered}
\]
formed by \(s(\underline{p}_*F)\) and the inclusion of \(p_*F\) is exact.

**Proof.** By adjunction,
\[
\begin{aligned}\operatorname{Hom}(B_n(G),F)&=\operatorname{Hom}(p_n^*G,F_n)\\&=\operatorname{Hom}(G,p_{n*}F_n),\end{aligned}
\]
and \(\operatorname{Hom}(\partial_k,F)\) becomes composition with the \(k\)-th coface \(p_{(n-1)*}F_{n-1}\to p_{n*}F_n\), as in the proof of Proposition 3.4 of the lesson on cohomology of total topoi. Since \(F\) is injective, \(\operatorname{Hom}(-,F)\) carries the exact complex of Lemma 1.1 to an exact complex. Taking \(G=\mathbb Z_K\) for the objects \(K\) of \(Y\), the complex of the statement is exact on sections over every object, hence exact. \(\square\)

## 2. Cohomology of simplicial total topoi

**Theorem 2.1.** Let \(E\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\).

1. If \(I^\bullet\) is a bounded below complex of injectives representing \(E\), the total complex of the double complex \(p_{n*}I^q_n\) represents \(Rp_*E\).
2. If \(E\) is represented by a bounded below complex \(E^\bullet\) whose terms have totally acyclic levels, the total complex of \(p_{n*}E^q_n\) represents \(Rp_*E\). In particular, for an abelian sheaf \(E\) with totally acyclic levels,
\[
R^qp_*E=H^q\bigl(s(\underline{p}_*E)\bigr)\qquad(q\geq0).
\]

**Proof.** (1) By Proposition 1.2, each row \(p_{\bullet*}I^q_\bullet\) is a resolution of \(p_*I^q\). The double complex vanishes for \(n<0\) and for \(q\) below a fixed bound, so \(p_*I^\bullet\) is quasi-isomorphic to its total complex [Stacks, Tag 0133]. And \(p_*I^\bullet\) represents \(Rp_*E\).

(2) Choose a quasi-isomorphism \(E^\bullet\to I^\bullet\) to a bounded below complex of injectives. For each \(n\), the cone of \(E^\bullet_n\to I^\bullet_n\) is an exact complex of totally acyclic sheaves, bounded below: the levels of injectives are injective (Lemma 1.1 of the lesson on cohomology of total topoi). By Lemma 1.3 (5) of that lesson, \(p_{n*}\) of this cone is exact, so the map of double complexes is a quasi-isomorphism on every column. Since the filtrations by \(n\) are finite in each total degree, the map of total complexes is a quasi-isomorphism [Stacks, Tag 0132]. Now apply (1). \(\square\)

**Corollary 2.2.** For \(E\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\) there is a spectral sequence, functorial in \(E\),
\[
E_1^{n,q}=R^qp_{n*}(E_n)\Longrightarrow R^{n+q}p_*E,
\]
whose differential \(d_1\) is the alternating sum of the maps \(R^qp_{(n-1)*}(E_{n-1})\to R^qp_{n*}(E_n)\) induced by the cofaces.

**Proof.** Filter the total complex of Theorem 2.1 (1) by \(n\). The column \(n\) is \(p_{n*}I^\bullet_n\), and \(I^\bullet_n\) is a bounded below complex of injectives representing \(E_n\). So \(E_1^{n,q}=R^qp_{n*}(E_n)\), and \(d_1\) is induced by the differential in the \(n\) direction. The filtration is finite in each degree, so the spectral sequence converges [Stacks, Tag 0132]. \(\square\)

The same argument applies to multisimplicial index categories.

**Theorem 2.3.** Let \(X\) be a topos fibred over \((\Delta^{\mathrm{op}})^k\), and \(p\colon X\to Y\) a morphism to a topos. If \(E\) is an abelian sheaf on \(\operatorname{Top}(X)\) whose levels \(E_{\underline n}\), \(\underline n=(n_1,\ldots,n_k)\), are totally acyclic, then \(R^qp_*E\) is the cohomology of the total complex of the \(k\)-fold cochain complex \(\underline n\mapsto p_{\underline n*}E_{\underline n}\).

**Proof.** For \(G\in\operatorname{Ab}(Y)\), put \(B_{\underline n}(G)=\underline n^{\mathrm{ab}}_!(p_{\underline n}^*G)\), with the faces in each of the \(k\) directions defined as in Lemma 1.1. At the level \(\underline m\), the \(k\)-fold complex \(B_{\bullet}(G)\) is \(p_{\underline m}^*G\) tensored with the \(k\)-fold complex
\[
\mathbb Z[\Delta[m_1]]\otimes\cdots\otimes\mathbb Z[\Delta[m_k]],
\]
by the computation of Lemma 1.1 in each direction. Each augmentation \(\mathbb Z[\Delta[m_j]]\to\mathbb Z\) is a homotopy equivalence of complexes of free abelian groups, so the augmentation of the total complex of the tensor product to \(\mathbb Z\) is a homotopy equivalence. So the total complex of \(B_\bullet(G)\) is a resolution of \(p^*G\). The proofs of Proposition 1.2 and Theorem 2.1 then apply word for word. \(\square\)

## 3. The simplicial topos of a fibred topos

Let \(X\) be a topos fibred over a small category \(I\), and \(N_n(I)\) the set of functors \(x\colon[n]\to I\), that is, of strings of \(n\) composable arrows. For \(x\in N_n(I)\) and \(0\leq a\leq b\leq n\), write \(x(a\to b)\) for the image of the arrow \(a\to b\) of \([n]\).

**Definition 3.1.** The simplicial topos \(C_\bullet(X)\) has levels the product topoi
\[
C_n(X)=\prod_{x\in N_n(I)}X_{x(0)} .
\]
For \(\alpha\colon[m]\to[n]\), the morphism \(C_\alpha\colon C_n(X)\to C_m(X)\) has as inverse image
\[
\begin{aligned}&(L_y)_{y\in N_m(I)}\\&\quad\longmapsto\bigl(X_{x(0\to\alpha(0))}^*L_{x\alpha}\bigr)_{x\in N_n(I)} ,\end{aligned}
\]
which is exact and has the right adjoint \((L_x)_x\mapsto\bigl(\prod_{x\alpha=y}X_{x(0\to\alpha(0))*}L_x\bigr)_y\). Here \(X_f\) is the morphism of the fibred topos \(X\) for an arrow \(f\) of \(I\). The transitivity isomorphisms are those of \(X\), since \(x(0\to\alpha\beta(0))\) is the composite of \(x\alpha(0\to\beta(0))\) and \(x(0\to\alpha(0))\). For an abelian sheaf \(E\) on \(\operatorname{Top}(X)\), the sheaf \(C_\bullet(E)\) on \(\operatorname{Top}(C_\bullet(X))\) has levels \(C_n(E)=(E_{x(0)})_x\), and its map for \(\alpha\) has the component \(E_{x(0\to\alpha(0))}\) at \(x\). A morphism \(p\colon X\to Y\) to a topos gives the morphism \(C_\bullet(X)\to Y\) with components \(p_{x(0)}\), again written \(p\).

**Proposition 3.2.** For \(E\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\) there is a canonical isomorphism
\[
Rp_*E\xrightarrow{\ \sim\ }Rp_*C_\bullet(E).
\]

**Proof.** Represent \(E\) by a bounded below complex of injectives \(I^\bullet\). The levels of each \(I^q\) are injective, so the levels of \(C_\bullet(I^q)\) are families of injectives, which are injective in the product topoi, hence totally acyclic. By Theorem 2.1 (2), \(Rp_*C_\bullet(E)\) is represented by the total complex of the double complex
\[
p_{n*}C_n(I^q)=\prod_{x\in N_n(I)}p_{x(0)*}I^q_{x(0)} .
\]
Its coface for \(\delta^k\) has at \(x\) the component \(p_{x(0)*}I^q_{x(0)}\to p_{x(0)*}I^q_{x(0)}\) from the factor \(x\delta^k\), the identity, when \(k\geq1\), and the map of \(\underline{p}_*I^q\) for the arrow \(x(0\to1)\) when \(k=0\). This is the cosimplicial complex \(C^n(\underline{p}_*I^q)\) of Definition 3.2 of the lesson on cohomology of total topoi, whose total complex represents \(Rp_*E\) by Theorem 3.5 (1) there. \(\square\)

## 4. Décalage

**Definition 4.1.** Let \(X\) be a simplicial topos. The *décalage* \(\operatorname{Dec}_1(X)\) is the simplicial topos with levels \(\operatorname{Dec}_1(X)_n=X_{n+1}\) and morphisms \(X(\mathrm{id}_{[0]}\sqcup\alpha)\) for \(\alpha\colon[m]\to[n]\), where \([0]\sqcup[n]=[n+1]\) is the ordered sum. For \(n\geq0\), let \(\iota_n\colon[0]\to[n+1]\) be the inclusion of the vertex \(0\). The morphisms \(d_n=X(\iota_n)\colon X_{n+1}\to X_0\) form a morphism \(d\colon\operatorname{Dec}_1(X)\to X_0\) to the topos \(X_0\), because \((\mathrm{id}_{[0]}\sqcup\alpha)\circ\iota_m=\iota_n\). For an abelian sheaf \(M\) on \(\operatorname{Top}(X)\), \(\operatorname{Dec}_1^+(M)\) is the sheaf on \(\operatorname{Top}(\operatorname{Dec}_1(X))\) with levels \(M_{n+1}\) and maps \(M_{\mathrm{id}\sqcup\alpha}\).

Dropping the vertex \(0\) forgets the first face operator: the faces of \(\operatorname{Dec}_1(X)\) are the faces \(\delta^{k+1}\) of \(X\), and \(\delta^1\colon[0]\to[1]\) becomes the augmentation.

**Proposition 4.2.** For \(M\in D^+(\operatorname{Ab}(\operatorname{Top}(X)))\), the canonical map
\[
M_0\longrightarrow Rd_*\operatorname{Dec}_1^+(M),
\]
adjoint to the maps \(M_{\iota_n}\colon d_n^*M_0\to M_{n+1}\), is an isomorphism.

**Proof.** Let \(\Delta_0\subset\Delta\) be the subcategory of the maps \(\alpha\) with \(\alpha(0)=0\), and \(\iota^k\colon[0]\to[k]\) the inclusion of the vertex \(0\). For an abelian sheaf \(M\), the rule
\[
\Phi([k])=X(\iota^k)_*M_k
\]
is a functor from \(\Delta_0\) to \(\operatorname{Ab}(X_0)\): for \(\alpha\colon[k]\to[l]\) in \(\Delta_0\), \(\alpha\circ\iota^k=\iota^l\), and \(\Phi(\alpha)\) is \(X(\iota^k)_*\) of the adjoint \(M_k\to X(\alpha)_*M_l\) of \(M_\alpha\), followed by \(X(\iota^k)_*X(\alpha)_*\cong X(\iota^l)_*\). By construction, the cosimplicial sheaf \(\underline{d}_*\operatorname{Dec}_1^+(M)\) is \([n]\mapsto\Phi([n+1])\), with cofaces \(\Phi(\delta^{k+1})\), and the canonical map from \(M_0=\Phi([0])\) is \(\Phi(\delta^1)\). Put \(A^n=\Phi([n+1])\) for \(n\geq-1\), with cofaces \(d^k=\Phi(\delta^{k+1})\colon A^{n-1}\to A^n\) for \(0\leq k\leq n\), and \(h=\Phi(\sigma^0)\colon A^n\to A^{n-1}\); note that \(\sigma^0\) lies in \(\Delta_0\). The identities \(\sigma^0\delta^1=\mathrm{id}\) and \(\sigma^0\delta^{k+1}=\delta^k\sigma^0\) for \(k\geq1\) give
\[
\begin{gathered}hd^0=\mathrm{id},\\ hd^k=d^{k-1}h\quad(k\geq1).\end{gathered}
\]
Hence, for the augmented complex \(0\to A^{-1}\to A^0\to A^1\to\cdots\) with differential \(\delta=\sum_k(-1)^kd^k\), and \(x\in A^n\),
\[
\begin{aligned}h\delta x&=x+\sum_{k=1}^{n+1}(-1)^kd^{k-1}hx\\&=x-\delta hx .\end{aligned}
\]
So the augmented complex is contractible. Now let \(M\) be represented by a bounded below complex of injectives \(I^\bullet\). The functor \(\operatorname{Dec}_1^+\) is exact, so \(\operatorname{Dec}_1^+(I^\bullet)\) represents \(\operatorname{Dec}_1^+(M)\), and its terms have the injective, hence totally acyclic, levels \(I^q_{n+1}\). By Theorem 2.1 (2) applied to \(d\), \(Rd_*\operatorname{Dec}_1^+(M)\) is represented by the total complex of the double complex \(A^n(I^q)\), \(n\geq0\). By the contraction, each row is a resolution of \(A^{-1}(I^q)=I^q_0\), so the map from \(I^\bullet_0\) to the total complex is a quasi-isomorphism [Stacks, Tag 0133]. \(\square\)

## 5. Simplicial objects of a topos

Let \(T\) be a topos and \(X\) a simplicial object of \(T\). By Examples 1.2 (c) of the lesson on fibred topoi, \([n]\mapsto T/X_n\) is a simplicial topos, again written \(X\). The localization morphisms \(p_n\colon T/X_n\to T\) form a morphism \(p\colon X\to T\), and \(p^*E\) has levels \(E|_{X_n}=E\times X_n\). Let \(\mathbb Z(X)\) be the chain complex of the simplicial abelian sheaf \([n]\mapsto\mathbb Z_{X_n}\), the free abelian sheaves on the \(X_n\), placed in degrees \(\leq0\) as a cochain complex.

**Lemma 5.1.** For an object \(U\) of \(T\), with localization \(j\colon T/U\to T\), and \(E\in\operatorname{Ab}(T)\), there is an isomorphism \(j_*j^*E\cong\underline{\operatorname{Hom}}(\mathbb Z_U,E)\), natural in \(U\) and \(E\). The functor \(j^*\) carries injectives to injectives.

**Proof.** For \(V\in T\), adjunction gives \(\operatorname{Hom}(\mathbb Z_V,j_*j^*E)=E(U\times V)\), and also
\[
\begin{aligned}&\operatorname{Hom}\bigl(\mathbb Z_V,\underline{\operatorname{Hom}}(\mathbb Z_U,E)\bigr)\\&\quad=\operatorname{Hom}(\mathbb Z_V\otimes\mathbb Z_U,E)\\&\quad=\operatorname{Hom}(\mathbb Z_{V\times U},E)=E(U\times V),\end{aligned}
\]
naturally in \(V\), \(U\) and \(E\). By the Yoneda lemma, the two sheaves are isomorphic. The functor \(j^*\) has the exact left adjoint \(j_!\), extension by zero on abelian sheaves, so it carries injectives to injectives [Stacks, Tag 015Z]. \(\square\)

**Proposition 5.2.** For \(E\in D^+(T)\), there is a canonical isomorphism, natural in \(X\),
\[
Rp_*p^*E\cong R\underline{\operatorname{Hom}}\bigl(\mathbb Z(X),E\bigr).
\]

**Proof.** Represent \(E\) by a bounded below complex of injectives \(I^\bullet\). By Lemma 5.1, the levels \(I^q|_{X_n}\) of \(p^*I^q\) are injective, hence totally acyclic. By Theorem 2.1 (2), \(Rp_*p^*E\) is represented by the total complex of the double complex
\[
p_{n*}p_n^*I^q\cong\underline{\operatorname{Hom}}\bigl(\mathbb Z_{X_n},I^q\bigr),
\]
where the isomorphism is that of Lemma 5.1, and its naturality identifies the cofaces with the maps induced by the faces of \(\mathbb Z_{X_\bullet}\). This total complex is isomorphic to the Hom complex \(\underline{\operatorname{Hom}}^\bullet(\mathbb Z(X),I^\bullet)\): in each degree only finitely many terms are nonzero, since \(I^\bullet\) is bounded below. A bounded below complex of injectives is K-injective [Stacks, Tag 070J], so this Hom complex represents \(R\underline{\operatorname{Hom}}(\mathbb Z(X),E)\) [Stacks, Tag 08J7]. \(\square\)

A *hypercovering of the final object* of \(T\) is a simplicial object \(X\) such that \(X_0\to e\) and, for every \(n\geq0\), the maps \(X_{n+1}\to(\operatorname{cosk}_n\operatorname{sk}_nX)_{n+1}\) are epimorphisms. For \(n=0\), the target is \(X_0\times X_0\).

**Corollary 5.3 (cohomological descent).** If \(X\) is a hypercovering of the final object of \(T\), then for every \(E\in D^+(T)\) the adjunction map
\[
E\longrightarrow Rp_*p^*E
\]
is an isomorphism. In particular there is a spectral sequence
\[
E_1^{n,q}=H^q(X_n,E)\Longrightarrow H^{n+q}(T,E).
\]

**Proof.** The augmentation \(\mathbb Z(X)\to\mathbb Z\) is a quasi-isomorphism: this is [Stacks, Tag 01GE], applied to a site of \(T\) and the augmentation \(X\to e\), whose hypotheses are the epimorphisms above. Under Proposition 5.2, the adjunction map is \(R\underline{\operatorname{Hom}}(-,E)\) applied to this augmentation: in degree \(0\) of the double complex, it is the map from \(E=\underline{\operatorname{Hom}}(\mathbb Z,E)\) to \(\underline{\operatorname{Hom}}(\mathbb Z_{X_0},E)=p_{0*}p_0^*E\). So it is an isomorphism. For the spectral sequence, apply Corollary 2.2 to the morphism from \(X\) to the punctual topos whose components are the global sections of the topoi \(T/X_n\). It gives
\[
\begin{aligned}E_1^{n,q}&=H^q(T/X_n,E|_{X_n})\\&\Longrightarrow H^{n+q}(\operatorname{Top}(X),p^*E).\end{aligned}
\]
Here \(H^q(T/X_n,E|_{X_n})=H^q(X_n,E)\), since restriction to \(T/X_n\) is exact and preserves injectives (Lemma 5.1). Since \(p_*\) carries injectives to injectives, \(H^m(\operatorname{Top}(X),p^*E)\) is \(H^m(T,Rp_*p^*E)\) [Stacks, Tag 015M], which is \(H^m(T,E)\) by the first part. \(\square\)

No hypothesis on the points of \(T\) is needed here. For general quasi-isomorphisms, the same argument gives the following.

**Corollary 5.4.** Let \(f\colon X\to X'\) be a morphism of simplicial objects of \(T\), with the morphisms \(p\colon X\to T\) and \(p'\colon X'\to T\). Suppose that \(\mathbb Z(f)\colon\mathbb Z(X)\to\mathbb Z(X')\) is a quasi-isomorphism. This holds when \(T\) has enough points and \(f\) is a quasi-isomorphism (Theorem 4.1 of the lesson on homotopy sheaves), and when \(f\) underlies a homomorphism of simplicial abelian sheaves that is a quasi-isomorphism (Theorem 7.1 of that lesson). Then for every \(E\in D^+(T)\) the map
\[
Rp'_*p'^*E\longrightarrow Rp_*p^*E
\]
defined by \(f\) is an isomorphism.

**Proof.** By the naturality in Proposition 5.2, the map is \(R\underline{\operatorname{Hom}}(\mathbb Z(f),E)\), an isomorphism when \(\mathbb Z(f)\) is a quasi-isomorphism. Under either condition, the cited theorem shows that the map of free abelian simplicial sheaves induced by \(f\) is an \(n\)-quasi-isomorphism for every \(n\), since \(f\) is one for every \(n\). For simplicial abelian sheaves this means that it induces isomorphisms on the homology of the normalized complexes (Section 2 of the lesson on homotopy sheaves). The normalized complex is quasi-isomorphic to the complex \(\mathbb Z(-)\) of alternating sums of faces, naturally [Stacks, Tag 019C], so \(\mathbb Z(f)\) is a quasi-isomorphism. \(\square\)

**Remark 5.5.** For an arbitrary topos and an arbitrary quasi-isomorphism \(f\), the free abelian functor still carries \(f\) to a quasi-isomorphism, by a theorem of Van Osdol proved with Boolean localizations (Remark 7.3 of the lesson on homotopy sheaves). That proof rests on Barr's theorem that every topos has a Boolean localization, which is not proved in this programme. So Corollary 5.4 is proved here only under the two stated conditions.

## 6. Exercises

**Exercise 6.1.** Let \(U\to e\) be an epimorphism in \(T\), and \(X\) its Čech nerve, with \(X_n=U^{n+1}\) and the projections and diagonals as faces and degeneracies. Show that \(X\) is a hypercovering of the final object, and deduce a spectral sequence \(E_1^{n,q}=H^q(U^{n+1},E)\Rightarrow H^{n+q}(T,E)\).

**Exercise 6.2.** Let \(K\) be a simplicial set, regarded as a simplicial object of the punctual topos, and \(A\) an abelian group. Show that \(H^n(\operatorname{Top}(K),p^*A)\) is the cohomology of the cochain complex \(n\mapsto A^{K_n}\), with the alternating sums of the maps induced by the faces as differentials, that is, the cohomology of \(K\) with coefficients in \(A\).

**Exercise 6.3.** Let \(X\) be the constant simplicial topos with value a topos \(T\), and \(p\colon X\to T\) the identity on every level. Show that \(Rp_*p^*E\cong E\) for \(E\in D^+(T)\), and that \(H^n(\operatorname{Top}(X),p^*E)=H^n(T,E)\).

## 7. Complete solutions

**6.1.** The map \(X_0=U\to e\) is an epimorphism by hypothesis. The Čech nerve is \(0\)-coskeletal: a map into \(X_{n+1}=U^{n+2}\) is the family of its vertices. So \(X\to\operatorname{cosk}_n\operatorname{sk}_nX\) is an isomorphism for every \(n\geq0\), and all the maps \(X_{n+1}\to(\operatorname{cosk}_n\operatorname{sk}_nX)_{n+1}\) are isomorphisms, in particular epimorphisms. Corollary 5.3 gives the spectral sequence.

**6.2.** Here \(T\) is the category of sets, internal Homs are Homs of abelian groups, and \(H^n(\operatorname{Top}(K),p^*A)=H^n(Rp_*p^*A)\), the global sections of the punctual topos being the identity. Choose an injective resolution \(A\to J^\bullet\). By Proposition 5.2 and its proof, \(Rp_*p^*A\) is represented by the Hom complex \(\operatorname{Hom}^\bullet(\mathbb Z(K),J^\bullet)\). The map \(A\to J^\bullet\) induces a map from the double complex \(\operatorname{Hom}(\mathbb Z[K_n],A)\) to \(\operatorname{Hom}(\mathbb Z[K_n],J^\bullet)\). On each column it is a product of copies of \(A\to J^\bullet\), hence a quasi-isomorphism, because products of abelian groups are exact. So the total complexes are quasi-isomorphic. The first one is the cochain complex \(n\mapsto\operatorname{Hom}(\mathbb Z[K_n],A)=A^{K_n}\) with the alternating sums of the maps induced by the faces.

**6.3.** Let \(I^\bullet\) be a bounded below complex of injectives representing \(E\). The levels of \(p^*I^q\) are \(I^q\), injective and hence totally acyclic, and every \(X(\alpha)\) is the identity. So \(\underline{p}_*p^*I^q\) is the constant cosimplicial sheaf with value \(I^q\). In its cochain complex, the differential from degree \(n-1\) to degree \(n\) is \(\sum_{k=0}^{n}(-1)^k\mathrm{id}\), which is \(0\) for \(n\) odd and the identity for \(n\) even. So the complex is \(I^q\xrightarrow{0}I^q\xrightarrow{\mathrm{id}}I^q\xrightarrow{0}I^q\to\cdots\), a resolution of \(I^q\) concentrated in degree \(0\). By Theorem 2.1 (2) and [Stacks, Tag 0133], \(Rp_*p^*E\cong E\), and taking global sections gives the second statement. Alternatively, \(X\) is the simplicial topos of the constant simplicial object \(e\) of \(T\), the final object, and \(\mathbb Z(e)\to\mathbb Z\) is a quasi-isomorphism, so Proposition 5.2 applies.

## Sources

The cohomology of simplicial topoi, the simplicial topos of a fibred topos, the décalage statement and the formula of Proposition 5.2 are due to Illusie, in his work on the cotangent complex. The resolution of Lemma 1.1 is the one used in the Stacks project for simplicial sites [Stacks, Tags 09WI and 0D78]. Cohomological descent for hypercoverings goes back to SGA 4, Exposé Vbis; the acyclicity of the free abelian sheaves of a hypercovering used here is [Stacks, Tag 01GE]. The theorem of Van Osdol mentioned in Remark 5.5 is discussed in J. F. Jardine's lecture notes *Local homotopy theory*, lecture 6a, [math.uwo.ca](https://www.math.uwo.ca/faculty/jardine/courses/localhom/localhom-lecture06a.pdf).
