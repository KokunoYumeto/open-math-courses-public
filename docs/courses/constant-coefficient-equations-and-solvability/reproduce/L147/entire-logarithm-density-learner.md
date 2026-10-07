# Entire logarithms: convergence, correction and interpolation

*Original learner exposition, examples and solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

An entire function may have zeros, so its logarithmic modulus may have deep negative holes. Nevertheless, normalized logarithms of entire scalar functions approximate every proper plurisubharmonic function in local integral norm. This lesson builds the approximation rather than assuming that complex analyticity follows from a favorable norm estimate. A weighted solution removes the Cauchy–Riemann error of finitely many local seeds; a second estimate makes its correction small at the selected centers.

Read the [complete original proof](entire-logarithm-density-formal.md). Its actual preceding inputs are [L143, full local compactness](../../AN02-L143.html#HC1), [L131, the signed Newtonian kernel](../../AN02-L131.html#NP4), [L140, positive PSH smoothing](../../AN02-L140.html#UE2), and [L144, strict weighted existence](../../AN02-L144.html#strict-weighted-existence). Every new convergence and interpolation step is written in the companion.

## 1. The density statement uses local integral norm

For a positive integer \(N\) and an entire function \(f\not\equiv0\), form \(N^{-1}\log|f|\), with \(\log0=-\infty\). [Theorem GD1](entire-logarithm-density-formal.md#entire-logarithm-density-theorem) states that these functions are dense among proper PSH local-integral classes:

\[
\int_K\left|N_j^{-1}\log|f_j|-\phi\right|dV\longrightarrow0
\quad\text{for every compact }K\subset\mathbb C^n.
\tag{L147.1}
\]

The functions are scalar entire functions, not a growing vector of holomorphic components. Zeros are allowed. A proper PSH function can have singular minus-infinite values and is still locally integrable; the everywhere minus-infinite function is not a class in this ambient space. The conclusion is not pointwise convergence at every point.

## 2. Two lemmas perform different jobs

The [dense-set lemma](entire-logarithm-density-formal.md#dense-set-convergence-lemma) takes a finite continuous subharmonic comparison \(\phi\), a sequence below it, and convergence at every point of a dense set. It gives full local \(L^1\) convergence. The bound is \(\phi_j\leq\phi\); it is not a requirement that all the functions be nonpositive.

The [local Cauchy–Riemann estimate](entire-logarithm-density-formal.md#bounded-dbar-point-estimate) takes \(u\in L^2(B_r)\) and a distributional coefficient vector \(\bar\partial u\in L^\infty(B_r)\). It supplies a unique continuous representative and

\[
|u(0)|\leq C_n\left(
r\|\bar\partial u\|_\infty+r^{-n}\|u\|_2\right).
\tag{L147.2}
\]

The derivative data are bounded, rather than just square integrable. The exponent \(-n\) comes from taking a square root of the real-volume scaling \(r^{2n}\). The estimate concerns the continuous representative; a changed value at an isolated point of an \(L^2\) representative does not acquire a point estimate.

The proof uses \(\Delta E=\delta_0\). Its two pieces are a locally integrable kernel against bounded data, and a smooth kernel against square-integrable data supported away from the evaluation point. Those pieces explain both continuity and the two terms of (L147.2).

## 3. How the entire functions are built

First make the target smooth and strictly PSH with a global Levi lower bound \(\kappa_0>0\). At a chosen center \(a\), subtract a holomorphic quadratic Taylor polynomial \(P_a\). Its real part captures the pure holomorphic and antiholomorphic Taylor terms, leaving the positive mixed Levi term:

\[
\phi(z)-\operatorname{Re}P_a(z)
\geq\tfrac12\kappa_0|z-a|^2
\quad\text{near }a.
\tag{L147.3}
\]

At stage \(j\), take the first \(j\) distinct points of a dense set. Choose disjoint cutoff balls and cutoffs \(\chi_\nu\) equal to one near those points. The preliminary sum

\[
A_{j,N}=\sum_{\nu\leq j}\chi_\nu e^{NP_{a_\nu}}
\tag{L147.4}
\]

has the desired values at the centers but is not generally holomorphic. Its closed \(\bar\partial\) error lives on the cutoff annuli, where the positive gap makes its weighted modulus exponentially small in \(N\). Apply the actual weighted existence theorem with weight \(2N\phi\) to obtain a correction \(v\), then use (L147.2) and small weight oscillation on fixed small balls to prove

\[
\bar\partial v=\bar\partial A_{j,N},\qquad
|v(z)|\leq Q_j e^{-c_jN/2}e^{N\phi(z)}
\quad(|z|\leq j).
\tag{L147.5}
\]

Both positive \(c_j\) and finite \(Q_j\) depend on the stage but are fixed while \(N\) grows. Choose an integer \(N_j\) with the coefficient in this bound strictly less than \(1/3\), and set \(f_j=(3/4)(A_{j,N_j}-v)\). The correction is continuous and the difference has zero \(\bar\partial\), so the proved joint regularity step makes it an entire function with those same pointwise values. Disjointness and the margins give

\[
|f_j(z)|\leq e^{N_j\phi(z)}\quad(|z|<j),
\qquad |f_j(a_\nu)|>\tfrac12e^{N_j\phi(a_\nu)}
\quad(\nu\leq j).
\tag{L147.6}
\]

The entire function is nonzero. Its normalized log is below the target on each eventually reached observation ball and converges to the target at every fixed dense center. The dense-set lemma completes this part. Radial smoothing plus \(\varepsilon|z|^2\), followed by a second diagonal selection, handles any proper PSH target. The full proof also establishes that the closure cannot contain any other local-integral classes.

## 4. Four worked examples

### Worked example 1. A pluriharmonic target already is an entire logarithm

Let \(q\) be entire and \(\phi=\operatorname{Re}q\). For every positive integer \(N\), take \(f_N=e^{Nq}\). It is entire and zero-free, and

\[
N^{-1}\log|f_N|=\operatorname{Re}q=\phi
\quad\text{everywhere}.
\tag{L147.7}
\]

For example \(q(z)=z^2-2z\) gives \(\phi(x+iy)=x^2-y^2-2x\), which can be negative. Its Levi matrix is zero. Thus the density theorem does not require the original target to be strictly PSH; strictness is a device in the general construction, introduced after smoothing.

### Worked example 2. Moving zeros and an exact error

In one variable choose

\[
\phi(z)=\max(0,\log|z|),\quad
f_N(z)=\frac{1+z^N}{2},\quad
w_N=N^{-1}\log|f_N|.
\tag{L147.8}
\]

The target is continuous and PSH. The triangle inequality gives \(w_N\leq\phi\). On \(|z|<1\), \(z^N\to0\), so \(w_N\to0\); on \(|z|>1\), factor \(z^N\) to obtain \(w_N\to\log|z|\). This proves dense-set convergence, and the lemma gives local \(L^1\) convergence.

The circle average can be calculated. For \(r<1\), expand \(\log(1+r^Ne^{iN\theta})\) as its uniformly convergent analytic series. Every term has zero average. For \(r>1\), factor the leading term and use the same series with \(r^{-N}\). Thus for \(r\ne1\),

\[
\frac1{2\pi}\int_0^{2\pi}w_N(re^{i\theta})d\theta
=\max(0,\log r)-\frac{\log2}{N}.
\tag{L147.9}
\]

Since the error is nonnegative, polar integration and Tonelli give the **exact** disk error

\[
\int_{|z|<R}|w_N-\phi|dA
=\frac{\pi R^2\log2}{N}.
\tag{L147.10}
\]

The radius \(r=1\) has zero radial measure, so its singular angles do not affect this computation. Local integrability of the proper logarithms is proved in GD4. Yet at the fixed point \(-1\), odd \(N\) gives \(w_N(-1)=-\infty\), while even \(N\) gives zero. Pointwise convergence fails there. For \(N=13\) the 13 simple zeros are \(e^{(2k+1)\pi i/13}\), and one is exactly \(-1\).

![Polynomial zeros and the exact local integral error](figures/circle-zeros-and-integral-convergence.png)

The error curve is a volume-integral quantity. It does not claim that values at the plotted zeros converge. This explicit family proves the general lesson's distinction between integral and pointwise convergence.

### Worked example 3. The scaling and the need for derivative data

In complex dimension one take \(u(z)=A+B\overline z\) on \(B_r\). Then \(\bar\partial u=B\), \(u(0)=A\), and integrating the circle cross term gives

\[
\|u\|_{L^2(B_r)}^2
=\pi r^2|A|^2+\tfrac\pi2r^4|B|^2.
\tag{L147.11}
\]

Hence the norm term in (L147.2) is \(\sqrt\pi\sqrt{|A|^2+r^2|B|^2/2}\), while the derivative term is \(r|B|\). Both have the dimensions of the point value. Already the constant function \(A\) shows that any valid dimension-one constant is at least \(1/\sqrt\pi\).

An \(L^2\) norm alone cannot control a point value for this class of functions. Take a fixed smooth bump \(\beta\) supported in \(B_1\), with \(\beta(0)=1\), and let \(u_\varepsilon(z)=\beta(z/\varepsilon)\) in \(B_1\), \(0<\varepsilon<1\). Then

\[
u_\varepsilon(0)=1,\quad
\|u_\varepsilon\|_2=\varepsilon^n\|\beta\|_2,
\quad \|\bar\partial u_\varepsilon\|_\infty
=\varepsilon^{-1}\|\bar\partial\beta\|_\infty.
\tag{L147.12}
\]

Every member has bounded derivative data, but those bounds are not uniform as the bump shrinks. The derivative term in the lemma records precisely this missing control.

### Worked example 4. Two actual quadratic seeds and their closed error

Use \(\phi(z)=|z|^2\), with \(\kappa_0=1\), and centers \(a=-1/2,1/2\). The Taylor polynomial and gap are exactly

\[
P_a(z)=2\overline a z-|a|^2,
\qquad \phi(z)-\operatorname{Re}P_a(z)=|z-a|^2.
\tag{L147.13}
\]

Choose radius \(\rho=1/4\), so the two center balls are disjoint. A smooth radial cutoff \(\chi_a\) equals one for distance at most \(1/12\), and zero for distance at least \(1/6\). Writing \(s=|z-a|\), the normalized seed modulus and actual weighted error modulus are

\[
|e^{NP_a}|e^{-N\phi}=e^{-Ns^2},\qquad
|\bar\partial\chi_a\,e^{NP_a}|e^{-N\phi}
=\tfrac12|\chi'(s)|e^{-Ns^2}.
\tag{L147.14}
\]

Only the annulus between \(1/12\) and \(1/6\) contributes to the error. There is no joining-circle derivative atom because the chosen cutoff is smooth and flat at both joins. The two contributions have disjoint supports. Their total weighted squared error norm is

\[
I_N=\pi\int_{1/12}^{1/6}s\,|\chi'(s)|^2e^{-2Ns^2}\,ds.
\tag{L147.15}
\]

The factor combines two centers, angular measure \(2\pi\), and the squared coefficient factor \(1/4\). The strict theorem with weight \(2N|z|^2\) gives an actual correction whose weighted squared norm is at most \(I_N/(2N)\). This is a bound on an existing correction, not a formula for its values or a claim that the bound is attained.

![The exact seed geometry and actual weighted cutoff error](figures/quadratic-seeds-and-closed-error.png)

The plot uses the displayed radial smooth cutoff and the actual error formula (L147.14). The entire interpolation theorem additionally needs the point estimate and the one-third margin; an error-norm plot does not replace them.

## 5. Ten graded exercises

1. **Foundational: scaling.** For \(U(w)=u(rw)\), derive both norm transformations used in (L147.2), including the real-volume factor.
2. **Foundational: the exact kernel identity.** Derive (GD10) in distributions and explain why changing the fundamental-solution sign without changing the identity would be wrong.
3. **Intermediate: continuity.** Prove why the convolution with bounded compact data is continuous and why the cutoff-derivative contribution is smooth near the center, even if the original \(u\) is only in \(L^2\).
4. **Intermediate: dense-set convergence.** Explain how a dense finite seed excludes compact collapse and how the remaining limit is identified everywhere, rather than only on the dense set.
5. **Intermediate: the Taylor coefficients.** For \(\phi(z)=|z|^2+\operatorname{Re}(z^2)\) and a real center \(a\), compute \(P_a\), its gap and the least Levi eigenvalue. Verify the factors in the general formula.
6. **Intermediate: cutoff disjointness.** Explain exactly where disjoint supports are used to obtain the one-sided seed bound and the center values. State what bound the triangle inequality would give for unrestricted overlap.
7. **Advanced: scaled curvature.** Starting from the weighted error bound \(\|g e^{-N\phi}\|_2\leq B e^{-cN}\), derive the correction estimate using the weight \(2N\phi\), retaining the exact curvature factor. Explain why no factor \(N\) appears in the cutoff error itself.
8. **Advanced: an exact integral.** Prove (L147.10) for every \(R>0\), including radii larger than one, and explain the failure of pointwise convergence at \(-1\).
9. **Advanced: the reverse inclusion.** Prove that a local \(L^1\) limit of proper PSH functions has locally uniform upper bounds along its approximating sequence and a proper PSH representative. Exclude compact collapse using the same norm evidence.
10. **Advanced: the second diagonal.** Give a precise expanding-ball choice of smooth strict weights and normalized entire logarithms that approximates a proper singular PSH target. Explain why the normalization integers can be made increasing.

## 6. Complete solutions

### Solution 1

The chain rule, also valid in distributions by changing variables in a compact test, gives \(\bar\partial_w U=r(\bar\partial_z u)(rw)\). Its coefficient-vector supremum is \(r\|\bar\partial u\|_\infty\). The real Jacobian in complex dimension \(n\) is \(r^{2n}\), so

\[
\|U\|_{L^2(B_1)}^2=r^{-2n}\|u\|_{L^2(B_r)}^2,
\qquad \|U\|_2=r^{-n}\|u\|_2.
\tag{L147.16}
\]

Applying the unit-ball point estimate to \(U(0)=u(0)\) gives the two terms of (L147.2). Replacing \(r^{-n}\) by \(r^{-2n}\) would forget the square root in the norm.

### Solution 2

The compact distribution \(\chi u\) obeys \(E*\Delta(\chi u)=(\Delta E)*(\chi u)=\delta_0*(\chi u)=\chi u\). The complex derivative identity is \(\Delta=4\sum_j\partial_j\bar\partial_j\). The product rule gives \(\bar\partial_j(\chi u)=\chi f_j+u\bar\partial_j\chi\). Move \(\partial_j\) onto the kernel in the convolution to obtain (GD10), with a plus sign and factor 4. For a kernel satisfying \(-\Delta E=\delta_0\), the first displayed recovery would instead have a minus sign. The actual NP4 convention is \(\Delta E=\delta_0\).

### Solution 3

The kernel vector has size proportional to \(|x|^{1-2n}\), which is locally integrable because its polar integral is proportional to \(\int_0^R1\,ds\). For compact bounded coefficient data, the difference of two convolution values is bounded by the data supremum times the local \(L^1\) translation difference of this kernel. Translation continuity follows by approximating the kernel on a slightly larger ball by a continuous integrable function, applying uniform translation continuity to the approximation, and bounding the two approximation errors in \(L^1\).

For \(u\bar\partial\chi\), its support is away from the center ball and its \(L^2\) norm is finite. It is also \(L^1\) on that compact support by Cauchy–Schwarz. The kernel and every derivative stay bounded there for centers in a smaller ball. Differentiation under the integral therefore gives a smooth function on that smaller ball. These pieces provide a continuous representative of the distributional identity; recentered balls and agreement on overlaps give continuity throughout the original open ball.

### Solution 4

Choose one dense-set point in a connected component. Its sequence values converge to a finite target value, so a subsequence collapsing to minus infinity uniformly on compact sets would contradict that fixed value. Compactness gives a further local \(L^1\) limit \(\psi\). The upper-limit comparison gives \(\phi\leq\psi\) at the dense points. The bound on the approximating sequence gives \(\psi\leq\phi\) almost everywhere and then everywhere by its submean inequality and continuity of \(\phi\).

For the remaining direction, \(\phi(x)\leq\) the ball average of \(\psi\) at dense centers. That average is continuous as the center moves, by translation continuity in local \(L^1\). Extend the inequality to every center, then shrink the ball; the canonical subharmonic values are recovered by submeans and upper semicontinuity. Thus \(\phi\leq\psi\) everywhere. All subsequential limits equal \(\phi\), giving full local \(L^1\) convergence. Finite component covers handle compact sets in a disconnected open domain.

### Solution 5

Here \(\phi_z=\overline z+z\), \(\phi_{zz}=1\), and \(\phi_{z\bar z}=1\). For real \(a\), its value is \(2a^2\), so

\[
P_a(z)=2a^2+4a(z-a)+(z-a)^2
=z^2+2az-a^2.
\tag{L147.17}
\]

Subtracting its real part from \(|z|^2+\operatorname{Re}z^2\) gives \(|z-a|^2\). The least Levi eigenvalue is 1. The mixed quadratic term is not included in the holomorphic seed; it is the positive gap. The factor 2 in the general linear term and the pure quadratic coefficient both give the formula above.

### Solution 6

At any point, disjoint supports allow at most one nonzero term. That term has cutoff at most one and exponential modulus at most the reference \(e^{N\phi}\), giving \(|A_{j,N}|\leq e^{N\phi}\). At a selected center, its own cutoff equals one and every other cutoff vanishes, giving exactly \(e^{N\phi(a_\nu)}\) before correction. With unrestricted overlap, the triangle inequality gives only \(j e^{N\phi}\), and other seeds might interfere with a center value. The fixed factor \(3/4\) and the stated margins cannot be justified by that weaker estimate. The construction chooses disjoint balls to obtain precisely the two facts it uses.

### Solution 7

The least Levi eigenvalue of \(2N\phi\) is \(2N\kappa_\phi\geq2N\kappa_0\). The strict weighted theorem therefore gives

\[
\int|v|^2e^{-2N\phi}
\leq\frac1{2N\kappa_0}\int|g|^2e^{-2N\phi}
\leq\frac{B^2}{2N\kappa_0}e^{-2cN}.
\tag{L147.18}
\]

Taking square roots yields \(\|v e^{-N\phi}\|_2\leq B(2N\kappa_0)^{-1/2}e^{-cN}\). The data are closed and their required curvature-weighted norm is finite, so every actual theorem hypothesis is met. The cutoff error is \((\bar\partial\chi)e^{NP}\); the other product-rule term is zero because \(P\) and \(e^{NP}\) are holomorphic. Differentiating in \(\bar z\) does not create an \(N\) factor here.

### Solution 8

For \(r<1\), the analytic logarithm series of \(1+r^N e^{iN\theta}\) converges uniformly, and every term has zero circle average. For \(r>1\), factor the leading power and apply that argument to \(r^{-N}\), adding \(N\log r\) before normalization. Dividing by 2 subtracts \(\log2/N\). This proves (L147.9) for all radii except one. The pointwise inequality \(w_N\leq\phi\) makes the absolute error equal \(\phi-w_N\), a nonnegative integrable function. Tonelli and polar coordinates therefore give

\[
\int_0^R 2\pi r\,\frac{\log2}{N}\,dr
=\frac{\pi R^2\log2}{N}.
\tag{L147.19}
\]

The omitted radius is a set of radial measure zero. The same formula holds beyond that radius, so there is no restriction \(R<1\). At \(-1\), odd \(N\) makes \(f_N=0\) and even \(N\) makes \(f_N=1\). Thus the normalized log alternates between minus infinity and zero there, despite the vanishing integral error.

### Solution 9

For any compact \(K\), choose a fixed small radius \(s\) so that all its center balls lie in a common compact neighborhood \(K_s\). Submeans give \(w_j(x)\leq |B_s|^{-1}\int_{K_s}|w_j|\). Local \(L^1\) convergence bounds the right side uniformly in \(j\), so the approximants have the required local upper bounds. Compact collapse would make their integrals on a fixed positive-volume ball tend to minus infinity, while their local absolute integrals are bounded; it is excluded. Actual PSH compactness supplies a proper PSH subsequential limit, and its PSH closure and strong-convergence assertions apply. That subsequential limit is the original local \(L^1\) limit almost everywhere by uniqueness of the integral-norm limit. Hence the original class has that proper representative. A sequence of constants tending to minus infinity does not contradict the assertion, because it has no finite local \(L^1\) limit.

### Solution 10

Smooth the proper locally integrable PSH target with a positive compact radial kernel and add \(\varepsilon|z|^2\). The resulting \(\phi_\varepsilon\) is smooth PSH with least Levi eigenvalue at least \(\varepsilon\) everywhere, and tends to \(\phi\) in local \(L^1\). At stage \(j\), choose \(\varepsilon_j\) so its integral error on \(B_j\) is below \(1/(2j)\). The smooth strict construction gives a sequence of normalized nonzero entire logarithms converging to that \(\phi_{\varepsilon_j}\). Choose one whose error on \(B_j\) is below \(1/(2j)\), and whose positive normalization integer exceeds the preceding selected integer; this is possible because those construction integers tend to infinity. The selected logarithm has error below \(1/j\) against \(\phi\) on \(B_j\). Every compact set lies in these balls eventually, proving the required local convergence with increasing integers. This argument works even where the target has minus-infinite singular values, since all comparisons use its locally integrable class.

## 7. Exact source and scope

Human scholarly source: Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.1, Theorem 15.1.6 and Lemmas 15.1.7–15.1.8, printed pp. 277–278. The formal companion compares the actual hypotheses and proof inputs. The source's remark that the density theorem is unused later does not remove it from the assigned target list. All examples, solutions, derivations and figures are original. Protected native pages stay private. The remaining assigned weighted Fourier and division targets, topology, and other course coverage still require completion.
