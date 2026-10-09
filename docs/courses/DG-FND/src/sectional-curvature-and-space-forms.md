# Sectional curvature and space forms

Sectional curvature determines the curvature tensor and controls the geometry of complete constant-curvature manifolds. This chapter develops their model spaces and quotients, the affine and Riemannian theories of flat manifolds, compact and noncompact finiteness, and the complete flat surfaces. Affine classification is distinguished throughout from isometric classification.

All manifolds are smooth, Hausdorff and second countable. A Riemannian metric is positive definite. We use the Levi-Civita connection and the convention
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
\tag{A.1}
\]
The connection, its metric symmetries and its Bianchi identities are proved in [Riemannian connections, A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) and [Geodesics, C.1–C.3](geodesics-normal-coordinates-and-curvature.md#theorem-c-1). We will use the complete ordinary differential equation and covering arguments in those lessons and in [Connections and parallel transport](connections-and-parallel-transport.md), Hopf–Rinow and [Flat connections, D.1–D.3](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1), with more specific locators at their uses.

## A. Curvature recovered from planes and traces

An algebraic curvature tensor on a real inner-product space \(V\) is a trilinear map \(R:V^3\to V\) for which
\[
A(x,y,z,w)=\langle R(x,y)z,w\rangle
\]
is skew in its first two and last two arguments, satisfies
\(A(x,y,z,w)=A(z,w,x,y)\), and has cyclic sum zero in its first three arguments. The curvature in (A.1) has these properties by [Geodesics C.1–C.3](geodesics-normal-coordinates-and-curvature.md#theorem-c-1).

**Theorem A.1 (sectional values determine the tensor).** For independent \(x,y\), the number
\[
K(\operatorname{span}\{x,y\})
=\frac{\langle R(x,y)y,x\rangle}
 {|x|^2|y|^2-\langle x,y\rangle^2}
\tag{A.2}
\]
depends only on their plane. All such numbers determine \(R\). They all equal \(c\) if and only if
\[
R(x,y)z=c\bigl(\langle y,z\rangle x-\langle x,z\rangle y\bigr).
\tag{A.3}
\]
The same uniqueness assertion holds when the diagonal values \(A(x,y,y,x)\), rather than their quotients, are specified for all pairs.

**Proof.** If \(x'=a x+b y\), \(y'=d x+e y\), skewness in both pairs gives
\[
A(x',y',y',x')=(ae-bd)^2 A(x,y,y,x).
\tag{A.4}
\]
The Gram matrix changes by multiplication on both sides by the change-of-basis matrix and its transpose, so its determinant has the same factor \((ae-bd)^2\). Alternatively direct expansion of the two-by-two determinant gives that identity. The denominator of (A.2) is positive: subtract the projection of \(y\) on \(x\), obtaining
\[
|x|^2|y|^2-\langle x,y\rangle^2
=|x|^2\left|y-\frac{\langle y,x\rangle}{|x|^2}x\right|^2>0.
\]
Thus (A.2) is well defined on the plane.

To prove uniqueness subtract two tensors with the same data. The difference, still denoted \(A\), satisfies \(A(x,y,y,x)=0\) for independent pairs; for dependent pairs the same equality follows from first-pair skewness. Fix \(y\). The bilinear form
\[
B_y(x,z)=A(x,y,y,z)
\]
is symmetric, because pair interchange and both skewness identities give
\[
A(x,y,y,z)=A(y,z,x,y)
          =-A(z,y,x,y)=A(z,y,y,x).
\]
Expanding \(B_y(x+z,x+z)=0\), and using the zero diagonal values, gives \(2B_y(x,z)=0\). Therefore \(A(x,y,y,z)=0\) for every triple. Replace the repeated \(y\) by \(y+w\). Expansion now gives
\[
A(x,y,w,z)+A(x,w,y,z)=0.
\tag{A.5}
\]
Hence \(A\) changes sign under the swaps of positions \(1,2\) and \(2,3\). Each cyclic permutation of its first three arguments is the product of two such swaps, so it preserves \(A\). The cyclic identity is consequently \(3A(x,y,w,z)=0\). Thus \(A=0\).

The expression on the right of (A.3) satisfies all four algebraic identities: its four-tensor is
\[
c\bigl(\langle y,z\rangle\langle x,w\rangle
       -\langle x,z\rangle\langle y,w\rangle\bigr);
\]
skewness and pair interchange follow by interchanging the factors, and the six terms of its cyclic sum cancel in pairs. Its diagonal value is \(c\) times the denominator of (A.2). The uniqueness just proved establishes (A.3) and its converse. □

Define the Ricci form and scalar curvature by
\[
\operatorname{Ric}(y,z)=\operatorname{tr}(x\mapsto R(x,y)z),
\qquad
\operatorname{Scal}=\operatorname{tr}_g\operatorname{Ric}.
\tag{A.6}
\]
Trace is independent of a basis: if \(C\) is a change-of-basis matrix, the coordinate identity \(\operatorname{tr}(UV)=\operatorname{tr}(VU)\) gives
\(\operatorname{tr}(C^{-1}TC)=\operatorname{tr}T\). This identity follows by writing both sides as \(\sum_{i,j}U_{ij}V_{ji}\).

**Theorem A.2 (Ricci symmetry and the contracted Bianchi identity).** The form \(\operatorname{Ric}\) is symmetric. On a Riemannian manifold it is smooth, as is \(\operatorname{Scal}\), and
\[
\sum_a(\nabla_{e_a}\operatorname{Ric})(e_a,Y)
=\tfrac12\,d\operatorname{Scal}(Y)
\tag{A.7}
\]
in any orthonormal frame. If the sectional curvature at a point is \(c\), then
\[
\operatorname{Ric}=(n-1)c\,g,\qquad
\operatorname{Scal}=n(n-1)c.
\tag{A.8}
\]

**Proof.** In an orthonormal basis write \(T_{abcd}=A(e_a,e_b,e_c,e_d)\). The cyclic identity with arguments \(e_a,e_b,e_c,e_a\) has middle term zero, so
\[
T_{abca}=-T_{caba}=T_{acba}.
\]
Summing over \(a\) proves symmetry of
\(\operatorname{Ric}_{bc}=\sum_aT_{abca}\).
The coordinate formulas for curvature and the inverse metric are smooth by [Geodesics C.1](geodesics-normal-coordinates-and-curvature.md#theorem-c-1) and [Riemannian connections F.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-1); their finite contractions prove smoothness.

For (A.7) fix a point and choose an orthonormal frame whose covariant derivative vanishes there. Such a frame exists by [Riemannian connections C.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-c-1): its radial connection matrix is zero at the centre. Write \(\nabla_i T_{abcd}\) for the full tensor derivative at this point. [Geodesics C.2](geodesics-normal-coordinates-and-curvature.md#theorem-c-2), with zero torsion, gives
\[
\nabla_kT_{ij\ell m}+
\nabla_iT_{jk\ell m}+
\nabla_jT_{ki\ell m}=0.
\]
Put \(m=k\) and sum. The last two contractions are
\(\sum_kT_{jk\ell k}=-\operatorname{Ric}_{j\ell}\) and
\(\sum_kT_{ki\ell k}=\operatorname{Ric}_{i\ell}\). Thus
\[
\sum_k\nabla_kT_{ij\ell k}
=\nabla_i\operatorname{Ric}_{j\ell}
 -\nabla_j\operatorname{Ric}_{i\ell}.
\tag{A.9}
\]
Now set \(\ell=j\) and sum over \(j\). Both skewness identities give
\(\sum_jT_{ijjk}=\operatorname{Ric}_{ik}\). As the frame derivatives vanish and \(\nabla g=0\), contraction commutes with the covariant derivative. Consequently
\[
\sum_k\nabla_k\operatorname{Ric}_{ik}
=\nabla_i\operatorname{Scal}
 -\sum_j\nabla_j\operatorname{Ric}_{ij}.
\]
Ricci symmetry makes the two sums equal. This is (A.7) at the chosen point. The expressions are tensorial and the point was arbitrary, so (A.7) holds everywhere.

Finally (A.3) gives
\[
\begin{aligned}
\sum_a\langle R(e_a,y)z,e_a\rangle
&=c\sum_a\bigl(\langle y,z\rangle
             -\langle e_a,z\rangle\langle y,e_a\rangle\bigr)\\
&=(n-1)c\langle y,z\rangle .
\end{aligned}
\]
Tracing once more gives (A.8). □

**Theorem A.3 (the dimension restriction in Schur's theorem).** Suppose \(M\) is connected and \(n\geq3\). If \(\operatorname{Ric}=\lambda g\) pointwise for a function \(\lambda\), then \(\lambda\) is constant. In particular, if at every point all tangent planes have the same sectional curvature \(c(p)\), then \(c\) is constant.

**Proof.** First \(\lambda=\operatorname{Scal}/n\), so it is smooth by A.2 without any separate regularity assumption. Metric compatibility gives
\[
(\nabla_X\operatorname{Ric})(Y,Z)=(X\lambda)g(Y,Z),
\qquad
d\operatorname{Scal}=n\,d\lambda .
\]
The contraction in (A.7) is \(d\lambda\); hence
\((n-2)d\lambda=0\). Since \(n\geq3\), \(d\lambda=0\).
In a coordinate ball with convex image, the chain rule and the fundamental theorem of calculus along line segments show that \(\lambda\) is constant. Thus each level set is open, and its complement is a union of open level sets. Connectedness makes the value global.

For the second assertion A.1 gives (A.3) at each point and A.2 gives
\(\lambda=(n-1)c\). Equivalently \(c=\operatorname{Scal}/(n(n-1))\), so \(c\) is smooth and constant. □

**Exercise A.4 (Ricci curvature in three dimensions).** Let \(R\) be an algebraic curvature tensor on a three-dimensional inner-product space, let \(r\) be its Ricci form and \(s\) its scalar curvature. For a plane with a unit normal \(\nu\), prove
\[
K(\nu^\perp)=s/2-r(\nu,\nu).
\tag{A.10}
\]
Deduce the corresponding conclusion for a connected three-dimensional manifold with \(\operatorname{Ric}=\lambda g\).

**Solution.** Choose an orthonormal basis \(e_1,e_2,e_3=\nu\). Put
\(k_{ij}=A(e_i,e_j,e_j,e_i)\). Formula (A.6), skewness, and pair interchange give
\[
\begin{aligned}
r(e_1,e_1)&=k_{12}+k_{13},\\
r(e_2,e_2)&=k_{12}+k_{23},\\
r(e_3,e_3)&=k_{13}+k_{23}.
\end{aligned}
\]
Their sum is \(s=2(k_{12}+k_{13}+k_{23})\). Subtracting the last equality gives (A.10). It applies to every plane because an orthonormal basis can be chosen with its given unit normal. Thus \(r\), which also determines \(s\), determines every sectional curvature; A.1 determines the full tensor. On the specified manifold A.3 makes \(\lambda\) constant, and \(s=3\lambda\). Equation (A.10) then makes every sectional curvature \(\lambda/2\), the same constant at every point. □

**Exercise A.5 (a complete surface with both curvature signs).** On \(\mathbb R^2\) put
\[
f(x)=2+\cos x,\qquad
g=f(x)^2(dx^2+dy^2).
\tag{A.11}
\]
Prove completeness and compute the curvature. Explain the role of \(n\geq3\) in both statements of A.3.

**Solution.** Here \(\cos x\) and \(\sin x\) are the real and imaginary parts of the circle exponential in [Connections, E.1](connections-and-parallel-transport.md#lemma-e-1). That proof supplies their period \(2\pi\), derivative identities and the values \(\cos0=1\), \(\cos\pi=-1\). Their squared sum is one, so \(1\leq f\leq3\). Each piecewise smooth path has \(g\)-length between its Euclidean length and three times that length. Taking infima, and using the straight segment for the upper bound, gives
\[
|p-q|\leq d_g(p,q)\leq3|p-q|.
\tag{A.12}
\]
A \(d_g\)-Cauchy sequence is Euclidean Cauchy, hence converges by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations); the second inequality makes its Euclidean limit a \(d_g\)-limit. The metric is complete. Hopf–Rinow B.2 also gives geodesic completeness.

Write \(u=\log f\), using the smooth logarithm proved in [Geodesics A.4](geodesics-normal-coordinates-and-curvature.md#example-a-4). The Levi-Civita formula in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) gives exactly
\[
\Gamma^x_{xx}=u',\qquad
\Gamma^x_{yy}=-u',\qquad
\Gamma^y_{xy}=\Gamma^y_{yx}=u',
\tag{A.13}
\]
with all other coefficients zero. For example the formula
\(\Gamma^k_{ij}=\frac12 g^{k\ell}
(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij})\)
has only \(x\)-derivatives here, and \(\partial_x(f^2)=2f^2u'\), giving all four entries.
[Geodesics C.1](geodesics-normal-coordinates-and-curvature.md#theorem-c-1) consequently gives
\[
R(\partial_x,\partial_y)\partial_y
=-u''\partial_x .
\]
Indeed its \(x\)-coefficient is
\(-u''+(u')(-u')-(-u')(u')=-u''\); its \(y\)-coefficient is zero since every possible term has a zero factor in (A.13). Thus
\[
K=-\frac{u''}{f^2}
  =\frac{(f')^2-ff''}{f^4}
  =\frac{1+2\cos x}{(2+\cos x)^4}.
\tag{A.14}
\]
It is positive at \(x=0\) and negative at \(x=\pi\).
At every point of a surface there is only one tangent two-plane, so the pointwise isotropy hypothesis holds automatically. Moreover (A.8) in dimension two gives \(\operatorname{Ric}=K g\). This example satisfies both pointwise hypotheses with a nonconstant coefficient. In dimension two equation (A.7) reduces to an identity and forces no derivative to vanish, exactly explaining the dimension restriction. □

## B. Geodesic variations and the radial metric

The free lecture notes of Urs Lang discuss the variation equation and constant-curvature Jacobi fields. We prove the full finite-interval realization and the radial metric, using the previously proved smooth geodesic flow and global linear transport.

**Theorem B.1 (Jacobi fields and variations on a whole compact interval).** Let \(\gamma:I\to M\) be an affine geodesic. The equation
\[
D_t^2J+R(J,\dot\gamma)\dot\gamma=0
\tag{B.1}
\]
has exactly one smooth solution on \(I\) with any specified \(J(t_0)\) and \(D_tJ(t_0)\). Its solution space has dimension \(2n\). A smooth variation through affinely parametrized geodesics has variation field satisfying (B.1). Conversely every solution on a compact subinterval is the field of a smooth geodesic variation defined on that entire subinterval. No completeness assumption is needed.

**Proof.** Parallel transport an orthonormal basis along \(\gamma\), using [Connections, C.1–C.2 and D.2](connections-and-parallel-transport.md#theorem-c-1) and metric compatibility. On each compact interval this gives a smooth parallel frame. Write \(J=\sum j_iE_i\). Equation (B.1) becomes
\[
j''+B(t)j=0,\qquad
B_{ij}(t)=\langle R(E_j,\dot\gamma)\dot\gamma,E_i\rangle .
\tag{B.2}
\]
The entries are smooth. For \(z=(j,j')\) this is a first-order linear equation
\[
z'=\begin{pmatrix}0&I\\-B(t)&0\end{pmatrix}z.
\tag{B.3}
\]
It is precisely the parallel equation for the trivial rank-\(2n\) bundle over the parameter interval with connection potential equal to the negative of this matrix times \(dt\). Such a connection is defined by [Linear connections A.1–A.2](linear-and-affine-connections.md#lemma-a-1); [Connections D.2](connections-and-parallel-transport.md#theorem-d-2) proves unique transport across every compact interval. Exhausting \(I\) by compact intervals and using uniqueness on overlaps proves existence and uniqueness on all of \(I\). The equation is linear; evaluation of \((j,j')\) at \(t_0\) is a linear bijection onto \(\mathbb R^{2n}\), proving the dimension statement.

For a smooth map \(\alpha(s,t)\) put \(T=\partial_t\alpha\), \(V=\partial_s\alpha\), considered as sections of the pullback tangent bundle. The chain rule and torsion identity in [Linear connections, B.2–B.3 and D.3](linear-and-affine-connections.md#theorem-b-2) give
\[
D_tV=D_sT,\qquad
D_tD_sT-D_sD_tT=R(T,V)T.
\tag{B.4}
\]
These identities hold even where the map has noninjective differential: they are pullback identities, not an assertion that \(T,V\) are independent vector fields on the target. If every \(t\)-curve is a geodesic, \(D_tT=0\), so (B.4) is exactly (B.1) for its variation field at \(s=0\).

For the converse shift the compact interval to \([0,b]\), and put \(p=\gamma(0)\), \(v=\dot\gamma(0)\), \(u=J(0)\), \(w=D_tJ(0)\). Choose a smooth curve \(\sigma(s)\) with \(\sigma(0)=p\), \(\sigma'(0)=u\), using a coordinate chart. Let \(P_s:T_pM\to T_{\sigma(s)}M\) be parallel transport along \(\sigma\), and set
\[
v(s)=P_s(v+s w).
\tag{B.5}
\]
This is a smooth curve in \(TM\), with \(v(0)=v\) and \(D_sv(s)|_{s=0}=w\). The derivative identity follows by writing \(v+s w\) in the parallel frame along \(\sigma\).

[Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) proves that the maximal geodesic flow has an open domain in \(\mathbb R\times TM\) and is smooth on it. That domain contains the compact set \([0,b]\times\{v\}\). Finitely many product neighbourhoods covering this set give one neighbourhood of \(v\) on which the flow is defined for every \(t\in[0,b]\): intersect their initial-vector neighbourhoods and retain their time intervals covering \([0,b]\). Shrink the \(s\)-interval so that every \(v(s)\) is in that neighbourhood. Define \(\alpha(s,t)\) to be the base point of the geodesic flow at \(v(s)\) and time \(t\). It is a smooth variation on the whole rectangle. Its field \(V_0\) has \(V_0(0)=u\), while (B.4) and (B.5) give \(D_tV_0(0)=w\). The first part makes it a Jacobi field, and uniqueness in (B.3) gives \(V_0=J\). The same argument after an affine time shift treats any compact interval. □

**Lemma B.2 (the constant-curvature scalar solutions).** For \(c\in\mathbb R\) define
\[
S_c(t)=
\begin{cases}
\sin(\sqrt c\,t)/\sqrt c,&c>0,\\
t,&c=0,\\
\sinh(\sqrt{-c}\,t)/\sqrt{-c},&c<0,
\end{cases}
\qquad C_c(t)=S_c'(t).
\tag{B.6}
\]
Then
\[
S_c'=C_c,\quad C_c'=-cS_c,\quad
S_c(0)=0,\quad C_c(0)=1,\quad C_c^2+cS_c^2=1.
\tag{B.7}
\]
The unique solution of \(y''+cy=0\), \(y(0)=a\), \(y'(0)=b\), is \(aC_c+bS_c\). Put
\[
D_c=\begin{cases}\pi/\sqrt c,&c>0,\\+\infty,&c\leq0.\end{cases}
\tag{B.8}
\]
One has \(S_c(t)>0\) for \(0<t<D_c\). When \(c>0\), the function \(C_c\) decreases strictly from \(1\) to \(-1\) on \([0,D_c]\).

**Proof.** [Connections E.1](connections-and-parallel-transport.md#lemma-e-1) constructs \(z(t)=\cos t+i\sin t\), with \(z'=iz\), unit norm, and the specified period and endpoint values. Thus \(\sin'=\cos\), \(\cos'=-\sin\), and \(\sin^2+\cos^2=1\). Its proof gives, for \(0<t<\pi\), the expression
\[
z(t)=\frac{1+iu}{1-iu},\qquad u>0.
\]
Its imaginary part is \(2u/(1+u^2)>0\). Hence \(\sin t>0\) on that interval. The endpoint values and the negative derivative of cosine prove its stated strict decrease. For \(c<0\), the exponential construction and hyperbolic identities of [Riemannian connections, D.1](riemannian-connections-and-convex-neighbourhoods.md#lemma-d-1) give the corresponding derivatives, \(\cosh^2-\sinh^2=1\), and \(\sinh t>0\) for \(t>0\). Substitution proves (B.7) and all positivity statements, including the immediate case \(c=0\). The proposed solution has the prescribed initial data and satisfies the equation by differentiation; uniqueness is the linear initial-value uniqueness proved in B.1. □

**Theorem B.3 (the polar metric, including singular radii).** Suppose \(M\) has dimension \(n\geq1\) and constant sectional curvature \(c\). In dimension one the sectional-curvature condition is empty, and the assertion holds for every \(c\). Let \(p\in M\), let \(v\in T_pM\) be unit, and write \(\gamma_v(t)=\exp_p(tv)\), wherever defined. If \(\xi\perp v\), the derivative obtained by varying \(v\) through unit vectors with derivative \(\xi\) is
\[
J_\xi(t)=S_c(t)P_t\xi,
\tag{B.9}
\]
where \(P_t\) denotes parallel transport along \(\gamma_v\). For the polar exponential map \(E(t,v)=\exp_p(tv)\), at every point of its domain,
\[
E^*g=dt^2+S_c(t)^2g_{S(T_pM)}.
\tag{B.10}
\]
This is an equality of quadratic forms even when \(dE\) is singular. For \(t>0\) the differential is invertible whenever \(S_c(t)\ne0\). This condition is also necessary when \(n\geq2\); in dimension one the differential is always invertible.

**Proof.** A direction variation can be chosen as
\[
v(s)=\frac{v+s\xi}{|v+s\xi|};
\]
orthogonality gives \(v'(0)=\xi\). Smooth flow provides the variation near each finite time in its open domain, by [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1). B.1 says its field solves the Jacobi equation with \(J(0)=0\), \(D_tJ(0)=\xi\). Metric compatibility and the geodesic equation show that \(\dot\gamma_v=P_tv\) has unit length and is perpendicular to \(P_t\xi\). From A.1,
\[
R(P_t\xi,\dot\gamma_v)\dot\gamma_v=cP_t\xi.
\]
Equation (B.7) therefore makes (B.9) a solution with exactly those initial data; B.1 proves equality with the variation field.

The radial derivative is \(dE(\partial_t)=P_tv\). For two angular vectors \(\xi,\eta\), parallel transport is an isometry and preserves their orthogonality to \(v\). Thus
\[
\begin{aligned}
g(dE(\partial_t),dE(\partial_t))&=1,\\
g(dE(\partial_t),dE(\xi))&=0,\\
g(dE(\xi),dE(\eta))&=S_c(t)^2\langle\xi,\eta\rangle .
\end{aligned}
\]
These are exactly (B.10); no step assumes injectivity of \(dE\). When \(t>0\), its domain and target tangent spaces both have dimension \(n\). If \(S_c(t)\ne0\), the displayed form is positive definite, so the differential has zero kernel and is invertible. If \(S_c(t)=0\) and \(n\geq2\), (B.9) kills every angular vector, and a nonzero one exists. In dimension one every \(\xi\perp v\) is zero and the angular tangent space is zero, so (B.9) is the zero identity and (B.10) consists solely of the unit radial derivative. That derivative is invertible. The inverse function theorem, [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), gives a local diffeomorphism at every invertible differential. □

## C. The complete models

For \(a>0\) write
\[
\begin{aligned}
S_a^n&=\{p\in\mathbb R^{n+1}:|p|^2=a^2\},\\
H_a^n&=\{(x,s)\in\mathbb R^n\times\mathbb R:
                  |x|^2-s^2=-a^2,\ s>0\}.
\end{aligned}
\tag{C.1}
\]
The sphere has the induced Euclidean metric. The hyperboloid has the metric induced by
\[
\eta((x,s),(y,t))=x\cdot y-st.
\tag{C.2}
\]
Euclidean \(\mathbb R^n\) with its constant inner product is the third model. The quadric descriptions in Ballmann's free notes motivate the following direct calculation; no general submanifold curvature theorem is needed.

**Theorem C.1 (the quadric connection and its curvature).** The metrics just defined are smooth and positive definite. The sphere has constant sectional curvature \(a^{-2}\), and the hyperboloid has constant sectional curvature \(-a^{-2}\). On either quadric write \(\epsilon=1\) or \(-1\), respectively, and \(c=\epsilon/a^2\). If \(D\) denotes ordinary differentiation in the ambient vector space, then
\[
\nabla_XY=D_XY+c\,g(X,Y)p
\tag{C.3}
\]
at the position vector \(p\). Euclidean space has its ordinary derivative as Levi-Civita connection and has curvature zero.

**Proof.** The differential of the quadric equation at \(p\) sends \(v\) to \(2\eta(p,v)\), with the Euclidean form used for the sphere. It is nonzero since \(\eta(p,p)=\epsilon a^2\ne0\). [Local tools 1.3](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives a smooth hypersurface with tangent space \(p^\perp\). On the sphere the restricted form is positive definite. On the upper hyperboloid the map
\[
x\longmapsto\bigl(x,\sqrt{a^2+|x|^2}\bigr)
\tag{C.4}
\]
is a smooth global parametrization with inverse the spatial projection. Its metric on a vector \(v\) is
\[
|v|^2-\frac{(x\cdot v)^2}{a^2+|x|^2}
\ \geq\ \frac{a^2}{a^2+|x|^2}|v|^2.
\tag{C.5}
\]
The inequality follows by decomposing \(v\) along \(x\) and perpendicular to it, or directly by the projection calculation in A.1. Thus the metric is positive definite and smooth. Formula (C.4) also proves connectedness of the hyperboloid.

Differentiate \(\eta(Y,p)=0\) along a tangent field \(X\). Since \(D_Xp=X\), this gives \(\eta(D_XY,p)=-g(X,Y)\). As \(c\eta(p,p)=1\), the vector in (C.3) is tangent. The formula has the connection product rules. Its metric derivative is that of the ambient constant form, because the added multiples of \(p\) are orthogonal to tangent vectors. Its torsion is zero: the ambient derivative has \(D_XY-D_YX=[X,Y]\), as follows by applying both sides in ambient coordinates, and the added terms cancel by symmetry of \(g\). The uniqueness theorem in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) proves (C.3).

For tangent fields use
\[
D_XY=\nabla_XY-cg(X,Y)p .
\]
The tangential part of \(D_XD_YZ\) is
\(\nabla_X\nabla_YZ-cg(Y,Z)X\); the derivative of the scalar coefficient contributes only a normal term. Interchange \(X,Y\) and subtract the tangential part of \(D_{[X,Y]}Z\). The ambient curvature is zero, because its coordinate derivatives commute. Therefore
\[
0=R(X,Y)Z-cg(Y,Z)X+cg(X,Z)Y.
\]
This is (A.3), giving the asserted sectional curvatures by A.1. For the Euclidean metric the ordinary derivative is itself metric and torsion free, so the same uniqueness theorem identifies it, and commuting coordinate derivatives give zero curvature. □

**Theorem C.2 (complete geodesics and the model exponential charts).** All three models are geodesically and metrically complete. On either quadric the geodesic with initial position \(p\), velocity \(w\), and \(k=|w|\), is
\[
\gamma(t)=C_{ck^2}(t)p+S_{ck^2}(t)w.
\tag{C.6}
\]
On \(S_a^n\), for every \(p\), the exponential map is a diffeomorphism
\[
\exp_p:B_{\pi a}(0)\subset T_pS_a^n
                   \longrightarrow S_a^n\setminus\{-p\}.
\tag{C.7}
\]
On \(H_a^n\), at \(o=(0,a)\), it is a diffeomorphism \(T_oH_a^n\to H_a^n\). The Euclidean exponential \(\exp_p(w)=p+w\) is a diffeomorphism onto \(\mathbb R^n\).

**Proof.** Put \(d=ck^2\). Since \(\eta(p,w)=0\), \(\eta(p,p)=\epsilon a^2\) and \(\eta(w,w)=k^2\), (B.7) gives
\[
\eta(\gamma(t),\gamma(t))
=\epsilon a^2\bigl(C_d(t)^2+dS_d(t)^2\bigr)
=\epsilon a^2.
\]
In the hyperbolic case the time coordinate cannot vanish on this level set. It is positive at zero, so continuity keeps it positive for all real \(t\). Thus (C.6) stays on the chosen model. Differentiating (B.7) gives
\[
\gamma''=-d\gamma,\qquad
\eta(\gamma',\gamma')=k^2(C_d^2+dS_d^2)=k^2.
\]
Formula (C.3) consequently yields \(\nabla_t\gamma'=0\).
Its initial data are \(p,w\), and [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) gives uniqueness. Since it exists for all \(t\), all geodesics are complete. When \(w=0\) the formula is the constant curve, as \(C_0=1\) and \(S_0(t)=t\).
Euclidean lines prove the analogous completeness there. The models are connected: (C.4) proves this for the hyperboloid, and straight segments do so for Euclidean space. On the sphere, two nonantipodal points are joined by normalizing their straight segment to length \(a\); antipodal points can first be joined through any perpendicular point. Such a point exists in every positive dimension. Hopf–Rinow B.2 gives metric completeness.

For a unit tangent vector \(v\), formula (C.6) reads
\[
\exp_p(rv)=C_c(r)p+S_c(r)v.
\tag{C.8}
\]
This follows by substituting the three formulas in (B.6), which give \(C_{cr^2}(1)=C_c(r)\) and \(rS_{cr^2}(1)=S_c(r)\) for \(r>0\). It also holds at zero by continuity.

On the sphere, if \(q\ne p,-p\), its scalar \(\langle p,q\rangle/a^2\) is strictly between \(-1\) and \(1\). Indeed write \(q=\alpha p+q^\perp\); its norm gives \(\alpha^2\leq1\), with equality exactly at \(q=\pm p\).
By B.2 there is one \(r\in(0,\pi a)\) for which \(C_c(r)=\alpha\). Set
\[
v=\frac{q-C_c(r)p}{S_c(r)}.
\tag{C.9}
\]
It is tangent and unit: the squared norm of its numerator is
\(a^2(1-C_c(r)^2)=S_c(r)^2\), using \(c=a^{-2}\) and (B.7). Thus (C.9) recovers the unique polar data of \(q\), proving bijectivity in (C.7), including \(q=p\) from the zero vector. Its differential is invertible away from zero by B.3, since \(S_c>0\) there. In dimension one there are no angular directions, and (C.8) has a nonzero unit radial derivative, giving the same conclusion directly. At zero its differential is the identity by [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). The smooth local inverses from that theorem and [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) glue, by bijectivity, to a global smooth inverse.

For \(H_a^n\) take \(p=o\) and \(v=(u,0)\), \(|u|=1\). Formula (C.8) is
\[
\exp_o(rv)=\bigl(a\sinh(r/a)u,\ a\cosh(r/a)\bigr).
\tag{C.10}
\]
The function \(r\mapsto a\sinh(r/a)\) is strictly increasing from zero onto \([0,\infty)\). Its derivative is positive, and its unboundedness follows from the exponential growth proved in [Geodesics A.4](geodesics-normal-coordinates-and-curvature.md#example-a-4) and the definition in [Riemannian connections D.1](riemannian-connections-and-convex-neighbourhoods.md#lemma-d-1). Hence every nonzero spatial vector \(x\) in (C.4) determines exactly one \(r>0\) and \(u=x/|x|\). The zero spatial vector corresponds to \(r=0\).
This proves bijectivity. Again B.3 gives an invertible differential away from zero (in dimension one, use the unit radial derivative just described), and [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1) at zero; its inverse is smooth. The Euclidean assertion follows directly from its straight-line geodesics. □

**Lemma C.3 (simple connectivity of the models).** For \(n\geq2\), the sphere \(S_a^n\) is simply connected. Euclidean space and \(H_a^n\) are simply connected in every positive dimension.

**Proof.** Scale the sphere to radius one. It is path connected: (C.8) joins \(p\) to every point other than \(-p\), and any unit \(v\perp p\) reaches \(-p\) at time \(\pi\). Such a vector exists for \(n\geq1\).
Let \(\alpha:[0,1]\to S^n\) be a continuous based loop. Uniform continuity on the compact interval follows from [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations): otherwise pairs with parameter difference tending to zero but images separated by a fixed amount have a common convergent parameter subsequence, contradicting continuity. Choose a subdivision so that the image of each subinterval stays within Euclidean distance \(\delta=1/8\) of its left endpoint \(u_i=\alpha(t_i)\). Join consecutive endpoints by normalized straight segments
\[
\beta(t)=\frac{(1-s)u_i+s u_{i+1}}
 {|(1-s)u_i+s u_{i+1}|},
\qquad s=\frac{t-t_i}{t_{i+1}-t_i}.
\tag{C.11}
\]
Their denominators are nonzero, since their numerators are within \(\delta<1\) of \(u_i\). A vector \(q\) within \(\delta\) of a unit vector satisfies
\(\left|q/|q|-u_i\right|\leq2\delta\), by the triangle inequality and \(\bigl||q|-1\bigr|\leq|q-u_i|\). Thus \(|\beta(t)-\alpha(t)|\leq3\delta<1\). The normalization of
\[
(1-s)\alpha(t)+s\beta(t),\qquad 0\leq s\leq1,
\]
is consequently a continuous homotopy between the loops with their base point fixed; the vector being normalized stays within distance \(3\delta\) of the unit \(\alpha(t)\).

The image of each segment (C.11) lies in the linear span of two vectors. Since \(n+1\geq3\), this is a proper subspace of \(\mathbb R^{n+1}\). A finite union of proper subspaces does not fill that vector space. Here is an elementary justification. For each choose a nonzero linear form vanishing on it, by extending a basis. Their product is a nonzero polynomial: products of nonzero polynomials are nonzero, as follows by multiplying highest powers in one variable and inducting on the number of variables. A nonzero real polynomial cannot vanish everywhere: regard it as a polynomial in its last variable, choose values of the other variables where a nonzero coefficient is nonzero by induction, and then choose the last variable outside its finitely many roots. The one-variable root bound follows by division by each linear factor and induction on the degree. A vector where the product is nonzero is outside every chosen subspace. Normalize it to a point \(b\in S^n\). The loop \(\beta\) avoids \(b\).

For clarity the complement of \(b\) is a coordinate copy of \(\mathbb R^n\). Choose orthogonal coordinates carrying \(b\) to the north pole; the Gram–Schmidt proof in [Riemannian connections, F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2) constructs such coordinates. Stereographic projection and its inverse are
\[
(x,t)\longmapsto\frac{x}{1-t},\qquad
z\longmapsto
\left(\frac{2z}{1+|z|^2},
      \frac{|z|^2-1}{1+|z|^2}\right).
\tag{C.12}
\]
Substitution verifies that they are inverse smooth maps between \(S^n\setminus\{b\}\) and \(\mathbb R^n\). Linearly contract the image of \(\beta\) to its base point and apply the inverse map. Together with the preceding homotopy this contracts \(\alpha\) with its base point fixed. The sphere is simply connected. Euclidean loops contract by the same linear homotopy, and the diffeomorphism (C.4) transfers it to \(H_a^n\). □

**Exercise C.4 (upper half-space as the same complete model).** For \(u\in\mathbb R^{n-1}\), \(z>0\), put \(\rho=|u|^2+z^2\) and
\[
\Psi(u,z)=
\left(\frac{au}{z},
      \frac{a(\rho-1)}{2z},
      \frac{a(\rho+1)}{2z}\right).
\tag{C.13}
\]
The last coordinate is time in (C.2). Prove that \(\Psi\) is a diffeomorphism onto \(H_a^n\) and determine its pullback metric and completeness.

**Solution.** Write its coordinates as \((x,y,t)\). One has
\[
t-y=\frac a z,\qquad t+y=\frac{a\rho}{z}.
\tag{C.14}
\]
Thus \(t^2-y^2=a^2\rho/z^2=|x|^2+a^2\), and \(t>0\). Its image lies in the upper hyperboloid. Conversely any point of that hyperboloid has \(t>|y|\), and the formulas
\[
z=\frac a{t-y}>0,\qquad u=\frac{x}{t-y}
\tag{C.15}
\]
recover it. In fact \(t+y=(|x|^2+a^2)/(t-y)\), which, after (C.15), is the second identity of (C.14). All formulas are smooth, so they give the required diffeomorphism.

For a tangent variation \((du,dz)\), differentiation gives
\[
\begin{aligned}
dx&=a\left(\frac{du}{z}-\frac{u\,dz}{z^2}\right),\\
d(t-y)&=-\frac{a\,dz}{z^2},\\
d(t+y)&=a\left(\frac{2u\cdot du+2z\,dz}{z}
                         -\frac{\rho\,dz}{z^2}\right).
\end{aligned}
\]
The quadratic form \(dy^2-dt^2\) equals \(-d(t-y)d(t+y)\). Adding it to \(|dx|^2\) cancels the two mixed terms \(u\cdot du\,dz\). Its remaining \(dz^2\) coefficient is
\(a^2(|u|^2-\rho)/z^4+2a^2/z^2=a^2/z^2\). Hence
\[
\Psi^*g=\frac{a^2}{z^2}\bigl(|du|^2+dz^2\bigr).
\tag{C.16}
\]
The map is a global isometry for this metric. [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) transfers the curvature and geodesic equations, and lengths in both directions. C.1–C.2 therefore give constant curvature \(-a^{-2}\) and geodesic and metric completeness of the upper-half-space model. □

## D. Global constant-curvature geometry

A **space form** here means a nonempty connected complete Riemannian manifold of constant sectional curvature. We prove the passage from local polar metrics to its global quotient, following the two-chart construction in Lang's free lecture notes and supplying all the covering and quotient details.

**Lemma D.1 (a local isometry is determined by one tangent map).** Let \(F,G:N\to M\) be local isometries with \(N\) connected. If \(F(p)=G(p)\) and \(dF_p=dG_p\) at one point, then \(F=G\). In particular, for real inner-product spaces \(V,W\) of dimension \(n\geq2\), a smooth map \(j:S(V)\to S(W)\) whose differential is an isometry at every point is the restriction of a linear orthogonal isomorphism \(V\to W\).

**Proof.** Equal dimensions and the inverse function theorem make each local isometry a local diffeomorphism. [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) proves that it preserves geodesics with their parameters. Thus near zero in each tangent space,
\[
F\circ\exp_x=\exp_{F(x)}\circ dF_x,
\qquad
G\circ\exp_x=\exp_{G(x)}\circ dG_x.
\tag{D.1}
\]
Let \(A\) be the set of points where both the values and differentials agree. It is closed: near a limit point whose two image values agree, put the images in a common target chart; continuity of the coordinate functions and their derivatives preserves both equalities. Equality of image values itself is closed because \(M\) is Hausdorff. The set is open by (D.1) and the normal-coordinate diffeomorphism of [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1): at a point in \(A\), the two maps agree on a neighbourhood, and hence so do their derivatives. It is nonempty by hypothesis. Connectedness gives \(A=N\).

For the second assertion fix \(v\in S(V)\). The splittings
\[
V=\mathbb Rv\oplus v^\perp,\qquad
W=\mathbb Rj(v)\oplus j(v)^\perp
\]
identify the second summands with the two sphere tangent spaces. Define \(L(v)=j(v)\) and \(L|_{v^\perp}=dj_v\), extending linearly. These are orthogonal splittings and \(dj_v\) is an isometry onto the target tangent space, so \(L\) is an orthogonal isomorphism. Both \(j\) and \(L|_{S(V)}\) are local isometries with the same value and differential at \(v\). The sphere is connected, as proved by its explicit geodesics in C.2–C.3, also when it is a circle. The first assertion makes them equal everywhere. □

**Theorem D.2 (the complete constant-curvature classification).** Let \(M\) be a space form of dimension \(n\geq2\) and curvature \(c\). Define
\[
X_c^n=
\begin{cases}
S_{1/\sqrt c}^n,&c>0,\\
\mathbb R^n,&c=0,\\
H_{1/\sqrt{-c}}^n,&c<0 .
\end{cases}
\tag{D.2}
\]
There is a surjective covering local isometry \(F:X_c^n\to M\). It is a global isometry when \(M\) is simply connected.

**Proof.** Choose \(q\in M\), a model point \(p\), and a linear isometry \(L:T_pX_c^n\to T_qM\), by orthonormal bases. In the hyperbolic case take \(p=(0,a)\) as in C.2. Completeness of \(M\) makes \(\exp_q\) defined on all of \(T_qM\), by Hopf–Rinow B.2. On the model exponential chart of C.2 set
\[
F=\exp_q\circ L\circ(\exp_p)^{-1}.
\tag{D.3}
\]
It is smooth. Away from the chart centre, B.3 gives the same polar metric on both sides of this expression, since the dimension and \(c\) agree and \(L\) is an isometry on the unit tangent spheres. Therefore \(F^*g_M=g_{X_c^n}\) there. At the centre its differential is \(L\), because both exponential differentials at zero are identities by [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1), so the same metric equality holds there. Its differential is invertible everywhere in the chart; thus it is a local isometry.

For \(c\leq0\), C.2 makes the chart all of \(X_c^n\). For \(c>0\), its domain is \(S_a^n\setminus\{-p\}\). Choose \(\widetilde p\ne p,-p\), set \(\widetilde q=F(\widetilde p)\), and repeat (D.3) with the isometry \(dF_{\widetilde p}\). This gives a local isometry \(\widetilde F\) on \(S_a^n\setminus\{-\widetilde p\}\). The two maps have the same value and differential at \(\widetilde p\).

Their common domain is connected. In fact stereographic projection (C.12) from one removed point identifies it with \(\mathbb R^n\) minus one point. In dimension at least two this complement is path connected: for two given points choose an intermediate point outside the two lines through the omitted point and those endpoints; the resulting two line segments avoid the omitted point. Such an intermediate point exists, since a circle in an affine two-plane meets each of the two lines in at most two points and has more than four points. The intersection bound follows by substituting a line into the circle's quadratic equation. D.1 therefore makes \(F=\widetilde F\) on the common domain. Their union is a smooth local isometry on the entire sphere.

In either curvature sign, the model is connected and complete by C.2. Hopf–Rinow E.4 now makes the global \(F\) a surjective smooth covering. The model is simply connected by C.3. If \(M\) is simply connected too, [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) identifies every connected covering with the cover belonging to the trivial subgroup of its trivial fundamental group; this is the identity covering. Thus \(F\) is a diffeomorphism. Its local metric equality then makes it a global isometry. □

A group \(\Gamma\) of isometries acts **freely** if no nonidentity element fixes a point. We call its action **properly discontinuous** if
\[
\{\gamma\in\Gamma:\gamma K\cap K\ne\varnothing\}
\quad\hbox{is finite for every compact }K .
\tag{D.4}
\]

**Theorem D.3 (quotients and their isometries).** Every space form of dimension \(n\geq2\) is isometric to \(X_c^n/\Gamma\) for a free properly discontinuous group of model isometries. Conversely every such quotient, with its induced metric, is a space form. Two quotients of the same \(X_c^n\) are isometric if and only if their groups are conjugate by an isometry of \(X_c^n\).

**Proof.** For the covering \(F:X_c^n\to M\) in D.2, the simple connectivity in C.3 and [Flat connections D.2–D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) identify it with the universal cover. Its deck group \(\Gamma\) acts freely, is transitive on each fibre, and is determined element by element by the image of one point. Deck transformations are smooth. Differentiating \(F\circ\gamma=F\) and using that \(F\) is a local isometry gives
\[
g_{\gamma x}(d\gamma_xv,d\gamma_xw)=g_x(v,w).
\]
Their smooth inverses are deck transformations as well, so they are model isometries.

We verify (D.4). Otherwise choose distinct \(\gamma_j\) and \(x_j\in K\) with \(y_j=\gamma_jx_j\in K\). Compactness and the metric sequential criterion in Hopf–Rinow, G.1, give subsequences with \(x_j\to x\) and \(y_j\to y\). The equalities \(F(x_j)=F(y_j)\) imply \(F(x)=F(y)\). Choose a connected evenly covered coordinate neighbourhood of this common value, and its sheets \(U_x,U_y\) containing \(x,y\). Eventually \(x_j\in U_x\) and \(y_j\in U_y\). A deck map sends a sheet to a sheet, so \(\gamma_jU_x=U_y\). There is at most one such deck map: the unique point over any chosen base value in \(U_x\) must be sent to the unique point over it in \(U_y\), and [Flat D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) gives uniqueness from that value. This contradicts the distinct \(\gamma_j\). The fibres are exactly the orbits, so \(F\) induces a bijection \(X_c^n/\Gamma\to M\); in inverse sheet charts it and its inverse are smooth isometries.

Conversely let \(\Gamma\) act freely and satisfy (D.4) on \(X=X_c^n\). The orbit map \(\pi:X\to X/\Gamma\), with the quotient topology, is open: \(\pi^{-1}\pi(U)=\bigcup_\gamma\gamma U\) is open for open \(U\). Choose a compact coordinate neighbourhood \(K\) of a point \(x\). Such neighbourhoods exist by taking a closed ball strictly inside a coordinate chart and applying [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Only finitely many \(\gamma\) have \(\gamma K\cap K\ne\varnothing\). For each of their nonidentity elements, freeness gives \(\gamma x\ne x\); Hausdorff separation and continuity give a neighbourhood \(U_\gamma\) of \(x\) disjoint from its \(\gamma\)-translate. Intersect these finitely many neighbourhoods with the interior of \(K\), obtaining \(U\). Every nonidentity translate of \(U\) is disjoint from \(U\), including those outside the finite set, since their translates of \(K\) miss \(K\). It follows that
\[
\pi^{-1}(\pi U)=\coprod_{\gamma\in\Gamma}\gamma U
\tag{D.5}
\]
and each restriction of \(\pi\) is a homeomorphism onto \(\pi U\). To see the inverse is continuous, an open subset of \(U\) has open saturation and hence open image in the quotient.

The quotient is Hausdorff. For points \(x,y\) in different orbits choose compact coordinate neighbourhoods \(K_x,K_y\). Apply (D.4) to \(K_x\cup K_y\): only finitely many \(\gamma\) can have \(\gamma K_x\cap K_y\ne\varnothing\). None satisfies \(\gamma x=y\). Shrink neighbourhoods of \(x,y\) to exclude those finitely many intersections, using continuity and Hausdorff separation as above. No other group element can intersect them because they stay inside the chosen compact sets. Their images under \(\pi\) are disjoint open neighbourhoods. Images of a countable basis of \(X\) form a countable basis of the quotient, by openness of \(\pi\).

Give each quotient chart \(\pi U\) the smooth coordinates of \(U\). On an overlap its transition map locally lifts to a fixed element of \(\Gamma\): use the disjoint sheets (D.5) and shrink about each point of the overlap. Such a map is a smooth isometry. The charts therefore define a smooth Hausdorff second-countable manifold and a well-defined smooth metric for which \(\pi\) is a covering local isometry. The quotient is connected as the image of the connected model. [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) transfers its curvature, which is \(c\). Hopf–Rinow E.4 transfers completeness from \(X\). This proves that it is a space form.

For the isometry assertion, let \(\phi:X/\Gamma\to X/\Gamma'\) be an isometry. The map \(\phi\circ\pi\) is a universal covering of \(X/\Gamma'\), since \(X\) is simply connected. The uniqueness statement in [Flat D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) supplies a based covering isomorphism \(\widetilde\phi:X\to X\) with
\[
\pi'\circ\widetilde\phi=\phi\circ\pi.
\tag{D.6}
\]
In sheet charts it is a smooth local isometry. The covering isomorphism has a smooth inverse, so it is a global model isometry. For \(\gamma\in\Gamma\), equation (D.6) makes
\(\widetilde\phi\gamma\widetilde\phi^{-1}\) a deck map of \(\pi'\). This proves inclusion in \(\Gamma'\), and using \(\phi^{-1}\) proves equality. Conversely a model isometry conjugating the groups sends orbits to orbits, descends through their charts to an isometry, and its inverse descends in the same way. □

**Theorem D.4 (lens examples and even-dimensional spherical quotients).** For integers \(p\geq1\) and \(q_1,\ldots,q_m\) each relatively prime to \(p\), put \(\zeta=\exp(2\pi i/p)\). The cyclic action on the unit sphere in \(\mathbb C^m\) generated by
\[
(z_1,\ldots,z_m)\longmapsto
(\zeta^{q_1}z_1,\ldots,\zeta^{q_m}z_m)
\tag{D.7}
\]
is free, has order \(p\), and gives a complete constant-curvature quotient. When \(2m-1\geq2\) it is a space form in the dimension range of D.3. For every even \(n\geq2\), the only spherical space forms of curvature \(a^{-2}\) are \(S_a^n\) and \(S_a^n/\{I,-I\}\), the round real projective space.

**Proof.** [Connections E.1](connections-and-parallel-transport.md#lemma-e-1) proves that \(\exp(it)=1\) exactly for \(t\in2\pi\mathbb Z\). Hence \(\zeta^k=1\) exactly when \(p\) divides \(k\). If a power \(k\) of (D.7) fixes a sphere point, at least one coordinate \(z_j\ne0\), so \(p\mid kq_j\). Coprimality gives integers \(a,b\) with \(a q_j+b p=1\), and multiplying by \(k\) shows \(p\mid k\). The asserted integer relation follows from the Euclidean division algorithm: its successive remainders are integer combinations of \(q_j,p\), its strictly decreasing positive remainders terminate, and the last nonzero remainder is their greatest common divisor, here one. Thus no nonidentity group element fixes a point, and the group has exactly \(p\) elements. Its diagonal operators preserve the standard real metric. A finite group satisfies (D.4) automatically. The quotient construction and completeness proof in D.3 apply; their converse part only needs connectedness and completeness of the source, so it also applies to the circle when \(m=1\). The name for these quotients is **lens spaces**.

Now let \(n\) be even. By D.2–D.3 any spherical space form has a group \(\Gamma\) of free properly discontinuous sphere isometries. D.1 makes every sphere isometry the restriction of an orthogonal map of \(\mathbb R^{n+1}\): scale to unit radius and apply its direction-sphere assertion with \(\dim V=n+1\). Moreover \(\Gamma\) is finite, by applying (D.4) to the compact whole sphere.
An orthogonal map in odd real dimension has a real eigenvalue: its real characteristic polynomial has odd degree, hence opposite signs for sufficiently large positive and negative inputs; the intermediate value theorem, [Local tools 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), supplies a real root. The singular matrix at that root has a nonzero real kernel vector. Orthogonality forces the eigenvalue to have absolute value one, so it is \(1\) or \(-1\).

For \(\gamma\in\Gamma\), a \(+1\) eigenvector would give a sphere fixed point and hence \(\gamma=I\). If \(\gamma\ne I\), it therefore has a \(-1\) eigenvector. Then \(\gamma^2\) fixes a sphere point and must equal \(I\). If this \(\gamma\) differed from \(-I\), choose \(v\) with \((\gamma+I)v\ne0\). That vector is fixed by \(\gamma\), since
\(\gamma(\gamma+I)v=(I+\gamma)v\), contradicting freeness. Thus each nonidentity element is exactly \(-I\). The only groups are the trivial group and \(\{I,-I\}\). Both act freely and have the required quotients by D.3; identifying antipodal points is precisely the definition of real projective space with its round quotient metric. □

## E. Finite groups acting without fixed vectors

The sphere condition has a useful linear form. If a finite group \(\Gamma\) acts orthogonally on a nonzero real inner-product space \(V\), its sphere action is free exactly when
\[
\ker(\gamma-I)=0\qquad(\gamma\ne1).
\tag{E.1}
\]
Indeed every nonzero fixed vector can be normalized to a sphere point, and a sphere point is already a nonzero vector. This also makes the representation faithful.

Allcock's free author manuscript proves the two-prime restriction by moving between character spaces. We develop the counting and linear-algebra ingredients before making that argument.

**Lemma E.1 (the finite-group counting needed below).** Let \(G\) be a finite group.

1. The order of a subgroup divides \(|G|\), and the size of an orbit of a \(G\)-action is the index of its stabilizer.
2. If a prime \(p\) divides \(|G|\), some element has order \(p\).
3. Every group of order \(p^2\) is abelian.
4. If \(|G|=pq\), with primes \(p<q\), there is a unique subgroup \(Q\) of order \(q\); it is normal. There is a subgroup \(P\) of order \(p\), and every element of \(G\) is uniquely \(ab\), with \(a\in Q\), \(b\in P\).

**Proof.** For a subgroup \(H\), the left cosets \(gH\) partition \(G\). In fact an intersection \(gH\cap kH\ne\varnothing\) gives \(g^{-1}k\in H\), and hence \(gH=kH\). Multiplication by \(g\) bijects \(H\) with \(gH\). Thus
\[
|G|=[G:H]|H|.
\tag{E.2}
\]
For a point \(x\) of any \(G\)-set, \(gx=kx\) holds exactly when \(k^{-1}g\) belongs to its stabilizer \(H_x\). The orbit is consequently in bijection with the left cosets of \(H_x\). These observations prove the first assertion. Applied to the cyclic subgroup generated by an element, they also show that its order divides \(|G|\). More directly, if the least positive \(r\) with \(g^r=1\) exists, division of any exponent \(s\) by \(r\) proves that \(g^s=1\) exactly when \(r\mid s\).

For the second assertion consider
\[
\mathcal T=\{(g_1,\ldots,g_p)\in G^p\mid g_1\cdots g_p=1\}.
\]
The first \(p-1\) entries can be chosen freely, and the last is then forced, so \(|\mathcal T|=|G|^{p-1}\). Cyclically rotate the entries. Rotation preserves \(\mathcal T\), since
\[
g_2\cdots g_pg_1=g_1^{-1}(g_1\cdots g_p)g_1=1.
\]
The cyclic rotation group has order \(p\); each orbit therefore has size \(1\) or \(p\), by the first assertion. A fixed tuple has all entries equal to some \(g\) satisfying \(g^p=1\). As \(|\mathcal T|\) is divisible by \(p\), the number of fixed tuples is divisible by \(p\). One is the identity tuple, so at least one more exists. Its entry \(g\ne1\) has order \(p\), because its order divides the prime \(p\).

For the third assertion let \(|G|=p^2\). If an element has order \(p^2\), it generates \(G\), and the assertion follows. Otherwise each nonidentity element has order \(p\), by (E.2). For a noncentral element \(g\), its centralizer contains \(\langle g\rangle\) and is a proper subgroup, so it has order \(p\). The conjugacy class of \(g\) has size \(p\), by the orbit formula applied to conjugation. Splitting \(G\) into its central elements and its noncentral conjugacy classes shows
\[
|G|=|Z(G)|+p\,k
\]
for an integer \(k\). Hence \(p\mid |Z(G)|\). The centre contains the identity, and (E.2) leaves the possibilities \(|Z(G)|=p\) or \(p^2\). In the latter case \(G\) is abelian. In the former case the quotient \(G/Z(G)\) has order \(p\), hence is generated by any of its nonidentity elements. Choose a lift \(g\) of such a generator. Every element of \(G\) is \(g^jz\) for \(z\in Z(G)\). Two such expressions commute, since their central factors commute with everything and their powers of \(g\) commute. This makes \(G\) abelian too, and in fact contradicts \(|Z(G)|=p\). Thus only the abelian case occurs.

For the fourth assertion the second gives subgroups of orders \(p\) and \(q\). Distinct subgroups of order \(q\) intersect only in the identity: a nonidentity intersection element generates both. Let \(r\) be the number of subgroups of order \(q\). Counting their disjoint sets of \(q-1\) nonidentity elements gives
\[
r(q-1)\le pq-1,\qquad
r\le p,
\tag{E.3}
\]
where the last inequality uses \(p<q\) and
\((pq-1)/(q-1)=p+(p-1)/(q-1)<p+1\).

Fix one of them, \(Q\), and let it act by conjugation on the set of all such subgroups. Each orbit has size \(1\) or \(q\). The subgroup \(Q\) itself is fixed. No other subgroup \(Q'\) can be fixed. If it were, \(Q\) would normalize \(Q'\), and \(QQ'\) would be a subgroup of order \(q^2\). To check both points of this last claim, normalizing allows factors from \(Q\) to be moved past factors from \(Q'\), proving closure and inverses of the product set; and \(ab=a'b'\) forces
\(a'^{-1}a=b'b^{-1}\in Q\cap Q'=\{1\}\), proving that its \(q^2\) expressions are distinct. Equation (E.2) forbids \(q^2\mid pq\). Thus \(Q\) is the only fixed point of its conjugation action, and
\[
r=1+qk
\]
for a nonnegative integer \(k\). Together with (E.3), this gives \(r=1\). The unique \(Q\) is normal, because every conjugate has the same order. Choose any subgroup \(P\) of order \(p\). Its intersection with \(Q\) is trivial by (E.2); therefore the \(pq\) products \(ab\), \(a\in Q,b\in P\), are distinct and exhaust \(G\), as claimed. □

**Lemma E.2 (finite-order eigenspaces and finite circle groups).** Let \(T\) be a complex linear operator on a finite-dimensional complex vector space \(W\), with \(T^m=I\), \(m\ge1\). Put \(\zeta=\exp(2\pi i/m)\). Then
\[
W=\bigoplus_{k=0}^{m-1}\ker(T-\zeta^k I).
\tag{E.4}
\]
A finite family of commuting finite-order operators has a common eigenspace decomposition. Every finite subgroup of \(U(1)\) is cyclic.

**Proof.** The exponential and its exact period are proved in [Connections, E.1](connections-and-parallel-transport.md#lemma-e-1). They imply that \(\zeta^r=1\) exactly when \(m\mid r\). The finite geometric-sum identity therefore gives
\[
\sum_{j=0}^{m-1}\zeta^{rj}
=\begin{cases}m,&m\mid r,\\0,&m\nmid r.\end{cases}
\tag{E.5}
\]
For the nontrivial case multiply the sum by \(1-\zeta^r\): all intermediate terms cancel and the remaining term is \(1-\zeta^{rm}=0\).

Define operators
\[
P_k=\frac1m\sum_{j=0}^{m-1}\zeta^{-kj}T^j.
\tag{E.6}
\]
Equation (E.5), summing first over \(k\), gives \(\sum_kP_k=I\). Reindexing the sum and using \(T^m=I\) gives \(TP_k=\zeta^kP_k\), so the range of \(P_k\) belongs to the indicated eigenspace. Conversely, on an eigenvector of eigenvalue \(\zeta^\ell\), (E.5) gives \(P_kv=v\) if \(k=\ell\) and zero otherwise. Thus those eigenspaces are independent: applying \(P_k\) to a sum of vectors in them isolates its \(k\)-th term. Their sum is all \(W\) by \(\sum P_k=I\). This proves (E.4), including \(m=1\).

If another operator commutes with \(T\), it preserves each of these eigenspaces, because \(T(Sv)=S(Tv)\). Apply (E.4) to its restriction on each eigenspace. Continuing through the finite commuting family proves the simultaneous decomposition. On each resulting nonzero subspace all the operators act as scalars; choosing any nonzero vector there gives a common eigenvector.

Now let \(A\subset U(1)\) be finite, of order \(N\). E.1 gives \(a^N=1\) for every \(a\in A\). Write \(a=\exp(it)\), using [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). Its period makes \(Nt\in2\pi\mathbb Z\), so \(a\) is a power of \(\exp(2\pi i/N)\). Thus \(A\) is a subgroup of that cyclic group. For completeness, any subgroup of a finite cyclic group is cyclic: the set of integers \(j\) whose powers belong to the subgroup is closed under sums and differences and contains \(N\). Choose its least positive element \(d\). Dividing any such \(j\) by \(d\), the remainder is another nonnegative member smaller than \(d\), so it is zero. The powers in the subgroup are consequently exactly the powers of the \(d\)-th power of the original generator. □

**Theorem E.3 (the two-prime restriction).** Suppose a finite group \(\Gamma\) acts freely and orthogonally on a sphere. Every abelian subgroup is cyclic. Every subgroup of order \(pq\), where \(p,q\) are primes that may coincide, is cyclic.

**Proof.** Let \(V\ne0\) be the real representation space. Its complexification \(W=V\otimes_{\mathbb R}\mathbb C\) also satisfies (E.1). Indeed if \(\gamma\) fixes \(x+iy\ne0\), it fixes both real vectors \(x,y\), at least one of which is nonzero. Equip \(W\) with the Hermitian inner product obtained by extending an orthonormal real basis; the real orthogonal operators become unitary.

Let \(A\subseteq\Gamma\) be abelian. Its elements are a finite commuting family of finite-order operators on \(W\). By E.2 there is a nonzero common eigenvector \(v\). Write
\[
av=\chi(a)v\qquad(a\in A).
\]
The equations for a product give \(\chi(ab)=\chi(a)\chi(b)\), and unitarity gives \(|\chi(a)|=1\). If \(\chi(a)=1\), freeness on \(W\) implies \(a=1\). Therefore \(\chi\) identifies \(A\) with a finite subgroup of \(U(1)\), which is cyclic by E.2.

Consider a subgroup \(G\) of order \(pq\). If \(p=q\), E.1 makes it abelian, and the first part makes it cyclic. Otherwise reorder the primes so that \(p<q\). E.1 supplies a normal subgroup \(Q=\langle a\rangle\) of order \(q\) and a subgroup \(P=\langle b\rangle\) of order \(p\), with \(G=QP\). Conjugation has the form
\[
bab^{-1}=a^r
\tag{E.7}
\]
for a nonzero residue \(r\) modulo \(q\). If \(r=1\), the two generators commute and \(G\) is abelian, hence cyclic by the first part.

Suppose instead \(r\ne1\). Conjugating \(p\) times gives \(r^p=1\) modulo \(q\). The order of \(r\) in the multiplicative residue group therefore divides \(p\), by the exponent-division argument of E.1, and hence is exactly \(p\). Inverses of nonzero residues exist by the Euclidean algorithm, as used in D.4.

Apply E.2 to the operator \(a\) and choose a nonzero eigenvector \(v\in W\), say \(av=\lambda v\). Since \(a\ne1\), freeness gives \(\lambda\ne1\). Also \(\lambda^q=1\); as \(q\) is prime, the order of \(\lambda\) is exactly \(q\). Equation (E.7) implies
\[
a(b^jv)=\lambda^{\,r^{-j}}b^jv
\qquad(0\le j<p).
\tag{E.8}
\]
Here the inverse power of \(r\) is taken modulo \(q\); changing its integer representative does not change the expression. The formula follows by moving \(a\) past \(b^j\):
\(b^{-j}ab^j=a^{r^{-j}}\).

The \(p\) residues \(r^{-j}\) are distinct, since \(r\) has order \(p\), and the \(p\) eigenvalues in (E.8) are consequently distinct, since \(\lambda\) has order \(q\). Every \(b^jv\) is nonzero. Their eigenspaces form a direct sum by E.2, so
\[
w=v+bv+\cdots+b^{p-1}v\ne0.
\tag{E.9}
\]
But \(b^p=1\), and therefore \(bw=w\). This contradicts freeness, because \(b\ne1\). The noncommuting case is impossible. Every subgroup of the stated order is cyclic. □

## F. Which spherical quotients are homogeneous?

A Riemannian manifold is **homogeneous** if, for any two of its points, there is a smooth Riemannian isometry carrying the first to the second. For a spherical quotient we can test this condition entirely in the ambient orthogonal group. Wolf's free author article explains the real, complex and quaternionic alternatives; the proof here uses the earlier complete programme proof of the real commutant and an explicit finite-coset argument.

**Lemma F.1 (the centralizer criterion).** Let \(n\ge2\) and let \(\Gamma\subseteq O(n+1)\) be finite and act freely on \(S_a^n\). Define
\[
\begin{aligned}
C&=\{U\in O(n+1):U\gamma=\gamma U
                    \text{ for all }\gamma\in\Gamma\},\\
N&=\{U\in O(n+1):U\Gamma U^{-1}=\Gamma\}.
\end{aligned}
\tag{F.1}
\]
Then \(S_a^n/\Gamma\) is homogeneous if and only if \(C\) is transitive on \(S_a^n\).

**Proof.** Every element of \(N\) descends to an isometry of the quotient, by D.3. Conversely D.3 lifts every quotient isometry to a sphere isometry normalizing \(\Gamma\), and D.1 realizes that sphere isometry as an orthogonal linear map. Thus all quotient isometries arise from \(N\).

If the quotient is homogeneous, \(N\) is transitive on the sphere. Indeed, given \(x,y\in S_a^n\), choose a quotient isometry carrying the orbit of \(x\) to that of \(y\), and lift it to \(U\in N\). Then \(Ux=\gamma y\) for some \(\gamma\in\Gamma\). Since \(\Gamma\subseteq N\), the element \(\gamma^{-1}U\in N\) carries \(x\) to \(y\).

Conjugation defines a homomorphism
\[
N\longrightarrow\operatorname{Aut}(\Gamma)
\]
whose kernel is \(C\). The target is finite, since its elements are permutations of the finite set \(\Gamma\). Consequently \(N\) is a finite union of cosets \(U_1C,\ldots,U_rC\): two elements have the same conjugation action exactly when their quotient belongs to \(C\).

The group \(C\) is compact. It is defined inside the matrix space by the closed equations \(U^TU=I\) and \(U\gamma=\gamma U\), and its entries are bounded by one because its columns have norm one. [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) gives compactness. For a fixed \(x\in S_a^n\), its orbit \(Cx\) is the continuous image of \(C\), so it is compact and closed in the sphere. Transitivity of \(N\) gives
\[
S_a^n=\bigcup_{j=1}^r U_j(Cx).
\tag{F.2}
\]
A finite union of closed sets with empty interior cannot cover this nonempty space. To see this directly, start with the whole sphere as a nonempty open set. Removing a closed set with empty interior leaves a nonempty open set; repeat with each of the finitely many sets. The final open set misses their union. Thus (F.2) implies that at least one \(U_j(Cx)\), and hence \(Cx\), has nonempty interior.

Every point of \(Cx\) is an interior point. Fix one interior point \(z\in Cx\). If \(y\in Cx\), some \(c\in C\) sends \(z\) to \(y\), by the definition of an orbit; it carries an open neighbourhood of \(z\) in \(Cx\) to one of \(y\). Hence \(Cx\) is open as well as closed. The sphere is connected by C.2, so \(Cx=S_a^n\). This proves centralizer transitivity without an assumption about connected components of an isometry group.

Conversely, if \(C\) is transitive on the sphere, its elements normalize \(\Gamma\) and descend to quotient isometries by D.3. An element carrying one chosen lift to another gives the required isometry of quotient points. The quotient is homogeneous. □

**Lemma F.2 (orthogonal scalar coordinates for the commutant).** Suppose \(C\subseteq O(V)\) is transitive on the unit sphere of a nonzero finite-dimensional real inner-product space \(V\). Its commuting algebra
\[
\mathcal D=\{T\in\operatorname{End}_{\mathbb R}V:
                   TU=UT\text{ for every }U\in C\}
\tag{F.3}
\]
is isomorphic, with its adjoint operation, to \(\mathbb R\), \(\mathbb C\) or \(\mathbb H\), with the usual conjugation. For one of these algebras \(\mathbb F\) there is a real linear isometry
\[
\Phi:\mathbb F^m\longrightarrow V
\tag{F.4}
\]
in which every element of \(\mathcal D\) acts by left multiplication by the same scalar on all \(m\) coordinates. Its orthogonal elements are exactly the unit scalars.

**Proof.** A nonzero \(C\)-invariant real subspace contains a unit vector. Transitivity makes it contain every unit vector and hence every vector. Thus \(C\) acts irreducibly. The complete proof in [De Rham decomposition, AC.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-ac-1) applies, without any connectedness or closedness hypothesis on \(C\). It gives an algebra isomorphism
\[
\rho:\mathbb F\longrightarrow\mathcal D,\qquad
\rho(\overline\alpha)=\rho(\alpha)^*,\qquad
\rho(\overline\alpha)\rho(\alpha)=|\alpha|^2 I.
\tag{F.5}
\]
In the quaternionic case its construction sends \(1,i,j,k\) to \(I,J,K,JK\), with \(J^2=K^2=-I\) and \(JK=-KJ\). In the complex case only \(I,J\) are needed. The quaternion norm and conjugation identities are also proved explicitly in [De Rham decomposition, Y.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-y-1).

We construct the coordinates in (F.4), including their side of scalar multiplication. Choose a unit vector \(e\in V\). The map
\[
\mathbb F\longrightarrow V,\qquad
\alpha\longmapsto\rho(\alpha)e
\tag{F.6}
\]
is a real linear isometry. Indeed (F.5) gives norm \(|\alpha|\), and real polarization recovers the inner product from the squared norm:
\[
2\langle u,v\rangle=|u+v|^2-|u|^2-|v|^2.
\]
In particular (F.6) is injective. Its image \(W_e=\mathcal D e\) is \(\mathcal D\)-invariant. Its orthogonal complement is invariant as well: if \(v\perp W_e\), \(w\in W_e\), then
\[
\langle\rho(\alpha)v,w\rangle
=\langle v,\rho(\overline\alpha)w\rangle=0,
\]
because the vector on the right belongs to \(W_e\).

If the complement is nonzero, choose a unit vector there and repeat. Each step removes the positive real dimension \(\dim_{\mathbb R}\mathbb F\), so finitely many steps give an orthogonal direct sum
\[
V=W_{e_1}\oplus\cdots\oplus W_{e_m}.
\tag{F.7}
\]
Define
\[
\Phi(\alpha_1,\ldots,\alpha_m)
=\sum_{j=1}^m\rho(\alpha_j)e_j.
\tag{F.8}
\]
The orthogonal summands and (F.6) make \(\Phi\) a real isometry onto \(V\). Associativity of \(\rho\) gives
\[
\rho(\beta)\Phi(\alpha_1,\ldots,\alpha_m)
=\Phi(\beta\alpha_1,\ldots,\beta\alpha_m).
\tag{F.9}
\]
Thus the action is exactly the asserted left scalar action. Finally (F.5) says that \(\rho(\alpha)\) is orthogonal exactly when \(|\alpha|=1\). This proves every assertion. □

**Theorem F.3 (homogeneous spherical space forms).** Let \(M\) be connected, complete and homogeneous, of dimension \(n\ge2\) and constant sectional curvature \(a^{-2}>0\). Up to orthogonal coordinates, its spherical deck group has one of the following forms.

The real scalar case, available in every dimension, is the trivial group or the antipodal group \(\{I,-I\}\).

The complex scalar case, when \(n+1=2m\), is a finite group of transformations
\[
(z_1,\ldots,z_m)\longmapsto(\lambda z_1,\ldots,\lambda z_m),
\qquad |\lambda|=1 .
\tag{F.10}
\]
Every such group is cyclic.

The quaternionic scalar case, when \(n+1=4m\), is a finite group of transformations
\[
(q_1,\ldots,q_m)\longmapsto(\alpha q_1,\ldots,\alpha q_m),
\qquad |\alpha|=1 .
\tag{F.11}
\]

Conversely every finite group of scalars in these descriptions acts freely on the sphere and gives a homogeneous quotient with its round metric. When \(n\) is even, only the sphere and round real projective space occur. When \(n+1\) is twice an odd integer, all deck groups can be represented as complex scalar cyclic groups. When \(n+1\) is divisible by four, the quaternionic description includes the real and complex scalar cases.

**Proof.** D.2–D.3 identify \(M\) isometrically with \(S_a^n/\Gamma\), where \(\Gamma\) acts freely and properly discontinuously. The group is finite: use the compact sphere as \(K\) in (D.4), so every element belongs to its finite intersection set. By F.1 its orthogonal centralizer \(C\) is transitive on the sphere, and hence on the unit sphere after scaling. Every \(\gamma\in\Gamma\) commutes with \(C\) and is orthogonal. F.2 therefore puts \(\Gamma\), in orthogonal coordinates, inside the unit scalars of \(\mathbb R\), \(\mathbb C\), or \(\mathbb H\).

The real unit scalars are \(1,-1\), whose only subgroups are the first two listed groups. In the complex case E.2 proves cyclicity. The coordinate decomposition (F.7) forces the real dimension \(n+1\) to be \(m\), \(2m\), or \(4m\), respectively. This proves necessity of the list.

Conversely choose any of the listed finite scalar groups on \(\mathbb F^m\), with its standard real inner product. Scalar multiplication by a unit is orthogonal, by norm multiplication in \(\mathbb R,\mathbb C\), or by the quaternionic norm calculation of [De Rham Y.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-y-1). If a scalar \(\alpha\) fixes a sphere vector, at least one coordinate \(q_j\) is nonzero, and
\[
(\alpha-1)q_j=0.
\]
Each of the three algebras is a division algebra, so multiplication by \(q_j^{-1}\) gives \(\alpha=1\). Thus the action is free. The group is finite, so it is properly discontinuous. D.3 gives a complete quotient with the required curvature.

It remains to prove homogeneity of every such quotient. In the real case the orthogonal group on \(\mathbb R^m\) commutes with the real scalars and is sphere-transitive, by the rotation construction in [De Rham decomposition, Y.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-y-2); here \(m=n+1\ge3\). In the complex case \(\mathrm U(m)\) commutes with complex scalar multiplication and is sphere-transitive by the same theorem.

For the quaternionic case the side of multiplication matters. [De Rham Y.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-y-2) constructs \(\mathrm{Sp}(m)\) as the quaternionic matrices \(A\) with \(A^*A=I\), acting by left matrix multiplication on quaternionic columns. These are real isometries, are transitive on the sphere, and commute with **right** scalar multiplication:
\[
A(v\beta)=(Av)\beta .
\tag{F.12}
\]
Let \(J\) denote componentwise quaternionic conjugation; it is a real orthogonal involution. The conjugate group
\[
K=\{J A J:A\in\mathrm{Sp}(m)\}
\tag{F.13}
\]
is still sphere-transitive and consists of real isometries. It commutes with the **left** scalar action in (F.11). Explicitly, using reversal of quaternionic products and (F.12),
\[
\begin{aligned}
(JAJ)(\alpha v)
&=J\bigl(A((Jv)\overline\alpha)\bigr)\\
&=J\bigl((A(Jv))\overline\alpha\bigr)
=\alpha(JAJ)v.
\end{aligned}
\tag{F.14}
\]
Thus \(K\) belongs to the centralizer of every group in (F.11). In all three cases a transitive orthogonal group centralizes the scalar group, so F.1 proves homogeneity.

Finally, if \(n\) is even then \(n+1\) is odd, excluding the complex and quaternionic coordinate dimensions. If \(n+1\) is twice an odd integer, the quaternionic case is excluded and the real scalar groups embed in the complex scalar group; hence all cases are cyclic. If \(n+1=4m\), real scalars already belong to \(\mathbb H\), and the real isometry
\[
\mathbb C^{2m}\longrightarrow\mathbb H^m,\qquad
(z_1,z_2,\ldots,z_{2m-1},z_{2m})
\longmapsto
(z_1+z_2j,\ldots,z_{2m-1}+z_{2m}j)
\tag{F.15}
\]
carries common left complex multiplication to common left quaternionic multiplication by that same complex scalar. The norm identity follows from the real basis \(1,i,j,k\) in [De Rham Y.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-y-1), and the intertwining identity follows by distributing \(\lambda(z_1+z_2j)\). This proves the final inclusions and completes the classification. □

## G. Affine-flat coordinates and complete quotients

A connection on \(TM\) is **affine-flat** when both its curvature \(R\) and its torsion \(\mathcal T\) vanish. An **affine map** between manifolds with connections is a smooth local diffeomorphism preserving those connections. On \(\mathbb R^n\), the standard connection \(\nabla^0\) has zero coefficients in the usual coordinates. Its geodesics are \(t\mapsto x+tv\).

**Theorem G.1 (affine coordinates and affine holonomy).** For a connection on a connected manifold, the following are equivalent:

1. It is affine-flat.
2. Every point has coordinates in which all connection coefficients vanish.
3. The associated normalized affine connection has trivial restricted holonomy.

The transition functions between the coordinates in item 2 are restrictions of invertible affine transformations on each connected overlap. For the Levi-Civita connection of a Riemannian metric, these conditions are equivalent to \(R=0\), and to the metric being locally isometric to Euclidean space.

**Proof.** The frame correspondence in [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) and the curvature formula in [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3) identify \(R=0\) with flatness of the connection on the linear frame bundle. On a simply connected coordinate ball, [Flat connections E.1](flat-connections-and-infinitesimal-holonomy.md#theorem-e-1) supplies a smooth horizontal frame \(E_1,\ldots,E_n\). Each \(E_i\) is parallel by the same frame correspondence. Torsion is
\[
\mathcal T(E_i,E_j)=
\nabla_{E_i}E_j-\nabla_{E_j}E_i-[E_i,E_j],
\]
as proved in [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1). Thus zero torsion makes these fields commute.

Fix \(p\) in the ball. Their smooth local flows exist by [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). After restricting all times to a sufficiently small common rectangle, define
\[
F(t_1,\ldots,t_n)=
\phi_n^{t_n}\circ\cdots\circ\phi_1^{t_1}(p).
\tag{G.1}
\]
[De Rham B.1](holonomy-and-the-de-rham-decomposition-theorem.md#lemma-b-1) shows that these flows commute and preserve the other fields. Differentiation in \(t_i\) therefore gives \(dF(\partial_{t_i})=E_i(F(t))\). In particular \(dF_0\) is invertible. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives a coordinate neighbourhood with coordinate vector fields \(E_i\). Their parallelness gives zero connection coefficients. Conversely, in such coordinates the coordinate fields commute and their covariant derivatives vanish. The displayed torsion formula and [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3) give \(\mathcal T=R=0\).

For the affine-holonomy assertion, [Linear connections E.2](linear-and-affine-connections.md#theorem-e-2) constructs the normalized affine connection with translational component equal to the solder form \(\theta\). [Linear connections E.3](linear-and-affine-connections.md#theorem-e-3) computes its curvature, on the zero-origin linear frames, as
\[
\begin{pmatrix}\Omega&\Theta\\0&0\end{pmatrix}.
\tag{G.2}
\]
Here \(\Omega\) represents \(R\), and \(\Theta\) represents \(\mathcal T\), by [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3) and D.1. Vanishing on these frames is equivalent to vanishing everywhere: every affine frame is a right translate of a zero-origin frame, and curvature transforms equivariantly. The flatness/holonomy equivalence in [Curvature G.6](curvature-and-holonomy-groups.md#theorem-g-6) now identifies item 3 with \(R=\mathcal T=0\).

Let \(f\) be the transition map between two zero-coefficient charts. Preservation of the connection, evaluated on the coordinate fields, gives
\[
\partial_i\partial_j f^a=0
\quad\text{for all }i,j,a.
\tag{G.3}
\]
Indeed the derivative of the coefficients of \(f_*\partial_j\) in direction \(f_*\partial_i\) is precisely the left side, while the pushforward of \(\nabla_{\partial_i}\partial_j\) is zero. Each first derivative is constant on every sufficiently small ball, by integration on straight segments and [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). A locally constant function on a connected set is constant: the set where it has one chosen value and its complement are both open. Thus \(df=A\) is constant on a connected overlap, and the same argument applied to \(f(x)-Ax\) gives \(f(x)=Ax+b\). The matrix \(A\) is invertible because \(f\) is a chart transition. Conversely such a map has zero Hessian, and the same calculation proves that it preserves \(\nabla^0\).

A Levi-Civita connection has zero torsion by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). If \(R=0\), choose the initial parallel frame above orthonormally. Metric compatibility preserves its pairings, so the coordinates (G.1) have metric coefficients \(\delta_{ij}\). They are Euclidean isometry charts. Conversely a Euclidean isometry chart preserves the Levi-Civita connection by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) and hence gives zero coefficients and zero curvature. □

**Theorem G.2 (complete affine-flat manifolds).** A connected geodesically complete affine-flat \(n\)-manifold is affinely diffeomorphic to
\[
\mathbb R^n/\Gamma,
\tag{G.4}
\]
where \(\Gamma\) is a group of invertible affine transformations acting freely and properly discontinuously. Its universal cover, with the lifted connection, is affinely diffeomorphic to \((\mathbb R^n,\nabla^0)\). Conversely every such quotient is a connected geodesically complete affine-flat manifold. The group \(\Gamma\) is discrete in the ordinary topology of
\(\operatorname{Aff}(n,\mathbb R)=\operatorname{GL}(n,\mathbb R)\ltimes\mathbb R^n\).

Here proper discontinuity means that for every compact \(K\subset\mathbb R^n\), only finitely many \(\gamma\in\Gamma\) satisfy \(\gamma K\cap K\ne\varnothing\). It is part of the hypothesis in the converse.

**Proof.** [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) supplies a connected simply connected smooth universal cover \(q:\widetilde M\to M\). Pull the connection back through its local inverse charts, or equivalently use [Linear connections B.2](linear-and-affine-connections.md#theorem-b-2) and the identification \(T\widetilde M\simeq q^*TM\) given by \(dq\). These local definitions agree by the chain rule. In coordinates coming from \(M\), the lifted coefficients are the original coefficients composed with \(q\), so curvature and torsion still vanish.

The lifted connection is geodesically complete. Given an initial vector upstairs, take the complete downstairs geodesic with its projected initial vector. Lift its restrictions to \([-j,j]\), \(j=1,2,\ldots\), with the prescribed value at time zero. [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) gives these lifts and makes them agree on overlaps, both for positive and negative times. In each inverse chart a lift satisfies the lifted geodesic equation. Their union is consequently a geodesic on all of \(\mathbb R\) with the required initial data.

[Flat connections E.1](flat-connections-and-infinitesimal-holonomy.md#theorem-e-1) and [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) give a global parallel frame \(E_1,\ldots,E_n\) on \(\widetilde M\). Define a smooth positive metric \(h\) by declaring this frame orthonormal at every point. If \(Y=\sum y_iE_i\) and \(Z=\sum z_iE_i\), parallelness gives
\[
Xh(Y,Z)=\sum_i\bigl(X(y_i)z_i+y_iX(z_i)\bigr)
=h(\nabla_XY,Z)+h(Y,\nabla_XZ).
\tag{G.5}
\]
Thus the lifted derivative is metric-compatible and torsion-free, so it is the Levi-Civita derivative of \(h\) by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). Its geodesic completeness makes \(h\) metrically complete by Hopf–Rinow B.2. The parallel frame also makes its full linear holonomy trivial: transport preserves every frame column along every path. [De Rham E.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-2) now gives a global isometry from Euclidean space onto \((\widetilde M,h)\). It preserves the connections by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). This proves the required affine identification, in every positive dimension; in dimension zero the connected manifold is a point.

Deck transformations preserve the lifted connection, because \(q\circ\gamma=q\) and its definition is local pullback through \(q\). In Euclidean coordinates, (G.3) makes each deck map \(x\mapsto A_\gamma x+b_\gamma\). The argument giving constant first derivatives applies on the connected space \(\mathbb R^n\), so this is a single affine map on the entire cover. Its inverse is a deck map, and \(A_\gamma\) is invertible.

The deck action is free and transitive on each fibre by [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2). To prove proper discontinuity, suppose that distinct deck maps \(\gamma_j\) have \(x_j,\gamma_jx_j\in K\) for some compact \(K\). Euclidean compactness in [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) gives subsequences with \(x_j\to x\) and \(\gamma_jx_j\to y\). Continuity and the Hausdorff property give \(q(x)=q(y)\). Take a connected evenly covered neighbourhood of that point and its sheets \(U_x,U_y\) through \(x,y\). Eventually \(x_j\in U_x\) and \(\gamma_jx_j\in U_y\). A deck transformation permutes the sheets, so \(\gamma_jU_x=U_y\). There is at most one such deck transformation: on \(U_x\) it must be \((q|_{U_y})^{-1}\circ q\), and uniqueness of path lifting in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) extends equality from one point to the connected cover. This contradicts distinctness. The fibre-orbit correspondence and inverse charts identify \(M\) affinely with (G.4).

For the converse, form the orbit space with its quotient topology. We give its manifold construction explicitly. The projection \(\pi\) is open because the saturation of an open set is the union of its translates. Choose a compact ball neighbourhood \(K\) of \(x\). Only finitely many group elements have \(\gamma K\cap K\ne\varnothing\). For each nonidentity one, freeness gives \(\gamma x\ne x\); disjoint neighbourhoods of these two points and continuity give an open neighbourhood of \(x\) disjoint from its translate. Intersect these finitely many neighbourhoods with the interior of \(K\). The resulting \(U\) has pairwise disjoint translates, since an intersection of two translates would give an intersection of \(U\) with a nonidentity translate. Consequently
\[
\pi^{-1}(\pi U)=\coprod_{\gamma\in\Gamma}\gamma U,
\tag{G.6}
\]
with each restriction of \(\pi\) a homeomorphism onto \(\pi U\).

For two distinct orbits choose compact neighbourhoods \(K_x,K_y\) of representatives. Proper discontinuity applied to \(K_x\cup K_y\) leaves only finitely many \(\gamma\) which could send \(K_x\) to meet \(K_y\). None sends \(x\) to \(y\). Shrink neighbourhoods of \(x,y\) to eliminate these finitely many intersections. Their images separate the two orbits, proving Hausdorffness. Images of a countable Euclidean basis form a countable basis of the quotient, by openness of \(\pi\). The charts (G.6) therefore give a Hausdorff second-countable smooth manifold. Their transitions locally come from a fixed \(\gamma\), so are affine by hypothesis. G.1's Hessian calculation makes the zero-coefficient connections agree on overlaps. They define an affine-flat quotient connection. Every initial vector downstairs lifts to a vector \((x,v)\) upstairs, and \(\pi(x+tv)\) is a geodesic defined for all real \(t\). Local uniqueness of the geodesic equation in [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) proves completeness. Connectedness follows by projecting Euclidean paths.

Finally choose \(x\in U\) in a covering chart as in (G.6), either for the universal cover or for the constructed quotient. If \(\gamma x\in U\), then \(U\cap\gamma U\ne\varnothing\), so \(\gamma=e\). Evaluation at \(x\) is continuous on \(\operatorname{Aff}(n,\mathbb R)\); the condition \(Ax+b\in U\) is an open neighbourhood of the identity meeting \(\Gamma\) only there. Left translation by any group element gives an isolating neighbourhood for every element of \(\Gamma\). This proves discreteness in the stated ambient topology. □

**Theorem G.3 (discrete translation groups).** A discrete additive subgroup \(L\subset\mathbb R^n\) has a basis over \(\mathbb Z\) consisting of real-linearly independent vectors \(v_1,\ldots,v_k\), where \(0\leq k\leq n\). Its translation action is free and properly discontinuous, and
\[
\mathbb R^n/L\ \simeq\ (S^1)^k\times\mathbb R^{\,n-k}
\tag{G.7}
\]
as smooth manifolds. The quotient is compact if and only if \(k=n\).

**Proof.** Discreteness at zero gives \(\varepsilon>0\) such that every nonzero \(v\in L\) has \(|v|\geq\varepsilon\). Applying this to differences makes distinct elements of \(L\) at least \(\varepsilon\) apart. Every bounded closed ball is compact by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and has a finite cover by balls of radius \(\varepsilon/3\). Each of these small balls contains at most one element of \(L\). Thus \(L\) meets every bounded set in finitely many points.

We prove the basis assertion by induction on \(n\). If \(L=0\), use the empty basis. Otherwise choose a nonzero \(w\in L\). There are finitely many nonzero elements with length at most \(|w|\), so one of them, \(v_1\), has the least positive length in \(L\). For any \(tv_1\in L\), subtract \(\lfloor t\rfloor v_1\); a nonzero remainder would have smaller positive length. Therefore
\[
L\cap\mathbb Rv_1=\mathbb Zv_1.
\tag{G.8}
\]

Let \(P\) be orthogonal projection onto \(v_1^\perp\). We claim \(P(L)\) is discrete. Write any \(\ell\in L\) as \(tv_1+P\ell\), and subtract an integer multiple of \(v_1\) so that \(0\leq t<1\). If \(|P\ell|\leq1\), the resulting representative belongs to the bounded cylinder
\[
C=\{sv_1+z\mid 0\leq s\leq1,\ z\perp v_1,\ |z|\leq1\}.
\]
The set \(L\cap C\) is finite. Among its nonzero projected lengths there is consequently a positive minimum if any occur. A smaller positive number, or \(1\) if none occur, isolates zero in \(P(L)\). As before, translation isolates every other point. This proves the claim.

Identify \(v_1^\perp\) with \(\mathbb R^{n-1}\) using an orthonormal basis, obtained by successively subtracting projections from an ordinary basis and normalizing the nonzero residual vectors. Apply the induction hypothesis to \(P(L)\). Lift its real-linearly independent integral basis to \(v_2,\ldots,v_k\in L\). Subtracting an integral combination of these lifts from any \(\ell\in L\) leaves an element of (G.8). Hence \(v_1,\ldots,v_k\) generate \(L\). A real relation among them projects to a relation among the chosen basis of \(P(L)\), forcing all coefficients except possibly the first to vanish; then the first also vanishes. This proves independence, uniqueness of the integral expression, and \(k\leq n\). For \(n=0\) the group is zero, supplying the induction's initial case.

Translations act freely. If \((K+\ell)\cap K\ne\varnothing\), then \(\ell\) is the difference of two points of the compact, hence bounded, set \(K\). Only finitely many \(\ell\in L\) have this bounded length, proving proper discontinuity. The quotient has the smooth structure of G.2.

Extend \(v_1,\ldots,v_k\) to a real basis by adjoining standard coordinate vectors which are not in the span so far. Each step raises its dimension, so this process terminates at a basis. The corresponding invertible linear map identifies \(L\) with \(\mathbb Z^k\times0\). In these coordinates consider
\[
(x_1,\ldots,x_n)\longmapsto
\bigl(e^{2\pi i x_1},\ldots,e^{2\pi i x_k},
x_{k+1},\ldots,x_n\bigr).
\tag{G.9}
\]
[Connections E.1](connections-and-parallel-transport.md#lemma-e-1) proves the period, surjectivity and local smooth circle charts of the exponential. Thus (G.9) is onto and has precisely \(\mathbb Z^k\times0\) as its fibre differences. Its local inverses are obtained by choosing a circle angle on each of the first \(k\) factors, leaving the remaining coordinates unchanged. These inverses and the quotient charts prove (G.7).

If \(k=n\), the compact cube \([0,1]^n\) maps onto the quotient by taking each coordinate modulo an integer; its continuous image is compact. If \(k<n\), (G.7) gives a continuous surjection of the quotient onto \(\mathbb R^{n-k}\). A compact domain would have compact image, whereas this Euclidean space is unbounded and thus not compact by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). This proves the last assertion, including the point quotient when \(n=0\). □

## H. Affine tori and rotational linear parts

**Example H.1 (a complete affine torus with shear).** Fix \(a\in\mathbb R\setminus\{0\}\). The affine transformations
\[
\gamma_{m,n}(x,y)=
\left(x+m+an y+\frac{an^2}{2},\,y+n\right),
\qquad (m,n)\in\mathbb Z^2,
\tag{H.1}
\]
form a free properly discontinuous group. Its quotient is a smooth two-torus with a complete affine-flat connection. This connection is not the Levi-Civita connection of any nondegenerate metric. The same torus nevertheless has a complete flat Riemannian metric.

**Proof.** Define a polynomial diffeomorphism and its inverse by
\[
F_a(u,v)=\left(u+\frac{av^2}{2},v\right),
\qquad
F_a^{-1}(x,y)=\left(x-\frac{ay^2}{2},y\right).
\tag{H.2}
\]
Let \(T_{m,n}(u,v)=(u+m,v+n)\). Substituting (H.2) gives
\(F_aT_{m,n}F_a^{-1}=\gamma_{m,n}\), including the term \(an^2/2\) in (H.1). Hence
\(\gamma_{m,n}\gamma_{r,s}=\gamma_{m+r,n+s}\), and distinct integer pairs give distinct maps. Freeness, proper discontinuity and compactness of the quotient follow from the translation action of \(\mathbb Z^2\) in G.3: a diffeomorphism carries compact sets to compact sets, so the finite-intersection condition is preserved by conjugation. The map \(F_a\) descends to a diffeomorphism of the ordinary torus with this quotient. Since the maps (H.1) are affine, G.2 makes the descended standard connection \(\overline\nabla^0\) affine-flat and geodesically complete.

Suppose a nondegenerate metric on the quotient had Levi-Civita derivative \(\overline\nabla^0\). Its pullback to \(\mathbb R^2\) would be a \(\nabla^0\)-parallel symmetric metric. Metric compatibility in the standard coordinate fields says that all partial derivatives of its coefficients vanish. Integration along segments gives a constant matrix
\[
B=\begin{pmatrix}b_{11}&b_{12}\\b_{12}&b_{22}\end{pmatrix}.
\]
Invariance under the deck transformation \(\gamma_{0,1}\) requires
\[
A^{\mathsf T}BA=B,\qquad
A=\begin{pmatrix}1&a\\0&1\end{pmatrix}.
\tag{H.3}
\]
The upper-right entry gives \(ab_{11}=0\); the lower-right entry then gives \(2ab_{12}=0\). Since \(a\ne0\), both \(b_{11}\) and \(b_{12}\) vanish. The vector \((1,0)\) is in the kernel of \(B\), contradicting nondegeneracy. This also excludes positive metrics.

There is a different invariant metric:
\[
h=(dx-ay\,dy)^2+dy^2.
\tag{H.4}
\]
It is positive definite because the displayed two one-forms form a coframe, and \(F_a^*h=du^2+dv^2\). Conjugacy with translations makes \(h\) invariant under every (H.1). Thus it descends to the quotient, where \(F_a\) induces an isometry from the standard flat torus. The standard torus is complete by G.2 and Hopf–Rinow B.2, since its standard connection is its Levi-Civita connection by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). Hence the descended metric is complete and flat.

For an explicit distinction between the two connections, the pushforwards by \(F_a\) of \(\partial_u,\partial_v\) are
\[
E_1=\partial_x,\qquad E_2=ay\,\partial_x+\partial_y.
\]
They are parallel for the Levi-Civita derivative of \(h\), by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Writing \(\partial_y=E_2-ayE_1\) and using the connection product rule gives
\[
\nabla^h_{\partial_y}\partial_y=-a\,\partial_x,\qquad
\nabla^h_{\partial_x}\partial_x
=\nabla^h_{\partial_x}\partial_y
=\nabla^h_{\partial_y}\partial_x=0.
\tag{H.5}
\]
The standard affine-flat derivative has all these coefficients zero. Both derivatives descend, but they are different. □

**Example H.2 (discrete motions with a dense linear image).** There is a free properly discontinuous cyclic group of Euclidean motions of \(\mathbb R^3\) whose linear parts form a dense proper subgroup of a circle of rotations. Its quotient is a complete flat manifold diffeomorphic to \(\mathbb R^2\times S^1\).

**Proof.** For \(t\in\mathbb R\), let \(R_t\) be the planar rotation corresponding to multiplication by \(e^{it}\) on \(\mathbb C=\mathbb R^2\). [Connections E.1](connections-and-parallel-transport.md#lemma-e-1) proves \(R_{s+t}=R_sR_t\), orthogonality and period \(2\pi\). Choose an irrational \(\alpha\), for example \(\sqrt2\). To verify this example is irrational, a hypothetical fraction \(p/q\) with \(q>0\) may be chosen with least denominator. From \(p^2=2q^2\), parity first makes \(p\) even and then \(q\) even; dividing both by two contradicts minimality. Here an odd integer has odd square by expansion of \((2j+1)^2\).

On \(\mathbb R^2\times\mathbb R\), put
\[
\gamma(v,z)=(R_{2\pi\alpha}v,z+1).
\tag{H.6}
\]
Induction and inversion give
\[
\gamma^k(v,z)=(R_{2\pi k\alpha}v,z+k)
\quad(k\in\mathbb Z).
\tag{H.7}
\]
No nonzero power fixes a point, because it changes the last coordinate. If \(K\) is compact, its last coordinates lie in an interval \([-B,B]\). An intersection \(\gamma^kK\cap K\ne\varnothing\) implies \(|k|\leq2B\). Only finitely many integers satisfy that inequality, proving proper discontinuity. G.2 gives a complete affine-flat quotient and ambient discreteness of the affine group \(\langle\gamma\rangle\). The transformations are Euclidean isometries, so the Euclidean metric descends. It has the descended standard connection as its Levi-Civita derivative by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1), and geodesic completeness gives metric completeness by Hopf–Rinow B.2.

The linear-part subgroup is
\[
\left\{\begin{pmatrix}R_{2\pi k\alpha}&0\\0&1\end{pmatrix}
\ \middle|\ k\in\mathbb Z\right\}.
\tag{H.8}
\]
The irrational-rotation argument proved in [Curvature D.4](curvature-and-holonomy-groups.md#example-d-4), using the full pigeonhole and uncountability proof in [Local tools 6.4](local-tools-for-bundles-and-transport.md#6-exercises-and-complete-solutions), says that these planar rotations are dense and form a countable proper subgroup of the full rotation circle. Thus taking linear parts has lost discreteness.

Finally consider
\[
(v,z)\longmapsto
\left(R_{-2\pi\alpha z}v,\,e^{2\pi i z}\right).
\tag{H.9}
\]
It is invariant under (H.7). If two images agree, equality of the circle coordinates gives \(z'=z+k\) for an integer \(k\), and equality of the first coordinates then gives \(v'=R_{2\pi\alpha k}v\). Thus its fibres are exactly the orbits. It is onto: for \((w,\zeta)\), choose a real lift \(z\) of the circle point \(\zeta\), and take \(v=R_{2\pi\alpha z}w\). In each circle angle chart this formula is smooth and inverse to the induced map on the quotient. Changing the angle lift changes \((v,z)\) by (H.7), so these local inverses agree there. This proves the stated diffeomorphism. □

## I. Small rotations and commuting motions

For a real or complex matrix \(T\), write
\(\|T\|=\sup_{|v|=1}|Tv|\). The norm estimates in [Local tools 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) give
\(\|ST\|\leq\|S\|\|T\|\). Multiplication on either side by an orthogonal or unitary matrix preserves this norm, since those matrices preserve vector lengths and map the unit sphere onto itself. We use
\([A,B]=ABA^{-1}B^{-1}\), and the same convention for transformations.

**Lemma I.1 (unitary eigenspaces and invariant subspaces).** A unitary operator on \(\mathbb C^n\) has an orthogonal decomposition into complex eigenspaces, and all its eigenvalues have modulus one. Every complex invariant subspace is the direct sum of its intersections with those eigenspaces.

**Proof.** First let \(H=H^*\) be Hermitian. On the unit sphere the real-valued function \(v\mapsto v^*Hv\) attains a maximum by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), applied to \(\mathbb C^n=\mathbb R^{2n}\). For a maximizing \(v\) and any \(w\) with \(v^*w=0\), differentiate this function on
\((v+tw)/|v+tw|\) at \(t=0\). The derivative is \(2\operatorname{Re}(w^*Hv)\), so it vanishes. Replacing \(w\) by \(iw\) also makes the imaginary part vanish. Hence \(Hv\) is orthogonal to the complex orthogonal complement of \(v\), and \(Hv=\lambda v\) with \(\lambda=v^*Hv\in\mathbb R\). The complex orthogonal complement is invariant, since
\(v^*Hw=(Hv)^*w=\lambda v^*w=0\). Induction on complex dimension gives an orthonormal eigenbasis for \(H\).

If two Hermitian operators \(H,K\) commute, each eigenspace of \(H\) is invariant under \(K\): from \(Hv=\lambda v\) one gets \(H(Kv)=K(Hv)=\lambda Kv\). The restriction of \(K\) remains Hermitian. Applying the preceding proof on each such subspace gives a common orthonormal eigenbasis.

Now let \(A\) be unitary and put
\[
H=\frac{A+A^*}{2},\qquad K=\frac{A-A^*}{2i}.
\tag{I.1}
\]
These operators are Hermitian. They commute because \(AA^*=A^*A=I\), and \(A=H+iK\). Their common eigenbasis is therefore an eigenbasis for \(A\). If \(Av=\lambda v\) and \(v\ne0\), preservation of its length gives \(|\lambda|=1\). Grouping the orthonormal basis by the distinct eigenvalues gives the claimed orthogonal splitting.

For a distinct eigenvalue \(\lambda\), the polynomial
\[
P_\lambda=
\prod_{\mu\ne\lambda}\frac{A-\mu I}{\lambda-\mu}
\tag{I.2}
\]
acts as the identity on the \(\lambda\)-eigenspace and as zero on every other eigenspace. Thus it is exactly the orthogonal projection to that eigenspace. If there is only one eigenvalue, the empty product is \(I\). An \(A\)-invariant complex subspace \(W\) is invariant under every polynomial in \(A\), so \(P_\lambda W\subset W\). Decomposing each \(w\in W\) as \(\sum_\lambda P_\lambda w\) proves the final assertion. Dimension zero has the empty decomposition. □

**Lemma I.2 (the small-rotation lemma).** Let \(A,B\) be unitary matrices. If \(\|B-I\|<1\) and \(A\) commutes with \([A,B]\), then \(A\) commutes with \(B\).

**Proof.** Put \(D=BA^{-1}B^{-1}\). Since \([A,B]=AD\), the equality \(A(AD)=(AD)A\) is equivalent, after multiplying by \(A^{-1}\) on the left, to \(AD=DA\).

Write \(\mathbb C^n=\bigoplus_\lambda V_\lambda\) for the eigenspaces of \(A\) from I.1. The eigenspace of \(D\) for the eigenvalue \(\lambda^{-1}\) is \(B(V_\lambda)\): substituting \(Bv\) verifies one inclusion, and applying \(B^{-1}\) verifies the other. Commutation of \(A,D\) makes each \(B(V_\lambda)\) invariant under \(A\). By I.1 it is the direct sum of its intersections with the \(V_\mu\).

For \(\mu\ne\lambda\), that intersection is zero. Otherwise a nonzero vector \(Bv\in V_\mu\), \(v\in V_\lambda\), is orthogonal to \(v\). Unitarity gives
\[
|(B-I)v|^2=|Bv|^2+|v|^2=2|v|^2,
\]
contradicting \(|(B-I)v|<|v|\). Therefore \(B(V_\lambda)\subset V_\lambda\), and equality follows from their equal finite dimensions. On this subspace \(A\) is the scalar \(\lambda I\), so it commutes with \(B\). The direct sum of these equalities proves the result. □

**Lemma I.3 (nearby rotations force commuting motions).** Let \(\Gamma\) be a discrete subgroup of the Euclidean motion group. If
\[
g(x)=Ax+p,\qquad h(x)=Bx+q,\qquad
\|A-I\|<\frac14,\quad \|B-I\|<\frac14,
\tag{I.3}
\]
with \(g,h\in\Gamma\), then \(gh=hg\), including their translation parts.

**Proof.** We first give the full contraction argument. Composition and inversion of motions satisfy
\[
(A,p)(C,u)=(AC,p+Au),\qquad
(A,p)^{-1}=(A^{-1},-A^{-1}p).
\]
Consequently
\[
[(A,p),(C,u)]
=\left([A,C],\
A(I-C)A^{-1}p+AC(I-A^{-1})C^{-1}u\right).
\tag{I.4}
\]
This follows by multiplying the four displayed pairs in order: the translation is
\(p+Au-ACA^{-1}p-ACA^{-1}C^{-1}u\), which is the expression in (I.4).

Set \(g_0=h\) and \(g_{k+1}=[g,g_k]\), and write \(g_k=(C_k,u_k)\). Since
\[
[A,C]-I=(AC-CA)A^{-1}C^{-1},\qquad
AC-CA=(A-I)(C-I)-(C-I)(A-I),
\]
orthogonality and the operator norm give
\[
\|C_{k+1}-I\|\leq2\|A-I\|\|C_k-I\|,
\qquad
|u_{k+1}|\leq\|C_k-I\||p|+\|A-I\||u_k|.
\tag{I.5}
\]
Put \(b=\|B-I\|\). Iteration yields
\[
\|C_k-I\|\leq 2^{-k}b,\qquad
|u_k|\leq4^{-k}|q|+4b|p|\bigl(2^{-k}-4^{-k}\bigr).
\tag{I.6}
\]
The second identity is an upper bound obtained from
\(\sum_{j=0}^{k-1}4^{-(k-1-j)}2^{-j}
=4(2^{-k}-4^{-k})\); multiplying out this finite geometric sum also verifies the case \(k=0\). Both bounds tend to zero. Thus \(g_k\to e\) in the Euclidean motion group. Discreteness means there is a neighbourhood of \(e\) meeting \(\Gamma\) only at \(e\), so \(g_k=e\) for all sufficiently large \(k\).

In particular \(C_k=I\) eventually. Apply I.2 backwards through
\(C_{j+1}=[A,C_j]\). If \(C_{j+1}=I\) and \(j\geq1\), then \(A\) commutes with
\(C_j=[A,C_{j-1}]\). The bound in (I.6) gives \(\|C_{j-1}-I\|<1\), so I.2 gives \(C_j=I\). Repetition proves \(C_1=[A,B]=I\). Real orthogonal matrices are being viewed here as unitary matrices on the complexification. Their operator norm is unchanged: for a real matrix \(T\),
\(|T(x+iy)|^2=|Tx|^2+|Ty|^2\), giving one inequality, and real vectors give the reverse inequality.

Now \(A,B\) commute. Formula (I.4) makes their motion commutator the translation
\[
[g,h](x)=x+t,\qquad t=(I-B)p+(A-I)q.
\tag{I.7}
\]
For a translation \(\tau_v(x)=x+v\), the same formula gives
\([g,\tau_v]=\tau_{(A-I)v}\). Starting with \(\tau_t\in\Gamma\), repeated commutators therefore give translations by \((A-I)^k t\). Their lengths tend to zero because \(\|A-I\|<1/4\). Discreteness makes one of these vectors zero.

For an orthogonal \(A\), put \(F=\ker(A-I)\). Its orthogonal complement is invariant under \(A-I\), because for \(v\perp F\) and \(f\in F\),
\(\langle(A-I)v,f\rangle=\langle v,(A^{-1}-I)f\rangle=0\).
The restriction of \(A-I\) to \(F^\perp\) has zero kernel and hence is invertible there. Decomposing \(t\) into \(F\oplus F^\perp\) shows that
\((A-I)^k t=0\) forces \(t\in F\). Thus \(At=t\). Repeating the commutator argument with \(h\) gives \(Bt=t\). Taking the inner product of (I.7) with \(t\) now gives
\[
|t|^2=\langle p,(I-B^{-1})t\rangle
      +\langle q,(A^{-1}-I)t\rangle=0.
\]
Hence \(t=0\), and the whole motion commutator is the identity. □

## J. Translation lattices in compact flat geometry

We give the Euclidean motion group the topology of
\(\mathrm O(n)\times\mathbb R^n\), writing a motion as \((A,p)\) for \(x\mapsto Ax+p\). The orthogonal group is compact: its defining equations \(A^{\mathsf T}A=I\) are closed conditions, each entry has absolute value at most one, and [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) applies to the matrix entries.

**Lemma J.1 (discreteness and compact orbit spaces).** Let \(\Gamma\) be a discrete group of Euclidean motions. Its action satisfies the compact-intersection properness condition of G.2. The following conditions are equivalent:

1. \(\mathbb R^n/\Gamma\), with the quotient topology, is compact.
2. There is a compact \(K\subset\mathbb R^n\) with \(\Gamma K=\mathbb R^n\).
3. For some \(R\geq0\), every \(x\in\mathbb R^n\) has \(|x-\gamma0|\leq R\) for at least one \(\gamma\in\Gamma\).

Every subgroup of finite index in such a cocompact \(\Gamma\) is also cocompact. These statements allow fixed points of the action.

**Proof.** For each \(B\geq0\), only finitely many elements \((A,p)\in\Gamma\) have \(|p|\leq B\). Otherwise compactness of
\(\mathrm O(n)\times\overline B(0,B)\) gives a convergent subsequence of distinct elements \(\gamma_j\). Continuity of multiplication and inversion, evident from the formulas in I.3, gives
\(\gamma_j^{-1}\gamma_{j+1}\to e\). These elements are nonidentity elements of \(\Gamma\), contradicting discreteness at \(e\).

If a compact \(K\) lies in \(\overline B(0,B)\) and \(\gamma K\cap K\ne\varnothing\), choose \(x,\gamma x\in K\). For \(\gamma=(A,p)\),
\[
|p|=|\gamma x-Ax|\leq2B.
\]
The preceding finiteness proves the required properness, without a freeness assumption.

The orbit projection \(\pi\) is open: the inverse image of \(\pi U\) is the union of the translates of \(U\), and hence is open when \(U\) is open. The sets \(\pi(B(x,1))\), for \(x\in\mathbb R^n\), cover the orbit space. If it is compact, finitely many suffice. The union of the corresponding closed unit balls is a compact \(K\) whose translates cover \(\mathbb R^n\). Thus 1 implies 2. Conversely \(\pi(K)\) is the whole quotient when 2 holds, and a continuous image of a compact space is compact.

If \(K\subset\overline B(0,R)\) satisfies 2 and \(x=\gamma y\), \(y\in K\), then
\[
|x-\gamma0|=|\gamma y-\gamma0|=|y|\leq R,
\]
giving 3. Conversely 3 puts \(\gamma^{-1}x\) in the compact ball
\(\overline B(0,R)\), so that ball satisfies 2.

Finally let \(H\leq\Gamma\) have finite index. Choose representatives for its finitely many right cosets, so \(\Gamma=\bigcup_{i=1}^m H\gamma_i\). If \(\Gamma K=\mathbb R^n\), then
\[
H\left(\bigcup_{i=1}^m\gamma_i K\right)=\mathbb R^n.
\]
The finite union in parentheses is compact. Applying the already proved equivalence to \(H\), which is discrete as a subgroup of \(\Gamma\), gives its cocompactness. □

**Theorem J.2 (a normal abelian subgroup of bounded index).** For each \(n\) there is a finite integer \(N(n)\) such that every discrete group \(\Gamma\) of Euclidean motions of \(\mathbb R^n\) has a normal abelian subgroup \(\Gamma_*\) of index at most \(N(n)\). One may take \(\Gamma_*\) to be the subgroup generated by
\[
S=\{(A,p)\in\Gamma\mid \|A-I\|<1/4\}.
\tag{J.1}
\]
It contains every translation in \(\Gamma\).

**Proof.** Every two elements of \(S\) commute by I.3. Finite products of such elements and their inverses therefore commute as well: move each factor past every factor of the other product, using the pairwise commutation and its inverse identities. Thus \(\Gamma_*\) is abelian. It contains all translations because their linear part is \(I\).

For \(\gamma=(Q,q)\in\Gamma\), the linear part of \(\gamma(A,p)\gamma^{-1}\) is \(QAQ^{-1}\). Orthogonality gives
\[
\|QAQ^{-1}-I\|=\|Q(A-I)Q^{-1}\|=\|A-I\|.
\]
Conjugation consequently preserves \(S\) and hence \(\Gamma_*\); applying the inverse conjugation gives equality. This proves normality.

Choose a finite cover of \(\mathrm O(n)\) by open operator-norm balls of radius \(1/12\), and let \(N(n)\) be the number of balls in that cover. Existence follows from the compactness noted above; the matrix-entry topology and operator-norm topology agree because
\(\max_{ij}|T_{ij}|\leq\|T\|\leq n\max_{ij}|T_{ij}|\), the latter bound following from the finite-sum Cauchy–Schwarz inequality in [Local tools 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Fix this cover once for the given dimension.

Suppose \(\gamma_1,\ldots,\gamma_{N(n)+1}\) represent different left cosets of \(\Gamma_*\), and write \(A_i\) for their linear parts. Two \(A_i,A_j\) lie in the same ball, by the finite pigeonhole principle. Therefore
\[
\|A_i^{-1}A_j-I\|=\|A_j-A_i\|<1/6<1/4.
\]
It follows that \(\gamma_i^{-1}\gamma_j\in S\subset\Gamma_*\), contrary to the cosets being different. Hence there are at most \(N(n)\) cosets. This proof uses only a finite compact cover and requires no measure or integration on \(\mathrm O(n)\). □

**Theorem J.3 (Bieberbach's first theorem and the torus cover).** Let \(\Gamma\) be a discrete group of Euclidean motions with compact quotient \(\mathbb R^n/\Gamma\), \(n\geq1\). Its translation subgroup \(\Lambda\) is a full-rank lattice, normal and of finite index. The linear-part image \(r(\Gamma)\subset\mathrm O(n)\) is finite and is isomorphic to \(\Gamma/\Lambda\).

If the action is free, the quotient is a compact flat Riemannian manifold and
\[
\mathbb R^n/\Lambda\longrightarrow\mathbb R^n/\Gamma
\tag{J.2}
\]
is a finite regular covering by a flat torus, with deck group \(\Gamma/\Lambda\). Conversely every connected compact flat Riemannian manifold arises in this way.

**Proof.** The normal abelian group \(H=\Gamma_*\) of J.2 has finite index in \(\Gamma\). By J.1 it is cocompact. We show that every element of a cocompact abelian group of Euclidean motions is a translation.

Suppose \(g=(A,p)\in H\), and put \(F=\ker(A-I)\). As in I.3, \(A-I\) restricts to an invertible map of \(F^\perp\) onto itself and vanishes on \(F\). Decompose \(p=p_F+p_\perp\), and choose \(d\in F^\perp\) with \((A-I)d=-p_\perp\). Conjugating the entire group by the coordinate change \(x\mapsto x-d\) replaces \(g\) by
\[
x\longmapsto Ax+p+(A-I)d=Ax+p_F.
\]
It preserves commutation, discreteness and cocompactness, because it is a Euclidean isometry. We may therefore assume \(p\in F\).

For any \(h=(B,q)\in H\), the equality \(gh=hg\) gives
\[
AB=BA,\qquad (A-I)q=(B-I)p.
\tag{J.3}
\]
The right side belongs to \(F\): since \(Ap=p\) and \(A,B\) commute,
\(A(B-I)p=(B-I)p\). The left side belongs to \(F^\perp\). Thus both sides are zero, and \(q\in F\). This holds for every \(h\in H\), so the orbit \(H0\) lies in \(F\). If \(A\ne I\), then \(F\) is a proper subspace. A unit vector \(v\perp F\) has distance at least \(t\) from \(F\) at the point \(tv\), for \(t\geq0\), because
\(|tv-f|^2=t^2+|f|^2\). This contradicts the uniform orbit-distance bound in J.1. Therefore \(A=I\). As \(g\) was arbitrary, every element of \(H\) is a translation.

Identify translation subgroups with their translation vectors. By G.3, the discrete additive group \(H\) has rank \(n\), since its quotient is compact. The full translation subgroup \(\Lambda\) contains \(H\) and is again discrete and additive. Applying G.3 to \(\Lambda\), its rank is at most \(n\); containment of the spanning lattice \(H\) makes it at least \(n\). Thus it is a full-rank lattice.

For \(\gamma=(A,p)\), direct composition gives
\[
\gamma\,\tau_v\,\gamma^{-1}=\tau_{Av},
\qquad \tau_v(x)=x+v.
\tag{J.4}
\]
This proves normality of \(\Lambda\). It has finite index because \(H\subset\Lambda\) already has finite index: mapping an \(H\)-coset to its containing \(\Lambda\)-coset is a surjection of coset sets. The homomorphism \(r(A,p)=A\) has kernel \(\Lambda\). Two elements have equal linear part exactly when they lie in the same \(\Lambda\)-coset, so it induces the claimed group isomorphism with its finite image.

Now assume the action is free. J.1 gives properness, and the quotient construction in G.2 gives a connected smooth manifold. The Euclidean metric agrees across its charts because the transitions are Euclidean motions. Its Levi-Civita derivative is the descended zero-coefficient connection by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1), so its curvature is zero. Compactness is the hypothesis. The subgroup \(\Lambda\) likewise gives the flat torus \(\mathbb R^n/\Lambda\), with its torus description and compactness proved in G.3.

To verify the covering assertion, choose a neighbourhood \(U\) in \(\mathbb R^n\) whose distinct \(\Gamma\)-translates are disjoint, as constructed in G.2. Their images in \(\mathbb R^n/\Lambda\) are disjoint or identical according to their \(\Lambda\)-cosets, and each maps diffeomorphically onto the image of \(U\) in \(\mathbb R^n/\Gamma\). There are exactly \([\Gamma:\Lambda]\) such sheets. This proves that (J.2) is a finite covering and a local isometry.

Normality makes \(\Gamma/\Lambda\) act on the torus by \([x]\mapsto[\gamma x]\). If \([\gamma x]=[x]\), there is an \(\ell\in\Lambda\) with \(\gamma x=\ell x\); freeness of \(\Gamma\) forces \(\ell^{-1}\gamma=e\). Thus the quotient group acts freely, and it is transitive on each fibre of (J.2) by the orbit description. These are deck transformations. Every deck transformation is determined by its value at one point, by the unique path lifting in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) and connectedness of the torus. Transitivity therefore shows that they are all the deck transformations. The covering is regular with the stated deck group.

Finally let \(M\) be connected, compact and flat Riemannian. Hopf–Rinow B.3 makes its Levi-Civita connection geodesically complete; it is torsion-free by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) and has zero curvature by flatness. Apply G.2. In that proof choose the initial parallel frame on the universal cover orthonormally for the lifted metric. Metric compatibility preserves all its pairings, so the auxiliary metric constructed there is exactly the lifted metric. The resulting identification of the universal cover with \(\mathbb R^n\) is consequently an isometry. Its deck group is free, properly discontinuous and affine by G.2, and it preserves this metric. In affine coordinates, metric preservation says \(A^{\mathsf T}A=I\); hence it is a discrete group of Euclidean motions. Its quotient is \(M\), which is compact. The first part of the theorem now supplies (J.2). This includes dimension one; dimension zero consists of a point with the trivial covering. □

## K. Affine rigidity of compact flat quotients

A discrete cocompact group of Euclidean motions is called a **crystallographic group**. We allow torsion in this definition. By J.3 its subgroup of translations is a full lattice of finite index. We first identify that subgroup using only the abstract group structure.

**Lemma K.1 (recognizing translations abstractly).** In a crystallographic group \(\Gamma\), the translation subgroup \(\Lambda\) consists exactly of the elements whose conjugacy classes in \(\Gamma\) are finite. Consequently every abstract isomorphism between crystallographic groups carries their translation subgroups onto one another.

**Proof.** Write \(\tau_v(x)=x+v\). For \(\gamma=(A,p)\), the formula (J.4) gives
\[
\gamma\tau_v\gamma^{-1}=\tau_{Av}.
\tag{K.1}
\]
The linear image \(r(\Gamma)\) is finite by J.3. Thus, for \(v\in\Lambda\), there are only finitely many possible conjugates \(\tau_{Av}\).

Conversely, suppose \(\gamma=(A,p)\) is not a translation, so \(A\ne I\). The vectors of \(\Lambda\) span \(\mathbb R^n\) by J.3 and G.3. If \((I-A)v\) vanished for every \(v\in\Lambda\), linearity would give \(I-A=0\) on their real span. Choose, therefore, \(v\in\Lambda\) with \((I-A)v\ne0\). Direct composition gives, for every integer \(k\),
\[
\tau_{kv}\gamma\tau_{-kv}
   =\bigl(A,p+k(I-A)v\bigr).
\tag{K.2}
\]
Distinct integers give distinct translation parts, and hence distinct conjugates. The conjugacy class of \(\gamma\) is infinite.

An isomorphism \(\phi:\Gamma_1\to\Gamma_2\) maps the conjugacy class of \(\gamma\) bijectively onto that of \(\phi(\gamma)\): apply \(\phi\) to \(h\gamma h^{-1}\), and use surjectivity for the reverse inclusion and injectivity for bijectivity. It therefore preserves precisely the elements just characterized. In dimension zero the group and its translation subgroup are both trivial, so the same conclusion holds. □

**Lemma K.2 (finite averaging).** Let \(F\) be a finite group, \(V\) a finite-dimensional real vector space, and \(\rho:F\to\operatorname{GL}(V)\) a representation. Suppose \(c:F\to V\) satisfies
\[
c(fg)=c(f)+\rho(f)c(g).
\tag{K.3}
\]
Then, with
\[
u=\frac1{|F|}\sum_{g\in F}c(g),
\]
one has \(c(f)=u-\rho(f)u\) for every \(f\). Thus the affine action \(x\mapsto\rho(f)x+c(f)\) fixes \(u\). Moreover \(V\) admits a positive-definite inner product invariant under \(\rho(F)\).

**Proof.** Summing (K.3) over \(g\), and using that \(g\mapsto fg\) permutes \(F\), gives
\[
|F|u=|F|c(f)+\rho(f)\sum_{g\in F}c(g).
\]
Division by the positive integer \(|F|\) proves the claimed formula. It immediately gives \(\rho(f)u+c(f)=u\).

Choose a real basis of \(V\) and let \(\langle\ ,\ \rangle\) be the sum-of-products inner product in that basis. Define
\[
B(v,w)=\frac1{|F|}\sum_{f\in F}
       \langle\rho(f)v,\rho(f)w\rangle.
\tag{K.4}
\]
Each summand is bilinear and symmetric, so \(B\) is as well. If \(v\ne0\), the term for the identity is \(\langle v,v\rangle>0\), while all other diagonal terms are nonnegative. Hence \(B(v,v)>0\). Finally, for \(h\in F\), right multiplication \(f\mapsto fh\) permutes the group, and
\[
B(\rho(h)v,\rho(h)w)
 =\frac1{|F|}\sum_{f\in F}
       \langle\rho(fh)v,\rho(fh)w\rangle
 =B(v,w).
\]
This proves invariance. Both assertions also hold for the zero vector space. □

**Theorem K.3 (affine rigidity).** Let \(\Gamma_i\) be crystallographic groups of Euclidean motions of \(\mathbb R^{n_i}\). Every abstract isomorphism \(\phi:\Gamma_1\to\Gamma_2\) is induced by an invertible affine map between the two Euclidean spaces:
\[
\phi(\gamma)=F\gamma F^{-1}
\qquad(\gamma\in\Gamma_1).
\tag{K.5}
\]
In particular \(n_1=n_2\). Consequently connected compact flat Riemannian manifolds with isomorphic fundamental groups are affinely diffeomorphic for their Levi-Civita connections. The abstract group does not, in general, determine their Riemannian metrics up to isometry.

**Proof.** Let \(\Lambda_i\) be the translation lattices. K.1 gives an isomorphism \(\phi:\Lambda_1\to\Lambda_2\). We use additive notation for their translation vectors. By G.3 and J.3, each \(\Lambda_i\) has a real-linearly independent integral basis of \(n_i\) vectors. Its quotient by \(2\Lambda_i\) has exactly \(2^{n_i}\) elements: each integral coefficient has a unique residue zero or one, independently of the others. The isomorphism carries \(2\Lambda_1\) onto \(2\Lambda_2\), so these finite quotients have the same cardinality. Thus \(n_1=n_2=n\). For \(n=0\), the unique map of the point spaces proves the assertion. Assume now \(n>0\).

Choose an integral basis \(v_1,\ldots,v_n\) of \(\Lambda_1\). Their images \(w_1,\ldots,w_n\) under \(\phi\) form an integral basis of \(\Lambda_2\): generation and absence of integral relations follow by applying \(\phi\) and \(\phi^{-1}\). They span \(\mathbb R^n\), because they generate its full translation lattice. A spanning list of \(n\) vectors in an \(n\)-dimensional space is a real basis, as elimination of a dependent vector would otherwise give a spanning list of fewer than \(n\) vectors. There is consequently an invertible real-linear map \(S\) with \(Sv_i=w_i\), and
\[
\phi(\tau_v)=\tau_{Sv}\qquad(v\in\Lambda_1).
\tag{K.6}
\]

For \(\gamma=(A_\gamma,p_\gamma)\), write
\(\phi(\gamma)=(B_\gamma,q_\gamma)\). Apply \(\phi\) to (K.1) and use (K.6). This gives
\[
S A_\gamma v=B_\gamma Sv
\qquad(v\in\Lambda_1).
\]
Since \(\Lambda_1\) spans, the equality holds for every real vector. Therefore
\(B_\gamma=SA_\gamma S^{-1}\). Conjugating the second representation by \(S^{-1}\), set
\[
\Psi(\gamma)=S^{-1}\phi(\gamma)S
       =(A_\gamma,r_\gamma),\qquad
r_\gamma=S^{-1}q_\gamma.
\]
The homomorphism \(\Psi\) fixes every translation \(\tau_v\) in \(\Lambda_1\).

Define \(\delta(\gamma)=r_\gamma-p_\gamma\). The product formula for affine maps gives
\[
\delta(\gamma\eta)
 =\delta(\gamma)+A_\gamma\delta(\eta),
 \qquad \delta(\tau_v)=0.
\tag{K.7}
\]
In particular \(\delta(\tau_v\gamma)=\delta(\gamma)\). Since \(\Lambda_1\) is normal, this makes \(\delta\) well-defined on the finite quotient
\(H=\Gamma_1/\Lambda_1\), as is the linear representation \([\gamma]\mapsto A_\gamma\). Finiteness and normality were proved in J.3. The formula (K.7) becomes exactly (K.3) on \(H\). K.2 supplies a vector \(u\) with
\[
\delta(\gamma)=u-A_\gamma u.
\]
A direct conjugation now yields
\[
\tau_u\gamma\tau_{-u}
   =(A_\gamma,p_\gamma+u-A_\gamma u)
   =\Psi(\gamma).
\]
Thus
\[
F=S\tau_u,\qquad F(x)=Sx+Su
\tag{K.8}
\]
satisfies (K.5), including its prescribed isomorphism. This proves the group assertion even when the actions have fixed points.

For a connected compact flat Riemannian manifold, J.3 identifies the universal Riemannian cover with Euclidean space and the deck group with a freely acting crystallographic group. [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) identifies this deck group with the fundamental group. Given an isomorphism of two such groups, (K.8) induces
\[
\overline F:\mathbb R^n/\Gamma_1\longrightarrow
               \mathbb R^n/\Gamma_2,\qquad
[x]\longmapsto[F(x)].
\]
Equation (K.5) proves well-definedness; \(F^{-1}\) induces its inverse. In the covering charts of G.2, these maps are restrictions of \(F\) and \(F^{-1}\), so they are smooth. G.1 proves that an invertible affine map preserves the standard connection. The descended maps therefore preserve the quotient Levi-Civita connections, proving affine equivalence.

Conversely let \(f:M_1\to M_2\) be an affine diffeomorphism of these quotients. If \(q_i:\mathbb R^n\to M_i\) are their universal covers, both \(f\circ q_1\) and \(q_2\) are simply connected covers of \(M_2\). Their fundamental-group image subgroups are trivial. [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) therefore identifies these two based covers, giving a lift \(F\) with \(q_2F=fq_1\). Equivalently choose lifts of \(f\) and its inverse with matching base points; their compositions lift the identity and fix the chosen points, so uniqueness of path lifting in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) makes both compositions the identity. The lift is smooth in covering charts and preserves the lifted connections. The Hessian calculation in G.1 on connected \(\mathbb R^n\) makes it a single invertible affine map. Conjugating by that lift maps deck transformations to deck transformations, because the quotient maps commute with it; using its inverse proves bijectivity. Thus affine equivalence also gives an isomorphism of the groups.

To distinguish affine equivalence from isometry explicitly, let
\[
C_a=\mathbb R/a\mathbb Z,\qquad a>0,
\]
with its quotient Euclidean metric. G.3 gives a compact smooth circle, and G.2 gives the connection induced by the standard derivative. The map \(x\mapsto(b/a)x\) descends to an affine diffeomorphism \(C_a\to C_b\). Each circle's deck group is the infinite cyclic group.

For representatives \(x,y\in\mathbb R\), their distance in \(C_a\) is
\[
d_a([x],[y])=\min_{k\in\mathbb Z}|y-x+ka|.
\tag{K.9}
\]
Indeed a piecewise smooth path from \([x]\) to \([y]\) lifts, starting at \(x\), to a path ending at \(y+ka\) for some integer \(k\), by [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). The lift is piecewise smooth in inverse covering charts and has the same length, since those charts are local isometries. Its Euclidean length is at least its endpoint displacement: integrate its derivative, and apply the triangle inequality for integrals proved in [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) on each smooth piece. This gives the lower bound in (K.9). Conversely each straight segment from \(x\) to \(y+ka\) projects to a path with that length. The minimum exists, since \(|y-x+ka|\) tends to infinity as \(|k|\) does, leaving finitely many candidates below any fixed candidate value.

Subtracting an integer multiple of \(a\) from \(y-x\) places it in \([-a/2,a/2]\): take the integer part of \((y-x)/a+1/2\). Thus every distance is at most \(a/2\), and the pair \([0],[a/2]\) has distance exactly \(a/2\). The diameter of \(C_a\) is \(a/2\). A Riemannian isometry preserves lengths of curves and hence distances and diameter. Therefore \(C_a\) and \(C_b\) are not isometric when \(a\ne b\), despite their affine equivalence and isomorphic fundamental groups. □

## L. When an affine-flat connection comes from a metric

A **parallel Riemannian metric** for a connection \(\nabla\) is a smooth positive-definite symmetric two-tensor \(g\) with \(\nabla g=0\). For a torsion-free connection this is equivalent to saying that \(\nabla\) is the Levi-Civita connection of \(g\), by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). On a Euclidean torus \(\mathbb R^n/\Lambda\), the standard derivative has the parallel metric descended from the ordinary inner product. A covering map below is surjective.

**Lemma L.1 (descending a parallel metric through a finite cover).** Let \(p:N\to M\) be a smooth covering of connected manifolds, preserving their connections. If the covering has finitely many sheets and \(N\) has a parallel Riemannian metric \(h\), then \(M\) has a parallel Riemannian metric for its connection. Regularity of the covering is not required. Furthermore any covering with compact total space and Hausdorff base has finite fibres; if its base is connected, its number of sheets is a single finite positive integer.

**Proof.** On an evenly covered open set, inverse branches of \(p\) are in bijection with the fibre over any one point. Hence the fibre cardinality is locally constant. On a connected base a locally constant finite cardinality is constant: each set on which it has a chosen value and its complement are open. Write this value as \(m\geq1\).

For \(y\in M\) and \(v,w\in T_yM\), define
\[
g_y(v,w)=\frac1m\sum_{x\in p^{-1}(y)}
 h_x\bigl((dp_x)^{-1}v,(dp_x)^{-1}w\bigr).
\tag{L.1}
\]
Each \(dp_x\) is invertible, since \(p\) is a local diffeomorphism. On an evenly covered neighbourhood \(U\), with its \(m\) smooth inverse branches \(s_j:U\to N\), the formula reads
\[
g|_U=\frac1m\sum_{j=1}^m s_j^*h.
\tag{L.2}
\]
It is smooth, symmetric and bilinear. For \(v\ne0\), every \((dp_x)^{-1}v\) is nonzero, so every summand of \(g_y(v,v)\) is positive. Thus \(g\) is positive-definite. Changing the labelling of the branches only permutes the finite sum, and (L.1) makes agreement on all overlaps explicit.

Let \(\nabla\) be the connection on \(M\), and \(\nabla^N\) the one on \(N\). On a branch \(s=s_j\), write \(s_*X,s_*Y,s_*Z\) for the pushed-forward local fields. The hypothesis that \(p\) preserves connections, applied to its local inverse, gives
\[
\nabla^N_{s_*X}(s_*Y)=s_*(\nabla_XY).
\tag{L.3}
\]
This is also the pullback connection formula of [Linear connections B.2](linear-and-affine-connections.md#theorem-b-2). Since \(h\) is parallel, the tensor derivative formula of [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) gives
\[
\begin{aligned}
X\bigl((s^*h)(Y,Z)\bigr)
 &=\bigl((s_*X)h(s_*Y,s_*Z)\bigr)\circ s\\
 &=(s^*h)(\nabla_XY,Z)
   +(s^*h)(Y,\nabla_XZ).
\end{aligned}
\]
Sum over \(s_1,\ldots,s_m\) and divide by \(m\). The resulting equality is exactly \(\nabla g=0\). If \(\nabla\) is torsion-free, [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) then identifies it as the Levi-Civita connection of \(g\). Notice that no transitive action of deck transformations on the fibre was used.

Finally suppose merely that \(N\) is compact and the base is Hausdorff. For each \(y\), the singleton \(\{y\}\) is closed, so \(p^{-1}(y)\) is a closed subset of a compact space and is compact. It is discrete in its subspace topology: each sheet over an evenly covered neighbourhood meets this fibre in a singleton. A compact discrete space is finite, since its cover by all singleton open sets has a finite subcover. Surjectivity makes the fibres nonempty. If the base is connected, local constancy as above makes their finite cardinality a fixed positive integer. □

**Theorem L.2 (the torus-cover and metric criterion).** Let \(M\) be a connected geodesically complete affine-flat manifold. The following are equivalent:

1. A Euclidean torus \(\mathbb R^n/\Lambda\), with its standard flat connection, covers \(M\) by a connection-preserving map.
2. \(M\) is compact and its given connection is the Levi-Civita connection of a Riemannian metric.
3. In the affine universal-cover representation \(M=\mathbb R^n/\Gamma\) of G.2, the quotient is compact and the image of the linear-part homomorphism \(\Gamma\to\operatorname{GL}(n,\mathbb R)\) is finite.

Here \(\Lambda\) is a full lattice. Any covering in item 1 necessarily has finite degree. When these conditions hold, there is also a finite regular covering as in item 1 which is a local isometry for the metric in item 2. Finiteness of the linear image in item 3 does not depend on the choice of affine coordinates on the universal cover.

**Proof.** Suppose item 1 holds. The torus is compact by G.3, and a continuous image of a compact space is compact. Hence \(M\) is compact. Its Hausdorff property and L.1 show that this covering has finite degree, even though finiteness was not part of item 1. The Euclidean metric on the torus is parallel for its standard connection. Applying L.1 gives a parallel Riemannian metric on \(M\) for its given connection. This connection has zero torsion by affine-flatness, so [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) makes it the Levi-Civita connection. Thus 1 implies 2.

Suppose item 2 holds, with metric \(g\). Its curvature is zero because its Levi-Civita connection is the given affine-flat connection. The compact-flat assertion in J.3 supplies a finite regular local-isometry covering
\[
\mathbb R^n/\Lambda\longrightarrow (M,g)
\tag{L.4}
\]
by a full translation lattice \(\Lambda\). [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) proves that local isometries preserve Levi-Civita connections. The domain connection is the standard one in its Euclidean charts, so (L.4) has the connection-preserving property of item 1. This proves 2 implies 1 and the additional regular local-isometry assertion.

For 2 implies 3, use the metric choice in the final paragraph of J.3: an orthonormal parallel frame identifies the universal cover isometrically with Euclidean space. The deck group then consists of Euclidean motions, is discrete and has compact quotient. J.3 makes its linear image finite.

To verify that this conclusion is independent of the affine identification, let \(u_1,u_2:\mathbb R^n\to\widetilde M\) be two affine identifications of the universal cover with its lifted connection. The map \(u_2^{-1}u_1\) is a connection-preserving diffeomorphism of standard affine space. G.1, applied on connected \(\mathbb R^n\), gives
\[
u_2^{-1}u_1(x)=Sx+t
\]
with \(S\) invertible. Conjugation by this map changes every deck transformation's linear part \(A\) to \(SAS^{-1}\). Conjugation is a bijection of the two linear images, and so preserves their finiteness. This proves item 3 for any affine identification.

Finally assume item 3, and write the finite linear image as \(F\). Apply the inner-product assertion of K.2 to its defining representation on \(\mathbb R^n\). It gives a positive-definite inner product \(B\) invariant under all \(A\in F\). Give \(\mathbb R^n\) the constant metric
\[
h_x(v,w)=B(v,w).
\]
For a deck transformation \(\gamma(x)=A_\gamma x+b_\gamma\), its derivative is \(A_\gamma\). Consequently
\[
(\gamma^*h)_x(v,w)
   =B(A_\gamma v,A_\gamma w)=B(v,w)=h_x(v,w).
\tag{L.5}
\]
The metric descends to \(M\). More explicitly, in each inverse chart of the quotient covering of G.2, use the pullback of \(h\). Two inverse charts differ locally by a deck transformation, so (L.5) proves equality on their overlaps. The resulting tensor \(g\) is smooth and positive-definite.

In the affine charts its coefficients are constant and the connection coefficients vanish. The tensor derivative formula of [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) therefore gives \(\nabla g=0\). The given connection has zero torsion, so [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) identifies it as the Levi-Civita connection of \(g\). Compactness is already part of item 3, giving item 2. The proof also covers dimension zero: all spaces and groups involved are a point and the trivial group.

The compactness and metric conditions both concern the specified affine connection and its quotient. In particular H.1's complete affine torus with shear is topologically a torus but has infinite linear image and no parallel positive metric, as proved there. Thus its topology alone does not give the connection-preserving torus cover of item 1. □

## M. Abstract deck groups and finite extensions

Let \(F\) be a finite group with identity \(e\), let \(L\) be a free abelian group of rank \(n\), and fix a homomorphism
\(\rho:F\to\operatorname{Aut}(L)\). We write \(L\) additively. An **extension with action \(\rho\)** is an exact sequence
\[
1\longrightarrow L\xrightarrow{\ i\ }G
 \xrightarrow{\ \pi\ }F\longrightarrow1
\tag{M.1}
\]
such that conjugation by any lift of \(f\in F\) acts on \(i(L)\) as \(\rho(f)\). This action does not depend on the lift: two lifts differ by an element of the abelian kernel, whose conjugation on that kernel is the identity. Conjugation by a product proves that the resulting action is a homomorphism. Two extensions are **equivalent** if there is a group isomorphism between their middle groups commuting with the specified inclusions of \(L\) and projections onto \(F\). Thus the kernel and quotient identifications are part of the data.

**Lemma M.1 (factor sets and extension equivalence).** Extensions (M.1) with action \(\rho\) are classified, up to this equivalence, by functions \(c:F\times F\to L\) satisfying
\[
\begin{aligned}
c(e,f)&=c(f,e)=0,\\
c(f,g)+c(fg,h)&=\rho(f)c(g,h)+c(f,gh).
\end{aligned}
\tag{M.2}
\]
Two such functions \(c,c'\) give equivalent extensions precisely when
\[
c'(f,g)-c(f,g)
 =a(f)+\rho(f)a(g)-a(fg)
\tag{M.3}
\]
for some function \(a:F\to L\) with \(a(e)=0\).

**Proof.** Choose one lift \(s(f)\in G\) of each \(f\), taking \(s(e)=1\). There is a unique \(c(f,g)\in L\) with
\[
s(f)s(g)=i(c(f,g))s(fg),
\]
because both sides project to \(fg\) and \(i\) identifies \(L\) with the kernel. Each element of \(G\) has a unique form \(i(\ell)s(f)\): its projection determines \(f\), and then multiplication by \(s(f)^{-1}\) determines \(\ell\). In these coordinates multiplication is
\[
(\ell,f)(\ell',g)
 =\bigl(\ell+\rho(f)\ell'+c(f,g),\,fg\bigr).
\tag{M.4}
\]
The choice \(s(e)=1\) gives the first line of (M.2). Comparing \((s(f)s(g))s(h)\) and \(s(f)(s(g)s(h))\), and moving kernel elements past \(s(f)\) by conjugation, gives the second line.

Conversely, start with a function \(c\) satisfying (M.2) and use (M.4) on the set \(L\times F\). The two ways to multiply \((\ell,f),(\ell',g),(\ell'',h)\) have second component \(fgh\); their first components are respectively
\[
\begin{aligned}
&\ell+\rho(f)\ell'+\rho(fg)\ell''
       +c(f,g)+c(fg,h),\\
&\ell+\rho(f)\ell'+\rho(f)\rho(g)\ell''
       +\rho(f)c(g,h)+c(f,gh).
\end{aligned}
\]
They are equal by (M.2) and the homomorphism property of \(\rho\). Thus the operation is associative. Normalization gives the two-sided identity \((0,e)\). A two-sided inverse of \((\ell,f)\) is
\[
\left(-\rho(f^{-1})\bigl(\ell+c(f,f^{-1})\bigr),\,f^{-1}\right).
\tag{M.5}
\]
The right product is immediately \((0,e)\). For the left product, apply (M.2) to \((f^{-1},f,f^{-1})\), obtaining
\(c(f^{-1},f)=\rho(f^{-1})c(f,f^{-1})\); substitution gives \((0,e)\) again. We have therefore constructed a group \(G_c\).

The maps \(\ell\mapsto(\ell,e)\) and \((\ell,f)\mapsto f\) give the exact sequence (M.1). Indeed the first is an injective homomorphism, the second a surjective homomorphism, and its kernel is exactly \(L\times\{e\}\). Finally,
\[
(0,f)(\ell,e)=(\rho(f)\ell,f)
             =(\rho(f)\ell,e)(0,f),
\]
so the induced action is \(\rho\). The section \(f\mapsto(0,f)\) has factor set \(c\). The coordinate map \(i(\ell)s(f)\leftrightarrow(\ell,f)\) proves that this construction recovers the original extension.

If \(s'(f)=i(a(f))s(f)\), with \(a(e)=0\), substitution in the product defining the factor set gives (M.3). Conversely suppose (M.3) holds. The map
\[
G_c\longrightarrow G_{c'},\qquad
(\ell,f)\longmapsto(\ell-a(f),f)
\tag{M.6}
\]
is a bijection. To check that it is a homomorphism, its value on the product (M.4) has first component
\(\ell+\rho(f)\ell'+c(f,g)-a(fg)\). The product of the two images in \(G_{c'}\) has first component
\[
\ell-a(f)+\rho(f)(\ell'-a(g))+c'(f,g),
\]
which is the same by (M.3). Formula (M.6) fixes the kernel and quotient.

For the remaining direction, any equivalence \(\Phi:G_c\to G_{c'}\) must send \((0,f)\) to \((b(f),f)\) for some \(b(e)=0\), and must send \((\ell,f)\) to \((\ell+b(f),f)\) because it fixes the kernel. Apply its homomorphism identity to \((0,f)(0,g)\). It gives
\[
c(f,g)+b(fg)
 =b(f)+\rho(f)b(g)+c'(f,g).
\]
Taking \(a=-b\) proves (M.3). Thus no further equivalence classes are identified or omitted. □

**Lemma M.2 (averaging a factor set).** Put \(m=|F|\), identify \(L\) with \(\mathbb Z^n\) by a basis, and extend \(\rho\) linearly to \(V=\mathbb R^n\). For a function \(c\) satisfying (M.2), define
\[
B(f)=\sum_{h\in F}c(f,h)\in L,\qquad
b(f)=\frac{B(f)}m\in V.
\tag{M.7}
\]
Then \(B(e)=b(e)=0\), and
\[
\begin{aligned}
m\,c(f,g)&=B(f)+\rho(f)B(g)-B(fg),\\
c(f,g)&=b(f)+\rho(f)b(g)-b(fg).
\end{aligned}
\tag{M.8}
\]
In particular \(b(f)\in m^{-1}L\).

**Proof.** Normalization in (M.2) makes \(B(e)=0\). Sum its second identity over \(h\in F\). Since \(h\mapsto gh\) permutes \(F\), the result is
\[
m\,c(f,g)+B(fg)=\rho(f)B(g)+B(f).
\]
Rearranging gives the first formula in (M.8). Division by the positive integer \(m\) in the real vector space gives the second. Each \(B(f)\) is a sum of lattice vectors, proving the denominator assertion. The linear extension of \(\rho(f)\) is invertible because \(\rho(f^{-1})\) extends its inverse on the chosen basis, and the group identities extend from that basis to all vectors. Thus all terms in (M.8) are defined on \(V\). □

**Theorem M.3 (realizing an extension by Euclidean motions).** If \(\rho\) is faithful, every extension (M.1) is isomorphic to a crystallographic group on an \(n\)-dimensional Euclidean space. The specified subgroup \(L\) becomes its full translation subgroup, and its linear image is \(\rho(F)\), in suitable linear coordinates.

**Proof.** By M.1 it suffices to realize \(G_c\). With \(b\) from M.2, define an affine map for each \((\ell,f)\in G_c\) by
\[
T_{\ell,f}(x)=\rho(f)x+\ell+b(f).
\tag{M.9}
\]
Composition has linear part \(\rho(fg)\) and translation part
\[
\ell+\rho(f)\ell'+b(f)+\rho(f)b(g)
 =\ell+\rho(f)\ell'+c(f,g)+b(fg).
\]
By (M.4) and (M.8), this is exactly the map assigned to the product in \(G_c\). Hence (M.9) is a homomorphism into the affine group.

If \(T_{\ell,f}\) is the identity, its linear part is the identity. Faithfulness gives \(f=e\), and then \(b(e)=0\) gives \(\ell=0\). Thus the homomorphism is injective. For the same reason the image elements with identity linear part are exactly
\(T_{\ell,e}(x)=x+\ell\). Its full translation subgroup is the specified copy of \(L\).

K.2 gives a positive-definite inner product \(Q\) on \(V\) invariant under \(\rho(F)\). Each map (M.9) preserves the constant metric defined by \(Q\): its derivative is \(\rho(f)\), so the two tangent-vector pairings agree. Choose a \(Q\)-orthonormal basis, successively subtracting projections onto the previously chosen unit vectors and dividing each nonzero remainder by its \(Q\)-length. Starting from a basis makes each remainder nonzero; at each step the construction gives a unit vector orthogonal to the preceding ones, and their spans agree with the corresponding initial spans. These coordinates identify \(Q\) with the usual Euclidean inner product. The image of (M.9) consequently consists of Euclidean motions.

We check discreteness and cocompactness. Before the orthonormal coordinate change, the possible translation parts are the finite union
\[
\bigcup_{f\in F}\bigl(L+b(f)\bigr).
\tag{M.10}
\]
The standard integer lattice meets every bounded set in finitely many points, either by boundedness of each integer coordinate or by G.3. For each fixed \(f\), a bounded set of translation parts therefore gives only finitely many \(\ell\). There are only finitely many \(f\), so any bounded set of translation parts contains only finitely many image elements. In a bounded neighbourhood of the identity, exclude the finitely many other elements by disjoint smaller coordinate neighbourhoods; this isolates the identity. Group translation isolates each other element. An invertible linear coordinate change is a homeomorphism of the affine group, by its matrix multiplication and inverse formulas, so discreteness persists in the Euclidean coordinates.

The translations by \(L\) already cover \(V\) by translates of the compact parallelepiped
\[
P=\left\{\sum_{j=1}^n t_jv_j\ \middle|\ 0\leq t_j\leq1\right\},
\]
where \(v_j\) is the chosen integral basis: subtract the integer part of each coefficient. Compactness follows from that of \([0,1]^n\) and continuity of its linear image, as in G.3. Hence the full image group also has a compact set whose translates cover \(V\). J.1 proves compactness of its orbit space and proper discontinuity. This establishes every crystallographic assertion, without requiring the action to be free. If \(n=0\), faithfulness forces \(F\) to be trivial, and the construction is the trivial group acting on a point. □

**Theorem M.4 (the abstract compact-flat deck-group criterion).** An abstract group \(G\) is isomorphic to the deck group of the universal cover of a connected compact flat Riemannian \(n\)-manifold if and only if:

1. \(G\) is torsion-free;
2. \(G\) has a normal subgroup \(L\cong\mathbb Z^n\) of finite index which is maximal abelian.

Here maximal abelian means that no strictly larger abelian subgroup of \(G\) contains \(L\). It is not an assertion only about normal abelian subgroups.

**Proof.** Suppose first that \(G\) is such a deck group. J.3 identifies the universal cover isometrically with Euclidean space and \(G\) with a freely acting crystallographic group. Its translation subgroup \(L\) is normal, has finite index and is a full lattice of rank \(n\).

If a motion \(\gamma=(A,p)\) commutes with every \(\tau_v\), \(v\in L\), then (K.1) gives \(Av=v\) for every such \(v\). The lattice spans the space, so \(A=I\) and \(\gamma\) itself belongs to \(L\). Any abelian subgroup containing \(L\) consists of motions commuting with \(L\), and is therefore \(L\). This proves maximality.

A finite-order affine motion has a fixed point. Indeed its finitely many powers form a finite group acting affinely, and the translations of these powers satisfy (K.3) by the affine multiplication rule. K.2 supplies a common fixed point. Since the deck action is free, its only finite-order element is the identity. This proves torsion-freeness.

Conversely suppose the two conditions hold. Form \(F=G/L\), a finite group, and let \(\rho\) be its action on \(L\) by conjugation. This action is well-defined as explained after (M.1). If \(\rho(f)\) is the identity and \(g\) is any lift of \(f\), then \(g\) commutes with all of \(L\). The subgroup generated by \(g\) and \(L\) is abelian: its elements have the form \(\ell g^k\), and these commute because \(L\) is abelian and \(g\) commutes with it. Maximality forces \(g\in L\), so \(f=e\). Thus \(\rho\) is faithful.

M.3 now realizes \(G\) as a discrete cocompact Euclidean motion group \(\Gamma\). Its action is free. To see this, if \(\gamma\) fixes \(x\), then all powers of \(\gamma\) lie in the stabilizer of \(x\). J.1's compact-intersection assertion applied to the compact singleton \(\{x\}\) makes this stabilizer finite. Two nonnegative powers must coincide, giving a positive power equal to the identity. Torsion-freeness gives \(\gamma=e\).

The free quotient assertion in J.3 makes \(M=\mathbb R^n/\Gamma\) a connected compact flat Riemannian manifold. Its quotient map is a smooth covering by G.2. Euclidean space is simply connected: a loop based at \(x\) contracts with fixed endpoints by the formula \(x+(1-s)(\alpha(t)-x)\). Thus this is a universal cover. The transformations in \(\Gamma\) are deck transformations and act transitively on every fibre. Every deck transformation is determined by the image of one point by [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). Choosing the element of \(\Gamma\) with that same image proves that \(\Gamma\) is the full deck group. This realizes \(G\) as required. For dimension zero, a torsion-free finite group is trivial, and the manifold is a point; the argument includes this case. □

**Theorem M.5 (finitely many extensions for a fixed action).** For the fixed \(F,L,\rho\) above, only finitely many equivalence classes of extensions (M.1) induce \(\rho\). If \(m=|F|\) and \(L\) has rank \(n\), their number is at most
\[
m^{\,n(m-1)^2}.
\tag{M.11}
\]
No faithfulness or torsion-freeness hypothesis is needed for this assertion.

**Proof.** Let \(Z\) be the additive group of all functions satisfying (M.2). Addition and subtraction preserve both normalization and the cocycle identity, so this is a subgroup of the group of all normalized functions \(F\times F\to L\). After choosing a basis of \(L\), a normalized function is determined by its \(n\) integral coordinates on each of the \((m-1)^2\) pairs with neither entry equal to \(e\). Thus that ambient group is \(\mathbb Z^N\), where \(N=n(m-1)^2\).

For \(a:F\to L\) with \(a(e)=0\), put
\[
(da)(f,g)=a(f)+\rho(f)a(g)-a(fg).
\]
This function is normalized. Its cocycle identity follows by expanding both sides: both
\((da)(f,g)+(da)(fg,h)\) and
\(\rho(f)(da)(g,h)+(da)(f,gh)\) reduce to
\[
a(f)+\rho(f)a(g)+\rho(fg)a(h)-a(fgh).
\]
Consequently all such functions form a subgroup \(D\subset Z\); closure follows also from \(d(a+a')=da+da'\). M.1 identifies the extension classes exactly with the quotient group \(Z/D\).

For each \(c\in Z\), M.2 supplies the normalized integral function \(B:F\to L\) with \(mc=dB\). Hence
\[
mZ\subset D\subset Z.
\tag{M.12}
\]
To turn this exponent bound into finiteness, a finite-generation argument is essential. As a subgroup of \(\mathbb Z^N\subset\mathbb R^N\), the group \(Z\) is discrete: every nonzero integer vector has Euclidean length at least one. G.3 supplies an integral basis of \(r\leq N\) real-linearly independent vectors for \(Z\). Therefore \(Z/mZ\) has exactly \(m^r\) elements, represented uniquely by coefficients \(0,\ldots,m-1\) in that basis. Indeed integer division reduces each coefficient to this range, and equality modulo \(mZ\) forces equality of the residues by uniqueness of the basis coefficients.

Inclusion (M.12) makes the map \(Z/mZ\to Z/D\), sending a class modulo \(mZ\) to its containing class modulo \(D\), well-defined and surjective. Thus there are at most \(m^r\leq m^N\) extension classes, proving (M.11). When \(m=1\) or \(n=0\), \(N=0\), \(Z=0\), and the same argument gives exactly one class. □

## N. A finite-orbit lattice estimate

For an action of a finite group \(H\) on a full lattice \(L\subset V\), K.2 supplies an \(H\)-invariant positive inner product on \(V\). A shortest nonzero vector exists: by G.3 only finitely many lattice vectors have length below the length of any fixed nonzero vector. We examine the case in which the orbit of such a vector spans \(V\).

**Lemma N.1 (uniform coordinates in a shortest-vector basis).** For each positive integer \(k\) there is a constant \(C_k\geq1\) with the following property. Suppose \(v_1,\ldots,v_k\) are a basis of a \(k\)-dimensional Euclidean space, each has length one, and every nonzero integral combination of them has length at least one. If
\[
y=\sum_{j=1}^k t_jv_j,
\]
then the coefficient vector satisfies
\[
\left(\sum_{j=1}^k t_j^2\right)^{1/2}\leq C_k|y|.
\tag{N.1}
\]

**Proof.** In orthonormal coordinates consider the following set of real \(k\)-by-\(k\) matrices:
\[
\mathcal S_k=
 \left\{A\ \middle|\
 |Ae_j|=1\ (1\leq j\leq k),\
 |Az|\geq1\ \text{for every }0\ne z\in\mathbb Z^k
 \right\}.
\tag{N.2}
\]
Here \(e_j\) denotes the standard coordinate vector. Each condition is closed, because \(A\mapsto|Ax|\) is continuous for each fixed \(x\). An arbitrary intersection of closed sets is closed, since its complement is a union of open sets. The column-length conditions bound every entry in absolute value by one. Thus \(\mathcal S_k\) is closed and bounded in a finite-dimensional real space, and is compact by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). It is nonempty, since it contains the identity matrix.

We must verify that this closed family has no singular matrix; merely restricting to invertible matrices would not establish compactness. Let \(A\in\mathcal S_k\). The homomorphism
\[
\mathbb Z^k\longrightarrow A\mathbb Z^k,\qquad z\longmapsto Az
\]
is injective by the lower bound in (N.2). Its image is a discrete additive subgroup of the Euclidean space \(W=\operatorname{im}A\): the same bound isolates zero, and translation isolates every other element. Choose orthonormal coordinates on \(W\) and apply G.3 there. The image has an integral basis of \(r\leq\dim W\) vectors.

For a free abelian group with an integral basis of \(s\) vectors, the quotient by twice the group has exactly \(2^s\) elements, by reducing each basis coefficient modulo two. The displayed isomorphism therefore gives \(2^k=2^r\), and hence \(k=r\leq\dim W\). Since \(\dim W\leq k\), equality holds and \(A\) is invertible.

The set
\(\mathcal S_k\times\{x\in\mathbb R^k:|x|=1\}\) is again closed and bounded in finite dimension, and therefore compact. The continuous function \((A,x)\mapsto|Ax|\) has a minimum \(\varepsilon_k\) on it by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Every value is positive because \(A\) is invertible and \(x\ne0\). Since the minimum is attained, \(\varepsilon_k>0\). Also \(\varepsilon_k\leq1\), by testing \(A=I\).

For the matrix \(A\) with columns \(v_j\), the hypotheses put \(A\in\mathcal S_k\). If \(t\ne0\), applying the minimum bound to \(t/|t|\) gives
\[
|At|\geq\varepsilon_k|t|.
\]
For \(t=0\) the same inequality is immediate. Taking \(C_k=\varepsilon_k^{-1}\) proves (N.1). □

**Theorem N.2 (a spanning shortest-vector orbit gives finitely many lattice actions).** Fix a finite abstract group \(H\) and a positive integer \(k\). Consider its actions on full lattices \(L\) in \(k\)-dimensional real vector spaces for which there is an \(H\)-invariant positive inner product and a shortest nonzero vector whose \(H\)-orbit spans the vector space. There are only finitely many such actions up to an \(H\)-equivariant lattice isomorphism, or equivalently up to a change of integral lattice basis.

**Proof.** For any one of these actions, rescale its inner product so that the chosen shortest vector \(v\) has length one. This leaves invariance intact, and every nonzero lattice vector now has length at least one. From the spanning orbit choose a real basis
\[
v_1=h_1v,\ldots,v_k=h_kv.
\]
Each basis vector has length one. Let \(L_0\) be their integral span. Then \(L_0\subset L\), and the hypotheses of N.1 hold for this basis.

We first bound the index of \(L_0\) in \(L\) uniformly in \(k\). Every coset in \(L/L_0\) has a unique representative in the half-open parallelepiped
\[
P_0=\left\{\sum_{j=1}^k t_jv_j\ \middle|\ 0\leq t_j<1\right\}.
\tag{N.3}
\]
Existence follows by subtracting the integer parts of the coefficients of a vector of \(L\). The resulting vector remains in \(L\). For uniqueness, the differences of two lists of coefficients in \([0,1)\) lie in \((-1,1)\); if they are all integers, they are all zero.

Each representative has length at most \(k\), by the triangle inequality and \(|v_j|=1\). In orthonormal coordinates it thus lies in the cube \([-k,k]^k\). Partition each coordinate line into half-open intervals of length
\[
s=\frac1{2\sqrt{k}},
\]
starting at \(-k\). At most \(\lceil4k\sqrt{k}\rceil+2\) such intervals meet \([-k,k]\), including any endpoint interval. In a product cell, two points have distance less than \(\sqrt{k}s=1/2\). Two distinct vectors of \(L\) have distance at least one, since their difference is a nonzero lattice vector. Hence each cell contains at most one representative. Therefore
\[
[L:L_0]\leq R_k,\qquad
R_k=\bigl(\lceil4k\sqrt{k}\rceil+2\bigr)^k.
\tag{N.4}
\]
This proves both finiteness and a bound without a volume formula.

Put \(D_k=R_k!\). For any \(\ell\in L\), the \(R_k+1\) classes
\(0,\ell,2\ell,\ldots,R_k\ell\) in \(L/L_0\) include a repetition by (N.4). Subtracting gives \(a\ell\in L_0\) for some integer \(1\leq a\leq R_k\). Since \(a\) divides \(D_k\), this implies \(D_k\ell\in L_0\). Consequently
\[
L_0\subset L\subset D_k^{-1}L_0.
\tag{N.5}
\]

Let \(A:\mathbb R^k\to V\) send \(e_j\) to \(v_j\), and express all data in these coordinates. The transformed lattice
\(L'=A^{-1}L\) satisfies
\[
\mathbb Z^k\subset L'\subset D_k^{-1}\mathbb Z^k.
\tag{N.6}
\]
The finite quotient \(D_k^{-1}\mathbb Z^k/\mathbb Z^k\) has \(D_k^k\) elements, obtained by reducing each coordinate to one of
\(0,1/D_k,\ldots,(D_k-1)/D_k\). Any intermediate subgroup in (N.6) is the inverse image of its image in this quotient. There are finitely many such images, since a finite set has finitely many subsets. Thus only finitely many transformed lattices \(L'\) can occur.

For \(h\in H\), the \(j\)-th column of its transformed real-linear map
\[
R_h=A^{-1}hA
\]
is \(A^{-1}(hv_j)\). Because the inner product is invariant, \(hv_j\) has length one. N.1 bounds the length of this column by \(C_k\). Moreover \(hv_j\in L\), so (N.6) places every coordinate of this column in \(D_k^{-1}\mathbb Z\). Each matrix entry therefore belongs to the finite set
\[
D_k^{-1}\mathbb Z\cap[-C_k,C_k].
\tag{N.7}
\]
There are only finitely many matrices with all \(k^2\) entries in that set, and only finitely many tuples \((R_h)_{h\in H}\), since \(H\) is finite. Requiring the group multiplication identities and preservation of \(L'\) only restricts these finitely many tuples.

We have produced finitely many possibilities for the pair consisting of \(L'\) and its entire \(H\)-action. If two original actions yield the same pair, the map \(A_2A_1^{-1}\) carries the first lattice onto the second and intertwines every \(h\), directly from the equality of the transformed matrices. It is an \(H\)-equivariant lattice isomorphism. Conversely, with an integral basis on each lattice supplied by G.3, any lattice isomorphism is represented by an integer matrix with integer inverse, and intertwining is precisely conjugacy of the action matrices by that basis change. This proves the stated finiteness. The zero-dimensional lattice, if included separately, is the zero group and has only one action. □

## O. Integral representations of a finite group

We now remove the spanning-orbit hypothesis from N.2. The argument uses a lower-rank quotient lattice and an explicit finiteness proof for extensions of integral representations.

**Lemma O.1 (projection along a lattice subspace).** Let \(L\) be a full lattice in a Euclidean vector space \(V\), and let \(W\subset V\) be a real subspace spanned by vectors of \(L\). Then \(L_W=L\cap W\) is a full lattice in \(W\), and the orthogonal projection \(P:V\to W^\perp\) has image lattice
\[
Q=P(L)\subset W^\perp.
\]
The sequence of additive groups
\[
0\longrightarrow L_W\longrightarrow L
 \xrightarrow{\ P\ }Q\longrightarrow0
\tag{O.1}
\]
is exact and splits as a sequence of abelian groups. If a group acts by isometries preserving both \(L\) and \(W\), it preserves \(W^\perp\) and all maps in (O.1) intertwine the actions. The abelian-group splitting need not intertwine them.

**Proof.** The group \(L_W\) is discrete, because it is a subgroup of the discrete lattice \(L\), and spans \(W\) by the hypothesis on \(W\). G.3 supplies an integral basis \(a_1,\ldots,a_r\) which is also a real basis of \(W\), where \(r=\dim W\). The parallelepiped
\[
K=\left\{\sum_{i=1}^r t_i a_i\ \middle|\ 0\leq t_i\leq1\right\}
\]
is compact and meets every coset of \(L_W\) in \(W\).

For any \(\ell\in L\) with \(|P\ell|\leq1\), subtract an element of \(L_W\) so that the \(W\)-component of the remaining vector lies in \(K\). The remaining vector still lies in \(L\) and belongs to the compact set
\[
K+\{z\in W^\perp:|z|\leq1\}.
\]
This set is compact as a continuous image of a product of two compact subsets of finite-dimensional Euclidean spaces; equivalently both factors are closed and bounded and [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) applies. By G.3, \(L\) meets it in finitely many points. Subtraction from \(L_W\) does not change the projection, so \(Q\) has only finitely many elements in its closed unit ball. Choose a positive radius smaller than the lengths of all its nonzero elements there, or use any radius less than one if there are none. This isolates zero in \(Q\), and translation isolates every other point. Thus \(Q\) is discrete.

Since \(L\) spans \(V\), its projection spans \(W^\perp\). G.3 makes \(Q\) a full lattice of rank \(\dim V-r\). The kernel of \(P|_L\) is precisely \(L\cap W\), giving exactness. Choose an integral basis \(q_1,\ldots,q_s\) of \(Q\) and lifts \(b_j\in L\). Define
\[
\sigma\left(\sum_{j=1}^s m_jq_j\right)=\sum_{j=1}^s m_jb_j.
\]
Uniqueness of the integral coefficients makes this a well-defined group homomorphism, and \(P\sigma\) is the identity. Every \(\ell\in L\) has a unique decomposition
\(\ell=a+\sigma(q)\) with \(a\in L_W\), \(q=P\ell\), proving the splitting.

If \(h\) is an isometry preserving \(W\), then for \(z\in W^\perp\) and \(w\in W\) one has
\(\langle hz,w\rangle=\langle z,h^{-1}w\rangle=0\).
Thus \(h\) preserves \(W^\perp\), and uniqueness of the orthogonal decomposition gives \(Ph=hP\). Preservation of \(L_W\) and \(Q\), and equivariance of (O.1), follow. Nothing in the arbitrary choice of the lifts \(b_j\) imposes equivariance on \(\sigma\). The cases \(W=0\) and \(W=V\) use empty bases where appropriate. □

**Lemma O.2 (finite extensions of two integral representations).** Fix a finite group \(H\), actions \(\alpha,\beta\) of \(H\) on free abelian groups \(A,Q\) of ranks \(r,s\), and put \(m=|H|\). Up to an equivariant group isomorphism which is the identity on the specified kernel and quotient, there are only finitely many equivariant exact sequences of abelian groups
\[
0\longrightarrow A\longrightarrow E\longrightarrow Q\longrightarrow0.
\tag{O.2}
\]
Their number is at most \(m^{rs(m-1)}\).

**Proof.** Lift an integral basis of \(Q\) to \(E\) and extend by integral linear combinations. As in the explicit final construction of O.1, this gives an abelian-group section and identifies \(E\) with \(A\oplus Q\). It follows in particular that \(E\) is free abelian. In these coordinates the action of \(h\) has the form
\[
R(h)=
\begin{pmatrix}
\alpha(h)&u(h)\\
0&\beta(h)
\end{pmatrix},
\qquad u(h)\in\operatorname{Hom}_{\mathbb Z}(Q,A).
\tag{O.3}
\]
Let \(B=\operatorname{Hom}_{\mathbb Z}(Q,A)\). Choosing integral bases identifies \(B\) with the additive group of all integer \(r\)-by-\(s\) matrices, so \(B\cong\mathbb Z^{rs}\). The formula
\[
\eta(h)T=\alpha(h)T\beta(h)^{-1}
\tag{O.4}
\]
defines an action of \(H\) on \(B\). All entries are integral because \(\alpha(h),\beta(h)\) and their inverses preserve the chosen lattices. The homomorphism identity follows by multiplying the two factors, with the inverse factors on the right in reverse order.

Set \(c(h)=u(h)\beta(h)^{-1}\in B\). The upper-right block of
\(R(hg)=R(h)R(g)\) gives exactly
\[
c(hg)=c(h)+\eta(h)c(g).
\tag{O.5}
\]
This also forces \(c(e)=0\), by setting \(h=e\). Conversely any \(B\)-valued function satisfying (O.5) defines (O.3) with \(u(h)=c(h)\beta(h)\). Direct block multiplication proves that these matrices form an action; the matrix at \(e\) is the identity and the one at \(h^{-1}\) is the inverse. They preserve \(A\oplus Q\) and give the required actions on its two ends.

Changing the section by a homomorphism \(t:Q\to A\) changes coordinates by \((a,q)\mapsto(a+tq,q)\). Conjugating (O.3) in the new coordinates replaces \(c(h)\) by
\[
c(h)+\eta(h)t-t.
\tag{O.6}
\]
Also, any equivalence between two sequences in these coordinates must have the form \((a,q)\mapsto(a+tq,q)\): its identity restriction to \(A\) and its identity map on \(Q\) leave exactly this additive homomorphism \(t\). Intertwining their actions gives
\(c'(h)-c(h)=t-\eta(h)t\), which is a difference of the form (O.6), with \(-t\) in place of \(t\). Conversely this coordinate map intertwines whenever that equality holds.

Let \(C\) be the additive group of functions satisfying (O.5), and let \(D\) be the subgroup of functions \(h\mapsto\eta(h)t-t\), \(t\in B\). These functions satisfy (O.5), because
\[
\eta(hg)t-t=(\eta(h)t-t)+\eta(h)(\eta(g)t-t).
\]
Thus the equivalence classes in (O.2) are exactly \(C/D\).

For \(c\in C\), put \(S=\sum_{g\in H}c(g)\in B\). Summing (O.5) over \(g\), and reindexing \(g\mapsto hg\), gives
\[
mc(h)=S-\eta(h)S.
\tag{O.7}
\]
Consequently \(mC\subset D\). On the other hand \(C\), by \(c(e)=0\), is a subgroup of
\(B^{H\setminus\{e\}}\cong\mathbb Z^{rs(m-1)}\). It is discrete in the associated Euclidean space. G.3 gives it an integral basis of rank \(d\leq rs(m-1)\). Coefficient reduction modulo \(m\) shows that \(C/mC\) has \(m^d\) elements, exactly as in M.5. The natural map from \(C/mC\) onto \(C/D\) proves the asserted bound. This includes \(m=1\), \(r=0\) or \(s=0\), when the relevant quotient has one element. □

**Theorem O.3 (finiteness of integral representations).** For every finite group \(H\) and integer \(n\geq0\), there are only finitely many homomorphisms
\[
H\longrightarrow\operatorname{GL}(n,\mathbb Z)
\]
up to conjugation by \(\operatorname{GL}(n,\mathbb Z)\). The homomorphisms need not be faithful.

**Proof.** In basis-free terms we must show that there are finitely many \(H\)-equivariant isomorphism classes of rank-\(n\) free abelian groups with an \(H\)-action. A choice of integral basis gives the displayed homomorphism, and an equivariant lattice isomorphism is exactly an integral change of basis conjugating the matrices, as proved at the end of N.2.

Induct on \(n\). For \(n=0\) the zero group has a unique action. Given an action on a rank-\(n\) lattice \(L\), extend it real-linearly to \(V\) and choose an invariant positive inner product by K.2. For \(n>0\), choose a shortest nonzero lattice vector \(v\), whose existence follows from G.3's bounded-set finiteness. Let
\[
W=\operatorname{span}_{\mathbb R}\{hv:h\in H\},\qquad
r=\dim W.
\tag{O.8}
\]
Then \(1\leq r\leq n\), and \(W\) is \(H\)-invariant because left multiplication by any \(h\) permutes the orbit. It is spanned by lattice vectors.

If \(r=n\), N.2 already gives finitely many possibilities for \(L\) with this action. Suppose \(r<n\). By O.1, \(L_W=L\cap W\) has rank \(r\), while \(Q=P(L)\subset W^\perp\) has rank \(n-r\), and (O.1) is an equivariant exact sequence of abelian groups. The vector \(v\) is shortest also in \(L_W\), because \(L_W\subset L\), and its orbit spans \(W\). N.2 gives finitely many possible actions on \(L_W\) up to equivariant lattice isomorphism. The induction hypothesis gives finitely many on \(Q\), since \(n-r<n\).

Choose one representative of each of these finitely many possibilities for the two ends. Transporting the inclusions and projections along chosen end isomorphisms regards every possible \(L\) as an extension of one of these fixed pairs. O.2 gives finitely many extension classes for each pair. An equivalence fixing the two ends is in particular an equivariant isomorphism of the middle lattices, so this also bounds the number of possible middle-lattice isomorphism classes. Changing the chosen end identifications can only identify some of these possibilities, and cannot create further middle lattices.

Finally \(r\) has only the finitely many values \(1,\ldots,n-1\). Combining these cases with \(r=n\) proves finiteness in rank \(n\). The argument imposes no injectivity requirement on the action on \(L\), either end, or any intermediate span. This completes the induction. □

## P. Finiteness in compact flat geometry

**Theorem P.1 (finite integral matrix groups).** For each integer \(n\geq0\), every finite subgroup of \(\operatorname{GL}(n,\mathbb Z)\) has order at most \(3^{n^2}\). There are only finitely many conjugacy classes of these subgroups under \(\operatorname{GL}(n,\mathbb Z)\).

**Proof.** Reduction of integer entries modulo three defines a homomorphism
\[
\theta:\operatorname{GL}(n,\mathbb Z)
       \longrightarrow\operatorname{GL}(n,\mathbb F_3),
\tag{P.1}
\]
where \(\mathbb F_3=\mathbb Z/3\mathbb Z\). The reduced matrix is invertible because the integer inverse reduces to its inverse. The codomain is a finite group: it is a subset of the set of \(n\)-by-\(n\) matrices with three possible entries in each position, which has \(3^{n^2}\) elements.

We prove that \(\ker\theta\) has no nonidentity element of finite order. If it did, choose one of order \(d>1\) and a prime divisor \(p\) of \(d\). A prime divisor exists by taking the smallest integer divisor greater than one; if that divisor factored nontrivially it would not be smallest. Raising the element to the power \(d/p\) gives an element \(C\) of order \(p\), still in the kernel: its \(p\)-th power is the identity, and it is not the identity by minimality of \(d\).

Since \(C\equiv I\pmod3\) and \(C\ne I\), write
\[
C=I+3^aB,
\]
where \(a\geq1\), \(B\) is an integer matrix, and at least one entry of \(B\) is not divisible by three. Such a largest common exponent \(a\) exists because some entry of \(C-I\) is a nonzero integer. The identity and \(B\) commute, so expanding \(C^p=I\) by successive multiplication gives
\[
0=pB+\sum_{j=2}^p
       \binom pj\,3^{a(j-1)}B^j
\tag{P.2}
\]
after division by \(3^a\). Each term in the sum is divisible entrywise by three. Reduction modulo three gives \(pB=0\). If \(p\ne3\), its residue is one or two and is invertible in \(\mathbb F_3\), forcing every entry of \(B\) to be divisible by three, a contradiction. Therefore \(p=3\).

In this remaining case expand the cube before reducing:
\[
0=3^{a+1}B+3^{2a+1}B^2+3^{3a}B^3.
\]
Division by \(3^{a+1}\) gives
\[
0=B+3^aB^2+3^{2a-1}B^3.
\tag{P.3}
\]
Since \(a\geq1\), both coefficients following \(B\) are divisible by three. Again \(B\equiv0\pmod3\), the required contradiction. Thus the kernel is torsion-free.

Let \(H\) be a finite subgroup of \(\operatorname{GL}(n,\mathbb Z)\). Every element of a finite group has finite order, because two nonnegative powers coincide and cancellation gives a positive power equal to the identity. Hence \(H\cap\ker\theta=\{I\}\). The restriction \(\theta|_H\) is injective: equal images give a quotient in this intersection. Its image lies in the finite group of (P.1), proving the order bound.

There are only finitely many subgroups of \(\operatorname{GL}(n,\mathbb F_3)\), since there are only finitely many subsets of a finite set. Each finite integral matrix group \(H\) is abstractly isomorphic to one of these subgroups, by its injective reduction. For each such abstract finite group, O.3 gives finitely many integral representations of dimension \(n\) up to integral conjugation. Restricting to faithful representations and then taking their images still gives only finitely many conjugacy classes of subgroups. Every \(H\) occurs among these images. The finite union over the possible abstract groups proves the second assertion. In dimension zero all groups and matrices here are trivial, and both assertions hold directly. □

**Theorem P.2 (Bieberbach finiteness).** For each fixed dimension \(n\geq1\), there are only finitely many affine conjugacy classes of discrete cocompact groups of Euclidean motions of \(\mathbb R^n\), including groups with torsion. Consequently there are only finitely many affine equivalence classes of connected compact flat Riemannian \(n\)-manifolds.

**Proof.** Let \(\Gamma\) be such a motion group. Its full translation subgroup \(\Lambda\) is a normal full lattice of finite index by J.3. Choose an integral basis of \(\Lambda\). Conjugation by \(\gamma=(A,p)\) sends \(\tau_v\) to \(\tau_{Av}\), as in (K.1), so its linear part induces an integral automorphism of this lattice. This yields an action of the finite quotient \(\Gamma/\Lambda\) on \(\mathbb Z^n\). The action is faithful: if \(A\) fixes every lattice vector, it fixes their real span and therefore equals \(I\), which means \(\gamma\in\Lambda\). Thus the quotient is identified with a finite subgroup
\(F\subset\operatorname{GL}(n,\mathbb Z)\), and we obtain an extension
\[
1\longrightarrow\mathbb Z^n\longrightarrow\Gamma
 \longrightarrow F\longrightarrow1
\tag{P.4}
\]
whose specified action is the defining action of \(F\) on \(\mathbb Z^n\).

By P.1, there are finitely many possibilities for \(F\) up to integral conjugacy. Choose representatives \(F_1,\ldots,F_t\). Changing the integral basis of \(\Lambda\) and identifying the quotient accordingly puts every extension (P.4) over one of these \(F_i\), with the fixed defining action on the fixed lattice \(\mathbb Z^n\). M.5 gives finitely many extension equivalence classes for each such action. In particular their middle groups have only finitely many abstract isomorphism types. Every crystallographic group \(\Gamma\) has appeared in this list. Conversely M.3 realizes each listed extension as a crystallographic group, because the defining action of \(F_i\) is faithful; torsion in the extension is permitted throughout this step.

K.3 says that any isomorphism between two crystallographic groups of the same dimension is induced by an invertible affine map of their Euclidean spaces. Hence each abstract isomorphism type in the finite list gives just one affine conjugacy class of realized groups. This proves the first assertion, including groups with fixed points.

Finally J.3 represents each connected compact flat Riemannian \(n\)-manifold as the quotient of Euclidean space by a freely acting group of this kind. An affine conjugacy of two such groups descends to an affine diffeomorphism of the quotient manifolds with their Levi-Civita connections, as proved in K.3. Restricting the finite list to the free actions therefore proves the stated manifold finiteness. The affine equivalence assertion leaves the metric parameters free, as the circle calculation (K.9) illustrates. □

## Q. The compact core of a complete flat manifold

The translation subgroup of a noncompact Euclidean quotient need not have finite index. A screw motion, for example, can have an irrational normal rotation. We instead begin with the normal abelian subgroup supplied by J.2.

**Lemma Q.1 (the common minimum set of commuting motions).** Let \(H\) be any abelian group of Euclidean motions of a finite-dimensional real inner-product space. Write \(h(x)=A_hx+p_h\), and put
\[
U=\bigcap_{h\in H}\ker(A_h-I),\qquad W=U^\perp.
\]
There is \(c\in W\) such that, in the decomposition \(x=u+c+w\),
\[
h(u+c+w)=u+t_h+c+A_hw,\qquad t_h\in U.
\tag{Q.1}
\]
The map \(h\mapsto t_h\) is an additive homomorphism. Moreover the intersection of the minimum-displacement sets of all \(h\in H\) is exactly the affine plane \(C=c+U\). Any Euclidean motion normalizing \(H\) preserves \(C\).

**Proof.** Every \(A_h\) fixes \(U\) pointwise and preserves \(W\), because it is orthogonal. Decompose \(p_h=t_h+q_h\) into these two spaces. The induced motions
\(\widehat h(w)=A_hw+q_h\) on \(W\) commute. Their linear parts have no common fixed vector other than zero, by the definition of \(U\).

Choose finitely many \(h_1,\ldots,h_s\) whose linear fixed subspaces in \(W\) have intersection zero. Such a choice does not require \(H\) to be finitely generated: start with \(W\), and, while the current intersection is nonzero, choose an element whose fixed subspace does not contain it. The dimension strictly decreases at each step, so after at most \(\dim W\) steps the intersection is zero. If \(W=0\), take \(c=0\); the following argument is unnecessary.

For \(W\ne0\), set \(T_i=A_{h_i}-I\) on \(W\) and consider
\[
f(w)=\sum_{i=1}^s|T_iw+q_{h_i}|^2,\qquad
S=\sum_i T_i^*T_i,\qquad b=\sum_i T_i^*q_{h_i}.
\]
Here the star is the adjoint for the inner product. For \(w\ne0\),
\(\langle Sw,w\rangle=\sum_i|T_iw|^2>0\), since the common kernel is zero. Thus \(S\) has zero kernel and is invertible in finite dimension. Put \(c=-S^{-1}b\). Expanding the squares gives
\[
f(w)-f(c)=\langle S(w-c),w-c\rangle.
\tag{Q.2}
\]
Consequently \(c\) is the unique minimum point of \(f\).

For \(g\in H\), commutation and the isometry property give
\[
|\widehat h_i(\widehat g w)-\widehat g w|
 =|\widehat g(\widehat h_i w)-\widehat g w|
 =|\widehat h_i w-w|.
\]
Thus \(f(\widehat g w)=f(w)\). The unique minimum must be fixed by every \(\widehat g\), so \(q_g=c-A_gc\). This proves (Q.1). Its composition law on \(C\), where every \(h\) is a translation, gives \(t_{hg}=t_h+t_g\).

For \(x=u+c+w\), orthogonality yields
\[
|hx-x|^2=|t_h|^2+|(A_h-I)w|^2.
\tag{Q.3}
\]
Its global minimum is \(|t_h|^2\), attained precisely when
\(w\in\ker(A_h-I)|_W\). Intersecting these conditions over all \(h\) gives \(w=0\). Thus \(C\) is intrinsically the common minimum set. If \(\gamma\) normalizes \(H\), then
\[
|(\gamma h\gamma^{-1})(\gamma x)-\gamma x|=|hx-x|.
\]
It maps the minimum set of \(h\) onto that of \(\gamma h\gamma^{-1}\). Conjugation permutes \(H\), so it preserves their intersection \(C\). This also proves the last assertion in the case \(W=0\). □

**Theorem Q.2 (an invariant cocompact affine plane).** Let \(\Gamma\) be a discrete torsion-free group of Euclidean motions of \(\mathbb R^n\). There is a \(\Gamma\)-invariant affine plane \(P\), of dimension \(0\leq r\leq n\), on which its action is faithful, free, discrete and cocompact. The quotient \(B=P/\Gamma\) is a connected compact flat manifold. Dimension \(r=0\) occurs precisely when \(\Gamma\) is trivial.

**Proof.** First the action of \(\Gamma\) on all of \(\mathbb R^n\) is free. By J.1 the stabilizer of any point is finite, using the compact singleton as its compact-intersection test set. Every element of a finite group has finite order, by repetition among its powers. Torsion-freeness therefore makes each stabilizer trivial.

J.2 supplies a normal abelian subgroup \(H\) of finite index in \(\Gamma\). Apply Q.1 to \(H\), with its notation \(U,c,C\) and \(t_h\). If \(t_h=0\), then \(h\) fixes \(c\), so freeness gives \(h=e\). Thus \(t:H\to U\) is injective.

For any bounded set of vectors \(t_h\), the points \(hc=c+t_h\) are bounded. Since \(p_h=hc-A_hc\) and \(|A_hc|=|c|\), the translation parts \(p_h\) are also bounded. The bounded-motion finiteness proved in J.1 shows that only finitely many \(h\) occur. In particular \(t(H)\) has only finitely many elements in the unit ball. A sufficiently small ball then isolates zero, and translation isolates every other element. Hence \(t(H)\) is a discrete additive group. By G.3 it is a full lattice in its real span
\[
V=\operatorname{span}_{\mathbb R}t(H)\subset U.
\tag{Q.4}
\]

Normality of \(H\) and Q.1 make \(C\) invariant under \(\Gamma\). If \(\gamma(x)=A_\gamma x+p_\gamma\), invariance of \(C\) makes \(A_\gamma U=U\). Conjugating the translation by \(t_h\) on \(C\) gives the translation by \(A_\gamma t_h\), which also comes from \(H\). Thus \(A_\gamma V=V\).

The quotient affine space \(C/V\) has an induced Euclidean metric on its direction space, identified with \(U\cap V^\perp\). The action of \(\Gamma\) on it is affine and isometric. Every element of \(H\) acts there trivially, since its translation vector belongs to \(V\). Therefore this action factors through the finite group \(\Gamma/H\). K.2 gives a fixed point for this finite affine action. Its inverse image in \(C\) is a \(\Gamma\)-invariant affine plane \(P\) parallel to \(V\). On \(P\), the group \(H\) acts by exactly the full translation lattice \(t(H)\), so \(P/H\) is compact by G.3. Its continuous quotient map onto \(P/\Gamma\) proves cocompactness.

The restricted action on \(P\) is free, since a fixed point there would be a fixed point in \(\mathbb R^n\). It is consequently faithful: an element acting as the identity on \(P\) fixes a point. To see discreteness, choose \(p\in P\). Only finitely many \(\gamma\in\Gamma\) have \(|\gamma p-p|\leq1\), because this bounds their full translation parts by
\[
|p_\gamma|=|\gamma p-A_\gamma p|\leq1+2|p|,
\]
and J.1 applies. Every nonidentity member of that finite set has positive displacement at \(p\). Choose a positive \(\varepsilon<1\) smaller than all those displacements, or any \(\varepsilon<1\) if there are none. The open condition \(|gp-p|<\varepsilon\) on the Euclidean motion group of \(P\) then meets the restricted \(\Gamma\) only at the identity. Group translation proves discreteness everywhere.

For \(r>0\), J.1 and the free-quotient assertion of J.3 now make \(B=P/\Gamma\) a connected compact flat manifold. If \(r=0\), then \(P\) is a point and faithfulness makes \(\Gamma\) trivial, so the quotient is the zero-dimensional compact flat manifold consisting of one point. Conversely for the trivial group the construction may take \(P\) to be any point, so \(r=0\). □

**Theorem Q.3 (the flat orthogonal bundle description).** With \(\Gamma,P,B\) as in Q.2, let \(V\) be the direction space of \(P\) and let \(N=V^\perp\). The quotient \(\mathbb R^n/\Gamma\) is the total space of the rank-\((n-r)\) flat orthogonal vector bundle
\[
E_\rho=(P\times N)/\Gamma\longrightarrow B,\qquad
\gamma(p,z)=(\gamma p,\rho(\gamma)z),
\tag{Q.5}
\]
where \(\rho(\gamma)=A_\gamma|_N\). Its zero section is a deformation retract.

Conversely, if \(B=P/\Gamma\) is a connected compact flat manifold with Euclidean universal cover \(P\), every orthogonal representation \(\rho:\Gamma\to\mathrm O(k)\) gives by (Q.5) a connected complete flat Riemannian manifold of dimension \(\dim B+k\). Every connected complete flat Riemannian manifold has the bundle description above, including the point base for Euclidean space.

**Proof.** Orthogonality and invariance of \(V\) imply invariance of \(N\): for \(z\perp V\) and \(v\in V\),
\(\langle A_\gamma z,v\rangle=\langle z,A_\gamma^{-1}v\rangle=0\).
The restrictions form an orthogonal representation by multiplication of the linear parts. Every \(x\in\mathbb R^n\) has a unique expression \(x=p+z\) with \(p\in P,z\in N\). This is a smooth isometry from the Euclidean product \(P\times N\) to \(\mathbb R^n\), and
\[
\gamma(p+z)=\gamma p+A_\gamma z.
\]
It is equivariant for (Q.5), and so identifies the quotient spaces and their local Euclidean metrics.

We give the bundle charts explicitly. Over a connected evenly covered neighbourhood \(U\subset B\), choose an inverse branch \(s:U\to P\) of the covering \(P\to B\). Every orbit over \(y\in U\) has a unique representative \((s(y),w)\): transitivity of the deck group on the fibre moves its first component to \(s(y)\), and freeness makes that move unique. Thus
\[
U\times N\longrightarrow E_\rho|_U,\qquad
(y,w)\longmapsto[(s(y),w)]
\tag{Q.6}
\]
is a bundle chart. In covering charts its inverse and itself are smooth. If another inverse branch satisfies \(s'(y)=\gamma s(y)\) on a connected overlap, then the same orbit has coordinates \(w'=\rho(\gamma)w\). The deck element is locally constant on overlaps by uniqueness of covering sheets and path lifting, [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). Hence these transitions are locally constant orthogonal matrices. Their inverse and cocycle identities follow from those of the deck transformations. They define a smooth vector bundle with a fibre metric.

The ordinary derivative of vector-valued functions in each chart is preserved by a constant transition matrix, so these derivatives agree to give a connection. Its local connection matrices are zero; [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3) gives zero curvature, and [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) shows that the constant fibre metric is parallel. This proves the asserted flat orthogonal structure. At the zero section the vertical vectors are precisely the Euclidean orthogonal normals to \(P\), so this bundle is also its normal bundle in the quotient.

For \(0\leq t\leq1\), the formula
\[
H_t([(p,z)])=[(p,(1-t)z)]
\tag{Q.7}
\]
is well-defined because scalar multiplication commutes with every \(\rho(\gamma)\). It is smooth in the bundle charts. At \(t=0\) it is the identity, at \(t=1\) its image is the zero section, and it fixes that section for every \(t\). This is a deformation retraction.

For the converse, use the given deck action on \(P\) and the chosen representation in (Q.5). These are Euclidean motions of \(P\times\mathbb R^k\). The action is free, because a fixed point projects to a fixed point on \(P\). It is properly discontinuous: if a translate of a compact set meets it, the corresponding translate of its compact projection to \(P\) meets that projection, allowing only finitely many deck transformations. The covering-chart construction in G.2 therefore gives a connected smooth quotient with the descended standard affine-flat connection. Its Euclidean metric descends as well, and its Levi-Civita connection is the descended one by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). Every initial vector has a complete geodesic obtained by projecting its affine line in the product. Thus the quotient is geodesically complete, and Hopf–Rinow B.2 gives metric completeness. Its vector-bundle structure and deformation retraction are exactly (Q.6)–(Q.7).

Finally let \(M\) be any connected complete flat Riemannian manifold. Its Levi-Civita connection is complete, has zero torsion and zero curvature. Apply G.2. In its proof choose the initial parallel frame on the universal cover orthonormally for the lifted metric. Metric compatibility makes the auxiliary metric in that proof equal to the lifted metric, so the resulting affine identification with Euclidean space is an isometry. The deck group is discrete, free and Euclidean. A finite-order Euclidean motion has a fixed point by K.2, as shown in M.4, so this deck group is torsion-free. Q.2 and the first part of this theorem supply (Q.5). In dimension zero the manifold and its base are a point, with the zero bundle. □

## R. Deforming orthogonal holonomy to a finite image

Let \(L\cong\mathbb Z^r\) be normal in a group \(G\), with finite quotient \(F=G/L\) of order \(m\). Conjugation gives an action \(\theta:F\to\operatorname{Aut}(L)\), whether or not it is faithful. Choose an integral basis and put \(V=L\otimes_{\mathbb Z}\mathbb R\), meaning the real vector space with that basis. Each \(\theta(f)\) extends linearly to \(V\).

A character of \(L\) means a homomorphism \(\chi:L\to S^1\). The action on characters is
\[
(f\chi)(\ell)=\chi(\theta(f)^{-1}\ell),
\]
and complex conjugation is \(\overline\chi(\ell)=\chi(\ell)^{-1}\).

**Lemma R.1 (equivariant averaged logarithms).** Suppose a finite set \(\Omega\) of characters is stable under \(F\) and complex conjugation. There are real-linear functions \(\lambda_\chi:V\to\mathbb R\), for \(\chi\in\Omega\), such that
\[
\begin{aligned}
\lambda_{f\chi}(v)&=\lambda_\chi(\theta(f)^{-1}v),\\
\lambda_{\overline\chi}(v)&=-\lambda_\chi(v),\\
\exp(2\pi i\,2m\lambda_\chi(\ell))&=\chi(\ell)^{2m}
                 \qquad(\ell\in L).
\end{aligned}
\tag{R.1}
\]
In particular \(\lambda_\chi=0\) for every real-valued character \(\chi=\overline\chi\).

**Proof.** For each \(\chi\), choose real arguments of its values on the chosen integral basis of \(L\). Such arguments exist by the surjectivity of the circle exponential proved in [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). Extend these real numbers to a real-linear function \(\alpha_\chi:V\to\mathbb R\). On lattice vectors the homomorphism property and the exponential addition identity give
\[
\exp(2\pi i\,\alpha_\chi(\ell))=\chi(\ell).
\]
No compatibility between the different choices of \(\alpha_\chi\) is assumed.

For \(\varepsilon=1\) use \(\chi^\varepsilon=\chi\), and for \(\varepsilon=-1\) use its conjugate. Define
\[
\lambda_\chi(v)=
 \frac1{2m}\sum_{f\in F}\ \sum_{\varepsilon\in\{1,-1\}}
 \varepsilon\,\alpha_{(f\chi)^\varepsilon}(\theta(f)v).
\tag{R.2}
\]
This is a finite sum of real-linear functions. Replacing \(\chi\) by \(h\chi\) and setting \(g=fh\) turns the argument
\(\theta(f)v\) into \(\theta(g)\theta(h)^{-1}v\). Since \(f\mapsto fh\) permutes \(F\), this proves the first identity in (R.1). Replacing \(\chi\) by \(\overline\chi\) replaces the index \(\varepsilon\) by \(-\varepsilon\); the sign in front of \(\alpha\) changes accordingly. This proves the second identity.

For each lattice vector \(\ell\), each individual summand before division by \(2m\) has exponential
\[
\begin{aligned}
\exp\!\left(2\pi i\,\varepsilon
 \alpha_{(f\chi)^\varepsilon}(\theta(f)\ell)\right)
 &=\bigl((f\chi)^\varepsilon(\theta(f)\ell)\bigr)^\varepsilon\\
 &=\chi(\ell).
\end{aligned}
\]
There are \(2m\) summands. Multiplication of their exponentials gives the third identity of (R.1). If \(\chi=\overline\chi\), the second identity says
\(\lambda_\chi=-\lambda_\chi\), which over \(\mathbb R\) gives zero. □

**Theorem R.2 (finite-image deformation with a fixed quotient).** Every orthogonal representation
\(\rho:G\to\mathrm O(k)\) has a smooth deformation \(\rho_t\), \(0\leq t\leq1\), through orthogonal representations, with \(\rho_0=\rho\), such that \(\rho_1\) factors through
\[
G/(2mL).
\tag{R.3}
\]
Here \(2mL=\{2m\ell:\ell\in L\}\), viewed as a normal subgroup of \(G\). This quotient has order \(m(2m)^r\), so
\[
|\rho_1(G)|\leq m(2m)^r.
\tag{R.4}
\]
Smoothness means that the matrix \(\rho_t(g)\) depends smoothly on \(t\) for every fixed \(g\). Neither faithfulness of \(\rho\) nor a splitting of \(G\) is required.

**Proof.** Complexify the real representation to \(\mathbb C^k\), with its usual Hermitian inner product. Its matrices are unitary. On \(L\), the matrices of the \(r\) basis generators commute. I.1 diagonalizes the first one orthogonally. The other matrices and their inverses preserve each of its eigenspaces by commutation, so their restrictions are still unitary. Diagonalize the next restricted matrix on each such space, and continue through the finitely many generators. We obtain an orthogonal decomposition
\[
\mathbb C^k=\bigoplus_{\chi\in\Omega}E_\chi,\qquad
\rho(\ell)|_{E_\chi}=\chi(\ell)I,
\tag{R.5}
\]
with finitely many nonzero summands. The eigenvalues on a common eigenvector define a character on all integral combinations of the basis generators, proving the formula for every \(\ell\). Equal characters are grouped into one summand. If \(r=0\), use the single trivial character; if \(k=0\), the desired deformation is the constant one and all assertions hold directly.

Complex conjugation takes \(E_\chi\) onto \(E_{\overline\chi}\), because the original matrices are real. For \(g\in G\) with image \(f\in F\), and \(w\in E_\chi\), one has
\[
\rho(\ell)\rho(g)w
 =\rho(g)\rho(g^{-1}\ell g)w
 =\chi(\theta(f)^{-1}\ell)\rho(g)w.
\]
Thus \(\rho(g)E_\chi=E_{f\chi}\), using \(g^{-1}\) for equality. The set \(\Omega\) is stable under both required actions. Apply R.1 to it.

For \(v\in V\) and \(t\in\mathbb R\), define \(D_t(v)\) on (R.5) by
\[
D_t(v)|_{E_\chi}
   =\exp(-2\pi i\,t\lambda_\chi(v))I.
\tag{R.6}
\]
These operators are unitary and satisfy
\(D_t(v+w)=D_t(v)D_t(w)\). The identity
\(\lambda_{\overline\chi}=-\lambda_\chi\) makes \(D_t(v)\) commute with complex conjugation. Its restriction to the fixed real subspace \(\mathbb R^k\) is therefore a real orthogonal transformation. The first identity in (R.1), together with the permutation of eigenspaces, gives
\[
\rho(g)D_t(v)\rho(g)^{-1}
       =D_t(\theta(f)v).
\tag{R.7}
\]
Indeed on \(E_{f\chi}\) the scalar on the left is the scalar for \(\chi,v\), and the scalar on the right agrees because
\(\lambda_{f\chi}(\theta(f)v)=\lambda_\chi(v)\).

We also need a translation cocycle on the whole group, not just on \(L\). Choose the normalized section of \(G\to F\) from M.1, giving a factor set \(c\) and unique coordinates \(g=(\ell,f)\). M.2 supplies \(b:F\to V\) with \(b(e)=0\) and
\[
c(f,h)=b(f)+\theta(f)b(h)-b(fh).
\]
Set \(z(g)=\ell+b(f)\). Substitution in the group multiplication law (M.4) proves
\[
z(gg')=z(g)+\theta(f)z(g'),\qquad
z(\ell)=\ell\quad(\ell\in L).
\tag{R.8}
\]
This calculation uses no faithfulness or splitting assumption.

Define
\[
\rho_t(g)=D_t(z(g))\rho(g).
\tag{R.9}
\]
Equations (R.7)–(R.8) give
\[
\begin{aligned}
\rho_t(g)\rho_t(g')
 &=D_t(z(g))D_t(\theta(f)z(g'))\rho(gg')\\
 &=D_t(z(gg'))\rho(gg')=\rho_t(gg').
\end{aligned}
\]
Thus \(\rho_t\) is an orthogonal representation for every real \(t\), and \(\rho_0=\rho\). Each fixed \(g\) gives a finite collection of scalar exponentials in fixed orthogonal subspaces, so its matrix depends smoothly on \(t\).

For \(\ell\in L\), the endpoint acts on \(E_\chi\) by the scalar
\[
\chi(\ell)\exp(-2\pi i\,\lambda_\chi(\ell)).
\]
Its \(2m\)-th power is one by (R.1). Hence
\(\rho_1(2m\ell)=\rho_1(\ell)^{2m}=I\) for every \(\ell\), proving the kernel assertion in (R.3). The subgroup \(2mL\) is normal because every conjugation automorphism of \(L\) preserves its integer multiples. In an integral basis, \(L/(2mL)\) has \((2m)^r\) elements, by reducing every coefficient modulo \(2m\). Each of the \(m\) cosets of \(L\) in \(G\) splits into that many cosets of \(2mL\). Therefore the quotient (R.3) has exactly the stated order, and (R.4) follows. Restricting the smooth family to \(0\leq t\leq1\) completes the proof. □

## S. Finiteness for noncompact complete flat manifolds

**Lemma S.1 (finitely many orthogonal representations of a finite group).** For a finite group \(K\) and fixed \(k\geq0\), the homomorphisms \(K\to\mathrm O(k)\) have only finitely many conjugacy classes under \(\mathrm O(k)\).

**Proof.** The case \(k=0\) is immediate. For \(k>0\), regard a representation as the finite tuple of its matrices, one for each element of \(K\). Orthogonality and the multiplication identities are closed polynomial conditions on this tuple. Its entries have absolute value at most one, so the representation space is compact by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

We show that all sufficiently close representations are conjugate. Let \(\rho,\sigma:K\to\mathrm O(k)\) satisfy
\(\|\sigma(h)-\rho(h)\|<1/2\) for every \(h\in K\), and put
\[
T=\frac1{|K|}\sum_{h\in K}\sigma(h)\rho(h)^{-1}.
\tag{S.1}
\]
Then \(\|T-I\|<1/2\). If \(Tv=0\), the inequality
\(|v|=|(I-T)v|<|v|/2\) for \(v\ne0\) is impossible. Hence \(T\) is invertible. Reindexing the finite sum by \(h\mapsto gh\) gives
\[
\sigma(g)T=T\rho(g).
\tag{S.2}
\]
Let \(C=T^{\mathsf T}T\). Equation (S.2) and orthogonality imply
\(\rho(g)^{\mathsf T}C\rho(g)=C\), so \(C\) commutes with every \(\rho(g)\).

We supply the positive square-root step. The real symmetric matrix \(C\) is Hermitian on \(\mathbb C^k\), and I.1 gives an orthonormal eigenbasis. Each eigenvalue is positive, since
\(\langle Cv,v\rangle=|Tv|^2>0\) for \(v\ne0\). Let \(\lambda_1,\ldots,\lambda_s\) be the distinct eigenvalues. The real polynomial
\[
p(x)=\sum_{j=1}^s \lambda_j^{-1/2}
       \prod_{a\ne j}\frac{x-\lambda_a}{\lambda_j-\lambda_a}
\]
has \(p(\lambda_j)=\lambda_j^{-1/2}\). Thus \(P=p(C)\) is real symmetric, commutes with every \(\rho(g)\), and satisfies \(PCP=I\), as checked on the eigenbasis. The real matrix \(U=TP\) is orthogonal and, by (S.2), satisfies
\(\sigma(g)U=U\rho(g)\). This proves orthogonal conjugacy.

The condition that the finitely many differences have operator norm less than \(1/2\) defines an open neighbourhood of each representation; continuity of this norm follows from the finite-dimensional norm estimates in [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). These neighbourhoods cover the compact representation space. A finite subcover suffices, and each chosen neighbourhood is contained in the conjugacy class of its centre. There are therefore only finitely many classes. □

**Lemma S.2 (a smooth deformation gives isomorphic bundles).** Let \(B=P/\Gamma\) be a connected compact flat manifold, and let \(\rho_t:\Gamma\to\mathrm O(k)\) be a family of representations defined for \(t\) in an open interval containing \([0,1]\), smooth in \(t\) on every fixed group element. Then the bundles \(E_{\rho_0}\) and \(E_{\rho_1}\) of Q.3 are smoothly isomorphic as vector bundles over \(B\). This does not assert an isomorphism of their flat connections.

**Proof.** Form the family quotient
\[
\mathcal E=(P\times\mathbb R^k\times I)/\Gamma,\qquad
\gamma(p,z,t)=(\gamma p,\rho_t(\gamma)z,t),
\tag{S.3}
\]
over \(B\times I\). Here \(I\) is the given open interval. Over a covering neighbourhood \(U\subset B\), choose the inverse branch \(s:U\to P\) used in (Q.6). The map
\[
(y,t,w)\longmapsto[(s(y),w,t)]
\]
is a vector-bundle chart. Points over distinct base points are separated by disjoint inverse images of base neighbourhoods; points over the same base point are separated in one such product chart. A countable subcover of base charts, each with a countable product basis, gives a countable basis upstairs. Thus the total space is Hausdorff and second countable. On an overlap the transition is
\(w\mapsto\rho_t(\gamma)w\), where \(\gamma\) is locally constant in \(y\). It is smooth in \((y,t)\) by hypothesis. The inverse and cocycle identities follow from the representation identities for each \(t\). Thus (S.3) is a smooth real vector bundle on the smooth manifold \(B\times I\), and its restriction at \(t\) is \(E_{\rho_t}\).

[Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) proves that every smooth vector bundle admits a covariant derivative, by the full frame-bundle correspondence. Choose one on \(\mathcal E\). Its parallel transport along
\[
[0,1]\longrightarrow B\times I,\qquad s\longmapsto(y,s)
\]
exists for every initial vector, by the same theorem and [Connections C.1](connections-and-parallel-transport.md#theorem-c-1). It is a linear isomorphism from the fibre at \((y,0)\) to the one at \((y,1)\); reverse transport is its inverse. [Connections C.2](connections-and-parallel-transport.md#theorem-c-2) proves smooth dependence on initial data and finite-dimensional smooth families of paths. In a coordinate chart of \(B\), the displayed paths are such a smooth family with parameter \(y\). Hence the fibre isomorphisms assemble to a smooth bundle map over \(B\), and reverse transport gives its smooth inverse. The auxiliary derivative need not preserve the original flat connections, which is why the conclusion concerns smooth vector bundles. □

**Theorem S.3 (bundle finiteness over a compact flat base).** For a fixed connected compact flat manifold \(B=P/\Gamma\) and fixed rank \(k\), only finitely many smooth vector-bundle isomorphism classes occur among the bundles \(E_\rho\) arising from orthogonal representations \(\rho:\Gamma\to\mathrm O(k)\).

**Proof.** For the point base the deck group is trivial and the only bundle is \(\mathbb R^k\), so suppose the base has positive dimension. By J.3 the deck group has a normal translation lattice
\(L\cong\mathbb Z^r\) of finite index \(m\), where \(r=\dim B\). Fix this subgroup once for the given base, and put
\[
K=\Gamma/(2mL).
\]
It is one fixed finite group, of order \(m(2m)^r\), by R.2.

For every \(\rho\), R.2 supplies a deformation to a representation \(\rho_1\) factoring through \(K\). Its formula is smooth for all real parameters, so S.2 applies and gives \(E_\rho\cong E_{\rho_1}\) as smooth bundles. By S.1 there are only finitely many orthogonal conjugacy classes of rank-\(k\) representations of \(K\). If two are conjugate by an orthogonal matrix \(U\), the formula
\[
[(p,z)]\longmapsto[(p,Uz)]
\]
is a well-defined bundle isomorphism between their bundles: the relation
\(U\rho_1(\gamma)=\rho'_1(\gamma)U\) makes it independent of representatives, and \(U^{-1}\) supplies its smooth inverse. Thus the finite representation list yields a finite list of possible bundles. □

**Theorem S.4 (finiteness for all complete flat manifolds).** For every fixed \(n\geq0\), the connected complete flat Riemannian \(n\)-manifolds have only finitely many diffeomorphism classes, and therefore only finitely many homeomorphism classes. Each is diffeomorphic to a complete flat manifold with finite linear holonomy.

**Proof.** Q.3 expresses every such manifold as \(E_\rho\) over a connected compact flat base \(B\) of some dimension \(r\), with fibre rank \(k=n-r\). There are only the finitely many possibilities \(0\leq r\leq n\). For \(r>0\), P.2 gives finitely many affine equivalence classes of compact flat bases; for \(r=0\) the base is a point.

Choose one base from each of these classes. Passing to the chosen base loses no possible total-space diffeomorphism class. Indeed an affine equivalence between bases lifts to an affine map of their Euclidean universal covers inducing an isomorphism of deck groups, by K.3. Compose the normal representation with this group isomorphism. The map on products given by the lifted affine map on the base factor and the identity on the vector factor is equivariant. It descends in the charts (Q.6) to a smooth diffeomorphism of the two bundle total spaces, covering the given base equivalence.

For each chosen base and each fixed rank \(n-r\), S.3 gives only finitely many smooth vector bundles. A smooth bundle isomorphism is in particular a diffeomorphism of total spaces. A finite union over the finitely many bases and dimensions proves the claimed diffeomorphism finiteness. Every diffeomorphism is a homeomorphism, so the homeomorphism assertion follows.

For the last statement start with one \(E_\rho\). R.2 and S.2 replace it, without changing its smooth bundle or total-space diffeomorphism type, by \(E_{\rho_1}\) with \(\rho_1(\Gamma)\) finite. Q.3 equips this new total space with its complete flat quotient metric. The linear part of each deck motion on \(P\times\mathbb R^k\) is the block matrix
\[
\begin{pmatrix}A_\gamma|_{\operatorname{dir}P}&0\\
0&\rho_1(\gamma)\end{pmatrix}.
\tag{S.4}
\]
The first block has finite image by J.3 for the compact base, and the second has finite image by construction. Thus these block matrices form a finite group.

To relate this directly to holonomy, lift a loop in the quotient to the Euclidean universal cover. Parallel vectors in its standard connection are constant in Euclidean coordinates, by [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) with zero connection matrix. If the lifted loop ends at \(\gamma x\), identifying its endpoint with \(x\) uses the inverse derivative of \(\gamma\). Hence the resulting linear parallel transport belongs to the inverses of the finite group (S.4). This proves finite linear holonomy. Dimension zero again consists only of a point. □

## T. Complete flat surfaces and shortest Klein-bottle loops

**Theorem T.1 (complete flat surfaces).** Every connected complete flat Riemannian surface is isometric to one of the following Euclidean quotients, with the indicated positive parameters:

- the plane \(\mathbb R^2\);
- a cylinder, generated by \((x,y)\mapsto(x+\ell,y)\);
- a torus \(\mathbb R^2/L\), where \(L\) is a full rank-two translation lattice;
- an infinite-width Möbius band, generated by \((x,y)\mapsto(x+\ell,-y)\);
- a Klein bottle, generated by the following two motions:

\[
g(x,y)=(x+\ell,-y),\qquad h(x,y)=(x,y+b),\qquad \ell,b>0.
\tag{T.1}
\]

Every quotient in this list is complete and flat. The torus and Klein bottle are the compact possibilities. The Möbius band and Klein bottle are nonorientable; the other three possibilities are orientable. The torus lattice need not be rectangular.

**Proof.** By Q.3 write the surface isometrically as \(\mathbb R^2/\Gamma\), with \(\Gamma\) a discrete torsion-free Euclidean group acting freely. Q.2 gives an invariant affine plane \(P\) of dimension \(r\in\{0,1,2\}\) on which the restricted action is free, discrete and cocompact. The orthogonal decomposition of Q.3 is an isometric decomposition of the ambient Euclidean space.

If \(r=0\), the group fixes a point, so freeness makes it trivial. The quotient is the plane.

If \(r=1\), an isometry of the affine line \(P\) has the form \(x\mapsto\varepsilon x+a\), where \(\varepsilon\in\{1,-1\}\). The sign \(-1\) gives the fixed point \(a/2\), so freeness excludes it. The restricted group consists of translations and, by G.3 and cocompactness, is generated by translation through a length \(\ell>0\). Restriction is faithful by Q.2. In orthonormal coordinates on \(P\) and its one-dimensional normal space, a generator of the full group therefore has the form
\[
(x,y)\longmapsto(x+\ell,\varepsilon y),\qquad \varepsilon\in\{1,-1\}.
\]
These are the cylinder and the infinite-width Möbius band.

Suppose \(r=2\). Then \(P=\mathbb R^2\) and the quotient is compact. An orientation-preserving orthogonal matrix \(A\ne I\) in dimension two has no nonzero fixed vector. Indeed, if it fixes a unit vector, orthogonality preserves its perpendicular line and determinant one forces the action on that line also to be \(+1\); then \(A=I\). Thus \(I-A\) is invertible when \(A\ne I\). The Euclidean motion \(x\mapsto Ax+p\) would fix \((I-A)^{-1}p\). Freeness consequently forces every orientation-preserving element of \(\Gamma\) to be a translation.

If every element preserves orientation, G.3 and cocompactness make \(\Gamma\) a full rank-two lattice, giving a flat torus. It remains to classify the case with an orientation-reversing element.

A real orthogonal \(2\)-by-\(2\) matrix of determinant \(-1\) has, for a unit first column \((a,c)\), second column \((c,-a)\). Its square is \(I\), its trace is zero, and its \(+1\) and \(-1\) eigenspaces are perpendicular lines. It is therefore a reflection. Moreover, any two orientation-reversing elements of \(\Gamma\) have the same linear part: their product preserves orientation and is a translation, so the product of their linear parts is \(I\); each of the two reflection matrices is its own inverse. Choose orthonormal coordinates in which this common reflection is
\[
A(x,y)=(x,-y).
\]
Every element of \(\Gamma\) now has linear part either \(I\) or \(A\).

Let \(L\) be the full translation lattice from J.3. It has rank two and is invariant under \(A\), by normality of the translation subgroup. There is \(v=(v_x,v_y)\in L\) with \(v_y\ne0\), since \(L\) spans the plane. Then
\[
v-Av=(0,2v_y)
\]
is a nonzero vertical vector in \(L\). Hence the vertical axis is a lattice subspace. O.1 shows that the horizontal projection of \(L\) is a discrete full rank-one lattice; write it as \(d\mathbb Z\) with \(d>0\).

For \(\gamma\in\Gamma\), let \(a(\gamma)\) be its horizontal displacement. All the linear parts fix the horizontal coordinate, so \(a:\Gamma\to\mathbb R\) is a homomorphism. A reversing element has square a translation, hence \(2a(\gamma)\in d\mathbb Z\). Translating elements already have \(a(\gamma)\in d\mathbb Z\). Thus
\[
d\mathbb Z\subset a(\Gamma)\subset \frac d2\mathbb Z.
\]
This is a nonzero discrete subgroup of the line, so G.3 gives
\(a(\Gamma)=\ell\mathbb Z\) for some \(\ell>0\).

The kernel of \(a\) consists exactly of vertical translations. In fact a reversing element with zero horizontal displacement would have the form
\((x,y)\mapsto(x,-y+c)\), fixing the entire line \(y=c/2\), which freeness forbids. The kernel is a nonzero discrete group of vertical translations, so G.3 gives a generator \(h(x,y)=(x,y+b)\), \(b>0\).

Choose an element with horizontal displacement \(\ell\). It must reverse orientation. If it were a translation, every element of \(\Gamma\), after multiplication by a suitable power of it, would lie in the translation kernel of \(a\). That would make all elements translations, contrary to the case under consideration. Our chosen element has the form \((x,y)\mapsto(x+\ell,-y+c)\). Moving the vertical origin to \(c/2\) puts it into the form \(g\) in (T.1). Every group element is uniquely
\[
h^p g^q(x,y)=(x+q\ell,(-1)^q y+pb),\qquad p,q\in\mathbb Z.
\tag{T.2}
\]
Existence follows by first matching horizontal displacement, then using the kernel; uniqueness follows from the two displayed coordinates. This proves the asserted form of the Klein-bottle quotient.

For clarity, these names can be read directly from fundamental regions. For the cyclic groups use the strip \([0,\ell]\times\mathbb R\), identifying the two vertical edges either directly or with \(y\mapsto-y\); these give the cylinder and Möbius band. For (T.2) use the rectangle \([0,\ell]\times[0,b]\). Identify the horizontal edges by translation, and the vertical edges by \(y\mapsto-y\) modulo \(b\); this is the Klein-bottle gluing. A lattice parallelogram gives the usual torus by G.3.

Conversely, the cyclic actions above are free because every nontrivial power has nonzero horizontal displacement. For (T.2), a nonidentity element either has \(q\ne0\), giving nonzero horizontal displacement, or has \(q=0,p\ne0\), giving nonzero vertical displacement. Thus this action also is free. Bounded translation parts bound the relevant integers \(q\), or \(p,q\), so each of these groups is discrete. For a lattice this is part of G.3. J.1 gives proper discontinuity. The standard Euclidean metric descends in covering charts and has the standard zero-coefficient connection as Levi-Civita connection by [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). Its geodesics lift to straight Euclidean lines, which are defined for all time; equivalently this is the complete quotient construction of G.2. Hopf–Rinow B.2 then gives metric completeness. The metric is flat in these same charts.

An orientation on a quotient pulls back to a deck-invariant orientation on the connected plane. Relative to the usual orientation its sign is locally constant and hence constant, so such an orientation is possible only when every deck transformation has positive determinant. Conversely the usual plane orientation descends through the covering charts whenever all deck transformations have positive determinant. This gives exactly the orientation assertions.

A torus is compact by G.3. In (T.2) the translations generated by \(g^2\) and \(h\) form a full rank-two lattice of index two, so its compact torus maps onto the Klein bottle, making that quotient compact too. The plane is noncompact. On the cylinder and Möbius band the function \([(x,y)]\mapsto |y|\) is continuous and unbounded, so neither quotient is compact. This completes all the classifications asserted. □

**Exercise T.2 (shortest noncontractible loops on a flat Klein bottle).** On the Klein bottle (T.1), find the least length of a noncontractible piecewise smooth loop based at \([(x,y)]\). Then find the least length of a noncontractible closed geodesic when the basepoint is free to vary.

**Solution.** Put
\[
\Delta(y)=\min_{p\in\mathbb Z}|2y-pb|,\qquad 0\leq\Delta(y)\leq b/2.
\tag{T.3}
\]
The minimum exists: one of the two integers adjacent to \(2y/b\) is nearest. The answers are respectively
\[
\boxed{\ \min\{b,\,2\ell,\,\sqrt{\ell^2+\Delta(y)^2}\}\ },
\qquad
\boxed{\ \min\{b,\ell\}\ }.
\tag{T.4}
\]

To prove the first formula, lift a based loop starting at \(z=(x,y)\). By the covering and homotopy lifting results in [Flat connections D.1–D.2](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1), it ends at a unique deck translate \(h^pg^qz\). The loop is contractible exactly when that translate is \(z\). For the forward implication lift a based contraction. For the reverse implication a closed lift contracts in the plane by the straight homotopy to \(z\), and projection contracts the original loop. Freeness makes the endpoint condition equivalent to \((p,q)=(0,0)\).

The covering is a local isometry, so lifting preserves length. The length of a Euclidean piecewise smooth path is at least the norm of its endpoint displacement, by the integration inequality of [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Conversely the straight segment to any deck translate projects to a based piecewise smooth loop of precisely that length. Consequently the required minimum is the minimum, over \((p,q)\ne(0,0)\), of
\[
|h^pg^qz-z|
 =\sqrt{q^2\ell^2+\bigl(pb+((-1)^q-1)y\bigr)^2}.
\tag{T.5}
\]
When \(q=0,p\ne0\), the minimum is \(b\). When \(q\) is nonzero and even, it is \(2\ell\), obtained at \(q=\pm2,p=0\). When \(q\) is odd, its absolute value is at least one and the smallest vertical difference is \(\Delta(y)\); the minimum is therefore \(\sqrt{\ell^2+\Delta(y)^2}\). Each minimum is attained, proving the first part of (T.4). Changing the representative of the basepoint does not change \(\Delta\), since \(y\) changes to \(\pm y+pb\).

Every noncontractible loop, at any basepoint, has length at least \(\min\{b,\ell\}\) by this formula. This lower bound is attained by a closed geodesic. The vertical line through any point, divided by \(h\), gives one of length \(b\); the horizontal axis \(y=0\), divided by \(g\), gives one of length \(\ell\). Their Euclidean tangent vectors agree under the endpoint deck derivatives, so the projections are smooth periodic geodesics, not merely loops with a corner. Their lifted endpoints differ by a nonidentity deck transformation, so both are noncontractible. Taking the shorter proves the second formula. □

## Further reading
- Werner Ballmann, [*Basic Differential Geometry: Semi-Riemannian Metrics*, author lecture notes, 29 May 2003](https://people.mpim-bonn.mpg.de/hwbllmnn/archiv/dg2srm03.pdf), especially the curvature identities, sectional and Ricci curvature, quadric models, and Schur exercises.
- Urs Lang, [*Lecture Notes on Riemannian Geometry*, ETH Zürich, 16 June 2020](https://metaphor.ethz.ch/x/2020/fs/401-3532-08L/sc/DG2_16June2020.pdf), §§3.4–3.7 and §§4.7–4.11, for geodesic variations, Jacobi fields, complete constant-curvature geometry and spherical quotients.

- Daniel Allcock, [*Spherical Space Forms Revisited*, author manuscript, 9 September 2016](https://web.ma.utexas.edu/users/allcock/research/ssforms.pdf), Lemma 2.2, for the character-space argument behind the two-prime restriction.
- Joseph A. Wolf, [*On the Homogeneity Conjecture*, author manuscript, 28 March 2023](https://math.berkeley.edu/~jawolf/publications.pdf/paper_201.pdf), §2B, for the scalar-algebra description of homogeneous spherical quotients.

- William M. Goldman, [*Geometric structures on manifolds*, author manuscript, 11 December 2021](https://math.umd.edu/~wmg/gstom.pdf), §§1.4.1, 6.2.1, 8.2 and 8.3.2, for parallel metrics, translation quotients, affine-flat connections and geodesic completeness.
- Oliver Baues and William M. Goldman, [*Is the deformation space of complete affine structures on the 2-torus smooth?*, author manuscript, 12 January 2004](https://math.umd.edu/~wmg/torus.pdf), §3, especially equations (3.2)–(3.3), for the affine shear action.

- Bruno Martelli, [*An Introduction to Geometric Topology*, free author edition, version 4, September 2025](https://people.dm.unipi.it/martelli/Geometric_topology.pdf), §3.4.8 and §4.4, especially Proposition 3.4.12, Lemma 4.4.1 and results 4.4.8–4.4.11, for flat surface quotients, small rotations and translation lattices.

- Ho Yiu Chung, [*Bieberbach groups and fibering flat manifolds of diagonal type*, doctoral thesis, University of Southampton, January 2020, free institutional edition](https://eprints.soton.ac.uk/452883/1/Final_Thesis_Chung.pdf), §§2.3–2.4, especially Theorems 2.3.18, 2.4.1, 2.4.2 and 2.4.9 and Proposition 2.4.5, for finite extensions, crystallographic-group realization, integral matrix groups, the translation-subgroup criterion and affine conjugacy.

- Michał Sadowski, [*Topological and affine structure of complete flat manifolds*, arXiv:math/0502449v1](https://arxiv.org/pdf/math/0502449v1), §§1–2, especially Propositions 2.1–2.2 and Theorem 2.1, for the normal-bundle description and finiteness of complete flat manifolds.
