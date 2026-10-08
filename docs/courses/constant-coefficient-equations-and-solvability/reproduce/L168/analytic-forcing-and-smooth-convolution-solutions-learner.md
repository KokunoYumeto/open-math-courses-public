# Analytic forcing and smooth convolution solutions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An analytic right-hand side can be solved against every nonzero compact convolution kernel on a convex domain. A kernel may have characteristic zeros or may smooth away singularities. We explain why neither phenomenon prevents smooth solvability for analytic forcing. We then work through reflection, resonance, a compact smooth kernel, and growth near a boundary.

Basic references are [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's tempered-distribution notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. Read Exponential-polynomial solutions and convex approximation for the exact homogeneous approximation and Gaussian localization theorems. Fourier transforms of analytic functionals on a real convex carrier supplies the analytic-functional transform and germ results. The full proof below also identifies the required Baire, Hahn–Banach and endpoint Lebesgue-duality statements.

## 1. A local equation on the correct domain

Our convention is
\[
 (\mu*u)(x)=\mu_y(u(x-y)),\qquad
 X_\mu=\{x:x-\operatorname{supp}\mu\subset X\}.
 \tag{L1}
\]
For \(0\ne\mu\in\mathcal E'(\mathbb R^n)\), an open convex \(X\), and every real-analytic \(f\) on \(X_\mu\), there is a smooth \(u\) on \(X\) satisfying \(\mu*u=f\) on \(X_\mu\). “Real analytic” allows complex values. The input need not extend to an entire function. The output is smooth; no analytic regularity or global boundedness is asserted.

If \(X_\mu\) is empty, the equation has no points at which it must hold, and \(u=0\) suffices. A nonempty \(X\) can still have empty \(X_\mu\): the translations demanded by the entire support of the kernel may not fit.

The construction has two scales. On every smaller convex domain \(Y\) with compact closure inside \(X\), a transpose estimate gives a globally defined bounded smooth solution of the equation on \(Y_\mu\). On successively larger \(Y\), homogeneous exponential-polynomial corrections make the local solutions converge on every compact subset of \(X\). Their global bounds need not stay uniform.

## 2. What makes the estimate uniform

Fix a nonzero compact smooth \(\psi\). Put
\[
 \rho=\check\mu*\psi,\quad A=F_\rho,\quad
 L=\operatorname{conv}\operatorname{supp}\rho,\quad
 D=\overline{Y_\mu}.
 \tag{L2}
\]
The norm in the full proof is
\[
 \|\Phi\|=\sup_{\zeta\in\mathbb C^n}
 |A(\zeta)\Phi(\zeta)|
 e^{-H_L(\operatorname{Im}\zeta)-H_D(\operatorname{Im}\zeta)} .
 \tag{L3}
\]
Zeros of \(A\) do not make this norm degenerate. A nonzero entire multiplier is nonzero on some open set, and holomorphic identity then determines the entire quotient everywhere. More strongly, Cauchy's formula on a suitable translated circle bounds each quotient on a compact set by its product on a larger compact set. This proves completeness of the space in (L3).

The convex quotient theorem places the analytic functional associated to \(\Phi\) on the real carrier \(D\). Its polynomial moments are
\[
 v_\Phi(P)=P(i\partial_\zeta)\Phi(0).
 \tag{L4}
\]
Every individual functional has a local holomorphic supremum bound. Baire's theorem in the complete quotient space turns those separate bounds into one bound valid for every \(\Phi\). Gaussian approximation in a fixed complex neighborhood then allows evaluation on \(f\), even when \(f\) is not entire.

For an actual test \(\phi\) in \(Y_\mu\), this gives
\[
 \left|\int f\phi\right|
 \le C\sup_K|\widetilde f|\,
                 \|\check\mu*\psi*\phi\|_1 .
 \tag{L5}
\]
The test support and its derivative order do not change \(C\). Hahn–Banach extends the functional on these smoothed tests to \(L^1\). Its bounded representing function \(v\) yields
\[
 U=v*\check\psi,\qquad
 \|\partial^\alpha U\|_\infty
 \le \|v\|_\infty\|\partial^\alpha\psi\|_1 .
 \tag{L6}
\]
The two reflections have different roles: \(\check\mu\) enters the test, and \(\check\psi\) enters the solution. The full proof checks both transposes.

## 3. Four worked examples

### Example 1: a translated derivative

Take \(a=3/4\), \(X=(-2,2)\), \(\mu=\delta'_a\), and \(f(x)=e^{2x}\). By the distributional derivative convention,
\[
 (\delta'_a*u)(x)
 =-\left.\frac{d}{dy}u(x-y)\right|_{y=a}
 =u'(x-a).
 \tag{L7}
\]
Here \(X_\mu=X+a=(-5/4,11/4)\). Set
\[
 u(t)=\frac12e^{2(t+a)}.
 \tag{L8}
\]
Then \(u'(x-a)=e^{2x}=f(x)\) throughout \(X_\mu\). Both the plus sign and the translation by \(+a\) in (L8) matter. Every constant can be added to \(u\).

### Example 2: a resonant averaging kernel

Let \(\mu\) have density \(1/2\) on \([-1,1]\), take \(X=(-3,3)\), and let \(f(x)=\cos(\pi x)\) on \(X_\mu=(-2,2)\). For a complex parameter \(\lambda\),
\[
 \mu*e^{\lambda x}=b(\lambda)e^{\lambda x},\qquad
 b(\lambda)=\frac{\sinh\lambda}{\lambda},\quad b(0)=1.
 \tag{L9}
\]
This follows by directly integrating \(e^{-\lambda y}/2\) over \([-1,1]\). At \(\lambda=i\pi\), \(b=0\), so a constant multiple of \(e^{i\pi x}\) cannot produce that forcing. Differentiate the integral identity with respect to \(\lambda\):
\[
 \mu*(xe^{\lambda x})
     =[b'(\lambda)+xb(\lambda)]e^{\lambda x}.
 \tag{L10}
\]
Since \(b'(i\pi)=i/\pi\), the function \(-i\pi xe^{i\pi x}\) produces \(e^{i\pi x}\). Taking real parts gives the real smooth solution
\[
 u(x)=\pi x\sin(\pi x),\qquad
 \frac12\int_{-1}^{1}u(x-y)\,dy=\cos(\pi x).
 \tag{L11}
\]
Resonance adds a polynomial factor; it does not obstruct this analytic right-hand side.

![The resonant averaging solution and its exact averaged output on the eroded interval](figures/resonant-averaging-solution.png)

The curve \(u(x)=\pi x\sin(\pi x)\) is defined on \(X=(-3,3)\). Its average is the lower-amplitude curve \(f(x)=\cos(\pi x)\) on \(X_\mu=(-2,2)\). The marked points \(x=\pm2\) are excluded boundary points. Formula (L11), not the sampled curves, proves the identity. The editable figure source accompanies the illustration.

### Example 3: a compact smooth kernel

Let
\[
 \beta(y)=
 \begin{cases}
 e^{-1/(1-y^2)},&|y|<1,\\
 0,&|y|\ge1,
 \end{cases}
 \quad Z=\int_{-1}^{1}\beta(y)\,dy,\quad
 d\mu(y)=Z^{-1}\beta(y)\,dy .
 \tag{L12}
\]
Every derivative of the inside expression is an exponential times a rational function whose only singular factors are powers of \(1-y^2\). As \(y\to\pm1\), \(e^{-1/(1-y^2)}(1-y^2)^{-m}\to0\) for each \(m\), by the exponential series or repeated elementary comparison. Thus all derivatives extend by zero, and \(\beta\in C_c^\infty\). Also \(Z>0\).

For \(f(x)=e^{2x}\) on the full real line, define
\[
 c=Z^{-1}\int_{-1}^{1}\beta(y)e^{-2y}\,dy
   =Z^{-1}\int_{-1}^{1}\beta(y)\cosh(2y)\,dy>1.
 \tag{L13}
\]
Evenness gives the second equality. The strict inequality follows because \(\cosh(2y)>1\) away from zero and \(\beta>0\) throughout \((-1,1)\). Then \(u(x)=e^{2x}/c\) is an entire solution by direct integration.

This kernel erases a compact singularity: \(\mu*\delta_0=\mu\) is smooth, whereas \(\delta_0\) is not a smooth distribution. The last claim follows, for example, by testing smooth bumps of height one whose supports shrink to zero: \(\delta_0\) takes value one, whereas a locally bounded smooth density has integrals tending to zero. Nevertheless the analytic forcing above is solvable. Its solution is unbounded on the line, which is allowed by the global theorem.

### Example 4: analytic forcing near a boundary

Take \(X=(-2,2)\), \(\mu=\delta_0-\delta_1\), and \(f(x)=1/(2-x)\). Then \(X_\mu=(-1,2)\). The forcing is analytic on this interval and becomes unbounded as \(x\uparrow2\).

Choose a smooth \(h\) with \(h(t)=0\) for \(t\le-7/4\) and \(h(t)=1\) for \(t\ge-5/4\). One explicit choice is
\[
 B(s)=
 \begin{cases}e^{-1/s},&s>0,\\0,&s\le0,\end{cases}
 \qquad
 h(t)=\frac{B(t+7/4)}{B(t+7/4)+B(-5/4-t)}.
 \tag{L14}
\]
The denominator is positive everywhere, and the same flat-exponential argument as in Example 3 proves smoothness. On \(X\), set
\[
 u(x)=\sum_{k=0}^{3}\frac{h(x-k)}{2-x+k}.
 \tag{L15}
\]
All denominators are positive for \(x<2\), so \(u\) is smooth on \(X\). Subtracting the same sum at \(x-1\) telescopes:
\[
 u(x)-u(x-1)=\frac{h(x)}{2-x}
       -\frac{h(x-4)}{6-x}=\frac1{2-x}
             \quad(-1<x<2).
 \tag{L16}
\]
Indeed \(h(x)=1\) for \(x>-1\), and \(h(x-4)=0\) for \(x<2\). This example needs no control at the excluded endpoint \(x=2\). It also shows why bounded local solutions need not give a bounded solution on the whole domain.

## 4. How the local solutions become compatible

Choose bounded convex \(Y_j\) with compact closure \(K_j\), \(K_j\subset Y_{j+1}\), and union \(X\). Let \(Z_j=(Y_j)_\mu\). Their closures fit inside the next \(Z_j\), and their union is \(X_\mu\). Compactness of the entire translated kernel support proves that union assertion.

Take local global smooth solutions \(V_j\). The difference \(V_j-u_{j-1}\) solves the homogeneous equation on \(Z_{j-1}\). Approximate it on \(K_{j-2}\), through derivative order \(j\), by a global homogeneous exponential-polynomial \(h_j\). Then \(u_j=V_j-h_j\) still solves the equation on \(Z_j\), and
\[
 \max_{|\alpha|\le j}\sup_{K_{j-2}}
       |\partial^\alpha(u_j-u_{j-1})|<2^{-j}.
 \tag{L17}
\]
The two-index separation ensures that the approximation compact set is inside the domain on which the difference is homogeneous. Every fixed compact set and derivative order eventually fit these bounds. Summing the geometric tail proves convergence in every smooth seminorm. Convolution with the fixed compact distribution is continuous for those seminorms, so the limit solves the equation throughout \(X_\mu\).

![Nested source intervals and their eroded equation domains, with strict compact margins](figures/convex-exhaustion-and-eroded-domains.png)

Here \(X=(-4,4)\), \(\operatorname{supp}\mu=\{0,2\}\), \(Y_j=(-4+1/(j+1),4-1/(j+1))\), and \(Z_j=(-2+1/(j+1),4-1/(j+1))\), for \(j=1,2,3,4\). Open circles mark every excluded endpoint. The compact closure of each interval is strictly inside the next interval of the same type. These intervals illustrate the nesting used in the proof; no local solution is identified with an interval.

## 5. Exercises and full solutions

The ten exercises total 100 points. Each solution includes the argument required for its conclusion.

**Exercise 1 (10 points; introductory).** For \(X=(-3,5)\), \(\mu=\delta''_{-1/2}\), and \(f(x)=e^{3x}\), determine \(X_\mu\), the sign of \(\mu*u\), and one solution. Describe the homogeneous freedom for this kernel.

*Solution.* The support is \(\{-1/2\}\), so \(X_\mu=X-1/2=(-7/2,9/2)\). Two distributional derivatives give
\[
 (\delta''_{-1/2}*u)(x)=
 \left.\partial_y^2u(x-y)\right|_{y=-1/2}
 =u''(x+1/2).
 \tag{S1}
\]
The two chain-rule minus signs cancel. Taking \(u(t)=e^{3(t-1/2)}/9\) gives \(u''(x+1/2)=e^{3x}\). The difference of any two smooth solutions has second derivative zero on all of \(X\), because \(x+1/2\) ranges through \(X\). Its derivative is constant by the fundamental theorem of calculus, so the difference is affine. Every affine addition indeed leaves the equation unchanged.

**Exercise 2 (10 points; intermediate).** Let the uniform averaging kernel of Example 2 be convolved with itself, and call the resulting kernel \(\nu\). Find a real solution of \(\nu*u=\cos(\pi x)\), and verify why the linear prefactor from Example 2 is insufficient.

*Solution.* Its exponential multiplier is \(c(\lambda)=b(\lambda)^2\), where \(b(\lambda)=\sinh\lambda/\lambda\). At \(\lambda_0=i\pi\), \(b=0\), \(b'=i/\pi\). Thus \(c(\lambda_0)=c'(\lambda_0)=0\) and
\[
 c''(\lambda_0)=2b'(\lambda_0)^2=-2/\pi^2.
 \tag{S2}
\]
Twice differentiating \(\nu*e^{\lambda x}=c(\lambda)e^{\lambda x}\) gives
\(\nu*(x^2e^{\lambda_0x})=c''(\lambda_0)e^{\lambda_0x}\).
Consequently
\[
 u(x)=-\frac{\pi^2}{2}x^2\cos(\pi x)
 \tag{S3}
\]
solves the real equation. The transform calculation is justified by parameter differentiation over the compact kernel support. For every affine polynomial \(a+dx\), convolution of \((a+dx)e^{\lambda_0x}\) is zero because both \(c\) and \(c'\) vanish. A degree-one prefactor therefore cannot produce the nonzero forcing. On a chosen open domain the equation is asserted only where the support \([-2,2]\) fits.

**Exercise 3 (8 points; introductory).** Let \(Y=(-7/3,5/2)\) and let the kernel support be \(\{-2/3,4/3\}\). Determine \(Y_\mu\) and its closure. If \(\overline Y\subset X\), prove that this closure is a compact subset of \(X_\mu\).

*Solution.* The two conditions are \(x+2/3\in Y\) and \(x-4/3\in Y\). Their intervals are \((-3,11/6)\) and \((-1,23/6)\), respectively, so
\[
 Y_\mu=(-1,11/6),\qquad D=[-1,11/6].
 \tag{S4}
\]
For every \(x\in D\), both \(x+2/3\) and \(x-4/3\) are in \(\overline Y\), hence in \(X\). Thus \(D\subset X_\mu\). It is closed and bounded, hence compact. Since \(X_\mu\) is open by the compact-support argument, compactness gives a positive neighborhood of \(D\) inside \(X_\mu\). The endpoints of \(D\) do not belong to \(Y_\mu\); using the closure does not change the domain where the local equation is asserted.

**Exercise 4 (10 points; advanced).** Explain why a norm-Cauchy sequence for (L3) converges as entire quotients, even when \(A\) vanishes at zero. Identify what fails if \(A\equiv0\).

*Solution.* Choose a direction \(\theta\) at each center for which the first nonzero Taylor term of \(A\) does not vanish. A circle in that complex line avoids the isolated zeros of \(A\), and its positive minimum persists for nearby centers. Cauchy's formula bounds the quotient there by its product on the circle. A finite cover proves \(\sup_Q|\Phi|\le C_Q\|\Phi\|\) on every compact \(Q\), including those containing zeros of \(A\).

A norm-Cauchy sequence is therefore uniformly Cauchy on each compact. Cauchy's integral formula on slightly larger polydisks gives convergence of all derivatives and ensures that the limit is entire. Fixing \(\zeta\), passing to the limit in the original weighted inequality for \(\Phi_j-\Phi_k\), and then taking the supremum proves convergence in the norm itself. Its limit has finite norm by the triangle inequality with one term of the sequence. If \(A\equiv0\), every entire function has displayed value zero; it is not a norm, the nonzero Taylor direction does not exist, and none of these quotient estimates follows.

**Exercise 5 (8 points; intermediate).** Let \(\Phi(\zeta_1,\zeta_2)=e^{-i(2\zeta_1-\zeta_2/3)}\). Compute the moment \(v_\Phi(x_1^2x_2)\) using (L4), and verify it by identifying the carrier.

*Solution.* Here \(P(i\partial)=(i\partial_1)^2(i\partial_2)\). The exponential derivatives multiply by \(-2i,-2i,i/3\), respectively, so
\[
 i^3(-2i)^2(i/3)=-4/3.
 \tag{S5}
\]
The function \(\Phi\) is the transform of the point mass at \((2,-1/3)\). Its moment is \(2^2(-1/3)=-4/3\), agreeing with the derivative result. Omitting \(i^{|\alpha|}\) would give a different, imaginary answer.

**Exercise 6 (10 points; advanced).** In the Baire argument suppose \(B(\Phi_0,r)\subset\mathcal C_m\). Prove the bound \(4m/r\) for all polynomial moments, including \(\Phi=0\), and explain why the polynomial space need not be complete.

*Solution.* For \(\|h\|<r\), both \(\Phi_0+h\) and \(\Phi_0\) satisfy the defining moment bound. Subtract them and use the triangle inequality to get \(|v_h(P)|\le2m\sup_K|P|\). For \(\Phi\ne0\), the choice \(h=r\Phi/(2\|\Phi\|)\) is inside that ball difference. Linearity gives
\[
 |v_\Phi(P)|\le (4m/r)\|\Phi\|\sup_K|P|.
 \tag{S6}
\]
For \(\Phi=0\), all its moments vanish by (L4). The sets \(\mathcal C_m\) are closed subsets of the complete quotient space, and their union covers that space by individual analytic-functional bounds. Baire uses precisely that completeness. Polynomials merely index the closed moment inequalities; their own norm completion is not used.

**Exercise 7 (10 points; intermediate).** Starting from \(T(q)=\int vq\), prove both convolution transposes in (4.12) and the reflected smoothing \(U=v*\check\psi\). Show the difference between \(v*\check\psi\) and \(v*\psi\) on the bounded function \(v(t)=e^{it}\).

*Solution.* By definition,
\((v*\check\psi)(x)=\int v(t)\psi(t-x)\,dt\).
Pair it with \(\check\mu*\phi\), change the order of the absolutely integrable compact-kernel integral, and obtain
\[
 \int U(x)(\check\mu*\phi)(x)\,dx
 =\int v(t)\left[\int\psi(t-x)(\check\mu*\phi)(x)\,dx\right]dt
 =\int v(t)(\psi*\check\mu*\phi)(t)\,dt.
 \tag{S7}
\]
The first transpose is \(\langle\mu*U,\phi\rangle=\langle U,\check\mu*\phi\rangle\), obtained by changing \(x-y\) to the new \(x\) in the compact-distribution pairing. Finite order justifies that change using the corresponding finitely many smooth derivatives of the compact tests.

For \(v(t)=e^{it}\), (S7)'s reflected smoothing is
\((v*\check\psi)(x)=e^{ix}F_\psi(-1)\); unreflected smoothing is
\((v*\psi)(x)=e^{ix}F_\psi(1)\).
These need not agree. For example take a nonnegative even compact smooth bump \(\beta\) supported in \((-1/4,1/4)\), not zero, and \(\psi(t)=\beta(t-\pi/2)\). Its real \(F_\beta(1)>0\), since \(\cos t>0\) on the support. Then \(F_\psi(1)=-iF_\beta(1)\), whereas \(F_\psi(-1)=iF_\beta(1)\). The two smoothings are opposite nonzero functions. No evenness of \(\psi\) is assumed in the theorem.

**Exercise 8 (8 points; intermediate).** Give a numerical tail bound from (L17). If all relevant compact and derivative conditions hold for \(j\ge12\), bound the distance between \(u_{11}\) and the limit in that smooth seminorm. Explain the use of \(K_{j-2}\).

*Solution.* Sum the inequalities over \(j=12,13,\ldots\):
\[
 \|u-u_{11}\|_{Q,m}\le\sum_{j=12}^{\infty}2^{-j}
           =2^{-11}=1/2048.
 \tag{S8}
\]
The difference before correction is homogeneous on the domain \(Y_{j-1}\). Its approximation compact set must lie inside that domain. The inclusion \(K_{j-2}\subset Y_{j-1}\) guarantees this. The closed set \(K_{j-1}\) can touch the boundary of \(Y_{j-1}\), so replacing \(K_{j-2}\) by it is not justified by the stated approximation theorem. Every fixed compact eventually lies in \(K_{j-2}\), which makes the smaller index sufficient for full convergence.

**Exercise 9 (8 points; intermediate).** For the compact smooth probability kernel of Example 3, prove \(1<c<\cosh2\). Decide whether its smoothing of \(\delta_0\) prevents the analytic-forcing theorem from applying.

*Solution.* The kernel density is strictly positive in \((-1,1)\), normalized to integral one, and even. Therefore \(c\) is its average of \(\cosh(2y)\). This continuous function equals one only at zero and is strictly between one and \(\cosh2\) for \(0<|y|<1\). Integrating over an interval where the strict inequalities hold proves \(1<c<\cosh2\). The kernel is nonzero and compact, so the theorem applies. Its smoothing of a point mass shows that it does not preserve every singularity; the analytic-forcing theorem requires no such preservation. The explicitly verified solution \(e^{2x}/c\) confirms this distinction for the chosen forcing.

**Exercise 10 (18 points; advanced).** Explain why uniform entire approximation of \(f\) on the complex compact \(K\), rather than only smooth convergence on real \(D\), is used in the local estimate. Then verify the boundary solution of Example 4 and prove that no bounded \(u\) on \((-2,2)\) can solve that example.

*Solution.* For each \(\Phi\), the analytic functional has a supremum bound on a complex neighborhood of its carrier. Lemma 3.2 has the common bound on \(K\) for entire tests. Gaussian entire approximants converge uniformly to the local holomorphic extension \(\widetilde f\) on this very compact neighborhood. Continuity of the germ action permits their functional values to converge to \(v_\Phi(\widetilde f)\), while the uniform moment estimate yields \(|v_\Phi(\widetilde f)|\le C_K\|\Phi\|\sup_K|\widetilde f|\). Smooth convergence on the real carrier alone does not establish convergence in that holomorphic supremum topology. Analytic functionals can depend on arbitrarily high derivative information; their continuity has the precise complex-neighborhood hypothesis proved in the analytic-functional lesson.

For the explicit sum in (L15), subtract the sum with \(x\) replaced by \(x-1\). Relabel its index \(k+1\). The terms with indices \(1,2,3\) cancel, leaving exactly the two end terms in (L16). For \(-1<x<2\), their cutoff values are one and zero, respectively, so the difference is \(1/(2-x)\). All four denominators stay positive on \(X\), and the cutoff is smooth, so this is a smooth solution on the full domain. If another solution \(u\) were bounded by \(M\) throughout \(X\), then \(|u(x)-u(x-1)|\le2M\) on \(X_\mu=(-1,2)\). Its required value \(1/(2-x)\) tends to infinity as \(x\uparrow2\), a contradiction. Thus the global smooth conclusion cannot in general be strengthened to boundedness, even for this finite-support kernel.

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Introduction to Microlocal Analysis*, MIT, 2007, Chapter 1, “Tempered distributions and the Fourier transform,” freely readable [notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The full argument below provides the weighted quotient completeness, uniform analytic estimate, smooth transpose construction and convex-exhaustion convergence, with the precise earlier internal proofs linked in its introduction.
