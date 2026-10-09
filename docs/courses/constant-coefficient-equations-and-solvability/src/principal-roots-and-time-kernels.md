# Principal roots and uniform time kernels

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Time evolution starts with scalar polynomial roots. We bound their displacement from the real principal roots and construct time kernels uniformly even when roots repeat.

Read [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz inversion; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the integration estimates. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. Cauchy kernels and distributional boundary limits proves the Cauchy–Pompeiu formula; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) proves scalar factorization and the exponential series.

For Fourier background, Grubb's author-hosted Chapter 5, *Fourier transformation of distributions*, gives the differentiation convention used in Exercise 1: Theorem 5.4(2), equation (5.9), printed pp. 5.3–5.4. The root-displacement and uniform time-kernel estimates are proved below. Other general background references are Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## Sublinear displacement from the real characteristic roots

**Lemma 1.** Let \(P(\zeta,\tau)\) have total degree \(m\ge1\), with principal part \(F\) hyperbolic with respect to the last frequency vector \(N=(0,\ldots,0,1)\). Every root of \(P(\zeta,\tau)=0\) satisfies
\[
 |\tau|\le C(1+|\zeta|),\qquad \zeta\in\mathbb C^{n-1},
 \tag{1}
\]
and for real \(\xi\in\mathbb R^{n-1}\) also
\[
 |\operatorname{Im}\tau|
          \le C(1+|\xi|)^{1-1/m}.
 \tag{2}
\]
The constant depends on the full polynomial; every lower-order complex coefficient is allowed.

**Proof.** Divide by the nonzero constant \(F(N)\), which does not change any root or the hyperbolicity property. The result is monic in \(\tau\):
\[
\begin{gathered}
P(\zeta,\tau)=\tau^m+\sum_{j=1}^m a_j(\zeta)\tau^{m-j},
 \\
\qquad \deg a_j\le j.
\end{gathered}
\tag{3}
\]
There is \(C_1\ge1\) with \(|a_j(\zeta)|\le[C_1(1+|\zeta|)]^j\) for all \(j\): bound the finitely many polynomial coefficients and choose \(C_1\) greater than each resulting coefficient bound's \(j\)-th root. If \(|\tau|>2C_1(1+|\zeta|)\), then
\[
 \left|\sum_{j=1}^m a_j(\zeta)\tau^{m-j}\right|
 \le|\tau|^m\sum_{j=1}^m2^{-j}<|\tau|^m.
 \tag{4}
\]
This contradicts \(P=0\). Thus (1) holds, even for complex \(\zeta\).

For real \(\xi\), hyperbolicity and scalar factorization give
\[
\begin{gathered}
F(\xi,\tau)=\prod_{\ell=1}^m(\tau-\lambda_\ell(\xi)),
 \\
\qquad \lambda_\ell(\xi)\in\mathbb R.
\end{gathered}
\tag{5}
\]
Multiplicity is included. Hence \(|F(\xi,\tau)|\ge|\operatorname{Im}\tau|^m\). At a root of \(P\), \(F=-(P-F)\). The latter polynomial has total degree at most \(m-1\), and (1) bounds \(|\tau|\) by a fixed multiple of \(1+|\xi|\). Bounding its finitely many monomials gives \(|P-F|\le C_2(1+|\xi|)^{m-1}\). Taking the \(m\)-th root proves (2). For \(m=1\), the exponent is zero, and the imaginary parts are uniformly bounded. We do not extend the real-principal-root argument to complex \(\xi\). \(\square\)

## A contour that remains away from every root

**Lemma 2.** Let \(p(\tau)=\tau^m+a_1\tau^{m-1}+\cdots+a_m\) be a monic scalar polynomial, \(m\ge1\). Suppose each of its roots satisfies \(|\tau|\le A\) and \(|\operatorname{Im}\tau|\le B\), where \(A,B\ge0\). For \(0\le k<m\), the Cauchy problem
\[
\begin{gathered}
p(D_t)v_k=0,\\
\qquad D_t^jv_k(0)=\delta_{jk}\\
\quad(0\le j<m)
\end{gathered}
\tag{6}
\]
has a unique smooth solution on the real line, and, for every integer \(j\ge0\),
\[
 |D_t^jv_k(t)|
 \le2^m(A+1)^{j+m-k}e^{(B+1)|t|}.
 \tag{7}
\]
Repeated roots are permitted.

**Proof.** Put \(R=A+1\), \(h=B+1\), and let \(\Omega\) be the intersection of the disk \(|\tau|<R\) with the strip \(|\operatorname{Im}\tau|<h\), with positively oriented boundary. All roots are inside. At a boundary point on the circle, its distance from every root is at least \(R-A=1\); at a boundary point on a horizontal edge, its imaginary-coordinate distance is at least \(h-B=1\). Thus
\[
 |p(\tau)|=\prod_{\ell=1}^m|\tau-\tau_\ell|\ge1,
 \qquad \tau\in\partial\Omega.
 \tag{8}
\]

Its perimeter is at most \(2\pi R\). If \(h\ge R\), it is the circle. Otherwise put \(u=h/R\in(0,1)\). The two circular side arcs have total length \(4R\arcsin u\), and the two horizontal chords have total length \(4R\sqrt{1-u^2}\). Their sum is \(4R(\arcsin u+\sqrt{1-u^2})\). The expression in parentheses has derivative \((1-u)/\sqrt{1-u^2}\ge0\) and value \(\pi/2\) at \(u=1\), proving the bound. This retains the constant used below, including the corners where arcs meet chords.

Let \(q_k\) be the polynomial part of \(p(\tau)\tau^{-1-k}\). Its degree is \(m-1-k\). Define
\[
 v_k(t)=\frac1{2\pi i}
       \int_{\partial\Omega}e^{it\tau}\frac{q_k(\tau)}{p(\tau)}\,d\tau.
 \tag{9}
\]
The contour is compact and avoids all poles, so differentiation of every time order is legitimate. Applying \(p(D_t)\) cancels its denominator; the remaining entire function \(e^{it\tau}q_k(\tau)\) has zero contour integral by Cauchy's formula. Thus the equation holds.

For the initial conditions,
\[
\begin{gathered}
\frac{q_k(\tau)}{p(\tau)}
       =\tau^{-1-k}+O(\tau^{-m-1})\\
\quad\text{at infinity}.
\end{gathered}
\tag{10}
\]
Indeed, subtract the negative-power part of \(p(\tau)\tau^{-1-k}\); its highest power is at most \(-1\), and division by the monic degree-\(m\) polynomial gives the displayed remainder. For \(j<m\), the coefficient of \(\tau^{-1}\) in \(\tau^jq_k/p\) is precisely \(\delta_{jk}\). Its integral over our boundary equals the integral over a large positive circle: the rational function has no poles between those contours, so the annular Cauchy formula applies. Expanding its convergent Laurent series on that circle selects exactly the coefficient of \(\tau^{-1}\). In (9), \(D_t^je^{it\tau}=\tau^je^{it\tau}\); hence all the initial values in (6) follow.

The scalar coefficients obey \(|a_\ell|\le\binom m\ell A^\ell\), by their elementary-symmetric root formula. On \(|\tau|\le R\) this gives
\[
\begin{gathered}
|q_k(\tau)|
 \\
\le R^{-1-k}\sum_{\ell=0}^m\binom m\ell A^\ell R^{m-\ell}
 \\
=R^{-1-k}(R+A)^m
 \\
\le2^mR^{m-1-k}.
\end{gathered}
\tag{11}
\]
Here \(a_0=1\); extending the sum through \(m\) only increases its nonnegative bound. On our contour, \(|\tau|^j\le R^j\) and \(|e^{it\tau}|\le e^{h|t|}\). Combine (8), (11), the perimeter bound and the prefactor \(1/(2\pi)\) in (9). The result is exactly (7).

Finally, uniqueness does not require distinct roots. The vector of the first \(m\) \(D_t\)-jets of a difference of two solutions satisfies a constant companion system \(\partial_tV=iCV\) with \(V(0)=0\). Integration on an interval of length \(\ell\) gives \(\sup|V|\le\|C\|\ell\sup|V|\). Choose \(\|C\|\ell<1\), or any length if \(C=0\); the supremum must be zero. Iterate in both directions on the real line. The difference is zero everywhere. Existence was already supplied by (9). \(\square\)

## Exercises with complete solutions

**Exercise 1 — basic: the sideways heat scale.** Regard \(-\partial_x^2+\partial_t\) as a second-order equation with Cauchy normal in the \(x\)-direction. Compute the time-kernel roots after Fourier transformation in \(t\), and verify the exponent in Lemma 1.

**Solution.** With \(D=-i\partial\), the symbol is \(P(\xi,\tau)=\tau^2+i\xi\), where \(\xi\) is the frequency of \(t\) and \(\tau\) that of \(x\). Its principal part is \(\tau^2\), hyperbolic with respect to the last vector, since its repeated characteristic root is real. For real \(\xi\ne0\), the roots satisfy \(\tau^2=-i\xi\); therefore
\[
 |\tau|=|\xi|^{1/2},\qquad
 |\operatorname{Im}\tau|=(|\xi|/2)^{1/2}.
 \tag{12}
\]
At \(\xi=0\) both roots are zero. The growth exponent \(1-1/m=1/2\) is attained. This identifies the root growth that the full endpoint small-Gevrey order \(\delta=2\) must control; it is not yet a proof of the full Cauchy existence theorem.

**Exercise 2 — intermediate: repeated roots create no denominator loss.** For \(p(\tau)=(\tau-iB)^m\), \(B\ge0\), find \(v_{m-1}\) in (6) and check the first \(m\) jets.

**Solution.** The function
\[
 v_{m-1}(t)=\frac{(it)^{m-1}}{(m-1)!}e^{-Bt}
 \tag{13}
\]
has \((D_t-iB)^m v_{m-1}=0\): multiplying by \(e^{Bt}\) conjugates \(D_t-iB\) to \(D_t\), which annihilates the degree-\((m-1)\) polynomial after \(m\) derivatives. Every derivative of order less than \(m-1\) at zero is zero. At order \(m-1\), its ordinary derivative is \(i^{m-1}\); multiplying by \((-i)^{m-1}\) gives one. Thus all prescribed \(D_t\)-jets agree, and uniqueness identifies it with the contour kernel. The polynomial factor records the root multiplicity, while Lemma 2 remains valid with \(A=B\) and no inverse root gap.

**Exercise 3 — advanced: the general displacement exponent is sharp.** For \(m\ge2\), consider \(P(\xi,\tau)=(\tau-\xi)^m+i\xi^{m-1}\). Show that its principal part is hyperbolic and that an imaginary root displacement of order \(\xi^{1-1/m}\) occurs as real \(\xi\to+\infty\).

**Solution.** The principal part is \((\tau-\xi)^m\), with the repeated real root \(\tau=\xi\) for every real \(\xi\). Its value at the last frequency vector is 1. For \(\xi>0\), choose any \(c\) with \(c^m=-i\); then
\[
 \tau=\xi+c\xi^{(m-1)/m}
 \tag{14}
\]
is an exact root. At least one such \(c\), and in fact every real candidate fails, has nonzero imaginary part: a real number's integer power is real, whereas \(-i\) is not. Hence
\(|\operatorname{Im}\tau|=|\operatorname{Im}c|\xi^{1-1/m}\). The exponent of Lemma 1 cannot be reduced uniformly over this class of full polynomials. The lower-order term and its complex coefficient are retained, rather than replaced by a condition on the full polynomial's hyperbolicity.

## References

- Gerd Grubb, *Fourier transformation of distributions*, author-hosted Chapter 5 of *Distributions and Operators*. Theorem 5.4(2), equation (5.9), printed pp. 5.3–5.4, supplies Fourier differentiation background for Exercise 1. The root-displacement and uniform contour-kernel arguments are proved in this lesson. [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in *Classics in Mathematics*, Springer, 2003, e-ISBN 978-3-642-61497-2. Definition 7.1.1 and Lemma 7.1.3, printed pp. 160–161, give Fourier convention and differentiation background for Exercise 1 (Fourier transformation in t). The root-displacement and uniform time-kernel estimates are proved in this lesson.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
