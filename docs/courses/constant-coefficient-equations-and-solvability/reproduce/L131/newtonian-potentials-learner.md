# Local Newtonian potentials and subharmonic regularity

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original proof exposition and figures: CC0-1.0.

A subharmonic function can have a downward point singularity. In the plane, \(\log|x|\) tends to \(-\infty\) at the origin. In three dimensions, \(-1/|x|\) does the same. These singularities are still locally integrable. We will identify the exact integrability range and explain why averaging can turn a singular function into a continuous one.

The mechanism is local. The Laplacian records a positive measure of mass. Retain the mass near the region of interest, form its Newtonian potential, and subtract that potential. The remaining function is harmonic in the region and therefore smooth. The two conclusions then reduce to two properties of the explicit kernel.

The written distribution tools used here are [Order, positivity and distributional limits, Theorem 4.1](../../prerequisites/order-positivity-and-limits.html#positivity-forces-order-zero), [Tensor products and parameter-dependent distributions, Lemma 1.1](../../prerequisites/tensor-products-and-parameters.html#pairing-with-a-moving-smooth-test), and [Convolution as addition of supports, Theorems 1.1–3.1](../../prerequisites/convolution-as-addition-of-supports.html#which-pairs-can-contribute-to-an-output). Ordinary integration, polar coordinates, Taylor's formula and the divergence theorem are the elementary prerequisites. The [full proof](newtonian-potentials-formal.md) includes the measure representation and harmonic smoothing arguments.

## 1. The precise conclusion

Let \(X\subset\mathbb R^n\) be open, \(n\ge2\), and let \(v:X\to[-\infty,\infty)\) be upper semicontinuous and subharmonic. Its value at the centre of a ball is at most its spherical average. Assume it is not identically \(-\infty\) on any connected component.

Then

\[
 v\in L^p_{\mathrm{loc}}(X)
 \quad\begin{cases}
 \text{for }1\le p<n/(n-2),&n>2,\\
 \text{for every finite }p\ge1,&n=2.
 \end{cases}                                                     \tag{L131.1}
\]

There is also a continuity statement. Let \(f\in\mathcal E'(\mathbb R^n)\) be a **compactly supported distribution**. Suppose its potential \(f*E_n\) is a continuous function on all of \(\mathbb R^n\). Then the local distribution convolution \(f*v\) has a continuous representative on

\[
 \Omega_f=\{x:x-\operatorname{supp}f\subset X\}.                 \tag{L131.2}
\]

This domain matters. Every point sampled by the translated support of \(f\) must stay in \(X\). Compact support alone does not imply continuity: \(f=\delta_0\) leaves a point singularity unchanged. The extra condition concerns the potential of the convolution factor.

## 2. The kernel and the exponent

Use \(\Delta=\sum_j\partial_j^2\), and write \(s_n\) for the area of the unit sphere. The kernel with \(\Delta E_n=\delta_0\) is

\[
 E_n(x)=-\frac{|x|^{2-n}}{(n-2)s_n}\quad(n>2),\qquad
 E_2(x)=\frac{\log|x|}{2\pi}.                                  \tag{L131.3}
\]

The higher-dimensional kernel is negative. Its radial derivative is positive, and the outward flux through every sphere is

\[
 s_nr^{n-1}E_n'(r)=1.
\]

Green's identity on a punctured ball turns this flux into \(\Delta E_n=\delta_0\). The boundary term containing the kernel itself tends to zero. [NP4 of the full proof](newtonian-potentials-formal.md#NP4) supplies both boundary terms and their signs.

For \(n>2\), the local integral of \(|E_n|^p\) is a constant times

\[
 \int_0^R r^{n-1-p(n-2)}\,dr.
\]

This is finite exactly when \(n-p(n-2)>0\). At equality it becomes \(\int_0^Rdr/r\), which diverges. In two dimensions, substitute \(r=e^{-t}\): the integral near zero of \(r|\log r|^p\) becomes the tail of \(t^pe^{-2t}\), which is finite for every finite \(p\). The logarithm remains unbounded, so this does not give a local \(L^\infty\) bound.

**Worked example: an atom.** In three dimensions,

\[
 v(x)=-\frac1{4\pi|x|},\qquad \Delta v=\delta_0.
\]

For \(p<3\), its integral over \(B(0,R)\) is \((4\pi)^{1-p}R^{3-p}/(3-p)\). At \(p=3\), the integral outside radius \(\varepsilon\) is \((4\pi)^{-2}\log(R/\varepsilon)\), and grows without bound as \(\varepsilon\to0\). Thus even one atom makes the endpoint fail. The planar example \((2\pi)^{-1}\log|x|\) has every finite local \(L^p\) norm and no local boundedness near zero.

## 3. Cutting off the mass

The submean inequality first implies local \(L^1\) integrability. At a point where \(v(a)\) is finite, choose a local upper bound \(M\). Every spherical average of the nonnegative function \(M-v\) is at most \(M-v(a)\). Polar integration gives an integrable neighborhood. Integrability then propagates across each connected component: near a limit point of such neighborhoods, select a nearby point of finite value and apply the same ball argument. The excluded identically \(-\infty\) component is the only component on which this cannot begin.

Smooth \(v\) locally with a nonnegative radial mollifier. The smooth functions retain the submean inequality. Their small-radius spherical averages have expansion

\[
 v_\varepsilon(x)+\frac{r^2}{2n}\Delta v_\varepsilon(x)+o(r^2),
\]

so \(\Delta v_\varepsilon\ge0\). Passing to distributions gives \(\Delta v\ge0\). A positive distribution is a positive Radon measure \(\mu\): positivity bounds its pairing by a constant times the supremum norm on each compact support. Extending to continuous tests and constructing a measure from the masses of open sets proves the representation. [NP2–NP3](newtonian-potentials-formal.md#NP2) give these steps in full.

For a relatively compact observation region \(Y\subset X\), choose \(\chi\in C_c^\infty(X)\) with \(0\le\chi\le1\), equal to one near \(\overline Y\). Then \(\nu=\chi\mu\) has finite mass and compact support. Subtract its potential:

\[
 v=E_n*\nu+h,\qquad
 \Delta h=(1-\chi)\mu=0\text{ near }\overline Y.                 \tag{L131.4}
\]

The remainder is smooth and harmonic. Here is the local smoothing proof. A mollification of \(h\) is smooth and harmonic, hence equal to its average against any fixed normalized radial smooth kernel whose support stays inside the harmonic region. Letting the mollification radius tend to zero shows that \(h\), as a distribution, already equals that fixed smooth average. Thus it is smooth. [NP5](newtonian-potentials-formal.md#NP5) proves the mean-value identity and the distribution limit.

If \(\nu\) has mass \(M\) and \(A-\operatorname{supp}\nu\subset B(0,R)\), Jensen's inequality followed by Tonelli gives

\[
 \|E_n*\nu\|_{L^p(A)}\le M\|E_n\|_{L^p(B(0,R))}.              \tag{L131.5}
\]

The finite mass, rather than a density bound, controls the potential. Adding the locally bounded harmonic remainder proves (L131.1). The potential may be \(-\infty\) on a null set; local \(L^p\) is a statement about its almost-everywhere values. Radial smoothing also identifies the original subharmonic representative pointwise with (L131.4).

![Local cutoff and the mass that remains outside the observation disc.](figures/local-cutoff.png)

*Figure 1.* The planar example has \(X=B(0,3.6)\), \(Y=B(0,2)\), cutoff one on \(r\le2.2\) and zero on \(r\ge3\), and atoms of masses \(1,2,1,1\) at \((-1.2,0.3)\), \((0.8,-0.7)\), \((2.5,0.8)\), \((-2.8,-1.5)\). Blue disc areas show the retained mass; orange ring areas show the remainder. The transition atom contributes to both potentials. Every remaining singularity is outside \(Y\), so its potential is harmonic there. The exact smooth cutoff is \(\chi(x)=S((|x|-2.2)/0.8)\), with \(S(t)=b(1-t)/(b(t)+b(1-t))\) and \(b(t)=e^{-1/t}\) for \(t>0\), zero otherwise. See NP7 and NP10, Example 3.

## 4. Why the continuity condition works

Fix \(x_0\in\Omega_f\). Compactness of \(\operatorname{supp}f\) gives a small output ball \(B\) with \(\overline B-\operatorname{supp}f\) contained in one relatively compact region \(Y\subset X\). Use decomposition (L131.4) throughout that region.

The two compact factors \(f\) and \(\nu\) allow associativity:

\[
 f*(E_n*\nu)=(f*E_n)*\nu.
\]

If \(F=f*E_n\) is continuous, this is the function

\[
 x\longmapsto\int F(x-y)\,d\nu(y).
\]

On a compact output neighborhood, all arguments \(x-y\) lie in one compact set. Uniform continuity of \(F\) there, multiplied by the finite mass of \(\nu\), proves continuity of the integral. There is no assumption that \(F\) is globally bounded.

For \(f*h\), multiply the smooth local remainder by a smooth compact cutoff equal to one near \(\overline B-\operatorname{supp}f\). This changes no convolution value on \(B\). Pairing the resulting smooth translated functions with the compact distribution \(f\) gives a smooth function. The sum is continuous on \(B\), and these local functions agree wherever their domains overlap. [NP8](newtonian-potentials-formal.md#NP8) defines the local distribution convolution and proves all support conditions.

**Worked example: ordinary ball averages.** Let \(q_a=\mathbf1_{B(0,a)}/|B(0,a)|\). Its potential is continuous and equals, for \(r=|x|\),

\[
 E_2*q_a=\begin{cases}
 (2\pi)^{-1}\log a+(r^2-a^2)/(4\pi a^2),&r\le a,\\
 (2\pi)^{-1}\log r,&r\ge a,
 \end{cases}
\]

and, in dimension three,

\[
 E_3*q_a=\begin{cases}
 (r^2-3a^2)/(8\pi a^3),&r\le a,\\
 -1/(4\pi r),&r\ge a.
 \end{cases}
\]

Outside the averaging ball the kernel is harmonic in the averaging variable, so the ball average leaves it unchanged. Inside, the potential has constant Laplacian equal to the ball density; the radial solution is a quadratic plus a constant. Continuity fixes that constant. Values and first derivatives match at the boundary. NP10 derives the formulas, including every dimension above two.

Consequently \(q_a*v\) is continuous wherever the translated closed ball of radius \(a\) stays in \(X\). For \(X=B(0,R)\), this domain is exactly \(B(0,R-a)\) when \(0<a<R\).

![Exact kernels and ball averages in two and three dimensions; the critical integral in dimension three.](figures/kernel-integrability.png)

*Figure 2.* The averaging radius is one. The first two panels compare the point kernels with the explicitly calculated ball potentials; the latter stay finite at zero. The last panel plots the exact three-dimensional radial integrals \(1-\varepsilon\), \(\log(1/\varepsilon)\) and \(\varepsilon^{-1}-1\) for \(p=2,3,4\). Multiplying by \((4\pi)^{1-p}\) gives the truncated integral of \(|E_3|^p\). The logarithmic divergence is the excluded critical case.

## 5. What happens in one dimension

The one-dimensional fundamental kernel is \(E_1(x)=|x|/2\), whose derivative has jump one. A finite positive measure produces a locally Lipschitz potential, since

\[
 |(E_1*\nu)(x)-(E_1*\nu)(x')|\le\tfrac12\nu(\mathbb R)|x-x'|.
\]

The local zero-Laplacian remainder is affine. A nontrivial one-dimensional subharmonic function is therefore locally continuous, locally bounded and convex. The same convolution continuity argument applies when \(f*E_1\) is continuous. These are direct one-dimensional conclusions. The higher-dimensional expression \(n/(n-2)\) supplies no positive exponent for \(n=1\), so it is not used there. NP9 proves the supplement.

## 6. Exercises

1. Compute the flux of the higher-dimensional kernel through a sphere. Which sign of the kernel gives \(\Delta E=\delta_0\)?
2. In dimension three, find the divergence of the truncated kernel integral for \(p=3\) and \(p=4\).
3. A positive measure of mass \(M\) is supported in \(B(0,b)\). Bound its potential on \(B(0,c)\) in an admissible \(L^p\) norm.
4. For \(X=B(0,R)\) and the unit-mass ball density \(q_a\), determine the continuity domain, including its boundary.
5. Explain why \(f=\delta_0\), and then \(f=\partial_1\delta_0\), do not satisfy the continuity hypothesis in dimensions at least two.
6. Compute \(E_1*q_a\) for the uniform interval density \(q_a=\mathbf1_{(-a,a)}/(2a)\).

## 7. Complete solutions

**1.** The derivative is \(1/(s_nr^{n-1})\), so multiplying by the sphere area gives flux one. Its primitive tending to zero at infinity is \(-r^{2-n}/((n-2)s_n)\). The positive kernel instead gives flux minus one and \(\Delta E=-\delta_0\). For the planar logarithm, the same flux calculation is \(2\pi r\cdot(2\pi r)^{-1}=1\).

**2.** The three-dimensional truncated integral is \((4\pi)^{1-p}\int_\varepsilon^Rr^{2-p}\,dr\). At \(p=3\) this is \((4\pi)^{-2}\log(R/\varepsilon)\). At \(p=4\) it is \((4\pi)^{-3}(\varepsilon^{-1}-R^{-1})\). Both diverge as \(\varepsilon\to0\), logarithmically in the first case and by a reciprocal power in the second.

**3.** Since \(B(0,c)-B(0,b)\subset B(0,b+c)\), (L131.5) gives \(\|E_n*\nu\|_{L^p(B(0,c))}\le M\|E_n\|_{L^p(B(0,b+c))}\). Use \(p<n/(n-2)\) for \(n>2\), or any finite \(p\ge1\) for \(n=2\). If \(M=0\), the potential is zero. No absolute continuity of the measure is needed.

**4.** The support is \(\overline{B(0,a)}\), and the farthest point of \(x-\operatorname{supp}q_a\) from zero has distance \(|x|+a\). Thus \(|x|+a<R\) is necessary and sufficient, giving \(B(0,R-a)\). At equality the translated support touches \(\partial X\); it is not contained in the open set. If \(a\ge R\), this domain is empty.

**5.** For \(f=\delta_0\), \(f*E_n=E_n\), which is unbounded at zero. For \(f=\partial_1\delta_0\), the result is \(\partial_1E_n=x_1/(s_n|x|^n)\) away from zero. Along the positive first coordinate axis it diverges as \(r^{1-n}/s_n\). Neither distribution has a continuous representative at zero. Taking \(v=E_n\) also gives explicit failures of the proposed unconditional conclusion.

**6.** Direct integration gives

\[
 (E_1*q_a)(x)=\begin{cases}
 a/4+x^2/(4a),&|x|\le a,\\
 |x|/2,&|x|\ge a.
 \end{cases}
\]

At \(\pm a\), both values equal \(a/2\) and both first derivatives equal \(\pm1/2\). Inside the interval the second derivative is \(1/(2a)\); outside it is zero. Hence its distributional second derivative is precisely \(q_a\), without extra endpoint masses.

## Source credit

The classical result is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Chapter 16, Proposition 16.1.1, printed page 304 (PDF page 317). The [complete argument NP1–NP11](newtonian-potentials-formal.md), examples, solutions and diagrams are original exposition. The full proof supplies the positive-measure representation, Laplacian kernel, local estimate and harmonic smoothing argument used above.
