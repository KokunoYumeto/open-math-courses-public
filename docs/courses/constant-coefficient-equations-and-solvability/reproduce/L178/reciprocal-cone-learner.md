# Zero-free cones turn slow decrease into reciprocal bounds

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI GPT-6.1 Sol (OpenAI). Public domain (CC0 1.0).*

An inverse Fourier transform needs control of the reciprocal transform, not merely absence of zeros. This chapter explains how a logarithmic lower bound near each real frequency supplies that control in a zero-free cone. It also gives a smooth compact kernel whose transform has no nonreal zeros but whose reciprocal grows too fast near a logarithmic boundary.

Basic references are Richard Melrose's [Differential Analysis](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), Gerd Grubb's [Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), and Lars Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. The prerequisites are Slow decrease and entire Fourier division, Theorem 1.1; Local compactness and Hartogs bounds, HC1; Entire logarithms and the approximation of plurisubharmonic functions, GD4; and Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1. The complete proof below supplies the new estimates.

## 1. The scale that connects two kinds of lower bound

For a compact kernel, write \(F(\zeta)=\langle\mu,e^{-ix\cdot\zeta}\rangle\) and \(\rho=2+|\zeta|\). Invertibility means slow decrease in the precise sense of the preceding Fourier-division lesson. It gives a polynomial lower value somewhere in a logarithmic real window. Suppose in addition that \(F\) has no zeros when
\[
\operatorname{Im}\zeta\in\Lambda_S,\qquad
|\operatorname{Im}\zeta|>D_S\log\rho,
\tag{E1.1}
\]
for every compact angular set \(S\) inside an open imaginary-direction cone.

Theorem 1.1 in the complete proof gives, after increasing the barrier,
\[
|F(\zeta)^{-1}|\le e^{A_S|\operatorname{Im}\zeta|}.
\tag{E1.2}
\]
The reverse implication holds even when its starting estimate includes an additional polynomial factor. The cone may contain all directions; this particular criterion does not require convexity.

Set \(r=|\operatorname{Im}\zeta|\), \(\xi=\operatorname{Re}\zeta\), and
\[
w=(z-\xi)/r,\qquad
u(w)=r^{-1}\log|F(\xi+rw)|.
\tag{E1.3}
\]
The target frequency becomes \(i\theta\), with \(|\theta|=1\). The real logarithmic window becomes a bounded, possibly very small real ball near zero. It still contains a point where \(u\) has a finite lower value. Hence a sequence of these logarithms cannot collapse uniformly on compact sets.

Compactness now bounds the local integral of \(|u|\) along a subsequence. A slightly enlarged angular set gives a whole zero-free ball around \(i\theta\). There \(u\) is harmonic, and its mean value bounds its negative value at the center by that local integral. Lemmas 2.1 and 3.1 and equation (3.8) give every constant and every subsequence step.

![A complex frequency and its normalized image, with the real logarithmic witness interval, the exact harmonic ball, and sampled transform zeros below the real axis.](figures/frequency-normalization-and-harmonic-ball.png)

*Figure 1.* A one-dimensional specialization of Lemmas 2.1 and 3.1. The original target is \(40+64i\); \(w=(z-40)/64\) sends it to \(i\). The original ball has radius \(16\), and the normalized ball has radius \(1/4\), so \(d=1/8\). The real witness interval has radius \(\log42\) and becomes radius \(\log42/64\). The shaded region is the actual inequality \(\eta>\log(2+\sqrt{\xi^2+\eta^2})\), with barrier constant 1. For \(D_0=1\), the proof chooses \(D=4(1+\log3/\log2)+1\), and \(64>D\log(2+|40+64i|)\). Red markers sample the exact zeros of Example 1; they are not the boundary of the general shaded region. Both circles lie inside that region. Proof locators: complete proof, (2.1)–(3.6). Background: Melrose, Grubb and Hörmander.

## 2. An inverse with a sharp exponential rate

**Example 1.** Let
\[
\mu=\delta_{-3/4}-\tfrac32\delta_{-1/4},\qquad
F(z)=e^{3iz/4}\bigl(1-\tfrac32e^{-iz/2}\bigr).
\tag{E2.1}
\]
On the real axis \(|F|\ge1/2\), so the complex-window slow-decrease criterion holds. Its zeros are exactly
\[
z=4\pi k-2i\log(3/2),\qquad k\in\mathbb Z.
\tag{E2.2}
\]
Thus the whole upper half-plane is zero-free. At \(z=\xi+i\eta\), \(\eta\ge0\),
\[
\frac1{3/2+e^{-\eta/2}}
\le e^{-\eta/4}|F(z)^{-1}|
\le\frac1{3/2-e^{-\eta/2}}.
\tag{E2.3}
\]
This follows by factoring \((3/2)e^{\eta/2}\) out of the second factor's modulus. The upper endpoint is attained at \(\xi=0\), and the lower endpoint at \(\xi=2\pi\). Both tend to \(2/3\). The reciprocal therefore grows at the precise exponential rate \(e^{\eta/4}\); a polynomial bound alone would fail at \(\xi=0\).

One can see that rate directly in the inverse:
\[
E=-\sum_{k=1}^{\infty}(3/2)^{-k}\delta_{\,3/4-k/2}.
\tag{E2.4}
\]
The point locations escape to minus infinity, so the distributional sum is locally finite. Convolution with the two point masses cancels all nonzero-location coefficients and leaves \(\delta_0\). Its closed convex support hull is \((-\infty,1/4]\), whose support value for positive \(\eta\) is \(\eta/4\). This agrees with (E2.3).

## 3. A direction can be safe while a nearby boundary is not

**Example 2.** In two dimensions let \(\mu=\partial_{x_1}\delta_0\), so \(F(z)=iz_1\). At every real center \(\xi\), moving a distance one in the first coordinate, with the sign of \(\xi_1\), makes \(|F|\ge1\). The complex-window criterion with window radius \(2\log(2+|\xi|)\) proves invertibility.

On an angular set with \(\eta_1\ge\varepsilon|\eta|\), \(\varepsilon>0\),
\[
|F(\xi+i\eta)|\ge|\eta_1|\ge\varepsilon|\eta|,
\qquad
|F(\xi+i\eta)^{-1}|\le(\varepsilon|\eta|)^{-1}.
\tag{E3.1}
\]
In contrast, the points \(z=(0,iR)\) are zeros for every \(R>0\). They eventually exceed every logarithmic barrier. Hence a cone including that direction fails the zero-free hypothesis. Compact angular sets inside \(\{\eta_1>0\}\) keep a positive distance from this boundary, exactly as the enlargement in (3.1) requires.

## 4. A zero-free transform of a smooth compact kernel

**Example 3.** The product
\[
F(z)=\prod_{j\ge1}\frac{\sin(2^{-j}z)}{2^{-j}z}
\tag{E4.1}
\]
has only real zeros. Proposition 5.1 proves that its inverse transform is a nonzero smooth kernel supported in \([-1,1]\), and that it fails slow decrease. The proof uses locally uniform product convergence and the exact compact-support growth theorem; it does not assume existence of an infinite random sum.

At \(z=R+id\log(R+2)\), with \(J=\lfloor\log_2R\rfloor\),
\[
\log|F(z)|\le
d\log(R+2)-\tfrac{\log2}{2}J(J-1).
\tag{E4.2}
\]
The negative term is quadratic in \(\log R\). A reciprocal estimate consisting of a fixed power of \(\rho\) times \(e^{A|\operatorname{Im}z|}\) could supply only a lower bound linear in \(\log R\) on this path. Thus it cannot hold, despite zero-freeness of the entire upper half-plane.

![Exact rescaled reciprocal bounds for the two-atom kernel and finite-product evaluations with a rigorous tail bound for the smooth compact counterexample.](figures/exponential-rate-and-smooth-counterexample.png)

*Figure 2.* Left: the two exact endpoints in (E2.3), with limit \(2/3\); the rescaling removes \(e^{\eta/4}\). Right: the natural logarithm of the product (E4.1) at \(R=2^J\), \(d=6\), \(J=4,\ldots,48\). Each value uses \(K=J+120\) factors. Equations (5.6)–(5.7) bound its relative omitted tail by \(2^{-240}\), so the plotted samples represent the infinite product with that stated error. The orange curve is the proved upper bound (E4.2), and the dotted comparison is \(-10\log(R+2)\). The proof establishes eventual failure of every fixed polynomial lower bound, not just this displayed comparison. Proof locators: Example 1 and complete proof, Proposition 5.1. Background: Grubb and Hörmander.

**Example 4.** A single point mass works in every direction. For \(\mu=\delta_a\), \(a\in\mathbb R^n\),
\[
F(\zeta)=e^{-ia\cdot\zeta},\qquad
u(w)=a\cdot\operatorname{Im}w,\qquad
|F(\zeta)^{-1}|=e^{-a\cdot\operatorname{Im}\zeta}.
\tag{E4.3}
\]
Its inverse is \(\delta_{-a}\). Its normalized logarithm is already harmonic and independent of the scale or real center. This example allows the whole direction space in Theorem 1.1.

## 5. Exercises and full solutions

The exercises give 100 points in total.

### Exercise 1. The scale and the real witness (10 points)

Suppose \(r>D\log(2+|\xi+i\eta|)\), \(|\eta|=r\), and \(|h|<\log(2+|\xi|)\). Prove \(|h/r|<1/D\). If \(|F(\xi+h)|>(b+|\xi|)^{-b}\), \(b\ge2\), give a lower bound for \(r^{-1}\log|F(\xi+h)|\) independent of \(\xi,\eta\).

**Solution.** Put \(\rho=2+|\xi+i\eta|\). Then \(2+|\xi|\le\rho\), so \(|h|/r<\log\rho/(D\log\rho)=1/D\). Also \(b+|\xi|\le b\rho\) and \(r>D\log\rho\ge D\log2\). Hence the normalized logarithm exceeds \(-b/D-b\log b/(D\log2)\). This is the fixed compact witness in Lemma 2.1. Allocate 4 points to the radius and 6 to the uniform lower bound.

### Exercise 2. Verify the harmonic ball (10 points)

In Figure 1 use \(D_0=1\), \(d=1/8\), \(\xi=40\), and \(r=64\). Verify the proof's barrier condition. Explain why every \(w\in B(i,1/4)\) satisfies the zero-free inequality after returning to the original frequency.

**Solution.** Here \(\beta=1+\log3/\log2<2.585\), so \(D=4\beta+1<11.34\). The modulus of \(40+64i\) is \(\sqrt{5696}<76\), giving \(\log(2+|40+64i|)<\log78<4.357\). Thus \(D\log\rho<49.41<64\). In the normalized ball, \(\operatorname{Im}w>3/4\) and \(|w|<5/4\). The new imaginary part exceeds \(48\), whereas \(\log(2+|40+64w|)\le\log(3\rho)<\log234<5.46\). Hence every point of the ball lies in the upper zero-free region for \(D_0=1\). Allocate 5 points to each inequality.

### Exercise 3. Angular enlargement in two dimensions (10 points)

Let \(\Gamma=\{v:v_1>0\}\), and \(S=\{\theta\in\mathbb S^1:\theta_1\ge\sqrt3/2\}\). Show that \(d=1/16\) is valid in (3.1). Explain what fails if \(S\) is replaced by all directions with \(\theta_1>0\).

**Solution.** For \(\operatorname{dist}(\omega,S)\le1/4\), choose a closest point \(\theta\in S\), which exists by compactness. Then \(\omega_1\ge\theta_1-|\omega-\theta|\ge\sqrt3/2-1/4>0\). Thus \(T\subset\Gamma\). The full set of strictly positive first-coordinate directions is not compact in the sphere; directions approach \((0,1)\). No positive enlargement radius keeps them inside \(\Gamma\). For \(F(z)=iz_1\), the limiting direction has zeros \((0,iR)\) at arbitrarily large imaginary size. Allocate 6 points to the estimate and 4 to the boundary obstruction.

### Exercise 4. Translation of a kernel (10 points)

If \(G\) is the transform of \(\nu\), find the transform of \(\tau_a\nu\) and its normalized logarithm. If \(|G(\zeta)^{-1}|\le e^{A|\operatorname{Im}\zeta|}\), give a pure exponential reciprocal bound after translation.

**Solution.** Translation in the exponential pairing gives \(F(\zeta)=e^{-ia\cdot\zeta}G(\zeta)\). Since the real center contributes a factor of modulus one,
\[
r^{-1}\log|F(\xi+rw)|
=a\cdot\operatorname{Im}w+r^{-1}\log|G(\xi+rw)|.
\tag{S4.1}
\]
The reciprocal has the factor \(e^{-a\cdot\operatorname{Im}\zeta}\le e^{|a||\operatorname{Im}\zeta|}\). Its bound is therefore \(e^{(A+|a|)|\operatorname{Im}\zeta|}\). Allocate 4 points to the transform, 3 to the normalized logarithm, and 3 to the new bound.

### Exercise 5. Integral convergence alone does not control a value (15 points)

On \(\mathbb C\), consider \(v_j(w)=j^{-1}\log|w-i|\). Show that these functions are locally uniformly bounded above and converge to zero in local \(L^1\), but all have value minus infinity at \(i\). Identify the additional property used in (3.8).

**Solution.** On a compact set the distance to \(i\) has a finite upper bound, so all \(v_j\) have a common upper bound, for example the nonnegative part of the logarithm of that distance bound. The function \(\log|w-i|\) is locally integrable: near \(i\), polar coordinates give the finite integral \(2\pi\int_0^\varepsilon r|\log r|\,dr\); away from \(i\) it is continuous. Dividing its local integral norm by \(j\) proves convergence to zero. Its value at \(i\) is nevertheless minus infinity for every \(j\). A common zero-free neighborhood makes the actual normalized logarithms harmonic near the observation point. Their ball-mean identity then bounds their absolute values by the local integral norms. Allocate 4 points to the upper bound, 6 to integral convergence, and 5 to the missing harmonic-neighborhood property.

### Exercise 6. A certified product tail (15 points)

Take \(R=2^{20}\), \(z=R+6i\log(R+2)\), and \(K=140\). Prove that the relative tail in (5.7) is smaller than \(2^{-240}\). Give the argument that makes the same bound valid at the plotted points \(R=2^J\), \(4\le J\le48\), \(K=J+120\).

**Solution.** At all these points \(|z|<2R\). Indeed the ratio \(\log(R+2)/R\) decreases for \(R\ge16\), and at \(R=16\) one has \(6\log18<\sqrt3\,16\). This follows, for example, from \(\log18<3\) and \(18<16\sqrt3\); differentiation verifies the decreasing ratio because \(R/(R+2)<\log(R+2)\). Thus \(|z|^2<4R^2\). For \(K=J+120\),
\[
s_K<\frac{e^{1/2}}{18}\,2^{-238}<2^{-241}.
\tag{S6.1}
\]
The last inequality uses \(e^{1/2}<2\) and \(2/18<1/8\). Also \(|z|2^{-K-1}<2^{-120}<1/2\), so (5.7) applies and gives \(2s_K<2^{-240}\). None of these points is a zero because its imaginary part is positive. Allocate 5 points to \(|z|<2R\), 6 to the tail sum, and 4 to checking all hypotheses.

### Exercise 7. Exact zero multiplicities of the smooth kernel (15 points)

For a nonzero integer \(m\), determine the multiplicity of the zero \(z=2\pi m\) of (5.1). Prove that there are no other zeros.

**Solution.** Write \(|m|=2^k\ell\), with \(\ell\) odd. The \(j\)-th factor vanishes there precisely when \(2^{1-j}m\) is a nonzero integer, namely for \(j=1,\ldots,k+1\). Each of these sine zeros is simple, and its denominator is nonzero. The remaining finite factors and convergent product tail are nonzero near that point, by the nonvanishing tail argument in Proposition 5.1. The multiplicity is \(k+1=1+v_2(|m|)\). The first factor already has its zeros at all \(2\pi m\), \(m\ne0\), and every other factor's zeros belong to this set. Outside their union, the locally convergent nonzero tail shows that the product is nonzero. Allocate 6 points to identifying the factors, 5 to multiplicity, and 4 to completeness of the zero set.

### Exercise 8. A second exact inverse and its support rate (15 points)

Find a locally finite point-mass inverse of \(\mu=\delta_{-2/3}-(5/4)\delta_{-1/3}\). Find its closed convex support hull and the precise exponential growth rate of \(F(i\eta)^{-1}\) as \(\eta\to+\infty\).

**Solution.** Set \(a=-2/3\), \(b=1/3\), and \(\lambda=5/4\). Then
\[
E=-\sum_{k\ge1}\lambda^{-k}\delta_{-a-kb}
=-\sum_{k\ge1}(5/4)^{-k}\delta_{\,2/3-k/3}.
\tag{S8.1}
\]
The locations tend to minus infinity, making the sum locally finite. The first translated sum in \(\mu*E\) has coefficients \(-\lambda^{-k}\) at \(-kb\), \(k\ge1\). The second has coefficient \(1\) at zero and \(+\lambda^{-k}\) at those same other locations. Thus the convolution is \(\delta_0\). The rightmost support point is \(1/3\), so its hull is \((-\infty,1/3]\). Factoring the transform gives
\[
|F(i\eta)^{-1}|=
\frac{e^{\eta/3}}{5/4-e^{-\eta/3}}
\sim\tfrac45e^{\eta/3}.
\tag{S8.2}
\]
The exponential rate is exactly \(1/3\), equal to the hull's support value at the unit positive direction. Allocate 6 points to the inverse and cancellation, 4 to the hull, and 5 to the growth rate.

## References

- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Gerd Grubb, *Fourier transformation of distributions*. [Author-hosted chapter](https://web.math.ku.dk/~grubb/dist5.pdf).
- Slow decrease and entire Fourier division, Theorem 1.1.
- Local compactness and Hartogs bounds, HC1.
- Entire logarithms and the approximation of plurisubharmonic functions, GD4.
- Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, volumes I and II, Springer. Background; the required estimates and all example and exercise proofs are supplied here or in the preceding linked lessons.
