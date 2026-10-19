# Cauchy kernels and distributional boundary limits

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

A holomorphic function can grow without having ordinary values on the edge of its domain. Integration against a test function can still have a limit. The test absorbs enough derivatives to balance the growth. The Cauchy kernel shows what this limit remembers: approaching a real pole from above or below gives the same principal value and opposite concentrated terms.

[Avi Zeff’s lecture on Pompeiu’s formula](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html), Section 2, is a primary human reference for the complex Green identity and punctured-circle argument. [Dyatlov 2026], Proposition 9.8, states the fundamental solution of the Cauchy–Riemann operator. We give the kernel and finite-order boundary proofs here. We use [Boundary flux and weak identities](boundary-flux-and-weak-identities.md) for Green’s formula and pointwise-to-weak equations, and [Order, positivity and distributional limits](order-positivity-and-limits.md) for finite-regularity tests. We use the elliptic regularity theorem in Elliptic tests and intrinsic wavefront; Section 2 checks its hypotheses for this operator. Entry prerequisites are multivariable calculus, dominated convergence and elementary geometric series.

## A small circle detects the Cauchy kernel

Write \(z=x+iy\), \(dA=dx\,dy\), and

\[
\bar\partial=\frac12(\partial_x+i\partial_y).
\tag{1.1}
\]

Distributions pair linearly with their tests; there is no complex conjugation in the pairing. An oriented boundary is positive when the region lies to the left as it is traversed. In particular the outer boundary of a disk is counterclockwise, while the inner boundary of a punctured disk is clockwise. Complex Green’s formula, proved in the boundary lesson, reads

\[
2\int_Y\bar\partial v\,dA
=-i\int_{\partial_XY}v\,dz
\quad(v\in C_c^1(X)).
\tag{1.2}
\]

Here \(Y\subset X\subset\mathbb C\) is open with a relative \(C^1\) boundary. Compact support makes the boundary integral finite even if \(Y\) is unbounded.

**Theorem 1.1 (Cauchy–Pompeiu with a relative boundary).** If \(\phi\in C_c^1(X)\) and \(\zeta\in Y\), then

\[
\phi(\zeta)=
\frac{1}{2\pi i}\int_{\partial_XY}
\frac{\phi(z)}{z-\zeta}\,dz
-\frac1\pi\int_Y
\frac{\bar\partial\phi(z)}{z-\zeta}\,dA(z).
\tag{1.3}
\]

Both integrals are ordinary integrals. The area kernel is locally integrable at \(\zeta\).

**Proof.** Polar coordinates give \(\int_{|z-\zeta|<r}|z-\zeta|^{-1}\,dA=2\pi r\). Choose \(\varepsilon>0\) so that the closed disk about \(\zeta\) of radius \(\varepsilon\) lies in \(Y\). On its complement the function \(\phi(z)/(z-\zeta)\) is \(C^1\), and

\[
\bar\partial\left(\frac{\phi(z)}{z-\zeta}\right)
=\frac{\bar\partial\phi(z)}{z-\zeta}.
\tag{1.4}
\]

To apply (1.2) literally to a compact \(C^1\) function on \(X\), multiply the quotient by a smooth radial cutoff which is zero for \(|z-\zeta|\leq\varepsilon/2\) and one for \(|z-\zeta|\geq3\varepsilon/4\). This does not change the function or its derivatives on the punctured region \(Y\setminus\overline{B(\zeta,\varepsilon)}\).

Let \(C_\varepsilon\) denote the circle with its counterclockwise orientation. Formula (1.2), with the clockwise inner orientation of the punctured region, gives

\[
\frac{1}{2\pi i}\int_{C_\varepsilon}
\frac{\phi(z)}{z-\zeta}\,dz
=\frac{1}{2\pi i}\int_{\partial_XY}
\frac{\phi(z)}{z-\zeta}\,dz
-\frac1\pi\int_{Y\setminus\overline{B(\zeta,\varepsilon)}}
\frac{\bar\partial\phi(z)}{z-\zeta}\,dA.
\tag{1.5}
\]

Parametrizing \(C_\varepsilon\) by \(z=\zeta+\varepsilon e^{i\theta}\), its left side is \((2\pi)^{-1}\int_0^{2\pi}\phi(\zeta+\varepsilon e^{i\theta})\,d\theta\), which tends to \(\phi(\zeta)\). The removed area integral has absolute value at most \(2\varepsilon\|\bar\partial\phi\|_\infty\). Passing to the limit proves (1.3). \(\square\)

**Corollary 1.2 (fundamental solution, including the normalization).** On \(\mathbb C\),

\[
E_\zeta(z)=\frac{1}{\pi(z-\zeta)},
\qquad \bar\partial E_\zeta=\delta_\zeta.
\tag{1.6}
\]

The same equality holds after restricting to an open \(X\) containing \(\zeta\).

**Proof.** For a compact smooth test choose a disk containing both its support and \(\zeta\). The boundary term in (1.3) is zero. Thus \(-\int E_\zeta\bar\partial\phi\,dA=\phi(\zeta)\), which is exactly the distributional derivative convention in (1.6). A test compactly supported in an arbitrary \(X\) extends smoothly by zero to \(\mathbb C\), so restriction gives the last assertion. \(\square\)

The point source in (1.6) comes from the shrinking circle. The classical derivative is zero away from that point, and deleting the circle without keeping its boundary integral would delete the entire source.

## Weak Cauchy–Riemann solutions are holomorphic

We use the following consequence of the linked elliptic-regularity theorem: if \(P\) is a properly supported classical elliptic operator and \(Pu\) is smooth, then a distribution \(u\) is smooth. The linked proof constructs a local inverse up to a smooth kernel; its wavefront formulation allows any fixed operator order. We need only a constant-coefficient differential operator of order one on an arbitrary open subset of \(\mathbb R^2\).

**Proposition 2.1 (exact regularity specialization).** If \(u\in\mathcal D'(X)\) and \(\bar\partial u=0\), then \(u\) is the distribution of a holomorphic function on \(X\).

**Proof.** Under the convention \(D_j=-i\partial_j\), the principal symbol of (1.1) is

\[
p(\xi_x,\xi_y)=\frac{i\xi_x-\xi_y}{2},
\qquad |p(\xi)|=\frac{|\xi|}{2}.
\tag{2.1}
\]

It is a scalar classical symbol of order one and is nonzero at every nonzero real covector. A differential operator has kernel supported on the diagonal; both projections of this support are proper on every open \(X\). Hence the stated elliptic theorem applies and gives a smooth representative \(h\) of \(u\). The equation becomes \(h_x+ih_y=0\) pointwise, or \(h_y=ih_x\).

Real differentiability now gives, for a small complex increment \(a+ib\),

\[
h(z+a+ib)-h(z)
=h_x(z)(a+ib)+o(|a+ib|).
\tag{2.2}
\]

Thus the complex derivative exists and equals \(h_x\); \(h\) is holomorphic. \(\square\)

There is no preliminary boundedness or continuity assumption on the distribution in this proposition.

**Corollary 2.2 (complex differentiability is enough).** A function which is complex differentiable at every point of \(X\) is smooth, satisfies (1.1) pointwise, and has a convergent power series in each disk whose closure lies in \(X\).

**Proof.** Complex differentiability implies continuity and real differentiability at each point, with \(h_y=ih_x\). Apply the pointwise-to-weak first-order identity of the boundary lesson with coefficients \(a_1=1/2\), \(a_2=i/2\), zero zeroth-order coefficient and zero right side. It yields \(\bar\partial h=0\) weakly even before derivative continuity is known. Proposition 2.1 gives a smooth representative, which agrees with the original continuous function everywhere.

For a closed disk \(\overline{B(a,R)}\subset X\), choose a compact smooth cutoff equal to one on a neighborhood of this disk. Apply (1.3) to the disk and to the cutoff times \(h\). The area term is zero, so

\[
h(\zeta)=\frac{1}{2\pi i}
\int_{|z-a|=R}\frac{h(z)}{z-\zeta}\,dz
\quad(|\zeta-a|<R).
\tag{2.3}
\]

On \(|\zeta-a|\leq r<R\), expand the denominator by its uniformly convergent geometric series. Termwise integration gives

\[
h(\zeta)=\sum_{j=0}^{\infty}c_j(\zeta-a)^j,
\qquad c_j=\frac{1}{2\pi i}
\int_{|z-a|=R}\frac{h(z)}{(z-a)^{j+1}}\,dz.
\tag{2.4}
\]

If \(M=\max_{|z-a|=R}|h(z)|\), then \(|c_j|\leq MR^{-j}\). This proves convergence on every smaller disk. The same estimate with the polynomial factors from differentiation permits differentiation of the series on smaller disks. Its coefficients are therefore \(c_j=h^{(j)}(a)/j!\). \(\square\)

## Test derivatives balance polynomial growth

Let \(I\subset\mathbb R\) be an open interval, \(\gamma>0\), and let \(f\) be holomorphic on \(I+i(0,\gamma)\). Assume, for an integer \(N\geq0\),

\[
|f(x+iy)|\leq C y^{-N}
\quad(x\in I,\ 0<y<\gamma).
\tag{3.1}
\]

For \(\phi\in C_c^{N+1}(I)\), its pairing at positive height is an ordinary integral. The function \(f\) need not have a pointwise limit at height zero.

**Theorem 3.1 (boundary limit on finite-regularity tests).** The limit

\[
\langle f_+,\phi\rangle
=\lim_{\varepsilon\downarrow0}
\int_I f(x+i\varepsilon)\phi(x)\,dx
\tag{3.2}
\]

exists for every \(\phi\in C_c^{N+1}(I)\). On smooth tests it defines a distribution of order at most \(N+1\). For each compact support set \(K\Subset I\), the positive-height pairings have a common bound in the \(C^{N+1}\) norm for all sufficiently small heights.

**Proof.** Extend \(\phi\) by zero along the real axis, and put

\[
\Phi(x,s)=\sum_{j=0}^N
\frac{(is)^j}{j!}\phi^{(j)}(x).
\tag{3.3}
\]

This compactly supported \(C^1\) function has an almost vanishing Cauchy–Riemann derivative:

\[
\bar\partial\Phi(x,s)
=\frac{(is)^N}{2N!}\phi^{(N+1)}(x).
\tag{3.4}
\]

Indeed the \(x\)-derivative of term \(j\) cancels the \(i\partial_s\) derivative of term \(j+1\), leaving precisely the last term. This calculation also holds for \(N=0\).

Fix \(0<T<\gamma\) and take \(0<\varepsilon<\gamma-T\). Differentiating \(A_\varepsilon(s)=\int_I f(x+i(\varepsilon+s))\Phi(x,s)\,dx\) and integrating by parts in \(x\) gives

\[
A_\varepsilon'(s)
=-2i\int_I f(x+i(\varepsilon+s))\bar\partial\Phi(x,s)\,dx
=-\frac{i^{N+1}s^N}{N!}
\int_I f(x+i(\varepsilon+s))\phi^{(N+1)}(x)\,dx.
\tag{3.5}
\]

No end terms occur since every derivative of \(\phi\) is supported in the same compact set. The first equality uses \(f_y=if_x\). Integrating (3.5) from zero to \(T\) yields the exact identity

\[
\int_I f(x+i\varepsilon)\phi(x)\,dx
=\int_I f(x+i(\varepsilon+T))\Phi(x,T)\,dx
+\frac{i^{N+1}}{N!}\int_0^T s^N
\int_I f(x+i(\varepsilon+s))\phi^{(N+1)}(x)\,dx\,ds.
\tag{3.6}
\]

Choose a compact interval \(K\Subset I\) containing the support. In the second term, (3.1) gives

\[
s^N|f(x+i(\varepsilon+s))|
\leq C\left(\frac{s}{\varepsilon+s}\right)^N
\leq C.
\tag{3.7}
\]

For \(N=0\) the ratio to the zeroth power is one. The integrable majorant is constant on \(K\times(0,T)\). Dominated convergence therefore passes the second term to its limit; the first converges by smoothness at height \(T\). In particular the limit is

\[
\langle f_+,\phi\rangle
=\int_I f(x+iT)\Phi(x,T)\,dx
+\frac{i^{N+1}}{N!}\int_0^T s^N
\int_I f(x+is)\phi^{(N+1)}(x)\,dx\,ds.
\tag{3.8}
\]

Every integral on the right is absolutely convergent. Formula (3.6) also gives, writing \(|K|\) for the length of the containing interval,

\[
\left|\int_I f(x+i\varepsilon)\phi(x)\,dx\right|
\leq C|K|\left(
T^{-N}\sum_{j=0}^N\frac{T^j}{j!}
+\frac{T}{N!}\right)
\|\phi\|_{C^{N+1}},
\tag{3.9}
\]

where \(\|\phi\|_{C^{N+1}}=\max_{0\leq j\leq N+1}\|\phi^{(j)}\|_\infty\). This proves the uniform bound and distributional continuity of the limit. The value in (3.8) is independent of \(T\) because it is the limit of the same left side of (3.6). \(\square\)

The order bound is a sufficient bound, and can exceed the actual order. For instance a function which extends smoothly across the interval has an order-zero boundary distribution regardless of a larger exponent chosen in (3.1).

**Corollary 3.2 (moving tests and the lower side).** If \(\phi_\varepsilon\) have a common compact support in \(I\) and converge to \(\phi\) in \(C^{N+1}\), then

\[
\int_I f(x+i\varepsilon)\phi_\varepsilon(x)\,dx
\longrightarrow\langle f_+,\phi\rangle.
\tag{3.10}
\]

For a holomorphic function on \(I+i(-\gamma,0)\) satisfying \(|f(x-iy)|\leq Cy^{-N}\), the lower limit \(f_-\) exists on the same tests and obeys (3.9). Its version of (3.8) uses \(\Phi_-(x,s)=\sum_{j=0}^N(-is)^j\phi^{(j)}(x)/j!\), height \(-T\), and coefficient \((-i)^{N+1}/N!\).

**Proof.** Subtract the fixed-test pairing from the moving-test pairing. Estimate their difference by (3.9), which tends to zero; Theorem 3.1 handles the remaining fixed test. For the lower side put \(g(w)=f(-w)\). This is holomorphic in the reflected upper strip and has the same bound. Apply the upper theorem with test \(\psi(t)=\phi(-t)\), then substitute \(x=-t\). Each test derivative contributes \((-1)^j\), giving the stated lower polynomial and coefficient. \(\square\)

Local bounds suffice as well: to obtain the limit on a compact subinterval, apply the proof in a slightly larger relatively compact interval where (3.1) holds with one constant. Uniqueness of limits makes the resulting local distributions agree on overlaps.

## A real pole remembers the side of approach

For a smooth compact test on \(\mathbb R\), define the principal value by symmetric deletion:

\[
\left\langle\operatorname{pv}\frac1x,\phi\right\rangle
=\lim_{r\downarrow0}\int_{|x|>r}\frac{\phi(x)}x\,dx
=\int_0^\infty\frac{\phi(x)-\phi(-x)}x\,dx.
\tag{4.1}
\]

The last integrand is bounded at zero by \(2\|\phi'\|_\infty\); it has compact support at infinity. This proves existence and an order-at-most-one estimate on each fixed support interval.

**Theorem 4.1 (individual pole limits and their jump).** In \(\mathcal D'(\mathbb R)\), and also on compact \(C^1\) tests,

\[
\frac1{x+i0}=\operatorname{pv}\frac1x-i\pi\delta_0,
\qquad
\frac1{x-i0}=\operatorname{pv}\frac1x+i\pi\delta_0.
\tag{4.2}
\]

In particular their difference is \(-2\pi i\delta_0\).

**Proof.** For \(y>0\), separate the real and imaginary kernels:

\[
\frac1{x+iy}=\frac{x}{x^2+y^2}
-i\frac{y}{x^2+y^2}.
\tag{4.3}
\]

The pairing of the real part is \(\int_0^\infty x[\phi(x)-\phi(-x)]/(x^2+y^2)\,dx\). On a fixed support interval it is dominated by \(2\|\phi'\|_\infty\), since \(|\phi(x)-\phi(-x)|\leq2x\|\phi'\|_\infty\). Its limit is (4.1). For the imaginary part, substitute \(x=yt\):

\[
\int_{\mathbb R}\frac{y\phi(x)}{x^2+y^2}\,dx
=\int_{\mathbb R}\frac{\phi(yt)}{1+t^2}\,dt
\longrightarrow\pi\phi(0).
\tag{4.4}
\]

Dominated convergence uses \(\|\phi\|_\infty/(1+t^2)\); the integral of \((1+t^2)^{-1}\) is \(\pi\). This proves the upper limit. Replacing \(iy\) by \(-iy\) reverses only the sign of the imaginary part, proving the lower limit. \(\square\)

For \(m\geq1\) define the finite-part distribution

\[
\operatorname{pf}\frac1{x^m}
=\frac{(-1)^{m-1}}{(m-1)!}
\partial_x^{m-1}\left(\operatorname{pv}\frac1x\right).
\tag{4.5}
\]

This definition agrees with \(x^{-m}\) away from zero, but for \(m\geq2\) it is not an ordinary integral across zero. The derivative definition fixes its normalization.

**Corollary 4.2 (higher poles).** For each integer \(m\geq1\),

\[
\frac1{(x\pm i0)^m}
=\operatorname{pf}\frac1{x^m}
\mp i\pi\frac{(-1)^{m-1}}{(m-1)!}\delta_0^{(m-1)}.
\tag{4.6}
\]

Their jump is \(-2\pi i(-1)^{m-1}\delta_0^{(m-1)}/(m-1)!\). These limits exist on all compact \(C^m\) tests.

**Proof.** At positive height, ordinary differentiation gives

\[
(x\pm iy)^{-m}
=\frac{(-1)^{m-1}}{(m-1)!}
\partial_x^{m-1}(x\pm iy)^{-1}.
\]

Pairing with a test and integrating by parts gives \(1/(m-1)!\) times the simple-pole pairing with \(\phi^{(m-1)}\). Theorem 4.1 applies when this derivative is \(C^1\), which is precisely ensured by \(\phi\in C_c^m\). Passing to the limit yields (4.5)–(4.6), with the distributional derivative sign intact. \(\square\)

For \(m=2\), the upper formula is \(\operatorname{pf}(1/x^2)+i\pi\delta'_0\); the jump pairs with \(\phi\) as \(-2\pi i\phi'(0)\). This is a useful sign check because \(\langle\delta'_0,\phi\rangle=-\phi'(0)\).

## Exercises

**Exercise 1 (basic: the inner orientation).** Put \(\zeta=0\). Let a compact \(C^1\) test equal one on a disk around zero. Compute the counterclockwise integral of \(\phi(z)/z\) on a sufficiently small circle, and the corresponding inner-boundary integral on the punctured region. Explain which distributional source is lost if the inner-boundary term is discarded.

**Exercise 2 (intermediate: testing a pole away from the origin).** For real \(a\), find the upper and lower boundary distributions of \((z-a)^{-1}\). Pair their difference with a compact smooth test \(\phi\). Does the jump vanish when the support of \(\phi\) misses \(a\)?

**Exercise 3 (intermediate: a rational principal part).** Let \(f(z)=2/(z-a)^3-3/(z-a)\), where \(a\) is real. Compute its upper boundary distribution, lower boundary distribution and jump. Express the jump pairing in terms of \(\phi(a)\) and \(\phi''(a)\), retaining all signs.

**Exercise 4 (advanced: the finite test norm matters).** Under (3.1), fix \(K\Subset I\) and \(0<T<\gamma\). Prove that a family \(\phi_\varepsilon\) supported in \(K\), with \(\|\phi_\varepsilon\|_{C^{N+1}}\leq\varepsilon^{1/3}\), has positive-height pairings tending to zero. Identify the exact step in the proof which uses the \((N+1)\)-st derivative, and explain why this proof alone gives no uniform estimate in the \(C^N\) norm.

**Exercise 5 (intermediate: holomorphicity before derivative continuity).** Suppose \(h\) is complex differentiable everywhere on an open \(X\). State the two separate results that make \(h\) a smooth weak Cauchy–Riemann solution, and check the ellipticity and properness hypotheses. Derive the estimate \(|h^{(j)}(a)|\leq j!M/R^j\) for a closed disk in \(X\).

**Exercise 6 (advanced: a finite part has a concentrated correction).** Prove \(x\,\operatorname{pv}(1/x)=1\) and \(x\,\operatorname{pf}(1/x^2)=\operatorname{pv}(1/x)\). Then prove \(x(x\pm i0)^{-2}=(x\pm i0)^{-1}\), including the point-supported terms. Explain why using \(x\delta'_0=0\) would give a wrong conclusion.

## Complete solutions

**Solution 1.** Parametrize the counterclockwise circle by \(z=re^{i\theta}\). Since \(\phi=1\) there, the integral is \(\int_0^{2\pi}i\,d\theta=2\pi i\). The clockwise inner orientation contributes \(-2\pi i\). It is this term in (1.5) which leaves \(\phi(0)\) in the limit. Omitting it would incorrectly assert that \(\bar\partial(1/(\pi z))\) is zero; its actual source is \(\delta_0\).

**Solution 2.** Substitute \(t=x-a\) in Theorem 4.1. The upper value is \(\operatorname{pv}(1/(x-a))-i\pi\delta_a\); the lower value has \(+i\pi\delta_a\). Their difference pairs as \(-2\pi i\phi(a)\). A test whose support misses \(a\) has \(\phi(a)=0\), so its jump pairing is zero. The two boundary distributions coincide with the same smooth function away from \(a\).

**Solution 3.** For \(m=3\), the coefficient of \(\delta_a''\) in the upper pole is \(-i\pi/2\). Thus the upper boundary is

\[
\begin{aligned}
f_+={}&2\operatorname{pf}\frac1{(x-a)^3}
-3\operatorname{pv}\frac1{x-a}\\
&-i\pi\delta_a''+3i\pi\delta_a.
\end{aligned}
\]

The lower boundary has the same finite parts and the opposite concentrated terms. The jump is \(-2i\pi\delta_a''+6i\pi\delta_a\), pairing as \(-2i\pi\phi''(a)+6i\pi\phi(a)\). The second delta derivative has a positive pairing sign, since its derivative order is even.

**Solution 4.** Enlarge \(K\) to one compact interval inside \(I\), and use its length in (3.9). Its right side is a fixed constant times \(\varepsilon^{1/3}\), which tends to zero for \(\varepsilon<\gamma-T\). Cancellation in (3.4) leaves \(s^N\phi^{(N+1)}\). This cancels the singular factor of size \(s^{-N}\) after the vertical integration in (3.6). A \(C^N\) norm does not control that remaining derivative, so (3.9) cannot be asserted with that smaller norm from this calculation. The exercise makes no assertion that a sharper estimate is impossible for a particular \(f\).

**Solution 5.** Complex differentiability implies continuity, real differentiability and the pointwise equation \((h_x+ih_y)/2=0\). The pointwise-to-weak theorem with constant coefficients gives that equation distributionally. The cited elliptic regularity theorem then makes its distribution smooth. Its continuous representative is \(h\) itself. Formula (2.1) gives a nonzero principal symbol with magnitude \(|\xi|/2\), and the diagonal kernel of a differential operator is proper on \(X\). Cauchy’s formula and the circle coefficient calculation in (2.4) give \(|c_j|\leq M/R^j\) and \(h^{(j)}(a)=j!c_j\), which prove the estimate.

**Solution 6.** Symmetric deletion gives \(\langle x\operatorname{pv}(1/x),\phi\rangle=\lim_{r\downarrow0}\int_{|x|>r}\phi(x)\,dx=\int\phi\). Put \(v=\operatorname{pv}(1/x)\); then \(\operatorname{pf}(1/x^2)=-v'\). The product rule \((xv)'=v+xv'\), together with \((xv)'=1'=0\), gives \(-xv'=v\). Finally \(\langle x\delta'_0,\phi\rangle=-(x\phi)'(0)=-\phi(0)\), so \(x\delta'_0=-\delta_0\). Multiply the \(m=2\) formula (4.6) by \(x\): the upper value becomes \(v-i\pi\delta_0\), and the lower becomes \(v+i\pi\delta_0\). These are exactly the simple-pole values. Setting \(x\delta'_0\) to zero would incorrectly remove their concentrated terms.

## References

- [Avi Zeff, *Lecture 12: Pompeiu’s formula*, March 6, 2026](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html). Section 2 gives the complex Green and Cauchy–Pompeiu formulas on planar domains.
- [Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications* (2026)](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf). Proposition 9.8 states \(\bar\partial(1/(\pi z))=\delta_0\); the proof is assigned there as an exercise and is supplied here in Section 1.
- *Elliptic tests and intrinsic wavefront*, equation (G27). The stronger elliptic-regularity result used in Proposition 2.1, with its exact symbol specialization in (2.1). The linked lesson is licensed under GFDL 1.2.

[Dyatlov 2026]: https://math.mit.edu/~dyatlov/18.155/155-notes.pdf
