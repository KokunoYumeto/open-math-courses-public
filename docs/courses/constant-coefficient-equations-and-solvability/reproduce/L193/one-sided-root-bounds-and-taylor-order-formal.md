# One-sided root bounds and Taylor order

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A bound on the upper imaginary parts of every nearby zero can force vanishing of all low-degree Taylor coefficients. The bound must hold for both signs of a real parameter. We prove the full germ statement with complex coefficients and repeated zeros.

Basic references are [Cauchy bounds, root counts and analytic extensions][cauchy], Puiseux's *Recherches sur les fonctions algébriques*, and Helmke's *On the Newton-Puiseux Series*. Newton's lowest-weight construction motivates the finite polynomial below. The proof uses the available Cauchy expansion and Rouché theorem in the first reference.

## 1. The two orders and the local hypothesis

Let \(g(z,\lambda)\) be holomorphic near \((0,0)\in\mathbb C^2\). Suppose that \(g(z,0)\) has finite exact zero order \(d\ge0\). Thus its first nonzero coefficient is the coefficient of \(z^d\). Write the convergent expansion as

\[
g(z,\lambda)=\sum_{j,\ell\ge0}a_{j\ell}z^j\lambda^\ell,
\qquad a_{d0}\ne0,\qquad a_{j0}=0\ (j<d).
\tag{1}
\]

The total Taylor order is the least \(j+\ell\) for which \(a_{j\ell}\ne0\). It is at most \(d\).

The expansion is absolutely convergent on a sufficiently small closed bidisk. Indeed, Lemma 1.1 and the iterated Cauchy formula in [Cauchy bounds, root counts and analytic extensions][cauchy] express each coefficient by the product-circle integral. If that product has radii \(R,S>0\) and supremum \(M\), then \(|a_{j\ell}|\le M R^{-j}S^{-\ell}\). The product of two geometric series proves absolute convergence at any smaller radii; expanding both Cauchy denominators identifies its sum with \(g\).

Our zero hypothesis means that there are \(\rho,\varepsilon>0\) and \(C\ge0\) such that \(g\) is defined on the product of these open disks and

\[
\begin{gathered}
|\lambda|<\varepsilon,\quad\lambda\in\mathbb R,\quad
|z|<\rho,\quad g(z,\lambda)=0\\
\Longrightarrow\quad \operatorname{Im}z\le C|\lambda|.
\end{gathered}
\tag{2}
\]

The coefficients need not be real, and no lower imaginary bound is assumed.

## 2. A low-degree term determines a fractional scale

**Lemma 2.1 (the lowest weight).** Suppose that some nonzero coefficient in (1) has \(j+\ell<d\). There is a rational number \(\alpha=p/q\), in lowest terms, with \(0<\alpha<1\) and \(q\ge2\), such that every nonzero term has weight \(\alpha j+\ell\ge\alpha d\). The polynomial

\[
H_\sigma(u)=
\sum_{\alpha j+\ell=\alpha d}
a_{j\ell}\sigma^\ell u^j,\qquad \sigma\in\{1,-1\},
\tag{3}
\]

has degree \(d\), leading coefficient \(a_{d0}\), and at least one nonzero coefficient of smaller degree.

**Proof.** For each \(j<d\) for which the function's \(z^j\)-coefficient is nonzero, let \(\ell_j\) be the smallest parameter exponent with \(a_{j\ell_j}\ne0\). By (1), \(\ell_j\ge1\). There are only finitely many such \(j\), and the assumed low-degree term makes this set nonempty. Define

\[
\alpha=\min_{j<d,\ \ell_j\text{ defined}}
\frac{\ell_j}{d-j}.
\tag{4}
\]

It is positive and rational. A term with \(j+\ell<d\) makes the corresponding ratio less than one, so \(\alpha<1\). Every term with \(j<d\) satisfies \(\ell\ge\ell_j\ge\alpha(d-j)\). Terms with \(j\ge d\) satisfy the weight inequality directly. Equality occurs at \((d,0)\) and at at least one pair with \(j<d\). The equality set is finite because it has \(0\le j\le d\) and \(0\le\ell\le\alpha d\). Thus (3) has the asserted properties. Reducing \(\alpha=p/q\) gives \(q\ge2\). \(\square\)

**Lemma 2.2 (a uniform polynomial limit).** For either sign and every compact subset of the \(u\)-plane,

\[
G_{r,\sigma}(u):=r^{-\alpha d}
g(r^\alpha u,\sigma r)\longrightarrow H_\sigma(u)
\qquad(r\downarrow0).
\tag{5}
\]

**Proof.** Fix \(B>0\). Choose \(r_0>0\) such that the series is absolutely convergent at \((B r_0^\alpha,r_0)\). For \(0<r\le r_0\), the absolute value of a scaled term on \(|u|\le B\) is at most

\[
r_0^{-\alpha d}|a_{j\ell}|
(B r_0^\alpha)^j r_0^\ell
(r/r_0)^{\alpha j+\ell-\alpha d}.
\tag{6}
\]

The last factor is at most one by Lemma 2.1, and the preceding factors have a finite sum. Choose a tail of that sum arbitrarily small, uniformly in \(r\) and \(u\). Among the remaining finitely many terms, those with positive excess weight tend uniformly to zero and those with zero excess weight give (3). This proves (5), including uniform convergence on every fixed circle. Each scaled function is holomorphic on a neighborhood of any fixed compact disk when \(r\) is sufficiently small. \(\square\)

Only positive real powers of \(r\) appear here. No choice of a fractional power of the complex parameter is made.

## 3. One sign has an upper-half-plane root

**Lemma 3.1 (rotation of the limiting roots).** Under Lemma 2.1, at least one of \(H_+\) and \(H_-\) has a root \(\beta\) with \(\operatorname{Im}\beta>0\). Its multiplicity may be greater than one.

**Proof.** Equality in the weight relation says

\[
p(d-j)=q\ell.
\tag{7}
\]

Because \(p,q\) are relatively prime, every exponent \(j\) occurring in \(H_+\) is congruent to \(d\) modulo \(q\). If \(j_*\) is the least such exponent, then \(H_+(u)=u^{j_*}Q(u^q)\), where \(Q\) has positive degree and \(Q(0)\ne0\).

A nonconstant complex polynomial has a complex root: this follows from Corollary 2.3 of [Cauchy bounds, root counts and analytic extensions][rouche] by comparing the leading monomial and all lower terms on a sufficiently large circle. Applied to \(Q\), it gives a nonzero root, because \(Q(0)\ne0\). Consequently \(H_+\) has a nonzero root \(\beta\). Its full orbit
\(\beta,\omega\beta,\ldots,\omega^{q-1}\beta\), with \(\omega=e^{2\pi i/q}\), consists of \(q\) distinct roots. Their sum is zero, since \(1+\omega+\cdots+\omega^{q-1}=0\).

If \(q\ge3\), these distinct nonzero points cannot all be real: their common modulus permits only the two real points of that modulus. If none had positive imaginary part, the sum of their imaginary parts would be strictly negative. This contradicts their zero sum. Thus \(H_+\) has an upper-half-plane root.

If \(q=2\), the orbit is \(\{\beta,-\beta\}\). A nonreal member already gives an upper-half-plane root. The remaining case has a positive real root \(\beta\) and its negative. Since \(0<p/q<1\), now \(\alpha=1/2\). On every edge term the weight relation gives

\[
H_-(e^{i\pi\alpha}u)
=e^{i\pi\alpha d}H_+(u).
\tag{8}
\]

Indeed, \((-1)^\ell e^{i\pi\alpha j}=e^{i\pi(\ell+\alpha j)}=e^{i\pi\alpha d}\). Since \(e^{i\pi\alpha}=i\), the positive root \(\beta\) becomes the upper-half-plane root \(i\beta\) of \(H_-\). The identity retains every multiplicity. \(\square\)

The argument uses no conjugation symmetry. The second parameter sign supplies exactly the extra rotation needed when the first orbit consists of two real points.

## 4. The zero bound forces the Taylor order

**Theorem 4.1 (one-sided root bound).** Under (1) and (2), every coefficient with \(j+\ell<d\) vanishes. Equivalently, the total Taylor order of \(g\) is exactly \(d\).

**Proof.** If \(d=0\), the constant coefficient is nonzero, so the total order is zero. If \(d=1\), the constant coefficient is zero and \(a_{10}\ne0\), so the total order is one. For any \(d\), suppose for a contradiction that a nonzero coefficient has total degree less than \(d\).

Lemmas 2.1–3.1 give \(0<\alpha<1\), a sign \(\sigma\), and an upper-half-plane root \(\beta\) of \(H_\sigma\). Choose a closed disk \(D\) centered at \(\beta\), of positive radius less than \(\operatorname{Im}\beta/2\), whose boundary contains no root of \(H_\sigma\). Such a radius exists because this nonzero polynomial has finitely many distinct roots. Throughout \(D\), \(\operatorname{Im}u\ge c>0\) for some \(c\).

The positive number \(\min_{\partial D}|H_\sigma|\) and Lemma 2.2 allow [Rouché's theorem][rouche] to be applied on \(D\). For every sufficiently small \(r>0\), \(G_{r,\sigma}\) has the same positive number of zeros in \(D\) as \(H_\sigma\), counted with multiplicity. Choose one such zero \(u_r\). Then

\[
g(z_r,\lambda_r)=0,\qquad
z_r=r^\alpha u_r,\quad \lambda_r=\sigma r,\qquad
\operatorname{Im}z_r\ge c r^\alpha.
\tag{9}
\]

The disk is bounded, so \(z_r\to0\); also \(\lambda_r\to0\) through real parameters of the chosen sign. These zeros therefore enter the product neighborhood in (2). That hypothesis gives \(c r^\alpha\le Cr\), or \(c\le C r^{1-\alpha}\), which is impossible as \(r\downarrow0\). This proves the coefficient vanishing. Since \(a_{d0}\ne0\), the total order cannot exceed \(d\), so it equals \(d\). \(\square\)

This is a local statement. It makes no claim about roots outside the supplied neighborhood, about analytic root labels, or about simple zeros. In derivative notation it says
\(\partial_z^j\partial_\lambda^\ell g(0,0)=0\) whenever \(j+\ell<d\).

For several real parameters, the available real-line specialization in [Hyperbolicity and lower order terms][comparison], “An analytic strip comparison,” applies this theorem to \(g(z,a\lambda,b\lambda)\) and compares the resulting coefficient polynomials. Its remaining denominator and finite-rescaling argument is a separate proved application.

## References

- [Cauchy bounds, root counts and analytic extensions][cauchy], Lemma 1.1, Theorem 2.2 and Corollary 2.3. The linked proofs retain their stated component terms.
- Victor A. Puiseux, *Recherches sur les fonctions algébriques*, Journal de Mathématiques Pures et Appliquées, series 1, volume 15 (1850), 365–480. [Original article](https://www.numdam.org/item/JMPA_1850_1_15__365_0/).
- Stefan Helmke, *On the Newton-Puiseux Series*, Kyoto University Research Institute for Mathematical Sciences, 2018. [Lecture description and historical references](https://www.kurims.kyoto-u.ac.jp/kenkyubu/zengaku/18/helmke.html).

[cauchy]: ../../AN02-L045.html#cauchy-estimates-and-parameter-contours
[rouche]: ../../AN02-L045.html#modulus-and-multiplicity-on-a-disk
[comparison]: ../../AN02-L038.html#an-analytic-strip-comparison
