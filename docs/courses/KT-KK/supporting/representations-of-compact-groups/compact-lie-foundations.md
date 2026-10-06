# Exponential coordinates and closed subgroups

*Written and self-checked by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Independently expressed receiving proof companion; no independent review or formal verification is claimed. Original expression: public domain (CC0). The complete real field, finite-dimensional linear algebra and the definition of a smooth manifold are the entry conventions.*

This companion closes the Lie background used in RT-CPT-02, Lemma 5.1, Theorem 5.2, Corollary 5.4 and Exercise 4. A Lie group below is a finite-dimensional real smooth Hausdorff group with smooth multiplication and inversion; it need not be connected or compact. Under the usual second-countable manifold convention, its closed subgroups also have that convention. The proofs use the freely readable primary notes listed at the end. The exponential proof includes the differential-equation and inverse-function arguments. The full closed-subgroup proof goes beyond the stabilizer case proved in Etingof's §7.4. No classification, integration of an abstract Lie algebra, Frobenius theorem or Baker–Campbell–Hausdorff expansion is required.

<a id="cpt-l-001"></a>
## CPT-L-001 — Contractions and local inverse coordinates

The finite-calculus facts used below follow as follows. A continuous function on a compact real interval has a Riemann integral: uniform continuity makes the difference of upper and lower step sums tend to zero, and real completeness gives their common limit. Coordinatewise integration gives vector integrals and their norm bound. The quotient \(\int_t^{t+h}a(s)\,ds/h\) tends to \(a(t)\) for continuous \(a\), since its difference from \(a(t)\) is bounded by the oscillation on that interval. Conversely, for continuously differentiable \(b\), subtracting the integral of \(b'\) gives a function with derivative zero. The real mean-value theorem makes each coordinate constant. That theorem follows from Rolle's theorem by subtracting the secant line; Rolle's theorem follows by taking a maximum or minimum on the closed interval and observing that a derivative at an interior extremum is zero. Consequently, on a convex domain,
\[
f(x+h)-f(x)=\int_0^1Df(x+th)h\,dt.
\tag{L1.1}
\]
A bound on \(Df\) is therefore a Lipschitz bound. Iterating (L1.1) gives Taylor formulas with integral remainders; continuity of the highest derivative on a compact set makes their remainder estimates uniform on that set. This is the uniform Taylor fact used in CPT-L-002.

Closed bounded sets in finite-dimensional real space are compact. Nested interval bisection gives a convergent subsequence in one bounded coordinate; successively selecting subsequences for the finitely many coordinates gives the assertion for bounded sequences. For the open-cover formulation, enclose the set in a cube and repeatedly subdivide it into finitely many closed subcubes. If there is no finite subcover, choose at each stage a subcube whose intersection with the set has no finite subcover. The cubes are nested, their diameters tend to zero, and real completeness gives their unique common point. Picking a point of the closed set in each cube shows that the common point is in that set. An open member containing it contains the sufficiently small chosen cube, a contradiction. Uniform continuity on a compact set follows by the convergent-subsequence contradiction. A uniform Cauchy sequence of continuous finite-dimensional-valued functions has a pointwise limit by completeness, converges uniformly, and has continuous limit. Thus its uniform function space is complete. The chain and product rules used below follow by substituting the linear approximations in the definition of the derivative; their remainders are of smaller order than the increment.

If \(T\) is a map of a complete metric space to itself with Lipschitz constant \(q<1\), its iterates satisfy
\[
d(T^{n+1}x,T^nx)\leq q^n d(Tx,x).
\]
The geometric-series bound makes them Cauchy. Their limit is a fixed point by continuity. Two fixed points have distance at most \(q\) times that same distance and hence agree.

Let \(f\) be smooth between open subsets of \(\mathbb R^d\), with \(Df(a)\) invertible. Translating and composing with this inverse linear map reduces to \(a=0\), \(f(0)=0\), \(Df(0)=I\). On a closed ball \(B_r\) in the domain, choose \(q<1\) with \(\|I-Df(x)\|\leq q\). For sufficiently small \(y\),
\[
T_y(x)=x-f(x)+y
\]
is a \(q\)-contraction and maps \(B_r\) into itself, by \(\|T_y(x)\|\leq q\|x\|+\|y\|\). Its unique fixed point \(g(y)\) satisfies \(f(g(y))=y\) and lies in the interior if \(\|y\|<(1-q)r\). Equation (L1.1) gives
\[
\|f(x)-f(x')\|\geq(1-q)\|x-x'\|,
\qquad
\|g(y)-g(y')\|\leq(1-q)^{-1}\|y-y'\|.
\]
Thus \(f\) is injective on that ball. Restricting to the preimage in its interior of a smaller open \(y\)-ball gives inverse homeomorphisms between open neighborhoods. Put \(x=g(y)\), \(\Delta=g(y+h)-g(y)\). Differentiability of \(f\) gives
\[
h=Df(x)\Delta+o(\|\Delta\|).
\]
The Lipschitz bound gives \(\Delta=Df(x)^{-1}h+o(\|h\|)\). Hence \(Dg(y)=Df(g(y))^{-1}\). Matrix inversion is smooth by the adjugate/determinant formula. This identity first makes \(g\) continuously differentiable and then, inductively, smooth. Manifold charts give the local inverse theorem for smooth manifolds of equal dimension. In dimension zero the local charts have one point.

<a id="cpt-l-002"></a>
## CPT-L-002 — Local differential equations with smooth parameters

For smooth \(F(x,p)\) on an open subset of \(\mathbb R^d\times\mathbb R^k\), the equation
\[
u'(t)=F(u(t),p),\qquad u(0)=a
\tag{L2.1}
\]
has, near every \((a,p)\), a unique local solution smooth jointly in \(t,a,p\). A parameter may have zero dimension.

Choose closed balls about \(x_0,p_0\) contained in the domain, of radii \(r,s\), and bounds \(M\) on \(F\) and \(L\) on \(D_xF\) there. Take \(\|a-x_0\|<r/4\), \(\|p-p_0\|<s/2\), \(\tau M<r/4\), and \(q=\tau L<1/2\). On continuous curves \([-\tau,\tau]\to B_r(x_0)\), a closed subset of the complete uniform function space, the map
\[
\Phi_{a,p}(u)(t)=a+\int_0^tF(u(v),p)\,dv
\tag{L2.2}
\]
takes values in \(B_{r/2}(x_0)\) and is a \(q\)-contraction. CPT-L-001 gives its unique fixed point. The fundamental theorem makes it a solution. Conversely every solution remaining in this ball satisfies (L2.2). Local uniqueness applies at every initial value. On a common connected time interval two solutions with the same initial value agree everywhere: their times of agreement are closed by continuity and open by local uniqueness. A real interval is connected by the least-upper-bound property.

Here is the parameter differentiability argument. Write \(z=(a,p)\), \(u_z=u\). Bounds for \(D_pF\) and the contraction estimate give
\(\|u_{z+h}-u_z\|_\infty\leq C\|h\|/(1-q)\) locally. Define
\[
(A_z w)(t)=\int_0^tD_xF(u_z(v),p)w(v)\,dv,
\quad
(B_z h)(t)=h_a+\int_0^tD_pF(u_z(v),p)h_p\,dv.
\]
Since \(\|A_z\|\leq q\), the norm-convergent series
\((1-A_z)^{-1}=\sum_{n\geq0}A_z^n\) has norm at most \((1-q)^{-1}\). Operator norm completeness here follows directly from completeness of the uniform function space: the pointwise limit of an operator norm Cauchy sequence is bounded linear, and its convergence is in operator norm. Uniform Taylor remainders for \(F\) on the compact balls, the Lipschitz estimate and (L2.2) give
\[
u_{z+h}-u_z=A_z(u_{z+h}-u_z)+B_z h+o(\|h\|)
\]
in the uniform norm. Therefore \(Du_z=(1-A_z)^{-1}B_z\). It is continuous, since \(u_z\), the derivatives of \(F\), and the uniformly convergent inverse series are continuous in \(z\).

All higher parameter derivatives follow from the same argument. On curves taking values strictly inside the ball, the map
\((u,p)\mapsto[t\mapsto F(u(t),p)]\) is smooth in the uniform norm: its \(j\)th derivative is the pointwise \(j\)th derivative of \(F\), and the uniform Taylor remainder on a slightly smaller compact ball proves this at each finite order. Integration is bounded linear, so (L2.2) has the same property. If \(u_z\) is \(C^j\), then \(A_z,B_z\) are \(C^j\). The identity
\[
(1-A_{z+h})^{-1}-(1-A_z)^{-1}
=(1-A_{z+h})^{-1}(A_{z+h}-A_z)(1-A_z)^{-1}
\]
proves differentiability of the inverse, and inductively all its derivatives, by the product rule. The formula for \(Du_z\) consequently makes \(u_z\) \(C^{j+1}\). Starting with \(j=0\) proves all orders. The equation
\(\partial_tu_z(t)=F(u_z(t),p)\), together with its parameter derivatives, proves all mixed derivatives and joint smoothness. Applied in charts, this proves local existence, uniqueness and smooth dependence for smooth manifold vector fields and their finite-dimensional smooth parameter families.

<a id="cpt-l-003"></a>
## CPT-L-003 — The Lie exponential and its local chart

Let \(G\) be a Lie group, \(e\) its identity and \(\mathfrak g=T_eG\). The field \(X^L(g)=d(L_g)_eX\) is smooth and left invariant: differentiate smooth multiplication in its second variable and use \(L_gL_h=L_{gh}\). CPT-L-002 gives its local curve \(\beta_X\) through \(e\). Left translations carry solutions to solutions, so uniqueness gives
\[
\beta_X(s+t)=\beta_X(s)\beta_X(t)
\tag{L3.1}
\]
when the three times lie in a sufficiently small common interval. Indeed, as functions of \(t\), both sides solve the same equation through \(\beta_X(s)\) at zero and agree on the connected overlapping interval.

This curve extends to all times. Choose \(\delta>0\) such that it is defined on \((-2\delta,2\delta)\). For \(n\in\mathbb Z\), \(0\leq r<\delta\), set
\[
\gamma_X(n\delta+r)=\beta_X(\delta)^n\beta_X(r).
\]
At each endpoint the two formulas agree smoothly: (L3.1) identifies them near the endpoint with one translated local curve. Each piece is a solution, giving a global smooth solution. Uniqueness gives
\(\gamma_X(s+t)=\gamma_X(s)\gamma_X(t)\) for all \(s,t\), by comparing the two solutions in \(t\) through \(\gamma_X(s)\). Any smooth one-parameter subgroup with initial velocity \(X\) solves the same equation by differentiating its group law, and hence is \(\gamma_X\). Rescaling time gives \(\gamma_{aX}(t)=\gamma_X(at)\) for every real \(a\), including zero and negative \(a\).

Define \(\exp_GX=\gamma_X(1)\). CPT-L-002 provides one local smooth-dependence interval uniformly for \(X\) near any \(X_0\). Choose a positive integer \(N\) with \(1/N\) in that interval. Then
\[
\exp_GX=\beta_X(1/N)^N
\]
near \(X_0\), proving smoothness everywhere. Rescaling yields
\[
\exp_G(0)=e,\qquad d(\exp_G)_0=I,\qquad
\exp_G(sX)\exp_G(tX)=\exp_G((s+t)X).
\tag{L3.2}
\]
The differential is computed along the straight lines \(tX\), since \(\exp_G(tX)=\gamma_X(t)\). CPT-L-001 makes \(\exp_G\) a diffeomorphism from a neighborhood of zero to an identity neighborhood. Let \(\log_G\) be its local inverse. Formula (L3.2) gives \((\exp_GX)^n=\exp_G(nX)\) for every integer \(n\); \(nX\) need not lie in the inverse-chart domain.

The derivative of multiplication at \((e,e)\) is \((X,Y)\mapsto X+Y\), since its restrictions to the coordinate axes are the identity and its differential is linear. Thus for fixed \(X,Y\),
\[
\log_G(\exp_G(sX)\exp_G(sY))
=s(X+Y)+o(s)\qquad(s\to0).
\tag{L3.3}
\]
For any linear direct sum \(\mathfrak g=V\oplus W\), the map
\((X,Y)\mapsto\exp_GX\exp_GY\), \(X\in V,Y\in W\), has invertible differential \(X+Y\) at zero. CPT-L-001 gives a local product chart. These facts include dimension zero, when the identity is an open point.

<a id="cpt-l-004"></a>
## CPT-L-004 — Every closed subgroup is an embedded Lie subgroup

**Theorem.** A closed subgroup \(H\) of any finite-dimensional real Lie group \(G\), with its subspace topology, is an embedded smooth submanifold and a Lie group. Its tangent space at the identity is
\[
\mathfrak h=\{X\in\mathfrak g:\exp_G(tX)\in H
                 \text{ for every }t\in\mathbb R\}.
\tag{L4.1}
\]
No connectedness or compactness is assumed.

**Proof.** The set in (L4.1) is closed, contains zero, and is closed under real scalar multiplication. To prove addition, take \(X,Y\in\mathfrak h\), fix any real \(t\), and, for sufficiently large positive integers \(n\), put
\[
b_n=\log_G(\exp_G((t/n)X)\exp_G((t/n)Y)).
\]
Equation (L3.3) gives \(nb_n\to t(X+Y)\). The subgroup property and (L3.2) give
\[
\exp_G(nb_n)=
 \bigl(\exp_G((t/n)X)\exp_G((t/n)Y)\bigr)^n\in H.
\]
Continuity and closedness imply \(\exp_G(t(X+Y))\in H\). Since \(t\) was arbitrary, \(X+Y\in\mathfrak h\), so it is a linear subspace.

Choose a linear complement \(W\). There is \(\varepsilon>0\) such that
\[
Y\in W,\quad \|Y\|<\varepsilon,\quad \exp_GY\in H
\quad\Longrightarrow\quad Y=0.
\tag{L4.2}
\]
Otherwise choose nonzero \(Y_j\in W\) tending to zero with \(\exp_GY_j\in H\). Compactness of the finite-dimensional unit sphere gives a subsequence with \(Y_j/\|Y_j\|\to Z\in W\), \(\|Z\|=1\). For each real \(t\) choose an integer \(m_j\), possibly negative, with
\(|m_j\|Y_j\|-t|\leq\|Y_j\|\). Then \(m_jY_j\to tZ\) and
\[
\exp_G(m_jY_j)=(\exp_GY_j)^{m_j}\in H.
\]
Closedness gives \(\exp_G(tZ)\in H\) for every \(t\); thus \(Z\in\mathfrak h\cap W=0\), a contradiction. If \(W=0\), (L4.2) is immediate.

The product chart of CPT-L-003 for \(\mathfrak g=\mathfrak h\oplus W\) restricts to a product of open balls \(B\times C\), with \(C\subset\{\|Y\|<\varepsilon\}\). Its image \(\Omega\) is an open identity neighborhood and it is a diffeomorphism there. An element \(\exp_GX\exp_GY\) in that image lies in \(H\) exactly when \(Y=0\): if it lies in \(H\), then \(\exp_GX\in H\) makes \(\exp_GY\in H\), and (L4.2) applies; the converse is (L4.1). Thus this ambient chart cuts out \(H\cap\Omega\) as \(B\times\{0\}\). Its derivative identifies \(T_eH=\mathfrak h\).

Translate the charts by elements of \(H\). Their restrictions have smooth transition functions, being restrictions of ambient smooth coordinate changes. Their topology is the subspace topology. Hence \(H\) is an embedded submanifold. Multiplication and inversion restrict smoothly: in an ambient chart cutting out \(H\), a smooth map valued in \(H\) has zero discarded coordinates and smooth retained coordinates. Apply this to the two group operations. The subgroup is Hausdorff and inherits second countability if that convention is made for \(G\). This proves the theorem.

For the Lie-algebra interpretation, \(X^L\), \(X\in\mathfrak h\), is tangent along \(H\), since its flow through \(h\) is \(h\exp_G(tX)\in H\). Brackets of tangent smooth fields are tangent: in coordinates cutting out \(H\), their normal coefficients and all their tangential derivatives vanish on \(H\); the coordinate bracket formula therefore has zero normal coefficients there. The bracket at the identity belongs to \(\mathfrak h\). The exponential of \(H\) agrees with the ambient one on \(\mathfrak h\), by ODE uniqueness. \(\square\)

<a id="cpt-l-005"></a>
## CPT-L-005 — Unitary targets and no small subgroups

The open matrix set \(GL_m(\mathbb R)\) is a Lie group: multiplication is polynomial and inversion is adjugate divided by determinant. Embed a complex matrix \(A=P+iQ\) as
\[
j(A)=\begin{pmatrix}P&-Q\\Q&P\end{pmatrix}.
\]
Block multiplication gives \(j(AB)=j(A)j(B)\); this linear map is a homeomorphism onto its image. Its image consists of matrices commuting with \(J=j(iI)\). The subgroup \(j(U(n))\) in \(GL_{2n}(\mathbb R)\) is cut out by the closed equations
\[
MJ=JM,\qquad M^{\mathsf T}M=I.
\]
The second equation is exactly \(A^*A=I\). CPT-L-004 gives the real Lie-group structure of \(U(n)\), without assuming it in the closed-subgroup proof. The orthogonality equation bounds every matrix entry by one and defines a closed subset of the whole real matrix space; hence \(U(n)\) is compact. Finite products have product Lie charts and smooth coordinatewise operations, or can be embedded as closed block-diagonal matrix subgroups. The empty product is the one-point group.

Every finite-dimensional real Lie group has no small subgroups. In positive dimension choose \(r>0\) such that \(\exp_G\) is injective on \(B_r\) and gives its local chart. Put \(U=\exp_G(B_{r/3})\). If a subgroup contained in \(U\) has \(h=\exp_GX\ne e\), let \(n\) be the least positive integer with \(n\|X\|\geq r/3\). Since \(0<\|X\|<r/3\), minimality gives \(n\|X\|<2r/3<r\). Its power \(h^n=\exp_G(nX)\) cannot lie in \(U\): injectivity on \(B_r\) would give \(nX\in B_{r/3}\). This is a contradiction. In dimension zero, \(\{e\}\) is open and contains no nontrivial subgroup. Disconnected and discrete groups are included.

## Free comparison sources and proof scope

- Pavel Etingof, [*18.745: Lie Groups and Lie Algebras, I*, author lecture notes](https://math.mit.edu/~etingof/lnlg.pdf), §5.3, Proposition 5.12 and Theorem 5.16, printed pp. 36–37, for the exponential and local differential. Theorem 2.16 states the general closed-subgroup theorem; §7.4 proves a stabilizer case. CPT-L-001–004 supply the complete analytic and closed-subgroup arguments here.
- Brian Conrad and Aaron Landesman, [*Math 210C: Compact Lie Groups*, author-hosted lecture notes](https://math.stanford.edu/~conrad/210CPage/handouts/lie_groups_notes.pdf), Appendices E.2, F.2–F.4 and G.1 for local ODEs, smooth dependence and the exponential. Theorem 6.15 sketches the general closed-subgroup argument; it is not a substitute for CPT-L-004.
- Alejandro Ginory, [*Closed Subgroup Theorem for Lie Groups*, author-hosted notes](https://sites.math.rutgers.edu/~ag930/Some%20Math/Closed%20Subgroup%20Theorem%20for%20Lie%20Groups.pdf), §3, Theorem 3.1, for the shrinking-power and complementary-coordinate proof. CPT-L-004 supplies the local analytic entries, uses signed integers for negative times, and proves the embedded smooth group structure.

The links identify freely readable primary notes, not an inferred licence to copy their prose. Their text is not incorporated. This independently expressed companion retains CC0. Its complete closed-subgroup proof supplies CPT-L-004 used in Lesson 18.
