# Weighted inversion on a half-line

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The characteristic Cauchy construction needs estimates on a half-line rather than on the whole time axis. Taking an infimum over Schwartz extensions does not automatically preserve a full-line identity: the inverse must also preserve the half-line restriction. We prove that exact point for polynomials whose roots lie in the upper half-plane, including repeated roots and both norm endpoints.

Read [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The weight and the quotient are exact

Let \(k:\mathbb R\to(0,\infty)\) be measurable and satisfy, for fixed \(C\ge0\) and integer \(N\ge0\),
\[
\begin{gathered}
k(\xi+\eta)\le k(\xi)(1+C|\eta|)^N.
 \\
\quad
 \|u\|_{p,k}=(2\pi)^{-1/p}
       \|k\widehat u\|_{L^p(\mathbb R)},\\
\quad u\in\mathcal S(\mathbb R),
 \\
\quad 1\le p\le\infty.
\end{gathered}
\tag{1}
\]
The factor is one when \(p=\infty\). Both weight directions follow by using \(\xi=0\) and then \(\eta=-\xi\):
\[
\begin{gathered}
k(0)(1+C|\xi|)^{-N}\\
\le k(\xi)
 \\
\le k(0)(1+C|\xi|)^N.
\end{gathered}
\tag{2}
\]
Thus every Schwartz function has finite norm, and the reciprocal weight has at most polynomial growth.

Let \(\mathbb R_-=\{t:t<0\}\). For \(u\in\mathcal S\) define
\[
\begin{gathered}
\|u\|^-_{p,k}
 \\
=\inf\{\|v\|_{p,k}:v\in\mathcal S,\ v\\
=u\text{ on }\mathbb R_-\}.
\end{gathered}
\tag{3}
\]
This depends only on the restriction to the open negative half-line. It is the norm of its class in \(\mathcal S/\mathcal N\), where \(\mathcal N\) consists of Schwartz functions vanishing there; completeness of this quotient is not assumed here.

For precision, it really is a norm of restriction classes, not a possibly degenerate seminorm. Let \(\phi\in C_c^\infty(\mathbb R_-)\) and let \(p'\) be the conjugate exponent. Schwartz inversion, its bilinear product identity, and Hölder give
\[
\begin{gathered}
\left|\int u(t)\phi(t)\,dt\right|
 \\
\le (2\pi)^{-1/p'}\left\|
           \frac{\widehat\phi(-\xi)}{k(\xi)}
        \right\|_{p'}\|u\|^-_{p,k}.
\end{gathered}
\tag{4}
\]
Indeed the pairing is unchanged by replacing \(u\) with any extension \(v\), and its Fourier integral is \((2\pi)^{-1}\int\widehat v(\xi)\widehat\phi(-\xi)\,d\xi\). The displayed constant is finite by(2), including \(p'=1,\infty\). Take the infimum over \(v\). If the quotient norm is zero, every such test pairing is zero. A nonzero continuous value of \(u\) on the negative half-line would be detected by a sufficiently small nonnegative smooth cutoff, multiplied by a fixed complex phase; this contradicts that conclusion. Hence \(u=0\) there. Homogeneity and the triangle inequality follow by scaling and adding extensions within any positive error of their infima.

## A causal inverse preserves the restriction

For \(\lambda=a+ib\), \(b>0\), define
\[
\begin{gathered}
K_\lambda(r)=i\,\mathbf1_{\{r\ge0\}}e^{i\lambda r},\\
\qquad
 T_\lambda f(t)=\int_0^\infty i e^{i\lambda r}f(t-r)\,dr.
\end{gathered}
\tag{5}
\]
The kernel is in \(L^1\) and has every absolute moment:
\[
\begin{gathered}
\int_0^\infty r^j|K_\lambda(r)|\,dr=j!\,b^{-j-1},
 \\
\qquad j\ge0.
\end{gathered}
\tag{6}
\]
For \(j=0\), evaluate the exponential integral; ordinary integration by parts proves the recursion for higher \(j\), with both endpoint terms controlled by exponential decay.

Differentiation under the integral is valid at every fixed order, since the corresponding derivative of a Schwartz function is bounded and the kernel is integrable. For every integer \(L\ge0\),
\[
\begin{gathered}
\sup_t |t|^L|\partial_t^\ell T_\lambda f(t)|
 \\
\le\sum_{j=0}^L {L\choose j}j!b^{-j-1}
             \sup_y |y|^{L-j}|\partial_y^\ell f(y)|.
\end{gathered}
\tag{7}
\]
This follows by \(|t|^L\le\sum_j{L\choose j}r^j|t-r|^{L-j}\). It proves that \(T_\lambda\) continuously maps \(\mathcal S\) into itself, with every Schwartz seminorm controlled by finitely many actual seminorms of \(f\).

Directly evaluating the absolutely convergent kernel transform gives
\[
\begin{gathered}
\widehat K_\lambda(\xi)
   =i\int_0^\infty e^{i(\lambda-\xi)r}\,dr
   =\frac1{\xi-\lambda},
 \\
\qquad \xi\in\mathbb R.
\end{gathered}
\tag{8}
\]
The convolution Fourier identity follows by Fubini, since the absolute double integral is bounded by \(\|K_\lambda\|_1\|f\|_1\). The written Fourier inversion and differentiation identities now give
\[
\begin{gathered}
(D-\lambda)T_\lambda f=f,\\
\qquad
 T_\lambda(D-\lambda)f=f,\\
\qquad D=-i\partial_t.
\end{gathered}
\tag{9}
\]
Most importantly, \(T_\lambda f(t)=0\) for \(t<0\) whenever \(f=0\) for \(t<0\): each sampled point \(t-r\) is negative. Thus \(T_\lambda\mathcal N\subset\mathcal N\). The forward differential operator also preserves \(\mathcal N\), by locality.

## The exact polynomial quotient identity

**Theorem.** Let \(q\) be a nonzero one-variable polynomial all of whose zeros have positive imaginary part. Constants are allowed. Then, for every \(u\in\mathcal S(\mathbb R)\),
\[
\begin{gathered}
\|u\|^-_{p,|q|k}=\|q(D)u\|^-_{p,k},
 \\
\qquad 1\le p\le\infty.
\end{gathered}
\tag{10}
\]

**Proof.** Write \(q(\xi)=c\prod_{\nu=1}^m(\xi-\lambda_\nu)\), with repetitions included and \(c\ne0\). Set \(T_q=c^{-1}T_{\lambda_1}\cdots T_{\lambda_m}\). For degree zero set \(T_q=c^{-1}I\). Equations(7)–(9) prove that \(T_q\) is the two-sided inverse of \(q(D)\) on \(\mathcal S\). Both maps preserve \(\mathcal N\), so
\[
\begin{gathered}
v=u\text{ on }\mathbb R_-
 \\
\quad\Longleftrightarrow\\
\quad
 q(D)v=q(D)u\text{ on }\mathbb R_-.
\end{gathered}
\tag{11}
\]
The forward implication is locality. For the reverse, apply \(T_q\) to \(q(D)(v-u)\in\mathcal N\). This is also an exact bijection between the two extension families: for any Schwartz extension \(w\) of \(q(D)u\), the function \(v=T_qw\) is a Schwartz extension of \(u\), and \(q(D)v=w\).

On the whole line, the Fourier multiplier identity gives \(\|v\|_{p,|q|k}=\|q(D)v\|_{p,k}\). Use the just-proved bijection in the infimum:
\[
\begin{gathered}
\inf_{v|_{\mathbb R_-}=u|_{\mathbb R_-}}\|v\|_{p,|q|k}
 \\
=\inf_{w|_{\mathbb R_-}=q(D)u|_{\mathbb R_-}}\|w\|_{p,k}.
\end{gathered}
\tag{12}
\]
This proves(10), without requiring that either infimum be attained.

The new weight \(|q|k\) remains in the stated weight class. For real \(\xi,\eta\), each factor satisfies
\[
 \frac{|\xi+\eta-\lambda_\nu|}{|\xi-\lambda_\nu|}
 \le1+\frac{|\eta|}{\operatorname{Im}\lambda_\nu}.
 \]
Choose a common constant at least \(C\) and every reciprocal imaginary part. Multiplying the factor inequalities and(1) gives the same weight inequality with exponent \(N+m\). No zero on the real axis occurs. This also justifies applying the restriction-norm argument to \(|q|k\). \(\square\)

For a single root, \(|\xi-\lambda|\ge b=\operatorname{Im}\lambda\) on the real axis. The full-line pointwise norm inequality passes to the common extension infimum. With(10), it gives the precise estimate
\[
\begin{gathered}
b\,\|u\|^-_{p,k}
 \le\|(D-\lambda)u\|^-_{p,k},\\
\qquad b>0.
\end{gathered}
\tag{13}
\]
All endpoints \(p=1,\infty\) are included. For a general \(q\) with roots as above, the same reasoning gives \(|c|\prod_\nu\operatorname{Im}\lambda_\nu\) as one valid lower-bound coefficient.

## Exercises with complete solutions

**Exercise 1 — basic: phase and preservation.** Prove(9) directly from the integral, and explain why it preserves vanishing on the negative half-line.

**Solution.** Write \(I(t)=\int_0^\infty e^{i\lambda r}f(t-r)\,dr\), so \(T_\lambda f=iI\). Use \(\partial_t f(t-r)=-\partial_r f(t-r)\), and integrate in \(r\). The upper endpoint is zero by exponential decay; the lower endpoint is \(f(t)\). The result is \(\partial_tT_\lambda f=i f+i\lambda T_\lambda f\), hence \((D-\lambda)T_\lambda f=f\). All derivatives are legitimate by the Schwartz bound and exponential moments. The other inverse identity follows by the same calculation with \(f\) replaced by \(Df-\lambda f\), or by the already proved Fourier identity. If \(t<0\), every \(t-r<0\), so a forcing zero on that half-line makes its inverse zero there too. A coefficient \(-i\) instead of \(i\) would give \(-f\).

**Exercise 2 — intermediate: a repeated root.** Give the kernel of the inverse of \(q(D)=(D-i)^2\), prove its sign, and state the exact quotient norm identity.

**Solution.** The two identical first-order kernels convolve. For \(t>0\), their integrand on \(0<r<t\) is \(i^2e^{-r}e^{-(t-r)}=-e^{-t}\); for \(t<0\) their supports do not meet. Thus
\[
 K_q(t)=-\mathbf1_{\{t\ge0\}}\,t e^{-t}.
 \tag{14}
\]
It has all absolute moments and maps Schwartz functions into Schwartz functions. One application of \(D-i\) sends this kernel to \(i\mathbf1_{\{t\ge0\}}e^{-t}\): ordinary differentiation of \(te^{-t}\) gives that expression, and the possible Dirac coefficient at zero is zero because \(te^{-t}\) vanishes there. A second application gives \(\delta_0\), with the first-order \(i\) phase. The theorem says \(\|u\|^-_{p,(\xi^2+1)k}=\|(D-i)^2u\|^-_{p,k}\), including \(p=1,\infty\). Repetition creates a polynomial factor in the causal kernel and no new restriction ambiguity.

**Exercise 3 — advanced: why the upper half-plane matters.** For \(\operatorname{Im}\lambda<0\), construct a nonzero Schwartz restriction on \(\mathbb R_-\) whose image under \(D-\lambda\) is zero there. Explain the failure of(10).

**Solution.** Choose a smooth function \(\chi\) equal to one on \(t\le0\) and zero on \(t\ge1\), with a smooth transition on \((0,1)\), using the flat cutoff. Put
\[
\begin{gathered}
u(t)=\chi(t)e^{i\lambda t},\\
\qquad
 (D-\lambda)u=-i\chi'(t)e^{i\lambda t}.
\end{gathered}
\tag{15}
\]
As \(t\to-\infty\), the exponential modulus \(e^{-\operatorname{Im}\lambda\,t}\) decays, and every derivative has the same exponential decay up to a fixed constant. On the positive side the function is compactly supported. Thus \(u\in\mathcal S\), and it is nonzero on the negative half-line. Its image is supported in \([0,1]\) and vanishes on \(\mathbb R_-\); the image quotient norm is zero. The restriction norm \(\|u\|^-_{p,|\xi-\lambda|k}\) is positive by the test-separation proof(4), since that real-axis weight is positive and moderate by the same absolute-imaginary-part argument. Therefore the asserted equality fails. A full-line inverse remains available, but it does not preserve this particular half-line restriction.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
