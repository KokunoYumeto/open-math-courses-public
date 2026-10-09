# Compactness and complex-line positivity

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition by GPT-6.1 Sol (OpenAI). Original exposition: CC0. Linked programme prerequisites retain their stated licences. Self-checked by the writing AI.*

Subharmonic limits are controlled by their integrals and their upper values. Complex-line positivity gives an additional monotonicity: the normalized Laplacian mass of a ball increases with its radius. We prove these facts, identify the density of a holomorphic zero, and compute two families whose curvature lies on algebraic cuts.

The exact inputs are [Positive derivatives and canonical representatives](positive-derivatives-and-canonical-representatives.md), Theorems 3.1–3.2, Corollary 3.3 and Lemma 2.1; [Order, positivity and distributional limits](order-positivity-and-limits.md), Corollary 3.3 and Theorems 4.1, 5.1–5.2; [Convolution as addition of supports](convolution-as-addition-of-supports.md), B1–B3 and Proposition 5.1; Boundary flux and weak identities, Theorem 2.1 and Corollaries 2.2–2.4; and [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1 and Corollary 1.2. The polydisk proof and Lemma 3.1 of [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md) supply convergent holomorphic power series and the identity principle. Their supplied scalar, finite-algebra, integration and angular foundations provide compactness, cutoffs, Fubini, linear changes of variables and sphere measure. Every additional argument is given below.

Subharmonic means the canonical upper semicontinuous function with values in \([-\infty,\infty)\), satisfying the sphere submean inequality and not identically minus infinity on any component. Means use probability measure. We use \(\Delta=\sum_j\partial_{x_j}^2\). An assertion on a closed ball always requires that entire ball to lie in the open domain.

## Curvature on complex lines

Write \(z_j=x_j+iy_j\), and set
\[
\partial_{z_j}=\tfrac12(\partial_{x_j}-i\partial_{y_j}),\qquad
\partial_{\bar z_j}=\tfrac12(\partial_{x_j}+i\partial_{y_j}).
\tag{1.1}
\]
For a real distribution and \(w\in\mathbb C^n\), define
\[
L_wu=\sum_{j,k}w_j\overline{w_k}\partial_{z_j}\partial_{\bar z_k}u.
\tag{1.2}
\]
Conjugation and interchange of \(j,k\) show that it is real. For smooth \(u\), two applications of the chain rule give
\[
\Delta_\zeta[u(z+\zeta w)]=4(L_wu)(z+\zeta w),
\qquad \Delta u=4\sum_j L_{e_j}u.
\tag{1.3}
\]

An upper semicontinuous \(u:X\to[-\infty,\infty)\), \(X\subset\mathbb C^n\) open, is **plurisubharmonic** when its restriction to each complex affine line is subharmonic or identically minus infinity on each component of the line intersection. It is **proper** if no ambient component has the latter behavior. Thus properness permits a line contained in the minus-infinity set, as for \(\log|z_1|\).

**Theorem 1.1 (the Levi criterion).** Proper plurisubharmonic functions are locally integrable and real subharmonic in dimension \(2n\). Their distributions satisfy \(L_wu\ge0\) for every \(w\). Conversely, a real distribution with all these positive Levi forms has exactly one proper plurisubharmonic representative. Its averages with any fixed nonnegative smooth radial unit-mass profile supported in the unit ball decrease to that representative as the radius decreases to zero.

**Proof.** Suppose first that \(u\) has the line property, and fix a closed ball with center \(z\) and radius \(r\) inside \(X\). Upper semicontinuity gives a finite upper bound \(C\) there. For a complex unit vector \(w\),
\[
u(z)\le \frac1{2\pi}\int_0^{2\pi}u(z+re^{i\theta}w)\,d\theta.
\tag{1.4}
\]
This includes a line component with value minus infinity. Average over \(w\) on the real unit sphere. The map \(w\mapsto e^{i\theta}w\) is orthogonal, so it preserves sphere measure by the surface-invariance proof preceding U023 Lemma 2.1. Tonelli applied to \(C-u\) justifies both orders even if an integral is infinite. The double mean is the real sphere mean. Thus \(u\) satisfies the real submean inequality. Properness and U023 Theorem 3.2 now give local integrability and real subharmonicity.

For a nonnegative smooth mollifier, \(u_\epsilon=u*\rho_\epsilon\) is smooth on \(\{z:\operatorname{dist}(z,X^c)>\epsilon\}\). Integrate (1.4) on translated disks against the mollifier. The product integral of the absolute value is finite: bound the translation density by \(\|\rho_\epsilon\|_\infty\), integrate \(|u|\) on one compact neighborhood containing every translated circle, and then integrate over the finite angle interval. Fubini proves the line submean inequality for \(u_\epsilon\). The two-dimensional Taylor mean formula U023 (3.9) and (1.3) give \(L_wu_\epsilon\ge0\). Local distributional convergence passes this positivity to \(u\).

Conversely the trace in (1.3) gives \(\Delta u\ge0\). U023 supplies a proper real subharmonic representative \(u_0\) and radial smoothings decreasing pointwise to it. Each \(L_wu_\epsilon\) is the positive distribution \(L_wu\) applied to a nonnegative translated test, hence is nonnegative. Equation (1.3) and U023 in dimension two make the smooth line restrictions subharmonic.

Fix a compact line disk. For all sufficiently small radii the smoothings are defined on a neighborhood of it and bounded above by one earlier smoothing on that compact set. Subtract from this bound and use monotone convergence on its boundary circle. The circle inequalities pass to \(u_0\), including minus-infinity values. The restriction is upper semicontinuous. On a connected line component, either it is everywhere minus infinity or it has a finite point, so U023 Theorem 3.2 applies. It is therefore plurisubharmonic. Any other proper representative is real subharmonic by the first argument; uniqueness in U023 identifies it everywhere. Radial recovery is exactly U023 Corollary 3.3. \(\square\)

**Proposition 1.2 (finite maxima and decreasing limits).** A finite maximum of proper plurisubharmonic functions is proper plurisubharmonic. The limit of a decreasing sequence of plurisubharmonic functions is, on each ambient component, either proper plurisubharmonic or identically minus infinity.

**Proof.** A finite maximum is upper semicontinuous. At a finite center value, select a summand attaining it; its circle mean is at most that of the maximum. At a minus-infinity center the inequality is automatic. If a line restriction has a finite point, the two-dimensional converse submean theorem makes it subharmonic throughout that component. In the ambient space the maximum is finite almost everywhere, since its finitely many summands are locally integrable. It is proper.

A decreasing limit is upper semicontinuous: its strict sublevel set is the union of those of the terms. On each compact disk a common finite upper bound is supplied by the first term. Monotone convergence of its differences from that bound passes every circle inequality to the limit. The line restriction is subharmonic or identically minus infinity as above. On an ambient component with a finite point, averaging over directions gives the real submean inequality and U023 propagates integrability throughout that component. \(\square\)

A smooth real convex function has nonnegative second derivatives along both real directions of every complex line, and hence is plurisubharmonic. The converse fails: \(\operatorname{Re}(z_1^2)=x_1^2-y_1^2\) has zero Levi form but negative second derivative in the \(y_1\) direction.

## Integral convergence controls upper values

Fix a nonnegative smooth radial unit-mass profile \(\rho\) supported in the unit ball. U023 gives \(v\le v*\rho_\delta\), with pointwise decrease to \(v\) as \(\delta\downarrow0\).

**Theorem 2.1 (distributional convergence and Hartogs' bound).** If subharmonic \(v_j\) on any real open set \(X\) converge distributionally to \(T\), then \(T\) has a canonical subharmonic representative \(v\) and \(v_j\to v\) in \(L^1_{\mathrm{loc}}\). For every nonempty compact \(K\Subset X\) and every continuous real \(f\) on \(K\),
\[
\limsup_j\sup_K(v_j-f)\le\sup_K(v-f).
\tag{2.1}
\]
In particular \(\limsup_jv_j(x)\le v(x)\) everywhere, with equality and finite values almost everywhere. If \(f\ge v\) on \(K\), then \(v_j\le f+\eta\) there eventually for every \(\eta>0\).

**Proof.** The limit has positive Laplacian, so U023 gives \(v\). For fixed \(\delta>0\) and compact \(L\) where the averages are defined, the tests \(\rho_\delta(x-\cdot)\), \(x\in L\), have one compact support and bounded derivatives of every order. U008 Theorem 5.1 therefore gives uniform convergence of their pairings. U021 B1 justifies parameter derivatives, and the same bounded-family argument covers those derivatives. In particular
\[
v_j\le v_j*\rho_\delta\longrightarrow v*\rho_\delta
\quad\hbox{uniformly on }L.
\tag{2.2}
\]
Only the smoothed functions converge uniformly in this formula. It supplies a common finite local upper bound for the original sequence, including its finitely many initial terms.

Let \(\chi\ge0\) be compact smooth and choose \(\delta\) valid near its support. For any \(\eta>0\), put \(g=v*\rho_\delta+\eta\). Eventually \(v_j\le g\), and \(v\le g\), so
\[
\int|v_j-v|\chi\le \int(g-v_j)\chi+\int(g-v)\chi.
\tag{2.3}
\]
The first term tends to the second by distributional convergence. The latter tends to zero as \(\delta,\eta\downarrow0\), by the \(L^1\) approximation theorem in the integration foundations, §15.4. Taking \(\chi=1\) on any desired compact proves local \(L^1\) convergence.

Uniform convergence of the smoothings gives
\[
\limsup_j\sup_K(v_j-f)\le\sup_K(v*\rho_\delta-f).
\tag{2.4}
\]
These right sides decrease to \(\sup_K(v-f)\). Indeed choose decreasing radii \(\delta_l\to0\) and maximizing points \(x_l\in K\). Compactness gives a convergent subsequence \(x_l\to x_*\). For fixed \(m\) and \(l\ge m\), its maximum is at most \((v*\rho_{\delta_m})(x_l)-f(x_l)\). Take the limit and then \(m\to\infty\). This bounds the limiting maxima by \(v(x_*)-f(x_*)\), while every maximum is at least \(\sup_K(v-f)\). If this supremum is minus infinity, the same argument bounds the limit by every real number. This proves (2.1) without extending \(f\) off \(K\).

Apply (2.1) to a singleton for the pointwise inequality. Choose a compact exhaustion \(K_l\) and a subsequence \(j_l\) with \(\int_{K_l}|v_{j_l}-v|<2^{-l}\). On each \(K_m\), Tonelli makes the sum of errors for \(l\ge m\) finite almost everywhere. Hence this subsequence converges to \(v\) almost everywhere throughout \(X\), and the full limsup is at least \(v\) there. Local integrability makes these equal values finite. The eventual bound follows from (2.1). \(\square\)

For a proper plurisubharmonic sequence, all Levi forms pass positively to the limit distribution, so Theorem 1.1 makes this same limit representative plurisubharmonic.

**Lemma 2.2 (a bounded family of integrals has a subsequential distributional limit).** If real \(a_j\in L^1_{\mathrm{loc}}(X)\) have uniformly bounded \(L^1\) norms on every compact subset, a subsequence converges distributionally to a real order-zero distribution.

**Proof.** Use the compact exhaustion from the integration foundations to choose open relatively compact \(V_m\) with \(\overline V_m\subset V_{m+1}\) and union \(X\). We first construct a countable uniformly dense family of smooth tests, allowing approximation of functions supported in \(V_m\) by tests supported in \(\overline V_{m+1}\).

Extend such a continuous function by zero. On the grid \(h\mathbb Z^d\), \(h=1/l\), use the continuous hats
\[
\lambda_{h,k}(x)=\prod_{\nu=1}^d(1-|x_\nu/h-k_\nu|)_+ .
\tag{2.5a}
\]
They sum to one, since in each coordinate at most two adjacent hats are nonzero and sum to one. The interpolant with vertex values \(f(hk)\) differs uniformly from \(f\) by at most its modulus of continuity at \(\sqrt d\,h\). Only finitely many vertex values are nonzero. Replace them by rational real values, adding an arbitrarily small error. All finite rational arrays over these grids form a countable set.

Choose a fixed smooth cutoff \(\chi_m=1\) on \(\overline V_m\), supported in \(V_{m+1}\). Multiplication by \(\chi_m\), chosen between zero and one, preserves the error bound. Convolve with a fixed smooth bump at rational positive radii smaller than the distance of its support from \(V_{m+1}^c\). The resulting tests stay in \(V_{m+1}\) and approximate uniformly by uniform continuity. These choices form a countable family; real functions suffice, since complex tests split into real and imaginary parts.

Pairings with every test in the union over \(m\) are bounded. Bolzano–Weierstrass followed by successive subsequence selection and a diagonal choice gives convergence of all these countably many pairings. For an arbitrary smooth \(\phi\) supported in \(V_m\), use the constructed approximants \(\phi_l\):
\[
\left|\int a_j(\phi-\phi_l)\right|
\le\left(\sup_j\int_{\overline V_{m+1}}|a_j|\right)
\|\phi-\phi_l\|_\infty.
\tag{2.5}
\]
Thus the selected pairings are Cauchy for every \(\phi\). Their limit is linear, real on real tests, and has a common order-zero bound on each compact support. The distribution criterion of U008 makes it a distribution; its Corollary 3.3 identifies it with a signed Radon measure if desired. \(\square\)

**Theorem 2.3 (compactness or collapse).** On a connected real open set \(X\), a sequence of subharmonic functions with a common upper bound on each compact either tends uniformly to minus infinity on every compact, or has an \(L^1_{\mathrm{loc}}\)-convergent subsequence with subharmonic limit. For proper plurisubharmonic functions the limit in the second alternative is plurisubharmonic.

**Proof.** Failure of uniform collapse gives a subsequence, a compact \(K\), points \(x_j\in K\), and a real \(a\) such that \(v_j(x_j)\ge a\). Take a further subsequence with \(x_j\to x_0\). Choose \(\overline B_{2r}(x_0)\Subset X\). Eventually
\(B_r(x_0)\subset B_j:=B_{r+|x_j-x_0|}(x_j)\subset B_{2r}(x_0)\).
If \(C\) is the common upper bound on the latter closed ball, ball submean gives
\[
\int_{B_r(x_0)}v_j\ge |B_j|a-C|B_j\setminus B_r(x_0)|.
\tag{2.6}
\]
The right side is bounded below and the positive parts have a uniform bound. Hence the negative parts, and the \(L^1\) norms, are uniformly bounded on this first ball. The discarded finitely many terms cause no difficulty.

Here is the propagation step. Suppose a ball \(B\) has a uniform \(L^1\) bound \(A\). Suppose \(\overline B_{R+2\eta}(b)\Subset X\) and \(B\cap B_\eta(b)\) contains a ball \(E\) of positive volume. For each \(j\) some finite-valued \(y_j\in E\) satisfies \(v_j(y_j)\ge-A/|E|-1\); otherwise its negative integral on \(E\) exceeds \(A\). The ball \(B_{R+\eta}(y_j)\) covers \(B_R(b)\) and lies in \(B_{R+2\eta}(b)\). The same submean and upper-bound calculation as (2.6) gives a uniform \(L^1\) bound on \(B_R(b)\).

Any two points of \(X\) can be joined by a polygonal path: the set reachable from a fixed point is open, and its complement is open, by inserting short segments in small balls. Connectedness makes it all of \(X\). A compact path has a positive distance from the complement. Choose \(R\) below that distance and the radius of the initial bounded ball, then \(0<\eta<R/4\) so that \(R+2\eta\) is still below that distance. Partition the path parameter finely enough that consecutive centers are less than \(\eta\) apart. At each step \(B_\eta(b)\) lies in the preceding radius-\(R\) ball, so it contains the required positive-volume \(E\). The bound propagates along this finite chain. This reaches a neighborhood of every point. Finitely many such neighborhoods cover each compact set.

Lemma 2.2 now gives a distributional subsequential limit and Theorem 2.1 gives the claimed \(L^1\) limit. Levi positivity passes to that distribution in the complex case. Uniform collapse cannot also hold on this subsequence: on a compact ball of positive volume it would force its integral to minus infinity, contradicting a finite \(L^1\) limit. \(\square\)

## Holomorphic logarithms are stable in integrals

**Lemma 3.1 (holomorphic zero sets are null).** A holomorphic function which is not identically zero on any component of an open subset of \(\mathbb C^n\) has a zero set of real Lebesgue measure zero.

**Proof.** In one variable, its first nonzero Taylor coefficient makes each zero isolated. Choose for each zero a rational-center, rational-radius disk which contains it and no other zero. Distinct zeros require distinct disks, so the zero set is at most countable and has area zero.

Induct on \(n\). On a polydisk, translating its first center to zero, the polydisk Cauchy formula gives
\[
f(t,z')=\sum_{l\ge0}a_l(z')t^l.
\tag{3.1}
\]
Each coefficient is holomorphic in \(z'\): it is the first-variable circle integral of \(f\), and the locally uniformly convergent differentiated polydisk series from U015 permits differentiation under that compact integral. At least one coefficient is not identically zero on the parameter polydisk. Otherwise \(f\) vanishes on the whole polydisk and then on its ambient component by the identity principle.

By induction the zero set of this coefficient is null in parameter space. Outside it the one-variable function has a null zero set. Fubini on bounded polydisks, including the exceptional null set times the finite-area first disk, gives zero total volume. A countable polydisk cover exists from the rational Euclidean basis, so the full zero set is null. \(\square\)

**Proposition 3.2 (logarithms of holomorphic functions).** For such a holomorphic \(f\), \(\log|f|\), with value minus infinity at its zeros, is proper plurisubharmonic and locally integrable. In one complex dimension,
\[
\Delta\log|f|=2\pi\sum_p\operatorname{ord}_p(f)\delta_p.
\tag{3.2}
\]

**Proof.** Upper semicontinuity follows from continuity of \(|f|\) and the increasing logarithm, including its limit at zero. On any line the holomorphic restriction is identically zero on a component or has isolated finite-order zeros. In the latter case, near a zero \(p\), factor
\(f(\zeta)=(\zeta-p)^m h(\zeta)\), \(h\ne0\).
U020 Corollary 1.2 proves local integrability and (3.2), including a local logarithm for \(h\) whose real part is harmonic. The pointwise function is the positive potential \(m\log|\zeta-p|\) plus that harmonic function. U023 identifies it as the canonical subharmonic representative at every point, including \(p\). Off the zeros it is harmonic. Thus it has the line property. The assumption supplies a finite point on each ambient component, and Theorem 1.1 supplies ambient integrability. \(\square\)

**Theorem 3.3 (stability of logarithms).** Suppose holomorphic \(f_j\to f\) locally uniformly on open \(X\subset\mathbb C^n\), and \(f\) is not identically zero on any component. For each compact \(K\Subset X\), all sufficiently late \(\log|f_j|\) are locally integrable on a neighborhood of \(K\) and converge to \(\log|f|\) in \(L^1(K)\). If each \(f_j\) is nonzero on every component, this is usual \(L^1_{\mathrm{loc}}(X)\) convergence.

**Proof.** First work on a connected relatively compact open neighborhood \(V\Subset X\). The identity principle supplies \(p\in V\) with \(f(p)\ne0\). Eventually \(f_j(p)\ne0\), so those \(f_j\) are not identically zero on \(V\). Proposition 3.2 applies. Their logarithms have common local upper bounds from local uniform convergence, and their values at \(p\) have a finite lower bound. Consequently collapse is impossible for every subsequence. Theorem 2.3 gives an \(L^1_{\mathrm{loc}}(V)\)-convergent further subsequence.

At almost every point of \(V\), \(f\ne0\) by Lemma 3.1, and \(\log|f_j|\to\log|f|\) there. The summable-error argument in Theorem 2.1 gives almost-everywhere convergence along a further subsequence of any \(L^1\)-convergent subsequence. Its limit is therefore \(\log|f|\). If convergence of the whole sequence failed on a compact in \(V\), select a subsequence with errors bounded below by some \(\eta>0\). The further subsequence just obtained contradicts that bound. Finally cover \(K\) by finitely many connected relatively compact neighborhoods and take the largest exceptional index. This also handles infinitely many ambient components. \(\square\)

## A monotone measure of logarithmic curvature

Let \(C_m=\pi^{m/2}/\Gamma(1+m/2)\) be the volume of the real \(m\)-dimensional unit ball, with \(C_0=1\). The angular foundations A4–A5 prove these constants. Gamma recurrence gives \(\sigma_{2n-1}=2\pi C_{2n-2}\). For proper plurisubharmonic \(u\) and its positive measure \(\mu=\Delta u\), define
\[
\Theta(u,r,a)=\frac{\mu(B_r(a))}{2\pi C_{2n-2}r^{2n-2}},
\qquad 0<r<\operatorname{dist}(a,X^c).
\tag{4.1}
\]
For \(X=\mathbb C^n\), the distance is infinite. Balls here are open, so boundary mass is excluded. The small-radius limit is called the Lelong number with this normalization.

We will use the following consequence of U008 Theorem 5.2. If positive measures \(\nu_j\) converge distributionally to \(\nu\), then they converge on each ball \(B_r(a)\) whose closed ball is interior and whose boundary has zero \(\nu\)-mass. To prove it, put all cutoffs in a slightly larger compact ball. A smooth function equal to one there bounds every mass by its convergent pairings. Continuous radial cutoffs which equal one on \(\overline B_{r-\eta}\) and zero outside \(B_r\) bound \(1_{B_r}\) from below. Cutoffs equal to one on \(\overline B_r\) and zero outside \(B_{r+\eta}\) bound it from above. Pass to the continuous-test limits, then let \(\eta\downarrow0\). Continuity from below and above gives \(\nu(B_r)\) and \(\nu(\overline B_r)\), equal by the boundary assumption. This proves the squeeze without assuming convergence on all Borel sets.

**Theorem 4.1 (density monotonicity).** The function \(r\mapsto\Theta(u,r,a)\) is nonnegative and increasing. Its limit at zero exists and is finite.

**Proof.** Translate \(a\) to zero. For smooth \(u\), let \(h(r)\) be its real sphere mean. For a complex unit vector \(w\), let \(q_w(r)\) be the circle mean of \(g_w(\zeta)=u(\zeta w)\). Planar flux and (1.3) give
\[
r q_w'(r)=\frac1{2\pi}\int_{|\zeta|<r}\Delta_\zeta g_w\,dA.
\tag{4.2}
\]
This is nonnegative and increasing, since \(L_wu\ge0\). Phase invariance of real sphere measure makes the average of \(q_w(r)\) equal to \(h(r)\). All parameter derivatives pass through this compact smooth integral. Thus \(rh'(r)\) is nonnegative and increasing. Real flux gives
\[
\mu(B_r)=\sigma_{2n-1}r^{2n-1}h'(r),
\qquad \Theta(u,r,0)=rh'(r).
\tag{4.3}
\]

For general \(u\), radial smoothings are smooth plurisubharmonic on smaller domains. Their positive Laplacians converge distributionally. The preceding cutoff argument gives mass convergence at every radius without boundary mass. In any fixed larger compact ball only countably many spheres have positive mass: for each integer \(k\), only finitely many disjoint spheres can have mass at least \(1/k\). Their countable union includes every positive mass sphere.

Pass the smooth monotonicity inequality at two radii outside this countable set. Approach any desired positive radii from below by such radii, keeping their order. These choices exist because a countable set has Lebesgue measure zero while each nonempty interval has positive measure. Increasing open balls exhaust the desired open ball, so continuity from below and the continuous positive denominator prove the inequality at every radius. A fixed larger interior ball has finite mass and bounds all smaller densities. Hence the nonnegative increasing function has a finite limit at zero, its infimum. \(\square\)

**Lemma 4.2 (annular change in a sphere mean).** For a real subharmonic \(u\) in dimension \(d\), write \(M(r)\) for its sphere mean about \(a\), and \(\mu=\Delta u\). Then
\[
M(r)-M(s)=\int_s^r\frac{\mu(B_t(a))}{\sigma_{d-1}t^{d-1}}\,dt,
\qquad 0<s<r<\operatorname{dist}(a,X^c).
\tag{4.4}
\]
Both means are finite and \(M\) is locally absolutely continuous in the positive radius.

**Proof.** On a slightly larger ball, U023 Theorem 3.1 represents \(u\) as a compact positive potential plus a smooth harmonic function. Harmonic means cancel. Write \(\phi_d\) for the radial point-source kernel. U023 Lemma 2.1 gives the shell mean \(\phi_d(\max(t,|y-a|))\) for a source at \(y\). Its difference between \(r\) and \(s\) is
\[
\int_s^r\frac{1_{\{|y-a|<t\}}}{\sigma_{d-1}t^{d-1}}\,dt,
\]
by \(\phi_d'(t)=1/(\sigma_{d-1}t^{d-1})\), including \(d=1\). Integrate this nonnegative quantity against the compact source measure and use Tonelli. In \(B_r(a)\) that measure equals \(\mu\), proving (4.4). The integrand is bounded on every closed positive-radius interval by finite local mass and a positive denominator. Its integral over disjoint intervals is bounded by this common bound times their total length, which proves absolute continuity there. We subtracted finite sphere means, not a possibly infinite center value. \(\square\)

**Proposition 4.3 (logarithmic homogeneity).** If proper plurisubharmonic \(u\) on \(\mathbb C^n\) satisfies
\[
e^{u(tz)}=t^k e^{u(z)}\qquad(t>0)
\tag{4.5}
\]
for real \(k\), then \(k\ge0\) and \(\Theta(u,r,0)=k\) for every \(r>0\). The same statement holds on a ball about zero at radii where the homogeneity relation holds between its points.

**Proof.** With \(e^{-\infty}=0\), (4.5) gives \(u(tz)=u(z)+k\log t\), including singular values. Its finite sphere means consequently differ by \(k\log(r/s)\). Subtract this from (4.4). The locally bounded integrand
\(\mu(B_t)/(\sigma_{2n-1}t^{2n-1})-k/t\)
has zero integral on every positive-radius interval. It is zero almost everywhere: its indefinite integral is zero, hence its distribution is zero by one-dimensional integration against test derivatives and Fubini, and U023's initial \(L^1\) identification fact applies. Thus \(\Theta=k\) almost everywhere.

Open-ball mass is left continuous at positive radii by continuity from below. So is the normalized density. Approach every radius from below through the full-measure equality set to obtain equality everywhere. Nonnegativity gives \(k\ge0\). \(\square\)

## Rescaling detects the order of a zero

**Theorem 5.1 (holomorphic order and polynomial degree).** Let \(f\) be holomorphic and not identically zero on any component of \(X\subset\mathbb C^n\). At \(a\in X\), let \(k\) be the least degree of a nonzero Taylor term. Then
\[
\lim_{r\downarrow0}\Theta(\log|f|,r,a)=k.
\tag{5.1}
\]
If \(P\) is a nonzero polynomial of degree \(D\) on \(\mathbb C^n\), then at every center \(a\),
\[
\lim_{r\to\infty}\Theta(\log|P|,r,a)=D.
\tag{5.2}
\]

**Proof.** Translate \(a\) to zero and group its convergent Taylor series by degree, \(f=f_k+f_{k+1}+\cdots\). Define
\[
F_r(z)=r^{-k}f(rz).
\tag{5.3}
\]
These functions converge locally uniformly on the expanding domains to \(f_k\). Explicitly, on \(|z_j|\le M\), choose a polydisk of radius \(R\) where the Cauchy coefficient bound is \(|c_\alpha|\le A R^{-|\alpha|}\). For \(rM/R\le1/2\), the sum of terms of degree at least \(k+1\), after division by \(r^k\), is bounded by a constant times \(r\). To see this, factor out \((rM/R)^{k+1}r^{-k}\); the remaining series is bounded by
\(\sum_{|\alpha|\ge k+1}2^{-(|\alpha|-k-1)}\le 2^{k+1}\prod_{j=1}^n\sum_{l\ge0}2^{-l}\).
The finite lower-degree terms are absent by the choice of \(k\).

Theorem 3.3 on each fixed ball, applied to every sequence \(r\downarrow0\), gives \(L^1_{\mathrm{loc}}\) convergence of \(\log|F_r|\) to \(\log|f_k|\). Sequential convergence implies the full radius limit: otherwise choose radii below \(1/j\) where a fixed error stays positive. The positive Laplacian measures therefore converge distributionally.

Since \(f_k(tz)=t^kf_k(z)\), Proposition 4.3 gives
\(\Delta\log|f_k|(B_s)=2\pi C_{2n-2}k s^{2n-2}\).
This is continuous in \(s>0\), including \(n=1\). Decreasing slightly larger open balls to \(\overline B_s\) shows that its boundary has zero mass. The cutoff squeeze above therefore gives convergence of the rescaled measures on \(B_1\).

For the original measure \(\mu=\Delta\log|f|\) and rescaled measure \(\mu_r=\Delta\log|F_r|\), the exact law is
\[
\mu_r(E)=r^{2-2n}\mu(rE).
\tag{5.4}
\]
To check it, pair the left side with a compact smooth \(\phi\) and use \(x=rz\) in \(\int\log|f(rz)|\Delta\phi(z)\,dz\). The volume contributes \(r^{-2n}\), and
\(\Delta_x[\phi(x/r)]=r^{-2}\Delta\phi(x/r)\)
contributes \(r^2\). The constant \(-k\log r\) has zero Laplacian because the integral of a compact test derivative is zero by Fubini and the fundamental theorem. Equality on smooth tests identifies the Radon measures, as proved in U008. Formula (5.4) gives \(\Theta(\log|F_r|,1,0)=\Theta(\log|f|,r,0)\); convergence of the masses proves (5.1).

For a polynomial use \(F_r(z)=r^{-D}P(a+rz)\) as \(r\to\infty\). Its finite expansion converges uniformly on compact sets to the nonzero highest homogeneous part \(P_D(z)\). Repeat the same logarithm convergence, boundary-mass squeeze and translated dilation law. Proposition 4.3 gives limit \(D\), proving (5.2). This includes nonzero constants with degree zero. \(\square\)

In one complex dimension (3.2) makes the density exactly the number of zeros in the open disk, counted with multiplicity. In higher dimensions the argument determines the order without assuming that the zero set is a smooth hypersurface.

## Positive sources along algebraic cuts

We first supply two elementary local tools. A nonvanishing holomorphic \(g\) has a local \(N\)th root for each integer \(N\ge1\). Near \(p\), shrink until \(|g/g(p)-1|<1/2\). The logarithmic series and exponential calculation proved in U020 Corollary 1.2 give a holomorphic function
\[
\ell=\log|g(p)|+i\theta+
\sum_{l\ge1}\frac{(-1)^{l+1}}l\bigl(g/g(p)-1\bigr)^l.
\tag{6.0a}
\]
It satisfies \(e^\ell=g\), where \(g(p)=|g(p)|e^{i\theta}\). Thus \(h=e^{\ell/N}\) has \(h^N=g\) and \(Nh^{N-1}h'=g'\). The convergent series permits every derivative on smaller disks.

Next let a continuous function \(q\) be smooth and harmonic on the two sides of a straight interval, with smooth traces up to the interval. Choose a unit normal \(\nu\) pointing from the minus side to the plus side. Green's identity on each side, with compact test \(\phi\), gives the interface contribution
\[
\langle\Delta q,\phi\rangle
=\int_{\text{interval}}\phi\,
  (\partial_\nu q_+-\partial_\nu q_-)\,dS.
\tag{6.0}
\]
Indeed \(\int q\Delta\phi=\int_{\partial}(q\partial_{\nu_{\rm out}}\phi-\phi\partial_{\nu_{\rm out}}q)\). The two \(q\)-terms cancel by continuity. The plus side has outward normal \(-\nu\), the minus side \(+\nu\), giving the displayed sign. Localize away from endpoints with compact cutoffs; finite partitions sum the formula. Regions cut by finitely many segments and circles satisfy the proved corner version U011 Corollary 2.4, so the same calculation applies after removing small disks about exceptional endpoints.

**Proposition 6.1 (an absolute imaginary square root).** For real \(a\), define the continuous single-valued function
\[
q_a(z)=|\operatorname{Im}\sqrt{z^2+a}|
=\sqrt{\frac{|z^2+a|-\operatorname{Re}(z^2+a)}2}.
\tag{6.1}
\]
It is subharmonic. If \(a\ne0\), its Laplacian is the sum of the following measures, the first on \(z=x\) and the second on \(z=iy\):
\[
\frac{2|x|}{\sqrt{x^2+a}}1_{\{x^2+a>0\}}\,dx,
\qquad
\frac{2|y|}{\sqrt{a-y^2}}1_{\{a-y^2>0\}}\,dy.
\tag{6.2}
\]
Each density is defined by the displayed quotient on its indicated open set and is zero elsewhere. If \(a=0\), \(q_0(x+iy)=|y|\) and \(\Delta q_0=2\,dx\otimes\delta_0(dy)\). There are no additional endpoint or crossing atoms.

**Proof.** If \(h^2=g=z^2+a\), write \(h=s+it\). Then \(|g|=s^2+t^2\) and \(\operatorname{Re}g=s^2-t^2\), which proves (6.1) and its independence of the root sign. Its real expression is continuous everywhere. Away from zeros of \(g\), the local root constructed above gives \(q_a=|\operatorname{Im}h|\). This is harmonic where \(\operatorname{Im}h\) has a fixed nonzero sign.

The possible cuts satisfy \(\operatorname{Im}g=2xy=0\) and \(\operatorname{Re}g\ge0\). At a point with \(g>0\) and \(z\ne0\), the relevant cut is a straight axis interval and \(v=\operatorname{Im}h\) vanishes on it. Its tangential derivative is zero and its gradient has norm \(|h'|\), by the Cauchy–Riemann equations. Since \(2hh'=g'=2z\ne0\), the normal derivative does not vanish. The fundamental theorem in the normal variable shows that \(v\) changes sign across the interval. Formula (6.0) applied to \(|v|\) gives the positive density \(2|\nabla v|=2|h'|=|g'|/\sqrt g\).

On the real axis \(g=x^2+a\); on the imaginary axis \(g=a-y^2\). This is precisely (6.2). For \(a>0\), the cut consists of the whole real axis and the interval \(|y|<\sqrt a\). For \(a<0\), it consists of the real rays \(|x|>\sqrt{-a}\). Off these cuts the imaginary part cannot vanish, and the function is harmonic.

Each finite endpoint \(p\) when \(a\ne0\) is a simple zero of \(g\). The factorization \(g(z)=(z-p)g_1(z)\) with \(g_1(p)\ne0\) gives both upper and lower bounds comparable to \(|z-p|\). Thus \(q_a=O(|z-p|^{1/2})\) and the branch gradients have size at most
\(|h'|=|g'|/(2|g|^{1/2})=O(|z-p|^{-1/2})\).
The curve densities have the same inverse-square-root bound and are locally integrable.

Remove a radius-\(\epsilon\) disk at each such endpoint and use Green on the finitely many harmonic pieces meeting a compact test support. On its small circular boundary the term involving \(q_a\partial_\nu\phi\) is \(O(\epsilon^{3/2})\), and the term involving \(\phi\partial_\nu q_a\) is \(O(\epsilon^{1/2})\). Both vanish. The integrable curve densities converge to their full integrals. This proves equality with (6.2) on all tests, leaving no point-supported distribution there.

For \(a>0\), the only extra crossing is at zero. Choose the local root with \(h(0)=\sqrt a\). The identity \(h-\sqrt a=z^2/(h+\sqrt a)\) gives \(q_a=O(|z|^2)\), and \(h'=z/h=O(|z|)\). The same circle errors vanish at this crossing; its two axis densities are integrable and add without an atom. For \(a<0\), choose a root with nonzero imaginary part near zero, so \(q_a\) is harmonic there. For \(a=0\), the roots are \(\pm z\); one-dimensional integration by parts twice gives \((|y|)''=2\delta_0\), and Fubini gives the stated planar measure.

We have proved a positive distributional Laplacian for a continuous locally integrable function. Its ball averages recover it at every point by continuity. The canonical representative from U023 has the same ball averages and hence the same pointwise values. It is therefore subharmonic. \(\square\)

**Proposition 6.2 (the largest real part of a root).** For integer \(N\ge1\), let \(p_N(z)=\max_{w^N=z}\operatorname{Re}w\). It is continuous and subharmonic, with
\[
\Delta p_N=\frac2N\sin\frac\pi N\,
|x|^{1/N-1}1_{\{x<0\}}\,dx\otimes\delta_0(dy).
\tag{6.3}
\]
There is no mass at zero. For \(N=1\) this measure is zero.

**Proof.** If \(z=re^{i\theta}\ne0\), \(-\pi\le\theta\le\pi\), its roots have modulus \(r^{1/N}\) and arguments \((\theta+2\pi l)/N\) modulo \(2\pi\). This follows by modulus and the circle exponential law; conversely these \(N\) distinct values all have \(N\)th power \(z\), and any root has one of their arguments. Among them the representative closest to angle zero has angular distance \(|\theta|/N\). Indeed \(N\) times any circular representative differs from \(\theta\) by an integer multiple of \(2\pi\), whose least possible absolute value for this \(\theta\) is \(|\theta|\). Cosine decreases on \([0,\pi]\), so
\[
p_N(z)=r^{1/N}\cos(\theta/N).
\tag{6.4}
\]
The two choices at the negative axis agree, and \(|p_N(z)|\le r^{1/N}\) gives continuity at zero.

Away from the negative axis and zero, the selected root is locally a holomorphic branch. One verification is the local logarithm construction above: match its value with \(r^{1/N}e^{i\theta/N}\) at one point. Their ratio is a continuous \(N\)th root of unity, hence constant on a connected sufficiently small disk, so they agree throughout it. Thus \(p_N\) is harmonic there. Differentiating the local logarithm gives \(\partial_y\theta=x/(x^2+y^2)\); also \(\partial_y r=y/r\). At \(z=-t+i0\), \(t>0\), (6.4) yields
\[
\partial_y p_N(-t+i0)=\frac1N t^{1/N-1}\sin(\pi/N).
\tag{6.5}
\]
The lower trace is its negative. Formula (6.0) gives (6.3) away from zero. Its density is integrable there because \(1/N-1>-1\).

Near zero, \(p_N=O(r^{1/N})\). A local root branch has derivative of modulus \(N^{-1}r^{1/N-1}\), so its real part has that gradient bound. In the punctured Green calculation the two circular errors are \(O(\epsilon^{1+1/N})\) and \(O(\epsilon^{1/N})\). They vanish. Thus no origin-supported term remains, and (6.3) is the complete distributional Laplacian. It is positive for \(N\ge2\). For \(N=1\), (6.4) is \(\operatorname{Re}z\) and \(\sin\pi=0\). Continuous ball recovery and U023 again prove subharmonicity. \(\square\)

## Exercises

**Exercise 1 (basic: a strict pointwise loss).** For \(v_j(z)=\log|z|/(j+1)\) on the unit disk, compute the \(L^1\) norm, its limit and the pointwise limsup. Compare with Theorem 2.1.

**Exercise 2 (basic: why connectedness matters).** On the disjoint union \(B_1(0)\cup B_1(4)\subset\mathbb C\), put \(v_j=0\) on the first disk and \(v_j=-j\) on the second. Show that neither alternative in Theorem 2.3 holds on this disconnected open set.

**Exercise 3 (intermediate: positive diagonal entries are insufficient).** Compute the Levi form and real Laplacian of
\[
Q(z)=|z_1|^2+2|z_2|^2+
4\operatorname{Re}(z_1\overline z_2)+\operatorname{Re}(z_1^2).
\tag{7.1}
\]
Show that real subharmonicity and positive diagonal Levi entries do not give plurisubharmonicity.

**Exercise 4 (intermediate: a homogeneous maximum).** For
\(u=\max(\log|z_1^2+z_2^2|,\log|3z_1z_2|)\) on \(\mathbb C^2\), with \(u(0)=-\infty\), prove plurisubharmonicity and find \((\Delta u)(B_r(0))\). Is there an atom at zero?

**Exercise 5 (intermediate: a smooth density tending to one).** For \(u(z)=\tfrac12\log(1+|z|^2)\) on \(\mathbb C^n\), compute the Levi form, Laplacian, density \(\Theta(u,r,0)\) and exact ball mass.

**Exercise 6 (advanced: orders at two scales).** For \(P(z_1,z_2)=z_1^2+z_2^3+2z_1z_2^2\), determine both density limits about zero and bounds for the density and ball mass at every radius.

**Exercise 7 (advanced: a translated cubic cut).** For \(b=1+i\) and \(v(z)=5\max_{w^3=z-b}\operatorname{Re}w\), determine the Laplacian, its mass on \(\{b-t:0<t<R\}\), and whether there is an atom at \(b\).

**Exercise 8 (advanced: two shifted rays).** For \(b=-1+2i\) and \(v(z)=2|\operatorname{Im}\sqrt{(z-b)^2-9}|\), determine the Laplacian and its mass on \(\{b+x:3<|x|<R\}\). Prove the endpoint masses vanish and evaluate the mass at \(R=5\).

## Solutions

**Solution 1.** Proposition 3.2 gives subharmonicity. Polar integration and integration by parts give
\[
\|v_j\|_{L^1(B_1)}
=\frac{2\pi}{j+1}\int_0^1(-\log r)r\,dr
=\frac{\pi}{2(j+1)}.
\tag{8.1}
\]
The endpoint term \(r^2\log r\) tends to zero, for example by the logarithmic bound from the scalar foundations. Thus the \(L^1\) limit and its canonical representative are zero. At every nonzero point the sequence tends to zero, while at zero it remains minus infinity. The limsup inequality holds everywhere and equality fails only on that null singleton.

**Solution 2.** Every term is harmonic on each component and bounded above by zero. It does not collapse on any compact in the first disk. On a positive-area compact disk \(K\) in the second, its \(L^1\) norm is \(j|K|\), unbounded along every subsequence. An \(L^1(K)\)-convergent sequence has bounded norms by the triangle inequality, so no local \(L^1\) subsequence exists. This is precisely where connected propagation is needed.

**Solution 3.** The real part of the holomorphic term \(z_1^2\) has zero Levi form. Direct differentiation of the remaining quadratic gives
\[
L_wQ=|w_1|^2+2|w_2|^2+
4\operatorname{Re}(w_1\overline w_2),\qquad \Delta Q=12.
\tag{8.2}
\]
Thus the smooth function is real subharmonic and has diagonal Levi entries \(1,2\). For \(w=(-2,1)\), however, \(L_wQ=4+2-8=-2\). Its line Laplacian is \(-8\), so it fails the line criterion.

**Solution 4.** Both nonzero polynomial logarithms are proper plurisubharmonic by Proposition 3.2; their maximum is so by Proposition 1.2. Their common zero is only the origin: \(z_1z_2=0\) and \(z_1^2+z_2^2=0\) force both coordinates to vanish. The exponential of their maximum is homogeneous of degree two under positive real dilation, so Proposition 4.3 gives \(\Theta=2\). Since \(C_2=\pi\),
\[
(\Delta u)(B_r)=4\pi^2r^2.
\tag{8.3}
\]
Continuity from above of this finite local measure as \(r\downarrow0\) gives zero mass to the origin. A singular function value need not give a Laplacian atom in real dimension four.

**Solution 5.** Put \(s=|z|^2\). Differentiating a radial expression gives
\[
L_wF(s)=F'(s)|w|^2+
F''(s)\left|\sum_jw_j\overline z_j\right|^2.
\tag{8.4}
\]
Here \(F'=1/[2(1+s)]\), \(F''=-1/[2(1+s)^2]\). Cauchy–Schwarz yields
\(L_wu\ge |w|^2/[2(1+s)^2]>0\) for \(w\ne0\). Summing coordinate entries and multiplying by four gives
\[
\Delta u=\frac{2[n+(n-1)|z|^2]}{(1+|z|^2)^2}.
\tag{8.5}
\]
The sphere mean is \(h(r)=\tfrac12\log(1+r^2)\). Formula (4.3) gives \(\Theta=r^2/(1+r^2)\), whose derivative is \(2r/(1+r^2)^2>0\) and whose endpoints are zero and one. Consequently
\[
(\Delta u)(B_r)=2\pi C_{2n-2}\frac{r^{2n}}{1+r^2}.
\tag{8.6}
\]
For \(n=1\), direct polar integration of \(2/(1+r^2)^2\) gives \(2\pi r^2/(1+r^2)\), confirming the constant.

**Solution 6.** The lowest nonzero homogeneous term is \(z_1^2\) of degree two. The highest is \(z_2^3+2z_1z_2^2\), degree three. Theorem 5.1 gives the two density limits; Theorem 4.1 gives
\[
2\le\Theta(\log|P|,r,0)\le3\qquad(r>0).
\tag{8.7}
\]
The denominator in dimension two is \(2\pi^2r^2\). Thus the open-ball Laplacian mass lies between \(4\pi^2r^2\) and \(6\pi^2r^2\). No regularity of the zero hypersurface was assumed.

**Solution 7.** Translation commutes with distributional differentiation by substitution in tests. Scaling the function by five scales its measure by five. Proposition 6.2 with \(N=3\) therefore gives, on \(z=b-t\), \(t>0\), the density
\[
\frac{5\sqrt3}{3}t^{-2/3}\,dt.
\tag{8.8}
\]
For the sine value, the scalar angle-addition identities give \(4c^3-3c+1=(c+1)(2c-1)^2=0\) at \(c=\cos(\pi/3)\), while \(0<c<1\). Thus \(c=1/2\) and the positive sine is \(\sqrt3/2\). The endpoint estimate in Proposition 6.2 gives no atom at \(b\). Integrating the density from zero to \(R\) gives \(5\sqrt3 R^{1/3}\); there is no mass off this ray.

**Solution 8.** Substitute \(\zeta=z-b\) in Proposition 6.1 with \(a=-9\). Only the real rays \(|x|>3\) contribute. Multiplication by two gives the density \(4|x|/\sqrt{x^2-9}\) there. At each finite endpoint the function and gradient have the square-root bounds proved in Proposition 6.1, so the small-circle Green terms vanish and there are no endpoint atoms. The two rays contribute equally:
\[
\int_{3<|x|<R}\frac{4|x|}{\sqrt{x^2-9}}\,dx
=8\sqrt{R^2-9}.
\tag{8.9}
\]
The antiderivative follows directly by differentiation on \(x>3\) and its zero limit at \(3\). At \(R=5\) the mass is \(32\).

## Programme proof locations and freely accessible sources

- [Positive derivatives and canonical representatives](positive-derivatives-and-canonical-representatives.md), Lemma 2.1, Theorems 3.1–3.2 and Corollary 3.3: complete shell formula, canonical representative, local integrability, sphere recovery and radial smoothing.
- [Order, positivity and distributional limits](order-positivity-and-limits.md), Corollary 3.3 and Theorems 4.1, 5.1–5.2: Radon measures, sequential bounded-test convergence, and convergence on continuous compact tests. [Convolution as addition of supports](convolution-as-addition-of-supports.md), B1–B3 and Proposition 5.1: parameter tests and local smoothing.
- Boundary flux and weak identities, Theorem 2.1 and Corollaries 2.2–2.4: flux, Green identities and planar corners. [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1 and Corollary 1.2: normalized Laplacian and log-modulus sources, with local logarithm proof.
- [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), polydisk Cauchy proof, (3.1), and Lemma 3.1: locally convergent power series with coefficient and derivative bounds, and the identity principle.
- [Integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15–16; [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13; [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6; and [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5: the measure, compactness, scalar calculus, Euclidean and sphere proofs used above.
- Ahmed Zeriahi, *Introduction to Pluripotential Theory*, SEAMS School, Hanoi, 2017, [free author-hosted lecture notes](https://www.math.univ-toulouse.fr/~zeriahi/PPT-SEAMS2017.pdf), Proposition 1.34, Propositions 1.45–1.46, Theorem 1.49, Lemma 2.26, Theorem 2.32 and Corollary 2.34. Their proofs provide comparisons for line averaging, smoothing, compactness and logarithmic curvature. The present lesson supplies the stated arbitrary-domain generality, subsequence construction, boundary-mass limits, holomorphic rescaling and full cut calculations.
