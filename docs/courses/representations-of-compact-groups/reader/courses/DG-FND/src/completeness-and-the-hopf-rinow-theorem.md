# Completeness and the Hopf–Rinow theorem

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Draft; self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Original text is CC0 1.0; the attributed Clifton half-cylinder subsection retains CC BY 4.0.*

A geodesic is specified by a position and a velocity. A Cauchy sequence concerns only positions. On a Riemannian manifold these two kinds of completeness nevertheless agree. The link is positivity of the metric: constant geodesic speed controls the velocity whenever the position stays in a compact region. A second link is more surprising. Extending every geodesic from one point produces shortest geodesics and compact distance balls throughout the manifold.

Read [Riemannian connections and convex neighbourhoods](riemannian-connections-and-convex-neighbourhoods.md), Sections 1–4, for the distance topology, Levi-Civita connection, normal-ball minimization and uniform local normal balls. [Geodesics, normal coordinates and curvature](geodesics-normal-coordinates-and-curvature.md), Section 2, proves the exponential map and uniqueness of geodesic initial values. [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md), Theorem 2.1, supplies differential-equation continuation. Section 4 below also uses development, proved in [Linear and affine connections](linear-and-affine-connections.md), Section 5. Basic references are [Meinrenken], [Kunzinger–Steinbauer] and [Wilkins]. The example of a metric connection with torsion in Section 6 uses the open treatment [Erickson–McKay].

## 1. What can fail at a finite endpoint?

Throughout, \(M\) is a nonempty connected finite-dimensional smooth manifold without boundary, and \(g\) is a positive definite smooth Riemannian metric. It is Hausdorff and second countable. Write \(d=d_g\) for its Riemannian distance and

\[
\begin{aligned}
B_r(p)&=\{q:d(p,q)<r\},\\
\overline B_r(p)&=\{q:d(p,q)\le r\}.
\end{aligned}
\]

The second symbol denotes a closed distance ball. The distance topology is the manifold topology, by Riemannian connections and convex neighbourhoods, Proposition 1.1. In particular, \(d(p,\cdot)\) is continuous in that topology: the triangle inequality gives

\[
|d(p,x)-d(p,y)|\le d(x,y).
\tag{1.1}
\]

The metric is **complete** if every Cauchy sequence converges in \(M\). A sequence \((x_j)\) is Cauchy if for every \(\varepsilon>0\) all sufficiently late pairs satisfy \(d(x_j,x_k)<\varepsilon\).

The metric is **geodesically complete** if every maximal affinely parametrized Levi-Civita geodesic is defined on all of \(\mathbb R\). Constant geodesics already have this property. A nonconstant one has constant speed, so it can be rescaled to have speed one. Rescaling an affine parameter does not change whether its domain has a finite endpoint.

A **minimizing geodesic** between two points has length equal to their distance. When discussing uniqueness between fixed endpoints, we use its affine parametrization on \([0,1]\).

A metric space is **proper** if every closed bounded subset is compact. Here bounded means contained in some finite-radius ball. By the triangle inequality the centre used in this definition is immaterial. Properness is equivalent to compactness of all closed distance balls: one implication applies to those balls; the other puts a closed bounded set in one such ball and uses closedness.

Completeness and properness differ for general metric spaces. The discrete metric \(d(x,y)=1\) for distinct points on an infinite set is complete: a Cauchy sequence is eventually constant. The whole set is closed and bounded but not compact, since its singleton open cover has no finite subcover. The geometry of a Riemannian distance will supply the missing implication.

**Lemma 1.1 (normal radii near a compact set).** If \(K\subset M\) is compact, there is \(\rho>0\) such that, for every \(x\in K\), \(\exp_x\) maps the tangent ball \(\{|v|_{g_x}<\rho\}\) diffeomorphically onto \(B_\rho(x)\). Its radial segments are the unique minimizing geodesics in \(M\).

**Proof.** The proof of Riemannian connections and convex neighbourhoods, Theorem 4.1, gives an open neighbourhood \(W\) of each point and one positive radius \(\rho_W\) valid for every centre in \(W\). Indeed the pair map

\[
(x,v)\longmapsto(x,\exp_xv)
\]

is a diffeomorphism on a coordinate product near the zero vector. A uniform lower bound for the metric norm puts a fixed tangent metric ball in that product. Its fibre exponential is injective with invertible differential. Theorem 3.2 of that lesson then identifies its image with the whole-manifold distance ball and proves the asserted minimization.

Take finitely many of these neighbourhoods covering \(K\), and let \(\rho\) be the minimum of their positive radii. Restricting a larger tangent ball to radius \(\rho\) gives the claimed normal ball, again by that theorem. □

**Lemma 1.2 (finite-time extension).** Let \(\gamma:[a,b)\to M\) be a geodesic, where \(b<\infty\). If \(\gamma(t)\) converges to a point of \(M\) as \(t\uparrow b\), then \(\gamma\) extends as a geodesic beyond \(b\).

**Proof.** Let its constant speed be \(\kappa\). Choose a coordinate ball with compact closure around the limit point, contained in a slightly larger chart. The tail of \(\gamma\) lies in this closed ball. On it positivity gives a constant \(m>0\) such that

\[
|w|_{g_x}\ge m|w|_{\mathbb R^n}.
\]

Thus the coordinate velocity of this tail is bounded by \(\kappa/m\). The geodesic equation is the smooth first-order equation for position and velocity

\[
\begin{aligned}
(x^i)'&=v^i,\\
(v^k)'&=-\Gamma^k_{ij}(x)v^iv^j.
\end{aligned}
\tag{1.2}
\]

Its phase trajectory therefore lies in a compact product of the closed coordinate ball and a closed velocity ball. Include a compact interval of time ending at \(b\). This product lies inside the equation's open domain. The continuation part of Local tools for bundles and transport, Theorem 2.1, gives a positive uniform existence time for initial phase points in this compact product. Start at a time sufficiently close to \(b\); the resulting solution exists beyond \(b\). Uniqueness makes it agree with the old solution on their common interval. □

The proof controls velocity as well as position. Merely assigning a limiting position is not an initial condition for (1.2).

**Lemma 1.3 (a minimizing broken geodesic has no corner).** Suppose a path is the concatenation of finitely many unit-speed geodesic segments and has length equal to the distance between its endpoints. Then it is one smooth unit-speed geodesic.

**Proof.** Every subpath minimizes between its endpoints. Otherwise choose a competing path whose length is strictly smaller than that subpath's length, and replace it. The resulting whole path would be shorter than the distance between its endpoints.

Consider a joining point \(z\). By the local version of Lemma 1.1, centres near \(z\) have a common normal radius \(\rho>0\). Choose points \(a\) and \(b\) just before and after this join so that \(a\) is one of those centres and the subpath from \(a\) to \(b\) has length less than \(\rho\). Every point of this subpath has distance from \(a\) at most the length already traversed, hence lies in \(B_\rho(a)\). It is a minimizing path in that normal ball.

Riemannian connections and convex neighbourhoods, Theorem 3.2, proves that every piecewise \(C^1\) minimizer from its centre traces the radial geodesic monotonically. Since the path here has speed one on both pieces, its radial parameter is the elapsed length. Both pieces are therefore the same affinely parametrized radial geodesic across the join. Apply this at every join. □

This argument uses local minimality and its equality case. No variational formula is required.

## 2. One point gives compact balls

Saying that \(\exp_p\) is defined on all of \(T_pM\) means that each initial vector at \(p\) has a geodesic existing through time one. By rescaling initial vectors this is equivalent to every geodesic starting at \(p\) existing for all positive and negative times:

\[
\gamma_v(t)=\exp_p(tv).
\tag{2.1}
\]

The exponential map need not be injective on this full tangent space.

**Theorem 2.1 (one-point completeness).** Suppose \(\exp_p\) is defined on all of \(T_pM\) for some \(p\in M\). Then every \(q\in M\) can be joined to \(p\) by a minimizing geodesic, and every closed distance ball centred at \(p\) is compact. Consequently every closed bounded subset of \(M\) is compact.

**Proof.** If \(M\) has dimension zero, connectedness makes it a single point and everything is immediate. Suppose its dimension is positive.

For \(R\ge0\), consider the initial vectors whose radial geodesics really minimize:

\[
\begin{gathered}
A_R=\{v\in T_pM:\\
|v|_{g_p}\le R,\quad
d(p,\exp_pv)=|v|_{g_p}\},\\
E_R=\exp_p(A_R),\\
S_R=\overline B_R(p).
\end{gathered}
\tag{2.2}
\]

The tangent closed ball is compact in a finite-dimensional vector space. The equality in (2.2) is a closed condition, since the norm, exponential and distance are continuous. Thus \(A_R\) and \(E_R\) are compact for every \(R\), even before we know that \(S_R\) is compact. Moreover

\[
E_R\subset S_R,
\]

and the sets \(E_R\) increase with \(R\).

Every point of \(E_R\) is reached by a geodesic of length equal to its distance from \(p\). Conversely, a minimizing geodesic from \(p\) of length at most \(R\), parametrized on \([0,1]\), has initial velocity of norm its length and places its endpoint in \(E_R\). Thus \(E_R\) is precisely the part of \(S_R\) already reached by minimizing geodesics.

A normal ball at \(p\) proves \(E_R=S_R\) for all sufficiently small \(R\), including zero. Define

\[
\begin{gathered}
R_*=\sup\{R\ge0:\\
E_s=S_s\text{ for all }s\in[0,R]\}.
\end{gathered}
\tag{2.3}
\]

We will prove that \(R_*=\infty\). Suppose instead that \(0<R_*<\infty\). First we show

\[
E_{R_*}=S_{R_*}.
\tag{2.4}
\]

If \(d(p,q)<R_*\), choose \(s\) strictly between these numbers. The definition of the supremum, together with the requirement for every smaller radius in (2.3), gives \(E_s=S_s\), hence \(q\in E_{R_*}\).

Now let \(d(p,q)=R_*\). Choose positive \(\varepsilon_j\downarrow0\), with \(\varepsilon_j<R_*\), and paths from \(p\) to \(q\) of length less than \(R_*+\varepsilon_j\). Along each path the accumulated length is continuous from zero to its total length. Choose a point \(q_j\) at accumulated length \(R_*-\varepsilon_j\). The remaining path has length less than \(2\varepsilon_j\), so

\[
\begin{aligned}
d(p,q_j)&\le R_*-\varepsilon_j<R_*,\\
d(q_j,q)&<2\varepsilon_j.
\end{aligned}
\tag{2.5}
\]

Each \(q_j\) lies in \(E_{R_*}\) by the preceding case. This set is compact, hence closed in \(M\). Since \(q_j\to q\), it also contains \(q\). This proves (2.4), and in particular makes \(S_{R_*}\) compact.

By Lemma 1.1 choose a common normal radius \(\rho>0\) for centres in \(S_{R_*}\), and choose \(0<\delta<\rho\). We claim that every point at distance at most \(R_*+\delta\) is also reached by a minimizing geodesic from \(p\). Only a point \(q\) with

\[
R_*<D:=d(p,q)\le R_*+\delta
\]

needs to be considered.

Choose paths \(\eta_j\) from \(p\) to \(q\) with \(L(\eta_j)<D+1/j\). Continuity of \(d(p,\eta_j(t))\) gives a point \(x_j\) on each path at distance exactly \(R_*\) from \(p\). Splitting the path there yields

\[
\begin{aligned}
D&\le R_*+d(x_j,q)\\
&\le L(\eta_j)<D+1/j.
\end{aligned}
\tag{2.6}
\]

The points \(x_j\) lie in the compact set \(S_{R_*}\). Pass to a subsequence converging to \(x\). Continuity in (1.1) gives

\[
\begin{gathered}
d(p,x)=R_*,\\
d(x,q)=D-R_*,\\
D-R_*\le\delta<\rho.
\end{gathered}
\tag{2.7}
\]

Equation (2.4) supplies a minimizing unit-speed segment from \(p\) to \(x\). The normal ball at \(x\) supplies a minimizing unit-speed segment from \(x\) to \(q\). Their concatenation has length

\[
R_*+(D-R_*)=D=d(p,q).
\]

Lemma 1.3 makes this concatenation a single smooth geodesic. If \(w\) is its initial unit vector, its endpoint is \(\exp_p(Dw)\). The vector \(Dw\) belongs to \(A_{R_*+\delta}\). In fact it belongs to \(A_s\) whenever \(D\le s\). Together with (2.4), this proves \(E_s=S_s\) for every \(s\le R_*+\delta\), contradicting (2.3).

Therefore \(R_*=\infty\), so \(E_R=S_R\) for every finite \(R\). Equation (2.2) proves that each such ball is compact and every point in it has a minimizing geodesic from \(p\). Finally any closed bounded set lies in a ball centred at \(p\), by the triangle inequality, and is a closed subset of that compact ball. □

The compactness used in this proof comes first from a bounded set of initial vectors. It is then transferred to distance balls. Assuming compact distance balls at the outset would assume part of the conclusion.

*References:* [Meinrenken, Section 17] gives a radius-extension proof; [Kunzinger–Steinbauer, Lemma 2.4.1] gives a proof by continuing a geodesic toward a fixed endpoint.

## 3. The completeness equivalences

**Theorem 3.1 (Hopf–Rinow).** For a connected Riemannian manifold the following conditions are equivalent:

1. Its Riemannian distance is a complete metric.
2. Every affinely parametrized geodesic exists on all of \(\mathbb R\).
3. For some \(p\in M\), \(\exp_p\) is defined on all of \(T_pM\).
4. Every closed bounded subset of \(M\) is compact.

When these conditions hold, every pair of points is joined by a minimizing geodesic.

**Proof.** First assume metric completeness. If a maximal nonconstant geodesic has a finite upper endpoint \(b\), rescale it to speed one and choose \(t_j\uparrow b\). Length bounds distance, so

\[
d(\gamma(t_j),\gamma(t_k))\le|t_j-t_k|.
\tag{3.1}
\]

This is a Cauchy sequence and has a limit \(x\in M\). The whole curve tends to \(x\), not just the chosen sequence: for \(t\) and \(t_j\) close to \(b\),

\[
d(\gamma(t),x)
\le |t-t_j|+d(\gamma(t_j),x),
\]

and both terms can be made arbitrarily small. Lemma 1.2 extends the geodesic beyond \(b\), a contradiction. Reversing time excludes a finite lower endpoint. This proves \(1\Rightarrow2\).

The implication \(2\Rightarrow3\) follows from the definition of the exponential map. Theorem 2.1 proves \(3\Rightarrow4\).

For \(4\Rightarrow1\), let \((x_j)\) be Cauchy. Its tail lies in \(B_1(x_N)\) for some \(N\). Including the finitely many earlier points in a larger ball shows that the whole sequence is bounded. It lies in a compact closed ball and thus has a convergent subsequence, say \(x_{j_k}\to x\). To see that the whole sequence converges, given \(\varepsilon>0\) choose late indices so that \(d(x_j,x_{j_k})<\varepsilon/2\) and \(d(x_{j_k},x)<\varepsilon/2\); the triangle inequality gives \(d(x_j,x)<\varepsilon\). The subsequence exists because a compact metric space is sequentially compact: if a sequence has no accumulation point, each point has a neighbourhood containing only finitely many of its terms, and a finite subcover gives a contradiction. An accumulation point supplies a subsequence in its successive radius-\(1/k\) balls.

Finally, condition 2 gives the hypothesis of Theorem 2.1 at every chosen starting point. That theorem supplies a minimizing geodesic to every other point. □

Thus **complete Riemannian manifold** can mean either metric or geodesic completeness. The positive metric and the Levi-Civita connection are part of the assertion.

Having a shortest geodesic for every pair is a consequence, not an equivalent fifth condition. An open Euclidean ball has a straight minimizing segment between every pair but is incomplete: a sequence tending radially to its missing boundary is Cauchy with no limit in the ball. Nor does completeness force uniqueness. Opposite points of a round sphere have many shortest great-circle semicircles.

**Corollary 3.2 (compact manifolds).** Every compact Riemannian manifold is geodesically complete, and its connected components are complete metric spaces.

**Proof.** A connected component is closed in the compact manifold, hence compact. It is also open, since manifolds have connected coordinate neighbourhoods. Its Riemannian distance gives its topology. Every closed bounded subset of the component is a closed subset of this compact component, so Theorem 3.1 applies. Geodesics remain in their connected component. □

**Corollary 3.3 (homogeneous manifolds).** If the isometries of a Riemannian manifold act transitively on it, the manifold is geodesically complete. Each connected component is metrically complete.

**Proof.** Fix \(p\). In positive dimension the set of unit initial vectors at \(p\) is compact. Smooth local existence and a finite cover of this sphere give \(\epsilon>0\) such that every one of these initial geodesics exists on \((-\epsilon,\epsilon)\). In dimension zero all geodesics are constant.

For any \(q\) and any unit vector \(v\in T_qM\), choose an isometry \(F\) with \(F(p)=q\). The vector \((dF_p)^{-1}v\) has norm one. Isometries preserve geodesics, by Riemannian connections and convex neighbourhoods, Proposition 2.2. Its geodesic, followed by \(F\), gives a geodesic with initial data \((q,v)\) on the same interval \((-\epsilon,\epsilon)\). Thus every unit initial datum at every point has this uniform existence time.

Start a unit-speed geodesic again at the end of successive intervals of length \(\epsilon/2\). The new segment exists for time \(\epsilon\); initial-value uniqueness glues it to the preceding one. Finitely many steps reach any prescribed finite positive or negative time. Rescale for other nonzero speeds. Theorem 3.1 then gives metric completeness on each component. □

Transitivity here concerns isometries of the given metric. An arbitrary transitive smooth action need not preserve that metric and does not provide the argument.

## 4. Completeness and development

Development compares a path with a path in its initial tangent space. Let \(\gamma(0)=p\), let \(u_0:\mathbb R^n\to T_pM\) be an orthonormal frame, and let \(u(t)\) be its parallel transport along \(\gamma\). The development, proved in Linear and affine connections, Theorem 5.1, is

\[
\begin{aligned}
\delta(t)&=u_0\int_0^t u(s)^{-1}\gamma'(s)\,ds,\\
\delta'(t)&=T_{0t}^{-1}\gamma'(t).
\end{aligned}
\tag{4.1}
\]

Here \(T_{0t}\) is linear parallel transport. Metric compatibility makes it an isometry, so

\[
|\delta'(t)|_{g_p}=|\gamma'(t)|_g.
\tag{4.2}
\]

Thus development preserves length on every subinterval, though it need not preserve endpoints or the shape of a curve.

**Theorem 4.1 (prescribed finite developments).** If \(M\) is complete, every piecewise \(C^1\) curve \(\delta:[0,a]\to T_pM\), with \(\delta(0)=0\), is the development of a unique piecewise \(C^1\) curve \(\gamma:[0,a]\to M\) starting at \(p\). Conversely, if every such curve can be realized at one fixed point \(p\), then \(M\) is complete.

**Proof.** Write \(d(t)=u_0^{-1}\delta(t)\). To recover the base path and its parallel frame, solve simultaneously

\[
\begin{aligned}
\gamma'&=u(t)d'(t),\\
(u^k_{\alpha})'
&=-\Gamma^k_{ij}(\gamma)\,
  (\gamma^i)'u^j_{\alpha},\\
\gamma(0)&=p,\qquad u(0)=u_0.
\end{aligned}
\tag{4.3}
\]

The second equation is precisely parallel transport of each frame column. In a chart these equations are continuous in time and smooth, with locally bounded derivatives, in the position and frame entries on each \(C^1\) piece. The integral-equation proof of Local tools for bundles and transport, Theorem 2.1, works under these time conditions: it uses bounds and continuity in time, not time derivatives, for existence and uniqueness. This gives a local solution.

Along it,

\[
\frac{d}{dt}g(u_\alpha,u_\beta)=0,
\]

so its frame remains orthonormal. Hence \(|\gamma'|=|d'|\), and (4.1) recovers the prescribed development.

We show that this solution reaches the end of a whole \(C^1\) piece. Suppose its maximal upper endpoint on that piece is \(b\le a\). Since \(d'\) is bounded there, for \(s<t<b\)

\[
\begin{aligned}
d(\gamma(s),\gamma(t))
&\le\int_s^t|d'(\tau)|\,d\tau\\
&\le C(t-s).
\end{aligned}
\tag{4.4}
\]

Completeness implies that \(\gamma(t)\) has a limit as \(t\uparrow b\), by the same Cauchy and whole-tail argument as in Theorem 3.1.

Take a compact coordinate ball \(K\) containing this tail and its limiting point. The orthonormal frames above \(K\) form a compact subset of the frame coordinates. To verify this directly, let \(G(x)\) be the metric matrix. A frame matrix \(U\) satisfies

\[
U^TG(x)U=I.
\tag{4.5}
\]

A uniform positive lower bound for \(G\) bounds every column of \(U\). Equation (4.5) defines a closed set over compact \(K\), so the resulting matrices form a compact set. Every one is invertible: a vector in the kernel of \(U\) would contradict (4.5). Thus this compact set lies inside the frame equation's domain.

The time-continuous continuation argument for (4.3) now gives a uniform existence time on this compact set, and extends the solution to and, when inside the piece, beyond \(b\). At a piece endpoint the continuous coefficient \(d'\) can be extended by its endpoint value to apply that argument on a slightly larger time interval. Take the limiting frame there as the initial frame for the next piece. Finitely many such steps reach \(a\). Local uniqueness glues the solution and proves global uniqueness.

For the converse, prescribe \(\delta(t)=tv\), for any \(v\in T_pM\) and any finite interval. Equation (4.1) says \(\gamma'(t)=T_{0t}v\), so \(D_t\gamma'=0\). This is the geodesic with initial vector \(v\), defined through the prescribed time. Taking time one for every vector gives \(\exp_p\) on all of \(T_pM\). Theorem 3.1 proves completeness. □

The compact fibre in (4.5) and the speed identity (4.2) are the two features that prevent this coupled equation from escaping. For a general affine connection they are unavailable. Geodesic completeness alone must therefore not be used to assert arbitrary prescribed-development existence for that connection.

## 5. Local isometries become coverings

A **local isometry** \(F:(N,h)\to(M,g)\) in this section has equal-dimensional source and target, is a local diffeomorphism, and satisfies \(F^*g=h\). A **covering map** is a surjective map such that each point has an open neighbourhood \(V\) whose inverse image is a disjoint union of open sets, each mapped homeomorphically onto \(V\). For a smooth local isometry these restrictions are smooth isometries.

**Theorem 5.1 (complete local isometries).** Let \(N\) and \(M\) be nonempty and connected, and let \(F:(N,h)\to(M,g)\) be a local isometry.

1. If \(N\) is complete, then \(M\) is complete and \(F\) is a surjective covering map.
2. If \(F\) is a covering map and \(M\) is complete, then \(N\) is complete.

**Proof.** First suppose \(N\) is complete. Fix \(\widetilde p\in N\), and put \(p=F(\widetilde p)\). Every vector \(v\in T_pM\) is the image of a unique vector \(\widetilde v\in T_{\widetilde p}N\). The geodesic in \(N\) with that initial vector exists for all times. Its image is the geodesic in \(M\) with initial vector \(v\), by Riemannian connections and convex neighbourhoods, Proposition 2.2. Thus \(M\) is geodesically complete at this one point \(p\). Theorem 3.1 makes it complete everywhere.

To prove surjectivity, join \(p\) to any \(q\in M\) by a minimizing geodesic, parametrized on \([0,1]\), with initial vector \(v\). The geodesic in \(N\) with initial vector \((dF_{\widetilde p})^{-1}v\) is defined through time one and maps to that segment. Its endpoint maps to \(q\).

We now prove the covering property. Fix any \(p\in M\), and choose \(r>0\) such that \(\exp_p\) is a diffeomorphism on its tangent ball of radius \(2r\). For each \(\widetilde p\in F^{-1}(p)\), geodesic naturality gives

\[
F\circ\exp_{\widetilde p}
=\exp_p\circ dF_{\widetilde p}.
\tag{5.1}
\]

On the tangent ball of radius \(2r\), the right-hand side is a diffeomorphism onto \(B_{2r}(p)\). Consequently \(\exp_{\widetilde p}\) is injective there. Its differential is invertible, because \(dF\) is invertible and the differential of their composition is invertible. It is a diffeomorphism onto its open image. The normal-ball theorem identifies that image with \(B_{2r}(\widetilde p)\). Equation (5.1) therefore makes

\[
F:B_r(\widetilde p)\longrightarrow B_r(p)
\tag{5.2}
\]

a diffeomorphism and a local isometry.

These balls exhaust \(F^{-1}(B_r(p))\). Indeed, if \(F(\widetilde q)=q\in B_r(p)\), take the reversed radial minimizing geodesic from \(q\) to \(p\). Launch its lift from \(\widetilde q\) with the unique corresponding initial velocity. Completeness of \(N\) defines this lifted geodesic through its full length, and naturality maps it to the chosen radial segment. It ends at some \(\widetilde p\in F^{-1}(p)\) and has length \(d(p,q)<r\). Hence \(\widetilde q\in B_r(\widetilde p)\).

The balls in (5.2) are disjoint. If two meet at \(\widetilde q\), the triangle inequality gives

\[
d_h(\widetilde p,\widetilde p')<2r.
\]

Thus \(\widetilde p'\in B_{2r}(\widetilde p)\), where (5.1) makes \(F\) injective. Since both centres map to \(p\), they coincide. This proves the covering property.

Conversely suppose \(F\) is a covering and \(M\) is complete. We recall why a path on a compact interval has a unique lift after its initial point is fixed. The inverse images in the interval of evenly covered neighbourhoods form an open cover. There is a finite subdivision such that each closed subinterval maps into one of those neighbourhoods. To justify the subdivision, a finite open cover of a compact interval has a positive Lebesgue number: otherwise intervals of length tending to zero, contained in no cover member, have points with a convergent subsequence; a neighbourhood of the limit lying in one cover member gives a contradiction. Subdivide more finely than this number. On the first piece use the inverse of the sheet containing the initial point; on each subsequent piece use the sheet containing the endpoint already reached. These lifts agree at the breaks. Local sheet inverses also prove uniqueness.

Given initial data in \(N\), the corresponding geodesic in \(M\) exists on all of \(\mathbb R\). Lift it on every interval \([-k,k]\) with the specified point over time zero, applying the preceding construction in both directions from zero. Uniqueness makes these lifts agree. Each lift is smooth and a geodesic, since the local sheet inverse is a local isometry. Their union is a geodesic in \(N\) on all of \(\mathbb R\) with the specified initial data. Hence \(N\) is complete. □

Completeness of the source is essential in the first assertion. The inclusion of an open Euclidean ball into Euclidean space is a local isometry with a proper open image.

**Corollary 5.2 (compact immersions of equal dimension).** A smooth immersion from a nonempty connected compact manifold \(N\) to a connected manifold \(M\) of the same dimension is a covering map onto \(M\), and \(M\) is compact.

**Proof.** Choose a Riemannian metric \(g\) on \(M\), whose existence is proved in Linear and affine connections, Theorem 2.1. The pullback \(F^*g\) is positive definite because the equal-dimensional immersion has invertible differential. Local inversion makes \(F\) a local isometry for this pullback metric. Its source is complete by Corollary 3.2. Theorem 5.1 proves that it is a covering onto \(M\). The image of compact \(N\) is compact, so \(M\) is compact. □

**Corollary 5.3 (open isometry orbits).** If an orbit of a group of isometries of connected \(M\) contains a nonempty open subset, then that orbit is all of \(M\).

**Proof.** Let \(O\) be that orbit. Translate its open subset by group elements to see that every point of \(O\) has a neighbourhood contained in \(O\); thus \(O\) is open. Let \(C\) be one connected component of \(O\). It is open, because \(O\) is a manifold. For \(x,y\in C\) choose a group element sending \(x\) to \(y\). It maps \(O\) onto itself and its components onto components. The image of \(C\) is the component containing \(y\), namely \(C\). Hence its restriction is an isometry of \(C\), and \(C\) is homogeneous. Corollary 3.3 makes \(C\) complete. Its inclusion into \(M\) is a local isometry, so Theorem 5.1 makes that inclusion surjective. Therefore \(C=M\) and \(O=M\). □

**Proposition 5.4 (closed pieces of a submanifold).** Suppose \(M\) is complete and \(N\subset M\) is an embedded submanifold with its induced metric. Assume that every point of \(M\) has an open neighbourhood \(U\) such that every connected component of \(N\cap U\) is closed in \(U\). Then each component of \(N\) is complete. In particular, a closed embedded submanifold of a complete Riemannian manifold is complete for its intrinsic metric.

**Proof.** Work on a connected component of \(N\). Its intrinsic distance \(d_N\) can exceed the ambient distance, but

\[
d_M(x,y)\le d_N(x,y),
\tag{5.3}
\]

because every path in \(N\) is a competing ambient path of the same length.

If a unit-speed intrinsic geodesic \(\gamma\) has a finite maximal endpoint \(b\), then (5.3) makes \(\gamma(t)\), as \(t\uparrow b\), Cauchy in \(M\). Let its ambient limit be \(x\). Choose the neighbourhood \(U\) at \(x\) from the hypothesis. The whole tail lies in \(U\); being connected, it lies in one connected component \(C\) of \(N\cap U\). Closedness of \(C\) in \(U\) gives \(x\in C\). The embedded submanifold topology is the subspace topology, so the tail converges to \(x\) in \(N\) too. Lemma 1.2, applied to the induced metric on \(N\), extends this intrinsic geodesic beyond \(b\). Time reversal treats a lower endpoint, proving completeness.

If \(N\) is closed in \(M\), then \(N\cap U\) is closed in \(U\), and its connected components are closed there as well. This proves the final assertion. □

Intrinsic geodesics of a submanifold need not be ambient geodesics. For example, a round circle in the Euclidean plane is intrinsically complete, although its nonconstant geodesics have nonzero ambient acceleration.

*References:* [Wilkins, Theorem 7.3] proves the complete-local-isometry covering theorem.

## 6. Finite and infinite distance to a missing boundary

### The punctured plane

Give \(M=\mathbb R^2\setminus\{0\}\) its Euclidean metric. The points

\[
q_j=(1/j,0)
\]

form a Cauchy sequence. The straight segment between two of them stays on the positive horizontal axis, and Euclidean displacement is a lower bound for any path length. Therefore

\[
d(q_j,q_k)=|1/j-1/k|.
\tag{6.1}
\]

They have no limit in \(M\): convergence in the Riemannian distance would imply convergence in the manifold topology, while their only Euclidean limit is the removed origin.

The set \(\{q_j:j\ge1\}\) is closed in \(M\). Its only additional accumulation point in \(\mathbb R^2\) is zero, which is absent. It is bounded by (6.1), and is not compact because its displayed sequence has no convergent subsequence in \(M\). This witnesses the failure of properness.

Geodesic incompleteness is equally explicit. The path

\[
\gamma(t)=(1-t,0),\qquad t<1,
\tag{6.2}
\]

is a unit-speed geodesic, since the Euclidean Levi-Civita coefficients vanish. It cannot extend continuously through \(t=1\) in \(M\). All three failures are the same obstruction seen through Theorem 3.1.

Riemannian connections and convex neighbourhoods, Exercise 6.4, proves a further effect of this puncture: the distance from \((-1,0)\) to \((1,0)\) is two, but no path of length two exists. A sequence of shorter and shorter detours has an infimum without a minimizing path.

### Hyperbolic space

For \(n\ge2\), let

\[
\begin{gathered}
\mathbb H^n=\mathbb R^{n-1}\times(0,\infty),\\
g=\frac{|dx|^2+dz^2}{z^2}.
\end{gathered}
\tag{6.3}
\]

Although the plane \(z=0\) is missing, it is infinitely far away in this metric. For every path from height \(z_0\) to height \(z_1\),

\[
L_g(\eta)\ge
\left|\log(z_1/z_0)\right|,
\tag{6.4}
\]

by integrating \(|z'|/z\). This is proved, including its equality case, in Riemannian connections and convex neighbourhoods, Section 5. In particular no finite-length path can approach height zero.

There are several concrete ways to prove completeness. The maps

\[
\begin{gathered}
(x,z)\longmapsto(ax+b,az),\\
a>0,\quad b\in\mathbb R^{n-1},
\end{gathered}
\tag{6.5}
\]

preserve (6.3): their differential multiplies Euclidean lengths by \(a\), and their new height is \(az\). They act transitively, since the map with \(a=z\) and \(b=x\) takes \((0,1)\) to \((x,z)\). Corollary 3.3 proves completeness. The previous lesson's explicit vertical exponential and semicircle formulas also give every geodesic for all real times.

We can see compactness of distance balls directly as well. Fix \((x_0,z_0)\) and let \(d((x_0,z_0),(x,z))\le R\). For every \(\varepsilon>0\) take a path of length less than \(R+\varepsilon\). Inequality (6.4) on each initial subpath bounds its height by \(z_0e^{R+\varepsilon}\), and bounds the endpoint height below by \(z_0e^{-(R+\varepsilon)}\). Also

\[
\begin{aligned}
|x-x_0|
&\le\int |x'|\,dt\\
&\le z_0e^{R+\varepsilon}
       \int\frac{|x'|}{z}\,dt\\
&\le z_0e^{R+\varepsilon}(R+\varepsilon).
\end{aligned}
\]

Letting \(\varepsilon\downarrow0\) shows that the closed distance ball lies in the Euclidean compact set

\[
\begin{gathered}
|x-x_0|\le z_0 R e^R,\\
z_0e^{-R}\le z\le z_0e^R.
\end{gathered}
\tag{6.6}
\]

This compact set is contained in the upper half-space. The distance ball is closed in its manifold, hence Euclidean, topology, so it is compact. This proves properness without starting from geodesic completeness.

### An affine connection on a complete metric space

Theorem 3.1 concerns the connection selected by \(g\). An arbitrary affine connection on the same manifold can be incomplete. On the Euclidean line take

\[
\nabla_{\partial_x}\partial_x=\partial_x.
\]

Its geodesic equation is \(x''+(x')^2=0\). With \(x(0)=0\), \(x'(0)=1\), its solution is

\[
\begin{gathered}
x(t)=\log(1+t),\\
-1<t<\infty.
\end{gathered}
\tag{6.7}
\]

Direct differentiation verifies the equation. The solution cannot extend through \(t=-1\), where its position tends to \(-\infty\). The Euclidean distance on \(\mathbb R\) is complete, but this connection is not its Levi-Civita connection. This example also appears, with its full initial-value calculation, in Geodesics, normal coordinates and curvature, Exercise 6.3.

An indefinite metric has a further difficulty: null vectors can have zero metric square while being nonzero. Neither the positive speed bound in Lemma 1.2 nor a Riemannian distance construction is then available. No indefinite version of the completeness equivalences is asserted here.

### Clifton's half-cylinder: a metric connection with torsion

*This subsection adapts Jacob W. Erickson and Benjamin McKay, [Inequivalence of the various notions of completeness for Cartan geometries](https://arxiv.org/abs/2606.00354v1), Section 4.1, under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). They present an example due to Yeaton H. Clifton on a half-cylinder, replacing his punctured-plane presentation. The coframe and geodesic-completeness argument are retained; the linear connection, torsion, scalar-ODE argument and finite \(C^1\) development below are made explicit here. This subsection retains CC BY 4.0.*

Let

\[
\begin{gathered}
C=(\mathbb R/\mathbb Z)\times(0,\infty),\\
g=dx^2+dy^2,\\
R(\theta)=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix},\\
\upsilon=R(1/y)\binom{dx}{dy}.
\end{gathered}
\tag{6.8}
\]

The coordinate \(x\) is read modulo one. The translation charts of this circle make \(dx\), \(\partial_x\) and (6.8) well defined. Let \(e_1,e_2\) be the frame dual to the coframe \(\upsilon\). Its matrix in the coordinate frame is \(R(-1/y)\), so it is orthonormal. Define a connection by declaring this global frame parallel:

\[
\begin{gathered}
\nabla_X(V^1e_1+V^2e_2)\\
=X(V^1)e_1+X(V^2)e_2.
\end{gathered}
\tag{6.9}
\]

Differentiating the Euclidean inner product of the coefficient vectors proves \(\nabla g=0\). Thus parallel transport for this connection preserves the metric. But it is not the Levi-Civita connection.

Indeed put \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\). If \(B=R(-1/y)\) is the frame matrix, its coordinate connection matrix is

\[
\begin{aligned}
A&=-dB\,B^{-1}\\
&=J\,d(1/y)\\
&=-y^{-2}J\,dy.
\end{aligned}
\tag{6.10}
\]

This follows by differentiating \(\nabla e_i=0\), namely \(dB+AB=0\). Hence

\[
\begin{aligned}
\nabla_{\partial_x}\partial_y&=0,\\
\nabla_{\partial_y}\partial_x&=-y^{-2}\partial_y,\\
T(\partial_x,\partial_y)&=y^{-2}\partial_y.
\end{aligned}
\tag{6.11}
\]

The torsion is nonzero. The connection is flat as well: its global parallel frame gives \(\nabla_X\nabla_Y e_i-\nabla_Y\nabla_X e_i-\nabla_{[X,Y]}e_i=0\), and curvature is tensorial.

The metric \(g\) is incomplete. The sequence \(([0],1/j)\) is Cauchy, since a vertical segment has length \(|1/j-1/k|\); this is also a lower bound by its height displacement. Its only possible limiting height is zero, outside \(C\).

Nevertheless all geodesics of (6.9) are complete. Their velocity coefficients in the parallel frame are constant, so, for some \(v=(a,b)\),

\[
\begin{gathered}
\binom{x'}{y'}=R(-1/y)v,\\
y'=-a\sin(1/y)+b\cos(1/y).
\end{gathered}
\tag{6.12}
\]

Erickson and McKay explain the mechanism: “all of the exponential curves for the geometry have \(y\)-components bounded away from \(0\)”. Here their exponential curves are exactly these geodesics. We give the full scalar argument.

If \(v=0\), the curve is constant. Otherwise the scalar function

\[
f(y)=-a\sin(1/y)+b\cos(1/y)
\]

has positive zeros tending to zero: a nonzero linear combination of sine and cosine has zeros at angles differing by \(\pi\), and their positive reciprocal angles tend to zero. For an initial height \(y_0>0\), choose such a zero \(y_*<y_0\). The constant solution \(y=y_*\) of \(y'=f(y)\) cannot meet another solution at a finite time, by uniqueness for this smooth scalar ODE. Continuity prevents crossing without meeting. Thus the height of the geodesic stays above \(y_*\) in both time directions.

Equation (6.12) also gives \(|x'|\le |v|\) and \(|y'|\le |v|\). On any bounded time interval its height is bounded above and below by positive constants. Its position stays in a compact slab of the cylinder, and its smooth first-order vector field in (6.12) has a uniform existence time there. The continuation theorem therefore excludes a finite maximal endpoint in either direction. This proves geodesic completeness for \(\nabla\).

There is even a prescribed \(C^1\) development that cannot be realized through its finite endpoint. Set \(p=([0],1)\), take \(u_0=(e_1(p),e_2(p))\), and consider

\[
\gamma(t)=([0],(1-t)^2),\qquad 0\le t<1.
\]

Its parallel frame is \(u(t)=(e_1(\gamma(t)),e_2(\gamma(t)))\), by (6.9). Define

\[
\begin{gathered}
\delta(t)=u_0\int_0^t w(s)\,ds,\\
w(s)=R(\theta(s))\binom{0}{-2(1-s)},\\
\theta(s)=(1-s)^{-2}.
\end{gathered}
\tag{6.13}
\]

The integrand has norm \(2(1-s)\), so it extends continuously by zero at \(s=1\). Its integral defines a \(C^1\) curve on the closed interval \([0,1]\), with \(\delta'(1)=0\). Equation (4.1) verifies that it is the development of \(\gamma\) on \([0,1)\). Any realization with the same initial point agrees with this one on that interval, by local uniqueness of the development equations. It cannot have an endpoint in \(C\), since its height tends to zero.

Thus geodesic completeness for a metric-compatible connection with torsion need not imply metric completeness or the prescribed-development conclusion. The torsion-free hypothesis that singles out the Levi-Civita connection is essential to those implications.

## 7. Exercises and complete solutions

### Exercise 7.1 (easy): a line with a finite end

On \(\mathbb R\), give the coordinate \(x\) the metric \(g=e^{2x}\,dx^2\). Find the distance, all affinely parametrized geodesics and their maximal domains. Determine completeness.

**Solution.** The coordinate \(r=e^x\) is a diffeomorphism from \(\mathbb R\) to \((0,\infty)\), and \(dr^2=e^{2x}dx^2\). Thus it is an isometry to the positive Euclidean half-line. The straight segment between two positive values stays positive, giving

\[
d_g(x,y)=|e^x-e^y|.
\tag{7.1}
\]

Euclidean geodesics in that coordinate are \(r(t)=r_0+ct\), so all the original geodesics are

\[
x(t)=\log(r_0+ct),\qquad r_0>0,
\tag{7.2}
\]

on the maximal interval where \(r_0+ct>0\). If \(c=0\), this interval is \(\mathbb R\). If \(c>0\), it is \((-r_0/c,\infty)\); if \(c<0\), it is \((-\infty,-r_0/c)\). With initial coordinate velocity \(v_0\), \(c=e^{x_0}v_0\) and \(r_0=e^{x_0}\).

For a coordinate check, the one-dimensional Levi-Civita formula gives \(\Gamma^x_{xx}=1\), and (7.2) satisfies \(x''+(x')^2=0\). This is the same equation as (6.7), but here it belongs to a different, incomplete metric.

The sequence \(x_j=-\log j\) has \(e^{x_j}=1/j\), so (7.1) makes it Cauchy. It cannot converge to any real \(x\), since that would require \(e^x=0\). The metric is incomplete, consistently with the finite endpoints in (7.2). □

### Exercise 7.2 (medium): enlarging a complete metric

Let \(g\) and \(h\) be smooth Riemannian metrics on the same connected manifold. Assume that \(h\) is complete and that some constant \(c>0\) satisfies \(g(v,v)\ge c^2h(v,v)\) for every tangent vector. Prove that \(g\) is complete. Decide whether a uniform upper bound for \(g\) in terms of \(h\) is needed.

**Solution.** For every piecewise \(C^1\) path, \(L_g\ge cL_h\); taking infima gives

\[
d_g(x,y)\ge c\,d_h(x,y).
\tag{7.3}
\]

A \(d_g\)-Cauchy sequence is therefore \(d_h\)-Cauchy. Completeness of \(h\) gives a limit \(x\) in the \(h\)-distance. Both distances induce the manifold topology, by Riemannian connections and convex neighbourhoods, Proposition 1.1. Convergence in \(d_h\) is thus convergence in that topology and hence in \(d_g\). This proves completeness of \(g\).

No global upper bound is needed. For example, on the line \(h=dx^2\) and \(g=(1+x^2)^2dx^2\) satisfy the lower bound with \(c=1\), while \(g/h=(1+x^2)^2\) is unbounded. The preceding proof still applies. Its use of the common local topology is what supplies convergence in the larger metric. □

### Exercise 7.3 (medium): the shortest route on a flat cylinder

For \(\ell>0\), form \(C=\mathbb R\times(\mathbb R/\ell\mathbb Z)\), with the metric descended from \(dx^2+dy^2\). Prove completeness. For representatives \(y_0,y_1\), write \(p_i=(x_i,[y_i])\) and show that

\[
\begin{gathered}
d_C(p_0,p_1)
=\min_{k\in\mathbb Z}\sqrt{\Delta x^2+\Delta y_k^2},\\
\Delta x=x_1-x_0,\\
\Delta y_k=y_1-y_0+k\ell.
\end{gathered}
\tag{7.4}
\]

Determine when the minimizing geodesic is unique.

**Solution.** The circle factor is the quotient of the line by translations by \(\ell\). An interval of length less than \(\ell\) gives a coordinate neighbourhood on it; transition functions are translations. These charts make the metric well defined. They also show that

\[
P:\mathbb R^2\to C,\qquad
P(x,y)=(x,[y])
\]

is a covering local isometry: take a circle interval shorter than \(\ell\); its inverse image consists of its disjoint translates. Euclidean geodesics are lines existing for all times, so \(\mathbb R^2\) is complete. Theorem 5.1 gives completeness of \(C\).

Lift any competing path to \(\mathbb R^2\), starting at \((x_0,y_0)\), using the path-lifting proof in Theorem 5.1. Its endpoint is \((x_1,y_1+k\ell)\) for some integer \(k\), and its length is unchanged by the local isometry. Euclidean displacement bounds that length below by the corresponding quantity in (7.4).

Conversely each straight segment to one of these lifted endpoints projects to a geodesic of exactly that length. The quantity tends to infinity as \(|k|\to\infty\), so its infimum over the integers is a minimum. This proves (7.4).

The minimizing integers are precisely those making \(|y_1-y_0+k\ell|\) smallest. There is one such integer unless \(y_1-y_0\) is congruent to \(\ell/2\) modulo \(\ell\); in that case there are two, with opposite angular displacements \(\ell/2\) and \(-\ell/2\).

For each integer the Euclidean minimizing affine segment is unique. Indeed equality between length and displacement forces its velocity to be a nonnegative multiple of that displacement; constant speed then fixes its affine parametrization. A minimizing geodesic in \(C\) lifts to one of these segments, because its length equals the minimum in (7.4). Hence there is one minimizing geodesic, or exactly two in the half-period case. This includes the constant path as the unique minimizer when the endpoints coincide. □

### Exercise 7.4 (hard): a metric that controls an exhaustion

Let \(h\) be a Riemannian metric on a connected manifold, and suppose a smooth function \(\rho:M\to[0,\infty)\) is proper: the inverse image of every compact set is compact. No completeness of \(h\) is assumed. Prove that

\[
g=(1+|d\rho|_h^2)\,h
\tag{7.5}
\]

is complete. Here \(|d\rho|_h\) is the norm of the covector for the inverse metric. Explain how \(\rho\) prevents a Cauchy sequence from escaping.

**Solution.** Put \(a=|d\rho|_h^2\). This is a smooth nonnegative function, so \(g\) is a smooth positive metric. The inverse metric scales by \((1+a)^{-1}\); hence

\[
|d\rho|_g^2=\frac{a}{1+a}\le1.
\tag{7.6}
\]

The covector–vector Cauchy–Schwarz inequality gives

\[
|(\rho\circ\eta)'|
\le |d\rho|_g\,|\eta'|_g
\le|\eta'|_g.
\]

Integrate on each smooth path piece and add. For every path from \(x\) to \(y\), its length bounds \(|\rho(y)-\rho(x)|\). Taking the infimum gives

\[
|\rho(y)-\rho(x)|\le d_g(x,y).
\tag{7.7}
\]

Let \((x_j)\) be \(d_g\)-Cauchy. Equation (7.7) makes \((\rho(x_j))\) Cauchy in \(\mathbb R\), hence bounded. Since \(\rho\ge0\), choose \(R\) containing all these values in \([0,R]\). Properness puts the whole sequence in the compact set \(\rho^{-1}([0,R])\). The manifold topology equals the \(g\)-distance topology, so it has a \(d_g\)-convergent subsequence. As in Theorem 3.1, the Cauchy property makes the whole sequence converge to the same point. Thus \(g\) is complete.

The argument does not assert that the original metric \(h\) is complete. It enlarges \(h\) precisely enough to make changes in the proper function cost length. A sequence escaping every compact set would have unbounded \(\rho\)-values, which (7.7) excludes for a Cauchy sequence. □

## References

[Erickson–McKay] J. W. Erickson and B. McKay, [*Inequivalence of the various notions of completeness for Cartan geometries*](https://arxiv.org/abs/2606.00354v1), arXiv:2606.00354v1, 29 May 2026, CC BY 4.0. Section 4.1 presents Clifton's half-cylinder and explains its completeness properties.

[Meinrenken] E. Meinrenken, [*Riemannian Geometry*](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf), lecture notes, University of Toronto, Spring 2002. Section 17 treats radial minimization, Hopf–Rinow, compact distance balls and one-point completeness.

[Kunzinger–Steinbauer] M. Kunzinger and R. Steinbauer, [*Riemannian Geometry*](https://www.mat.univie.ac.at/~stein/teaching/courses/skripten/rg-2021-04-17.pdf), lecture notes for the fall term 2020, University of Vienna, dated 16 April 2021. Section 2.4 proves the completeness equivalences; Sections 2.2–2.3 discuss continuation and minimizing curves.

[Wilkins] D. R. Wilkins, [*A Course in Riemannian Geometry*](https://www.maths.tcd.ie/~dwilkins/Courses/425/RiemGeom.pdf), 2005. Section 7.1 proves that a complete local isometry is a surjective covering.

