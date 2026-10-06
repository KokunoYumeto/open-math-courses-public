# Riemannian connections and convex neighbourhoods

A metric determines lengths, its Levi-Civita derivative and locally minimizing paths. This lesson proves these constructions for positive and nondegenerate metrics with their distinct hypotheses, develops radial parallel frames and strong convexity, and works out the upper half-space and the exact convexity radius of the sphere. Every used result is proved here or in an exact earlier programme lesson, using freely accessible construction material.

## A. Metric derivatives and the induced distance

All manifolds are finite-dimensional, Hausdorff, second countable and without boundary. A pseudo-Riemannian metric is a smooth symmetric bilinear form on each tangent space with zero kernel. A Riemannian metric is additionally positive definite. We use the connection convention \(\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k\).

The free construction source is Peter W. Michor's exact [author manuscript, *Topics in Differential Geometry*, §§22.5 and 23.1–23.5](https://www.mat.univie.ac.at/~michor/dgbook.pdf). The programme proofs below supply every mathematical prerequisite: **Local** means [Local tools](local-tools-for-bundles-and-transport.md), **Linear** means [Linear and affine connections](linear-and-affine-connections.md), **Geo** means [Geodesics, normal coordinates and curvature](geodesics-normal-coordinates-and-curvature.md), and **PB** means [Principal bundles](principal-bundles-and-associated-bundles.md). We distinguish the indefinite-metric connection identities from distance arguments, which use a positive metric.

**Theorem A.1 (the connection selected by a nondegenerate metric).** Every smooth pseudo-Riemannian metric \(g\) has exactly one metric-compatible torsion-free connection. It is determined by
\[
\begin{split}
2g(\nabla_XY,Z)
={}&Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)\\
&-g(X,[Y,Z])+g(Y,[Z,X])+g(Z,[X,Y]).
\end{split}
\tag{A.1}
\]
Writing \(g_{ij}=g(\partial_i,\partial_j)\) and \(g^{ij}\) for its inverse matrix, its coordinate coefficients are
\[
\Gamma^k_{ij}
 =\frac12g^{kl}
   (\partial_i g_{jl}+\partial_j g_{il}-\partial_l g_{ij}).
\tag{A.2}
\]
Along any smooth curve,
\[
\frac d{dt}g(V,W)=g(D_tV,W)+g(V,D_tW).
\tag{A.3}
\]
Parallel transport therefore preserves \(g\). On every affinely parametrized geodesic \(g(\dot\gamma,\dot\gamma)\) is constant; for positive \(g\), speed is constant as well.

**Proof.** The complete positive-metric proof is DG-CHAR-17 V.1. We give the extension and the coordinate consequences explicitly. Let \(K(X,Y,Z)\) denote the right side of (A.1). The bracket product rules proved in PB C.3 give
\[
\begin{aligned}
K(fX,Y,Z)&=fK(X,Y,Z),\\
K(X,Y,fZ)&=fK(X,Y,Z),\\
K(X,fY,Z)&=fK(X,Y,Z)+2X(f)g(Y,Z).
\end{aligned}
\tag{A.4}
\]
The cancellations use symmetry, not positivity, of \(g\). In the first line the additional terms are
\[
\begin{split}
&Y(f)g(Z,X)-Z(f)g(X,Y)\\
&\quad+Z(f)g(Y,X)-Y(f)g(Z,X)=0.
\end{split}
\]
In the second they are
\[
\begin{split}
&X(f)g(Y,Z)+Y(f)g(Z,X)\\
&\quad-Y(f)g(X,Z)-X(f)g(Y,Z)=0.
\end{split}
\]
In the third the two \(X(f)g(Y,Z)\) terms remain and the two \(Z(f)g(X,Y)\) terms cancel. Additivity and real scalar linearity follow directly from the defining expression.

Thus \(K(X,Y,\cdot)/2\) is a smooth covector: expand its last argument in any local frame and use the second identity of (A.4). Nondegeneracy says that the matrix \(g_{ij}\) is invertible, and Local 0.4 proves that its inverse is smooth. There is therefore a unique smooth vector field \(\nabla_XY\) with all the pairings (A.1). The first and third identities of (A.4), followed by nondegeneracy, give its connection axioms. The formula is intrinsic, so the local constructions agree.

Adding \(K(X,Y,Z)\) and \(K(X,Z,Y)\) cancels all terms except \(2Xg(Y,Z)\), proving metric compatibility. Subtracting \(K(Y,X,Z)\) from \(K(X,Y,Z)\) leaves \(2g([X,Y],Z)\), proving zero torsion. Conversely, for any compatible torsion-free derivative, add the metric identities in directions \(X,Y\) and subtract the one in direction \(Z\). Replace \(\nabla_YX\), \(\nabla_ZX\) and \(\nabla_ZY\) using zero torsion. The result is (A.1), so nondegeneracy proves uniqueness. None of these steps uses a sign for \(g(V,V)\).

For coordinate vector fields the brackets vanish by PB C.3. Formula (A.1) then gives
\[
2g_{lk}\Gamma^k_{ij}
 =\partial_i g_{jl}+\partial_j g_{il}-\partial_l g_{ij}.
\]
Multiplication by the inverse metric proves (A.2), whose lower indices are symmetric.

For fields along a curve, the derivative along maps in Linear B.2 and the tensor product rule in Linear C.1 pull the metric-compatibility identity back to the parameter interval. In coordinates this just differentiates \(g_{ij}(\gamma)V^iW^j\); the derivatives of \(g_{ij}\) are replaced by their compatibility formula and give the two connection corrections in (A.3). Parallel fields make its right side zero; Local 0.3 then gives constancy, also across the finitely many pieces of a piecewise smooth path. Linear A.2 supplies the full parallel transport. Finally \(D_t\dot\gamma=0\) gives constancy of its squared \(g\)-speed by (A.3). If \(g\) is positive, taking the nonnegative square root gives constant speed. In indefinite signature the constant may be negative or zero, so no distance assertion follows from this identity alone. □

**Theorem A.2 (length, distance and topology).** Let \(g\) be Riemannian. For a continuous piecewise \(C^1\) curve \(\eta:[a,b]\to M\), with finitely many pieces, define
\[
L_g(\eta)=\int_a^b
 \sqrt{g_{\eta(t)}(\dot\eta(t),\dot\eta(t))}\,dt
\tag{A.5}
\]
by summing the integrals on those pieces. On each connected component set
\[
d_g(p,q)=\inf_{\eta:p\to q} L_g(\eta).
\tag{A.6}
\]
This is a finite metric and induces the manifold topology. A sufficiently small coordinate ball around \(p\), with coordinates \(x(p)=0\), admits constants \(0<c\leq C\) such that
\[
c|x(q)|\leq d_g(p,q)\leq C|x(q)|
\tag{A.7}
\]
for every \(q\) in that ball. Points in different components may be assigned distance \(+\infty\), giving an extended metric on all of \(M\).

**Proof.** Smoothness of the metric and piecewise continuity of the velocity make the nonnegative integrand continuous on each piece, including its one-sided endpoint values. The integral exists by Local 0.3. Additivity under subdivision and concatenation follows by splitting integrals. The substitution rule follows from that same lemma: if \(F'=f\) and \(\phi\) is \(C^1\), integrate \((F\circ\phi)'=(f\circ\phi)\phi'\). This also proves length invariance under orientation reversal. An increasing \(C^1\) change of parameter multiplies the speed by its nonnegative derivative, so substitution preserves length. The same proof on finitely many pieces permits an increasing piecewise \(C^1\) bijection, including points where its derivative is zero.

Fix a coordinate chart and a closed coordinate ball \(\overline B(0,r)\) contained in it. On the product of that ball with the Euclidean unit sphere, the continuous function
\((x,v)\mapsto g_x(v,v)\) has a positive minimum and a finite maximum, by Local 0.1. Its minimum is positive because every value is positive. By homogeneity there are \(c,C>0\) with
\[
c|v|\leq |v|_{g_x}\leq C|v|
\qquad (x\in\overline B(0,r)).
\tag{A.8}
\]
The positive square roots exist by the real completeness properties in Local 0.0. In dimension zero use singleton charts and the unique constant curves instead.

For any curve segment contained in this coordinate ball, the fundamental theorem gives
\[
L_g(\eta)\geq c\int|\dot x(t)|\,dt
 \geq c\,|x(b)-x(a)|.
\tag{A.9}
\]
For the last inequality, if the displacement is nonzero take its Euclidean unit direction \(e\). Then
\(|x(b)-x(a)|=\int e\cdot\dot x\,dt\leq\int|\dot x|\,dt\).
The pointwise bound \(e\cdot w\leq|w|\) follows by expanding
\(|w-(e\cdot w)e|^2\geq0\). Zero displacement is immediate.

A curve starting at the centre that reaches the complement of \(B(0,r)\) has an initial segment ending on its coordinate sphere and lying in the closed ball. Here the sphere is interpreted inside the larger chart, so it is a compact subset of \(M\). To justify the assertion, let \(t_*\) be the supremum of times up to which the curve stays in the open ball. Continuity gives \(t_*>a\), where \(a\) is the starting time. Continuity and compactness put its value in the closed ball; if it were in the interior, continuity would extend the interval, while an endpoint outside the closed ball cannot be a limit of these values. Thus it lies on the sphere. Equivalently one can use the first hitting time of this compact boundary. Applying (A.9) to that initial segment gives length at least \(cr\). The same reasoning applies if the final point lies back in the open ball after an excursion.

For \(q\in B(0,r)\), a curve from \(p\) to \(q\) that stays in the ball has length at least \(c|x(q)|\), by (A.9). A curve that leaves it has length at least \(cr>c|x(q)|\). Conversely the straight coordinate segment lies in the ball and has length at most \(C|x(q)|\), by (A.8). Taking infima proves (A.7). Moreover every \(q\) outside the open ball in the same connected component has \(d_g(p,q)\geq cr\).

Every two points of a connected component can be joined by a finite concatenation of straight segments in charts. To prove this, fix a point and consider its set of reachable points by such paths. A small coordinate ball about any reachable point is reachable by adding a segment, so this set is open. The same statement holds for each reachability class; hence its complement, a union of the other classes, is open. Connectedness forces a single class. Such a finite path has finite length, so (A.6) is finite.

Nonnegativity, symmetry and \(d_g(p,p)=0\) follow from length and constant curves. If \(p\ne q\), choose the preceding ball about \(p\) so small that it does not contain \(q\); the exit bound gives \(d_g(p,q)\geq cr>0\). For the triangle inequality choose curves of lengths less than \(d_g(p,q)+\epsilon\) and \(d_g(q,z)+\epsilon\), concatenate them and let \(\epsilon\downarrow0\). The infimum property from Local 0.0 justifies these choices. Thus this is a metric.

Finally the upper bound in (A.7) makes points sufficiently close in coordinates lie in any given distance ball about \(p\). Conversely the exit bound puts the distance ball of radius \(cr\) inside the chosen coordinate ball. Since the latter can be chosen inside any prescribed manifold neighbourhood, the two neighbourhood systems coincide. The arguments apply separately to each component and give the stated extended-metric convention. □

**Theorem A.3 (what a local isometry preserves).** Let \(F:(M,g)\to(N,h)\) be a smooth map between pseudo-Riemannian manifolds of the same dimension, with \(F^*h=g\). It is a local diffeomorphism and preserves their Levi-Civita connections, parallel transport along paths and affinely parametrized geodesics. For positive metrics it also preserves lengths of curves. A globally defined such map satisfies
\[
d_h(Fp,Fq)\leq d_g(p,q)
\tag{A.10}
\]
on each component. A global isometry has equality.

**Proof.** If \(dF_pv=0\), then \(g_p(v,w)=h_{Fp}(dF_pv,dF_pw)=0\) for all \(w\), so \(v=0\). Equal dimensions make \(dF_p\) invertible; Local 1.2 makes \(F\) a diffeomorphism on a neighbourhood of each point. On such a neighbourhood define
\[
\widetilde\nabla_XY
 =(dF)^{-1}\bigl(\nabla^h_{F_*X}(F_*Y)\bigr).
\]
The derivative axioms and the ordinary chain rule give its connection axioms. Differentiating \(g(Y,Z)=h(F_*Y,F_*Z)\circ F\) shows metric compatibility. The bracket identity
\(F_*[X,Y]=[F_*X,F_*Y]\) follows by applying both sides to a function and using the commutator definition in PB C.3. Hence zero torsion for \(\nabla^h\) gives zero torsion for \(\widetilde\nabla\). A.1's uniqueness proves \(\widetilde\nabla=\nabla^g\). These local equalities agree on overlaps and express the global preservation assertion.

Pull this equality back to a curve using Linear B.2. It gives
\[
D_t^h(dF\,V)=dF(D_t^gV).
\tag{A.11}
\]
Thus \(dF\) takes parallel fields to parallel fields. Uniqueness of parallel transport, Linear A.2, identifies the endpoint transports. This is valid on an entire piecewise smooth path: compactness gives finitely many local-isometry charts and the identities compose across their endpoints. Setting \(V=\dot\gamma\) proves preservation of the geodesic equation and its parameter wherever the curve is defined. No equality of maximal existence intervals is asserted for a merely local isometry.

For positive metrics \(h(dF\dot\eta,dF\dot\eta)=g(\dot\eta,\dot\eta)\) gives equality of the integrands in (A.5), hence of lengths. Every path from \(p\) to \(q\) maps to a path from \(Fp\) to \(Fq\); taking infima proves (A.10). For a global isometry its smooth inverse is also an isometry, so applying the same inequality in reverse proves equality. □

**Exercise A.4 (all metric connections with the same parametrized geodesics).** Let \(g\) be pseudo-Riemannian and \(\nabla\) its Levi-Civita connection. For a smooth three-form \(H\), define \(K\) by
\[
g(K(X,Y),Z)=\tfrac12H(X,Y,Z).
\tag{A.12}
\]
Then \(\nabla'=\nabla+K\) is metric and has the same affinely parametrized geodesics. Its torsion satisfies
\[
\mathcal T'(X,Y)=2K(X,Y),\qquad
g(\mathcal T'(X,Y),Z)=H(X,Y,Z).
\tag{A.13}
\]
Every metric connection with these same parametrized geodesics arises from exactly one such \(H\).

**Solution.** Nondegeneracy and smooth inversion of the metric, as in A.1, make (A.12) a unique smooth bilinear tensor \(K\). Alternation of \(H\) in its first two positions makes \(K(X,Y)=-K(Y,X)\). Linear A.3 shows that adding this tensor gives a connection, and Geo A.3 proves equality of all its affinely parametrized geodesics, including their maximal domains.

The difference between the two metric-compatibility identities is
\[
g(K(X,Y),Z)+g(Y,K(X,Z))
 =\tfrac12H(X,Y,Z)+\tfrac12H(X,Z,Y)=0.
\]
Thus \(\nabla'\) is metric. Its torsion is the old zero torsion plus \(K(X,Y)-K(Y,X)=2K(X,Y)\), proving (A.13).

Conversely let \(\nabla'\) be metric with the same geodesics, and put \(K=\nabla'-\nabla\). Linear A.3 makes \(K\) a smooth tensor; Geo A.3 makes it skew in \(X,Y\). Subtracting metric compatibility makes \(B(X,Y,Z)=g(K(X,Y),Z)\) skew in \(Y,Z\) as well. These two adjacent transpositions generate all permutations of three positions: in particular exchanging the first and third is the composition of three adjacent exchanges and also changes the sign. Hence \(B\) is alternating in all three positions. Set \(H=2B\). It is a smooth three-form giving (A.12); its uniqueness follows directly from that formula. This converse uses no definiteness assumption. □

**Exercise A.5 (a variable transverse scale).** For a smooth function \(f:\mathbb R\to(0,\infty)\), put
\(g=dx^2+f(x)^2dy^2\). Its only possibly nonzero connection coefficients and its geodesic equations are
\[
\begin{gathered}
\Gamma^x_{yy}=-ff',\qquad
\Gamma^y_{xy}=\Gamma^y_{yx}=f'/f,\\
x''-f(x)f'(x)(y')^2=0,\qquad
y''+2\frac{f'(x)}{f(x)}x'y'=0.
\end{gathered}
\tag{A.14}
\]
For \(f(x)=e^x\), these become
\[
x''-e^{2x}(y')^2=0,\qquad y''+2x'y'=0.
\tag{A.15}
\]

**Solution.** The metric and inverse matrices are
\(\operatorname{diag}(1,f^2)\) and \(\operatorname{diag}(1,f^{-2})\).
Their only nonzero coefficient derivative is
\(\partial_xg_{yy}=2ff'\).
Substitute into (A.2). For the upper \(x\) component the only contribution is
\(-\tfrac12\partial_xg_{yy}=-ff'\) when both lower indices are \(y\). For the upper \(y\) component it is
\(\tfrac12f^{-2}\partial_xg_{yy}=f'/f\) when the lower indices are \(x,y\) in either order. All other terms are zero. Geo A.1's coordinate geodesic equation now gives (A.14), with the factor two coming from the two mixed lower-index orders. Geo A.4 constructs the positive real exponential and proves its derivative is itself. Thus \(f'=f=e^x\), and substitution gives (A.15). □

## B. Radial length and genuinely minimizing neighbourhoods

The free construction source for the Gauss identity and radial comparison is Michor's exact [author manuscript, §§23.1–23.5](https://www.mat.univie.ac.at/~michor/dgbook.pdf). We combine those arguments with the full programme proof of convex normal neighbourhoods, Geo B.3. In particular, uniqueness of a geodesic contained in a coordinate neighbourhood is supplemented below by a comparison with every competing path in the manifold.

**Theorem B.1 (Gauss's identity, including indefinite signature).** Let \(g\) be pseudo-Riemannian, and let \(\exp_p:\mathcal E_p\to M\) be the full exponential domain of its Levi-Civita connection. For every \(v\in\mathcal E_p\) and every \(w\in T_pM\),
\[
g_{\exp_pv}\bigl((d\exp_p)_v v,(d\exp_p)_v w\bigr)=g_p(v,w).
\tag{B.1}
\]
No injectivity or nonsingularity of \((d\exp_p)_v\) is required.

**Proof.** Geo A.1–A.2 prove that \(\mathcal E_p\) is open and star-shaped and that \(t\mapsto\exp_p(tu)\) is the geodesic of initial velocity \(u\). Fix \(v,w\). For all sufficiently small \(|s|\), \(v+sw\in\mathcal E_p\). The smooth map
\[
F(t,s)=\exp_p\bigl(t(v+sw)\bigr),\qquad 0\leq t\leq1,
\]
is consequently defined on the whole strip. Write \(T=\partial_tF\) and \(V=\partial_sF\) for vector fields along it. Along its \(t\)-curves \(D_tT=0\). Metric compatibility and A.1 give
\[
g(T,T)(t,s)=g_p(v+sw,v+sw).
\tag{B.2}
\]
Linear D.3's formula for torsion along a map gives \(D_tV=D_sT\), because the parameter fields commute and Levi-Civita torsion vanishes. That formula is valid also where \(F\) is not an immersion. Hence A.1's product identity gives
\[
\begin{split}
\partial_t g(T,V)
 &=g(T,D_tV)=g(T,D_sT)\\
 &=\tfrac12\partial_s g(T,T)=g_p(v+sw,w).
\end{split}
\tag{B.3}
\]
At \(t=0\), \(F(0,s)=p\), so \(V(0,s)=0\). Integrating (B.3) with Local 0.3 gives \(g(T,V)(1,0)=g_p(v,w)\). At \((1,0)\), the chain rule identifies \(T=(d\exp_p)_v v\) and \(V=(d\exp_p)_v w\), proving (B.1). This calculation used nondegeneracy only to obtain the Levi-Civita connection; it never replaced an indefinite quadratic form by a norm. □

**Lemma B.2 (radial comparison, including passages through the centre).** Now let \(g\) be positive definite. Suppose
\[
\exp_p:B_R(0)\subset T_pM\longrightarrow U
\tag{B.4}
\]
is a diffeomorphism, where the ball uses \(g_p\) and \(0<R<\infty\). For a continuous piecewise \(C^1\) path \(\eta:[a,b]\to U\), put
\[
u=\exp_p^{-1}\eta,\qquad r=|u|_{g_p}.
\]
Then for every subinterval \([\alpha,\beta]\subset[a,b]\),
\[
L_g(\eta|_{[\alpha,\beta]})\geq |r(\beta)-r(\alpha)|.
\tag{B.5}
\]
Where \(r>0\), write \(u=re\), \(|e|_{g_p}=1\). On each smooth piece,
\[
|\dot\eta|_g^2=(r')^2+
 \bigl|(d\exp_p)_{re}(r e')\bigr|_g^2.
\tag{B.6}
\]
The second term vanishes exactly when \(e'=0\).

**Proof.** On \(r>0\), the norm is smooth by the positive-square-root construction and inverse function theorem in DG-CHAR-17 D.2, or by applying Local 1.2 to \(t\mapsto t^2\) on \(t>0\). Differentiating \(g_p(e,e)=1\) gives \(g_p(e,e')=0\). At \(re\), B.1 gives
\[
|(d\exp_p)_{re}e|_g^2=1,\qquad
g\bigl((d\exp_p)_{re}e,(d\exp_p)_{re}(r e')\bigr)=0.
\]
For the first identity divide B.1 with \(v=w=re\) by \(r^2\); for the second use \(v=re,w=re'\) and divide by \(r\). The chain rule now proves (B.6). The differential in (B.4) is invertible, \(r>0\), and \(g\) is positive, so its second term is zero exactly when \(e'=0\). In particular speed is at least \(|r'|\).

If \(r\) has no zero on a closed subinterval, integrate this last inequality on its finitely many pieces; the fundamental theorem gives (B.5). If there are zeros, their set is compact by continuity. Between \(\alpha\) and the first zero \(s\), \(r\) is positive except possibly at \(\alpha=s\). Apply the already proved bound up to times tending to \(s\); continuity of \(r\) and of the accumulated length gives length at least \(r(\alpha)\). If \(s=\alpha\) that bound is zero and immediate. Between the last zero \(t\) and \(\beta\), the same argument gives length at least \(r(\beta)\). These two disjoint portions therefore give total length at least \(r(\alpha)+r(\beta)\), which is at least the absolute difference. This proves (B.5) without differentiating the norm at zero. Applying it to every interval in a finite partition also bounds the total radial variation on that partition by the full length. □

**Theorem B.3 (normal balls, global distance and equality).** Under (B.4), if \(q=\exp_pv\), \(r_0=|v|_{g_p}<R\), then
\[
d_g(p,q)=r_0,\qquad U=\{q\in M:d_g(p,q)<R\}.
\tag{B.7}
\]
Here distance is the extended metric of A.2. The radial geodesic \(t\mapsto\exp_p(tv)\), \(0\leq t\leq1\), is the unique affinely parametrized minimizing geodesic with these endpoints. Every continuous piecewise \(C^1\) path from \(p\) to \(q\) of length \(r_0\) follows this radial segment monotonically, possibly with pauses. Conversely every such piecewise \(C^1\) radial path is minimizing.

**Proof.** A.1 gives radial speed \(r_0\), so the radial segment has length \(r_0\). A competitor contained in \(U\) has length at least \(r_0\), by B.2.

To compare paths that leave \(U\), choose \(r_0<r_1<R\). The image \(K=\exp_p(\overline B_{r_1})\) is compact and is contained in \(U\). It is closed in the Hausdorff manifold; inside \(U\) its interior and boundary are the images of the open ball and its sphere, by (B.4). Thus the same descriptions hold in \(M\). Any continuous path starting at \(p\) that leaves this open image has an initial segment inside \(K\) ending on that sphere: the first-exit argument in A.2 applies to this coordinate ball. B.2 makes the length of that segment at least \(r_1>r_0\). A path that leaves \(U\) must first leave this smaller ball and therefore cannot be minimizing. All competitors have now been covered, proving \(d_g(p,q)=r_0\).

For a point outside \(U\) in the same connected component, the first-exit argument gives length at least \(r_1\) for every \(r_1<R\), along every path to it. Taking their infimum and then letting \(r_1\uparrow R\) gives distance at least \(R\). Points in other components have infinite distance. Together with the distance formula inside \(U\), this proves the set identity in (B.7).

Let \(\eta:[a,b]\to M\) have the stated endpoints and length \(r_0\). It stays in \(U\), by the strict exit estimate just proved. If \(r_0=0\), every subpath from \(p\) has length zero and A.2's positive distance forces \(\eta\) to be constant. Assume \(r_0>0\). For \(a\leq s\leq t\leq b\), subdivision and B.2 give
\[
r_0=L_g(\eta)\geq r(s)+|r(t)-r(s)|+|r_0-r(t)|.
\tag{B.8}
\]
Taking \(s=t\) first shows \(r(t)\leq r_0\). If \(r(s)>r(t)\), the right side of (B.8) is \(r_0+2(r(s)-r(t))>r_0\), a contradiction. Thus \(r\) is nondecreasing. On any \([s,t]\) the length is at least \(r(t)-r(s)\); the other two portions have total length at least \(r(s)+r_0-r(t)\). Equality of the full length consequently forces equality on this subinterval.

Where \(r>0\), on each smooth piece the continuous function \(|\dot\eta|_g-r'\) is nonnegative, by (B.6) and monotonicity. Its integral on every closed subinterval is zero, by the preceding equality. If it were positive at a point, continuity would give a positive integral on a small interval, so it is identically zero. Equation (B.6) now forces \(e'=0\). The positive set of the nondecreasing \(r\) is a terminal interval; the fundamental theorem and continuity across the finitely many corners make \(e\) constant throughout that interval. Its endpoint value is \(v/r_0\). Thus
\[
\eta(t)=\exp_p\bigl(r(t)v/r_0\bigr).
\tag{B.9}
\]
This includes any initial pause at \(p\). The scalar \(r\) is piecewise \(C^1\) even at that pause, because in (B.9) it equals the smooth linear functional \(u\mapsto g_p(u,v/r_0)\) applied to the piecewise \(C^1\) inverse-coordinate path \(u\). Conversely any nondecreasing piecewise \(C^1\) scalar \(r\) with endpoints \(0,r_0\) gives length \(\int r'=r_0\) in (B.9).

Finally a minimizing affine geodesic has constant speed by A.1, so its length on each interval is that speed times the parameter length. On \([0,1]\) the speed is \(r_0\), and the equality just proved gives \(r(t)=tr_0\). This identifies it with the stated radial geodesic, including the constant case. □

**Exercise B.4 (the exact cost of an outward excursion).** Let a path \(\eta:[a,b]\to U\) in (B.4) go from \(p\) to \(q=\exp_pv\), \(r_0=|v|_{g_p}\). If it visits radius \(\rho\) with \(r_0<\rho<R\), then
\[
L_g(\eta)\geq 2\rho-r_0.
\tag{B.10}
\]
This bound is sharp. If, on a smooth interval away from \(p\), its angular direction has nonzero derivative somewhere, the inequality is strict.

**Solution.** Split the path at a time at which \(r=\rho\). B.2 gives lengths at least \(\rho\) and \(\rho-r_0\), proving (B.10). A radial path out to \(\rho\) and then back to \(r_0\), in the direction of \(v\), attains the sum. For \(v=0\) use any unit vector; the assumed positive excursion implies positive dimension, so such a vector exists. This path has two smooth pieces.

For strictness choose a smaller closed interval \([s,t]\), away from the centre and from the finitely many corners, on which the angular derivative is nonzero at an interior point. Continuity and invertibility in (B.6) make
\(\delta=\int_s^t(|\dot\eta|_g-|r'|)>0\).
Insert \(s,t\) and the visiting time into a partition. On the pieces of \([s,t]\), speed integrates to the integral of \(|r'|\) plus this positive excess; outside it B.2 bounds length by the absolute radial increments. The sum of those absolute increments is at least \(2\rho-r_0\), by grouping the pieces before and after the visiting time and applying the real triangle inequality. Hence \(L_g(\eta)\geq2\rho-r_0+\delta\). □

**Theorem B.5 (arbitrarily small strong convexity and smooth squared distance).** Every point of a Riemannian manifold has arbitrarily small open neighbourhoods \(V\) such that each pair \(x,y\in V\) has a unique minimizing affine geodesic \([0,1]\to M\), and that geodesic lies in \(V\) and depends smoothly on \((x,y)\). Every other minimizing piecewise \(C^1\) path traces it monotonically. For each \(x\in V\), an open star-shaped neighbourhood \(W_x\subset T_xM\) is mapped diffeomorphically onto \(V\) by \(\exp_x\). The global squared distance is smooth on all of \(V\times V\), including its diagonal.

**Proof.** Dimension zero is immediate. Fix a point \(p\) and any prescribed neighbourhood. Geo B.1 supplies an endpoint inverse \(\Psi(x,v)=(x,\exp_xv)\) on an open set \(O\) about \((p,0)\) in a coordinate trivialization. Choose a smaller coordinate neighbourhood \(N_0\) with compact closure and a number \(a>0\) such that
\[
\{(x,v):x\in\overline N_0,\ |v|_{\rm coord}\leq a\}\subset O.
\tag{B.11}
\]
This is possible by taking a sufficiently small product about \((p,0)\) inside \(O\). Positivity and compactness as in A.2 give a uniform \(c>0\) with \(|v|_{g_x}\geq c|v|_{\rm coord}\) for \(x\in\overline N_0\). Fix \(0<\delta<ca\). For every \(x\in N_0\), the \(g_x\)-ball \(B_\delta(0)\) lies in the fibre of \(O\). The fibre-preserving diffeomorphism \(\Psi|_O\) therefore restricts to a diffeomorphism
\[
\exp_x:B_\delta(0)\longrightarrow U_x.
\tag{B.12}
\]
Indeed its restriction to a fibre has a smooth inverse and invertible differential, because both \(\Psi\) and its inverse preserve the first coordinate; its image is open in that fibre's target. B.3 applies to (B.12), with the same radius for all these \(x\).

Shrink a neighbourhood \(N_1\) of \(p\) so that \(N_1\subset N_0\), \(N_1\times N_1\subset\Psi(O)\), and the endpoint inverse \(v(x,y)\) satisfies \(|v(x,y)|_{g_x}<\delta\) there. This follows from openness, continuity and \(v(p,p)=0\). In the proof of Geo B.3, start with the endpoint neighbourhood restricted to \(O\) and use a coordinate chart contained in \(N_1\) and in the prescribed neighbourhood. That proof permits every one of these restrictions: its inverse neighbourhood is repeatedly shrunk about \((p,0)\), and its final radius is then chosen smaller. It gives an arbitrarily small \(V\subset N_1\) whose joining segment is exactly the inverse family \(\exp_x(tv(x,y))\), lies in \(V\), and is the unique contained affine segment. Its proof also supplies the asserted open star-shaped \(W_x\) and the smooth joining map.

For \(x,y\in V\), the same vector \(v(x,y)\) lies in \(B_\delta(0)\). B.3 applied at \(x\) shows that this segment minimizes among all paths in the manifold, is the unique minimizing affine geodesic there, and has the stated equality characterization. It also gives
\[
d_g(x,y)^2=g_x\bigl(v(x,y),v(x,y)\bigr).
\tag{B.13}
\]
The right side is a smooth function on \(V\times V\), since \(g\) and the endpoint inverse are smooth. At the diagonal \(v(x,x)=0\), so this formula proves smoothness there without differentiating a square root. No completeness or global existence of minimizing curves was assumed. □

**Exercise B.6 (a distance whose infimum is not attained).** In \(M=\mathbb R^2\setminus\{0\}\) with its Euclidean metric, let \(p=(-1,0)\), \(q=(1,0)\). Then \(d_g(p,q)=2\), but no piecewise \(C^1\) path attains this distance. This is consistent with B.5.

**Solution.** For any such path \((x(t),y(t))\), Local 0.3 gives
\[
L_g=\int\sqrt{x'^2+y'^2}\geq\int x'=2.
\]
For \(\epsilon>0\), use the three straight segments through
\[
(-1,0),\quad(-1,\epsilon),\quad(1,\epsilon),\quad(1,0).
\]
They avoid the removed origin and have lengths \(\epsilon,2,\epsilon\), respectively, by integrating their constant speeds. Their total \(2+2\epsilon\) tends to \(2\), proving the infimum.

If equality held, the continuous nonnegative function \(\sqrt{x'^2+y'^2}-x'\) on each smooth piece would have zero integral and would therefore vanish. It follows that \(y'=0\) and \(x'\geq0\) on every piece. The fundamental theorem and continuity at the corners give \(y=0\) on the full path. Continuity and Local 0.0's intermediate value theorem force \(x\) to pass through zero, contradicting the removed point. Finally a sufficiently small Euclidean ball about any point of \(M\) avoids zero; its straight segments are unique minimizing affine geodesics on \([0,1]\), by the same length inequality and its equality case. B.5 makes a local assertion of this kind and does not assert a minimizing path between arbitrary distant points. □

## C. Parallel frames along the radii

We use the frame and coframe identities in Michor's free [author manuscript, §§25.1–25.6](https://www.mat.univie.ac.at/~michor/dgbook.pdf), with their full programme proofs in Linear A.1–A.2, B.3 and D.1. These identities concern a moving orthonormal frame; they do not assume that it consists of coordinate vector fields.

**Theorem C.1 (a smooth radial frame and the polar metric).** Let \(g\) be Riemannian and \(E=\exp_p:B_R(0)\to U\) a normal ball. Choose an isometry \(e_0:\mathbb R^n\to T_pM\) to identify this ball with a Euclidean ball. Parallel transport of \(e_0\) along \(t\mapsto E(tx)\), \(0\leq t\leq1\), gives a smooth orthonormal frame \(e(E(x))\) on \(U\), including at \(p\). Pull its connection matrix and coframe back to \(B_R\), and denote them by \(A\) and \(\zeta\). Thus
\[
\zeta_x(v)=e(E(x))^{-1}(dE)_xv.
\tag{C.1}
\]
For the coordinate radial field \(\mathcal R_x=x\),
\[
A(\mathcal R)=0,\qquad \zeta(\mathcal R)=x,\qquad
A_0=0,\qquad \zeta_0=I.
\tag{C.2}
\]
In polar variables \(x=r\nu\), \(|\nu|=1\), \(r>0\), the pulled-back forms satisfy
\[
A(\partial_r)=0,\qquad
\zeta=\nu\,dr+\phi,\qquad
\phi(\partial_r)=0,\qquad \nu^T\phi=0.
\tag{C.3}
\]
Consequently the metric is
\[
E^*g=dr^2+\sum_{i=1}^n\phi^i\otimes\phi^i
\tag{C.4}
\]
on the polar domain. For \(n=1\) the two possible radial directions have no angular tangent vectors and the last sum is zero.

**Proof.** Linear A.2 and Connections C.1 supply the full parallel frame along each radial path. Connections C.2 proves its smooth dependence on the finite-dimensional parameter \(x\), including \(x=0\): the path family \((x,t)\mapsto E(tx)\) is smooth on a neighbourhood of every compact parameter segment. At zero it is the constant path, so the resulting frame equals \(e_0\). A.1 says that transport is an isometry, hence this frame is orthonormal everywhere.

Along any fixed ray, the frame just constructed is parallel as a function of the radial parameter. Indeed, the path to a point on the ray is the initial portion of the same radial geodesic, up to an increasing linear reparametrization. The concatenation and reparametrization identities of Connections C.2 identify its transported frame with the restriction of that parallel frame. The matrix equation of Linear A.2 then gives \(A_x(x)=0\). The velocity of \(t\mapsto E(tx)\) is itself parallel, with initial components \(x\) in \(e_0\). At \(t=1\) those components are still \(x\); this is \(\zeta_x(x)=x\).

For a fixed vector \(v\), the first identity at \(x=tv\), \(t\ne0\), gives \(A_{tv}(v)=0\). Smoothness and \(t\to0\) imply \(A_0(v)=0\). Geo B.1 gives \((dE)_0=e_0\) under the chosen identification, and therefore (C.1) gives \(\zeta_0=I\).

On the polar domain, \(\partial_r\) pushes to \(\nu\) in the ball, and a tangent vector \(W\) on the unit sphere pushes to \(rW(\nu)\). The two radial identities give \(A(\partial_r)=0\) and \(\zeta(\partial_r)=\nu\). Set \(\phi=\zeta-\nu\,dr\); it vanishes on \(\partial_r\). B.1 applied to \(r\nu\) and \(rW(\nu)\) shows that the corresponding radial and angular tangent vectors in \(M\) are perpendicular, because \(\nu\cdot W(\nu)=0\), obtained by differentiating \(|\nu|^2=1\). In the orthonormal frame this perpendicularity says \(\nu^T\phi(W)=0\). It also holds on \(\partial_r\), where \(\phi=0\), proving (C.3).

Orthonormality makes the metric equal to \(\sum_i\zeta^i\otimes\zeta^i\). Substitution of (C.3), \(|\nu|=1\) and the vanishing cross terms gives (C.4). The polar coordinates omit the centre, but the Cartesian forms \(A,\zeta\) and the frame itself remain smooth there by their construction. In dimension zero there is only the empty frame on the singleton chart and no polar domain. □

**Theorem C.2 (radial evolution from torsion and curvature).** In the notation of C.1, let \(W\) be a smooth angular vector field independent of \(r\), and put
\(\alpha_W=\phi(W)\), \(\beta_W=A(W)\). Then
\[
\begin{split}
\partial_r\alpha_W&=W(\nu)+\beta_W\nu,\\
\partial_r\beta_W&=
 e^{-1}R(e\nu,e\alpha_W)e.
\end{split}
\tag{C.5}
\]
Here every frame and curvature value on the right is at \(E(r\nu)\), and the second expression is an endomorphism of \(\mathbb R^n\). At the centre the limiting data are
\[
\alpha_W(0,\nu)=0,\qquad
\beta_W(0,\nu)=0,\qquad
\lim_{r\downarrow0}\frac{\alpha_W(r,\nu)}r=W(\nu).
\tag{C.6}
\]
Equivalently these differential identities may be integrated from \(0\) using those limiting data.

**Proof.** Linear D.1 gives the full torsion equation in the chosen frame. Since the Levi-Civita torsion is zero, its pullback is
\[
d\zeta=-A\wedge\zeta.
\tag{C.7}
\]
The evaluated exterior derivative, proved in Curvature A.2, gives
\[
d\zeta(\partial_r,W)
 =\partial_r\alpha_W-W(\nu),
\]
because \([\partial_r,W]=0\). The right side of (C.7) is
\(-A(\partial_r)\zeta(W)+A(W)\zeta(\partial_r)=\beta_W\nu\),
by C.1. This proves the first identity in (C.5), including its sign and the angular derivative term.

Linear B.3 gives \(F=dA+A\wedge A\). Evaluating on the same pair, \(A(\partial_r)=0\) and the zero bracket remove all terms except \(\partial_r\beta_W\). The same theorem identifies the pulled-back curvature:
\[
F(\partial_r,W)
 =e^{-1}R\bigl(dE(\partial_r),dE(W)\bigr)e.
\]
In this formula \(dE\) includes the polar-coordinate map; C.1 identifies these vectors with \(e\nu,e\alpha_W\), respectively. This is the second identity of (C.5).

For completeness, write the angular pullbacks in the original smooth Cartesian forms:
\[
\alpha_W(r,\nu)=r\,\zeta_{r\nu}(W(\nu)),\qquad
\beta_W(r,\nu)=r\,A_{r\nu}(W(\nu)).
\tag{C.8}
\]
Smoothness at zero, \(\zeta_0=I\) and \(A_0=0\) give all limits in (C.6). They also make both right sides of (C.5) continuous up to \(r=0\) for fixed \(\nu\). Apply Local 0.3 on \([\epsilon,r]\) and let \(\epsilon\downarrow0\). This proves, with no singular initial-value assertion,
\[
\begin{split}
\alpha_W(r,\nu)&=rW(\nu)+\int_0^r\beta_W(s,\nu)\nu\,ds,\\
\beta_W(r,\nu)&=\int_0^r
 e_s^{-1}R_{E(s\nu)}(e_s\nu,e_s\alpha_W(s,\nu))e_s\,ds.
\end{split}
\tag{C.9}
\]
These are identities for the actual smooth frame already constructed, rather than an assumption that a coordinate frame can be parallel in all directions. □

## D. The upper half-space in every dimension

Michor's free [author manuscript, §25.8](https://www.mat.univie.ac.at/~michor/dgbook.pdf) develops the upper half-plane, its circular and vertical geodesics, and its isometries and distance. Here we prove the required higher-dimensional version directly. Only the already proved connection, geodesic and real-calculus facts are used; no external shortest-path theorem is assumed.

**Lemma D.1 (the scalar functions in the geodesic formulas).** With the real exponential and logarithm constructed in Geo A.4, define
\[
\begin{gathered}
\cosh u=\frac{e^u+e^{-u}}2,\qquad
\sinh u=\frac{e^u-e^{-u}}2,\\
\tanh u=\frac{\sinh u}{\cosh u},\qquad
\operatorname{sech}u=\frac1{\cosh u}.
\end{gathered}
\tag{D.1}
\]
They are smooth for real \(u\), \(\cosh u>0\), and
\[
\begin{gathered}
\cosh^2u-\sinh^2u=1,\qquad
\tanh^2u+\operatorname{sech}^2u=1,\\
(\tanh u)'=\operatorname{sech}^2u,\qquad
(\operatorname{sech}u)'=-\operatorname{sech}u\,\tanh u.
\end{gathered}
\tag{D.2}
\]
The map \(\tanh:\mathbb R\to(-1,1)\) is a strictly increasing diffeomorphism, whose inverse is
\[
\operatorname{artanh}s=\tfrac12\log\frac{1+s}{1-s}.
\tag{D.3}
\]

**Proof.** Geo A.4 proves positivity of the exponential, its derivative, its addition identity and the smooth inverse logarithm. Thus all denominators above are nonzero and the displayed functions are smooth. Expanding the difference of squares in (D.1) gives \(e^ue^{-u}=1\); division by \(\cosh^2u\) gives the second identity of (D.2). Differentiation first gives \((\cosh)'=\sinh\), \((\sinh)'=\cosh\), and then the quotient rule gives the two remaining identities. In particular \((\tanh)'>0\). Also
\[
\tanh u=\frac{e^{2u}-1}{e^{2u}+1}.
\]
This value is in \((-1,1)\). Conversely, if \(|s|<1\), the positive number \((1+s)/(1-s)\) has a logarithm; substituting (D.3) into this last fraction gives exactly \(s\). Strict increase proves uniqueness, and (D.3) is smooth on its stated interval. The same definitions show \(\operatorname{sech}u>0\), and give limits \(\tanh u\to\pm1\), \(\operatorname{sech}u\to0\) as \(u\to\pm\infty\), by the exponential limits in Geo A.4. □

**Theorem D.2 (all upper-half-space geodesics and their full domains).** For \(n\geq2\), let
\[
\mathbb H^n=\{(x,z):x\in\mathbb R^{n-1},\ z>0\},
\qquad
g=z^{-2}\bigl(|dx|^2+dz^2\bigr).
\tag{D.4}
\]
Writing \(z\) as coordinate \(n\), its coefficients and geodesic equations are
\[
\begin{split}
\Gamma^k_{ij}
 &=-z^{-1}
 \bigl(\delta_i^n\delta_j^k+\delta_j^n\delta_i^k-\delta_n^k\delta_{ij}\bigr),\\
x''-2(z'/z)x'&=0,\qquad
z''+\bigl(|x'|^2-(z')^2\bigr)/z=0.
\end{split}
\tag{D.5}
\]
Every maximal geodesic is defined on all of \(\mathbb R\). The nonconstant ones are precisely
\[
x(t)=b,\qquad z(t)=a e^{ct},
\qquad a>0,\ c\ne0,
\tag{D.6}
\]
or
\[
\begin{split}
x(t)&=b+\rho\tanh(\kappa t+\tau)e,\\
z(t)&=\rho\operatorname{sech}(\kappa t+\tau),
\end{split}
\qquad
\rho,\kappa>0,\quad |e|=1.
\tag{D.7}
\]
The vector \(b\) lies in \(\mathbb R^{n-1}\). Their metric speeds are \(|c|\) and \(\kappa\), respectively. The images in (D.7) are the upper semicircles of radius \(\rho\), in the vertical plane of direction \(e\), centred at the boundary point \((b,0)\).

**Proof.** The inverse metric is \(g^{ij}=z^2\delta_{ij}\), and
\(\partial_i g_{jl}=-2z^{-3}\delta_i^n\delta_{jl}\).
Substitution into A.1's coefficient formula gives the first line of (D.5) after the three contractions of Kronecker symbols. Geo A.1's equation \(q''^k+\Gamma^k_{ij}q'^i q'^j=0\) then gives its second line. The horizontal equation also gives
\[
\frac d{dt}\left(\frac{x'}{z^2}\right)=0,
\]
while A.1 proves that \((|x'|^2+(z')^2)/z^2\) is constant.

For (D.6), \(x'=0\), \(z'=cz\), \(z''=c^2z\), so both equations hold and the speed is \(|c|\). For (D.7) put \(T=\tanh(\kappa t+\tau)\), \(S=\operatorname{sech}(\kappa t+\tau)\). D.1 gives
\[
x'=\rho\kappa S^2e,\quad z'=-\rho\kappa ST,\quad
x''=-2\rho\kappa^2S^2Te,\quad
z''=\rho\kappa^2S(T^2-S^2).
\tag{D.8}
\]
Substituting these four expressions into (D.5) makes both left sides zero. The speed squared is
\(\kappa^2(S^2+T^2)=\kappa^2\), and \(x'/z^2=(\kappa/\rho)e\), as required.

We verify that this list supplies every initial condition, which also resolves maximal existence. Let the initial point be \((x_0,z_0)\) and velocity \((v,w)\). If \(v=0\), (D.6) with \(b=x_0,a=z_0,c=w/z_0\) has exactly these data, allowing \(c=0\) for the constant solution. If \(s=|v|>0\), set
\[
\begin{gathered}
\kappa=\frac{\sqrt{s^2+w^2}}{z_0},\quad
e=v/s,\quad
\tau=\operatorname{artanh}\left(-\frac{w}{\kappa z_0}\right),\\
\rho=\frac{\kappa z_0^2}{s},\qquad
b=x_0-\rho\tanh\tau\,e.
\end{gathered}
\tag{D.9}
\]
The argument of \(\operatorname{artanh}\) lies strictly between \(-1\) and \(1\), because \(s>0\). D.1 gives
\(\operatorname{sech}\tau=s/(\kappa z_0)>0\).
Therefore (D.7) at zero has height \(\rho\operatorname{sech}\tau=z_0\), horizontal position \(x_0\), horizontal derivative
\(\rho\kappa\operatorname{sech}^2\tau\,e=se=v\),
and vertical derivative
\(-\kappa z_0\tanh\tau=w\).
Geo A.1's uniqueness identifies it with the geodesic of those data.

Every displayed solution stays in \(z>0\) and is smooth for every finite real time. Thus uniqueness identifies the full maximal domain with \(\mathbb R\); no geodesic ends at a boundary point in finite affine time. In particular the connection is geodesically complete and its exponential domain at every point is the entire tangent space, by Geo A.2.

Finally (D.2) gives
\[
|x-b|^2+z^2=\rho^2.
\]
As \(t\) runs over \(\mathbb R\), \(T\) runs over \((-1,1)\) and \(S>0\), so the entire upper semicircle is traced exactly once. Its Euclidean tangent at either boundary endpoint is vertical, hence perpendicular to the boundary plane. These endpoints are limiting points outside \(\mathbb H^n\), never points of a finite-time segment. □

**Theorem D.3 (global minimizing paths in upper half-space).** Every two distinct points of \(\mathbb H^n\) have exactly one minimizing affinely parametrized geodesic on \([0,1]\). It is the vertical or circular segment described in D.2. Every piecewise \(C^1\) path of that same length follows that segment monotonically, with pauses allowed. In particular every finite segment of every geodesic in D.2 minimizes globally.

**Proof.** First, for any path \((x(t),z(t))\) from \((x_1,z_1)\) to \((x_2,z_2)\),
\[
\begin{split}
L_g&=\int\frac{\sqrt{|x'|^2+(z')^2}}z\,dt\\
&\geq\int\frac{|z'|}z\,dt
\geq\left|\log z_2-\log z_1\right|.
\end{split}
\tag{D.10}
\]
All statements follow from A.2's length formula and Local 0.3, since \((\log z)'=z'/z\) by Geo A.4. If \(x_1=x_2\), a vertical segment with monotone logarithmic height attains this bound. Equality in the first inequality forces \(x'=0\) on every smooth piece: its continuous nonnegative difference has zero integral, so is identically zero. Equality in the second forces \((\log z)'\) to have the single weak sign of the endpoint difference on each piece. Indeed, subtract either \(\int(\log z)'\) or its negative from \(\int|(\log z)'|\); the nonnegative integrand must vanish. Thus every equality path is a monotone vertical path. When the endpoints coincide, length zero implies a constant path by A.2.

We next construct the needed isometry in every dimension. For a boundary point \(a=(a_x,0)\), put
\[
I_a(q)=\frac{q-a}{|q-a|^2}.
\tag{D.11}
\]
It maps \(\mathbb H^n\) into itself, with height \(z/|q-a|^2>0\). Its smooth inverse is \(y\mapsto a+y/|y|^2\), as direct substitution shows. If \(h=q-a\), then
\[
(dI_a)_qv=\frac1{|h|^2}
 \left(v-2h\,\frac{h\cdot v}{|h|^2}\right).
\tag{D.12}
\]
The expression in parentheses preserves Euclidean inner products: expanding the product of its values on \(v,w\) gives two negative terms
\(-2(h\cdot v)(h\cdot w)/|h|^2\) and one positive term
\(4(h\cdot v)(h\cdot w)/|h|^2\), which cancel. The differential therefore scales Euclidean squared lengths by \(|h|^{-4}\). The reciprocal square of the new height is \(|h|^4/z^2\), so those factors cancel and \(I_a^*g=g\). A.3 now proves length, distance and affine-geodesic preservation for this global isometry.

For a circular geodesic (D.7), choose \(a=(b-\rho e,0)\). Put \(u=\kappa t+\tau\). The identity
\[
|q-a|^2=2\rho^2(1+\tanh u)
\]
follows by expanding and using (D.2). Consequently
\[
I_a(q(t))=\left(\frac{e}{2\rho},\frac{e^{-u}}{2\rho}\right).
\tag{D.13}
\]
For the height, use
\[
\begin{aligned}
\frac{\operatorname{sech}u}{1+\tanh u}
 &=\frac1{\cosh u+\sinh u}\\
 &=e^{-u},
\end{aligned}
\]
proved immediately from (D.1). Thus this is a vertical geodesic with strictly monotone logarithmic height. Applying \(I_a\) to every competing path and using (D.10) proves that every finite circular segment minimizes. Its equality cases are exactly the inverse images of monotone vertical segments, so have the asserted form. The unique affine parametrization on a fixed interval follows either from constant speed or from the vertical formula and A.3.

It remains to show that every pair is on one of these geodesics. Equal horizontal coordinates were handled. Otherwise put
\[
\begin{gathered}
d=|x_2-x_1|>0,\qquad e=(x_2-x_1)/d,\\
a_0=\frac{d^2+z_2^2-z_1^2}{2d},\qquad
b=x_1+a_0e,\qquad \rho=\sqrt{a_0^2+z_1^2}.
\end{gathered}
\tag{D.14}
\]
Then
\[
|x_1-b|^2+z_1^2
=|x_2-b|^2+z_2^2=\rho^2,
\]
since their difference is \(d^2-2da_0+z_2^2-z_1^2=0\). The scalar coordinates along \(e\) are \(s_1=-a_0\), \(s_2=d-a_0\). Positivity of each \(z_i\) gives \(|s_i|<\rho\). Therefore \(u_i=\operatorname{artanh}(s_i/\rho)\) exists, and
\(\rho\operatorname{sech}u_i=z_i\), by (D.2) and the positive sign. Formula (D.7) with parameter \(u\) passes through both endpoints at \(u_1,u_2\); \(u_1<u_2\) because \(s_1<s_2\). A linear change of parameter puts that segment on \([0,1]\). Its minimizing and equality assertions have already been proved, and they give uniqueness for the pair. □

## E. Two different radii on the round sphere

The sphere construction is supplied by the complete programme proof Geo F.3, itself reconstructed from Michor's free [author manuscript, §§23.1 and 25.7](https://www.mat.univie.ac.at/~michor/dgbook.pdf), the earlier projection-connection proof, and the programme's circle calculus. We use its exact exponential map and prove the global distance and convexity assertions here.

**Theorem E.1 (distance and all minimizing spherical arcs).** On the unit round sphere \(S^2\), for all \(p,q\),
\[
d_g(p,q)=\arccos(p\cdot q)\in[0,\pi].
\tag{E.1}
\]
For \(q\ne-p\), the short great-circle arc is the unique minimizing affine geodesic on \([0,1]\); every other minimizing piecewise \(C^1\) path traces it monotonically. For \(q=-p\), every great semicircle from \(p\) to \(-p\) is minimizing, so uniqueness fails.

**Proof.** Geo F.3 proves the full geodesics
\[
\gamma_v(t)=
\begin{cases}
\cos(|v|t)p+\dfrac{\sin(|v|t)}{|v|}v,&v\ne0,\\
p,&v=0,
\end{cases}
\tag{E.2}
\]
and proves that \(\exp_p\) maps \(|v|<\pi\) diffeomorphically onto \(S^2\setminus\{-p\}\). Its tangent metric is the ambient Euclidean inner product. The cosine is strictly decreasing on \([0,\pi]\), with range \([-1,1]\), as established by the circle construction in Connections E.1 and used with full details in Geo F.3. Thus \(\arccos\) here means its unique inverse on that interval.

For \(q\ne-p\), the dot product of (E.2) at \(t=1\) with \(p\) gives \(\cos|v|=p\cdot q\). B.3 applied with \(R=\pi\) now proves (E.1), uniqueness and the equality characterization, including \(q=p\).

A great semicircle from \(p\) to \(-p\) has speed \(\pi\) on \([0,1]\) by (E.2), so \(d_g(p,-p)\leq\pi\). Choose points \(q_j\ne-p\) tending to \(-p\) along that semicircle. A.2's equality of distance and manifold topologies gives \(d_g(q_j,-p)\to0\). The triangle inequality gives
\[
d_g(p,-p)\geq d_g(p,q_j)-d_g(q_j,-p).
\]
The first term tends to \(\pi\), because its radial parameter along (E.2) tends to \(\pi\). Hence \(d_g(p,-p)\geq\pi\), proving equality. For every unit vector \(e\in T_pS^2\), the curve \(\cos(\pi t)p+\sin(\pi t)e\) has that length and those endpoints, and is minimizing. Distinct such initial directions give distinct arcs by their initial velocities and Geo A.1. □

**Theorem E.2 (the exact strongly convex spherical balls).** For any \(p\in S^2\), the open distance ball \(B_g(p,r)\), \(r>0\), is strongly convex exactly when
\[
0<r\leq\pi/2.
\tag{E.3}
\]
For those radii, each point of the ball is a centre for a star-shaped exponential domain mapping diffeomorphically onto the whole ball. The squared distance is smooth on the product of the ball with itself. In contrast the normal exponential ball about \(p\) has radius \(\pi\), as in E.1.

**Proof.** Suppose first \(0<r\leq\pi/2\). By E.1 the ball is the cap
\[
V=\{q\in S^2:p\cdot q>\cos r\}.
\tag{E.4}
\]
Every point of this cap has positive dot product with \(p\), so no two points in it are antipodal. For distinct \(q_1,q_2\in V\), put
\(\alpha=\arccos(q_1\cdot q_2)\in(0,\pi)\).
Their short arc is
\[
\gamma(t)=
\frac{\sin((1-t)\alpha)}{\sin\alpha}\,q_1+
\frac{\sin(t\alpha)}{\sin\alpha}\,q_2,\qquad 0\leq t\leq1.
\tag{E.5}
\]
To verify this formula, put
\(w=(q_2-\cos\alpha\,q_1)/\sin\alpha\).
The dot products give \(w\cdot q_1=0\), \(|w|=1\). The sine subtraction identity follows by taking the imaginary part of the exponential addition identity in Connections E.1. Substitution into (E.5) therefore gives
\(\gamma(t)=\cos(t\alpha)q_1+\sin(t\alpha)w\).
By (E.2) this is the geodesic with the correct endpoints and speed \(\alpha\); E.1 makes it the unique global minimizer.

For \(0<t<1\), both coefficients \(A,B\) in (E.5) are positive. Since \(|\gamma(t)|=1\), the Euclidean triangle inequality gives \(A+B\geq1\). Taking the dot product with \(p\), and using \(\cos r\geq0\), gives
\[
p\cdot\gamma(t)
 =A(p\cdot q_1)+B(p\cdot q_2)
 \mathrel{>}(A+B)\cos r\geq\cos r.
\tag{E.6}
\]
This also works at \(r=\pi/2\), because the two endpoint dot products are strictly positive. Endpoints already lie in \(V\), so the entire arc does. For equal endpoints the unique minimizing path is constant. This proves strong convexity, including its global uniqueness assertion.

Fix \(x\in V\). Since \(-x\notin V\), Geo F.3's diffeomorphism \(\exp_x:B_\pi(0)\to S^2\setminus\{-x\}\) has the open inverse image \(W_x=\exp_x^{-1}(V)\). It contains zero and maps diffeomorphically onto \(V\). The containment of every initial portion of (E.5) in \(V\), and Geo A.2's scaling identity, show \(tv\in W_x\) for \(v\in W_x\), \(0\leq t\leq1\); hence it is star-shaped.

Away from the diagonal the initial vector of the joining arc is the smooth expression
\[
v(x,y)=\frac{\alpha}{\sin\alpha}\bigl(y-(x\cdot y)x\bigr),
\qquad \alpha=\arccos(x\cdot y)\in(0,\pi).
\tag{E.7}
\]
Smoothness of the inverse cosine there follows from Local 1.2 and its nonzero derivative \(-\sin\alpha\). Near a diagonal point, Geo B.1 supplies a smooth endpoint inverse; its small vectors lie in the fibre balls of radius \(\pi\), so fibre injectivity identifies it with (E.7) off the diagonal and with zero on it. These local inverses agree, giving a smooth map \(v\) on all of \(V\times V\). E.1 yields \(d_g(x,y)^2=g_x(v(x,y),v(x,y))\), which is consequently smooth on the whole product.

Now suppose \(\pi/2<r\leq\pi\). Choose \(\theta\) with \(\pi/2<\theta<r\), and choose any unit \(e\in T_pS^2\). The two points
\[
q_\pm=\cos\theta\,p\ \pm\sin\theta\,e
\]
belong to \(B_g(p,r)\) by E.1. Their mutual angle is
\(\alpha=2(\pi-\theta)\in(0,\pi)\), since their dot product is \(\cos(2\theta)=\cos\alpha\). Their unique shorter arc (E.5) has midpoint
\[
\frac{q_++q_-}{2\cos(\alpha/2)}
=\frac{2\cos\theta\,p}{-2\cos\theta}=-p.
\]
Here the midpoint coefficient identity follows from
\(\sin\alpha=2\sin(\alpha/2)\cos(\alpha/2)\), again the circle addition identity. But \(d_g(p,-p)=\pi\geq r\), so that midpoint is outside the open ball. Thus this ball is not strongly convex even for a pair with a unique global minimizing arc.

If \(r>\pi\), E.1 makes the ball the entire sphere; an antipodal pair has multiple minimizing arcs, so it is not strongly convex either. These cases prove (E.3). They also show why the injective exponential radius \(\pi\) about one fixed centre does not give convexity for all pairs throughout that ball. □

## F. Metric algebra, frame reductions and energy

These details complete the metric and frame hypotheses used in the chapter. Construction uses Michor's free [author manuscript, §§22.5 and 25.1–25.6](https://www.mat.univie.ac.at/~michor/dgbook.pdf), together with the exact earlier programme proofs cited in each argument.

**Theorem F.1 (existence of positive metrics and raising indices).** Every manifold under the hypotheses of this chapter has a Riemannian metric. For any smooth pseudo-Riemannian metric \(g\), the maps
\[
v^\flat=g(v,\cdot),\qquad
\alpha^\sharp=g^{-1}\alpha
\tag{F.1}
\]
are mutually inverse smooth bundle maps \(TM\leftrightarrow T^*M\). In coordinates,
\[
(v^\flat)_i=g_{ij}v^j,\qquad
(\alpha^\sharp)^i=g^{ij}\alpha_j,\qquad
g^{-1}(\alpha,\beta)=g^{ij}\alpha_i\beta_j.
\tag{F.2}
\]
They raise or lower any chosen tensor index. Every metric-compatible connection commutes with these operations.

**Proof.** DG-CHAR-17 D.2 proves existence of a positive smooth fibre metric on every real vector bundle using a locally finite smooth partition of unity and positive local inner products. Apply that exact theorem to \(TM\); all its manifold hypotheses are the ones fixed at the start of this chapter. This proves existence without presuming a connection.

For a nondegenerate \(g\), its coordinate matrix \(G\) is invertible and its inverse is smooth by Local 0.4. Multiplying \(G^{-1}G=I=GG^{-1}\) proves that the first two expressions in (F.2) are inverse. They are independent of coordinates, since the first is the covector defined by the bilinear form and the second is its unique inverse. Hence they give the stated smooth bundle maps. Evaluating \(\alpha\) on \(\beta^\sharp\) gives the last expression; symmetry of \(G^{-1}\), obtained by transposing \(GG^{-1}=I\), gives its symmetry.

For tensors, apply these maps to one factor and the identity to all others. Linear C.1 proves that this tensor operation is smooth and gives its covariant product and contraction rules. If \(\nabla g=0\), applying those rules to \(G^{-1}G=I\), interpreted as the contraction of the inverse tensor with \(g\), gives
\((\nabla_Xg^{-1})g+g^{-1}\nabla_Xg=0\).
Invertibility then gives \(\nabla_Xg^{-1}=0\). The same product rule now shows that taking a derivative commutes with every raising or lowering map. This argument includes indefinite metrics. □

**Theorem F.2 (orthonormal frame bundles in every signature).** A pseudo-Riemannian metric has locally constant signature \((r,s)\), \(r+s=n\), and smooth local frames with Gram matrix \(J=\operatorname{diag}(I_r,-I_s)\). On any fixed-signature component those frames form a smooth principal \(\mathrm O(r,s)\)-bundle, where
\[
\mathrm O(r,s)=\{h\in\mathrm{GL}(n,\mathbb R):h^TJh=J\},\qquad
\mathfrak o(r,s)=\{B:B^TJ+JB=0\}.
\tag{F.3}
\]
A connection is metric-compatible exactly when its parallel transports are isometries. In any such frame its connection matrix obeys \(A^TJ+JA=0\); its principal frame connection restricts to this orthonormal frame bundle. For a positive metric these statements give \(\mathrm O(n)\) and skew-symmetric matrices.

**Proof.** First construct an orthonormal basis for any nondegenerate symmetric real bilinear form. There is a vector with nonzero squared value: if every squared value were zero, expansion of \(g(v+w,v+w)\) would give \(2g(v,w)=0\) for every pair, contradicting nondegeneracy in positive dimension. Normalize such a vector \(e\) by the positive square root of \(|g(e,e)|\), whose existence is Local 0.0. If \(g(e,e)=\epsilon\in\{1,-1\}\), every vector decomposes as
\[
v=\epsilon g(v,e)e+\bigl(v-\epsilon g(v,e)e\bigr).
\]
The second term is orthogonal to \(e\). The restriction to that complement is nondegenerate: a vector annihilating it and \(e\) annihilates the entire space, and is therefore zero. Induction on dimension produces an orthogonal basis with all squared values \(1\) or \(-1\). Reorder it to put positive signs first.

The numbers of each sign are intrinsic. If two such bases had positive dimensions \(r>r'\), the positive span of the first and the negative span of the second would have dimensions summing to \(r+(n-r')>n\), hence a nonzero intersection. Indeed, the union of their bases has more than \(n\) vectors, so has a linear dependence. Moving the terms from one basis to the other gives a vector in the intersection. If that vector were zero, independence within each separate basis would make every coefficient zero, a contradiction. A nonzero intersection vector would have both positive and negative squared value, also a contradiction. Interchange the bases to conclude \(r=r'\), hence \(s=s'\).

At a manifold point extend this basis to a smooth coordinate-frame combination nearby. Apply the following orthogonalization to these extended fields \(u_k\):
\[
w_k=u_k-\sum_{j<k}\epsilon_jg(u_k,e_j)e_j,\qquad
e_k=\frac{w_k}{\sqrt{|g(w_k,w_k)|}}.
\tag{F.4}
\]
At the original point each denominator equals one and its squared value has sign \(\epsilon_k\). Continuity lets us shrink the neighbourhood finitely many times so that all denominators stay nonzero with those same signs. Their square roots are smooth, by Local 1.2 applied to squaring on positive numbers. Direct pairing in (F.4) gives \(g(e_k,e_j)=0\) for \(j<k\) and \(g(e_k,e_k)=\epsilon_k\). These nonzero orthogonal vectors are independent, so they form a smooth frame with the same \(J\) throughout the neighbourhood. This proves local constancy of signature.

We also verify the needed Lie group, rather than assuming it. On the open matrix manifold \(\mathrm{GL}(n,\mathbb R)\), the smooth map \(h\mapsto h^TJh\) takes values in the symmetric matrices. At a point with \(h^TJh=J\), its derivative in direction \(hB\) is \(B^TJ+JB\). This is onto the symmetric matrices: for symmetric \(S\), choose \(B=\tfrac12J^{-1}S\). Local 1.3 then makes its level set \(J\) a smooth embedded submanifold, with tangent space at the identity exactly the kernel in (F.3). Matrix multiplication and inversion preserve this level set by multiplication of the defining equations. They restrict smoothly, using the submanifold coordinates and Local 0.4 for inversion. Thus it is a Lie group with the stated tangent Lie algebra.

If \(e\) is one local \(J\)-frame, every other such frame is uniquely \(eh\), with \(h^TJh=J\). The map \((x,h)\mapsto e(x)h\) is a smooth trivialization with smooth inverse given by its frame coordinates. On overlaps its changes are smooth multiplication by matrices in \(\mathrm O(r,s)\). The principal-bundle gluing and free transitive right action are precisely PB A.1, now applied to this verified Lie group. These charts are the orthonormal subbundle of the full frame bundle of Linear A.2.

For metric compatibility, differentiate the constant Gram matrix \(g(e_i,e_j)=J_{ij}\) and use Linear A.1's connection matrix. The result is \(A^TJ+JA=0\). Conversely this identity in a \(J\)-frame, followed by the ordinary product rule on the coordinate columns of two fields, gives metric compatibility. For parallel columns \(v'=-A(\dot\gamma)v\), \(w'=-A(\dot\gamma)w\), differentiation gives
\[
\frac d{dt}(v^TJw)=-v^T\bigl(A(\dot\gamma)^TJ+JA(\dot\gamma)\bigr)w=0.
\]
Linear A.2 supplies full transport, so a compatible connection transports isometrically. Conversely, suppose transport is isometric along every smooth path. Choose a path with any prescribed initial tangent and parallel fields with arbitrary initial values. Differentiate their constant pairing. The tensor product rule in Linear C.1 identifies that derivative with \((\nabla_{\dot\gamma}g)(V,W)\), because both fields are parallel. All three initial values were arbitrary, so \(\nabla g=0\).

Finally the full frame connection in the chart \((x,h)\) is
\(\omega=h^{-1}Ah+h^{-1}dh\), by Linear A.2. On \(\mathrm O(r,s)\), differentiating \(h^TJh=J\) makes \(h^{-1}dh\) lie in \(\mathfrak o(r,s)\); conjugation by \(h\) preserves that space by the same identity, so \(h^{-1}Ah\) lies there too. Its restriction retains equivariance and reproduces every fundamental vertical vector, as the full frame form does. These facts define a principal connection; its horizontal kernel has the base dimension because the form is an isomorphism on the vertical tangent space and is surjective there. Thus the restriction is a connection on the orthonormal bundle, with the same parallel frames. □

**Theorem F.3 (normal metric derivatives, unit speed and energy).** For Levi-Civita normal coordinates centred at \(p\),
\[
\Gamma^k_{ij}(p)=0,\qquad \partial_k g_{ij}(p)=0.
\tag{F.5}
\]
Choosing a \(J\)-orthonormal initial basis also gives \(g_{ij}(p)=J_{ij}\). For positive \(g\), every nonconstant geodesic has positive constant speed and can be affinely rescaled to unit speed. For any piecewise \(C^1\) path on \([0,1]\), define
\[
\mathcal E(\eta)=\tfrac12\int_0^1|\dot\eta|_g^2\,dt.
\]
Then
\[
2\mathcal E(\eta)-L_g(\eta)^2
=\int_0^1\bigl(|\dot\eta|_g-L_g(\eta)\bigr)^2\,dt\geq0.
\tag{F.6}
\]
Equality holds exactly when all smooth pieces have the same constant speed. The minimizing affine geodesics of B.3 and B.5 also uniquely minimize energy among paths with the same endpoints and parameter interval \([0,1]\).

**Proof.** Geo B.1 gives \(\Gamma^k_{ij}(p)=\tfrac12\mathcal T^k_{ij}(p)\) in normal coordinates, so zero Levi-Civita torsion gives the first identity. Compatibility in coordinate fields says
\[
\partial_k g_{ij}=\Gamma^a_{ki}g_{aj}+\Gamma^a_{kj}g_{ia}.
\]
Evaluating at \(p\) gives the second. Geo B.1 also identifies the coordinate basis at \(p\) with the chosen initial basis; F.2 supplies a \(J\)-orthonormal choice. These assertions are pointwise and do not assert that nearby metric coefficients are constant.

A.1 gives constant squared speed. In a positive metric zero speed at one time means zero initial velocity there, so Geo A.1's uniqueness makes the entire geodesic constant. Otherwise its speed is \(\kappa>0\). Replacing \(\gamma(t)\) by \(\gamma(t/\kappa)\), on the correspondingly scaled interval, gives unit speed and is still an affine geodesic by Geo A.2.

Write \(s(t)=|\dot\eta(t)|_g\) and \(L=\int_0^1s\). Integrating \(s^2-2Ls+L^2\) gives \(2\mathcal E-L^2\), proving (F.6). The nonnegative squared integrand has zero integral exactly when it is zero on each of the finitely many smooth pieces, by continuity and Local 0.3. Hence equality is equivalent to speed \(L\) throughout all pieces, with the same one-sided values at corners.

For a pair in B.3 or B.5 put \(d=d_g(x,y)\). Every competitor has \(2\mathcal E\geq L^2\geq d^2\). The minimizing affine segment has constant speed \(d\) on \([0,1]\), so has energy \(d^2/2\). Equality for a competitor forces both minimal length and that constant speed. The equality characterization in B.3 then removes pauses and fixes the radial parameter as \(dt\); for \(d=0\), A.2 forces the constant path. B.5 reduces to that same normal-ball argument at its first endpoint. Thus the energy minimizer is exactly the asserted affine segment. □

**Example F.4 (why an isometric immersion needs a different statement).** An isometric immersion of positive codimension can fail to preserve both intrinsic parallel fields and intrinsic geodesics.

**Proof.** Use the unit circle \(S^1\subset\mathbb R^2\) with its induced metric and the inclusion map. The smooth circle and its parameter
\(\gamma(t)=(\cos t,\sin t)\) are constructed in PB E.1 and Connections E.1. Their derivatives give \(\gamma'(t)=(-\sin t,\cos t)\), which has unit length and spans the tangent line. Its intrinsic Levi-Civita derivative must be a multiple \(a(t)\gamma'(t)\). Metric compatibility differentiates its constant squared norm to give \(2a(t)=0\). Hence \(\gamma'\) is intrinsically parallel and \(\gamma\) is an intrinsic geodesic. The Euclidean metric has zero Cartesian connection coefficients by A.1, whereas \(\gamma''(t)=-\gamma(t)\ne0\). Thus its image velocity is not ambient parallel and its image curve is not an ambient geodesic. The inclusion is isometric by the definition of the induced metric but has unequal source and target dimensions, so A.3's hypothesis is essential. □
