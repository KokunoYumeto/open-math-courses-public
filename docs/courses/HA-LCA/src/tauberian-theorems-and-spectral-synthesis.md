# Tauberian theorems and spectral synthesis

**Lesson HA-LCA-15.** Self-checked by the writing AI.

A single convolution average can determine the limits of all convolution averages. It need not determine a bounded function pointwise without a regularity condition. A related question asks whether the common zeros of a closed convolution ideal determine the ideal. We prove a useful positive criterion, then construct failures on spheres and on every nondiscrete frequency group.

Throughout, \(G\) is an arbitrary locally compact Hausdorff abelian group, \(\Gamma=\widehat G\), and
\[
 \widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,dx,\qquad
 L_yf(x)=f(x-y).
\]
Both groups are written additively. Write \(A(\Gamma)=\widehat{L^1(G)}\), with \(\|\widehat f\|_A=\|f\|_1\). Fourier uniqueness makes this an isometric Banach algebra. We use the [local units, local division, finite patching and Wiener theorem in HA-LCA-14](closed-ideals-of-l1-g-and-wieners-theorem.md), with exact locators below.

The free readings are Shu's [1974 thesis](https://digital.library.unt.edu/ark:/67531/metadc663188/m2/1/high_res_d/1002773742-Shu.pdf), Theorems 2.23–2.26; Fulsche, Luef and Werner's [arXiv:2405.08678v2](https://arxiv.org/pdf/2405.08678v2), Theorems 2.2–2.5, 4.1 and 4.9; Schwartz's [1951 paper, §§13–15](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/61696D1072603F9C186EFF0C4CD074BB/S0008414X00031217a.pdf/analyse-et-synthese-harmoniques-dans-les-espaces-de-distributions.pdf); Malliavin's [1959 paper, §§1–6](https://www.numdam.org/item/10.1007/BF02684707.pdf); and Melrose's [Spring 2016 functional-analysis notes, Chapter 1, §12](https://math.mit.edu/~rbm/18-102-Sp16/Chapter1.pdf). All mathematical inputs from these readings are proved here or supplied by exact earlier programme proofs.

Written and checked by GPT-6 Astra (OpenAI), Ultra, October 2026. The new exposition is released under CC0. Separately linked prerequisite readings and their source packages retain their licences.

## 0. The separation statements we will need

For a complex normed space \(E\), the weak-star topology on \(E^*\) is pointwise convergence on \(E\). For \(M\subset E\) and \(J\subset E^*\), write
\[
 M^\perp=\{\ell:\ell|_M=0\},\qquad
 {}^\perp J=\{x:\ell(x)=0\text{ for all }\ell\in J\}.
\]

<a id="ha-lca-15-lemma-0-1"></a>
**Lemma 0.1 — Extension and double annihilators.** A bounded complex linear functional on a subspace extends to the whole normed space with the same norm. Consequently
\[
 {}^\perp(M^\perp)=\overline M
 \quad\text{for a linear }M\subset E,\qquad
 ({}^\perp J)^\perp=\overline J^{\,w^*}
 \quad\text{for a linear }J\subset E^*.                    \tag{1}
\]

**Proof.** First consider a real linear functional \(r\) on a real subspace \(V\), with \(|r(v)|\le C\|v\|\). For \(x\notin V\), an extension with value \(a\) at \(x\) exists precisely when
\[
 \sup_{v\in V}\{r(v)-C\|v-x\|\}
 \le a\le
 \inf_{w\in V}\{C\|w+x\|-r(w)\}.
\]
The left terms do not exceed the right terms: \(r(v)+r(w)\le C\|v+w\|\le C\|v-x\|+C\|w+x\|\). Both bounds are finite, by taking one test vector to be zero. Choose \(a\) between them. These inequalities give \(|r(v)+ta|\le C\|v+tx\|\) for \(t=1,-1\), and then for all real \(t\ne0\) by rescaling \(v\); \(t=0\) is the original bound. Thus \(r(v+tx)=r(v)+ta\) is an admissible extension. For \(C=0\), simply use the zero functional.

Order all such extensions by restriction. A chain has the consistent functional on the union of its domains as an upper bound: any two vectors lie together in some member of the chain. Zorn's lemma, in our set-theoretic basis with choice, gives a maximal extension, and the one-dimensional step shows its domain is the whole underlying real space.

For a complex functional \(\ell\), extend \(r=\operatorname{Re}\ell\) in this way, and set \(L(x)=r(x)-i r(ix)\). Real linearity and \(L(ix)=iL(x)\) give complex linearity; on the original complex subspace this equals \(\ell\). Choose a scalar \(\zeta\) of modulus one with \(\zeta L(x)=|L(x)|\). Then
\(|L(x)|=r(\zeta x)\le C\|x\|\).
The extension therefore preserves the norm.

For the first equality in (1), replace \(M\) by its closure. On \(E/M\) define \(\|x+M\|=\inf_{m\in M}\|x-m\|\). Translation by an element of \(M\) leaves the infimum unchanged; homogeneity follows by rescaling \(M\), and the triangle inequality follows by adding two approximating elements of \(M\). If this infimum is zero, closedness gives \(x\in M\). Thus it is a norm, and if \(x\notin M\) then \(\|x+M\|>0\). The functional taking \(z(x+M)\) to \(z\) is bounded on that one-dimensional subspace. Extend it and compose with the contractive quotient map. It annihilates \(M\) but not \(x\).

For the second equality, assume \(J\) is weak-star closed and \(\ell_0\notin J\). A basic neighbourhood disjoint from \(J\) tests finitely many \(x_1,\ldots,x_m\in E\). Let \(T\ell=(\ell(x_1),\ldots,\ell(x_m))\). The linear subspace \(T(J)\subset\mathbb C^m\) is closed. To see this directly, choose an orthonormal basis for this finite-dimensional subspace by successive orthogonal projection; convergence of coordinates shows that limits stay in its span. The forbidden neighbourhood implies \(T\ell_0\notin T(J)\). Orthogonally projecting \(T\ell_0\) onto \(T(J)^\perp\) gives a complex linear functional on \(\mathbb C^m\) which vanishes on \(T(J)\) but not at \(T\ell_0\). Write it as \(z\mapsto\sum c_jz_j\). Then \(x=\sum c_jx_j\) belongs to \({}^\perp J\), while \(\ell_0(x)\ne0\). The same argument applied to the weak-star closure proves the general statement. The finite-dimensional orthogonal projection used here is a case of [Hilbert Corollary 2.2](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-corollary-2-2). \(\square\)

## 1. Limits of convolution averages

A bounded function tends to \(a\) **at infinity** if, for each \(\varepsilon>0\), it differs from \(a\) by less than \(\varepsilon\) outside a compact set. On a compact group this condition is vacuous. All claims below retain that convention.

<a id="ha-lca-15-lemma-1-0"></a>
**Lemma 1.0 — Bounded convolution.** For \(g\in L^1(G)\) and \(\phi\in L^\infty(G)\), convolution has a canonical bounded uniformly continuous representative and
\[
 \|g*\phi\|_\infty\le\|g\|_1\|\phi\|_\infty,\qquad
 \|L_y(g*\phi)-g*\phi\|_\infty
 \le\|L_yg-g\|_1\|\phi\|_\infty.                           \tag{2}
\]
Moreover \(h*(g*\phi)=(h*g)*\phi\). If \(\phi\) is bounded uniformly continuous, positive compactly supported mass-one approximate identities satisfy \(\psi_U*\phi\to\phi\) uniformly.

**Proof.** Choose a representative bounded everywhere by \(\|\phi\|_\infty\), modifying a null set. The integral \(\int g(t)\phi(x-t)\,dt\) exists for each \(x\), is independent of these modifications, and has the first bound: translations and inversion preserve Haar null sets. Substitution rewrites it as \(\int g(x-t)\phi(t)\,dt\), and gives the second bound. Norm continuity of translations on \(L^1\), proved in [Haar Lemma 6.1](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-lemma-6-1), now proves uniform continuity. Different representatives give the same continuous function.

Associativity follows by Fubini, since the absolute double integral is bounded by \(\|h\|_1\|g\|_1\|\phi\|_\infty\). More explicitly, choose the Borel representatives of \(g,h\) supported on open sigma-compact subgroups as in [Integration Theorem 3.1](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-3-1). A single open sigma-compact subgroup contains both supports. For each fixed \(x\), restrict \(\phi\) to its relevant coset, choose a Borel representative there, and apply the [sigma-finite full-Borel Fubini theorem](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-4-4). This also justifies the substitutions without assuming that \(G\) is sigma-compact.

Finally
\[
 |(\psi_U*\phi)(x)-\phi(x)|
 \le\sup_{t\in U}|\phi(x-t)-\phi(x)|
\]
when \(\psi_U\ge0\), \(\int\psi_U=1\), and \(\operatorname{supp}\psi_U\subset U\). Such kernels are supplied by [Haar Corollary 6.3](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-corollary-6-3), and uniform continuity makes the bound tend to zero. \(\square\)

A specified bounded measurable representative \(\phi\) is **slowly oscillating** if, for every \(\varepsilon>0\), there are a compact set \(K\) and a neighbourhood \(U\) of zero such that
\[
 |\phi(x-t)-\phi(x)|<\varepsilon
 \quad(x\notin K,\ t\in U).                               \tag{3}
\]
This is a condition on that representative, not merely its almost-everywhere class.

<a id="ha-lca-15-theorem-1-1"></a>
**Theorem 1.1 — Wiener–Pitt.** Suppose \(\int f=1\), \(\widehat f\) is nowhere zero, and \(f*\phi(x)\to a\) at infinity, where \(f\in L^1(G)\) and \(\phi\in L^\infty(G)\). Then
\[
 g*\phi(x)\longrightarrow a\int_G g
 \quad\text{for every }g\in L^1(G).                       \tag{4}
\]
If the specified representative of \(\phi\) is slowly oscillating, then \(\phi(x)\to a\).

**Proof.** The kernels satisfying (4) form a linear subspace \(M\). It is closed: for \(g_n\to g\) in \(L^1\), the difference between the corresponding expressions \(g*\phi-a\int g\) has uniform norm at most
\((\|\phi\|_\infty+|a|)\|g-g_n\|_1\).
Uniform limits of functions tending to zero at infinity also tend to zero, by first making this uniform error small and then using the compact exceptional set for one approximant.

The subspace is translation invariant because
\((L_yg)*\phi(x)=(g*\phi)(x-y)\) and \(\int L_yg=\int g\). Translating a compact exceptional set remains compact. Since \(f\in M\), the [\(L^1\) translate criterion, HA-LCA-14, Corollary 7.1](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-corollary-7-1), gives \(M=L^1(G)\).

For slow oscillation, choose \(K,U\) in (3) and a nonnegative mass-one kernel \(\psi\) supported in \(U\). Outside \(K\), \(|\phi-\psi*\phi|\le\varepsilon\); by (4), \(\psi*\phi\to a\). Thus outside a larger compact set \(|\phi-a|\le2\varepsilon\). \(\square\)

Call \(S\subset L^1(G)\) **regular** when its Fourier transforms have no common zero.

<a id="ha-lca-15-theorem-1-2"></a>
**Theorem 1.2 — Transfer to a closed translation space.** Let \(D\) be a norm-closed translation-invariant linear subspace of \(\operatorname{BUC}(G)\), and let \(S\subset L^1(G)\) be regular. If
\[
 s*\phi-a\int s\in D\quad(s\in S),
\]
the same holds for every \(s\in L^1(G)\). If \(\phi\in\operatorname{BUC}(G)\), these assertions are equivalent to \(\phi-a\in D\).

**Proof.** The inverse image of \(D\) under the bounded linear map
\(g\mapsto g*(\phi-a)\) is a closed translation-invariant subspace of \(L^1\), by Lemma 1.0. It contains \(S\). The closed span \(V\) of all translates of \(S\) is an ideal by [HA-LCA-14, Proposition 1.1](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-proposition-1-1). Its hull is the common zero set of \(S\): one inclusion follows from the Fourier translation formula and continuity, and the other from \(S\subset V\). Thus its hull is empty, and [HA-LCA-14, Theorem 5.3](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-theorem-5-3) gives \(V=L^1\).

For \(\phi\in\operatorname{BUC}\), the approximate identities in Lemma 1.0 imply \(\psi_U*(\phi-a)\to\phi-a\) uniformly, so membership of all convolutions in \(D\) implies \(\phi-a\in D\). Conversely, convolution of a member \(b\in D\) with \(g\in L^1\) stays in \(D\). For \(g\in C_c\), approximate the integral \(\int g(t)L_tb\,dt\) in uniform norm by finite sums: cover \(\operatorname{supp}g\) by finitely many translates of a neighbourhood on which \(\|L_tb-b\|_\infty<\varepsilon\), partition the support into Borel pieces, and integrate \(g\) over each piece. The error is at most \(\varepsilon\|g\|_1\). For general \(g\), use \(C_c\) density and (2). Closedness of \(D\) proves the converse. \(\square\)

<a id="ha-lca-15-theorem-1-3"></a>
**Theorem 1.3 — Uniform transfer.** Let \(S\) be regular, \(X\subset L^\infty(G)\) bounded in norm, and \(H\subset L^1(G)\) relatively compact in norm. If
\[
 \sup_{\phi\in X}|s*\phi(x)|\longrightarrow0
 \quad(s\in S),
\]
then
\[
 \sup_{h\in H}\sup_{\phi\in X}|h*\phi(x)|
 \longrightarrow0.                                     \tag{5}
\]
An empty supremum is zero.

**Proof.** Put \(C=\sup_{\phi\in X}\|\phi\|_\infty<\infty\). The hypothesis persists under translation and finite linear combinations of kernels: translate the finitely many compact exceptional sets and take their union. The preceding proof shows that the span \(V\) of those translates is dense in \(L^1\). Given \(\delta>0\), compactness of \(\overline H\) and density give finitely many \(v_1,\ldots,v_m\in V\) such that every \(h\in H\) has \(\|h-v_j\|_1<\delta\) for some \(j\). By (2),
\[
 \sup_{h\in H,\phi\in X}|h*\phi(x)|
 \le C\delta+\max_{1\le j\le m}\sup_{\phi\in X}|v_j*\phi(x)|.
\]
Outside a compact set the last term is arbitrarily small. Then let \(\delta\downarrow0\). The empty cases and \(C=0\) are immediate. \(\square\)

For a window \(h\in L^1(G)\), define the short-time Fourier expression with the following precise convention:
\[
 V_h\phi(x,\chi)
   =\int_G\phi(t)\overline{h(t-x)}\,\overline{\chi(t)}\,dt.
                                                               \tag{6}
\]
It exists for every \(x,\chi\). Put \(h^\sharp(y)=\overline{h(-y)}\). Substitution gives
\[
 V_h\phi(x,\chi)=\overline{\chi(x)}
                     \bigl((\chi h^\sharp)*\phi\bigr)(x). \tag{7}
\]

<a id="ha-lca-15-corollary-1-4"></a>
**Corollary 1.4 — Window criterion.** For \(\phi\in L^\infty(G)\), these are equivalent:

1. \(g*\phi\in C_0(G)\) for every \(g\in L^1(G)\).
2. For some nonzero \(h\in L^1(G)\), \(V_h\phi(x,\chi)\to0\) at infinity for every \(\chi\).
3. For some nonzero \(h\in L^1(G)\) and every compact \(C\subset\Gamma\),
   \(\sup_{\chi\in C}|V_h\phi(x,\chi)|\to0\).

When 1 holds, 3 holds for every nonzero window.

**Proof.** Fourier uniqueness implies \(\widehat{h^\sharp}(\eta_0)\ne0\) for some \(\eta_0\). The modulation formula
\(\widehat{\chi h^\sharp}(\eta)=\widehat{h^\sharp}(\eta-\chi)\)
shows that \(\{\chi h^\sharp:\chi\in\Gamma\}\) is regular. Hence 2, (7), and Theorem 1.2 with \(D=C_0(G)\) give 1. This is an allowed \(D\): [Radon Lemma 1.5](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-5) proves uniform closedness and uniform density of \(C_c\) in \(C_0\), and [Haar Lemma 1.1](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-lemma-1-1) proves uniform continuity of \(C_c\). Translation invariance follows directly from compact exceptional sets.

For 1 implies 3, the map \(\chi\mapsto\chi h^\sharp\) is norm continuous. Indeed, make the integral of \(|h^\sharp|\) outside a compact \(K\) small; on \(K\), convergence in the compact-open topology of characters makes the character difference uniformly small. The error is bounded by that difference times \(\|h^\sharp\|_1\), plus twice the tail. Thus the image of \(C\) is norm compact. Apply Theorem 1.3 with \(X=\{\phi\}\) and this compact family, then use (7). Finally 3 implies 2 by taking a singleton compact set. \(\square\)

<a id="ha-lca-15-example-1-5"></a>
**Example 1.5 — Why a family can be necessary.** There are LCA groups with regular families but no single function with nowhere-zero Fourier transform.

**Proof.** Take an uncountable set \(I\), \(K=\prod_{i\in I}\mathbb Z/2\mathbb Z\), and \(G=\mathbb R\times K\). [HA-LCA-02, Theorems 3.1 and 4.3](characters-and-the-dual-group.md#ha-lca-02-theorem-4-3) identify
\(\widehat G=\mathbb R\times\bigoplus_{i\in I}\mathbb Z/2\mathbb Z\).
Call the uncountable discrete second factor \(D\). For \(g\in L^1(G)\), the [Riemann–Lebesgue conclusion, HA-LCA-03, Corollary 2.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-corollary-2-2), says \(\widehat g\in C_0(\widehat G)\). On the closed slice \(\{0\}\times D\), each level set \(|\widehat g|\ge1/n\) is compact and therefore finite: the singleton cover of a discrete compact space has a finite subcover. The union of these finite sets is countable, so \(\widehat g\) vanishes at some point of the slice. On the other hand, the modulation family of any nonzero \(h^\sharp\) is regular by the proof just given. \(\square\)

## 2. A completely explicit Abel kernel

For bounded measurable \(A:(0,\infty)\to\mathbb C\), put \(\phi(x)=A(e^x)\) and
\[
 \mathcal A(T)=\frac1T\int_0^\infty e^{-t/T}A(t)\,dt.
\]

<a id="ha-lca-15-lemma-2-1"></a>
**Lemma 2.1 — Nonvanishing of the Abel kernel.** The function
\[
 k(s)=e^{-s}e^{-e^{-s}}
\]
is nonnegative, integrable with integral one, and satisfies
\[
 k*\phi(x)=\mathcal A(e^x),\qquad
 \widehat k(\xi)=\int_0^\infty e^{-u}u^{2\pi i\xi}\,du\ne0. \tag{8}
\]

**Proof.** The substitution \(u=e^{-s}\) proves the mass and Fourier identities. The substitution \(t=e^{x-s}\) proves the convolution identity. These substitutions, exponentials and complex derivatives are justified by [Real-variable Lemmas 1.2–1.4](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-2); all integrals are absolutely convergent.

Here is a proof of nonvanishing that does not invoke a formula for the gamma function. For real \(v\), dominated convergence gives
\[
 \int_0^\infty e^{-u}u^{iv}\,du
 =\lim_{n\to\infty}\int_0^n(1-u/n)^n u^{iv}\,du
 =\lim_{n\to\infty}
       \frac{n^{1+iv}n!}{(1+iv)(2+iv)\cdots(n+1+iv)}.      \tag{9}
\]
For the first equality, extend the integrand by zero beyond \(n\). The inequality \(\log(1-z)\le-z\), obtained by integrating its derivative for \(0\le z<1\), gives the dominator \(e^{-u}\); the derivative of \(\log\) at 1 gives pointwise convergence. For the second equality, substitute \(u=nt\) and integrate by parts \(n\) times in \(\int_0^1(1-t)^n t^{iv}\,dt\). At each step the primitive of \(t^{j+iv}\) is \(t^{j+1+iv}/(j+1+iv)\), which vanishes at zero. The resulting numerator is \(n!\), with the displayed denominator. Endpoint limits justify each integration by parts even though \(t^{iv}\) itself has no limit at zero.

The modulus of the last expression is
\[
 \frac n{n+1}\prod_{j=1}^{n+1}(1+v^2/j^2)^{-1/2}
 \ge \frac n{n+1}\exp\!\left(-\frac{v^2}{2}
                                      \sum_{j=1}^{n+1}j^{-2}\right)
 \ge \frac n{n+1}e^{-v^2}.
\]
Here \(\log(1+t)\le t\), and
\(\sum_{j\ge1}j^{-2}\le1+\sum_{j\ge2}1/[j(j-1)]=2\).
Taking the limit in (9) gives a strictly positive lower bound for its modulus. Apply this with \(v=2\pi\xi\). \(\square\)

<a id="ha-lca-15-corollary-2-2"></a>
**Corollary 2.2 — The one-sided Abel consequence.** If \(\mathcal A(T)\to a\) as \(T\to\infty\), then
\[
 g*\phi(x)\longrightarrow a\int_\mathbb R g
 \quad(x\to+\infty,\ g\in L^1(\mathbb R)).
\]
If, for each \(\varepsilon>0\), there are \(R,\delta>0\) such that
\[
 |A(te^{-s})-A(t)|<\varepsilon\quad(t>R,\ |s|<\delta),
\]
then \(A(t)\to a\).

**Proof.** The proof of Theorem 1.1 applies to a one-sided limit on \(\mathbb R\): the set of qualifying kernels is closed by the same uniform bound, and it is invariant under every fixed translation because \(x-y\to+\infty\) as \(x\to+\infty\). It contains the kernel \(k\) of Lemma 2.1. Its translates are dense by the earlier Wiener theorem, so it contains every kernel. The displayed condition becomes (3) with \(x\) restricted to a sufficiently far right half-line. A positive mass-one kernel supported in \((-\delta,\delta)\) gives the same \(\varepsilon\) estimate used in Theorem 1.1. \(\square\)

## 3. When common zeros determine an ideal

For a closed ideal \(I\subset L^1(G)\) put
\[
 \nu(I)=\{\gamma:\widehat f(\gamma)=0\ (f\in I)\},\qquad
 \iota(E)=\{f\in L^1(G):\widehat f|_E=0\}
\]
for closed \(E\subset\Gamma\). The set \(E\) **admits spectral synthesis** if the only closed ideal with hull \(E\) is \(\iota(E)\). We use the same notation for the corresponding ideals in \(A(\Gamma)\), when the argument is a Fourier transform.

<a id="ha-lca-15-lemma-3-0"></a>
**Lemma 3.0 — The minimal ideal.** For closed \(E\subset\Gamma\), define
\[
 j(E)=\overline{\{f\in L^1(G):
              \operatorname{supp}\widehat f
                 \text{ is compact and disjoint from }E\}}^{\,L^1}.
                                                               \tag{10}
\]
It is a closed ideal with hull \(E\). If \(\nu(I)=E\) for a closed ideal \(I\), then
\[
 j(E)\subseteq I\subseteq\iota(E).
\]
Furthermore
\[
 j(E)=\overline{\{f:\widehat f=0
                 \text{ on an open neighbourhood of }E\}}^{\,L^1}.
                                                               \tag{11}
\]
Synthesis is therefore equivalent to \(j(E)=\iota(E)\).

**Proof.** The set before closure in (10) is linear: finite unions of compact supports remain compact and disjoint from \(E\). Convolution with any \(L^1\) function only decreases Fourier support, so its closure is an ideal. It is contained in \(\iota(E)\). For \(\gamma\notin E\), [HA-LCA-14, Proposition 2.1](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-proposition-2-1), supplies a compact Fourier plateau supported outside \(E\) and equal to one near \(\gamma\). Thus no point outside \(E\) belongs to its hull.

If \(f\) has compact Fourier support disjoint from \(\nu(I)\), it is locally in \(I\) at every point of that support by [HA-LCA-14, Lemma 5.1](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-lemma-5-1). The [finite patching lemma, HA-LCA-14, Lemma 5.2](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-lemma-5-2), puts \(f\) in \(I\). Closure proves \(j(E)\subset I\), and the opposite upper inclusion is the definition of the hull.

A compact support disjoint from \(E\) vanishes on the open neighbourhood given by its complement. Conversely, if \(\widehat f\) vanishes on an open set containing \(E\), choose \(w\) with compact Fourier support and \(\|f-f*w\|_1\) arbitrarily small, using [HA-LCA-14, Lemma 3.1](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-lemma-3-1). The transform of \(f*w\) is supported in the intersection of that compact set with the closed complement of the neighbourhood, hence has compact support disjoint from \(E\). This proves (11) and the last assertion. \(\square\)

Say \(f\) is **locally in \(I\) at \(\gamma\)** if some \(a\in I\) has \(\widehat a=\widehat f\) on a neighbourhood of \(\gamma\). Write \(U_I(f)\) for the set of such points and \(Z(f)=\{\gamma:\widehat f(\gamma)=0\}\). A **perfect set** here means a closed set with no isolated points; it may be empty. Boundaries are taken in \(\Gamma\).

<a id="ha-lca-15-lemma-3-1"></a>
**Lemma 3.1 — The perfect defect set.** If \(I\) is closed and \(\nu(I)\subseteq Z(f)\), then
\[
 D_I(f)=\Gamma\setminus U_I(f)
\]
is perfect and
\[
 D_I(f)\subseteq\partial\nu(I)\cap\partial Z(f).            \tag{12}
\]

**Proof.** The set \(U_I(f)\) is open, since a local equality remains valid at every point of its open equality neighbourhood. Outside \(\nu(I)\), local division puts \(f\) locally in \(I\). In \(\operatorname{int}Z(f)\), the zero function does so. Since \(\nu(I)\subset Z(f)\), removing those two open sets leaves a subset of both boundaries, proving (12).

Suppose \(\gamma\) were an isolated point of \(D_I(f)\). Choose an open neighbourhood \(W\) with \(W\cap D_I(f)=\{\gamma\}\). The Fourier plateau theorem gives \(b\in L^1(G)\) with compact Fourier support inside \(W\) and \(\widehat b=1\) near \(\gamma\). Put \(v=f*b\). Because \(\gamma\in Z(f)\), \(\widehat v(\gamma)=0\). For every \(\varepsilon>0\), the [small-convolution lemma, HA-LCA-14, Lemma 4.1](closed-ideals-of-l1-g-and-wieners-theorem.md#ha-lca-14-lemma-4-1), supplies \(h\) with \(\widehat h=1\) near \(\gamma\) and \(\|v*h\|_1<\varepsilon\).

The function \(v-v*h\) has compact Fourier support. It is locally zero near \(\gamma\); outside \(\operatorname{supp}\widehat b\) it is locally zero; and at every other point of that support it is locally in \(I\), because \(f\) is locally in \(I\) there and multiplication by \(\widehat b(1-\widehat h)\) preserves a local ideal equality. Finite patching therefore gives \(v-v*h\in I\). Closedness and the arbitrary error yield \(v\in I\). Since \(\widehat v=\widehat f\) near \(\gamma\), this contradicts \(\gamma\in D_I(f)\). Hence there are no isolated points. \(\square\)

<a id="ha-lca-15-theorem-3-2"></a>
**Theorem 3.2 — The common-boundary criterion.** If \(I\) is a closed ideal, \(\nu(I)\subseteq Z(f)\), and
\(\partial\nu(I)\cap\partial Z(f)\) contains no nonempty perfect set, then \(f\in I\).

**Proof.** Lemma 3.1 forces \(D_I(f)=\varnothing\), so \(f\) is locally in \(I\) everywhere. For every compact-transform \(w\), the function \(f*w\) is also locally in \(I\) everywhere and has compact Fourier support. Finite patching puts it in \(I\). The compact-transform approximation from HA-LCA-14, Lemma 3.1, gives such products converging in \(L^1\) to \(f\). Closedness gives \(f\in I\). \(\square\)

<a id="ha-lca-15-corollary-3-3"></a>
**Corollary 3.3 — Synthesis on a small boundary.** If \(\partial E\) contains no nonempty perfect set, then the closed set \(E\) admits synthesis. This includes finite sets, closed discrete sets, and sets that are both closed and open. Also, for every closed ideal \(I\),
\[
 \widehat f=0\text{ on a neighbourhood of }\nu(I)
 \quad\Longrightarrow\quad f\in I.                        \tag{13}
\]
The minimal ideal is \(j(E)\), as described in (10)–(11).

**Proof.** For \(\nu(I)=E\) and \(f\in\iota(E)\), the common boundary in Theorem 3.2 is contained in \(\partial E\). Thus \(I=\iota(E)\). Every nonempty subset of a discrete subspace has isolated points in its relative topology; a closed discrete set and each subset of it therefore contain no nonempty perfect subset of \(\Gamma\). Finite sets are closed discrete in a Hausdorff space. A closed open set has empty boundary. Finally, if \(\widehat f\) vanishes near \(\nu(I)\), every point of \(\nu(I)\) is in \(\operatorname{int}Z(f)\); hence the common boundary is empty, and Theorem 3.2 applies. The assertion about \(j(E)\) is Lemma 3.0. \(\square\)

## 4. The dual question for bounded functions

Use the bilinear pairing
\[
 \langle f,\phi\rangle=\int_G f(x)\phi(-x)\,dx.             \tag{14}
\]
The reflection ensures that \(\langle f,\gamma\rangle=\widehat f(\gamma)\) for a character \(\gamma\). The [full-Haar dual theorem](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-theorem-1-2) identifies \(L^\infty(G)\) with \(L^1(G)^*\) under this pairing. A **co-ideal** means a weak-star closed, translation-invariant complex linear subspace of \(L^\infty(G)\).

For a co-ideal \(J\), define
\[
 \sigma(J)=\{\gamma\in\Gamma:\gamma\in J\},\qquad
 \tau(E)=\overline{\operatorname{span}\{\gamma:\gamma\in E\}}^{\,w^*}.
\]
For \(\phi\in L^\infty(G)\), let \(J_\phi\) be the weak-star closed span of all its translates, and put \(\sigma(\phi)=\sigma(J_\phi)\).

<a id="ha-lca-15-proposition-4-1"></a>
**Proposition 4.1 — Ideal/co-ideal duality.** The annihilators for (14) give inverse correspondences between closed ideals and co-ideals. Moreover
\[
 \sigma(I^\perp)=\nu(I),\qquad
 {}^\perp\tau(E)=\iota(E).                                \tag{15}
\]
A co-ideal \(J\) is generated by the characters it contains, that is,
\(J=\tau(\sigma(J))\), exactly when
\({}^\perp J=\iota(\nu({}^\perp J))\).

**Proof.** The double-annihilator statements are Lemma 0.1 and the proved \(L^1\) dual identification. The identity
\[
 \langle L_yf,\phi\rangle=\langle f,L_y\phi\rangle
\]
follows by translation in the integral. A closed ideal is translation invariant by HA-LCA-14, Proposition 1.1; consequently its annihilator is translation invariant and weak-star closed. Conversely the preannihilator of a co-ideal is norm closed and translation invariant, and that proposition makes it an ideal.

For clarity, translations are weak-star continuous, because each pairing with \(f\) becomes the pairing with \(L_yf\). Thus \(J_\phi\) and \(\tau(E)\) really are co-ideals: translates of a character are scalar multiples of it, and taking weak-star closure preserves invariance.

A character \(\gamma\) belongs to \(I^\perp\) exactly when \(\widehat f(\gamma)=0\) for all \(f\in I\), giving the first equality in (15). A pairing vanishes on the weak-star closed character span exactly when it vanishes on each of its generators; this is the second equality. Apply double annihilators to obtain the final equivalence. \(\square\)

For a finite complex Radon measure, its support means the support of its total variation.

<a id="ha-lca-15-proposition-4-2"></a>
**Proposition 4.2 — Spectra of individual functions.** One has
\[
 \sigma(\phi)=\nu\{f\in L^1(G):f*\phi=0\}.                 \tag{16}
\]
If \(\phi\in L^1(G)\cap L^\infty(G)\), its spectrum is
\(\operatorname{supp}\widehat\phi\). If
\[
 \phi(x)=\int_\Gamma\gamma(x)\,d\mu(\gamma)
\]
for a finite complex Radon measure \(\mu\), then
\[
 \sigma(\phi)=\operatorname{supp}\mu,\qquad
 J_\phi=\tau(\operatorname{supp}\mu).                      \tag{17}
\]

**Proof.** The pairing with \(L_y\phi\) equals \((f*\phi)(-y)\). Thus
\({}^\perp J_\phi=\{f:f*\phi=0\}\), and Proposition 4.1 gives (16).

For \(\phi\in L^1\cap L^\infty\), Fourier multiplication and [HA-LCA-09, Corollary 4.2](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-2) show
\[
 f*\phi=0\quad\Longleftrightarrow\quad
       \widehat f\,\widehat\phi=0
 \quad\Longleftrightarrow\quad
       \widehat f|_{\operatorname{supp}\widehat\phi}=0.
\]
The last equivalence uses continuity and the definition of support as the closure of the nonzero set. The hull of this kernel is that support by HA-LCA-14, Proposition 2.1.

For the measure representation, bounded Fubini and the Fourier conventions give
\[
 f*\phi(x)=\int_\Gamma\widehat f(\gamma)\gamma(x)\,d\mu(\gamma).
\]
For precision, \(f(t)\,dt\) is a finite complex Radon measure by [HA-LCA-03, Lemma 4.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-4-1). The kernel \((t,\gamma)\mapsto\gamma(x-t)\) is bounded and jointly continuous by [HA-LCA-09, Lemma 1.1](the-pontryagin-duality-theorem.md#ha-lca-09-lemma-1-1). Apply the [bounded-continuous finite-Radon product theorem](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-theorem-2-2) to that measure and \(\mu\). The absolute integral is at most \(\|f\|_1\|\mu\|\). [Fourier–Stieltjes uniqueness, HA-LCA-09, Theorem 4.1](the-pontryagin-duality-theorem.md#ha-lca-09-theorem-4-1), then says that \(f*\phi=0\) exactly when \(\widehat f\,\mu=0\).

For a continuous function \(b\), the identity \(b\mu=0\) is equivalent to \(b=0\) on \(\operatorname{supp}\mu\). Indeed, on an open set where \(b\ne0\), bounded reciprocal restrictions on the sets \(|b|\ge1/n\) imply that the restriction of \(\mu\) is zero. The variation is therefore zero there. Conversely a finite Radon measure is concentrated on its support: every compact subset of its open complement is covered by finitely many open measure-zero neighbourhoods, and inner regularity gives zero measure for the complement. Thus \(b=0\) on the support implies \(b\mu=0\).

We obtain \({}^\perp J_\phi=\iota(\operatorname{supp}\mu)\). Its hull is exactly that closed set, and (15) plus double annihilators gives both assertions in (17). \(\square\)

## 5. A sphere that does not admit synthesis

We first establish the elementary smooth and geometric ingredients, so the construction needs no distribution theory or quoted special-function estimate. For \(\mathbb R^n\), Fourier transform uses \(e^{-2\pi i x\cdot\xi}\) and Lebesgue measure.

<a id="ha-lca-15-lemma-5-0"></a>
**Lemma 5.0 — Smooth cutoffs and rapid inverse transforms.** If \(K\subset O\subset\mathbb R^n\), with \(K\) compact and \(O\) open, there is \(b\in C_c^\infty(\mathbb R^n)\) with \(0\le b\le1\), \(b=1\) near \(K\), and \(\operatorname{supp}b\subset O\). For every \(b\in C_c^\infty\), its inverse Fourier integral
\[
 \check b(x)=\int_{\mathbb R^n}b(\xi)e^{2\pi ix\cdot\xi}\,d\xi
\]
is smooth; it and all its derivatives decrease faster than every reciprocal power of \(1+|x|\). In particular, all its polynomial moments are integrable, and \(\widehat{\check b}=b\). Smooth compactly supported functions are uniformly dense in \(C_c\) when supports are allowed in one fixed compact enlargement.

**Proof.** Define \(\eta(t)=e^{-1/t}\) for \(t>0\) and zero for \(t\le0\). Every derivative on \(t>0\) is a finite sum of powers of \(t^{-1}\) times \(e^{-1/t}\). They all tend to zero at \(0\): for every integer \(m\), the exponential series gives \(s^m e^{-s}\to0\) as \(s\to\infty\), by bounding with the term of degree \(m+1\) and then, if necessary, a still higher term. Induction on the derivative order therefore proves that \(\eta\) is smooth across zero. The function
\(\eta(t)/[\eta(t)+\eta(1-t)]\) is a smooth step, zero for \(t\le0\) and one for \(t\ge1\). Composing it with affine functions of \(|\xi-a|^2\) gives a bump equal to one on a smaller closed ball and zero outside a larger open ball. Cover \(K\) by finitely many smaller balls whose larger closures lie in \(O\). If the resulting bumps are \(b_j\), the function \(1-\prod_j(1-b_j)\) has the required properties.

Differentiating the inverse integral under its compactly supported integrable dominator is justified by [Real-variable Lemma 1.4](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-4), applied in each coordinate. Integration by parts in each coordinate, using [Real-variable Lemma 1.3](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-3) and Fubini, yields
\[
 (1+|x|^2)^m\partial_x^\beta\check b(x)
 =\int
   \left(1-\frac{\Delta_\xi}{4\pi^2}\right)^m
       [(2\pi i\xi)^\beta b(\xi)]\,e^{2\pi ix\cdot\xi}\,d\xi. \tag{18}
\]
Here \(\beta\) is a tuple of nonnegative integers and
\(\partial^\beta=\prod_j\partial_j^{\beta_j}\). The integrand has finite \(L^1\) norm, independent of \(x\), proving every claimed decay bound. The [dyadic volume estimate, HA-LCA-11, Lemma 2.0](the-poisson-summation-formula.md#ha-lca-11-lemma-2-0), then makes every required moment integrable. [Fourier inversion, HA-LCA-09, Theorem 4.1](the-pontryagin-duality-theorem.md#ha-lca-09-theorem-4-1), with the reflected transform, gives \(\widehat{\check b}=b\) everywhere.

Finally, normalize a nonnegative smooth bump to integral one and rescale it into balls of radius \(\varepsilon\). Its convolution with \(f\in C_c\) is smooth, has support in a fixed compact enlargement, and differs uniformly from \(f\) by at most its modulus of uniform continuity on translations of size \(\varepsilon\). Differentiation follows by differentiating the smooth kernel. This proves the density statement. The same fixed-support estimate proves \(L^1\) convergence, when needed. \(\square\)

Let \(\sigma_n\) be the rotation-invariant probability measure on \(S^{n-1}\). The next proof constructs it directly. In dimension three write \(\mu_3=4\pi\sigma_3\) for ordinary surface measure.

<a id="ha-lca-15-lemma-5-1"></a>
**Lemma 5.1 — A full-sphere Fourier bound.** For \(n\ge3\),
\[
 |\widehat{\sigma_n}(x)|\le \frac{C_n}{1+|x|}.
                                                               \tag{19}
\]
For \(n=3\), more precisely,
\[
 \widehat{\sigma_3}(x)
   =\frac{\sin(2\pi|x|)}{2\pi|x|},
\]
with value one at zero. The measure has full support on the sphere.

**Proof.** On \(\mathbb R^n\) take the probability density
\(\pi^{-n/2}e^{-|z|^2}\), whose total mass is one by the [Gaussian calculation](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-theorem-2-1) and finite product integration. Push it to the sphere by \(z\mapsto z/|z|\), omitting the null point \(z=0\). This is a finite Radon measure: compact approximations away from zero have compact images, and their omitted mass tends to zero. An orthogonal linear substitution preserves \(|z|\) and Lebesgue measure, by the [linear volume formula, HA-LCA-10, Lemma 6.0](subgroups-quotients-and-annihilators.md#ha-lca-10-lemma-6-0). Thus the pushforward is rotation invariant. Every nonempty relatively open patch of the sphere has a nonempty open cone as preimage; the strictly positive Gaussian density gives that cone positive measure. This proves full support.

We derive its first-coordinate density using only one-variable substitutions. A squared Gaussian coordinate has density
\(c\,y^{-1/2}e^{-y}\) on \(y>0\), by the two substitutions \(z=\pm\sqrt y\). The sum of \(m\) independent squared coordinates has density
\[
 c_m y^{m/2-1}e^{-y}\quad(y>0),\qquad c_m>0.
\]
Indeed this holds for \(m=1\). Convolution with the density for one more square gives, after \(s=yv\), a constant times
\[
 e^{-y}y^{(m+1)/2-1}
       \int_0^1 v^{m/2-1}(1-v)^{-1/2}\,dv.
\]
The last integral is positive and finite by comparison near its two endpoints. This proves the assertion by induction; convolution of these densities follows directly from Fubini and the translation substitution in one variable.

Consequently \(r=(z_2^2+\cdots+z_n^2)^{1/2}\) has density \(c r^{n-2}e^{-r^2}\) on \(r>0\), independently of \(z_1=u\). For fixed \(r\), substitute
\[
 t=\frac{u}{\sqrt{u^2+r^2}},\qquad
 u=\frac{rt}{\sqrt{1-t^2}},\qquad
 du=\frac{r\,dt}{(1-t^2)^{3/2}}.
\]
The joint density then has the factor
\[
 r^{n-1}(1-t^2)^{-3/2}e^{-r^2/(1-t^2)}\,dr\,dt.
\]
Integrating in \(r\), using \(r=s\sqrt{1-t^2}\), gives the normalized density
\[
 c_n(1-t^2)^{(n-3)/2}\,1_{(-1,1)}(t)\,dt,\qquad
 c_n^{-1}=\int_{-1}^1(1-t^2)^{(n-3)/2}\,dt.               \tag{20}
\]
All interchanges are of nonnegative integrands or bounded test functions against probability densities.

Rotation invariance, and an orthogonal map carrying \(x/|x|\) to the first coordinate axis, now give
\[
 \widehat{\sigma_n}(x)
   =c_n\int_{-1}^1 e^{-2\pi i|x|t}(1-t^2)^{(n-3)/2}\,dt. \tag{21}
\]
Such a map exists by completing a unit vector to an orthonormal basis, the elementary finite-dimensional construction already used in Lemma 0.1.

For \(n=3\), \(c_3=1/2\), so direct integration gives the asserted sine formula. For \(n>3\), put \(a=(n-3)/2>0\). The weight \(w(t)=(1-t^2)^a\) vanishes at the endpoints and
\[
 \int_{-1}^1|w'(t)|\,dt
 =2\int_0^1 2at(1-t^2)^{a-1}\,dt=2.
\]
Integrate (21) by parts on \([-1+\varepsilon,1-\varepsilon]\) and pass to the limit; the boundary terms vanish and the derivative is integrable. For \(|x|>0\) this gives the bound \(2c_n/(2\pi|x|)\). The probability bound \(|\widehat{\sigma_n}|\le1\) handles \(|x|\le1\), proving (19).

To check the stated ordinary normalization in dimension three, parametrize the sphere away from its poles by
\((t,\theta)\mapsto(t,\sqrt{1-t^2}\cos\theta,\sqrt{1-t^2}\sin\theta)\).
The tangent vectors are orthogonal and the product of their lengths is one; thus its usual surface element is \(dt\,d\theta\), of total mass \(4\pi\). For the Gaussian construction, the angle of \((z_2,z_3)\) is uniform and independent of its radius and of \(z_1\). To verify this without a polar integration theorem, average any bounded test product over rotations of the last two coordinates: rotational invariance leaves the integral unchanged and the angular factor becomes its circle average, while radial and \(z_1\) factors are fixed. Fubini justifies the averaging. Formula (20) now shows that \(\sigma_3\) has coordinate element \(dt\,d\theta/(4\pi)\), as claimed. \(\square\)

<a id="ha-lca-15-theorem-5-2"></a>
**Theorem 5.2 — Schwartz's nonsynthesis sphere.** For every \(n\ge3\), the sphere \(E=S^{n-1}\subset\widehat{\mathbb R^n}=\mathbb R^n\) does not admit spectral synthesis.

**Proof.** Define
\[
 \Phi(x)=-2\pi ix_1\widehat{\sigma_n}(x),\qquad
 \Lambda(f)=\int_{\mathbb R^n}f(x)\Phi(x)\,dx.
\]
Lemma 5.1 proves that \(\Phi\) is bounded; therefore \(\Lambda\) is a bounded linear functional on \(L^1\). Whenever \(x_1f\in L^1\), differentiating its Fourier integral and then using finite-measure Fubini gives
\[
 \Lambda(f)=\int_{S^{n-1}}\partial_1\widehat f(\xi)
                                        \,d\sigma_n(\xi). \tag{22}
\]

We prove that \(\Lambda\) annihilates the genuine closed ideal \(j(E)\) of Lemma 3.0. Suppose \(\widehat f\) has compact support \(K\) disjoint from \(E\). By Lemma 5.0 choose \(b\in C_c^\infty\), equal to one near \(K\) and zero near \(E\), and put \(h=\check b\). Then \(f*h=f\) by Fourier uniqueness. Bounded Fubini yields
\[
 \Lambda(f*h)=\int f(y)\left(\int h(x-y)\Phi(x)\,dx\right)dy.
\]
This interchange requires only \(\|\Phi\|_\infty\|f\|_1\|h\|_1<\infty\), not an integrable moment of \(f\). For each fixed \(y\), the rapid decay of \(h\) does permit a first moment, and the inner integral is
\[
 \int_E e^{-2\pi iy\cdot\xi}
           [\,\partial_1 b(\xi)-2\pi iy_1b(\xi)\,]\,d\sigma_n(\xi)=0.
\]
Both \(b\) and \(\partial_1b\) vanish near \(E\). Hence \(\Lambda(f)=0\); continuity proves its vanishing on all of \(j(E)\).

Choose a smooth compact cutoff \(\beta\) equal to one near \(E\), and put
\[
 F(\xi)=(|\xi|^2-1)\xi_1\beta(\xi),\qquad f=\check F.
\]
Lemma 5.0 gives \(f\in L^1\), \(x_1f\in L^1\), and \(\widehat f=F\). Thus \(f\in\iota(E)\), whereas (22) gives
\[
 \Lambda(f)=2\int_E\xi_1^2\,d\sigma_n(\xi)=\frac2n>0.
\]
The last equality follows because coordinate permutations preserve \(\sigma_n\), the integrals of the \(n\) coordinate squares are equal, and their sum is the integral of \(|\xi|^2=1\). Consequently \(f\notin j(E)\). The two closed ideals \(j(E)\) and \(\iota(E)\) have the same hull \(E\) and are different. \(\square\)

## 6. Failure on every nondiscrete frequency group

For a compact abelian group \(K\), normalize Haar measure to one and write \(D=\widehat K\). [Compact/discrete duality](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-4) and the [Fourier formulas for counting measure](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-proposition-3-3) identify
\[
 A(K)=\left\{F=\sum_{d\in D}a_d d:\sum_{d\in D}|a_d|<\infty\right\},
 \qquad \|F\|_A=\sum_d|a_d|.
\]
Only countably many coefficients of any such series are nonzero; the series converges absolutely and uniformly. In this section, write
\(c_d(F)=\int_K F(k)\overline{d(k)}\,dk\).
The coefficients are unique by the [compact Fourier basis theorem](the-plancherel-theorem.md#ha-lca-08-corollary-4-1). Multiplying series shows
\[
 \sup_d|c_d(FH)|\le\|F\|_A\sup_d|c_d(H)|                 \tag{23}
\]
for \(F\in A(K)\) and bounded measurable \(H\), by an absolutely convergent integral interchange.

<a id="ha-lca-15-lemma-6-0a"></a>
**Lemma 6.0a — A level-set criterion.** Suppose a real-valued \(q\in A(K)\) satisfies
\[
 B(u)=\sup_{d\in D}|c_d(e^{iuq})|,\qquad
 \int_\mathbb R(1+|u|)B(u)\,du<\infty.                    \tag{24}
\]
Then some closed level set \(E=\{k:q(k)=a\}\) does not admit synthesis.

**Proof.** The pushforward \(\nu=q_*dk\) is a probability measure on the compact real interval \([-\|q\|_\infty,\|q\|_\infty]\). Its characteristic function
\(\psi(u)=\int e^{iut}\,d\nu(t)=c_0(e^{iuq})\) obeys (24). Therefore
\[
 w(t)=\frac1{2\pi}\int_\mathbb R e^{-iut}\psi(u)\,du
\]
is continuously differentiable, by dominated convergence for both the integral and its derivative.

We verify that \(\nu=w(t)\,dt\). For \(\zeta\in C_c^\infty(\mathbb R)\), Lemma 5.0 and Fourier inversion, with the substitution \(u=2\pi\xi\), give
\[
 \int\zeta(t)w(t)\,dt
 =\frac1{2\pi}\int\psi(u)
                  \left(\int\zeta(t)e^{-iut}\,dt\right)du
 =\int\zeta\,d\nu.
\]
Both interchanges are absolutely integrable, since \(\psi\in L^1\), \(\zeta\in L^1\), and the scalar Fourier transform of \(\zeta\) is integrable. Nonnegative smooth test bumps show that \(w\) is real and nonnegative: a nonzero imaginary part or a negative real value, being continuous, could be detected in a sufficiently small neighbourhood. Bumps outside the displayed interval similarly show that \(w\) vanishes there. Hence \(w\) is integrable. The smooth approximation in Lemma 5.0 extends the identity to \(C_c\); finite Radon uniqueness from [Radon Theorem 3.1](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-theorem-3-1) gives the claimed equality of measures. In particular \(\int w=1\), so \(w(a)>0\) for some \(a\).

Choose a nonnegative \(\theta\in C_c^\infty((-1,1))\) with integral one and set
\[
 h_\varepsilon(t)=\varepsilon^{-2}
                         \theta'((t-a)/\varepsilon),\qquad
 \Lambda_\varepsilon(F)=\int_K F(k)h_\varepsilon(q(k))\,dk.
\]
With the angular scalar transform
\(\mathcal F_{\!a}\theta(u)=\int\theta(t)e^{-iut}\,dt\),
integration by parts gives
\[
 \mathcal F_{\!a}h_\varepsilon(u)
       =iu\,e^{-iua}\mathcal F_{\!a}\theta(\varepsilon u).
\]
It follows by scalar inversion and Fubini that
\[
 \Lambda_\varepsilon(d)
 =\frac1{2\pi}\int iu\,e^{-iua}
       \mathcal F_{\!a}\theta(\varepsilon u)
       c_{-d}(e^{iuq})\,du.                              \tag{25}
\]
Since \(|\mathcal F_{\!a}\theta|\le1\), every such value has modulus at most
\(M=(2\pi)^{-1}\int |u|B(u)\,du\). Expanding an absolutely convergent Fourier series now gives
\(|\Lambda_\varepsilon(F)|\le M\|F\|_A\).
Dominated convergence in (25) gives a limit for every character. Absolute summability of the coefficients of \(F\), with the same bound \(M\), then gives a bounded linear functional
\(\Lambda(F)=\lim_{\varepsilon\downarrow0}\Lambda_\varepsilon(F)\) on all of \(A(K)\).

If \(F\) vanishes on an open neighbourhood \(O\) of \(E=\{q=a\}\), compactness gives
\(\inf_{K\setminus O}|q-a|>0\), unless that complement is empty. Thus \(Fh_\varepsilon(q)=0\) for sufficiently small \(\varepsilon\), and \(\Lambda(F)=0\). By (11), \(\Lambda\) annihilates \(j(E)\).

On the other hand \(q-a\in\iota(E)\), and the density \(w\) gives
\[
 \Lambda_\varepsilon(q-a)
 =\int (t-a)h_\varepsilon(t)w(t)\,dt
 =\int s\theta'(s)w(a+\varepsilon s)\,ds
 \longrightarrow -w(a)\ne0.
\]
The last step uses continuity of \(w\), compact support of \(\theta\), and
\(\int s\theta'(s)\,ds=-\int\theta=-1\).
Therefore \(\iota(E)\ne j(E)\). \(\square\)

<a id="ha-lca-15-lemma-6-0b"></a>
**Lemma 6.0b — Uniform cyclic estimates.** For an element \(g\in D\) of order \(r\), \(2\le r\le\infty\), expand
\[
 e^{iv\operatorname{Re}g(k)}
       =\sum_{m\in\mathbb Z/r\mathbb Z}p_{m,r}(v)\,g(k)^m,
\]
where for \(r=\infty\) the index set is \(\mathbb Z\). There are constants \(\delta>0\), \(0<\rho<1\), independent of \(r\), such that

\[
 \sum_m|p_{m,r}(v)|\le3(1+|v|),\qquad
 |p_{m,r}(v)|\le1,                                       \tag{26}
\]
and
\[
 \delta\le |v|\le2\delta
       \quad\Longrightarrow\quad |p_{m,r}(v)|\le\rho
                  \quad\text{for every }m,r.             \tag{27}
\]
For every \(R,\varepsilon>0\), an integer \(d\) can be chosen independently of \(r\) such that, for \(|v|\le R\),
\[
 \sum_{|m|_r>d}|p_{m,r}(v)|<\varepsilon,                  \tag{28}
\]
where \(|m|_r\) is the least absolute value of an integer representing the class.

**Proof.** Begin on the circle with \(E_v(t)=e^{iv\cos(2\pi t)}\). Its exponential power series converges in \(A(\mathbb T)\): the trigonometric polynomial \(\cos(2\pi t)\) has \(A\)-norm one, so the norms of its \(j\)-th exponential terms are at most \(|v|^j/j!\). Let \(b_m(v)\) be its coefficients. Since the \(j\)-th power has no frequencies with \(|m|>j\),
\[
 \sum_{|m|>d}|b_m(v)|
 \le\sum_{j>d}\frac{|v|^j}{j!}.                           \tag{29}
\]
This tends to zero uniformly for \(|v|\le R\).

Integration by parts gives the Fourier coefficients of \(E_v'\) as \(2\pi im b_m(v)\). Parseval, using \(|E_v|=1\) and
\(E_v'=-2\pi iv\sin(2\pi t)E_v\), gives
\[
 \sum_m|b_m(v)|^2=1,\qquad
 \sum_m m^2|b_m(v)|^2=v^2/2.
\]
Thus Cauchy–Schwarz and \(\sum_m(1+m^2)^{-1}\le5\) imply
\[
 \sum_m|b_m(v)|\le\sqrt5\sqrt{1+v^2/2}\le3(1+|v|).
\]
Parseval here is precisely the compact Fourier basis result cited above.

For finite \(r\), restricting this absolutely convergent series to the \(r\)-th roots of unity groups its coefficients by residue classes:
\(p_{m,r}(v)=\sum_{j\equiv m\ (r)}b_j(v)\).
Finite character orthogonality, proved in [HA-LCA-01, Theorem 2.1](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-2-1), verifies this formula and identifies these with the normalized Fourier coefficients on that finite cyclic group. It proves (26), and (29) proves (28), because any class with \(|m|_r>d\) receives only terms with \(|j|>d\). For infinite \(r\), \(p_{m,\infty}=b_m\). The coefficient formula for an arbitrary \(g\) is valid because restriction \(K\to\widehat{\langle g\rangle}\) is onto by [HA-LCA-10, Theorem 2.1](subgroups-quotients-and-annihilators.md#ha-lca-10-theorem-2-1), and pushes normalized Haar to normalized Haar. The latter follows from translation invariance and Haar uniqueness.

It remains to give a strict uniform bound. In the finite cyclic probability space or on the circle, let \(X=\cos(2\pi t)\). Character orthogonality gives
\(\mathbb EX=0\), and \(\mathbb EX^2=1\) for \(r=2\), or \(1/2\) for \(r\ge3\), including \(r=\infty\). Every nonconstant Fourier coefficient of \(e^{ivX}\) has modulus at most
\(\mathbb E|e^{ivX}-1|\le |v|\).
For the constant coefficient, take an independent copy \(Y\) of \(X\). If \(|v|\le1/4\), then \(|v(X-Y)|\le1\), and the elementary power series bound
\(\cos s\le1-s^2/4\) for \(|s|\le1\) gives
\[
 |\mathbb E e^{ivX}|^2
   =\mathbb E\cos(v(X-Y))
   \le1-\tfrac14v^2\mathbb E(X-Y)^2
   \le1-v^2/4.
\]
The cosine bound follows from
\(\cos s\le1-s^2/2+s^4/24\) on this interval, by the alternating power series. Take \(\delta=1/8\) and
\(\rho=\sqrt{1-\delta^2/4}<1\); it also exceeds \(2\delta\). These estimates prove (27) for every coefficient, including order two. \(\square\)

<a id="ha-lca-15-lemma-6-0c"></a>
**Lemma 6.0c — Constructing the small coefficients.** If \(K\) is infinite compact abelian, there is a real \(q\in A(K)\) satisfying (24).

**Proof.** Its discrete dual \(D\) is infinite: if \(D\) were finite, its dual, which is \(K\) by [Pontryagin duality](the-pontryagin-duality-theorem.md#ha-lca-09-theorem-2-1), would be finite. We construct a sequence \(g_k\in D\), and in each case set
\[
 q=\sum_{k=1}^\infty k^{-2}\operatorname{Re}g_k.           \tag{30}
\]
Each summand without its scalar coefficient has \(A\)-norm at most one, so this series converges in \(A(K)\) and uniformly to a real function.

For \(u>0\), call an integer \(k\) active when
\(\delta\le u/k^2\le2\delta\), using Lemma 6.0b. The number \(N(u)\) of active integers satisfies
\[
 N(u)\ge c\sqrt u-2,\qquad
 c=\delta^{-1/2}-(2\delta)^{-1/2}>0,                      \tag{31}
\]
by counting integers in
\([\sqrt{u/(2\delta)},\sqrt{u/\delta}]\).

**Bounded orders.** Suppose some positive integer \(M\) kills every element of \(D\). Then \(D[p]=\{d:pd=0\}\) is infinite for some prime divisor \(p\) of \(M\). Indeed, if all these kernels were finite, induction on the number of prime factors of \(M\), counting multiplicity, would show \(D\) finite. Choose a prime factor \(p\). The image \(pD\) is killed by \(M/p\); its prime kernels are subgroups of the corresponding finite kernels of \(D\), so by induction it is finite. Each fibre of \(D\to pD\) has size \(|D[p]|<\infty\), proving finiteness of \(D\), a contradiction.

In the infinite vector space \(D[p]\) over the finite field \(\mathbb F_p\), choose \(g_k\) recursively outside the finite span of their predecessors. Then their generated subgroup is the direct sum \(H=\bigoplus_k\langle g_k\rangle\). Restriction \(K\to\widehat H\) is onto, with Haar-probability pushforward, by HA-LCA-10, Theorem 2.1.

The function \(e^{iuq}\) factors through \(\widehat H\). Its coefficient at a character outside \(H\) is zero: there exists a point of \(H^\perp\) on which that character is nontrivial, by [double annihilation, HA-LCA-10, Proposition 1.2](subgroups-quotients-and-annihilators.md#ha-lca-10-proposition-1-2); translation by that point leaves the function unchanged and multiplies the coefficient by a nontrivial scalar. At a character in \(H\), split \(H\) into its finite active-coordinate subgroup and the complementary direct sum. The [product duality of HA-LCA-02, Theorem 4.3](characters-and-the-dual-group.md#ha-lca-02-theorem-4-3) and normalized Haar product integration factor the coefficient into the active cyclic coefficients and a coefficient of modulus at most one on the remaining factor. Every active coefficient is at most \(\rho\). Consequently
\[
 B(u)\le\rho^{N(u)}\le\rho^{\,c\sqrt u-2}.                \tag{32}
\]

**Unbounded finite orders.** Suppose every element has finite order but their orders are unbounded. We give the diagonal choices explicitly. For each integer \(q_0\ge1\), put \(R_{q_0}=e^{q_0}\), and for \(k>q_0\) put
\(\varepsilon_{q_0,k}=2^{-k-2}e^{-R_{q_0}}\).
Choose integers \(d_{q_0,k}\ge1\) by (28) so that its tail bound is less than \(\varepsilon_{q_0,k}\) for every order and \(|v|\le R_{q_0}\). All these choices can be made before choosing the group elements.

Choose nonzero \(g_1\). Having chosen \(g_1,\ldots,g_{k-1}\), choose \(g_k\) of finite order \(r_k\) so large that
\[
 r_k>2\max_{1\le q_0<k}d_{q_0,k}\prod_{j<k}r_j.           \tag{33}
\]
This is possible by unboundedness. For each fixed \(q_0\), distinct finite sums
\(\sum_{k>q_0}m_kg_k\), with \(|m_k|\le d_{q_0,k}\), are distinct. Otherwise subtract two sums and choose the largest index \(k\) with nonzero difference \(n_k\). Multiply the resulting relation by \(\prod_{j<k}r_j\). It says that \(r_k\) divides the nonzero integer \(n_k\prod_{j<k}r_j\), whose absolute value is strictly less than \(r_k\) by (33), a contradiction. For finite cyclic indices we choose one representative of least absolute value, so each truncated coefficient is counted once.

Fix \(q_0\) and \(0\le u\le R_{q_0}\). In the tail product of \(e^{iuq}\), truncate the \(k\)-th cyclic factor at \(|m|_{r_k}\le d_{q_0,k}\); call it \(T_k\). Then
\[
 \|T_k-e^{iu k^{-2}\operatorname{Re}g_k}\|_\infty
       <\varepsilon_{q_0,k},\qquad
 \|T_k\|_\infty\le1+\varepsilon_{q_0,k}.
\]
Both infinite products converge uniformly. For the true factors use
\(\sum_{k>q_0}|u|k^{-2}<\infty\); for the truncated factors also use
\(\sum\varepsilon_{q_0,k}<\infty\). A telescoping product estimate gives
\[
 \left\|\prod_{k>q_0}T_k
      -e^{iu\sum_{k>q_0}k^{-2}\operatorname{Re}g_k}\right\|_\infty
 \le \exp\!\left(\sum_{k>q_0}\varepsilon_{q_0,k}\right)-1
 <e^{-R_{q_0}}.                                         \tag{34}
\]
For the last bound, the sum is at most \(e^{-R_{q_0}}/8\), and
\(e^s-1\le2s\) for \(0\le s\le1\).

In every finite product of the \(T_k\), uniqueness of the truncated frequency sums means that a Fourier coefficient is either zero or exactly a product of cyclic coefficients. All these factors have modulus at most one; the active factors have modulus at most \(\rho\). Once the finite product includes all active indices larger than \(q_0\), its coefficient supremum is at most
\(\rho^{N(u)-q_0}\), with a bound larger than one allowed if this exponent is negative. Uniform passage to the infinite product preserves the bound. The error (34) contributes at most \(e^{-R_{q_0}}\) to every coefficient.

The first \(q_0\) untruncated factors have \(A\)-norm at most
\([3(1+u)]^{q_0}\), by (26). Using (23) we have proved
\[
 B(u)\le[3(1+u)]^{q_0}
       \bigl(e^{-R_{q_0}}+\rho^{\,c\sqrt u-2-q_0}\bigr)
       \quad(0\le u\le R_{q_0}).                         \tag{35}
\]

**An element of infinite order.** Choose one such element \(g_0\). Use the same numbers \(R_{q_0},\varepsilon_{q_0,k},d_{q_0,k}\), now with the infinite-order cyclic coefficients. Set \(g_k=N_kg_0\), where \(N_1=1\) and the positive integers \(N_k\) are chosen recursively so that
\[
 N_k>N_{k-1},\qquad
 N_k>2\sum_{q_0<j<k}d_{q_0,j}N_j
                  \quad(1\le q_0<k).                   \tag{36}
\]
There are only finitely many requirements at each step. A nontrivial relation between two truncated tail sums, with largest index \(k\), would imply
\[
 N_k\le |n_k|N_k
       =\left|\sum_{q_0<j<k}n_jN_j\right|
       \le2\sum_{q_0<j<k}d_{q_0,j}N_j<N_k.
\]
Thus uniqueness again holds, and the entire proof of (34)–(35) applies unchanged with the infinite-order coefficients.

Finally, in either case covered by (35), choose
\(q_0=\lceil\log u\rceil\) for \(u\ge e\). Then \(R_{q_0}\ge u\), and taking logarithms in its two terms shows
\[
 B(u)\le C e^{-c'\sqrt u}
\]
for sufficiently large \(u\), with \(C,c'>0\): the positive logarithmic contribution is \(O((\log u)^2)\), while the negative contributions are \(-u\) and \(-c|\log\rho|\sqrt u\). To verify the comparison, put \(v=\log u\); the exponential series gives \(v^2e^{-v/2}\to0\). The same bound already follows from (32) in the bounded-order case. Since \(q\) is real,
\(c_d(e^{-iuq})=\overline{c_{-d}(e^{iuq})}\), so \(B(-u)=B(u)\), and always \(B(u)\le1\). Also \(B\) is measurable: each coefficient is continuous in \(u\), and its supremum is lower semicontinuous. The substitution \(v=\sqrt u\) and repeated integration by parts show
\(\int_1^\infty(1+u)e^{-c'\sqrt u}\,du<\infty\).
This proves (24) in all cases. \(\square\)

<a id="ha-lca-15-theorem-6-1"></a>
**Theorem 6.1 — The compact construction.** Every infinite compact abelian group \(K\) has a closed set which does not admit synthesis for \(A(K)\).

**Proof.** Lemma 6.0c constructs the real Fourier-algebra function \(q\) on the given group, with no metrizability assumption on \(K\). Lemma 6.0a then constructs a closed level set \(E\), a function \(q-a\in\iota(E)\), and a bounded functional annihilating \(j(E)\) but not \(q-a\). Thus \(j(E)\ne\iota(E)\). \(\square\)

<a id="ha-lca-15-lemma-6-2"></a>
**Lemma 6.2 — Two transfer principles.** If a closed subgroup \(H\) of an LCA frequency group \(\Gamma\) contains a nonsynthesis set, then that same set is a nonsynthesis set in \(\Gamma\). A nonsynthesis set in \(\mathbb T=\mathbb R/\mathbb Z\) also yields a closed nonsynthesis set in \(\mathbb R\).

**Proof.** We first prove that restriction
\[
 R:A(\Gamma)\longrightarrow A(H),\qquad F\longmapsto F|_H
                                                               \tag{37}
\]
is a bounded surjection. Put \(G=\widehat\Gamma\) and \(N=H^\perp\). The quotient duality of [HA-LCA-10, Theorem 2.1](subgroups-quotients-and-annihilators.md#ha-lca-10-theorem-2-1) identifies \(\widehat H\) with \(G/N\). Choose compatible Haar measures. The quotient averaging map
\[
 Pf(x+N)=\int_N f(x+n)\,dn
\]
is contractive from \(L^1(G)\) to \(L^1(G/N)\), and
\(\widehat{Pf}=\widehat f|_H\), by [HA-LCA-10, Theorem 4.1 and Lemma 5.0](subgroups-quotients-and-annihilators.md#ha-lca-10-lemma-5-0).

Here is the needed surjectivity with norm control. For \(u\in C_c(G/N)\), let \(C=\operatorname{supp}u\). Choose \(w\in C_c(G)\), \(w\ge0\), with \(Pw>0\) on \(C\). Such a function follows from [HA-LCA-10, Lemma 3.1](subgroups-quotients-and-annihilators.md#ha-lca-10-lemma-3-1): lift a compactly supported continuous cutoff which is one on \(C\), and take the absolute value of that lift. Define \(v=u/Pw\) where \(Pw>0\), and zero elsewhere. This is continuous and compactly supported, because \(Pw\) is positive on a neighbourhood of \(C\). If \(q:G\to G/N\) is the quotient map, the function \(f=w(v\circ q)\) belongs to \(C_c(G)\), and Weil's formula gives
\[
 Pf=u,\qquad \|f\|_1=\int_{G/N}|u|=\|u\|_1.
\]
For arbitrary \(u\in L^1(G/N)\), write \(u=\sum_{j\ge1}u_j\) with \(u_j\in C_c\) and \(\sum_j\|u_j\|_1<\infty\). To construct this series, take \(C_c\) approximants with errors at most \(2^{-j}\), and use their successive differences, the first approximant being the first term. Lift every \(u_j\) with the norm equality just proved and sum the lifts in \(L^1(G)\). Contractivity gives \(Pf=u\). This proves (37), without a measurable choice of representatives for quotient cosets.

Let \(E\subset H\) be closed and not a synthesis set there. Choose \(a\in\iota_H(E)\setminus j_H(E)\), and lift it by (37) to \(F\in A(\Gamma)\). Since \(F|_E=0\), synthesis of \(E\) in \(\Gamma\) would imply \(F\in j_\Gamma(E)\). But restriction takes functions vanishing on a neighbourhood of \(E\) in \(\Gamma\) to functions vanishing on a neighbourhood of \(E\) in \(H\); its boundedness and (11) imply \(Rj_\Gamma(E)\subset j_H(E)\). This contradicts \(RF=a\). Since \(H\) is closed, \(E\) is also closed in \(\Gamma\).

For the circle-to-line assertion, let \(\pi:\mathbb R\to\mathbb T\) be the quotient. We establish a bounded cutoff-periodization map. For \(c\in C_c^\infty(\mathbb R)\), put
\[
 P_cF(t+\mathbb Z)=\sum_{n\in\mathbb Z}c(t+n)F(t+n)
 \quad(F\in A(\mathbb R)).
\]
On \(0\le t\le1\) only finitely many terms occur, uniformly in \(t\), so this is continuous and periodic. If \(F=\widehat f\), its \(m\)-th circle Fourier coefficient is, by absolutely integrable Fubini,
\[
 \int_\mathbb R c(t)F(t)e^{-2\pi imt}\,dt
       =\int_\mathbb R f(x)\widehat c(m+x)\,dx.
\]
Lemma 5.0, with reflection, gives rapid decay of \(\widehat c\). Therefore
\[
 C_c:=\sup_{x\in\mathbb R}\sum_{m\in\mathbb Z}|\widehat c(m+x)|<\infty.
\]
Indeed the sum is periodic in \(x\), so restrict \(x\) to \([0,1]\) and use
\(|\widehat c(t)|\le C(1+|t|^2)^{-1}\) and \(|m+x|\ge|m|-1\).
It follows that these coefficients are absolutely summable, with sum at most \(C_c\|f\|_1\). Their uniformly convergent Fourier series equals \(P_cF\), by Fourier uniqueness on the circle. Thus
\[
 \|P_cF\|_{A(\mathbb T)}\le C_c\|F\|_{A(\mathbb R)}.       \tag{38}
\]

Choose a nonnegative \(b\in C_c^\infty(\mathbb R)\) which is positive on \([0,1]\). The locally finite sum \(s(t)=\sum_n b(t+n)\) is smooth, periodic and everywhere positive. Set \(b_0=b/s\); then \(b_0\in C_c^\infty\) and
\(\sum_n b_0(t+n)=1\). Choose \(c\in C_c^\infty\) equal to one on \(\operatorname{supp}b_0\).

For \(a\in A(\mathbb T)\), the function
\[
 F(t)=b_0(t)a(\pi t)
\]
belongs to \(A(\mathbb R)\). In fact, expand \(a\) in its absolutely convergent Fourier series; multiplication of \(b_0\) by a character is an isometry of \(A(\mathbb R)\), so the series converges in that norm with bound \(\|b_0\|_A\|a\|_A\). Also \(P_cF=a\).

Now take a closed nonsynthesis set \(E\subset\mathbb T\) and \(a\in\iota(E)\setminus j(E)\). The associated \(F\) vanishes on the closed set \(E'=\pi^{-1}E\). If \(E'\) admitted synthesis, (11) would approximate \(F\) in \(A(\mathbb R)\) by \(F_j\) vanishing on open neighbourhoods \(U_j\supset E'\). Each \(P_cF_j\) vanishes on a neighbourhood of \(E\). To see this precisely, the set
\(\pi(\operatorname{supp}c\setminus U_j)\) is compact and disjoint from \(E\); on its open complement, every nonzero summand in \(P_cF_j\) is zero. Hence \(P_cF_j\in j(E)\). By (38) their limit is \(P_cF=a\), a contradiction. Thus \(E'\) is a nonsynthesis set in \(\mathbb R\). \(\square\)

<a id="ha-lca-15-theorem-6-3"></a>
**Theorem 6.3 — Malliavin.** Every nondiscrete LCA frequency group \(\Gamma\) has a closed nonsynthesis set. Equivalently, for every noncompact LCA group \(G\), some closed ideal of \(L^1(G)\) differs from the kernel of its hull.

**Proof.** The [full structure theorem, HA-LCA-12, Corollary 4.4](the-structure-of-locally-compact-abelian-groups.md#ha-lca-12-corollary-4-4), gives
\(\Gamma\cong\mathbb R^a\times H\), where \(H\) has a compact open subgroup \(K\). If \(a>0\), \(\Gamma\) contains a closed copy of \(\mathbb R\). Theorem 6.1 gives a nonsynthesis set on the infinite compact circle; Lemma 6.2 transfers it to \(\mathbb R\), then to \(\Gamma\). If \(a=0\), the compact open subgroup \(K\) must be infinite. Otherwise its finite Hausdorff topology would be discrete; since it is open, the identity would be open in \(\Gamma\), making \(\Gamma\) discrete. Apply Theorem 6.1 to \(K\) and then the closed-subgroup part of Lemma 6.2.

Finally [HA-LCA-09, Corollary 4.4](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-4) says that \(\widehat G\) is discrete exactly when \(G\) is compact. Fourier transform is an isometric algebra isomorphism \(L^1(G)\to A(\widehat G)\); for a nonsynthesis set \(E\), its minimal ideal has hull \(E\) and differs from \(\iota(E)\), by Lemma 3.0. This proves the equivalent formulation. \(\square\)

## 7. Exercises with complete solutions

<a id="ha-lca-15-exercise-7-1"></a>
**Exercise 7.1 — The limit space.** For fixed \(\phi\in L^\infty(G)\) and \(a\in\mathbb C\), prove directly that the kernels satisfying (4) form a closed translation-invariant linear subspace.

**Solution.** Linearity follows by intersecting the finitely many complements of compact exceptional sets, equivalently by taking their finite union as one exceptional set. If \(g_n\to g\) in \(L^1\), then
\[
 \|(g-g_n)*\phi-a\!\int(g-g_n)\|_\infty
 \le(\|\phi\|_\infty+|a|)\|g-g_n\|_1.
\]
Given an error tolerance, first choose \(n\) making this bound small, then use the limiting property of \(g_n\). This proves closedness. The identity
\((L_yg)*\phi(x)=(g*\phi)(x-y)\), together with invariance of \(\int g\), proves translation invariance, because a translate of a compact set is compact. These calculations use Lemma 1.0 and do not require a countable exhaustion of \(G\). \(\square\)

<a id="ha-lca-15-exercise-7-2"></a>
**Exercise 7.2 — Logarithmic averages.** Let \(A\) be bounded measurable. If, for one \(\alpha>0\),
\[
 \frac{\alpha}{T^\alpha}\int_0^T t^{\alpha-1}A(t)\,dt
        \longrightarrow a\quad(T\to\infty),
\]
prove the same assertion for every \(\beta>0\), and prove convergence of the Abel means to \(a\). Give a sufficient condition for \(A(t)\to a\).

**Solution.** Put \(\phi(x)=A(e^x)\) and
\(k_\alpha(s)=\alpha e^{-\alpha s}1_{[0,\infty)}(s)\).
Elementary integration gives
\[
 \int k_\alpha=1,\qquad
 \widehat k_\alpha(\xi)=\frac{\alpha}{\alpha+2\pi i\xi}\ne0.
\]
The substitution \(t=e^{x-s}\) gives
\[
 k_\alpha*\phi(x)
       =\alpha e^{-\alpha x}\int_0^{e^x}t^{\alpha-1}A(t)\,dt.
\]
The hypothesis is thus a one-sided limit for a regular kernel. The closed translation-space proof in Corollary 2.2, now starting with \(k_\alpha\), transfers it to every \(g\in L^1(\mathbb R)\). Taking \(g=k_\beta\) proves the assertion for every \(\beta>0\). Taking \(g=k\) from Lemma 2.1 proves the Abel assertion. A sufficient pointwise condition is the multiplicative slow-oscillation condition in Corollary 2.2; its proof uses a small positive convolution kernel and gives \(A(t)\to a\). \(\square\)

<a id="ha-lca-15-exercise-7-3"></a>
**Exercise 7.3 — One frequency.** Prove that \(\{\gamma_0\}\) admits synthesis and identify a co-ideal with precisely that spectrum.

**Solution.** A singleton is closed discrete in the Hausdorff group \(\Gamma\), so Corollary 3.3 gives \(j(\{\gamma_0\})=\iota(\{\gamma_0\})\). The co-ideal is the one-dimensional space \(\mathbb C\gamma_0=\tau(\{\gamma_0\})\). To verify weak-star closedness explicitly, choose \(f\) with \(\widehat f(\gamma_0)=1\), using a Fourier plateau. If a net \(a_i\gamma_0\) converges weak-star to \(\phi\), pairing with \(f\) gives \(a_i\to a=\langle f,\phi\rangle\). Pairing with arbitrary \(g\) then gives \(\langle g,\phi\rangle=a\widehat g(\gamma_0)\), so the full-Haar dual identification implies \(\phi=a\gamma_0\). Translates are scalar multiples, proving invariance. Proposition 4.1 and the hull of \(\iota(\{\gamma_0\})\) show that its spectrum is exactly the singleton. \(\square\)

<a id="ha-lca-15-exercise-7-4"></a>
**Exercise 7.4 — The sphere derivative and a closed ideal.** In \(\mathbb R^3\), use ordinary surface measure on \(S^2\) to carry out the derivative construction with the forward Fourier convention. Specify a closed ideal, not merely a derivative condition on a smaller domain.

**Solution.** With \(\mu_3=4\pi\sigma_3\), Lemma 5.1 gives
\[
 \widehat{\mu_3}(x)=2\frac{\sin(2\pi|x|)}{|x|},\qquad
 \Phi_3(x)=-2\pi ix_1\widehat{\mu_3}(x)
          =-4\pi i\frac{x_1}{|x|}\sin(2\pi|x|).
\]
Use \(\widehat{\mu_3}(0)=4\pi\) and \(\Phi_3(0)=0\).
Then \(\|\Phi_3\|_\infty\le4\pi\). For \(f,x_1f\in L^1\), differentiation of the forward transform gives, with a plus sign,
\[
 \int f(x)\Phi_3(x)\,dx
        =\int_{S^2}\partial_1\widehat f(\xi)\,d\mu_3(\xi).
\]
The closed ideal is
\[
 J=j(S^2)=
   \overline{\{f\in L^1:
       \operatorname{supp}\widehat f
           \text{ compact and disjoint from }S^2\}}^{\,L^1}.
\]
Lemma 3.0 proves closedness, the ideal property and its exact hull. The cutoff-convolution argument in Theorem 5.2 applies to the bounded functional \(f\mapsto\int f\Phi_3\) and proves that it vanishes on \(J\), including elements without first moments. For the explicit witness
\(F(\xi)=(|\xi|^2-1)\xi_1\beta(\xi)\), \(\beta=1\) near \(S^2\), its inverse transform lies in \(\iota(S^2)\), but the functional has value
\(2\int_{S^2}\xi_1^2\,d\mu_3=8\pi/3\).
Thus \(J\ne\iota(S^2)\). No assertion that an unbounded derivative operation is continuous on all of \(L^1\) is required. \(\square\)

## Source correspondence and proved inputs

The local perfect-set argument is developed from Shu's Theorems 2.23–2.26 and the fully proved local approximation results of HA-LCA-14. The regular-family, uniform and window statements correspond to the specified version of Fulsche–Luef–Werner; (6)–(7) fix all reflections and phases explicitly. The sphere construction follows Schwartz's free 1951 paper, while Lemmas 5.0–5.1 supply the smoothness and decay arguments used here. The three group-theoretic cases and the level-set mechanism come from Malliavin's free original paper; Lemmas 6.0a–6.0c prove the scalar regularity, coefficient bounds and diagonal construction in full. Using real parts of characters makes the coefficient argument valid also at order two. Lemma 0.1 provides the functional extension and separation needed for co-ideals.

Every imported mathematical result has an exact earlier programme locator in its proof. Neither a source citation nor an external theorem stated without proof replaces a proof in this lesson.
