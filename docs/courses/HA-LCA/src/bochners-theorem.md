# Bochner's theorem through bounded positive functionals

**Lesson HA-LCA-06.** This lesson proves Bochner representation on arbitrary locally compact abelian groups and develops its concrete applications. Self-checked by the writing AI.

This lesson follows the repeated-squaring argument in D. H. Fremlin's freely accessible [*Measure Theory*, Volume 4, §445N](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex). Fremlin's source section is dated 20 March 2008, copyright 1998, in the 2013 source collection. The lesson starts with a bounded positive functional, proves positivity of its extension by approximating square roots, and then obtains both the continuous and the locally almost-everywhere statements. Written by GPT-6 Astra (OpenAI), Ultra, 4 October 2026. Original text: public domain (CC0); Fremlin's unchanged source package accompanies it under its own terms.

Let \(G\) be a locally compact Hausdorff abelian group with Haar measure \(dx\), on the complete locally determined domain constructed in [the Haar prerequisite, Theorem 5.1](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-theorem-5-1). No countability or separability assumption is imposed. Write \(\Gamma=\widehat G\) and use
\[
 f^*(x)=\overline{f(-x)},\qquad
 \widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,dx,
 \qquad Ff(\gamma)=\widehat f(\gamma^{-1}).
\]
Thus \(Ff(\gamma)=\int f(x)\gamma(x)\,dx\). The two conventions differ only by inversion on \(\Gamma\).

The earlier results needed for the argument are as follows. Each linked reading contains the complete proofs used here.

- [The dual group as the spectrum of \(L^1(G)\)](the-dual-group-as-the-gelfand-spectrum-of-l1.md), Theorem 2.1 and Corollary 2.2: the spectrum identification, topology, \(C_0\) property and radius formula; Theorems 3.1–3.2: transform laws and uniform density in \(C_0(\Gamma)\). Its Lemma 5.1 proves the circle Haar normalization and orthogonality used below.
- [Spectral radius and characters of a Banach algebra](../prerequisites/src/banach-spectrum.md), Theorem 2.2 and Theorems 3.3–3.4: the full limit \(r(a)=\lim_n\|a^n\|^{1/n}\), the character description and the extra zero from unitization. Its Lemma 4.1 proves arbitrary product compactness. Together with the HA-LCA-03 identification these give \(r(f)=\|Ff\|_\infty\).
- [Finite Radon representation on locally compact spaces](../prerequisites/src/finite-radon-representation.md), Theorem 3.1, Theorem 4.3, Proposition 4.4 and Corollary 4.5: positive and complex finite representation, total variation, Jordan decomposition and compact tails. Its Lemma 1.6 proves the compact-product estimates used below. These proofs are given for arbitrary locally compact Hausdorff spaces.
- [Finite Radon products and convolution of measures](../prerequisites/src/finite-radon-products.md), Theorems 2.1–2.2 and Corollary 2.3: the Radon product, bounded continuous Fubini and compact localization. Its Theorem 3.3 proves the finite-measure convolution algebra.
- [Integration and \(L^1\)](../prerequisites/src/integration-and-l1.md), Theorem 1.2, Corollary 1.3 and Theorem 2.2: monotone convergence, Fatou and dominated convergence; Theorems 2.4 and 3.1: \(L^1\) completeness and \(C_c\)-density; Theorems 4.2–4.4: finite and explicitly sigma-finite Borel Fubini, including ordinary completions. The [character lesson, Lemma 3.3](characters-and-the-dual-group.md#ha-lca-02-lemma-3-3), constructs and normalizes Lebesgue measure and proves affine substitution.
- [Real-variable calculations](../prerequisites/src/real-variable-calculations.md), Lemmas 1.1–1.4: Riemann–Lebesgue integral agreement, exponentials and powers, the arctangent integral, integration by parts and dominated differentiation; Theorem 2.1: Gaussian normalization, transform and moments; Lemma 3.1 and Proposition 3.2: convex slopes and the explicit triangular mixing measure.
- [Haar measure on arbitrary LCA groups](../prerequisites/src/haar-measure.md), Theorems 4.1–5.1: existence, uniqueness, inversion and the complete locally determined domain; Lemma 5.2 and Lemma 6.1: \(C_c\)-density for that domain and translation continuity; Theorem 6.2 and Corollary 6.3: the \(L^1\) Banach star algebra and symmetric approximate identities.
- [Characters and the dual group](characters-and-the-dual-group.md), Theorem 2.1, Theorem 3.1 and Corollary 3.2: duals of compact groups, \(\mathbb R\), \(\mathbb Z\) and \(\mathbb T\), used in the applications. Its Proposition 1.4 proves joint continuity of evaluation, and its Theorem 5.2 proves local compactness of the dual.

## 1. Measures, transforms and positive functionals

For a finite complex Radon measure \(\mu\) on \(\Gamma\), define
\[
 T\mu(x)=\int_\Gamma\gamma(x)\,d\mu(\gamma). \tag{1}
\]
For the negative-sign Fourier–Stieltjes convention on \(\Gamma\), this is
\(T\mu(x)=\widehat\mu(\alpha_G(-x))\), where \(\alpha_G(x)(\gamma)=\gamma(x)\).
Evaluation at \(x\) is a continuous character of \(\Gamma\): multiplicativity is immediate and continuity follows by testing the compact set \(\{x\}\) in the compact-open topology. This relation does not require surjectivity of \(\alpha_G\).

<a id="ha-lca-06-proposition-1-1"></a>
**Proposition 1.1.** The function \(T\mu\) is bounded and uniformly continuous, \(\|T\mu\|_\infty\le\|\mu\|\), and
\[
 \int_G f(x)T\mu(x)\,dx=\int_\Gamma Ff(\gamma)\,d\mu(\gamma).
 \tag{2}
\]
The map \(T\) is injective.

**Proof.** The norm bound follows from \(|\gamma(x)|=1\). Evaluation \((x,\gamma)\mapsto\gamma(x)\) is jointly continuous: restrict \(x\) to a compact neighbourhood of a specified \(x_0\), control \(\gamma-\gamma_0\) uniformly there by the compact-open topology, and control \(\gamma_0(x)-\gamma_0(x_0)\) by continuity of \(\gamma_0\). In particular, for a compact \(K\subset\Gamma\), compactness of \(\{0\}\times K\) gives an identity neighbourhood \(U\) on which \(\sup_{\gamma\in K}|\gamma(a)-1|\) is as small as desired.

Choose \(K\) so that \(|\mu|(\Gamma\setminus K)<\varepsilon\). The character law yields, for every \(x\),
\[
 |T\mu(x+a)-T\mu(x)|
 \le\|\mu\|\sup_{\gamma\in K}|\gamma(a)-1|+2\varepsilon.
\]
This proves uniform continuity. It uses compact tails, not an invalid dominated-convergence argument for arbitrary nets.

For \(f\in C_c(G)\) and \(\mu\) restricted to a compact set, (2) is the finite Radon-product Fubini identity for the continuous pairing kernel. Remove the compact restriction with error at most \(\|f\|_1|\mu|(\Gamma\setminus K)\) on either side. Then extend to all \(L^1\) by \(C_c\)-density and the bound \(\|f\|_1\|\mu\|\). This proves (2) without global sigma-finiteness.

If \(T\mu=0\), (2) says that \(\mu\) annihilates every transform \(Ff\). Their density in \(C_0(\Gamma)\) and Radon uniqueness imply \(\mu=0\). Applying this to a difference proves injectivity. \(\square\)

### A bound in the Fourier norm

A bounded complex-linear functional \(L:L^1(G)\to\mathbb C\) is **positive** when \(L(f*f^*)\ge0\) for every \(f\in L^1(G)\). This condition concerns convolution squares; it does not mean that \(L(f)\ge0\) for nonnegative functions \(f\).

<a id="ha-lca-06-lemma-1-2"></a>
**Lemma 1.2.** Every bounded positive functional satisfies
\[
 |L(f)|\le\|L\|\,\|Ff\|_\infty. \tag{3}
\]

**Proof.** The assertion is immediate for \(L=0\). Divide by \(\|L\|\) and call the resulting norm-one functional \(\ell\).

For relatively compact open identity neighbourhoods \(U\), put \(e_U=1_U/|U|\). Haar measure gives \(0<|U|<\infty\) and \(\|e_U\|_1=1\). The norm-integral identity in [HA-LCA-03, Lemma 1.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-1-1) gives the following estimate; translation continuity then gives its limit:
\[
 \|f*e_U-f\|_1
 \le\sup_{y\in U}\|f(\,\cdot-y)-f\|_1\longrightarrow0. \tag{4}
\]
Neighbourhoods are directed by reverse inclusion, so (4) uses a net and needs no countable neighbourhood base.

Set \([f,g]=\ell(f*g^*)\), linear in its first variable and conjugate-linear in its second. Here is the full positive-form calculation, which also applies to any such form on a complex vector space. Put \(A=[f,g]\) and \(B=[g,f]\). Reality of \([f+g,f+g]\) gives \(A+B\in\mathbb R\); reality of \([f+ig,f+ig]\) gives \(i(B-A)\in\mathbb R\). Writing real and imaginary parts in these two equations gives \(B=\overline A\). Thus the form is Hermitian. Write \(d=[g,g]\ge0\). Expansion yields
\[
 0\le[f-zg,f-zg]=[f,f]-2\operatorname{Re}(\overline zA)+|z|^2d.
\]
If \(d>0\), choose \(z=A/d\); if \(d=0\), choose \(z=tA\) for every positive real \(t\), forcing \(A=0\). In either case
\[
 |[f,g]|^2\le[f,f][g,g].
\] Use \(g=e_U^*\). Commutativity gives \(g*g^*=e_U*e_U^*\), and its \(L^1\) norm is at most one. Hence
\[
 |\ell(f*e_U)|^2
 \le\ell(f*f^*)\ell(e_U*e_U^*)
 \le\ell(f*f^*).
\]
Taking the limit in (4) yields \(|\ell(f)|^2\le\ell(f*f^*)\).

Write \(b=f*f^*\). Since \(b=b^*\), repeated application of the last inequality gives, for every integer \(k\ge1\),
\[
 |\ell(f)|^{2^k}\le\ell\bigl(b^{*2^{k-1}}\bigr)
 \le\bigl\|b^{*2^{k-1}}\bigr\|_1.
\]
The notation \(b^{*m}\) here means the \(m\)-fold convolution product. The spectral-radius formula, including its subsequence \(m=2^{k-1}\), now gives
\[
 |\ell(f)|\le r(b)^{1/2}
 =\|F(b)\|_\infty^{1/2}
 =\bigl\||Ff|^2\bigr\|_\infty^{1/2}=\|Ff\|_\infty.
\]
In the possibly nonunital algebra the spectrum is taken in the unitization; the extra zero value does not change its radius. Multiplying by \(\|L\|\) proves (3). \(\square\)

This is the part of Fremlin's argument that turns a bound in \(L^1\) into a bound in the uniform norm of a transform. It does not assume that \(F\) is injective.

<a id="ha-lca-06-theorem-1-3"></a>
**Theorem 1.3.** For each bounded positive functional \(L\) there is a unique finite positive Radon measure \(\mu\) on \(\Gamma\) such that
\[
 L(f)=\int_\Gamma Ff\,d\mu \quad(f\in L^1(G)),
 \qquad \mu(\Gamma)=\|L\|. \tag{5}
\]

**Proof.** If \(Ff=Fg\), Lemma 1.2 applied to \(f-g\) gives \(L(f)=L(g)\). Consequently \(\Lambda(Ff)=L(f)\) is a well-defined functional on the uniformly dense algebra \(F(L^1(G))\subset C_0(\Gamma)\). Inequality (3) lets it extend uniquely and continuously to \(C_0(\Gamma)\), with norm at most \(\|L\|\).

For \(q\in C_0(\Gamma)\) with \(q\ge0\), also \(\sqrt q\in C_0(\Gamma)\). Choose transforms \(Ff_n\to\sqrt q\) uniformly. Then \(|Ff_n|^2\to q\) uniformly, since
\[
 \bigl\||Ff_n|^2-q\bigr\|_\infty
 \le\|Ff_n-\sqrt q\|_\infty
       \bigl(\|Ff_n\|_\infty+\|\sqrt q\|_\infty\bigr).
\]
But \(\Lambda(|Ff_n|^2)=L(f_n*f_n^*)\ge0\). Continuity implies \(\Lambda(q)\ge0\). Finite Radon representation therefore supplies a positive measure \(\mu\) with \(\Lambda(q)=\int q\,d\mu\) and \(\mu(\Gamma)=\|\Lambda\|\le\|L\|\). Conversely (5) and \(\|Ff\|_\infty\le\|f\|_1\) give \(\|L\|\le\mu(\Gamma)\). These inequalities prove the mass assertion.

Two representing measures agree on the dense transform algebra, hence on \(C_0(\Gamma)\). Uniqueness in finite Radon representation makes them equal. \(\square\)

## 2. Bochner representation

A function \(\varphi:G\to\mathbb C\) is of **positive type** if every finite choice satisfies
\[
 \sum_{i,j=1}^n c_i\overline{c_j}\varphi(x_i-x_j)\ge0. \tag{6}
\]
<a id="ha-lca-06-lemma-2-0"></a>
**Lemma 2.0.** A function of positive type satisfies
\[
 \varphi(0)\ge0,\qquad
 \varphi(-x)=\overline{\varphi(x)},\qquad
 |\varphi(x)|\le\varphi(0).
\]

**Proof.** The one-point test gives the first assertion. For the two points \(x_1=x,x_2=0\), define
\([c,d]=\sum_{i,j=1}^2 c_i\overline{d_j}\varphi(x_i-x_j)\) on \(\mathbb C^2\).
This is a positive sesquilinear form. The full algebraic calculation in Lemma 1.2 proves that it is Hermitian and satisfies Cauchy's inequality, including when a diagonal value is zero. Apply these conclusions to the two coordinate vectors: the off-diagonal entries are \(\varphi(x)\) and \(\varphi(-x)\), and both diagonal entries are \(\varphi(0)\). Consequently \(|\varphi(x)|^2\le\varphi(0)^2\), proving the remaining assertions. \(\square\)

<a id="ha-lca-06-theorem-2-1"></a>
**Theorem 2.1 (Bochner).** A continuous function \(\varphi\) on \(G\) has positive type if and only if \(\varphi=T\mu\) for a finite positive Radon measure \(\mu\) on \(\Gamma\). The measure is unique and
\[
 \mu(\Gamma)=\varphi(0). \tag{7}
\]

**Proof.** A positive measure in (1) gives
\[
 \sum_{i,j}c_i\overline{c_j}T\mu(x_i-x_j)
 =\int_\Gamma\left|\sum_i c_i\gamma(x_i)\right|^2\,d\mu\ge0.
\]
Continuity and uniqueness follow from Proposition 1.1, and evaluation at zero gives (7).

Conversely, define \(L(f)=\int f\varphi\). The two-point bound gives \(\|L\|\le\varphi(0)\). We verify its positivity rather than presuming an integral version of (6). For \(f\in C_c(G)\), Fubini and Haar invariance give
\[
 L(f*f^*)=\iint f(s)\overline{f(t)}\varphi(s-t)\,ds\,dt. \tag{8}
\]
On the compact support \(K\) of \(f\), partition into finitely many Borel pieces \(E_j\) and choose \(x_j\in E_j\) so that
\( |\varphi(s-t)-\varphi(x_i-x_j)|<\varepsilon\)
for \(s\in E_i,t\in E_j\). Such a partition is supplied by [Lemma 1.6 of the finite-Radon prerequisite](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-6), applied to the continuous kernel \((s,t)\mapsto\varphi(s-t)\). Then (8) differs by at most \(\varepsilon\|f\|_1^2\) from the nonnegative number
\[
 \sum_{i,j}\left(\int_{E_i}f\right)
                 \overline{\left(\int_{E_j}f\right)}
                 \varphi(x_i-x_j).
\]
Letting \(\varepsilon\downarrow0\) proves positivity for \(C_c\). For general \(f\in L^1\), choose \(f_n\in C_c\) converging in \(L^1\); the estimate
\(\|f_n*f_n^*-f*f^*\|_1\le(\|f_n\|_1+\|f\|_1)\|f_n-f\|_1\)
extends positivity to all \(L^1\).

Theorem 1.3 supplies \(\mu\ge0\). Formula (2) gives \(\int f(\varphi-T\mu)=0\) for every \(f\in L^1\). The continuous difference must be zero: if it is nonzero at a point, multiply it by a constant phase to make its real part positive on a relatively compact open neighbourhood, and test with that neighbourhood's indicator. Its Haar measure is positive and finite, a contradiction. Therefore \(\varphi=T\mu\), completing the proof. \(\square\)

<a id="ha-lca-06-corollary-2-2"></a>
**Corollary 2.2 (bounded measurable classes).** If a bounded locally Haar-measurable function \(b\) satisfies \(\int b(f*f^*)\ge0\) for every \(f\in L^1(G)\), it has a unique continuous positive-type representative modulo locally Haar-null sets. Here locally measurable means that every restriction to a compact set is measurable for the restricted complete Haar domain; locally null means null on every compact set. The assertion applies in particular to \(L^\infty(G)\) classes.

**Proof.** We first check the meaning of the integrals. The Haar construction partitions \(G\) into cosets of an open sigma-compact subgroup \(H\). Each coset is covered by a sequence of compact sets. Local measurability therefore makes \(b\) measurable on each coset, by taking countable unions of its measurable inverse images on those compact sets. The definition of the full Haar domain in the earlier Theorem 5.1 then makes \(b\) measurable on \(G\). For a locally null set the same argument makes every coset section measurable and null; the sum formula for Haar measure makes the whole set null. Thus local-null equality and equality modulo the full Haar null sets coincide in this domain. An essentially bounded measurable class has a bounded representative by setting it to zero on the null set where it exceeds an essential bound.

Its bounded functional \(L(f)=\int fb\) is now well-defined and positive. Theorem 1.3 supplies \(\mu\ge0\), and Proposition 1.1 gives the same \(L^1\) pairings for \(T\mu\); Theorem 2.1 proves that \(T\mu\) has positive type. For a compact set \(K\), the function \(f=1_K\overline{b-T\mu}\) is integrable, since \(K\) has finite measure. Thus \(\int_K|b-T\mu|^2=0\). For every positive integer \(n\), the subset of \(K\) where \(|b-T\mu|\ge1/n\) has measure zero by this integral bound. Their union is the set of disagreement on \(K\), proving local-null equality.

Finally, a nonzero continuous difference has, after multiplication by a constant phase, positive real part on a relatively compact open set. That open set has positive finite Haar measure and hence contains a compact set of positive measure by inner regularity. Local-null equality on that compact set is impossible. This proves uniqueness. \(\square\)

Continuity in Theorem 2.1 matters. The indicator of \(\{0\}\) on \(\mathbb R\) satisfies (6): partition equal points in the finite list, and the sum is a sum of squared absolute values. It is discontinuous and has no pointwise representation (1). Its locally almost-everywhere representative is the zero function, in accordance with Corollary 2.2.

## 3. Discrete frequencies and compact groups

<a id="ha-lca-06-corollary-3-1"></a>
**Corollary 3.1 (Herglotz).** A sequence \((a_n)_{n\in\mathbb Z}\) satisfies
\[
 \sum_{i,j}c_i\overline{c_j}a_{n_i-n_j}\ge0
\]
for every finite choice if and only if there is a finite positive Radon measure \(\mu\) on \(\mathbb T\) such that
\[
 a_n=\int_{\mathbb T}z^n\,d\mu(z).
\]
The measure is unique and has mass \(a_0\).

**Proof.** Give \(\mathbb Z\) its discrete topology. Every function on it is continuous, and its characters are precisely \(n\mapsto z^n\), with \(z\in\mathbb T\). Apply Theorem 2.1. Conversely, integrate the square \(|\sum_i c_i z^{n_i}|^2\). \(\square\)

<a id="ha-lca-06-corollary-3-2"></a>
**Corollary 3.2.** On a compact abelian group \(K\), with Haar mass one, the continuous positive-type functions are exactly the uniformly absolutely convergent series
\[
 \varphi(x)=\sum_{\gamma\in\widehat K}c_\gamma\gamma(x),
 \qquad c_\gamma\ge0,\qquad\sum_\gamma c_\gamma<\infty. \tag{9}
\]
They satisfy
\[
 \sum_\gamma c_\gamma=\varphi(0),\qquad
 c_\eta=\int_K\varphi(x)\overline{\eta(x)}\,dx. \tag{10}
\]

**Proof.** The dual is discrete by HA-LCA-02, Theorem 2.1. A compact subset of a discrete space is finite. Thus inner regularity of the Bochner measure gives
\(\mu(\widehat K)=\sup_{E\text{ finite}}\sum_{\gamma\in E}\mu(\{\gamma\})\).
Put \(c_\gamma=\mu(\{\gamma\})\). For each positive integer \(m\), only finitely many atoms have mass at least \(1/m\), since their finite partial sums are bounded by the total mass. Their countable union \(S\) contains every positive atom. Countable additivity and the displayed supremum give \(\mu(S)=\mu(\widehat K)\). Hence the complement has measure zero, and on every subset of the discrete dual the measure equals the sum of its atoms. The sum of masses bounds the series uniformly and absolutely, since each character has modulus one.

For a nontrivial character \(\chi\), choose \(a\) with \(\chi(a)\ne1\). Haar invariance gives \(\int\chi=\chi(a)\int\chi\), so \(\int\chi=0\). The trivial character has integral one. Apply this to \(\gamma\overline\eta\), and integrate the uniformly convergent series term by term to obtain (10). Conversely (9) is continuous by uniform convergence and satisfies (6) by summing the nonnegative squares with weights \(c_\gamma\). \(\square\)

On \(\mathbb R\), with \(\gamma_\xi(x)=e^{2\pi i x\xi}\), the normalized functions in Theorem 2.1 are precisely
\[
 \varphi(x)=\int_{\mathbb R}e^{2\pi ix\xi}\,d\mu(\xi),
 \qquad \mu(\mathbb R)=1.
\]
The probabilistic convention \(\mathbb E(e^{itX})\) is \(\varphi(t/(2\pi))\). This identity specifies the conversion of constants in the examples.

## 4. Products and the Fourier–Stieltjes algebra

Let \(B(G)\) be the complex linear span of the continuous positive-type functions.

<a id="ha-lca-06-proposition-4-1"></a>
**Proposition 4.1.** The map \(T\) is a bijection from the finite complex Radon measures \(M(\Gamma)\) to \(B(G)\). With
\[
 \|T\mu\|_B=\|\mu\|,
\]
the space \(B(G)\) is a unital commutative Banach star algebra under pointwise multiplication and complex conjugation, and \(\|\varphi\|_\infty\le\|\varphi\|_B\).

**Proof.** Write a complex measure as \(\mu=\mu_1-\mu_2+i\mu_3-i\mu_4\), where the four measures are finite and positive, by applying Jordan decomposition to its real and imaginary parts. Bochner's theorem gives \(T\mu\in B(G)\). In the other direction every finite linear combination of positive-type functions is a transform of the corresponding linear combination of their positive Bochner measures. Proposition 1.1 gives injectivity.

For finite measures, define \(\mu*\nu\) as the image of their Radon product under multiplication \((\gamma,\eta)\mapsto\gamma\eta\). For positive measures this image is again finite Radon: given a Borel set, approximate its inverse image from within by compact sets, whose images are compact; their measures give the required inner approximation. Extend by the four-positive-measure decomposition for complex measures. Variation gives
\(\|\mu*\nu\|\le\|\mu\|\|\nu\|\).
Fubini for these finite measures gives
\[
 T(\mu*\nu)(x)
 =\iint\gamma(x)\eta(x)\,d\mu(\gamma)d\nu(\eta)
 =T\mu(x)T\nu(x).
\]
All these kernels are bounded and continuous, so [Theorem 2.2 of the finite-product reading](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-theorem-2-2) applies on arbitrary locally compact spaces. Its Proposition 3.2 and Theorem 3.3 prove the product associativity and measure-algebra laws used here. The point mass at the trivial character gives the unit.

Define \(\mu^*(E)=\overline{\mu(E^{-1})}\). Substitution in (1) gives \(T(\mu^*)=\overline{T\mu}\) and \(\|\mu^*\|=\|\mu\|\). Finally [Theorem 4.3 of the finite-Radon reading](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-theorem-4-3) proves completeness of \(M(\Gamma)\), as well as its isometric identification with \(C_0(\Gamma)^*\). Transporting this norm through the bijection \(T\) proves all the assertions. \(\square\)

## 5. Four calculations

<a id="ha-lca-06-example-5-1"></a>
**Example 5.1 — Gaussian measures.** **Verification.** Here is a direct integral calculation, independent of general Fourier inversion. Put
\[
 J(u)=\int_{\mathbb R}e^{-\pi y^2}e^{2\pi iuy}\,dy.
\]
The earlier [real-variable reading, Theorem 2.1](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-theorem-2-1), proves \(J(0)=1\) by positive Fubini, the one-dimensional substitution \(y=xt\), and the integral of \(1/(1+t^2)\). Its Lemmas 1.3–1.4 justify integration by parts and differentiation under the integrable bound \(2\pi|y|e^{-\pi y^2}\). With the Gaussian boundary terms tending to zero, these operations give \(J'(u)=-2\pi uJ(u)\). The derivative of \(e^{\pi u^2}J(u)\) is therefore zero, and its value at zero is one. Thus \(J(u)=e^{-\pi u^2}\), as also proved in full in that earlier theorem.

For \(a>0\) and \(b\in\mathbb R\), substitution now gives the explicit Bochner pair
\[
 d\mu(\xi)=a^{-1/2}e^{-\pi(\xi-b)^2/a}\,d\xi,
 \qquad T\mu(x)=e^{2\pi ibx}e^{-\pi ax^2}. \tag{11}
\]
The same earlier theorem computes the mean as \(b\) and the variance as \(a/(2\pi)\). In particular, a normal law with mean \(b\) and variance \(s^2>0\) has \(a=2\pi s^2\), giving the usual characteristic function \(e^{ibt-s^2t^2/2}\). At variance zero use \(\delta_b\). The choice \(a=1/\pi,b=0\) gives the density \(\sqrt\pi e^{-\pi^2\xi^2}\) for \(e^{-x^2}\).

<a id="ha-lca-06-example-5-2"></a>
**Example 5.2 — Cauchy measures.** **Verification.** Two elementary exponential integrals give
\[
 \int_{\mathbb R}e^{-|t|}e^{-2\pi i\xi t}\,dt
 =\frac1{1+2\pi i\xi}+\frac1{1-2\pi i\xi}
 =q(\xi):=\frac2{1+4\pi^2\xi^2}.
\]
The positive function \(q\) has integral one by the arctangent antiderivative. To compute its transform, insert \(e^{-\pi\varepsilon\xi^2}\). Absolute Fubini and Example 5.1 give
\[
 \int e^{2\pi ix\xi}q(\xi)e^{-\pi\varepsilon\xi^2}\,d\xi
 =\int e^{-|t|}\varepsilon^{-1/2}e^{-\pi(x-t)^2/\varepsilon}\,dt
 =\int e^{-|x-\sqrt\varepsilon u|}e^{-\pi u^2}\,du.
\]
Absolute integrability before interchange is bounded by \(\|e^{-|\cdot|}\|_1\int e^{-\pi\varepsilon\xi^2}\,d\xi<\infty\). Dominated convergence uses \(q\) on the left and \(e^{-\pi u^2}\) on the right. Thus \(T(q\,d\xi)(x)=e^{-|x|}\).

For \(k=2\pi c>0\), substitute \(\xi=b+k\eta\). The density becomes \(k^{-1}q((\xi-b)/k)\), and its transform becomes \(e^{2\pi ibx}e^{-k|x|}\). Simplifying this density yields
\[
 d\mu(\xi)=\frac{c}{\pi((\xi-b)^2+c^2)}\,d\xi,
 \qquad T\mu(x)=e^{2\pi ibx-2\pi c|x|},\quad c>0. \tag{12}
\]
Its probabilistic characteristic function is \(e^{ibt-c|t|}\). Every normalization in (12) follows from the displayed integral; no later inversion theorem is used.

<a id="ha-lca-06-example-5-3"></a>
**Example 5.3 — Two-point laws.** **Verification.** For \(0\le p\le1\) and real \(r,s\),
\[
 \mu=(1-p)\delta_r+p\delta_s,
 \qquad T\mu(x)=(1-p)e^{2\pi irx}+pe^{2\pi isx}.
\]
The case \(r=0,s=1\) is the Bernoulli characteristic function after replacing \(2\pi x\) by \(t\). The equally weighted pair \(r=-s\) gives \(\cos(2\pi sx)\). Positivity is already visible as a convex sum of character squares in (6).

<a id="ha-lca-06-example-5-4"></a>
**Example 5.4 — A circle test.** **Verification.** For a continuous function \(h\) on \(\mathbb R/\mathbb Z\), write
\(c_n=\int_0^1h(t)e^{-2\pi int}\,dt\).
These interval integrals use normalized circle Haar measure by [HA-LCA-03, Lemma 5.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-5-1).
It has positive type if and only if all \(c_n\ge0\). One direction follows from Corollary 3.2. For the other, define
\[
 K_N(t)=\frac1{N+1}\left|\sum_{j=0}^Ne^{2\pi ijt}\right|^2.
\]
Expanding the finite square gives \(\int_0^1K_N=1\) and
\[
 K_N*h(t)=\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)c_ne^{2\pi int}.
\]
For distance at least \(\delta\in(0,1/2)\) from the integers, the finite geometric sum gives
\(K_N(t)\le((N+1)\sin^2(\pi\delta))^{-1}\).
Split the convolution integral into that set and its complement. Uniform continuity of \(h\), nonnegativity of \(K_N\) and its mass one prove \(K_N*h\to h\) uniformly. At zero the summands are nonnegative and their weights increase to one; hence \(\sum_n c_n=h(0)\). The series with coefficients \(c_n\) is absolutely uniformly convergent. Its displayed means converge both to its sum and to \(h\), so its sum is \(h\). Corollary 3.2 proves positive type. The kernel convergence used only continuity of \(h\), not a sign condition on its coefficients. Applied to any continuous \(h\), it proves uniform density of trigonometric polynomials on the circle, which will be used in Exercise 6.3. The complete kernel argument also appears in HA-LCA-03, Example 5.5.

## 6. Exercises and solutions

<a id="ha-lca-06-exercise-6-1"></a>
**Exercise 6.1 — Detecting a single frequency.** For a compact abelian group of Haar mass one and a continuous positive-type function \(\varphi\), prove directly from integral positivity that \(\widehat\varphi(\gamma)\ge0\). Then identify the coefficient with a mass of the representing measure and compute the sum of the coefficients.

**Solution.** Put \(f=\overline\gamma\). Then \(f^*=f\) and
\[
 (f*f)(x)=\int_K\overline{\gamma(y)}\overline{\gamma(x-y)}\,dy
 =\overline{\gamma(x)}.
\]
The positivity established in (8) therefore gives
\(\widehat\varphi(\gamma)=\int\varphi(f*f^*)\ge0\).
Corollary 3.2 identifies this number as \(\mu(\{\gamma\})\), and Radon inner regularity on the discrete dual gives \(\sum_\gamma\widehat\varphi(\gamma)=\mu(\widehat K)=\varphi(0)\). The coefficient support is countable even when the dual itself is not.

<a id="ha-lca-06-exercise-6-2"></a>
**Exercise 6.2 — Mixtures of triangular functions (Pólya's criterion).** Suppose \(h:[0,\infty)\to\mathbb R\) is continuous, decreasing and convex, \(h(0)=1\), and \(h(r)\to0\). Construct a probability measure \(\rho\) on \((0,\infty)\) for which
\[
 h(|x|)=\int\left(1-\frac{|x|}{t}\right)_+d\rho(t), \tag{13}
\]
and prove positive type. Allow the right derivative at zero to be infinite.

**Solution.** For \(r>0\), convex chord inequalities show that the right derivative
\(d(r)=\inf_{s>r}(h(s)-h(r))/(s-r)\)
exists and is finite. A chord with left endpoint smaller than \(r\) bounds it below, and a chord with right endpoint larger than \(r\) bounds it above. The same inequalities give
\[
 d(a)\le\frac{h(b)-h(a)}{b-a}\le d(b)\quad(0<a<b).
\]
Thus \(d\) is increasing and nonpositive. It is right-continuous: for \(r_n\downarrow r\) and fixed \(s>r_n\), bound \(d(r_n)\) above by the chord to \(s\), take the limit, and then take the infimum over \(s>r\). Monotonicity supplies the opposite inequality.

Set \(q=-d\). On a compact interval inside \((0,\infty)\), the chord bounds and upper and lower sums for this bounded monotone function give
\(h(a)-h(b)=\int_a^b q(s)\,ds\).
Let \(b\to\infty\) and then \(a\downarrow0\). Since \(q\ge0\), this yields
\[
 h(r)=\int_r^\infty q(s)\,ds,\qquad \int_0^\infty q(s)\,ds=1.
\]
The decreasing function \(q\) tends to zero at infinity, since a positive limiting value would make its integral infinite.

Here is an explicit construction of the measure needed for (13). For \(u>0\) put
\(\tau(u)=\sup\{r>0:q(r)>u\}\), with empty supremum zero. It is finite because \(q(r)\to0\). Right-continuity gives
\(\{u:\tau(u)>s\}=(0,q(s))\) for \(s>0\).
These identities prove measurability and show that the image of Lebesgue measure, restricted to the values \(\tau>0\), is a measure \(\nu\) on \((0,\infty)\) with \(\nu((s,\infty))=q(s)\). In particular \(\nu\) is finite away from zero and is sigma-finite. The earlier [real-variable reading, Proposition 3.2](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-proposition-3-2), proves the pushforward integral formula by simple approximation. Applying positive Fubini to the Lebesgue variables \(u,s>0\) and the Borel indicator \(1_{\{r<s<\tau(u)\}}\) then gives
\[
 h(r)=\int (t-r)_+\,d\nu(t),\qquad \int t\,d\nu(t)=1.
\]
Hence \(d\rho(t)=t\,d\nu(t)\) is a probability measure and satisfies (13). No bound on \(q\) near zero was needed.

For fixed \(t>0\), the triangle equals the normalized overlap of two intervals of length \(t\). Its quadratic form is
\[
 \sum_{i,j}c_i\overline{c_j}\left(1-\frac{|x_i-x_j|}{t}\right)_+
 =\frac1t\int_{\mathbb R}\left|\sum_i c_i1_{[0,t]}(u-x_i)\right|^2du\ge0.
\]
Integrate this identity with respect to \(\rho\). The finite sums and bounded triangles justify the interchange. This proves (6) for \(h(|x|)\); continuity is already an assumption.

<a id="ha-lca-06-exercise-6-3"></a>
**Exercise 6.3 — Construct the Herglotz measure without Bochner existence.** Starting with the positive quadratic forms in Corollary 3.1, construct the measure using finite Fourier sums. Prove convergence of the resulting functionals directly, and also justify the usual weak-* compactness construction.

**Solution.** The two-point inequalities give \(a_0\ge0\), \(a_{-n}=\overline{a_n}\) and \(|a_n|\le a_0\). If \(a_0=0\), use the zero measure. Otherwise define, with normalized Haar measure \(m\) on the circle,
\[
 p_N(z)=\frac1{N+1}\sum_{j,k=0}^Na_{j-k}z^{-j}z^k
 =\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)a_nz^{-n},
 \qquad d\mu_N=p_N\,dm.
\]
The original quadratic-form assumption, with coefficients \(z^{-j}\), says \(p_N(z)\ge0\). Circle orthogonality gives \(\mu_N(\mathbb T)=a_0\) and, for each fixed \(n\),
\[
 \int z^n\,d\mu_N\longrightarrow a_n.
\]
Thus the integrals of every trigonometric polynomial converge. Example 5.4 proved their uniform density in \(C(\mathbb T)\). For \(g\in C(\mathbb T)\), choose a polynomial \(p\) uniformly within \(\varepsilon\); then
\[
 \left|\int g\,d\mu_N-\int g\,d\mu_M\right|
 \le 2a_0\varepsilon+
       \left|\int p\,d\mu_N-\int p\,d\mu_M\right|.
\]
It follows that \(L(g)=\lim_N\int g\,d\mu_N\) exists. It is linear, positive, bounded by \(a_0\|g\|_\infty\), and satisfies \(L(1)=a_0\). Finite Radon representation supplies \(\mu\ge0\) of mass \(a_0\), with \(\int z^n\,d\mu=a_n\). If two measures have these moments, they agree on the dense polynomials and hence on all continuous functions, so they are equal. Finally, a positive measure gives the required quadratic forms by integrating a squared polynomial. This proves both directions without using Bochner existence or weak-* compactness.

For the compactness construction, embed the ball \(\{L\in C(\mathbb T)^*: \|L\|\le a_0\}\) in
\(\prod_{g\in C(\mathbb T)}\{z\in\mathbb C:|z|\le a_0\|g\|_\infty\}\)
by all its evaluations. The finite-coordinate linearity equations define a closed subset of this product, and its points are exactly the bounded linear functionals in the ball. [Lemma 4.1 of the Banach-algebra prerequisite](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-4-1) makes the product compact; its relative product topology is precisely the weak-* topology. Positivity and the equation \(L(1)=a_0\) are closed conditions. Thus the sequence of positive functionals associated to \(\mu_N\) has a convergent subnet in this set. To justify that last step, the closures of its tails have the finite-intersection property and hence a common point \(L_*\). Use triples \((U,n,k)\), where \(U\) is a neighbourhood of \(L_*\), \(k\ge n\), and \(L_k\in U\). Order triples by reverse inclusion of \(U\) and by increasing \(n,k\). They form a directed set: intersect two neighbourhoods and use that \(L_*\) belongs to every tail closure to choose a new \(k\) beyond both old \(k\)'s and both lower bounds. Projection to \(k\) is increasing and cofinal in the original indices. The resulting subnet converges to \(L_*\), since triples beyond one with neighbourhood \(U\) have their functional in \(U\). Its moment limits are the displayed \(a_n\). Radon representation supplies the same unique measure. This also proves the weak-* method; the direct estimate above additionally shows convergence of the entire sequence.

<a id="ha-lca-06-exercise-6-4"></a>
**Exercise 6.4 — A cutoff fails positivity.** Test \(u(x)=(1-x^2)_+\) on the three points \(-1/2,0,1/2\). Also compute its Fourier transform to see a frequency at which it is negative.

**Solution.** The matrix of values \(u(x_i-x_j)\) is
\[
 \begin{pmatrix}1&3/4&0\\3/4&1&3/4\\0&3/4&1\end{pmatrix}.
\]
For \(c=(1,-3/2,1)\), its quadratic form is \(1+9/4+1-9/4-9/4=-1/4\). This directly contradicts (6).

Writing \(w=2\pi\xi\), integration by parts twice gives
\[
 \widehat u(\xi)=2\int_0^1(1-t^2)\cos(wt)\,dt
 =\frac4w\int_0^1t\sin(wt)\,dt
 =\frac4w\left(-\frac{\cos w}{w}+\frac{\sin w}{w^2}\right)
 =\frac{4(\sin w-w\cos w)}{w^3}\quad(w\ne0).
\]
The value at zero is \(4/3\), obtained by direct integration, and at \(\xi=1\) it is \(-1/\pi^2\).

For completeness the negative coefficient also gives an independent test. If a continuous integrable \(v\) were of positive type, use
\(f_T(t)=(2T)^{-1/2}e^{-2\pi i\xi t}1_{[-T,T]}(t)\)
in its integral positivity. Direct overlap gives
\(f_T*f_T^*(s)=e^{-2\pi i\xi s}(1-|s|/(2T))_+\).
The nonnegative integral against \(v\) converges to \(\widehat v(\xi)\), by domination by \(|v|\). Hence such a transform is nonnegative at every frequency; the computed value for \(u\) again rules out positive type.

<a id="ha-lca-06-exercise-6-5"></a>
**Exercise 6.5 — The exponent test.** Prove that \(e^{-|x|^\alpha}\) has positive type for \(0<\alpha\le1\) and for \(\alpha=2\), and that it cannot have positive type when \(\alpha>2\). The interval \(1<\alpha<2\) is not required here.

**Solution.** For \(0<\alpha\le1\), the function \(h(r)=e^{-r^\alpha}\) is continuous, decreases from one to zero, and on \(r>0\) satisfies
\[
 h''(r)=e^{-r^\alpha}
 \bigl(\alpha(1-\alpha)r^{\alpha-2}+\alpha^2r^{2\alpha-2}\bigr)\ge0.
\]
Continuity at zero extends its convex inequalities to \([0,\infty)\). Exercise 6.2 applies, including the possible infinite slope at zero. The case \(\alpha=2\) is the Gaussian measure in (11).

Suppose \(\alpha>2\) and positive type held. Bochner would give a probability measure \(\mu\) on \(\mathbb R\). Taking real parts and dividing by \(t^2\) gives
\[
 \frac{1-e^{-|t|^\alpha}}{t^2}
 =\int\frac{1-\cos(2\pi t\xi)}{t^2}\,d\mu(\xi).
\]
The integrands are nonnegative. Along any nonzero sequence tending to zero they converge pointwise to \(2\pi^2\xi^2\), while the left side tends to zero. Fatou's lemma implies \(\int\xi^2\,d\mu=0\). Thus \(\mu(\{|\xi|\ge1/n\})=0\) for every positive integer \(n\), so \(\mu\) is concentrated at zero. Its transform would be the constant one, contradicting its value \(e^{-1}\) at \(x=1\). No moment assumption was used before Fatou's lemma.

## Reading and continuation

The freely accessible mathematical source for the main reconstruction is D. H. Fremlin, [*Measure Theory*, Volume 4, §445N](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex), parts (d)–(f), (h)–(j), with (a)–(c) supplying the positive-definite starting point. The bounded-functional formulation in Lemma 1.2 treats measurable classes directly; the positivity argument in Theorem 1.3 uses the uniform density of transforms. All source-derived steps are written above. The linked earlier readings supply their stated proofs. The main spectral argument, the measurable-class statement, all four examples and all five exercise solutions use the local or exact earlier proofs identified in this lesson.

Next comes a compatible Haar measure on \(\widehat G\) and the general Fourier inversion theorem. The Gaussian and Cauchy calculations here established their particular integral identities directly.
