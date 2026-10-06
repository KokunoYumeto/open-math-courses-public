# Jets, supported distributions and local operators

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

A distribution concentrated on a point can measure derivatives of a test there. A distribution concentrated on a plane can measure normal derivatives along that plane, with distributions as tangential coefficients. The total order limits both kinds of measurement: spending one derivative in the normal direction leaves one fewer tangential derivative available. We prove that precise order bound, then use it to characterize operators whose kernels lie on the diagonal.

The prerequisites are [Distributions as kernels of continuous operators](distributions-as-kernels.md), [Tensor products and parameter-dependent distributions](tensor-products-and-parameters.md), Taylor's formula, smooth cutoffs and convolution with a smooth compactly supported function. We use ordinary derivatives \(\partial\), with the bilinear distribution convention; no powers of \(i\) are hidden in the coefficients. Basic references are [Dyatlov 2026], [Melrose 2016] and [Whitney 1934]. The special extension needed here is proved directly by smoothing at a scale set by the distance to the plane.

## What a supported distribution can detect

The order of a distribution is at most \(k\) if, on each fixed compact test-support set, its pairing is bounded by a constant times the supremum of derivatives through order \(k\). The constant may depend on the compact set. For a compactly supported distribution, one compact neighborhood of its support gives
\[
|u(f)|\le C\max_{|\gamma|\le k}\sup_M|\partial^\gamma f|
\tag{1.1}
\]
for all smooth \(f\), after a cutoff equal to one near the support. The controlling set \(M\) is a neighborhood of the support; (1.1) is not an assertion that the supremum may be restricted to the support itself.

An order-at-most-\(k\) distribution acts on compactly supported \(C^k\) functions. To define the pairing, approximate such a function by smooth ones, with one common compact support and uniform convergence of derivatives through order \(k\). Convolution after a slightly larger cutoff supplies these approximations. The order bound makes their pairings Cauchy and makes the limit independent of the approximation. For a compact distribution the same construction acts on arbitrary \(C^k\) functions, by a cutoff near its support.

**Theorem 1.1 (vanishing jets are invisible).** Let \(u\) be a distribution of order at most \(k\), and let \(f\in C_c^k(U)\). If
\[
\partial^\gamma f(x)=0
\quad(x\in\operatorname{supp}u,\ |\gamma|\le k),
\tag{1.2}
\]
then \(u(f)=0\). If \(u\) is compactly supported, \(f\) need not have compact support.

**Proof.** First assume \(u\) has compact support \(F\) in Euclidean space. For \(\varepsilon>0\), write \(F_a\) for the open \(a\)-neighborhood of \(F\). Take a nonnegative smooth mollifier \(\rho\) of integral one supported in the unit ball, and put
\[
\chi_\varepsilon=\mathbf1_{F_{2\varepsilon}}*\rho_\varepsilon.
\]
For small \(\varepsilon\), this is a compact smooth function supported in a fixed neighborhood of \(F\). It equals one on \(F_\varepsilon\), is supported in \(\overline{F_{3\varepsilon}}\), and satisfies
\[
|\partial^\beta\chi_\varepsilon|\le C_\beta\varepsilon^{-|\beta|}.
\tag{1.3}
\]
These estimates follow by differentiating the mollifier and taking its \(L^1\) norm; the indicator is bounded by one.

Taylor's formula at a nearest point of \(F\), with (1.2), gives, uniformly near \(F\),
\[
|\partial^\gamma f(x)|
\le C\operatorname{dist}(x,F)^{k-|\gamma|}
\omega(\operatorname{dist}(x,F)),
\quad |\gamma|\le k,
\tag{1.4}
\]
where \(\omega(a)\to0\) as \(a\downarrow0\). One can take a constant multiple of a common modulus of continuity of the order-\(k\) derivatives on a fixed compact neighborhood. For \(|\gamma|=k\), (1.4) is the continuity estimate against a derivative which is zero on \(F\). For lower orders it follows from the integral Taylor remainder along the segment to the nearest point.

The functions \(f\) and \(\chi_\varepsilon f\) agree near \(F\), so they have the same pairing with \(u\). This also holds for \(C^k\) functions: approximate a function vanishing on a neighborhood of \(F\) by smooth functions still vanishing on a smaller neighborhood, and use the order estimate. The product rule, (1.3) and (1.4) give
\[
\max_{|\gamma|\le k}\|\partial^\gamma(\chi_\varepsilon f)\|_\infty
\le C'\omega(3\varepsilon)
\quad(0<\varepsilon\le1).
\]
The possible powers \(\varepsilon^{k-|\gamma|}\) are at most one and do not obstruct convergence to zero. Estimate (1.1) proves \(u(f)=0\).

For an arbitrary distribution and compactly supported \(f\), multiply \(u\) by a cutoff equal to one near \(\operatorname{supp}f\). The resulting compact distribution has order at most \(k\) and support contained in \(\operatorname{supp}u\), so the case just proved applies. Its pairing with \(f\) equals that of \(u\). For a compact \(u\) and a noncompact \(f\), first cut off \(f\) near \(\operatorname{supp}u\). Its vanishing jets there are preserved. \(\square\)

The theorem concerns jets that vanish. It does not provide a norm estimate using only the values of a jet on an arbitrary closed support. An extension problem enters when we prescribe a nonzero jet.

## Extending one normal jet without losing derivatives

Write \((t,z)\in\mathbb R^d\times\mathbb R^n\), with \(d\ge1\), and let \(\alpha\) be a multi-index in the \(t\) variables. Put \(a=|\alpha|\), and fix an integer \(k\ge a\). For a function on Euclidean space, \(\|\cdot\|_{C^s}\) denotes the maximum of the suprema of all derivatives through order \(s\).

**Lemma 2.1 (a controlled normal-jet extension).** Let \(s=k-a\). For each \(g\in C_c^s(\mathbb R^n)\), there is a compactly supported \(G\in C^k(\mathbb R^{d+n})\), linear in \(g\), such that
\[
\partial_t^\beta G(0,z)=
\begin{cases}g(z),&\beta=\alpha,\\0,&\beta\ne\alpha,\end{cases}
\quad |\beta|\le k,
\tag{2.1}
\]
and
\[
\|G\|_{C^k}\le C_{k,\alpha}\|g\|_{C^s}.
\tag{2.2}
\]
If \(g\) ranges over functions supported in one compact set, all these extensions have one common compact support. The assertion includes \(s=0\).

**Proof.** We give the construction and its full regularity estimate.

Choose a smooth compactly supported function \(\rho\) on \(\mathbb R^n\) with
\[
\int\rho=1,\qquad \int w^\gamma\rho(w)\,dw=0
\quad(1\le|\gamma|\le k).
\tag{2.3}
\]
Positivity is not required. Such a function is easy to construct with finitely many dilations. Start with any integral-one smooth bump \(\rho_0\). Choose distinct positive numbers \(\lambda_0,\ldots,\lambda_k\), and solve the Vandermonde system
\[
\sum_{j=0}^k c_j\lambda_j^b=
\begin{cases}1,&b=0,\\0,&1\le b\le k.\end{cases}
\]
Then \(\rho(w)=\sum_jc_j\lambda_j^{-n}\rho_0(w/\lambda_j)\) has (2.3), since a moment of total degree \(b\) scales by \(\lambda_j^b\).

For \(h>0\), set \(\rho_h(w)=h^{-n}\rho(w/h)\), and for \(t\ne0\) define
\[
G_0(t,z)=\frac{t^\alpha}{\alpha!}(g*\rho_{|t|})(z).
\tag{2.4}
\]
The scale \(|t|\) is smooth off the plane. The moment conditions make convolution reproduce every polynomial of degree at most \(s\), independently of the scale. In particular, differentiating that convolution in \(t\) kills each such polynomial whenever at least one \(t\) derivative is taken.

Let \(b=|\beta|\), \(c=|\gamma|\), and \(b+c\le k\). Differentiating a scaled convolution kernel in \(t\) through total order \(b\), and in \(z\) through total order \(c\), costs at most a constant times \(|t|^{-b-c}\) in its \(L^1\) norm. Here each derivative of \(|t|\) has size bounded by a constant times the appropriate power of \(|t|\); the chain rule gives the same scaling at every order. The differentiated kernels remain supported in \(|w|\le R|t|\), with fixed \(R\).

At a fixed \(z\), subtract the Taylor polynomial of \(g\) through degree \(s\). Its remainder on that ball is bounded by
\[
C|t|^s\omega_g(R|t|),
\tag{2.5}
\]
where \(\omega_g(h)\to0\), uniformly in \(z\). For \(s=0\), this is the modulus of continuity of \(g\). For \(s>0\), it is a constant multiple of the modulus of continuity of the order-\(s\) derivatives, by the integral Taylor formula. The differentiated kernel estimate therefore gives
\[
\partial_t^\nu\partial_z^\gamma(g*\rho_{|t|})(z)=
\begin{cases}\partial_z^\gamma g(z),&\nu=0,\ c\le s,\\0,&\text{otherwise},\end{cases}
+O\big(|t|^{s-|\nu|-c}\omega_g(R|t|)\big).
\tag{2.6}
\]
The leading term is found by applying the differentiated convolution to the fixed Taylor polynomial, using polynomial reproduction. If \(c>s\), that derivative of the polynomial is zero. If \(\nu\ne0\), its convolution is scale-independent, so that term is zero. This justifies (2.6) even when the derivatives of \(g\) appearing in the remainder calculation do not exist beyond order \(s\).

Apply the product rule to (2.4). When \(\beta\le\alpha\) coordinatewise and \(c\le s\), the leading term is
\[
\frac{t^{\alpha-\beta}}{(\alpha-\beta)!}\partial_z^\gamma g(z).
\tag{2.7}
\]
Otherwise there is no leading term. Every remainder is bounded by
\[
C|t|^{k-b-c}\omega_g(R|t|),
\tag{2.8}
\]
because the degree \(a\) of the prefactor and \(s=k-a\) add to \(k\). Thus all derivatives of \(G_0\) through order \(k\), initially defined off the plane, extend continuously to it. Their traces are zero except for \(\beta=\alpha\), \(c\le s\), when the trace is \(\partial_z^\gamma g\).

These extensions really are the derivatives of a \(C^k\) function. One can verify this successively in derivative order. Along a normal coordinate segment leaving the plane, use the fundamental theorem of calculus off the plane and then the continuous limiting derivative at its endpoint. Along a tangential segment in the plane, the asserted nonzero traces are derivatives of \(g\), whose required orders are at most \(s\); all other traces are zero. This proves differentiability in each coordinate across the plane, with the prescribed continuous partial derivatives, at each order up to \(k\).

On \(0<|t|\le1\), the same calculations with \(\omega_g\) bounded by \(C\|g\|_{C^s}\) give a uniform \(C^k\) bound for \(G_0\). Choose a compact smooth \(\theta(t)\), equal to one near zero and supported in \(|t|<1\), and put \(G=\theta G_0\), with the continuous extension at the plane. The product rule proves (2.2), and multiplication by \(\theta\) preserves (2.1). If \(g\) is supported in \(M\), the extension is supported in the compact product of \(\operatorname{supp}\theta\) with \(M+\overline{B(0,R)}\). This proves every assertion. If \(n=0\), there is no convolution: take \(G(t)=\theta(t)t^\alpha g/\alpha!\), with the same conclusions. \(\square\)

The elementary extension \(t^\alpha g(z)/\alpha!\) would require too many tangential derivatives away from the plane. The scale-dependent smoothing in (2.4) supplies those missing derivatives, while the vanishing moments preserve the prescribed jet.

## The exact structure on a plane

**Theorem 3.1 (normal jets of a supported distribution).** Let \(u\in\mathcal E'(\mathbb R^{d+n})\) have order at most \(k\), with
\[
\operatorname{supp}u\subset\{0\}\times\mathbb R^n.
\]
There are unique compactly supported distributions \(w_\alpha\) on \(\mathbb R^n\), for \(|\alpha|\le k\), such that
\[
u(f)=\sum_{|\alpha|\le k}w_\alpha\big(\partial_t^\alpha f(0,\cdot)\big)
\tag{3.1}
\]
for every smooth \(f\). Each \(w_\alpha\) has order at most \(k-|\alpha|\), and its support is contained in the tangential projection of \(\operatorname{supp}u\). Equivalently,
\[
u=\sum_{|\alpha|\le k}(-1)^{|\alpha|}
(\partial_t^\alpha\delta_0)\otimes w_\alpha.
\tag{3.2}
\]
Formula (3.1) also holds for all \(C^k\) functions, using the continuous extensions of the pairings.

**Proof.** Choose \(\theta(t)=1\) near zero with compact support, and define
\[
w_\alpha(g)=u\left(\theta(t)\frac{t^\alpha}{\alpha!}g(z)\right),
\quad g\in\mathcal D(\mathbb R^n).
\tag{3.3}
\]
Initially this is a distribution of order at most \(k\). Its support lies in the stated projection, because the test in (3.3) vanishes near \(\operatorname{supp}u\) when \(g\) does. It is independent of \(\theta\) with the specified value near zero.

Taylor expansion in the normal variables shows that
\[
f(t,z)-\theta(t)\sum_{|\alpha|\le k}
\frac{t^\alpha}{\alpha!}\partial_t^\alpha f(0,z)
\]
has every total derivative through order \(k\) equal to zero on the plane. Theorem 1.1 therefore makes its pairing with \(u\) zero, proving (3.1) on smooth functions. Testing a proposed representation on the functions in (3.3) isolates each coefficient, proving uniqueness. The signs in (3.2) are precisely the signs of distributional differentiation of the point mass.

To obtain the sharper coefficient order, apply Lemma 2.1 to a smooth compactly supported \(g\), using \(s=k-|\alpha|\). Let \(G\) be its \(C^k\) extension with only the normal jet \(\alpha\) nonzero. The difference between \(G\) and the test in (3.3) has all total derivatives through order \(k\) zero on the plane. Theorem 1.1 applies to that \(C^k\) difference, so
\[
w_\alpha(g)=u(G).
\]
Estimate (1.1) and (2.2) give
\[
|w_\alpha(g)|\le C'\|g\|_{C^{k-|\alpha|}},
\tag{3.4}
\]
proving the claimed order. Finally, approximate an arbitrary \(C^k\) function on a neighborhood of the compact support by smooth functions in that norm. Its normal trace of order \(|\alpha|\) converges in \(C^{k-|\alpha|}\) on tangential compact sets. The bounds just proved permit passage to the limit in (3.1). \(\square\)

When \(n=0\), the coefficients are scalars, and the theorem says that a distribution supported at one point is a finite sum of derivatives of a point mass, with degree bounded by its order. Translation moves the point from zero to any prescribed point. Conversely every such finite sum has that support containment and finite order. This is the point-supported structure theorem; the plane theorem gives its tangential version with the additional order information.

Localizing an arbitrary distribution supported on a plane by compact cutoffs gives the same description locally. The number of normal derivatives can increase from one region to another. Coefficient uniqueness makes those local descriptions agree on overlaps.

**Corollary 3.2 (coordinate multiplication singles out the point mass).** Let \(X\subset\mathbb R^d\) be open, \(d\geq1\), and suppose \(u\in\mathcal D'(X)\) obeys \(x_j u=0\) for every \(j=1,\ldots,d\). If \(0\in X\), then \(u=c\delta_0\) for a unique scalar \(c\). If \(0\notin X\), then \(u=0\); every scalar multiple of the restricted \(\delta_0\) is then zero, so no uniqueness of that scalar is asserted.

**Proof.** Near any nonzero point some coordinate \(x_j\) is nonzero. Multiplication there by its smooth reciprocal shows \(u=(1/x_j)(x_j u)=0\). Consequently the support is contained in \(\{0\}\). If the origin is absent, empty support gives the zero distribution. If it is present, choose \(\chi\in C_c^\infty(X)\) equal to one near it. Multiplication by \(\chi\) does not change \(u\). The pairing \(\phi\mapsto u(\chi\phi)\) extends it to a compact distribution on \(\mathbb R^d\) supported at zero: its continuity follows from the test estimate on the fixed support of \(\chi\). Apply the point-supported specialization of Theorem 3.1 to this extension and restrict back to \(X\). It gives a finite sum \(u=\sum_\alpha c_\alpha\partial^\alpha\delta_0\) with unique coefficients. The product rule on test jets gives

\[
x_j\partial^\alpha\delta_0
=-\alpha_j\partial^{\alpha-e_j}\delta_0
\quad(\alpha_j>0),
\qquad x_j\partial^\alpha\delta_0=0
\quad(\alpha_j=0).
\tag{3.5}
\]

For fixed \(j\), every resulting jet index \(\beta\) receives exactly the coefficient \(-(\beta_j+1)c_{\beta+e_j}\). Their independence and the equation \(x_ju=0\) make each such coefficient zero. Every positive-degree \(\alpha\) has \(\alpha_j>0\) for at least one coordinate, so only \(c_0\delta_0\) remains. A test equal to one near zero recovers \(c_0\) uniquely. \(\square\)

## Kernels on the diagonal

Let \(X\subset\mathbb R^n\) be open. A linear map \(T:\mathcal D(X)\to\mathcal D'(X)\) is support-preserving if
\[
\operatorname{supp}T\phi\subset\operatorname{supp}\phi
\quad(\phi\in\mathcal D(X)).
\tag{4.1}
\]

**Theorem 4.1 (continuous local operators with distributional coefficients).** Suppose \(T\) is weakly continuous. The following conditions are equivalent:

1. \(T\) is support-preserving.
2. Its kernel is supported in the diagonal \(\{(x,y):x=y\}\).
3. There are unique distributions \(a_\alpha\in\mathcal D'(X)\), locally finite as a family, such that
\[
T\phi=\sum_\alpha a_\alpha\,\partial^\alpha\phi.
\tag{4.2}
\]

Here locally finite means that every point has a neighborhood on which all but finitely many \(a_\alpha\) vanish. Consequently every compact set meets the supports of only finitely many nonzero terms. The order need not be bounded on all of \(X\). Every locally finite expression (4.2) defines a weakly continuous support-preserving map.

**Proof.** If (4.1) holds, take disjoint open neighborhoods \(A,B\subset X\). For \(\psi\in\mathcal D(A)\), \(\phi\in\mathcal D(B)\),
\[
K(\psi\otimes\phi)=\langle T\phi,\psi\rangle=0.
\]
Product tests detect distributions, so \(K\) vanishes on \(A\times B\). Such rectangles cover the complement of the diagonal, proving condition 2. Conversely, if the kernel is supported in the diagonal, its support relation from Proposition 6.5 of the kernel lesson sends \(\operatorname{supp}\phi\) into itself, proving condition 1.

For condition 2 to imply condition 3, change variables by
\[
z=x,\qquad t=y-x.
\]
This invertible linear map has determinant of absolute value one. The kernel in these variables is supported on \(t=0\). Near any fixed relatively compact output region, multiply it by a compact cutoff in \(z\) and a cutoff in \(t\) equal to one near zero. Choose the latter with sufficiently small support that \(z+t\in X\) on the chosen coordinate region. Extend that compact localization by zero into the full Euclidean product. It has some finite order \(k\), so Theorem 3.1 applies.
For an original test \(H(x,y)\), write \(\widetilde H(t,z)=H(z,z+t)\). On a smaller output region where the localizing cutoff is one, the formula is
\[
K(H)=\sum_{|\alpha|\le k}
w_\alpha\big(\partial_t^\alpha\widetilde H(0,\cdot)\big).
\]
Only the germ of the test near the diagonal contributes, so inserting a normal cutoff equal to one there does not affect this formula. On a product test \(H(x,y)=\psi(x)\phi(y)\), with \(\psi\) supported in that smaller output region, it becomes
\[
K(\psi\otimes\phi)=\sum_{|\alpha|\le k}
w_\alpha(\psi\,\partial^\alpha\phi).
\]
Thus \(a_\alpha=w_\alpha\) gives (4.2) locally. Changing local cutoffs does not affect the distribution near the diagonal over a smaller output region. Uniqueness in Theorem 3.1 makes the coefficients agree on these smaller regions, including zero coefficients beyond the locally required order. They therefore glue to unique distributions \(a_\alpha\) on \(X\). Their orders and the number of terms are locally bounded, giving the stated local finiteness.

Finally start with a locally finite expression. On each compact output test support, only finitely many terms contribute. Pairing a term with \(\psi\) gives \(a_\alpha(\psi\partial^\alpha\phi)\), a continuous scalar functional of \(\phi\) on every fixed input support space. The inductive-limit property gives weak continuity. Each term has support contained in \(\operatorname{supp}\phi\), since multiplication of a distribution by a smooth function cannot create support where that function is locally zero. The locally finite sum has the same property. The kernel theorem then supplies its kernel, completing all implications. \(\square\)

There is a regularity refinement, provided continuity has been assumed as in this theorem.

**Corollary 4.2 (smooth outputs give smooth coefficients).** For a support-preserving weakly continuous \(T\), all the coefficients in (4.2) are smooth if and only if \(T\phi\) is smooth for every \(\phi\in\mathcal D(X)\). In that case \(T\) extends naturally to a differential operator on all distributions, by smooth multiplication and distributional differentiation.

**Proof.** Smooth coefficients plainly give smooth test outputs. For the converse, fix a relatively compact coordinate neighborhood \(W\) where (4.2) has order at most \(k\). Choose \(\chi\in\mathcal D(X)\), equal to one near \(\overline W\). The test \(\chi\) gives \(a_0=T\chi\) on \(W\), so \(a_0\) is smooth there. For a multi-index \(\beta\), test with \(\chi x^\beta/\beta!\). On \(W\),
\[
T(\chi x^\beta/\beta!)
=\sum_{\alpha\le\beta}a_\alpha
\frac{x^{\beta-\alpha}}{(\beta-\alpha)!}.
\]
The term \(\alpha=\beta\) is \(a_\beta\). Induction on total degree expresses it as a smooth output minus smooth polynomial multiples of previously proved smooth coefficients. Thus every locally present coefficient is smooth. These local conclusions give global smoothness. The extension to distributions is defined by the locally finite expression, with its smooth coefficients, and agrees on test functions. Its transpose takes a compact test to a compact test by finitely many derivatives and smooth multiplications on its support; this also proves continuity of the extension for the strong distribution topology. \(\square\)

The hypothesis of weak continuity was used to obtain a distribution kernel. Removing that hypothesis for maps with smooth outputs is a further theorem of Peetre; it is not a consequence of the kernel theorem alone.

## A local operator need not have a global order

On \(\mathbb R\), choose nonzero smooth bumps \(b_j\), supported in \((3j-1/4,3j+1/4)\), for integers \(j\ge1\), and positive at \(3j\). Set
\[
T\phi=\sum_{j\ge1}b_j\partial^j\phi.
\]
The sum is locally finite, so it defines a continuous support-preserving map. Its coefficients are smooth, but it has no finite order valid everywhere. Indeed its unique coefficient of degree \(j\) is \(b_j\), which is nonzero for every \(j\). A competing finite-order representation would contradict coefficient uniqueness. The associated kernel lies on the diagonal and its order grows with the location along that diagonal.

A distributional coefficient can instead concentrate the output. For example,
\[
T\phi=\phi'(2)\delta_2
\]
has coefficient \(a_1=\delta_2\) and all other coefficients zero. Its kernel pairs as \(K(H)=\partial_yH(2,2)\), or \(K=-\delta_2\otimes\delta'_2\). It is support-preserving, but a test with \(\phi'(2)\ne0\) has a singular output. Thus diagonal support alone does not make the coefficients smooth.

## Exercises

**Exercise 1 (basic: vanishing order and point masses).** Let \(u=3\delta_0-2\delta'_0+\delta''_0\). Express \(u(f)\) in terms of the jet of \(f\) at zero. Find its exact order, and show directly that it kills every \(C^2\) function with its first three jet values zero.

**Exercise 2 (intermediate: recovering tangential coefficients).** On \(\mathbb R_t\times\mathbb R_z\), define
\[
u(f)=\int_0^1 f(0,z)\,dz
+\partial_t\partial_z f(0,1/2)
-2\partial_t^2 f(0,1/3).
\]
Find the \(w_\alpha\) in (3.1), their orders and their supports. Determine the exact order of \(u\), and verify the coefficient-order bound.

**Exercise 3 (intermediate: a moment-cancelling mollifier).** Let \(\rho_0\) be an even smooth integral-one bump on the line, and let \(\rho_{0,2}(x)=\rho_0(x/2)/2\). Show that \(\rho=(4\rho_0-\rho_{0,2})/3\) has vanishing first and second moments. Explain why using a nonnegative mollifier could not give all the required moment conditions for the normal-jet extension.

**Exercise 4 (advanced: normal derivatives and coefficient order).** Let \(v\) be a nonzero point-supported distribution of exact order \(s\) on \(\mathbb R^n\), and take a transverse multi-index \(\alpha\). Prove that \((\partial_t^\alpha\delta_0)\otimes v\) has exact order \(|\alpha|+s\). Use suitable scaled tests, rather than inferring equality from the upper bound for a tensor product.

**Exercise 5 (advanced: deciding locality from a kernel).** Let \(h\in C^\infty(\mathbb R)\) be nowhere zero. Compare
\[
T_1\phi(x)=h(x)\phi'(x),\qquad
T_2\phi(x)=h(x)\phi'(x+1).
\]
Find their distributional kernels and their supports. Which operator is support-preserving? Find the bilinear transpose of each one and retain all coefficient derivatives and translation signs.

**Exercise 6 (intermediate: annihilation at a translated point).** Let \(a\in X\subset\mathbb R^d\), and suppose \((x_j-a_j)u=0\) for all coordinates. Determine \(u\). For \(v=\partial_1\delta_a\), compute \((x_1-a_1)v\) and the other coordinate products. Explain why support at \(a\) alone is weaker than simultaneous coordinate annihilation.

## Solutions

**Solution 1.** Distributional derivatives give
\[
u(f)=3f(0)+2f'(0)+f''(0).
\]
It has order at most two and annihilates the stated vanishing jets. Choose \(g\in\mathcal D(\mathbb R)\) with \(g''(0)\ne0\), and set \(f_\varepsilon(x)=\varepsilon g(x/\varepsilon)\). Its supremum and first derivative are uniformly bounded, while the pairing contains \(\varepsilon^{-1}g''(0)\); the lower-order terms remain bounded. Thus an order-one estimate is impossible, and the exact order is two.

**Solution 2.** The coefficients are
\[
w_0=\mathbf1_{[0,1]}(z)\,dz,
\qquad w_1=-\delta'_{1/2},
\qquad w_2=-2\delta_{1/3}.
\]
Their supports are \([0,1]\), \(\{1/2\}\), \(\{1/3\}\), and their exact orders are zero, one and zero. The product derivatives in the displayed formula give total order at most two. Localizing near \((0,1/3)\), away from \(z=1/2\), choose \(f_\varepsilon(t,z)=\varepsilon g(t/\varepsilon)b(z)\), with \(g''(0)\ne0\), \(b(1/3)\ne0\), and \(b\) supported near \(1/3\). First derivatives remain uniformly bounded, while the normal-second-derivative term has size proportional to \(\varepsilon^{-1}\); the integral term tends to zero. Hence the exact total order is two. The bounds \(\operatorname{ord}w_j\le2-j\) hold, with equality for \(j=1,2\).

**Solution 3.** Evenness gives zero first moments for both bumps. If the second moment of \(\rho_0\) is \(M_2\), that of its dilation is \(4M_2\). Thus the integral of \(\rho\) is \((4-1)/3=1\), and its second moment is \((4M_2-4M_2)/3=0\). A nonnegative smooth integral-one function has strictly positive \(\int x^2\rho(x)\,dx\): if that integral were zero, it would vanish away from zero, and smoothness would force its integral to be zero. Signed kernels are therefore necessary once second-moment cancellation is required.

**Solution 4.** The point-supported specialization of Theorem 3.1 gives \(v=\sum_{|\beta|\le s}c_\beta\partial_z^\beta\delta_b\), with some coefficient of total degree \(s\) nonzero. If all such coefficients vanished, the order would be at most \(s-1\). Choose compact smooth \(g\) in \(t\) with \(\partial_t^\alpha g(0)\ne0\). Choose compact smooth \(q\) in \(z\) whose order-\(s\) jet at zero makes \(\sum_{|\beta|=s}c_\beta(-1)^{|\beta|}\partial^\beta q(0)\ne0\); a polynomial jet times a cutoff produces one. For \(m=|\alpha|+s>0\), take
\[
f_\varepsilon(t,z)=\varepsilon^{m-1}g(t/\varepsilon)q((z-b)/\varepsilon).
\]
All derivatives through total order \(m-1\) are uniformly bounded, and the top-order pairing is a nonzero multiple of \(\varepsilon^{-1}\). The terms from \(|\beta|<s\) remain bounded. Thus order at most \(m-1\) is impossible. The tensor derivative estimate gives order at most \(m\), so the exact order is \(m\). If \(m=0\), the product is a nonzero multiple of the point mass at \((0,b)\), with exact order zero.

**Solution 5.** Let
\[
D_c(H)=\int h(x)H(x,x+c)\,dx.
\]
Then the kernels are \(K_1=-\partial_yD_0\), \(K_2=-\partial_yD_1\), because their pairings with \(\psi(x)\phi(y)\) give the derivative of \(\phi\) on the corresponding graph. Their supports are exactly \(y=x\) and \(y=x+1\). Containment follows from differentiation not increasing support. For equality, take a small graph neighborhood and a test \(H(x,y)=a(x)(y-x-c)b(y-x-c)\), with \(b=1\) near zero and \(\int h(x)a(x)\,dx\ne0\). Its pairing is nonzero and it can be supported in that neighborhood. Such an \(a\) exists because \(h\) is nowhere zero and continuous.

The first operator is support-preserving by Theorem 4.1. The second is not: choose a test whose derivative is nonzero near an input point \(y_0\), with support in an interval of length less than \(1/2\). Its output is nonzero near \(y_0-1\), outside that input support. Integration by parts gives
\[
T_1^t\psi(y)=-\partial_y(h(y)\psi(y)),
\]
and, after setting \(y=x+1\),
\[
T_2^t\psi(y)=-\partial_y(h(y-1)\psi(y-1)).
\]
Expanding either derivative gives both the derivative of \(h\) and the derivative of \(\psi\), each with the displayed minus sign. These are bilinear transposes; complex conjugation would belong to a separate sesquilinear adjoint convention.

**Solution 6.** Translate coordinates by \(a\) and apply Corollary 3.2; it gives \(u=c\delta_a\), with unique scalar since \(a\in X\). Formula (3.5) gives \((x_1-a_1)\partial_1\delta_a=-\delta_a\), while every other coordinate product is zero. Thus \(v\) has support at the single point but fails one of the annihilation equations. More general positive-degree point jets also have point support and can fail these equations; the simultaneous vanishing is what removes all such derivatives.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- [Melrose 2016] Richard Melrose, *18.155 Lecture 15: Schwartz's kernel theorem*, MIT, 2016. [Open lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf).
- [Whitney 1934] Hassler Whitney, *Analytic extensions of differentiable functions defined in closed sets*, Transactions of the American Mathematical Society 36 (1934), 63–89. [Full text](https://www.ams.org/journals/tran/1934-036-01/S0002-9947-1934-1501735-3/S0002-9947-1934-1501735-3.pdf).
