# Almost periodic functions and the Bohr compactification

**Lesson HA-LCA-16.** Self-checked by the writing AI.

A continuous function can fail to have a period while its translates still form a compact family after taking their uniform closure. The compact group that records all these functions is the Bohr compactification. Its group of characters is familiar; its topology is usually much weaker on the original group. We construct it, prove the uniform approximation theorem, and calculate its invariant mean.

Throughout, \(G\) is an arbitrary locally compact Hausdorff abelian group, \(\Gamma=\widehat G\), and \(L_yf(x)=f(x-y)\). Write \(\Gamma_d\) for the same abstract group with the discrete topology. A trigonometric polynomial on \(G\) is a finite sum \(\sum_\gamma c_\gamma\gamma\) of continuous unit-circle characters. There is no countability assumption on \(G\) or \(\Gamma\).

The free readings are Davalo and Fléchelles, [*Les fonctions presque périodiques*, §§2.1–2.2 and 3.1–3.3](https://www.math.ens.psl.eu/shared-files/9497/?DAVALO_FLECHELLES.pdf=), and Spitters, [*Almost periodic functions, constructively*, §3, exact arXiv revision cs/0512009v3](https://arxiv.org/pdf/cs/0512009v3). We work in classical mathematics. All results needed from these readings are proved below or in the exact earlier programme results cited.

Written and checked by GPT-6 Astra (OpenAI), Ultra, October 2026. The new exposition is released under CC0. Separately linked prerequisite readings and their source packages retain their licences.

## 1. A compact group with all the original characters

<a id="ha-lca-16-theorem-1-1"></a>
**Theorem 1.1 — The Bohr compactification.** The group
\[
 bG=\widehat{\Gamma_d},\qquad
 \beta:G\longrightarrow bG,\qquad \beta(x)(\gamma)=\gamma(x)       \tag{1}
\]
is compact abelian. The map \(\beta\) is a continuous injective homomorphism with dense image. Every continuous homomorphism \(\rho:G\to K\) into a compact Hausdorff group has a unique continuous homomorphism \(\widetilde\rho:bG\to K\) satisfying \(\rho=\widetilde\rho\circ\beta\). The target \(K\) need not be abelian.

**Proof.** Compact/discrete duality, [HA-LCA-02, Theorem 2.1](characters-and-the-dual-group.md#ha-lca-02-theorem-2-1), makes \(bG\) compact. Compact subsets of \(\Gamma_d\) are finite, so its dual topology is precisely pointwise convergence on \(\Gamma\); each coordinate \(x\mapsto\gamma(x)\) is continuous. Formula (1) is a homomorphism, and characters separate points by [HA-LCA-05, Corollary 4.2](raikovs-theorem-and-the-gelfand-raikov-theorem.md#ha-lca-05-corollary-4-2), so it is injective.

By [Pontryagin duality, HA-LCA-09, Theorem 2.1](the-pontryagin-duality-theorem.md#ha-lca-09-theorem-2-1), every character of \(bG\) is evaluation at a unique \(\gamma\in\Gamma_d\). Such a character is one on \(\beta(G)\) exactly when \(\gamma(x)=1\) for every \(x\), that is, when \(\gamma=0\). The double-annihilator formula [HA-LCA-10, Proposition 1.2](subgroups-quotients-and-annihilators.md#ha-lca-10-proposition-1-2) now gives \(\overline{\beta(G)}=bG\).

Let \(H=\overline{\rho(G)}\subset K\). It is a compact subgroup. It is abelian because the commutator map is continuous and is one on the dense subset \(\rho(G)\times\rho(G)\) of \(H\times H\). The pullback
\[
 \widehat H\longrightarrow\Gamma_d,\qquad \chi\longmapsto\chi\circ\rho
\]
is a continuous homomorphism, since \(\widehat H\) is discrete. Dualize it using [HA-LCA-09, Proposition 5.1](the-pontryagin-duality-theorem.md#ha-lca-09-proposition-5-1), and identify \(\widehat{\widehat H}\) with \(H\) by Pontryagin duality. This gives a continuous homomorphism \(bG\to H\). At \(\beta(x)\), its value has \(\chi\)-coordinate \(\chi(\rho(x))\) for every \(\chi\); separation of points identifies that value with \(\rho(x)\). Compose with \(H\subset K\). Two continuous maps from \(bG\) to the Hausdorff space \(K\) that agree on the dense image \(\beta(G)\) agree everywhere: their equalizer is closed. This proves uniqueness. \(\square\)

## 2. The topology of the dense image

A continuous injective map need not be a homeomorphism onto its image. We prove the stronger fact that the image in (1) is proper for every noncompact \(G\).

<a id="ha-lca-16-lemma-2-0"></a>
**Lemma 2.0 — A discontinuous abstract character.** Every nondiscrete LCA group \(E\) admits a group homomorphism \(E\to\mathbb T\) that is not continuous.

**Proof.** The structure theorem [HA-LCA-12, Corollary 4.4](the-structure-of-locally-compact-abelian-groups.md#ha-lca-12-corollary-4-4) writes \(E=\mathbb R^a\times H\), where \(H\) has a compact open subgroup \(K\). The divisible-group extension argument [HA-LCA-12, Lemma 4.1](the-structure-of-locally-compact-abelian-groups.md#ha-lca-12-lemma-4-1) says that an abstract homomorphism from a subgroup into \(\mathbb T\) extends to the whole group. Divisibility here follows from the existence of all circle roots, proved in [HA-LCA-02, Lemma 1.3](characters-and-the-dual-group.md#ha-lca-02-lemma-1-3).

If \(a>0\), define on \(\mathbb Z+\sqrt2\,\mathbb Z\subset\mathbb R\)
\[
 m+n\sqrt2\longmapsto(-1)^n.
\]
The expression is unique because \(\sqrt2\) is irrational: an equality \(r^2=2s^2\) for coprime positive integers would force both \(r,s\) even. Extend to an abstract character \(\theta\) of \(\mathbb R\). A continuous character has the form \(x\mapsto e^{2\pi itx}\), by [HA-LCA-02, Theorem 3.1](characters-and-the-dual-group.md#ha-lca-02-theorem-3-1). Its value at \(1\) forces \(t\in\mathbb Z\), whereas its value at \(\sqrt2\) would force \(t\sqrt2\in\frac12+\mathbb Z\), which is impossible. Thus \(\theta\) is discontinuous. Composing with one coordinate projection gives the required character on \(E\); restriction to that coordinate line proves discontinuity.

Suppose \(a=0\). The compact open \(K\) is infinite: a finite Hausdorff group is discrete, and an open discrete subgroup would make \(E\) discrete. Its discrete dual \(\widehat K\) is infinite by Pontryagin duality. Choose a countably infinite subgroup \(D\subset\widehat K\): recursively choose distinct elements and take their generated subgroup. Restriction of characters gives a continuous surjection
\[
 \pi:K\longrightarrow L=\widehat D
\]
by [HA-LCA-10, Theorem 2.1](subgroups-quotients-and-annihilators.md#ha-lca-10-theorem-2-1). The group \(L\) is infinite compact metrizable by [HA-LCA-12, Theorem 5.1](the-structure-of-locally-compact-abelian-groups.md#ha-lca-12-theorem-5-1); finiteness would imply finiteness of its dual \(D\).

Finite \(1/n\)-nets in \(L\) exist by compactness. Their union is countable and dense, so it generates a countable dense subgroup \(A\). The group \(L\) is uncountable. Indeed, its normalized Haar measure gives the same mass \(c\) to every singleton. Arbitrarily large finite sets imply \(c=0\), and countability of \(L\) would then give total mass zero. Consequently \(A\ne L\).

Choose \(z\notin A\). On the cyclic subgroup generated by \(z+A\) in the abstract quotient \(L/A\), take a character nontrivial at \(z+A\): a primitive root of unity if its order is finite, or the value \(-1\) if its order is infinite. Extend it to \(L/A\) by divisibility and pull it back to \(L\). The resulting \(\theta\) kills the dense subgroup \(A\) but is not identically one, so it cannot be continuous.

A continuous surjection from a compact space to a Hausdorff space is a quotient map: it is closed since compact subsets of a Hausdorff space are closed, as proved in [PRE-RADON, Lemma 1.1](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-1). Hence \(\theta\circ\pi\) is discontinuous on \(K\). Extend this abstract character from \(K\) to \(E\). Its restriction to \(K\) remains discontinuous, completing the proof. \(\square\)

<a id="ha-lca-16-lemma-2-1"></a>
**Lemma 2.1 — Locally compact subgroups.** A subgroup of a Hausdorff topological group that is locally compact in the subspace topology is closed.

**Proof.** Here is the full argument also established in [HA-LCA-09, Lemma 1.2](the-pontryagin-duality-theorem.md#ha-lca-09-lemma-1-2). Let \(B\subset A\) be the subgroup. Choose a compact neighbourhood \(C\) of its identity in \(B\), and an open neighbourhood \(V\) of the identity in \(A\) with \(V\cap B\subset C\). For \(x\in V\cap\overline B\), each neighbourhood of \(x\), intersected with \(V\), meets \(B\); hence \(x\in\overline{V\cap B}\subset C\), because \(C\) is compact and therefore closed in \(A\). Thus \(V\cap\overline B\subset B\), making \(B\) an open subgroup of \(\overline B\). An open subgroup is closed: its complementary cosets are open. As \(B\) is also dense in \(\overline B\), it equals \(\overline B\). \(\square\)

<a id="ha-lca-16-lemma-2-2"></a>
**Lemma 2.2 — The image is proper.** If \(G\) is noncompact, \(\beta(G)\ne bG\).

**Proof.** Its dual \(\Gamma\) is nondiscrete by [HA-LCA-09, Corollary 4.4](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-4). Lemma 2.0 supplies a discontinuous abstract character \(\theta:\Gamma\to\mathbb T\). It is continuous on \(\Gamma_d\), so it is a point of \(bG\). Every \(\beta(x)\), however, is a continuous character of \(\Gamma\), by the evaluation pairing [HA-LCA-09, Lemma 1.1](the-pontryagin-duality-theorem.md#ha-lca-09-lemma-1-1). Thus \(\theta\notin\beta(G)\). \(\square\)

<a id="ha-lca-16-corollary-2-3"></a>
**Corollary 2.3 — The Bohr map is an embedding exactly in the compact case.** If \(G\) is compact, \(\beta:G\to bG\) is a homeomorphism. If \(G\) is noncompact, its dense image is neither open nor locally compact in the subspace topology, and \(\beta\) is not a homeomorphism onto that image.

**Proof.** In the compact case the continuous injection has compact, hence closed, image. Density makes it onto, and a compact-to-Hausdorff continuous bijection is a homeomorphism by the closed-map argument above. In the noncompact case the image is proper and dense. An open subgroup would be closed, and a locally compact subgroup would be closed by Lemma 2.1, each contradicting proper density. If \(\beta\) were a homeomorphism onto its image, that image would inherit the local compactness of \(G\), another contradiction. \(\square\)

## 3. Uniformly almost periodic functions

Give \(C_b(G)\) the uniform norm. A function \(f\in C_b(G)\) is **uniformly almost periodic**, abbreviated \(f\in AP(G)\), when \(\{L_yf:y\in G\}\) has compact closure in that norm.

<a id="ha-lca-16-lemma-3-0"></a>
**Lemma 3.0 — The metric compactness facts.** A complete totally bounded metric space is compact. A compact metric space is complete and totally bounded. The space \(C_b(G)\) is complete.

**Proof.** “Totally bounded” means that for every positive radius finitely many balls cover the space. Given a sequence in such a space, successively select infinitely many of its terms in one ball of radius \(1,1/2,1/3,\ldots\), refining the previous selection. Taking a diagonal subsequence produces a Cauchy sequence, since the diameter at stage \(n\) is at most \(2/n\). Completeness gives a convergent subsequence.

To pass from this property to compactness, let an open cover be given. If no \(\delta>0\) has the property that every ball of radius \(\delta\) is contained in a member of the cover, choose \(x_n\) whose \(1/n\)-ball is contained in no member. A convergent subsequence tends to \(x\) in some open member \(U\). A small ball about \(x\) lies in \(U\), and eventually it contains the \(1/n\)-balls about the selected \(x_n\), a contradiction. Such a \(\delta\) therefore exists, and a finite \(\delta/2\)-net gives a finite subcover.

Compactness itself gives finite radius nets. For a Cauchy sequence in a compact space, the closures of its tails have the finite intersection property, hence a common point. The Cauchy estimate then implies convergence to this point, proving completeness.

Finally, a uniformly Cauchy sequence of bounded continuous functions converges pointwise in the complete field \(\mathbb C\), and its uniform Cauchy estimates give uniform convergence to a bounded function. At any point, approximate the limit within \(\varepsilon\) by one continuous term and use that term's continuity; the resulting \(3\varepsilon\) estimate proves continuity of the limit. \(\square\)

<a id="ha-lca-16-lemma-3-1"></a>
**Lemma 3.1 — A compact isometry group.** For a nonempty compact metric space \((X,d)\), its surjective isometries form a compact topological group for
\[
 D(S,T)=\sup_{x\in X}d(Sx,Tx).                              \tag{2}
\]

**Proof.** This is a finite metric, since compact \(X\) is bounded: a finite unit-ball cover gives a finite bound on distances from any one centre. Composition obeys
\[
 D(ST,S'T')\le D(S,S')+D(T,T'),\qquad
 D(S^{-1},T^{-1})=D(S,T).                                  \tag{3}
\]
For the second identity substitute \(x=Ty\) and apply the isometry \(S\). Thus the group operations are continuous.

A uniformly Cauchy sequence \(T_n\) has a uniform limit \(T:X\to X\) by completeness of \(X\). It preserves distances. Formula (3) shows that \(T_n^{-1}\) also has a uniform limit \(R\). Passing to the limit in the compositions, using the first inequality in (3), gives \(TR=RT=\mathrm{id}\). Hence \(T\) is a surjective isometry, proving completeness.

For total boundedness choose a finite \(\delta\)-net \(x_1,\ldots,x_m\) of \(X\), and for each isometry \(T\) choose a net point within \(\delta\) of each \(Tx_i\). There are only finitely many possible lists of choices. Two isometries with the same list differ by at most \(2\delta\) at each \(x_i\), and by at most \(4\delta\) everywhere, by moving to a nearby \(x_i\). Choosing one isometry for each nonempty list gives a finite \(4\delta\)-net. Lemma 3.0 proves compactness. \(\square\)

<a id="ha-lca-16-theorem-3-2"></a>
**Theorem 3.2 — Three characterizations.** For \(f\in C_b(G)\), the following are equivalent:

1. \(f\in AP(G)\).
2. \(f=F\circ\beta\) for some \(F\in C(bG)\).
3. \(f\) is a uniform limit of trigonometric polynomials.

The \(F\) in (2) is unique. Pullback by \(\beta\) is an isometric unital star-algebra isomorphism \(C(bG)\to AP(G)\). Every almost periodic function is uniformly continuous.

**Proof.** First suppose the translates of \(f\) have compact closure. Choose a finite \(\varepsilon\)-net of this orbit consisting of orbit elements \(g_1,\ldots,g_m\). Continuity at zero gives a neighbourhood \(U\) with
\[
 |g_j(-h)-g_j(0)|<\varepsilon\quad(h\in U,\ 1\le j\le m).
\]
For every \(x\), approximate \(L_{-x}f\) by one \(g_j\). Evaluating at \(-h,0\) yields
\[
 |f(x-h)-f(x)|<3\varepsilon \quad(h\in U,\ x\in G).          \tag{4}
\]
Thus \(f\) is uniformly continuous, and \(y\mapsto L_yf\) is norm continuous.

Let \(X\) be the compact metric closure of its orbit in \(C_b(G)\). The operators \(\rho(x)=L_{-x}|_X\) are surjective isometries. For an orbit element \(g=L_yf\),
\(\|L_{-x}g-g\|_\infty=\|L_{-x}f-f\|_\infty\); passage to a uniform limit gives the same equality for \(g\in X\). In particular
\[
 D(\rho(x),\mathrm{id})=\|L_{-x}f-f\|_\infty.
\]
This tends to zero at the identity by (4), and the group law gives continuity everywhere. Lemma 3.1 makes \(\operatorname{Iso}(X)\) a compact group. Theorem 1.1 extends \(\rho\) to \(\widetilde\rho:bG\to\operatorname{Iso}(X)\). Set
\[
 F(z)=\bigl(\widetilde\rho(z)f\bigr)(0).
\]
Evaluation at \(f\), followed by evaluation at \(0\in G\), is continuous for the metric (2). Hence \(F\) is continuous and \(F(\beta(x))=f(x)\), proving (1)\(\Rightarrow\)(2).

The characters of \(bG\) separate its points. Their linear span contains constants, is closed under products and conjugation, and is uniformly dense in \(C(bG)\) by [complex Stone–Weierstrass, PRE-APPROX, Corollary 2.2](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-corollary-2-2). Each such character is evaluation at some \(\gamma\in\Gamma_d\), whose pullback is \(\gamma\). This proves (2)\(\Rightarrow\)(3).

The translates of \(p=\sum_{j=1}^m c_j\gamma_j\) lie in
\[
 \left\{\sum_{j=1}^m c_j z_j\gamma_j:(z_1,\ldots,z_m)\in\mathbb T^m\right\},
\]
a compact set by continuity and finite compact products. If \(\|f-p\|_\infty<\varepsilon\), every translate of \(f\) is within \(\varepsilon\) of the corresponding translate of \(p\). Finite nets for the latter show that the orbit of \(f\) is totally bounded. Its closure in the complete space \(C_b(G)\) is complete and totally bounded, so Lemma 3.0 makes it compact. This proves (3)\(\Rightarrow\)(1).

Density of \(\beta(G)\) gives uniqueness and
\(\|F\circ\beta\|_\infty=\|F\|_\infty\). Pullback preserves sums, products, conjugation and the constant one, so it is the asserted isomorphism. Its range is closed: a Cauchy sequence in the range lifts isometrically to a Cauchy sequence in the complete space \(C(bG)\). \(\square\)

<a id="ha-lca-16-proposition-3-3"></a>
**Proposition 3.3 — The Gelfand space.** The character space of the unital commutative Banach algebra \(AP(G)\) is canonically \(bG\). Under this identification evaluation at \(x\in G\) corresponds to \(\beta(x)\), and the Gelfand transform sends \(f=F\circ\beta\) to \(F\).

**Proof.** We first prove that every character of \(C(K)\), for a compact Hausdorff space \(K\), is evaluation at a point. Let \(\ell\) be a nonzero multiplicative complex linear functional. Then \(\ell(1)=1\). If the functions in its kernel had no common zero, compactness would give \(F_1,\ldots,F_m\in\ker\ell\) with
\(h=\sum_j|F_j|^2>0\) everywhere. Since \(1/h\) is continuous,
\[
 1=\sum_{j=1}^m F_j\,\frac{\overline{F_j}}h
\]
would belong to the ideal \(\ker\ell\), a contradiction. There is therefore \(z\in K\) where every member of \(\ker\ell\) vanishes. Since \(F-\ell(F)1\in\ker\ell\), we have \(\ell(F)=F(z)\). Such \(z\) is unique because continuous functions separate points by [PRE-RADON, Lemma 1.2](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-2).

The evaluation map from \(K\) to the character space is continuous in the pointwise topology, since each coordinate is a continuous function on \(K\). The character space is Hausdorff, as also proved in [PRE-BANACH, Theorem 4.2](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-4-2). This continuous bijection is a homeomorphism by compactness and the closed-map argument of Lemma 2.0. Apply this to \(K=bG\), and use the isomorphism in Theorem 3.2. Evaluation of \(F\circ\beta\) at \(x\) is exactly \(F(\beta(x))\), proving both final assertions. \(\square\)

<a id="ha-lca-16-proposition-3-4"></a>
**Proposition 3.4 — The compact metric group of one function.** For \(f\in AP(G)\), put
\[
 d_f(a,b)=\sup_{t\in G}|f(t+a)-f(t+b)|,\qquad
 N_f=\{a:d_f(a,0)=0\}.                                    \tag{5}
\]
This translation-invariant pseudometric induces a metric on \(G/N_f\). Its metric completion \(K_f\) is a compact metrizable abelian group. The canonical map \(j_f:G\to K_f\) is a continuous homomorphism with dense image, and
\[
 f=F_f\circ j_f
\]
for a continuous function \(F_f\) on \(K_f\). A continuous surjective homomorphism \(bG\to K_f\) intertwines \(\beta\) and \(j_f\).

The topology used to complete \(G/N_f\) is the metric topology from (5); it need not equal its topology as a quotient of the original \(G\).

**Proof.** The triangle inequality and translation invariance of \(d_f\) follow directly from the uniform norm and substitution in the supremum. They show that \(N_f\) is a subgroup and that changing either argument by an element of \(N_f\) leaves (5) unchanged. Distance zero in the resulting quotient occurs only for equal cosets.

Map \(a+N_f\) to the function \(T_af\), where \(T_af(t)=f(t+a)\). This is an isometry onto the translation orbit. Its closure \(X\) in \(C_b(G)\) is compact by almost periodicity, and complete by Lemma 3.0. Every point in the closure is the limit of a sequence of orbit elements, by choosing an element at distance less than \(1/n\). Thus \(X\) is a metric completion; we take it as \(K_f\).

On the dense quotient the group operations satisfy
\[
 d_f(a+b,c+d)\le d_f(a,c)+d_f(b,d),\qquad
 d_f(-a,-b)=d_f(a,b).                                     \tag{6}
\]
For two points of \(X\), choose Cauchy sequences \(a_n+N_f,b_n+N_f\) tending to them and define their sum as the limit of \(a_n+b_n+N_f\). Inequality (6) makes that sequence Cauchy and shows that its limit is independent of both choices. The same construction defines inversion. Passing to limits in (6) proves continuity; passing to limits in the group identities proves associativity, commutativity, the identity and the inverse identities. Hence \(K_f\) is a compact metric abelian group.

The map \(j_f\) is continuous since
\(d_f(a+h,a)=\|T_hf-f\|_\infty\to0\), by the uniform continuity in Theorem 3.2. Evaluation at \(0\), namely \(F_f(g)=g(0)\) on \(X\), is \(1\)-Lipschitz for its uniform metric and satisfies \(F_f(j_f(a))=f(a)\). Finally Theorem 1.1 extends \(j_f\) to a continuous homomorphism \(bG\to K_f\). Its compact image is closed and contains the dense set \(j_f(G)\), so it is onto. \(\square\)

## 4. Mean, coefficients, and equidistribution

Normalize Haar measure on \(bG\) to mass one. For \(f=F\circ\beta\) define
\[
 M(f)=\int_{bG}F(z)\,dz,\qquad
 a_\gamma(f)=M(f\overline\gamma).                          \tag{7}
\]

<a id="ha-lca-16-proposition-4-1"></a>
**Proposition 4.1 — Mean and Parseval.** The functional \(M\) is positive, bounded of norm one, and invariant under all translations of \(G\). It is the unique bounded linear functional on \(AP(G)\) with translation invariance and \(M(1)=1\). Moreover
\[
 M(|f|^2)=\sum_{\gamma\in\Gamma}|a_\gamma(f)|^2,             \tag{8}
\]
where the sum means the supremum of sums over finite subsets. Only countably many of the coefficients are nonzero. If \(G=\mathbb R\), then
\[
 \lim_{T\to\infty}\ \sup_{s\in\mathbb R}
 \left|\frac1{2T}\int_{s-T}^{s+T}f(x)\,dx-M(f)\right|=0.    \tag{9}
\]

**Proof.** Haar measure and its normalization are proved in [PRE-HAAR, Theorems 2.2, 3.1 and 4.1](../prerequisites/src/haar-measure.md). Positivity, \(|M(f)|\le\|f\|_\infty\), and \(M(1)=1\) give the norm assertion. Translation of \(f\) corresponds to translation of \(F\) by \(\beta(y)\); Haar invariance gives invariance of \(M\).

If \(\ell\) is another such functional and \(\gamma\ne1\), choose \(y\) with \(\gamma(y)\ne1\). Since \(L_y\gamma=\overline{\gamma(y)}\gamma\), invariance gives
\((1-\overline{\gamma(y)})\ell(\gamma)=0\). Thus \(\ell(\gamma)=0\). The same holds for \(M\), and both give value one at the trivial character. They agree on all trigonometric polynomials and then on \(AP(G)\) by boundedness and Theorem 3.2.

The characters of the compact group \(bG\), indexed by \(\Gamma_d\), are an orthonormal basis of \(L^2(bG)\), by [HA-LCA-08, Corollary 4.1](the-plancherel-theorem.md#ha-lca-08-corollary-4-1). The coefficient of \(F\) at evaluation by \(\gamma\) is exactly (7). The arbitrary-index Parseval identity [PRE-HILBERT, Theorem 4.2](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-4-2) proves (8). For each \(n\), only finitely many coefficients can have modulus at least \(1/n\), since otherwise the finite sums in (8) would be unbounded. Their union over \(n\) contains every nonzero coefficient.

On \(\mathbb R\), a character is \(\gamma_\lambda(x)=e^{2\pi i\lambda x}\) by HA-LCA-02, Theorem 3.1. For \(\lambda\ne0\), direct integration gives
\[
 \frac1{2T}\int_{s-T}^{s+T}\gamma_\lambda(x)\,dx
 =e^{2\pi i\lambda s}\frac{\sin(2\pi\lambda T)}{2\pi\lambda T}. \tag{10}
\]
The fundamental theorem for this calculation is [PRE-REAL, Lemmas 1.1 and 1.3](../prerequisites/src/real-variable-calculations.md). The right side tends to zero uniformly in \(s\); the trivial character has average one. Thus (9) holds for polynomials. Given \(\varepsilon>0\), choose a polynomial \(p\) with \(\|f-p\|_\infty<\varepsilon\). Both an interval average and \(M\) have norm at most one, so the error for \(f\) is at most \(2\varepsilon\) plus the uniform error for \(p\). This proves (9). \(\square\)

Parseval is an \(L^2\) assertion on \(bG\). Theorem 3.2 separately provides uniform polynomial approximation. No assertion about uniform convergence of arbitrary Fourier partial sums is needed.

For a compact abelian group \(K\), a sequence \(z_n\) is **equidistributed** if
\[
 \frac1N\sum_{n=0}^{N-1}\varphi(z_n)\longrightarrow
 \int_K\varphi\,dm_K \quad\text{for every }\varphi\in C(K),
\]
where \(m_K(K)=1\).

<a id="ha-lca-16-lemma-4-2"></a>
**Lemma 4.2 — Character criterion.** A sequence in \(K\) is equidistributed exactly when
\[
 \frac1N\sum_{n=0}^{N-1}\chi(z_n)\longrightarrow0
 \quad\text{for every nontrivial }\chi\in\widehat K.         \tag{11}
\]

**Proof.** A nontrivial character has Haar integral zero: translation by a point where its value is not one multiplies the integral by that value and also leaves it unchanged. This proves necessity. Conversely (11), together with the constant character's average one, proves the desired limit for every character polynomial. Characters separate points by HA-LCA-05, Corollary 4.2, and their algebra is uniformly dense in \(C(K)\) by PRE-APPROX, Corollary 2.2. Approximate \(\varphi\) uniformly within \(\varepsilon\); the empirical average and Haar integral each have norm one, so the total error is at most \(2\varepsilon\) plus the polynomial error. Letting \(\varepsilon\) decrease proves sufficiency. \(\square\)

<a id="ha-lca-16-proposition-4-3"></a>
**Proposition 4.3 — Uniform rotation averages.** Let \(a\in K\), with \(K\) compact abelian, and \(H=\overline{\mathbb Za}\). Then for every \(\varphi\in C(K)\),
\[
 \frac1N\sum_{n=0}^{N-1}\varphi(z+na)
 \longrightarrow \int_H\varphi(z+h)\,dm_H(h)
 \quad\text{uniformly for }z\in K.                        \tag{12}
\]
The sequence \(na\) is equidistributed in \(H\). On \(K=\mathbb R^d/\mathbb Z^d\), the sequence \(n\alpha+\mathbb Z^d\) is equidistributed in \(K\) exactly when
\[
 k\cdot\alpha\notin\mathbb Z
 \quad\text{for every }0\ne k\in\mathbb Z^d.               \tag{13}
\]

**Proof.** For \(\varphi=\chi\in\widehat K\), the average is
\(\chi(z)N^{-1}\sum_{n=0}^{N-1}\chi(a)^n\). If \(\chi(a)=1\), the character is one on \(H\) by density and both sides of (12) equal \(\chi(z)\). Otherwise the geometric-sum identity bounds the average by
\[
 \frac{2}{N|1-\chi(a)|},
\]
uniformly in \(z\), whereas the Haar integral on the right is zero. Linear combinations and uniform polynomial approximation prove (12), using again the norm-one bounds for the two averaging maps.

Apply the same argument directly on \(H\): a nontrivial character of \(H\) cannot be one at \(a\), since its kernel is closed and would then contain the dense cyclic subgroup. Lemma 4.2 proves equidistribution in \(H\). This does not require extending a continuous test function from \(H\) to \(K\).

The torus characters are \(x+\mathbb Z^d\mapsto e^{2\pi i k\cdot x}\), by [HA-LCA-02, Corollary 4.2](characters-and-the-dual-group.md#ha-lca-02-corollary-4-2). Formula (11) and the geometric sum prove sufficiency of (13). If (13) fails for a nonzero \(k\), the corresponding nontrivial character has value one at every \(n\alpha\); its average cannot tend to its Haar integral zero. This proves necessity. Equivalently, the double-annihilator formula identifies (13) with \(\overline{\mathbb Z(\alpha+\mathbb Z^d)}=K\). \(\square\)

## 5. Three examples

<a id="ha-lca-16-example-5-1"></a>
**Example 5.1 — Almost periodic without a period.** The function
\[
 f(x)=\sin x+\sin(\sqrt2\,x)
\]
is almost periodic on \(\mathbb R\), but its only period is zero.

**Proof.** It is a linear combination of the four distinct characters \(e^{ix},e^{-ix},e^{i\sqrt2x},e^{-i\sqrt2x}\), so Theorem 3.2 applies. Distinct characters have mean inner product zero by Proposition 4.1. If \(f(x+T)=f(x)\) for all \(x\), multiply the difference by each conjugate character and take its mean. Every nonzero coefficient then forces \(e^{iT}=e^{i\sqrt2T}=1\). Thus \(T=2\pi m\) and \(\sqrt2T=2\pi n\) for integers \(m,n\). Irrationality of \(\sqrt2\), proved in Lemma 2.0, forces \(m=n=0\). The same orthogonality gives \(M(f)=0\) and \(M(|f|^2)=4\cdot(1/2)^2=1\). \(\square\)

<a id="ha-lca-16-example-5-2"></a>
**Example 5.2 — The Bohr compactification of the integers.** One has
\[
 b\mathbb Z=\widehat{\mathbb T_d},\qquad
 \beta(n)(z)=z^n.
\]
It is a nonmetrizable compact group with a countable proper dense subgroup.

**Proof.** The dual of \(\mathbb Z\) is \(\mathbb T\), by [HA-LCA-02, Corollary 3.2](characters-and-the-dual-group.md#ha-lca-02-corollary-3-2). Formula (1) gives the asserted group and map. Density follows from Theorem 1.1; properness follows from Lemma 2.2 because \(\mathbb Z\) is noncompact. The dual of \(b\mathbb Z\) is the uncountable discrete group \(\mathbb T_d\), by Pontryagin duality. The uncountability follows already from the injective parametrization of any real interval of length less than one by \(t\mapsto e^{2\pi it}\), using the real uncountability argument in [HA-LCA-10, Example 6.3](subgroups-quotients-and-annihilators.md#ha-lca-10-example-6-3). A compact abelian group is metrizable exactly when its dual is countable, by HA-LCA-12, Theorem 5.1. Thus \(b\mathbb Z\) is not metrizable. \(\square\)

<a id="ha-lca-16-example-5-3"></a>
**Example 5.3 — Bounded continuity is insufficient.** The function \(g(x)=\sin(x^2)\) is not almost periodic.

**Proof.** Let
\[
 x_n=\sqrt{2\pi n+\pi/2},\qquad
 y_n=\sqrt{2\pi n+3\pi/2}.
\]
Then \(g(x_n)=1\), \(g(y_n)=-1\), but
\[
 |y_n-x_n|=\frac{\pi}{y_n+x_n}\longrightarrow0.
\]
Thus \(g\) is not uniformly continuous. Every almost periodic function is uniformly continuous by Theorem 3.2. \(\square\)

## 6. Exercises with solutions

<a id="ha-lca-16-exercise-6-1"></a>
**Exercise 6.1.** Prove that the product of two almost periodic functions is almost periodic.

**Solution.** Write \(f=F\circ\beta\) and \(g=H\circ\beta\), using Theorem 3.2. Then \(fg=(FH)\circ\beta\), and \(FH\in C(bG)\). The same theorem gives \(fg\in AP(G)\). Directly from polynomial approximation, if \(p_n\to f\) and \(q_n\to g\) uniformly, then the polynomial products satisfy
\[
 \|p_nq_n-fg\|_\infty
 \le\|p_n\|_\infty\|q_n-g\|_\infty
     +\|p_n-f\|_\infty\|g\|_\infty\longrightarrow0,
\]
since the uniformly convergent \(p_n\) are uniformly bounded. This also proves the claim. \(\square\)

<a id="ha-lca-16-exercise-6-2"></a>
**Exercise 6.2.** Prove that \(\sin(x^2)\) is not almost periodic.

**Solution.** The points \(x_n,y_n\) of Example 5.3 have distance tending to zero and function-value difference two. To see explicitly why this contradicts almost periodicity, a finite \(\varepsilon\)-net of translates, with \(\varepsilon=1/4\), and continuity of those finitely many functions at zero give (4), so all sufficiently small increments change the function by less than \(3/4\), uniformly in the base point. Taking the increment \(y_n-x_n\) at \(x_n\) contradicts the difference two. \(\square\)

<a id="ha-lca-16-exercise-6-3"></a>
**Exercise 6.3.** If \(G\) is noncompact, prove that \(\beta(G)\) is not open and that \(\beta\) is not a homeomorphism onto its image.

**Solution.** The dual \(\Gamma\) is nondiscrete. Lemma 2.0 supplies a discontinuous abstract character of \(\Gamma\), which is a point of \(bG\) outside \(\beta(G)\). Hence \(\beta(G)\) is proper, while Theorem 1.1 makes it dense. An open subgroup is closed because its complementary cosets are open, so \(\beta(G)\) cannot be open. If \(\beta\) were a homeomorphism onto its image, that image would be a locally compact subgroup of \(bG\), and Lemma 2.1 would make it closed. This again contradicts proper density. The proper-image argument is essential to this proof. \(\square\)

<a id="ha-lca-16-exercise-6-4"></a>
**Exercise 6.4.** For \(f\in AP(\mathbb R)\), prove that its symmetric interval averages converge to \(M(f)\), and prove
\(M(|f|^2)=\sum_\gamma|M(f\overline\gamma)|^2\).

**Solution.** For a polynomial \(p=\sum_\lambda c_\lambda e^{2\pi i\lambda x}\), formula (10) with \(s=0\) shows that its interval average tends to \(c_0\), which equals \(M(p)\). Given \(\varepsilon>0\), choose \(\|f-p\|_\infty<\varepsilon\). The difference between the average of \(f\) and \(M(f)\) has limit superior at most \(2\varepsilon\), by the norm-one bounds on both averages; letting \(\varepsilon\to0\) proves the limit.

Lift \(f\) to \(F\in C(b\mathbb R)\). Its inner product with the character \(z\mapsto z(\gamma)\) is \(M(f\overline\gamma)\), while \(\|F\|_2^2=M(|f|^2)\). The orthonormal basis theorem HA-LCA-08, Corollary 4.1, and the arbitrary-index Parseval theorem PRE-HILBERT, Theorem 4.2, give the displayed identity. The sum is the supremum over finite subsets, so it is meaningful even though \(\widehat{\mathbb R}\) is uncountable. The finite-level-set argument in Proposition 4.1 shows that only countably many terms are nonzero. \(\square\)

