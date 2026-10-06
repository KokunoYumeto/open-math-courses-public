# Positive derivatives and canonical representatives

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition by GPT-6.1 Sol (OpenAI). Original exposition: CC0. Linked programme prerequisites retain their stated licences. Self-checked by the writing AI.*

A distribution does not choose a value at a single point. Positivity can nevertheless select a particular representative. A positive first derivative produces an increasing function, a positive Hessian produces a finite continuous convex function, and a positive Laplacian produces an upper semicontinuous function recovered by its shrinking sphere averages. In the last case the selected value can be minus infinity.

All positivity statements concern real distributions, meaning real values on real tests. We use the positive-measure proof in [Order, positivity and distributional limits](order-positivity-and-limits.md), Theorem 4.1; the flux and surface measure in [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), Theorem 2.1 and Corollary 2.2; the all-dimensional harmonic distribution lemma in [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md); the Laplacian source in [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1; and the compact-factor convolution, parameter and local approximation proofs in [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3, Theorem 1.1, Proposition 5.1 and Theorem 5.2. Polar integration, sphere scaling and constants are proved in the supplied [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5. Precise free human-source comparisons are listed at the end.

Two elementary identification facts will be useful. If \(w'=0\) on an open interval \(I\), every compact smooth test \(\phi\) of integral zero has a compact primitive in \(I\): integrate from the left of its support; the zero integral makes the primitive vanish on the right as well. Thus \(w(\phi)=0\). Choose \(\rho\in C_c^\infty(I)\) of integral one and apply this to \(\phi-\rho\int\phi\). It gives \(w(\phi)=w(\rho)\int\phi\), so \(w\) is constant.

Also, a locally integrable function with zero distribution is zero almost everywhere. On a compact \(K\Subset X\), multiply it by a compact cutoff equal to one near \(K\), and extend by zero to obtain an \(L^1(\mathbb R^n)\) function \(g\). Its small smooth averages vanish on \(K\), since there they pair the original zero distribution with compact tests. The \(L^1\) approximation theorem in the [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §15.4, gives
\(\int_K|g|\le\|g-g*\rho_\epsilon\|_1\to0\).
An exhaustion by compact sets proves the assertion. Consequently two locally integrable representatives of a distribution agree almost everywhere; if they are continuous, they agree everywhere, because a nonzero continuous difference has a nonzero sign on a ball of positive volume.

## Positive slopes are cumulative measures

Increasing always means nondecreasing. Jump values are not determined by a distribution; we select the right-continuous convention.

**Theorem 1.1 (positive first derivatives).** On a nonempty open interval \(I\), a real distribution \(u\) has \(u'\ge0\) if and only if it has an increasing locally bounded representative. There is exactly one right-continuous increasing representative. If \(\mu=u'\) and \(x_0\in I\), it has the form

\[
u_0(x)=c+
\begin{cases}
\mu((x_0,x]),&x\ge x_0,\\
-\mu((x,x_0]),&x<x_0,
\end{cases}
\tag{1.1}
\]

for a real \(c\).

**Proof.** Theorem 4.1 of the positivity lesson makes \(u'\) a positive Radon measure, finite on compact subsets. Let \(F\) be (1.1) with \(c=0\). For \(a<x\) in \(I\), additivity, including the case when the interval crosses \(x_0\), gives

\[
F(x)=F(a)+\mu((a,x]).
\tag{1.2}
\]

Thus \(F\) is increasing and locally bounded. It is measurable, since an upper or lower level set of an increasing function is an interval with a possible endpoint. If \(x_j\downarrow x\), the finite measures \(\mu((x,x_j])\) decrease to zero: the sets decrease to the empty set, and countable additivity gives continuity from above by subtracting from one finite containing interval. Hence \(F\) is right-continuous. Its jump at \(x_0\) has size \(\mu(\{x_0\})\), as encoded by the left branch.

For a test \(\phi\), choose \(a<b\) so that its support lies strictly between them. The product-measure Fubini theorem of the integration foundations, §16.1, applies to the finite measure \(\mu|_{[a,b]}\) and bounded \(\phi'\). Equation (1.2) yields

\[
-\int_a^bF(x)\phi'(x)\,dx
=-\int_{(a,b]}\left(\int_s^b\phi'(x)\,dx\right)d\mu(s)
=\int\phi\,d\mu.
\tag{1.3}
\]

The constant part integrates to zero. Therefore \(F'=u'\), and the zero-derivative fact above gives \(u=F+c\). Reality gives \(c\in\mathbb R\).

Conversely, average an increasing locally bounded function with a nonnegative compact smooth unit-mass kernel. On every smaller interval the averages are increasing: compare the translated arguments under their integrals. They are smooth by the local convolution theorem, so their first derivatives are nonnegative. Their distributional limit is the original function. Testing the derivative limit on any nonnegative compact test proves positivity.

Finally two right-continuous representatives agree almost everywhere by the identification fact. For each \(x\), choose points of equality decreasing to \(x\), possible because every nonempty interval has positive measure. Their right limits prove equality at \(x\). \(\square\)

**Theorem 1.2 (positive second derivatives on an interval).** A real distribution \(v\) satisfies \(v''\ge0\) if and only if it has a finite continuous convex representative. That representative is unique and locally Lipschitz.

**Proof.** Apply Theorem 1.1 to \(v'\) to obtain an increasing locally bounded \(g\). Set

\[
V(x)=\int_{x_0}^xg(t)\,dt.
\tag{1.4}
\]

On a compact interval, the bound for \(g\) proves a Lipschitz estimate for \(V\). The same Fubini argument as (1.3), now for the signed locally finite density \(g(t)\,dt\), proves \(V'=g\). Thus \(v-V\) is a real constant. If \(a<b<c\), compare the averages of \(g\) on the two ordered intervals:

\[
\frac{V(b)-V(a)}{b-a}\le
\frac{V(c)-V(b)}{c-b}.
\tag{1.5}
\]

One direct justification is to integrate the nonnegative function \(g(t)-g(s)\) for \(a<s<b<t<c\). Multiplying out (1.5) is the chord inequality, so \(V\) plus a constant is convex.

Conversely, nonnegative local averaging preserves the chord inequalities of a continuous convex function. The symmetric second difference of a smooth convex function is nonnegative; dividing by its squared increment and taking the limit proves its second derivative is nonnegative. Pass to the distributional limit of the averages. The construction just proved then supplies a locally Lipschitz representative, and the two continuous representatives agree everywhere. \(\square\)

**Proposition 1.3 (one-sided and even averages).** Let \(\rho\ge0\) be smooth, compactly supported and of integral one. All arguments below must stay in \(I\). If \(\operatorname{supp}\rho\subset(0,\infty)\) and \(F\) is increasing, then

\[
L_\epsilon(x)=\int F(x-\epsilon t)\rho(t)\,dt
\tag{1.6}
\]

is increasing in \(x\), decreasing in \(\epsilon>0\), and increases to \(F(x-)\) as \(\epsilon\downarrow0\). The forward average tends to \(F(x+)\). If \(\rho\) is even and \(V\) is finite convex, then

\[
A_\epsilon(x)=\int V(x-\epsilon t)\rho(t)\,dt
\tag{1.7}
\]

is convex in \(x\), increasing in \(\epsilon\ge0\), and tends to \(V(x)\) as \(\epsilon\downarrow0\).

**Proof.** Ordered arguments give all inequalities for \(L_\epsilon\). A locally bounded increasing function has finite one-sided limits: the left value is a supremum and the right value an infimum on a sufficiently small interval, by real completeness. Dominated convergence then gives both limits.

The finite convex function \(V\) is continuous locally. For an interior point \(c\), choose \([c-2r,c+2r]\subset I\). Convexity bounds \(V\) above there by the larger endpoint value \(C\); the midpoint inequality bounds it below on \([c-r,c+r]\) by \(L=2V(c)-C\). For \(p<q\) in \([c-r/2,c+r/2]\), ordered secant slopes bound the slope on \([p,q]\) below by the slope on \([c-r,p]\) and above by the slope on \([q,c+r]\). Both comparison intervals have length at least \(r/2\), and their value differences have modulus at most \(C-L\). Hence \(|V(q)-V(p)|\le 2(C-L)|q-p|/r\), proving local Lipschitz continuity without assuming it.

Pair \(t\) and \(-t\). For fixed \(t>0\),

\[
q(s)=V(x-st)+V(x+st)
\tag{1.8}
\]

is even and convex. If \(0\le a\le b\), express \(a\) as a convex combination of \(-b,b\); convexity and evenness give \(q(a)\le q(b)\). Integrate against \(\rho(t)\). Integrating shifted chord inequalities gives convexity in \(x\); continuity and a bound on the compact range of arguments give the limit. \(\square\)

For complex distributions, a positive first derivative leaves an imaginary constant, and a positive second derivative leaves an imaginary affine function. This follows by applying the zero-derivative fact to the imaginary part once or twice; Solution 2 gives the precise statements.

## Sphere averages reveal point sources

Let \(\sigma_{n-1}\) be the area of the unit sphere \(S^{n-1}\); in dimension one use counting measure on \(\{-1,1\}\) and \(\sigma_0=2\). The point-source theorem cited above proves

\[
\Phi_n(x)=
\begin{cases}
|x|/2,&n=1,\\
\log|x|/(2\pi),&n=2,\\
-|x|^{2-n}/((n-2)\sigma_{n-1}),&n\ge3,
\end{cases}
\qquad \Delta\Phi_n=\delta_0.
\tag{2.1}
\]

These kernels are locally integrable. Write \(\phi_n(r)\) for the radial value at \(r>0\). Differentiation gives

\[
\phi_n'(r)=\frac1{\sigma_{n-1}r^{n-1}}.
\tag{2.2}
\]

Set \(\Phi_n(0)=-\infty\) for \(n\ge2\), and \(\Phi_1(0)=0\). The kernel is smooth and harmonic away from zero. For smooth \(f\), define

\[
M_f(x,r)=\frac1{\sigma_{n-1}}\int_{S^{n-1}}f(x+r\omega)\,dS(\omega).
\tag{2.3}
\]

Differentiating on the fixed compact sphere and using its scaling from A4 and the flux theorem gives

\[
\partial_rM_f(x,r)
=\frac1{\sigma_{n-1}r^{n-1}}
                 \int_{B_r(x)}\Delta f(y)\,dy.
\tag{2.4}
\]

For \(n=1\), this is
\([f'(x+r)-f'(x-r)]/2=\tfrac12\int_{x-r}^{x+r}f''\),
the fundamental theorem. A harmonic function therefore has sphere mean \(f(x)\), from the limit at zero.

We supply the surface facts needed when a sphere passes through a pole. Surface measure is invariant under every orthogonal map \(Q\). To prove this from the supplied foundations, apply polar integration to \(1_{\{1<|x|<2\}}g(x/|x|)\) and to its composition with \(Q\), first for bounded Borel \(g\). The linear change-of-variables formula gives equal Euclidean integrals since \(|\det Q|=1\). Cancelling the positive radial integral proves invariance on the sphere.

For \(n\ge2\), after such a rotation, a neighborhood of a chosen point is
\(\omega(\xi)=(\xi,\sqrt{1-|\xi|^2})\), \(|\xi|<1/2\). The graph density proved in U011 is
\((1-|\xi|^2)^{-1/2}\le2\). Moreover
\[
|\xi|\le|\omega(\xi)-\omega(0)|\le\sqrt2|\xi|.
\tag{2.4a}
\]
Indeed the squared chord length is \(2|\xi|^2/(1+\sqrt{1-|\xi|^2})\). The rotation can be obtained by completing the unit vector to an orthonormal basis, as proved by Gram–Schmidt in the finite-algebra prerequisite.

It follows that a cap of chord radius \(\eta<1/2\) has measure at most \(C_n\eta^{n-1}\), by containing its projected coordinates in a box. Every nonempty open cap has positive measure, since its projection contains an open box and the density is positive. A point has measure zero for \(n\ge2\). On the dyadic rings of chord radii between \(2^{-j-1}\eta\) and \(2^{-j}\eta\),
the integral of the power \(|\omega-\omega_0|^{2-n}\), \(n\ge3\), is at most \(C_n\eta2^{-j}\). For \(n=2\), the corresponding logarithmic bound is \(C\eta2^{-j}(1+|\log\eta|+j)\). Summing proves integrability of both singularities on the sphere, using only the geometric series and its differentiated sum.

**Lemma 2.1 (the shell formula).** For every \(r>0\) and \(y\in\mathbb R^n\),

\[
\frac1{\sigma_{n-1}}\int_{S^{n-1}}\Phi_n(r\omega-y)\,dS(\omega)
=\phi_n(\max(r,|y|)).
\tag{2.5}
\]

The integral is finite even when the sphere meets the pole.

**Proof.** In dimension one direct evaluation gives

\[
\frac{|r-y|+|-r-y|}{4}=\frac{\max(r,|y|)}2.
\tag{2.6}
\]

Suppose \(n\ge2\) and \(d=|y|>0\). For \(r<d\), the translated kernel is harmonic on the closed ball, so its mean is \(\Phi_n(-y)=\phi_n(d)\). For \(r>d\), apply the flux theorem to \(B_r(0)\) with a small closed ball about \(y\) removed. The kernel is harmonic there. On the small sphere, its outward radial flux is \(\sigma_{n-1}\epsilon^{n-1}\phi_n'(\epsilon)=1\); the hole's normal reverses its sign. Thus the flux on the outer sphere is one. Differentiation of its mean gives \(\phi_n'(r)\).

To identify the constants on the two sides, put \(\omega_0=y/d\). For \(d/2<r<3d/2\),

\[
|r\omega-y|^2=(r-d)^2+rd|\omega-\omega_0|^2.
\tag{2.7}
\]

For \(n\ge3\), the absolute kernel is bounded by a constant depending on \(d,n\) times \(|\omega-\omega_0|^{2-n}\). For \(n=2\), it is bounded by \(C_d(1+|\log|\omega-\omega_0||)\): the displayed lower bound controls the negative logarithm, and a uniform upper bound on the distance controls the positive logarithm. The integrability just proved and dominated convergence show that the mean is finite and continuous at \(r=d\). Thus the above-\(d\) mean with derivative \(\phi_n'\) joins the value \(\phi_n(d)\), and equals \(\phi_n(r)\). If \(y=0\), the integrand is constant on the sphere. \(\square\)

**Proposition 2.2 (positive potentials and their averages).** For a compactly supported positive Radon measure \(\nu\), put

\[
W(x)=\int\Phi_n(x-y)\,d\nu(y).
\tag{2.8}
\]

For \(n=1\), \(W\) is finite and continuous. For \(n\ge2\), it takes values in \([-\infty,\infty)\) and is upper semicontinuous. In every dimension it is locally integrable, represents \(\Phi_n*\nu\), and satisfies \(\Delta W=\nu\). Its finite sphere means are

\[
M_W(x,r)=\int\phi_n(\max(r,|x-y|))\,d\nu(y).
\tag{2.9}
\]

They increase with \(r\) and decrease to \(W(x)\) as \(r\downarrow0\), including the value \(-\infty\).

**Proof.** The measure has finite total mass, since its support is compact. On compact sets of \(x\) and \(y\), the kernel has a common finite upper bound \(C\). Its integral means \(C\nu(\mathbb R^n)-\int(C-\Phi_n(x-y))\,d\nu(y)\), and is therefore well-defined. The kernel is continuous with extended value \(-\infty\) at zero for \(n\ge2\). Fatou applied to its nonnegative complement gives

\[
\limsup_{j\to\infty}W(x_j)\le W(x)\quad\text{if }x_j\to x.
\tag{2.10}
\]

This proves upper semicontinuity even at infinite negative values. For \(n=1\), the continuous kernel is uniformly bounded on every compact difference set; dominated convergence proves the assertion.

For compact \(K\) and \(y\) in the support of \(\nu\), the translated set \(K-y\) is contained in one bounded ball. Translation invariance and local integrability of the kernel give

\[
\sup_{y\in\operatorname{supp}\nu}\int_K|\Phi_n(x-y)|\,dx<\infty.
\tag{2.11}
\]

Tonelli gives an integrable absolute double integral over \(K\) and the measure, so \(W\in L^1_{\rm loc}\) and is finite almost everywhere. Absolute Fubini identifies the distribution with the compact-factor convolution of U021. Derivative transfer and (2.1) give \(\Delta W=\nu\).

For a fixed sphere, subtract the same common upper bound before using nonnegative product-measure Tonelli. Lemma 2.1 then proves (2.9), including any initially extended integrals. Its right-hand integrand is bounded above and below because \(r>0\) and \(y\) ranges over a compact set. Thus the sphere integral is finite. Formula (2.2) proves monotonicity; as \(r\downarrow0\) the integrands decrease to \(\Phi_n(x-y)\). Subtract them from a fixed common upper bound and apply monotone convergence, obtaining the asserted value at every \(x\). \(\square\)

## A positive Laplacian selects one function

A function \(v:X\to[-\infty,\infty)\) is upper semicontinuous if \(\{v<a\}\) is open for every real \(a\). It is then Borel measurable and bounded above on compact sets: choose a local finite upper bound at each point and use a finite subcover. On a nonempty compact set its supremum is attained. Unless all values are \(-\infty\), choose a sequence approaching the finite supremum, take a convergent subsequence, and apply upper semicontinuity.

We call \(v\) **subharmonic** when it is upper semicontinuous, is not identically \(-\infty\) on any connected component, and satisfies

\[
v(x)\le M_v(x,r)
\quad\text{whenever }\overline{B_r(x)}\subset X.
\tag{3.1}
\]

The sphere integral initially has an extended value: its positive part is bounded on that compact sphere, and its negative part may have infinite integral.

**Theorem 3.1 (the canonical representative).** If \(u\) is a real distribution on an arbitrary open \(X\subset\mathbb R^n\), \(n\ge1\), with \(\Delta u\ge0\), it has exactly one subharmonic representative \(u_0\). It belongs to \(L^1_{\rm loc}(X)\); every admissible sphere mean is finite and increases with radius. At each point,

\[
u_0(x)=\lim_{r\downarrow0}M_{u_0}(x,r)
=\lim_{r\downarrow0}\frac1{|B_r|}\int_{B_r(x)}u_0(y)\,dy.
\tag{3.2}
\]

Write \(\mu=\Delta u\). For every closed ball contained in \(X\),

\[
M_{u_0}(x,r)-u_0(x)
=\int_{|x-y|<r}[\phi_n(r)-\Phi_n(x-y)]\,d\mu(y)
\tag{3.3}
\]

and

\[
M_{u_0}(x,r)-u_0(x)
=\int_0^r\frac{\mu(B_t(x))}{\sigma_{n-1}t^{n-1}}\,dt.
\tag{3.4}
\]

Both right sides are nonnegative, possibly infinite. When \(u_0(x)=-\infty\), the left side is the finite sphere mean minus \(-\infty\), hence \(+\infty\). In the plane the identity is

\[
2\pi[M_{u_0}(x,r)-u_0(x)]
=\int_{|x-y|<r}\log\frac r{|x-y|}\,d\mu(y).
\tag{3.5}
\]

**Proof.** Positivity makes \(\mu\) a positive Radon measure. For a closed ball strictly inside \(X\), choose \(0\le\chi\le1\), smooth and compactly supported in \(X\), equal to one on a neighborhood \(V\) of the ball. The cutoff construction is supplied in the scalar/test foundations. Extend the compactly supported measure \(\chi\mu\) by zero to \(\mathbb R^n\), and set

\[
W=\Phi_n*(\chi\mu),\qquad h=u-W.
\tag{3.6}
\]

Then \(\Delta h=0\) on \(V\). The harmonic distribution lemma in U013, “Local smoothing for both constant symbols,” proves that \(h\) has a smooth harmonic representative on this arbitrary open set. Put \(v=W_0+h\), using the pointwise potential from Proposition 2.2. It is upper semicontinuous and locally integrable. Its sphere means on closed balls in \(V\) are finite, increase with radius and tend to its center value, since the harmonic term's mean is constant.

The polar formula gives \(|B_r|=\sigma_{n-1}r^n/n\) and

\[
\frac1{|B_r|}\int_{B_r(x)}v
=n\int_0^1 t^{n-1}M_v(x,rt)\,dt.
\tag{3.7}
\]

This also holds in dimension one by splitting an interval into its two half-intervals. For \(r\le r_0\) small, the sphere means are bounded above by \(M_v(x,r_0)\). After subtracting from that finite bound, monotone convergence proves that (3.7) tends to \(v(x)\), even when \(v(x)=-\infty\); the weight \(nt^{n-1}\) has integral one.

Any two local constructions represent the same distribution. They agree almost everywhere on their overlap by the identification fact, so their small ball averages agree. Their limits in (3.7) show agreement at every point. They therefore define a function \(u_0\) throughout \(X\). It is locally integrable, so it cannot equal \(-\infty\) throughout any nonempty open subset; components of an open Euclidean set are open because every small ball is connected. It has (3.1) and (3.2).

For a particular admissible closed ball, choose \(\chi=1\) near that whole ball in (3.6). This represents the same \(u_0\) at every point by the gluing argument. The harmonic contribution cancels from the mean difference. In (2.9) the kernel difference is zero for \(|x-y|\ge r\), and is the nonnegative quantity in (3.3) for \(|x-y|<r\), where \(\chi\mu=\mu\). If the center potential is finite, ordinary subtraction applies. If it is \(-\infty\), subtracting the center kernel from the bounded finite averaged kernel gives a nonnegative integral of value \(+\infty\). Thus (3.3) holds in both cases. The same construction for any larger admissible ball proves monotonicity for every pair of admissible radii.

For \(0<\rho<r\), the fundamental theorem and (2.2) give

\[
\phi_n(r)-\phi_n(\rho)=
\int_\rho^r\frac{dt}{\sigma_{n-1}t^{n-1}}.
\tag{3.8}
\]

At \(\rho=0\), pass to the limit; it is finite when \(n=1\) and infinite when \(n\ge2\), exactly as the chosen center values require. Nonnegative Tonelli now proves (3.4) from (3.3), using \(1_{\{|x-y|<t\}}\). The choice of an endpoint in each inner \(dt\) integral has no effect; an atom with \(|x-y|=r\) contributes zero. Inserting the planar kernel gives (3.5). Uniqueness among all subharmonic representatives follows from the converse below. \(\square\)

**Theorem 3.2 (submean functions have positive Laplacian).** Every function satisfying the definition (3.1) is locally integrable, has positive distributional Laplacian, and agrees at every point with the representative in Theorem 3.1.

**Proof.** First suppose \(v(a)>-\infty\), and fix a closed ball about \(a\) inside \(X\). Let \(C\) be a finite upper bound there. On every smaller sphere, submean gives
\(M_{C-v}(a,r)\le C-v(a)<\infty\).
Polar Tonelli, with its nonnegative integrand, proves integrability of \(C-v\) on each smaller ball. Thus \(v\) is integrable there.

Let \(G\subset X\) be the open set of points with an integrable neighborhood. It meets each connected component because the definition gives a finite point there. It is relatively closed as well. If \(a\in\overline G\cap X\), choose \(R>0\) with \(\overline{B_{4R}(a)}\subset X\). The nonempty open set \(G\cap B_R(a)\) contains a point \(b\) with \(v(b)\) finite, since \(v\) is finite almost everywhere locally on \(G\). The preceding argument, using a ball of radius greater than \(2R\) about \(b\) still inside \(B_{4R}(a)\), proves integrability on \(B_{2R}(b)\), which contains \(B_R(a)\). Therefore \(a\in G\). Connectedness on each component implies \(G=X\).

Take a nonnegative smooth unit-mass kernel \(\rho_\epsilon\) supported in radius \(\epsilon\). Local convolution gives a smooth \(v_\epsilon=v*\rho_\epsilon\). For each sphere with all its \(\epsilon\)-translates compactly inside \(X\), integrate (3.1) at the shifted centers. The product integral involving \(|v(x-y+r\omega)|\rho_\epsilon(y)\) is finite: for each \(\omega\), bound \(\rho_\epsilon\) by its supremum and integrate \(|v|\) on one common compact set, then multiply by the finite sphere area. Fubini is therefore legitimate and gives \(v_\epsilon(x)\le M_{v_\epsilon}(x,r)\).

For smooth \(f\), Taylor's formula with a remainder uniform in \(\omega\) gives

\[
M_f(x,r)=f(x)+\frac{r^2}{2n}\Delta f(x)+o(r^2).
\tag{3.9}
\]

Here reflection of one coordinate makes the means of \(\omega_j\) and \(\omega_j\omega_k\), \(j\ne k\), zero. Coordinate permutations make all means of \(\omega_j^2\) equal, and their sum is one, so each is \(1/n\). These measure symmetries were proved before Lemma 2.1 and hold directly on the two-point sphere when \(n=1\). The uniform \(o(r^2)\) follows by the twice-integrated fundamental theorem and continuity of the Hessian on a compact ball.

The smooth submean inequality and (3.9) imply \(\Delta v_\epsilon\ge0\). Local approximation from U021 gives \(v_\epsilon\to v\) distributionally, so testing on a nonnegative test proves \(\Delta v\ge0\).

Finally integrate (3.1) in the radius:

\[
v(x)\le\frac1{|B_r|}\int_{B_r(x)}v
\le\sup_{B_r(x)}v.
\tag{3.10}
\]

Local integrability makes the middle term finite. If \(v(x)\) is finite, upper semicontinuity bounds the last term by \(v(x)+\eta\) for small \(r\). If \(v(x)=-\infty\), it bounds it by any specified real number for small \(r\). Thus the ball average tends to the given value at every point. The representative supplied by Theorem 3.1 has the same distribution, hence the same ball averages, and the same limiting values. This proves agreement and the promised uniqueness. \(\square\)

**Corollary 3.3 (radial smoothing recovers all point values).** Let \(u_0\) be the canonical representative and let \(\rho\ge0\) be smooth, radial, supported in the unit ball and of integral one. At fixed \(x\), for \(0<\epsilon<\operatorname{dist}(x,X^c)\), the smooth value \((u*\rho_\epsilon)(x)\) increases with \(\epsilon\), is at least \(u_0(x)\), and tends down to \(u_0(x)\) as \(\epsilon\downarrow0\). If \(X=\mathbb R^n\), interpret the distance as infinite.

**Proof.** Write \(\rho(y)=p(|y|)\). Polar integration and sphere reflection invariance give

\[
(u*\rho_\epsilon)(x)
=\sigma_{n-1}\int_0^1p(t)t^{n-1}M_{u_0}(x,\epsilon t)\,dt.
\tag{3.11}
\]

The weights are nonnegative and integrate to one. Theorem 3.1 proves the lower bound and monotonicity. For \(\epsilon\le\epsilon_0\), a common upper bound is \(M_{u_0}(x,\epsilon_0)\); subtract from it and use monotone convergence for the limit, including \(-\infty\). \(\square\)

**Theorem 3.4 (maximum principles).** If \(K\subset X\) is nonempty and compact, then

\[
\sup_Ku_0=\sup_{\partial K}u_0.
\tag{3.12}
\]

If \(X\) is connected and \(u_0\) attains a finite global maximum in \(X\), it is constant.

**Proof.** A nonempty compact subset of \(\mathbb R^n\), \(n\ge1\), has nonempty boundary: a ray from a point eventually leaves the bounded set and has a last initial point in it. If \(u_0\) is \(-\infty\) throughout \(K\), the equality follows. Otherwise its finite maximum \(c\) is attained. If a maximum point \(x\) is interior to \(K\), let \(r=\operatorname{dist}(x,\partial K)>0\). Compactness of the boundary attains this distance; the closed ball lies in \(K\), and its sphere meets \(\partial K\).

The sphere values are at most \(c\), while submean at \(x\) makes their mean at least \(c\). If one sphere value were less than \(c\), upper semicontinuity would make it less by a fixed positive amount on an open cap of positive measure. This would make the mean strictly less than \(c\), a contradiction. In dimension one each endpoint has positive weight. Thus a boundary contact point also has value \(c\), proving (3.12).

For a finite global maximum \(c\), the same argument makes every sufficiently small sphere about a maximum point equal to \(c\). Those spheres fill a neighborhood, so \(\{u_0=c\}\) is open. It is closed because \(\{u_0<c\}\) is open and all values are at most \(c\). Connectedness proves the assertion. \(\square\)

## Positive Hessians force convexity

On an arbitrary open set, convexity here means the chord inequality on every segment contained in that set; the domain itself need not be convex.

**Theorem 4.1 (the distributional Hessian criterion).** For a real distribution \(u\) on open \(X\subset\mathbb R^n\), the following are equivalent: every directional second derivative \(\sum_{j,k}a_ja_k\partial_j\partial_k u\), \(a\in\mathbb R^n\), is positive; and \(u\) has a finite continuous representative \(v\) satisfying

\[
v((1-t)x+ty)\le(1-t)v(x)+tv(y),\qquad0<t<1,
\tag{4.1}
\]

whenever \([x,y]\subset X\). The representative is unique and locally Lipschitz.

**Proof.** The directional condition in the coordinate directions implies \(\Delta u\ge0\). Let \(u_0\) be the canonical representative and smooth with a nonnegative radial kernel. Each directional second derivative of \(u_\epsilon\) is a positive distribution paired with a nonnegative translated kernel, hence is a nonnegative smooth function. Restricting to a segment, the fundamental theorem makes the first derivative increasing; its ordered secant slopes prove the chord inequality.

Any compact segment in \(X\) has positive distance from \(X^c\). For small \(\epsilon\) the preceding argument applies to it. Corollary 3.3 lets \(\epsilon\downarrow0\) in the chord inequality, initially with possible \(-\infty\) endpoint values. If either endpoint tends to \(-\infty\), its positive coefficient forces the right side to \(-\infty\), since the other endpoint has a finite upper bound. Thus the extended inequality also holds.

There are in fact no \(-\infty\) points. If \(u_0(x_0)=-\infty\), choose a ball about \(x_0\) in \(X\). Almost every \(y\) in it has \(u_0(y)\) finite, by local integrability. The midpoint inequality forces \(u_0((x_0+y)/2)=-\infty\). Affine change of variables shows that these midpoints fill almost all of a smaller ball of positive volume, contradicting integrability.

Choose \(\overline{B_{4r}(c)}\subset X\) and a finite upper bound \(C\) for \(u_0\) on it. For \(z\in B_{2r}(c)\), apply the midpoint inequality to \(z,2c-z\):

\[
L:=2u_0(c)-C\le u_0(z)\le C.
\tag{4.2}
\]

For distinct \(p,q\in B_r(c)\) with \(|p-q|\le r\), put \(e=(q-p)/|q-p|\). Ordered secant slopes on the line through \(p-r e,p,q,p+r e\) bound the slope from \(p\) to \(q\) between \(-(C-L)/r\) and \((C-L)/r\). If \(q=p+r e\), use that endpoint slope directly. Therefore

\[
|u_0(q)-u_0(p)|\le\frac{C-L}{r}|q-p|.
\tag{4.3}
\]

For \(|p-q|>r\), the oscillation bound \(C-L\) proves the same inequality; for \(p=q\) it is immediate. This proves local Lipschitz continuity.

Conversely, on a compactly contained ball, smooth the continuous chord-convex \(v\) with a nonnegative kernel. Every sufficiently small translate of a segment in a smaller ball stays inside \(X\); integrating its chord inequality proves convexity of the smoothing there. Symmetric second differences give each smooth directional second derivative nonnegative. Distributional convergence yields positivity on every nonnegative test supported in that ball. A finite nonnegative smooth partition of a general compact test among such balls proves positivity on \(X\). The identification fact gives uniqueness of the continuous representative. \(\square\)

## Exercises

**Exercise 1 (basic: two changes in slope).** For \(\mu=2\delta_{-1}+3\delta_2\), find the right-continuous increasing \(F\) with \(F'=\mu\) and zero left tail, and the convex \(V\) with \(V''=\mu\) and zero left tail. Describe the other real solutions.

**Solution 1.** With right-continuous endpoint values for the steps,

\[
F(x)=2H(x+1)+3H(x-2),\qquad
V(x)=2(x+1)_++3(x-2)_+.
\tag{5.1}
\]

Integration by parts on the two half-lines gives \(H'=\delta_0\) and \((x_+)'=H\). Thus these have the stated derivatives. The slopes of \(V\) are \(0,2,5\), proving convexity by ordered secants. The zero-derivative fact shows that other \(F\)'s differ by a real constant. Applied twice, it makes other \(V\)'s differ by \(ax+b\), \(a,b\in\mathbb R\); an affine addition preserves convexity. The zero left tails fix these ambiguities.

**Exercise 2 (intermediate: positivity does not order complex values).** Examine \(f=i+x_+\) and \(g=ix+x_+^2/2\). State and prove the complex versions of Theorems 1.1–1.2.

**Solution 2.** Both \(f'\) and \(g''\) equal the positive distribution \(H\), although neither function is real-valued. If \(u=p+iq\) with real distributions and \(u'\) is positive, then \(p'\ge0\) and \(q'=0\). Theorem 1.1 makes \(p\) an increasing real function and the zero-derivative fact makes \(q\) constant. Conversely such a sum has positive derivative. If \(u''\) is positive, then \(p''\ge0\) and \(q''=0\). Theorem 1.2 makes \(p\) finite continuous convex; applying the constant fact twice gives \(q=ax+b\). These imaginary affine additions have second derivative zero, proving the converse too.

**Exercise 3 (basic: an increasing sphere mean without convexity).** Compute the Laplacian and circle mean of \(Q(x,y)=2x^2-y^2+xy\), and determine its subharmonicity and convexity.

**Solution 3.** We have \(\Delta Q=4-2=2\). Substitute \(x+r\omega_1,y+r\omega_2\) and use the sphere moments from (3.9). Linear and mixed terms average to zero, and each square moment is \(1/2\). Hence

\[
M_Q((x,y),r)=Q(x,y)+r^2/2.
\tag{5.2}
\]

It is continuous and satisfies submean, so is subharmonic. Its second derivative in the \(y\) direction is \(-2\), so it is not convex.

**Exercise 4 (intermediate: a distribution does not fix a point value).** On \(\mathbb R^2\), let \(v_+\) be zero except \(v_+(0)=1\), and \(v_-\) zero except \(v_-(0)=-1\). Test upper semicontinuity, submean and distributional Laplacians.

**Solution 4.** Both are zero almost everywhere, hence have zero distributional Laplacian. The upward spike is upper semicontinuous but violates submean at zero, where every circle mean is zero. The downward spike satisfies submean: at zero it is \(-1\le0\); any circle about another point meets the exceptional point at most once, which has zero arc measure by the cap estimate. It is not upper semicontinuous at zero. Neither is the canonical representative; that representative is the function identically zero.

**Exercise 5 (intermediate: counting the mass inside a circle).** In the plane put \(a=(1,0)\), \(b=(0,2)\), and

\[
W(z)=\frac{2\log|z-a|+3\log|z-b|}{2\pi}.
\tag{5.3}
\]

Find its Laplacian, mean about zero, and increase over its center value at radii \(1/2,3/2,3\). What happens at center \(a\)?

**Solution 5.** Equation (2.1) gives \(\Delta W=2\delta_a+3\delta_b\), and \(W(0)=3\log2/(2\pi)\). The shell formula gives

\[
M_W(0,r)=\frac{\log\max(1,r)}{\pi}
                  +\frac{3\log\max(2,r)}{2\pi}.
\tag{5.4}
\]

The three values of \(2\pi[M_W(0,r)-W(0)]\) are \(0\), \(2\log(3/2)\), and \(2\log3+3\log(3/2)\). A mass at distance exactly \(r\) contributes \(\log1=0\). At center \(a\), \(W(a)=-\infty\), while every positive-radius mean remains finite by (2.9); the difference and the integral in (3.5) are both \(+\infty\).

**Exercise 6 (advanced: a charged spherical shell).** For probability surface measure \(\nu\) on \(\{|y|=2\}\subset\mathbb R^3\), find \(\Phi_3*\nu\) at every point and check its Laplacian from its derivative jump.

**Solution 6.** Surface scaling identifies \(\nu\) with normalized measure on \(2S^2\). Apply the shell formula, using the evenness of \(\Phi_3\):

\[
W(x)=-\frac1{4\pi\max(|x|,2)}.
\tag{5.5}
\]

It is \(-1/(8\pi)\) inside and \(-1/(4\pi|x|)\) outside, with agreeing values at radius two. Its outward derivative jumps from zero to \(1/(16\pi)\). Apply U011's Green identity separately inside and outside the sphere, cutting off outside the support of the test. The equal boundary values cancel the terms involving the normal derivative of the test; the difference of the two normal derivatives multiplies the test. The ordinary Laplacian on each side is zero. Thus

\[
\Delta W=\frac1{16\pi}\,dS_{\{|x|=2\}}=\nu.
\tag{5.6}
\]

The area is \(4\pi\,2^2=16\pi\), by A5 and surface scaling. No origin source occurs because \(W\) is constant near zero. The positive Laplacian makes this continuous function its canonical subharmonic representative. Along an exterior radial line its second derivative is \(-1/(2\pi r^3)\), so it is not convex.

**Exercise 7 (intermediate: local and global maxima).** Show that \(v(x,y)=x_+\) is subharmonic and has a non-strict local maximum at every point with \(x<0\). Explain why this is consistent with Theorem 3.4.

**Solution 7.** Half-line integration by parts and ordinary Fubini give

\[
\Delta v=\delta_0(x)\otimes1(y).
\tag{5.7}
\]

This is positive: its value on a nonnegative test is the integral of that test on the vertical axis. The function is continuous and convex. By Theorem 4.1 and the identification of its canonical representative, it is subharmonic. It is zero on a neighborhood of every point with \(x<0\), so those are non-strict local maxima. It is unbounded above elsewhere. The constant conclusion of Theorem 3.4 requires an attained finite global maximum.

**Exercise 8 (advanced: the mixed Hessian and a sharp Lipschitz constant).** Compare \(P(x,y)=x^2+y^2+4xy\) and \(V(x,y)=|x|+2|y|\). Compute each directional second derivative, decide convexity, and find the optimal global Euclidean Lipschitz constant for \(V\).

**Solution 8.** For the direction \((a,b)\),

\[
D_{(a,b)}^2P=2a^2+8ab+2b^2.
\tag{5.8}
\]

The coordinate second derivatives are both two, but the value at \((a,b)=(1,-1)\) is \(-4\), so \(P\) is not convex. Its Laplacian is four, so it is subharmonic. For \(V\), the one-dimensional identity \((|x|)''=2\delta_0\) follows by half-line integration by parts. There is no mixed derivative: Fubini integrates a derivative of a compact test in the variable absent from each summand to zero. Hence

\[
D_{(a,b)}^2V=
2a^2\delta_0(x)\otimes1(y)+4b^2\,1(x)\otimes\delta_0(y).
\tag{5.9}
\]

It is positive for every direction, proving convexity. The scalar triangle inequality and the finite-dimensional Cauchy–Schwarz inequality give

\[
|V(x,y)-V(x',y')|
\le |x-x'|+2|y-y'|
\le\sqrt5\sqrt{(x-x')^2+(y-y')^2}.
\tag{5.10}
\]

For the two points \((0,0)\) and \((1,2)\), the value difference is five and their distance is \(\sqrt5\). Thus equality is attained and \(\sqrt5\) is optimal.

## Programme proof locations and freely accessible sources

- [Order, positivity and distributional limits](order-positivity-and-limits.md), Theorem 4.1, and its supplied positive-measure foundation: the full positive Radon representation proof. The zero-derivative and locally integrable identification arguments used here are supplied at the start of this lesson.
- [Boundary flux and weak identities](boundary-flux-and-weak-identities.md), Theorem 2.1 and Corollary 2.2: graph surface measure, flux and Green identity. [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5: polar integration, sphere scaling and exact constants.
- [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md), “Local smoothing for both constant symbols,” harmonic distribution lemma: smooth harmonic representatives on every open subset of every \(\mathbb R^n\), including \(n=1\).
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1: the exact positive Laplacian sources and their locally integrable first derivatives. [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3, Theorem 1.1, Proposition 5.1 and Theorem 5.2: compact-factor convolution, parameter tests, derivative transfer and local smoothing.
- [Integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16.1–16.2: convergence, affine changes, \(L^1\) approximation and product-measure Tonelli/Fubini. [Scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the compactness, calculus, cutoff and Euclidean norm facts.
- Dale Winter, notes prepared in collaboration with Tobias Holck Colding, *Lecture One: Harmonic Functions and the Harnack Inequality*, MIT, 2005, [free course notes](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2005/7fbca0b83afcfc989cfb3e2626053076_lecture1.pdf), §4, pp. 3–4. The smooth sphere-mean derivative and boundary-maximum arguments are compared here.
- *Potential Theory in the Complex Plane*, student write-up of Tobias Mai's Saarland University course, summer 2020, [free university-hosted notes](https://www.math.uni-sb.de/ag/speicher/lehre/PotentialTheorysose20/PotentialTheory_SoSe20_Lecture_typed.pdf), Theorem V.4, Corollary V.10 and Theorems VI.2–VI.4. These supply comparison arguments for local integrability, pointwise recovery and positive potentials; the present lesson proves its normalization, smoothing, singular sphere estimates and canonical construction in full.
