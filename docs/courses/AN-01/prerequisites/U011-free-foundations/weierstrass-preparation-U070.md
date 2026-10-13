# Weierstrass preparation and division

*Written by Claude Opus 5.5 (Anthropic), October 2026; Exercise 1 and its solution by GPT-6.1 Sol (OpenAI), Ultra. Self-checked by the writing AI. Original text: CC0.*

Near the origin, a holomorphic function that does not vanish identically on the last coordinate axis behaves like a polynomial in the last coordinate. It is a nonvanishing factor times a monic polynomial whose roots tend to zero, and every other holomorphic function can be divided by it with a polynomial remainder. This reading proves both statements, gives division constants that do not depend on the dividend, and deduces that the ring of convergent power series is Noetherian. In this course it supplies the analytic input for Classical finite-order preparation and division.

**Conventions.** We write \(\mathcal O_n=\mathbb C\{z_1,\ldots,z_n\}\) for the ring of germs at zero of holomorphic functions, \(z=(z',w)\) with \(w=z_n\), \(\Delta_\rho=\{w\in\mathbb C:|w|<\rho\}\) and \(\Delta'_\delta=\{z'\in\mathbb C^{n-1}:|z_k|<\delta\text{ for all }k\}\). For \(n=1\) the factor \(\mathbb C^{n-1}\) is a point. A function of several variables is holomorphic when it is continuous and holomorphic in each variable separately, as in Holomorphic functions of several variables, Definition 1.1; Theorem 2.1 there gives Taylor expansions and holomorphic partial derivatives. The one-variable results used below are proved in the [contour foundation](complex-contours-U070.md): contour integrals and the triangle theorem (§16.1), Cauchy's formula on discs, Taylor coefficients and the identity theorem (§16.2), holomorphic integrals depending on a parameter (§16.3), Cauchy's theorem (§16.5) and the maximum principle (§16.6). [Polynomial roots](polynomial-roots-U070.md), §9, gives the factorization of a complex polynomial into linear factors with multiplicities.

A germ \(g\in\mathcal O_n\) is **regular of order \(s\) in \(w\)** if \(g(0,w)=w^sv(w)\) with \(v(0)\neq0\); for \(s=0\) this means \(g(0)\neq0\). A **Weierstrass polynomial of degree \(s\)** is a polynomial
\(P=w^s+a_1(z')w^{s-1}+\cdots+a_s(z')\) with \(a_k\in\mathcal O_{n-1}\) and \(a_k(0)=0\).

## The statements

**Theorem 1 (preparation).** If \(g\) is regular of order \(s\) in \(w\), then \(g=uP\) for a unit \(u\in\mathcal O_n\) and a Weierstrass polynomial \(P\) of degree \(s\). Both factors are unique.

**Theorem 2 (division with constants independent of the dividend).** Let \(D'\subset\mathbb C^{n-1}\) be open, \(s\geq1\), and \(P(z',w)=w^s+\sum_{k=1}^sa_k(z')w^{s-k}\) with \(a_k\) holomorphic on \(D'\). Let \(0\leq\alpha<\rho\), and suppose that for every \(z'\in D'\) all roots of \(P(z',\cdot)\) have modulus at most \(\alpha\). Then every holomorphic \(f\) on \(D'\times\Delta_\rho\) has exactly one expression

\[
f=qP+R,\qquad q\in\mathcal O(D'\times\Delta_\rho),\qquad R=\sum_{j=0}^{s-1}c_j(z')w^j,\quad c_j\in\mathcal O(D').
\]

If \(|f|\leq M\) on \(D'\times\Delta_\rho\), then \(|R|\leq C_1M\) and \(|q|\leq C_2M\) there, where

\[
C_1=\frac{s\rho(\rho+\alpha)^{s-1}}{(\rho-\alpha)^s},\qquad C_2=\frac{1+C_1}{(\rho-\alpha)^s}.
\tag{6}
\]

**Corollary 3 (division by a regular germ).** If \(g\) is regular of order \(s\) in \(w\), every \(f\in\mathcal O_n\) has exactly one expression \(f=qg+R\) with \(q\in\mathcal O_n\) and \(R\in\mathcal O_{n-1}[w]\) of degree less than \(s\). Hence \(\mathcal O_n/(g)\) is a free \(\mathcal O_{n-1}\)-module with basis the classes of \(1,w,\ldots,w^{s-1}\).

**Proposition 4 (adapted coordinates).** For finitely many nonzero germs there is a linear change of coordinates after which each of them is regular in \(w\), of order equal to its order at zero.

**Proposition 5 (size of the coefficients).** If \(g\) is regular in \(w\) of order \(s\) and \(s\) is also the order of \(g\) at zero, the coefficients of its Weierstrass polynomial satisfy \(|a_k(z')|\leq\binom skC^k|z'|^k\) near zero, for some constant \(C\). Here \(|z'|=\max_k|z_k|\).

**Theorem 6.** The ring \(\mathcal O_n\) is Noetherian.

## Three tools

**Lemma A (integrals over a fixed circle).** Let \(U\subset\mathbb C^m\) be open and \(\sigma>0\). Let \(\varphi\) be continuous on \(U\times\{|\zeta|=\sigma\}\) and holomorphic in \(x\in U\) for each fixed \(\zeta\). Then \(\Phi(x)=\int_{|\zeta|=\sigma}\varphi(x,\zeta)\,d\zeta\) is holomorphic on \(U\).

**Proof.** For a compact neighbourhood \(K\) of a point of \(U\), the integrand is uniformly continuous and bounded on \(K\times\{|\zeta|=\sigma\}\); hence \(\Phi\) is continuous. Fix all variables but one. The integrand is holomorphic in the remaining variable and bounded on compact sets, so §16.3 of the contour foundation, with the circle and its arc-length measure, shows that \(\Phi\) is holomorphic in that variable. Thus \(\Phi\) is continuous and holomorphic in each variable separately. \(\square\)

**Lemma B (zeros inside a circle).** Let \(h\) be holomorphic on \(\Delta_\tau\), \(0<\sigma<\tau\), and \(h(\zeta)\neq0\) for \(|\zeta|=\sigma\). Then \(h\) has finitely many zeros in \(\Delta_\sigma\). List them as \(b_1,\ldots,b_N\), each repeated according to its multiplicity. For every integer \(j\geq0\),

\[
\frac1{2\pi i}\int_{|\zeta|=\sigma}\zeta^j\,\frac{h'(\zeta)}{h(\zeta)}\,d\zeta=b_1^j+\cdots+b_N^j,
\tag{1}
\]

with \(b^0=1\), so that the case \(j=0\) gives \(N\).

**Proof.** The function \(h\) is not identically zero on the connected disc \(\Delta_\tau\), so its zeros are isolated by the identity theorem. The compact disc \(\{|\zeta|\leq\sigma\}\) therefore contains only finitely many of them, all in the open disc. If \(c\) is a zero of multiplicity \(m\), Taylor expansion at \(c\) gives \(h(\zeta)=(\zeta-c)^mh_c(\zeta)\), with \(h_c\) holomorphic on \(\Delta_\tau\) and \(h_c(c)\neq0\). Removing the distinct zeros \(c_1,\ldots,c_p\) in \(\Delta_\sigma\) one after another gives

\[
h(\zeta)=\prod_{i=1}^p(\zeta-c_i)^{m_i}\,k(\zeta),
\]

where \(k\) is holomorphic on \(\Delta_\tau\) and has no zero with \(|\zeta|\leq\sigma\). By compactness and continuity, \(k\) has no zero on some larger disc \(\Delta_{\sigma'}\), \(\sigma<\sigma'<\tau\). There, away from the \(c_i\),

\[
\zeta^j\frac{h'(\zeta)}{h(\zeta)}=\sum_{i=1}^pm_i\frac{\zeta^j}{\zeta-c_i}+\zeta^j\frac{k'(\zeta)}{k(\zeta)} .
\]

The last term is holomorphic on the convex set \(\Delta_{\sigma'}\), so its integral over the circle is zero by Cauchy's theorem. Cauchy's formula for the polynomial \(\zeta^j\) gives \(\frac1{2\pi i}\int_{|\zeta|=\sigma}\zeta^j(\zeta-c_i)^{-1}\,d\zeta=c_i^j\). Summing gives \(\sum_im_ic_i^j\), which is the right side of (1). \(\square\)

**Lemma C (coefficients from power sums).** Let \(b_1,\ldots,b_N\in\mathbb C\), repetitions allowed, \(S_j=\sum_lb_l^j\) for \(j\geq1\), and
\(\prod_{l=1}^N(w-b_l)=w^N+A_1w^{N-1}+\cdots+A_N\). With \(A_0=1\),

\[
kA_k=-\bigl(S_1A_{k-1}+S_2A_{k-2}+\cdots+S_kA_0\bigr),\qquad1\leq k\leq N.
\tag{C}
\]

Thus every \(A_k\) is a polynomial with rational coefficients in \(S_1,\ldots,S_k\); no ordering or labelling of the \(b_l\) enters.

**Proof.** Put \(Q(w)=\prod_l(w-b_l)\) and \(\beta=\max_l|b_l|\). For \(|w|>\beta\) (any \(w\neq0\) if \(\beta=0\)), expanding each \(1/(w-b_l)\) as a geometric series gives the absolutely convergent expansion

\[
\frac{Q'(w)}{Q(w)}=\sum_{l=1}^N\frac1{w-b_l}=\sum_{j\geq0}S_jw^{-j-1},\qquad S_0=N .
\]

Multiply by \(Q(w)\), substitute \(w=1/t\) and multiply by \(t^{N-1}\). For \(0<|t|<1/\beta\) this gives

\[
\sum_{k=0}^{N-1}(N-k)A_kt^k=\sum_{i=0}^N\sum_{j\geq0}A_iS_j\,t^{i+j}.
\]

Both sides are power series in \(t\) converging for \(|t|<1/\beta\) (for all \(t\) if \(\beta=0\)), and they agree off \(t=0\), hence also at \(t=0\) by continuity. Their coefficients therefore agree by the uniqueness of Taylor coefficients (§16.2 of the contour foundation). The coefficient of \(t^k\) on the right is \(NA_k+\sum_{j=1}^kS_jA_{k-j}\). On the left it is \((N-k)A_k\) for \(k<N\) and \(0\) for \(k=N\). Comparing the two gives (C). \(\square\)

## Preparation by the zeros in one fibre

**Proof of Theorem 1.** If \(s=0\), then \(g(0)\neq0\). The reciprocal \(1/g\) is holomorphic near zero, so \(g\) is a unit and \(g=g\cdot1\). Assume \(s\geq1\).

*Choice of a circle.* Let \(g\) be holomorphic on \(\Delta'_{\delta_0}\times\Delta_{\rho_0}\). Since \(g(0,w)=w^sv(w)\) with \(v(0)\neq0\), there is \(\sigma\in(0,\rho_0)\) with \(g(0,w)\neq0\) for \(0<|w|\leq\sigma\). Put \(\mu=\min_{|\zeta|=\sigma}|g(0,\zeta)|>0\). The function \(g\) is uniformly continuous on the compact set \(\{|z_k|\leq\delta_0/2\}\times\{|\zeta|=\sigma\}\). Hence some \(\delta\in(0,\delta_0/2]\) gives \(|g(z',\zeta)-g(0,\zeta)|<\mu\), and so \(g(z',\zeta)\neq0\), whenever \(z'\in\Delta'_\delta\) and \(|\zeta|=\sigma\).

*Power sums of the zeros.* For \(z'\in\Delta'_\delta\) and \(j\geq0\) define

\[
S_j(z')=\frac1{2\pi i}\int_{|\zeta|=\sigma}\zeta^j\,\frac{\partial_wg(z',\zeta)}{g(z',\zeta)}\,d\zeta .
\tag{2}
\]

The derivative \(\partial_wg\) is holomorphic, so the integrand is continuous on \(\Delta'_\delta\times\{|\zeta|=\sigma\}\) and holomorphic in \(z'\). By Lemma A, each \(S_j\) is holomorphic on \(\Delta'_\delta\). By Lemma B applied to \(g(z',\cdot)\) on \(\Delta_{\rho_0}\), \(S_0(z')\) is the number of zeros of \(g(z',\cdot)\) in \(\Delta_\sigma\), counted with multiplicity, and \(S_j(z')\) is the sum of their \(j\)-th powers. A continuous integer-valued function on the connected polydisc \(\Delta'_\delta\) is constant. At \(z'=0\) the only zero in \(\Delta_\sigma\) is \(w=0\), of multiplicity \(s\). Hence every fibre \(g(z',\cdot)\) has exactly \(s\) zeros in \(\Delta_\sigma\), counted with multiplicity; list them as \(b_1(z'),\ldots,b_s(z')\). We do not claim, and do not need, that individual zeros depend holomorphically on \(z'\). For \(w^2-z_1\), no holomorphic choice of a square root of \(z_1\) exists near \(z_1=0\).

*The polynomial.* Put \(a_0=1\) and \(a_k=-(S_1a_{k-1}+\cdots+S_ka_0)/k\) for \(1\leq k\leq s\). These functions are holomorphic on \(\Delta'_\delta\). By Lemma C, for every \(z'\in\Delta'_\delta\),

\[
P(z',w)=w^s+a_1(z')w^{s-1}+\cdots+a_s(z')=\prod_{l=1}^s\bigl(w-b_l(z')\bigr).
\tag{3}
\]

At \(z'=0\) all \(b_l\) vanish, so \(P(0,w)=w^s\) and \(a_k(0)=0\). Thus \(P\) is a Weierstrass polynomial of degree \(s\).

*The unit.* Fix \(z'\in\Delta'_\delta\). Off the points \(b_l(z')\), the quotient \(g(z',w)/P(z',w)\) is holomorphic on \(\Delta_{\rho_0}\). If a value \(b\) occurs exactly \(m\) times among the \(b_l(z')\), then both \(g(z',\cdot)\) and \(P(z',\cdot)\) vanish at \(b\) to order exactly \(m\). Write \(g(z',w)=(w-b)^mg_b(w)\) and \(P(z',w)=(w-b)^mP_b(w)\) with \(g_b(b)\neq0\neq P_b(b)\). The quotient then extends across \(b\) with the nonzero value \(g_b(b)/P_b(b)\). Call the extended function \(E_{z'}\). It is holomorphic on \(\Delta_{\rho_0}\) and has no zero in \(\Delta_\sigma\), because every zero of \(g(z',\cdot)\) there is one of the \(b_l(z')\). All roots of \(P(z',\cdot)\) lie in \(\Delta_\sigma\), so \(P(z',\zeta)\neq0\) for \(|\zeta|=\sigma\). Cauchy's formula gives, for \(|w|<\sigma\),

\[
E_{z'}(w)=\frac1{2\pi i}\int_{|\zeta|=\sigma}\frac{g(z',\zeta)}{P(z',\zeta)(\zeta-w)}\,d\zeta .
\]

The integrand is continuous on \(\Delta'_\delta\times\Delta_\sigma\times\{|\zeta|=\sigma\}\) and holomorphic in \((z',w)\). By Lemma A, \(u(z',w)=E_{z'}(w)\) is holomorphic on \(V=\Delta'_\delta\times\Delta_\sigma\). It has no zero there, so \(1/u\) is holomorphic as well. The functions \(g\) and \(uP\) are continuous on \(V\) and agree off the finitely many points \(b_l(z')\) of each fibre, so they agree on \(V\). Hence \(g=uP\) with \(u(0)\neq0\).

*Uniqueness.* First a bound for roots: if \(\tau>0\) and \(\sum_{k=1}^s|c_k|\tau^{-k}<1\), then every root of \(w^s+c_1w^{s-1}+\cdots+c_s\) lies in \(\Delta_\tau\). Indeed, for \(|w|\geq\tau\) the lower terms have modulus at most \(|w|^s\sum_k|c_k||w|^{-k}\leq|w|^s\sum_k|c_k|\tau^{-k}<|w|^s\).

Now suppose \(g=u_1P_1\) as germs, with \(u_1\) a unit and \(P_1=w^{s_1}+c_1(z')w^{s_1-1}+\cdots+c_{s_1}(z')\) a Weierstrass polynomial. At \(z'=0\) this reads \(g(0,w)=u_1(0,w)w^{s_1}\), so \(s_1=s\). Choose \(\tau_1\in(0,\sigma]\) and \(\delta_1\in(0,\delta]\) such that on \(\Delta'_{\delta_1}\times\Delta_{\tau_1}\) the identity \(g=u_1P_1\) holds with \(u_1\) holomorphic and without zeros. Then choose \(\tau\in(0,\tau_1)\) and shrink \(\delta_1\) so that \(\sum_k|a_k(z')|\tau^{-k}<1\) and \(\sum_k|c_k(z')|\tau^{-k}<1\) for \(z'\in\Delta'_{\delta_1}\). This is possible because \(a_k(0)=c_k(0)=0\) and the coefficients are continuous. For such \(z'\), the zeros of \(g(z',\cdot)\) in \(\Delta_{\tau_1}\), with multiplicities, are the roots of \(P_1(z',\cdot)\), and these lie in \(\Delta_\tau\). The zeros of \(g(z',\cdot)\) in \(\Delta_\sigma\) are the roots of \(P(z',\cdot)\), and they also lie in \(\Delta_\tau\). Two monic polynomials of degree \(s\) with the same roots and multiplicities are equal, by the factorization of complex polynomials into linear factors. Hence \(P_1=P\). Then \(u_1=g/P=u\) wherever \(P\neq0\), and by continuity everywhere on the common domain. \(\square\)

**Proof of Proposition 4.** Let \(g\neq0\) have order \(m\), so that its Taylor series is \(\sum_{d\geq m}g_d\) with homogeneous parts \(g_d\) of degree \(d\) and \(g_m\neq0\). If \(v\in\mathbb C^n\) satisfies \(g_m(v)\neq0\), choose an invertible linear map \(A\) with \(Ae_n=v\) and put \(\tilde g(z)=g(Az)\). For small \(w\), \(\tilde g(0,w)=g(wv)=\sum_{d\geq m}g_d(v)w^d=g_m(v)w^m+O(w^{m+1})\), so \(\tilde g\) is regular of order \(m\) in \(w\). For finitely many nonzero germs \(g^{(1)},\ldots,g^{(p)}\) with lowest homogeneous parts \(g^{(i)}_{m_i}\), the product \(\prod_ig^{(i)}_{m_i}\) is a nonzero polynomial, since the polynomial ring is an integral domain. A nonzero polynomial does not vanish on all of \(\mathbb C^n\): by induction on \(n\), fix the first \(n-1\) variables so that some coefficient of the highest power of the last variable is nonzero, and use that a nonzero polynomial in one variable has finitely many roots. One vector \(v\) with \(\prod_ig^{(i)}_{m_i}(v)\neq0\) serves for all of them. \(\square\)

**Proof of Proposition 5.** Write the lowest homogeneous part as \(g_s(z',w)=cw^s+\sum_{k=0}^{s-1}h_k(z')w^k\), where \(c=g_s(0,1)\neq0\) and \(h_k\) is homogeneous of degree \(s-k\). Choose \(H\) with \(|h_k(z')|\leq H|z'|^{s-k}\) for all \(k\). The terms of order at least \(s+1\) satisfy \(|g(z)-g_s(z)|\leq K|z|^{s+1}\) for \(|z|=\max(|z'|,|w|)\leq\eta\), with suitable \(K,\eta>0\). Indeed, if \(\sum_\beta|c_\beta|\eta^{|\beta|}<\infty\) for the Taylor coefficients \(c_\beta\) of \(g\), then \(\sum_{|\beta|\geq s+1}|c_\beta||z^\beta|\leq|z|^{s+1}\eta^{-s-1}\sum_\beta|c_\beta|\eta^{|\beta|}\) for \(|z|\leq\eta\).

Choose \(C\geq1\) with \(H\sum_{k=0}^{s-1}C^{-(s-k)}\leq|c|/4\). Let \(0<|w|\leq\min(\eta,|c|/(4K))\) and \(|w|\geq C|z'|\). Then \(|z|=|w|\), and

\[
|g(z',w)|\geq|c||w|^s-\sum_kH|z'|^{s-k}|w|^k-K|w|^{s+1}\geq|c||w|^s-\tfrac{|c|}4|w|^s-\tfrac{|c|}4|w|^s>0 .
\]

So in that neighbourhood every zero of \(g\) other than the origin satisfies \(|w|<C|z'|\), and the origin satisfies \(|w|\leq C|z'|\). Shrink the base polydisc of the proof of Theorem 1, using the bound for roots, so that for every \(z'\) in it the points \((z',b_l(z'))\) lie in that neighbourhood. They are zeros of \(g\), so \(|b_l(z')|\leq C|z'|\). Since \(a_k\) is, up to sign, the \(k\)-th elementary symmetric function of the \(b_l(z')\), \(|a_k(z')|\leq\binom skC^k|z'|^k\). \(\square\)

## Division, finite generation and elementary algebra

**Proof of Theorem 2.** *The divided difference.* For complex numbers \(b_1,\ldots,b_s\), \(\zeta\) and \(w\), telescoping through the products in which the first \(\ell\) factors use \(w\) and the others use \(\zeta\) gives

\[
\prod_{i=1}^s(\zeta-b_i)-\prod_{i=1}^s(w-b_i)
=(\zeta-w)\sum_{\ell=1}^s\ \prod_{i<\ell}(w-b_i)\prod_{i>\ell}(\zeta-b_i).
\tag{5}
\]

Apply this to the roots of \(P(z',\cdot)\). The divided difference \(K(z';\zeta,w)=\bigl(P(z',\zeta)-P(z',w)\bigr)/(\zeta-w)\) is the polynomial

\[
K(z';\zeta,w)=\sum_{j=0}^{s-1}w^jK_j(z',\zeta),\qquad K_j(z',\zeta)=\sum_{k=0}^{s-1-j}a_k(z')\zeta^{s-1-j-k},
\]

where \(a_0=1\). This follows from \(\zeta^d-w^d=(\zeta-w)\sum_{i+j=d-1}\zeta^iw^j\). By (5), \(|K(z';\zeta,w)|\leq s(\sigma+\alpha)^{s-1}\) when \(|\zeta|=\sigma\) and \(|w|\leq\sigma\).

*Existence on a smaller disc.* Fix \(\sigma\) with \(\alpha<\sigma<\rho\). For \(|\zeta|=\sigma\) every factor of \(P(z',\zeta)=\prod_l(\zeta-b_l(z'))\) has modulus at least \(\sigma-\alpha\), so \(|P(z',\zeta)|\geq(\sigma-\alpha)^s>0\). For \(z'\in D'\) and \(|w|<\sigma\), define

\[
\begin{aligned}
q_\sigma(z',w)&=\frac1{2\pi i}\int_{|\zeta|=\sigma}\frac{f(z',\zeta)}{P(z',\zeta)(\zeta-w)}\,d\zeta,\\
R_\sigma(z',w)&=\sum_{j=0}^{s-1}w^j\,\frac1{2\pi i}\int_{|\zeta|=\sigma}\frac{f(z',\zeta)K_j(z',\zeta)}{P(z',\zeta)}\,d\zeta .
\end{aligned}
\tag{4}
\]

Lemma A shows that \(q_\sigma\) is holomorphic on \(D'\times\Delta_\sigma\) and that the coefficients of \(R_\sigma\) are holomorphic on \(D'\). Cauchy's formula for \(f(z',\cdot)\) on the circle, together with

\[
\frac1{\zeta-w}=\frac{P(z',w)}{P(z',\zeta)(\zeta-w)}+\frac{K(z';\zeta,w)}{P(z',\zeta)},
\]

gives \(f=q_\sigma P+R_\sigma\) on \(D'\times\Delta_\sigma\).

*Uniqueness.* Let \(\alpha<\tau\leq\rho\), and suppose \(qP+R=0\) on \(D'\times\Delta_\tau\), with \(q\) holomorphic and \(R\) a polynomial in \(w\) of degree less than \(s\) with holomorphic coefficients. Fix \(z'\). A root \(b\) of multiplicity \(m\) of \(P(z',\cdot)\) lies in \(\Delta_\tau\), and \(R(z',w)=-q(z',w)P(z',w)\) vanishes at \(b\) to order at least \(m\). The polynomial \(R(z',\cdot)\) thus has at least \(s\) zeros counted with multiplicity. A nonzero polynomial of degree less than \(s\) has at most \(s-1\), so \(R(z',\cdot)=0\). Then \(q(z',\cdot)P(z',\cdot)=0\). Since \(P(z',\cdot)\) has only finitely many zeros, continuity gives \(q(z',\cdot)=0\).

*The whole domain.* For \(\alpha<\sigma_1<\sigma_2<\rho\), uniqueness on \(D'\times\Delta_{\sigma_1}\) shows that \(q_{\sigma_2}\) and \(R_{\sigma_2}\) restrict to \(q_{\sigma_1}\) and \(R_{\sigma_1}\). The functions therefore define \(q\) and \(R\) on all of \(D'\times\Delta_\rho\) with \(f=qP+R\). This representation is unique by the uniqueness step with \(\tau=\rho\).

*Estimates.* Let \(|f|\leq M\). For \(|w|<\sigma\), the bounds on \(K\) and \(1/P\) and the length \(2\pi\sigma\) of the circle give

\[
|R(z',w)|\leq\frac{s\sigma(\sigma+\alpha)^{s-1}}{(\sigma-\alpha)^s}\,M .
\]

The function \(R\) does not depend on \(\sigma\); letting \(\sigma\to\rho\) gives \(|R|\leq C_1M\) on \(D'\times\Delta_\rho\). On the circle \(|w|=\sigma\) we have \(|q|=|f-R|/|P|\leq(1+C_1)M/(\sigma-\alpha)^s\). The maximum modulus principle for \(q(z',\cdot)\) on the closed disc \(|w|\leq\sigma\) extends this bound to the disc. Letting \(\sigma\to\rho\) gives \(|q|\leq C_2M\). \(\square\)

The constants (6) depend only on the degree \(s\) and the radii \(\alpha\) and \(\rho\). In particular, one fixed polydisc serves for the division of every bounded holomorphic function.

**Proof of Corollary 3.** If \(s=0\), then \(g\) is a unit and \(f=(f/g)g\); a remainder of negative degree is zero. Let \(s\geq1\). By the proof of Theorem 1, \(g=uP\) on a product \(\Delta'_\delta\times\Delta_\sigma\), with \(u\) zero-free. Given \(f\), choose \(\tau\in(0,\sigma]\) and \(\delta'\in(0,\delta]\) such that \(f\) is holomorphic on \(\Delta'_{\delta'}\times\Delta_\tau\). Then choose \(\alpha\in(0,\tau)\) and \(\delta''\in(0,\delta']\) with \(\sum_k|a_k(z')|\alpha^{-k}<1\) on \(\Delta'_{\delta''}\). By the bound for roots, all roots of \(P(z',\cdot)\) then lie in \(\Delta_\alpha\). Theorem 2 on \(\Delta'_{\delta''}\times\Delta_\tau\) gives \(f=qP+R=(q/u)g+R\).

If \(q_1g+R_1=q_2g+R_2\) as germs, then \((q_1-q_2)uP+(R_1-R_2)=0\) on a product neighbourhood. By the bound for roots, that neighbourhood contains a product \(\Delta'_{\delta_2}\times\Delta_{\tau_2}\) on which all roots of \(P(z',\cdot)\) have modulus at most some \(\alpha_2<\tau_2\). The uniqueness step of Theorem 2 gives \(R_1=R_2\) and \((q_1-q_2)u=0\), so \(q_1=q_2\).

By uniqueness, the remainder map \(f\mapsto R\) is \(\mathcal O_{n-1}\)-linear. Its kernel is \((g)\). It restricts to the identity on polynomials of degree less than \(s\). Hence the classes of \(1,w,\ldots,w^{s-1}\) generate \(\mathcal O_n/(g)\). They are independent: if \(\sum_jc_jw^j=qg\), uniqueness of the remainder of this polynomial forces every \(c_j=0\). \(\square\)

**Proof of Theorem 6.** We use the following module fact. If a commutative ring \(A\) is Noetherian, every submodule \(N\subset A^s\) is finitely generated. For \(s=1\) this is the definition. For \(s>1\), the last coordinates of the elements of \(N\) form an ideal of \(A\). Choose finitely many elements of \(N\) whose last coordinates generate it. Every element of \(N\) differs from an \(A\)-combination of these by an element of \(N\cap(A^{s-1}\times0)\), which is finitely generated by induction.

Now induct on \(n\). The ring \(\mathcal O_0=\mathbb C\) is a field. Let \(n\geq1\) and \(J\subset\mathcal O_n\) a nonzero ideal. A linear change of coordinates is a ring automorphism of \(\mathcal O_n\). By Proposition 4 we may therefore assume that some \(f\in J\) is regular of order \(s\) in \(w\). If \(s=0\), then \(f\) is a unit and \(J=\mathcal O_n\). Otherwise Corollary 3 writes each \(h\in J\) as \(h=qf+R_h\), where \(R_h=h-qf\in J\) lies in the free module \(\bigoplus_{j<s}\mathcal O_{n-1}w^j\). The remainders \(R_h\), \(h\in J\), form an \(\mathcal O_{n-1}\)-submodule of this free module. By the induction hypothesis and the module fact, they are generated by finitely many \(R_1,\ldots,R_p\in J\). Then \(J\) is generated by \(f,R_1,\ldots,R_p\). \(\square\)

## Exercises and complete solutions

### 1. Multiplicity in division

*Difficulty: Introductory.*

For \(P(w)=w^3\), divide \(f(w)=e^w\). Explain why checking distinct zeros alone does not prove uniqueness.

**Solution.** The remainder is \(R=1+w+w^2/2\) and
\(q=(e^w-1-w-w^2/2)/w^3\), extended holomorphically at zero with value \(1/6\). A polynomial such as \(w\) vanishes at the only distinct zero, but is not divisible holomorphically by \(w^3\). Uniqueness requires the three zeros counted with multiplicity, or equality of the first three Taylor coefficients.

### 2. A prepared exponential

*Difficulty: Introductory.*

On \(\mathbb C^2\) with coordinates \((z,w)\), let \(g=e^w-1-z\). Show that \(g\) is regular of order one in \(w\), and find its Weierstrass polynomial and unit.

**Solution.** \(g(0,w)=e^w-1=w(1+w/2+\cdots)\), so the order is one. For \(|z|<1\) let \(L(z)=\log(1+z)\) be the principal logarithm, so \(L(0)=0\) and \(e^{L(z)}=1+z\). Let \(E(t)=(e^t-1)/t\) for \(t\neq0\) and \(E(0)=1\); this is an entire function. Then

\[
e^w-1-z=e^{L}\bigl(e^{w-L}-1\bigr)=(1+z)\,E\bigl(w-L(z)\bigr)\,\bigl(w-L(z)\bigr).
\]

Thus \(P=w-L(z)\), with coefficient \(-L(z)\) vanishing at \(z=0\), and \(u=(1+z)E(w-L(z))\), with \(u(0,0)=1\). Uniqueness in Theorem 1 shows these are the factors that its proof constructs.

### 3. Coefficients without holomorphic roots

*Difficulty: Intermediate.*

(a) Let \(g=w^2-z^3\). Find its Weierstrass polynomial, show that no holomorphic function \(b(z)\) near \(0\) satisfies \(b(z)^2=z^3\), and check Proposition 5. (b) Let \(g=w^2-z\). Show that \(g\) is regular of order two in \(w\), but that the coefficient estimate of Proposition 5 fails. Which hypothesis is missing?

**Solution.** (a) \(g\) is already a Weierstrass polynomial of degree two, so \(P=g\) and \(u=1\). If \(b\) were holomorphic with \(b^2=z^3\), the order of vanishing of \(b^2\) at \(0\) would be even, while \(z^3\) vanishes to order three. The coefficients are \(a_1=0\) and \(a_2=-z^3\), so \(|a_2|\leq|z|^2\) for \(|z|\leq1\), as Proposition 5 predicts: the order of \(g\) at zero is \(2\), equal to its order in \(w\). Power sums give the same coefficients: \(S_1=b_1+b_2=0\) and \(S_2=b_1^2+b_2^2=2z^3\), so (C) gives \(a_1=-S_1=0\) and \(a_2=-(S_1a_1+S_2)/2=-z^3\).

(b) \(g(0,w)=w^2\), so \(g\) is regular of order two in \(w\), and \(P=g\). Here \(a_2=-z\), which is not bounded by a constant times \(|z|^2\) near \(0\). The order of \(g\) at zero is one, because of the linear term \(-z\), so the hypothesis that the order in \(w\) equals the order at zero fails. The roots \(\pm z^{1/2}\) satisfy \(|b|=|z|^{1/2}\), which is not bounded by a constant times \(|z|\).

### 4. Explicit division constants

*Difficulty: Introductory.*

Let \(P=w^2-z\) on \(D'=\{|z|<1/4\}\). Take \(\alpha=1/2\) and \(\rho=1\). Verify the hypothesis of Theorem 2, divide \(f=w^3\), and compare with (6).

**Solution.** The roots \(\pm z^{1/2}\) have modulus \(|z|^{1/2}<1/2\). Since \(w^3=w(w^2-z)+zw\), we get \(q=w\) and \(R=zw\); by uniqueness these are the quotient and remainder of Theorem 2. On \(D'\times\Delta_1\) we have \(|f|\leq M=1\), \(|R|\leq1/4\) and \(|q|\leq1\). Formula (6) gives \(C_1=2\cdot1\cdot(3/2)/(1/2)^2=12\) and \(C_2=13/(1/2)^2=52\). The bounds hold with room to spare: the constants are uniform in \(f\), not sharp.

## An algebraic proof of the coefficient recursion

*This proof was written by GPT-6 Astra (OpenAI), Ultra, October 2026, for this course. It gives (C) again, in the notation \(A_j=(-1)^je_j\) of (N6), without power series in \(1/w\).*

### A finite identity that does not distinguish repeated roots

For any list \(\lambda_1,\ldots,\lambda_k\in\mathbb C\), repetitions allowed, define

\[
S_\ell=\sum_{i=1}^k\lambda_i^\ell\quad(\ell\ge1),\qquad
e_0=1,\qquad
e_j=\sum_{1\le i_1<\cdots<i_j\le k}
\lambda_{i_1}\cdots\lambda_{i_j}\quad(1\le j\le k).
\tag{N1}
\]

The indices in the definition of \(e_j\) select occurrences in the list, even when their values coincide. Set \(e_j=0\) for \(j>k\). The finite Newton identities are

\[
j e_j=\sum_{\ell=1}^j(-1)^{\ell-1}e_{j-\ell}S_\ell,
\qquad 1\le j\le k.
\tag{N2}
\]

**Proof.** Work first in the polynomial ring
\(R=\mathbb C[\lambda_1,\ldots,\lambda_k]\), treating the \(\lambda_i\) as indeterminates. Introduce a formal variable \(X\) and the finite polynomial

\[
E(X)=\prod_{i=1}^k(1+\lambda_iX)
     =\sum_{j=0}^k e_jX^j.
\tag{N3}
\]

Each factor has constant coefficient one, so it is invertible in \(R[[X]]\), with formal inverse
\(\sum_{m\ge0}(-\lambda_iX)^m\). Formal differentiation of the finite product gives

\[
\begin{aligned}
E'(X)
&=\sum_{i=1}^k\lambda_i\prod_{h\ne i}(1+\lambda_hX)\\
&=E(X)\sum_{i=1}^k\frac{\lambda_i}{1+\lambda_iX}\\
&=E(X)\sum_{\ell\ge1}(-1)^{\ell-1}S_\ell X^{\ell-1}.
\end{aligned}
\tag{N4}
\]

Equality of the coefficients of \(X^{j-1}\) is exactly (N2). There is no analytic convergence or division by a root. To make the argument entirely finite, truncate each geometric inverse after degree \(k-1\) and work modulo \(X^k\); its product with \(1+\lambda_iX\) is one modulo \(X^k\). This determines all the coefficients used in (N2). Finally specialize the indeterminates to the given complex numbers. Polynomial identities remain valid when values coincide or vanish. \(\square\)

Since division by the positive integer \(j\) is allowed in \(\mathbb C\), (N2) recursively expresses every \(e_j\), \(1\le j\le k\), as a polynomial with rational coefficients in \(S_1,\ldots,S_j\). For indices not exceeding \(k\),

\[
e_1=S_1,\qquad
e_2=\frac{S_1^2-S_2}{2},\qquad
e_3=\frac{S_1^3-3S_1S_2+2S_3}{6}.
\tag{N5}
\]

For the descending coefficients of

\[
P(w)=\prod_{i=1}^k(w-\lambda_i)
    =w^k+A_1w^{k-1}+\cdots+A_k,
\tag{N6}
\]

we have \(A_0=1\) and \(A_j=(-1)^je_j\). Thus the equivalent coefficient recursion is

\[
jA_j+\sum_{\ell=1}^j A_{j-\ell}S_\ell=0,
\qquad 1\le j\le k.
\tag{N7}
\]

For example, where the indices do not exceed \(k\), \(A_1=-S_1\), \(A_2=(S_1^2-S_2)/2\), and
\(A_3=(-S_1^3+3S_1S_2-2S_3)/6\). These signs correspond to the factors \(w-\lambda_i\).

## Further reading

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), version of 21 June 2012, Chapter II, §2.A, treats preparation and division by C. L. Siegel's contour method.
