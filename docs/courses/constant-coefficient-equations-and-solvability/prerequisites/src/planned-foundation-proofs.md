# Planned prerequisites for AN-02

This page records precisely stated prerequisites and their individual proof statuses. Each entry links to an available proof or identifies the statement still needed. Other entries retain their stated statuses; recursive prerequisite closure remains incomplete.

## Local distributional Holmgren uniqueness

Contract identifier: `generic-noncharacteristic-Holmgren`. Proof status: available.

A distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. [Analytic coefficients and one-sided uniqueness](../../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2, supplies the complete proof for every scalar order and for square systems with invertible highest normal coefficient.

The proof first reduces every finite order to the available first-order distributional theorem, then handles a \(C^1\) surface by an interior analytic-paraboloid contact. It assumes no regularity, trace or growth bound for the solution. The other cone, order and microlocal prerequisites retain their separate statuses.

## Homogeneous hyperbolic component cone and zero-free tube

The proof is available in [Real roots and their convex component](../../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1.

**Theorem.** For a positive-degree homogeneous \(F\), if \(F(N)\ne0\) and \(F(\xi+zN)\) has only real roots for every real \(\xi\), the component \(\Gamma(F,N)\) of \(N\) in \(\{F\ne0\}\subset\mathbb R^n\) is an open convex cone. Every \(\theta\in\Gamma\) is a hyperbolic direction, \(F/F(N)\) has real coefficients, and the roots of \(F(x+z\theta)\) are strictly negative exactly when \(x\in\Gamma\). Also \(F(x+iy)\ne0\) for real \(x\), \(y\in\Gamma\).

The proof includes multiple roots and complex coefficients. The zero-free tube uses imaginary vectors inside the open component; no zero-free boundary assertion is made. Nonzero constant polynomials are treated separately. The analytic Taylor-order theorem is available in [One-sided root bounds and Taylor order](../../AN02-L193.html#4-the-zero-bound-forces-the-taylor-order), Theorem 4.1.

## Local tangent tubes and closed positive polars

For a fixed homogeneous hyperbolic polynomial, [Tangent cones that permit an imaginary push](../../AN02-L118.html#exact-scope-and-mathematical-inputs) proves the tangent-order adapter, the compact smaller-cone imaginary tube with its multiplicity power, persistence of permitted directions, the closed graph of the positive polars, and uniform compact-field bounds. Its complete proof supplies the polynomial cone and deformation inputs used by the sphere and equatorial cycle constructions. The tangent degree may change. Both imaginary signs, repeated roots and degree-zero points are included.

The broader real-analytic microhyperbolic theorem is a separate foundation topic; these polynomial applications use the full polynomial proof available here.

## One-sided analytic zero-strip total Taylor order

The proof is available in [One-sided root bounds and Taylor order](../../AN02-L193.html#4-the-zero-bound-forces-the-taylor-order), Theorem 4.1.

**Theorem.** If a germ \(g(z,\lambda)\) is holomorphic at zero, \(g(z,0)\) has exact order \(d\), and every local zero with real \(\lambda\) satisfies \(\operatorname{Im}z\le C|\lambda|\), the total Taylor order of \(g\) is at least \(d\). The assertion permits complex coefficients and uses both signs of the real parameter.

The proof controls the entire convergent series and retains every root multiplicity. Both real parameter signs are essential; no reality assumption on the coefficients is needed. The axis coefficient also shows that the total order equals the finite axis order.

## Compact Fourier division and exponential-polynomial annihilator equivalence

Contract identifier: `compact-support-polynomial-division`. Proof status: planned.

Fix a nonzero complex polynomial \(P\), put \(D=-i\partial\), and use complex-linear distribution pairings. The formal transpose is
\[
P^t=P(-D).
\]
For a compactly supported distribution \(v\), \(\operatorname{ch}\operatorname{supp}v\) denotes the convex hull of its support.

Applications: [Approximation and global solvability from support geometry](../../src/approximation-and-global-support-solvability.md).

An **exponential-polynomial solution** is a function
\[
h(x)=e^{ix\cdot z}A(x),\qquad z\in\mathbb C^n,
\quad A\text{ a polynomial},\qquad P(D)h=0.
\tag{1}
\]
Equivalently, \(P(D+z)A=0\). The polynomial factor records multiplicities; the class includes more than the plane exponentials for which \(P(z)=0\).

Applications: [Approximation and global solvability from support geometry](../../src/approximation-and-global-support-solvability.md).

- If \(\mu\) is compactly supported and annihilates every solution in (1), then there is a compactly supported \(v\) with
  \[
  P^tv=\mu.
  \tag{3}
  \]
  The solution is unique by (2). In Fourier–Laplace language, annihilation makes \(\widehat\mu(z)/P(-z)\) entire, and polynomial division preserves the growth estimate needed for compact support.

Applications: [Approximation and global solvability from support geometry](../../src/approximation-and-global-support-solvability.md).

For compact \(\mu\), set
\[
F(\zeta)=\widehat\mu(\zeta)
=\mu\bigl(e^{-ix\cdot\zeta}\bigr).
\tag{4}
\]
This is entire. The transpose of \(P(D)\) is \(P(-D)\), so the divisor relevant to (4) is \(P(-\zeta)\).

Applications: [Choosing polynomial and exponential approximants](../../src/choosing-polynomial-and-exponential-approximants.md).

- \(\mu\) annihilates every exponential-polynomial solution \(e^{ix\cdot z}A(x)\) of the equation if and only if \(F(\zeta)/P(-\zeta)\) is entire.
- The quotient is entire if and only if there is a compactly supported distribution \(v\) with \(P(-D)v=\mu\). This \(v\) is unique, and

Applications: [Choosing polynomial and exponential approximants](../../src/choosing-polynomial-and-exponential-approximants.md).

## Local polynomial-annihilator quotient equivalence

Contract identifier: `local-polynomial-annihilator`. Proof status: planned.

For compact \(\mu\), set
\[
F(\zeta)=\widehat\mu(\zeta)
=\mu\bigl(e^{-ix\cdot\zeta}\bigr).
\tag{4}
\]
This is entire. The transpose of \(P(D)\) is \(P(-D)\), so the divisor relevant to (4) is \(P(-\zeta)\).

Applications: [Choosing polynomial and exponential approximants](../../src/choosing-polynomial-and-exponential-approximants.md).

- \(\mu\) annihilates every polynomial solution of \(P(D)h=0\) if and only if \(F(\zeta)/P(-\zeta)\) is holomorphic in a neighborhood of \(0\).

Applications: [Choosing polynomial and exponential approximants](../../src/choosing-polynomial-and-exponential-approximants.md).

## Compact singular-support convex-hull equality

Proof reference: [Locating singularities through logarithmic Fourier strips](../../AN02-L158.html#5-a-nonzero-polynomial-cannot-change-the-compact-singular-hull), Theorem 5.1.

Throughout, \(P\) is a nonzero constant-coefficient complex polynomial, \(D=-i\partial\), and \(P^t=P(-D)\) is the complex-linear transpose. Singular support is denoted by \(\operatorname{singsupp}\): its complement is the largest open set on which a distribution is smooth. Differential operators do not increase singular support.

Applications: [Singular supports and arbitrary distribution data](../../src/singular-supports-and-distribution-data.md).

We use the following compact Fourier prerequisite, for \(v\in\mathcal E'(\mathbb R^n)\):
\[
\operatorname{ch}\operatorname{singsupp}P^tv
=\operatorname{ch}\operatorname{singsupp}v,
\tag{2}
\]
The convex hull of the empty set is empty. This is the singular-support version of the compact support theorem. The full compact polynomial singular-support hull identity is proved in [Locating singularities through logarithmic Fourier strips](../../AN02-L158.html#5-a-nonzero-polynomial-cannot-change-the-compact-singular-hull), Theorem 5.1, including the empty singular-support case. It applies to the transpose because its symbol is the original polynomial evaluated at the negative Fourier variable, which is also nonzero. It is separate from the already proved ordinary support-hull theorem. In particular, a compact distribution whose image is smooth is itself smooth. Formula (2) places every singularity of \(v\) in the convex hull of the singularities of \(P^tv\). For an open convex \(X\), that hull lies in \(X\) and proves (1).

Applications: [Singular supports and arbitrary distribution data](../../src/singular-supports-and-distribution-data.md).

## Exact characteristic halfspace smooth homogeneous solution

Contract identifier: `characteristic-halfspace-homogeneous-solution`.

The complete proof is [Smooth solutions with an exact characteristic halfspace as support](../../AN02-L111.html#exact-characteristic-halfspace-theorem), Theorem 1, Lemma 2, CH1–CH31 and Appendix A. It treats every nonzero complex constant-coefficient polynomial \(P\), all its lower order terms, and every nonzero real \(N\) with \(P_m(N)=0\). It constructs a nonzero global smooth solution of the full equation with exact support \(x\cdot N\le0\), proves every boundary jet vanishes, and imposes no growth restriction at infinity. Replacing \(N\) by \(-N\) gives the positive halfspace for the same operator. Thus the uses below apply to \(A=P^t\) without requiring real lower order coefficients. The lesson supplies its root and complex-analysis tools directly and links the precise scalar integral providers LP2 and LP4; its ordinary entry toolkit remains explicit. This written contract does not certify recursive prerequisite closure or the other general proofs on this page.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

- **Halfspace solution.** If the principal part of \(A\) vanishes at a real nonzero normal \(N\), each closed halfspace with that normal is the exact support of a global smooth solution of \(Au=0\).

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

- **Characteristic halfspaces.** If \(P_m(N)=0\), a nonzero global smooth homogeneous solution has exact support \(\{x: N\cdot x\geq0\}\). This is the halfspace-solution entry in the second lesson above.

Applications: [Causal solvability forces hyperbolicity](../../src/causal-solvability-forces-hyperbolicity.md).

## Analytic elliptic regularity and differential wavefront ellipticity

Contract identifier: `analytic-elliptic-wavefront-regularity`. Proof status: available. Full proof: [Theorem 1.1 and Corollaries 7.1–7.2](../../AN02-L199.html#complete-proof). Smooth coefficients give ordinary microlocal ellipticity; analytic coefficients give every admissible derivative class,including the analytic class. Arbitrary finite scalar order,complex coefficients and the elliptic analytic-regularity consequence are included.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

- **Analytic elliptic regularity.** A homogeneous distributional solution of a constant-coefficient elliptic operator is real analytic. In particular it vanishes throughout a connected open set if it vanishes on a nonempty open subset.

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

Both wavefront sets are closed conic subsets of the cotangent bundle with the zero covectors removed. Their projections are respectively the smooth and analytic singular supports; the latter lies in the support. Differential operators do not increase either wavefront set. Elliptic regularity at a covector means
\[
\begin{gathered}
\operatorname{WF}(u)\subset
\operatorname{Char}A\cup\operatorname{WF}(Au),\\
\operatorname{WF}_A(u)\subset
\operatorname{Char}A\cup\operatorname{WF}_A(Au).
\end{gathered}
\tag{6}
\]

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

## Real principal type smooth propagation and exact realization

Contract identifier: `real-principal-type-smooth-propagation-and-realization`. Proof status: available. Full proof: [Theorem 1.1,assertions 2 and 3](../../AN02-L200.html#complete-proof). Includes arbitrary complex lower-order terms and global exact one-ray realization at every prescribed finite differentiability.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

- **Smooth wavefront propagation and realization.** Suppose \(A_m\) is real and \(\nabla A_m(\xi)\ne0\) for every nonzero characteristic \(\xi\). If \((x,\xi)\in\operatorname{WF}(u)\setminus\operatorname{WF}(Au)\), then \(A_m(\xi)=0\), and the wavefront point propagates along any segment in direction \(\nabla A_m(\xi)\) avoiding \(\operatorname{WF}(Au)\) at the same covector. Conversely, for each such \(\xi\) there is a global \(u\in C^m\) for which \(Au\) is smooth and
  \[
  \begin{gathered}
  \operatorname{WF}(u)=\{(t\nabla A_m(\xi),s\xi):\\
  t\in\mathbb R,\ s>0\}.
  \end{gathered}
  \tag{5}
  \]

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

## Real principal type analytic wavefront propagation

Contract identifier: `real-principal-type-analytic-propagation`. Proof status: available. Full proof: [Theorem 6.1 and Corollary 6.2](../../AN02-L201.html#complete-proof). Includes every admissible derivative class,its analytic specialization,all positive scalar orders and arbitrary complex lower coefficients. The tempered spherical representation,conic localization and full cutoff argument are proved there.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

- **Smooth wavefront propagation and realization.** Suppose \(A_m\) is real and \(\nabla A_m(\xi)\ne0\) for every nonzero characteristic \(\xi\). If \((x,\xi)\in\operatorname{WF}(u)\setminus\operatorname{WF}(Au)\), then \(A_m(\xi)=0\), and the wavefront point propagates along any segment in direction \(\nabla A_m(\xi)\) avoiding \(\operatorname{WF}(Au)\) at the same covector. Conversely, for each such \(\xi\) there is a global \(u\in C^m\) for which \(Au\) is smooth and

  \[
   \operatorname{WF}(u)=\{(t\nabla A_m(\xi),s\xi):t\in\mathbb R,\ s>0\}.
  \]

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

- **Analytic wavefront propagation.** Under the same principal type hypothesis, the preceding propagation statement holds with \(\operatorname{WF}_A\) in place of \(\operatorname{WF}\).

Applications: [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md).

## Both signed support normals lie in analytic wavefront set

The full proof is [Support normals and analytic singularities](../../AN02-L194.html#3-a-supporting-analytic-function-produces-a-singular-normal), Theorem 3.1 and Corollary 4.1.

- **A support normal is an analytic singularity.** If a real analytic function \(h\) attains its maximum on \(\operatorname{supp}u\) at \(x\), with \(dh(x)\ne0\), then \((x,\pm dh(x))\in\operatorname{WF}_A(u)\).

* The **analytic support normal** theorem: a real analytic function with nonzero gradient having a maximum on a distribution's support forces both signed gradient covectors into its analytic wavefront set.

The local theorem also permits C1 supporting functions. Both normal signs, complex distributions, nearest support points and closed normal-set limits are included.

## Distributional continuation on a proper convex cone

Contract identifier: `convex-conic-unique-continuation`. Proof status: available. Full proof: [Corollary 0.4 and its proper-cone consequence](../../AN02-L016.html#two-consequences-with-different-geometric-hypotheses).

We use \(D=-i\partial\), the complex-linear transpose \(P^t=P(-D)\), and the Euclidean boundary distance \(d_X\) from [Boundary distance and propagation](../../src/boundary-distance-and-propagation.md). The nonzero complex polynomial \(P\) has constant coefficients. No condition of reality is placed on its lower order coefficients.

Applications: [Planar domains and directional solvability](../../src/planar-domains-and-directional-solvability.md).

We need one exact continuation input for general constant-coefficient operators:

**Conic continuation input.** Let \(\Gamma\) be an open proper convex cone with vertex \(q\). Suppose no characteristic hyperplane through \(q\) meets \(\overline\Gamma\) only at \(q\). If \(P^tu=0\) on \(\Gamma\) and \(u\) vanishes there outside a bounded set, then \(u=0\) on \(\Gamma\).

The complete proper-cone argument follows from the convex continuation theorem and its ray criterion. Properness here means that a real linear functional is strictly positive on every nonzero vector of the closed cone. In the application every characteristic line has a ray in the interior of \(\Gamma\), a stronger version of its hypothesis.

Applications: [Planar domains and directional solvability](../../src/planar-domains-and-directional-solvability.md).

## Convex open-set characteristic-hyperplane continuation

Contract identifier: `convex-open-set-characteristic-continuation`. Proof status: available. Full proof: [Theorem 0.1](../../AN02-L016.html#convex-continuation).

We use the following general analytic continuation theorem. Let \(R\ne0\) be any complex constant-coefficient polynomial on \(\mathbb R^n\), with principal homogeneous part \(R_d\). Suppose \(U\subset V\) are nonempty convex open sets and every affine hyperplane whose real normal \(N\ne0\) satisfies \(R_d(N)=0\), and which meets \(V\), also meets \(U\). If \(u\in\mathcal D'(V)\), \(R(D)u=0\) in \(V\), and \(u=0\) in \(U\), then \(u=0\) in \(V\). The complete proof is Theorem 0.1 of the Lorentz lesson, including complex lower order coefficients and every finite degree.

Applications: [Lorentz cones and domain solvability](../../src/lorentz-cones-and-domain-solvability.md).

- **Convex continuation.** If \(U\subset V\) are nonempty convex open sets, every characteristic affine hyperplane meeting \(V\) meets \(U\), and a distribution \(w\) satisfies \(P(D)w=0\) in \(V\) and \(w=0\) in \(U\), then \(w=0\) in \(V\). Characteristic normals are nonzero real \(M\) with \(P_m(M)=0\). This is the general theorem declared in the convex-continuation section of the first lesson above; arbitrary complex lower order coefficients are allowed.

Applications: [Causal solvability forces hyperbolicity](../../src/causal-solvability-forces-hyperbolicity.md).

## Smooth compact holomorphic polynomial averaging

Contract identifier: `holomorphic-polynomial-averaging`. Written proof: [L120, PA1–PA16](../../AN02-L120.html#pa036-1-the-precise-statement), for fixed finite-degree smooth polynomial-dependent entire-function averaging. The common compact punctured support for positive dimension, uniform denominator, coefficient differentials and separate zero-dimensional unit-mass case retain their stated scope. The scalar prerequisites remain explicit. [L004](../../AN02-L004.html#what-a-regular-inverse-controls) receives this proof in its regular-kernel construction.

Here is the precise prerequisite. Let \(\mathcal P_m\) be the complex vector space of polynomials of degree at most \(m\), and give it the norm
\[
|q|_J=\left(\sum_{|\alpha|\leq m}|\partial^\alpha q(0)|^2\right)^{1/2}.
\]
For every \(\rho>0\), there is a nonnegative smooth function \(\Phi(q,z)\), defined for \(q\ne0\) and \(z\in\mathbb C^n\), with these properties:

1. Its \(z\)-support is contained in a fixed compact subset of \(\{|z|<\rho\}\).
2. \(\Phi(aq,z)=\Phi(q,z)\) for every nonzero complex scalar \(a\).
3. For every entire holomorphic \(H\),
   \[
   \int_{\mathbb C^n}H(z)\Phi(q,z)\,d\lambda(z)=H(0).
   \tag{3}
   \]
4. There is a constant \(c>0\) such that
   \[
   |q(z)|\geq c|q|_J\quad\hbox{whenever }\Phi(q,z)\ne0.
   \tag{4}
   \]

Here \(\lambda\) is real \(2n\)-dimensional Lebesgue measure. The constants depend on \(m,n,\rho\). We use this holomorphic averaging lemma as a prerequisite, including its smooth dependence on the real and imaginary coefficient coordinates. The averaging construction is due to Hörmander; a reference for the existence and regularity method is [Hormander 1971]. The existence theorem it supports is the Malgrange–Ehrenpreis theorem. The argument below derives the stronger estimates from the stated averaging properties.

Applications: [Regular kernels and changes in the equation](../../src/regular-kernels-and-parameter-changes.md).

## Real-carrier analytic-functional hyperfunction realization and localization

The full localization proof is [Splitting real carriers and gluing hyperfunctions](../../AN02-L197.html#6-gluing-and-the-local-differential-equation), Theorems 3.1-6.2 and Corollary 6.3. It proves finite compact-real-carrier decomposition,completeness for decreasing real carriers,well-defined quotient restriction and gluing of every compatible family on any open cover. Harmonic Runge approximation and the required global Laplace correction are proved in its Sections 1-2.

Every compact-real-carrier analytic functional defines a hyperfunction with the same support;restriction preserves equality off a carrier;constant-coefficient derivatives and the Dirac functional have their ordinary meanings. The proof retains general analytic functionals of infinite differential order and nonconvex carriers. The local test and least-carrier foundations are [Harmonic potentials and real carriers](../../AN02-L196.html#complete-proof), Lemma 1.1 and Theorems 4.2-5.1.

The carrier estimates and cutoff identities in [Small Gevrey fundamental solutions in the principal polar cone](../../AN02-L052.html#from-the-functional-to-a-hyperfunction) therefore give its stated supported hyperfunction fundamental solution.

## Analytic convolution ellipticity with polynomially bounded conic reciprocal

The full proof is [Holomorphic reciprocals and convolution regularity](../../AN02-L195.html#4-the-reciprocal-criterion-for-a-convolution-kernel), Theorem 4.1 and Corollary 4.2.

* The exact **analytic convolution ellipticity** theorem, distinct from differential ellipticity: for a tempered convolution kernel \(\mu\) and compact distribution \(v\), analytic singular directions of \(v\) are contained in those of \(\mu*v\) or in the convolution characteristic set. A real nonzero direction is outside that characteristic set if \(\widehat\mu\) has a holomorphic reciprocal at infinity on a complex conic neighborhood of it, polynomially bounded there and having distributional product one with its Fourier transform on the real cone.

The product with the Fourier transform is interpreted distributionally. The reciprocal may vanish on a real direction. The proper-support extension permits input distributions of arbitrary growth.

## Written support theorem kept separate

The compact Fourier division and exponential-polynomial annihilator entries retain their individual proof statements. The compact polynomial singular-support hull identity is proved in [Locating singularities through logarithmic Fourier strips](../../AN02-L158.html#5-a-nonzero-polynomial-cannot-change-the-compact-singular-hull), Theorem 5.1. The ordinary differential support-hull equality is a separate assertion. The latter is proved in Convex supports and convolution cancellation, Corollary 4.3, with the derivative convention adapted explicitly in AN-02.

## Smooth wavefront convolution

This seventeenth entry is a separately stated receiving prerequisite for the AN-02 hypoellipticity lesson. Its complete local cutoff proof is written in [L130, WFC0–WFC4](../../AN02-L130.html#complete-original-proof), under the stated compact-distribution, Fourier and test-family hypotheses. It is distinct from the sixteen mapped AN-01 source contracts above; strong-distribution topology and differential wavefront decrease remain separate hypotheses.

If \(E\in\mathcal D'(\mathbb R^n)\) is smooth on \(\mathbb R^n\setminus\{0\}\) and \(f\in\mathcal E'(\mathbb R^n)\), the convolution exists and
\[
WF(E*f)\subset WF(f). \] The complete [L130 proof](../../AN02-L130.html#complete-original-proof) supplies this exact specialization without a temperateness assumption on the kernel. The WFC4 calculation covers L021 equation (1), the compact inverse identity and the separated-support commutator/test-family step; strong-distribution topology and all other containing-lesson assertions remain separate.
