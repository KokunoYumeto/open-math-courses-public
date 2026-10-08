# The Fourier inversion theorem and the dual Haar measure

**Lesson HA-LCA-07.** Self-checked by the writing AI.

Fix a locally compact Hausdorff abelian group \(G\) and a Haar measure \(dx\) on its complete locally determined domain. No countability assumption is made. Its dual \(\Gamma=\widehat G\) is locally compact by [HA-LCA-02, Theorem 5.2](characters-and-the-dual-group.md#ha-lca-02-theorem-5-2). We write \(G\) additively and multiply characters in \(\Gamma\). Our conventions are
\[
 \widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,dx,
 \qquad T\mu(x)=\int_\Gamma\gamma(x)\,d\mu(\gamma).
 \tag{1}
\]
By [HA-LCA-06, Proposition 4.1](bochners-theorem.md#ha-lca-06-proposition-4-1), every \(f\in B(G)\) has a unique finite complex Radon measure \(\mu_f\) with \(f=T\mu_f\), and
\(\|f\|_{B(G)}=\|\mu_f\|\). Put \(B^1(G)=B(G)\cap L^1(G,dx)\). Members of \(B(G)\) are actual bounded continuous functions. If such functions are equal almost everywhere, they agree everywhere: a nonzero continuous difference is bounded away from zero on some nonempty open set, which has positive Haar measure.

The freely accessible source for the construction is D. H. Fremlin, [*Measure Theory*, §445P–Q, version of 20 March 2008](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex). We give the measure-representation step on arbitrary groups and extend the argument from integrable positive-type functions to all of \(B^1(G)\). The sign in (1) determines every formula below.

Written by GPT-6 Astra (OpenAI), Ultra, October 2026. Original text: public domain (CC0). Fremlin's copyright 1998 and original notices are retained in the unchanged original source package.

The exact earlier proof tools are these:

- [HA-LCA-03, Theorem 3.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-theorem-3-1) gives the transform, translation, modulation, convolution and involution laws; its [Corollary 2.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-corollary-2-2) gives \(\widehat f\in C_0(\Gamma)\), and its [Lemma 4.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-4-1) identifies the Radon measure and variation of an \(L^1\) density.
- [HA-LCA-04, Proposition 2.2](functions-of-positive-type.md#ha-lca-04-proposition-2-2) proves positivity of autocorrelations. Its [Exercise 7.1](functions-of-positive-type.md#ha-lca-04-exercise-7-1) proves that products of positive-type functions have positive type. [HA-LCA-06, Theorem 2.1](bochners-theorem.md#ha-lca-06-theorem-2-1) is Bochner's theorem, including the mass formula \(\mu_f(\Gamma)=f(0)\) for positive-type \(f\); its [Proposition 1.1](bochners-theorem.md#ha-lca-06-proposition-1-1) proves injectivity of \(T\).
- [The Haar reading, Theorem 3.1](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-theorem-3-1) proves positive \(C_c\) representation on every sigma-compact locally compact Hausdorff space. [The general Haar reading, Lemma 1.1 and Theorems 3.1–3.3](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-1-1) proves the open sigma-compact subgroup construction, full-domain Haar existence, uniqueness and uniqueness from \(C_c\) integrals. Its [Lemma 5.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-5-1) proves \(C_c\)-density in \(L^1\).
- [The finite-Radon reading, Lemmas 1.3 and 1.6](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3) supplies cutoffs and compact-product continuity. Its [Theorem 4.3](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-theorem-4-3) includes finite complex Radon uniqueness. [The product reading, Corollary 2.3](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-corollary-2-3) proves Fubini after restricting both variables to compact sets; its [Proposition 3.1](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-proposition-3-1) proves pushforward and substitution. [The integration reading, Theorem 1.2 and Lemma 2.1](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-1-2) proves monotone convergence and the complex integral estimates.

## 1. Local denominators and compatible measures

We first supply the representation step that will turn an invariant integral into a Haar measure without requiring the whole group to be sigma-compact.

<a id="ha-lca-07-lemma-1-0"></a>
**Lemma 1.0 — An invariant positive integral.** Let \(S\) be a locally compact Hausdorff group. Every nonzero positive complex-linear functional \(J:C_c(S)\to\mathbb C\) invariant under left translation is integration against a unique Haar measure on the full complete locally determined domain.

**Proof.** Positivity means \(Jv\ge0\) for real \(v\ge0\). It implies that \(J\) is real on real functions, by their positive and negative parts. If \(K\) is compact, choose a cutoff \(w\ge0\) equal to one on \(K\). For \(v\) supported in \(K\), choose a complex scalar \(\zeta\) of modulus one with \(\zeta Jv=|Jv|\), unless \(Jv=0\), when no estimate is needed. Pointwise,
\(\operatorname{Re}(\zeta v)\le\|v\|_\infty w\), and hence
\[
 |Jv|\le J(w)\|v\|_\infty.
\]
Thus the restriction to each fixed compact support is bounded.

Choose an open, closed, sigma-compact subgroup \(H\) of \(S\), as in the general Haar reading, Lemma 1.1. Extend \(C_c(H)\) by zero and restrict \(J\) to obtain \(J_H\). Every compact set in \(S\) meets only finitely many left cosets \(rH\), since these cosets form a disjoint open cover. Consequently every \(v\in C_c(S)\) is a finite sum of the translates of functions \(v_r(h)=v(rh)\) in \(C_c(H)\). Left invariance gives
\[
 Jv=\sum_r J_H(v_r).
\]
Since \(J\ne0\), the functional \(J_H\) is nonzero.

The proved sigma-compact representation theorem supplies a nonzero positive Borel measure \(\nu_H\), finite on compact sets and regular, with \(J_Hv=\int_Hv\,d\nu_H\). Its uniqueness shows that \(\nu_H\) is left invariant: translation of the representing measure has the same \(C_c\) integrals. Complete this measure. Fix any full-domain Haar measure \(\nu_0\) on \(S\), whose existence was proved in the general Haar reading. Its restriction to \(H\) is a nonzero Haar measure; uniqueness on \(H\) gives
\(\nu_H=c\,\nu_0|_H\), with \(c>0\). Both completions on \(H\) are the ordinary Borel completion, as proved in that reading, Lemma 5.1.

The finite coset decomposition now gives \(Jv=c\int_Sv\,d\nu_0\) for every \(v\in C_c(S)\). Thus the full-domain measure \(c\nu_0\) represents \(J\). Haar uniqueness on \(S\), followed by evaluation on one nonnegative \(C_c\) function of positive integral, gives uniqueness. This argument constructs the required full-domain measure from the already proved Haar measure; it assumes no global \(C_c\) representation theorem. \(\square\)

Write \(\widetilde g(x)=\overline{g(-x)}\), and let \(P(G)\) denote the continuous functions of positive type.

<a id="ha-lca-07-lemma-1-1"></a>
**Lemma 1.1.** For every compact \(K\subseteq\Gamma\), there is \(h\in C_c(G)\cap P(G)\) such that \(\widehat h\ge0\) everywhere and \(\widehat h>0\) on \(K\). One can arrange \(h(0)>0\).

**Proof.** Choose a nonzero nonnegative \(u\in C_c(G)\), using a cutoff at the identity. Haar positivity on nonempty open sets gives \(\int u>0\). For each \(\gamma_0\in K\cup\{1\}\), put \(g_{\gamma_0}=\gamma_0 u\). Then
\(\widehat {g_{\gamma_0}}(\gamma_0)=\int u>0\).
Continuity of its transform gives a neighbourhood \(W_{\gamma_0}\) on which that transform is nonzero. Choose finitely many of these neighbourhoods covering \(K\cup\{1\}\), and let \(g_1,\ldots,g_m\) be the corresponding functions. Set
\[
 h=\sum_{j=1}^m g_j*\widetilde g_j.
 \tag{2}
\]
Each summand is continuous, has support in the compact set
\(\operatorname{supp}g_j-\operatorname{supp}g_j\), and has positive type by the autocorrelation proposition. A finite sum has positive type by addition of its defining nonnegative quadratic forms. The transform laws give
\[
 \widehat h=\sum_{j=1}^m|\widehat g_j|^2.
\]
At least one term is positive at each point of \(K\). Finally,
\(h(0)=\sum_j\int|g_j|^2>0\). Including the trivial character in the cover also handles \(K=\varnothing\). Only compactness of \(K\), not sigma-compactness of \(G\), has been used. \(\square\)

<a id="ha-lca-07-lemma-1-2"></a>
**Lemma 1.2.** For \(f,g\in B^1(G)\), the following finite complex Radon measures on \(\Gamma\) are equal:
\[
 \widehat f\,\mu_g=\widehat g\,\mu_f.
 \tag{3}
\]

**Proof.** Bounded continuous weights times finite complex Radon measures are finite complex Radon measures. Indeed their total variations are dominated by a constant times the original variation, and the finite-product reading, Lemma 1.2, proves that the resulting positive parts are Radon.

For \(f\in L^1(G)\), \(g=T\mu_g\in B(G)\), and every \(x\in G\), direct integration gives
\[
 T(\widehat f\,\mu_g)(x)
 =\int_G f(y)\int_\Gamma\gamma(x-y)\,d\mu_g(\gamma)\,dy
 =\int_Gf(y)g(x-y)\,dy.
 \tag{4}
\]
Here is a justification that does not impose sigma-finiteness. First take \(f\in C_c(G)\) and restrict \(\mu_g\) to a compact set. The pairing kernel is continuous by HA-LCA-02, Proposition 1.4, and compact-localized Radon Fubini proves the identity. Remove the measure restriction using the bound
\(\|f\|_1|\mu_g|(\Gamma\setminus C)\), which tends to zero along compact tails. Then approximate an arbitrary \(L^1\) function by \(C_c\) functions. On either side the error is at most \(\|f-f_j\|_1\|\mu_g\|\). The same estimates show that all fixed-\(x\) integrals are absolutely convergent and independent of the \(L^1\) representative.

For \(f,g\in B^1(G)\), both functions are bounded and integrable. Substitution \(y\mapsto x-y\), which preserves Haar measure by the earlier inversion and translation theorem, interchanges their convolution integrals at every \(x\). Thus (4) gives
\(T(\widehat f\,\mu_g)=T(\widehat g\,\mu_f)\).
Injectivity of \(T\) proves (3). \(\square\)

## 2. Constructing the dual Haar integral

<a id="ha-lca-07-theorem-2-1"></a>
**Theorem 2.1 — Fourier inversion on \(B^1(G)\).** There is a unique Haar measure \(d\xi\) on \(\Gamma\) for which every \(f\in B^1(G)\) satisfies
\[
 \widehat f\in L^1(\Gamma,d\xi),\qquad
 \mu_f=\widehat f\,d\xi,\qquad
 f(x)=\int_\Gamma\widehat f(\gamma)\gamma(x)\,d\xi(\gamma)
 \quad(x\in G).
 \tag{5}
\]
In particular \(\int_\Gamma|\widehat f|\,d\xi=\|f\|_{B(G)}\).

**Proof.** For \(q\in C_c(\Gamma)\), choose \(h\) from Lemma 1.1 with \(\widehat h>0\) on \(\operatorname{supp}q\), and define
\[
 I(q)=\int_\Gamma\frac{q}{\widehat h}\,d\mu_h.
 \tag{6}
\]
The quotient is set to zero off \(\operatorname{supp}q\). It is continuous and compactly supported: the denominator is positive on a neighbourhood of this compact support and has a positive lower bound there after shrinking that neighbourhood, while the numerator vanishes off its support. Bochner makes \(\mu_h\) positive.

If \(k\) is another such choice, the compactly supported continuous function
\(q/(\widehat h\,\widehat k)\) and (3) give
\[
 \int\frac q{\widehat h}\,d\mu_h
 =\int\frac q{\widehat h\,\widehat k}\widehat k\,d\mu_h
 =\int\frac q{\widehat h\,\widehat k}\widehat h\,d\mu_k
 =\int\frac q{\widehat k}\,d\mu_k.
 \tag{7}
\]
Thus \(I\) is well defined. Choosing one denominator for the union of two compact supports proves additivity; the same choice proves complex homogeneity. For \(q\ge0\), (6) is nonnegative.

We prove that \(I\) is nonzero before using any full-support property of its representing measure. Choose \(a\in C_c(G)\cap P(G)\) as in Lemma 1.1, so \(\mu_a(\Gamma)=a(0)>0\). Finite Radon inner regularity supplies a compact set \(C\) with \(\mu_a(C)>0\), and a nonnegative cutoff \(q\) equal to one there has \(\int q\,d\mu_a>0\). Choose \(h\) positive on \(\operatorname{supp}q\). The compatibility identity gives
\[
 I(q\widehat a)
 =\int\frac{q\widehat a}{\widehat h}\,d\mu_h
 =\int q\,d\mu_a>0.
 \tag{8}
\]

For \(\eta\in\Gamma\), put \(h_\eta(x)=\eta(x)h(x)\). Multiplication by a character preserves positive type: in the defining quadratic form replace each coefficient \(c_j\) by \(c_j\eta(x_j)\). Moreover
\[
 \widehat {h_\eta}(\gamma)=\widehat h(\eta^{-1}\gamma),
 \qquad \mu_{h_\eta}=(\gamma\mapsto\eta\gamma)_*\mu_h.
 \tag{9}
\]
The first identity is the modulation law. For the second, applying \(T\) to the displayed pushforward gives \(\eta h\); pushforward is Radon and \(T\) is injective. If \(q_\eta(\gamma)=q(\eta^{-1}\gamma)\), then \(h_\eta\) is a permissible denominator for \(q_\eta\). Substitution in (6) gives \(I(q_\eta)=I(q)\). Lemma 1.0 now provides a nonzero full-domain Haar measure \(d\xi\) representing \(I\).

Fix an arbitrary, possibly complex, \(f\in B^1(G)\). Given \(q\in C_c(\Gamma)\), choose a denominator positive on \(\operatorname{supp}q\). Equations (3) and (6) yield
\[
 \int_\Gamma q\widehat f\,d\xi
 =I(q\widehat f)
 =\int_\Gamma\frac{q\widehat f}{\widehat h}\,d\mu_h
 =\int_\Gamma q\,d\mu_f.
 \tag{10}
\]
We must prove \(\widehat f\) integrable before identifying its measure. Given compact \(K\subseteq\Gamma\), choose \(v\in C_c(\Gamma)\) with \(0\le v\le1\) and \(v=1\) on \(K\). For \(\varepsilon>0\), use
\[
 q_\varepsilon
 =v\,\frac{\overline{\widehat f}}{|\widehat f|+\varepsilon}
 \quad\text{in (10).}
\]
This is a compactly supported continuous function of modulus at most one, so
\[
 0\le\int v\,\frac{|\widehat f|^2}{|\widehat f|+\varepsilon}\,d\xi
 =\int q_\varepsilon\,d\mu_f\le\|\mu_f\|.
 \tag{11}
\]
The middle integral is real and nonnegative because it equals the first one; the final inequality follows from its absolute-value bound. Letting \(\varepsilon\) decrease to zero and applying monotone convergence gives
\(\int_K|\widehat f|\,d\xi\le\|\mu_f\|\).
Since \(\widehat f\in C_0(\Gamma)\), the sets
\(K_n=\{|\widehat f|\ge1/n\}\) are compact and increase to the set where \(\widehat f\ne0\). A second monotone convergence argument gives
\(\int_\Gamma|\widehat f|\,d\xi\le\|\mu_f\|<\infty\).

Apply the already proved \(L^1\)-density measure theorem, HA-LCA-03, Lemma 4.1, to the LCA group \(\Gamma\) with Haar measure \(d\xi\). It makes \(\widehat f\,d\xi\) a finite complex Radon measure whose variation norm is \(\int|\widehat f|\,d\xi\). Identity (10) and uniqueness of finite Radon measures from \(C_c\) integrals imply
\(\mu_f=\widehat f\,d\xi\).
Here \(C_c\) tests suffice because they are uniformly dense in \(C_0\). Applying \(T\) proves (5) at every point, and equality of variation norms proves the norm assertion.

Finally any other Haar measure on \(\Gamma\) is \(b\,d\xi\) for some \(b>0\). Choose the nonzero \(a\) used in (8). Inversion at zero gives
\(a(0)=\int\widehat a\,d\xi>0\);
if inversion also holds for \(b\,d\xi\), it forces \(b=1\). This proves uniqueness. \(\square\)

We call \(d\xi\) the **dual Haar measure** of \(dx\). The complex argument (10)–(11) is needed: being a linear combination of positive-type functions does not by itself show that the individual positive-type summands are integrable.

## 3. Products, scaling and classical normalizations

<a id="ha-lca-07-lemma-3-0"></a>
**Lemma 3.0 — Products on the full Haar domain.** Let \(G_1,G_2\) be LCA groups with Haar measures \(dx_1,dx_2\). There is a unique full-domain Haar measure \(dx_1\otimes dx_2\) such that every \(v\in C_c(G_1\times G_2)\) has integral equal to either iterated integral. If \(d\xi_j\) is dual to \(dx_j\), then \(d\xi_1\otimes d\xi_2\) is dual to \(dx_1\otimes dx_2\), under the product identification of the duals.

**Proof.** The product group is Hausdorff and locally compact: products of compact neighbourhoods are compact neighbourhoods, by the finite-product compactness theorem in the finite-Radon reading, Lemma 1.6. For \(v\in C_c(G_1\times G_2)\), compact localization makes the two iterated integrals finite and equal. The inner integral is continuous with compact support: restrict to the compact support projections and use continuity of integration of a continuous kernel against a finite Radon measure, proved in the product reading, Lemma 1.1. The resulting functional of \(v\) is complex linear and positive. Translating either variable leaves it invariant. It is nonzero, since a product of two nonzero nonnegative \(C_c\) functions has integral the product of two positive numbers. Lemma 1.0 supplies its unique full-domain Haar measure. This is the meaning of the product notation here.

We also need the factor integral for nonnegative \(a\in C_0(G_1)\), \(b\in C_0(G_2)\) with finite integrals. Choose \(u_n\in C_c(G_1)\), \(0\le u_n\le1\), equal to one on \(\{a\ge1/n\}\); when this set is empty one may choose zero. Replace \(u_n\) by \(\max_{j\le n}u_j\). Then \(a_n=au_n\) is an increasing sequence of nonnegative \(C_c\) functions converging to \(a\). Construct \(b_n\) in the same way. Their products increase to \(a(x_1)b(x_2)\). The \(C_c\) formula and monotone convergence in each space give
\[
 \int a(x_1)b(x_2)\,d(dx_1\otimes dx_2)
 =\left(\int a\,dx_1\right)\left(\int b\,dx_2\right).
 \tag{12}
\]
No assertion about a product sigma-algebra is needed for this argument.

The topological identification
\(\widehat{G_1\times G_2}=\widehat G_1\times\widehat G_2\), with pairing
\((\gamma_1,\gamma_2)(x_1,x_2)=\gamma_1(x_1)\gamma_2(x_2)\),
was proved in [HA-LCA-02, Proposition 4.1](characters-and-the-dual-group.md#ha-lca-02-proposition-4-1).
Construct \(d\xi_1\otimes d\xi_2\) by the first part of the proof on these dual groups. By Haar uniqueness, the actual dual of \(dx_1\otimes dx_2\) is \(c(d\xi_1\otimes d\xi_2)\) for some \(c>0\).

Choose nonzero positive autocorrelations \(h_j\in C_c(G_j)\) as in Lemma 1.1. The product
\(h(x_1,x_2)=h_1(x_1)h_2(x_2)\) has positive type: pulling back a positive-type function along a homomorphism preserves each defining nonnegative quadratic form, and products preserve positive type. Thus \(h\in B^1(G_1\times G_2)\). Compact-localized integration gives
\[
 \widehat h(\gamma_1,\gamma_2)
 =\widehat h_1(\gamma_1)\widehat h_2(\gamma_2).
\]
Each factor is nonnegative, belongs to \(C_0\cap L^1\), and has integral \(h_j(0)>0\), by Lemma 1.1 and Theorem 2.1. Equation (12), applied on the duals, now gives
\[
 \int\widehat h\,d(\xi_1\otimes\xi_2)=h_1(0)h_2(0)=h(0)>0.
\]
Inversion for \(h\) with the actual dual measure forces \(c=1\). Iterating proves the corresponding assertions for any finite product. \(\square\)

<a id="ha-lca-07-proposition-3-1"></a>
**Proposition 3.1 — Scaling.** If \(dx\) is replaced by \(c\,dx\), \(c>0\), then the dual Haar measure is \(c^{-1}d\xi\).

**Proof.** The integrable classes and \(B(G)\) are unchanged, and the new transform is \(\widehat f_c=c\widehat f\). Thus \(\widehat f_c\) is integrable against \(c^{-1}d\xi\) and
\[
 \int_\Gamma \widehat f_c(\gamma)\gamma(x)c^{-1}\,d\xi(\gamma)=f(x)
 \quad(f\in B^1(G)).
\]
The uniqueness clause of Theorem 2.1 proves the assertion. \(\square\)

<a id="ha-lca-07-proposition-3-2"></a>
**Proposition 3.2 — Euclidean constants.** Ordinary Lebesgue measure on \(\mathbb R^n\) is self-dual for the pairing \(e^{2\pi i x\cdot\xi}\). For the pairing \(e^{i x\cdot s}\), its dual measure is \((2\pi)^{-n}ds\).

**Proof.** The real-dual homeomorphism was proved in [HA-LCA-02, Theorem 3.1](characters-and-the-dual-group.md#ha-lca-02-theorem-3-1), and its Lemma 3.3 constructed Lebesgue Haar measure and affine substitution. Therefore in dimension one the dual is \(a\,d\xi\) for some \(a>0\).

The function \(h(x)=e^{-\pi x^2}\) is positive type: the positive Gaussian \(e^{-t^2}\) of [HA-LCA-04, Example 6.1](functions-of-positive-type.md#ha-lca-04-example-6-1) is pulled back under \(x\mapsto\sqrt\pi x\), which preserves its defining quadratic forms. The full Gaussian calculation in [the real-variable reading, Theorem 2.1](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-theorem-2-1) gives
\[
 \widehat h(\xi)=e^{-\pi\xi^2},
 \qquad \int_{\mathbb R}e^{-\pi\xi^2}\,d\xi=1.
\]
Inversion at zero gives \(1=h(0)=a\), fixing the dual constant.

The product measure of \(n\) copies of one-dimensional Lebesgue measure is ordinary Lebesgue measure on \(\mathbb R^n\): its iterated integral gives the volume of rectangular boxes, and the sigma-finite Radon product construction in [the integration reading, Theorem 4.4](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-4-4) gives precisely this Borel measure. The theorem gives inner regularity on finite-measure Borel sets. Intersecting any Borel set with the increasing compact boxes \([-k,k]^n\) and using measure continuity extends this to all Borel sets. Its \(C_c\) integrals agree with the product Haar measure constructed in Lemma 3.0, so uniqueness from \(C_c\) identifies their ordinary completions. Equivalently, this supplies the construction of \(n\)-dimensional Lebesgue measure from the one-dimensional one. Lemma 3.0 proves self-duality in dimension \(n\).

Finally \(e^{i x\cdot s}=e^{2\pi i x\cdot(s/(2\pi))}\). In each coordinate, affine substitution gives \(d\xi=ds/(2\pi)\); applying the product integral yields the factor \((2\pi)^{-n}\). Thus the conversion, with primal measure always \(dx\), is

| Pairing | Forward transform | Dual Haar measure |
|---|---|---|
| \(e^{2\pi i x\cdot\xi}\) | \(\int f(x)e^{-2\pi i x\cdot\xi}\,dx\) | \(d\xi\) |
| \(e^{i x\cdot s}\) | \(\int f(x)e^{-i x\cdot s}\,dx\) | \(ds/(2\pi)^n\) |

These are coordinate descriptions of the same character pairing. \(\square\)

<a id="ha-lca-07-proposition-3-3"></a>
**Proposition 3.3 — Compact, discrete and finite groups.** If \(G\) is compact and \(dx(G)=1\), its dual measure is counting measure on the discrete group \(\Gamma\). If \(G\) is discrete with counting measure, its dual is Haar probability measure on the compact group \(\Gamma\). In particular, if \(G\) is finite of order \(N\) with counting measure, every dual point has mass \(1/N\).

**Proof.** The compact/discrete assertions about the dual topology are [HA-LCA-02, Theorem 2.1](characters-and-the-dual-group.md#ha-lca-02-theorem-2-1). Suppose first that \(G\) is compact with mass one. For any nontrivial character \(\omega\), choose \(a\) with \(\omega(a)\ne1\). Translation invariance gives
\(\int_G\omega=\omega(a)\int_G\omega\), so its integral is zero. The trivial character has integral one. For any \(\chi\in\Gamma\), the function \(\chi\) has positive type, is integrable, and satisfies
\[
 \widehat\chi(\gamma)
 =\int_G\chi(x)\overline{\gamma(x)}\,dx
 =1_{\{\chi\}}(\gamma).
\]
Inversion at zero now gives \(\xi(\{\chi\})=1\). Compact sets in a discrete group are finite, so inner regularity gives counting measure on all sets, including uncountable ones with infinite measure.

For discrete \(G\), \(\delta_0=1_{\{0\}}\) is a compactly supported function of positive type; this follows from [HA-LCA-04, Example 6.3](functions-of-positive-type.md#ha-lca-04-example-6-3) with the open subgroup \(\{0\}\). With counting measure its transform is the constant one. Inversion at zero gives
\(1=\int_\Gamma1\,d\xi\).
Thus the dual is Haar probability measure. On a finite group, translation invariance gives equal mass to each dual point and [HA-LCA-01, Theorem 1.1](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-1-1) gives \(|\Gamma|=N\); hence each mass is \(1/N\).

More generally compact primal mass \(m\) gives \(m^{-1}\) times counting measure, by Proposition 3.1. Normalized counting measure on a finite primal group gives counting measure on its dual. \(\square\)

## 4. Positivity, Fourier series and the angular convention

<a id="ha-lca-07-corollary-4-1"></a>
**Corollary 4.1.** If a class \(f\in L^1(G)\) is of positive type, its unique continuous positive-type representative has \(\widehat f\ge0\) everywhere and
\(\int_\Gamma\widehat f\,d\xi=f(0)\).
If \(f\in B^1(G)\) and \(\widehat f=0\), then \(f=0\).

**Proof.** The continuous representative exists and is unique by [HA-LCA-04, Corollary 3.2](functions-of-positive-type.md#ha-lca-04-corollary-3-2). Its transform is unchanged by an almost-everywhere modification. Bochner makes \(\mu_f\) positive, and Theorem 2.1 identifies it with \(\widehat f\,d\xi\). To see pointwise nonnegativity, identity (10) gives a nonnegative real number whenever \(q\in C_c(\Gamma)\) is nonnegative. If the imaginary part of the continuous function \(\widehat f\) were nonzero somewhere, it would have a fixed strict sign on an open neighbourhood. A nonzero nonnegative cutoff supported there, whose integral is positive by full support of Haar measure, would give a nonreal value in (10), a contradiction. Hence \(\widehat f\) is real. If it were negative somewhere, the same cutoff argument would give a negative value. Thus \(\widehat f\ge0\). Inversion at zero gives its integral. The last assertion follows immediately from (5) for any \(B^1\) function. \(\square\)

<a id="ha-lca-07-example-4-2"></a>
**Example 4.2 — The integers and the circle.** Write \(\mathbb T=\{z:|z|=1\}\), with Haar probability measure \(dm(z)\) and pairing \(z^n\) with \(n\in\mathbb Z\). Then \(B^1(\mathbb Z)=\ell^1(\mathbb Z)\), and
\[
 \widehat f(z)=\sum_{n\in\mathbb Z}f(n)z^{-n},
 \qquad f(n)=\int_{\mathbb T}\widehat f(z)z^n\,dm(z).
 \tag{13}
\]
On \(\mathbb T\), \(B^1(\mathbb T)=B(\mathbb T)\). Its members are exactly the functions with an absolutely convergent Fourier series
\[
 f(z)=\sum_{n\in\mathbb Z}\widehat f(n)z^n,
 \qquad \widehat f(n)=\int_{\mathbb T}f(z)z^{-n}\,dm(z).
 \tag{14}
\]

**Proof.** The topological dual identifications are HA-LCA-02, Corollary 3.2; the Haar measures and circle orthogonality were proved in HA-LCA-03, Lemma 5.1. If \(f\in\ell^1(\mathbb Z)\), the first series in (13) converges uniformly, since its uniform tails are at most the corresponding \(\ell^1\) tails. It defines a continuous function \(h\) on the circle, and termwise integration against \(z^n\), justified by uniform convergence, gives \(\int h(z)z^n\,dm=f(n)\). Hence \(f=T(h\,dm)\in B(\mathbb Z)\), because \(h\,dm\) is a finite Radon measure. It is already integrable for counting measure, proving the claimed equality of spaces. Proposition 3.3 and Theorem 2.1 also give (13).

On the compact circle every bounded continuous function is integrable, so \(B^1=B\). Its dual measure is counting measure. Equation (5) says that the coefficients of a \(B\) function belong to \(\ell^1(\mathbb Z)\) and gives (14). The series is uniformly absolutely convergent by its \(\ell^1\) bound. Conversely every \(\ell^1\) family \((a_n)\) defines a finite complex Radon measure \(\sum_n a_n\delta_n\) on the discrete dual: countable additivity follows from absolute convergence, finite partial sums approximate its variation on every set, and finite sets are compact. Its transform is the uniformly convergent series \(\sum_na_nz^n\), which therefore belongs to \(B(\mathbb T)\). Termwise orthogonality gives \(\widehat f(n)=a_n\). This assertion concerns \(B(\mathbb T)\); no absolute-convergence assertion for arbitrary continuous functions is required. \(\square\)

<a id="ha-lca-07-example-4-3"></a>
**Example 4.3 — Finite groups.** If \(G\) is finite of order \(N\) and the primal measure is counting measure, then
\[
 \widehat f(\gamma)=\sum_{x\in G}f(x)\overline{\gamma(x)},\qquad
 f(x)=\frac1N\sum_{\gamma\in\Gamma}\widehat f(\gamma)\gamma(x).
 \tag{15}
\]
With normalized counting measure on \(G\), the forward sum has factor \(1/N\) and the inverse sum has no factor.

**Proof.** Every function on \(G\) belongs to \(B^1(G)\). Indeed the character basis and inversion proved in HA-LCA-01, Theorem 2.1 and Theorem 2.2, express it as a finite linear combination of characters, each the transform of a point mass on the dual. Proposition 3.3 gives the factor \(1/N\) in (5). Scaling by \(1/N\) on the primal side and Proposition 3.1 give the second convention. Thus (15) agrees with the earlier finite-dimensional calculation. \(\square\)

<a id="ha-lca-07-example-4-4"></a>
**Example 4.4 — The angular-frequency convention.** With primal measure \(dt\) on \(\mathbb R\) and characters \(t\mapsto e^{ist}\), the formulas are
\[
 \widehat f(s)=\int_{\mathbb R}f(t)e^{-ist}\,dt,
 \qquad
 f(t)=\frac1{2\pi}\int_{\mathbb R}\widehat f(s)e^{ist}\,ds
 \quad(f\in B^1(\mathbb R)).
 \tag{16}
\]

**Proof.** Proposition 3.2 gives dual measure \(ds/(2\pi)\); substitution in Theorem 2.1 gives (16). As a direct check, the Gaussian computation gives
\(\widehat {e^{-t^2}}(s)=\sqrt\pi\,e^{-s^2/4}\).
Its integral against \(ds/(2\pi)\) is
\((\sqrt\pi/(2\pi))\,2\sqrt\pi=1\), as required by its value at zero. In calculations that use these characters, the measure in a dual integral is therefore \(ds/(2\pi)\). \(\square\)

## 5. Exercises with complete solutions

<a id="ha-lca-07-exercise-5-1"></a>
**Exercise 5.1 — Direct integer normalization.** Starting from counting measure on \(\mathbb Z\), show directly that its dual is normalized Haar measure on \(\mathbb T\).

**Solution.** For any \(f\in\ell^1(\mathbb Z)\), uniform convergence and circle orthogonality give
\[
 \int_{\mathbb T}\left(\sum_k f(k)z^{-k}\right)z^n\,dm(z)
 =\sum_k f(k)\int_{\mathbb T}z^{n-k}\,dm(z)=f(n).
\]
The transform is continuous and hence \(m\)-integrable. Example 4.2 proves \(B^1(\mathbb Z)=\ell^1(\mathbb Z)\), so \(m\) has exactly the inversion property that defines the dual Haar measure. Theorem 2.1 gives uniqueness. Already \(f=\delta_0\) forces total dual mass one. \(\square\)

<a id="ha-lca-07-exercise-5-2"></a>
**Exercise 5.2 — Finite products.** If \(dx_j\) and \(d\xi_j\) are dual pairs, prove that the product dual measure is the dual of the product primal measure, without a sigma-finiteness assumption.

**Solution.** Use the full-domain product Haar measures constructed from compactly supported iterated integrals in Lemma 3.0. The dual group identification is a homeomorphism, so Haar uniqueness makes the unknown dual measure \(c(d\xi_1\otimes d\xi_2)\). Choose nonzero \(h_j\in C_c(G_j)\cap P(G_j)\) by Lemma 1.1. The product \(h=h_1h_2\), with separate variables, belongs to \(B^1(G_1\times G_2)\), has transform \(\widehat h_1\widehat h_2\), and \(h(0)=h_1(0)h_2(0)>0\). Each transform is nonnegative and integrable. The increasing compact-cutoff calculation (12) yields
\[
 \int\widehat h\,d(\xi_1\otimes\xi_2)
 =\left(\int\widehat h_1\,d\xi_1\right)
  \left(\int\widehat h_2\,d\xi_2\right)=h(0).
\]
Inversion with the unknown dual measure reads \(h(0)=c h(0)\), forcing \(c=1\). Induction proves the result for any finite number of factors. The argument uses compact localization and monotone convergence for \(C_0\) functions; it does not apply a sigma-finite product theorem to the whole groups. \(\square\)

<a id="ha-lca-07-exercise-5-3"></a>
**Exercise 5.3 — The multiplicative real group.** Compute the dual Haar measure of \(dx/|x|\) on \(\mathbb R^\times\).

**Solution.** The map
\[
 \Phi:\mathbb R^\times\longrightarrow\{1,-1\}\times\mathbb R,
 \qquad x\longmapsto(\operatorname{sgn}x,\log|x|)
\]
is a group isomorphism with continuous inverse \((\epsilon,t)\mapsto\epsilon e^t\). These assertions follow from the proved exponential and logarithm identities in the real-variable reading, Lemma 1.2. On each of the two rays, its substitution theorem, Lemma 1.3, gives for \(v\in C_c(\mathbb R^\times)\)
\[
 \int_{\mathbb R^\times}v(x)\frac{dx}{|x|}
 =\int_{\mathbb R}\bigl(v(e^t)+v(-e^t)\bigr)\,dt.
 \tag{17}
\]
Thus \(\Phi\) sends the given measure to counting measure on the two-element group times \(dt\). To identify the measures fully, \(dx/|x|\) is locally finite and inner regular on \(\mathbb R^\times\): exhaust by the compact sets \(\{1/n\le|x|\le n\}\), on which the continuous density is bounded, and apply finite Radon regularity and monotone convergence. Equality on \(C_c\) in (17) identifies the Borel measures, and both full Haar domains here are their ordinary completions because the groups are sigma-compact.

The two characters of \(\{1,-1\}\) are \(\epsilon\mapsto\epsilon^m\), \(m=0,1\), by the finite character calculation. All characters of the product, and their topology, are given by HA-LCA-02, Proposition 4.1. Pullback by \(\Phi\) is a bijection on continuous characters; it and its inverse preserve uniform convergence on compact sets because \(\Phi\) and \(\Phi^{-1}\) take compact sets to compact sets. Consequently the dual can be written as \(\{0,1\}\times\mathbb R\) with pairing
\[
 \chi_{m,\xi}(x)=\operatorname{sgn}(x)^m e^{2\pi i\xi\log|x|}.
\]
Propositions 3.2–3.3 and the product result give
\[
 d\widehat x=\frac12\sum_{m=0}^1\delta_m\otimes d\xi.
 \tag{18}
\]
Explicitly, if \(f\in B^1(\mathbb R^\times)\), then
\[
 \widehat f(m,\xi)=\int_{\mathbb R^\times}
 f(x)\operatorname{sgn}(x)^m e^{-2\pi i\xi\log|x|}\frac{dx}{|x|},
 \qquad
 f(x)=\frac12\sum_{m=0}^1\int_{\mathbb R}
 \widehat f(m,\xi)\operatorname{sgn}(x)^m
 e^{2\pi i\xi\log|x|}\,d\xi.
\]
For characters \(\operatorname{sgn}(x)^m e^{is\log|x|}\), the change \(s=2\pi\xi\) makes the dual measure
\((4\pi)^{-1}\sum_{m=0}^1\delta_m\otimes ds\).
The factor \(1/2\) comes from counting measure on the sign group, and the factor \(1/(2\pi)\) from the angular real pairing. \(\square\)

<a id="ha-lca-07-exercise-5-4"></a>
**Exercise 5.4 — Compact support without sigma-compactness.** Give the denominator construction for a non-sigma-compact \(G\), and verify that the choice in (6) is immaterial.

**Solution.** A single relatively compact identity neighbourhood supplies a nonzero nonnegative \(u\in C_c(G)\). Its integral and squared norm are finite and positive. For each \(\gamma\) in the prescribed compact \(K\subseteq\Gamma\), the function \(g_\gamma=\gamma u\) satisfies
\(\widehat {g_\gamma}(\gamma)=\int u>0\). Continuity provides an open set on which that transform stays nonzero. A finite subcover of \(K\cup\{1\}\) gives \(g_1,\ldots,g_m\); hence
\[
 h=\sum_jg_j*\widetilde g_j\in C_c(G)\cap P(G),\qquad
 \widehat h=\sum_j|\widehat g_j|^2>0\text{ on }K.
\]
Its support lies in a finite union of compact difference sets. No covering of the whole group and no countable family of identity neighbourhoods has entered this construction.

For two permissible choices \(h,k\) and \(q\) supported in \(K\), the function
\(p=q/(\widehat h\,\widehat k)\), extended by zero, is in \(C_c(\Gamma)\). The finite-measure identity (3) gives
\[
 \int q/\widehat h\,d\mu_h
 =\int p\,\widehat k\,d\mu_h
 =\int p\,\widehat h\,d\mu_k
 =\int q/\widehat k\,d\mu_k.
\]
All measures in this computation are finite Radon measures. The passage from the resulting invariant integral to a Haar measure on the entire dual was separately proved in Lemma 1.0 using an open sigma-compact subgroup and finite coset decompositions of compact supports. This also covers a non-sigma-compact dual. \(\square\)

## Scope and further reading

The source construction is Fremlin's freely accessible [§445P, parts (a)–(h), and §445Q](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex). The local denominator and compatible-measure arguments above use the negative-sign transform convention (1). Lemma 1.0 supplies the representation step from earlier proved Haar results; (10)–(11) proves the full complex \(B^1\) extension. Every normalization and all four exercises have been proved here using the exact earlier results identified above.

The lesson proves inversion on \(B(G)\cap L^1(G)\). General \(L^1\) inversion, general uniqueness for \(L^1\) and finite measures on \(G\), and surjectivity of \(G\to\widehat{\widehat G}\) remain later results. None is used in constructing the dual Haar measure.
