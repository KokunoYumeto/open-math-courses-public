# Boundary flux and weak identities

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

A boundary term records what differentiation sees when a function is cut off by a region. The indicator of the region is constant on each side, yet its derivative is a surface measure. This gives an efficient route from a local graph calculation to integration by parts, including vector fields whose ordinary derivatives need not all exist.

We use [Order, positivity and distributional limits](order-positivity-and-limits.md) for measures and finite-order test extensions, [Local data and compatible products](local-data-and-compatible-products.md) for localization, and [Weak equations and classical functions](weak-equations-and-classical-functions.md) for the distinction between weak and pointwise equations. Entry prerequisites are the \(C^1\) implicit function theorem, ordinary change of variables, compact cutoffs and partitions of unity. [Dyatlov 2026], §10.1.6, discusses the surface-measure distribution for a regular level set. An integrable weak divergence suffices for the flux identity proved below.

Basic references are Dyatlov’s notes cited below and Juha Heinonen’s *Lectures on Lipschitz Analysis* (2005), which places differentiable boundary graphs in the broader setting of Lipschitz maps.

## A boundary separates two local sides

Let \(Y\subset X\subset\mathbb R^n\) be open. Throughout, the boundary is relative to \(X\):

\[
\partial_XY=X\cap\partial Y.
\]

We say that \(Y\) has a \(C^1\) boundary in \(X\) if each boundary point has a neighborhood \(U\subset X\) and a real \(C^1\) function \(\rho\) such that

\[
Y\cap U=\{\rho<0\},\qquad
\partial_XY\cap U=\{\rho=0\},\qquad
\nabla\rho\ne0\ \text{on }\{\rho=0\}.
\tag{1.1}
\]

Shrinking a neighborhood around a point where the gradient is nonzero gives this form from the usual local definition. The implicit function theorem and a rotation turn the boundary into a graph. We can arrange the local side to be

\[
Y=\{(x',t):t<\gamma(x')\}.
\tag{1.2}
\]

Here and below such an equality is restricted to the chosen chart. Our normal always points **out of \(Y\)**. On (1.2),

\[
\nu(x',\gamma(x'))=
\frac{(-\nabla\gamma(x'),1)}
{\sqrt{1+|\nabla\gamma(x')|^2}},
\qquad
dS=\sqrt{1+|\nabla\gamma(x')|^2}\,dx'.
\tag{1.3}
\]

The second formula is the Euclidean surface element: the graph parametrization has Gram matrix \(I+\nabla\gamma(\nabla\gamma)^{\mathsf T}\), whose determinant is \(1+|\nabla\gamma|^2\). If two \(C^1\) parametrizations overlap, their Gram determinants transform by the square of the coordinate Jacobian. Ordinary change of variables therefore makes their integrals agree. These graph measures define one locally finite positive measure \(dS\) on \(\partial_XY\). A compact part of the boundary meets finitely many charts, and the graph densities are bounded on their compact subcharts. In dimension one, \(dS\) is counting measure on the locally isolated boundary points.

The gradient of any local defining function points to the positive side. Consequently \(\nabla\rho=|\nabla\rho|\nu\) on its zero set, including when a different chart is used.

**Proposition 1.1 (one defining function on the ambient open set).** A \(C^1\) boundary in \(X\) has a real \(\rho\in C^1(X)\) such that

\[
Y=\{\rho<0\},\qquad
\partial_XY=\{\rho=0\},\qquad
\nabla\rho\ne0\ \text{on }\partial_XY.
\tag{1.4}
\]

**Proof.** Cover the boundary by the neighborhoods in (1.1), and complete this to a cover of \(X\) by \(Y\) and \(X\setminus\overline Y\). The closure here is taken relative to \(X\). Choose a smooth locally finite partition subordinate to this cover, with each support contained in its assigned open set. Associate to a boundary chart its local defining function, to an interior chart the constant \(-1\), and to an exterior chart the constant \(1\). Form their partition-weighted sum.

Each summand, extended by zero beyond its chart, is \(C^1\): its partition factor has support inside that chart. Local finiteness gives a \(C^1\) function on \(X\). At an interior point every active local function is negative; at an exterior point each is positive. At a boundary point all active local functions vanish, and the interior and exterior partition factors vanish nearby. Thus the sum is zero precisely at the boundary and has the required negative set.

When differentiating the sum at a boundary point, the terms in which the derivative falls on the partition vanish because their defining functions are zero. The remaining gradient is

\[
\sum_i\chi_i\nabla\rho_i
=\left(\sum_i\chi_i|\nabla\rho_i|\right)\nu.
\tag{1.5}
\]

The weights are nonnegative, sum to one there, and every active gradient has positive length. The coefficient is strictly positive. This proves (1.4). The argument also covers an empty boundary using the constant functions on the open interior and exterior pieces. \(\square\)

No uniform lower bound on \(|\nabla\rho|\) over a noncompact boundary is asserted.

## The derivative of a region is its oriented surface measure

The indicator \(\chi_Y\) is locally integrable on \(X\). Values assigned on the boundary do not affect its distribution: a \(C^1\) graph has zero \(n\)-dimensional volume, and the boundary has a countable graph cover.

**Theorem 2.1 (indicator derivative and flux).** For every coordinate,

\[
\partial_j\chi_Y=-\nu_j\,dS
\quad\text{in }\mathcal D'(X).
\tag{2.1}
\]

Consequently every \(F\in C_c^1(X;\mathbb C^n)\) satisfies

\[
\int_Y\operatorname{div}F\,dx
=\int_{\partial_XY}F\cdot\nu\,dS.
\tag{2.2}
\]

The dot product in this complex-linear identity has no conjugation.

**Proof.** Work first in the graph chart (1.2), with a test \(\phi\) compactly supported there. Extend it by zero outside a smaller column containing its support. One-dimensional integration gives

\[
-\int_{t<\gamma(x')}\partial_t\phi(x',t)\,dx'\,dt
=-\int\phi(x',\gamma(x'))\,dx'.
\tag{2.3}
\]

For \(j<n\), put \(G(x')=\int_{-\infty}^{\gamma(x')}\phi(x',t)\,dt\). Differentiating this ordinary integral gives

\[
\partial_jG(x')
=\int_{-\infty}^{\gamma(x')}\partial_j\phi(x',t)\,dt
+\phi(x',\gamma(x'))\partial_j\gamma(x').
\]

Its integral is zero, because \(G\) is compactly supported. Therefore

\[
-\int_{t<\gamma(x')}\partial_j\phi\,dx
=\int\phi(x',\gamma(x'))\partial_j\gamma(x')\,dx'.
\tag{2.4}
\]

Equations (2.3)–(2.4) are exactly (2.1) using (1.3). Rotating coordinates rotates both sides as vectors. In a neighborhood inside or outside \(Y\) the derivative is zero. Local uniqueness for distributions now proves (2.1) on all of \(X\).

For a smooth compact field, pair (2.1) with its components:

\[
\int_Y\sum_j\partial_jF_j
=-\sum_j(\partial_j\chi_Y)(F_j)
=\int_{\partial_XY}\sum_jF_j\nu_j\,dS.
\]

Approximate a \(C_c^1\) field in \(C^1\), with one compact support neighborhood. Volume integrals and the integrals over the compact part of the boundary both converge. This proves (2.2) at its stated regularity. \(\square\)

Formula (2.1) says that every component of the derivative is a measure. Its support is contained in the boundary. The whole vector measure is \(-\nu\,dS\), so its total variation is \(dS\). Also

\[
\operatorname{singsupp}\chi_Y=\partial_XY:
\]

off the boundary the indicator is constant locally. At a boundary point a continuous representative would have to equal one on the open inside and zero on the open outside. Those two sides approach that point, which precludes continuity.

**Corollary 2.2 (a function cut off by a region).** If \(u\in C^1(X)\), then

\[
\partial_j(u\chi_Y)
=(\partial_j u)\chi_Y-u|_{\partial_XY}\nu_j\,dS.
\tag{2.5}
\]

**Proof.** Apply (2.2) to the compact \(C^1\) field \(u\phi e_j\), where \(\phi\) is a smooth test and \(e_j\) is a coordinate vector. Expand its ordinary divergence and rearrange:

\[
-\int_Yu\,\partial_j\phi
=\int_Y(\partial_ju)\phi
-\int_{\partial_XY}u\phi\nu_j\,dS.
\]

This is (2.5). Only the continuous boundary value of \(u\) is used in the surface term. \(\square\)

For the interval \(Y=(a,b)\), the outward normals at \(a,b\) are \(-1,1\), respectively. Thus \(\chi_Y'=\delta_a-\delta_b\). This checks the sign against the one-dimensional jump formula.

**Corollary 2.3 (complex notation in the plane).** Write \(z=x+iy\) and \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\). Orient the boundary so that \(Y\) lies to its left. For compact \(C^1\) \(\phi\),

\[
2\int_Y\partial_{\bar z}\phi\,dx\,dy
=-i\int_{\partial_XY}\phi\,dz,
\tag{2.6}
\]

and, on a smooth test,

\[
(\partial_{\bar z}\chi_Y)(\phi)
=\frac i2\int_{\partial_XY}\phi\,dz.
\tag{2.7}
\]

**Proof.** A positively oriented unit tangent is \((dx/ds,dy/ds)\). The outward normal is its right rotation, \((dy/ds,-dx/ds)\), so

\[
(\nu_x+i\nu_y)\,ds=dy-i\,dx=-i\,dz.
\]

Apply (2.2) to \((\phi,i\phi)\) for (2.6), and use (2.1) for (2.7). Compact support makes the integrals finite even for a noncompact relative boundary. \(\square\)

## Integration by parts with an integrable weak divergence

An arbitrary continuous field need not have ordinary coordinate derivatives. Its divergence still exists as a distribution. When that distribution is an integrable function on the region, continuity of the field supplies an ordinary boundary flux.

**Theorem 3.1 (weak Gauss–Green identity).** Suppose \(F\in C_c(X;\mathbb C^n)\) and its distributional divergence, restricted to \(Y\), is represented by \(g\in L^1(Y)\). Then, for every \(\phi\in C_c^1(X)\),

\[
\int_Y[g\phi+F\cdot\nabla\phi]\,dx
=\int_{\partial_XY}\phi F\cdot\nu\,dS.
\tag{3.1}
\]

In particular,

\[
\int_Yg\,dx=\int_{\partial_XY}F\cdot\nu\,dS.
\tag{3.2}
\]

**Proof.** It is enough first to prove (3.1) for a smooth test supported in one graph chart. Write \(d(x',t)=\gamma(x')-t\), which is positive inside \(Y\). Choose a real smooth nondecreasing \(H\) with \(H=0\) on \((-\infty,1/2]\) and \(H=1\) on \([1,\infty)\). Set

\[
\chi_\varepsilon(x',t)=H(d(x',t)/\varepsilon).
\]

The \(C^1\) test \(\phi\chi_\varepsilon\) has compact support strictly inside \(Y\). The weak-divergence identity extends to such \(C^1\) tests by \(C^1\) approximation within that open set: \(g\) is integrable on the compact neighborhood, and \(F\) is bounded there. Hence

\[
\int_Yg\phi\chi_\varepsilon
=-\int_Y\chi_\varepsilon F\cdot\nabla\phi
-\int_Y\phi F\cdot\nabla\chi_\varepsilon.
\tag{3.3}
\]

The first two integrals converge by dominated convergence. For the last integral, use

\[
\nabla\chi_\varepsilon
=\varepsilon^{-1}H'(d/\varepsilon)(\nabla\gamma,-1).
\]

Changing \(t=\gamma(x')-\varepsilon r\) turns its negative into

\[
\int\!\!\int_{1/2}^{1}
H'(r)\phi(x',\gamma(x')-\varepsilon r)
F(x',\gamma(x')-\varepsilon r)
\cdot(-\nabla\gamma(x'),1)\,dr\,dx'.
\tag{3.4}
\]

The integrands have common compact \(x'\)-support. The functions \(F,\phi,\nabla\gamma\) are bounded there, and continuity gives the limit under the integral. Since \(\int_{1/2}^1H'=1\), the result is

\[
\int\phi(x',\gamma(x'))F(x',\gamma(x'))
\cdot(-\nabla\gamma(x'),1)\,dx'
=\int_{\partial_XY}\phi F\cdot\nu\,dS.
\]

This proves the localized formula. For a test supported in the interior of \(Y\), it is precisely the defining weak identity with no boundary term. For a test supported in the exterior both sides vanish. Decompose any compact test with a finite partition across those neighborhoods and the boundary charts. Summing proves (3.1) for smooth tests, because the derivatives of the partition sum to zero. Compact \(C^1\) approximation then gives its stated test class.

Finally choose a compact smooth \(\phi\) equal to one on a neighborhood of \(\operatorname{supp}F\). Inside \(Y\), the function \(g\) is zero almost everywhere away from \(\operatorname{supp}F\): its distribution there is the divergence of the zero field. Thus \(g\phi=g\), \(F\cdot\nabla\phi=0\), and the boundary factor \(\phi\) is one wherever \(F\) is nonzero. Equation (3.1) gives (3.2). \(\square\)

The proof uses the weak divergence only on \(Y\). No representative for it outside \(Y\) enters the argument.

## Cubes and a pointwise equation with a rough gradient

Cubes have corners, so they do not meet our \(C^1\) boundary definition. The flux formula for a compact coordinate cube \(Q=\prod_j[a_j,b_j]\subset X\) follows directly by integrating each \(\partial_jF_j\) along its coordinate interval:

\[
\int_Q\operatorname{div}F\,dx
=\sum_{\text{faces }S}\int_SF\cdot\nu_S\,dS,
\qquad F\in C^1\text{ near }Q.
\tag{4.1}
\]

The normal \(\nu_S\) is the constant outward face normal. Intersections of faces have zero face measure when \(n\ge2\); in dimension one the right side is the endpoint difference. Opposite fluxes cancel on shared faces in a subdivision.

We can now address a subtle implication. Knowing that \(u\) is differentiable at every point need not make its derivative continuous, bounded or locally integrable. Even so, a continuous first-order equation satisfied at every point has the expected weak meaning.

**Theorem 4.1 (an everywhere pointwise identity is weak).** Let

\[
P=\sum_{j=1}^n a_j(x)\partial_j+b(x),
\qquad a_j\in C^1(X),\quad b\in C(X).
\tag{4.2}
\]

The coefficients may be complex. Suppose \(u:X\to\mathbb C\) is differentiable at every point and that the pointwise function \(Pu\) equals a continuous \(f\). Then

\[
Pu=f\quad\text{in }\mathcal D'(X).
\tag{4.3}
\]

Here multiplication of \(a_j\) with \(\partial_ju\) uses the order-one extension to \(C^1\) tests. Equivalently, (4.3) means

\[
\int_Xu\left[b\phi-\sum_j\partial_j(a_j\phi)\right]dx
=\int_Xf\phi\,dx
\quad(\phi\in C_c^\infty(X)).
\tag{4.4}
\]

**Proof.** Differentiability implies continuity, so \(u\) is locally integrable. Fix a smooth compact test \(\phi\). For each compact coordinate cube \(Q\subset X\), define its integration defect by

\[
D(Q)=
\int_Q\left[f\phi+
u\left(\sum_j\partial_j(a_j\phi)-b\phi\right)\right]dx
-\int_{\partial Q}u\phi\,a\cdot\nu_Q\,dS,
\tag{4.5}
\]

where \(a=(a_1,\ldots,a_n)\) and the last integral is the face sum. All integrands are continuous. The defect is additive under a dyadic subdivision: the volume integrals add, and shared faces have equal traces with opposite normals.

Fix \(x_0\in X\) and replace \(u\) by its affine approximation

\[
v(x)=u(x_0)+du(x_0)(x-x_0).
\]

For \(v\), with the forcing \(Pv\), formula (4.1) applied to \(v\phi a\) makes the defect zero. Subtracting that identity from (4.5) gives

\[
\begin{aligned}
D(Q)={}&\int_Q(f-Pv)\phi\,dx\\
&+\int_Q(u-v)\left(\sum_j\partial_j(a_j\phi)-b\phi\right)dx\\
&-\int_{\partial Q}(u-v)\phi\,a\cdot\nu_Q\,dS.
\end{aligned}
\tag{4.6}
\]

Consider cubes containing \(x_0\) with side length \(s\downarrow0\). Since \(f(x_0)=Pu(x_0)=Pv(x_0)\) and \(Pv\) is continuous, the first integral is \(o(s^n)\). Differentiability gives \(\sup_Q|u-v|=o(s)\). The bounded coefficient in the second line therefore gives \(o(s^{n+1})\). There are \(2n\) faces of area \(s^{n-1}\), so the last line is \(o(s^n)\). Thus, at each fixed point,

\[
\frac{D(Q)}{|Q|}\longrightarrow0
\quad\text{for cubes }Q\ni x_0,\ s(Q)\downarrow0.
\tag{4.7}
\]

This pointwise estimate is sufficient; it need not be uniform over \(X\). Indeed, suppose some cube \(Q_0\) had nonzero defect. Additivity and the triangle inequality select one dyadic child \(Q_1\) with

\[
\frac{|D(Q_1)|}{|Q_1|}
\ge\frac{|D(Q_0)|}{|Q_0|}.
\]

Repeat to obtain nested closed cubes \(Q_l\), all compactly inside \(X\), whose sides tend to zero and whose defect ratios stay bounded below by a positive number. Their intersection is a single point \(x_*\). Each cube contains \(x_*\), so (4.7) gives a contradiction. Hence \(D(Q)=0\) on every compact cube.

If the support of \(\phi\) lies inside the interior of one such cube, its boundary integral vanishes, and \(D(Q)=0\) is (4.4). Any compact test can be split into finitely many tests supported in cube interiors. Summing their identities proves (4.4) in general. This also verifies the precise meaning of (4.3), without treating the pointwise gradient of \(u\) as an integrable function. \(\square\)

For example, set \(u(0)=0\) and \(u(x)=x^2\sin(x^{-2})\) for \(x\ne0\). It is differentiable at zero with derivative zero. Its derivative away from zero contains \(-2x^{-1}\cos(x^{-2})\), which is not locally absolutely integrable. Nevertheless

\[
x^2u'(x)=
2x^3\sin(x^{-2})-2x\cos(x^{-2}),\qquad x\ne0,
\tag{4.8}
\]

extends continuously with value zero at the origin. The theorem gives (4.8) as a distributional equation too.

## Exercises

1. **A tilted interface — foundation.** In the plane let \(Y=\{y<2x\}\). Define the graph measure \(M\) by \(M(\phi)=\int_{\mathbb R}\phi(x,2x)\,dx\). Compute \(\partial_x\chi_Y\), \(\partial_y\chi_Y\), and both partial derivatives of \((1+x^2)\chi_Y\). Distinguish \(M\) from Euclidean arclength measure.
2. **A hole reverses the normal — intermediate.** For \(n\ge2\), let \(Y=\{1<|x|<2\}\). Show \(\rho=(|x|^2-1)(|x|^2-4)\) is a global defining function. Write \(\nabla\chi_Y\) as its two surface measures. Calculate the fluxes of \(x/|x|^n\) through the two spheres, using a smooth compact cutoff that equals one near \(\overline Y\).
3. **A continuous field without all ordinary derivatives — intermediate.** On \(\mathbb R^2\), put \(Y=\{y<x^2\}\) and \(F(x,y)=(0,|x|^{1/2}\eta(x,y))\), where \(\eta\in C_c^\infty(\mathbb R^2)\). Determine the weak divergence and both sides of (3.2). Explain why the nonexistence of \(\partial_xF_2\) at many points of the vertical axis causes no extra boundary term.
4. **Why “every point” matters — advanced.** Subdivide \([0,1]^n\) dyadically. Choose an interior point \(p\) with no dyadic-rational coordinate, and put \(D(Q)=1\) if a dyadic cube contains \(p\), \(D(Q)=0\) otherwise. Verify dyadic additivity. Show the small-cube density limit is zero at every point except \(p\), although \(D([0,1]^n)=1\). Identify the exact step of the proof of Theorem 4.1 that would fail with an almost-everywhere hypothesis.
5. **An unbounded gradient in a continuous equation — advanced.** For the function in (4.8), prove differentiability at zero and failure of local absolute integrability of its pointwise derivative. Verify the continuous pointwise forcing in \(x^2u'=f\), and explain the meaning of this equality on a test.
6. **The planar sign — foundation.** Let \(Y=\{|z|<R\}\), \(R>0\), and choose a smooth compact \(\phi\) equal to \(\bar z\) on a neighborhood of \(\overline Y\). Compute \((\partial_{\bar z}\chi_Y)(\phi)\) both from its defining volume pairing and from the counterclockwise boundary integral in (2.7).

## Complete solutions

**Solution 1.** Here \(\nu=(-2,1)/\sqrt5\) and \(dS=\sqrt5\,dM\). Therefore

\[
\partial_x\chi_Y=2M,\qquad
\partial_y\chi_Y=-M.
\]

Use (2.5) with \(u=1+x^2\):

\[
\partial_x[(1+x^2)\chi_Y]
=2x\chi_Y+2(1+x^2)M,\qquad
\partial_y[(1+x^2)\chi_Y]=-(1+x^2)M.
\]

The coefficients on \(M\) are evaluated on its graph. \(M\) integrates the \(x\)-parameter without a Jacobian, whereas \(dS\) includes the constant speed \(\sqrt5\).

**Solution 2.** The defining function is negative exactly for \(1<|x|^2<4\), zero on both spheres, and positive elsewhere. Its gradient is \(2x(2|x|^2-5)\), equal to \(-6x\) at radius one and \(6x\) at radius two. Thus it is nonzero on the boundary and points in the outward direction on both components. If \(dS_1,dS_2\) denote their Euclidean measures,

\[
\nabla\chi_Y=x\,dS_1-\frac x2\,dS_2.
\]

The first sphere's outward normal relative to the annulus is \(-x\), while the second's is \(x/2\). For \(V=x/|x|^n\), ordinary differentiation gives

\[
\operatorname{div}V
=n|x|^{-n}-n|x|^{-n-2}|x|^2=0
\quad(x\ne0).
\]

Take a smooth cutoff supported in an annular neighborhood of \(\overline Y\), equal to one near it; its product with \(V\), extended by zero near the origin, is a smooth compact field. Write \(\omega_n=|S^{n-1}|\). At radius two its outward flux is \(2^{1-n}\omega_n2^{n-1}=\omega_n\). At radius one it is \(-\omega_n\). They cancel, agreeing with the zero bulk divergence. Treating both sphere normals as radial outward would give an incorrect nonzero sum.

**Solution 3.** Fubini and one-dimensional integration by parts in \(y\) show

\[
\operatorname{div}F=|x|^{1/2}\partial_y\eta(x,y)
\]

on the whole plane. This is a continuous compactly supported function, hence integrable. The graph has \(\nu=(-2x,1)/\sqrt{1+4x^2}\) and \(dS=\sqrt{1+4x^2}\,dx\). Thus

\[
\int_{\partial Y}F\cdot\nu\,dS
=\int_{\mathbb R}|x|^{1/2}\eta(x,x^2)\,dx.
\]

For the bulk integral, integrate \(|x|^{1/2}\partial_y\eta\) from \(-\infty\) to \(x^2\). Compact support makes the lower endpoint zero and gives the same expression. Where \(\eta(0,y)\ne0\), the difference quotient for \(F_2\) in the \(x\)-direction has magnitude comparable to \(|h|^{-1/2}\), so that partial does not exist. Divergence differentiates \(F_1\) in \(x\) and \(F_2\) in \(y\); no \(\partial_xF_2\) occurs. The continuous trace of \(F\) determines the boundary term.

**Solution 4.** Since no coordinate of \(p\) lies on a dyadic face, each dyadic parent containing \(p\) has exactly one child containing it. The sum of the child values is therefore its own value, including when that value is zero. At any \(x\ne p\), a sufficiently small cube containing \(x\) has diameter less than \(|x-p|\), so it does not contain \(p\) and its defect ratio is zero. The unique nested sequence containing \(p\) has ratio \(1/|Q|\), which tends to infinity. The top cube has value one.

The contradiction in Theorem 4.1 needs the vanishing density limit at the intersection point selected by the nested cubes. That point could belong to an exceptional set of volume zero; here it is exactly \(p\). Almost-everywhere vanishing does not rule out a singular defect concentrated at that point.

**Solution 5.** The difference quotient at zero is \(u(h)/h=h\sin(h^{-2})\), tending to zero. At a nonzero point,

\[
u'=2x\sin(x^{-2})-\frac2x\cos(x^{-2}).
\]

The first term is integrable near zero. For the second, on the positive side the substitution \(s=x^{-2}\) gives

\[
\int_0^\varepsilon\frac{2|\cos(x^{-2})|}{x}\,dx
=\int_{\varepsilon^{-2}}^\infty\frac{|\cos s|}{s}\,ds.
\]

On a fixed positive-length portion of each period, \(|\cos s|\ge1/2\). The corresponding integrals dominate a constant times the divergent harmonic series. Thus \(u'\) is not locally absolutely integrable.

Multiplication by \(x^2\) gives (4.8), whose two terms tend to zero. At zero the pointwise product \(x^2u'(x)\) is also zero. Theorem 4.1 applies with \(a=x^2\), \(b=0\) and this continuous \(f\). Its weak meaning is

\[
-\int_{\mathbb R}u(x)\,[x^2\phi(x)]'\,dx
=\int_{\mathbb R}f(x)\phi(x)\,dx
\quad(\phi\in C_c^\infty(\mathbb R)).
\]

These integrals exist because \(u,f\) are continuous on compact sets. The left side is the finite-order pairing of \(u'\) with \(x^2\phi\), rather than an integral of the nonintegrable pointwise derivative.

**Solution 6.** On \(Y\), \(\partial_{\bar z}\phi=\partial_{\bar z}\bar z=1\). Therefore the defining pairing gives \(-\pi R^2\). Parametrize the circle by \(z=Re^{it}\), \(0\le t\le2\pi\), so that \(\bar z\,dz=iR^2dt\). Formula (2.7) gives

\[
\frac i2\int_0^{2\pi}iR^2\,dt=-\pi R^2.
\]

The agreement checks both the orientation and the factor \(1/2\).

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026, §10.1.6, Proposition 10.12, regular level sets and surface measure. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- Juha Heinonen, *Lectures on Lipschitz Analysis*, Report 100, University of Jyväskylä, 2005, §3, almost-everywhere differentiability. This gives a starting point for extending graph calculations below \(C^1\) boundary regularity. [Full text](https://jyx.jyu.fi/handle/123456789/22526).
