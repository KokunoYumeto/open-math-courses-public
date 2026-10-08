# Affine transformations and the isometry group

A connection turns the derivative of a transformation at one point into global information. We first identify that information, then show how it gives a smooth structure on the group of global transformations. The distinction between a locally defined flow and a global one is essential when the manifold is incomplete.

Manifolds are smooth, finite dimensional, Hausdorff and second countable. They have no boundary and are connected unless stated otherwise. Metrics are positive definite. Our conventions are
\[
T(Y,Z)=\nabla_YZ-\nabla_ZY-[Y,Z],\qquad
R(Y,Z)V=\nabla_Y\nabla_ZV-\nabla_Z\nabla_YV-\nabla_{[Y,Z]}V.
\]
The freely available notes of Čap explain the use of a coframe on a frame bundle; Pecastaing's notes explain one-jet determination and Killing fields. Their exact versions are listed at the end. The later sections combine these local tools with the covering, de Rham and space-form theorems to compute quotient groups and classify maximal symmetry. All results used below have proofs here or at the linked earlier programme locators.

## A. The data carried by a symmetry

For a smooth map \(f:M\to N\) between manifolds with connections, **affine** means \(\nabla df=0\), with the pullback connection on \(f^*TN\). An affine transformation is an affine diffeomorphism from \(M\) onto itself. A smooth field \(X\) is **infinitesimally affine** if each map of its local flow is affine on its domain.

**Lemma A.1 (Affine maps and their first data).** The affine condition is equivalent to the parallelism of \(df\), and in coordinates reads
\[
\partial_i\partial_j f^\alpha+
\Gamma'{}^\alpha_{\beta\gamma}(f)\partial_i f^\beta\partial_j f^\gamma
-\Gamma^k_{ij}\partial_k f^\alpha=0.
\tag{A.1}
\]
It implies transport and exponential naturality:
\[
df_{\gamma(t)}P^\gamma_{0t}
=P^{f\gamma}_{0t}df_{\gamma(0)},\qquad
f(\exp_pv)=\exp_{f(p)}(df_pv)
\tag{A.2}
\]
whenever the source geodesic segment in the second formula exists. An affine map on a connected domain is determined by its value and differential at one point. A \(C^2\) map satisfying (A.1) is automatically smooth. Equivalently, one may start with a \(C^1\) map that takes every parallel vector along a smooth curve to a parallel vector along its image: that map is smooth and affine as defined above. Transport along the \(C^1\) image curves has the meaning proved in [Curvature and holonomy C.2](curvature-and-holonomy-groups.md#lemma-c-2).

**Proof.** [Killing fields A.1](holonomy-killing-fields-and-analytic-extension.md#lemma-a-1) proves the coordinate equation, transport identity, geodesic naturality and connected-domain uniqueness directly from the derivative axioms. The geodesic identity holds for a whole existing source segment: its image solves the target geodesic equation with the stated initial data, so [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) identifies it with that target solution on the entire segment. In particular the required target segment exists.

For the regularity assertion, a \(C^2\) solution of (A.1) still satisfies the same chain-rule calculation along geodesics. On a normal neighbourhood it therefore equals
\[
x\longmapsto \exp_{f(p)}\!\left(df_p\,\exp_p^{-1}x\right).
\]
The exponential and its local inverse are smooth by [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). The right side is smooth after restricting the neighbourhood, and proves the assertion at every \(p\).

For the \(C^1\) transport formulation, take a source geodesic \(\gamma\). Its velocity is parallel, so the velocity \(df(\dot\gamma)\) of the \(C^1\) image curve is parallel there. In coordinates, a parallel vector along a \(C^1\) path solves a linear equation with continuous coefficients, and is \(C^1\), by [Curvature and holonomy C.2](curvature-and-holonomy-groups.md#lemma-c-2) and [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2). Thus the image curve is \(C^2\); its velocity has zero covariant derivative and it solves the geodesic equation. [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) gives the same exponential identity. The preceding normal-coordinate formula therefore makes \(f\) smooth. Along any curve now expand a vector as \(V(t)=P_{0t}c(t)\) in a parallel frame. Transport preservation gives \(dfV=P'_{0t}df_p c(t)\). Differentiating the coefficient column yields \(D_t(dfV)=dfD_tV\), by [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2). At each initial point and in every tangent direction this says \(\nabla df=0\). The converse was already proved by transport naturality. No rank assumption or torsion-free condition is used. □

Define the endomorphism
\[
A_X(Y)=[X,Y]-\nabla_XY=-\nabla_YX-T(X,Y).
\tag{A.3}
\]
The last equality follows from the definition of torsion. In particular the formula \(A_X=-\nabla X\) applies only when the torsion vanishes.

**Theorem A.2 (The affine infinitesimal equation with torsion).** A smooth field \(X\) is infinitesimally affine if and only if
\[
\nabla_YA_X=R(X,Y)\quad\text{for every }Y.
\tag{A.4}
\]
These fields form a vector space and a Lie algebra for the usual vector-field bracket. If \(X,Y\) belong to it, then
\[
A_{[X,Y]}=[A_X,A_Y]-R(X,Y).
\tag{A.5}
\]
At each \(p\), the map \(X\mapsto(X_p,(A_X)_p)\) is injective. Consequently the dimension is at most \(n+n^2\).

**Proof.** Write \(L_XZ=[X,Z]\) on vector fields. The coordinate bracket of [Principal bundles C.3](principal-bundles-and-associated-bundles.md#lemma-c-3) gives \(L_X=\nabla_X+A_X\); the derivative terms cancel in their difference, which is precisely the smooth tensor (A.3). Differentiate the pullback of the connection by the local flow of \(X\). The derivative at zero is
\[
(\mathcal L_X\nabla)(Y,Z)
=[X,\nabla_YZ]-\nabla_{[X,Y]}Z-\nabla_Y[X,Z].
\tag{A.6}
\]
Indeed the derivative of the pullback of a vector field is its bracket with \(X\), and the product rule gives the three terms. This is the same coordinate differentiation used in [Killing fields E.1](holonomy-killing-fields-and-analytic-extension.md#lemma-e-1); it does not require zero torsion. Substituting \(L_X=\nabla_X+A_X\) into (A.6), as an operator on \(Z\), gives
\[
[L_X,\nabla_Y]-\nabla_{[X,Y]}
=R(X,Y)+[A_X,\nabla_Y]
=R(X,Y)-\nabla_YA_X.
\tag{A.7}
\]
The connection on endomorphisms is the one proved in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1).

If the local flow preserves the connection, (A.7) vanishes. Conversely the flow law and the chain rule show that the derivative of \(\phi_t^*\nabla\) is \(\phi_t^*(\mathcal L_X\nabla)\). Differences of connections are tensors: the derivative-of-a-scalar terms cancel when their Leibniz rules are subtracted. Thus this differentiation can be done entry by entry in any coordinate chart. If (A.7) vanishes, the pullback is constant on each flow interval by [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). This proves (A.4).

Linearity follows from the linearity of (A.7) in \(X\). For bracket closure, pullback by an affine local diffeomorphism preserves equation (A.7), by its definition as the derivative of a pulled-back connection. Thus, when \(X,Y\) are affine fields, \(\phi_t^*Y\) is an affine field on every common flow neighbourhood. Differentiating its zero equation at \(t=0\) gives the zero equation for \([X,Y]\). Smooth dependence, and commutation of these finite coordinate derivatives, follow from [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and 0.3. This argument is local at each point, hence proves global bracket closure.

The identity \([L_X,L_Y]=L_{[X,Y]}\) follows from the Jacobi identity for vector fields, [Principal bundles C.3](principal-bundles-and-associated-bundles.md#lemma-c-3). Expanding it using \(L_X=\nabla_X+A_X\) yields
\[
A_{[X,Y]}
=R(X,Y)+\nabla_XA_Y-\nabla_YA_X+[A_X,A_Y].
\]
Equation (A.4) says that the middle two terms are respectively \(R(Y,X)\) and \(-R(X,Y)\); their sum with the first term is \(-R(X,Y)\). This proves (A.5).

Along any smooth path \(\gamma\), the pair \(v=X|_\gamma,A=A_X|_\gamma\) obeys
\[
D_tv=-A\dot\gamma-T(v,\dot\gamma),\qquad
D_tA=R(v,\dot\gamma).
\tag{A.8}
\]
In any local frame this is a homogeneous linear ordinary differential equation for the \(n+n^2\) entries of \((v,A)\). [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) supplies the frame expression, and [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) gives uniqueness. A pair initially zero remains zero, successively on the finitely many chart pieces of a path. Any two points of a connected manifold can be joined by a piecewise smooth coordinate path, [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4). Thus a field with zero initial pair vanishes everywhere. Injection into the \(n+n^2\)-dimensional space gives the dimension bound by [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). □

**Corollary A.3 (Killing fields and their geodesic restrictions).** For a Riemannian metric and its Levi-Civita connection, a field is Killing exactly when
\[
g(\nabla_YX,Z)+g(Y,\nabla_ZX)=0.
\tag{A.9}
\]
It is then infinitesimally affine, \(A_X=-\nabla X\) is skew-adjoint, and its value and covariant derivative at one point determine it. The space of Killing fields has dimension at most \(n(n+1)/2\). Along an affinely parametrized geodesic,
\[
D_t^2X+R(X,\dot\gamma)\dot\gamma=0.
\tag{A.10}
\]

**Proof.** [Killing fields E.1](holonomy-killing-fields-and-analytic-extension.md#lemma-e-1) proves (A.9), its equivalence to preservation by the local flow, bracket closure, and (A.4) for the Levi-Civita connection. [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) proves that a local isometry preserves that connection. The one-jet injection is A.2, restricted to \(T_pM\oplus\mathfrak{so}(T_pM,g_p)\). In an orthonormal frame the second summand consists of skew matrices, with one free entry for each pair \(i<j\), and hence dimension \(n(n-1)/2\); [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2) constructs those frames. Finally \(D_tX=-A_X\dot\gamma\); differentiate, use \(D_t\dot\gamma=0\) and (A.4), to obtain (A.10) with the displayed sign. □

## B. Distance detects the smooth structure

**Lemma B.1 (Smooth distance coordinates).** At any point \(q\) of an \(n\)-dimensional Riemannian manifold, \(n>0\), one can choose nearby points \(b_1,\ldots,b_n\) so that
\[
D_b(y)=\bigl(d(y,b_1)^2,\ldots,d(y,b_n)^2\bigr)
\tag{B.1}
\]
is a smooth coordinate map near \(q\). This map and its local inverse depend smoothly on sufficiently small changes of the \(b_i\).

**Proof.** Work in a strongly convex neighbourhood supplied by [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5). For \(b,y\) there, let \(\sigma_y:[0,1]\to M\) be the unique affine minimizing geodesic from \(b\) to \(y\). Its constant speed and energy-length relation, [Riemannian connections F.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-3), give energy \(d(b,y)^2/2\). The first variation formula of [Jacobi fields A.3](jacobi-fields-conjugate-points-and-the-morse-index-theorem.md#theorem-a-3), with the initial endpoint fixed and the final endpoint varying with velocity \(w\), gives
\[
d_y\!\left(\tfrac12 d(b,y)^2\right)(w)
=g_y(\dot\sigma_y(1),w)=-g_y(\log_y b,w).
\tag{B.2}
\]
The final equality follows by reversing the same affine segment and using geodesic uniqueness, [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1). Smooth dependence on both endpoints is part of [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5).

Choose an orthonormal basis \(e_i\) at \(q\), as in [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2), and set \(b_i=\exp_q(\epsilon e_i)\) for one sufficiently small \(\epsilon>0\). The differential of (B.1) at \(q\) has rows \(w\mapsto-2\epsilon g_q(e_i,w)\), so it is invertible. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) gives the coordinate chart. For parameter dependence apply that same inverse theorem to the map \((b,y)\mapsto(b,D_b(y))\); its block derivative is invertible at the chosen data. Its inverse keeps \(b\) fixed and is therefore the desired smooth family of inverses. □

**Theorem B.2 (A distance isometry is a smooth metric isometry).** Any distance-preserving bijection \(f:(M,d_g)\to(N,d_h)\) is a smooth diffeomorphism and satisfies \(f^*h=g\). Conversely a smooth metric-preserving diffeomorphism preserves distance.

**Proof.** Such a bijection and its inverse are continuous. [Riemannian connections A.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-2) identifies the distance topology with the manifold topology. Near \(q=f(p)\), choose the points of B.1 so close to \(q\) that both they and their preimages \(a_i=f^{-1}(b_i)\) lie in respective strongly convex neighbourhoods of \(q,p\). This is possible by continuity of the inverse. Shrink the neighbourhood of \(p\) so that \(f\) takes it into the distance-coordinate chart. There
\[
D_b(f(x))=\bigl(d_g(x,a_1)^2,\ldots,d_g(x,a_m)^2\bigr),
\]
where \(m=\dim N\). Each component is smooth by [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5). Composing with the smooth inverse of \(D_b\) proves that \(f\) is smooth. Apply the same argument to its inverse. Thus their differentials are inverse linear maps, and the dimensions agree. If one manifold has dimension zero, connectedness makes it a point and bijectivity gives the same conclusion directly.

For a smooth curve \(c\) with \(c(0)=p,c'(0)=v\), normal coordinates and [Riemannian connections B.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-3) give
\[
\lim_{t\to0}\frac{d_g(p,c(t))}{|t|}=|v|_g.
\]
Indeed the logarithm of \(c(t)\) is \(tv+o(t)\), and in this normal ball its norm is the distance. Apply the identity to \(f\circ c\) and use distance preservation to obtain \(|df_pv|_h=|v|_g\). The polarization identity
\(2g(v,w)=|v+w|^2-|v|^2-|w|^2\)
then proves \(f^*h=g\). The converse, including preservation of the infimum of curve lengths, is [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). □

Write \(G=\operatorname{Isom}(M,g)\), with the compact-open topology, equivalently uniform convergence on compact subsets. Fix an orthonormal frame \(u:\mathbb R^n\to T_pM\) and put
\[
J(f)=df_pu\in\operatorname O(M).
\tag{B.3}
\]

**Lemma B.3 (Closed frame orbit without completeness).** The map \(J\) is a homeomorphism of \(G\) onto a closed subset of \(\operatorname O(M)\). Convergence in \(G\) to an isometry gives smooth convergence on compact subsets. In particular, convergence of \(J(f_j)\) to any orthonormal frame produces a global isometry as the smooth limit of \(f_j\).

**Proof.** Injectivity follows from A.1 and [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3). We give the global convergence argument, because a target exponential need not exist for every tangent vector.

First define a local compactness radius
\[
\rho(x)=\min\left(1,\sup\{r>0:\overline B(x,r)\text{ is compact}\}\right).
\tag{B.4}
\]
It is positive: a small closed distance ball is contained in a compact coordinate neighbourhood, by the local distance estimates in [Riemannian connections A.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-2). Every closed ball of radius less than \(\rho(x)\) is compact, since it is a closed subset of a larger compact ball. If \(s+d(x,y)<r<\rho(x)\), the closed \(s\)-ball at \(y\) is a closed subset of that compact \(r\)-ball. Letting \(r\) increase shows \(\rho(y)\geq\rho(x)-d(x,y)\); exchange \(x,y\) to see that \(\rho\) is 1-Lipschitz. Distance isometries preserve it. A Cauchy sequence \(y_j\) with \(\rho(y_j)\geq\delta>0\) converges in \(M\): its tail lies in the compact closed ball of radius \(3\delta/4\) about one sufficiently late \(y_j\). Compactness gives a convergent subsequence, and the Cauchy property gives convergence of the whole sequence, using [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations).

Suppose now \(J(f_j)\to a\), with \(a\) based at \(q\). On a sufficiently small normal neighbourhood of \(p\),
\[
f_j(x)=\exp_{f_j(p)}\!\left(df_j|_p\,\log_p x\right).
\tag{B.5}
\]
The target exponential is defined uniformly here for all sufficiently large \(j\): the initial frames lie in a compact subset of a frame chart near \(a\), and the local geodesic existence theorem gives a common small vector ball. [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1) and B.1 therefore give smooth convergence on smaller compact subsets.

Let \(U\) be the set of points having a neighbourhood on which this whole sequence converges smoothly on compact subsets. It is nonempty and open. Its local limits agree on overlaps and preserve the metric. For \(x,z\in U\), passage to the limit in the distance identity gives \(d(f(x),f(z))=d(x,z)\), including when the points lie in different members of the cover.

We show that \(U\) is closed. If \(x_k\in U\) tends to \(x\), the sequence \(f_j(x)\) is Cauchy. For any tolerance, first fix \(k\) with \(d(x,x_k)\) smaller than a third of it; then use convergence of \(f_j(x_k)\) and
\[
d(f_j(x),f_l(x))
\leq 2d(x,x_k)+d(f_j(x_k),f_l(x_k)).
\tag{B.6}
\]
Since \(\rho(f_j(x))=\rho(x)>0\), (B.4) shows \(f_j(x)\to y\in M\). Choose an orthonormal frame \(v\) at \(x\). The frames \(df_j|_xv\) lie over a compact set, so [Hopf–Rinow D.2](completeness-and-the-hopf-rinow-theorem.md#lemma-d-2) makes them precompact. Every convergent subsequence of these frames gives, by (B.5) centred at \(x\), a smooth limiting local isometry on the same sufficiently small connected normal neighbourhood \(V\) of \(x\). The neighbourhood can be fixed for all these subsequences because the frames over a compact neighbourhood of \(y\) form a compact set.

Any two such limits agree on \(V\cap U\), which contains a nonempty open set since \(x\) is in the closure of \(U\). They consequently have the same first data at a point of that set; A.1 makes them equal on connected \(V\). Thus all cluster frames are identical, and the whole frame sequence converges: otherwise a subsequence outside a fixed neighbourhood of the unique cluster frame would have another convergent subsequence by compactness. Formula (B.5) now gives smooth convergence on \(V\), so \(x\in U\). Connectedness implies \(U=M\).

The resulting global map \(f\) is distance preserving and satisfies \(f^*g=g\). To see that it is onto, use (B.5) near \(p\) and its smoothly varying local inverses near \(q=f(p)\). The inverse theorem of [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) shows that \(f_j^{-1}(q)\to p\) and the derivatives there converge to \(df_p^{-1}\). These are the actual global inverse maps on that neighbourhood by injectivity. Apply the preceding convergence argument to \(f_j^{-1}\), now at the fixed point \(q\), obtaining a global map \(h\). Smooth local convergence and the identities \(f_jf_j^{-1}=\operatorname{id}=f_j^{-1}f_j\) imply \(fh=hf=\operatorname{id}\): the moving intermediate points stay in a compact coordinate neighbourhood, on which convergence is uniform. Thus \(f\) is a global isometry. This proves that \(J(G)\) is closed and that its inverse parametrization gives smooth convergence.

For the remaining direction of continuity, fix \(f_0\), choose small \(\epsilon>0\), and put \(p_i=\exp_p(\epsilon ue_i)\). For every isometry \(f\) sufficiently close to \(f_0\) at these finitely many points,
\[
df_pue_i=\epsilon^{-1}\log_{f(p)}f(p_i).
\tag{B.7}
\]
The uniform small normal radius about \(f_0(p)\), supplied by the endpoint inverse of [Riemannian connections B.5](riemannian-connections-and-convex-neighbourhoods.md#theorem-b-5), justifies the formula: the vector on the right is the unique small logarithm, and the isometric vector \(\epsilon df_pue_i\) has that prescribed small norm. The right side is continuous in the finitely many values. This proves continuity of \(J\) in the compact-open topology.

Finally, the topology of uniform convergence on compact sets agrees here with the compact-open topology. In one direction, a compact image inside an open set has a positive distance from the complement after covering it by finitely many metric balls. In the other, cover a compact source set by finitely many small balls and impose closeness at their centres; the common 1-Lipschitz bound for isometries and the triangle inequality give uniform closeness on the source set. These observations also show directly that the preceding sequential convergence assertions describe the stated topology, since the frame bundle has countable coordinate neighbourhood bases. □

## C. Turning the closed orbit into a Lie group

We retain \(G,u,J\) from Part B. A useful consequence of the exponential formula is **smooth propagation of first data near an actual isometry**. Namely, on every fixed compact source set the map \(f\), and every finite number of its derivatives, are smooth functions of \(J(f)\), restricted to the possible frame values. Here “smooth” means that the functions extend smoothly to a neighbourhood in the ambient frame bundle.

To verify this consequence, fix an actual \(f_0\). Join \(p\) to a desired point by a finite chain of small normal neighbourhoods, each next centre lying in the preceding neighbourhood. [Curvature and holonomy C.4](curvature-and-holonomy-groups.md#lemma-c-4) supplies a piecewise smooth path, and compactness of its parameter interval gives a finite chain using [Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1). Start with (B.5). Evaluate and differentiate that formula at the next centre to obtain its new first data, and use the same exponential formula there. At \(J(f_0)\) every necessary segment exists. Openness of the finite-time geodesic domain and its smooth dependence, [Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1), permit all these operations for arbitrary initial frames sufficiently close to \(J(f_0)\). They need not be frames of actual isometries. Finitely many chains cover any given compact set. This proves the asserted smooth extensions, including their derivatives. Extensions from different chains need agree only on actual isometries; that is all that will be used.

**Lemma C.1 (A limiting infinitesimal symmetry is complete).** Choose frame coordinates \(z\) centred at \(u\). Suppose \(g_j\in G\), \(\epsilon_j>0\), \(\epsilon_j\to0\), and
\[
z(J(g_j))/\epsilon_j\longrightarrow w.
\tag{C.1}
\]
The normalized coordinate differences \((g_j-\operatorname{id})/\epsilon_j\) converge smoothly on compact coordinate subsets to a global Killing field \(X\). Its lifted first data at \(u\) are \(w\), and \(X\) is complete.

**Proof.** Let \(F(a,x)\) be any of the smooth propagation formulas just established, with \(F(0,x)=x\). In coordinates, the fundamental theorem of calculus gives
\[
\frac{F(a_j,x)-x}{\epsilon_j}
=\int_0^1 D_aF(sa_j,x)\frac{a_j}{\epsilon_j}\,ds
\longrightarrow D_aF(0,x)w.
\tag{C.2}
\]
The same formula after every fixed number of \(x\)-derivatives proves smooth convergence on compact subsets, by uniform continuity of the next derivatives, [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Taylor expansion of a coordinate change shows that these limits transform as tangent vectors. Since the actual maps agree on overlaps, so do their limiting vectors. They define a smooth global \(X\). Dividing \(g_j^*g-g=0\) by \(\epsilon_j\) and taking the limit with first derivatives gives \(\mathcal L_Xg=0\), the coordinate equation of [Killing fields E.1](holonomy-killing-fields-and-analytic-extension.md#lemma-e-1). At \(p\) the initial exponential formula has exactly the prescribed value and derivative, so the derivative of its lifted frame value is the identity in the \(a\)-coordinates. Hence the lifted first data of \(X\) are \(w\).

It remains to prove completeness, which does not follow from A.3. Lift each \(g_j\) to the orthonormal frame bundle by \(\widehat g_j(v)=dg_jv\). The first-derivative version of (C.2) gives, in any relatively compact frame chart,
\[
\widehat g_j(v)=v+\epsilon_j\widehat X(v)+\epsilon_j r_j(v),
\qquad \|r_j\|_{C^1}\longrightarrow0.
\tag{C.3}
\]
Here \(\widehat X\) is the generator of the natural lift of the local flow of \(X\); differentiating a flow and its first spatial derivatives gives exactly this vector field, by [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). The inverses have the same expansion with \(-\widehat X\), by local inversion and the chain rule.

For clarity we prove the iteration assertion needed from (C.3). In a frame chart about \(u\), choose a closed box and a smaller box containing \(u\). The vector field and its first derivative are bounded there. For one fixed sufficiently small \(\tau>0\), its integral curve \(v(t)\), \(|t|\leq2\tau\), stays in the smaller box, by [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Its exact one-step increment at time \(t\) differs from \(\epsilon_j\widehat X(v(t))\) by at most \(C\epsilon_j^2\): integrate the vector field over the step and use its derivative bound and the speed bound. For the approximate iterates the error consequently satisfies
\[
e_{k+1}\leq(1+C\epsilon_j)e_k+
\epsilon_j\eta_j+C\epsilon_j^2,\qquad e_0=0,
\tag{C.4}
\]
where \(\eta_j\to0\) bounds \(r_j\). Summing the geometric series gives
\(e_k\leq C_\tau(\eta_j+\epsilon_j)\)
for \(k\epsilon_j\leq\tau\). The bound keeps all iterates in the larger box for large \(j\): if there were a first exit, the same estimate up to that step would contradict the positive margin. For negative times apply this argument to the inverse maps. Taking integers \(m_j\) with \(m_j\epsilon_j\to t\) proves
\[
J(g_j^{m_j})=\widehat g_j^{\,m_j}(u)\longrightarrow v(t)
\quad (|t|<\tau).
\tag{C.5}
\]
For example, decrease \(\tau\) so \(C\tau<1/2\). The elementary inequalities
\((1+x)\leq(1-x)^{-1}\) for \(0\leq x<1\) and
\((1-x)^k\geq1-kx\), the latter by induction, give
\((1+C\epsilon_j)^k\leq2\) for \(k\epsilon_j\leq\tau\).
Summing at most \(k\) terms then gives the stated error bound directly.

B.3 now makes \(g_j^{m_j}\) converge to a global isometry \(h_t\). These maps depend smoothly on \(t\): their frames \(v(t)\) do, and the propagation formulas give smooth dependence near every fixed \(t\) and on every compact source set. Apply the same iteration estimate on a small neighbourhood of \(p\) where the local flow of \(X\) exists for \(|t|\leq2\tau\), decreasing \(\tau\) if necessary. It shows \(h_t=\phi_t^X\) on that neighbourhood for \(|t|<\tau\). Consequently
\[
h_sh_t=h_{s+t}
\tag{C.6}
\]
whenever \(|s|+|t|\) is sufficiently small: the equality holds on a smaller nonempty neighbourhood by the local flow law, and A.1 extends equality to all of connected \(M\).

This local group extends to all real parameters. Explicitly, for \(t\in\mathbb R\), choose a positive integer \(m\) with \(|t|/m\) in a fixed interval on which (C.6) applies, and define \(H_t=(h_{t/m})^m\). Two choices agree by refining to a common multiple and repeatedly applying (C.6) while the partial sums remain in that small interval. Taking a common sufficiently large \(m\) for \(s,t,s+t\) proves \(H_sH_t=H_{s+t}\); the two small factors commute by (C.6). Near any parameter \(t\), write \(H_{t+r}=H_th_r\), which proves smoothness.

At every point \(x\), a small local flow interval for \(X\) exists. Applying the same coordinate iteration estimate at \(x\), for a possibly smaller time interval depending on \(x\), shows \(h_r(x)=\phi_r^X(x)\) there. Thus the derivative of \(H_r(x)\) at zero is \(X_x\). Differentiating \(H_{t+r}(x)=H_r(H_t(x))\) at \(r=0\) gives \(\frac d{dt}H_t(x)=X_{H_t(x)}\) for all real \(t\). These are global integral curves, proving completeness. □

**Theorem C.2 (The isometry group and its Lie algebra).** With its compact-open topology, \(G\) is a finite-dimensional Lie group acting smoothly on \(M\), and
\[
\dim G\leq n(n+1)/2.
\tag{C.7}
\]
Its stabilizer at a point is compact. If \(M\) is compact, \(G\) is compact. Its one-parameter subgroups are exactly the flows of complete Killing fields. For a left action, the map from the group Lie algebra to its fundamental vector fields is an anti-isomorphism; negating those fields gives an isomorphism with the usual vector-field bracket. No completeness of \(M\) is required.

**Proof.** Work first with \(n>0\). In the tangent space \(T_u\operatorname O(M)\), let \(E\) be the set of velocities at zero of curves \(J(g(t))\) that are smooth as ambient frame curves, with \(g(0)=\operatorname{id}\). Multiplication and inversion of such frame-parametrized curves are smooth near zero before any manifold structure on \(G\) has been declared. Indeed,
\[
J(fg)=df_{g(p)}\,dg_pu
\]
is a smooth function of \(J(f),J(g)\) by the propagation formula and its derivatives. For inversion, solve the smooth local formula \(F(a,x)=p\) near \(a=0,x=p\) by [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) and differentiate its inverse. This gives a smooth expression for \(J(f^{-1})\).

At the identity, the derivative of the multiplication expression adds the two frame velocities, since each factor alone gives the identity on its own tangent variable. Thus products of the curves \(g_1(at)g_2(bt)\) show that \(E\) is a vector subspace. The zero curve is included. It has finite dimension \(d\leq\dim\operatorname O(M)=n(n+1)/2\), the frame dimension computed in [Riemannian connections F.2](riemannian-connections-and-convex-neighbourhoods.md#theorem-f-2).

Every \(w\in E\) is the first data of a complete Killing field: apply C.1 to \(g(1/j)\), \(\epsilon_j=1/j\). Conversely the global flow of any complete Killing field gives such a curve, smooth by [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). First-data injectivity in A.3 shows that these identifications are injective. Choose a basis \(w_1,\ldots,w_d\) of \(E\) and the corresponding complete fields \(X_i\). Write
\[
\Phi_a=\phi^{X_1}_{a_1}\circ\cdots\circ\phi^{X_d}_{a_d}.
\]
Choose a smooth coordinate slice \(s\mapsto u(s)\) through \(u\), tangent to a vector-space complement of \(E\). Linear algebra in [Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) supplies the complement. The map
\[
(a,s)\longmapsto\widehat\Phi_a(u(s))
\tag{C.8}
\]
has invertible derivative at zero, since its two derivative images are precisely those complementary spaces. [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes it a diffeomorphism on sufficiently small neighbourhoods.

The slice meets \(J(G)\) only at \(u\) near \(u\). Otherwise take nonzero \(s_j\to0\) with \(u(s_j)=J(r_j)\). Normalize the frame-coordinate differences by \(\epsilon_j=|z(J(r_j))|\). A subsequence converges to a unit tangent vector \(w\) in the complementary slice, by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Lemma C.1 makes that vector the first data of a complete Killing field. Its global flow puts \(w\) in \(E\), contradicting complementarity.

For \(f\) sufficiently close to the identity, (C.8) writes \(J(f)=\widehat\Phi_a(u(s))\). Then \(J(\Phi_a^{-1}f)=u(s)\), so the slice conclusion and injectivity of \(J\) give \(s=0\) and \(f=\Phi_a\). Conversely all these \(\Phi_a\) belong to \(G\). Hence (C.8) identifies \(J(G)\) locally with the embedded slice \(s=0\). Left translates give a \(d\)-dimensional smooth manifold structure on \(G\), with exactly its given topology by B.3. It is Hausdorff and second countable because \(J(G)\) is a subspace of the second-countable frame manifold.

Multiplication is smooth everywhere by the same frame expression and smooth propagation near any fixed pair of actual isometries. Inversion is smooth by solving \(F(a,x)=p\) near \(x=f_0^{-1}(p)\); its derivative in \(x\) is invertible at the fixed \(f_0\). In a target slice chart, the transverse coordinates of these maps vanish, so their ambient smoothness implies smoothness into \(G\). This proves the Lie-group assertion. The propagation formulas also prove joint smoothness of the action on every group chart and manifold chart.

The usual Lie-group exponential and uniqueness of one-parameter subgroups are proved in [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Differentiating a smooth action shows that a one-parameter subgroup is the global flow of its fundamental vector field; it preserves the metric, so that field is Killing. Conversely we have just proved that every complete Killing flow is a smooth one-parameter subgroup. The sign can be seen directly from conjugation: the fundamental field associated to \(\operatorname{Ad}(f)Y\) is \(f_*Y_M\), whereas differentiating \((\phi_t^X)_*Y_M\) gives \(-[X_M,Y_M]\), the negative of the pullback derivative in [Principal bundles C.3](principal-bundles-and-associated-bundles.md#lemma-c-3). Thus \([X,Y]_M=-[X_M,Y_M]\).

Finally \(J(G_p)\) is the closed subset \(J(G)\cap\operatorname O_p(M)\) of a compact orthogonal fibre, so \(G_p\) is compact. If \(M\) is compact, [Hopf–Rinow D.2](completeness-and-the-hopf-rinow-theorem.md#lemma-d-2) makes the whole orthonormal frame bundle compact, and B.3 makes \(G\) compact. In dimension zero \(M\) is one point and \(G\) is the trivial zero-dimensional Lie group, with all the asserted properties. □

## D. Frames, affine groups and complete fields

On the full frame bundle \(P=\operatorname{Fr}(TM)\), let \(\theta\) be the solder form and \(\omega\) the connection form. [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1) and H.2 prove that
\[
\eta=(\theta,\omega):TP\longrightarrow
\mathbb R^n\oplus\mathfrak{gl}(n,\mathbb R)
\tag{D.1}
\]
is a coframe, meaning a smooth linear isomorphism on each tangent space.

**Lemma D.1 (Natural lifts and the torsion term).** A diffeomorphism \(f\) has the equivariant lift \(\widehat f(u)=df_{\pi(u)}u\), which preserves \(\theta\). Conversely every equivariant bundle diffeomorphism preserving \(\theta\) has this form. The lift preserves \(\omega\) if and only if \(f\) is affine.

The generator \(\widehat X\) of the lifted local flow of \(X\) satisfies
\[
\theta_u(\widehat X)=u^{-1}X_p,\qquad
\omega_u(\widehat X)=-u^{-1}(A_X)_pu.
\tag{D.2}
\]
It preserves \(\theta\), is equivariant, and preserves \(\omega\) precisely when \(X\) is infinitesimally affine. In that case it commutes with every field having a constant value under \(\eta\).

**Proof.** Equivariance follows from \(df(ua)=(dfu)a\). Since \(\pi\widehat f=f\pi\), the definition of the solder form gives
\[
\theta_{\widehat f(u)}(d\widehat f\,V)
=(dfu)^{-1}df(d\pi V)=u^{-1}d\pi V.
\]
For the converse, if \(F\) covers \(f\), this same equation applied to arbitrary \(V\in T_uP\) says \(F(u)^{-1}df(d\pi V)=u^{-1}d\pi V\). The submersion \(d\pi\) is onto, so \(F(u)=dfu\). In particular \(df\) is invertible.

[Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) identifies the connection form with covariant differentiation. Its local expression along a frame path \(u(t)\) is the matrix of the derivatives of its columns:
\[
\omega(\dot u)=u^{-1}D_tu.
\tag{D.3}
\]
An affine map commutes with vector transport by A.1, so its lift preserves horizontal spaces; equivariance preserves the fundamental vertical fields, and [Connections A.2](connections-and-parallel-transport.md#theorem-a-2) then gives preservation of \(\omega\). Conversely preservation of \(\omega\) takes horizontal frame paths to horizontal frame paths, hence takes every parallel vector to a parallel vector. Along a curve, write any vector in a parallel frame; differentiating its coefficient column proves \(D_t(dfV)=dfD_tV\). At each point and in each tangent direction this is \(\nabla df=0\).

For the flow \(\phi_t\), the base velocity of \(d\phi_tu\) is \(X\), which proves the first identity of (D.2). For a column \(v\) of \(u\), choose a curve \(c(s)\) with \(c'(0)=v\). In the surface \(\phi_t(c(s))\), the coordinate derivatives commute. The definition of torsion in [Linear connections D.1](linear-and-affine-connections.md#theorem-d-1) therefore gives
\[
D_t(d\phi_t v)\big|_{t=0}=\nabla_vX+T(X,v)=-A_Xv.
\]
Substitute in (D.3) to obtain the second identity. Equivariance and preservation of \(\theta\) follow by differentiating the already proved identities for the lifted flow. Preservation of \(\omega\) is equivalent to the affine flow condition, also just proved. Finally if \(Z_b\) is the field with constant \(\eta(Z_b)=b\), then
\[
(\mathcal L_{\widehat X}\eta)(Z_b)
=\widehat X(\eta(Z_b))-\eta([\widehat X,Z_b])
=-\eta([\widehat X,Z_b]).
\]
The left side vanishes for an affine field. Invertibility of \(\eta\) proves the commutation assertion. This Lie-derivative formula is the degree-one identity in [Curvature and holonomy A.2](curvature-and-holonomy-groups.md#lemma-a-2). □

**Lemma D.2 (Automorphisms of a coframe).** Let \(N\) be connected and let \(\eta:TN\to\mathbb R^m\) be a smooth coframe. A diffeomorphism preserving \(\eta\) is determined by its value at any fixed \(v\in N\). Its values on compact subsets depend smoothly on that one value, restricted to the values that occur. The automorphisms form a Lie group of dimension at most \(m\), and evaluation at \(v\) is a smooth embedding onto a closed subset of \(N\). Its Lie algebra consists, with the left-action sign convention of C.2, of complete fields \(Z\) satisfying \(\mathcal L_Z\eta=0\).

**Proof.** Let \(Z_i=\eta^{-1}(e_i)\). A coframe-preserving map \(F\) carries each \(Z_i\) to itself, so it commutes with their local flows by uniqueness, [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). The map
\[
(t_1,\ldots,t_m)\longmapsto
\phi^{Z_m}_{t_m}\cdots\phi^{Z_1}_{t_1}(v)
\tag{D.4}
\]
has invertible derivative at zero, so [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) makes it a coordinate map near \(v\). Commuting \(F\) past the finite flow word expresses its value in this chart as the same word starting at \(F(v)\). The expression is smooth for arbitrary nearby starting values. Flow words can reach every point of \(N\): their reachability classes are open by (D.4), and partition the connected manifold into disjoint open sets. Propagating the formula along a finite word proves uniqueness and smooth dependence near every point; finitely many such neighbourhoods handle a compact set.

Define the Riemannian metric \(h=\sum_i\eta^i\otimes\eta^i\). It is smooth and positive definite because \(\eta\) is a coframe. Every automorphism is an isometry of \(h\). The automorphism subgroup is closed in \(\operatorname{Isom}(N,h)\): C.2 and B.3 give smooth local convergence of isometries, and the identity \(F^*\eta=\eta\) passes to the limit with first derivatives. [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) now makes it an embedded Lie subgroup. Its action is smooth by C.2. A one-parameter subgroup gives a complete field \(Z\) with \(\mathcal L_Z\eta=0\). Conversely that condition makes \((\phi_t^Z)^*\eta\) constant wherever the flow exists, by the chain rule and [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), so a complete such field gives a one-parameter subgroup.

If \(\mathcal L_Z\eta=0\), the last computation in D.1 gives \([Z,Z_i]=0\). In coordinates, differentiation of \(d\phi_{-t}^{Z_i}Z(\phi_t^{Z_i}x)\) equals the pullback of \([Z_i,Z]\), [Principal bundles C.3](principal-bundles-and-associated-bundles.md#lemma-c-3) and [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Hence the flows of every \(Z_i\) carry \(Z\) into itself. Its value at \(v\) determines it along all the words in (D.4), and hence everywhere. Thus evaluation of these infinitesimal fields at \(v\) is injective, proving both the dimension bound and injectivity of the derivative of the group evaluation map. The constant-rank theorem, [Local tools 1.4](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion), gives local immersion charts.

Evaluation is a homeomorphism onto its image and that image is closed. In fact preservation of the coframe forces
\[
dF_v=\eta_{F(v)}^{-1}\eta_v.
\tag{D.5}
\]
If \(F_j(v)\to w\), their \(h\)-orthonormal frame values consequently converge by (D.5). B.3 supplies a global limiting isometry, which still preserves the coframe; it is the required limiting automorphism. Conversely convergence in the group topology gives convergence of values. The same formulas, or their countable local bases, prove the homeomorphism assertion. A smooth injective immersion that is a homeomorphism onto its image is an embedding: in a constant-rank chart it is the coordinate inclusion, and the homeomorphism lets one restrict the ambient neighbourhood to exclude the rest of the image near the point. Thus evaluation has the stated embedding property. □

**Theorem D.3 (The affine transformation group).** The affine transformation group of a connected smooth \(n\)-manifold with a connection is a Lie group of dimension at most \(n+n^2\). It acts smoothly on \(M\). Its Lie algebra is the space of complete infinitesimally affine fields, with the sign convention in C.2. The topology is smooth convergence on compact subsets, equivalently the topology of one frame value \(f\mapsto df_pu\). The connection need not be complete.

**Proof.** Dimension zero is the trivial group on a point. Otherwise take the coframe (D.1) and the connected component \(P_0\) of a fixed frame \(u\). This component maps onto \(M\): lift a piecewise smooth path from \(\pi(u)\) to any desired base point horizontally, using [Connections C.1](connections-and-parallel-transport.md#theorem-c-1). The lifted path remains in \(P_0\).

Put \(K=\{a\in\operatorname{GL}(n,\mathbb R):R_a(P_0)=P_0\}\). It is an open subgroup: the inverse image of the open component \(P_0\) under \(a\mapsto ua\) is exactly \(K\). To check that equivalence, \(R_a(P_0)\) is the component containing \(ua\), since right translation is a homeomorphism. The subgroup and inverse conditions follow by composition. It is closed as well, because its complement is a union of its open cosets. Within any fibre of \(P_0\), two frames differ by exactly one \(a\in K\). Local sections with values in \(P_0\) give local trivializations with fibre \(K\). These claims follow directly by restricting the frame charts of [Principal bundles C.1](principal-bundles-and-associated-bundles.md#theorem-c-1) and A.2.

By D.2 the coframe automorphism group of \(P_0\) is a Lie group. In it take the subgroup \(H\) of maps commuting with every \(R_a\), \(a\in K\). It is closed: for fixed \(a,v\) the equation \(F(va)=F(v)a\) is a closed equality of continuous evaluations, and one intersects these equalities over all \(a,v\). [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) makes \(H\) a Lie subgroup.

Every \(F\in H\) descends to a diffeomorphism \(f\) on \(M\), because it maps each \(K\)-fibre onto a \(K\)-fibre; its inverse does the same. In local sections the formula \(f(x)=\pi F(s(x))\) proves smoothness. The solder-form calculation of D.1, applied on \(P_0\), says \(F(u)=dfu\); the connection-form calculation then says \(f\) is affine. Conversely the lift of an affine transformation that preserves \(P_0\) belongs to \(H\). Thus \(H\) identifies exactly with that subgroup \(A_0\) of the full affine group \(A\). The derivative evaluation injection in D.2 gives \(\dim A_0\leq\dim P_0=n+n^2\).

There is no connected-frame-bundle assumption here. Every component of \(P\) is \(R_aP_0\) for some \(a\): a horizontal path gives a frame in \(P_0\) over the base point of a chosen frame, and the two frames differ by such an \(a\). An equivariant lift preserving \(P_0\) therefore preserves every component, so \(A_0\) is normal in \(A\). Its cosets inject into the set of components of \(P\) by their image of \(P_0\); that set is countable because \(P\) is second countable and its components are disjoint nonempty open sets.

Give each coset the translated smooth structure of \(A_0\). This is a Hausdorff second-countable manifold, with each coset open. Evaluation \(J_A(f)=df_pu\) identifies its topology with its image topology in \(P\): on \(A_0\) this is D.2 restricted to the closed subgroup \(H\); on each other coset use the fixed natural lift of its representative. Distinct cosets have frame values in distinct components of \(P\).

The same finite chain of exponential formulas used at the start of Part C applies to affine maps by A.1, without any metric: near a fixed actual affine map, all the finitely many needed geodesic segments still exist for nearby initial frames. It expresses their values and derivatives smoothly in \(J_A(f)\). Consequently the formulas for \(J_A(fg)\) and \(J_A(f^{-1})\) used in C.2 prove smooth multiplication and inversion on every pair of cosets. As there, local embedded charts on each coset justify smoothness into the group. The action on \(M\) is smooth by those propagation formulas (also directly by the local-section formula for \(H\)). The same formulas show that frame convergence gives smooth convergence on compact sets; the reverse follows by evaluating first derivatives at \(p\).

Finally a smooth one-parameter subgroup acts by the global flow of its fundamental field, which is infinitesimally affine by differentiation. Conversely a complete infinitesimally affine field has affine flow maps for all real times, by A.2 on successive local intervals. Their natural lifts preserve \(P_0\), since each frame trajectory begins there. They depend smoothly on time by [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters), so give a smooth one-parameter subgroup of \(A_0\), by its frame embedding. This proves the Lie-algebra assertion and the sign is precisely the left-action sign already proved in C.2. □

**Theorem D.4 (Geodesic completeness makes affine fields complete).** If the connection is geodesically complete, every infinitesimally affine field is complete. In particular every Killing field on a complete Riemannian manifold is complete.

**Proof.** Let \(X\) be an affine field and lift it to \(\widehat X\) on \(P\). By D.1 it commutes with each standard horizontal field \(B(e_i)\), and with each fundamental vertical field \(\zeta_C\). The horizontal fields are complete by [Geodesics G.1](geodesics-normal-coordinates-and-curvature.md#theorem-g-1). The vertical fields have the complete flow \(R_{\exp(tC)}\), by [Connections A.2](connections-and-parallel-transport.md#theorem-a-2) and [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Choose a matrix basis for \(C\). These \(n+n^2\) complete fields span every tangent space by [Linear connections H.2](linear-and-affine-connections.md#theorem-h-2).

On a connected component of \(P\), their flow words reach every point, by the inverse-function and open-orbit argument in D.2. Fix a frame \(u\), and choose an interval \((-\epsilon,\epsilon)\) on which the integral curve of \(\widehat X\) starting there exists. If \(v=W(u)\), where \(W\) is a finite composition of the complete flows just listed, the curve
\[
t\longmapsto W(\phi_t^{\widehat X}(u))
\tag{D.6}
\]
exists on that same interval and is an integral curve of \(\widehat X\) starting at \(v\). Indeed vanishing brackets imply that each constituent flow preserves \(\widehat X\), by the derivative calculation in D.2. Two choices of \(W\) give the same curve by the uniqueness theorem of [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). Thus the maximal flow is defined for all starting frames in this component for the common interval \((-\epsilon,\epsilon)\). It is smooth there by that local flow theorem; existence on the common interval is the new assertion furnished by (D.6).

Iterating intervals of length less than \(\epsilon\) extends every trajectory for all positive and negative time, the pieces agreeing by uniqueness. The projection of this complete lifted trajectory is the integral curve of \(X\), by (D.2). Since \(P_0\) projects onto \(M\), all such base curves are complete. For a complete Riemannian metric, [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) gives geodesic completeness of its Levi-Civita connection, and A.3 makes every Killing field affine. The preceding argument then applies. □

## E. Passing to quotients and computing examples

**Theorem E.1 (The deck normalizer).** Let \(\pi:\widetilde M\to M\) be the universal covering of a connected manifold with a connection, and give \(\widetilde M\) the pulled-back connection. Let \(\Gamma\) be its deck group. Then
\[
\operatorname{Aff}(M)=
N_{\operatorname{Aff}(\widetilde M)}(\Gamma)/\Gamma.
\tag{E.1}
\]
For a Riemannian metric and its lifted metric the analogous formula is
\[
\operatorname{Isom}(M)=
N_{\operatorname{Isom}(\widetilde M)}(\Gamma)/\Gamma.
\tag{E.2}
\]
These are isomorphisms of Lie groups. The normalizers are closed, the deck group is discrete, and each quotient projection is a local diffeomorphism. In particular the group downstairs and its normalizer upstairs have the same dimension. Neither connection nor metric completeness is required.

**Proof.** The covering and lifting constructions, including uniqueness of based lifts, are proved in [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1) and [Flat connections D.3](flat-connections-and-infinitesimal-holonomy.md#theorem-d-3). For an automorphism \(f\) of \(M\), the composite \(f\pi\) is another universal covering. The based covering isomorphism gives a lift \(\widetilde f:\widetilde M\to\widetilde M\) with \(\pi\widetilde f=f\pi\). Applying the inverse construction to \(f^{-1}\) proves that the lift is a diffeomorphism. Covering charts show it preserves the pulled-back connection, or metric, respectively. Moreover
\(\widetilde f\gamma\widetilde f^{-1}\) is a deck map for every \(\gamma\in\Gamma\). Conversely a normalizing automorphism sends deck orbits to deck orbits, so descends to an automorphism, smooth and structure-preserving in covering charts. The kernel of descent is exactly \(\Gamma\). This proves the group equalities.

Write \(G\) for either group upstairs; its Lie structure and first-jet embedding are C.2 and D.3. The fibre \(\pi^{-1}(\pi(x))\) is closed and discrete. If deck maps \(\gamma_j\) converge in \(G\), their values at \(x\) eventually coincide: a convergent sequence in that fibre is eventually constant. Deck maps agreeing at one point agree everywhere by uniqueness of lifts. Thus \(\Gamma\) is closed and discrete in \(G\). If \(g_j\) normalize \(\Gamma\) and \(g_j\to g\), then for every \(\gamma\in\Gamma\)
\[
g_j\gamma g_j^{-1}\longrightarrow g\gamma g^{-1}\in\Gamma.
\]
Using inverses too gives \(g\Gamma g^{-1}=\Gamma\). Hence \(N=N_G(\Gamma)\) is closed. [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1) makes it an embedded Lie subgroup; [Local tools 4.1](local-tools-for-bundles-and-transport.md#4-quotients-by-a-closed-lie-subgroup) gives the smooth quotient \(N/\Gamma\). Since \(\Gamma\) has zero-dimensional tangent space, the quotient charts there are local diffeomorphisms. Normality makes multiplication and inversion smooth in these local charts.

For completeness, the abstract bijection with the group downstairs respects the Lie structures already constructed. Fix \(x\) over \(p\), and a covering sheet \(V\) containing \(x\). For \(f\) near the identity downstairs there is a unique lift with \(\widetilde f(x)\in V\); its value is the smooth expression \((\pi|_V)^{-1}(f(p))\), and its derivative is
\[
d\widetilde f_x=(d\pi_{\widetilde f(x)})^{-1}\,df_p\,d\pi_x.
\]
Thus its first jet depends smoothly on the first jet of \(f\). The embedded jet descriptions of C.2 and D.3, and the embeddedness of \(N\), make this a smooth map into \(N\). Conversely the jet of a descended map is obtained from this equation by multiplication by the two differentials of \(\pi\), so descent is smooth. These maps are local inverses; translating them proves (E.1) and (E.2) as Lie-group statements. □

**Proposition E.2 (Round spheres).** For the round sphere \(S_a^n\subset\mathbb R^{n+1}\) of radius \(a>0\), \(n\geq1\),
\[
\operatorname{Isom}(S_a^n)=O(n+1),\qquad
\mathfrak{kill}(S_a^n)=\{x\mapsto Bx:B^T=-B\}.
\tag{E.3}
\]
The dimension is \(n(n+1)/2\). On \(S_a^1\) the Killing fields are precisely constant angular-speed fields.

**Proof.** Orthogonal maps restrict to isometries. [Killing fields D.3](holonomy-killing-fields-and-analytic-extension.md#exercise-d-3) proves that every local sphere isometry extends uniquely to an ambient orthogonal map by extending its value and differential; that proof includes \(n=1\). In particular every global isometry has this form. Its explicit extension formula is smooth in the first jet, so the identification is an isomorphism of Lie groups by C.2.

For a skew matrix \(B\), the linear ODE gives \(e^{tB}\); differentiating \((e^{tB})^Te^{tB}\) gives zero and its value at zero is \(I\). Thus \(Bx\) is a complete Killing field. The sphere spans its ambient vector space, so this assignment is injective. There are \((n+1)n/2\) independent skew entries; A.3 bounds the entire Killing space by the same number, giving equality. For \(n=1\) every skew matrix is a constant multiple of \(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), whose field is constant angular rotation. The linear ODE and its global exponential are [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) and [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters). □

**Proposition E.3 (Euclidean space and flat tori).** Euclidean affine and metric transformations are, respectively,
\[
x\longmapsto Ax+b,\quad A\in GL(n,\mathbb R);
\qquad
x\longmapsto Qx+b,\quad Q\in O(n).
\tag{E.4}
\]
Their infinitesimal fields are \(Bx+b\), with arbitrary \(B\), or skew \(B\), respectively; all these fields are complete.

If \(L\subset\mathbb R^n\) is a full lattice and \(T_L=\mathbb R^n/L\) has the flat metric, then
\[
\begin{aligned}
\operatorname{Isom}(T_L)&=T_L\rtimes O(L),
&O(L)&=\{Q\in O(n):QL=L\},\\
\operatorname{Aff}(T_L)&=T_L\rtimes\operatorname{Aut}_{\mathbb Z}(L),
&\operatorname{Aut}_{\mathbb Z}(L)&=\{A\in GL(n,\mathbb R):AL=L\}.
\end{aligned}
\tag{E.5}
\]
The first linear group is finite and the second is discrete, conjugate to \(GL(n,\mathbb Z)\) in a lattice basis. Both identity components are \(T_L\), and all infinitesimal affine fields, hence all Killing fields, on the torus are translations.

**Proof.** The Euclidean Christoffel symbols vanish. Equation (A.1) says that every second derivative of an affine map is zero; its first derivative is constant on connected \(\mathbb R^n\), giving (E.4), with invertibility exactly when \(A\) is invertible. The metric identity makes \(A^TA=I\). For a field, Theorem A.2 with \(R=T=0\) says that \(-DX\) is constant, so \(X=Bx+b\). The Killing equation is \(B+B^T=0\). Its integral curve is
\[
\Phi_t(x)=e^{tB}x+\int_0^t e^{(t-s)B}b\,ds,
\]
defined for all real \(t\); differentiation verifies the equation and uniqueness is [Local tools 2.1](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters).

Choose a lattice basis and write \(L=V\mathbb Z^n\), with \(V\) invertible. Nonzero lattice vectors are uniformly separated from zero because
\(\lvert Vk\rvert\geq\lvert k\rvert/\|V^{-1}\|\).
Translations by \(L\) therefore act freely and properly discontinuously; the quotient covering and its metric are constructed in [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3). Its universal cover is \(\mathbb R^n\), which contracts by \(x\mapsto tx\). Conjugation by \(f(x)=Ax+b\) sends the translation by \(\lambda\) to translation by \(A\lambda\). E.1 now proves (E.5), including the multiplication
\[
(\bar b,A)(\bar d,C)=(\bar b+A\bar d,AC).
\]
Here \(A\) acts on the torus because it preserves \(L\).

In a lattice basis \(V^{-1}AV\) and its inverse have integer entries. Their determinants are integers with product one, so the determinant is \(\pm1\); conversely an integer matrix of determinant \(\pm1\) has integer inverse by the cofactor formula. This is exactly \(GL(n,\mathbb Z)\), a discrete set of matrices. If \(Q\in O(L)\), the image of each fixed lattice basis vector has the same length as that vector. Only finitely many lattice vectors lie in a bounded ball, since their integer coordinates are bounded by \(\|V^{-1}\|\) times its radius. There are consequently only finitely many possible ordered images of the basis, proving finiteness of \(O(L)\).

The torus is connected, being the continuous image of \(\mathbb R^n\); the quotient linear groups in (E.5) are discrete. The identity components are therefore exactly its translations. One can also see every infinitesimal field directly: its unique lift is obtained by applying \((d\pi_x)^{-1}\) to the field at \(\pi(x)\). It is affine locally, hence \(Bx+b\) by the same equation as above. Deck invariance requires \(B(x+\lambda)+b=Bx+b\), so \(B\lambda=0\) for every lattice vector. Since \(L\) spans, \(B=0\). All constant fields descend and are Killing. □

## F. Completeness and affine rigidity

An affine map preserves a connection. A metric supplies additional parallel data, so an affine transformation of its Levi–Civita connection need not preserve the metric. Completeness severely restricts that difference.

**Theorem F.1 (A complete manifold with a strict homothety).** Suppose a connected complete Riemannian manifold admits a diffeomorphism \(f\) with \(f^*g=c^2g\), where \(c>0\) and \(c\ne1\). Then the manifold is globally isometric to Euclidean space.

**Proof.** Replace \(f\) by its inverse if necessary, so \(0<c<1\). Lengths of curves scale by \(c\); applying the same observation to \(f^{-1}\) proves
\[
d(fx,fy)=c\,d(x,y).
\]
Starting at \(x_0\), put \(x_k=f^kx_0\). The triangle inequality gives, for \(m>k\),
\[
d(x_k,x_m)\leq
d(x_0,fx_0)\sum_{j=k}^{m-1}c^j
\leq \frac{c^k}{1-c}\,d(x_0,fx_0).
\]
Metric completeness gives \(x_k\to q\); continuity gives \(f(q)=q\). If \(q'\) were another fixed point, \(d(q,q')=c\,d(q,q')\) would force \(q=q'\).

The Levi–Civita connection for \(c^2g\) is the same as that for \(g\): it is torsion-free and compatible with both, so uniqueness in [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3) applies. Naturality there shows \(f\) is affine. Write \(df_q=cO\), where \(O\) is orthogonal on \(T_qM\). [Hopf–Rinow B.2](completeness-and-the-hopf-rinow-theorem.md#theorem-b-2) makes
\(E=\exp_q:T_qM\to M\) defined everywhere and onto. Lemma A.1 gives
\[
E(cOv)=f(E(v)).
\tag{F.1}
\]
If \(E(v)=E(w)\), iteration gives
\(E(c^kO^kv)=E(c^kO^kw)\).
For large \(k\) both vectors lie in the normal ball where \(E\) is injective ([Geodesics B.1](geodesics-normal-coordinates-and-curvature.md#theorem-b-1)). Hence \(v=w\).

It remains to prove that this bijection is an isometry; injectivity alone would not exclude a singular derivative. Set \(h=E^*g\), a smooth bilinear tensor on the entire vector space, initially allowing degeneracy. Differentiating (F.1) and using \(f^*g=c^2g\) yields
\[
h_v(V,W)=h_{cOv}(OV,OW)
=h_{c^kO^kv}(O^kV,O^kW).
\tag{F.2}
\]
At zero, \(dE_0=I\), so \(h_0=g_q\). Smoothness implies
\(\|h_z-g_q\|\to0\) as \(z\to0\), where the operator norm uses \(g_q\). The difference between the last expression in (F.2) and \(g_q(V,W)\) is at most
\[
\|h_{c^kO^kv}-g_q\|\,|V|\,|W|,
\]
because \(O^k\) is orthogonal. It tends to zero. Thus \(E^*g=g_q\) everywhere. Its differential is invertible everywhere, so the inverse theorem makes the bijection \(E\) a global diffeomorphism and isometry. This is the contraction argument of [De Rham decomposition G.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-g-2) with an orthogonal factor allowed in the contraction. It also covers the zero-dimensional point. □

**Theorem F.2 (Irreducible factors and identity components).** Let \(M\) be connected and complete, with irreducible full real holonomy representation and positive dimension. Every affine transformation is an isometry, except when \(M\) is the Euclidean line.

For a complete simply connected manifold with the de Rham decomposition
\[
M=\mathbb R^r\times M_1\times\cdots\times M_k,
\tag{F.3}
\]
where the \(M_i\) are non-Euclidean irreducible factors, one has
\[
\begin{aligned}
\operatorname{Aff}(M)^0&=
\operatorname{Aff}(\mathbb R^r)^0
\times\prod_i\operatorname{Isom}(M_i)^0,\\
\operatorname{Isom}(M)^0&=
\operatorname{Isom}(\mathbb R^r)^0
\times\prod_i\operatorname{Isom}(M_i)^0.
\end{aligned}
\tag{F.4}
\]
An arbitrary affine transformation preserves the Euclidean distribution and permutes the non-Euclidean factor distributions; those permutations need not belong to the identity component.

**Proof.** If \(f\) is affine, \(f^*g\) is a parallel positive definite symmetric tensor. Write it as \(g(S\,\cdot,\cdot)\); the induced tensor-connection rules in [Linear connections C.1](linear-and-affine-connections.md#theorem-c-1) show that \(S\) is parallel and self-adjoint. Transport around a loop commutes with \(S_p\). The real spectral proof in [De Rham decomposition H.2](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-h-2) decomposes \(T_pM\) into its orthogonal eigenspaces, all invariant under the full holonomy group. Irreducibility therefore gives \(S_p=\lambda I\). Parallel transport along paths gives the same constant \(\lambda>0\) at every point. Hence \(f\) is a homothety. If \(\lambda\ne1\), F.1 makes \(M\) Euclidean. The trivial holonomy representation of Euclidean space is irreducible in positive dimension only in dimension one. This proves the first assertion, including manifolds which are not simply connected.

[De Rham decomposition E.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-3) proves (F.3) with its uniqueness as a decomposition into parallel distributions. We spell out why its uniqueness applies to affine transformations, which might not initially be orthogonal. At a product point the holonomy is the product of the independent factor holonomies; its fixed subspace is exactly \(E_0=T\mathbb R^r\), and each nontrivial factor module \(E_i\) is irreducible. Every nontrivial irreducible invariant subspace \(W\) equals some \(E_i\): choose a nonzero projection of \(W\) onto \(E_i\). Since that factor has no fixed vectors, some factor-holonomy element \(h\), acting trivially on all other factors, has \((h-I)W\ne0\). Thus \(W\cap E_i\ne0\), and irreducibility forces \(W=E_i\). This is also the module argument in [De Rham decomposition E.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-3).

By transport naturality (A.2), \(df_p\) conjugates full holonomy at \(p\) to full holonomy at \(f(p)\). It consequently carries the fixed subspace to the fixed subspace and the nontrivial irreducible subspaces to a permutation of their counterparts. Parallel transport makes that permutation independent of the point. The image distributions vary continuously with \(f\), so the permutation is constant on the identity component and equals the identity there.

Suppose first that every distribution is preserved. In product coordinates the derivative of each output component vanishes on all the other input distributions. A connected manifold is joined by piecewise coordinate paths ([Local tools 0.2](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations)), so that output depends only on its own input. Thus
\[
f(x,y_1,\ldots,y_k)
=(f_0(x),f_1(y_1),\ldots,f_k(y_k)).
\]
The inverse has the same splitting, proving each factor map is a diffeomorphism. The product connection equation, proved in [De Rham decomposition E.3](holonomy-and-the-de-rham-decomposition-theorem.md#theorem-e-3), makes each \(f_i\) affine on its factor. The first part of the present proof makes \(f_i\) an isometry for \(i\geq1\). The Euclidean factor is unrestricted within its affine group. For a permutation of distributions the same argument applies after reordering output factors; maps between different factors are only asserted to be affine.

All these product identifications and their inverses are smooth: values and first derivatives of the factor maps are obtained by restricting the product first jet, and C.2 and D.3 give the jet embeddings. A finite product of connected Lie groups is connected; conversely the projection of a connected set to any factor is connected. Therefore the identity component of a finite product is the product of identity components. Applying this to the subgroup with no factor permutation proves the affine formula in (F.4). For an isometry, its Euclidean factor must also be an isometry, and the same argument gives the second formula. Zero-dimensional Euclidean factors and empty products mean the trivial group. □

**Corollary F.3 (Bounded affine fields).** On a connected complete Riemannian manifold, every bounded infinitesimal affine field is Killing. If its universal cover has no Euclidean de Rham factor, then
\(\operatorname{Aff}(M)^0=\operatorname{Isom}(M)^0\).
The same equality holds on every compact connected Riemannian manifold.

**Proof.** Theorem D.4 makes every infinitesimal affine field \(X\) complete. Lift the metric and the field to the universal cover. Completeness of the lifted metric is [Hopf–Rinow E.4](completeness-and-the-hopf-rinow-theorem.md#corollary-e-4): a lifted geodesic can be continued by lifting its complete projected geodesic. More explicitly, the lift of the field is defined by the inverse covering differential. Each complete integral curve downstairs has a unique path lift on every compact time interval by [Flat connections D.1](flat-connections-and-infinitesimal-holonomy.md#lemma-d-1); uniqueness joins these lifts for all real times. They are integral curves upstairs. Local covering charts and uniqueness of ODE solutions make the resulting flow smooth. It consists of affine transformations, starts at the identity, and lies in the identity component in F.2.

On the product universal cover the lifted generator consequently has the form
\[
\widetilde X(x,y_1,\ldots,y_k)
=(Bx+b,Y_1(y_1),\ldots,Y_k(y_k)),
\tag{F.5}
\]
with every \(Y_i\) Killing. If \(|X|\) is bounded, so is \(|\widetilde X|\), because the covering is a local isometry. Fix all \(y_i\) and put \(x=tv\). The product norm bounds \(|tBv+b|\) for all real \(t\), forcing \(Bv=0\) for every \(v\). Thus \(B=0\) and \(\widetilde X\) is Killing. The Killing equation is local, so it descends to \(X\).

If there is no Euclidean factor, (F.5) is Killing without a boundedness hypothesis. The Lie algebra description D.3 then shows that every one-parameter affine subgroup consists of isometries. The identity component is generated by its exponential neighbourhood, as proved in [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters), so it is contained in the isometry group. These paths lie in its identity component; the reverse inclusion is immediate from the Levi–Civita naturality and the common jet topology. If \(M\) is compact, [Hopf–Rinow B.3](completeness-and-the-hopf-rinow-theorem.md#corollary-b-3) gives completeness and every smooth field is bounded. The first argument then gives the same Lie-algebra equality and identity-component equality. □

## G. What maximal symmetry forces

The dimensions of fields and of global transformation groups need not agree on an incomplete manifold. The first theorem concerns all fields with locally structure-preserving flows; the next two concern groups of transformations defined on the whole manifold.

**Theorem G.1 (Maximal infinitesimal symmetry).** If a connected Riemannian \(n\)-manifold, \(n\geq2\), has \(n(n+1)/2\) linearly independent Killing fields, its sectional curvature is constant. If a connected manifold with a connection has \(n+n^2\) linearly independent infinitesimal affine fields, its torsion and curvature vanish and it has local coordinates in which the connection coefficients vanish. No completeness hypothesis is needed.

**Proof.** At any \(p\), the injective Killing first-data map from A.3 takes values in
\(T_pM\oplus\mathfrak{so}(T_pM)\).
Equality of dimensions makes it onto. In particular, given any skew map \(B\), there is a Killing field with \(X(p)=0\) and \((\nabla X)_p=B\). Its local flow fixes \(p\), and its differential there solves \(\dot F=BF\), so equals \(e^{tB}\). Thus the curvature at \(p\) is invariant under these orthogonal maps: local isometries preserve the Levi–Civita connection by [Riemannian connections A.3](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-3), and hence preserve its curvature.

We record explicitly the elementary rotation facts used here and below. A rotation in a coordinate two-plane, identity on the perpendicular complement, is the exponential of the skew matrix with entries \(B_{ij}=-\theta,B_{ji}=\theta\); the two-dimensional exponential and its angles are [Connections E.1](connections-and-parallel-transport.md#lemma-e-1). Such plane rotations generate \(SO(m)\). Indeed, successively rotate in the planes containing the first coordinate axis to eliminate the other coordinates of the first column of an orthogonal matrix, ending with \(e_1\). If a negative sign remains, a rotation by \(\pi\) in a plane containing that axis changes it. The remaining block is orthogonal with determinant one; induction reduces it in its own coordinate planes. The terminal one-dimensional block is \(1\). Reversing this finite elimination writes the original matrix as a product of plane rotations. Each rotation has a path to the identity, so \(SO(m)\) is connected. Invariance under small \(e^{tB}\) implies invariance under every \(e^{tB}\) by finite subdivision of \(t\), and hence under \(SO(n)\).

For \(n\geq3\), any two unoriented tangent two-planes are carried to each other by an element of \(SO(n)\): choose orthonormal bases of the planes, extend to orthonormal bases of the whole space by subtracting projections and normalizing, and choose the sign of one complementary basis vector to make the resulting map have determinant one. For \(n=2\) there is only one tangent two-plane. Thus at every point all sectional curvatures have a common value \(\kappa(p)\). [Sectional curvature A.1](sectional-curvature-and-space-forms.md#theorem-a-1) proves, by polarization of the algebraic curvature symmetries, that
\[
R_p(u,v)w=\kappa(p)\bigl(g_p(v,w)u-g_p(u,w)v\bigr).
\tag{G.1}
\]
A smooth local orthonormal frame, obtained by the same Gram–Schmidt operations on a coordinate frame, shows that \(\kappa\) is smooth: it is the curvature of the plane spanned by the first two frame vectors. Every local Killing flow preserves it, so \(X\kappa=0\). The first-data map is onto also in its value component, and hence Killing values span every tangent space. It follows that \(d\kappa=0\); along coordinate paths it is constant, and connectedness makes it globally constant.

For the affine statement, A.2 gives an injective map of the affine-field space into
\(T_pM\oplus\operatorname{End}(T_pM)\), again onto by the assumed dimension. Choose \(X(p)=0\) and \(A_X(p)=-I\). Since \(A_X=-\nabla X-T(X,\cdot)\), this means \(dX_p=I\). Its local affine flow fixes \(p\) and has differential \(e^tI\). Torsion and curvature are natural under affine maps: substituting the transported connection and bracket into their definitions gives, for any affine \(f\),
\[
df\,T(u,v)=T(df\,u,df\,v),\qquad
df\,R(u,v)w=R(df\,u,df\,v)df\,w.
\tag{G.2}
\]
The bracket naturality is [Principal bundles C.3](principal-bundles-and-associated-bundles.md#lemma-c-3) and the connection tensor definitions are [Linear connections A.2](linear-and-affine-connections.md#theorem-a-2) and [Linear connections B.3](linear-and-affine-connections.md#theorem-b-3). For this particular flow, (G.2) says
\(e^tT_p=e^{2t}T_p\) and \(e^tR_p=e^{3t}R_p\).
Choosing a small nonzero \(t\) forces both tensors to vanish. This works at every \(p\). [Sectional curvature G.1](sectional-curvature-and-space-forms.md#theorem-g-1) supplies the complete local-coordinate proof that \(T=R=0\) is equivalent to vanishing connection coefficients in suitable charts. □

**Theorem G.2 (Maximal global isometry groups).** A connected Riemannian manifold of dimension \(n\geq2\) has an isometry group of dimension \(n(n+1)/2\) if and only if it is isometric to one of
\[
\mathbb R^n,\qquad H_a^n,\qquad S_a^n,\qquad
\mathbb{RP}_a^n=S_a^n/\{I,-I\},\quad a>0.
\tag{G.3}
\]
In dimension one, the manifolds with a one-dimensional isometry group are the line and the circles, with their arclength metrics.

**Proof.** By C.2 the group's Lie algebra is the space of complete Killing fields. Maximal dimension fills the entire possible first-data space at every point. Choose \(n\) such fields whose values form a tangent basis. The map obtained by composing their small flows and applying them to \(p\) has invertible derivative at zero; [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) shows that the orbit contains a neighbourhood of \(p\). The same is true at every point. Orbits of the identity component are therefore disjoint open sets; connectedness forces a single orbit. [Hopf–Rinow B.3](completeness-and-the-hopf-rinow-theorem.md#corollary-b-3) now proves completeness of \(M\). This step obtains completeness from the isometry group; it was not assumed.

Theorem G.1 gives constant curvature. [Sectional curvature D.2](sectional-curvature-and-space-forms.md#theorem-d-2) and [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3) identify
\[
M=X_\kappa/\Gamma
\]
where \(X_\kappa\) is the corresponding complete simply connected Euclidean, spherical or hyperbolic model, and \(\Gamma\) is its freely acting deck group. The simply connected assertions for \(n\geq2\) are [Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3). Write \(G=\operatorname{Isom}(X_\kappa)\). It has dimension \(n(n+1)/2\). In the Euclidean and spherical cases this follows from E.2 and E.3. In the hyperbolic case use the hyperboloid
\[
H_a^n=\{(x,t):|x|^2-t^2=-a^2,\ t>0\},\qquad o=(0,a).
\]
Spatial rotations give \(n(n-1)/2\) independent infinitesimal stabilizers at \(o\). For each unit spatial vector \(v\), the map which is the identity on \(v^\perp\) and is
\[
\begin{pmatrix}\cosh s&\sinh s\\ \sinh s&\cosh s\end{pmatrix}
\]
on the \((v,t)\)-plane preserves the Lorentz form and its future sheet. It restricts to an isometry of the induced metric. The \(n\) coordinate boost fields have independent values at \(o\), so together these transformations attain the upper bound of A.3. They also act transitively with spatial rotations: the points
\((a\sinh s\,v,a\cosh s)\), \(s\geq0\), exhaust the hyperboloid by [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2). Both rotations and boosts have paths to the identity.

By E.1, \(N_G(\Gamma)\) has the same dimension as \(G\), so its embedded inclusion is locally a diffeomorphism at the identity. It therefore contains an identity neighbourhood, and hence all of \(G^0\) by generation from that neighbourhood ([Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters)). For any fixed \(\gamma\in\Gamma\), conjugation
\[
G^0\longrightarrow\Gamma,\qquad h\longmapsto h\gamma h^{-1}
\]
is continuous and has connected domain and discrete target. It is constant, so \(G^0\) centralizes \(\Gamma\).

On \(\mathbb R^n\), a map commuting with every translation satisfies
\(\gamma(x)=x+b\), by applying commutation to \(x=T_x(0)\). If it also commutes with every rotation in \(SO(n)\), then \(b\) is fixed by all such rotations. For \(n\geq2\) every nonzero vector is moved by a rotation in a plane containing it, so \(b=0\).

On \(H_a^n\), the point \(\gamma(o)\) must be fixed by all spatial \(SO(n)\) rotations. Its spatial coordinate is consequently zero, and the future hyperboloid equation then forces \(\gamma(o)=o\). Commutation with the transitive rotations and boosts gives \(\gamma(x)=x\) for every \(x\).

On \(S_a^n\), the stabilizer in \(SO(n+1)\) of a point \(p\) rotates its \(n\)-dimensional perpendicular space. Its only fixed points on the sphere are \(p,-p\), since \(n\geq2\). Thus a map commuting with \(SO(n+1)\) has \(\gamma(p)\in\{p,-p\}\). The scalar \(\langle\gamma(p),p\rangle/a^2\) is continuous with values in \(\{1,-1\}\) on the connected sphere, so its sign is constant. Hence \(\gamma=I\) or \(-I\). These arguments show that the only deck possibilities are the trivial group in the first two cases, and either the trivial or antipodal group in the spherical case.

Conversely the first three models have the stated maximal dimensions by the preceding calculations. The antipodal group is central in \(O(n+1)\) and acts freely, so E.1 gives
\(\operatorname{Isom}(\mathbb{RP}_a^n)=O(n+1)/\{I,-I\}\),
with the same dimension. [Sectional curvature D.3](sectional-curvature-and-space-forms.md#theorem-d-3) constructs its quotient metric.

In dimension one the orbit argument still proves completeness. Curvature is zero, since it is alternating in two tangent inputs ([Linear connections B.3](linear-and-affine-connections.md#theorem-b-3)). The complete flat classification [Sectional curvature G.2](sectional-curvature-and-space-forms.md#theorem-g-2) makes the universal cover the metric line: equivalently its global unit parallel frame gives arclength coordinate on \(\mathbb R\). Every deck isometry is \(x\mapsto\varepsilon x+b\) by E.3. A reflection has the fixed point \(b/2\), so cannot be a nontrivial deck map. [Sectional curvature G.3](sectional-curvature-and-space-forms.md#theorem-g-3) shows that a discrete translation subgroup of \(\mathbb R\) is zero or \(\ell\mathbb Z\), \(\ell>0\). The quotients are the line or the circle of circumference \(\ell\); E.2 and E.3 show that their isometry groups have dimension one. □

**Theorem G.3 (Maximal global affine groups).** A connected \(n\)-manifold with a connection has affine transformation group of dimension \(n+n^2\) if and only if it is affinely isomorphic to \(\mathbb R^n\) with its standard connection. For \(n=0\) this means the point.

**Proof.** By D.3 the Lie algebra consists of complete infinitesimal affine fields. The full dimension makes their first-data map onto at every \(p\). Theorem G.1 therefore gives \(T=R=0\). We must still prove completeness; transitivity of an affine group alone would not do so.

At each \(p\) choose a complete affine field \(X\) with \(X(p)=0\) and \(dX_p=I\). Its global flow \(f_t\) fixes \(p\) and has \(df_t|_p=e^tI\). Given any \(v\in T_pM\), choose \(s>0\) large enough that \(e^{-s}v\) lies in a small exponential neighbourhood. The geodesic with this initial vector exists on an open time interval containing \([0,1]\). Its image under \(f_s\) is a geodesic on the same interval with initial vector \(v\), by A.1. Hence the geodesic with any initial vector exists at least through time one. For any finite positive time \(T\), apply the same assertion to \(Tv\) and rescale its affine parameter; for negative times use \(-v\). Geodesic uniqueness ([Geodesics A.1](geodesics-normal-coordinates-and-curvature.md#theorem-a-1)) joins these segments to the entire real line. Thus the connection is geodesically complete.

[Sectional curvature G.2](sectional-curvature-and-space-forms.md#theorem-g-2) now gives \(M=\mathbb R^n/\Gamma\) with its standard affine connection and a freely acting deck subgroup \(\Gamma\subset\operatorname{Aff}(\mathbb R^n)\). E.1 and the assumed dimension show that its normalizer has full dimension in \(\operatorname{Aff}(\mathbb R^n)\). As in G.2, it contains the identity component and that component centralizes \(\Gamma\). It contains all translations and all positive scalar dilations, each joined to the identity by an explicit path. Commutation with translations makes any \(\gamma\in\Gamma\) a translation \(x\mapsto x+b\). Commutation with \(x\mapsto2x\) then gives \(b=2b\), so \(b=0\). The deck group is trivial, proving the result in every positive dimension, including one. Conversely E.3 identifies the Euclidean affine group with \(\mathbb R^n\rtimes GL(n,\mathbb R)\), of dimension \(n+n^2\). A connected zero-dimensional manifold is a point and its group has dimension zero. □

## H. Worked comparisons

**Exercise H.1 (Euclidean fields and the bracket sign).** Determine all infinitesimal affine and Killing fields on Euclidean space and their brackets. Compare the usual vector-field bracket with the commutator of affine matrices.

**Solution.** Proposition E.3 gives
\[
X(x)=Bx+b,\qquad Y(x)=Cx+d,
\]
with arbitrary matrices for affine fields and skew matrices for Killing fields. In coordinates the usual bracket is \(dY(X)-dX(Y)\), hence
\
[X,Y=(CB-BC)x+Cb-Bd.
\tag{H.1}
\]
The homogeneous affine matrices representing the same generators are
\[
\widehat X=\begin{pmatrix}B&b\\0&0\end{pmatrix},
\qquad
\widehat Y=\begin{pmatrix}C&d\\0&0\end{pmatrix}.
\]
Their matrix commutator is
\[
[\widehat X,\widehat Y]
=\begin{pmatrix}BC-CB&Bd-Cb\\0&0\end{pmatrix}.
\tag{H.2}
\]
Thus the map taking a matrix generator to its field for the left action is an anti-homomorphism, as in C.2; putting a minus sign in that map makes it a homomorphism for the usual field bracket. At any point \(p\), the derivative gives \(B=dX_p\) and the value then gives \(b=X(p)-Bp\), explicitly recovering the field from its first data. The affine field space and group both have dimension \(n+n^2\); the Killing field space and isometry group both have dimension \(n+n(n-1)/2=n(n+1)/2\). The flows are the complete flows written in E.3. □

**Exercise H.2 (Square and rectangular tori).** Compare the full isometry and affine groups and their fields for
\[
L_{\mathrm{sq}}=\mathbb Z(1,0)+\mathbb Z(0,1),
\qquad
L_{\mathrm{rec}}=\mathbb Z(1,0)+\mathbb Z(0,\sqrt2).
\]
Do the isometry-group dimensions distinguish the metrics?

**Solution.** For the square lattice the unit lattice vectors are exactly
\(\pm e_1,\pm e_2\). An orthogonal lattice map must take the ordered standard basis to a signed permutation of that basis; each such permutation does preserve the lattice. There are \(2^2\cdot2=8\) possibilities. For the rectangular lattice a vector \((m,\sqrt2\,n)\) has squared length \(m^2+2n^2\). Its shortest nonzero vectors are only \(\pm e_1\). Any orthogonal lattice map therefore preserves the first axis and its perpendicular axis, giving just the four diagonal sign matrices. All four do preserve the lattice.

By E.3 the respective isometry groups are the translation torus semidirect these groups of orders eight and four. Their identity components are both two-dimensional tori, so their dimensions do not distinguish the metrics. Their point stabilizers do: an isometry between the two tori would conjugate stabilizers, contradicting the different orders.

In each lattice's own basis its full affine group is
\[
(\mathbb R^2/\mathbb Z^2)\rtimes GL(2,\mathbb Z).
\]
Indeed the linear identification between the bases induces an affine diffeomorphism of the tori and conjugates the affine groups. In the original rectangular Euclidean coordinates its linear factors are \(VAV^{-1}\), \(A\in GL(2,\mathbb Z)\), \(V=\operatorname{diag}(1,\sqrt2)\), usually not orthogonal. Every infinitesimal affine or Killing field on either torus is a constant translation; both field spaces have dimension two. □

**Exercise H.3 (The open Euclidean ball).** On the open unit ball \(B^n\subset\mathbb R^n\), \(n\geq2\), determine the Killing fields, the global isometries and the complete Killing fields. Give a bounded affine field which is not Killing.

**Solution.** The flat first-data equation A.2 gives \(X(x)=Bx+b\) on any connected Euclidean open set: \(-DX\) is constant, and then \(X-Bx\) has zero derivative and is constant along coordinate paths. A.3 says exactly that \(B\) is skew for a Killing field. Thus the ball has the maximal \(n(n+1)/2\)-dimensional space of Killing fields.

A global isometry is smooth by B.2 and affine by Levi–Civita naturality. The vanishing Hessian equation makes it \(f(x)=Qx+b\), \(Q\in O(n)\). If \(f(B^n)=B^n\), take the supremum of the scalar product with any unit vector \(v\). The supremum on the ball is \(1\), while that on its image is
\[
\sup_{|x|<1}\langle v,Qx+b\rangle=1+\langle v,b\rangle.
\]
Thus \(\langle v,b\rangle=0\) for every unit \(v\), so \(b=0\). Every orthogonal map preserves the ball; its full isometry group is therefore \(O(n)\), of dimension \(n(n-1)/2\).

If a Killing field on the ball is complete, its global flow consists of these isometries and fixes zero; differentiating there gives \(b=0\). Conversely a field \(Bx\) with \(B\) skew has the complete rotational flow \(e^{tB}x\). Finally \(X(x)=x\) is infinitesimally affine and bounded by one in norm, but
\(\mathcal L_Xg=2g\), so it is not Killing. Its flow \(e^tx\), starting at any nonzero point, leaves the ball in finite positive time. This shows why completeness is necessary in F.3. The unrestricted affine fields \(Bx+b\) also have the maximal \(n+n^2\) dimension on this ball, although Theorem G.3 prevents its global affine group from having that dimension. □

**Exercise H.4 (A line times a round sphere).** For \(M=\mathbb R\times S_a^2\) with its product metric, compute both full transformation groups, both infinitesimal field spaces, bounded affine fields, dimensions and components.

**Solution.** The sphere is complete and simply connected by [Sectional curvature C.2](sectional-curvature-and-space-forms.md#theorem-c-2) and [Sectional curvature C.3](sectional-curvature-and-space-forms.md#lemma-c-3). Its holonomy is irreducible on its two-dimensional tangent space: [Sectional curvature C.1](sectional-curvature-and-space-forms.md#theorem-c-1) gives
\[
R(e_1,e_2)e_1=-a^{-2}e_2,\qquad
R(e_1,e_2)e_2=a^{-2}e_1
\]
for an orthonormal pair. This nonzero rotation generator belongs to the holonomy Lie algebra by [Curvature and holonomy G.3](curvature-and-holonomy-groups.md#theorem-g-3). Any holonomy-invariant real line would be invariant under that generator by differentiation, which the displayed formula forbids. Hence the product has exactly its line as Euclidean factor and exactly one non-Euclidean irreducible factor.

The distribution argument in F.2 applies even outside the identity component. With just one non-Euclidean factor, no permutation is possible, so every affine map is a product. Its sphere factor is an isometry by the irreducible part of F.2. Therefore
\[
\begin{aligned}
\operatorname{Aff}(M)&=\operatorname{Aff}(\mathbb R)\times O(3),\\
f(t,y)&=(\alpha t+\beta,Qy),
&&\alpha\ne0,\quad Q\in O(3),\\
\operatorname{Isom}(M)&=(\mathbb R\rtimes\{1,-1\})\times O(3),
\end{aligned}
\tag{H.3}
\]
where the isometry formula restricts \(\alpha\) to \(\pm1\).

Completeness and D.4 identify all infinitesimal affine fields with generators of the identity component. E.2 and E.3 give precisely
\[
X(t,y)=(ct+b,By),\qquad B^T=-B.
\tag{H.4}
\]
It is Killing exactly when \(c=0\), by the product Killing equation. Its squared norm is
\((ct+b)^2+|By|^2\).
The sphere term is bounded by \(a^2\|B\|^2\), so the field is bounded exactly when \(c=0\). Thus the bounded and Killing fields are \((b,By)\), and every \(c\ne0\) produces an unbounded non-Killing affine field. The affine group and affine field space have dimension \(2+3=5\); the isometry group and Killing space have dimension \(1+3=4\).

The two components of \(\operatorname{Aff}(\mathbb R)\) are distinguished by the sign of \(\alpha\), each connected in its coordinates \((\alpha,\beta)\). The two components of \(O(3)\) are distinguished by determinant: its positive component \(SO(3)\) is connected by the plane-rotation argument in G.1, and multiplication by a fixed reflection identifies the other component with it. Thus each full group in (H.3) has four components. This includes all orientation reversals on either factor. □

## Further reading

- Andreas Čap, *G-structures*, lecture notes, Fall Term 2021/22, §§1.2 and 3.10. [Author-hosted notes](https://www.mat.univie.ac.at/~cap/files/G-Struct.pdf).
- Vincent Pecastaing, *Lie groups and Riemannian symmetric spaces*, lecture notes, 28 July 2023, §§1.4 and 3.3. [Author-hosted notes](https://math.univ-cotedazur.fr/~pecastaing/symmetric_spaces.pdf).

Earlier programme proofs used here are linked at their points of use. In particular, the local flow and inverse theorems are in [Local tools 1.2](local-tools-for-bundles-and-transport.md#1-contraction-and-local-inversion) and 2.1, and the closed-subgroup theorem is in [Invariant connections A.1](invariant-connections-on-homogeneous-bundles.md#theorem-a-1).
