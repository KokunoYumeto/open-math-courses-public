# Supported fundamental solutions and test estimates

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A fundamental distribution supported at nonnegative time yields an estimate using only negative-time derivatives of the transposed test. An ordinary fixed-support distribution bound initially measures derivatives on a full neighborhood. We reduce that bound to the half-space by extending the negative-time test with a finite reflection formula. The matching coefficients supply exactly as many boundary derivatives as the distribution's order requires.

Read [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), [Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Local distributional uniqueness is proved in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2.
Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## Finite-order tests and flat boundary functions

Let \(T\) be a compact distribution with a bound
\[
\begin{gathered}
|T(\phi)|\le C\max_{|\alpha|\le M}
                     \sup_{\mathbb R^n}|\partial^\alpha\phi|,
                                 \\
\qquad\phi\in C_c^\infty.
\end{gathered}
\tag{1}
\]
Every compact distribution has such a bound: insert one compact cutoff equal to one near its support and apply its fixed-compact distributional continuity estimate to the cut-off test, using the product rule.

This \(T\) has a unique extension to \(C_c^M\), compatible on functions with a common compact support. To prove it, convolve a compact \(C^M\) function \(w\) with smooth unit-mass compact mollifiers. Each derivative through order \(M\) converges uniformly to that derivative of \(w\), by uniform continuity and the support radius tending to zero. The mollified functions are smooth and have one common compact support for sufficiently small radii. Estimate(1) makes their distributional values Cauchy. The same bound proves independence of the approximants and continuity of the extension in the uniform \(C^M\) norm. It agrees with the original \(T\) on smooth functions.

If \(\operatorname{supp}T\subset\{t\le0\}\), that extension kills every compact \(C^M\) function vanishing on \(t<0\). Here is the finite-regularity boundary argument. All its derivatives through order \(M\) vanish at \(t=0\). Taylor's formula with the continuous highest derivative, uniformly over the compact tangential support, gives
\[
\begin{gathered}
\sup_{0\le t\le2\varepsilon}
       |\partial^\alpha w(x,t)|
                  =o(\varepsilon^{M-|\alpha|})
                         \\
\quad(|\alpha|\le M).
\end{gathered}
\tag{2}
\]
For \(|\alpha|=M\), this means \(o(1)\). For smaller orders, repeated integration of the highest normal derivative with zero boundary values gives the displayed power and little-oh bound, including mixed derivatives.

Choose a smooth \(\sigma\) which is zero at \(s\le1\) and one at \(s\ge2\). The compact \(C^M\) functions \(\sigma(t/\varepsilon)w\) converge to \(w\) in \(C^M\): every product-rule term has a factor \(\varepsilon^{-j}\) multiplying a derivative of order \(|\alpha|-j\) in(2), and is \(o(\varepsilon^{M-|\alpha|})\). They have support in \(t\ge\varepsilon\). Mollifying each with a radius below \(\varepsilon/2\) approximates it by smooth tests supported in positive time, where \(T\) vanishes. Hence its extended value on each is zero, and continuity gives \(T(w)=0\). No measure representation or infinite-order extension theorem is used.

## A finite reflection extension from the negative half-space

For \(j=1,\ldots,M+1\), define
\[
\begin{gathered}
a_j=\prod_{\substack{1\le\ell\le M+1\\\ell\ne j}}
                 \frac{1+\ell}{\ell-j},\\
\qquad
                      \sum_{j=1}^{M+1}a_j(-j)^r=1
                                          \\
\quad(0\le r\le M).
\end{gathered}
\tag{3}
\]
The product for \(M=0\) is one. To prove the identities, the Lagrange polynomials
\(L_j(z)=\prod_{\ell\ne j}(z+\ell)/(\ell-j)\)
are one at \(-j\) and zero at the other nodes. For any polynomial \(b\) of degree at most \(M\), \(b-\sum_j b(-j)L_j\) has \(M+1\) distinct zeros and degree at most \(M\), hence vanishes identically. The finite-root argument here is elementary: if \(q(a)=0\), the identities \(z^r-a^r=(z-a)\sum_{\ell=0}^{r-1}z^{r-1-\ell}a^\ell\) factor \(q(z)=q(z)-q(a)\) by \(z-a\). At every other distinct root the quotient also vanishes. Repetition would make a nonzero polynomial with \(M+1\) roots have degree at least \(M+1\), a contradiction. Evaluate the resulting interpolation identity at \(z=1\) and take \(b(z)=z^r\). This proves(3), including the zeroth moment.

Given \(\phi\in C_c^\infty(\mathbb R^n)\), set
\[
 W\phi(x,t)=
 \begin{cases}
   \phi(x,t),&t\le0,\\
   \displaystyle\sum_{j=1}^{M+1}a_j\phi(x,-jt),&t>0.
 \end{cases}
 \tag{4}
\]
This is compactly supported and \(C^M\). Compactness follows from the finite number of reflected compact supports. For each normal derivative through order \(M\), the two traces match by(3); tangential derivatives preserve the same identities. Thus all mixed derivatives through total order \(M\) match continuously. With a constant depending only on \(M\),
\[
\begin{gathered}
\max_{|\alpha|\le M}\sup|\partial^\alpha W\phi|
       \\
\le A_M\max_{|\alpha|\le M}
                   \sup_{t\le0}|\partial^\alpha\phi|.
\end{gathered}
\tag{5}
\]
For example take \(A_M=\max(1,\sum_j|a_j|(M+1)^M)\). Every normal derivative of a reflected term gains a factor \((-j)^r\), and its evaluation remains at negative time. The traces at time zero obey the same bound by continuity.

When \(T\) is supported in \(t\le0\), \(\phi-W\phi\) is a compact \(C^M\) function vanishing there. The preceding flat-boundary argument and(1),(5) give the support-sensitive estimate
\[
\begin{gathered}
|T(\phi)|\\
=|T(W\phi)|
      \\
\le CA_M\max_{|\alpha|\le M}
                    \sup_{t\le0}|\partial^\alpha\phi|.
\end{gathered}
\tag{6}
\]
Only a finite number of boundary jets has been matched. An arbitrary \(C^\infty\) reflection extension is unnecessary.

## From a supported fundamental solution to the test estimate

Suppose \(P(D)E=\delta_0\), \(\operatorname{supp}E\subset H=\{t\ge0\}\). No global temperedness or finite global order of \(E\) is assumed. Fix the compact neighborhood \(K=\overline{B(0,1)}\), and choose a smooth compact \(\chi\) equal to one near \(K\). The compact distribution \(T=\chi\check E\) has support in \(t\le0\) and some finite order \(M\).

For every \(u\in C_c^\infty\) with support in \(K\), differentiation does not enlarge its support. Reflection and transposition therefore give
\[
\begin{gathered}
u(0)=\check E(P(D)u)=T(P(D)u),\\
\qquad
 |u(0)|\le C'\sum_{|\alpha|\le M}
                     \sup_{t\le0}|D^\alpha P(D)u|.
\end{gathered}
\tag{7}
\]
The first equality follows from \(P(-D)\check E=\delta_0\). The cutoff is one on the entire support of \(P(D)u\). Apply(6) to this test; ordinary derivatives and \(D\)-derivatives have identical absolute values. This is the exact clause(ii) of [the five-way theorem](analytic-root-barriers-and-supported-solvability.md), obtained from clause(i).

## A fixed compact observation set away from the origin

Assume the estimate in(7) is given, with its compact neighborhood and derivative bound. Choose \(\theta\in C_c^\infty(\operatorname{int}K)\) equal to one near zero, and let
\[
          K'=\{t\le0\}\cap\operatorname{supp}d\theta.
 \tag{8}
\]
It is compact and does not contain zero. Every positive-order derivative of \(\theta\) is supported in \(\operatorname{supp}d\theta\), since it is a derivative of at least one first-order derivative and differentiation preserves support.

For a global smooth homogeneous solution \(P(D)u=0\), apply(7) to \(\theta u\). The exact finite product formula is
\[
\begin{gathered}
P(D)(\theta u)=
       \sum_{0<|\beta|\le m}
                  \frac{D^\beta\theta}{\beta!}
                                    P^{(\beta)}(D)u,
                         \\
\qquad m=\deg P.
\end{gathered}
\tag{9}
\]
To verify it, expand every monomial operator by the ordinary product rule; its multinomial coefficient is exactly the coefficient in \(P^{(\beta)}/\beta!\). The zero-index term is \(\theta P(D)u=0\). Derivatives of order above \(m\) are absent.

If \(m\ge1\), differentiating the right side through order \(M\) uses derivatives of \(u\) through at most \(M+m-1\). All cutoff coefficients and their derivatives are fixed and supported in \(K'\) on the negative half-space. Thus
\[
\begin{gathered}
|u(0)|\le C''\sum_{|\gamma|\le M+m-1}
                           \sup_{K'}|D^\gamma u|,
          \\
\qquad u\in C^\infty(\mathbb R^n),\ P(D)u=0.
\end{gathered}
\tag{10}
\]
This is the full finite compact observation estimate needed to test the later analytic-root family. For \(m=0\), every homogeneous solution is zero and the assertion is immediate. No growth condition on the global smooth \(u\) is needed, because \(\theta u\) is compact.

## The full-frequency and tangential root conditions

For the unit normal \(N=e_t\), the clause(iii) allows the base frequency to vary in all \(n\) complex coordinates, not just the tangential \(d=n-1\). Its root is a displacement \(\sigma\) along \(N\):
\[
\begin{gathered}
P(z,s+\sigma(z,s))=0,\\
\qquad
 \sup_{B_n((c,b),A_1)}\operatorname{Im}\sigma\ge A_2,
                       \\
\quad c\in\mathbb R^d,\ b\in\mathbb R.
\end{gathered}
\tag{11}
\]
This condition, with some radius and height, is equivalent to([equation 1 in Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md)), with some radius and height. If \(r(z)\) is an analytic tangential normal root on \(B_d(c,A_1)\), then \(\sigma(z,s)=r(z)-s\) is a full-frequency displacement root on \(B_n((c,b),A_1)\). Projection stays in the tangential ball and \(|\operatorname{Im}s|<A_1\). Hence(11) implies
\[
 \sup_{B_d(c,A_1)}\operatorname{Im}r\ge A_2-A_1.
 \tag{12}
\]
Conversely, if([equation 1 in Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md)) holds with radius \(A_1\) and height \(B_2\), any full displacement root restricts at the real center value \(s=b\) to the analytic tangential root \(r(z)=b+\sigma(z,b)\) on the same tangential ball. Its imaginary supremum is at least \(B_2\), so the full displacement root has supremum at least \(B_2\) as well. This proves the reverse condition with that height. No simplicity or nonvanishing leading coefficient is used. In dimension \(d=0\), the section is one real center point and the same argument is just the scalar root-height shift. The results proved with([equation 1 in Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md)) therefore receive the clause(iii) with an explicit change of height, not an assumption that its two coordinate formulations are literally identical.

## The other two elementary logical implications

Clause(iv) of [the five-way theorem](analytic-root-barriers-and-supported-solvability.md), if assumed, implies clause(v) without an additional Holmgren assumption. For finite-order \(f\) of order \(M_0\), the direct Fourier estimate([equation 18 in Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md)) puts it in \(B^{\rm loc}_{2,\langle\xi\rangle^{-r}}\), \(r=M_0+n+1\). Clause(iv) gives a supported solution in \(B^{\rm loc}_{2,\langle\xi\rangle^{-r}S_P}\). The strictly positive constant lower bound of \(S_P\) and the explicit norm test([equation 19 in Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md)) give one uniform finite distributional order for that solution. These two Fourier computations depend only on the weighted-space formulas, not on the global existence theorem or its available Holmgren theorem.

Clause(v) implies clause(i) by taking the finite-order datum \(\delta_0\). This proves the elementary chain(iv) to(v) to(i) to(ii). The implication(ii) to(iii) is proved in [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md).

## Exercises with complete solutions

**Exercise 1 (entry).** Compute the reflection coefficients for \(M=1\). Show that they match value and first derivative, but need not produce a \(C^2\) extension.

**Solution.** The coefficients are \(a_1=3,a_2=-2\). Their zeroth and first moments are \(3-2=1\) and \(3(-1)-2(-2)=1\). Thus \(W\phi(t)=3\phi(-t)-2\phi(-2t)\) at positive time has the same value and first derivative as \(\phi\) at zero. If \(\phi(t)=t^2\) near zero, the negative side is \(t^2\), while the positive side is \((3-8)t^2=-5t^2\). Its second derivative has traces \(2\) and \(-10\); the extension is \(C^1\) and is not \(C^2\). The second moment is \(-5\), so no second-jet matching was asserted.

**Exercise 2 (intermediate).** For \(P(s)=s-i\) and \(u\in C_c^\infty((-1,1))\), derive the supported test estimate with no derivatives of \(P(D)u\).

**Solution.** Its retarded fundamental kernel is \(E(t)=iH(t)e^{-t}\), so \(\check E(t)=iH(-t)e^t\). Direct integration gives
\[
\begin{gathered}
\int_{-\infty}^0 i e^t(D_t-i)u(t)\,dt
       \\
=\int_{-\infty}^0 e^t(u'+u)\,dt\\
=u(0).
\end{gathered}
\]
The integrand is the derivative of \(e^tu(t)\), and the compact support kills its lower endpoint. Therefore
\(|u(0)|\le(1-e^{-1})\sup_{t\le0}|(D_t-i)u(t)|\).
The weight integral is over \([-1,0]\). This illustrates order zero in(7); using a higher order is allowed but unnecessary for this kernel.

**Exercise 3 (advanced).** For \(P(D)=D_t^2+D_x\), compute the cutoff commutator on a homogeneous solution and verify the largest derivative order in(10).

**Solution.** The product rule gives
\(P(D)(\theta u)=2(D_t\theta)D_tu+
(D_t^2\theta)u+(D_x\theta)u\),
after the term \(\theta P(D)u\) is removed. Every term is supported in the fixed derivative support of \(\theta\). Applying any \(D^\alpha\), \(|\alpha|\le M\), gives derivatives of \(u\) through at most \(M+1\), because only the first summand initially contains one derivative of \(u\). The other summands use at most \(M\). Here \(m=2\), so \(M+m-1=M+1\), exactly(10). The constants involve finitely many derivatives of the fixed cutoff and do not depend on the particular homogeneous solution.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
