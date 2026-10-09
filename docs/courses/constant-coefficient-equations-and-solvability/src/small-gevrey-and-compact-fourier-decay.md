# Small Gevrey classes and compact Fourier decay

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Every derivative scale corresponds to every Fourier decay constant. We prove this correspondence with its exact compact support, and construct the cutoffs needed for orders greater than one.

Read [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz inversion; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the integration estimates. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. Cauchy kernels and distributional boundary limits proves the Cauchy–Pompeiu formula; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) proves scalar factorization and the exponential series.

For Fourier background, Grubb's author-hosted Chapter 5, *Fourier transformation of distributions*, gives differentiation and Schwartz inversion in Theorem 5.4(2–3), equations (5.9)–(5.10), printed pp. 5.3–5.6, and compact-support holomorphy in Remark 5.18, printed pp. 5.14–5.15. The exact compact-support and all-scale small Gevrey correspondence is proved below. Other general background references are Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## The quantifiers and the algebra

For \(\delta>0\), define \(\gamma^{(\delta)}(\mathbb R^n)\) to consist of the smooth functions such that, for every compact \(L\subset\mathbb R^n\) and every \(\varepsilon>0\), there is \(C_{L,\varepsilon}\) with
\[
\begin{gathered}
|\partial^\alpha f(x)|
 \le C_{L,\varepsilon}\varepsilon^{|\alpha|}(|\alpha|!)^\delta,
 \\
\qquad x\in L,\quad |\alpha|\ge1.
\end{gathered}
\tag{1}
\]
The same condition with \(D=-i\partial\) is identical in modulus. Including \(|\alpha|=0\) changes no class, since \(f\) is bounded on each compact set. Put \(\gamma^{(\delta)}_0=\gamma^{(\delta)}\cap C_c^\infty\).

**Lemma 1.** These classes are closed under sums, products and fixed affine coordinate substitutions. When \(\delta>1\), every compact set inside an open set has a cutoff in \(\gamma^{(\delta)}_0\), equal to one on its neighborhood and supported in that open set.

**Proof of the algebra.** Sums follow by adding constants. For a product, use each factor's estimate at scale \(\varepsilon/2\), also for order zero. If \(k=|\alpha|\), each term in Leibniz's formula has
\((|\beta|!)^\delta((k-|\beta|)!)^\delta\le(k!)^\delta\). The sum of the multi-index binomial coefficients is \(2^k\), so
\[
\begin{gathered}
|\partial^\alpha(fg)|
 \\
\le C_{L,\varepsilon/2}^{f}C_{L,\varepsilon/2}^{g}
       (\varepsilon/2)^k(k!)^\delta
       \\
\sum_{\beta\\
\le\alpha}\binom{\alpha}{\beta}
 \\
\le C\varepsilon^k(k!)^\delta.
\end{gathered}
\tag{2}
\]
Finite products follow by iteration. For a fixed affine substitution \(x=Ay+b\), each of the \(k\) derivative operations is a linear combination with coefficients from \(A\). Expanding successively bounds the sum of coefficient moduli by \(C_A^k\), for a fixed \(C_A\ge1\). Use the original estimate at scale \(\varepsilon/C_A\) on the compact image set. This proves affine closure without changing the order.

**Proof of cutoff existence.** Choose \(1<\sigma<\delta\) and \(a>0\) with \(\sigma=1+1/a\). Set
\[
 h(x)=
 \begin{cases}e^{-x^{-a}},&x>0,\\0,&x\le0.\end{cases}
 \tag{3}
\]
For every positive real \(x\), a fixed sufficiently small \(c\in(0,1/2)\), depending only on \(a\), makes the branch \(z^{-a}\) holomorphic on \(|z-x|\le cx\), with
\(\operatorname{Re}z^{-a}\ge x^{-a}/2\). Indeed, on \(|\omega|<1\) the series \(L(\omega)=\sum_{j\ge1}(-1)^{j+1}\omega^j/j\) converges uniformly on smaller closed disks and has derivative \(1/(1+\omega)\). The function \(\exp(-aL(\omega))\) is holomorphic and equals 1 at zero. On positive real \(1+\omega\), scalar differentiation or the real logarithm identifies it with \((1+\omega)^{-a}\). With \(z=x(1+\omega)\), define \(z^{-a}=x^{-a}\exp(-aL(\omega))\) in that disk. Continuity at zero permits \(c\) so that its normalized real part is at least \(1/2\) for \(|\omega|\le c\). This constructs the required local branch explicitly, using the written complex exponential series in [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html), Section 9.1. Cauchy's derivative bound gives
\[
 |h^{(k)}(x)|\le k!(cx)^{-k}e^{-x^{-a}/2}.
 \tag{4}
\]
For each fixed \(k\), this tends to zero as \(x\downarrow0\): put \(s=x^{-a}\) and use the exponential series to dominate every fixed power \(s^{k/a}\). The derivatives therefore join continuously to zero at the origin. Induction using the mean value theorem shows that these continuous extensions are the derivatives of the joined function. Thus \(h\) is smooth and flat at zero.

For \(k\ge1\), maximize \(s^{k/a}e^{-s/2}\) at \(s=2k/a\). Also
\[
 k!\ge(k/e)^k,
 \tag{5}
\]
because \(\log k!=\sum_{j=1}^k\log j\ge\int_1^k\log t\,dt
=k\log k-k+1\). Equations (4)–(5) imply
\[
\begin{gathered}
\sup_{x\in\mathbb R}|h^{(k)}(x)|
 \\
\le c^{-k}(2/a)^{k/a}(k!)^{1+1/a}
 \\
\le C^k(k!)^\sigma.
\end{gathered}
\tag{6}
\]
The order-zero bound is \(|h|\le1\).

The bump \(b(x)=h(x)h(1-x)\) is smooth, nonnegative, supported in \([0,1]\), and positive inside. Leibniz's formula and (6) give
\(\|b^{(k)}\|_\infty\le C_0C_1^k(k!)^\sigma\): after factoring out \((k!)^\sigma\), the sum is at most \(k+1\), since \(\binom{k}{j}^{1-\sigma}\le1\); absorb \(k+1\) into \(2^k\), handling \(k=0\) separately. For every \(\varepsilon>0\),
\[
 \sup_{k\ge0}\frac{(C_1/\varepsilon)^k}{(k!)^{\delta-\sigma}}
 <\infty.
 \tag{7}
\]
This follows from (5), since the denominator's positive factorial power eventually exceeds any fixed exponential. Hence \(b\in\gamma^{(\delta)}_0(\mathbb R)\).

Normalize its primitive \(H(x)=\int_{-\infty}^x b(s)\,ds/\int b\). It is zero for \(x\le0\), one for \(x\ge1\), and its positive-order derivatives are derivatives of \(b\) divided by the nonzero integral. They obey the same order-\(\sigma\) bound after enlarging constants, and thus the small order-\(\delta\) bounds by (7). Products of translated and rescaled copies of \(H\) give a cutoff supported in any prescribed closed interval and equal to one on a smaller interval in its interior. Products in the individual coordinates give cutoffs on rectangular boxes, using the algebra and affine closure already proved.

Cover the given compact set by finitely many inner boxes whose corresponding slightly larger closed boxes are contained in the given open set. If their cutoffs are \(\chi_j\), then \(\chi=1-\prod_j(1-\chi_j)\) has compact support in their union, belongs to the small class by its algebra, and is one near the given compact set. This proves the assertion. \(\square\)

The choice \(\sigma<\delta\) is essential in this construction: a fixed estimate \(C^k(k!)^\delta\) alone does not give the small class's bound for every \(\varepsilon\).

## The exact supporting function and every decay constant

Let \(K\subset\mathbb R^n\), \(n\ge1\), be nonempty, compact and convex, and set \(H_K(\eta)=\sup_{x\in K}x\cdot\eta\). This function is positively homogeneous, including when \(K\) is translated and \(H_K\) takes negative values.

**Theorem 2.** An entire function \(\Phi\) on \(\mathbb C^n\) is the Fourier–Laplace transform
\(\Phi(\zeta)=\int\phi(x)e^{-ix\cdot\zeta}\,dx\) of a function \(\phi\in\gamma^{(\delta)}_0\) with support contained in \(K\) if and only if for every \(B>0\) there is \(C_B\) with
\[
\begin{gathered}
|\Phi(\zeta)|\\
\le C_B
  \exp\bigl(H_K(\operatorname{Im}\zeta)
                         -B|\operatorname{Re}\zeta|^{1/\delta}\bigr),
 \\
\qquad \zeta\in\mathbb C^n.
\end{gathered}
\tag{8}
\]
The exact set \(K\) and the full supporting-function term are retained in both directions.

**Forward proof.** Compact support makes the transform entire, by differentiating the finite-support integral uniformly on complex compact sets. Every derivative of \(\phi\) also has support in \(K\). Choose a fixed ball containing \(K\), of finite volume \(V>0\). Integration by parts in coordinate \(j\) gives, for every \(k\ge1\),
\[
 |\zeta_j|^k|\Phi(\zeta)|
 \le V C_\varepsilon\varepsilon^k(k!)^\delta
                    e^{H_K(\operatorname{Im}\zeta)}.
 \tag{9}
\]
There is no boundary term or conjugation; multiplication by \(\zeta_j\) is the transform of \(D_j=-i\partial_j\). For \(k=0\), use the bounded order-zero derivative and the same exponential term.

Put \(r=|\operatorname{Re}\zeta|>0\). Some coordinate has
\(|\zeta_j|\ge|\operatorname{Re}\zeta_j|\ge r/\sqrt n\). Since \(k!\le k^k\), (9) yields the upper bound \(VC_\varepsilon(\varepsilon\sqrt n\,k^\delta/r)^k\) times the supporting-function exponential. Set
\[
 q=\left(\frac{r}{e^\delta\varepsilon\sqrt n}\right)^{1/\delta},
 \qquad k=\lfloor q\rfloor .
 \tag{10}
\]
When \(q\ge2\), \(k\ge q/2\) and the parenthesized factor is at most \(e^{-\delta}\). Consequently the additional bound is
\[
 VC_\varepsilon
 \exp\left(-\frac{\delta}{2e(\varepsilon\sqrt n)^{1/\delta}}
                                      r^{1/\delta}\right).
 \tag{11}
\]
Given \(B>0\), choose \(\varepsilon\) small enough that this coefficient is at least \(B\). When \(q<2\), \(r^{1/\delta}\) lies in a bounded interval depending on that chosen scale. The order-zero transform bound absorbs \(e^{Br^{1/\delta}}\) there into a larger constant. This proves (8), including \(r=0\), for every \(B\).

**Reverse proof: real inversion.** Put \(a=1/\delta>0\). Bound (8) on the real axis gives decay faster than every power. Its real derivatives have the same property. Indeed, for a polydisk of fixed radius 1 about a real point \(\xi\), the imaginary vector has norm at most \(\sqrt n\), and \(H_K\) there is at most \(R_K\sqrt n\), \(R_K=\max_{x\in K}|x|\). For \(|\xi|\ge2\sqrt n\), its real vectors have norm at least \(|\xi|/2\). The polydisk Cauchy estimate therefore gives
\[
 |\partial^\alpha\Phi(\xi)|
 \le \alpha!\,C_B e^{R_K\sqrt n}
                     e^{-B2^{-a}|\xi|^a}
 \tag{12}
\]
for each fixed \(\alpha\); the remaining real compact set has a finite bound. Thus \(\Phi|_{\mathbb R^n}\in\mathcal S\). Exact Schwartz inversion defines a Schwartz function
\[
 \phi(x)=(2\pi)^{-n}
       \int_{\mathbb R^n}e^{ix\cdot\xi}\Phi(\xi)\,d\xi.
 \tag{13}
\]

We will repeatedly use that \(J_c=\int_{\mathbb R^n}e^{-c|\xi|^a}\,d\xi<\infty\), for any \(c>0\). To verify this without a gamma-function asymptotic, split into the unit ball and shells \(j\le|\xi|<j+1\). A shell's volume is at most \(C(j+1)^n\). Choose an integer \(q\) with \(aq>n+2\). The positive exponential series gives \(e^{cj^a}\ge(cj^a)^q/q!\). The shell integrals are then bounded by a constant times \(j^{n-aq}\), a summable series. The same argument covers any finite polynomial weight.

**Reverse proof: support by an contour shift.** For a fixed real vector \(\eta\), the one-variable rectangle argument successively in each coordinate gives
\[
\begin{gathered}
\phi(x)=(2\pi)^{-n}
       \\
\int_{\mathbb R^n}e^{ix\cdot(\xi+i\eta)}
                                      \Phi(\xi+i\eta)\,d\xi.
\end{gathered}
\tag{14}
\]
Here are its convergence and side estimates. At a particular coordinate shift, keep the already shifted coordinates fixed and shift that coordinate between imaginary parts 0 and \(\eta_j\). All imaginary vectors on these strips lie in a fixed compact box, so \(H_K\) and the factor \(e^{-x\cdot\operatorname{Im}\zeta}\) have finite uniform bounds. On a vertical side with real coordinate \(\pm R\), and remaining real vector \(\xi'\),
\[
 (R^2+|\xi'|^2)^{a/2}\ge
       \tfrac12(R^a+|\xi'|^a).
 \tag{15}
\]
Indeed the left side is at least each of the two powers separately. Thus, after integrating that side and all the other real coordinates, (8) bounds its modulus by a fixed constant times
\(|\eta_j|e^{-BR^a/2}\int_{\mathbb R^{n-1}}e^{-B|\xi'|^a/2}\,d\xi'\), which tends to zero. In dimension one the last integral over zero coordinates is 1. The horizontal integrals converge absolutely, and dominated convergence allows their truncated real coordinate to tend to the full line. Fubini is applicable by these same integrable bounds. Cauchy's rectangle formula then proves equality for this shift. Iterate over the finitely many coordinates; negative components simply reverse the rectangle orientation. This proves (14) for the original entire \(\Phi\), not for an assumed compact-support transform.

Equation (14) and (8) give, for a fixed \(B>0\),
\[
 |\phi(x)|\le(2\pi)^{-n}C_BJ_B
                      e^{H_K(\eta)-x\cdot\eta}.
 \tag{16}
\]
If \(x\notin K\), let \(y_0\in K\) minimize \(|x-y|\), possible by compactness. For every \(y\in K\), the segment \(y_0+t(y-y_0)\) lies in \(K\); its squared distance from \(x\) has a minimum at \(t=0\), so its right derivative is nonnegative. Thus, with \(\eta_0=x-y_0\ne0\), \((y-y_0)\cdot\eta_0\le0\). It follows that
\(H_K(\eta_0)\le y_0\cdot\eta_0<x\cdot\eta_0\), the gap being \(|x-y_0|^2\). Take \(\eta=t\eta_0\) in (16) and let \(t\to\infty\). Positive homogeneity makes the right side tend to zero; its prefactor is independent of \(t\). Hence \(\phi(x)=0\) outside \(K\). This proves the exact compact support, including when \(K\) has empty interior.

**Reverse proof: the small derivative scales.** Let \(k=|\alpha|\ge1\). Differentiating (13) gives
\[
\begin{gathered}
|\partial^\alpha\phi(x)|
 \\
\le(2\pi)^{-n}C_B
                  \int_{\mathbb R^n}|\xi|^k e^{-B|\xi|^{1/\delta}}\,d\xi.
\end{gathered}
\tag{17}
\]
For \(s=|\xi|^{1/\delta}\), maximize \(s^{\delta k}e^{-Bs/2}\) at \(s=2\delta k/B\). Using (5), the moment is bounded by
\[
 \left(\frac{2\delta k}{eB}\right)^{\delta k}J_{B/2}
 \le \left(\frac{2\delta}{B}\right)^{\delta k}
                              (k!)^\delta J_{B/2}.
 \tag{18}
\]
For a prescribed \(\varepsilon>0\), take \(B\ge2\delta\varepsilon^{-1/\delta}\). Equations (17)–(18) give (1), even globally in \(x\), with the constant \((2\pi)^{-n}C_BJ_{B/2}\). Thus \(\phi\in\gamma_0^{(\delta)}\).

Finally, Schwartz inversion makes the real Fourier transform of \(\phi\) equal to \(\Phi\) on \(\mathbb R^n\). Compact support makes the former entire. Equality extends to all \(\mathbb C^n\): fix all but the first coordinate real and apply the one-variable identity principle, then successively allow each remaining coordinate to be complex. This proves the asserted Fourier–Laplace identity and the theorem. \(\square\)

## Exercises with complete solutions

**Exercise 1 — basic: a fixed scale is weaker.** Show that \(f(x)=1/(1+x^2)\) has a local bound \(C^{k+1}k!\) on every real compact set, but does not belong to \(\gamma^{(1)}(\mathbb R)\). Also justify the factorial-to-power replacement in the small Gevrey definition without invoking Stirling's formula.

**Solution.** The function is holomorphic away from its two poles \(\pm i\). Around every real point the complex disk of radius \(1/2\) stays a uniform positive distance from these poles. On disks about a fixed real compact set, \(f\) has a finite bound. Cauchy's estimate gives \(M2^k k!\), and enlarging \(C\) gives the stated estimate. At zero its geometric series is \(1-x^2+x^4-\cdots\), so
\[
 |f^{(2j)}(0)|=(2j)!.
 \tag{19}
\]
If it were in the small order-one class, a scale \(0<\varepsilon<1\) would give \(1\le C_\varepsilon\varepsilon^{2j}\) for every \(j\), which is impossible. Thus a single fixed exponential derivative scale does not give the every-scale condition.

For \(k\ge1\), (5) and \(k!\le k^k\) give
\((k/e)^{\delta k}\le(k!)^\delta\le k^{\delta k}\). A bound with \((k!)^\delta\) implies the one with \(k^{\delta k}\). Conversely use the latter bound at scale \(\varepsilon/e^\delta\) to obtain the former at scale \(\varepsilon\). The constants may change with the scale, exactly as allowed. Both definitions are therefore equivalent; no asymptotic formula is needed.

**Exercise 2 — intermediate: the compact class is zero at order at most one.** Prove that \(\gamma_0^{(\delta)}(\mathbb R^n)=\{0\}\) when \(0<\delta\le1\).

**Solution.** For a compactly supported \(\phi\) in this class, its derivative estimate on a compact ball containing its support is also a global estimate, since all derivatives are zero outside that support. Fix a point \(x_0\) in the open complement of the support and an arbitrary \(x\), and put \(h=x-x_0\). Every derivative at \(x_0\) is zero. On the segment between these points, the \(k\)-th derivative of \(g(t)=\phi(x_0+th)\) is bounded by \(C_\varepsilon\varepsilon^k(k!)^\delta |h|_1^k\), by expanding the directional derivative and summing its multinomial coefficients. Taylor's theorem with its integral remainder gives
\[
 |\phi(x)|\le C_\varepsilon
     (\varepsilon|h|_1)^{k+1}((k+1)!)^{\delta-1}.
 \tag{20}
\]
If \(h\ne0\), choose a fixed \(\varepsilon\) with \(\varepsilon|h|_1<1\). Since \(\delta-1\le0\), the factorial factor is at most one, and the right side tends to zero as \(k\to\infty\). If \(h=0\), the value is already zero. Thus \(\phi=0\). Together with Lemma 1, this establishes the precise cutoff threshold: nonzero compact cutoffs in the small class exist for every \(\delta>1\), and none exist for \(\delta\le1\).

**Exercise 3 — advanced: retaining a translated support set.** Let \(\psi\in\gamma_0^{(\delta)}(\mathbb R)\) have support in \([-R,R]\), \(R>0\), and set \(\phi(x)=\psi(x-a)\), \(a\in\mathbb R\). Compute the entire transform and its exact supporting-function term. Explain why negative values of that supporting function cause no difficulty.

**Solution.** Affine closure gives \(\phi\in\gamma_0^{(\delta)}\), and its support is contained in \(K=[a-R,a+R]\). Substitution \(y=x-a\) in the Fourier integral gives
\[
\begin{gathered}
\Phi(\zeta)=e^{-ia\zeta}\widehat\psi(\zeta),
 \\
\qquad H_K(\eta)=a\eta+R|\eta|.
\end{gathered}
\tag{21}
\]
The modulus of the phase is \(e^{a\operatorname{Im}\zeta}\). Combining it with the original \([-R,R]\) bound gives exactly
\(|\Phi(\zeta)|\le C_B\exp(a\operatorname{Im}\zeta+R|\operatorname{Im}\zeta|-B|\operatorname{Re}\zeta|^{1/\delta})\).
If \(a>R\) and \(\eta<0\), the supporting function is \((a-R)\eta<0\), so the transform has additional decay along that imaginary direction. The integration and contour proofs use this exact signed term throughout. Replacing it by the radius term alone would discard the translation phase and no longer express the original set \(K\).

## References

- Gerd Grubb, *Fourier transformation of distributions*, author-hosted Chapter 5 of *Distributions and Operators*. Theorem 5.4(2–3), equations (5.9)–(5.10), printed pp. 5.3–5.6; Remark 5.18, printed pp. 5.14–5.15. These passages supply differentiation, Schwartz inversion and compact-support holomorphy background. The exact-support, all-scale small Gevrey theorem and cutoff construction are proved in this lesson. [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in *Classics in Mathematics*, Springer, 2003, e-ISBN 978-3-642-61497-2. Definition 7.1.1, Lemma 7.1.3 and Theorem 7.1.5, printed pp. 160–161; Theorem 7.3.1, printed pp. 181–182. These give ordinary Fourier and compact-support background. The exact-support, all-scale small Gevrey theorem and cutoff construction are proved in this lesson.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
