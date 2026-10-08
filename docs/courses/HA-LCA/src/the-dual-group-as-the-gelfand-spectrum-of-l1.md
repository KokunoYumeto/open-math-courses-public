# The dual group as the spectrum of \(L^1(G)\)

**Lesson HA-LCA-03.** This lesson identifies frequencies with all multiplicative functionals on the convolution algebra, proves the transform laws, and computes explicit examples. Self-checked by the writing AI.

Let \(G\) be a locally compact Hausdorff abelian group. Fix the Haar measure \(dx\) on the complete locally determined domain constructed in [the Haar reading, Theorem 5.1](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-theorem-5-1). Write \(\Gamma=\widehat G\), with the compact-convergence topology from [Characters and the dual group](characters-and-the-dual-group.md). We impose no countability assumption.

The source for the spectrum and transform arguments is D. H. Fremlin, [*Measure Theory*, §§445F–K, version of 20 March 2008](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex), in the freely accessible 2013 source collection. We supply a finite-approximation proof of the integral step instead of importing a dual-space representation theorem. All compactness, integration, representation and Banach-algebra results invoked below have exact earlier programme proofs.

Written by GPT-6 Astra (OpenAI), Ultra, October 2026. Original text: public domain (CC0). Fremlin's copyright 1998 and original notices are retained in the unchanged original source package.

## 1. Translations and multiplicative functionals

Put
\[
 L_af(x)=f(x-a),\qquad f^*(x)=\overline{f(-x)},\qquad
 (f*g)(x)=\int_G f(y)g(x-y)\,dy .
\]
The convolution expression represents an \(L^1\) class; its existence and independence of representatives are proved in [the Haar reading, Theorem 6.2](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-theorem-6-2). That theorem proves that \(L^1(G)\) is a commutative Banach star algebra. Translations are isometries and depend continuously on \(a\) in \(L^1\), by its Lemma 6.1.

Let \(\Delta(L^1(G))\) be the set of nonzero complex-linear multiplicative functionals on this algebra. Such functionals are automatically contractive by [the Banach reading, Theorem 3.4](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-3-4); continuity is a conclusion, not an extra assumption in this definition.

<a id="ha-lca-03-lemma-1-1"></a>
### Lemma 1.1. Translations inside convolution

For \(f,g\in L^1(G)\) and \(a\in G\),
\[
 (L_af)*g=L_a(f*g)=f*(L_ag).                            \tag{1.1}
\]
If \(f,g\in L^1(G)\) and \(\Lambda\) is a bounded linear functional on \(L^1(G)\), then
\[
 \Lambda(g*f)=\int_G g(y)\Lambda(L_yf)\,dy.              \tag{1.2}
\]

The norm integral \(g*f=\int_Gg(y)L_yf\,dy\) exists as a limit of integrals of finite simple \(L^1(G)\)-valued functions. Every \(L^1\) class has a representative vanishing outside a sigma-compact open subgroup.

**Proof.** For \(f,g\in C_c(G)\), translating the integration variable gives
\[
 ((L_af)*g)(x)=\int f(y-a)g(x-y)\,dy
             =\int f(z)g(x-a-z)\,dz.
\]
This is both \(L_a(f*g)(x)\) and \(f*(L_ag)(x)\). Translations are \(L^1\) isometries, convolution satisfies
\(\|f*g\|_1\le\|f\|_1\|g\|_1\), and \(C_c\) is dense in \(L^1\), by the Haar reading, Lemma 5.2 and Theorem 6.2. Approximating both factors therefore proves (1.1) in full.

We prove (1.2) first for \(f,g\in C_c(G)\); the case \(g=0\) is immediate. Set \(K=\operatorname{supp}g\). The map \(y\mapsto L_yf\) is continuous into \(L^1\). Given \(\varepsilon>0\), finitely many open sets \(U_j\), with centres \(y_j\in K\), cover \(K\), with
\(\|L_yf-L_{y_j}f\|_1<\varepsilon\) for \(y\in U_j\cap K\).
Make a disjoint Borel partition \(K=\coprod_j E_j\) subordinate to that finite cover by assigning a point to the first open set containing it. Define
\[
 v=\sum_j\left(\int_{E_j}g(y)\,dy\right)L_{y_j}f .
\]
Both \(g*f\) and the finitely many translates in \(v\) vanish off the compact set \(K+\operatorname{supp}f\). Using the triangle inequality and nonnegative Fubini on compact restrictions gives
\[
 \|g*f-v\|_1
 \le\sum_j\int_{E_j}|g(y)|\,\|L_yf-L_{y_j}f\|_1\,dy
 \le\varepsilon\|g\|_1.                               \tag{1.3}
\]
The Fubini statement here is precisely the earlier [integration reading, Theorem 4.2](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-4-2): the kernel is Borel, and both variables are restricted to compact sets with finite Radon Haar restrictions. It does not require the whole Haar measure to be sigma-finite.

The function \(y\mapsto\Lambda(L_yf)\) is continuous and bounded by \(\|\Lambda\|\|f\|_1\). Its scalar integral differs from
\(\sum_j(\int_{E_j}g)\Lambda(L_{y_j}f)=\Lambda(v)\)
by at most \(\|\Lambda\|\varepsilon\|g\|_1\). The same bound follows for
\(|\Lambda(g*f)-\Lambda(v)|\) from (1.3). Letting \(\varepsilon\) tend to zero proves (1.2) for \(g\in C_c\). Finally both sides of (1.2), viewed as linear functionals of \(g\), are bounded in \(L^1\) by \(\|\Lambda\|\|f\|_1\|g\|_1\). Density extends the identity to all \(g\in L^1\). For general \(f\in L^1\), approximate it by \(f_n\in C_c\). The convolution bound controls the change in the left side by \(\|\Lambda\|\|g\|_1\|f-f_n\|_1\); translation isometry gives the identical bound for the right side. Thus (1.2) holds for all \(f,g\).

Here is also the claimed norm-integral construction. For compactly supported continuous \(f,g\), the piecewise constant choices of \(L_{y_j}f\) approximate \(L_yf\) with integrated error at most \(\varepsilon\|g\|_1\). Approximating the bounded scalar \(g\) uniformly on \(K\) by a finite simple function makes their products finite simple \(L^1(G)\)-valued functions; the additional integrated error is at most the scalar uniform error times \(|K|\|f\|_1\). Their integrals therefore converge in \(L^1\) to \(g*f\), by (1.3). In general, choose \(f_n,g_n\in C_c\) converging in \(L^1\). Translation isometry gives
\[
 \int_G\|g(y)L_yf-g_n(y)L_yf_n\|_1\,dy
 \le\|g-g_n\|_1\|f\|_1+\|g_n\|_1\|f-f_n\|_1\to0.
\]
The norms in this estimate are measurable: approximate the scalar factors by measurable simple functions and use continuity of translations, followed by pointwise limits. The norm of the integral of a finite simple vector-valued function is bounded by the integral of its norm, by the triangle inequality. Completeness of \(L^1\) now makes the limits of all these simple integrals exist and agree, and the convolution bound identifies their common value with \(g*f\). This defines the asserted norm integral.

Finally the Haar reading, Lemma 5.2, gives a representative vanishing outside a sigma-compact set \(S\). Adjoin the open sigma-compact subgroup \(H\) from its Lemma 1.1. The subgroup generated by \(H\cup S\) is the union of \(H\) and the sets \(H+(S\cup(-S))+\cdots+(S\cup(-S))\) with finitely many summands. These are sigma-compact: express each factor as a countable union of compact sets, use compactness of finite products, and take their continuous sum images. Their countable union is sigma-compact. It is open because it contains the open subgroup \(H\). The chosen representative vanishes off it, as required. \(\square\)

<a id="ha-lca-03-lemma-1-2"></a>
### Lemma 1.2. Frequencies give distinct algebra characters

For \(\gamma\in\Gamma\), put
\[
 h_\gamma(f)=\int_G f(x)\gamma(x)\,dx .
\]
Then \(h_\gamma\in\Delta(L^1(G))\), \(\|h_\gamma\|=1\), and
\(\gamma\mapsto h_\gamma\) is injective.

**Proof.** Linearity and \(|h_\gamma(f)|\le\|f\|_1\) follow from the integral. For \(f,g\in C_c(G)\), compactly supported Fubini and the substitution \(x=y+z\) give
\[
 \int_G(f*g)(x)\gamma(x)\,dx
   =\iint_{G\times G} f(y)g(z)\gamma(y+z)\,dy\,dz
   =h_\gamma(f)h_\gamma(g).                            \tag{1.4}
\]
The first interchange involves only the compact supports of \(f,g\) and their sum, so the [finite-product reading, Corollary 2.3](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-corollary-2-3), applies. Translation invariance justifies the substitution; the last equality uses the character law and finite Fubini. The \(L^1\) convolution bound and \(C_c\)-density extend (1.4) to arbitrary \(f,g\in L^1\).

Choose nonnegative \(u\in C_c(G)\) with \(\int u=1\), as constructed in the Haar reading, Corollary 6.3. The function \(f=\overline\gamma u\) has norm one and \(h_\gamma(f)=1\). This proves nontriviality and the exact norm.

If \(\gamma\ne\eta\), their difference \(d=\gamma-\eta\) is nonzero at some point \(x_0\). On some open neighbourhood \(O\) of \(x_0\), \(|d|\ge c>0\). The earlier [Radon reading, Lemma 1.3](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3), supplies a nonnegative \(u\in C_c(G)\), supported in \(O\), with \(u(x_0)=1\). Haar positivity on open sets gives \(\int u>0\). For \(f=\overline d\,u\),
\[
 h_\gamma(f)-h_\eta(f)=\int |d|^2u>0 .
\]
The functionals are distinct. \(\square\)

## 2. The spectrum and its topology

<a id="ha-lca-03-theorem-2-1"></a>
### Theorem 2.1. Every algebra character is a frequency

The map
\[
 \Gamma\longrightarrow\Delta(L^1(G)),\qquad
 \gamma\longmapsto h_\gamma
\]
is a bijection and a homeomorphism, where the spectrum carries pointwise convergence on \(L^1(G)\), also called its weak-star topology. For a nonzero algebra character \(h\) and any \(f\) with \(h(f)\ne0\), its corresponding frequency satisfies
\[
 \gamma(a)=\frac{h(L_af)}{h(f)}\quad(a\in G).            \tag{2.1}
\]

**Proof.** Fix \(h\in\Delta(L^1(G))\). Contractivity and \(C_c\)-density supply \(f_0\in C_c(G)\) with \(h(f_0)\ne0\); rescale to \(h(f_0)=1\). By multiplicativity and Lemma 1.1,
\[
 h(L_af)h(g)
 =h((L_af)*g)=h(f*(L_ag))=h(f)h(L_ag)                  \tag{2.2}
\]
for all \(f,g\in L^1(G)\). Define \(\gamma(a)=h(L_af_0)\). Taking \(g=f_0\) in (2.2) gives
\[
 h(L_af)=\gamma(a)h(f) \quad(f\in L^1(G)).              \tag{2.3}
\]
This proves the independence asserted in (2.1). It also gives
\(\gamma(a+b)=h(L_aL_bf_0)=\gamma(a)\gamma(b)\) and
\(\gamma(0)=1\). In particular \(\gamma(a)\ne0\), since
\(\gamma(a)\gamma(-a)=1\).

Translation continuity proves continuity of \(\gamma\). Contractivity gives
\(|\gamma(a)|\le\|f_0\|_1\) for all \(a\). Therefore
\(|\gamma(a)|^n=|\gamma(na)|\le\|f_0\|_1\) for every integer \(n\), positive or negative. If \(|\gamma(a)|>1\), positive powers are unbounded; if it is less than one, negative powers are unbounded. Thus \(|\gamma(a)|=1\), and \(\gamma\in\Gamma\).

Lemma 1.1 now identifies the functional itself:
\[
 h(g)=h(g)h(f_0)=h(g*f_0)
     =\int_Gg(y)h(L_yf_0)\,dy
     =\int_Gg(y)\gamma(y)\,dy .
\]
Together with Lemma 1.2, this proves the bijection.

We check both topology directions directly. If \(f\in L^1\), choose \(u\in C_c\) close to \(f\), and put \(K=\operatorname{supp}u\). For \(\gamma,\eta\in\Gamma\),
\[
 |h_\gamma(f)-h_\eta(f)|
 \le 2\|f-u\|_1+\|u\|_1d_K(\gamma,\eta).                \tag{2.4}
\]
First choose the approximation error, then the compact-convergence tolerance. This proves continuity into the weak-star topology.

Conversely fix \(h_0=h_{\gamma_0}\) and choose \(f\in L^1\) with \(h_0(f)=1\). For compact \(K\subseteq G\), the set
\(S=\{L_xf:x\in K\}\) is compact in \(L^1\), since it is the continuous image of a compact set. Given \(\delta>0\), choose a finite \(\delta\)-net \(f_1,\ldots,f_r\) for \(S\). Such a net exists by the finite-subcover definition of compactness, applied to norm balls. For any \(h\in\Delta(L^1(G))\), contractivity gives
\[
 \sup_{v\in S}|h(v)-h_0(v)|
 \le 2\delta+\max_j|h(f_j)-h_0(f_j)|.                  \tag{2.5}
\]
The weak-star neighbourhood conditions on the finitely many \(f_j\), and on \(f\), can make the right side of (2.5) and \(|h(f)-1|\) arbitrarily small. By (2.3) and \(|\gamma(x)|=1\),
\[
 |\gamma(x)-\gamma_0(x)|
 \le |\gamma(x)-h(L_xf)|+|h(L_xf)-h_0(L_xf)|
 =|1-h(f)|+|h(L_xf)-h_0(L_xf)|.
\]
Taking the supremum over \(K\) proves inverse continuity. These neighbourhood arguments apply to arbitrary nets; no sequential replacement is made. \(\square\)

<a id="ha-lca-03-corollary-2-2"></a>
### Corollary 2.2. Local compactness from the spectrum

The group \(\Gamma\) is locally compact Hausdorff. For \(f\in L^1(G)\), the function
\[
 Ff(\gamma)=h_\gamma(f)=\int_G f(x)\gamma(x)\,dx
\]
belongs to \(C_0(\Gamma)\), and
\[
 \|Ff\|_\infty
 =r_{(L^1(G))^+}((0,f))
 =\lim_{n\to\infty}\|f^{*n}\|_1^{1/n}.                 \tag{2.6}
\]
Here \(f^{*n}\) means \(n\)-fold convolution, whereas \(f^*\) means the involution.

**Proof.** The earlier [Banach reading, Theorem 4.2](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-4-2), proves local compactness and the \(C_0\) property for the spectrum of any commutative Banach algebra, as well as the displayed radius formula in its unitization. Apply it to \(L^1(G)\), already proved a Banach algebra in the Haar reading, Theorem 6.2. The homeomorphism of Theorem 2.1 transfers each assertion to \(\Gamma\). Its topological group structure is proved in the character lesson, Proposition 1.1. This also gives a second route to that lesson's direct local-compactness theorem. \(\square\)

## 3. The Fourier algebra

Use the negative-sign convention
\[
 \widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,dx
                  =Ff(\gamma^{-1}).
\]
For \(\eta\in\Gamma\), write \(M_\eta f(x)=\eta(x)f(x)\).

<a id="ha-lca-03-theorem-3-1"></a>
### Theorem 3.1. Transform laws and vanishing at infinity

For \(f,g\in L^1(G)\), \(a\in G\), and \(\gamma,\eta\in\Gamma\),
\[
 \widehat f\in C_0(\Gamma),\qquad
 \|\widehat f\|_\infty\le\|f\|_1,\qquad
 \widehat{f*g}=\widehat f\,\widehat g,\qquad
 \widehat{f^*}=\overline{\widehat f},                    \tag{3.1}
\]
\[
 \widehat{L_af}(\gamma)=\overline{\gamma(a)}\,\widehat f(\gamma),
 \qquad
 \widehat{M_\eta f}(\gamma)=\widehat f(\gamma\eta^{-1}).  \tag{3.2}
\]
The map \(f\mapsto\widehat f\) is complex-linear.

**Proof.** Inversion on \(\Gamma\) is a homeomorphism by the character lesson, Proposition 1.1. Composing the \(C_0\) function \(Ff\) from Corollary 2.2 with inversion preserves continuity and compact level sets, proving the first assertion. The integral norm estimate gives the bound, and linearity follows from linearity of integration. Lemma 1.2 applied to \(\gamma^{-1}\) gives the convolution identity.

Inversion invariance of Haar measure, proved in the Haar reading, Theorems 4.1–5.1, yields
\[
 \widehat{f^*}(\gamma)
 =\int_G\overline{f(-x)}\,\overline{\gamma(x)}\,dx
 =\int_G\overline{f(y)}\,\gamma(y)\,dy
 =\overline{\widehat f(\gamma)}.
\]
Translation invariance and \(x=y+a\) give the first formula in (3.2). For the second, use
\(\eta(x)\overline{\gamma(x)}
 =\overline{(\gamma\eta^{-1})(x)}\)
inside the defining integral. All substitutions preserve the full completed Haar domain, as proved in the earlier Haar reading. \(\square\)

<a id="ha-lca-03-theorem-3-2"></a>
### Theorem 3.2. Uniform density of Fourier transforms

The set
\[
 \mathcal A(G)=\{\widehat f:f\in L^1(G)\}
\]
is a self-adjoint subalgebra of \(C_0(\Gamma)\), separates points of \(\Gamma\), vanishes at no point, and is uniformly dense in \(C_0(\Gamma)\).

**Proof.** Linearity, the product formula and the involution formula in Theorem 3.1 give the algebra and self-adjointness assertions. Given \(\gamma\), Lemma 1.2 supplies \(f\) with \(h_{\gamma^{-1}}(f)\ne0\), which is \(\widehat f(\gamma)\). For \(\gamma\ne\eta\), the characters \(\gamma^{-1},\eta^{-1}\) are distinct, and the same lemma supplies \(f\) with
\(h_{\gamma^{-1}}(f)\ne h_{\eta^{-1}}(f)\).
This is separation by \(\widehat f\). The earlier [uniform approximation reading, Theorem 3.2](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-theorem-3-2), proves that a self-adjoint, point-separating and nowhere-vanishing subalgebra of \(C_0\) on an LCH space is uniformly dense. Its hypotheses have all been checked, and Corollary 2.2 supplies the LCH property. \(\square\)

## 4. Measures and the \(L^1\) ideal

Let \(M(G)\) be the complex finite Radon measures, with the total-variation norm. Its identification with \(C_0(G)^*\) is proved in [the Radon reading, Theorem 4.3](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-theorem-4-3). Convolution of measures is defined using the finite Radon product and addition:
\[
 \mu*\nu=(x,y\mapsto x+y)_*(\mu\otimes\nu),\qquad
 \mu^*(B)=\overline{\mu(-B)} .
\]
The full construction, associativity, involution and norm inequality are proved in [the finite-product reading, Theorem 3.3](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-theorem-3-3). In particular \(M(G)\) is a commutative unital Banach star algebra with unit \(\delta_0\). This definition uses the finite Radon product, not an unproved product of two infinite Haar measures.

<a id="ha-lca-03-lemma-4-1"></a>
### Lemma 4.1. Integrable densities are finite Radon measures

For \(f\in L^1(G)\), define on Borel sets
\[
 j(f)(B)=\int_B f(x)\,dx .
\]
This is well-defined on the \(L^1\) class and is a complex finite Radon measure, with
\[
 |j(f)|(B)=\int_B|f(x)|\,dx,\qquad
 \|j(f)\|=\|f\|_1.                                    \tag{4.1}
\]
The map \(j:L^1(G)\to M(G)\) is linear, injective, isometric, has closed image, and preserves the involution. For bounded Borel \(v\),
\[
 \int_G v\,dj(f)=\int_G vf\,dx.                        \tag{4.2}
\]

**Proof.** The Haar reading, Lemma 5.2, supplies an everywhere finite Borel representative of \(f\); choose one. Changing this representative on a Haar-null set changes none of the integrals. Countable additivity follows by integrating the increasing finite disjoint unions and using dominated convergence with bound \(|f|\). The positive finite measure
\(\lambda_f(B)=\int_B|f|\)
dominates the variation of \(j(f)\): for any finite Borel partition \(B=\coprod B_k\),
\(\sum_k|\int_{B_k}f|\le\int_B|f|\), and taking the supremum proves
\(|j(f)|\le\lambda_f\).

We check Radon regularity. For \(u\in C_c(G)\), the measure
\(\lambda_u(B)=\int_B|u|\)
is dominated by \(\|u\|_\infty\) times Haar measure restricted to the compact set \(\operatorname{supp}u\). The latter restriction is finite Radon by the finite-product reading, Corollary 2.3. Domination transfers Radon regularity by its Lemma 1.2. For general \(f\), take \(u\in C_c\) with \(\|f-u\|_1<\varepsilon\). Then
\[
 |\lambda_f(B)-\lambda_u(B)|\le\|f-u\|_1<\varepsilon
 \quad\hbox{for every Borel }B .
\]
For any Borel \(B\), choose compact \(K\subseteq B\) with
\(\lambda_u(B\setminus K)<\varepsilon\).
It follows that \(\lambda_f(B\setminus K)<2\varepsilon\), proving inner regularity. Because \(\lambda_f\) is finite, inner approximation of the complement gives outer approximation of \(B\) by the open complement of a compact set. Thus \(\lambda_f\) is Radon, and \(|j(f)|\le\lambda_f\) and the domination lemma make \(j(f)\) Radon too.

To prove equality of variation, put
\(s(x)=\overline{f(x)}/|f(x)|\) when \(f(x)\ne0\), and \(s(x)=1\) otherwise. This is a Borel circle-valued function. A finite \(\delta\)-net \(w_1,\ldots,w_r\) on the compact circle, with a first-choice rule, gives a Borel partition \(G=\coprod E_k\) such that \(|s-w_k|<\delta\) on \(E_k\). Therefore for every Borel \(B\),
\[
 \lambda_f(B)
 =\int_Bs f
 \le\left|\sum_k w_k j(f)(B\cap E_k)\right|
       +\delta\lambda_f(B)
 \le |j(f)|(B)+\delta\lambda_f(B).
\]
The first integral is real and nonnegative, so the displayed inequality follows by the complex triangle inequality. Letting \(\delta\downarrow0\) proves (4.1).

Linearity is immediate. Isometry gives injectivity on almost-everywhere classes. If \(j(f_n)\) converges in \(M(G)\), then \(f_n\) is Cauchy in \(L^1\), which is complete by the earlier integration reading, Theorem 2.4. Its limit \(f\) satisfies \(j(f_n)\to j(f)\), proving the image closed. Inversion invariance of Haar measure gives
\(j(f)^*(B)=\int_B\overline{f(-x)}\,dx=j(f^*)(B)\).
Finally (4.2) holds for indicators by definition, then for simple functions by linearity. Uniform approximation of a bounded Borel function by simple functions, together with the bounds on both integrals, proves the general case. \(\square\)

<a id="ha-lca-03-theorem-4-2"></a>
### Theorem 4.2. The measure algebra contains \(L^1(G)\) as a closed ideal

For every \(\mu\in M(G)\) and \(f\in L^1(G)\), there is a unique \(h\in L^1(G)\) such that
\[
 \mu*j(f)=j(h),\qquad \|h\|_1\le\|\mu\|\|f\|_1.        \tag{4.3}
\]
For \(f\in C_c(G)\), it is represented by the continuous function
\[
 h(x)=\int_G f(x-y)\,d\mu(y).                          \tag{4.4}
\]
Moreover \(j(f*g)=j(f)*j(g)\). Thus the closed image of \(j\) is a star ideal, with its original \(L^1\) convolution.

**Proof.** First let \(f\in C_c(G)\). The integral (4.4) exists for every \(x\), since its integrand is bounded by \(\|f\|_\infty\). It is continuous: the parameter-integral assertion of the finite-product reading, Theorem 2.2, applies to the bounded continuous kernel \((x,y)\mapsto f(x-y)\) and the finite Radon measure \(\mu\).

In fact \(h\in C_0(G)\). Given \(\varepsilon>0\), choose compact \(K\subseteq G\) with \(|\mu|(G\setminus K)<\varepsilon\), by compact inner regularity of the finite variation measure. Restricting \(\mu\) to \(K\) in (4.4) gives a continuous \(h_K\) supported in the compact set \(K+\operatorname{supp}f\). Thus \(h_K\in C_c(G)\), and
\(\|h-h_K\|_\infty\le\varepsilon\|f\|_\infty\).
The closure assertion for \(C_0\) in the Radon reading, Lemma 1.5, gives \(h\in C_0\).

For any compact \(A\subseteq G\), finite positive Fubini for Haar measure restricted to \(A\) and \(|\mu|\) gives
\[
 \int_A|h(x)|\,dx
 \le\int_G\int_A|f(x-y)|\,dx\,d|\mu|(y)
 \le \|\mu\|\|f\|_1.                                  \tag{4.5}
\]
The kernel is bounded continuous, so the finite-product reading, Theorem 2.2, suffices. Translation invariance bounds the inner integral by \(\|f\|_1\). The compact sets
\(A_n=\{x:|h(x)|\ge1/n\}\) increase and cover the nonzero set of \(h\), because \(h\in C_0\). Monotone convergence applied to \(|h|\mathbf1_{A_n}\) now proves that \(h\in L^1\) and gives the bound in (4.3). This argument does not assume a compact exhaustion of the whole group.

Let \(\psi\in C_c(G)\). Restrict the Haar \(x\)-variable to \(\operatorname{supp}\psi\); that is a finite Radon restriction. Finite complex Fubini with \(\mu\), followed by translation invariance, gives
\[
 \begin{aligned}
 \int_G\psi(x)h(x)\,dx
 &=\int_G\left(\int_G\psi(x)f(x-y)\,dx\right)d\mu(y)\\
 &=\int_G\left(\int_G\psi(y+z)f(z)\,dz\right)d\mu(y)\\
 &=\int_G\psi\,d(\mu*j(f)).
 \end{aligned}                                      \tag{4.6}
\]
The first kernel is bounded continuous. For the last equality use (4.2), the finite Radon product definition and its bounded continuous Fubini theorem. Hence \(\mu*j(f)\) and \(j(h)\) have the same \(C_c\) integrals, and finite Radon uniqueness proves equality.

For arbitrary \(f\in L^1\), choose \(f_n\in C_c\) with \(f_n\to f\) in \(L^1\). Let \(h_n\) be (4.4) for \(f_n\). Applying the bound just proved to \(f_n-f_m\) shows that \((h_n)\) is Cauchy in \(L^1\). Its limit \(h\) obeys the same norm bound. The measure convolution bound and the isometry of \(j\) allow passage to the limit in
\(\mu*j(f_n)=j(h_n)\), giving (4.3). Isometry also proves uniqueness.

Finally for \(f,g\in C_c\), formula (4.4) with \(\mu=j(g)\), together with (4.2), is exactly the original function convolution. Hence \(j(g)*j(f)=j(g*f)\). Approximate both \(f,g\) in \(L^1\) and use the two convolution norm bounds to extend this identity to all \(L^1\) pairs. The closed-image and star assertions are Lemma 4.1, and commutativity makes the ideal two-sided. \(\square\)

<a id="ha-lca-03-theorem-4-3"></a>
### Theorem 4.3. Fourier–Stieltjes transforms

For \(\mu\in M(G)\), define
\[
 \widehat\mu(\gamma)=\int_G\overline{\gamma(x)}\,d\mu(x).
\]
It is bounded and uniformly continuous on \(\Gamma\), and
\[
 \|\widehat\mu\|_\infty\le\|\mu\|,\quad
 \widehat{\mu*\nu}=\widehat\mu\,\widehat\nu,\quad
 \widehat{\mu^*}=\overline{\widehat\mu},\quad
 \widehat{j(f)}=\widehat f.                            \tag{4.7}
\]
Here uniform continuity means that for each \(\varepsilon>0\) there is an identity neighbourhood \(U\subseteq\Gamma\) such that
\(|\widehat\mu(\gamma\eta)-\widehat\mu(\gamma)|<\varepsilon\)
for all \(\gamma\in\Gamma\), \(\eta\in U\).

**Proof.** The variation bound for the integral gives the norm estimate. For compact \(K\subseteq G\), the character law gives
\[
 |\widehat\mu(\gamma\eta)-\widehat\mu(\gamma)|
 \le \|\mu\|\,d_K(\eta,1)+2|\mu|(G\setminus K).          \tag{4.8}
\]
Given \(\varepsilon>0\), choose \(K\) with tail variation less than \(\varepsilon/4\); then impose
\(d_K(\eta,1)<\varepsilon/(2(1+\|\mu\|))\).
The bound is strictly less than \(\varepsilon\), uniformly in \(\gamma\). This proves uniform continuity, including \(\mu=0\), and works for arbitrary nets.

The finite-product reading, Theorem 3.3, proves the convolution and involution identities for integration against any continuous character, including the character \(\overline\gamma\). These are exactly the middle identities in (4.7). The final identity follows from (4.2) with \(v=\overline\gamma\). \(\square\)

<a id="ha-lca-03-example-4-4"></a>
### Example 4.4. A transform that does not vanish at infinity

For any \(a\in G\), \(\widehat{\delta_a}(\gamma)=\overline{\gamma(a)}\). In particular \(\widehat{\delta_0}=1\). If \(\Gamma\) is noncompact, this last function is not in \(C_0(\Gamma)\).

**Verification.** Integration against a point mass is evaluation. The level set \(\{|1|\ge1/2\}\) is all of \(\Gamma\), which is compact exactly in the excluded case. For example, \(G=\mathbb R\) has \(\Gamma\cong\mathbb R\) by the character lesson, Theorem 3.1, and \(\mathbb R\) is noncompact: the open cover \(\{(-n,n):n\ge1\}\) has no finite subcover. Thus the \(C_0\) conclusion for \(L^1\) transforms does not extend to every finite measure.

For a second explicit example on \(\mathbb R\), let \(\mu=(\delta_{-a}+\delta_a)/2\). Evaluation and the exponential identity for cosine give
\(\widehat\mu(\xi)=(E(a\xi)+E(-a\xi))/2=\cos(2\pi a\xi)\).
If \(a\ne0\), the unbounded sequence \(\xi=n/a\) lies in its level set \(\{|\widehat\mu|\ge1/2\}\), so that set is not compact. A compact subset of \(\mathbb R\) is bounded, since the cover by the intervals \((-n,n)\) would otherwise have no finite subcover. If \(a=0\), this is the preceding constant example. \(\square\)

## 5. Concrete transforms

<a id="ha-lca-03-lemma-5-1"></a>
### Lemma 5.1. Counting measure and circle measure

On \(\mathbb Z\), use counting Haar measure. On \(\mathbb T\), normalized Haar measure \(m\) is the image of Lebesgue measure on \([0,1)\) under \(t\mapsto E(t)\). Consequently, for integrable \(f\) on the circle,
\[
 \int_{\mathbb T}f(z)\,dm(z)=\int_0^1 f(E(t))\,dt,\qquad
 \int_{\mathbb T}z^n\,dm(z)=
 \begin{cases}1&n=0,\\0&n\ne0.\end{cases}               \tag{5.1}
\]

**Proof.** Counting measure is countably additive on all subsets of \(\mathbb Z\), invariant under translations, and finite on the finite compact sets. Any set is approximated from within in measure by its finite subsets; for an infinite set the supremum is infinite. Every subset is open, so outer regularity is immediate. Thus it is a Haar measure with singleton mass one.

For the circle, take Lebesgue measure restricted to \([0,1]\), viewed as a finite Radon measure on \(\mathbb R\). Its continuous image under \(E\) is finite Radon by the finite-product reading, Proposition 3.1, and has mass one. The endpoints have zero measure, so this is also the image of \([0,1)\). For \(a\in[0,1)\) and a bounded Borel \(f\), split \(\int_0^1 f(E(t+a))\,dt\) at \(1-a\). The substitutions \(s=t+a\) on the first interval and \(s=t+a-1\) on the second give
\[
 \int_0^1 f(E(t+a))\,dt
 =\int_a^1 f(E(s))\,ds+\int_0^a f(E(s))\,ds .
\]
Period one of \(E\) and the affine substitution in HA-LCA-02, Lemma 3.3, justify both equalities. Every circle element is \(E(a)\) for some such \(a\). The image measure is therefore invariant, and Haar uniqueness on the compact group, proved in the Haar reading, Theorem 4.1, identifies it with normalized Haar measure.

The integral formula holds for Borel indicators by the image definition, for nonnegative functions by simple approximation, and for integrable functions by decomposition. Completed measurable functions have Borel representatives by the earlier integration reading, Lemma 1.1; the inverse image of a Borel null set has measure zero by the image definition, so the same formula holds for the completion. Finally the integral of \(E(nt)\) on \([0,1]\) is one when \(n=0\), and for \(n\ne0\) its antiderivative is \(E(nt)/(2\pi in)\), with equal endpoint values. The real-variable reading, Lemma 1.1, identifies this continuous Riemann integral with its Lebesgue integral. \(\square\)

<a id="ha-lca-03-example-5-2"></a>
### Example 5.2. Three transforms on the real line

Use Lebesgue measure and the pairing \(E(x\xi)\). Then
\[
 \widehat{\mathbf1_{[-1,1]}}(\xi)
 =\begin{cases}\dfrac{\sin(2\pi\xi)}{\pi\xi}&\xi\ne0,\\[4pt]2&\xi=0,\end{cases}
 \qquad
 \widehat{e^{-\pi x^2}}(\xi)=e^{-\pi\xi^2},
 \qquad
 \widehat{e^{-|x|}}(\xi)=\frac2{1+4\pi^2\xi^2}.         \tag{5.2}
\]

**Verification.** For the interval, put \(\omega=2\pi\xi\). If \(\omega\ne0\), integrate \(e^{-i\omega x}\) on \([-1,1]\) with antiderivative \(e^{-i\omega x}/(-i\omega)\), giving \(2\sin\omega/\omega\). At zero the interval has measure two.

The Gaussian formula is [the real-variable reading, Theorem 2.1](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-theorem-2-1), with parameter \(u=-\xi\). That proof establishes absolute integrability, the normalization and the transform without using general Fourier inversion.

For the exponential, split the integral into its positive and negative half-lines. The first gives
\(\int_0^\infty e^{-(1+i\omega)x}\,dx=1/(1+i\omega)\).
Its antiderivative and zero boundary limit are justified by the real-variable reading, Lemmas 1.2–1.3; the modulus is bounded by \(e^{-x}\). Substituting \(x\mapsto-x\) in the negative half gives \(1/(1-i\omega)\). Adding the two values proves the last formula. \(\square\)

<a id="ha-lca-03-example-5-3"></a>
### Example 5.3. A Fejér kernel on the line

For \(a>0\), define
\[
 K_a(x)=a\left(\frac{\sin(\pi ax)}{\pi ax}\right)^2,
 \qquad K_a(0)=a .
\]
It is nonnegative and integrable, has integral one, and
\[
 \widehat K_a(\xi)=\left(1-\frac{|\xi|}{a}\right)_+ .   \tag{5.3}
\]

**Verification.** Put \(T_a(t)=(1-|t|/a)_+\). Direct integration gives
\[
 \int_{-a}^a T_a(t)e^{2\pi ixt}\,dt
 =2\int_0^a(1-t/a)\cos(2\pi xt)\,dt
 =K_a(x).
\]
For \(x\ne0\), integration by parts evaluates the middle expression as
\(2(1-\cos(2\pi ax))/(a(2\pi x)^2)\), which equals the displayed square because \(1-\cos(2u)=2\sin^2u\), an identity from the exponential multiplication law. At \(x=0\) the triangle has area \(a\). The limit \(\sin t/t\to1\) follows from the derivative of \(\sin\) at zero, so the assigned value makes \(K_a\) continuous.

The bound \(|\sin t|\le|t|\), from the exponential Lipschitz estimate in HA-LCA-02, Lemma 1.3, gives \(K_a\le a\). Also
\(K_a(x)\le1/(\pi^2a x^2)\) for \(x\ne0\).
The antiderivative of \(x^{-2}\), justified by the real-variable reading, Lemmas 1.2–1.3, proves integrability of this tail bound. Hence \(K_a\in L^1\).

To compute its transform without assuming inversion, multiply by \(e^{-\pi\varepsilon x^2}\), where \(\varepsilon>0\). Substitute the preceding integral representation for \(K_a\). Absolute Fubini is justified by
\(\|T_a\|_1\int e^{-\pi\varepsilon x^2}\,dx<\infty\).
The Gaussian transform and scaling then give
\[
 \begin{aligned}
 \int_{\mathbb R}K_a(x)e^{-2\pi i\xi x}e^{-\pi\varepsilon x^2}\,dx
 &=\int_{\mathbb R}T_a(t)\varepsilon^{-1/2}
                 e^{-\pi(t-\xi)^2/\varepsilon}\,dt\\
 &=\int_{\mathbb R}T_a(\xi+\sqrt\varepsilon\,u)e^{-\pi u^2}\,du.
 \end{aligned}
\]
The last integral tends to \(T_a(\xi)\) by continuity of \(T_a\), its bound by one, Gaussian mass one and dominated convergence. On the left, domination by \(K_a\) gives the limit \(\widehat K_a(\xi)\). This proves (5.3). At \(\xi=0\), the formula gives \(\int K_a=1\). \(\square\)

<a id="ha-lca-03-example-5-4"></a>
### Example 5.4. Absolutely convergent Fourier series

For \(G=\mathbb Z\), \(L^1(G)=\ell^1(\mathbb Z)\) and \(\Gamma=\mathbb T\). Its transform is
\[
 a\longmapsto F_a(z)=\sum_{n\in\mathbb Z}a_n z^{-n}.
\]
Its range is the **Wiener algebra** of absolutely convergent Fourier series. The coefficients are unique, and the norm
\(\|F_a\|_{\mathcal A}=\sum_n|a_n|\)
makes this range a Banach star algebra isometrically isomorphic to \(\ell^1(\mathbb Z)\) with convolution.

**Verification.** Counting measure and HA-LCA-02, Corollary 3.2, give the formula. Absolute summability bounds every tail uniformly in \(z\), so the series converges uniformly to a continuous function. Lemma 5.1 and integration of finite partial sums give
\[
 \int_{\mathbb T}F_a(z)z^k\,dm(z)=a_k .
\]
Uniform convergence permits passage to the limit since \(m\) has mass one. Thus the coefficients are unique and the displayed norm is well-defined. By definition every absolutely convergent series of this form comes from an \(\ell^1\) sequence. The product and involution laws are Theorem 3.1. Completeness follows from completeness of \(\ell^1=L^1(\mathbb Z)\), already proved in the integration reading, Theorem 2.4. The uniform norm satisfies \(\|F_a\|_\infty\le\|F_a\|_{\mathcal A}\); the two norms are not identified by this argument. \(\square\)

<a id="ha-lca-03-example-5-5"></a>
### Example 5.5. Circle coefficients and Fejér means

For normalized Haar measure on \(\mathbb T\), the transform of \(f\in L^1(\mathbb T)\) is
\[
 \widehat f(n)=\int_0^1 f(E(t))e^{-2\pi int}\,dt
 \quad(n\in\mathbb Z).
\]
These coefficients tend to zero as \(|n|\to\infty\). The circle Fejér kernels
\[
 P_N(z)=\frac1{N+1}\left|\sum_{j=0}^N z^j\right|^2
\]
are nonnegative of mass one, and
\[
 (P_N*f)(z)
 =\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)\widehat f(n)z^n.
                                                               \tag{5.4}
\]
For continuous \(f\), these means converge uniformly to \(f\).

**Verification.** HA-LCA-02, Corollary 3.2, and Lemma 5.1 give the coefficient formula. Theorem 3.1 places the transform in \(C_0(\mathbb Z)\). Compact sets in the discrete integers are finite, so each nonzero level set is finite, exactly the assertion that the coefficients tend to zero.

Expanding the finite square counts \(N+1-|n|\) pairs with index difference \(n\). Thus
\[
 P_N(z)=\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)z^n.
\]
Circle orthogonality from Lemma 5.1 makes its mass one. In the convolution integral write
\(P_N(zw^{-1})\), insert this finite sum and integrate \(f(w)w^{-n}\); this proves (5.4).

For \(|z-1|\ge\delta>0\), the geometric sum gives
\[
 P_N(z)\le\frac4{(N+1)\delta^2}.
\]
For continuous \(f\), compact-parameter continuity, proved in the Radon reading, Lemma 1.6, gives
\(\sup_z|f(zw^{-1})-f(z)|\to0\) as \(w\to1\).
Choose \(\delta>0\) so that this supremum is below a prescribed \(\varepsilon\) when \(|w-1|<\delta\). In
\[
 P_N*f(z)-f(z)=\int_{\mathbb T}P_N(w)
                     (f(zw^{-1})-f(z))\,dm(w),
\]
the integral over that neighbourhood is bounded by \(\varepsilon\), because the kernel is nonnegative of mass one. The remaining integral is bounded uniformly in \(z\) by
\(8\|f\|_\infty/((N+1)\delta^2)\).
Let \(N\to\infty\), and then \(\varepsilon\downarrow0\). This proves uniform convergence and, in particular, uniform density of trigonometric polynomials in \(C(\mathbb T)\). \(\square\)

## 6. Exercises with complete solutions

<a id="ha-lca-03-exercise-6-1"></a>
### Exercise 6.1. Convolving two intervals

Compute \(f*f\) and its Fourier transform for \(f=\mathbf1_{[-1,1]}\) on \(\mathbb R\), and verify the product law directly.

**Solution.** The convolution value at \(x\) is the length of
\([-1,1]\cap[x-1,x+1]\).
This intersection is empty up to an endpoint when \(|x|\ge2\), and has length \(2-|x|\) when \(|x|<2\). Hence \(f*f(x)=(2-|x|)_+\).
Put \(\omega=2\pi\xi\). For \(\omega\ne0\), evenness and integration by parts give
\[
 \widehat{f*f}(\xi)
 =2\int_0^2(2-x)\cos(\omega x)\,dx
 =\frac{2(1-\cos(2\omega))}{\omega^2}
 =\left(\frac{2\sin\omega}{\omega}\right)^2 .
\]
The first integration by parts gives
\((2/\omega)\int_0^2\sin(\omega x)\,dx\), which is the middle expression. At \(\omega=0\), direct integration of the triangle gives four. These are exactly the square of the values of \(\widehat f\) in Example 5.2, proving the product formula in this case by a separate calculation.

For the unit-length interval \(u=\mathbf1_{[-1/2,1/2]}\), the same overlap computation gives \(u*u=(1-|x|)_+\). The substitution \(y=2x\) gives
\(\widehat u(\xi)=\tfrac12\widehat f(\xi/2)=\sin(\pi\xi)/(\pi\xi)\) for \(\xi\ne0\), with value one at zero. Directly integrating \(2\int_0^1(1-x)\cos(2\pi\xi x)\,dx\) by parts gives
\(\widehat{u*u}(\xi)=(\sin(\pi\xi)/(\pi\xi))^2\), again with value one at zero. This supplies the normalized interval version as well. \(\square\)

<a id="ha-lca-03-exercise-6-2"></a>
### Exercise 6.2. Independence of the chosen test function

Let \(h\) be a nonzero algebra character. Prove directly that
\(h(L_af)/h(f)\) is independent of \(f\) whenever \(h(f)\ne0\), and defines a continuous group character.

**Solution.** Lemma 1.1 and multiplicativity give
\[
 h(L_af)h(g)=h((L_af)*g)
           =h(f*(L_ag))=h(f)h(L_ag).
\]
If both denominators are nonzero, division proves independence. Fix one such \(f\), and call the quotient \(\gamma(a)\). The same identity with arbitrary \(g\) gives
\(h(L_ag)=\gamma(a)h(g)\), including when \(h(g)=0\).
Putting \(g=L_bf\) yields
\(\gamma(a+b)=\gamma(a)\gamma(b)\).
Also \(\gamma(0)=1\), so \(\gamma(a)\gamma(-a)=1\). Continuity of translations in \(L^1\), followed by boundedness of \(h\), makes \(\gamma\) continuous. Contractivity of \(h\) and the isometry of translations give
\[
 |\gamma(a)|\le\frac{\|f\|_1}{|h(f)|}
\]
uniformly in \(a\). Applying this to all integer multiples of \(a\), positive and negative, forces \(|\gamma(a)|=1\). Thus \(\gamma\in\widehat G\), with exactly the claimed independence. \(\square\)

<a id="ha-lca-03-exercise-6-3"></a>
### Exercise 6.3. A necessary condition for an \(L^1\) unit

Show that if \(L^1(G)\) has an identity for convolution, then \(\widehat G\) is compact.

**Solution.** Let \(e*f=f\) for all \(f\in L^1(G)\). Fix \(\gamma\in\Gamma\). Lemma 1.2 supplies an \(f\) with
\(h_{\gamma^{-1}}(f)=1\).
Applying this functional to \(e*f=f\) gives
\(h_{\gamma^{-1}}(e)=1\), which means \(\widehat e(\gamma)=1\).
Thus \(\widehat e\) is the constant one function on \(\Gamma\). By Theorem 3.1 it belongs to \(C_0(\Gamma)\), so its level set
\(\{\gamma:|\widehat e(\gamma)|\ge1/2\}=\Gamma\)
is compact. The argument needs neither Pontryagin duality nor a converse implication. \(\square\)

<a id="ha-lca-03-exercise-6-4"></a>
### Exercise 6.4. Uniform continuity for a finite measure

Prove that \(\widehat\mu\) is uniformly continuous for every finite complex Radon measure \(\mu\), using compact tails explicitly.

**Solution.** Given \(\varepsilon>0\), choose compact \(K\subseteq G\) with
\(|\mu|(G\setminus K)<\varepsilon/4\).
For any \(\gamma,\eta\in\Gamma\), the character law and variation estimate give
\[
 \begin{aligned}
 |\widehat\mu(\gamma\eta)-\widehat\mu(\gamma)|
 &\le\int_G|\eta(x)-1|\,d|\mu|(x)\\
 &\le\|\mu\|\sup_{x\in K}|\eta(x)-1|
         +2|\mu|(G\setminus K).
 \end{aligned}
\]
Take the compact-convergence neighbourhood
\(U=N(K,\varepsilon/(2(1+\|\mu\|)))\).
The right side is strictly less than \(\varepsilon\) for every \(\eta\in U\), independently of \(\gamma\). This is the asserted group-uniform continuity. The argument uses one fixed compact set and a neighbourhood, so also controls every net approaching the identity. \(\square\)

<a id="ha-lca-03-exercise-6-5"></a>
### Exercise 6.5. The real-line spectrum directly

Identify the spectrum of \(L^1(\mathbb R)\), with its weak-star topology, with the usual real line, without using the general homeomorphism in Theorem 2.1.

**Solution.** Let \(h\) be a nonzero algebra character. Choose \(f_0\in C_c(\mathbb R)\) with \(h(f_0)=1\), using contractivity and density. The calculation in Exercise 6.2, which uses only translation identities, proves that
\(\gamma(x)=h(L_xf_0)\)
is a continuous real-line character and
\(h(L_xf)=\gamma(x)h(f)\).
HA-LCA-02, Theorem 3.1, therefore gives
\(\gamma(x)=E(\xi x)\) for a unique \(\xi\in\mathbb R\).
The finite approximation identity of Lemma 1.1 now gives
\[
 h(f)=h(f*f_0)=\int_{\mathbb R}f(x)h(L_xf_0)\,dx
             =\int_{\mathbb R}f(x)E(\xi x)\,dx.
\]
Conversely these functionals are nonzero algebra characters by Lemma 1.2, and that lemma proves their distinctness. This establishes the algebraic identification directly.

For its forward continuity, fix \(f\in L^1(\mathbb R)\) and choose \(u\in C_c(\mathbb R)\) with small \(\|f-u\|_1\). Let its support lie in \([-R,R]\). The exponential Lipschitz estimate gives
\[
 |h_\xi(f)-h_\eta(f)|
 \le2\|f-u\|_1+2\pi R\|u\|_1|\xi-\eta|.
\]
Choosing first \(u\) and then \(|\xi-\eta|\) proves continuity for every weak-star coordinate.

For inverse continuity at \(\eta\), use the single integrable test function
\(g_\eta(x)=e^{-\pi x^2}e^{-2\pi i\eta x}\).
The earlier Gaussian transform gives
\[
 h_\xi(g_\eta)=e^{-\pi(\xi-\eta)^2},\qquad h_\eta(g_\eta)=1.
\]
Given \(\varepsilon>0\), the weak-star neighbourhood
\[
 |h(g_\eta)-1|<1-e^{-\pi\varepsilon^2}
\]
contains \(h_\eta\). For \(h=h_\xi\), the explicit real positive value above shows that this inequality forces \(|\xi-\eta|<\varepsilon\). Hence the inverse is continuous. This proof of the topology on the real-line spectrum uses the scalar Gaussian calculation and no general spectrum homeomorphism. \(\square\)

## 7. The next step

We have identified all nonzero multiplicative functionals on \(L^1(G)\), proved its transform laws and uniform density, and embedded \(L^1(G)\) as a closed ideal in the finite-measure algebra. General injectivity and inversion for Fourier transforms will be proved later in the course. None of those later conclusions was needed in the spectrum or density proofs here.

