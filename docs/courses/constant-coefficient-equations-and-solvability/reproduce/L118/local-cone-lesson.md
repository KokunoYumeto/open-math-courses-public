# Tangent cones that permit an imaginary push

A characteristic polynomial may vanish at a real frequency, yet become nonzero when that frequency is pushed a little in a permitted imaginary direction. The permitted directions depend on the tangent polynomial at the frequency. This lesson explains their variation and proves that a compact family of such pushes can use one small parameter and one power bound.

The proof companion is [Local tangent cones and small imaginary deformations](local-cone-proof.md), LC035-1 through LC035-6. This lesson uses the preceding tangent-hyperbolicity input C1/D1 and elementary complex analysis D4. It supplies the homogeneous polynomial portion needed by AN-02's sphere and equatorial cycle constructions. It does not supply the general analytic wavefront or topological component theorems.

## The object and its positive polar

Let \(F\) be a real homogeneous polynomial of degree \(m\ge1\), hyperbolic in \(N\). At a nonzero real frequency \(\xi\), retain the first nonzero homogeneous term of its Taylor expansion:
\[
 F(\xi+h)=H_\xi(h)+\text{terms of higher degree},\qquad \deg H_\xi=\mu_\xi.
\]
The preceding tangent theorem makes \(H_\xi\) hyperbolic in \(N\). Its component \(\Gamma_\xi\) is the component of \(N\) in \(\{H_\xi\ne0\}\). It is open and convex. Its positive polar is
\[
 C_\xi=\{x:x\cdot v\ge0\text{ for every }v\in\Gamma_\xi\}.
\]
At a noncharacteristic frequency \(F(\xi)\ne0\), the tangent degree is zero. The component is all of \(\mathbb R^n\), its positive polar is \(\{0\}\), and the imaginary field value may be zero. At a characteristic point the tangent degree is positive and zero is outside the permitted component.

Two conclusions describe the variation precisely. Every fixed permitted vector at \(\xi_0\) remains permitted at all sufficiently nearby frequencies. The same real neighborhood works for a compact set of permitted vectors. Conversely, if \(\xi_j\to\xi\ne0\), \(x_j\to x\), and \(x_j\in C_{\xi_j}\), then \(x\in C_\xi\). The second conclusion follows by testing each fixed \(v\in\Gamma_\xi\) in the first conclusion and passing \(x_j\cdot v\ge0\) to the limit. It uses the positive-polar sign exactly as written.

These conclusions allow jumps of tangent degree and cone shape. They do not assert that the tangent-polynomial coefficients vary continuously after normalizing their changing degrees.

## Example 1: a crossing, a simple point, and a noncharacteristic point

Take
\[
 F(\tau,\eta_1,\eta_2)=(\tau-\eta_1)(\tau-\eta_2),\qquad N=(1,0,0).
\]
Each factor along an \(N\)-line has a real root, so \(F\) is hyperbolic. At \(\xi_0=(1,1,1)\),
\[
 H_{\xi_0}(v)=(v_\tau-v_1)(v_\tau-v_2),\quad
 \Gamma_{\xi_0}=\{v_\tau>v_1,\ v_\tau>v_2\}.
\]
Both factors are positive at \(N\); their signs cannot change within a nonzero component. This identifies the component containing \(N\). Its polar is
\[
 C_{\xi_0}=\{s(1,-1,0)+t(1,0,-1):s,t\ge0\}.
\]
To see the reverse inclusion in this polar formula, use the freely variable positive quantities \(a=v_\tau-v_1\), \(b=v_\tau-v_2\), and the freely variable \(v_\tau\). Then
\[
 x\cdot v=(x_\tau+x_1+x_2)v_\tau-x_1a-x_2b.
\]
Nonnegativity for all such choices forces \(x_\tau+x_1+x_2=0\), \(x_1\le0\), \(x_2\le0\), exactly the displayed nonnegative span.

At \(\xi_d=(1,1,1+d)\), \(d\ne0\), only the first factor vanishes:
\[
 H_{\xi_d}(v)=-d(v_\tau-v_1),\quad
 \Gamma_{\xi_d}=\{v_\tau>v_1\},\quad
 C_{\xi_d}=\mathbb R_+(1,-1,0).
\]
The nonzero scalar \(-d\) does not change the component containing \(N\), even when \(d\) changes sign. At \(\zeta_d=(1,1+d,1+d)\), both factors are nonzero for \(d\ne0\): the tangent degree is zero, every direction is permitted, and the polar is zero.

![Exact component and polar slices at a crossing, a simple characteristic, and a noncharacteristic point.](figures/crossing-cone-variation.png)

*Figure 1.* The upper row shows the exact affine slice \(v_\tau=1\): a quadrant at the crossing, the halfplane \(v_1<1\) at the simple point, and the whole plane at the noncharacteristic point. The lower row shows the exact polar slice \(x_\tau=1\): the segment between \((-1,0)\) and \((0,-1)\), one endpoint, and the empty slice because the polar is \(\{0\}\). All plots are two-coordinate affine slices of the stated three-dimensional cones. The excluded boundaries in the upper row are dashed; the included polar segment and point are solid. The marked vector \(N\) is permitted in all three cases. Proof locators: LC035-3–4 and the calculations above.

In fact this example has an exact denominator inequality near the crossing. If \(\theta_\tau-\theta_j\ge a>0\), \(j=1,2\), then for every real \(w\) and every \(\varepsilon>0\),
\[
 |F(w\pm i\varepsilon\theta)|
 =\prod_{j=1}^2\sqrt{(w_\tau-w_j)^2+
       \varepsilon^2(\theta_\tau-\theta_j)^2}
 \ge a^2\varepsilon^2.
\]
The local center has tangent degree two. The same bound remains valid at neighboring simple and noncharacteristic points; it is not always their sharp bound.

## Why a root cluster gives a power bound

Fix a characteristic center \(\xi_0\) and a compact set of unit directions strictly inside \(\Gamma_{\xi_0}\). Enlarge it to a compact connected angular section containing \(N/|N|\), still strictly inside that component. The enlargement has a positive linear functional on its entire angular section; it never contains opposite directions.

The Taylor term \(H_{\xi_0}(\theta)\ne0\) makes \(F(\xi_0+iz\theta)\) have exactly \(\mu_{\xi_0}\) roots near zero, all initially zero. Two small circles and Rouché keep exactly that many small roots for nearby real bases \(w\), small real \(t\), and all chosen directions in
\[
 z\longmapsto F(w+itN+iz\theta).
\]
For \(t<0\), no small root can cross the imaginary axis: on that axis the frequency has real part \(w-u\theta\) and imaginary part \(tN\), and hyperbolicity excludes a zero. At the direction \(N/|N|\), the real part of every root is exactly \(-t|N|>0\). The connected parameter set keeps all small roots in that right halfplane. In the limit \(t\uparrow0\), their real parts remain nonnegative.

Divide the polynomial by the product of these small-root factors. The quotient has no remaining zero in the disk. Its boundary has a uniform positive modulus; the maximum principle for its reciprocal brings that bound into the disk. A negative real test value \(z=-a\) is at least distance \(a\) from every root in the closed right halfplane. Multiplying the \(\mu_{\xi_0}\) distances yields
\[
 |F(w-iy)|\ge c|y|^{\mu_{\xi_0}}
\]
for small nonzero \(y\) in the compact smaller cone. Reality gives the identical bound for \(w+iy\). See LC035-2 for the uniform circle choices, multiplicities, parameter domains and constants.

The next step is essential: the bound also forces neighboring tangent components to contain the same smaller cone. At any nearby \(w\), rescale
\[
 \delta^{-\mu_w}F(w+\delta z)\longrightarrow H_w(z).
\]
The approximants are zero-free locally throughout the tube whose imaginary directions lie in the negative smaller cone. Restricting to a small complex line disk and using one-variable Hurwitz proves that their nonzero polynomial limit is zero-free there too. Thus \(H_w(v)\ne0\) for every vector \(v\) in the smaller cone. Its connectedness and inclusion of \(N\) place all these vectors in \(\Gamma_w\). This proves persistence without pretending that \(\mu_w\) stays constant.

## Example 2: a transverse field on the whole wave sphere

In three variables let
\[
 F(\tau,\eta)=\tau^2-|\eta|^2,\quad \eta=(\eta_1,\eta_2),\quad
 N=(1,0,0).
\]
At a nonzero characteristic \(\xi=(\tau,\eta)\),
\[
 H_\xi(v)=2(\tau v_\tau-\eta\cdot v_\eta),\qquad
 \Gamma_\xi=\left\{v:
   \frac{\tau v_\tau-\eta\cdot v_\eta}{\tau}>0\right\}.
\]
The division by \(\tau\ne0\) matters on the past characteristic sheet. The positive polar is
\[
 C_\xi=\mathbb R_+(|\tau|,-\operatorname{sgn}(\tau)\eta).
\]
For \(\tau=1\), \(\eta=(\cos\phi,\sin\phi)\), the slice \(v_\tau=1\) is the halfplane
\(\cos\phi\,v_1+\sin\phi\,v_2<1\). Its normal rotates with the actual characteristic frequency.

Now use the even degree-zero field, defined for every \(\xi\ne0\),
\[
 V(\tau,\eta)=
 \left(0,-\frac{\tau\eta}{\tau^2+|\eta|^2}\right).
 \tag{E1}
\]
It is orthogonal to \(x=(1,0,0)\). At a characteristic point its component test equals
\[
 \frac{\tau V_\tau-\eta\cdot V_\eta}{\tau}
 =\frac{|\eta|^2}{\tau^2+|\eta|^2}>0.
\]
Elsewhere every vector is permitted, including the zero values at \(\tau=0\) or \(\eta=0\). On the unit sphere, writing \(u=\tau^2\in[0,1]\), direct substitution gives
\[
 F(\xi\pm i\varepsilon V(\xi))
 =2u-1+\varepsilon^2u(1-u)
   \ \pm 2i\varepsilon\tau(1-u).
 \tag{E2}
\]
Its imaginary part can vanish only at \(\tau=0\) or \(|\eta|=0\); its real part is then \(-1\) or \(1\). Hence both deformations avoid zero for every \(\varepsilon>0\).

Here is an explicit uniform small-parameter estimate. For \(1/4\le u\le3/4\), the imaginary modulus is at least
\(2\varepsilon(1/2)(1/4)=\varepsilon/4\). For \(u\le1/4\), the negative real part has modulus at least \(1/2-\varepsilon^2/4\ge1/4\) when \(0<\varepsilon\le1\). For \(u\ge3/4\), the real part is at least \(1/2\). Therefore
\[
 |F(\xi\pm i\varepsilon V(\xi))|\ge\varepsilon/4
 \quad(|\xi|=1,\ 0<\varepsilon\le1).
 \tag{E3}
\]
This exact estimate independently checks the compact-field theorem in this example. At \(\xi_*=(1,1,0)/\sqrt2\), the trajectory is
\[
 F(\xi_*\pm i\varepsilon V(\xi_*))
 =\varepsilon^2/4\pm i\varepsilon/\sqrt2.
\]

![Rotating wave tangent halfplanes and exact imaginary exclusion on the sphere.](figures/wave-imaginary-exclusion.png)

*Figure 2.* Left: exact halfplane boundaries in the slice \(v_\tau=1\) at three characteristic directions \(\phi=0,\pi/3,2\pi/3\); arrows point into the permitted halfplanes and the unit disk is the global future-cone slice. Middle: the two exact complex trajectories \(\varepsilon^2/4\pm i\varepsilon/\sqrt2\) at \(\xi_*\), for \(0<\varepsilon\le1\). They approach zero only at the excluded parameter \(\varepsilon=0\). Right: the exact modulus along the meridian \(\xi=(\tau,\sqrt{1-\tau^2},0)\), at \(\varepsilon=1/4\), and the proved uniform bound \(\varepsilon/4=1/16\). The plotted points illustrate (E1)–(E3); the algebra, rather than sampling, proves exclusion.

## Example 3: multiplicity controls the power

Let \(F(\tau,\eta)=(\tau^2-\eta^2)^2\), \(N=(1,0)\), and \(\xi_0=(1,1)\). Then
\[
 H_{\xi_0}(v)=4(v_\tau-v_\eta)^2,\qquad \mu_{\xi_0}=2,\qquad
 \Gamma_{\xi_0}=\{v_\tau>v_\eta\}.
\]
Despite the square, the component containing \(N\) is this halfplane; the other component is \(v_\tau<v_\eta\). Pushing with \(V=N\) gives
\[
 |F(1\pm i\varepsilon,1)|=\varepsilon^2(4+\varepsilon^2)\ge4\varepsilon^2.
\]
This cannot have a uniform lower bound \(c\varepsilon\) with \(c>0\) as \(\varepsilon\downarrow0\). The root cluster has two roots counting multiplicity, even though they coincide. The proof counts both.

## Compact families and the cycle receivers

The compact-family theorem is more general than a single sphere field. If
\[
 Q\subset\{(\xi,v):\xi\ne0,\ v\in\Gamma_\xi\}
\]
is compact, then for one \(\varepsilon_0,c>0\) and one integer \(M\le m\),
\[
 |F(\xi\pm i\varepsilon v)|\ge c\varepsilon^M
 \quad((\xi,v)\in Q,\ 0<\varepsilon\le\varepsilon_0).
\]
Near characteristic pairs one uses the local cone estimate and a positive lower bound for \(|v|\). Near noncharacteristic pairs one uses an ordinary nonzero complex neighborhood. A finite cover gives one parameter, constant and maximum exponent. Joint continuity of a permitted family on a compact parameter space makes its value graph compact; boundedness alone does not give an angular margin.

This is the exact input needed to deform C7's sphere field with both signs, interpolate the allowed equatorial fields in C9, and extend AH3's equatorial field to the sphere. For the last construction, project nearby sphere points onto the equator, normalize, and compose with the equatorial field. The open permitted graph keeps this extension allowed on a uniform neighborhood. An even cutoff blends it with \(N\), using convexity. The compact-family theorem then excludes \(F=0\) on the whole sphere. The separate AH4 logarithm calculation can use that nonzero map; no assertion about projective tube injectivity or full component constancy follows from zero exclusion alone.

## Exercises and complete solutions

**Exercise 1 (component and sign).** For the wave polynomial at \(\xi=(-1,1,0)\), determine the tangent component and positive polar. Is the inequality \(H_\xi(v)>0\) the component test?

**Solution.** Here \(H_\xi(v)=-2(v_\tau+v_1)\), so \(H_\xi(N)=-2\). The component test is \(H_\xi(v)/H_\xi(N)>0\), giving \(v_\tau+v_1>0\). Its polar is \(\mathbb R_+(1,1,0)\). One can verify this directly: on the open halfspace \(a\cdot v>0\), a functional nonnegative everywhere must vanish on \(\ker a\), hence equal a nonnegative multiple of \(a\). The inequality \(H_\xi(v)>0\) selects the opposite component and would give the wrong polar sign.

**Exercise 2 (a change of tangent degree).** In Example 1, take \(\xi_j=(1,1,1+1/j)\). Verify the closed-graph conclusion for a convergent sequence \(x_j=s_j(1,-1,0)\), \(s_j\ge0\). Explain why it does not require the crossing polar to be a ray.

**Solution.** Convergence forces \(s_j\to s\ge0\), by the first coordinate. The limit \(s(1,-1,0)\) belongs to the crossing polar because it is its generator with the second coefficient zero. The crossing polar also contains the other ray and their positive combinations. A limit from one family of simple points can occupy only a subset of that larger cone; the closed graph requires inclusion of every such limit, not equality with every limiting ray.

**Exercise 3 (why the compactness hypothesis matters).** At the crossing in Example 1, put \(\theta_j=(1,1-1/j,0)\). Are these directions permitted? Can their pushes use one constant \(c>0\) in \(|F(\xi_0-i\varepsilon\theta_j)|\ge c\varepsilon^2\), for all \(j\) and small positive \(\varepsilon\)?

**Solution.** Both component inequalities hold: \(1>1-1/j\) and \(1>0\). Direct substitution gives
\[
 F(\xi_0-i\varepsilon\theta_j)
 =(-i\varepsilon/j)(-i\varepsilon)=-\varepsilon^2/j.
\]
Thus any such \(c\) must satisfy \(c\le1/j\) for every \(j\), which is impossible. The values are bounded, but their closure contains \((1,1,0)\) on the excluded tangent-cone boundary. The combined value set is not a compact subset of the permitted graph. This is an exact counterexample, not a numerical test.

**Exercise 4 (a zero field value).** A smooth sphere field is permitted and vanishes at \(\xi_0\). Prove \(F(\xi_0)\ne0\). Does the compact-field estimate fail at that point?

**Solution.** At positive tangent degree the component is a subset of \(\{H_{\xi_0}\ne0\}\), while homogeneity gives \(H_{\xi_0}(0)=0\). Hence zero cannot be permitted there. A permitted zero value forces tangent degree zero and \(F(\xi_0)\ne0\). A complex neighborhood has a fixed nonzero lower bound; the push at the point stays exactly \(\xi_0\). The finite-cover proof includes this ordinary noncharacteristic case and needs no division by \(|V(\xi_0)|\).

**Exercise 5 (both signs and scalar normalization).** Let \(\widetilde F=(2-i)F\) with real \(F\). Starting from \(|F(w-iy)|\ge c|y|^\mu\), derive the estimate for \(\widetilde F(w+iy)\). Must \(\widetilde F\) itself have real coefficients?

**Solution.** Real \(w,y\) give \(F(w+iy)=\overline{F(w-iy)}\), so \(|F(w+iy)|=|F(w-iy)|\). Multiplication by \(2-i\) multiplies the modulus by \(\sqrt5\), giving \(|\widetilde F(w+iy)|\ge\sqrt5 c|y|^\mu\). Its coefficients need not be real. Its nonzero set and tangent components are unchanged, and the underlying real normalization is sufficient.

**Exercise 6 (the Hurwitz step).** Why does a lower bound with exponent \(\mu_{\xi_0}\) at the original center not itself prove \(H_w(v)\ne0\) after division by \(\delta^{\mu_w}\) at a neighboring point? Supply the correct limiting argument.

**Solution.** If \(\mu_w<\mu_{\xi_0}\), the divided lower bound contains the positive factor \(\delta^{\mu_{\xi_0}-\mu_w}\), which tends to zero. A limit could vanish without contradicting that numerical bound. Instead use the whole zero-free tube: \(\delta^{-\mu_w}F(w+\delta z)\) is eventually zero-free on each compact subset and converges locally uniformly to the nonzero polynomial \(H_w\). If \(H_w\) had a zero there, select a complex line through it with a nonzero first Taylor term. The restricted limit is not identically zero and has a zero in a disk, contradicting one-variable Hurwitz. Thus \(H_w(-iv)\ne0\), homogeneity gives \(H_w(v)\ne0\), and connectedness of the permitted smaller cone containing \(N\) identifies the component. No constant-order assumption is needed.

## Reading credit

[Atiyah, Bott and Gårding, Part I (1970)](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02394570), Lemma 5.1, Lemma 5.9, and Corollary 5.11, treat local roots and cone variation. The proof companion writes the required fixed-polynomial arguments in full. Lemma 8.7.4 and the graph statement in Theorem 8.7.5 of Hörmander's *The Analysis of Linear Partial Differential Operators I* treat local cones of microhyperbolic functions; they are not needed here.

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning. Original proof, examples, exercise solutions and reproducible figures. Self-checked by the writing AI.
