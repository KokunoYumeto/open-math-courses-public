# Locating singularities through logarithmic Fourier strips

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Public domain (CC0 1.0).*

The support of a compact distribution may include a large smooth part. Its singularities occupy a smaller set. To see that set through the Fourier transform, we allow complex frequencies whose imaginary part grows only logarithmically with their total size. Smooth Fourier decay can absorb any fixed logarithmic width. A fixed polynomial growth order then locates the convex hull of the singularities.

Basic references are Terence Tao's *Some connections with the Fourier transform* and Lars Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The [complete proof](singular-support-hull-formal.md) is supplied below. Its exact preceding inputs are [compact Fourier bounds and division](../../AN02-L122.html#3-a-bounded-complex-displacement-for-polynomial-division), [whole-complex smooth decay and the logarithmic contour](../../AN02-L153.html#tp3-the-complete-logarithmically-shifted-contour), and [joint logarithmic-frequency limits](../../AN02-L157.html#2-the-compactness-and-support-statement).

## 6. The growth order stays fixed while the strip widens

We use \(F_u(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle\). For a nonempty compact convex set \(K\), its support function is \(H_K(\eta)=\max_{x\in K}x\cdot\eta\).

The strip criterion says that \(\operatorname{sing\,supp}u\subset K\) exactly when

\[
|F_u(\zeta)|\le C_m(1+|\zeta|)^N e^{H_K(\operatorname{Im}\zeta)}
\quad\text{for }|\operatorname{Im}\zeta|\le m\log(1+|\zeta|),
\quad m=1,2,\ldots,
\tag{6.1}
\]

with **one fixed exponent \(N\)**. Each width has its own constant \(C_m\). The exponent cannot depend on that width. Exercise 1 explains why changing the exponent would make the criterion unable to locate singularities.

For necessity, cut off the distribution very close to \(K\). The retained compact part has ordinary carrier \(K+\delta\overline B\), which adds \(\delta|\operatorname{Im}\zeta|\) to the exponential bound. Choosing \(\delta=1/(m+1)\) costs at most one extra polynomial order in the \(m\)-th strip. The discarded part is smooth and has arbitrary whole-complex polynomial decay, so it fits the same strip bound. The order of the original compact distribution therefore gives one fixed exponent for every strip.

For sufficiency, take a point outside \(K\), and a direction \(\theta\) strictly separating it from \(K\). Fourier inversion moves to the complex contour

\[
\zeta(\xi)=\xi+iR\theta\log(2+|\xi|^2).
\tag{6.2}
\]

The support bound and the inverse Fourier exponential combine to give a negative power of \(2+|\xi|^2\). The separation gap determines that power. Increasing \(R\) makes it dominate any desired derivative order. The [full contour proof](singular-support-hull-formal.md#3-moving-the-gaussian-contour-and-removing-the-regularization) keeps the Jacobian, deforms a Gaussian-regularized entire integrand, and proves a majorant independent of the regularization parameter before removing it.

![A separating direction for a compact vertical carrier and a slice of its logarithmic complex contour](figures/separation-and-logarithmic-strip.png)

**Figure 1.** The spatial carrier is \(K=\{0\}\times[-1,1]\), the observation point is \(x_0=(2,0)\), and its neighborhood has radius \(1/2\). The closest point is \(p=(0,0)\); the unit separating direction is \(\theta=(1,0)\), with gap at least \(3/2\) throughout the neighborhood. The right panel shows the \(\xi_2=0\) slice of (6.2), with \(R=2\) and \(\zeta_2=0\). Its imaginary height is \(2\log(2+\xi_1^2)\). The shaded region is the actual upper logarithmic strip \(\eta\le4\log(1+\sqrt{\xi_1^2+\eta^2})\). Equal scales are used in the spatial plane. The full proof integrates over all real frequency coordinates; the right panel is a specified slice.

## 7. Recovering the convex hull from every limiting profile

In the preceding lesson, \(\mathcal J(u)\) denotes the support functions obtained from all escaping logarithmic-window profile limits, including the collapsed support function \(-\infty\). The hull theorem is

\[
H_{\operatorname{conv}\operatorname{sing\,supp}u}(\eta)
=\sup_{h\in\mathcal J(u)}h(\eta).
\tag{7.1}
\]

Here the support function of the empty set is identically \(-\infty\). In particular a compact smooth distribution has only the collapsed profile.

One inequality comes directly from the strip criterion. If all singularities lie in \(K\), every proper profile is bounded by a constant plus \(H_K(\operatorname{Im}z)\), and its recession support function is at most \(H_K\).

For the reverse inequality, form the closed convex hull \(D\) of all the proper profile sets. Each lies inside a fixed ordinary carrier, so \(D\) is compact. If \(D\) failed the strip criterion, the failing complex frequencies would produce an escaping real sequence and bounded, moving observation points. A profile extraction and the compact Hartogs bound contradict that failure. The strip criterion then puts every singularity in \(D\).

If there were no proper profile despite a singularity, the real Fourier transform would decrease faster than every polynomial. Its differentiable inverse integral would make the distribution smooth. The [complete hull proof](singular-support-hull-formal.md#4-the-hull-recovered-from-all-logarithmic-profiles) includes that empty case and the comparison at moving observation points.

## 8. Polynomial differentiation preserves the compact singular hull

For \(D=(1/i)\partial\), a nonzero polynomial differential operator satisfies

\[
\operatorname{conv}\operatorname{sing\,supp}P(D)u
=\operatorname{conv}\operatorname{sing\,supp}u
\quad\text{when }u\text{ is compactly supported}.
\tag{8.1}
\]

The operator can be nonelliptic. Polynomial zeros are handled by the proved bounded complex-displacement division estimate. That estimate transfers a logarithmic-strip bound for \(P(D)u\) to one for \(u\), with the same growth order. In the smooth case it transfers arbitrary rapid real decay.

Thus a compact distribution whose polynomial image is smooth is itself smooth. Compactness is essential, as Worked example 3 shows.

## Worked example 1. A large smooth support and one singular point

Let \(\phi(t)=e^{-1/(1-t^2)}\) for \(|t|<1\), zero otherwise, and put \(b(x)=\phi(x/3)\). Then \(b\) is positive inside \((-3,3)\), smooth and compact, with support \([-3,3]\). Consider \(u=\delta_1+b\).

Its singular support is exactly \(\{1\}\). The smooth term changes no singularities. A point mass cannot have a smooth representative near its point: a shrinking test bump with value one there pairs to 1 with the mass, while its pairing with a bounded smooth function tends to zero. Its ordinary support is the entire interval \([-3,3]\).

For \(K=\{1\}\), the support function is \(H_K(\eta)=\eta\). The point-mass transform \(e^{-i\zeta}\) has exactly that exponential modulus. Smooth decay bounds the other term by \(B_L(1+|\zeta|)^{-L}e^{3|\operatorname{Im}\zeta|}\). Since \(3|\eta|-\eta\le4|\eta|\), choose \(L>4m\) on the \(m\)-th strip. The sum satisfies (6.1) with \(N=0\).

A global bound by a fixed polynomial times \(e^\eta\) would fail. On \(\zeta=i\eta\), \(\eta>0\), positivity gives
\(F_b(i\eta)\ge c e^{2\eta}/2\), where \(c=\min_{[2,5/2]}b>0\). The exponential \(e^{2\eta}\) cannot be bounded by any fixed polynomial times \(e^\eta\). The restriction to logarithmic strips is what removes the effect of the distant smooth support.

By smooth invariance, every proper logarithmic-window limit for \(u\) is the point-mass profile \(\operatorname{Im}z\). Its profile set is \(\{1\}\), agreeing with the singular hull.

## Worked example 2. Derivative order and the contour budget

For \(u=D^r\delta_a\), \(r\ge0\), \(F_u(\zeta)=\zeta^re^{-ia\zeta}\). The strip bound with \(K=\{a\}\) holds at every complex frequency with \(N=r\). Its proper logarithmic profile on positive real centers is \(r+a\operatorname{Im}z\), whose support set is \(\{a\}\).

At a point a positive distance from \(a\), choose the separating sign \(\theta=\operatorname{sign}(x-a)\). Each additional physical derivative introduces another power of the complex frequency. A larger \(R\) makes the logarithmic contour decay dominate that power, giving smoothness away from \(a\) to every order.

The Gaussian regularization can also be evaluated directly. For \(r=2\), \(a=0\), it is

\[
u_\varepsilon(x)=D^2q_\varepsilon(x)
=\left(\frac1{2\varepsilon}-\frac{x^2}{4\varepsilon^2}\right)
 (4\pi\varepsilon)^{-1/2}e^{-x^2/(4\varepsilon)}.
\tag{9.1}
\]

On each compact set separated from zero, this function and every derivative tend uniformly to zero: the Gaussian dominates all the powers of \(1/\varepsilon\). Distributionally it tends to \(D^2\delta_0\), whose singularity remains at zero.

## Worked example 3. A nonelliptic operator and the compactness hypothesis

In two dimensions set \(u=\delta_0(x_1)\otimes\phi(x_2)\), with the bump \(\phi\) above. Its singular support is the vertical segment \(K=\{0\}\times[-1,1]\). At every interior point of the segment, a test shrinking only in \(x_1\), with a fixed nonzero pairing against \(\phi\) in \(x_2\), distinguishes the point-mass factor from a bounded smooth representative. Closedness includes the endpoints. Away from the segment the distribution is zero.

Take \(P(\zeta)=\zeta_1\). It vanishes at every nonzero real frequency \((0,\xi_2)\), so it is nonelliptic; its complex zero set is the line \(\zeta_1=0\) inside \(\mathbb C^2\). Nevertheless \(D_1u=(D_1\delta_0)\otimes\phi\) has the same singular segment. For the derivative factor choose a shrinking test whose first derivative at zero is nonzero; its pairing grows like the inverse shrinking scale. It cannot be locally represented by a bounded smooth function. The hull theorem applies and gives the same vertical segment for both distributions.

If compactness is dropped, take \(w=1(x_1)\otimes\delta_0(x_2)\). It is singular along \(x_2=0\), but \(D_1w=0\). This distribution extends through the whole \(x_1\)-axis, so the compact-distribution assertion does not apply.

## Worked example 4. A triangular function, three corners and one hull

Let \(u(x)=(1-|x|)_+\). It is smooth off \(\{-1,0,1\}\), and its slope jumps at all three points. Its distributional second derivative gives

\[
D^2u=-\delta_{-1}+2\delta_0-\delta_1,\qquad
F_u(\zeta)=\frac{2(1-\cos\zeta)}{\zeta^2},
\quad F_u(0)=1.
\tag{9.2}
\]

The sign follows from \(D^2=-\partial_x^2\). The Fourier formula follows either by integrating the two affine pieces or by multiplying it by \(\zeta^2\) and comparing with the transform of the three point masses, then using its value at zero. Thus both singular supports are \(\{-1,0,1\}\), and both hulls are \([-1,1]\).

Choose \(R_j=2\pi j\), \(s_j=\log R_j\). On the imaginary observation axis,

\[
L_u(i\eta,R_j)
=\frac{\log4+2\log|\sinh(s_j\eta/2)|
 -\log(R_j^2+s_j^2\eta^2)}{s_j}
\longrightarrow |\eta|-2\qquad(\eta\ne0).
\tag{9.3}
\]

The full complex profiles converge in local \(L^1\) to \(|\operatorname{Im}z|-2\). On compact sets above or below the real axis, one exponential in the cosine dominates uniformly, while \(\log|R_j+s_jz|/s_j\to1\) uniformly. This gives the displayed limit on both open half-planes. The value at \(z=i\) tends to \(-1\), which excludes uniform collapse on every subsequence. PSH compactness and canonical recovery then identify every proper extraction with \(|\operatorname{Im}z|-2\), and uniqueness gives the full local integral convergence.

At \(z=0\) the transform is exactly zero on every one of these centers, so that observation value stays minus infinite. The recession function still is \(|\eta|\), the support function of \([-1,1]\). The negative constant \(-2\) records real polynomial decay and disappears from the hull.

![The triangular function and its three signed second-derivative masses, beside its exact Fourier-window profiles](figures/triangular-corners-and-singular-hull.png)

**Figure 2.** The left panels show the actual function \((1-|x|)_+\), its singular points \(-1,0,1\), and the coefficients \(-1,2,-1\) of the point masses in \(D^2u\). The arrows denote distributional coefficients. The right panel evaluates (9.3) for \(j=1,10,100\), excludes the exact infinite value at \(\eta=0\), and shows the proper local integral limit \(|\eta|-2\). Its recession support function is \(|\eta|\), giving the same hull \([-1,1]\) before and after the polynomial operator.

## Exercises with complete solutions

1. **Why the exponent cannot depend on the width.** Show that \(\delta_1\) satisfies the strip bound with \(K=\{0\}\) if one allows \(N_m=m\), although its singular point is outside \(K\). Show that no fixed \(N\) works.

   **Solution.** Its transform has modulus \(e^{\operatorname{Im}\zeta}\), which is at most \((1+|\zeta|)^m\) on the \(m\)-th strip. Thus \(N_m=m\) and \(C_m=1\) work. For a fixed \(N\), choose an integer \(m>N\), and \(\zeta=T+im\log T\), \(T>2\). These points lie in the \(m\)-th strip because \(\log T\le\log(1+|\zeta|)\). Their transform modulus is \(T^m\), while \((1+|\zeta|)^N=O(T^N)\), since \((\log T)/T\to0\). No fixed \(C_m\) can bound their ratio. This also confirms the singular point at 1 cannot be placed in \(K=\{0\}\).

2. **The compact part near the singular carrier.** Explain why the cutoff decomposition in Theorem 1.1 leaves a compact smooth remainder, and why its compact part keeps the original order \(M\).

   **Solution.** The cutoff equals one on a neighborhood of every singular point, so \((1-\chi)u\) vanishes there. At every other point, \(u\) already has a smooth representative and multiplication keeps it smooth. The remainder has support inside the compact ordinary support of \(u\), hence is compact smooth. The derivatives of a product \(\chi\varphi\) through order \(M\) are finite sums of cutoff derivatives times derivatives of \(\varphi\) through order \(M\). They increase the constant in the finite-order bound but introduce no higher derivative of the test. Thus \(\chi u\) has order at most \(M\).

3. **The Gaussian can grow on a complex contour.** Derive its modulus on \(\zeta=\xi+iR\theta\ell\), and explain why (3.7) gives a bound independent of \(0<\varepsilon\le1\).

   **Solution.** Since \(|\theta|=1\), the real part of \(\sum_j\zeta_j^2\) is \(|\xi|^2-R^2\ell^2\); the cross term is purely imaginary. The modulus is \(e^{-\varepsilon|\xi|^2+\varepsilon R^2\ell^2}\). Its exponent can be positive near some finite radii. The quantity \(R^2\log^2(2+r^2)-r^2\) is continuous and tends to \(-\infty\), so its nonnegative supremum \(B_R\) is finite. For \(0<\varepsilon\le1\), multiplying that quantity by \(\varepsilon\) gives at most \(B_R\), proving the uniform bound \(e^{B_R}\).

4. **The exact derivative order of a point mass.** For \(D^r\delta_a\), prove that the least nonnegative strip exponent is \(r\), and compute its profile's recession function.

   **Solution.** The entire modulus is \(|\zeta|^r e^{a\operatorname{Im}\zeta}\), so exponent \(r\) works with constant 1 and carrier \(\{a\}\). On the real axis it equals \(|\xi|^r\). An exponent \(N<r\) could not dominate it as \(|\xi|\to\infty\), even on the first strip, so \(r\) is least. The profile is \(r+a\operatorname{Im}z\). Its envelope at height \(\eta\) is \(r+a\eta\), and division by the recession parameter removes \(r\), giving \(a\eta\).

5. **A quantitative separation budget.** For the vertical carrier in Figure 1, find a uniform gap on the radius-\(1/2\) neighborhood of \((2,0)\). With \(N=2\), \(q=3\), \(n=2\), give a value of \(R\) satisfying the proof's derivative bound.

   **Solution.** With \(\theta=(1,0)\), \(H_K(\theta)=0\), and every point in that neighborhood has first coordinate greater than \(3/2\). Thus \(\delta=3/2\) is a valid uniform lower bound. The condition is \(2R\delta>N+q+n+1=8\), namely \(3R>8\). Choose \(R=3\). Then the derivative majorant has large-radius exponent \(N+q-2R\delta=5-9=-4\), integrable in real dimension 2. This numerical choice uses the stated gap for the whole neighborhood.

6. **The empty profile family of sets.** Prove that a compact distribution has no proper escaping profile if and only if it is smooth.

   **Solution.** A compact smooth function has uniform collapse on every compact observation set by arbitrary whole-complex polynomial decay. Conversely, if arbitrary rapid real decay failed, choose an escaping real sequence with a fixed finite lower bound for the observed logarithm at \(z=0\), as in Theorem 4.1. Uniform collapse on every compact set would contradict that lower bound, so PSH compactness supplies a proper extraction. Thus absence of proper profiles forces arbitrary rapid real decay. Lemma 2.1 gives a smooth representative. The support function for the collapsed profile is \(-\infty\), whereas a proper constant profile has nonempty set \(\{0\}\).

7. **Moving observation points need compact control.** Construct continuous functions on a real interval that tend pointwise and in \(L^1\) to zero but have supremum 1. Explain the role of the PSH Hartogs bound in (4.5).

   **Solution.** For \(j\ge2\), take \(g_j(t)=\max(1-8j^2|t-1/j|,0)\). Its center is \(1/j\), its half-width is \(1/(8j^2)\), and its supremum is 1. At each fixed nonzero point it eventually vanishes, and at zero it always vanishes. Its integral is the triangle's area \(1/(8j^2)\), so it tends to zero in \(L^1\). The supremum is attained at moving points. These are auxiliary continuous real functions, with no PSH premise. In the hull proof the compact Hartogs comparison supplies the additional PSH control: the supremum of the normalized error on an entire compact ball has upper limit at most \(M\), including its values at the moving \(z_j\). That contradicts their lower bound \(M+1\).

8. **Division keeps the growth order fixed.** Explain why radius-two complex displacement changes the strip width and constant but does not change the polynomial exponent.

   **Solution.** If \(w=\zeta+t\theta\), \(|t|\le2\), and \(|\zeta|\ge4\), then (5.3) puts \(w\) in the strip of width \(2m+3\). The growth factor satisfies \((1+|w|)^N\le3^N(1+|\zeta|)^N\), and support subadditivity bounds its exponential by \(e^{H_K(\operatorname{Im}\zeta)}e^{2r_K}\). The uniform division constant multiplies these fixed factors and \(C_{2m+3}\). None adds a power of \(|\zeta|\). The bounded remaining ball changes only the constant. This supplies the fixed-order premise of the strip criterion for \(u\).

9. **The noncompact counterexample.** Compute \(D_1(1\otimes\delta_0)\), locate its singular support, and explain the hypotheses needed for Theorem 5.1.

   **Solution.** The first factor is constant in \(x_1\), so its distributional derivative is zero; consequently \(D_1(1\otimes\delta_0)=0\). The original distribution is singular on the full line \(x_2=0\), detected by a shrinking test in \(x_2\), and is zero off that line. It is not compactly supported because the first coordinate extends through all of \(\mathbb R\). The theorem requires both compact \(u\) and a nonzero polynomial \(P\). It does not require ellipticity; the compact vertical-segment example shows that this stronger condition is unnecessary.

10. **Three slope jumps and the Fourier sign.** Derive \(D^2(1-|x|)_+\), compute its Fourier transform, and recover its singular hull from the proper profile \(|\operatorname{Im}z|-2\).

    **Solution.** The first derivative has values \(0,1,-1,0\) on the four intervals separated by \(-1,0,1\). Its jumps are \(1,-2,1\), so its second distributional derivative is \(\delta_{-1}-2\delta_0+\delta_1\). Multiplication by \(-1\), since \(D^2=-\partial^2\), gives (9.2). The transform of that signed sum is \(2-e^{i\zeta}-e^{-i\zeta}=2(1-\cos\zeta)\), equal to \(\zeta^2F_u(\zeta)\). The quotient extends at zero with value 1. Each of the three corners is singular, so their convex hull is \([-1,1]\). The profile's horizontal envelope is \(|\eta|-2\); its recession is \(|\eta|\), exactly the support function of that interval.

## References

1. Terence Tao, [*246B, Notes 2: Some connections with the Fourier transform*](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), *What's New*, 23 January 2021.
2. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983; second edition 1990; reprint 2003.
3. Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983; second revised printing 1990; reprint 2005.

The [figure program](make_figures188.py), [geometry specifications](figures/geometry.json), and [direct contour calculations](check_contours188.py) accompany the proofs and examples.
