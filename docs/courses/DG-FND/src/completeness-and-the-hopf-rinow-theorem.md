# Completeness and the Hopf–Rinow theorem

This lesson proves the Riemannian completeness theorem, existence of prescribed developments and the covering consequences of complete affine maps. Explicit examples distinguish metric, geodesic and development completeness. The final part proves the length-space theorem, including all its compactness and endpoint prerequisites. Every used result is proved here or in an exact earlier programme lesson, using freely accessible construction material.

## A. Local facts that control an endpoint

Throughout these three parts, \(M\) is a nonempty finite-dimensional Hausdorff, second-countable smooth manifold without boundary, and \(g\) is a positive definite smooth metric. Its connection is its Levi-Civita connection. The notation \(d_g\) denotes the length distance: the infimum of the lengths of continuous piecewise \(C^1\) paths with the prescribed endpoints. We impose connectedness when speaking of a finite metric on all of \(M\). On separate components the arguments apply separately.

The earlier programme chapters used below are [Local tools](local-tools-for-bundles-and-transport.md), abbreviated **Local**; [Geodesics, normal coordinates and curvature](geodesics-normal-coordinates-and-curvature.md), abbreviated **Geo**; and [Riemannian connections and convex neighbourhoods](riemannian-connections-and-convex-neighbourhoods.md), abbreviated **Riem**. Riem A.1 proves metric compatibility and constant geodesic speed. Riem A.2 proves that length distance is a metric on each connected component and induces exactly its manifold topology. Geo A.1–A.2 give the maximal geodesic flow, its smooth dependence, and the rescaling identity \(\gamma_v(t)=\exp_p(tv)\), with equality of the two domains. These are complete programme proofs, not external prerequisites.

The free construction source for the completeness argument is Peter W. Michor's [author manuscript, *Topics in Differential Geometry*](https://www.mat.univie.ac.at/~michor/dgbook.pdf), §23.6, printed pp.294–296. The argument below includes its needed local ingredients and all metric completeness steps. The manuscript is credited for mathematical ideas; this edition uses new exposition and does not reproduce its figures or prose.

**Lemma A.1 (a uniform normal radius over a compact set).** For every compact \(K\subset M\), some \(\rho>0\) has the following property for every \(x\in K\):
\[
\exp_x:B_\rho(0)\subset T_xM\longrightarrow B_{d_g}(x,\rho)
\]
is a diffeomorphism. Its radial segments minimize among all paths in \(M\), and are the unique minimizing affine geodesics on the fixed parameter interval \([0,1]\).

**Proof.** The empty set requires nothing. At a point \(p\), Geo B.1 gives a diffeomorphism \(\Psi(x,v)=(x,\exp_xv)\) on an open neighbourhood \(O\) of \((p,0)\) in a tangent coordinate chart. Choose a coordinate neighbourhood \(N\) of \(p\), with compact closure inside that chart, and \(a>0\) such that
\[
\{(x,v):x\in\overline N,\ |v|_{\mathrm{coord}}\leq a\}\subset O.
\tag{A.1}
\]
One first takes a product of open balls about \((p,0)\) inside \(O\), then smaller closed balls, so this selection uses only openness and finite-dimensional compactness (Local 0.1).

There is a constant \(c>0\) with \(|v|_{g_x}\geq c|v|_{\mathrm{coord}}\) for \(x\in\overline N\). Indeed the continuous positive function \(g_x(u,u)\) on the product of \(\overline N\) and the coordinate unit sphere attains a positive minimum, by Local 0.1; take its square root and rescale \(u\). Choose \(0<\delta<ca\). For every \(x\in N\), the metric tangent ball \(B_\delta(0)\) lies in the corresponding fibre of \(O\). Since \(\Psi\) and its inverse preserve the first coordinate, their restrictions to that fibre give a diffeomorphism \(\exp_x:B_\delta(0)\to U_x\). Riem B.3 proves that \(U_x=B_{d_g}(x,\delta)\) and supplies global minimality and its uniqueness assertion.

The sets \(N\), constructed at all points of \(K\), cover \(K\). Choose finitely many and let \(\rho\) be the minimum of their positive radii \(\delta\). Restricting each diffeomorphism to the smaller tangent ball and applying Riem B.3 again proves the assertion with this common radius. In dimension zero every sufficiently small neighbourhood is a singleton; the same conclusion is immediate. □

**Lemma A.2 (a convergent finite endpoint extends a geodesic).** Suppose that \(\gamma:[a,b)\to M\) is an affine geodesic, \(b<\infty\), and \(\gamma(t)\to q\in M\) as \(t\uparrow b\). Then \(\gamma\) extends as an affine geodesic past \(b\).

**Proof.** If its constant speed is zero, Riem A.1 and positivity make it constant, so extension is immediate. Let its speed be \(s>0\). Choose a coordinate neighbourhood of \(q\) and a smaller neighbourhood with compact closure \(K\) inside that chart. The curve lies in this smaller neighbourhood for all sufficiently large \(t<b\). The compactness argument for the norm bound in A.1 gives \(c>0\) such that
\[
|\dot\gamma(t)|_{\mathrm{coord}}\leq s/c
\]
on this tail. Choose any sequence \(t_j\uparrow b\) in the tail. The coordinate velocities have a convergent subsequence, by Local 0.1; along it the tangent data \((\gamma(t_j),\dot\gamma(t_j))\) converge to some \((q,w)\in TM\).

Geo A.1 gives an open geodesic-flow domain containing \((0,(q,w))\). Therefore there are \(\epsilon>0\) and a neighbourhood \(U\) of \((q,w)\) such that the flow from every initial datum in \(U\) exists for times in \((-\epsilon,\epsilon)\). For sufficiently large \(j\), its datum lies in \(U\) and \(b-t_j<\epsilon/2\). The solution restarted there exists until \(t_j+\epsilon>b\). By uniqueness in Geo A.1 it agrees with the original geodesic on their common time interval, and consequently extends it. This argument needs a convergent subsequence of velocities; it does not assume in advance that the velocity has an endpoint limit. □

**Lemma A.3 (a shortest broken geodesic has no corner).** Let \(\eta:[0,L]\to M\) be a continuous concatenation of finitely many unit-speed affine geodesic segments, with \(L>0\). If \(d_g(\eta(0),\eta(L))=L\), then the whole curve is one smooth unit-speed affine geodesic.

**Proof.** Every subpath from \(u\) to \(v\) is minimizing. If its endpoint distance were smaller than \(v-u\), the definition of an infimum would supply a piecewise \(C^1\) competitor of length less than \(v-u\). Replacing that subpath would give a path between the original endpoints of length less than \(L\), a contradiction.

At a joining time \(t_0\), take a strongly convex neighbourhood \(V\) of \(\eta(t_0)\) supplied by Riem B.5. Continuity allows \(u<t_0<v\) with \(\eta([u,v])\subset V\), and with no other joining time in this interval. The equality assertion of Riem B.5 says that this minimizing piecewise smooth path follows the unique radial segment from \(\eta(u)\) to \(\eta(v)\) monotonically. Every initial subpath has length \(t-u\) and realizes its endpoint distance, by the preceding paragraph. The radial distance parameter in that equality assertion is therefore exactly \(t-u\). Thus \(\eta|_{[u,v]}\) is the unit-speed parametrization of the smooth joining geodesic. Its two one-sided velocities agree and it satisfies the geodesic equation across \(t_0\). Repeat at the finitely many joining times; uniqueness of the geodesic initial-value problem (Geo A.1) then identifies all segments as restrictions of one geodesic. □

## B. From one exponential map to global completeness

**Theorem B.1 (one point controls distance and compactness).** Let \(M\) be connected. Suppose some \(p\in M\) has \(\exp_p\) defined on all of \(T_pM\). Then every \(q\in M\) can be joined to \(p\) by a minimizing affine geodesic. For every \(R\geq0\),
\[
\overline B_{d_g}(p,R)=\exp_p\{v\in T_pM:|v|_{g_p}\leq R\}.
\tag{B.1}
\]
These closed balls are compact. Every closed bounded subset of \(M\) is compact.

**Proof.** For \(q=p\), use the constant geodesic. Otherwise set \(r=d_g(p,q)>0\). Choose \(0<\delta<r\) so that \(\exp_p\) is a diffeomorphism on \(B_{2\delta}(0)\). Geo B.1 allows this. By Riem B.3 the metric sphere of radius \(\delta\) about \(p\) is exactly
\[
S=\{\exp_p(\delta u):|u|_{g_p}=1\}.
\]
It is nonempty and compact, by Local 0.1. The function \(z\mapsto d_g(z,q)\) is continuous: the triangle inequality bounds the difference of two of its values by their distance. Hence it attains a minimum \(m\) on \(S\). Every path \(\eta:[a,b]\to M\) from \(p\) to \(q\) hits \(S\). To check the real-order step, let \(f(t)=d_g(p,\eta(t))\), and let \(t_*=\sup\{t\in[a,b]:f(t)\leq\delta\}\), using the real supremum property in Local 0.0. Since \(f(a)=0<\delta<f(b)\), continuity makes \(a<t_*<b\); values in that set approach \(t_*\), so \(f(t_*)\leq\delta\). A strict inequality would, by continuity, put larger times in the set. Hence \(f(t_*)=\delta\). The length of \(\eta\) is consequently at least \(\delta+m\). Conversely the triangle inequality at a minimizer of \(m\) gives \(r\leq\delta+m\). Taking infima of path lengths proves
\[
r=\delta+m.
\tag{B.2}
\]
Choose a unit \(u\) for which \(z=\exp_p(\delta u)\) attains \(m\). The curve \(c(t)=\exp_p(tu)\) exists for every real \(t\) and is a unit-speed geodesic, by Geo A.2 and Riem A.1.

Consider the closed subset
\[
E=\{t\in[\delta,r]:d_g(c(t),q)=r-t\}.
\]
It is nonempty by (B.2). If \(t\in E\) and \(0\leq s\leq t\), then
\[
\begin{aligned}
d_g(c(s),q)&\leq d_g(c(s),c(t))+d_g(c(t),q)\leq (t-s)+(r-t)=r-s,\\
d_g(c(s),q)&\geq r-d_g(p,c(s))\geq r-s.
\end{aligned}
\tag{B.3}
\]
Here a geodesic segment gives an upper bound on distance even before its minimality has been proved. Thus equality holds for every such \(s\). Let \(t_0=\max E\), which exists by compactness (Local 0.1). Suppose \(t_0<r\), and put \(x=c(t_0)\). Choose \(0<\epsilon<r-t_0\) so that the metric sphere of radius \(\epsilon\) about \(x\) is a compact normal sphere. Repeating the path-crossing and minimum argument of (B.2), now at \(x\), gives a point \(z'\) on that sphere such that
\[
d_g(z',q)=r-t_0-\epsilon.
\tag{B.4}
\]
The segment of \(c\) up to \(x\), followed by the radial unit-speed segment from \(x\) to \(z'\), has length \(t_0+\epsilon\). The opposite distance bound follows from the triangle inequality and (B.4):
\[
d_g(p,z')\geq r-d_g(z',q)=t_0+\epsilon.
\tag{B.5}
\]
Consequently this broken geodesic is minimizing. Lemma A.3 removes its corner, and uniqueness of geodesics identifies its second piece with \(c\). Thus \(z'=c(t_0+\epsilon)\); equation (B.4) says \(t_0+\epsilon\in E\), contradicting maximality. Hence \(t_0=r\), and (B.3) gives \(d_g(c(r),q)=0\). Therefore \(c(r)=q\), and its segment of length \(r\) is minimizing.

For \(|v|\leq R\), the radial curve to \(\exp_pv\) has length \(|v|\), proving one inclusion in (B.1). Conversely the minimizing segment just proved expresses any point at distance at most \(R\) as \(\exp_p(ru)\) with \(r\leq R\); the case \(r=0\) uses \(v=0\). This proves (B.1). Its right side is a continuous image of a finite-dimensional closed bounded ball, hence compact by Local 0.1 and smoothness of \(\exp_p\).

Finally, let \(A\) be a nonempty closed bounded subset of \(M\), choose \(a\in A\), and take a finite bound \(D\) for \(d_g(a,z)\) over \(z\in A\). Then \(A\subset\overline B_{d_g}(p,d_g(p,a)+D)\). It is a closed subset of that compact ball, hence compact by Local 0.1. The empty set is compact as well. □

**Theorem B.2 (Hopf–Rinow).** On a nonempty connected Riemannian manifold the following statements are equivalent:

1. Every Cauchy sequence for \(d_g\) converges in \(M\).
2. Every maximal affine geodesic has domain \(\mathbb R\).
3. For some \(p\in M\), \(\exp_p\) is defined on all of \(T_pM\).
4. Every closed bounded subset of \((M,d_g)\) is compact.

When they hold, every exponential map has full domain, and any two points are joined by a minimizing affine geodesic.

**Proof.** Assume (1). Let \(\gamma:(a,b)\to M\) be a maximal geodesic and suppose \(b<\infty\). Its constant speed \(s\geq0\) gives
\[
d_g(\gamma(t),\gamma(u))\leq s|t-u|\qquad(a<t,u<b).
\tag{B.6}
\]
For a sequence \(t_j\uparrow b\), (B.6) makes \(\gamma(t_j)\) Cauchy, so it converges to some \(q\in M\). In fact the whole curve tends to \(q\): given \(\varepsilon>0\), take \(j\) such that \(d_g(\gamma(t_j),q)<\varepsilon/2\) and \(s(b-t_j)<\varepsilon/2\), with the latter condition automatic if \(s=0\). For \(t_j\leq t<b\), (B.6) and the triangle inequality give \(d_g(\gamma(t),q)<\varepsilon\). Riem A.2 converts this to convergence in the manifold topology. Lemma A.2 extends \(\gamma\) past \(b\), contradicting maximality. Applying the same argument to the reversed geodesic rules out finite \(a\). This proves (2).

Geo A.2 proves that (2) makes \(\exp\) defined on all of \(TM\), so (3) follows. Theorem B.1 proves (3) implies (4).

Assume (4) and let \((x_j)\) be a Cauchy sequence. Its distances from \(x_1\) are bounded: the tail lies within distance one of one fixed tail term, and only finitely many earlier terms remain. A closed ball containing the sequence is therefore compact. Local 0.1 supplies a subsequence \(x_{j_k}\to x\). Given \(\varepsilon>0\), choose \(N\) so that \(d_g(x_i,x_j)<\varepsilon/2\) for \(i,j\geq N\), and then choose \(k\) with \(j_k\geq N\) and \(d_g(x_{j_k},x)<\varepsilon/2\). For every \(i\geq N\), the triangle inequality gives \(d_g(x_i,x)<\varepsilon\). Thus the whole sequence converges and (1) holds.

Under these equivalent conditions, every point has a full exponential domain by (2) and Geo A.2. Applying B.1 with either endpoint as its base gives the last assertion. A connected zero-dimensional nonempty manifold is a point, and all assertions then hold directly. □

**Corollary B.3 (compact and homogeneous manifolds).** A compact Riemannian manifold is geodesically complete, and each of its connected components is metrically complete. The same conclusions hold for a Riemannian manifold whose isometries act transitively.

**Proof.** In the compact case, A.1 gives one radius \(\rho>0\) valid at every point. A geodesic with initial speed \(s>0\) at any point exists for at least \(|t|<\rho/s\), because \(t\dot\gamma(0)\) stays in its exponential domain and Geo A.2 identifies the domains. For a geodesic of speed \(s\) with a hypothetical finite maximal endpoint \(b\), restart it at a time \(t_0<b\) with \(b-t_0<\rho/(2s)\). This solution exists past \(b\); uniqueness identifies it with the old one on their common interval, a contradiction. The reverse-time argument handles the left endpoint. Zero-speed geodesics are constant for all time.

In the transitive case, fix \(p\) and a normal radius \(\rho>0\) there (Geo B.1). At any \(x\), choose an isometry taking \(p\) to \(x\). Riem A.3 proves that it preserves velocities' norms and takes parametrized geodesics to parametrized geodesics. Therefore the same lifetime bound \(\rho/s\) holds at \(x\). The preceding restart argument proves completeness again. No compactness or Lie-group structure of the collection of isometries is required.

Finally a geodesic stays in its connected component. An interval is connected: a separation into two nonempty relatively open sets would give a continuous function equal to zero on one and one on the other, contradicting Local 0.0's intermediate-value assertion. A continuous image of a connected space is connected, since a separation of the image would pull back to a separation of the domain. These facts apply both to the original curve and its complete extension. Components are themselves open manifolds: a coordinate ball is path connected by straight segments, hence connected by the same interval argument, so each point has an open neighbourhood contained in its component. Theorem B.2 on each component now gives metric completeness. □

## C. Three ways to test completeness

These exercises apply the proved metric criterion and elementary programme calculus. A proper map means a continuous map whose inverse image of every compact set is compact. A metric inequality such as \(g\geq c^2h\) means \(g_p(v,v)\geq c^2h_p(v,v)\) for every point and tangent vector.

**Exercise C.1 (one lower metric bound suffices).** Suppose \(g,h\) are smooth Riemannian metrics on a connected manifold, \(c>0\) is constant, \(g\geq c^2h\), and \(h\) is complete. Prove that \(g\) is complete, and explain whether a constant upper bound for \(g\) by \(h\) is needed.

**Solution.** Along every piecewise \(C^1\) path, the pointwise norm inequality integrates to \(L_g\geq cL_h\); taking infima gives
\[
d_g(p,q)\geq c\,d_h(p,q).
\tag{C.1}
\]
Thus a \(d_g\)-Cauchy sequence is \(d_h\)-Cauchy and converges to some \(p\) in \(d_h\). Both distance topologies are the manifold topology by Riem A.2, so the same sequence converges to \(p\) in \(d_g\). Theorem B.2 also gives geodesic completeness.

No global upper bound is needed. For example, on \(\mathbb R\) take \(h=dx^2\) and \(g=(1+x^2)dx^2\). The Euclidean distance is \(|x-y|\): every path has length at least its endpoint displacement by the integral triangle inequality (Local 0.0–0.3), and the straight segment attains it. Hence \(h\) is complete by Local 0.1. We have \(g\geq h\), whereas the ratio \(1+x^2\) is unbounded. The argument just given proves \(g\) complete. □

**Exercise C.2 (a proper function prevents escape).** Let \(h\) be any Riemannian metric on a connected manifold and let \(\rho:M\to[0,\infty)\) be a smooth proper function. Show that
\[
g=(1+|d\rho|_h^2)h
\tag{C.2}
\]
is complete. Here the norm of a covector is its dual norm for \(h\).

**Solution.** The dual metric is smooth, by the inverse-matrix construction in Riem F.1, so (C.2) is a positive definite smooth metric. Put \(w=(d\rho)^\sharp\), using that same programme theorem. The quadratic argument of Local 0.0 applies to \(h\): if \(v\ne0\), substitute \(t=h(w,v)/h(v,v)\) into \(0\leq h(w-tv,w-tv)\) to obtain \(|h(w,v)|^2\leq h(w,w)h(v,v)\); the case \(v=0\) is immediate. Since \(d\rho(v)=h(w,v)\) and \(|w|_h=|d\rho|_h\), this gives
\[
|d\rho(v)|\leq |d\rho|_h\,|v|_h\leq |v|_g.
\tag{C.3}
\]
Integrating the derivative of \(\rho\) on each smooth part of a path and summing at its finitely many joining points (Local 0.3) yields
\[
|\rho(p)-\rho(q)|\leq L_g(\eta).
\]
Taking the infimum over paths proves \(|\rho(p)-\rho(q)|\leq d_g(p,q)\).

Let \((p_j)\) be \(d_g\)-Cauchy. Its distances from \(p_1\) are bounded by the Cauchy argument in B.2. The last inequality therefore bounds all \(\rho(p_j)\) by some finite \(R\). Every term lies in \(\rho^{-1}([0,R])\), which is compact by properness and Local 0.1. Riem A.2 makes it a compact metric subspace for \(d_g\); Local 0.1 supplies a convergent subsequence. The final Cauchy-subsequence argument in B.2 gives convergence of the whole sequence in \(d_g\). Thus \(g\) is complete. This proof assumes the specified proper function; it does not use an unproved existence theorem for such functions. □

**Exercise C.3 (a finite-distance end on the line).** For \(g=e^{2x}dx^2\) on \(\mathbb R\), determine the distance and all maximal affine geodesics, and decide completeness.

**Solution.** The exponential and logarithm, including their domains and derivatives, were constructed in Geo A.4. The diffeomorphism \(F(x)=e^x\) takes \(\mathbb R\) onto \((0,\infty)\) and pulls \(dy^2\) back to \(g\). Riem A.3 proves preservation of path lengths and distance by such a global isometry. On the interval \((0,\infty)\), length is at least endpoint displacement and a straight segment stays in the interval and attains it, by the same calculus argument as in C.1. Hence
\[
d_g(x_0,x_1)=|e^{x_0}-e^{x_1}|.
\tag{C.4}
\]
The Euclidean connection in the coordinate \(y\) has coefficient zero by Riem A.1's formula, so its affine geodesic equation is \(y''=0\). Local 0.3 gives \(y(t)=a+bt\). Every geodesic whose domain contains zero is therefore
\[
x(t)=\log(a+bt),\qquad a>0,\quad b\in\mathbb R,\qquad
I=\{t\in\mathbb R:a+bt>0\}.
\tag{C.5}
\]
Conversely every curve in (C.5) is geodesic by Riem A.3. This interval is maximal. At a finite endpoint, \(a+bt\to0\); an extension in \(\mathbb R\) would give a finite value \(x_*\) there and hence a positive limit \(e^{x_*}\), a contradiction. If \(b=0\), the constant solution has domain all of \(\mathbb R\). If \(b>0\), \(I=(-a/b,\infty)\); if \(b<0\), \(I=(-\infty,-a/b)\). Initial data \(x(0)=x_0,\ \dot x(0)=v\) give \(a=e^{x_0}\) and \(b=e^{x_0}v\), so the list covers every initial vector.

Finally \(x_j=-j\) is Cauchy for (C.4), because \(e^{-j}\to0\) (Geo A.4). It cannot converge to a point \(x_*\in\mathbb R\), since (C.4) would force \(e^{x_*}=0\). Thus the metric is incomplete, in agreement with the finite geodesic endpoints in (C.5). □

## D. Prescribing a development

For a path \(\gamma:[0,a]\to M\), parallel transport from time \(s\) to time \(t\) is denoted \(T_{st}\). Its **development in the initial tangent space** is
\[
\delta_\gamma(t)=\int_0^t T_{r0}\dot\gamma(r)\,dr\in T_{\gamma(0)}M.
\tag{D.1}
\]
The full construction is [Linear F.1 and G.1](linear-and-affine-connections.md); [Curvature C.2](curvature-and-holonomy-groups.md) proves its transport prerequisites for finitely piecewise \(C^1\) paths. Here and below a piecewise \(C^1\) path has a finite subdivision, with a \(C^1\) extension to the endpoints of each piece. No derivative matching is required at a joining time. Inverting (D.1) is a nonlinear existence problem, since the transport itself depends on the unknown path.

**Lemma D.1 (continuous time coefficients and compact continuation).** Let \(F(t,z)\) be a vector field in local coordinates, continuous in \(t,z\), with spatial derivative \(D_zF\) also continuous. Then the initial-value problem \(z'=F(t,z)\) has unique local \(C^1\) solutions. If a solution's time-position graph stays in a compact subset of the domain as it approaches a finite endpoint, it extends across that endpoint. These assertions hold on a smooth manifold and for finite concatenations of such time pieces.

**Proof.** Around \((t_0,z_0)\) take a closed time interval and closed spatial ball inside the domain. Local 0.1 bounds \(|F|\) and \(\|D_zF\|\) there by \(B,L\). On a smaller ball of initial values and a sufficiently short interval \([-\epsilon,\epsilon]\), the operator
\[
(\mathcal T u)(s)=z_*+\int_0^s F(t_*+\tau,u(\tau))\,d\tau
\tag{D.2}
\]
maps a closed supremum-norm ball of continuous curves into itself: choose \(\epsilon B\) smaller than the available spatial margin. The spatial segment formula of Local 0.3 gives
\[
\|\mathcal T u-\mathcal T v\|_\infty
 \leq\epsilon L\|u-v\|_\infty.
\tag{D.3}
\]
Choose also \(\epsilon L<1\). The curve space is complete by Local 0.2; the contraction theorem, Local 1.1, therefore supplies a unique fixed point. The fundamental theorem of calculus in Local 0.3 makes it \(C^1\) and gives the differential equation. This proof never differentiates \(F\) in time.

Any two solutions through the same datum stay in one such rectangle on a sufficiently small interval. Equation (D.3) applied to their integral equations proves that they agree there. Agreement then propagates along their common time interval: if it had a first boundary before a specified later time, continuity gives agreement at that boundary and local uniqueness extends agreement past it. Reversing time gives the same conclusion to the left.

The choices of margin, \(B,L,\epsilon\) above work for all initial data in a smaller time-position rectangle. Finitely many such smaller rectangles cover any compact graph set. The minimum of their finitely many positive existence times is positive. Restarting sufficiently near a finite endpoint gives a solution across that endpoint; uniqueness identifies it with the old solution on the overlap. Coordinate changes preserve the equation by Local 0.3's chain rule, and uniqueness glues the coordinate solutions on a manifold. At a specified endpoint of a closed time piece one may first extend its continuous coefficient constantly in time in the formula \(F(t,z)\); this retains the stated spatial regularity. Finally solve successive pieces with the last endpoint value as the next initial value. Finite concatenation gives the piecewise assertion. □

**Lemma D.2 (compact orthonormal frames over a compact base set).** If \(K\subset M\) is compact, the set of all \(g\)-orthonormal frames based at points of \(K\) is compact in \(\operatorname{Fr}(TM)\).

**Proof.** Riem F.2 constructs smooth orthonormal-frame trivializations with fibre
\[
\mathrm O(n)=\{Q\in\mathbb R^{n\times n}:Q^TQ=I\}.
\tag{D.4}
\]
This set is closed because its defining equations are continuous. Every column has Euclidean norm one, so its entries are bounded. Local 0.1 proves it compact. Every matrix in this set is invertible, with inverse \(Q^T\), so (D.4) is also exactly the orthogonal group used in the bundle construction.

Choose, near each point of \(K\), a smaller coordinate neighbourhood whose compact closure is contained in one such trivializing chart. Finitely many smaller neighbourhoods cover \(K\). Their closures intersected with \(K\) give compact sets \(K_1,\ldots,K_m\), each inside its chart, covering \(K\). In that chart the frames over \(K_i\) are the continuous image of \(K_i\times\mathrm O(n)\). The product is compact: its coordinate image is a closed bounded subset of a finite-dimensional Euclidean space, by Local 0.1. Thus the frames over each \(K_i\) are compact, and their finite union is compact by the same lemma. For \(n=0\) the fibre is a singleton, with the same conclusion. □

**Theorem D.3 (complete metrics and prescribed developments).** On a connected complete Riemannian manifold, every finitely piecewise \(C^1\) curve \(\delta:[0,a]\to T_pM\) with \(\delta(0)=0\) is the development of a unique finitely piecewise \(C^1\) curve starting at \(p\), on that entire interval. Conversely, if every such curve can be realized at one fixed point \(p\), then the manifold is complete.

**Proof.** The case \(a=0\) is immediate. Choose an orthonormal frame \(u_0:\mathbb R^n\to T_pM\) and put \(v(t)=u_0^{-1}\dot\delta(t)\) on each \(C^1\) piece. Let \(B(v)\) denote the standard horizontal vector field on the frame bundle from Linear H.2. Its two defining identities are
\[
\omega(B(v))=0,\qquad d\pi(B(v)_u)=uv.
\tag{D.5}
\]
Riem F.2 proves that the connection restricts to the orthonormal frame bundle \(P_{\mathrm O}\), so these fields are tangent to it. Seek a curve \(U\) there solving
\[
\dot U(t)=B(v(t))_{U(t)},\qquad U(0)=u_0.
\tag{D.6}
\]
The field is smooth in the frame and linear in \(v\), by Linear H.2. Since \(v\) is continuous on each closed time piece, D.1 gives unique local solutions.

For any such solution, put \(\gamma=\pi U\). Equations (D.5) give \(\dot\gamma=Uv\). Orthonormality therefore implies
\[
|\dot\gamma(t)|_g=|v(t)|=|\dot\delta(t)|_{g_p}.
\tag{D.7}
\]
The total integral \(L=\int_0^a|v(t)|\,dt\) is finite by Local 0.1 and 0.3 on the finitely many pieces. Before any prospective endpoint, the curve stays in the closed metric ball \(\overline B(p,L)\), because its traveled length bounds its distance from \(p\). This ball is compact by B.1–B.2. Lemma D.2 makes all orthonormal frames over it compact. The time-position graph of (D.6) thus stays in a compact set, and D.1 extends the solution to the end of each time piece. Solving and joining finitely many pieces yields \(U\) on \([0,a]\).

Horizontality and the uniqueness of transport (Linear A.2 and Curvature C.2) give \(U(t)=T_{0t}u_0\). Consequently
\[
T_{t0}\dot\gamma(t)=T_{t0}U(t)v(t)
 =u_0v(t)=\dot\delta(t).
\tag{D.8}
\]
Integrating on the pieces, using continuity at their endpoints and the common initial value zero, proves \(\delta_\gamma=\delta\). If another curve has this same development, transport its initial frame \(u_0\) along that curve. Its frame then satisfies exactly (D.6), by (D.8) and the horizontal coframe isomorphism of Linear H.2. D.1 proves equality of the two frame curves and hence of their base curves. This also makes the resulting base curve independent of the auxiliary choice of \(u_0\).

For the converse, realize \(\delta(t)=tw\) on \([0,1]\) for every \(w\in T_pM\). In (D.6) its frame coefficient is constant. Geo G.1 proves that the projection of this horizontal-field integral curve is the geodesic with initial velocity \(w\). Alternatively the smooth constant field makes the frame curve smooth by Local 2.1, and (D.8) makes its velocity parallel. Thus every \(w\) lies in the exponential domain at \(p\). Theorem B.1 followed by B.2 proves completeness.

The forward proof used only metric compatibility of the connection, in addition to completeness of the metric. It therefore also proves existence of all these developments for any metric-compatible connection on a complete Riemannian manifold. The converse in this theorem uses the Levi-Civita connection through B.1; it is not asserted here for an arbitrary connection with torsion. □

## E. Complete maps and their sheets

In E.1–E.3 the manifolds carry arbitrary smooth linear connections, which may have torsion; no metric is required. They are nonempty, connected and without boundary. A smooth local diffeomorphism \(F:N\to M\) is **affine** if, wherever it is a diffeomorphism on an open set, it intertwines the two covariant derivatives:
\[
F_*(\nabla^N_XY)=\nabla^M_{F_*X}(F_*Y).
\tag{E.1}
\]
A smooth covering means a surjective smooth map for which every point has an open neighbourhood \(V\) whose inverse image is a disjoint union of open sets, each mapped diffeomorphically onto \(V\). We prove all needed lifting statements below. The construction uses the complete programme proofs of arbitrary-connection normal coordinates (Geo B.1), affine parameter rescaling (Geo A.2), and the covariant chain rule (Linear B.2).

**Lemma E.1 (geodesic naturality and finite polygon reachability).** An affine local diffeomorphism preserves parametrized geodesics. Any two points of a connected manifold with a smooth linear connection can be joined by a finite concatenation of affine geodesic segments.

**Proof.** In a neighbourhood on which \(F\) is a diffeomorphism, apply the curve form of the chain rule in Linear B.2 to (E.1):
\[
D_t^M(dF\,\dot\eta)=dF(D_t^N\dot\eta).
\tag{E.2}
\]
One can check this directly by writing the velocity in a local frame: the coefficient derivative transforms by the ordinary chain rule, and the connection term transforms by (E.1). Thus a zero covariant acceleration stays zero. The identity is local at each time, so it holds along a whole geodesic even when different local inverse charts are needed.

Say two points are related when a finite geodesic polygon joins them. Constant segments give reflexivity, reversing an affine parameter gives symmetry by Geo A.2, and concatenation gives transitivity. Every equivalence class is open: at any of its points \(x\), Geo B.1 provides a normal neighbourhood in which each point is reached by a radial geodesic from \(x\), on \([0,1]\). The complement of a class is the union of the other open classes and is open. Connectedness forces a single class. □

**Theorem E.2 (a complete affine source gives a covering).** Suppose \(N\) is geodesically complete and \(F:N\to M\) is an affine local diffeomorphism. Then \(F\) is a surjective smooth covering and \(M\) is geodesically complete.

**Proof.** Start at any \(n_0\in N\). By E.1, a point \(y\in M\) can be reached from \(F(n_0)\) by a finite geodesic polygon. Lift its first segment by taking the initial velocity through the inverse of \(dF_{n_0}\), and taking the complete geodesic of \(N\) with that initial vector. By E.1 and uniqueness in Geo A.1 its projection is the prescribed segment. Repeat at the successive lifted endpoints. There are finitely many segments, so this reaches a preimage of \(y\) and proves surjectivity.

Given any \(w\in T_yM\), choose \(n\in F^{-1}(y)\) and the complete geodesic in \(N\) with initial velocity \((dF_n)^{-1}w\). Its projection is a geodesic on all of \(\mathbb R\) with initial data \(y,w\), by E.1. The maximal-solution uniqueness of Geo A.1 proves completeness of \(M\).

It remains to construct the covering sheets; surjectivity and a local inverse alone do not suffice. Fix \(y\) and choose a normal neighbourhood
\[
\exp_y:B_\epsilon(0)\subset T_yM\longrightarrow V
\]
as in Geo B.1, where the ball is for any chosen linear-coordinate norm. Write \(\ell(q)=(\exp_y|_{B_\epsilon})^{-1}(q)\). For each \(n\in F^{-1}(y)\), define
\[
s_n(q)=\exp_n\bigl((dF_n)^{-1}\ell(q)\bigr),\qquad q\in V.
\tag{E.3}
\]
It is defined and smooth everywhere on \(V\), by completeness of \(N\) and Geo A.2. Naturality and uniqueness of the geodesic initial-value problem give
\[
F(s_n(q))=q.
\tag{E.4}
\]
Differentiating (E.4) shows \(ds_n=(dF_{s_n(q)})^{-1}\); hence the inverse-function theorem (Local 1.2) makes \(s_n\) a local diffeomorphism. Equation (E.4) also makes it injective. Its image \(V_n=s_n(V)\) is open, since a local diffeomorphism takes open sets to open sets, and \(F|_{V_n}\) is a diffeomorphism onto \(V\) with inverse \(s_n\).

These images are disjoint. If \(s_n(q)=s_{n'}(q)=z\), the radial geodesics from \(n\) and \(n'\) used in (E.3) have the same projection
\[
\alpha(t)=\exp_y(t\ell(q)),\qquad 0\leq t\leq1.
\]
At their common endpoint \(z\), both velocities must equal \((dF_z)^{-1}\dot\alpha(1)\). Uniqueness in Geo A.1, backwards from time one, makes these geodesics identical, so \(n=n'\).

Finally take any \(z\in F^{-1}(V)\) and put \(q=F(z)\). Lift the reversed radial geodesic \(t\mapsto\alpha(1-t)\) starting at \(z\), using its initial velocity and completeness of \(N\). Its endpoint \(n\) lies over \(y\). Reverse the lift again. Its initial velocity at \(n\) is \((dF_n)^{-1}\ell(q)\), because it projects to \(\alpha\) and \(\dot\alpha(0)=\ell(q)\), by Geo B.1. Uniqueness identifies it with the curve in (E.3), so \(z=s_n(q)\). We have proved
\[
F^{-1}(V)=\coprod_{n\in F^{-1}(y)}V_n,
\]
with the required smooth sheet maps. □

**Theorem E.3 (a complete affine target lifts through a covering).** If \(F:N\to M\) is an affine smooth covering and \(M\) is geodesically complete, then \(N\) is geodesically complete.

**Proof.** First we prove the path-lifting fact used here. Let \(\alpha:[a,b]\to M\) be a continuous path and prescribe a preimage of \(\alpha(a)\). The inverse images in \([a,b]\) of evenly covered neighbourhoods give an open cover of the compact interval. There is \(\delta>0\) such that each relative ball of radius \(\delta\) in the interval lies in one member of this cover. Otherwise choose \(t_j\) whose relative radius-\(1/j\) ball lies in none. Local 0.1 gives a subsequence tending to \(t\). A member containing \(t\) contains a relative interval of some positive radius \(r\) about it. For large subsequence indices, \(|t_j-t|+1/j<r\), contradicting the choice. Subdivide \([a,b]\) into finitely many closed intervals of length less than \(\delta\). On the first interval choose the covering sheet containing the prescribed initial point and compose \(\alpha\) with its inverse sheet map. At each subsequent interval choose the sheet containing the endpoint already obtained. This gives a continuous lift on the whole interval.

The lift is unique. Two lifts agreeing at a time agree nearby, since both remain in the same inverse chart there. Their agreement set is closed, by continuity and the Hausdorff property of \(N\), and the preceding observation makes it open. The interval is connected as proved in B.3, so lifts with one common value agree on the whole interval. If \(\alpha\) is smooth, the lift is smooth even at subdivision points: near each point it is expressed by one smooth local inverse of \(F\), by continuity and the local uniqueness just proved.

Now take any tangent vector \(v\in T_nN\). The geodesic \(\alpha:\mathbb R\to M\) with initial vector \(dF_nv\) exists by completeness. For each \(T>0\), lift its restrictions to \([0,T]\) and, reversing time, to \([-T,0]\), with value \(n\) at zero. Uniqueness makes all these lifts agree on overlaps; their union is a smooth curve on \(\mathbb R\). Equation (E.2) and invertibility of \(dF\) show that its covariant acceleration is zero. Its initial velocity is \(v\). Geo A.1 identifies it with the maximal geodesic of those data, proving that its maximal interval is \(\mathbb R\). □

**Corollary E.4 (local isometries and compact immersions).** For a local isometry \(F:(N,h)\to(M,g)\) between nonempty connected Riemannian manifolds:

1. Completeness of \(N\) implies completeness of \(M\), and \(F\) is a surjective smooth covering.
2. If \(F\) is a covering and \(M\) is complete, then \(N\) is complete.

Moreover, every smooth immersion from a nonempty connected compact manifold into a connected manifold of the same dimension is a smooth covering onto that manifold, and the target is compact.

**Proof.** Riem A.3 proves that a local isometry is an affine local diffeomorphism for the two Levi-Civita connections. Theorem B.2 converts metric completeness into geodesic completeness and back. Thus E.2 proves the first assertion and E.3 the second.

For the immersion, choose a Riemannian metric \(g\) on the target using the complete existence proof in Riem F.1. Its pullback \(h=F^*g\) is positive definite because \(dF\) is injective. It is smooth by the coordinate pullback formula. Equal dimensions make \(dF\) invertible, and Local 1.2 makes \(F\) a local isometry for \(h,g\). The source is complete by compactness and B.3. The first assertion makes \(F\) a surjective covering. Its image, the entire target, is a continuous image of a compact space and therefore compact by Local 0.1. □

**Corollary E.5 (an isometry orbit containing an open set).** Suppose a group acts by isometries on a connected Riemannian manifold \(M\). If one orbit contains a nonempty open subset of \(M\), then that orbit is all of \(M\).

**Proof.** Let \(O\) be the orbit and \(U\subset O\) a nonempty open subset. For any \(x\in O\), choose a point \(u\in U\) and a group element taking \(u\) to \(x\). The image of \(U\) is open, contains \(x\), and is contained in \(O\). Thus \(O\) is open in \(M\), and is a Riemannian manifold with the restricted metric. The group restricts to transitive isometries of \(O\). Corollary B.3 proves that every connected component \(O_0\) is complete. A component is open by the coordinate-ball argument in B.3. The inclusion \(O_0\hookrightarrow M\) is therefore a local isometry between connected manifolds. Corollary E.4 makes it surjective, so \(O_0=M\) and \(O=M\). No prior closedness or connectedness of the orbit, and no Lie-group structure of the acting group, was assumed. □

**Theorem E.6 (intrinsic completeness from closed local pieces).** Let \(M\) be a complete Riemannian manifold and \(N\subset M\) an embedded submanifold with its induced metric. Suppose every \(p\in M\) has an open neighbourhood \(U\) such that each connected component of \(N\cap U\) is closed in \(U\). Then every connected component of \(N\) is complete for its intrinsic distance. In particular this conclusion holds when \(N\) is closed in \(M\).

**Proof.** Work in one component \(C\) of \(N\), with intrinsic length distance \(d_C\). The image of any path in \(C\) is an ambient path of the same length, because the metric is induced. Taking infima gives
\[
d_M(x,y)\leq d_C(x,y)\qquad(x,y\in C).
\tag{E.5}
\]
An intrinsic Cauchy sequence \((x_j)\) is therefore ambient Cauchy. It stays in one ambient component; completeness there gives a limit \(p\). Choose \(U\) at \(p\) as in the hypothesis and \(r>0\) with \(B_{d_M}(p,3r)\subset U\), using Riem A.2. Take a tail with \(d_M(p,x_j)<r\) and \(d_C(x_j,x_k)<r/2\). Fix an index \(j_0\) in the tail. By the definition of the distance infimum, for each later \(j\) there is a path in \(C\) from \(x_{j_0}\) to \(x_j\) of length less than \(r\). At every point \(z\) of that path,
\[
d_M(p,z)\leq d_M(p,x_{j_0})+
 L(\text{initial part of the path})<2r.
\tag{E.6}
\]
Thus these paths lie in \(N\cap U\). The tail is contained in one connected component \(D\) of \(N\cap U\). Since \(D\) is closed in \(U\) and \(x_j\to p\in U\), we have \(p\in D\subset N\). Also \(D\subset C\), because it is connected and meets the component \(C\). Embeddedness means that ambient convergence to a point of \(N\) is convergence in its subspace manifold topology. Components are open, by B.3's coordinate argument, so the convergence is in the topology of \(C\). Riem A.2 identifies that topology with \(d_C\), proving completeness.

For closed embedded \(N\) one can finish even more directly. Equation (E.5) still gives an ambient limit \(p\), and closedness puts \(p\) in \(N\). A connected coordinate neighbourhood of \(p\) in \(N\) contains the sequence tail, by the subspace topology. It meets \(C\), hence is contained in \(C\), so \(p\in C\). Riem A.2 and the same topology argument give intrinsic convergence. □

## F. Ends, quotients and the torsion hypothesis

The first four examples use the complete earlier programme proofs named in their arguments. For the fifth, the exact free construction source is Jacob W. Erickson and Benjamin McKay, [*Inequivalence of the various notions of completeness for Cartan geometries*, arXiv:2606.00354v1](https://arxiv.org/pdf/2606.00354v1), §4.1. We use their half-cylinder presentation, credit its origin, and give explicit connection, barrier and prescribed-development calculations below. The paper is available under CC BY 4.0; no source prose or figure is reproduced here.

**Example F.1 (the punctured Euclidean plane).** On \(M=\mathbb R^2\setminus\{0\}\) with its Euclidean metric, \(d_M(p,q)=|p-q|\). A minimizing path between distinct points exists exactly when the straight segment joining them avoids zero. The metric and its Levi-Civita connection are incomplete.

**Proof.** For every piecewise \(C^1\) path, the integral norm inequality of Local 0.3 gives \(L\geq|p-q|\). If the straight segment avoids zero it attains this bound. Otherwise \(p,q\) lie on opposite rays. Choose orthonormal coordinates in which \(p=(-a,0),q=(b,0)\), with \(a,b>0\); a Euclidean orthogonal change preserves lengths by direct preservation of its inner product, or by Riem A.3. The polygon
\[
(-a,0),\quad(-a,\epsilon),\quad(b,\epsilon),\quad(b,0)
\]
avoids zero and has length \(a+b+2\epsilon\). Letting \(\epsilon\downarrow0\) proves the distance formula. If a path attained \(a+b\), the nonnegative continuous integrand \(\sqrt{x'^2+y'^2}-x'\) would have zero integral on each smooth piece and hence would vanish there. Thus \(y'=0\) and \(x'\geq0\); continuity at the joining times gives \(y=0\) throughout. The intermediate-value theorem, Local 0.0, would then force the path through the origin. This is the same equality mechanism proved in Riem B.6, now for arbitrary opposite endpoints.

The constant Euclidean metric has zero connection coefficients by Riem A.1. Its geodesics are restrictions of \(p+tv\), by Geo A.1 and Local 0.3. Their maximal domains are the connected intervals containing the initial time on which \(p+tv\ne0\): at a finite boundary they tend to the removed origin and cannot extend in \(M\). For example \(p=(1,0),v=(-1,0)\) has maximal domain \((-\infty,1)\). Also the sequence \((1/j,0)\) is Cauchy for the displayed distance and has no limit in \(M\). This directly proves both failures of completeness. □

**Example F.2 (the hyperbolic boundary is infinitely far away).** For
\[
\mathbb H^n=\{(x,z)\in\mathbb R^{n-1}\times\mathbb R:z>0\},\qquad
g=\frac{|dx|^2+dz^2}{z^2},
\tag{F.1}
\]
the metric is complete. For any two points,
\[
d_g((x_1,z_1),(x_2,z_2))\geq|\log z_2-\log z_1|.
\tag{F.2}
\]
For \(n\geq2\), its nonconstant geodesics are vertical lines or upper semicircles perpendicular to the boundary, with the full affine parametrizations and unique minimizing segments proved in Riem D.2–D.3.

**Proof.** Along a path, its speed is at least \(|z'|/z\). The fundamental theorem and the logarithmic derivative proved in Geo A.4 give
\[
L_g\geq\int |z'|/z\geq|\log z_2-\log z_1|,
\]
which proves (F.2) after taking infima.

Here is a metric proof of completeness that also controls horizontal escape. If \(p_j=(x_j,z_j)\) is \(d_g\)-Cauchy, (F.2) makes \(\log z_j\) Cauchy in \(\mathbb R\). Local 0.1 gives a limit \(b\); continuity of the exponential gives \(z_j\to e^b>0\). In particular \(z_j\leq Z\) for a fixed finite \(Z>0\). For two sufficiently late terms, \(d_g(p_j,p_k)<1/2\). Choose a joining path of length less than \(d_g(p_j,p_k)+\epsilon<1\). Applying the same logarithmic estimate to every initial subpath bounds its height by \(eZ\). Hence
\[
|x_k-x_j|\leq\int|x'|
 \leq eZ\,L_g
 <eZ\bigl(d_g(p_j,p_k)+\epsilon\bigr).
\tag{F.3}
\]
Let \(\epsilon\downarrow0\). Thus \(x_j\) is Euclidean Cauchy and converges, by Local 0.1. The coordinate limit \((x,e^b)\) belongs to \(\mathbb H^n\), and Riem A.2 turns coordinate convergence into metric convergence. For \(n=1\) the horizontal argument is absent and the logarithm is a global isometry onto \(\mathbb R\), with the same conclusion.

For clarity, the exact earlier geodesic proof Riem D.2 gives \(x=b_0,\ z=ae^{ct}\) and
\[
x=b_0+\rho\tanh(\kappa t+\tau)e,\qquad
z=\rho\,\operatorname{sech}(\kappa t+\tau),
\]
with \(a,\rho,\kappa>0,\ |e|=1\), together with the constant solutions. It derives the coefficients, checks every initial condition and proves existence for every real \(t\). Riem D.3 proves global minimality and uniqueness by an explicit isometry to a vertical line. Those complete programme proofs supply these last assertions. Formula (F.2) independently shows why approach to \(z=0\) cannot occur along a finite-length path. □

**Exercise F.3 (distance and minimizing geodesics on a flat cylinder).** Let \(\ell>0\) and equip \(C_\ell=\mathbb R\times(\mathbb R/\ell\mathbb Z)\) with the descended metric \(dx^2+dy^2\). Prove completeness, compute its distance, and characterize uniqueness of a minimizing affine geodesic.

**Solution.** Local 6.3 constructs the smooth quotient charts of \(\mathbb R/\mathbb Z\); rescaling the coordinate by \(\ell\) gives the charts for \(\mathbb R/\ell\mathbb Z\). Products with an interval in the first coordinate give cylinder charts. Their transitions are translations in \(y\), so the Euclidean metric descends smoothly. The projection \(\pi:\mathbb R^2\to C_\ell\) is a local isometry and a smooth covering: over a product of an \(x\)-interval and a quotient interval of length less than \(\ell\), its sheets are the disjoint translates of that product by \(k\ell\) in the second coordinate. The Euclidean plane is metrically complete by Local 0.1 and its Euclidean distance calculation (the integral norm bound and straight segments). Corollary E.4 therefore makes \(C_\ell\) complete.

Fix representatives \(p=(x_1,[y_1])\), \(q=(x_2,[y_2])\). The lifting proof in E.3 gives, for any piecewise \(C^1\) path between them, a piecewise \(C^1\) lift starting at \((x_1,y_1)\), ending at \((x_2,y_2+k\ell)\) for some \(k\in\mathbb Z\). Local inverse charts prove the piecewise regularity, exactly as in that proof's smooth case. The lift has the same length by Riem A.3. Thus its length is at least the Euclidean displacement of these endpoints. Conversely the straight segment between these lifts projects to a path of exactly that length. Consequently
\[
d_{C_\ell}(p,q)=
\min_{k\in\mathbb Z}
\sqrt{(x_2-x_1)^2+(y_2-y_1+k\ell)^2}.
\tag{F.4}
\]
The minimum exists: the inequality
\(|y_2-y_1+k\ell|\geq |k|\ell-|y_2-y_1|\) makes all but finitely many integers give a value larger than the value for \(k=0\).

Every affine geodesic lifts locally to a Euclidean affine line by E.1's naturality identity and the local inverse, and uniqueness of initial-value solutions joins these lifts into the same affine line. Thus on \([0,1]\) the geodesics with the given endpoints are precisely the projections of the straight segments just described. Distinct \(k\) give distinct initial velocities at \(p\), since \(d\pi\) is invertible, and hence distinct geodesics.

There is exactly one minimizing integer except when
\[
(y_2-y_1)/\ell\in\mathbb Z+\tfrac12,
\tag{F.5}
\]
in which case there are exactly two. Indeed, put \(s=-(y_2-y_1)/\ell\) and choose the integer \(m\) with \(m\leq s<m+1\). Such an integer exists by the unboundedness of the integers proved in Local 0.1: in a sufficiently large finite integer interval containing \(s\), take the largest integer at most \(s\). Integers below \(m\) are farther from \(s\) than \(m\), and those above \(m+1\) are farther than \(m+1\). The two remaining distances \(s-m\) and \(m+1-s\) agree exactly at \(s=m+1/2\). This proves (F.5) and the asserted uniqueness criterion, including the constant geodesic when \(p=q\). □

**Example F.4 (a complete background metric does not complete an arbitrary connection).** On \(\mathbb R\), the Euclidean metric \(h=dx^2\) is complete, but the connection \(\nabla_{\partial_x}\partial_x=\partial_x\) is not geodesically complete.

**Proof.** Euclidean metric completeness was proved in C.1. For the specified connection, Geo A.4 proves for every initial point \(p\) and velocity \(v\)
\[
\gamma_v(t)=p+\log(1+vt),\qquad I_v=\{t:1+vt>0\}.
\tag{F.6}
\]
It checks the differential equation \(\gamma''+(\gamma')^2=0\), initial data and maximality. For instance \(v=-1\) gives a finite upper endpoint \(t=1\), with no extension in \(\mathbb R\). This connection is not the Levi-Civita connection of \(h\): its metric derivative satisfies
\[
(\nabla_{\partial_x}h)(\partial_x,\partial_x)
=\partial_x(1)-h(\partial_x,\partial_x)-h(\partial_x,\partial_x)=-2
\]
by the tensor product rule of Linear C.1. Thus the metric hypothesis in B.2 cannot be replaced by an unrelated complete metric. □

**Example F.5 (the Clifton half-cylinder: torsion changes the conclusion).** On \(C=(\mathbb R/\mathbb Z)\times(0,\infty)\), with coordinates \(([x],y)\), let \(g=dx^2+dy^2\), put \(\phi=1/y\), and define the global frame
\[
E_1=\cos\phi\,\partial_x-\sin\phi\,\partial_y,\qquad
E_2=\sin\phi\,\partial_x+\cos\phi\,\partial_y.
\tag{F.7}
\]
The connection making \(E_1,E_2\) parallel is metric-compatible, flat and geodesically complete. Its torsion is nonzero, and \(g\) is incomplete. Moreover a \(C^1\) curve in an initial tangent space need not have an inverse development on its full closed interval.

**Proof.** The quotient and the global coordinate fields are constructed as in F.3. The trigonometric functions and their derivatives are the real and imaginary parts of the circle exponential in Connections E.1. In particular (F.7) is a smooth orthonormal frame. Define
\[
\nabla_X(f^1E_1+f^2E_2)=X(f^1)E_1+X(f^2)E_2.
\tag{F.8}
\]
The product rule proves all connection axioms, and differentiating the Euclidean inner product of the coefficient columns proves metric compatibility. Its curvature is zero: the coefficient of \(\nabla_X\nabla_YV-\nabla_Y\nabla_XV-\nabla_{[X,Y]}V\) is \(X(Yf^i)-Y(Xf^i)-[X,Y]f^i=0\), by the bracket definition in [Principal bundles C.3](principal-bundles-and-associated-bundles.md).

For a direct torsion computation, put
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
R(\theta)=
\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.
\]
The frame matrix in (F.7) is \(S=R(-\phi)\), so \(dS=-JS\,d\phi\) by differentiating sine and cosine. Its connection potential in the coordinate frame is
\[
A=-dS\,S^{-1}=J\,d\phi=-y^{-2}J\,dy.
\tag{F.9}
\]
This follows also by substituting the frame columns \(S\) in the parallel condition \(dS+AS=0\), as in Linear A.1–A.2. Thus \(\nabla_{\partial_x}\partial_y=0\) and \(\nabla_{\partial_y}\partial_x=-y^{-2}\partial_y\). Since the coordinate fields commute, Linear D.1 gives
\[
\mathcal T(\partial_x,\partial_y)=y^{-2}\partial_y\ne0.
\tag{F.10}
\]

The geodesic equation in the parallel frame says that its velocity coefficients are constant, by Linear B.2. Write them as \(a,b\); every geodesic is therefore an integral curve of
\[
x'=a\cos(1/y)+b\sin(1/y),\qquad
y'=-a\sin(1/y)+b\cos(1/y).
\tag{F.11}
\]
If \(a=b=0\), the curve is constant. Otherwise write \(a=A_0\cos\beta,\ b=A_0\sin\beta\), where \(A_0=\sqrt{a^2+b^2}>0\). Existence of \(\beta\) follows from the circle parametrization in Connections E.1. The scalar height equation is
\[
y'=A_0\sin(\beta-1/y).
\tag{F.12}
\]
For all sufficiently large integers \(k\), the positive numbers \(y_k=1/(\beta+k\pi)\) tend to zero and are equilibria of (F.12). Here \(\sin(k\pi)=0\) follows from the same circle exponential and its value \(-1\) at \(\pi\). Given an initial height \(y_0>0\), choose such an equilibrium \(y_*<y_0\). Uniqueness for the smooth scalar ODE, both forwards and backwards (Local 2.1), prevents a solution starting at \(y_0\) from reaching or crossing \(y_*\) at a finite time. Also \(|y'|\leq A_0\), so on any finite time interval \(|t|\leq T\) its height is at most \(y_0+A_0T\).

Thus before any hypothetical finite maximal endpoint, the base curve stays in a compact cylinder
\[
(\mathbb R/\mathbb Z)\times[y_*,y_0+A_0T].
\]
The circle is compact, being the continuous image of \([0,1]\) under its quotient map; alternatively Connections E.1 identifies it with the unit circle. Its product with the displayed closed interval is compact by Local 0.1 under that identification as a closed bounded subset of \(\mathbb R^3\). The vector field in (F.11) is smooth. Compact continuation in Local 2.1 rules out each finite endpoint. This proves geodesic completeness.

The metric is nevertheless incomplete. The points \(([0],1/j)\) are Cauchy, since the vertical segment between two of them has length \(|1/j-1/k|\). Every path also has length at least its change in \(y\), by Local 0.3. A limit in \(C\) would therefore need height zero, which is excluded.

We give an explicit prescribed \(C^1\) development that fails, so no separate equivalence theorem about developments is needed. Let \(p=([0],1)\), and let \(u_0\) be the frame (F.7) at \(p\). On \(0\leq t<1\) take
\[
\gamma(t)=([0],(1-t)^2),\qquad
v(t)=2(1-t)
 \begin{pmatrix}
 \sin((1-t)^{-2})\\
 -\cos((1-t)^{-2})
 \end{pmatrix}.
\tag{F.13}
\]
Set \(v(1)=0\). The bound \(|v(t)|=2(1-t)\) proves continuity at one. Hence
\[
\delta(t)=u_0\int_0^t v(r)\,dr,\qquad 0\leq t\leq1,
\tag{F.14}
\]
is \(C^1\), with \(\delta(0)=0\), by Local 0.3. Since the global frame is parallel, the coefficients of \(\dot\gamma=(0,-2(1-t))\) in it are obtained by multiplying by \(R(1/y)\); they are exactly \(v(t)\). Thus \(\gamma\) has development \(\delta\) on every interval \([0,T]\) with \(T<1\).

If an inverse development existed on \([0,1]\), its velocity in the global parallel frame would be \(v(t)\). Lemma D.1 gives uniqueness of this time-dependent ODE on each \([0,T]\). It would therefore equal \(\gamma\) for every \(t<1\). Its continuous endpoint would have height zero, impossible in \(C\). The factor \(2(1-t)\) in (F.13) is what ensures that the prescribed development is \(C^1\) at the endpoint despite the rotating frame. This example distinguishes geodesic completeness from metric completeness for a metric-compatible connection with torsion, and from existence of all prescribed finite developments. □

**Exercise F.6 (a complete affine torus with curvature and torsion).** Construct a translation-invariant connection on \(\mathbb R^2\) with straight complete geodesics but nonzero torsion and curvature, and descend it to a complete affine connection on the torus.

**Solution.** The difference construction in Linear A.3 permits adding any endomorphism-valued one-form to the ordinary derivative \(D\). Choose the constant one-form \(\alpha=-dy\) and set
\[
\nabla_XY=D_XY+\alpha(X)Y-\alpha(Y)X.
\tag{F.15}
\]
The added term is bilinear in the tangent vectors and smooth, so Linear A.3 proves it is a connection. Its quadratic value on \((v,v)\) vanishes. The coordinate geodesic equation of Geo A.1 is therefore ordinary zero acceleration, giving every geodesic \(p+tv\) for all real \(t\).

With \(e_1=\partial_x,e_2=\partial_y\), (F.15) gives
\[
\nabla_{e_1}e_2=e_1,\qquad
\nabla_{e_2}e_1=-e_1,\qquad
\nabla_{e_1}e_1=\nabla_{e_2}e_2=0.
\]
Its potential matrices are \(A_1=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\) and \(A_2=\left(\begin{smallmatrix}-1&0\\0&0\end{smallmatrix}\right)\). Linear D.1 gives torsion \(2e_1\) on \((e_1,e_2)\); the curvature formula in Geo C.1 gives
\[
R(e_1,e_2)=[A_1,A_2]
=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0,
\]
because the matrices are constant. These computations also appear with full further tensor details in the earlier programme proof Geo F.1.

Curvature D.3 constructs the quotient charts of \(\mathbb R^2/\mathbb Z^2\), whose changes are locally constant translations. Their derivatives are the identity; the constant coefficients in (F.15) consequently agree in every quotient chart and define a smooth connection on the torus. The projection is affine. Every geodesic \([p+tv]\) exists for all time and has the prescribed initial data, so Geo A.1 proves completeness. Equivalently, E.2 applies to this affine projection from the complete source. Torsion and curvature have the same nonzero local coordinate values on the quotient. Thus compactness is not being used to assert completeness of an arbitrary affine connection; it has been established by its explicit geodesics. □

## G. Length spaces and the metric completeness theorem

The metric formulation also covers spaces without tangent vectors. Free construction material for this part is Michael Kunzinger and Roland Steinbauer, *Metric Geometry*, [the Vienna lecture notes dated 27 April 2025](https://www.mat.univie.ac.at/~stein/teaching/skripten/Metric_Geometry_Lecture_Notes-2025-04-27.pdf), §§1.2–1.4. All compactness, curve and endpoint arguments needed below are proved here or in Local 0.0–0.1. In particular, the external statement of the compactness theorem for Lipschitz curves is not being used as its proof.

Throughout this part, a metric takes finite real values. Write
\[
B(p,r)=\{q:d(p,q)<r\},\qquad
K_r(p)=\{q:d(p,q)\leq r\}.
\]
The latter denotes the closed ball, including \(K_0(p)=\{p\}\); it need not be the closure of the open ball. A metric space is **totally bounded** if, for every \(\varepsilon>0\), finitely many open balls of radius \(\varepsilon\) cover it. It is **locally compact** if each point has a compact neighbourhood, and **proper** if every closed bounded subset is compact.

**Lemma G.1 (the compactness criteria).** For a metric space, the following are equivalent: compactness; completeness and total boundedness; sequential compactness.

**Proof.** The equivalence of compactness and sequential compactness, with its full metric proof, is Local 0.1. A compact space is totally bounded by applying its finite-subcover property to the cover by all \(\varepsilon\)-balls. Every Cauchy sequence in it has a convergent subsequence by Local 0.1. If that subsequence tends to \(x\), the triangle inequality, using one sufficiently late subsequence term, shows that the entire Cauchy sequence tends to \(x\). Thus compactness implies completeness.

Conversely, suppose completeness and total boundedness hold, and take a sequence. At stage \(k\), cover the space by finitely many balls of radius \(2^{-k}\). One such ball contains infinitely many of the indices retained at the previous stage; retain those indices. Choose a strictly increasing sequence of indices, the \(k\)-th chosen index belonging to the \(k\)-th retained infinite set. The retained sets are nested. Any two chosen terms with indices after stage \(k\) therefore lie in one ball of radius \(2^{-k}\), so their distance is less than \(2^{1-k}\). They form a Cauchy subsequence, which converges by completeness. The space is sequentially compact and hence compact by Local 0.1. □

For a continuous curve \(c:[a,b]\to X\), define its length by
\[
L(c)=
\sup_{a=t_0<\cdots<t_m=b}
\sum_{i=1}^{m}d(c(t_{i-1}),c(t_i)).
\tag{G.1}
\]
Length may be infinite; a finite-length curve is **rectifiable**. A **length space** is a metric space for which
\[
d(p,q)=\inf\{L(c):c\text{ is a continuous rectifiable curve from }p\text{ to }q\}.
\tag{G.2}
\]
In particular the set on the right is nonempty for every pair. A curve is **shortest** when its length equals the distance between its endpoints. A **local metric geodesic** is a continuous curve each of whose parameter points has a relative interval neighbourhood on which every compact restriction is shortest. This definition permits nonconstant speed and constant portions. A **unit-speed minimizing metric geodesic** satisfies
\[
d(c(s),c(t))=|s-t|
\tag{G.3}
\]
on its whole parameter interval; it is in particular a local metric geodesic.

**Lemma G.2 (length, ordered arc length and finite tails).** Length is additive at each division point of a parameter interval. Every continuous rectifiable curve \(c:[a,b]\to X\), of length \(L\), has a representation
\[
c(t)=\beta(s(t)),\qquad
s(t)=L(c|_{[a,t]}),
\tag{G.4}
\]
where \(s\) is continuous, nondecreasing and onto \([0,L]\), and \(\beta:[0,L]\to X\) is \(1\)-Lipschitz. Its restrictions have length \(L(\beta|_{[r,u]})=u-r\). If \(L=0\), both curves are constant. Every continuous finite-length curve on \([0,a)\), with \(a<\infty\), has Cauchy tails as \(t\uparrow a\).

**Proof.** Inserting a point in a partition cannot decrease its sum, by the triangle inequality. Inserting a fixed division point \(t\) shows that every full partition sum is bounded by the sum of the two subinterval lengths. Conversely, concatenate partitions on the two subintervals whose sums approach their suprema. This proves additivity, including the possibility of infinite length. The two-point partition shows that length bounds the distance between endpoints. Length zero therefore forces all curve values to coincide.

For the stated finite-length curve, additivity makes \(s\) nondecreasing. We prove its continuity without assuming an arc-length theorem. For \(a<t\leq b\), put \(s(t-)=\sup_{u<t}s(u)\). Fix any partition of \([a,t]\), and let \(v<t\) be its penultimate point. For \(v<u<t\), the triangle inequality bounds its sum by the sum of the same partition ending at \(u\), plus \(d(c(u),c(t))\). The former is at most \(s(u)\). Continuity of \(c\) gives a bound of \(s(t-)\) on letting \(u\uparrow t\). Taking the supremum over the original partitions gives \(s(t)\leq s(t-)\). The reverse inequality is monotonicity. This proves left continuity, including at \(b\). Apply this argument to the reversed curve and use additivity with total length \(L\); it gives right continuity, including at \(a\). Thus \(s\) is continuous. Its endpoint values are \(0,L\), so the intermediate-value theorem in Local 0.0 makes it onto.

If \(s(t)=s(u)\) with \(t\leq u\), additivity says the intervening length is zero. Hence \(c(t)=c(u)\). We may define \(\beta(s(t))=c(t)\) unambiguously. For \(s(t)\leq s(u)\), choose ordered preimages, possible by monotonicity; then
\[
d(\beta(s(t)),\beta(s(u)))
\leq L(c|_{[t,u]})=s(u)-s(t).
\]
This proves the Lipschitz bound. Consequently a partition of \([r,u]\) has \(\beta\)-sum at most \(u-r\). For the reverse bound, choose preimages \(t_r\leq t_u\). Every partition sum for \(c|_{[t_r,t_u]}\) becomes a partition sum for \(\beta|_{[r,u]}\) after repeated \(s\)-values are removed. Its supremum is \(s(t_u)-s(t_r)=u-r\). These two bounds prove the claimed restriction lengths, also when \(L=0\).

For a continuous curve on \([0,a)\), its total length means the supremum of lengths over compact subintervals. Put \(s(t)=L(c|_{[0,t]})\) and \(L=\sup_{t<a}s(t)<\infty\). Additivity gives, for \(t\leq u<a\),
\[
d(c(t),c(u))\leq s(u)-s(t)\leq L-s(t).
\tag{G.5}
\]
Monotonicity and the definition of the supremum give \(s(t)\to L\) as \(t\uparrow a\). Equation (G.5) is the Cauchy-tail assertion. □

The Riemannian distance of A.1 is a length-space metric. Indeed, for every piecewise \(C^1\) path, each distance in a partition is at most that subpath's Riemannian length, by the definition of distance. Additivity of the integral in Local 0.3 therefore gives \(L(c)\leq L_g(c)\). On the other hand every continuous curve has \(L(c)\geq d(c(a),c(b))\) by its two-point partition. Taking the infimum over piecewise \(C^1\) curves, whose Riemannian lengths define \(d\), proves (G.2). Local compactness follows by taking a compact closed coordinate ball and using the equality of the metric and manifold topologies proved in Riem A.2. No unproved formula equating the two lengths for arbitrary curves is needed.

**Lemma G.3 (compactness of Lipschitz curves and lower semicontinuity of length).** Let \(K\) be a compact metric space. Any sequence of maps \(f_n:[0,T]\to K\) with a common finite Lipschitz bound has a uniformly convergent subsequence. Its limit has the same Lipschitz bound. If continuous curves on a fixed compact interval converge pointwise to a continuous curve \(f\), then
\[
L(f)\leq\liminf_{n\to\infty}L(f_n).
\tag{G.6}
\]

**Proof.** Let the common Lipschitz bound be \(C\). The case \(T=0\) is sequential compactness of \(K\). If \(T>0\), enumerate the union of all finite grids with vertices \(jT/2^k\). At the first vertex, choose a convergent subsequence by G.1; at the second choose a subsequence of that subsequence, and continue. Taking its successive diagonal terms yields one subsequence converging at every grid vertex.

This subsequence is uniformly Cauchy. Given \(\varepsilon>0\), choose a grid so fine that \(2CT/2^k<\varepsilon/2\) (if \(C=0\), any grid suffices). At all its finitely many vertices, the sufficiently late terms differ by less than \(\varepsilon/2\). For an arbitrary point \(t\), choose a vertex within \(T/2^k\). The triangle inequality and the two Lipschitz bounds show that the two late values at \(t\) differ by less than \(\varepsilon\). Completeness of \(K\), proved in G.1, gives pointwise limits. Passing to those limits in this uniform Cauchy estimate proves uniform convergence. Passing to the limit in
\(d(f_n(s),f_n(t))\leq C|s-t|\) proves the Lipschitz bound for the limit.

For (G.6), fix a finite partition. Pointwise convergence makes its distance sum converge: the difference of any two corresponding distances is at most the sum of the two endpoint errors. Each sum for \(f_n\) is bounded by \(L(f_n)\), so the limiting sum is at most \(\liminf L(f_n)\). Taking the supremum over partitions proves (G.6), also when the supremum is infinite. □

**Lemma G.4 (approximation by an inner ball and compact thickening).** In a length space, if \(R\geq0\), \(\eta>0\), and \(d(p,q)\leq R+\eta\), there is \(z\in K_R(p)\) with \(d(z,q)<2\eta\). If the space is also locally compact and \(K_R(p)\) is compact, then \(K_{R+\delta}(p)\) is compact for some \(\delta>0\).

**Proof.** Take a curve from \(p\) to \(q\) of length \(L<d(p,q)+\eta\leq R+2\eta\), using (G.2), and use its ordered arc-length representation from G.2. If \(L\leq R\), use \(z=q\). Otherwise use \(z=\beta(R)\). The Lipschitz bound yields
\[
d(p,z)\leq R,\qquad d(z,q)\leq L-R<2\eta.
\]
This also proves the assertion when \(R=0\).

For each \(x\in K_R(p)\), local compactness supplies a compact neighbourhood \(N_x\). Choose \(\rho_x>0\) so that \(B(x,3\rho_x)\subset N_x\), possible because \(N_x\) contains an open neighbourhood of \(x\). Then \(K_{2\rho_x}(x)\) is a closed subset of \(N_x\), hence compact by Local 0.1. Finitely many balls \(B(x_i,\rho_i)\) cover \(K_R(p)\). Put \(\delta=\frac14\min_i\rho_i>0\). For \(q\in K_{R+\delta}(p)\), the first assertion gives \(z\in K_R(p)\) with \(d(q,z)<2\delta\). Choose \(i\) with \(d(z,x_i)<\rho_i\). Then
\[
d(q,x_i)<2\delta+\rho_i\leq\tfrac32\rho_i<2\rho_i.
\]
Thus \(K_{R+\delta}(p)\) is contained in the finite union of the compact sets \(K_{2\rho_i}(x_i)\). It is closed there, since the triangle inequality makes distance to \(p\) continuous. The finite union and its closed subset are compact by Local 0.1. □

**Theorem G.5 (Hopf–Rinow–Cohn-Vossen for length spaces).** In a nonempty locally compact length space \(X\), the following four conditions are equivalent:

1. \(X\) is complete.
2. \(X\) is proper.
3. Every rectifiable local metric geodesic \(c:[0,a)\to X\), where \(0<a<\infty\), has a continuous extension to \([0,a]\).
4. There is a point \(p\in X\) such that every such geodesic starting at \(p\) has a continuous extension to \([0,a]\).

They are still equivalent if conditions 3 and 4 quantify only over unit-speed minimizing metric geodesics with finite parameter intervals. Under these conditions every pair of points is joined by a shortest curve, which for distinct endpoints has a unit-speed minimizing parametrization on the interval of length equal to their distance.

**Proof.** We prove all implications and the existence assertion.

Suppose 2 holds. A Cauchy sequence is bounded: after some index all terms are within distance one of a fixed late term, and the finitely many earlier distances also have a finite bound. It lies in a compact closed ball. G.1 gives a convergent subsequence; the Cauchy property and the triangle inequality then make the entire sequence converge. Thus 2 implies 1.

Suppose 1 holds. In fact every continuous rectifiable curve \(c:[0,a)\to X\) has an endpoint. Choose \(t_j\uparrow a\). Equation (G.5) makes \(c(t_j)\) Cauchy, so it has a limit \(q\). The same estimate, followed by the triangle inequality with a late \(c(t_j)\), proves \(c(t)\to q\) as \(t\uparrow a\). Define \(c(a)=q\); the resulting extension is continuous. This proves 3 without using a geodesic assumption. Clearly 3 implies 4 by choosing any point of the nonempty space.

It remains to show that 4 implies 2. The following argument uses condition 4 only for unit-speed minimizing geodesics, which will also prove the stated weaker versions. Fix its point \(p\). Consider
\[
\mathcal S=\{r\geq0:K_r(p)\text{ is compact}\}.
\tag{G.7}
\]
This set is downward closed: a smaller closed ball is a closed subset of a larger compact one. Local compactness gives some positive radius in \(\mathcal S\), by taking a sufficiently small closed ball inside a compact neighbourhood. If \(\mathcal S\) is unbounded, all closed balls about \(p\) are compact. Every closed bounded set is contained in one of them (change the bounding centre by the triangle inequality) and is compact by Local 0.1. This is 2.

Suppose for a contradiction that \(R=\sup\mathcal S<\infty\). Then \(R>0\), and every \(K_T(p)\) with \(0\leq T<R\) is compact: choose an element of \(\mathcal S\) larger than \(T\) and use downward closure. We shall prove \(K_R(p)\) compact as well.

Take any sequence \(q_n\in K_R(p)\). If infinitely many of its terms lie in some \(K_T(p)\) with \(T<R\), they have a convergent subsequence there. Otherwise, for every \(T<R\), only finitely many terms lie in \(K_T(p)\). Hence
\[
r_n=d(p,q_n)\longrightarrow R.
\]
By the length-space property choose a curve from \(p\) to \(q_n\) with length
\[
r_n\leq L_n<r_n+\frac1n.
\tag{G.8}
\]
Reparametrize by G.2 to obtain a \(1\)-Lipschitz curve \(\sigma_n:[0,L_n]\to X\), and extend it constantly at \(q_n\) to \([0,R+1]\). This extension is \(1\)-Lipschitz: if one parameter precedes \(L_n\) and the other follows it, its distance is at most the first parameter's distance in time to \(L_n\), which is at most the difference of the two parameters.

Let \(T_j=R(1-2^{-j})\), \(j\geq1\). For \(t\leq T_j\), the extended curve satisfies \(d(p,\sigma_n(t))\leq t\), also when \(t\geq L_n\). Thus its restriction to \([0,T_j]\) takes values in the compact set \(K_{T_j}(p)\). Lemma G.3 supplies a uniformly convergent subsequence on \([0,T_1]\); from it choose one converging on \([0,T_2]\), and continue. The successive diagonal terms converge uniformly on every \([0,T_j]\). Their limits agree on overlaps because limits in a metric space are unique. They therefore give a \(1\)-Lipschitz curve
\[
\gamma:[0,R)\longrightarrow X,\qquad \gamma(0)=p.
\]
We relabel this diagonal subsequence by \(n\); (G.8) and \(L_n-r_n\to0\) still hold along it.

For fixed \(0\leq s<t<R\), eventually \(L_n>t\), since \(L_n\to R\). The triangle inequality between \(p,\sigma_n(s),\sigma_n(t),q_n\), and the Lipschitz bounds on the first and last portions, give
\[
r_n
\leq s+d(\sigma_n(s),\sigma_n(t))+(L_n-t).
\]
Therefore
\[
t-s-(L_n-r_n)
\leq d(\sigma_n(s),\sigma_n(t))\leq t-s.
\]
Pass to the limit at \(s,t\). We obtain \(d(\gamma(s),\gamma(t))=t-s\). Thus \(\gamma\) is a unit-speed minimizing metric geodesic. Its total length is \(R\): every compact restriction has length equal to its parameter length by (G.3) and partition telescoping. Condition 4 gives a continuous endpoint \(q_\infty=\gamma(R)\).

The same subsequence of endpoints tends to \(q_\infty\). For fixed \(t<R\) and large \(n\) with \(L_n>t\),
\[
d(q_n,q_\infty)
\leq (L_n-t)
 +d(\sigma_n(t),\gamma(t))
 +d(\gamma(t),q_\infty).
\tag{G.9}
\]
Given \(\varepsilon>0\), first choose \(t\) sufficiently close to \(R\) that \(R-t<\varepsilon/4\) and the last term is less than \(\varepsilon/4\). Then choose \(n\) so large that \(|L_n-R|<\varepsilon/4\) and the middle term is less than \(\varepsilon/4\). Equation (G.9) proves convergence. Distance to \(p\) is continuous, so \(q_\infty\in K_R(p)\).

We have proved that every sequence in \(K_R(p)\) has a subsequence converging in that ball. By G.1 the ball is compact. Lemma G.4 now gives a larger compact ball \(K_{R+\delta}(p)\), contradicting the definition of \(R\). This proves 4 implies 2.

For the versions involving only unit-speed minimizing geodesics, 1 still implies the restricted condition 3 by the same finite-length argument, and 3 implies the restricted 4. The preceding proof of 4 implies 2 used only these restricted geodesics. Both sets of four conditions are therefore equivalent.

Finally assume these conditions hold, and take \(p,q\in X\), with \(r=d(p,q)\). If \(r=0\), then \(p=q\) and the constant curve suffices. If \(r>0\), choose curves with lengths \(L_n\) satisfying \(r\leq L_n<r+1/n\). Reparametrize them by G.2 and then linearly onto \([0,1]\). The resulting curves \(f_n\) have Lipschitz bounds \(L_n\leq r+1\) and take values in \(K_{r+1}(p)\), which is compact by properness. Lemma G.3 gives a uniformly convergent subsequence with limit \(f\). Its endpoints are \(p,q\), and passing to the limit in the sharper bounds \(d(f_n(s),f_n(t))\leq L_n|s-t|\) gives
\[
d(f(s),f(t))\leq r|s-t|.
\]
For \(0\leq s<t\leq1\), apply the triangle inequality through \(f(s),f(t)\):
\[
r=d(p,q)\leq rs+d(f(s),f(t))+r(1-t).
\]
The reverse bound follows, so \(d(f(s),f(t))=r(t-s)\). Thus \(u\mapsto f(u/r)\) on \([0,r]\) is a unit-speed minimizing geodesic, with length \(r\) by (G.1). □

The endpoint in this theorem is a continuous endpoint **at** \(a\). For a unit-speed minimizing geodesic its distance identity also extends to the closed interval, by continuity of distance. Neither the theorem nor the proof asserts that a geodesic continues past that endpoint.

**Exercise G.6 (completeness without local compactness).** Give a complete length space that is not proper, and identify precisely which hypothesis of G.5 fails.

**Solution.** Take countably many copies of the nonnegative real half-line, identify their origins, and retain the following explicit set and metric:
\[
X=\{o\}\ \cup\ \{(n,t):n\in\mathbb N,\ t>0\},
\]
\[
d(o,(n,t))=t,\qquad
d((n,s),(m,t))=
\begin{cases}
|s-t|,&n=m,\\
s+t,&n\ne m.
\end{cases}
\tag{G.10}
\]
Also put \(d(o,o)=0\), and use symmetry for reversed pairs. Positivity, symmetry and separation follow from the formula. For the triangle inequality, if the first and last points are on one branch, an intermediate point on that branch gives the real triangle inequality; a point off that branch gives a sum at least \(s+t\geq|s-t|\). If the first and last branches differ, an intermediate point at \(o\) gives equality; one on a third branch adds twice its radius; one on the first branch gives \(|s-u|+u+t\geq s+t\), and one on the last gives \(s+u+|u-t|\geq s+t\). Cases with \(o\) follow from the same inequalities with one radius zero. Thus (G.10) is a metric.

On one branch the straight interval joining two points is an isometric copy of the real interval of their distance. Between different branches, move at unit speed to \(o\) and then at unit speed out along the other branch. Two parameters on different portions have distance equal to the sum of their distances to the joining time, hence to their parameter difference. Parameters on one portion have the same property by (G.10). This is a unit-speed minimizing metric geodesic. Consequently every pair has a curve of length its distance, and the two-point partition bounds every competing length below by that distance. The space is a length space.

To prove completeness, let \(x_j\) be Cauchy, and put \(r_j=d(o,x_j)\). The reverse triangle inequality gives \(|r_j-r_k|\leq d(x_j,x_k)\). Thus \(r_j\) is Cauchy in \(\mathbb R\), and it has a limit \(r\geq0\) by Local 0.0. If \(r=0\), then \(x_j\to o\). If \(r>0\), eventually \(r_j>r/2\) and every pairwise tail distance is less than \(r\). Two points on different branches would have distance \(r_j+r_k>r\). Hence the tail lies on a single branch, with positive coordinates \(r_j\to r\), and it converges to that branch's point of radius \(r\).

The closed unit ball is not compact: the points \((n,1)\) have pairwise distance two, so no subsequence is Cauchy or convergent, contrary to G.1. More precisely, local compactness fails at \(o\). If a compact neighbourhood \(K\) of \(o\) existed, it would contain some \(B(o,\varepsilon)\). Its points \((n,\varepsilon/2)\) would have pairwise distance \(\varepsilon\), again contradicting sequential compactness of \(K\). Completeness and the length-space property both hold; the missing hypothesis is local compactness. □

**Exercise G.7 (extension to an endpoint versus past it).** Verify all four conditions of G.5 for the closed interval \(X=[0,1]\) with its usual metric, and show why the conclusion does not extend unit-speed geodesics beyond every finite endpoint.

**Solution.** The interval is compact by Local 0.1, hence complete by G.1. It is locally compact because the whole compact space is a neighbourhood of each of its points. Every closed subset is compact, so it is proper. Real straight segments have length their endpoint distance by telescoping the sums in (G.1), and every other curve has length at least that distance. Thus it is a length space. The equivalence in G.5 now proves conditions 3 and 4 as well; directly, its completeness and (G.5) give the asserted endpoint for every rectifiable curve.

The unit-speed minimizing geodesic \(\gamma(t)=t\), \(0\leq t<1\), extends to \(\gamma(1)=1\). It cannot remain unit-speed minimizing on \([0,1+\varepsilon]\), because the distance from its starting point would need to exceed the diameter one. It cannot even have a continuation that is locally unit-speed and minimizing around time one. Indeed, choose small \(h>0\) within such a proposed local interval and within the continuation's domain. Local unit-speed minimality gives
\[
d(1,\gamma(1+h))=h,\qquad
d(\gamma(1-h),\gamma(1+h))=2h.
\]
The first equation forces \(\gamma(1+h)=1-h\) in \([0,1]\), whereas \(\gamma(1-h)=1-h\) already. The second equation would then say \(0=2h\), a contradiction. A constant extension is continuous but has no unit-speed continuation property. This proves the distinction using a space that satisfies every hypothesis and conclusion of G.5. □
