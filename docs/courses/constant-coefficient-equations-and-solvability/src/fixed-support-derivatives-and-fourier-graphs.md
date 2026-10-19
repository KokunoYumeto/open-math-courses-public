# Fixed-support derivatives and logarithmic Fourier graphs

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A fixed cutoff costs only a fixed number of derivatives, even when the derivative being estimated has high order. We first make that fact quantitative. We then move a Fourier inverse through a logarithmic complex graph, deriving its exact boundary flux and the decay that removes it.

[Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html), Theorems 1.1–2.1 and Section 7, proves the Fourier results with the normalization used here. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html), Section 13.10, constructs smooth cutoffs. [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html), Theorem 2.1, proves the complex-linear flux formula.

Keep \(D_j=-i\partial_j\) and

\[
\begin{gathered}
\widehat v(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}v(x)\,dx,
\\
\qquad
\|v\|_{H^n}=(2\pi)^{-n/2}
\|\langle\xi\rangle^n\widehat v(\xi)\|_2,
\\
\qquad \langle\xi\rangle=(1+|\xi|^2)^{1/2}.
\end{gathered}
\tag{1}
\]

Dimension zero uses its one-point Lebesgue measure of mass 1 and the identity Fourier transform.

Grubb’s notes and Melrose’s course develop the Fourier and Sobolev background. The fixed-cutoff estimate and the complete graph deformation are proved below with the Fourier normalization displayed here.

## A fixed cutoff and high derivatives

**Lemma 1.1 (an explicit integer Sobolev bound).** For \(n\ge1\), put

\[
\begin{gathered}
A_n^2=2^n+\frac{2^{2n}}{1-2^{-n}}.
\\
\qquad
\|v\|_\infty\le (2\pi)^{-n/2}A_n\|v\|_{H^n}.
\end{gathered}
\tag{2}
\]

The inequality holds for compact smooth \(v\), and by the full completed Fourier theorem for every \(H^n\) element, with its continuous representative.

**Proof.** On \(|\xi|\le1\), the integral of \(\langle\xi\rangle^{-2n}\) is at most the volume \(2^n\) of the enclosing cube. On the shell \(2^j<|\xi|\le2^{j+1}\), \(j\ge0\), this integrand is at most \(2^{-2nj}\), whereas the enclosing cube has volume \(2^{n(j+2)}\). Summing the geometric series gives

\[
\begin{gathered}
\int_{\mathbb R^n}\langle\xi\rangle^{-2n}\,d\xi
\\
\le 2^n+2^{2n}\sum_{j=0}^{\infty}2^{-nj}=A_n^2.
\end{gathered}
\tag{3}
\]

Cauchy–Schwarz therefore gives \(\|\widehat v\|_1\le A_n\|\langle\xi\rangle^n\widehat v\|_2\). The exact Fourier inverse integral, with coefficient \((2\pi)^{-n}\), proves (2). For a general \(H^n\) element the same weighted \(L^2\) argument makes its Fourier transform an \(L^1\) function; the completed-space result in [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) Section 7 inverse and ordinary-integral agreement identify it with the displayed inverse integral. Dominated convergence makes that integral continuous and proves the bound. No pointwise inversion is assumed for a general \(L^2\) element. \(\square\)

**Corollary 1.2 (the constant is independent of the high derivative).** Let \(K\subset U\subset\mathbb R^n\), with \(K\) compact and \(U\) open, and choose one \(\chi\in C_c^\infty(U)\) equal to 1 near \(K\). There is a constant \(C_\chi\) such that for every smooth \(u\) on \(U\) and every multi-index \(\gamma\),

\[
\begin{gathered}
\sup_K|D^\gamma u|
\\
\le C_\chi\sum_{|\alpha|\\
\le n}
\|D^{\gamma+\alpha}u\|_{L^2(\operatorname{supp}\chi)}.
\end{gathered}
\tag{4}
\]

In particular \(C_\chi\) does not depend on \(\gamma\).

**Proof.** The actual cutoff construction provides a smooth plateau in each ball of a finite cover of \(K\) by balls compactly contained in \(U\). Choose their smaller balls to cover \(K\), and set \(\chi=1-\prod_j(1-\chi_j)\). It has compact support in the union of the larger balls and is 1 on a neighborhood of \(K\).

The multinomial theorem and Plancherel give the exact integer norm identity

\[
\|v\|_{H^n}^2
=\sum_{|\beta|\le n}
\frac{n!}{(n-|\beta|)!\,\beta!}\,\|D^\beta v\|_2^2.
\tag{5}
\]

Indeed the coefficients are exactly those of \((1+\xi_1^2+\cdots+\xi_n^2)^n\), including the constant term. Apply this to \(v=\chi D^\gamma u\). The product rule is

\[
D^\beta(\chi D^\gamma u)
=\sum_{\delta\le\beta}\binom{\beta}{\delta}
(D^\delta\chi)D^{\gamma+\beta-\delta}u.
\tag{6}
\]

Only derivatives of \(\chi\) up to order \(|\beta|\le n\) occur. Their finitely many supremum norms and the finitely many binomial coefficients depend on the fixed cutoff and dimension, independently of \(\gamma\). Each factor involving \(u\) is one of the terms on the right of (4). Thus (5) bounds \(\|\chi D^\gamma u\|_{H^n}\) by a fixed \(C_\chi'\) times that sum. Formula (2), and \(\chi=1\) near \(K\), give (4). Dimension zero is the one-point identity with \(\chi=1\), where \(U\) is nonempty; an empty \(K\) has a zero left side. \(\square\)

This is the precise estimate needed by the anisotropic-derivative lesson Theorem 1.1. It does not introduce factorial or binomial factors depending on the high order \(\gamma\). The real-analytic extension and polydisk estimate are Lemmas 3.1 and 1.1 of [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md).

## Decay of a compact test transform

**Lemma 2.1 (Fourier–Laplace bound).** If \(\phi\in C_c^\infty(\mathbb R^n)\) has support in a fixed compact \(K\), let \(R_K=\max(1,\sup_{x\in K}|x|)\), taking \(R_K=1\) for empty \(K\). Its Fourier–Laplace transform is entire, and for every nonnegative integer \(N\) there is \(C_{K,N}\) such that

\[
\begin{gathered}
|\widehat\phi(\zeta)|
\le C_{K,N}\|\phi\|_{C^N}
\langle\operatorname{Re}\zeta\rangle^{-N}
e^{R_K|\operatorname{Im}\zeta|}
\\
\quad(\zeta\in\mathbb C^n).
\end{gathered}
\tag{7}
\]

**Proof.** The integral defining the transform and each fixed complex derivative can be taken over one enclosing compact ball. Its integrand is entire in \(\zeta\), with bounded derivatives on every compact parameter set. Differentiation under the compact integral, or its uniformly convergent exponential series, proves that the transform is entire.

Write \(r=|\operatorname{Re}\zeta|\). For \(r\ge1\) set \(v=\operatorname{Re}\zeta/r\), a real unit vector. Integration by parts in that direction, with no boundary term because \(\phi\) is compactly supported, gives

\[
\widehat\phi(\zeta)
=(iv\cdot\zeta)^{-N}
\int e^{-ix\cdot\zeta}\partial_v^N\phi(x)\,dx.
\tag{8}
\]

The real part of \(v\cdot\zeta\) is \(r\), so \(|v\cdot\zeta|\ge r\). Also \(|e^{-ix\cdot\zeta}|\le e^{R_K|\operatorname{Im}\zeta|}\), and expanding the directional derivative gives \(\|\partial_v^N\phi\|_\infty\le n^{N/2}\|\phi\|_{C^N}\), where the norm includes every derivative of order at most \(N\). The enclosing ball has fixed finite volume, so these bounds prove (7) for \(r\ge1\), after comparing \(r\) and \(\langle r\rangle\). For \(r\le1\) use the zeroth-order integral bound and \(\langle r\rangle^{-N}\ge2^{-N/2}\). Dimension zero is evaluation at the point and the estimate with constant 1. A zero test and an empty support cause no exception. \(\square\)

## The graph flux identity

Fix \(n\ge1\), a real vector \(\nu\), and a real smooth scalar \(\tau\). Define

\[
\begin{gathered}
Z_s(\xi)=\xi+is\tau(\xi)\nu,\\
\qquad
J_s(\xi)=\det D_\xi Z_s
=1+is\,\nu\cdot\nabla\tau(\xi),\\
\qquad 0\le s\le1.
\end{gathered}
\tag{9}
\]

**Lemma 3.1 (finite-ball graph deformation).** If \(F\) is holomorphic on a neighborhood of the image of \([0,1]\times\overline{B_R}\) under \(Z_s\), then

\[
\begin{gathered}
\int_{B_R}F(Z_1(\xi))J_1(\xi)\,d\xi
\\
-\int_{B_R}F(\xi)\,d\xi
\quad=
\\
\int_0^1\int_{|\xi|=R}
i\tau(\xi)F(Z_s(\xi))\,\nu\cdot n_R(\xi)\,dS(\xi)\,ds,
\end{gathered}
\tag{10}
\]

where \(n_R=\xi/R\) is the outward real normal. All products are complex-linear, without conjugation.

**Proof.** The matrix is \(I+is\nu\otimes\nabla\tau\). Expand its determinant by multilinearity in the columns. Terms with two replaced columns are zero because those columns are parallel to \(\nu\); the linear terms sum to \(is\nu\cdot\nabla\tau\). This proves (9), including its sign.

Put \(G_s=F(Z_s)\). The holomorphic chain rule gives

\[
\partial_s(G_sJ_s)
=\operatorname{div}_\xi\big(i\tau(\xi)\nu G_s(\xi)\big).
\tag{11}
\]

For completeness, let \(q=\nu\cdot\nabla\tau\) and \(L=\sum_l\nu_l(\partial_{z_l}F)(Z_s)\). The left side is \(i\tau L(1+isq)+iqG_s\). On the right, differentiating \(\tau\) gives \(iqG_s\); differentiating \(F\) gives \(i\tau\sum_{j,l}\nu_jF_l(\delta_{lj}+is\nu_l\partial_j\tau)=i\tau L(1+isq)\). Thus the two sides agree directly. The coordinate Cauchy–Riemann equations are exactly what removes anti-holomorphic derivative terms.

Multiply the vector field on the right by a compact smooth cutoff equal to 1 on a neighborhood of \(\overline{B_R}\). Its divergence on the ball and its values on the sphere are unchanged. [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) Theorem 2.1 applies to this compact C¹ complex vector field and gives its integral as the right-hand sphere flux. The fundamental theorem of calculus in \(s\), followed by integration over the compact ball, proves (10). Fubini is justified by continuity on the compact product. In dimension one this is the signed two-endpoint flux, with normals \(-1\) and \(1\) and counting measure. \(\square\)

In differential-form language, \(F(z)\,dz_1\wedge\cdots\wedge dz_n\) is closed: its anti-holomorphic derivatives vanish and each holomorphic derivative wedges with a repeated \(dz_j\). Its pulled-back endpoint coefficient is \(G_sJ_s\). Formula (11) identifies its lateral coefficient explicitly as \(i\tau\nu G_s\). Thus (10) proves the particular Stokes deformation that the logarithmic-inverse lesson actually uses, with its complete boundary coefficient and orientation; no general Stokes theorem on a cylinder with corners is an additional premise.

**Theorem 3.2 (logarithmic graph inversion).** Let \(\tau\) be nonnegative and smooth with \(\|\nabla\tau\|_\infty<\infty\) and

\[
0\le\tau(\xi)\le a\log\langle\xi\rangle+b
\quad(a,b\ge0).
\tag{12}
\]

For every compact smooth test \(\phi\),

\[
\begin{gathered}
\int_{\mathbb R^n}
\widehat\phi(-Z_1(\xi))J_1(\xi)\,d\xi
\\
=\int_{\mathbb R^n}\widehat\phi(-\xi)\,d\xi
\\
=(2\pi)^n\phi(0).
\end{gathered}
\tag{13}
\]

Both integrals are absolutely convergent. The scale used in the logarithmic-inverse lesson,
\(\tau(\xi)=\delta^{-1}\log(2+\delta\langle\xi\rangle)\), satisfies the hypotheses for every fixed \(\delta>0\).

**Proof.** Use (7) with \(F(z)=\widehat\phi(-z)\). Since \(\operatorname{Re}Z_s=\xi\) and \(|\operatorname{Im}Z_s|\le|\nu|\tau\), uniformly for \(0\le s\le1\),

\[
\begin{gathered}
|F(Z_s(\xi))|
\\
\le C_{K,N}'\|\phi\|_{C^N}
\langle\xi\rangle^{-N+aR_K|\nu|}.
\end{gathered}
\tag{14}
\]

The constant includes \(e^{bR_K|\nu|}\). Also \(|J_s|\le1+|\nu|\|\nabla\tau\|_\infty\). Choose \(N>aR_K|\nu|+n\). Integrability follows, for example from dyadic shells exactly as in (3) with exponent \(N-aR_K|\nu|>n\).

The sphere flux in (10) has absolute value at most a constant times

\[
(a\log\langle R\rangle+b)
R^{n-1}\langle R\rangle^{-N+aR_K|\nu|}.
\tag{15}
\]

Indeed the sphere area is its fixed unit-sphere area times \(R^{n-1}\), and \(|\nu\cdot n_R|\le|\nu|\). The fixed area is finite by its finite compact smooth graph cover; in \(n=1\) it is 2. The chosen \(N\) makes (15) tend to zero. Letting \(R\) tend to infinity in (10) is therefore valid by absolute convergence and gives the first equality in (13). The full written Fourier inverse at \(x=0\), with the change of variable \(\xi\mapsto-\xi\), gives the second equality and its coefficient.

For the scale in the logarithmic-inverse lesson,

\[
\begin{gathered}
\nabla\tau(\xi)=
\frac{\xi}{\langle\xi\rangle(2+\delta\langle\xi\rangle)},
\\
\qquad
|\nabla\tau|\le\tfrac12,\\
\qquad
\tau\le\delta^{-1}\log\langle\xi\rangle+
\delta^{-1}\log(2+\delta).
\end{gathered}
\tag{16}
\]

The last inequality uses \(\langle\xi\rangle\ge1\), hence \(2+\delta\langle\xi\rangle\le(2+\delta)\langle\xi\rangle\). Thus take \(a=\delta^{-1}\), \(b=\delta^{-1}\log(2+\delta)\). In dimension zero there is no graph deformation and (13) is the identity \(\widehat\phi(0)=\phi(0)\); the exact scalar \(\tau\) is immaterial. \(\square\)

If a compact low-frequency weight \(\chi_{\rm low}\) is subtracted, the remaining correction

\[
\begin{gathered}
H(x)\\
=-(2\pi)^{-n}\int
\chi_{\rm low}(\xi)e^{ix\cdot Z_1(\xi)}J_1(\xi)\,d\xi
\end{gathered}
\tag{17}
\]

is entire in \(x\in\mathbb C^n\). On its fixed compact frequency support \(Z_1\) and \(J_1\) are bounded. The exponential series and all fixed derivative series converge uniformly there on every compact complex \(x\)-set, bounded by an ordinary exponential majorant. Integration preserves these series. This verifies the remainder used in the logarithmic-inverse lesson without assuming analyticity of the smooth graph function \(\tau\).

## Exercises with complete solutions

**Exercise 1 (intermediate: high derivative).** In \(n=1\), expand (5)–(6) for \(v=\chi D^j u\), and exhibit a constant independent of \(j\) in (4).

**Solution 1.** Here \(\|v\|_{H^1}^2=\|v\|_2^2+\|Dv\|_2^2\), while \(Dv=(D\chi)D^j u+\chi D^{j+1}u\). Thus
\[
\begin{gathered}
\|v\|_{H^1}\\
\le(\|\chi\|_\infty+\|D\chi\|_\infty)\|D^j u\|_{L^2(\operatorname{supp}\chi)}
\\
+\|\chi\|_\infty\|D^{j+1}u\|_{L^2(\operatorname{supp}\chi)}
\end{gathered}
\].
Formula (2) has \(A_1^2=2+4/(1-1/2)=10\). Multiplying the larger of these two coefficients by \(\sqrt{10/(2\pi)}\) gives a valid \(C_\chi\), independently of \(j\). There is no differentiation of \(\chi\) \(j\) times, since the high derivative is taken before introducing the cutoff.

**Exercise 2 (basic: graph orientation).** Take \(n=1\), \(\nu=1\), a positive constant \(\tau=c\), and \(F(z)=z\). Check (10) on \((-R,R)\), including the two endpoint signs. Explain why this example does not satisfy the decay premise needed for (13).

**Solution 2.** The determinant is 1. The left side is
\(\int_{-R}^R[(\xi+ic)-\xi]\,d\xi=2icR\).
At each \(s\), the signed endpoint flux is
\(ic[(R+isc)-(-R+isc)]=2icR\);
integration over \(s\in[0,1]\) gives the same answer. The \(s\)-dependent terms cancel because the outward endpoint normals have opposite signs. This holomorphic \(F\) grows instead of having arbitrarily strong real-frequency decay; its lateral flux need not vanish as \(R\) grows. 3.2 is asserted for compact-test Fourier–Laplace transforms, not arbitrary entire functions.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
