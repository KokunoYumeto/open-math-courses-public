# Angular tests, point jets and polar integration

*Written by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Public domain (CC0).*

These proofs supply the geometric and test-space inputs to [Homogeneous extensions and angular moments](../../src/homogeneous-extensions-and-angular-moments.md). They use the [scalar calculus](metric-foundation-bridges.md), Sections 12–13, the [integration foundations](banach-foundation-bridges.md), Sections 15.0–15.1 and 16.1–16.2, and the [finite-order and bounded-test results](../../src/order-positivity-and-limits.md), Section 1. Surface measure and the flux theorem come from [Boundary flux and weak identities](../../src/boundary-flux-and-weak-identities.md), Theorem 2.1 and Solution 2. The [Schwartz Fourier companion](schwartz-fourier-foundations-U017.md), F3, supplies the Gaussian integral; the [gamma companion](gamma-foundations-U016.md) supplies its Euler normalization and recurrence. No general nonlinear change-of-variables theorem is assumed.

## A1. A concrete sphere test space

For \(n\ge2\), write \(S=\mathbb S^{n-1}\), \(X=\mathbb R^n\setminus\{0\}\), and \(\omega(x)=x/|x|\). The positive square root and chain rule make \(\omega\) smooth on \(X\). Define \(C^\infty(S)\) to be the functions \(g:S\to\mathbb C\) for which
\[
 g^\circ(x)=g(\omega(x))
\]
is smooth on \(X\). Give this space the increasing seminorms
\[
 q_m(g)=\max_{|\alpha|\le m}
       \sup_{1/2\le|x|\le2}|\partial^\alpha g^\circ(x)|,
 \qquad m=0,1,\ldots.
 \tag{A1}
\]
These are finite by compactness. They include the sup norm, so separate functions.

This definition agrees with smoothness in ordinary sphere charts. Explicit charts solve one coordinate as
\(\omega_j=\pm\sqrt{1-|y|^2}\), where \(y\) consists of the other coordinates and \(|y|<1\). Restrict them to the closed sets \(\pm\omega_j\ge1/(2\sqrt n)\); their interiors cover \(S\), because at least one \(|\omega_j|\ge1/\sqrt n\). Chart derivatives of \(g\) are derivatives of \(g^\circ\) composed with these smooth graph maps. Conversely \(g^\circ\) is locally the chart expression composed with the coordinate projection of \(\omega(x)\). Repeated chain and product rules on the finitely many compact chart pieces bound derivatives in either description by finitely many derivatives in the other. Thus (A1) gives the usual smooth topology, with no manifold-distribution theorem required.

The identity \(g^\circ(tx)=g^\circ(x)\), differentiated in \(x\), gives
\[
 \partial^\alpha g^\circ(r\omega)
     =r^{-|\alpha|}\partial^\alpha g^\circ(\omega),\qquad r>0.
 \tag{A2}
\]
Consequently all derivatives on any fixed compact annulus are bounded by \(Cq_m(g)\). Multiplication by a fixed smooth sphere function is continuous by the product rule; reflection \(g(\omega)\mapsto g(-\omega)\) preserves each \(q_m\).

An angular distribution is a continuous complex-linear functional \(T\) on this space. Continuity is equivalent to
\[
 |T(g)|\le Cq_m(g)
 \tag{A3}
\]
for some \(C,m\). Indeed a zero neighborhood involves only finitely many of the increasing seminorms; rescale by their largest one, with the zero-seminorm case settled by arbitrary scalar multiples. A set of sphere tests is bounded exactly when each \(q_m\) is uniformly bounded on it, directly from the finite-seminorm neighborhood definition.

For \(n=1\), take \(S=\{-1,1\}\), \(C^\infty(S)=\mathbb C^2\), and \(q_m(g)=\max(|g(-1)|,|g(1)|)\) for every \(m\). The radial lift is constant on each half-line. Every statement above and below has this interpretation.

## A2. Radial maps and all Taylor remainders

If \(\eta\in C_c^\infty((0,\infty))\), then
\[
 E_\eta g(x)=\eta(|x|)g^\circ(x)
 \tag{A4}
\]
is a compact smooth test supported in one fixed annulus, and
\(\|E_\eta g\|_{C^m}\le C_{\eta,m}q_m(g)\), by (A2) and the product rule. Hence \(E_\eta\) carries bounded sphere-test sets to bounded compact-test sets. The latter characterization, including their common compact support, is proved in U008, (T1).

For a test \(\phi\) supported in an annulus \(a\le|x|\le b\), the angular function
\[
 g(\omega)=\int_a^b h(r)\phi(r\omega)\,dr
\]
is smooth whenever \(h\) is integrable on \([a,b]\). To prove the assertion and the estimate, differentiate its radial lift on \(1/2\le|x|\le2\). The derivatives of \(\omega(x)\) are bounded there. Repeated chain rules give finite sums of derivatives of \(\phi\) through order \(m\), with bounded coefficients and factors \(r^j\), \(0\le j\le m\). Dominated difference quotients justify differentiation under the integral, giving
\[
 q_m(g)\le C_{a,b,m}\|h\|_1\|\phi\|_{C^m}.
 \tag{A5}
\]
The same proof permits an interval starting at zero when the displayed dominating weights are integrable.

We need an estimate preserving a specified power of \(r\) even after arbitrarily many angular derivatives. For \(M\ge1\), repeated one-dimensional integration of the fundamental theorem applied to \(s\mapsto\phi(sx)\) gives
\[
 \phi(x)=\sum_{|\alpha|<M}\frac{x^\alpha}{\alpha!}\partial^\alpha\phi(0)
 +M\sum_{|\alpha|=M}\frac{x^\alpha}{\alpha!}
       \int_0^1(1-s)^{M-1}\partial^\alpha\phi(sx)\,ds.
 \tag{A6}
\]
For clarity, the one-dimensional remainder is
\((M-1)!^{-1}\int_0^1(1-s)^{M-1}h^{(M)}(s)\,ds\).
Induction using integration by parts proves this formula from \(h(1)-h(0)=\int_0^1h'\). For a fixed vector \(x\), the constant-direction operator in the independent variable \(y\) satisfies
\((x\cdot\nabla_y)^M=\sum_{|\alpha|=M}(M!/\alpha!)x^\alpha\partial_y^\alpha\).
This follows by induction on \(M\), using commutation of smooth mixed derivatives; here the coefficients \(x^\alpha\) are constant under differentiation in \(y\). Evaluating at \(y=sx\) gives \(h^{(M)}(s)\). Substitution proves (A6), including its coefficient.

Put
\[
 P_j\phi(\omega)=\sum_{|\alpha|=j}
             \frac{\partial^\alpha\phi(0)}{\alpha!}\omega^\alpha,
 \qquad
 R_M(r,\omega)=\phi(r\omega)-\sum_{j<M}r^jP_j\phi(\omega).
\]
In the remainder expression (A6) substitute \(x=r\omega\) and retain the outside factor \(r^M\). Angular derivatives fall on \(\omega^\alpha\) or on \(\partial^\alpha\phi(sr\omega)\). On the fixed annulus for the radial lift, derivatives of \(\omega\) are bounded; each derivative on the latter expression introduces a factor \(sr\) and at most one more derivative of \(\phi\). For \(0\le r\le1\), all \(sr\le1\). Thus, for every \(q\),
\[
 q_q(R_M(r,\cdot))
       \le C_{M,q}r^M\|\phi\|_{C^{M+q}(\overline B(0,1))}.
 \tag{A7}
\]
This is the full estimate needed for an arbitrary finite-order angular distribution. For \(M=0\) the empty subtraction has the elementary bound (A5), and no negative factorial is used.

If all derivatives of a smooth \(\phi\) through order \(N\) vanish at zero, apply (A6) to \(\partial^\gamma\phi\), with \(M=N+1-|\gamma|\). On a fixed ball this gives
\[
 |\partial^\gamma\phi(x)|
      \le C_\phi |x|^{N+1-|\gamma|},
       \qquad |\gamma|\le N.
 \tag{A8}
\]

## A3. Every point-supported distribution is a finite jet

Let \(u\) be a distribution on \(\mathbb R^n\) supported at zero. On tests supported in one fixed ball, U008's defining finite-order estimate gives \(|u(\psi)|\le C\|\psi\|_{C^N}\). Choose a compact smooth \(\chi=1\) near zero and put \(\chi_\varepsilon(x)=\chi(x/\varepsilon)\). For sufficiently small \(\varepsilon>0\) all these cutoffs lie in that ball, and
\[
 u(\phi)=u(\chi_\varepsilon\phi).
 \tag{A9}
\]
Indeed their difference is a compact test supported away from zero, where \(u\) vanishes.

If \(\phi\) has zero derivatives through order \(N\) at zero, each term in a derivative \(\partial^\alpha(\chi_\varepsilon\phi)\), \(|\alpha|\le N\), is bounded by a constant times
\[
 \varepsilon^{-|\beta|}
       \sup_{|x|\le C_0\varepsilon}|\partial^\gamma\phi(x)|
 \le C_\phi\varepsilon^{N+1-|\alpha|},
 \qquad \beta+\gamma=\alpha,
\]
using (A8). All these bounds tend to zero, so (A9) implies \(u(\phi)=0\). Subtract from an arbitrary \(\phi\) its degree-\(N\) Taylor polynomial multiplied by a fixed cutoff equal to one near zero. The remainder has those zero derivatives. Therefore
\[
 u=\sum_{|\alpha|\le N}c_\alpha\partial^\alpha\delta_0,
 \qquad
 c_\alpha=(-1)^{|\alpha|}
          u\!\left(\chi(x)\frac{x^\alpha}{\alpha!}\right).
 \tag{A10}
\]
These coefficients are unique: the test \(\chi x^\beta/\beta!\) has derivative \(\partial^\alpha\) at zero equal to 1 if \(\alpha=\beta\) and 0 otherwise, for every multiindex in a finite collection. This also proves independence of all finite collections of point jets.

With \(E=\sum_jx_j\partial_j\), testing and the product rule give
\[
 E(\partial^\alpha\delta_0)=-(n+|\alpha|)\partial^\alpha\delta_0,
 \qquad
 \mathcal R(\partial^\alpha\delta_0)=(-1)^{|\alpha|}\partial^\alpha\delta_0.
 \tag{A11}
\]
For the first formula the transpose of \(E\) is \(-n-E\), and
\(\partial^\alpha(E\phi)(0)=|\alpha|\partial^\alpha\phi(0)\).
For the second, \(\partial^\alpha\phi(-x)=(-1)^{|\alpha|}\partial^\alpha\phi(0)\).
The dilation definition also gives directly
\(D_t\partial^\alpha\delta_0=t^{-n-|\alpha|}\partial^\alpha\delta_0\).

## A4. Polar integration from the flux theorem

For \(n\ge2\), let \(\sigma\) be the Euclidean graph surface measure on \(S\) constructed in U011, Theorem 2.1. It is finite because the sphere has a finite cover by compact graph pieces. On a graph \(x_n=\gamma(x')\) its density is \(\sqrt{1+|\nabla\gamma|^2}\). The radius-\(r\) graph is \(x_n=r\gamma(x'/r)\). Its gradient is \(\nabla\gamma(x'/r)\), while affine substitution in the base contributes \(r^{n-1}\). A partition among the finitely many graphs therefore proves, for every nonnegative or integrable \(g\),
\[
 \int_{|x|=r}g(x/r)\,dS_r(x)
       =r^{n-1}\int_Sg(\omega)\,d\sigma(\omega).
 \tag{A12}
\]
The sphere has zero \(n\)-dimensional Lebesgue measure: in each graph cylinder Fubini integrates singleton vertical sections, each of measure zero; finitely many charts suffice.

Take first \(g\in C^\infty(S)\). The vector field \(V(x)=xg^\circ(x)\) has divergence \(ng^\circ(x)\), because \(g^\circ(tx)=g^\circ(x)\) has radial derivative zero. Apply U011's flux theorem to \(a<|x|<b\), with \(0<a<b\), after multiplying \(V\) by a smooth cutoff equal to one near the closed annulus. The normals are \(-x/a\) and \(x/b\); (A12) gives
\[
 \int_{a<|x|<b}g^\circ(x)\,dx
       =\frac{b^n-a^n}{n}\int_Sg\,d\sigma.
 \tag{A13}
\]

We extend this equality to angular Borel sets explicitly. Smooth functions are uniformly dense in \(C(S)\): extend a continuous \(g\) to \(\eta(|x|)g^\circ(x)\) with a compact radial cutoff equal to one near \(S\), and convolve in \(\mathbb R^n\) with a smooth unit-mass bump. Uniform continuity and the integral bound for the bump prove uniform convergence on \(S\). Both finite measures in (A13) consequently agree on continuous \(g\). For an open \(O\subset S\), the continuous functions
\[
 h_j(\omega)=\min(1,j\,\operatorname{dist}(\omega,S\setminus O))
\]
increase to \(1_O\); use \(h_j=1\) if \(O=S\). Monotone convergence gives equality on opens. Opens are intersection-closed and generate the Borel sets, so the finite-measure generating-class argument of the integration foundation, (GM6), gives equality on every Borel set. Thus (A13) holds for all bounded Borel \(g\), and then for nonnegative \(g\) by increasing simple approximation.

The polar map \((r,\omega)\mapsto r\omega\) is a continuous bijection from \((0,\infty)\times S\) to \(X\), with continuous inverse \(x\mapsto(|x|,\omega(x))\). Both spaces have countable bases; hence the product Borel sigma-algebra is generated by radial-interval and angular-Borel rectangles. The pullback of Lebesgue measure and the measure defined by
\[
 \lambda(A)=\int_0^\infty \sigma(\{\omega:(r,\omega)\in A\})
                               r^{n-1}\,dr
\]
agree on these rectangles by (A13), including interval endpoints by the zero sphere-volume statement. The section integral is measurable: for the finite angular measure the class of product sets with a measurable section integral is a Dynkin class, since complements subtract from \(\sigma(S)\) and disjoint unions use monotone convergence. Rectangles belong to it, so (GM6) applies. That same monotone convergence proves countable additivity of \(\lambda\).

On bounded radial intervals bounded away from zero both measures are finite. Apply (GM6) there, then exhaust \((0,\infty)\). Equality on all Borel sets, followed by increasing simple approximation, proves
\[
 \int_{\mathbb R^n} f(x)\,dx
 =\int_0^\infty\int_S f(r\omega)\,d\sigma(\omega)\,r^{n-1}\,dr
 \tag{A14}
\]
for nonnegative Borel \(f\). Equality of the measures also identifies their completions: a Borel null set and every subset of it have zero integral on both sides. Thus (A14) holds for completed-measurable nonnegative \(f\), with the usual almost-everywhere interpretation of sections. Applying it to \(|f|\) and then to the four nonnegative parts proves the formula for every absolutely integrable complex \(f\).

For \(n=1\), take counting measure on \(S=\{-1,1\}\). Formula (A14) is the splitting of the line into two half-lines, with \(r^{n-1}=1\). Formula (A12) is counting measure on the two endpoints. This case requires no graph measure.

## A5. Sphere constants and circular moments

The Gaussian proof in the Schwartz Fourier companion gives
\(\int_{\mathbb R^n}e^{-|x|^2}\,dx=\pi^{n/2}\).
Apply (A14), then substitute \(s=r^2\) in the one-dimensional positive integral. This substitution follows first on compact intervals from the scalar fundamental theorem, then on the whole positive axis by monotone convergence. The Euler gamma integral gives
\[
 \sigma(S)=\frac{2\pi^{n/2}}{\Gamma(n/2)}.
 \tag{A15}
\]
Here \(\Gamma(n/2)>0\) by its positive integral. At \(n=2\) the value is \(2\pi\), since \(\Gamma(1)=1\). At \(n=3\), \(\Gamma(1/2)=2\int_0^\infty e^{-r^2}\,dr=\sqrt\pi\), and recurrence gives \(\Gamma(3/2)=\sqrt\pi/2\); hence the value is \(4\pi\). At \(n=1\) the same formula gives 2, as required.

The opening argument of U011, Corollary 2.4, identifies graph surface measure with arclength on a regular plane curve. Split the circle into finitely many regular arcs to apply it. The unit-circle parametrization \((\cos\theta,\sin\theta)\) has speed one, so
\[
 \int_{S^1}g\,d\sigma
       =\int_0^{2\pi}g(\cos\theta,\sin\theta)\,d\theta.
 \tag{A16}
\]
The scalar foundation's trigonometric addition formulas give
\(\cos^2\theta=(1+\cos2\theta)/2\); its elementary antiderivative yields
\(\int_{S^1}\omega_1^2\,d\sigma=\pi\).

## Freely accessible proof comparisons

[Semyon Dyatlov's lecture notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Theorem 4.19 and Lemma 4.22, give the shrinking-cutoff proof for point-supported distributions. The Taylor formula and every derivative estimate needed by that proof are supplied in A2–A3. Section 5.1 motivates the angular integral; its distributional meaning and every sphere-test estimate are supplied in A1–A2. The polar formula A4 is deduced from the complete earlier programme flux proof, and A5 keeps its constants explicit.
