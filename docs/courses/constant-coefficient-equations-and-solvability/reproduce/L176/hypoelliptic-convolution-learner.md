# Logarithmic zero retreat and reflected singularities

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI GPT-6.1 Sol (OpenAI). Public domain (CC0 1.0).*

For a differential operator, local regularity concerns the same spatial point on both sides of the equation. A convolution kernel can also translate that point. Its inverse must reverse the translation. More general compact kernels can have several singular points, and an inverse modulo smooth functions reflects their whole singular set.

Basic references are Gerd Grubb's [Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), Richard Melrose's [Differential Analysis](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. Read Slow decrease and entire Fourier division, Locating singularities through logarithmic Fourier strips, and Convolution modulo smooth functions and compact singularity bounds. The complete proof accompanying this chapter supplies the additional harmonic-profile and contour arguments.

## 1. How zeros can obstruct regularity

Use \(D=-i\partial\) and \(F(\zeta)=\langle\mu,e^{-ix\cdot\zeta}\rangle\). Every transform zero gives an exponential homogeneous solution:
\[
 \mu*e^{ix\cdot\zeta}=F(\zeta)e^{ix\cdot\zeta}=0.
 \tag{E1.1}
\]
The exponential itself is smooth. The obstruction comes from forming a distributional sum of such exponentials at escaping frequencies. When their imaginary parts are bounded by a fixed multiple of the logarithm of frequency, repeated integration by parts makes every compact test pairing bounded. Absolutely summable coefficients therefore give a distribution.

If every such solution were smooth, the closed graph theorem would bound its first derivative at a fixed point by the sum of its coefficient moduli. The one-term sums would then bound every complex frequency. This contradicts escape. That is why regularity requires
\[
 \frac{|\operatorname{Im}\zeta|}{\log|\zeta|}\longrightarrow+\infty
 \quad\text{along escaping zeros}.
 \tag{E1.2}
\]
The conclusion is about every fixed logarithmic width. A bound for only one width is insufficient.

There is a second requirement: the transform must be slowly decreasing. Otherwise the frequency-selective construction gives a compact nonsmooth input with smooth convolution. Combining slow decrease with (E1.2) defines hypoellipticity.

## 2. One exponent controls all widths

Let \(S=\operatorname{sing\,supp}\mu\). The complete proof shows that hypoellipticity is equivalent to
\[
 |F(\zeta)^{-1}|\le|\zeta|^B
       e^{H_S(-\operatorname{Im}\zeta)},\qquad
 |\operatorname{Im}\zeta|<m\log|\zeta|,\quad|\zeta|>C_m.
 \tag{E2.1}
\]
There is **one \(B\)** for every integer \(m\ge1\); the threshold \(C_m\) can change. The minus sign in the support function locates the inverse at the reflected spatial set.

To understand the common exponent, look at
\[
 L_c(z)=\frac{\log|F(c+z\log|c|)|}{\log|c|}.
 \tag{E2.2}
\]
Zero retreat makes this function harmonic on each fixed parameter ball once the center is sufficiently large. Slow decrease supplies a lower value at one nearby point. A positive harmonic comparison transfers that value to the center, with a constant independent of the later observation width.

Every limit becomes affine:
\[
 v(x+iy)=a\cdot y+b,\qquad a\in S,\qquad -A_0\le b\le N.
 \tag{E2.3}
\]
The spatial points \(a\) recovered from all profiles have closed union exactly \(S\). The contour construction uses \(B=A_0+1\).

On a neighborhood separated from \(-\operatorname{conv}S\), move the inverse integral to
\[
 \zeta(\xi)=\xi+it\theta\log(2+|\xi|^2).
 \tag{E2.4}
\]
If the separation gap is \(d>0\), the integrand after \(k\) spatial derivatives is bounded by a constant times
\[
 (1+|\xi|)^{B+k}(2+|\xi|^2)^{-td}.
 \tag{E2.5}
\]
The condition \(2td>B+k+n\) makes it integrable. Increasing \(t\) proves all derivative orders. Only the far-frequency part is moved; compact contour boundaries contribute smooth functions.

This gives a compact parametrix \(\nu\), meaning
\[
 \mu*\nu=\delta_0+r,\qquad r\in C_c^\infty.
 \tag{E2.6}
\]
Every global input satisfies
\[
 u=\nu*(\mu*u)-r*u.
 \tag{E2.7}
\]
The smooth compact factor \(r\) makes its convolution with any distribution smooth. Thus smooth forcing makes the input smooth.

The exact inverse singular set is stronger than its convex-hull bound. At high logarithmic frequencies,
\[
 L_\nu=-L_\mu+o(1).
 \tag{E2.8}
\]
Every singleton profile point \(a\) is replaced by \(-a\). The realization and nonconvex carrier theorems recover those closed unions, yielding
\[
 \operatorname{sing\,supp}\nu=-\operatorname{sing\,supp}\mu.
 \tag{E2.9}
\]
Subtracting a smooth solution for \(r\) produces a fundamental solution with the same exact singular set.

## 3. Four worked examples

### Example 1. A translated elliptic inverse

On the line let \(a=3/5\) and
\[
 \mu=(1-\partial_x^2)\delta_a,\qquad
 F(z)=(1+z^2)e^{-iaz},\qquad
 G_0(x)=\tfrac12e^{-|x|}.
 \tag{E3.1}
\]
The only transform zeros are \(i\) and \(-i\), so there is no escaping zero sequence. For real \(c\), \(|F(c)|=1+c^2\), which gives slow decrease.

The derivative of \(G_0\) jumps from \(1/2\) to \(-1/2\) at zero. Its ordinary second derivative off zero equals \(G_0\), while its distributional second derivative includes the jump:
\[
 G_0''=G_0-\delta_0,\qquad
 (1-\partial_x^2)G_0=\delta_0.
 \tag{E3.2}
\]
Consequently \(E(x)=G_0(x+a)\) satisfies \(\mu*E=\delta_0\). Its singularity is exactly at \(-a\); the derivative jump prevents smoothness there.

Choose a smooth compact cutoff \(\chi\) equal to one for \(|x|\le1\) and zero for \(|x|\ge2\). Then
\[
 \nu(x)=\chi(x+a)G_0(x+a)
 \tag{E3.3}
\]
is a compact parametrix with the same singular point. Direct differentiation gives
\[
 \mu*\nu=\delta_0+r,\qquad
 r(x)=-\chi''(x)G_0(x)-2\chi'(x)G_0'(x).
 \tag{E3.4}
\]
The error is smooth and supported in the two cutoff transition bands. The shifted argument in \(\nu\) becomes \(x\) after convolution with \(\delta_a\), explaining why \(r\) has no remaining \(a\).

### Example 2. Slow decrease with no logarithmic retreat

Take
\[
 \mu=\delta_{-1/2}+2\delta_{1/2},\qquad
 F(z)=e^{-iz/2}(e^{iz}+2).
 \tag{E3.5}
\]
On the real line the reverse triangle inequality gives \(|F(c)|\ge1\). Thus the kernel is slowly decreasing. Its complex zeros are exactly
\[
 z_j=(2j+1)\pi-i\log2,\qquad j\in\mathbb Z.
 \tag{E3.6}
\]
Their imaginary height is fixed, so (E1.2) fails.

There is an explicit nonsmooth homogeneous input:
\[
 u=\sum_{j\in\mathbb Z}(-2)^j\delta_j.
 \tag{E3.7}
\]
It is a distribution because the sum is locally finite. At the output point \(k+1/2\), the two convolution coefficients are
\((-2)^{k+1}+2(-2)^k=0\). Hence \(\mu*u=0\). The input is singular at every integer. Its coefficients grow in the positive direction, which is allowed in \(\mathcal D'(\mathbb R)\).

Its logarithmic profiles converge locally in integral to
\[
 v(x+iy)=\tfrac12|y|.
 \tag{E3.8}
\]
Above and below the real axis, one of the two exponential terms dominates, giving the two affine halves. Real lower and upper bounds exclude collapse; profile compactness identifies the local integral limit across the real axis. The corner at \(y=0\) is not harmonic. Its carrier is the whole interval \([-1/2,1/2]\), whereas the kernel's singular support is only the two endpoints. This is a nonhypoelliptic example where an individual carrier contains smooth points.

![The difference kernel's exact zeros have constant imaginary height; the sampled elliptic branch has a growing logarithmic retreat ratio.](../reproduce/L176/figures/zeros-and-logarithmic-retreat.png)

**Figure 1.** The upper panel displays the zeros (E3.6) for \(j=-3,\ldots,3\). The shaded comparison window is exactly \(|\eta|\le\log(2+|\xi|)/3\), expressed using the real center rather than the total complex norm. The two zeros closest to the origin are outside this narrow window; the large zeros enter it. The lower panel plots the exact ratios for \(j=q\) and for the elliptic branch \((t,i\sqrt{1+t^2})\), with \(t=q+1\), \(q=0,\ldots,50\). The two curves describe different kernels in dimensions one and two. The elliptic curve is one branch, not a proof for all its zeros. Example 2, Exercise 3 and Theorem 2.1 of the complete proof explain the obstruction and the scope of the comparison.

### Example 3. Local regularity despite a remote smooth tail

Let \(\mu\) be the kernel of Example 1 and let \(b\) be smooth, supported in \([11/4,13/4]\). Set \(\widetilde\mu=\mu+b\). The same compact \(\nu\) satisfies
\[
 \widetilde\mu*\nu=\delta_0+r+b*\nu.
 \tag{E3.9}
\]
The new error is smooth and compact. Thus \(\widetilde\mu\) remains hypoelliptic, and its singular set is still \(\{3/5\}\).

Use
\[
 X_1=X=(-1,1),\qquad X_2=(-2/5,8/5).
 \tag{E3.10}
\]
Both required singular inclusions hold with equality:
\[
 X+\{3/5\}=X_2,\qquad X_2-\{3/5\}=X_1.
 \tag{E3.11}
\]
Therefore a zero convolution class on \(X_2\) forces the input to be smooth on \(X\). At output zero, ordinary convolution with the remote tail would sample near input \(-3\), outside \(X_1\). The quotient operation remains defined because its sampling uses the singular point.

### Example 4. A hypoelliptic kernel with two separated singularities

This example makes the exact, nonconvex conclusion visible. Define the distributions
\[
 \lambda_\mp(x)=\operatorname{pv}\frac1{1-x^2}
                   \ \pm\ \frac{i\pi}{2}(\delta_{-1}+\delta_1).
 \tag{E3.12}
\]
Here \(\lambda_-\) uses the plus sign; it is the boundary value
\((1-x^2-i0)^{-1}\). The identity
\((s-i0)^{-1}=\operatorname{pv}(1/s)+i\pi\delta_0\)
follows by pairing \(s/(s^2+\varepsilon^2)+i\varepsilon/(s^2+\varepsilon^2)\) with a test: subtract its value at zero in the first integral, and rescale \(s=\varepsilon t\) in the second. Applying this at the two simple roots of \(1-x^2\), whose derivative moduli are two, gives (E3.12).

The elementary principal-value transform is
\[
 \mathcal F(\operatorname{pv}(1/x))(\xi)
                         =-i\pi\operatorname{sign}\xi.
 \tag{E3.13}
\]
For completeness, its odd integral is \(-2i\int_0^\infty\sin(\xi x)/x\,dx\). With a damping factor \(e^{-\varepsilon x}\), differentiation in \(\xi\) gives \(\varepsilon/(\varepsilon^2+\xi^2)\); integration from zero gives \(\arctan(\xi/\varepsilon)\). Letting \(\varepsilon\downarrow0\), with the principal value interpreted distributionally, proves (E3.13).

Use
\[
 \operatorname{pv}\frac1{1-x^2}
       =\tfrac12\left(-\operatorname{pv}\frac1{x-1}
                            +\operatorname{pv}\frac1{x+1}\right).
 \tag{E3.14}
\]
Translation and (E3.13) give
\[
 \widehat{\lambda_-}(\xi)=i\pi e^{-i|\xi|},\qquad
 \widehat{\lambda_+}(\xi)=-i\pi e^{i|\xi|}.
 \tag{E3.15}
\]
The imaginary delta terms contribute \(\pm i\pi\cos\xi\); the principal-value part contributes \(\pi\operatorname{sign}\xi\sin\xi\), which verifies both signs.

Choose \(\chi\in C_c^\infty((-2,2))\) equal to one near \([-3/2,3/2]\), and put
\[
 \mu_0=\chi\lambda_-,\qquad
 \nu_0=\pi^{-2}\chi\lambda_+.
 \tag{E3.16}
\]
The removed part \((1-\chi)/(1-x^2)\) is smooth and has every derivative integrable. Repeated integration by parts therefore makes its real Fourier transform \(q(\xi)\) decrease faster than every polynomial. Thus
\[
 \widehat{\mu_0}=i\pi e^{-i|\xi|}-q,\qquad
 \widehat{\nu_0}=\pi^{-2}(-i\pi e^{i|\xi|}-q).
 \tag{E3.17}
\]
Their product is one plus a rapidly decreasing function. Every derivative of its inverse Fourier error is absolutely integrable, so
\(\mu_0*\nu_0=\delta_0+r\), with \(r\) smooth. The error is compact because both kernels are compact. This proves hypoellipticity through the compact-parametrix equivalence.

Both singular sets are exactly \(\{-1,1\}\). The imaginary point masses ensure singularity at each endpoint, and the kernels are smooth elsewhere. Hence the parametrix is smooth at zero, although zero lies in the convex hull of its singular set.

The profiles also show the separation exactly. Fourier multiplication by \(\chi\) gives the entire formula
\[
 \widehat{\mu_0}(z)=\frac i2
           \int_{\mathbb R}\widehat\chi(z-s)e^{-i|s|}\,ds.
 \tag{E3.18}
\]
The integral converges locally uniformly in complex \(z\), by whole-complex smooth decay. If \(c=\operatorname{Re}z>1\), extend its positive-\(s\) contribution to all real \(s\). Fourier inversion, first on real \(z\) and then by the entire identity principle, identifies that contribution as \(i\pi e^{-iz}\chi(1)=i\pi e^{-iz}\). The changed negative-\(s\) tails obey
\[
 |\widehat{\mu_0}(z)-i\pi e^{-iz}|
             \le C_N(1+c)^{-N}e^{2|\operatorname{Im}z|}
 \quad(c>1)
 \tag{E3.19}
\]
for every \(N\): integrate the decay bound for \(\widehat\chi(z-s)\) over \(s<0\), where \(|c-s|\ge c+|s|\). On a fixed logarithmic strip that error is smaller than the leading term by every required power, after choosing \(N\) sufficiently large. Therefore the positive-center profile is \(y\). The negative-center calculation gives \(-y\). These are the only two profiles, with carriers \(\{1\}\) and \(\{-1\}\). Their closed union is the actual two-point singular set.

No ordinary convolution of the two noncompact boundary values was used. All products in this construction involve their compact representatives.

![Two affine profiles select the separated singular points minus one and one; the compact inverse has the reflected set, and a translated elliptic example shows the reflection from three fifths to minus three fifths.](../reproduce/L176/figures/affine-profiles-and-exact-reflected-singularities.png)

**Figure 2.** The first panel shows the exact profiles \(\eta\) and \(-\eta\) of the compact boundary-value kernel on the positive and negative real-center sequences. Its parametrix takes their negatives on those same sequences. The next panel marks the two actual singular sets \(\{-1,1\}\); the gray segments indicate their convex hulls, whose interiors are smooth. Vertical placement separates the two distributions schematically. The final panel marks the exact points \(3/5\) and \(-3/5\) from Example 1. Only horizontal coordinates carry spatial meaning. Examples 1 and 4 and Theorem 5.1 of the complete proof establish these sets and signs. These are original diagrams of the proved models.

## 4. Exercises and full solutions

Each exercise is worth 10 points, for a total of 100.

**Exercise 1.** Let \(W\ne\varnothing\). Explain why the exponential-series obstruction can use a first derivative at a point of \(W\), even when the zeros have nonzero imaginary parts and the observation point is not zero.

*Solution.* Choose \(x_0\in W\) and normalize each exponential as \(e_j(x)=e^{i(x-x_0)\cdot\zeta_j}\). Its compact test pairings have the additional factor \(e^{|x_0||\operatorname{Im}\zeta_j|}\), which is bounded by a fixed power of \(|\zeta_j|\). Increase the integration-by-parts order in (2.2) by that amount. This still makes the map \(\ell^1\to\mathcal D'\) continuous. Closed graph into \(C^\infty(W)\) bounds each first derivative at \(x_0\) by a constant times the coefficient norm. At a unit vector that derivative is \(i\zeta_{j,k}\), with no exponential modulus factor because the exponent vanishes at \(x_0\). Bounding all coordinates bounds \(|\zeta_j|\), giving the contradiction.

**Exercise 2.** Verify every zero in (E3.6), and verify the homogeneous equation for the full distribution (E3.7), including negative indices.

*Solution.* The nonzero factor \(e^{-iz/2}\) leaves the equation \(e^{iz}=-2\). Writing \(z=x+iy\) gives \(e^{-y}=2\) and \(e^{ix}=-1\), so \(y=-\log2\) and \(x=(2j+1)\pi\), with all \(j\in\mathbb Z\). For the distribution, translating by \(-1/2\) gives coefficient \((-2)^{k+1}\) at \(k+1/2\), while twice translating by \(1/2\) gives \(2(-2)^k\). Their sum vanishes for every integer \(k\), including negative \(k\), since the same integer-power identity holds there. Each compact test sees only finitely many output points, so coefficient cancellation proves the full distributional identity.

**Exercise 3.** In two dimensions consider \(P(\zeta)=1+\zeta_1^2+\zeta_2^2\). For \(t\ge1\), compute the zero-retreat ratio on the exact branch \(\zeta(t)=(t,i\sqrt{1+t^2})\). Compare it with the zeros of Exercise 2.

*Solution.* Substitution gives \(1+t^2-(1+t^2)=0\). Its imaginary modulus is \(\sqrt{1+t^2}\), and its complex Euclidean modulus is \(\sqrt{1+2t^2}\). Thus the ratio is \(\sqrt{1+t^2}/\log\sqrt{1+2t^2}\), which tends to infinity because its numerator grows linearly and its denominator logarithmically. For Exercise 2 the ratio is \((\log2)/\log\sqrt{((2j+1)\pi)^2+(\log2)^2}\), tending to zero. The first calculation checks one branch; the general elliptic criterion in the preceding polynomial lesson, rather than a single branch, proves retreat for every escaping polynomial zero.

**Exercise 4.** Derive the cutoff error in (E3.4) and locate its support and all singularities of the compact parametrix.

*Solution.* Product differentiation gives \((\chi G_0)''=\chi''G_0+2\chi'G_0'+\chi(G_0-\delta_0)\). Since \(\chi=1\) at zero, \((1-\partial^2)(\chi G_0)=\delta_0-\chi''G_0-2\chi'G_0'\). Convolution by the shifted differential kernel evaluates the parametrix at \(x-a\), turning \(\chi(x-a+a)G_0(x-a+a)\) into \(\chi(x)G_0(x)\); this proves (E3.4). Both cutoff derivatives vanish on \([-1,1]\) and outside \([-2,2]\). In their transition bands \(G_0\) is smooth, so the error is smooth there and everywhere. The parametrix has precisely the derivative jump at \(x=-a\), with no additional singularities from its smooth cutoff.

**Exercise 5.** Compute the real Fourier product of the two compact boundary-value representatives in (E3.17), using the same removed-tail transform \(q\). Explain why this produces a smooth compact error without assuming that the noncompact boundary values can be convolved.

*Solution.* Put \(r=|\xi|\). Then
\[
 \widehat{\mu_0}\widehat{\nu_0}
 =1+\pi^{-2}\bigl(q^2-2\pi q\sin r\bigr).
 \tag{E4.1}
\]
Indeed \((i\pi e^{-ir})(-i\pi e^{ir})=\pi^2\), and the sum of the two leading factors is \(i\pi(e^{-ir}-e^{ir})=2\pi\sin r\). The error has arbitrary polynomial decay because \(q\) does and the trigonometric factor is bounded. Multiplying it by any \(\xi^k\) remains integrable; Fourier inversion gives a smooth error. The compact convolution \(\mu_0*\nu_0\) exists and has compact support, so its difference from \(\delta_0\) is compact. The argument never forms \(\lambda_-*\lambda_+\).

**Exercise 6.** Suppose a proper profile has the form \(v=a\cdot\operatorname{Im}z+b\). Prove that \(a\) is a singular point, using the realization theorem. State why a general convex carrier cannot be treated the same way.

*Solution.* The indicator is \(a\cdot\eta\), whose carrier is \(\{a\}\). Realization gives a compact factor \(w\) singular only at zero for which the output singular hull is \(\{a\}\). That hull is nonempty, so the output singular set is itself exactly \(\{a\}\). Compact singular-support inclusion puts it inside \(\operatorname{sing\,supp}\mu+\{0\}\), proving \(a\in\operatorname{sing\,supp}\mu\). If the output hull is an interval or another larger convex set, its interior can consist of smooth points. Example 2 has an interval carrier with only its endpoints singular; the singleton step is essential.

**Exercise 7.** Let \(n=3\), \(B=4\), and suppose a separating neighborhood has gap \(d=2/5\). Find a \(t\) that makes the inverse contour integral and all its spatial derivatives through order five absolutely integrable. Explain the strict inequality.

*Solution.* The needed condition is \(2td>B+5+n=12\). Since \(2d=4/5\), take \(t=16\), giving \(2td=64/5>12\). The order-five tail is then bounded by a constant times \(|\xi|^{4+5-64/5}=|\xi|^{-19/5}\). In three dimensions its radial integral has exponent \(2-19/5=-9/5<-1\), so it converges. At equality \(2td=12\), the radial exponent is \(-1\), whose logarithmic integral diverges; a strict margin is needed.

**Exercise 8.** For \(\mu=\delta_2\), show why letting the reciprocal exponent depend on strip width would falsely permit the support function zero in place of the correct reflected support function.

*Solution.* The transform is \(e^{-2iz}\), and the reciprocal modulus is \(e^{-2\operatorname{Im}z}\). On \(|\operatorname{Im}z|<m\log|z|\), it is at most \(|z|^{2m}\). Thus using \(B_m=2m\) would permit the incorrect ceiling with \(H=0\). No single \(B\) works: choose an integer \(m>B+1\), put \(z=c-i(m/2)\log c\), and let \(c\to\infty\). This lies in that strip eventually, its reciprocal modulus is \(c^m\), and \(|z|\sim c\), exceeding \(|z|^B\). The correct singular set is \(\{2\}\); its contribution \(H_{\{2\}}(-\operatorname{Im}z)=-2\operatorname{Im}z\) gives exact equality with \(B=0\) in every strip.

**Exercise 9.** Replace the kernel of Example 1 by \(i\mu\). Find a fundamental solution, its singular point and the reflected kernel for the bilinear pairing.

*Solution.* Multiply the old inverse by \(1/i=-i\): \(\widetilde E(x)=-iG_0(x+a)\). Then \((i\mu)*\widetilde E=\mu*E=\delta_0\), and its singular point remains \(-a\). Reflection gives \(i(1-\partial_x^2)\delta_{-a}\), because the second derivative has even reflection parity and reflection does not conjugate the scalar coefficient. Replacing \(i\) by \(-i\) in that reflected kernel would be a sesquilinear convention and would reverse the sign of this inverse calculation.

**Exercise 10.** Give compatible domains showing that the sufficient local theorem needs \(X+S\subset X_2\), even though the necessary theorem does not assume it.

*Solution.* Take \(\mu=\delta_{3/5}\), \(X_1=(-2,2)\), \(X_2=(0,1)\), and \(X=(-3/2,-1)\). Its singular set is \(S=\{3/5\}\), and \(X_2-S=(-3/5,2/5)\subset X_1\). But \(X+S=(-9/10,-2/5)\) is disjoint from \(X_2\). The input \(u=\delta_{-5/4}\) is singular in \(X\); its output is \(\delta_{-13/20}\), whose restriction to \(X_2\) is zero. Thus a zero output class does not make this input smooth on \(X\). The missing inclusion is exactly the one that would permit the inverse to sample that point from the equation domain.

## References

- Gerd Grubb, *Fourier transformation of distributions*, University of Copenhagen, [freely accessible lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, [course and lecture notes](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* and *II*, Springer. The full convolution regularity and boundary-value theories are credited to these works. This chapter supplies the required proofs and links its exact preceding arguments.
