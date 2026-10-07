# Boundary measures and Green potentials in a half-space

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Original proof exposition, examples and diagrams: CC0 1.0.

An interior point mass creates a downward singularity in a subharmonic function. Boundary data create a harmonic function. A third harmonic contribution can grow linearly with height. In a half-space these three effects have explicit kernels, and a linear upper bound is enough to separate them uniquely.

This lesson proves the representation, including the boundary limit when no ordinary boundary function exists. The [complete proof GR1–GR11](half-space-green-riesz-formal.md) retains the constructions and estimates behind every step. Its written inputs are [the local Newtonian potential argument](../../AN02-L131.html#NP2), [the ball Poisson formula](../../AN02-L132.html#the-unit-ball-poisson-operator), and [the horizontal-envelope slope theorem](../../AN02-L133.html#the-asymptotic-slope-and-the-increment-bound).

## 1. Three terms, two measures and one slope

Work in dimension \(n\ge2\), with \(x=(z,t)\) and \(t>0\). Suppose \(v\) is upper semicontinuous, subharmonic, not identically \(-\infty\), and

\[
 v(z,t)\le C_0+C_1t.
 \tag{L135.1}
\]

Let \(s_n\) be the area of the unit sphere. For \(\Delta E_n=\delta_0\), the fundamental kernel is

\[
 E_n(x)=-\frac{|x|^{2-n}}{(n-2)s_n}\ (n>2),
 \qquad E_2(x)=\frac{\log|x|}{2\pi}.
\]

Reflect \(y=(\eta,s)\) across the boundary to \(y^*=(\eta,-s)\). The Green and Poisson kernels are

\[
 G(x,y)=E_n(x-y)-E_n(x-y^*),\qquad
 P(x,\eta)=\frac{2t}{s_n(|z-\eta|^2+t^2)^{n/2}}.
 \tag{L135.2}
\]

The first is nonpositive, has Laplacian \(\delta_y\) in the upper half-space and vanishes on its boundary. The second is positive and harmonic and has integral one over the whole boundary plane.

There is a unique signed boundary measure \(\sigma\), while the interior positive measure is \(\mu=\Delta v\). The slope is the previously proved limit

\[
 \gamma=\lim_{t\to\infty}\frac{\sup_zv(z,t)}t\in\mathbb R.
\]

The representation is

\[
 v(z,t)=\int P((z,t),\eta)\,d\sigma(\eta)
       +\int G((z,t),y)\,d\mu(y)+\gamma t.
 \tag{L135.3}
\]

The boundary integral is finite. The Green integral can equal \(-\infty\) at an interior singularity. Its required weight is

\[
 \int (1+|\eta|)^{-n}d|\sigma|(\eta)<\infty,
 \qquad \int s(1+|y|)^{-n}d\mu(y)<\infty.
 \tag{L135.4}
\]

These allow infinite total mass. Each horizontal slice of \(v\) is locally integrable, and for every continuous compactly supported \(\phi\),

\[
 \int v(z,t)\phi(z)dz\longrightarrow\int\phi\,d\sigma
 \quad(t\downarrow0).
 \tag{L135.5}
\]

Thus the boundary values exist as a weak limit of measures. They need not be finite pointwise values or have a density. The upper bound implies the useful inequality \(\sigma\le C_0\,dz\).

## 2. A reflected pole enforces zero boundary values

At a boundary point the distances to \(y\) and \(y^*\) agree. Subtracting their potentials makes the boundary value zero. Inside, the reflected pole is farther away; because \(E_n\) increases with radius, the difference is negative.

Write \(r_-=|x-y|\), \(r_+=|x-y^*|\). Since \(r_+^2-r_-^2=4ts\), the same identity works in dimensions two and above:

\[
 -G(x,y)=\frac{2ts}{s_n}\int_0^1(r_-^2+4\theta ts)^{-n/2}d\theta.
 \tag{L135.6}
\]

Bounding the denominator at either endpoint gives the precise estimates used for both existence and decay. In particular a finite value of the Green potential at one interior point controls the interior weight in (L135.4). This replaces any need to assume finite total mass.

The Poisson kernel is \(2\partial_tE_n(z-\eta,t)\). To check its normalization, project the boundary plane onto the upper unit hemisphere by \(q\mapsto(q,1)/\sqrt{1+|q|^2}\). Its surface Jacobian is \((1+|q|^2)^{-n/2}\), so its integral is half the sphere area. Scaling by height proves \(\int P\,d\eta=1\). Its tails outside a fixed boundary radius have mass at most a constant times \(t\) divided by that radius; therefore its averages approach continuous boundary data uniformly. [GR3](half-space-green-riesz-formal.md#GR3) gives the calculations.

![The source, its reflection and the boundary Poisson density.](figures/reflected-green.png)

*Figure 1.* The planar source is \((0.6,1.2)\), its reflection \((0.6,-1.2)\), and the marked observation point \((-0.8,1.6)\). The squared distances are 2.12 and 9.8, so the Green value there is \((4\pi)^{-1}\log(2.12/9.8)\). The potential is zero on the boundary and has a downward singularity at the source; the color scale is clipped near that pole as stated on the plot. The boundary curve is \(1/(\pi(1+\eta^2))\), whose integral over the whole line is one. These are exact kernels sampled for display. See GR8–GR12 of the complete proof.

## 3. Extract the full interior potential

The slope theorem shows that \(\sup_zv(z,t)-\gamma t\) is nonincreasing. Compare height \(t\) with a smaller height \(a\), use (L135.1), then let \(a\downarrow0\). This gives

\[
 \widetilde v=v-C_0-\gamma t\le0.
\]

Its limiting horizontal slope is zero.

Cut off a finite portion \(\chi\mu\) of the interior mass and subtract its reflected Green potential. At a shared singularity, form this remainder as a distribution and recover its unique subharmonic representative. The local Newtonian construction and harmonic smoothing prove that this representative exists: a distribution with positive Laplacian is locally a positive-mass potential plus a smooth harmonic function.

The remainder has Laplacian \((1-\chi)\mu\ge0\). The compact potential tends uniformly to zero near the boundary and at infinity. Outside a sufficiently large compact subset of the half-space, the remainder is at most any prescribed \(\varepsilon>0\). The written compact maximum principle gives the same bound inside. Thus the remainder is nonpositive everywhere.

Increase the cutoffs to one. Their Green potentials decrease and stay between \(\widetilde v\) and zero. Local \(L^1\) integrability of \(\widetilde v\) gives an integrable bound, so the potentials converge in local \(L^1\). Their limit is \(G\mu\), with Laplacian \(\mu\). What remains is a smooth harmonic function \(h\le0\), and

\[
 \widetilde v=h+G\mu,
 \qquad \widetilde v\le h\le0.
\]

The envelope of \(h\), divided by height, consequently tends to zero. [GR4–GR6](half-space-green-riesz-formal.md#GR4) prove the cutoff, limit and weighted-mass steps.

## 4. A sphere atom explains linear growth

We need a representation for the nonnegative harmonic function \(-h\). A positive harmonic function on the ball is the Poisson integral of a finite positive sphere measure. To construct that measure, use the boundary values on smaller concentric spheres: their total mass is fixed by the mean-value identity. A countable approximation of continuous tests gives a convergent subsequence of the measures; the ball Poisson formula passes to the limit and identifies the function. Its boundary approximate identity makes the measure unique.

Now use the inversion

\[
 T(y)=-e+\frac{2(y+e)}{|y+e|^2},\qquad e=(0,\ldots,0,1).
 \tag{L135.7}
\]

It maps the ball to the half-space. If \(u\ge0\) is harmonic in the half-space, then \(|y+e|^{2-n}u(T(y))\) is harmonic on the ball; differentiating proves the identity in every \(n\ge2\), with multiplier one when \(n=2\).

All sphere points except \(-e\) become finite boundary points. The point \(-e\) corresponds to infinity. Its atom becomes \(a t\), where \(a\ge0\); the rest becomes a positive weighted boundary measure \(\rho\). The result is

\[
 u(z,t)=a t+\int P((z,t),\eta)d\rho(\eta).
\]

For \(u=-h\), a positive \(a\) would force \(h\le-a t\), contradicting its already established zero limiting slope. Hence \(a=0\). Adding back \(C_0+\gamma t\) gives (L135.3), with \(\sigma=C_0\,dz-\rho\). [GR7–GR9](half-space-green-riesz-formal.md#GR7) prove the sphere-measure construction, inversion, exact mass factors and this conclusion.

![The ball-to-half-space inversion and the linear term at infinity.](figures/ball-to-half-space.png)

*Figure 2.* In dimension two, sphere masses 1 at \((0,1)\), 1 at \((1,0)\) and \(\pi/2\) at \((0,-1)\) become boundary masses \(1/2\) at 0, 1 at 1, and the coefficient \(1/4\) of height. The displayed positive harmonic function is \(u=P((z,t),0)/2+P((z,t),1)+t/4\). Its negative satisfies the theorem's upper bound. The atom at infinity is a sphere atom under the stated inversion, rather than a finite boundary location. See GR25–GR28 and Example 2.

## 5. Why the Green term has no boundary measure

One exact integral captures its behavior:

\[
 \int_{\mathbb R^{n-1}}-G((z,t),(\eta,s))dz=\min(t,s).
 \tag{L135.8}
\]

To derive it, integrate the vertical derivative of the fundamental kernel from height \(t-s\) to \(t+s\), away from the single horizontal source coordinate, which has Lebesgue measure zero. Its horizontal integral is \(\operatorname{sgn}(a)/2\); its absolute horizontal integral is \(1/2\). Fubini is therefore justified over that finite interval, and integrating the sign gives the minimum.

For a compact boundary test, this identity bounds the pairing with a fixed interior source by \(\|\phi\|_\infty\min(t,s)\), which tends to zero. The far-source estimate from (L135.6) supplies the common majorant \(C_\phi s(1+|y|)^{-n}\). Dominated convergence against the interior measure proves zero weak trace for the whole Green potential.

The Poisson term converges to its boundary measure by its approximate identity and the boundary weight. The height term tends to zero on compact boundary tests. Their sum proves (L135.5). It also establishes local integrability on every slice, including a height containing a Green pole. [GR10](half-space-green-riesz-formal.md#GR10) gives the bounds for continuous compact tests.

## 6. A complete example

In the plane let \(y=(0.6,1.2)\), and set

\[
 v(z,t)=G((z,t),y)-\frac{t}{\pi(z^2+t^2)}-\frac t4.
\]

All three terms of the representation are visible. The interior measure is \(\delta_y\), the boundary measure is \(-\delta_0\), and the slope is \(-1/4\). The function is at most \(-t/4\). At fixed height its first two terms approach zero as \(|z|\to\infty\), so its supremum is exactly \(-t/4\), approached without being attained. Its weak boundary limit pairs with \(\phi\) as \(-\phi(0)\), even though its values near the boundary atom become arbitrarily negative.

The complete proof also treats the affine function \(b+ct\), whose boundary measure \(b\,dz\) has infinite total variation but finite required weight, and Figure 2's harmonic boundary-atom example.

## 7. Exercises and complete solutions

**Exercise 1.** Explain the sign of the planar Green kernel.

**Solution.** It is \((2\pi)^{-1}\log(r_-/r_+)\). For positive source and observation heights, \(r_-<r_+\), so it is negative. At the boundary the distances agree and it is zero. At the source its value is \(-\infty\), with distributional Laplacian the positive point mass.

**Exercise 2.** Why does the interior weight include source height \(s\)?

**Solution.** The difference of squared distances is exactly \(4ts\). Formula (L135.6) therefore has numerator proportional to \(s\). At a fixed interior point the lower estimate is a positive constant times \(s(1+|y|)^{-n}\). A finite Green value controls that weighted mass, including sources approaching the boundary. Removing \(s\) would assert a stronger condition unsupported by this estimate.

**Exercise 3.** Evaluate (L135.8) for \(t=1,s=3\), and for \(t=3,s=1\).

**Solution.** In the first case the derivative interval is \([-2,4]\); half the signed length is \((4-2)/2=1\). In the second it is \([2,4]\), with half its length equal to one. Both equal \(\min(t,s)\). The sign factor \(1/2\) comes from half the normalized Poisson mass.

**Exercise 4.** Convert a planar sphere atom of mass \(\pi\) at \(-e\) to a harmonic half-space term.

**Solution.** The sphere area is \(2\pi\), so its height coefficient is \(\pi/(2\pi)=1/2\). It contributes \(t/2\) to the positive harmonic function. Its negative contributes \(-t/2\). It does not give a finite boundary atom.

**Exercise 5.** Compare positive and negative boundary atoms with the linear upper bound.

**Solution.** A positive atom gives \(P((0,t),0)=2/(s_nt^{n-1})\), which diverges to \(+\infty\) as \(t\downarrow0\). A fixed linear height bound stays finite there. A negative atom gives a nonpositive harmonic function and satisfies the bound with both constants zero. This is consistent with \(\sigma\le C_0\,dz\).

**Exercise 6.** Determine the boundary trace in the example of section 6.

**Solution.** The Green pairing is bounded by \(\|\phi\|_\infty\min(t,1.2)\to0\). The negative Poisson pairing tends to \(-\phi(0)\). The height pairing is \(-t\int\phi/4\to0\). Hence the limit is \(-\phi(0)\), the pairing with \(-\delta_0\). No value at the singular interior point is needed in this integration.

## Source credit

Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (1983 edition; second revised printing 1990; reprint 2005), §16.1, Theorem 16.1.7, printed pp. 310–312 (PDF pp. 323–325). The [complete original argument](half-space-green-riesz-formal.md) proves the half-space representation, both weighted conditions and the weak boundary trace. The ball appears as the explicitly linked harmonic tool.
