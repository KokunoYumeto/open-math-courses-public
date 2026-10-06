# Planned prerequisites for AN-02

This page records precisely stated prerequisites and their individual proof statuses. Most general proofs remain planned. Other entries retain their stated statuses; recursive prerequisite closure remains incomplete.

## Local distributional Holmgren uniqueness

Contract identifier: `generic-noncharacteristic-Holmgren`. Proof status: planned.

One prerequisite remains planned in Distributions, kernels and analytic singularities: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of this Holmgren theorem are conditional on that planned proof.

Statement retained from Analytic root barriers and supported solvability, source lines 9–9.

The two prerequisites in Incoming normal roots at a flat boundary remain planned prerequisites: the homogeneous hyperbolic cone theorem and the analytic zero-strip Taylor-order theorem. One further planned theorem is used here: local Holmgren uniqueness for a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface. The two continuation arguments below are proved from precisely this local theorem. No general convex continuation theorem or arbitrary-growth Cauchy uniqueness theorem is imported.

Statement retained from Boundary determinants annihilate causal solutions, source lines 90–90.

## Homogeneous hyperbolic component cone and zero-free tube

Contract identifier: `homogeneous-hyperbolic-cone`. Proof status: planned.

- **Homogeneous cone entry.** For a positive-degree homogeneous \(F\), if \(F(N)\ne0\) and \(F(\xi+zN)\) has only real roots for every real \(\xi\), the component \(\Gamma(F,N)\) of \(N\) in \(\{F\ne0\}\subset\mathbb R^n\) is an open convex cone. Every \(\theta\in\Gamma\) is a hyperbolic direction, \(F/F(N)\) has real coefficients, and the roots of \(F(x+z\theta)\) are strictly negative exactly when \(x\in\Gamma\). Also \(F(x+iy)\ne0\) for real \(x\), \(y\in\Gamma\).

Statement retained from Hyperbolicity and lower order terms, source lines 9–9.

## One-sided analytic zero-strip total Taylor order

Contract identifier: `analytic-zero-strip-Taylor-order`. Proof status: planned.

- **Analytic order entry.** If a germ \(g(z,\lambda)\) is holomorphic at zero, \(g(z,0)\) has exact order \(d\), and every local zero with real \(\lambda\) satisfies \(\operatorname{Im}z\le C|\lambda|\), the total Taylor order of \(g\) is at least \(d\). The assertion permits complex coefficients and uses both signs of the real parameter.

Statement retained from Hyperbolicity and lower order terms, source lines 10–10.

## Compact Fourier division and exponential-polynomial annihilator equivalence

Contract identifier: `compact-support-polynomial-division`. Proof status: planned.

Fix a nonzero complex polynomial \(P\), put \(D=-i\partial\), and use complex-linear distribution pairings. The formal transpose is
\[
P^t=P(-D).
\]
For a compactly supported distribution \(v\), \(\operatorname{ch}\operatorname{supp}v\) denotes the convex hull of its support.

Statement retained from Approximation and global solvability from support geometry, source lines 9–13.

An **exponential-polynomial solution** is a function
\[
h(x)=e^{ix\cdot z}A(x),\qquad z\in\mathbb C^n,
\quad A\text{ a polynomial},\qquad P(D)h=0.
\tag{1}
\]
Equivalently, \(P(D+z)A=0\). The polynomial factor records multiplicities; the class includes more than the plane exponentials for which \(P(z)=0\).

Statement retained from Approximation and global solvability from support geometry, source lines 19–25.

- If \(\mu\) is compactly supported and annihilates every solution in (1), then there is a compactly supported \(v\) with
  \[
  P^tv=\mu.
  \tag{3}
  \]
  The solution is unique by (2). In Fourier–Laplace language, annihilation makes \(\widehat\mu(z)/P(-z)\) entire, and polynomial division preserves the growth estimate needed for compact support.

Statement retained from Approximation and global solvability from support geometry, source lines 36–41.

For compact \(\mu\), set
\[
F(\zeta)=\widehat\mu(\zeta)
=\mu\bigl(e^{-ix\cdot\zeta}\bigr).
\tag{4}
\]
This is entire. The transpose of \(P(D)\) is \(P(-D)\), so the divisor relevant to (4) is \(P(-\zeta)\).

Statement retained from Choosing polynomial and exponential approximants, source lines 47–53.

- \(\mu\) annihilates every exponential-polynomial solution \(e^{ix\cdot z}A(x)\) of the equation if and only if \(F(\zeta)/P(-\zeta)\) is entire.
- The quotient is entire if and only if there is a compactly supported distribution \(v\) with \(P(-D)v=\mu\). This \(v\) is unique, and

Statement retained from Choosing polynomial and exponential approximants, source lines 58–59.

## Local polynomial-annihilator quotient equivalence

Contract identifier: `local-polynomial-annihilator`. Proof status: planned.

For compact \(\mu\), set
\[
F(\zeta)=\widehat\mu(\zeta)
=\mu\bigl(e^{-ix\cdot\zeta}\bigr).
\tag{4}
\]
This is entire. The transpose of \(P(D)\) is \(P(-D)\), so the divisor relevant to (4) is \(P(-\zeta)\).

Statement retained from Choosing polynomial and exponential approximants, source lines 47–53.

- \(\mu\) annihilates every polynomial solution of \(P(D)h=0\) if and only if \(F(\zeta)/P(-\zeta)\) is holomorphic in a neighborhood of \(0\).

Statement retained from Choosing polynomial and exponential approximants, source lines 57–57.

## Compact singular-support convex-hull equality

Contract identifier: `convex-singular-support-hull-differential`. Proof status: planned.

Throughout, \(P\) is a nonzero constant-coefficient complex polynomial, \(D=-i\partial\), and \(P^t=P(-D)\) is the complex-linear transpose. Singular support is denoted by \(\operatorname{singsupp}\): its complement is the largest open set on which a distribution is smooth. Differential operators do not increase singular support.

Statement retained from Singular supports and arbitrary distribution data, source lines 9–9.

We use the following compact Fourier prerequisite, for \(v\in\mathcal E'(\mathbb R^n)\):
\[
\operatorname{ch}\operatorname{singsupp}P^tv
=\operatorname{ch}\operatorname{singsupp}v,
\tag{2}
\]
The convex hull of the empty set is empty. This is the singular-support version of the compact support theorem. The full compact singular-support hull statement is a planned prerequisite of Distributions, kernels and analytic singularities. It is separate from the already proved ordinary support-hull theorem. In particular, a compact distribution whose image is smooth is itself smooth. Formula (2) places every singularity of \(v\) in the convex hull of the singularities of \(P^tv\). For an open convex \(X\), that hull lies in \(X\) and proves (1).

Statement retained from Singular supports and arbitrary distribution data, source lines 26–32.

## Exact characteristic halfspace smooth homogeneous solution

Contract identifier: `characteristic-halfspace-homogeneous-solution`.

The complete proof is Smooth solutions with an exact characteristic halfspace as support, Theorem 1, Lemma 2, CH1–CH31 and Appendix A. It treats every nonzero complex constant-coefficient polynomial \(P\), all its lower order terms, and every nonzero real \(N\) with \(P_m(N)=0\). It constructs a nonzero global smooth solution of the full equation with exact support \(x\cdot N\le0\), proves every boundary jet vanishes, and imposes no growth restriction at infinity. Replacing \(N\) by \(-N\) gives the positive halfspace for the same operator. Thus the uses below apply to \(A=P^t\) without requiring real lower order coefficients. The lesson supplies its root and complex-analysis tools directly and links the precise scalar integral providers LP2 and LP4; its ordinary entry toolkit remains explicit. This written contract does not certify recursive prerequisite closure or the other general proofs on this page.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

- **Halfspace solution.** If the principal part of \(A\) vanishes at a real nonzero normal \(N\), each closed halfspace with that normal is the exact support of a global smooth solution of \(Au=0\).

Statement retained from Boundary distance and propagation, source lines 56–58.

- **Characteristic halfspaces.** If \(P_m(N)=0\), a nonzero global smooth homogeneous solution has exact support \(\{x: N\cdot x\geq0\}\). This is the halfspace-solution entry in the second lesson above.

Statement retained from Causal solvability forces hyperbolicity, source lines 10–10.

## Analytic elliptic regularity and differential wavefront ellipticity

Contract identifier: `analytic-elliptic-wavefront-regularity`. Proof status: planned.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

Statement retained from Boundary distance and propagation, source lines 56–56.

- **Analytic elliptic regularity.** A homogeneous distributional solution of a constant-coefficient elliptic operator is real analytic. In particular it vanishes throughout a connected open set if it vanishes on a nonempty open subset.

Statement retained from Boundary distance and propagation, source lines 59–59.

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

Statement retained from Boundary distance and propagation, source lines 71–80.

## Real principal type smooth propagation and exact realization

Contract identifier: `real-principal-type-smooth-propagation-and-realization`. Proof status: planned.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

Statement retained from Boundary distance and propagation, source lines 56–56.

- **Smooth wavefront propagation and realization.** Suppose \(A_m\) is real and \(\nabla A_m(\xi)\ne0\) for every nonzero characteristic \(\xi\). If \((x,\xi)\in\operatorname{WF}(u)\setminus\operatorname{WF}(Au)\), then \(A_m(\xi)=0\), and the wavefront point propagates along any segment in direction \(\nabla A_m(\xi)\) avoiding \(\operatorname{WF}(Au)\) at the same covector. Conversely, for each such \(\xi\) there is a global \(u\in C^m\) for which \(Au\) is smooth and
  \[
  \begin{gathered}
  \operatorname{WF}(u)=\{(t\nabla A_m(\xi),s\xi):\\
  t\in\mathbb R,\ s>0\}.
  \end{gathered}
  \tag{5}
  \]

Statement retained from Boundary distance and propagation, source lines 60–67.

## Real principal type analytic wavefront propagation

Contract identifier: `real-principal-type-analytic-propagation`. Proof status: planned.

We assume the following distribution and wavefront results. They concern the operator \(A\) itself, and will be used with \(A=P^t\). They do not require its lower order coefficients to be real.

Statement retained from Boundary distance and propagation, source lines 56–56.

- **Smooth wavefront propagation and realization.** Suppose \(A_m\) is real and \(\nabla A_m(\xi)\ne0\) for every nonzero characteristic \(\xi\). If \((x,\xi)\in\operatorname{WF}(u)\setminus\operatorname{WF}(Au)\), then \(A_m(\xi)=0\), and the wavefront point propagates along any segment in direction \(\nabla A_m(\xi)\) avoiding \(\operatorname{WF}(Au)\) at the same covector. Conversely, for each such \(\xi\) there is a global \(u\in C^m\) for which \(Au\) is smooth and

Statement retained from Boundary distance and propagation, source lines 60–60.

- **Analytic wavefront propagation.** Under the same principal type hypothesis, the preceding propagation statement holds with \(\operatorname{WF}_A\) in place of \(\operatorname{WF}\).

Statement retained from Boundary distance and propagation, source lines 68–68.

## Both signed support normals lie in analytic wavefront set

Contract identifier: `analytic-support-normal`. Proof status: planned.

- **A support normal is an analytic singularity.** If a real analytic function \(h\) attains its maximum on \(\operatorname{supp}u\) at \(x\), with \(dh(x)\ne0\), then \((x,\pm dh(x))\in\operatorname{WF}_A(u)\).

Statement retained from Boundary distance and propagation, source lines 69–69.

* The **analytic support normal** theorem: a real analytic function with nonzero gradient having a maximum on a distribution's support forces both signed gradient covectors into its analytic wavefront set.

Statement retained from Uniqueness from the principal boundary symbol, source lines 24–24.

## Distributional continuation on a proper convex cone

Contract identifier: `convex-conic-unique-continuation`. Proof status: planned.

We use \(D=-i\partial\), the complex-linear transpose \(P^t=P(-D)\), and the Euclidean boundary distance \(d_X\) from Boundary distance and propagation. The nonzero complex polynomial \(P\) has constant coefficients. No condition of reality is placed on its lower order coefficients.

Statement retained from Planar domains and directional solvability, source lines 9–9.

We need one exact continuation input for general constant-coefficient operators:

**Conic continuation input.** Let \(\Gamma\) be an open proper convex cone with vertex \(q\). Suppose no characteristic hyperplane through \(q\) meets \(\overline\Gamma\) only at \(q\). If \(P^tu=0\) on \(\Gamma\) and \(u\) vanishes there outside a bounded set, then \(u=0\) on \(\Gamma\).

This distributional uniqueness result follows from continuation between convex open sets; we assume it here as an analytic continuation prerequisite. In the application every characteristic line has a ray in the interior of \(\Gamma\), a stronger version of its hypothesis.

Statement retained from Planar domains and directional solvability, source lines 62–66.

## Convex open-set characteristic-hyperplane continuation

Contract identifier: `convex-open-set-characteristic-continuation`. Proof status: planned.

We use the following general analytic continuation theorem. Let \(R\ne0\) be any complex constant-coefficient polynomial on \(\mathbb R^n\), with principal homogeneous part \(R_d\). Suppose \(U\subset V\) are nonempty convex open sets and every affine hyperplane whose real normal \(N\ne0\) satisfies \(R_d(N)=0\), and which meets \(V\), also meets \(U\). If \(u\in\mathcal D'(V)\), \(R(D)u=0\) in \(V\), and \(u=0\) in \(U\), then \(u=0\) in \(V\). We take this theorem from analytic distribution theory as a prerequisite; its generality includes complex lower order coefficients and operators of arbitrary degree.

Statement retained from Lorentz cones and domain solvability, source lines 43–43.

- **Convex continuation.** If \(U\subset V\) are nonempty convex open sets, every characteristic affine hyperplane meeting \(V\) meets \(U\), and a distribution \(w\) satisfies \(P(D)w=0\) in \(V\) and \(w=0\) in \(U\), then \(w=0\) in \(V\). Characteristic normals are nonzero real \(M\) with \(P_m(M)=0\). This is the general theorem declared in the convex-continuation section of the first lesson above; arbitrary complex lower order coefficients are allowed.

Statement retained from Causal solvability forces hyperbolicity, source lines 9–9.

## Smooth compact holomorphic polynomial averaging

Contract identifier: `holomorphic-polynomial-averaging`. Proof status: planned.

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

Statement retained from Regular kernels and changes in the equation, source lines 50–69.

## Real-carrier analytic-functional hyperfunction realization and localization

Contract identifier: `real-carrier-analytic-functional-localization`. Proof status: planned.

Two further results are planned in that same prerequisite course. Every direction in the component of a homogeneous hyperbolic polynomial is a hyperbolic direction. Compact real-carrier analytic functionals define hyperfunctions with the same support bound; their restrictions preserve equality off a carrier, compatible local hyperfunctions glue, and constant-coefficient derivatives and the Dirac functional have their usual meanings. The analytic carrier estimates and their application to the equation are proved below.

Statement retained from Small Gevrey fundamental solutions in the principal polar cone, source lines 11–11.

## Analytic convolution ellipticity with polynomially bounded conic reciprocal

Contract identifier: `analytic-convolution-ellipticity`. Proof status: planned.

* The exact **analytic convolution ellipticity** theorem, distinct from differential ellipticity: for a tempered convolution kernel \(\mu\) and compact distribution \(v\), analytic singular directions of \(v\) are contained in those of \(\mu*v\) or in the convolution characteristic set. A real nonzero direction is outside that characteristic set if \(\widehat\mu\) has a holomorphic reciprocal at infinity on a complex conic neighborhood of it, polynomially bounded there and agreeing with the reciprocal on the real cone.

Analytic convolution ellipticity in this form remains a planned prerequisite in Distributions, kernels and analytic singularities. The compact-input theorem is sufficient: we prove the arbitrary-growth localization ourselves. These two theorems are used at the stated places below; neither is claimed proved here.

Statement retained from Uniqueness from the principal boundary symbol, source lines 25–27.

## Written support theorem kept separate

The planned compact Fourier division, exponential-polynomial annihilator equivalence and singular-support hull contracts above are distinct from the written differential support-hull equality. The latter is proved in Convex supports and convolution cancellation, Corollary 4.3, with the derivative convention adapted explicitly in AN-02.

## Smooth wavefront convolution

This seventeenth entry is a separately stated receiving prerequisite for the AN-02 hypoellipticity lesson. Its local cutoff proof remains planned; it is distinct from the sixteen mapped AN-01 source contracts above.

If \(E\in\mathcal D'(\mathbb R^n)\) is smooth on \(\mathbb R^n\setminus\{0\}\) and \(f\in\mathcal E'(\mathbb R^n)\), the convolution exists and
\[
WF(E*f)\subset WF(f). \] The local cutoff proof of this convolution specialization is pending.
