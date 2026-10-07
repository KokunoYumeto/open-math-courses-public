# Analytic functionals: small exponential losses and a diagonal construction

*Original learner exposition, examples and solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

A compact distribution can differentiate a test only a finite number of times. An analytic functional can use infinitely many derivatives, because a holomorphic test has Cauchy bounds on every disk around its carrier. This lesson explains the Fourier growth that permits that extra freedom, and how a function satisfying the growth bounds reconstructs one well-defined analytic functional.

Read the [complete original proof](analytic-functional-fourier-formal.md) alongside this guide. The actual preceding inputs are [L145 E2, holomorphic extension with a growth bound](../../AN02-L145.html#extension-growth-corollary), and [L122 CF2.1, the compact-distribution Fourier theorem](../../AN02-L122.html#2-the-compact-support-growth-criterion). The extension is used in complex dimension \(2n\); the distribution theorem is used in real dimension \(2n\). These are different roles for the same numeral.

## 1. What the theorem says

Let \(K\) be a nonempty compact convex subset of \(\mathbb R^n\), regarded as a real subset of \(\mathbb C^n\). It can have empty interior. Its support function is

\[
h_K(\eta)=\max_{a\in K}a\cdot\eta.
\tag{L146.1}
\]

An analytic functional carried by \(K\) is initially a complex-linear map on **entire holomorphic tests**, with a separate bound for every complex neighborhood \(\Omega\) of \(K\):

\[
|u(h)|\leq C_\Omega\sup_\Omega|h|.
\tag{L146.2}
\]

Its transform uses the bilinear dot product and no conjugate:

\[
\widehat u(\zeta)=u(e^{-iz\cdot\zeta}).
\tag{L146.3}
\]

[Theorem AF1](analytic-functional-fourier-formal.md#analytic-functional-fourier-theorem) says that these transforms are exactly the entire functions for which

\[
\forall\varepsilon>0\ \exists C_\varepsilon<\infty:
\quad |F(\zeta)|\leq C_\varepsilon
e^{h_K(\operatorname{Im}\zeta)+\varepsilon|\zeta|}.
\tag{L146.4}
\]

The order of the quantifiers matters. The constant may become very large when the allowed loss becomes small. Every positive loss must work. On real frequencies the support term is zero, so the condition allows subexponential growth that exceeds every polynomial.

In contrast, the compact-distribution theorem asks for some fixed polynomial degree:

\[
|F(\zeta)|\leq C(1+|\zeta|)^N
e^{h_K(\operatorname{Im}\zeta)}.
\tag{L146.5}
\]

Any bound (L146.5) implies (L146.4), by absorbing a polynomial into each small exponential with a loss-dependent constant. The converse fails, as Worked example 3 proves.

## 2. The construction, with its coordinates visible

Write \(z=x+iy\), and enlarge the real carrier by a closed Euclidean ball in its complex neighborhood:

\[
L_\varepsilon=(K\times\{0\})+
\varepsilon\overline B_{\mathbb R^{2n}}(0,1).
\tag{L146.6}
\]

Its support function in the two real blocks is

\[
h_{L_\varepsilon}(\eta_1,\eta_2)
=h_K(\eta_1)+\varepsilon\sqrt{|\eta_1|^2+|\eta_2|^2}.
\tag{L146.7}
\]

Make this support function a weight on the imaginary coordinates of \(\mathbb C^{2n}\). Convexity gives the PSH circle inequality, and compactness of \(K\) gives a global Lipschitz bound. The entire function we want to extend is prescribed on the complex graph

\[
\zeta\longmapsto(\zeta,i\zeta),\qquad
\zeta=\xi+i\eta\longmapsto(\xi,\eta,-\eta,\xi).
\tag{L146.8}
\]

The imaginary block of the graph is \((\eta,\xi)\). Therefore the weight on the graph is exactly \(h_K(\eta)+\varepsilon|\zeta|\), the assumed exponent of (L146.4). L145 E2 extends \(F\) to an entire \(G_\varepsilon\) in the bigger complex space with a polynomial times that support-function bound. L122 CF2.1 then returns a distribution \(T_\varepsilon\) supported in the actual real \(2n\)-dimensional set \(L_\varepsilon\).

The transform identity on the graph is

\[
T_\varepsilon(e^{-i(x\cdot\zeta+y\cdot i\zeta)})
=T_\varepsilon(e^{-i(x+iy)\cdot\zeta})=F(\zeta).
\tag{L146.9}
\]

All representatives consequently have the same holomorphic polynomial moments. The global Taylor polynomials of an entire test converge with the finite number of derivatives required by either distribution, so their actions agree on every entire test. This is the compatibility argument that lets us define one functional \(u\), rather than an unrelated functional for each \(\varepsilon\).

For a given neighborhood \(\Omega\) of \(K\), choose a sufficiently small \(L_\varepsilon\) inside it. Insert a cutoff there and bound the finite derivatives of the test by Cauchy's formula on polydiscs still inside \(\Omega\). That gives (L146.2). Every step, including the cutoff estimate and uniqueness, is written in AF2–AF7.

![The exact complex carrier thickening and diagonal frequency coordinates](figures/complex-carrier-and-diagonal.png)

The graph has four real coordinates when \(n=1\). The right panel displays its parameter plane and states all four coordinates; it does not depict an unlabeled spatial projection. The closed thickening on the left is where the auxiliary distribution is supported, not the asserted support of a real one-dimensional distribution.

## 3. Four worked examples

### Worked example 1. A finite jet at a translated real point

Fix \(a\in\mathbb R\) and define

\[
u(h)=\sum_{j=0}^M c_j h^{(j)}(a).
\tag{L146.10}
\]

Choose a closed disk of radius \(r\) centered at \(a\) inside any specified neighborhood. Cauchy's bound gives a valid neighborhood constant \(\sum_j|c_j|j!r^{-j}\), so this functional is carried by \(\{a\}\). Its Fourier transform and support function are

\[
F(\zeta)=e^{-ia\zeta}\sum_{j=0}^M c_j(-i\zeta)^j,
\qquad h_{\{a\}}(\eta)=a\eta.
\tag{L146.11}
\]

For each \(\varepsilon>0\) and \(t\geq0\), the \(j\)-th term of the exponential series proves \(t^j\leq j!\varepsilon^{-j}e^{\varepsilon t}\). Thus (L146.4) holds with \(C_\varepsilon=\sum_j|c_j|j!\varepsilon^{-j}\). This example also satisfies the polynomial criterion (L146.5).

For instance \(u(h)=h'(-2)\) has \(F(\zeta)=-i\zeta e^{2i\zeta}\). Its exponential support term is \(-2\operatorname{Im}\zeta\), which must retain its negative sign when the imaginary part is positive. A distribution representing (L146.10) on real tests is \(\sum_j(-1)^j c_j\partial_x^j\delta_a\), since a distributional derivative contributes the transpose sign.

### Worked example 2. Cancellation of total mass does not give the zero functional

For \(K=[-1,1]\), take \(u(h)=h(1)-h(-1)\). Then

\[
h_K(\eta)=|\eta|,\quad
F(\zeta)=e^{-i\zeta}-e^{i\zeta}=-2i\sin\zeta,
\quad |F(\zeta)|\leq2e^{|\operatorname{Im}\zeta|}.
\tag{L146.12}
\]

The neighborhood bound has constant 2. Its total mass \(u(1)\) and transform \(F(0)\) are zero, but \(u(z)=2\) and \(F'(0)=-2i\). Checking just the value at the origin cannot establish uniqueness. The uniqueness proof uses all derivatives, hence all holomorphic moments, and then the Taylor expansion of every entire test.

### Worked example 3. Infinitely many derivatives at zero

Define

\[
u_0(h)=\sum_{m=0}^\infty\frac{i^m h^{(m)}(0)}{(m!)^2},
\qquad F_0(\zeta)=\sum_{m=0}^\infty\frac{\zeta^m}{(m!)^2}.
\tag{L146.13}
\]

On a closed disk of radius \(r>0\), Cauchy's derivative estimates make the series absolutely convergent and give the explicit constant \(e^{1/r}\) for (L146.2). For each positive loss,

\[
|F_0(\zeta)|\leq e^{2\sqrt{|\zeta|}}
\leq e^{1/\varepsilon}e^{\varepsilon|\zeta|}.
\tag{L146.14}
\]

The first bound follows by taking the diagonal subseries of the positive double series \(e^{\sqrt{|\zeta|}}e^{\sqrt{|\zeta|}}\). The second is the nonnegative-square inequality in AF9. These are actual bounds, not claimed exact values of \(F_0\).

For the test \(z^3\), only one derivative contributes, giving \(u_0(z^3)=-i/6\). Every monomial has a nonzero corresponding moment. AF9 proves that a distribution supported at a point only sees some finite jet, so no point-supported distribution gives this functional. Equally, on the positive real axis, choosing a single term of degree \(m>N\) proves that \(F_0\) eventually exceeds every proposed polynomial bound of degree \(N\).

![The infinite-order example and its explicitly labeled growth bounds](figures/infinite-order-point-growth.png)

This is why requiring a compact distribution on the real carrier would wrongly remove an actual part of the theorem. The auxiliary distributions on arbitrarily small complex thickenings provide the correct construction.

### Worked example 4. Check every block of the diagonal

Take \(n=1\), \(K=[-1,1]\) and \(\varepsilon=1/2\). The bigger-space weight is

\[
\Phi(\zeta_1,\zeta_2)
=|\operatorname{Im}\zeta_1|+
\tfrac12\sqrt{(\operatorname{Im}\zeta_1)^2+
                    (\operatorname{Im}\zeta_2)^2}.
\tag{L146.15}
\]

For \(\zeta=3+4i\), its graph point is \((3+4i,-4+3i)\), with real chart \((3,4,-4,3)\). The imaginary block is \((4,3)\), so \(\Phi=4+5/2=13/2\). The graph norm is \(5\sqrt2\), and its chart volume factor is 2. The weight's global Lipschitz bound is \(R_K+\varepsilon=3/2\). The growth extension gives the polynomial exponent \(4n+1=5\).

The value \(13/2\) is the exponent in an upper bound, not the logarithm of a constructed function's modulus. The distribution returned by the compact Fourier theorem is in real dimension 2, supported in the closed stadium of radius \(1/2\) around \([-1,1]\). The entire extension is in complex dimension 2, or real dimension 4. Confusing these spaces loses both the diagonal identity and the support geometry.

## 4. Ten graded exercises

1. **Foundational: signed support functions.** For \(K=\{(2,-1)\}+r\overline B_{\mathbb R^2}(0,1)\), \(r\geq0\), compute \(h_K\). Then give \(h_{L_\varepsilon}\) with its two real frequency blocks.
2. **Foundational: metric and dimension.** In \(n=2\), compute the norm and induced volume factor of the graph chart, its complex codimension, the real dimension of the carrier thickening, and the polynomial exponent furnished by E2.
3. **Foundational: moments and signs.** Derive \(\partial_1\partial_2 F(0)\) in terms of \(u(z_1z_2)\). Compute the transform of \(h\mapsto h'(a)\) and the real distributional derivative representing it.
4. **Intermediate: the quantifier failure.** For \(K=\{0\}\), show that \(F(\zeta)=e^{-2i\zeta}\) satisfies a bound with loss 2 but fails the theorem's condition. Also disprove that evaluation at 2 is carried by zero using only polynomial tests and a neighborhood of zero.
5. **Intermediate: compatibility.** Suppose two compact distributions on \(\mathbb R^{2n}\) have identical holomorphic polynomial moments. Prove that they agree on entire holomorphic tests. State the convergence needed beyond convergence of values.
6. **Intermediate: local holomorphic tests.** Let \(L=[-1,1]\subset\mathbb C\), and let \(V\) be supported in \(L\) with all holomorphic polynomial moments zero. Use the dilation \(h_\lambda(z)=1/(\lambda z-2)\) to prove \(V(1/(z-2))=0\). Describe a parameter domain containing the interval from 0 to 1.
7. **Intermediate: the infinite-order series.** Compute \(u_0(z^m)\), prove (L146.14), and show that the constants in an arbitrarily small exponential bound cannot remain bounded as the loss tends to zero.
8. **Advanced: the point-support obstruction.** Prove that a distribution supported at a point and of order \(M\) sees only the Taylor jet through degree \(M\), using a shrinking cutoff. Apply it to \(u_0\), without citing a point-support classification theorem.
9. **Advanced: why the carrier is real.** Show that evaluation at \(3i/2\) is carried by that complex point, but its transform cannot satisfy the theorem for any compact real carrier.
10. **Advanced: an explicit neighborhood constant.** In AF7 suppose the distribution estimate has constant \(B\) and order \(M\), every cutoff derivative through order \(M\) is bounded by \(A\), and the admissible Cauchy polydisc radius is \(0<r\leq1\). Give a valid explicit \(C_\Omega\) and justify every factor.

## 5. Complete solutions

### Solution 1

Maximization over the translated ball separates the translation and the ball. The latter has support \(r|\eta|\), attained in the direction of \(\eta\) when it is nonzero. Therefore

\[
h_K(\eta)=2\eta_1-\eta_2+r|\eta|.
\tag{L146.16}
\]

For blocks \(\eta^{(1)},\eta^{(2)}\in\mathbb R^2\), adding the closed complex-neighborhood ball gives

\[
h_{L_\varepsilon}(\eta^{(1)},\eta^{(2)})
=2\eta^{(1)}_1-\eta^{(1)}_2+r|\eta^{(1)}|
+\varepsilon\sqrt{|\eta^{(1)}|^2+|\eta^{(2)}|^2}.
\tag{L146.17}
\]

The translation term retains its sign. The real ball radius \(r\) and the complex thickening radius \(\varepsilon\) have different roles.

### Solution 2

For any \(\zeta\in\mathbb C^2\), the graph norm is \(\sqrt2|\zeta|\). The real graph chart has dimension 4 and metric matrix \(2I_4\), so its volume factor is \(\sqrt{\det(2I_4)}=4\). It has complex dimension 2 inside complex dimension 4, hence complex codimension 2. The carrier thickening lies in \(\mathbb R^4\). E2 gives exponent \(4+2\cdot2+1=9\). The extension's ambient space has real dimension 8.

### Solution 3

Differentiation of the negative exponential gives

\[
\partial_1\partial_2F(0)=(-i)^2u(z_1z_2)=-u(z_1z_2).
\tag{L146.18}
\]

In one variable, the derivative test has transform \(-i\zeta e^{-ia\zeta}\). The distribution \(-\partial_x\delta_a\) acts on \(h\) as \(h'(a)\), because \((\partial_x\delta_a)(h)=-h'(a)\). This pairing is complex-linear; inserting a conjugation would change the convention.

### Solution 4

We have \(|F(\zeta)|=e^{2\operatorname{Im}\zeta}\leq e^{2|\zeta|}\), so the single-loss estimate holds with constant 1. Along \(\zeta=it\), \(t>0\), the required estimate with a loss \(\varepsilon<2\) would give \(e^{(2-\varepsilon)t}\leq C_\varepsilon\), impossible as \(t\to\infty\).

For the neighborhood \(\Omega=\{|z|<1\}\), take \(h_N(z)=(z/2)^N\). Evaluation at 2 is 1, while \(\sup_\Omega|h_N|=2^{-N}\). No fixed neighborhood constant can satisfy \(1\leq C_\Omega2^{-N}\) for all \(N\). Thus the original definition fails as well.

### Solution 5

Their difference has compact support and a finite distribution order \(M\) on a compact neighborhood of that support. Expand an entire test in its global Taylor series on a larger polydisc. Cauchy coefficient bounds imply uniform convergence of the polynomials and their holomorphic derivatives through order \(M\) on a smaller polydisc containing the support neighborhood. For a holomorphic function each real derivative is a holomorphic derivative multiplied by a power of \(i\). Insert a fixed cutoff and apply the finite-order estimate to the difference between the test and each Taylor polynomial. The pairing difference tends to zero. Since it is zero on each polynomial, it is zero on the entire test. Uniform convergence of values alone would not justify applying an order-\(M\) distribution.

### Solution 6

For \(z\in[-1,1]\), the denominator can vanish only if \(\lambda\) is real and \(|\lambda|\geq2\). Thus use

\[
\Lambda=\mathbb C\setminus
\bigl(( -\infty,-2]\cup[2,\infty)\bigr).
\tag{L146.19}
\]

It is open and contains \([0,1]\). Near any fixed parameter in it, compactness supplies a common neighborhood of \(L\) with denominator bounded away from zero, so pairing with \(V\) is holomorphic in the parameter by its finite-order estimate. For small \(\lambda\), the series

\[
\frac1{\lambda z-2}
=-\frac12\sum_{m=0}^\infty(\lambda z/2)^m
\tag{L146.20}
\]

converges uniformly with the required derivatives near \(L\). Each term pairs to zero. The parameter identity principle on the component containing \([0,1]\) gives zero at \(\lambda=1\), which is the requested assertion. This is the concrete dilation argument of AF8.

### Solution 7

Only the \(m\)-th derivative of \(z^m\) is nonzero at zero, and it equals \(m!\). Thus \(u_0(z^m)=i^m/m!\). Absolute values of the transform series are bounded by its series in \(|\zeta|\). Put \(s=\sqrt{|\zeta|}\); the diagonal terms of \(e^se^s\) are exactly \(s^{2m}/(m!)^2\). This gives the first bound in (L146.14). Expanding \((\sqrt{\varepsilon|\zeta|}-1/\sqrt\varepsilon)^2\geq0\) gives the second.

If constants stayed bounded by \(C\) along losses tending to zero, the bound at each fixed positive real \(x\) would imply \(F_0(x)\leq C\). But the first two terms give \(F_0(x)\geq1+x\). This contradicts a bound independent of \(x\). The explicit available constant \(e^{1/\varepsilon}\) is allowed to diverge; no optimality for it is asserted.

### Solution 8

Subtract the Taylor polynomial of total degree \(M\) from a smooth test to obtain \(R\). On a ball of radius proportional to \(t\), its derivative of order \(j\leq M\) is bounded by \(C_jt^{M+1-j}\). A cutoff \(\chi(x/t)\) has derivatives of order \(k\) bounded by a constant times \(t^{-k}\). In a Leibniz term of total order \(|\beta|\leq M\), the product is therefore bounded by a constant times \(t^{M+1-|\beta|}\), at most a constant times \(t\) for \(0<t\leq1\). The cutoff equals one near the support point, so the distributional action on \(R\) equals its action on the cutoff remainder. The finite-order estimate makes that action tend to zero. Hence it is zero, and the distribution depends only on the jet through order \(M\). For \(m>M\), the test \(z^m\) has that jet zero; the nonzero value \(i^m/m!\) of \(u_0\) contradicts representation by such a distribution.

### Solution 9

Evaluation at \(3i/2\) is bounded by the supremum on any neighborhood of that point, with constant 1. Its negative-exponential transform is \(e^{3\zeta/2}\). For any compact real \(K\), its support function is zero at imaginary frequency zero. Along \(\zeta=x>0\), a bound (L146.4) with any loss \(\varepsilon<3/2\) would require \(e^{(3/2-\varepsilon)x}\leq C_\varepsilon\), a contradiction. A complex point carrier does not fall under the real-carrier theorem.

### Solution 10

A valid constant is

\[
C_\Omega=B A\,2^M M!\,r^{-M}.
\tag{L146.21}
\]

In the Leibniz rule for a real derivative of total order \(|\beta|\leq M\), the sum of the binomial coefficients is \(2^{|\beta|}\leq2^M\). Each cutoff derivative is at most \(A\). Each real derivative of the holomorphic test reduces, up to a unit complex factor, to a holomorphic multiindex derivative of total order at most \(M\). Its Cauchy factorial is at most \(M!\), and \(r^{-|\alpha|}\leq r^{-M}\) because \(r\leq1\). Multiply these bounds and the distribution constant \(B\). The same argument applies to a test holomorphic only on the chosen neighborhood. A coarse finite constant suffices for the carrier definition; it need not be optimal.

## 6. What is established and what comes later

The full proof establishes the exact every-loss Fourier criterion, uniqueness on entire tests, compatibility of auxiliary distributions, and a uniquely bounded action on holomorphic germs for this convex real carrier. It also gives an explicit infinite-order point functional. It does not assert that all analytic functionals are compact real distributions, nor a theorem for arbitrary complex carriers. The later weighted Fourier estimates and remaining course targets require their own proofs.

Human scholarly sources: Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.1, Theorem 15.1.5, printed p. 276; and volume I, Definition 9.1.1 and the local-test discussion following Proposition 9.1.2, printed pp. 326–328. Original derivations and scope comparisons are in the formal companion. Native protected pages are excluded from the original distributable packet.
