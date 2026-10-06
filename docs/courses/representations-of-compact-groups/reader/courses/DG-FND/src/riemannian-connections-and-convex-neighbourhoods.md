# Riemannian connections and convex neighbourhoods

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Self-checked by the writing AI. Original text dedicated to the public domain under CC0 1.0.*

A metric measures the speed of a curve, while a connection differentiates its velocity. Requiring that transport preserve the metric and that torsion vanish links these two operations in a unique way. The resulting geodesics are locally the shortest curves. We prove that assertion against all competing curves, including curves that leave the chosen coordinates, and obtain neighbourhoods in which every pair has a unique shortest geodesic.

Read [Linear and affine connections](linear-and-affine-connections.md), Sections 1–2, for covariant derivatives, tensor derivatives and fibre metrics. [Geodesics, normal coordinates and curvature](geodesics-normal-coordinates-and-curvature.md), Sections 1–2, proves the smooth exponential map and the affine convex-neighbourhood theorem. Its Section 3 fixes our torsion and curvature signs. [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md), Sections 1–3, supplies local inversion, smooth differential equations and partitions of unity. We assume finite-dimensional linear algebra and elementary multivariable calculus. Basic references are [Durrer], [Valencia] and [Pinkall–Gross].

## 1. Length before a connection

Let \(M\) be a finite-dimensional Hausdorff second-countable smooth manifold without boundary. A **Riemannian metric** is a smooth symmetric two-tensor \(g\) whose value on every tangent space is positive definite. Write

\[
|v|_g=\sqrt{g(v,v)}.
\]

Such metrics exist: apply the fibre-metric construction in Linear and affine connections, Theorem 2.1, to \(TM\). It sums local Euclidean metrics with a smooth partition of unity. Positivity holds because some weight is positive at every point.

In coordinates \(g=g_{ij}\,dx^i\otimes dx^j\), the symmetric matrix \(G=(g_{ij})\) is positive definite. Its inverse \((g^{ij})\) is smooth by the cofactor formula. The metric identifies vectors with covectors:

\[
v^\flat=g(v,\cdot),\qquad
(\alpha^\sharp)^i=g^{ij}\alpha_j.
\tag{1.1}
\]

These are inverse bundle maps. The induced pairing of covectors is \(g^{-1}(\alpha,\beta)=g^{ij}\alpha_i\beta_j\). Applying these maps to individual tensor factors raises and lowers indices; this changes the type of a tensor, rather than merely changing the way its coefficients are printed.

We will also use a **pseudo-Riemannian metric**: a smooth symmetric two-tensor that is nondegenerate at every point, with a fixed signature on each connected component. The maps (1.1) still exist. Its values can be negative on nonzero vectors, so the length and distance constructions below are reserved for positive definite metrics. No existence of a metric of an arbitrarily prescribed indefinite signature is asserted.

For a path \(\eta:[a,b]\to M\) that is \(C^1\) on finitely many closed subintervals, define its length by summing

\[
L_g(\eta)=\int_a^b|\dot\eta(t)|_g\,dt
\tag{1.2}
\]

over these pieces. One-sided derivatives may differ at a break. Refining the division does not change the integral. Pauses and constant pieces are allowed. A \(C^1\) diffeomorphism of the parameter interval preserves length: the chain rule introduces the absolute value of its derivative, and substitution in the integral cancels that factor. Reversing a path has the same length. Concatenation adds lengths.

Assume for the moment that \(M\) is connected. Any two points can be joined by such a path. Indeed, the points reachable from one fixed point by finitely many coordinate line segments form an open set. Its complement is open too: a sufficiently small coordinate ball joins each of its points to every nearby point. Connectedness therefore makes every point reachable.

Define the **Riemannian distance**

\[
d_g(p,q)=\inf_{\eta:p\to q}L_g(\eta),
\tag{1.3}
\]

where the infimum runs through these piecewise \(C^1\) paths. This is finite. Reversal and concatenation give symmetry and the triangle inequality. The infimum need not be attained; Exercise 6.4 gives an example.

**Proposition 1.1 (distance and topology).** The function \(d_g\) is a metric, and its topology is the manifold topology.

**Proof.** A connected zero-dimensional manifold is a single point, where the assertion is immediate. In positive dimension, centre a coordinate chart at \(p\), and choose a closed Euclidean ball \(\overline B_R\) lying inside it. On its compact product with the Euclidean unit sphere, \(g_x(v,v)\) has a positive minimum and a finite maximum. Thus constants \(0<m\le B\) satisfy

\[
\begin{gathered}
m|v|\le|v|_{g_x}\le B|v|,\\
x\in\overline B_R.
\end{gathered}
\tag{1.4}
\]

Here and only in this local estimate, unadorned norms are Euclidean coordinate norms.

A path contained in this ball has length at least \(m\) times the Euclidean displacement of its endpoints, by integrating the Euclidean speed. A path from \(p\) that leaves \(B_R\) first meets its boundary. The length up to that meeting is at least \(mR\). The boundary assertion follows because the coordinate closed ball is compact, hence closed in the Hausdorff manifold; its interior is the coordinate open ball.

Consequently, for \(q\in B_R\),

\[
m|q|\le d_g(p,q)\le B|q|.
\tag{1.5}
\]

For the lower bound, paths staying in the ball cost at least \(m|q|\), and paths leaving it cost at least \(mR\ge m|q|\). The upper bound uses the coordinate straight segment. If \(q\notin B_R\), every path to \(q\) costs at least \(mR\). These bounds prove \(d_g(p,q)>0\) when \(q\ne p\).

They also compare neighbourhoods at \(p\). Small coordinate balls lie in prescribed distance balls by the upper bound. Conversely a distance ball of radius less than \(mR\) lies inside \(B_R\), and its points satisfy the lower bound. The two topologies agree at every point. □

For a disconnected manifold the construction applies on each component. Distances between different components can be left undefined or taken to be \(+\infty\); an ordinary finite metric requires the connected-component convention.

## 2. The derivative selected by a metric

For a connection \(\nabla\), **metric compatibility** means

\[
\begin{aligned}
Xg(Y,Z)&=g(\nabla_XY,Z)\\
&\quad+g(Y,\nabla_XZ).
\end{aligned}
\tag{2.1}
\]

Equivalently \(\nabla g=0\), by the tensor derivative rule. It also means that parallel transport preserves the metric. Along a path, differentiate the pairing of two parallel fields; equation (2.1) makes the derivative zero. Conversely choose parallel extensions of arbitrary initial vectors along a path with any specified initial velocity. Constancy of their pairing gives \((\nabla_Xg)(Y,Z)=0\) at the initial point. This proof works for both positive and indefinite metrics.

The torsion convention is

\[
\begin{aligned}
T(X,Y)&=\nabla_XY-\nabla_YX\\
&\quad-[X,Y].
\end{aligned}
\tag{2.2}
\]

Compatibility alone does not force \(T=0\); Exercise 6.2 describes a family of metric connections with torsion.

**Theorem 2.1 (Levi-Civita).** Every smooth pseudo-Riemannian metric has exactly one compatible connection with zero torsion. It is determined by the Koszul formula

\[
\begin{aligned}
&2g(\nabla_XY,Z)\\
&=Xg(Y,Z)+Yg(Z,X)\\
&\quad-Zg(X,Y)-g(X,[Y,Z])\\
&\quad+g(Y,[Z,X])+g(Z,[X,Y]).
\end{aligned}
\tag{2.3}
\]

In particular the theorem applies to every Riemannian metric.

**Proof.** Denote the right side of (2.3) by \(K(X,Y,Z)\). The bracket rules

\[
\begin{gathered}
[X,fY]=f[X,Y]+X(f)Y,\\
[fX,Y]=f[X,Y]-Y(f)X.
\end{gathered}
\]

give

\[
\begin{aligned}
K(fX,Y,Z)&=fK(X,Y,Z),\\
K(X,fY,Z)&=fK(X,Y,Z)\\
&\quad+2X(f)g(Y,Z),\\
K(X,Y,fZ)&=fK(X,Y,Z).
\end{aligned}
\tag{2.4}
\]

Here is the cancellation in each slot. In the first slot, the extra terms from the three derivatives and three brackets are

\[
\begin{gathered}
Y(f)g(Z,X)-Z(f)g(X,Y)\\
+Z(f)g(Y,X)-Y(f)g(Z,X)=0.
\end{gathered}
\]

In the second slot they are

\[
\begin{gathered}
X(f)g(Y,Z)-Z(f)g(X,Y)\\
+Z(f)g(X,Y)+X(f)g(Z,Y)\\
=2X(f)g(Y,Z).
\end{gathered}
\]

In the third slot they are

\[
\begin{gathered}
X(f)g(Y,Z)+Y(f)g(Z,X)\\
-Y(f)g(X,Z)-X(f)g(Y,Z)=0.
\end{gathered}
\]

Additivity and real linearity are immediate from the same definition.

Thus \(Z\mapsto K(X,Y,Z)/2\) is a smooth covector field. Nondegeneracy of \(g\) defines one smooth vector field \(\nabla_XY\) by (2.3): in coordinates multiply the covector components by \(g^{ij}\). The first two identities in (2.4) are precisely linearity over functions in \(X\) and the derivative rule in \(Y\). Hence this operation is a connection.

Subtracting the definitions with \(X,Y\) exchanged gives

\[
\begin{gathered}
K(X,Y,Z)-K(Y,X,Z)\\
=2g([X,Y],Z).
\end{gathered}
\tag{2.5}
\]

The derivative terms cancel in pairs; the two remaining bracket terms are \(g(Z,[X,Y])-g(Z,[Y,X])\). Equation (2.5) and nondegeneracy prove zero torsion. Adding the definitions with \(Y,Z\) exchanged instead gives

\[
\begin{gathered}
K(X,Y,Z)+K(X,Z,Y)\\
=2Xg(Y,Z).
\end{gathered}
\tag{2.6}
\]

The other derivative terms cancel, as do all six bracket terms. This is metric compatibility.

For uniqueness, suppose a connection has both required properties. Write the three compatibility identities for \(Xg(Y,Z)\), \(Yg(Z,X)\) and \(Zg(X,Y)\). Add the first two and subtract the third. Replace \(\nabla_YX,\nabla_ZX,\nabla_ZY\) using (2.2) with \(T=0\). The terms not involving \(\nabla_XY\) cancel, leaving exactly (2.3). Since \(g\) is nondegenerate, (2.3) determines \(\nabla_XY\) uniquely. □

This is the **Levi-Civita connection**. Taking coordinate fields in (2.3), whose brackets vanish, gives

\[
\begin{aligned}
\Gamma^k_{ij}
&=\tfrac12g^{k\ell}\bigl(\partial_i g_{j\ell}\\
&\quad+\partial_j g_{i\ell}
-\partial_\ell g_{ij}\bigr).
\end{aligned}
\tag{2.7}
\]

The lower indices are symmetric. Formula (2.7) works for indefinite metrics as well: only matrix invertibility was required.

For a positive metric, the orthonormal frames form a smooth principal \(\mathrm O(n)\)-bundle. Smooth Gram–Schmidt on a local frame constructs its sections: subtract the earlier orthogonal projections and divide by the positive square root of the remaining squared norm. Compatibility makes transport preserve these frames. In an orthonormal frame its potential \(A\) satisfies \(A^T+A=0\), obtained by differentiating \(g(e_i,e_j)=\delta_{ij}\). Conversely a skew potential gives (2.1).

For signature \((p,q)\), the same argument is local with a frame whose Gram matrix is \(J=\operatorname{diag}(I_p,-I_q)\). Start with a basis of that signature at the chosen point. Orthogonalize in its fixed order nearby; each nonzero squared norm retains its sign, so division by the square root of its absolute value is smooth. The compatibility condition becomes \(A^TJ+JA=0\). This identifies the corresponding \(\mathrm O(p,q)\)-reduction.

The normal coordinates of Geodesics, normal coordinates and curvature, Theorem 2.1, now have

\[
\Gamma^k_{ij}(p)=0.
\]

If the initial basis is orthonormal, \(g_{ij}(p)=\delta_{ij}\). Compatibility gives

\[
\partial_k g_{ij}
=\Gamma^\ell_{ki}g_{\ell j}
+\Gamma^\ell_{kj}g_{i\ell},
\tag{2.8}
\]

so all first metric derivatives vanish at the centre. This is a pointwise statement; the metric need not be constant nearby.

**Proposition 2.2 (local isometries).** A local isometry between manifolds of the same dimension preserves their Levi-Civita connections, parallel transport and geodesics.

**Proof.** On a neighbourhood where \(F:(M,g)\to(N,h)\) is a diffeomorphism onto an open set, pull back the connection of \(h\) by \(dF\). The derivative rule follows from the chain rule. Because \(F^*h=g\), the pulled-back connection is metric; because diffeomorphisms preserve vector-field brackets, its torsion is zero. Uniqueness in Theorem 2.1 therefore gives

\[
dF(\nabla_XY)=\nabla^h_{dF(X)}dF(Y).
\tag{2.9}
\]

Along a path this equality makes the image of a parallel field parallel, and the image of a geodesic geodesic. Cover a compact path interval by finitely many such neighbourhoods and use uniqueness of parallel transport and of geodesic initial values to glue the statements. Thus \(F\) need not be globally injective. Wherever both sides are defined,

\[
F(\exp_pv)=\exp_{F(p)}(dF_pv).
\tag{2.10}
\]

□

The equal-dimension condition matters. An isometric immersion of positive codimension need not carry intrinsic parallel vectors to ambient parallel vectors. For the unit circle in the Euclidean plane, its unit tangent is intrinsically parallel along the circle, but its ambient derivative is the nonzero normal acceleration.

## 3. Radial orthogonality and shortest curves

From now on \(\nabla\) is the Levi-Civita connection of a positive metric, except where another signature is explicitly allowed. Along a geodesic,

\[
\frac{d}{dt}g(\dot\gamma,\dot\gamma)
=2g(D_t\dot\gamma,\dot\gamma)=0.
\tag{3.1}
\]

Thus every nonconstant geodesic has a constant positive speed. Its affine parameter can be rescaled to unit speed.

The **energy** of a path on \([0,1]\) is

\[
E_g(\eta)=\tfrac12\int_0^1|\dot\eta|_g^2\,dt.
\]

Writing \(L=L_g(\eta)\), direct expansion gives

\[
\begin{aligned}
2E_g(\eta)-L^2
&=\int_0^1\bigl(|\dot\eta|_g-L\bigr)^2\,dt\\
&\ge0.
\end{aligned}
\tag{3.2}
\]

Equality holds precisely when the speed is constant on every smooth piece, with that same value on all pieces. Length disregards the rate of traversal; energy detects it.

**Theorem 3.1 (Gauss lemma).** Write \(E=\exp_p\). Wherever this map is defined, its differential satisfies

\[
\begin{gathered}
g_{E(v)}\bigl((dE)_v v,(dE)_v w\bigr)\\
=g_p(v,w).
\end{gathered}
\tag{3.3}
\]

This identity also holds for a pseudo-Riemannian metric, with its Levi-Civita connection.

**Proof.** For \(s\) near zero consider the smooth variation

\[
F(t,s)=\exp_p\bigl(t(v+sw)\bigr),
\qquad 0\le t\le1.
\]

It is defined for all these \(t\) and sufficiently small \(s\). The geodesic for \(v\) exists on a neighbourhood of \([0,1]\), and the smooth initial-value theorem supplies nearby solutions on that compact interval. Put \(T=\partial_tF\), \(S=\partial_sF\), as vector fields along the map \(F\).

The connection pulled back along \(F\) gives \(D_tT=0\). It also gives \(D_tS=D_sT\). To verify the latter without requiring \(F\) to be an immersion, compute in any target coordinates:

\[
\begin{aligned}
(D_tS)^k
&=\partial_t\partial_sF^k
+\Gamma^k_{ij}(F)\,\partial_tF^i\,\partial_sF^j,\\
(D_sT)^k
&=\partial_s\partial_tF^k
+\Gamma^k_{ij}(F)\,\partial_sF^i\,\partial_tF^j.
\end{aligned}
\]

The mixed partials agree, and the coefficients are symmetric in \(i,j\). These local identities agree on overlapping charts, so they hold throughout the variation.

Metric compatibility and constant geodesic speed now give

\[
\begin{aligned}
\partial_t g(T,S)
&=g(T,D_tS)=g(T,D_sT)\\
&=\tfrac12\partial_s g(T,T)\\
&=g_p(v+sw,w).
\end{aligned}
\]

At \(t=0\), \(F(0,s)=p\), hence \(S(0,s)=0\). Integration therefore gives \(g(T,S)=t\,g_p(v+sw,w)\). At \((t,s)=(1,0)\), the two fields are \((d\exp_p)_v v\) and \((d\exp_p)_v w\). This proves (3.3). Positivity was never used. □

In particular a radial geodesic is perpendicular to the images under \(\exp_p\) of spheres in \(T_pM\). The assertion is about one radial factor. It does not say that the whole differential of \(\exp_p\) is an isometry.

Suppose \(\exp_p\) maps the open metric ball \(B_R(0)\subset T_pM\) diffeomorphically onto \(U\). For a lifted curve \(v(t)\ne0\), write

\[
r(t)=|v(t)|_{g_p},\qquad u(t)=v(t)/r(t).
\]

Then \(g_p(u,u)=1\) and \(g_p(u,u')=0\). Since \(v'=r'u+ru'\), Gauss lemma gives

\[
\begin{gathered}
|\dot\eta|_g^2
=(r')^2+
\bigl|(d\exp_p)_{ru}(ru')\bigr|_g^2,\\
\eta(t)=\exp_p(v(t)).
\end{gathered}
\tag{3.4}
\]

The radial factor has unit length. Thus angular motion can only increase the speed beyond its radial component.

**Theorem 3.2 (a normal ball minimizes in the manifold).** With this normal ball, for every \(q=\exp_pv\in U\),

\[
d_g(p,q)=|v|_{g_p}.
\tag{3.5}
\]

The radial geodesic is the unique minimizing geodesic on \([0,1]\) from \(p\) to \(q\). More generally, every piecewise \(C^1\) path of that length traces this radial segment monotonically, with pauses allowed. Also

\[
U=\{q\in M:d_g(p,q)<R\}.
\tag{3.6}
\]

All distances are taken in the connected component of \(p\).

**Proof.** First let a competing path \(\eta:[a,b]\to U\) start at \(p\). Its lift \(v=\exp_p^{-1}\eta\) is piecewise \(C^1\). The radius \(r=|v|\) need not be differentiable when \(v=0\). To handle every return to the centre, use instead the smooth function of \(v\)

\[
r_\varepsilon(t)=\sqrt{|v(t)|_{g_p}^2+\varepsilon^2}.
\]

Where \(v\ne0\), equation (3.4) implies

\[
|r_\varepsilon'|
=\frac{r}{r_\varepsilon}|r'|
\le|\dot\eta|_g.
\tag{3.7}
\]

At \(v=0\), direct differentiation gives \(r_\varepsilon'=0\), so the same inequality holds. Integrate it over the finitely many smooth pieces. Their endpoint terms telescope. Letting \(\varepsilon\downarrow0\) yields

\[
L_g(\eta)\ge r(b)-r(a)=|v(b)|_{g_p}.
\tag{3.8}
\]

No differentiability assumption on \(r\) at its zero set is required. The radial geodesic has exactly this length, by its constant speed.

For equality, consider an open interval on a smooth piece where \(r>0\). If \(r'<0\), or if the angular term in (3.4) is nonzero at some interior point, continuity gives a smaller interval on which \(|\dot\eta|_g-r'\) is strictly positive. On that interval \(r_\varepsilon'\to r'\) uniformly. Everywhere else \(|\dot\eta|_g-r_\varepsilon'\ge0\). Integrating and taking the limit would make (3.8) strict. Therefore equality forces \(r'\ge0\) and \(u'=0\) wherever \(r>0\); injectivity of \(d\exp_p\) was used for the second conclusion.

On each connected component of \(\{r>0\}\), continuity across the finitely many parameter breaks makes \(u\) constant and \(r\) nondecreasing. Such a component cannot end before \(b\): its positive nondecreasing radius could not tend to zero at that endpoint. If \(q\ne p\), there is consequently one terminal positive component, with the constant direction of \(v(b)\), and the path is at \(p\) before it. Its radius is nondecreasing. This proves the stated rigidity. If \(q=p\), length zero makes every smooth-piece velocity zero, so the path is constant. Conversely monotone radial traversal, with pauses, has length \(r(b)\).

We must still compare with paths that leave \(U\). For \(r(q)<\rho<R\), the image of the closed tangent ball \(\overline B_\rho\) is compact and lies inside \(U\). Its boundary in \(M\) is \(\exp_p(S_\rho)\), because \(\exp_p\) is a homeomorphism there and the compact image is closed in \(M\). A path from \(p\) that leaves \(U\) first crosses this boundary. Its initial portion, including that boundary point, lies in \(U\), and (3.8) gives length at least \(\rho>r(q)\). Such a path cannot shorten the radial segment or tie its length. This proves (3.5) against every path in the manifold.

Among constant-speed minimizing paths on \([0,1]\), the rigidity just proved forces the unique parametrization \(t\mapsto\exp_p(tv)\). In particular this is the unique minimizing geodesic.

Every \(q\in U\) has distance less than \(R\). If \(q\notin U\), each path from \(p\) to \(q\) crosses \(\exp_p(S_\rho)\) for every \(\rho<R\), and hence has length at least \(R\). This proves (3.6). □

It follows that every geodesic minimizes on sufficiently short subintervals: centre a normal ball at a point on it and take a short enough initial tangent vector. No completeness hypothesis is needed.

### The same geometry in parallel frames

Choose an orthonormal frame \(e_0\) at \(p\) and transport it along each radial geodesic. This gives a smooth orthonormal frame \(e(x)\) on the normal ball. Smoothness at the centre follows from the smooth transport equation for the family \(t\mapsto\exp_p(tx)\).

Identify the tangent normal coordinates with \(\mathbb R^n\), and write \(\zeta(X)=e^{-1}X\) for the dual coframe and \(A\) for the frame potential. Thus \(\zeta\) is the solder form pulled back by the frame section. For the radial field \(\mathcal R=x^i\partial_i\),

\[
A(\mathcal R)=0,\qquad \zeta(\mathcal R)=x.
\tag{3.9}
\]

The first identity holds because the frame is radially parallel; the second because radial velocity has the initial-vector components \(x\) in that frame. Letting \(x=\varepsilon a\) tend to zero in the first identity gives \(A_0(a)=0\) for every \(a\), so the potential vanishes at the centre.

Away from the centre put \(x=ru\), \(|u|=1\). Pull forms back to \((0,R)\times S^{n-1}\), and decompose

\[
\zeta=u\,dr+\phi,\qquad A(\partial_r)=0.
\tag{3.10}
\]

Here \(\phi\) has only angular components. Gauss lemma says \(u^T\phi=0\). Orthonormality of the frame consequently expresses the metric as

\[
g=dr^2+\sum_i\phi^i\otimes\phi^i.
\tag{3.11}
\]

For \(n=1\) there are two radial directions and no angular term.

The structure equations give more information without making the radial frame a coordinate frame. With \(F=dA+A\wedge A\), zero torsion gives \(d\zeta=-A\wedge\zeta\). Evaluating these equations on \(\partial_r\) and any angular coordinate field \(W\) gives

\[
\begin{aligned}
\partial_r\phi(W)&=du(W)+A(W)u,\\
\partial_r A(W)&=F(\partial_r,W).
\end{aligned}
\tag{3.12}
\]

Indeed, differentiate \(\zeta(W)=\phi(W)\), use \(\zeta(\partial_r)=u\), and note that \([\partial_r,W]=0\). In the second equation \(A(\partial_r)=0\) removes both the angular derivative and the product terms. Both \(\phi(W)\) and \(A(W)\) tend to zero at \(r=0\): the angular vector in Cartesian coordinates is \(r\,du(W)\), and all Cartesian coefficients are smooth. Thus (3.12) records how angular lengths and the frame connection evolve outward from the centre. Its curvature term is

\[
F(\partial_r,W)
=e^{-1}R(eu,e\phi(W))e,
\]

by the tensor/frame correspondence of the preceding lesson.

## 4. Every pair in a small neighbourhood

An open set is **strongly convex** here if each ordered pair of its points has a unique minimizing geodesic in the whole manifold and that segment lies in the set. Uniqueness refers to the affine parametrization on \([0,1]\); length-minimizing paths can insert pauses.

**Theorem 4.1 (strongly convex normal neighbourhoods).** Every point of a Riemannian manifold has arbitrarily small strongly convex neighbourhoods \(V\). Their joining geodesics depend smoothly on the two endpoints. For each \(x\in V\), \(\exp_x\) maps an open star-shaped neighbourhood of zero diffeomorphically onto \(V\). On \(V\times V\), the squared distance \(d_g(x,y)^2\) is smooth, including at the diagonal.

**Proof.** Work near \(p\) in coordinates, and use the pair map

\[
\Phi(x,v)=(x,\exp_xv)
\]

from the complete affine-convexity proof in Geodesics, normal coordinates and curvature, Theorem 2.2. Its differential at \((p,0)\) is invertible. Choose an inverse-function domain \(O\) containing a product

\[
\{|x|<a,\ |v|<b\}.
\tag{4.1}
\]

Shrink \(a\) so that the metric comparison \(|v|_{g_x}\ge m|v|\), for some \(m>0\), holds uniformly for these base points. Choose \(0<\rho<mb\). For every such \(x\), the tangent metric ball \(\{|v|_{g_x}<\rho\}\) lies in its fibre of \(O\).

On this ball \(\exp_x\) is injective. Its differential in \(v\) is invertible too: the differential of \(\Phi\) has identity in its first diagonal block and \(d_v\exp_x\) in its second. Thus it maps this ball diffeomorphically onto an open normal ball. Theorem 3.2 applies in the whole manifold with the same radius \(\rho\) for all these \(x\).

Now use the affine-convexity construction with this same pair map. Its endpoint inverse \(v(x,y)\) is smooth and satisfies \(v(p,p)=0\). Shrink its endpoint neighbourhood until

\[
|v(x,y)|_{g_x}<\rho.
\tag{4.2}
\]

That construction then chooses an arbitrarily small \(V\) inside the base box, with every pair in this endpoint neighbourhood. It proves that the segment launched with \(v(x,y)\) stays in \(V\), is unique among geodesics staying there, and gives the asserted star-shaped exponential domains. Its velocity bound excludes competing confined segments with large initial velocity; none are silently discarded here.

By (4.2), this segment is also the radial segment of the normal ball centred at \(x\). Theorem 3.2 proves that it is the unique minimizing geodesic among all curves in \(M\), including curves leaving \(V\). Thus \(V\) is strongly convex. Smooth dependence comes from

\[
\gamma_{x,y}(t)=\exp_x\bigl(t\,v(x,y)\bigr).
\]

Its constant speed gives

\[
d_g(x,y)^2=g_x(v(x,y),v(x,y)).
\tag{4.3}
\]

Both the metric and endpoint inverse are smooth, so this expression is smooth even where \(x=y\). This proves all assertions. □

The distance itself is smooth off the diagonal in this neighbourhood, since it is the positive square root of (4.3). In positive dimension it is not generally differentiable at the diagonal: along a radial line from \(p\), Theorem 3.2 gives \(d_g(p,\exp_p(tv))=|t|\,|v|_{g_p}\). Squaring removes that corner.

Nothing in this theorem says that an arbitrary large normal ball is strongly convex for all pairs. On the sphere a normal ball can have radius nearly \(\pi\), whereas the strong convexity radius is only \(\pi/2\).

## 5. Two geometries made explicit

### Hyperbolic upper half-space

For \(n\ge2\), put

\[
\begin{gathered}
\mathbb H^n=\{(x,z):x\in\mathbb R^{n-1},\ z>0\},\\
g=\frac{|dx|^2+dz^2}{z^2}.
\end{gathered}
\tag{5.1}
\]

The coordinate \(z\) is the \(n\)-th coordinate. Substituting \(g_{ij}=z^{-2}\delta_{ij}\) in (2.7) gives

\[
\begin{aligned}
\Gamma^k_{ij}&=-\frac1z\bigl(\delta^k_i\delta_{jn}\\
&\quad+\delta^k_j\delta_{in}
-\delta_{ij}\delta^k_n\bigr).
\end{aligned}
\tag{5.2}
\]

Thus the geodesic equations are

\[
\begin{aligned}
x''-2\frac{z'}z x'&=0,\\
z''+\frac{|x'|^2-(z')^2}{z}&=0.
\end{aligned}
\tag{5.3}
\]

The first equation says that \(c=x'/z^2\) is a constant vector. Constant metric speed supplies a second conserved quantity:

\[
\kappa^2=\frac{|x'|^2+(z')^2}{z^2}.
\tag{5.4}
\]

If \(c=0\), the nonconstant solutions are the vertical geodesics

\[
x=b,\qquad z=a e^{\pm\kappa t},
\quad a>0.
\tag{5.5}
\]

Indeed, (5.4) then gives \(z'/z=\pm\kappa\); its sign cannot change when \(\kappa>0\). If \(\kappa=0\), the curve is constant.

If \(c\ne0\), all solutions instead have the form

\[
\begin{aligned}
x(t)&=b+R\tanh(\kappa(t-t_0))e,\\
z(t)&=R\operatorname{sech}(\kappa(t-t_0)),\\
e&=c/|c|,\qquad R=\kappa/|c|.
\end{aligned}
\tag{5.6}
\]

Here \(b\in\mathbb R^{n-1}\), \(R>0\), \(|e|=1\) and \(\kappa>0\). For a direct verification, set \(u=\kappa(t-t_0)\). Then

\[
\begin{aligned}
x'&=R\kappa\operatorname{sech}^2u\,e,\\
z'&=-R\kappa\operatorname{sech}u\,\tanh u.
\end{aligned}
\]

Differentiating once more verifies both equations (5.3), using \(\tanh^2u+\operatorname{sech}^2u=1\). The same identity verifies (5.4) and \(x'/z^2=(\kappa/R)e=c\).

These formulas supply every initial value, rather than only some geodesics. For initial position \((x_0,z_0)\) and velocity \((v_x,v_z)\) with \(v_x\ne0\), let

\[
\begin{gathered}
s=|v_x|,\qquad E=\sqrt{s^2+v_z^2},\\
e=v_x/s,\quad \kappa=E/z_0,\quad R=z_0E/s,\\
\tanh u_0=-v_z/E,\\
t_0=-u_0/\kappa,\qquad b=x_0-R\tanh u_0\,e.
\end{gathered}
\]

Since \(|v_z|<E\), the real number \(u_0\) exists uniquely. Also \(\operatorname{sech}u_0=s/E\). Substitution in (5.6) at zero gives exactly the prescribed position and velocity. Initial-value uniqueness then proves the assertion. The case \(v_x=0\) is covered by (5.5), with its sign and speed chosen from \(v_z\). All formulas exist for every real \(t\); this connection is geodesically complete.

The images in (5.6) are Euclidean semicircles:

\[
|x-b|^2+z^2=R^2,\qquad z>0.
\]

They lie in the vertical plane with horizontal direction \(e\), and meet the boundary plane orthogonally at their two ideal endpoints. Those boundary points are outside \(\mathbb H^n\); they are reached only as \(t\to\pm\infty\).

We can also prove global length minimization directly. For any competing path between \((x_1,z_1)\) and \((x_2,z_2)\),

\[
L_g(\eta)\ge\int\frac{|z'|}{z}\,dt
\ge\left|\log\frac{z_2}{z_1}\right|.
\tag{5.7}
\]

For equal horizontal coordinates, a vertical segment attains this bound. Equality in the first inequality forces \(x'=0\) on every smooth piece. Equality in the second makes \(\log z\) monotone: subtract its derivative with the sign of its endpoint difference and integrate the resulting continuous nonnegative functions. Thus every minimizing path traces the vertical segment monotonically. If the endpoints coincide, equality means a constant path.

To treat a circular geodesic, let \(a\) be a boundary point and consider

\[
I_a(q)=\frac{q-a}{|q-a|^2}.
\tag{5.8}
\]

Its inverse is \(y\mapsto a+y/|y|^2\), and both maps preserve the upper half-space. With \(h=q-a\),

\[
dI_a=|h|^{-2}
\left(I-2\frac{h\otimes h}{|h|^2}\right).
\]

The matrix in parentheses is an orthogonal reflection, and the new height is \(z/|h|^2\). The scale in its Euclidean differential therefore cancels the height scale in (5.1). This proves \(I_a^*g=g\), including the length of every piecewise smooth path.

For the geodesic (5.6), choose \(a=(b-Re,0)\). The identity

\[
|q-a|^2=2R^2(1+\tanh u)
\]

gives

\[
I_a(q(t))
=\left(\frac{e}{2R},\frac{e^{-u}}{2R}\right).
\tag{5.9}
\]

This is a vertical geodesic. Applying (5.7) to every transformed competitor proves that each finite circular segment is globally minimizing and is the unique minimizing trace. Its affine parametrization on \([0,1]\) is unique as well, by constant speed.

Finally, every distinct pair lies on one of these geodesics. Equal horizontal coordinates give the vertical case. Otherwise write \(x_2-x_1=De\), \(D>0\), and set

\[
\begin{gathered}
b=x_1+\lambda e,\qquad
\lambda=\frac{D^2+z_2^2-z_1^2}{2D},\\
R=\sqrt{\lambda^2+z_1^2}.
\end{gathered}
\]

Both points lie on the circle with this centre and radius. Their heights are positive, so (5.6) parametrizes both at finite values of \(u\). An affine change of time joins them on \([0,1]\). The preceding minimization proof gives uniqueness. This conclusion has been proved from the explicit metric; it does not use a global curvature-comparison theorem.

### The convexity radius of the round sphere

Give \(S^2\subset\mathbb R^3\) its unit round metric. The projected ambient connection in Geodesics, normal coordinates and curvature, Section 5, is compatible and has zero torsion. Theorem 2.1 identifies it as the Levi-Civita connection. That section proves

\[
\exp_pv=\cos|v|\,p+\frac{\sin|v|}{|v|}v
\tag{5.10}
\]

and proves that \(\exp_p\) maps \(|v|<\pi\) diffeomorphically onto \(S^2\setminus\{-p\}\). Consequently Theorem 3.2 gives

\[
\begin{gathered}
d_g(p,q)=\arccos(p\cdot q),\\
q\ne-p.
\end{gathered}
\tag{5.11}
\]

At \(-p\) the distance is \(\pi\) too. A semicircle has that length, giving the upper bound. For points tending to \(-p\), equation (5.11) tends to \(\pi\); Proposition 1.1 and the metric triangle inequality make \(q\mapsto d_g(p,q)\) continuous in the manifold topology. This gives the lower bound.

Fix \(p\). The open distance ball \(B_g(p,r)\) is strongly convex whenever

\[
0<r\le\pi/2.
\tag{5.12}
\]

To prove this, take distinct \(q_1,q_2\) in the ball. They cannot be antipodal, since \(p\cdot q_i>0\). Put \(\alpha=\arccos(q_1\cdot q_2)\in(0,\pi)\). Their shorter great-circle arc is

\[
\begin{aligned}
\gamma(t)&=
\frac{\sin((1-t)\alpha)}{\sin\alpha}\,q_1\\
&\quad+\frac{\sin(t\alpha)}{\sin\alpha}\,q_2.
\end{aligned}
\tag{5.13}
\]

For example, write \(q_2=\cos\alpha\,q_1+\sin\alpha\,w\), where \(w\) is a unit tangent to the sphere at \(q_1\). Then (5.13) becomes \(\cos(t\alpha)q_1+\sin(t\alpha)w\). This verifies its unit norm and its geodesic parameter. Theorem 3.2 centred at \(q_1\) proves that it is the unique globally minimizing geodesic.

For \(0<t<1\), let \(A,B\) be the two positive coefficients in (5.13). Since \(|Aq_1+Bq_2|=1\), the Euclidean triangle inequality gives \(A+B\ge1\). If \(r<\pi/2\), then

\[
p\cdot\gamma(t)>(A+B)\cos r\ge\cos r.
\]

If \(r=\pi/2\), positivity of both \(p\cdot q_i\) gives \(p\cdot\gamma(t)>0\) directly. The endpoints already belong to the ball, so the entire segment does. Equal endpoints give the constant segment. This proves (5.12), including the open hemisphere at the endpoint radius.

Larger balls fail. Rotate \(p\) to \((0,0,1)\). For \(\pi/2<r\le\pi\), choose \(\pi/2<\theta<r\) and put

\[
q_\pm=(\pm\sin\theta,0,\cos\theta).
\tag{5.14}
\]

Both points have distance \(\theta\) from \(p\). Their unique shorter arc has length \(2(\pi-\theta)<\pi\) and passes through the south pole \(-p\). One way to see this is to parametrize the meridian by \(m(\beta)=(\sin\beta,0,\cos\beta)\): the endpoints are \(m(\theta)\) and \(m(2\pi-\theta)\), and the interval between these angles contains \(\pi\). The south pole has distance \(\pi\ge r\), so the minimizing arc leaves the ball. For \(r>\pi\) the ball is the whole sphere, which has several minimizing semicircles between antipodal points. Thus its convexity radius, the supremum of radii up to which all smaller centred balls are strongly convex, is exactly \(\pi/2\).

This example distinguishes two assertions. The exponential chart about \(p\) remains nonsingular and injective up to radius \(\pi\). Controlling the minimizing segment between every pair requires the smaller threshold \(\pi/2\).

![Upper half-plane geodesics and two meridian sections of the sphere: the smaller cap contains the shorter joining arc, while the larger cap loses it through the south pole.](figures/normal-and-convex.png)

*Figure 5.1.* Panel A shows Euclidean coordinate images of hyperbolic geodesics from (5.5)–(5.6); its vertical scale is the coordinate \(z\), and lengths are measured by (5.1). Panels B and C are meridian sections of the unit sphere, with the ball shown in green and its excluded endpoints marked by hollow circles. The blue or red arc is the unique shorter geodesic between the marked \(q_\pm\). Their radii and endpoint angles are in radians. The example in C implements (5.14): the shorter arc crosses the south pole outside the ball. Vector illustration and editable drawing source.

## 6. Exercises and complete solutions

### Exercise 6.1 (easy): a metric with one varying scale

Let \(f:\mathbb R\to(0,\infty)\) be smooth, and give the plane the metric \(g=dx^2+f(x)^2dy^2\). Find all its connection coefficients and geodesic equations. Specialize them to \(f(x)=e^x\).

**Solution.** The metric and its inverse are diagonal, with entries \(1,f^2\) and \(1,f^{-2}\). The only nonzero metric derivative is \(\partial_xg_{yy}=2ff'\). Formula (2.7) therefore gives

\[
\begin{gathered}
\Gamma^x_{yy}=-ff',\\
\Gamma^y_{xy}=\Gamma^y_{yx}=f'/f.
\end{gathered}
\tag{6.1}
\]

All other coefficients vanish: each corresponding summand contains either a zero metric entry or a derivative of a constant entry. Hence

\[
x''-ff'(y')^2=0,\qquad
y''+2(f'/f)x'y'=0.
\]

For \(f=e^x\), these become \(x''-e^{2x}(y')^2=0\) and \(y''+2x'y'=0\). The curves \(y=\text{constant}\), \(x=at+b\), are geodesics. A curve \(x=\text{constant}\) with nonzero \(y'\) is not: its first equation would require \(-e^{2x}(y')^2=0\). Varying metric scale bends those coordinate lines even though the chart is the whole plane. □

### Exercise 6.2 (medium): torsion invisible to geodesics

Let \(g\) be a pseudo-Riemannian metric, let \(\nabla\) be its Levi-Civita connection, and let \(H\) be a smooth three-form. Define \(K\) by

\[
g(K(X,Y),Z)=\tfrac12H(X,Y,Z).
\tag{6.2}
\]

Show that \(\nabla'=\nabla+K\) is metric and has the same geodesics with the same affine parameters. Compute its torsion. Conversely, prove that every metric connection with these same parametrized geodesics arises from exactly one such \(H\).

**Solution.** Nondegeneracy makes (6.2) a well-defined smooth tensor. The difference between the metric-compatibility identities for \(\nabla'\) and \(\nabla\) is

\[
\begin{gathered}
g(K(X,Y),Z)+g(Y,K(X,Z))\\
=\tfrac12\bigl(H(X,Y,Z)+H(X,Z,Y)\bigr)\\
=0.
\end{gathered}
\]

Thus \(\nabla'\) is metric. Alternation in \(X,Y\) gives \(K(v,v)=0\), so its geodesic equation agrees with that of \(\nabla\). Since \(\nabla\) has zero torsion,

\[
\begin{aligned}
T'(X,Y)&=K(X,Y)-K(Y,X)\\
&=2K(X,Y).
\end{aligned}
\tag{6.3}
\]

Equivalently \(g(T'(X,Y),Z)=H(X,Y,Z)\).

Conversely let \(K=\nabla'-\nabla\). The difference of two connections is a tensor. Launching their common geodesic with every initial vector gives \(K(v,v)=0\). Polarization makes \(K\) skew in its two inputs, as proved in Geodesics, normal coordinates and curvature, Section 1. Metric compatibility makes \(g(K(X,Y),Z)\) skew in its last two arguments. Skewness under the adjacent swaps \((X,Y)\) and \((Y,Z)\) makes it alternating under every swap, since the swap \((X,Z)\) is a composition of three adjacent swaps. Hence

\[
H(X,Y,Z)=2g(K(X,Y),Z)
\]

is a smooth three-form and satisfies (6.2). This formula also proves its uniqueness. In dimension less than three, every three-form is zero, so the Levi-Civita connection is the only metric connection with these parametrized geodesics. □

### Exercise 6.3 (medium): the cost of a radial excursion

Suppose \(\exp_p:B_R(0)\to U\) is a normal ball. A piecewise \(C^1\) path in \(U\) starts at \(p\), ends at \(q\) of radius \(r_0\), and at some time visits radius \(\rho>r_0\). Prove

\[
L_g(\eta)\ge 2\rho-r_0.
\tag{6.4}
\]

Show that the bound is sharp, and that nonzero angular motion on an interval away from the centre makes it strict.

**Solution.** Equation (3.7), integrated with either sign, gives for any subpath in \(U\)

\[
L_g(\eta|_{[a,b]})\ge|r(b)-r(a)|.
\]

This follows by letting \(\varepsilon\downarrow0\) after integration, so zeros of the lifted path cause no difficulty. Split at a time when its radius is \(\rho\). The two portions cost at least \(\rho\) and \(\rho-r_0\), respectively, proving (6.4).

If \(q\ne p\), follow its radial direction from radius zero to \(\rho\), then return along that same ray to \(r_0\). This path lies in \(U\), since \(\rho<R\), and has length \(2\rho-r_0\). If \(q=p\), use any unit tangent direction and return to the centre; the length is \(2\rho\). In positive dimension this proves sharpness in all cases. In dimension zero the assumed visit to a positive radius cannot occur.

Where \(r>0\) and \(u'\ne0\), invertibility of \(d\exp_p\) and (3.4) give \(|\dot\eta|_g>|r'|\). Continuity produces a subinterval with a positive integrated gap. The corresponding subpath inequality is then strict, by the same regularized-radius argument as in Theorem 3.2. Adding the inequalities for the two portions makes (6.4) strict. □

### Exercise 6.4 (hard): a finite distance with no shortest path

Give \(M=\mathbb R^2\setminus\{0\}\) its Euclidean metric, and let \(p=(-1,0)\), \(q=(1,0)\). Prove that \(d_g(p,q)=2\), but no piecewise \(C^1\) path realizes this distance. Explain why this does not contradict Theorem 4.1.

**Solution.** Integrating Euclidean speed bounds every path's length below by its Euclidean endpoint displacement, which is \(2\). For \(0<\varepsilon<1\), join \(p\) to \((-\varepsilon,0)\) by a straight segment, go around the upper semicircle of radius \(\varepsilon\), and follow a straight segment from \((\varepsilon,0)\) to \(q\). The origin is avoided and the length is

\[
2(1-\varepsilon)+\pi\varepsilon
=2+(\pi-2)\varepsilon.
\]

Taking \(\varepsilon\downarrow0\) proves \(d_g(p,q)=2\).

Suppose a path of length \(2\) existed. On each smooth piece, the nonnegative continuous function

\[
\sqrt{(x')^2+(y')^2}-x'
\]

would have integral zero, since the total integral of \(x'\) is \(2\). It therefore vanishes everywhere on each piece. This forces \(y'=0\) and \(x'\ge0\). Continuity across the breaks gives \(y=0\) along the whole path. The continuous function \(x\) goes from \(-1\) to \(1\), so it takes the value zero. The path would pass through the missing origin, a contradiction.

Theorem 4.1 gives a sufficiently small neighbourhood around each individual point; it does not put these two points in one strongly convex neighbourhood or promise a global minimizer. The puncture obstructs this particular infimum from being attained. □

## References

- **[Pinkall–Gross]** Ulrich Pinkall and Oliver Gross, *Differential Geometry: From Elastic Curves to Willmore Surfaces*, Springer, 2024, Chapter 9, [Levi-Civita Connection](https://link.springer.com/chapter/10.1007/978-3-031-39838-4_9). The chapter is distributed under CC BY 4.0 and treats the induced connection of an immersed surface.
- **[Valencia]** Fabricio Valencia, *Notes on flat pseudo-Riemannian manifolds*, English translation by Elizabeth Gasparim, August 2018; published in *Pro Mathematica* 30 (60), 2019, Section 4. [Open article](https://revistas.pucp.edu.pe/index.php/promathematica/en/article/view/21091), CC BY 4.0.
- **[Durrer]** Ruth Durrer, *General Relativity*, lecture notes, revised 2016, Section 3.6. [Freely available author notes](https://fiteoweb.unige.ch/~durrer/courses/relaE.pdf).
