# Compact multipliers and exponential solutions of convolution systems

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A common zero of the Fourier transforms of compact kernels gives a common exponential solution. Does every system with a nonzero solution have such a zero? In at least two variables the answer is no. We construct six kernels whose system has a nonzero smooth solution even though every exponential, and every exponential polynomial, fails.

Assume distributions, compact convolution and holomorphic functions. The exact compact-support Fourier theorem is Theorem CF2.1 in Compact Fourier division and multiplicity-sensitive annihilators. The weighted existence theorem used to construct an entire graph is Theorem W2 in Solving the Cauchy–Riemann equations with a weight. Both lessons supply full proofs. The [complete proof](compact-multipliers-and-convolution-systems-formal.md) supplies every additional argument, including functional separation and the topology of the entire-function ideal.

Basic references are D. I. Gurevich's *Counterexamples to a problem of L. Schwartz*, the compact Fourier lesson, and the weighted Cauchy–Riemann lesson. The summable sinc product in Zero-free cones turn slow decrease into reciprocal bounds provides another useful comparison. The product here has a different spacing and a stronger quantitative decay estimate.

## 1. What the exponential test can tell us

We use the conventions
\[
 \widehat\mu(z)=\langle\mu(t),e^{-it\cdot z}\rangle,
 \qquad D=-i\partial,\qquad z\in\mathbb C^n.
 \tag{E1.1}
\]
For any complex frequency \(\zeta\),
\[
 (\mu*e^{ix\cdot\zeta})(x)
   =e^{ix\cdot\zeta}\widehat\mu(\zeta).
 \tag{E1.2}
\]
Compact support makes this convolution well defined. A common zero of several transforms therefore gives a common exponential solution. If their common zero set is empty, no exponential works.

There is a further consequence: no nonzero exponential polynomial works. Such a function is a finite sum of polynomials times exponentials. Choose a real direction that separates its finitely many distinct frequencies. Apply constant coefficient differential operators that kill all but one frequency. Further derivatives reduce its polynomial to a nonzero constant. These operations commute with compact convolution, so an exponential polynomial solution would produce an exponential solution. Proposition 4.2 of the complete proof gives the full isolation argument.

This test excludes a particular class of solutions. To construct a solution outside that class, we need a different tool.

## 2. A system that defeats the exponential zero test

**Theorem 2.1.** In every dimension \(n\ge2\), there are six compact distributions \(\mu_1,\ldots,\mu_6\) for which
\[
 \mu_j*u=0\quad(j=1,\ldots,6)
 \tag{E2.1}
\]
has a smooth global solution with \(u(0)=1\), while it has no nonzero exponential polynomial solution. The solution extends to an entire function.

Here is the construction. Choose
\[
 \alpha=\frac34,\qquad \beta=\frac78,\qquad
 A=\frac1{16},\qquad d=1,\qquad
 a_j=A j^{-1/\beta},\qquad R=\sum_{j\ge1}a_j\le\frac12.
 \tag{E2.2}
\]
Form the two entire multipliers
\[
 Q_1(z)=\prod_{j\ge1}\frac{\sin(a_jz)}{a_jz},
 \qquad Q_2(z)=Q_1(z+i).
 \tag{E2.3}
\]
The value of each factor at zero is one. The zeros of the first product are real; the zeros of the second have imaginary part \(-1\). Thus the products have no common zero. Both are transforms of smooth compact functions supported in \([-R,R]\). Their real-axis decay is strong enough to absorb any growth of the form \(\exp(B|z|^\alpha)\), because \(\alpha<\beta\).

The geometric part produces an entire function \(g\) on \(\mathbb C\) and an entire function \(f_2\) on \(\mathbb C^2\). Put
\[
 f_1(z_1,z_2)=z_2-g(z_1),\qquad
 f_2(v,g(v))=e^{-v^2}.
 \tag{E2.4}
\]
Both \(g\) and \(f_2\) grow at most like \(\exp(B|z|^\alpha)\), with their own constants. The graph restriction in (E2.4) is never zero. Consequently \(f_1\) and \(f_2\) have no common zero. Propositions 5.2 and 5.3 of the complete proof construct these functions using the weighted Cauchy–Riemann theorem.

Define six transforms by
\[
 \begin{aligned}
 h_1&=f_1Q_1(z_1),&h_2&=f_1Q_2(z_1),\\
 h_3&=f_2Q_1(z_1)Q_1(z_2),&
 h_4&=f_2Q_1(z_1)Q_2(z_2),\\
 h_5&=f_2Q_2(z_1)Q_1(z_2),&
 h_6&=f_2Q_2(z_1)Q_2(z_2).
 \end{aligned}
 \tag{E2.5}
\]
Each is a compact-distribution transform. The first two kernels have order at most one and support in \([-R,R]\times\{0\}\). The last four are smooth functions supported in \([-R,R]^2\). For the first two, multiplication by \(z_2\) produces \(D\delta_0\) in the second coordinate. This is why the assertion concerns distributions rather than six measures.

At a hypothetical common zero, the first two equations force \(f_1=0\). In each coordinate one of \(Q_1,Q_2\) is nonzero. Select the corresponding product among the last four equations; it forces \(f_2=0\). This contradicts (E2.4). Thus the exponential test excludes every exponential polynomial.

The existence of a different solution follows from the proper ideal discussed next. For \(n>2\), tensor each two-dimensional kernel with point distributions in the extra coordinates and make the solution independent of those coordinates. Theorem 6.1 of the complete proof verifies the whole assertion.

## 3. Why an ideal can produce a solution

Let \(\mathcal A\) be the algebra of entire functions of finite exponential type. For each positive integer \(m\), let
\[
 E_m=\{F:\|F\|_m<\infty\},\qquad
 \|F\|_m=\sup_{z\in\mathbb C^2}|F(z)|e^{-m|z|},
 \qquad \mathcal A=\bigcup_{m\ge1}E_m.
 \tag{E3.1}
\]
Give this union its finest locally convex topology making every inclusion \(E_m\to\mathcal A\) continuous. This topology allows all finite exponential types.

The graph construction has the crucial property
\[
 1\notin\overline{f_1\mathcal A+f_2\mathcal A}.
 \tag{E3.2}
\]
Because every \(h_j\) in (E2.5) belongs to this ideal, the closure of the ideal they generate also misses 1. Functional separation gives a continuous linear functional \(L\) vanishing on that closure, with \(L(1)=1\). Set
\[
 U(w)=L_z(e^{iw\cdot z}).
 \tag{E3.3}
\]
This is entire. Moreover,
\[
 (\mu_j*U)(w)
   =L_z(e^{iw\cdot z}h_j(z))=0,\qquad U(0)=1.
 \tag{E3.4}
\]
Lemma 3.2 of the complete proof proves the interchange of the distributional pairing and \(L\), including the necessary derivative estimates. The real restriction of \(U\) is the required solution.

Why does (E3.2) hold? The graph is bounded after the substitution \(v=\sqrt z\) in the curved region
\[
 G=\{z:\operatorname{Re}z>|z|^{3/4}\}.
 \tag{E3.5}
\]
On that graph, an ideal element \(F=f_1A_1+f_2A_2\) becomes \(e^{-z}a(z)\), where \(a\) has growth of order at most \(1/2\) on \(G\). A suitable small neighborhood in \(\mathcal A\) controls \(F-1\) on the graph by growth of order \(2/3\). A maximum-principle argument then forces \(F\) to be small at one fixed large positive point, while the neighborhood condition forces it to be close to 1 there. These demands contradict one another. Proposition 5.4 of the complete proof supplies the constants and proves that the neighborhood controls every exponential type.

The empty common zero set and the proper ideal are separate facts. The first excludes exponentials; the second produces the nonzero solution.

## 4. Four worked examples

**Example 1. A smaller support and a larger imaginary shift.** Take \(\beta=3/4,A=1/32,d=2\). Then
\[
 a_j=\frac1{32}j^{-4/3},\qquad
 R=\frac1{32}\sum_{j\ge1}j^{-4/3}\le\frac18,\qquad
 c=(\log4)\,128^{-3/4}.
 \tag{E4.1}
\]
The support bound follows from \(R\le A/(1-\beta)\). The first multiplier has zeros \(32\pi m j^{4/3}\), with \(m\ne0\). The shifted multiplier has exactly those real parts and imaginary part \(-2\). If \(\rho\) is the nonnegative smooth kernel of the first multiplier, the second kernel is \(e^{2t}\rho(t)\). Its integral need not be one; its carrier stays within the same interval. The Fourier sign is checked directly:
\[
 \int e^{2t}\rho(t)e^{-itz}\,dt
      =\int\rho(t)e^{-it(z+2i)}\,dt=Q_1(z+2i).
 \tag{E4.2}
\]

**Example 2. An empty zero set can also mean there are no solutions.** On the real line take
\[
 \mu_1=\delta_1-2\delta_0,\qquad
 \mu_2=D\delta_0-b\delta_0.
 \tag{E4.3}
\]
Their transforms are \(e^{-iz}-2\) and \(z-b\). A common zero exists exactly when \(e^{-ib}=2\). For \(b=i\log2\), the function \(u(x)=e^{-x\log2}\) solves both equations: translation by one multiplies it by 2, and \(Du=i(\log2)u\). For \(b=0\), the second equation says \(u'=0\). A smooth solution is constant; the first equation then says \(-u=0\). Only the zero solution remains. The same conclusion holds for distributions: if \(T'=0\), every compactly supported test function of integral zero is a derivative of another test function, so \(T\) is a constant distribution. Its first equation kills that constant. Thus an empty common zero set alone neither constructs nor guarantees a nonzero solution.

**Example 3. A polynomial graph gives visible distribution kernels.** Let \(g(z_1)=z_1^2\), \(f_1=z_2-z_1^2\), and \(f_2=1\). Use either multiplier from Example 1, with kernel \(\rho_\ell\). The transform \(h_\ell=f_1Q_\ell(z_1)\) comes from
\[
 \mu_\ell=\rho_\ell\otimes D\delta_0
              -D_1^2\rho_\ell\otimes\delta_0.
 \tag{E4.4}
\]
Indeed the transforms of the two terms are \(z_2Q_\ell(z_1)\) and \(z_1^2Q_\ell(z_1)\). Both physical terms are supported on \([-R,R]\times\{0\}\); the derivative in the second variable has order one. This example makes the Fourier conversion explicit. It is not the graph used in Theorem 2.1: here \(f_2=1\), so the generated ideal contains 1 and the proper-ideal argument cannot apply.

**Example 4. Choosing the separating point explicitly.** Let \(C_0\ge0\) be the bound for \(g(\sqrt z)\) on the closed region \(G\), and put
\[
 D_0=3\left(\frac{1+C_0}{4}\right)^{4/3},\qquad
 K=\frac{1+D_0}{\cos(3\pi/8)},\qquad
 X=[2(K+1)]^4,\qquad
 \eta=\frac18e^{-D_0X^{2/3}}.
 \tag{E4.5}
\]
The symbol \(D_0\) here is a positive scalar constant, not the differential operator \(D\). We have \(X>16\) and
\[
 \frac{KX^{3/4}}X=\frac{K}{2(K+1)}<\frac12,\qquad
 2e^{-X+KX^{3/4}}<2e^{-8}<\frac12,\qquad
 \eta e^{D_0X^{2/3}}=\frac18.
 \tag{E4.6}
\]
An ideal element lying within this neighborhood of 1 would therefore have modulus less than \(1/2\) and at least \(7/8\) at the same graph point. This explicit choice closes the contradiction without choosing a new neighborhood for each exponential type.

## 5. Exercises and full solutions

The first four exercises are worth 10 points each. The last four are worth 15 points each, for a total of 100 points.

### Exercise 1. Support, decay and zero coordinates — 10 points

Take \(\beta=4/5,A=1/20,d=3/2\). Compute the support bound, the decay constant \(c\), and both zero sets. Explain why zero is not a zero of either multiplier.

**Solution.** The spacing is \(a_j=(1/20)j^{-5/4}\). The support radius and decay constant satisfy
\[
 R=\frac1{20}\sum_{j\ge1}j^{-5/4}\le\frac14,\qquad
 c=(\log4)\,80^{-4/5}.
 \tag{E5.1}
\]
The first zero set is \(\{20\pi m j^{5/4}:m\in\mathbb Z\setminus\{0\},j\ge1\}\). The second is its translate by \(-3i/2\). The product at zero is 1. The shifted product at zero is
\[
 Q_2(0)=\prod_{j\ge1}\frac{\sinh(3a_j/2)}{3a_j/2}>0.
 \tag{E5.2}
\]
The factors have no zeros and their deviations from 1 are summable, so their convergent product is positive. Alternatively the exact zero-set theorem already excludes this point. Award 3 points for the support bound, 2 for \(c\), 3 for both zero sets, and 2 for the values at zero.

### Exercise 2. Which weight moves the zeros downward? — 10 points

Let \(Q=\widehat\rho\), where \(\rho\) is smooth and supported in \([-R,R]\). Identify the physical kernel of \(Q(z+id)\), including the sign of its weight. Prove that this change does not enlarge support. If \(\rho\ge0\), show that the new kernel is nonnegative.

**Solution.** Substitute the shifted argument:
\[
 Q(z+id)=\int\rho(t)e^{-it(z+id)}\,dt
       =\int e^{dt}\rho(t)e^{-itz}\,dt.
 \tag{E5.3}
\]
Thus the weight is \(e^{dt}\). It is smooth, strictly positive and never zero. Multiplication by it leaves the support exactly unchanged: the function vanishes on an open set before multiplication if and only if it vanishes there afterward. In particular both supports are contained in \([-R,R]\). Nonnegativity is also preserved. Award 5 points for the transform calculation and its sign, 3 for support, and 2 for positivity.

### Exercise 3. Removing every support loss — 10 points

Suppose one entire function \(H\) satisfies, for every \(\delta>0\), the compact Fourier growth condition for the box \([-R-\delta,R+\delta]^k\). Each application of the compact Fourier theorem yields a distribution \(\nu_\delta\). Show that there is one distribution supported in \([-R,R]^k\). Explain why a single value of \(\delta\) would not suffice.

**Solution.** All the transforms equal \(H\). Fourier uniqueness gives \(\nu_\delta=\nu_{\delta'}\) for every pair of positive values. Denote this common distribution by \(\nu\). Its support lies in every larger box, hence in their intersection:
\[
 \operatorname{supp}\nu
 \subset\bigcap_{\delta>0}[-R-\delta,R+\delta]^k
 =[-R,R]^k.
 \tag{E5.4}
\]
Equivalently any point outside the smaller box has one coordinate of modulus larger than \(R\); choosing a smaller positive \(\delta\) gives a neighborhood where \(\nu\) vanishes. A single growth bound yields only its one larger box. For example a point distribution at \(R+\delta/2\) in one coordinate fits that box but lies outside the desired box. Award 4 points for uniqueness, 4 for intersection or the neighborhood argument, and 2 for the counterexample to one fixed loss.

### Exercise 4. Why all four products are present — 10 points

Suppose \(Q_1,Q_2\) have no common zero and \(f_1,f_2\) have no common zero. Prove that the six functions in (E2.5) have no common zero. State the extra assertion that is needed to obtain a nonzero solution.

**Solution.** At a common zero \(z\), at least one of \(Q_1(z_1),Q_2(z_1)\) is nonzero. The first two equations then imply \(f_1(z)=0\). Select a nonzero multiplier in the second coordinate as well. The corresponding one of the four products multiplying \(f_2\) is nonzero, so its equation implies \(f_2(z)=0\). This contradicts the premise. All four products allow either of the two choices in each coordinate. A nonzero solution is obtained from the separate assertion \(1\notin\overline{f_1\mathcal A+f_2\mathcal A}\), together with the compact-transform construction and functional separation. Example 2 shows why absence of common zeros does not supply this assertion. Award 3 points for forcing \(f_1=0\), 4 for selecting the product and forcing \(f_2=0\), and 3 for identifying the extra condition.

### Exercise 5. Positive Levi eigenvalues without a uniform bound — 15 points

For \(M>0\), put \(\phi(z)=M(1+|z|^2)^p\) on \(\mathbb C^2\), with \(p=3/8\). Calculate its tangential and radial Levi eigenvalues. Prove strict positivity and determine whether the least eigenvalue has a positive global lower bound.

**Solution.** Write \(s=|z|^2\). Differentiating gives the Hermitian matrix
\[
 \left(\frac{\partial^2\phi}{\partial z_j\partial\bar z_\ell}\right)
 =Mp(1+s)^{p-1}I
      +Mp(p-1)(1+s)^{p-2}(\bar z_j z_\ell)_{j,\ell}.
 \tag{E5.5}
\]
The rank-one term is zero on the complex tangent space perpendicular to the radial direction and has eigenvalue \(s\) on that direction. Consequently the two eigenvalues are
\[
 \lambda_{\mathrm{tan}}=Mp(1+s)^{p-1},\qquad
 \lambda_{\mathrm{rad}}=Mp(1+s)^{p-2}(1+ps).
 \tag{E5.6}
\]
Both are positive for all \(s\ge0\). Since \(p<1\), their ratio is \((1+ps)/(1+s)\le1\), so the radial eigenvalue is the least. As \(s\to\infty\), it is asymptotic to \(Mp^2s^{p-1}\), which tends to zero. Thus the weight is strictly plurisubharmonic everywhere but has no positive uniform global lower eigenvalue. The general weighted theorem used in the proof permits this situation; replacing it by a theorem requiring a uniform lower bound would change the hypotheses. Award 5 points for the matrix, 5 for both eigenvalues, and 5 for positivity and the failed uniform bound.

### Exercise 6. The strict sector gap — 15 points

For \(\alpha=3/4\), \(\pi/4\le\theta\le3\pi/4\), and \(s=\sin(3\pi\alpha/4)\), prove
\[
 s\cos(\alpha(\theta-\pi))
   +\cos(\alpha\theta+\pi/2-\pi\alpha/4)
 =\sin(\alpha(\pi-\theta))\cos(3\pi\alpha/4)<0.
 \tag{E5.7}
\]
Give an explicit uniform negative upper bound. Explain the consequence for a polynomial factor times the exponential error ratio in the graph construction.

**Solution.** Set \(t=\alpha(\pi-\theta)\) and \(a=3\pi\alpha/4\). Then \(\cos(\alpha(\theta-\pi))=\cos t\), while the second cosine is \(\cos(a+\pi/2-t)=-\sin(a-t)\). The left side is
\[
 \sin a\cos t-\sin(a-t)=\cos a\sin t.
 \tag{E5.8}
\]
Here \(a=9\pi/16\), so \(\cos a<0\). Also \(3\pi/16\le t\le9\pi/16\). The sine on this interval has minimum \(\sin(3\pi/16)>0\): it increases up to \(\pi/2\), then decreases to \(\sin(9\pi/16)>\sin(3\pi/16)\). Thus the left side is at most \(-\varepsilon\), where
\[
 \varepsilon=-\cos(9\pi/16)\sin(3\pi/16)>0.
 \tag{E5.9}
\]
An error ratio bounded by \(Cr^N e^{-\varepsilon r^{3/4}}\) tends uniformly to zero as \(r\to\infty\), because \(N\log r-\varepsilon r^{3/4}\to-\infty\). This is the strict gap that allows the selected exponential term to dominate. Award 5 points for the identity, 6 for the interval and explicit gap, and 4 for uniform error decay.

### Exercise 7. How fast must the neighborhood shrink? — 15 points

Replace the factors \(e^{-m^4}\) in the absolutely convex neighborhood by \(e^{-m^q}\), where \(q>1\). On a graph with \(|Z(z)|\le\sqrt r+C_0\), calculate the resulting power of \(r\) in the evaluation bound. For which \(q\) can this bound be absorbed on \(\operatorname{Re}z=r^{3/4}\)?

**Solution.** For \(a\ge0\), maximize \(-t^q+at\) over \(t\ge0\). Its derivative vanishes at \(t=(a/q)^{1/(q-1)}\), and the maximum is
\[
 (q-1)(a/q)^{q/(q-1)}.
 \tag{E5.10}
\]
Use \(a=\sqrt r+C_0\le(1+C_0)\sqrt r\) for \(r\ge1\). The evaluation envelope is bounded by \(\exp(C_q r^\tau)\), with
\[
 \tau=\frac{q}{2(q-1)},\qquad
 C_q=(q-1)\left(\frac{1+C_0}{q}\right)^{q/(q-1)}.
 \tag{E5.11}
\]
For absorption by a constant times \(r^{3/4}\), we need \(\tau\le3/4\). Solving \(2q\le3(q-1)\) gives \(q\ge3\). Equality at \(q=3\) is allowed by enlarging the damping constant; \(q>3\) gives a strictly smaller power. The choice \(q=4\) gives \(2/3\). At \(q=2\), the power is 1, so this particular damping argument fails. This does not prove that no other neighborhood or proof could work. Award 5 points for maximization, 5 for the envelope, and 5 for the threshold with its exact interpretation.

### Exercise 8. Extra coordinates and polynomial frequencies — 15 points

Starting with the six two-dimensional kernels and the normalized entire solution, extend them to \(\mathbb R^n\), \(n>2\). Prove that the normalization and empty common zero set survive. Then give the full differential argument excluding exponential polynomial solutions.

**Solution.** Set
\[
 \widetilde\mu_j=\mu_j\otimes\delta_0^{\otimes(n-2)},\qquad
 \widetilde U(w)=U(w_1,w_2).
 \tag{E5.12}
\]
The point distributions evaluate the extra variables at zero in the convolution pairing. Hence \(\widetilde\mu_j*\widetilde U=(\mu_j*U)(w_1,w_2)=0\), and \(\widetilde U(0)=1\). The extended transforms are \(h_j(z_1,z_2)\), independent of the extra coordinates. An empty common zero set in the first two coordinates stays empty.

Suppose a nonzero exponential polynomial solution has distinct frequencies \(\zeta_1,\ldots,\zeta_s\). Choose a real vector \(v\) such that the numbers \(v\cdot\zeta_j\) are distinct. For each unequal pair, the forbidden real vectors lie in the kernel of a nonzero real linear form, obtained from a nonzero real or imaginary part of their difference. The product of these finitely many linear forms is a nonzero real polynomial. Such a polynomial cannot vanish on all real space: induction on the number of variables reduces this assertion to the root bound for a one-variable polynomial. Therefore an allowed \(v\) exists.

Select a term \(p_j(x)e^{ix\cdot\zeta_j}\) with \(p_j\ne0\). Apply
\[
 T_j=\prod_{\ell\ne j}
       (v\cdot D-v\cdot\zeta_\ell)^{\deg p_\ell+1}.
 \tag{E5.13}
\]
On each other frequency, its matching factor acts as a degree-lowering derivative and kills the polynomial. On the selected frequency, each factor acts on its polynomial as the nonzero scalar \(v\cdot(\zeta_j-\zeta_\ell)\) plus a degree-lowering derivative. The highest homogeneous part is multiplied by nonzero scalars, so the result is still nonzero. Choose a highest total-degree monomial \(x^\gamma\) in the remaining polynomial. Applying \((D-\zeta_j)^\gamma\) kills every other monomial of that total degree, kills all smaller degrees, and sends the chosen monomial to the nonzero constant \((-i)^{|\gamma|}\gamma!\) times its coefficient. Thus a nonzero exponential solution results. All these differential operators commute with compact convolution, so it would still solve the system. The empty common zero set excludes it. Award 4 points for the extension and normalization, 3 for the zero set and separating direction, 5 for differential isolation, and 3 for reduction to an exponential and the contradiction.

## References

- Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1, the exact compact-support Fourier theorem and uniqueness.
- Solving the Cauchy–Riemann equations with a weight, Theorem W2, weighted existence with its full proof.
- Zero-free cones turn slow decrease into reciprocal bounds, Proposition 5.1, comparison with a geometrically spaced sinc product.
- D. I. Gurevich, *Counterexamples to a problem of L. Schwartz*, Functional Analysis and Its Applications 9 (1975), 116–120. [Original publication](https://www.mathnet.ru/eng/faa2235). Credit for the counterexample, the entire-graph construction and the six-generator idea. The complete proof and the exact linked lessons supply the required arguments.
