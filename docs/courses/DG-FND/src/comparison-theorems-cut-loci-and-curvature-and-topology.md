# Comparison theorems, cut loci and curvature and topology

This chapter develops Jacobi comparison, cut loci, the global consequences of curvature bounds, closed geodesics, Synge's theorem, barycentres and homogeneous spaces.

All metrics are positive definite and all manifolds are connected, smooth and without boundary. We use the curvature convention
\[
R(U,V)W=\nabla_U\nabla_VW-\nabla_V\nabla_UW-\nabla_{[U,V]}W,
\qquad K(U,V)=\langle R(U,V)V,U\rangle
\]
for orthonormal \(U,V\). The Jacobi equation is \(J''+R(J,T)T=0\). The complete variation and index-form arguments are in [Jacobi fields A.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-1), [Jacobi fields A.4](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-4), [Jacobi fields B.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#lemma-b-1) and [Jacobi fields D.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-d-2). Completeness is required only where stated.

## A. Curvature and radial spreading

**Theorem A.1 (Rauch comparison with unequal dimensions).** Let \(\gamma_M,\gamma_N:[0,b]\to M,N\) be unit-speed geodesics, with
\(\dim M\geq\dim N\geq1\). Suppose that, at each common time, every plane containing \(\gamma_M'\) has sectional curvature at least that of every plane containing \(\gamma_N'\). Suppose that \(\gamma_M\) has no conjugate time in \((0,b)\). For normal Jacobi fields \(X,Y\) along these geodesics satisfying
\[
X(0)=Y(0)=0,\qquad |X'(0)|=|Y'(0)|,
\]
one has
\[
|X(t)|\leq |Y(t)|\qquad(0\leq t\leq b).
\tag{A.1}
\]
There is no conjugate time for \(\gamma_N\) in \((0,b)\). The norm inequality also holds for fields with zero initial value whose initial derivatives have equal norms and equal tangential components.

**Proof.** Parallel transport is an isometry by [Connections D.2](connections-and-parallel-transport.md#theorem-d-2) and [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1). If the common initial norm is zero, Jacobi uniqueness, [Jacobi fields A.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-1), makes both normal fields zero. Assume that norm is positive. Then \(X(r)\ne0\) for \(0<r<b\), by the hypothesis and the definition of conjugacy in [Jacobi fields B.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-b-2).

Fix such an \(r\), put \(\lambda=|Y(r)|\), \(\mu=|X(r)|\), and choose a parallel orthonormal frame of the normal bundle of \(\gamma_N\). If \(\lambda>0\), choose its first vector to be \(Y(r)/\lambda\) at \(r\); if \(\lambda=0\), any first vector will do. In the normal bundle of \(\gamma_M\), choose an orthonormal system of the same size with first vector \(X(r)/\mu\) at \(r\), and transport it parallelly. Gram–Schmidt and parallel transport provide these choices; see [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2) and [Connections D.2](connections-and-parallel-transport.md#theorem-d-2).

Transfer the coordinates of \(Y\) in the first frame to the second system, obtaining a field \(Z\) along \(\gamma_M\). Then
\[
|Z|=|Y|,\quad |Z'|=|Y'|,\quad Z(0)=0,\quad
Z(r)=\frac{\lambda}{\mu}X(r).
\]
These assertions include \(\lambda=0\). The curvature assumption, including at zero field values by continuity, gives
\[
I_N(Y,Y)\geq I_M(Z,Z)
 \geq \frac{\lambda^2}{\mu^2}I_M(X,X).
\tag{A.2}
\]
The second inequality is precisely [Jacobi fields D.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-d-2) on \([0,r]\); it is available on the higher-curvature geodesic. Integration by parts for the two Jacobi fields, [Jacobi fields B.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#lemma-b-1), turns (A.2) into
\[
|X(r)|^2\langle Y(r),Y'(r)\rangle
 \geq |Y(r)|^2\langle X(r),X'(r)\rangle.
\]
Consequently \((|Y|^2/|X|^2)'\geq0\) on \((0,b)\). This calculation does not divide by \(|Y|\) and therefore does not assume the conclusion that \(Y\) has no later zero. In a parallel frame, differentiability at zero gives
\(X(t)=tX'(0)+o(t)\) and \(Y(t)=tY'(0)+o(t)\). The ratio tends to one. The fundamental theorem in [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) now gives (A.1) in the open interval, and continuity gives both endpoints.

For any nonzero normal initial derivative downstairs, choose one of the same norm upstairs and apply (A.1). Its upstairs field never vanishes in \((0,b)\), so neither does the downstairs one. [Jacobi fields B.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-b-2) says every endpoint-vanishing field is normal; this rules out all conjugate times downstairs.

Finally write arbitrary fields with zero initial value as their normal parts plus \(atT\). Their tangential coefficients are affine by [Jacobi fields B.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-b-2). Equal tangential initial components give the same \(a\); equal total initial norms give equal normal initial norms. Apply the normal inequality and add \(a^2t^2\) to the squared norms. □

**Corollary A.2 (constant-curvature and exponential bounds).** Define
\[
s_k(t)=
\begin{cases}
\sin(\sqrt{k}t)/\sqrt{k},&k>0,\\
t,&k=0,\\
\sinh(\sqrt{-k}t)/\sqrt{-k},&k<0.
\end{cases}
\]
In dimension \(n\geq2\), along a unit-speed geodesic whose radial sectional curvatures satisfy
\(k_0\leq K\leq k_1\), every normal Jacobi field with \(J(0)=0\) satisfies
\[
s_{k_1}(t)|J'(0)|\leq |J(t)|
 \leq s_{k_0}(t)|J'(0)|.
\tag{A.3}
\]
The interval is \(0\leq t<\pi/\sqrt{k_1}\) if \(k_1>0\), or every available nonnegative time if \(k_1\leq0\). There is no positive conjugate time in that interval. If \(k_0>0\) and the geodesic exists through \(\pi/\sqrt{k_0}\), its first conjugate time \(\tau\) exists and satisfies
\[
\frac{\pi}{\sqrt{k_1}}\leq\tau\leq\frac{\pi}{\sqrt{k_0}}.
\tag{A.4}
\]
For \(u\) unit, \(r>0\) in the interval of (A.3), and \(w=au+w_\perp\),
\[
a^2+\frac{s_{k_1}(r)^2}{r^2}|w_\perp|^2
\leq |(d\exp_p)_{ru}w|^2
\leq a^2+\frac{s_{k_0}(r)^2}{r^2}|w_\perp|^2.
\tag{A.5}
\]

**Proof.** The complete constant-curvature models and their radial geodesics are supplied by [Sectional curvature C.1](sectional-curvature-and-space-forms.md#theorem-c-1) and [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2). Their normal Jacobi fields with initial value zero are \(s_k(t)\) times a parallel field, by [Jacobi fields B.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#example-b-3); [Sectional curvature B.2](sectional-curvature-and-space-forms.md#lemma-b-2) proves the stated functions and their first zeros.

First take the \(k_1\)-model as the higher-curvature manifold in A.1. It has no conjugate time before the first positive zero of \(s_{k_1}\), or at any positive time when \(k_1\leq0\). This proves the lower bound and the nonconjugacy assertion for the given geodesic. Now take that geodesic as the higher-curvature one and the \(k_0\)-model as the lower-curvature one. A.1 gives the upper bound on every compact subinterval of the stated interval. At zero both inequalities follow by continuity.

If \(k_0>0\), the radial Ricci trace is at least \((n-1)k_0\), by [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1). [Jacobi fields F.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-f-2) gives a conjugate time no later than \(\pi/\sqrt{k_0}\). [Jacobi fields C.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#lemma-c-1) excludes a sufficiently short initial interval, and [Jacobi fields C.4](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#lemma-c-4) proves finiteness of the conjugate times on a compact interval. Hence a first one exists. The already proved exclusion gives its lower bound in (A.4).

For (A.5), [Jacobi fields B.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-b-2) identifies
\(J(t)=(d\exp_p)_{tu}(tw_\perp)\) with the normal Jacobi field of initial derivative \(w_\perp\). Divide (A.3) at \(t=r\) by \(r\). Gauss's identity, [Riemannian connections B.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-1), says that \((d\exp_p)_{ru}u\) is unit and orthogonal to the image of \(w_\perp\). Squaring and adding the tangential contribution proves (A.5). At \(r=0\) its limiting assertion is the identity differential, [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). □

**Exercise A.3 (a tangent embedding and the speed hypothesis).** Under A.1, let \(H:T_{\gamma_N(0)}N\to T_{\gamma_M(0)}M\) be a linear isometric embedding taking \(\gamma_N'(0)\) to \(\gamma_M'(0)\). Prove the exponential-differential comparison, and show why unrelated affine speeds cannot replace the common unit-speed assumption.

**Solution.** For any \(w\), choose the Jacobi fields with initial derivatives \(w,Hw\) and zero initial values. The tangential components and norms of those derivatives agree. A.1 and [Jacobi fields B.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-b-2) therefore give, for \(0<t\leq b\),
\[
\left|(d\exp_{\gamma_M(0)})_{t\gamma_M'(0)}Hw\right|
\leq
\left|(d\exp_{\gamma_N(0)})_{t\gamma_N'(0)}w\right|.
\tag{A.6}
\]
The conclusion at \(t=0\) is equality.

For the speed issue take two unit spheres. Give the geodesic called the higher-curvature one speed \(1\), and the other speed \(2\). Their sectional curvatures are both \(1\). Normal parallel unit fields \(E,F\) produce Jacobi fields
\[
X(t)=\sin t\,E(t),\qquad
Y(t)=\tfrac12\sin(2t)\,F(t)
\]
with initial derivative norm one, since their equations are respectively
\(X''+X=0\) and \(Y''+4Y=0\). These formulas follow from the constant-curvature equation in [Jacobi fields B.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#example-b-3) with the velocity norm retained. For \(0<t<\pi/2\),
\(|Y(t)|=\sin t\cos t<\sin t=|X(t)|\); the required comparison fails although the higher-curvature geodesic has no conjugate time there. The comparison is between curvature operators with the same velocity normalization. □

## B. The last minimizing time

Assume here that \(M\) is complete and \(\dim M\geq1\). Fix \(p\), let \(S_pM\) be its unit tangent sphere, and set
\[
\gamma_u(t)=\exp_p(tu),\qquad
c(u)=\sup\{t\geq0:d(p,\gamma_u(t))=t\}.
\tag{B.1}
\]
The value \(+\infty\) is allowed. A finite endpoint \(\gamma_u(c(u))\) is a cut point, and their set is \(\operatorname{Cut}(p)\). The word “minimizer” below refers to a geodesic segment parametrized by arc length; equality for arbitrary path parametrizations is treated in [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5).

**Theorem B.1 (the cut-point alternatives).** Each ray minimizes exactly for \(0\leq t\leq c(u)\), with the upper endpoint omitted only when infinite. The values \(c(u)\) have a common positive lower bound. Two distinct minimizing segments from \(p\) to the same point cannot continue to minimize past that point. At a finite cut time either the exponential differential is singular or there is a second minimizing segment. At every time \(0<t<c(u)\) the segment is the unique minimizer and the exponential differential is nonsingular.

**Proof.** [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) supplies the global exponential and minimizing segments between all endpoints. [Hopf–Rinow A.1](completeness-and-the-hopf-rinow-theorem.md#lemma-a-1) supplies one positive normal radius at \(p\) within which the radial segments minimize. This radius works for every \(u\).

If the equality in (B.1) holds at \(t\), it holds at every \(s\leq t\). Indeed,
\[
t=d(p,\gamma_u(t))
\leq d(p,\gamma_u(s))+(t-s)\leq s+(t-s)=t.
\]
Both inequalities must be equalities. Distance is continuous by [Riemannian connections A.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-2), so the set of such times is closed. This proves the assertion about its interval and finite endpoint.

Suppose two distinct minimizers arrive at \(q\). Their terminal unit velocities differ: if equal, backwards uniqueness for the geodesic equation, [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1), identifies both entire segments. Following the first segment and then the continuation of the second creates a corner. If that continuation minimized past \(q\), the broken path would have the same minimizing length. [Hopf–Rinow A.3](completeness-and-the-hopf-rinow-theorem.md#lemma-a-3) excludes a corner in such a path, a contradiction. Thus neither segment continues minimizing.

At an interior time \(t<c(u)\), another minimizer would contradict this conclusion by considering a slightly longer still minimizing radial segment. A singular exponential differential there gives a conjugate time by [Jacobi fields B.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-b-2), and [Jacobi fields F.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-f-1) would then shorten that longer segment. Hence the interior assertions hold.

Now let \(c=c(u)<\infty\). Suppose both that \((d\exp_p)_{cu}\) is invertible and that the minimizing segment to \(q=\gamma_u(c)\) is unique. Choose \(t_j>c\) tending to \(c\). Let
\[
r_j=d(p,\gamma_u(t_j))<t_j,\qquad
\exp_p(r_jv_j)=\gamma_u(t_j),\qquad |v_j|=1,
\]
using a minimizing segment. Continuity gives \(r_j\to c>0\). Compactness of the unit sphere, [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), gives a subsequence \(v_j\to v\). Its limit satisfies
\(\exp_p(cv)=q\), and its radial path has length \(c=d(p,q)\). Uniqueness therefore gives \(v=u\). The inverse function theorem, [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), makes \(\exp_p\) injective on a neighbourhood of \(cu\). Both \(r_jv_j\) and \(t_ju\) lie there for large \(j\), yet have equal exponential images and unequal norms. This contradiction proves the alternatives. □

**Theorem B.2 (continuity of cut time).** The function
\[
c:S_pM\longrightarrow(0,\infty]
\]
is continuous, with the extended topology at infinity.

**Proof.** We prove both bounds for a sequence \(u_j\to u\). If \(c(u)<t<\infty\), then
\(d(p,\exp_p(tu))<t\). This strict inequality persists for \(u_j\) close to \(u\), by smoothness of the exponential and continuity of distance. Thus \(c(u_j)<t\), proving
\(\limsup c(u_j)\leq c(u)\) when the latter is finite.

For the lower bound, fix \(0<t<c(u)\), also permitting \(c(u)=\infty\). Suppose a subsequence has \(c_j=c(u_j)\leq t\). By the uniform positive lower bound in B.1 and compactness of a real interval, pass to one with \(c_j\to a\), where \(0<a\leq t<c(u)\). The differential at \(au\) is nonsingular by B.1. In a neighbourhood of \(au\), the inverse function theorem makes \(\exp_p\) injective with nonsingular differential. Eventually \(c_ju_j\) lies in that neighbourhood. The singular alternative at its cut time is impossible, so B.1 supplies a different minimizing initial direction \(v_j\ne u_j\) with
\[
\exp_p(c_jv_j)=\exp_p(c_ju_j).
\]
Choose a convergent subsequence \(v_j\to v\). Passing to the limit makes the radial segment of length \(a\) in direction \(v\) a minimizer to \(\exp_p(au)\). This endpoint precedes the cut time in direction \(u\), so B.1 makes that minimizer unique and forces \(v=u\). Consequently both \(c_jv_j\) and \(c_ju_j\) eventually belong to the same injectivity neighbourhood. Their equal images contradict \(v_j\ne u_j\). Therefore \(c(u_j)>t\) eventually.

For finite \(c(u)\), let \(t\) increase to it. For infinite \(c(u)\), take every finite \(t\). Together with the upper bound, these are exactly sequential continuity in the stated topology. To see that this suffices, compose with the homeomorphism \(r\mapsto1/r\), with \(1/\infty=0\); the target becomes a metric subspace of \([0,\infty)\). In metric spaces failure of continuity supplies points within \(1/j\) whose images stay a fixed positive distance apart. The sequential conclusion excludes this failure. □

**Theorem B.3 (the normal domain and compactness).** Put
\[
D_p=\{0\}\cup\{ru:u\in S_pM,\ 0<r<c(u)\}.
\]
Then
\[
\exp_p:D_p\longrightarrow M\setminus\operatorname{Cut}(p)
\tag{B.2}
\]
is a diffeomorphism. The cut locus is closed, \(D_p\) is homeomorphic to \(\mathbb R^n\), and \(M\) is compact if and only if every cut time is finite.

**Proof.** Define \(a(u)=1/c(u)\), setting \(a(u)=0\) at infinite cut time. By B.2 it is continuous; by the uniform lower bound in B.1 it is bounded. For a nonzero vector \(v=ru\), membership in \(D_p\) is the strict inequality \(ra(u)<1\), so \(D_p\) is open away from zero. The common normal ball makes it open at zero as well.

Every point has a minimizing radial segment by [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2). Its length \(r\) satisfies \(r\leq c(u)\). If its endpoint is not a cut point then the inequality is strict, so it lies in the image in (B.2). Conversely a point reached before a cut time cannot also be a cut point: a cut representation would be a minimizer of the same length; it either is the same radial segment, contradicting the strict inequality, or is a second one, contrary to B.1. That theorem also proves injectivity of (B.2) and nonsingularity away from zero. At zero use [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). Local smooth inverses from [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) therefore glue to the global inverse. In particular the complement of the cut locus is open.

Identify \(T_pM\) with \(\mathbb R^n\) by an orthonormal basis. The maps
\[
su\longmapsto\frac{s}{1+s\,a(u)}u,\qquad
ru\longmapsto\frac{r}{1-r\,a(u)}u
\tag{B.3}
\]
are inverse radial maps from \(T_pM\) to \(D_p\) and back. They fix zero. Away from zero continuity follows from the formulas and the positive denominators. At zero, the first norm is at most \(s\), and the second is at most \(2r\) once \(r\sup a<1/2\). Thus both are continuous there, proving the homeomorphism assertion without requiring differentiability of cut time.

If \(M\) is compact, its diameter is finite by continuity of distance on \(M\times M\), or a finite bounded ball cover. Every minimizing segment has length at most that diameter, so all cut times are finite. Conversely, if all values are finite, B.2 makes \(c\) an ordinary continuous real function on the compact unit sphere. It is bounded by a finite \(C\). Every point is the exponential of a minimizing vector of norm at most \(C\), so \(M\) is a continuous image of the closed radius-\(C\) ball. This ball is compact by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), and hence so is \(M\). □

## C. A global exponential chart in nonpositive curvature

**Theorem C.1 (Cartan–Hadamard, with the metric estimate).** Let \(M\) be complete with sectional curvature \(K\leq0\). For every \(p\),
\[
|(d\exp_p)_v w|\geq |w|
\qquad(v,w\in T_pM).
\tag{C.1}
\]
The pullback metric \(h=\exp_p^*g\) is a complete Riemannian metric on \(T_pM\), and \(\exp_p:T_pM\to M\) is a covering. If \(M\) is simply connected it is a diffeomorphism, and every two points are joined by exactly one geodesic segment with parameter interval \([0,1]\).

**Proof.** For \(v=ru\ne0\), use the lower bound in (A.5) with \(k_1=0\). A finite lower bound \(k_0\) on the radial sectional curvatures exists on each compact interval: in a parallel frame the curvature matrix has continuous entries and hence bounded operator norm, by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Thus (A.5) applies and gives (C.1). At zero use the identity differential, [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). In dimension one the normal component is absent and Gauss's identity, [Riemannian connections B.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-1), gives equality directly. A connected zero-dimensional manifold is a point and every conclusion is immediate.

In positive dimension (C.1) makes every differential injective and therefore bijective. The smooth pullback \(h\) is positive definite and satisfies \(h_v(w,w)\geq|w|^2\). Integration over every piecewise smooth path gives
\[
d_h(v,z)\geq|v-z|.
\tag{C.2}
\]
An \(h\)-Cauchy sequence is consequently Euclidean Cauchy, and converges to some \(v\). On a fixed small closed Euclidean ball about \(v\), smoothness bounds \(h_z(w,w)\leq A^2|w|^2\) for one finite \(A\). The straight segment from a sufficiently late sequence point to \(v\) lies in that ball and has \(h\)-length at most \(A\) times its Euclidean length. Thus the sequence converges also in \(d_h\). This proves completeness.

The exponential is a local isometry by the definition of \(h\). [Hopf–Rinow E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4) makes it a surjective smooth covering. If \(M\) is simply connected, [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) implies that a connected cover has one sheet: its fundamental-group subgroup is a subgroup of the trivial group, and the universal cover in [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) is then the base itself. A bijective smooth covering is a diffeomorphism.

Apply this at either endpoint. Any geodesic on \([0,1]\) from \(p\) to \(q\) equals \(t\mapsto\exp_p(tv)\) by [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1). The unique inverse vector \(v=\exp_p^{-1}q\) proves uniqueness. [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) supplies a minimizing segment, so this unique geodesic is minimizing. □

A complete simply connected manifold with \(K\leq0\) is called a **Hadamard manifold**.

**Theorem C.2 (strong convexity of squared distance).** On a Hadamard manifold, \(f_q(x)=\tfrac12d(q,x)^2\) is smooth, including at \(x=q\), and
\[
\operatorname{Hess}f_q(v,v)\geq |v|^2.
\tag{C.3}
\]
For the geodesic \(\eta:[0,1]\to M\) from \(x\) to \(y\),
\[
d(q,\eta(t))^2\leq (1-t)d(q,x)^2+t\,d(q,y)^2
-t(1-t)d(x,y)^2.
\tag{C.4}
\]
Moreover \((q,x)\mapsto\exp_q^{-1}x\), regarded as a vector based at \(q\), is smooth.

**Proof.** Consider the smooth map
\[
TM\longrightarrow M\times M,\qquad (q,w)\longmapsto(q,\exp_qw).
\]
By C.1 it is bijective. In tangent-bundle coordinates its differential is block triangular with identity in the base block and the invertible exponential differential in the fibre block. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes it a local diffeomorphism; its local inverses glue to a smooth global inverse. This proves the final assertion. The minimizing and constant-speed conclusions of C.1 show that
\[
f_q(x)=\tfrac12|\exp_q^{-1}x|_q^2,
\]
which proves smoothness everywhere.

We use \(\operatorname{Hess}f(V,V)=V(Vf)-(\nabla_VV)f\); along an affine geodesic this is the ordinary second derivative of \(f\). Choose a geodesic \(x(s)\) with \(x(0)=x\) and \(x'(0)=v\). Form the smooth variation
\[
F(s,t)=\exp_q\!\left(t\exp_q^{-1}x(s)\right),\qquad 0\leq t\leq1.
\]
Its energy is exactly \(f_q(x(s))\). The central field \(J=\partial_sF|_0\) has \(J(0)=0,J(1)=v\). Both endpoint accelerations in [Jacobi fields A.4](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-4) vanish: the first endpoint is fixed, and the second follows the geodesic \(x(s)\). Hence
\[
\operatorname{Hess}f_q(v,v)
=\int_0^1\left(|J'|^2-\langle R(J,T)T,J\rangle\right)\,dt
\geq\int_0^1|J'|^2\,dt.
\tag{C.5}
\]
Here the curvature term is nonpositive: its tangential component vanishes, and its normal component is a radial sectional curvature times \(|T|^2|J^\perp|^2\), by [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1). The conclusion also holds when the central geodesic is constant.

Parallelly identify all tangent spaces along the central geodesic with the one at \(t=1\). In those coordinates \(v=\int_0^1J'(t)\,dt\). For any continuous vector function \(z\) on this interval,
\[
\int_0^1|z|^2-\left|\int_0^1z\right|^2
=\int_0^1\left|z-\int_0^1z\right|^2\geq0,
\]
by expansion and [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Apply this to the coordinates of \(J'\) to finish (C.3).

Put \(L=d(x,y)\) and \(r(t)=f_q(\eta(t))\). The affine geodesic has speed \(L\), so (C.3) gives \(r''(t)\geq L^2\). Thus \(r(t)-L^2t^2/2\) is convex. For completeness, a function with nonnegative second derivative has nondecreasing first derivative by the fundamental theorem; the mean derivative on \([0,t]\) is then at most that on \([t,1]\), so its value at \(t\) is at most the chord between its endpoint values. Apply this to the displayed function and multiply by two to obtain (C.4). □

## D. Positive Ricci curvature and its quantitative hypothesis

**Theorem D.1 (Bonnet–Myers).** Suppose \(n\geq2\), \(M\) is complete, and
\[
\operatorname{Ric}(v,v)\geq(n-1)k|v|^2
\qquad\text{for some constant }k>0.
\tag{D.1}
\]
Then
\[
\operatorname{diam}M\leq\frac{\pi}{\sqrt{k}},
\]
\(M\) is compact, and its fundamental group is finite.

**Proof.** Let a minimizing unit-speed segment have length \(L>0\). Every endpoint-fixed piecewise smooth field \(V\) along it is realized by a variation, [Jacobi fields A.2](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#lemma-a-2). The energy of any member of that variation is at least \(L/2\): on the time interval of length \(L\),
\[
\int_0^L |T_s|^2\,dt\geq\frac1L
 \left(\int_0^L|T_s|\,dt\right)^2\geq L.
\]
The first inequality follows by expanding the integral of
\((|T_s|-L^{-1}\int|T_s|)^2\); the second uses that any competing path has length at least the endpoint distance \(L\). The central energy is \(L/2\). The second variation formula, [Jacobi fields A.4](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-4), consequently gives \(I(V,V)\geq0\).

Choose a parallel orthonormal normal frame \(E_1,\ldots,E_{n-1}\), and put
\(V_j(t)=\sin(\pi t/L)E_j(t)\). Trace the curvature term using [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) and use (D.1):
\[
\begin{aligned}
0\leq\sum_{j=1}^{n-1}I(V_j,V_j)
&=\int_0^L\left((n-1)\frac{\pi^2}{L^2}\cos^2(\pi t/L)
-\operatorname{Ric}(T,T)\sin^2(\pi t/L)\right)\,dt\\
&\leq\frac{(n-1)L}{2}\left(\frac{\pi^2}{L^2}-k\right).
\end{aligned}
\tag{D.2}
\]
The sine and cosine integrals are \(L/2\), as follows from their derivative identities in [Sectional curvature B.2](sectional-curvature-and-space-forms.md#lemma-b-2) and the fundamental theorem. Thus \(L\leq\pi/\sqrt{k}\). [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) supplies such a minimizing segment for every pair of points, proving the diameter bound and compactness.

[Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) constructs the connected smooth universal cover \(\pi:\widetilde M\to M\). Give it the pullback metric. This is a Riemannian covering and is complete by [Hopf–Rinow E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4). A local isometry preserves the Levi-Civita connection by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Apply that identity twice and subtract the bracket term in the curvature definition: it also preserves curvature, and taking its trace in corresponding orthonormal frames preserves Ricci. Thus (D.1) holds upstairs. The same diameter argument makes \(\widetilde M\) compact. The fibre over \(p\) is closed and discrete: it is the inverse image of the closed singleton \(\{p\}\), and every covering chart isolates each point of that fibre. A compact discrete space is finite, since the cover by its singleton open subsets has a finite subcover. By the explicit path-class and deck construction in [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) this fibre is in bijection with \(\pi_1(M,p)\). Hence the fundamental group is finite. □

**Theorem D.2 (equality along a longest permitted minimizing segment).** Under (D.1), if a minimizing unit-speed geodesic has length \(L=\pi/\sqrt{k}\), then every radial sectional curvature along it is exactly \(k\). Equivalently,
\[
R(E,T)T=kE
\tag{D.3}
\]
for every normal vector \(E\) along the segment, including its endpoints.

**Proof.** Each summand in (D.2) is nonnegative and their sum is at most zero. Thus every \(V_j=\sin(\sqrt{k}t)E_j\) has \(I(V_j,V_j)=0\). The entire endpoint-fixed index form is nonnegative by the beginning of D.1. For any endpoint-fixed field \(W\) and real \(s\),
\[
0\leq I(V_j+sW,V_j+sW)=2sI(V_j,W)+s^2I(W,W).
\]
Both signs of sufficiently small \(s\) force \(I(V_j,W)=0\). By [Jacobi fields B.1](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#lemma-b-1) each \(V_j\) is therefore Jacobi. Substituting its expression into the Jacobi equation yields
\[
\sin(\sqrt{k}t)\bigl(R(E_j,T)T-kE_j\bigr)=0.
\]
The sine is positive for \(0<t<L\), so (D.3) holds for each vector of the parallel normal basis there. Linearity gives it for every normal vector. Continuity of curvature and the frame extends it to the endpoints. Taking its inner product with a unit normal vector gives the stated sectional curvature. □

**Example D.3 (everywhere positive Ricci curvature without a uniform bound).** On \(\mathbb R^2\), the smooth metric
\[
g=dx^2+dy^2+4(x\,dx+y\,dy)^2
\tag{D.4}
\]
is complete and noncompact, and
\[
K(x,y)=\frac{4}{(1+4x^2+4y^2)^2}>0,\qquad
\operatorname{Ric}=K g.
\tag{D.5}
\]
Thus pointwise strict positivity of Ricci does not imply the conclusions of D.1.

**Proof.** Formula (D.4) is smooth and positive definite, with \(g\geq dx^2+dy^2\). A \(g\)-Cauchy sequence is Euclidean Cauchy. On a Euclidean ball about its limit, the coefficients are bounded, so straight segments prove convergence in \(g\), exactly by the two inequalities used in C.1. Hence the metric is complete. Its topology is the ordinary topology of \(\mathbb R^2\), by [Riemannian connections A.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-2), and the space is not compact; the sequence \((j,0)\) has no convergent subsequence.

For \(r=\sqrt{x^2+y^2}>0\), polar coordinates give
\[
g=(1+4r^2)\,dr^2+r^2\,d\theta^2.
\]
Set \(t(r)=\int_0^r\sqrt{1+4s^2}\,ds\). Its derivative is positive, so it has a smooth local inverse by [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion); it is strictly increasing by [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). With \(f(t)=r\) the metric is \(dt^2+f(t)^2d\theta^2\). Put \(e_1=\partial_t,e_2=f^{-1}\partial_\theta\). The Koszul formula in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1), applied with \([e_1,e_2]=-(f'/f)e_2\), gives
\[
\nabla_{e_1}e_1=\nabla_{e_1}e_2=0,\quad
\nabla_{e_2}e_1=(f'/f)e_2,\quad
\nabla_{e_2}e_2=-(f'/f)e_1.
\]
Substituting these four identities into the curvature definition gives
\(R(e_2,e_1)e_1=-(f''/f)e_2\). Direct differentiation yields
\[
f'=(1+4r^2)^{-1/2},\qquad
f''=-4r(1+4r^2)^{-2}.
\]
Thus \(K=-f''/f\) has the value in (D.5) for \(r>0\). Smoothness of the original metric and curvature extends it to \(r=0\), with value \(4\). In dimension two the Ricci trace has just one perpendicular direction; the symmetries and trace identity of [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) give \(\operatorname{Ric}=Kg\). Finally \(K(r)\to0\) as \(r\to\infty\), so no positive constant \(k\) in (D.1) exists. □

## E. Exact models and higher homotopy

**Example E.1 (three cut loci).** On the unit sphere \(S^n\), \(n\geq2\), the cut locus of \(p\) is \(\{-p\}\) and every cut time is \(\pi\). On the locally round \(\mathbb{RP}^n=S^n/\{1,-1\}\), the cut locus of \([p]\) is the projective hyperplane
\[
\{[q]:\langle p,q\rangle=0\}\cong\mathbb{RP}^{n-1},
\tag{E.1}
\]
and every cut time is \(\pi/2\). On the rectangular flat torus
\[
T=\mathbb R^2/(a\mathbb Z\times b\mathbb Z),\qquad a,b>0,
\]
the normal domain at the origin is
\[
D=(-a/2,a/2)\times(-b/2,b/2).
\tag{E.2}
\]
The cut locus is the image of its boundary rectangle. A point on an open side has two minimizing lifts; a corner has four. The sphere cut point is conjugate, whereas the projective and torus cut points arise before any conjugacy.

**Proof.** [Riemannian connections E.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-e-1) gives
\(d_{S^n}(p,q)=\arccos\langle p,q\rangle\) and all minimizing great-circle arcs. [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2) gives
\(\exp_p(tu)=\cos t\,p+\sin t\,u\) for unit \(u\perp p\). It minimizes for \(0\leq t\leq\pi\), and not immediately beyond \(\pi\): for \(0<\varepsilon<\pi\), the distance to its value at \(\pi+\varepsilon\) is \(\pi-\varepsilon\). B.1 then gives cut time \(\pi\). [Jacobi fields B.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#example-b-3) gives a conjugate endpoint there with multiplicity \(n-1\). The tangent sphere of radius \(\pi\) is all mapped to the single point \(-p\).

The antipodal action is free and isometric. Its finite group satisfies the compact-intersection condition for proper discontinuity. Its smooth Riemannian quotient and covering are supplied by [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3). A curve from \([p]\) to \([q]\) lifts from \(p\) to either \(q\) or \(-q\), by [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1), and the covering preserves length by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Conversely either spherical minimizing arc projects to a path. Taking infima gives
\[
d_{\mathbb{RP}^n}([p],[q])
=\min\{\arccos\langle p,q\rangle,\arccos(-\langle p,q\rangle)\}
=\arccos|\langle p,q\rangle|.
\tag{E.3}
\]
The quotient ray therefore minimizes exactly through \(t=\pi/2\). At that time \(q=u\perp p\), proving (E.1). The map on the tangent boundary identifies \(u\) and \(-u\), and no other pair, since quotient equality on the unit sphere is exactly equality up to sign. Each orthogonal \(q\) has two shortest spherical lifts \(q,-q\); each is nonantipodal to \(p\) and so has a unique minimizing arc. Their projections are distinct: if equal as parametrized curves, their lifts from \(p\) would agree by path uniqueness. There are precisely two. The curvature is \(1\), so [Jacobi fields B.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#example-b-3) puts the first conjugate time at \(\pi\), strictly after this cut time.

Translations by the rectangular lattice act freely and isometrically. A compact set is coordinate bounded; if its translate intersects it, both translation coordinates are bounded, allowing only finitely many lattice elements. The action is therefore properly discontinuous and gives a Riemannian covering by [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3). For a point represented by \(z=(z_1,z_2)\), every path lifts from zero to
\((z_1+ma,z_2+nb)\) for integers \(m,n\). Its length is at least the Euclidean norm of that endpoint, and straight segments realize these norms. Hence
\[
d_T(0,[z])^2=\min_{m,n\in\mathbb Z}
 \bigl((z_1+ma)^2+(z_2+nb)^2\bigr).
\tag{E.4}
\]
The minimum is attained: terms with sufficiently large \(|m|+|n|\) exceed any fixed candidate. It separates into the two one-dimensional nearest-integer problems. In the centred rectangle, zero is the unique nearest multiple in a coordinate whose absolute value is smaller than half its period, and ties with exactly one other multiple at either endpoint. To verify this, if \(|z_1|\leq a/2\) and \(m\ne0\), then
\(|z_1+ma|\geq |m|a-|z_1|\geq a-|z_1|\geq |z_1|\);
equality is possible only for the adjacent multiple and \(|z_1|=a/2\). The second coordinate is identical.

For a unit ray \(tu=(tu_1,tu_2)\), its length equals the distance in (E.4) precisely until it first reaches the rectangle boundary. Its cut time is therefore
\[
c(u)=\min\left\{\frac{a}{2|u_1|},\,\frac{b}{2|u_2|}\right\},
\tag{E.5}
\]
where a zero component contributes \(+\infty\). This proves (E.2) and the asserted boundary image. The coordinate ties give exactly two shortest lifts on an open side and four at a corner; a minimizing geodesic lifts to a Euclidean straight segment by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), so these exhaust the geodesic minimizers. The metric is flat and its Jacobi fields with zero initial value are \(t\) times parallel fields, [Jacobi fields B.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#example-b-3). There is no positive conjugate time. □

**Exercise E.2 (asphericity and all lifting prerequisites).** Prove that every complete manifold with \(K\leq0\), in particular every compact hyperbolic manifold, has \(\pi_j(M)=0\) for \(j\geq2\).

**Solution.** [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) supplies the smooth universal cover
\(\pi:\widetilde M\to M\). The pullback metric is complete by [Hopf–Rinow E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4) and has the same sectional curvatures by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). It is simply connected by its construction. C.1 therefore identifies it diffeomorphically with a tangent space, by the exponential at any chosen point \(\widetilde p\).

We include the lifting step for arbitrary continuous maps. [Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3) proves that \(S^j\) is path connected and simply connected for \(j\geq2\), using based polygon approximation and an explicit stereographic contraction. Let \(f:(S^j,s_0)\to(M,p)\) be continuous. For \(s\in S^j\), choose a path \(\alpha\) from \(s_0\) to \(s\) and define \(\widetilde f(s)\) as the endpoint of the lift of \(f\circ\alpha\) beginning at \(\widetilde p\).

This is independent of the path. Two choices \(\alpha,\beta\) give a based loop \(\alpha*\beta^{-1}\) in the sphere, which has an endpoint-fixed null homotopy by simple connectivity. Compose that homotopy with \(f\). The path and square lifting proof in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) makes the lift of the resulting loop close at \(\widetilde p\). Reversal and path uniqueness then force the lifted \(\alpha\) and \(\beta\) to have the same endpoint.

The resulting map is continuous. Near any \(s\), choose a path-connected coordinate neighbourhood \(U\) whose image under \(f\) lies in an evenly covered open set \(V\) around \(f(s)\). Paths in \(U\) appended to a fixed path to \(s\) show that \(\widetilde f|_U\) is \(f|_U\) followed by the one inverse branch over \(V\) through \(\widetilde f(s)\). This branch is continuous. Thus \(\widetilde f\) is continuous everywhere and \(\pi\widetilde f=f\).

Use the global exponential inverse at \(\widetilde p\) to contract it:
\[
\widetilde H(s,t)=
\exp_{\widetilde p}\!\left((1-t)\exp_{\widetilde p}^{-1}\widetilde f(s)\right).
\tag{E.6}
\]
It is continuous, fixes the base point, starts at \(\widetilde f\), and ends at the constant \(\widetilde p\). Projection by \(\pi\) is a based null homotopy of \(f\). Since \(\pi_j\) consists of based homotopy classes of such sphere maps, every class is zero. A compact hyperbolic manifold is complete by [Hopf–Rinow B.3](completeness-and-the-hopf-rinow-theorem.md#corollary-b-3) and has \(K=-1\), so it satisfies the hypotheses. □

## F. Closed loops and positive curvature

**Lemma F.1 (nearby loops and polygons).** On a compact Riemannian manifold there is a number \(\rho>0\) such that two continuous loops \(a,b:[0,1]\to M\) with \(d(a(t),b(t))<\rho\) are freely homotopic. Every continuous loop has a finite geodesic polygon in its free homotopy class. Loops of length less than a sufficiently small fixed positive number are null homotopic.

**Proof.** [Hopf–Rinow A.1](completeness-and-the-hopf-rinow-theorem.md#lemma-a-1) gives a radius uniform over the compact set \(M\) in which the short minimizing vector from \(x\) to \(y\) is unique. Shrink the radius to \(\rho\). The map
\[
(x,v)\longmapsto (x,\exp_xv)
\]
has invertible derivative on these short vectors by [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1) and [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion). Its local inverse branches agree by uniqueness, so the short vector \(v(x,y)\) is jointly smooth for \(d(x,y)<\rho\). Consequently
\[
H(s,t)=\exp_{a(t)}(s\,v(a(t),b(t)))
\tag{F.1}
\]
is a continuous homotopy of loops; its values at \(t=0,1\) agree. If \(a(t)=b(t)\), that point stays fixed.

By uniform continuity choose a partition of the parameter interval so fine that the image of each subinterval lies within \(\rho/4\) of its initial point. Join consecutive vertex values by the short minimizing geodesic, using the same parameter subinterval. At every intermediate time this polygon and the original loop are within \(\rho/2\), by the triangle inequality. Formula (F.1) gives the required homotopy. For a rectifiable loop of length less than \(\rho\), every point is within \(\rho\) of its initial point; apply the same formula with the second loop constant. The elementary compactness and uniform-continuity facts used here are in [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). □

**Theorem F.2 (a shortest closed geodesic in a nontrivial class).** Every nontrivial free homotopy class of loops in a compact connected Riemannian manifold has a positive-length smooth closed geodesic shortest among its piecewise smooth representatives.

**Proof.** Lemma F.1 supplies a polygon representative, and its last assertion bounds the Riemannian lengths of all piecewise smooth representatives in this class below by one positive number. Thus their infimum \(\ell\) satisfies \(0<\ell<\infty\). Take representatives whose Riemannian lengths decrease to \(\ell\). [Hopf–Rinow G.2](completeness-and-the-hopf-rinow-theorem.md#lemma-g-2) writes each as \(\beta(s(t))\), where \(s\) is continuous, nondecreasing and onto \([0,L]\), and \(\beta\) is \(1\)-Lipschitz; its metric length \(L\) is at most its Riemannian length. Replace it on \([0,1]\) by \(c_j(t)=\beta(Lt)\). This preserves its free class, through the explicit homotopy \(\beta((1-u)s(t)+uLt)\). The resulting loops have one common Lipschitz bound. [Hopf–Rinow G.3](completeness-and-the-hopf-rinow-theorem.md#lemma-g-3) gives a uniformly convergent subsequence with limit a Lipschitz loop \(c\), and proves, for metric length,
\[
L(c)\leq\liminf_j L(c_j)=\ell .
\tag{F.2}
\]
For all large \(j\), Lemma F.1 makes \(c\) freely homotopic to \(c_j\).

Replace \(c\) by a sufficiently fine polygon as in F.1. Each segment has length the distance between its endpoints, at most the length of the corresponding part of \(c\). The resulting finite polygon lies in the same class and has length at most \(\ell\), hence exactly \(\ell\). Delete constant segments and parametrize it by arc length on \([0,\ell]\).

This polygon has no corner, including at the identified endpoints. Indeed, take two very nearby points on opposite sides of any vertex, so that the intervening two segments lie in a convex normal neighbourhood from [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5). If their unit tangents fail to agree, the corner obstruction of [Hopf–Rinow A.3](completeness-and-the-hopf-rinow-theorem.md#lemma-a-3) replaces these segments by a strictly shorter path in that neighbourhood. Both paths are homotopic with their endpoints fixed: the convex normal neighbourhood contracts paths between those endpoints by its short geodesics. The replacement is therefore in the original free class, contradicting minimality. All tangents agree. Uniqueness for the geodesic equation in [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) identifies successive segments with one smooth geodesic. It also identifies the final and initial germs, so the curve is smooth and periodic, not merely a geodesic segment with equal endpoint values. □

**Lemma F.3 (orthogonal parity and orientations).** If an orthogonal map \(A\) on a real \(d\)-dimensional inner-product space has no nonzero fixed vector, then \(\det A=(-1)^d\). Thus an orientation-preserving orthogonal map in odd dimension, or an orientation-reversing one in even dimension, has a nonzero fixed vector.

Every connected manifold has a two-sheeted orientation cover. It is connected precisely when the manifold is nonorientable. The cover itself is orientable; a simply connected manifold is orientable. For a Riemannian manifold, parallel transport around a loop preserves orientation precisely when the lift of that loop to the orientation cover closes. This property is unchanged under free homotopy.

**Proof.** If \(I-A\) is invertible, determinant multiplication and transposition give
\[
\begin{aligned}
\det A\,\det(I-A^{\mathsf T})
&=\det(A-I)=(-1)^d\det(I-A),\\
\det(I-A^{\mathsf T})&=\det(I-A)\ne0.
\end{aligned}
\tag{F.3}
\]
Cancel to obtain the assertion. These determinant identities and the two classes of real frames are proved in [Principal bundles D.3](principal-bundles-and-associated-bundles.md#theorem-d-3).

At \(x\in M\), an orientation is one of those two classes of frames of \(T_xM\). Form the set of pairs \((x,o)\), where \(o\) is such a class. A coordinate frame over \(U\) identifies this set over \(U\) with \(U\times\{+,-\}\). On overlaps the sign changes by the sign of the coordinate transition determinant. The chain rule makes these identifications satisfy the gluing identity on triple overlaps. They define a smooth two-sheeted covering \(\widehat M\to M\). It is Hausdorff because points over different base points are separated downstairs, and the two points of one fibre are separated in a covering chart. A countable coordinate basis downstairs gives one upstairs. Orient \(T_{(x,o)}\widehat M\) by requiring the differential of the covering to carry its positive frames to \(o\). This is consistent in all these charts.

An orientation of \(M\) is exactly a continuous section choosing one of the two sheets; such a section and its opposite split \(\widehat M\) into two components. Conversely, each component of \(\widehat M\) maps onto \(M\), since a path from any one base point to any other lifts starting in that component. If \(\widehat M\) is disconnected, its two-point fibres therefore contain one point in each of two components. Each component maps bijectively and locally diffeomorphically to \(M\), giving an orientation section. If \(M\) is simply connected, the covering classification in [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) says that each connected component of the cover has one sheet, so \(M\) is orientable.

Parallel transport of a frame is a continuous path of frames by [Connections D.2](connections-and-parallel-transport.md#theorem-d-2). Its orientation classes give the lift to \(\widehat M\); thus the sign of the determinant of loop transport detects whether the lift closes. The path and square lifting proof in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) shows that this closing property is constant under based homotopy. For a free homotopy, follow the path traced by its base point and lift the homotopy square. The permutations of the two-point fibres at the ends are conjugate by transport along that base-point path. Conjugation preserves whether that permutation is the identity. This proves free-homotopy invariance as well. □

**Lemma F.4 (a shortening variation).** A unit-speed smooth closed geodesic on a manifold with \(K>0\) cannot be shortest in its free homotopy class if it has a nonzero periodic parallel normal field.

**Proof.** Write the geodesic as \(\gamma:[0,\ell]\to M\), with \(T=\gamma'\), and let \(V\) be such a field. Put
\[
\gamma_s(t)=\exp_{\gamma(t)}(sV(t)).
\tag{F.4}
\]
For sufficiently small \(|s|\) this is defined and smooth, uniformly in \(t\), by compactness of the parameter circle and the geodesic flow. Periodicity of \(\gamma,T,V\) gives a smooth family of closed loops in the same free class. [Jacobi fields A.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-3) gives zero first derivative of energy: the geodesic interior term vanishes and the two endpoint terms cancel. In [Jacobi fields A.4](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-4) the endpoint acceleration terms vanish because \(s\mapsto\gamma_s(t)\) is a geodesic for fixed \(t\). Hence
\[
E'(0)=0,\qquad
E''(0)=\int_0^\ell
 \bigl(|\nabla_TV|^2-\langle R(V,T)T,V\rangle\bigr)\,dt<0 .
\tag{F.5}
\]
Here \(V\) has constant nonzero norm, is normal to \(T\), and the integrand is strictly negative. The second-order integral form of Taylor's formula from [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) gives \(E(s)<E(0)\) for small nonzero \(s\). The integral Cauchy–Schwarz inequality, also proved there, yields
\[
L(\gamma_s)^2\leq 2\ell E(s)<2\ell E(0)=\ell^2.
\]
This contradicts shortest length in the free class. □

**Theorem F.5 (Synge and the two parities).** A compact connected even-dimensional orientable Riemannian manifold with positive sectional curvature is simply connected. A compact connected even-dimensional manifold with positive sectional curvature is either orientable and simply connected, or nonorientable with fundamental group \(\mathbb Z/2\). Every compact connected odd-dimensional manifold with positive sectional curvature is orientable.

**Proof.** In even positive dimension suppose an orientable \(M\) has a non-null-homotopic loop. Its free class is nontrivial: a free null homotopy, together with the path traced by its base point, gives a based null homotopy by conjugating that path and its reverse. This also follows directly from the square path-lifting construction in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1). By F.2 choose a shortest unit-speed closed geodesic \(\gamma\) in that class. Parallel transport around it fixes \(T(0)\), preserves \(T(0)^\perp\), and has positive determinant by F.3. Its restriction to this odd-dimensional normal space also has positive determinant. F.3 gives a nonzero fixed normal vector, whose parallel field is periodic. Lemma F.4 is a contradiction.

If \(M\) is even-dimensional and nonorientable, its orientation cover is connected and orientable by F.3. It is compact: cover the compact base by finitely many coordinate sets with compact closures lying inside covering charts; the inverse image of each closure is the union of two compact sets, and these finitely many sets cover the cover. Pull back the metric. The covering is a local isometry, so has the same sectional curvatures by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) and the definition of curvature through iterated covariant derivatives. The even orientable case makes this cover simply connected. [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) then identifies its two sheets with the fundamental group of \(M\); the only group of order two is \(\mathbb Z/2\).

For odd dimension, suppose that \(M\) is nonorientable. The connected orientation cover has a path between the two points over one base point; its projection is an orientation-reversing loop. Such a loop is not null homotopic by F.3. A shortest geodesic in its free class has orientation-reversing parallel transport, since the sign is free-homotopy invariant. Its tangent is fixed, so its even-dimensional normal space has orientation-reversing transport. F.3 and F.4 again give a contradiction. In dimension one the normal space has dimension zero, where the determinant is \(+1\); the asserted negative determinant is already impossible. A connected zero-dimensional manifold is a point, so the even-dimensional assertion also holds in dimension zero. □

**Exercise F.6 (projective examples and pinching).** Verify the orientation and fundamental group of round \(\mathbb {RP}^n\), \(n\geq2\), and locate the role of the hypotheses in F.5. Define the usual positive-curvature pinching normalization.

**Solution.** [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2) gives curvature \(1\) on the unit sphere, and E.1 constructs its antipodal Riemannian quotient. Orient \(S^n\) by declaring a tangent frame positive when, preceded by the outward normal \(x\), it is a positive frame of \(\mathbb R^{n+1}\). The antipodal differential sends the full frame to its negative. Its sign on the oriented sphere is therefore \((-1)^{n+1}\). An orientation descends to the quotient precisely when the deck involution preserves it: one direction follows by pulling an orientation back; for the other, push it forward using either inverse sheet and invariance makes the choice agree. Thus \(\mathbb {RP}^n\) is orientable exactly when \(n\) is odd.

[Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3) proves that \(S^n\) is simply connected for \(n\geq2\). The antipodal covering has two sheets, so [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) gives \(\pi_1(\mathbb {RP}^n)=\mathbb Z/2\). In even dimensions these are the nonorientable examples in F.5; in odd dimensions they are orientable but not simply connected. The even-dimensional conclusion requires orientability, and the simply connected conclusion does not extend to odd dimensions. The flat two-torus in E.1 is compact and orientable with nontrivial fundamental group, but its curvature is zero.

A metric is positively \(\delta\)-pinched in the normalized convention if
\[
0<\delta\leq K(\sigma)\leq1
\]
for every tangent two-plane \(\sigma\). Multiplication of a metric by a positive constant \(a\) leaves its Levi–Civita connection unchanged: every term of the Koszul identity in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1) is multiplied by \(a\). The curvature operator is unchanged, while the numerator of the sectional curvature quotient is multiplied by \(a\) and its denominator by \(a^2\). Thus \(K_{ag}=a^{-1}K_g\), which explains this normalization. Round projective space is \(1\)-pinched and is not simply connected; pinching alone does not assert that a manifold is a sphere. □

## G. Barycentres and fixed points

A **Hadamard manifold** is a complete simply connected Riemannian manifold with \(K\leq0\). Its joint logarithm \(\log_x z=\exp_x^{-1}z\) is smooth by C.2.

**Lemma G.1 (the bounded integrals used below).** Let \((A,\mathcal B,\mu)\) be a measure space with \(\mu(A)=1\). Bounded measurable real functions have an integral that is linear, positive, and satisfies
\[
\left|\int_A f\,d\mu\right|\leq\sup_A|f|.
\tag{G.1}
\]
Uniform convergence of such functions implies convergence of their integrals. Finite-dimensional vector-valued integrals are defined componentwise and commute with linear maps. If \(h(x,a)\) and its first derivatives in a finite-dimensional variable \(x\) are continuous, with uniform first-order remainders for \(a\in A\) near \(x\), then
\[
D_x\int_A h(x,a)\,d\mu(a)=\int_A D_xh(x,a)\,d\mu(a).
\tag{G.2}
\]

**Proof.** For a measurable simple function, use a finite disjoint partition \(A=\bigcup_i E_i\) on which its values are \(c_i\), and set its integral equal to \(\sum_i c_i\mu(E_i)\). Any two such partitions have the common refinement by their intersections. Finite additivity shows that the value does not change upon refinement, and proves linearity. Nonnegative values give a nonnegative sum. Applying positivity to the two inequalities \(-\sup|f|\leq f\leq\sup|f|\) gives (G.1) for simple functions.

For a bounded measurable \(f\), the functions \(2^{-j}\lfloor2^j f\rfloor\) have finitely many values, are measurable, and converge uniformly to \(f\). Their integrals are Cauchy by (G.1) applied to differences. Define \(\int f\) as their limit. Any uniformly approximating simple sequence gives the same limit, again by the difference bound. Approximate two functions simultaneously to deduce linearity, positivity and (G.1); the same bound proves the uniform-limit assertion. Real completeness is the one used in [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). For a vector choose a basis and integrate its coordinates. Linearity shows that the vector is independent of the basis and that a linear map commutes with the integral.

Finally suppose
\[
h(x+v,a)=h(x,a)+D_xh(x,a)v+r(v,a),\qquad
\sup_a|r(v,a)|=o(|v|).
\]
Integrate the identity, then apply (G.1) to its last term. This proves differentiability and (G.2). One sufficient condition for that uniform remainder is uniform continuity of \(D_xh\) on a compact neighbourhood in \(x\) times a compact set containing its other variable: the segment integral formula of [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) bounds the remainder by \(|v|\) times the corresponding modulus of continuity. No exchange of an unbounded limit and an integral is required. □

**Theorem G.2 (barycentre of a compactly parametrized probability measure).** Let \(M\) be a Hadamard manifold, \(A\) compact Hausdorff, \(z:A\to M\) continuous, and \(\mu\) a positive Borel measure with \(\mu(A)=1\). The function
\[
F(x)=\int_A d(x,z(a))^2\,d\mu(a)
\tag{G.3}
\]
has a unique minimum \(b\). A point \(x\) equals \(b\) precisely when
\[
\int_A\log_x z(a)\,d\mu(a)=0\quad\text{in }T_xM.
\tag{G.4}
\]

**Proof.** The image \(Z=z(A)\) is compact. Choose \(o\in M\) and \(R\) with \(d(o,z)\leq R\) for \(z\in Z\). The integrands in (G.3) are continuous and bounded on \(A\), so G.1 defines their integrals. For \(x,y\) in a fixed bounded set, the triangle inequality gives a constant \(C\), independent of \(a\), such that
\[
|d(x,z(a))^2-d(y,z(a))^2|
\leq d(x,y)\bigl(d(x,z(a))+d(y,z(a))\bigr)
\leq C d(x,y).
\]
Thus \(F\) is continuous. If \(d(x,o)>R\), the reverse triangle inequality gives
\[
F(x)\geq(d(x,o)-R)^2.
\tag{G.5}
\]
Its nonempty sublevel \(\{F\leq F(o)\}\) is closed and bounded, hence compact by [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2). A minimum there exists by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and is a global minimum.

For the constant-speed geodesic \(x_t\) from \(x_0\) to \(x_1\), C.2 gives
\[
d(x_t,z)^2\leq (1-t)d(x_0,z)^2+t\,d(x_1,z)^2
-t(1-t)d(x_0,x_1)^2.
\]
Integrating with positivity and unit total mass yields
\[
F(x_t)\leq(1-t)F(x_0)+tF(x_1)
-t(1-t)d(x_0,x_1)^2.
\tag{G.6}
\]
Two different minimum points would contradict this inequality at \(t=1/2\).

The squared distance is jointly smooth by C.2. First variation in [Jacobi fields A.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-3), applied to the geodesic from \(x\) to \(z\) on \([0,1]\), gives
\[
D_x(d(x,z)^2)v=-2\langle\log_xz,v\rangle.
\tag{G.7}
\]
Indeed, its energy is \(d(x,z)^2/2\); the interior derivative vanishes, the fixed final endpoint contributes zero, and the initial endpoint contributes \(-\langle v,\log_xz\rangle\). In a relatively compact coordinate neighbourhood of \(x\), this smooth function and its derivatives are uniformly continuous on its compact closure times \(Z\). G.1 therefore permits differentiation under the integral, giving
\[
\nabla F(x)=-2\int_A\log_xz(a)\,d\mu(a).
\]
At a minimum the derivative is zero by one-variable differentiation along each coordinate direction. Conversely, if the derivative vanishes, divide (G.6), with \(x_0=x\), by \(t>0\) after subtracting \(F(x)\), and let \(t\downarrow0\). It follows that \(F(y)\geq F(x)+d(x,y)^2\) for every \(y\). This proves (G.4) and completes the characterization. □

**Theorem G.3 (bounded orbits have fixed points).** A group of isometries of a Hadamard manifold with a bounded orbit has a common fixed point. In particular this holds for a compact topological group acting continuously by isometries.

**Proof.** Let \(O\) be a bounded nonempty orbit and set
\[
Q(x)=\sup_{z\in O}d(x,z)^2.
\tag{G.8}
\]
This is finite. The distance-difference estimate in G.2 holds uniformly for \(z\in O\) and \(x,y\) in a bounded set, so taking suprema shows that \(Q\) is locally Lipschitz. Pick any \(z_0\in O\); then \(Q(x)\geq d(x,z_0)^2\). A nonempty sublevel is therefore compact by [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2), and continuity gives a minimum. Taking the supremum of the sharp convexity inequality from C.2 gives
\[
Q(x_t)\leq(1-t)Q(x_0)+tQ(x_1)
-t(1-t)d(x_0,x_1)^2.
\]
Thus its minimum is unique. Each group element permutes \(O\) and preserves distances, so \(Q(gx)=Q(x)\). Uniqueness forces every \(g\) to fix the minimum. A compact group with continuous action has compact, hence bounded, orbits. This argument uses the circumcentre (the minimum of \(Q\)); it does not require an invariant measure on the group. □

## H. Homogeneity and displacement

An isometry \(\phi\) has **constant displacement** if \(d(x,\phi x)\) is independent of \(x\).

**Lemma H.1 (deck displacement in a homogeneous cover).** Let \(M\) be a connected homogeneous Riemannian manifold. Every deck transformation of its universal Riemannian cover has constant displacement.

**Proof.** Homogeneity implies completeness by [Hopf–Rinow B.3](completeness-and-the-hopf-rinow-theorem.md#corollary-b-3). Let \(\pi:\widetilde M\to M\) be the connected simply connected cover constructed in [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2), equipped with its pullback metric. It is complete by [Hopf–Rinow E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4). Its deck group \(\Gamma\), identified with \(\pi_1(M)\), is countable by [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4).

Every isometry \(f\) of \(M\) lifts to an isometry \(F\) of \(\widetilde M\). To see this with prescribed value \(F(x)=y\), where \(\pi y=f(\pi x)\), use uniqueness of simply connected covers in [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) on the two covering maps \(\pi\) and \(f\pi\), with the stated base points. It gives a diffeomorphism \(F\) with \(\pi F=f\pi\). Pulling back the metric through this identity proves that \(F\) is an isometry. It normalizes \(\Gamma\), since
\[
\pi F\gamma F^{-1}=f\pi\gamma F^{-1}=f\pi F^{-1}=\pi .
\]
Fix \(o\in\widetilde M\) and \(\gamma\in\Gamma\). For each \(x\), transitivity downstairs and the prescribed lift provide such an \(F\) with \(F(x)=o\). Therefore
\[
d(x,\gamma x)=d(o,F\gamma F^{-1}o)
\in\{d(o,\delta o):\delta\in\Gamma\}.
\tag{H.1}
\]
The right side is a fixed countable subset of \(\mathbb R\). The displacement function is continuous. Along a path between any two points, its image contains the interval between its endpoint values by the intermediate value theorem of [Local tools 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). A nondegenerate interval cannot be countable: given an enumeration of points, choose successively nonempty closed subintervals in the interior of the preceding interval, of length at most \(2^{-j}\), with the \(j\)-th listed point excluded. The nested-interval completeness statement of [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) gives a point in all intervals, absent from the enumeration. Hence the two endpoint values agree. A connected manifold is path connected because the points reachable by piecewise coordinate paths form an open set with open complement. Thus displacement is constant on \(\widetilde M\). □

**Theorem H.2 (negative Ricci for a homogeneous manifold).** A connected homogeneous Riemannian manifold with \(K\leq0\) and negative-definite Ricci tensor is simply connected, and each of its exponential maps is a diffeomorphism. Every transitive subgroup of its isometry group has trivial centre.

**Proof.** We first establish the needed rigidity statement: a constant-displacement isometry \(\phi\) of a Hadamard manifold with negative-definite Ricci tensor is the identity. Let its displacement be \(L\); suppose \(L>0\). Fix \(x\) and any \(v\in T_xM\), and take the geodesic \(x(s)\) with initial velocity \(v\). Isometries preserve the connection and geodesics by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), so \(\phi(x(s))\) is also a geodesic. The joint logarithm from C.2 defines a smooth geodesic variation
\[
\alpha(s,t)=\exp_{x(s)}\bigl(t\log_{x(s)}\phi(x(s))\bigr),
\qquad 0\leq t\leq1.
\]
Every row has energy \(L^2/2\). Along the row \(s=0\), put \(T=\partial_t\alpha\), \(J=\partial_s\alpha\). Both endpoint curves have zero covariant acceleration, so [Jacobi fields A.4](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-4) gives
\[
0=\int_0^1
\bigl(|\nabla_TJ|^2-\langle R(J,T)T,J\rangle\bigr)\,dt .
\tag{H.2}
\]
The integrand is nonnegative: decompose \(J\) into its component parallel to \(T\) and its orthogonal component and use the sectional-curvature identity in [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1). Each of the two nonnegative continuous terms must vanish. At \(t=0\), \(J(0)=v\), and hence
\[
\langle R(v,T(0))T(0),v\rangle=0.
\]
This holds for every \(v\), since \(x\) and \(\phi x\), and therefore \(T(0)\ne0\), were fixed while \(v\) was arbitrary. Sum over an orthonormal basis. The definition of Ricci in [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) gives \(\operatorname{Ric}(T(0),T(0))=0\), contrary to negative definiteness. Thus \(L=0\) and \(\phi\) is the identity.

Now lift \(M\) to its universal Riemannian cover. Homogeneous completeness, completeness of the cover and curvature preservation were verified in H.1 and D.1. The cover is Hadamard by C.1 and has negative-definite Ricci. Every deck transformation has constant displacement by H.1, so the preceding paragraph makes the deck group trivial. [Flat connections D.2](flat-connections-and-infinitesimal-holonomy.md#theorem-d-2) identifies this group with \(\pi_1(M)\); thus \(M\) is simply connected. C.1 gives its global exponential diffeomorphisms.

Finally let \(G\) be any transitive subgroup of the isometry group, and let \(\phi\) lie in its centre. For every \(g\in G\),
\[
d(gx,\phi gx)=d(gx,g\phi x)=d(x,\phi x).
\]
Transitivity makes this displacement constant. Apply the proved rigidity statement on \(M\) to conclude \(\phi=1\). This uses the actual subgroup of isometries, so its action is faithful; no extra closedness or Lie-group assumption on \(G\) is needed. □

## I. Compact isotropy

Give the isometry group of a Hadamard manifold the topology of uniform convergence on compact sets.

**Lemma I.1 (compactness of isometry fibres).** Let \(M\) be a Hadamard manifold, \(p\in M\), and \(G\) a closed subgroup of its isometry group. The evaluation map \(G\to M\), \(g\mapsto gp\), has compact inverse images of compact sets. The stabilizer \(H=G_p\) is a compact Lie group, identified by its derivative at \(p\) with a closed subgroup of \(O(T_pM)\). If \(G\) is transitive, the map \(G/H\to M\), \(gH\mapsto gp\), is a homeomorphism.

**Proof.** An isometry preserves geodesics and their initial velocities by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). Since \(\exp_p\) is a global diffeomorphism, an isometry \(f\) is determined by its value \(q=f(p)\) and orthogonal derivative \(A=d f_p:T_pM\to T_qM\), through
\[
f(x)=\exp_q(A\log_p x).
\tag{I.1}
\]
These pairs \((q,A)\) form an orthonormal-frame bundle after fixing an orthonormal basis of \(T_pM\). Its restriction over a compact set is compact by [Hopf–Rinow D.2](completeness-and-the-hopf-rinow-theorem.md#lemma-d-2).

Convergence of pairs in (I.1) gives smooth convergence on compact coordinate sets, hence uniform convergence on compact sets, by smoothness of the exponential and C.2. Conversely, evaluations at the finitely many points \(p,\exp_p e_1,\ldots,\exp_p e_n\) recover the pair continuously:
\[
q=f(p),\qquad A e_i=\log_q\bigl(f(\exp_p e_i)\bigr).
\tag{I.2}
\]
Thus the pair topology and the stated isometry topology agree. Uniform convergence on compact sets is metrizable, for example by the sum of \(2^{-j}\) times the minimum of \(1\) and the uniform distance on the compact closed ball \(\overline B(p,j)\).

Suppose pairs of isometries \(f_i\) converge to \((q,A)\). Formula (I.1) defines a smooth limit \(f\). Distance preservation passes to the limit, and the smooth convergence of derivatives gives \(f^*g=g\). This map is onto: for any \(y\), write \(x_i=f_i^{-1}(y)\). Then
\[
d(p,x_i)=d(f_i p,y)
\]
is bounded. [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) gives a convergent subsequence \(x_i\to x\), and uniform convergence on its compact containing ball gives \(f(x)=y\). It is injective by distance preservation. The inverse function theorem, applied to its isometric derivative, gives a smooth inverse. Thus \(f\) is an isometry. If all \(f_i\) lie in \(G\), closedness implies \(f\in G\). The pairs representing \(G\) are consequently closed in the frame bundle. Intersecting with its compact restriction over a compact set proves the evaluation assertion.

In particular \(H\) is compact. The derivative at \(p\) is an injective continuous group homomorphism with closed image in \(O(T_pM)\), and (I.1) is its continuous inverse onto \(H\). The closed-subgroup theorem proved in [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) gives this image its embedded Lie-group structure. Formula (I.1) shows that its action on \(M\) depends smoothly on its matrix coordinate.

For clarity, the isometry topology makes multiplication and inversion continuous. On a compact \(C\),
\[
\begin{split}
d(f_i g_i x,fgx)&\leq d(g_i x,gx)+d(f_i gx,fgx),\\
d(f_i^{-1}y,f^{-1}y)&=d(y,f_i f^{-1}y).
\end{split}
\]
The first inequality uses that \(f_i\) is an isometry; the second is an equality for the same reason. Taking suprema over \(C\) uses only convergence on \(C,g(C)\), or \(f^{-1}(C)\). These estimates prove the assertion.

If \(G\) is transitive, evaluation is a continuous surjection with fibres the cosets \(gH\). It is closed. Indeed, for a closed \(C\subset G\), if \(g_i p\in\operatorname{ev}_p(C)\) converges to \(q\), then all those values and \(q\) form a compact set. Its inverse image is compact, so a subsequence of \(g_i\in C\) converges to an element \(g\in C\) with \(gp=q\). Since \(M\) is metrizable, this proves closedness. A continuous closed surjection is a quotient map: a set whose inverse image is closed is the image of that closed inverse image. The quotient topology therefore identifies \(G/H\) homeomorphically with \(M\). □

**Theorem I.2 (maximal compact stabilizers).** Suppose a closed subgroup \(G\) of the isometry group of a Hadamard manifold acts transitively. Its point stabilizers are maximal compact subgroups. Every maximal compact subgroup is a point stabilizer and is conjugate to any prescribed one. If \(G\) is connected, every point stabilizer is connected.

**Proof.** Put \(H=G_p\). It is compact by I.1. If \(K\) is a compact subgroup containing \(H\), its action is continuous and G.3 gives a fixed point \(q\). Hence
\[
H\subset K\subset G_q.
\tag{I.3}
\]
Choose \(g\in G\) with \(gp=q\). Then \(G_q=gHg^{-1}\). These compact Lie groups have the same dimension and the same number of connected components. Here the Lie-group assertion and the comparison are explicit: at a fixed point the group is its closed orthogonal derivative subgroup from I.1; conjugation by \(g\) is the linear change
\[
A\longmapsto (d g_p) A(d g_p)^{-1}
\]
between the two derivative representations, a smooth Lie-group isomorphism.

The inclusion \(H\subset G_q\) is also an embedded smooth inclusion. In derivative coordinates at \(p\), formula (I.1) expresses \(d f_q\) smoothly as a function of \(A=d f_p\). Conversely, for isometries in that image, the same formula based at \(q\) expresses \(d f_p\) smoothly as a function of \(d f_q\). The image is compact and therefore closed, and the closed-subgroup theorem from [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) supplies its embedded structure. The two smooth formulas identify that structure with the one on \(H\). Equal dimension and [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) now make the inclusion open near the identity, hence open everywhere by translation. An open subgroup is a union of connected components: each coset is open, and a connected set cannot meet two disjoint cosets. A compact Lie group has finitely many components because components are open in a locally path-connected manifold and compactness gives a finite subcover. Since \(H\) and \(G_q\) have the same number of components, the inclusion must be equality. Equation (I.3) gives \(K=H\), proving maximality.

Conversely, any maximal compact \(K\) fixes a point \(q\) by G.3. Since \(G_q\) is compact and contains \(K\), maximality gives \(K=G_q\). Transitivity supplies its conjugacy to \(H\).

It remains to prove connectedness of \(H\) when \(G\) is connected; no Lie structure on the whole group \(G\) is needed. Let \(H^0\) be the identity component of the compact Lie group \(H\). It is closed, normal in \(H\), and of finite index. Closedness follows because a component is closed; normality follows because conjugation preserves the identity component; openness and finite index follow from the manifold and compactness argument just given. In particular \(H^0\) is compact and closed also in the Hausdorff group \(G\).

The coset space \(X=G/H^0\) is Hausdorff, and its quotient map is open. For the latter assertion, the inverse image of the image of an open set \(U\) is \(UH^0\), a union of open translates. For Hausdorffness, if \(xH^0\ne yH^0\), then \(x^{-1}y\notin H^0\). By closedness and continuity of multiplication choose an identity neighbourhood \(W\) with
\[
W^{-1}x^{-1}yW\cap H^0=\varnothing.
\]
The open images of \(xW\) and \(yW\) in \(X\) are disjoint: intersection would give an element of the forbidden intersection. This separates the two cosets.

The finite group \(Q=H/H^0\) acts freely on \(X\) on the right by
\[
(gH^0)(hH^0)=ghH^0.
\]
Normality in \(H\) proves independence of both representatives; the quotient topology makes every such translation a homeomorphism. Freeness follows by cancellation. A free finite action on a Hausdorff space has a covering quotient. To verify this, for each nonidentity \(a\in Q\) separate \(x\) and \(xa\) by disjoint neighbourhoods \(V_a,W_a\). The neighbourhood
\[
U=\bigcap_{a\ne1}(V_a\cap W_a a^{-1})
\]
of \(x\) has \(U\cap Ua=\varnothing\) for every \(a\ne1\). Its distinct translates are disjoint, and the quotient, which is open, maps each homeomorphically onto the same open set. These are exactly the required covering charts.

The orbit space is \(G/H\): composing the two open quotient maps identifies both the equivalence classes and their quotient topology. I.1 identifies it with \(M\). Thus \(X\to M\) is a finite covering. It is connected because \(G\) is connected and \(G\to X\) is continuous and onto. Its covering charts give it a manifold structure; it is second countable by taking a countable subcover of evenly covered base charts and the finitely many sheets over each. Smooth coordinate changes are those downstairs. Since \(M\) is simply connected, [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3) implies that this connected cover has one sheet. Its fibre has size \(|Q|\), so \(Q\) is trivial and \(H=H^0\). □

## Further reading

- Urs Lang, [*Lecture Notes on Riemannian Geometry*, ETH Zürich, 16 June 2020](https://metaphor.ethz.ch/x/2020/fs/401-3532-08L/sc/DG2_16June2020.pdf), Theorem 3.8, §§3.16–3.19, Theorem 4.12 and §§6.3–6.5.
- Jost-Hinrich Eschenburg, [*Comparison Theorems in Riemannian Geometry*, lecture notes, September 1994](https://www.math.toronto.edu/vtk/eschenburg-comparison.pdf), the beginning of §5, including the cut-point alternatives and model examples.
- Claudio Gorodski, [Riemannian geometry lecture notes, Chapter 6](https://www.ime.usp.br/~gorodski/teaching/mat5771/ch6.pdf), §§6.3 and 6.5. The finite-set circumcentre construction motivates G.3; the probability-measure barycentre and the full bounded-orbit assertion are proved above.
- Joseph A. Wolf, [*Homogeneity and Bounded Isometries in Manifolds of Negative Curvature*, author-hosted article, 1964](https://math.berkeley.edu/~jawolf/publications.pdf/paper_016.pdf), pp. 14–18, for the displacement and homogeneity results. H proves the needed constant-displacement and negative-Ricci assertions directly, and I supplies the compact-subgroup arguments.
