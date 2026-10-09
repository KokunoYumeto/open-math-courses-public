# Theorems A and B on Stein manifolds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves H. Cartan's Theorems A and B for Stein manifolds: on a complex manifold with a smooth strictly plurisubharmonic exhaustion, every coherent analytic sheaf has vanishing cohomology in positive degrees (Theorem B) and is generated at every point by its global sections (Theorem A). The proof follows A. Andreotti and H. Grauert. A sublevel set of the exhaustion is enlarged to a bigger one through finitely many small bumps, each inside a coordinate ball, where the local results of the previous lessons apply. The Mayer–Vietoris sequence shows that cohomology in positive degrees does not change along the way. Since the smallest sublevel sets are empty, all these groups vanish, and an abstract Mittag-Leffler argument passes to the whole manifold. Schwartz's finiteness theorem enters once, to make the relevant groups Hausdorff.

We use Plurisubharmonic functions and Stein manifolds, [Stein domains in complex space](stein-domains-in-complex-space.md) and [Fréchet spaces of sections and Schwartz's theorem](frechet-spaces-of-sections-and-schwartzs-theorem.md). The Mayer–Vietoris sequence for two open sets is [Stacks, Tag 01EB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-mayer-vietoris).

Basic references are [Demailly] and [Andreotti–Grauert 1962].

Throughout, \(X\) is a complex manifold with a smooth strictly plurisubharmonic exhaustion \(\psi\), \(X_c=\{\psi<c\}\), and \(\mathcal S\) is a coherent analytic sheaf on \(X\). A **resolving ball** is an open subset of \(X\) identified by a chart with a ball \(B\subset\mathbf C^n\), such that \(\mathcal S\) has a finite free resolution on a neighbourhood of the closure of \(B\) in the chart. By the local syzygy theorem [Coherent sheaves and Oka's coherence theorem, Theorem 3.4](coherent-sheaves-and-okas-theorem.md#3-the-category-of-coherent-analytic-sheaves), every point has arbitrarily small resolving balls. Every Stein open subset of a resolving ball is a Stein domain in the chart on which \(\mathcal S\) has a finite free resolution, so by [Stein domains in complex space, Theorem 4.1](stein-domains-in-complex-space.md#4-coherent-sheaves-on-stein-domains) it carries no higher cohomology of \(\mathcal S\).

## 1. Local approximation

**Lemma 1.1.** Let \(W\) be a Stein open subset of a resolving ball and \(W'\subset W\) open. Suppose that for every compact \(L\subset W'\) there are a smooth strictly plurisubharmonic exhaustion \(\psi'\) of \(W\) and a number \(b\) with \(L\subset\{\psi'<b\}\) and \(\overline{\{\psi'<b\}}\subset W'\). Then the restriction \(\mathcal S(W)\to\mathcal S(W')\) has dense image.

**Proof.** Let \(W_b=\{\psi'<b\}\) for such a pair. Both \(W\) and \(W_b\) are Stein domains in the chart, so by Theorem 4.1 of [Stein domains in complex space](stein-domains-in-complex-space.md#4-coherent-sheaves-on-stein-domains) the maps \(\mathcal O(W)^{p_0}\to\mathcal S(W)\) and \(\mathcal O(W_b)^{p_0}\to\mathcal S(W_b)\) from the first term of the resolution are surjective, and the second is continuous and open by the definition of the Fréchet topology. By the approximation theorem [Stein domains in complex space, Theorem 3.1](stein-domains-in-complex-space.md#3-approximation-on-sublevel-sets), \(\mathcal O(W)^{p_0}\to\mathcal O(W_b)^{p_0}\) has dense image. Hence \(\mathcal S(W)\to\mathcal S(W_b)\) has dense image.

Now let \(s\in\mathcal S(W')\). Choose relatively compact open sets \(W'_1\subset W'_2\subset\cdots\) exhausting \(W'\). The map \(\mathcal S(W')\to\prod_k\mathcal S(W'_k)\) is a topological embedding, by the open mapping theorem, since its image is closed; so a neighbourhood of \(s\) contains a set \(\{t:\ t|_{W'_k}\in N\}\) for some \(k\) and some neighbourhood \(N\) of \(s|_{W'_k}\). Apply the hypothesis to \(L=\overline{W'_k}\): approximate \(s|_{W_b}\) by restrictions of elements of \(\mathcal S(W)\), and restrict further to \(W'_k\subset W_b\). \(\square\)

## 2. Enlarging a sublevel set by bumps

**Lemma 2.1.** Let \(c<d\). There are open sets \(X_c=G_0\subset G_1\subset\cdots\subset G_s=X_d\) and open sets \(U_0,\ldots,U_{s-1}\) such that, for each \(j\):

1. \(G_{j+1}=G_j\cup U_j\), and \(G_j=\{\psi_j<c_j\}\) for a smooth strictly plurisubharmonic exhaustion \(\psi_j\) of \(X\);
2. \(U_j\) is a Stein open subset of a resolving ball;
3. \(G_j\cap U_j\) is Stein, and for every compact \(L\subset G_j\cap U_j\) there are a smooth strictly plurisubharmonic exhaustion \(\psi'\) of \(U_j\) and \(b\) with \(L\subset\{\psi'<b\}\) and \(\overline{\{\psi'<b\}}\subset G_j\cap U_j\).

**Proof.** First fix \(c<c'\leq d\) with \(c'-c\leq\varepsilon_0\), where \(\varepsilon_0\) is chosen below. Cover the compact set \(\overline{X_d}\setminus X_c\) by finitely many resolving balls \(A_0,\ldots,A_{s-1}\), with centres \(a_j\) and radii \(r_j\) in their charts, and choose smooth \(\theta_j\geq0\) with compact support in \(A_j\), \(\sum_j\theta_j\leq1\), and \(\sum_j\theta_j=1\) near \(\overline{X_d}\setminus X_c\). By the perturbation lemma Plurisubharmonic functions and Stein manifolds, Lemma 2.4 there is \(\varepsilon_0>0\) such that \(\psi-\sum_j\varepsilon_j\theta_j\) is strictly plurisubharmonic whenever \(0\leq\varepsilon_j\leq\varepsilon_0\). Put \(\varepsilon=c'-c\) and

\[
\psi_j=\psi-\varepsilon\sum_{k<j}\theta_k,\qquad G_j=\{\psi_j<c\}\qquad(0\leq j\leq s).
\]

Each \(\psi_j\) is a strictly plurisubharmonic exhaustion (it differs from \(\psi\) by a bounded function). We have \(G_0=X_c\) and \(G_j\subset G_{j+1}\). Moreover \(G_s=X_{c'}\): where \(\psi<c\) we have \(\psi_s<c\); where \(c\leq\psi<c'\), the point lies in \(\overline{X_d}\setminus X_c\), so \(\psi_s=\psi-\varepsilon<c\); and where \(\psi\geq c'\), \(\psi_s\geq\psi-\varepsilon\geq c\). Since \(\psi_{j+1}-\psi_j=-\varepsilon\theta_j\) is supported in \(A_j\), we get \(G_{j+1}=G_j\cup U_j\) with \(U_j=G_{j+1}\cap A_j\).

\(U_j\) is the intersection of the Stein sets \(G_{j+1}\) (a sublevel set of \(\psi_{j+1}\)) and \(A_j\), so it is Stein, with the exhaustion \(\phi_j=1/(c-\psi_{j+1})+1/(r_j^2-|z-a_j|^2)\); similarly \(G_j\cap U_j=G_j\cap A_j\) is Stein. For (3), let \(L\subset G_j\cap U_j\) be compact, \(a=\max_L\psi_j<c\), and \(a<b<c\). For \(\eta>0\) the function \(\psi'=\psi_j+\eta\phi_j\) is a smooth strictly plurisubharmonic exhaustion of \(U_j\), as \(\psi_j\) is bounded on the relatively compact set \(U_j\). Since \(\phi_j\) is bounded on \(L\), \(L\subset\{\psi'<b\}\) for small \(\eta\). Since \(\phi_j>0\), every point of \(U_j\) with \(\psi'\leq b\) has \(\psi_j\leq b<c\); and \(\{\psi'\leq b\}\) is compact in \(U_j\). So \(\overline{\{\psi'<b\}}\subset G_j\cap U_j\).

For general \(c<d\), apply this to a subdivision \(c=c_0<c_1<\cdots<c_N=d\) with steps at most \(\varepsilon_0\) (the number \(\varepsilon_0\) depends only on the chosen balls and functions for the pair \(c,d\), which may be used for every step), and concatenate. \(\square\)

## 3. Comparison of sublevel sets

**Proposition 3.1.** Let \(c<d\). Then:

1. \(H^k(X_c,\mathcal S)\) is finite-dimensional and Hausdorff for \(k\geq1\);
2. the restriction \(H^k(X_d,\mathcal S)\to H^k(X_c,\mathcal S)\) is bijective for \(k\geq1\);
3. the restriction \(\mathcal S(X_d)\to\mathcal S(X_c)\) has dense image.

**Proof.** *Surjectivity.* Take the sets of Lemma 2.1. Since \(U_j\) and \(G_j\cap U_j\) are Stein open subsets of a resolving ball, \(H^k(U_j,\mathcal S)=H^k(G_j\cap U_j,\mathcal S)=0\) for \(k\geq1\). The Mayer–Vietoris sequence for \(G_{j+1}=G_j\cup U_j\),

\[
\mathcal S(G_j)\oplus\mathcal S(U_j)\to\mathcal S(G_j\cap U_j)\xrightarrow{\ \partial\ }H^1(G_{j+1},\mathcal S)\to H^1(G_j,\mathcal S)\to0\to\cdots\to H^k(G_{j+1},\mathcal S)\to H^k(G_j,\mathcal S)\to0,
\tag{3.1}
\]

shows that \(H^k(G_{j+1},\mathcal S)\to H^k(G_j,\mathcal S)\) is bijective for \(k\geq2\) and surjective for \(k=1\). Composing, \(H^k(X_d,\mathcal S)\to H^k(X_c,\mathcal S)\) is surjective for \(k\geq1\).

*Finiteness.* Choose a Leray covering \(\mathcal V=(V_\alpha)\) of \(X_d\) by Stein open subsets of resolving balls, and finitely many of its members \(V_{\alpha_1},\ldots,V_{\alpha_p}\) together with open \(V'_{\alpha_i}\) with compact closure in \(V_{\alpha_i}\), such that the \(V'_{\alpha_i}\) cover the compact set \(\overline{X_c}\). Let \(\mathcal W\) be a Leray covering of \(X_c\) refining the covering \((V'_{\alpha_i}\cap X_c)\). The refinement map \(C^\bullet(\mathcal V,\mathcal S)\to C^\bullet(\mathcal W,\mathcal S)\) factors through restrictions \(\mathcal S(V_{\alpha_{i_0}\ldots\alpha_{i_k}})\to\mathcal S(V'_{\alpha_{i_0}}\cap\cdots\cap V'_{\alpha_{i_k}})\) between finitely many factors, which are compact by [Fréchet spaces of sections, Proposition 5.2(3)](frechet-spaces-of-sections-and-schwartzs-theorem.md#5-the-topology-on-sections-of-coherent-sheaves); so it is compact in each degree, and it induces the surjection \(H^k(X_d,\mathcal S)\to H^k(X_c,\mathcal S)\). By the finiteness criterion [Fréchet spaces of sections, Theorem 2.2](frechet-spaces-of-sections-and-schwartzs-theorem.md#2-schwartz-s-theorem), \(H^k(X_c,\mathcal S)\) is finite-dimensional and Hausdorff for \(k\geq1\). The same argument applied to the exhaustion \(\psi_j\) shows that each \(H^k(G_j,\mathcal S)\), \(k\geq1\), is Hausdorff.

*Injectivity in degree one and density.* All maps in (3.1) are continuous: computed on Leray coverings refining \(\{G_j,U_j\}\), they are induced by continuous maps of Čech complexes. By Lemma 1.1 and Lemma 2.1(3), \(\mathcal S(U_j)\to\mathcal S(G_j\cap U_j)\) has dense image. The composite of this map with \(\partial\) is zero, and \(H^1(G_{j+1},\mathcal S)\) is Hausdorff, so \(\partial=0\). Hence \(H^1(G_{j+1},\mathcal S)\to H^1(G_j,\mathcal S)\) is injective, and

\[
\mathcal S(G_{j+1})\to\mathcal S(G_j)\oplus\mathcal S(U_j)\xrightarrow{\ (g,u)\mapsto u-g\ }\mathcal S(G_j\cap U_j)\to0
\]

is exact; the last map is open, being a continuous surjection of Fréchet spaces. Given \(g\in\mathcal S(G_j)\), choose \(u_\nu\in\mathcal S(U_j)\) with \(u_\nu|_{G_j\cap U_j}\to g|_{G_j\cap U_j}\). By openness there are \((g'_\nu,u'_\nu)\to0\) with \(u'_\nu-g'_\nu=u_\nu-g\) on \(G_j\cap U_j\). Then \(g-g'_\nu\) and \(u_\nu-u'_\nu\) agree on \(G_j\cap U_j\) and glue to \(f_\nu\in\mathcal S(G_{j+1})\) with \(f_\nu|_{G_j}=g-g'_\nu\to g\). So \(\mathcal S(G_{j+1})\to\mathcal S(G_j)\) has dense image, and composing gives (3). Composing the bijections and injections gives (2). \(\square\)

## 4. Theorem B

**Theorem 4.1 (Cartan's Theorem B).** If \(X\) is a complex manifold with a smooth strictly plurisubharmonic exhaustion, then \(H^k(X,\mathcal S)=0\) for every coherent analytic sheaf \(\mathcal S\) on \(X\) and every \(k\geq1\).

**Proof.** The exhaustion \(\psi\) is bounded below; choose \(c<\inf\psi\), so that \(X_c=\emptyset\). By Proposition 3.1(2), \(H^k(X_d,\mathcal S)\cong H^k(\emptyset,\mathcal S)=0\) for every \(d\) and \(k\geq1\).

Let \(\mathcal W=(W_\alpha)\) be a countable basis of the topology of \(X\) consisting of relatively compact Stein open subsets of resolving balls, and let \(\mathcal W_d\) be the family of those \(W_\alpha\) contained in \(X_d\). Then \(\mathcal W_d\) is a Leray covering of \(X_d\) and \(\mathcal W\) a Leray covering of \(X\) (Section 5 of the lesson on Fréchet spaces of sections). Put \(E^\bullet_\nu=C^\bullet(\mathcal W_{c+\nu},\mathcal S)\), \(\nu\in\mathbf N\). The restriction maps \(E^\bullet_{\nu+1}\to E^\bullet_\nu\) forget factors, so they are surjective; every finite intersection of members of \(\mathcal W\) is relatively compact, hence contained in some \(X_{c+\nu}\), so \(\varprojlim_\nu E^\bullet_\nu=C^\bullet(\mathcal W,\mathcal S)\), whose cohomology is \(H^\bullet(X,\mathcal S)\). For \(k\geq1\), \(H^k(E^\bullet_\nu)=H^k(X_{c+\nu},\mathcal S)=0\), so the maps \(H^k(E_{\nu+1})\to H^k(E_\nu)\) are injective; and the maps \(H^{k-1}(E_{\nu+1})\to H^{k-1}(E_\nu)\) have dense image, trivially for \(k\geq2\) and by Proposition 3.1(3) for \(k=1\). By the abstract Mittag-Leffler theorem [Fréchet spaces of sections, Proposition 3.1(3)](frechet-spaces-of-sections-and-schwartzs-theorem.md#3-an-abstract-mittag-leffler-theorem), \(H^k(X,\mathcal S)\to H^k(E^\bullet_0)=0\) is injective. \(\square\)

*Reference:* the bump argument is due to [Andreotti–Grauert 1962]; the arrangement follows [Demailly]. This theorem is the analytic vanishing theorem used in [Serre's comparison theorems and Chow's theorem, Section 1](course:AG-QC/serres-comparison-theorems-and-chows-theorem), in exactly that generality.

**Corollary 4.2.** \(H^k(V,\mathcal S)=0\) for \(k\geq1\) whenever \(V\) is a Stein open subset of a complex manifold and \(\mathcal S\) is coherent on \(V\). This applies to polydiscs, balls and their finite intersections, to the sets \((\mathbf C^*)^a\times\mathbf C^{n-a}\), to the sublevel sets of strictly plurisubharmonic exhaustions, and to closed submanifolds of Stein manifolds and their products.

**Proof.** Theorem 4.1 and the examples of Plurisubharmonic functions and Stein manifolds, Section 2. \(\square\)

## 5. Theorem A

**Theorem 5.1 (Cartan's Theorem A).** Let \(X\) be a Stein manifold and \(\mathcal S\) a coherent sheaf on \(X\). For every \(x\in X\), the germs at \(x\) of the global sections \(\mathcal S(X)\) generate the stalk \(\mathcal S_x\) as an \(\mathcal O_{X,x}\)-module.

**Proof.** Let \(\mathcal I_x\subset\mathcal O_X\) be the ideal sheaf of the point \(x\), coherent by Cartan's theorem (near \(x\) it is generated by the coordinate functions). The image \(\mathcal I_x\mathcal S\) of \(\mathcal I_x\otimes\mathcal S\to\mathcal S\) is coherent, and \(\mathcal S/\mathcal I_x\mathcal S\) is the skyscraper sheaf at \(x\) with stalk \(\mathcal S_x/\mathfrak m_x\mathcal S_x\). By Theorem 4.1, \(H^1(X,\mathcal I_x\mathcal S)=0\), so \(\mathcal S(X)\to\mathcal S_x/\mathfrak m_x\mathcal S_x\) is surjective. By Nakayama's lemma, elements of \(\mathcal S_x\) whose classes span \(\mathcal S_x/\mathfrak m_x\mathcal S_x\) generate \(\mathcal S_x\). \(\square\)

**Corollary 5.2.** On a Stein manifold \(X\): global holomorphic functions separate points, and at every point some \(n\) global holomorphic functions form local coordinates; for every closed analytic subset \(A\subset X\), every holomorphic function on \(A\) (a section of \(\mathcal O_A\)) extends to a holomorphic function on \(X\); and every coherent sheaf is, on every relatively compact open subset, a quotient of a free sheaf of finite rank.

**Proof.** For \(x\neq y\), apply Theorem 4.1 to the coherent ideal sheaf \(\mathcal I_{\{x,y\}}\): \(\mathcal O(X)\to\mathcal O_X/\mathcal I_{\{x,y\}}\cong\mathbf C_x\oplus\mathbf C_y\) is surjective, so some \(f\) has \(f(x)=0\neq f(y)\). Applying it to \(\mathcal I_x^2\), every element of \(\mathfrak m_x/\mathfrak m_x^2\), in particular a basis, is the differential at \(x\) of a global function. Extension from \(A\): \(H^1(X,\mathcal I_A)=0\) makes \(\mathcal O(X)\to(\mathcal O_X/\mathcal I_A)(X)=\mathcal O_A(A)\) surjective. For the last statement, by Theorem 5.1 and Lemma 1.3 of the lesson on Oka's theorem, each point has a neighbourhood on which finitely many global sections generate \(\mathcal S\); finitely many such neighbourhoods cover a compact closure. \(\square\)

## 6. Exercises

**Exercise 6.1.** Let \(X=(\mathbf C^*)^2\) and \(U_\pm=X\cap\{z_1\neq\pm1\}\). Explain why the Čech group \(\check H^1(\{U_+,U_-\},\mathcal O)\) vanishes, and why Exercise 4.3 of the Dolbeault lesson does not contradict Theorem 4.1.

*Solution.* \(X\) is Stein (Corollary 4.2), so \(H^1(X,\mathcal O)=0\), and for any covering the Čech \(H^1\) injects into \(H^1(X,\mathcal O)\), so it vanishes as well. In the Dolbeault lesson the space was \(\mathbf C^2\setminus\{0\}\), which is not Stein (Exercise 3.2 of the lesson on Stein manifolds); its nonzero \(H^1\) is the obstruction detected by the Laurent coefficient of \(z_1^{-1}z_2^{-1}\).

**Exercise 6.2.** Let \(A=\{z_1z_2=1\}\subset\mathbf C^2\). Use Corollary 5.2 to show that every holomorphic function on \(A\) is the restriction of an entire function on \(\mathbf C^2\), and find such an extension of \(f(z_1,z_2)=z_1^{-1}\) on \(A\).

*Solution.* \(A\) is a closed submanifold of the Stein manifold \(\mathbf C^2\), so Corollary 5.2 applies. On \(A\), \(z_1^{-1}=z_2\), so the polynomial \(z_2\) is an extension.

**Exercise 6.3.** Show in two ways that a compact connected complex manifold of positive dimension is not Stein.

*Solution.* On a compact connected manifold, global holomorphic functions are constant by the maximum principle, so they separate no points, which contradicts Corollary 5.2 if the manifold were Stein. (Directly: a strictly plurisubharmonic function attains a maximum on a compact manifold, and at a maximum its complex Hessian is negative semidefinite in every direction, a contradiction.)

## References

- [Andreotti–Grauert 1962] A. Andreotti and H. Grauert, Théorèmes de finitude pour la cohomologie des espaces complexes, *Bulletin de la Société Mathématique de France* 90 (1962), 193–259. <https://www.numdam.org/item/BSMF_1962__90__193_0/>
- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>
