# Curvature and holonomy groups

*Written by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026. Self-checked by the writing AI. Original text dedicated to the public domain under CC0 1.0.*

Transport around a loop can return a frame rotated relative to its starting position. Curvature measures the local failure of horizontal directions to close under brackets. Holonomy collects the resulting transformations for all loops. The two notions have different scales: curvature is a tensor, while the full holonomy group also remembers the topology of the base.

Take first Connections and parallel transport, including its whole-interval lifting proof, and the constant-rank proof in [Local tools for bundles and transport](local-tools-for-bundles-and-transport.md#section-1). We use the definitions of differential forms and the Lie bracket of vector fields. Section 1 specifies the exterior-derivative convention and verifies the identities needed here. The base \(M\) is connected, Hausdorff and second countable. A basic reference is [Meinrenken].

## 1. Exterior calculus with Lie algebra coefficients

For a scalar one-form \(a\), our convention is

\[
da(X,Y)=X(a(Y))-Y(a(X))-a([X,Y]).
\]

There is no factorial in evaluation on an ordered list of tangent vectors. In coordinates, \(d(a_i\,dx^i)=\partial_j a_i\,dx^j\wedge dx^i\). The alternating product is the ordinary exterior product. These conventions will also determine the later curvature-tensor signs.

Choose a basis \(e_a\) of \(\mathfrak g\). For \(\alpha=\sum_a\alpha^a e_a\) and \(\beta=\sum_b\beta^b e_b\), define

\[
[\alpha,\beta]=\sum_{a,b}\alpha^a\wedge\beta^b[e_a,e_b],\qquad
d\alpha=\sum_a d\alpha^a e_a.
\]

For degrees \(p,q\), these operations satisfy

\[
[\alpha,\beta]=-(-1)^{pq}[\beta,\alpha],\qquad
d[\alpha,\beta]=[d\alpha,\beta]+(-1)^p[\alpha,d\beta].
\]

They satisfy the graded Jacobi identity as well. To verify all three formulas, expand into scalar coefficient forms. The first two become, respectively, the sign rule for the exterior product and its Leibniz rule. In the cyclic sum for Jacobi, move the scalar forms into the same order; the resulting coefficient is the ordinary Jacobi sum in \(\mathfrak g\), hence zero. Also \(d^2=0\): each coefficient is a sum of second derivatives contracted with antisymmetric coordinate wedges, so mixed partial derivatives cancel in pairs. The coordinate formula transforms naturally under smooth pullback by the chain rule; it therefore defines these operations on manifolds independently of a chart.

For a one-form \(\omega\),

\[
\tfrac12[\omega,\omega](X,Y)=[\omega(X),\omega(Y)].
\]

The factor one-half compensates for the two terms produced by the wedge. It does not alter our evaluation convention.

## 2. Curvature as a horizontal tensor

Let \(h:TP\to HP\) be the horizontal projection. Define the **curvature form** by

\[
\Omega_p(Z,W)=d\omega_p(hZ,hW).
\]

It is horizontal, meaning that it vanishes when one argument is vertical. It is equivariant because \(h\) is equivariant and pullback commutes with exterior differentiation.

**Theorem 2.1 (structure equation).** A principal connection satisfies

\[
\Omega=d\omega+\tfrac12[\omega,\omega].
\]

For horizontal vector fields \(U,V\), it follows that

\[
\omega([U,V])=-\Omega(U,V).
\]

**Proof.** Differentiate \(R_{\exp(t\xi)}^*\omega=\operatorname{Ad}(\exp(-t\xi))\omega\). The derivative is \(\mathcal L_{\xi^\#}\omega=-[\xi,\omega]\). Evaluating the exterior-derivative formula on \(\xi^\#,Z\) gives

\[
d\omega(\xi^\#,Z)=(\mathcal L_{\xi^\#}\omega)(Z)-Z(\omega(\xi^\#))
=-[\xi,\omega(Z)],
\]

since \(\omega(\xi^\#)=\xi\) is constant. The bracket term gives \([\xi,\omega(Z)]\), so their sum vanishes on every vertical argument. The sum is also equivariant: both differentiation and the bracket commute with the fixed linear map \(\operatorname{Ad}(a^{-1})\). On horizontal arguments the bracket term vanishes, and the sum agrees with the definition of \(\Omega\). Splitting each argument into horizontal and vertical parts proves equality everywhere. Finally, the exterior-derivative formula on horizontal fields reduces to \(d\omega(U,V)=-\omega([U,V])\). □

A horizontal equivariant \(\mathfrak g\)-valued form corresponds to an \(\operatorname{ad}(P)\)-valued form on \(M\): lift each base argument, evaluate, and take its associated class. Independence of the lifts follows from horizontality; independence of the frame follows from equivariance. The inverse uses the unique Lie algebra coordinate in a chosen frame. This is the form-valued version of the section correspondence proved in the bundle lesson, and its local product charts verify smoothness in both directions.

For a local section with potential \(A\), the local curvature is

\[
F=s^*\Omega=dA+\tfrac12[A,A].
\]

If \(s_j=s_i g_{ij}\), then \(F_j=\operatorname{Ad}(g_{ij}^{-1})F_i\). Indeed, in differentiating \(s_i(x)g_{ij}(x)\), the extra derivative of \(g_{ij}\) is vertical and is annihilated by \(\Omega\). On the remaining arguments equivariance gives the formula. Curvature therefore transforms tensorially, although the potential does not.

## 3. The Bianchi identity and induced curvature

For a horizontal equivariant form \(\alpha\), define its exterior covariant derivative by \(D\alpha=(d\alpha)\circ h\) in every argument. Equivalently,

\[
D\alpha=d\alpha+[\omega,\alpha].
\]

To verify the equivalence, note that \(\mathcal L_{\xi^\#}\alpha=-[\xi,\alpha]\). From the coordinate formula for exterior differentiation, contraction satisfies

\[
\iota_{\xi^\#}d\alpha=\mathcal L_{\xi^\#}\alpha-d\iota_{\xi^\#}\alpha=-[\xi,\alpha].
\]

The contraction identity itself follows on a coefficient function and on \(dx^i\), then on their exterior products by the Leibniz rules. Because \(\alpha\) is horizontal, contraction of \([\omega,\alpha]\) is \([\xi,\alpha]\). Thus the sum is horizontal; on horizontal arguments it is just \(d\alpha\). It is equivariant by the same coefficient check as before, proving the claim.

**Theorem 3.1 (Bianchi identity).** \(D\Omega=0\).

**Proof.** Differentiate the structure equation using the graded rules of Section 1:

\[
d\Omega=\tfrac12\bigl([d\omega,\omega]-[\omega,d\omega]\bigr)
=[d\omega,\omega].
\]

On the other hand,

\[
[\omega,\Omega]=[\omega,d\omega]+\tfrac12[\omega,[\omega,\omega]].
\]

The first term cancels \(d\Omega\). Graded Jacobi with three degree-one copies of \(\omega\) gives \(3[\omega,[\omega,\omega]]=0\), so the remaining term vanishes over \(\mathbb R\). Hence \(d\Omega+[\omega,\Omega]=0\), which is the desired identity. □

The same computation gives \(D^2\alpha=[\Omega,\alpha]\): expand \((d+[\omega,\cdot])^2\), cancel the two terms containing \(d\alpha\), and use graded Jacobi to replace \([\omega,[\omega,\alpha]]\) by \(\tfrac12[[\omega,\omega],\alpha]\). Therefore covariant differentiation is generally not a cochain differential.

For \(E=P\times_GV\) with induced derivative \(\nabla\), extend it to vector-valued forms by

\[
\nabla(a\otimes v)=da\otimes v+(-1)^{\deg a}a\wedge\nabla v.
\]

In a local frame this is \(d+\rho_*(A)\wedge\). Squaring gives multiplication by

\[
\rho_*(F)=d\rho_*(A)+\rho_*(A)\wedge\rho_*(A),
\]

because differentiating the middle term cancels the other occurrence of \(A\wedge dv\), and \(\rho_*\) preserves the Lie bracket. Thus the endomorphism curvature is

\[
R^E(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}.
\]

For a \(\mathrm{GL}(V)\)-frame bundle, the representation is the defining representation, so its principal and vector-bundle curvature contain exactly the same information.

## 4. A Lie subgroup constructed from smooth families

The subgroup underlying holonomy need not be closed in \(G\). A theorem about closed subgroups therefore cannot establish the assertion we need. We prove the requisite immersed-subgroup construction directly.

**Lemma 4.1 (smoothly generated subgroup).** Let \(\mathcal C\) be a family of smooth maps into a finite-dimensional Lie group \(G\), each defined on a connected open subset of some \(\mathbb R^m\) and taking the value \(e\). The subgroup \(H\) generated by all their values has a connected second-countable Lie-group structure for which its inclusion in \(G\) is an injective immersion. Every finite product of the generating maps, with their parameters varying independently, is smooth as a map into this Lie group. The subgroup topology may be finer than its subspace topology.

**Proof.** Consider all smooth maps obtained by finite products of generating maps and their inverses, allowing constants which are themselves such products, restrictions to open sets, and fixed input variables. Their ranks are integers between zero and \(\dim G\). Let \(r\) be the largest rank achieved. Choose a product map achieving it, translate its value to \(e\), and fix all but \(r\) independent input variables. The resulting map \(f\) is an embedding of a small open ball in \(\mathbb R^r\) into \(G\), with image \(S\subset H\) containing \(e\). Its rank is \(r\). If \(r=0\), all generating maps have zero derivative and are constant on their connected domains, so \(H=\{e\}\); the rest of the proof concerns \(r>0\).

Whenever a product map \(K\) has value \(e\) at a parameter \(z_0\), the map \((x,z)\mapsto f(x)K(z)\) still belongs to this collection. Its rank is at most \(r\) everywhere, and at least \(r\) near \((0,z_0)\), by its \(x\)-derivative. It has constant rank there. The constant-rank proof in the local-tools lesson shows its local image is an embedded \(r\)-dimensional submanifold. This image contains \(f(x)\), so its germ at \(e\) agrees with the germ of \(S\): inclusion between two embedded manifolds of equal dimension is locally a diffeomorphism, by the inverse function theorem in their charts. Consequently \(K(z)\in S\) for \(z\) sufficiently near \(z_0\), and its \(S\)-coordinate is smooth.

Apply this observation to \(K=f(y)\), \(K=f(y)^{-1}\), and to the product map \(f(x)f(y)^{-1}\). After shrinking, products and inverses of sufficiently small elements of \(S\) stay in \(S\); their coordinates are smooth. The same constant-rank argument at \((x_0,z_0)\), with \(K(z_0)=e\), shows that multiplying elements near \(f(x_0)\) by sufficiently small elements of \(S\) stays in \(S\). Indeed the local image has dimension \(r\) and contains the germ of \(f(x)\) at \(f(x_0)\). Apply the identity-point observation also to \(K(z)=k f(z)k^{-1}\) for any fixed \(k\in H\). This proves that conjugation takes a sufficiently small piece of \(S\) smoothly into \(S\). Its differential on \(T_eS\) is injective and hence invertible, since its inverse is conjugation by \(k^{-1}\). These are the local group and conjugation charts needed below.

Every generating map lies in the subgroup generated by a small symmetric piece of \(S\). Such a piece exists: inversion is a local diffeomorphism of the identity chart, so intersect a sufficiently small chart with its inverse. For any parameter \(z_0\), the map \(c(z_0)^{-1}c(z)\) is a product map with value \(e\) at \(z_0\), so it lies in that piece for nearby \(z\). Membership of \(c(z)\) in the subgroup generated by the piece is therefore locally constant, including at points outside the subgroup. Since the parameter domain is connected and the map takes the value \(e\), membership holds everywhere. Thus \(H\) is generated by that piece of \(S\).

Use all translates \(kS\) as charts of \(H\). If two charts meet at \(y\), both contain \(yS'\) for a sufficiently small piece \(S'\) of the identity chart, by the local product property. Their transition is smooth: each chart is embedded in \(G\), and locally their images agree with the same embedded manifold \(yS'\). This defines a manifold topology, with continuous injective inclusion into \(G\); distinct points are separated by ambient open sets, so it is Hausdorff. Multiplication is smooth in these charts, since near \((k,\ell)\) it reduces to

\[
(s,t)\longmapsto k\ell\,(\ell^{-1}s\ell)t,
\]

and both conjugation and local multiplication have just been proved smooth. Inversion is handled in the same way. The inclusion is an immersion because every translated chart is embedded in \(G\).

Finally, \(H\) is the union of the images of finite products of a connected small symmetric identity chart. Each finite product map is smooth into the newly constructed manifold: around any input, multiply by its constant output inverse and apply the constant-rank observation to its increments. It is a submersion, since varying one factor supplies the full \(r\)-dimensional tangent space by group translation. A submersion is open in local projection coordinates. Images of countable product-chart bases under these maps therefore give a countable basis for \(H\). The images are connected and all contain \(e\); their union is connected. This proves every assertion. □

The argument also proves a useful additional fact: a smooth product family whose increments belong to the generating family is smooth in the immersed subgroup, even when continuity into the subgroup does not follow merely from ambient continuity.

## 5. Small loops and the topology of the base

A **small lasso based at \(x\)** is a path from \(x\) to a point \(y\), then a loop contained in a coordinate ball around \(y\), then the reverse of the first path. A coordinate ball means the image of a convex Euclidean ball under a chart. Its loop contracts to \(y\) by affine interpolation of its coordinates. Keeping the first and last paths fixed gives a contraction of the lasso as a based loop.

**Lemma 5.1 (finite lasso factorization).** Every finitely piecewise \(C^1\) nullhomotopic based loop is a product of finitely many small lassos and their inverses, up to inserting or deleting a path followed by its reverse. The lasso loops may be chosen finitely piecewise \(C^1\). Each lasso's holonomy is a value of a smooth curve of holonomies of nullhomotopic loops starting at the identity.

**Proof.** Choose a continuous based nullhomotopy on the square, with the original loop on its top edge and the constant loop on its bottom and vertical edges. Cover its compact image by coordinate balls. Pulling back a finite refinement and using the compactness argument for subdivisions in the transport lesson, subdivide the square into sufficiently small rectangles so that the image of the closed star of each rectangle lies in a coordinate ball. A closed star includes the rectangle and its neighbours, which gives room for the edge choices that follow.

Keep the top boundary paths equal to the given loop, subdividing additionally at its finitely many breaks, and keep the other boundary paths constant. On each interior grid edge replace the continuous image path by a finitely piecewise smooth path with the same vertex values, sufficiently close to the original image that it stays in every coordinate ball assigned to an adjacent rectangle. Here is a direct construction of that replacement. The intersection of the finitely many relevant balls is open and contains the compact image of the edge. Cover that image by smaller coordinate balls whose closures lie in the intersection. Subdivide the edge so each subpath lies in one of them, and join its endpoints by the straight segment in that smaller chart. These finitely many segments have the required endpoints and containment. Choose the same path for both uses of any shared edge.

Each rectangle now has a piecewise smooth boundary loop lying in a convex coordinate ball. The top boundary loop is a product of conjugates of these face loops. To see the algebraic identity, attach the rectangles one at a time along a grid traversal. The boundary of a union changes by multiplying by the boundary of the newly attached face, conjugated by an edge path from the base vertex to its attachment vertex. Shared edges occur with opposite directions and cancel as a path followed by its reverse. Induction over rows and columns gives the full outer boundary. The three constant outer sides can then be deleted. This proves the factorization; no transport invariance under homotopy has been assumed.

For a face loop \(\mu\) based at \(y\), let \(\mu_s\) have chart coordinates \(y+s(\mu(t)-y)\), \(0\leq s\leq1\). Its coefficients are smooth in \(s\), and piecewise \(C^1\) in \(t\), with one fixed finite subdivision. The parameter version of the integral-equation proof gives smooth holonomy in \(s\): continuity in time and uniformly smooth parameter derivatives suffice for that proof. These formulas extend to a slightly larger open \(s\)-interval since the original compact loop lies inside the coordinate ball. Adjoining the fixed outgoing and return paths preserves smooth parameter dependence. At \(s=0\) the lasso is a path followed by its reverse, whose transport is the identity. At \(s=1\) its transport is the original lasso holonomy. □

**Lemma 5.2 (countable fundamental group).** The fundamental group of a connected second-countable manifold is countable.

**Proof.** Take a countable cover by simply connected coordinate balls \(U_i\), choose a centre in each, and choose one point in every path component of every nonempty \(U_i\cap U_j\). There are only countably many such components: each is open, by local path connectivity, and contains a member of a countable basis distinct from those chosen in other components. For each chosen intersection point choose paths to the two centres in their respective balls, and choose a fixed path from the base point to each centre. This is countable data.

Subdivide any loop into finitely many segments lying in successive balls. At each joining point, move the joining point to the chosen representative in its intersection component, along a path in that component. Adjoin this path to one neighbouring segment and its inverse to the other; these insertions cancel. In a simply connected ball any two paths with the same endpoints are homotopic relative to the endpoints: their concatenation is a loop there and a contraction gives the path homotopy. Thus each resulting segment can be replaced by the two fixed centre paths just chosen. The loop is consequently represented by a finite word in countably many fixed paths and their reverses, together with the fixed base-to-centre paths. There are countably many finite words over a countable alphabet. This proves countability. It also shows that every homotopy class has a piecewise smooth representative, since paths in a chart can be replaced by finite coordinate segments as in Lemma 5.1. □

## 6. Full and restricted holonomy

Fix \(p\in P_x\). For a based loop \(\gamma\), write

\[
T_\gamma(p)=p\,h_\gamma.
\]

The set of all \(h_\gamma\) is the **holonomy group** \(\operatorname{Hol}_p\). Restricting to nullhomotopic loops gives \(\operatorname{Hol}_p^0\), the **restricted holonomy group**. Both are subgroups: transport reversal gives inverses, and concatenation gives products. With our convention that \(\gamma*\delta\) travels first along \(\gamma\), equivariance gives

\[
h_{\gamma*\delta}=h_\delta h_\gamma.
\]

Remembering this reversed order avoids a sign or multiplication error in loop calculations.

**Theorem 6.1 (holonomy is an immersed Lie subgroup).** \(\operatorname{Hol}_p^0\) is a connected immersed Lie subgroup of \(G\). It is a normal subgroup of \(\operatorname{Hol}_p\), which is itself an immersed Lie subgroup with identity component \(\operatorname{Hol}_p^0\). The quotient \(\operatorname{Hol}_p/\operatorname{Hol}_p^0\) is countable.

**Proof.** Take all smooth pointed families of holonomies of nullhomotopic loops, with parameters in connected open Euclidean sets, fixed finite time subdivisions, piecewise \(C^1\) time dependence, and smooth parameter dependence of every coefficient and time derivative. Include the contracting small lassos of Lemma 5.1. Parameter dependence of the transport equation proves smoothness into \(G\). All values lie in the restricted group, and the lasso families already generate it. Lemma 4.1 therefore gives its connected immersed Lie structure, including second countability. In particular, every family just specified is smooth into that structure. For a family of mutually homotopic loops that does not take the identity value, compose its transport with the inverse transport at one fixed parameter. This produces a pointed nullhomotopic family locally, so the original family is smooth into a coset of the restricted group.

Conjugating a nullhomotopic based loop by any based loop keeps it nullhomotopic. The transport product rule proves normality. If two based loops are homotopic, their concatenation with an appropriate reverse is nullhomotopic, so their holonomies have the same coset modulo the restricted group. Consequently \([\gamma]\mapsto h_\gamma^{-1}\operatorname{Hol}_p^0\) is a surjective homomorphism from \(\pi_1(M,x)\) to this quotient. Lemma 5.2 proves that the quotient is countable.

Give the full group the disjoint-union manifold structure of its countably many cosets of the restricted group. Left translation identifies each with the restricted group. Conjugation by any full-holonomy element is smooth on the restricted group: on each generating contraction family it is again the contraction holonomy of a small lasso, with an additional fixed outgoing and return loop. Thus it is smooth on the product charts constructed in Lemma 4.1. The inverse conjugation is of the same form. In the coset charts, multiplication and inversion therefore reduce to multiplication, inversion and these smooth conjugations in the restricted group. They are smooth. The full inclusion is an injective immersion, Hausdorffness follows from ambient separation, and countably many second-countable cosets give second countability. These cosets are connected and open, so the identity component is exactly the restricted group. □

If \(a\in G\), changing the frame to \(pa\) gives

\[
\operatorname{Hol}_{pa}=a^{-1}\operatorname{Hol}_p a,
\qquad
\operatorname{Hol}_{pa}^0=a^{-1}\operatorname{Hol}_p^0 a.
\]

Indeed, \(T_\gamma(pa)=T_\gamma(p)a=pa(a^{-1}h_\gamma a)\). If \(q=T_\lambda(p)\), then \(\operatorname{Hol}_q=\operatorname{Hol}_p\), and likewise for restricted groups: put loops at \(q\)'s base point between \(\lambda\) and its reverse, and use the transport rules. Since a connected manifold is path connected (its path components are open in charts), all holonomy groups on a connected base are conjugate in \(G\).

## 7. Worked examples

For the Hopf connection, write \(w=x+iy\) and \(D=1+x^2+y^2\). The potential from the preceding lesson is

\[
A_0=i\frac{x\,dy-y\,dx}{D},\qquad
F_0=dA_0=\frac{2i\,dx\wedge dy}{D^2}.
\]

In polar coordinates this is \(2ir(1+r^2)^{-2}dr\wedge d\phi\). The sphere's positively oriented area form in this chart is \(4D^{-2}dx\wedge dy\), so the curvature is \(i/2\) times that area form. Its integral is \(2\pi i\). The latitude transport found earlier takes values \(\exp(-2\pi i r^2/(1+r^2))\) for \(0\leq r<\infty\), giving every element of \(U(1)\). Since these loops contract in the chart, both full and restricted holonomy are \(U(1)\). For the tautological line the Chern-form convention \(iF/(2\pi)\) gives integral \(-1\), agreeing with its transition \(|w|/w\). The identification of that form with the topological Chern class is proved in the characteristic-class course, rather than assumed in this computation.

On the unit sphere, the tangent connection obtained by orthogonally projecting the derivative in \(\mathbb R^3\) preserves the induced metric. In spherical coordinates away from the poles, use the oriented orthonormal vectors \(e_\theta,e_\phi\). Differentiating their Euclidean coordinate expressions and taking tangential components gives

\[
\nabla_{\partial_\phi}e_\theta=\cos\theta\,e_\phi,
\qquad
\nabla_{\partial_\phi}e_\phi=-\cos\theta\,e_\theta.
\]

Thus the matrix potential along a latitude is \(\cos\theta\,J\,d\phi\), with \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\). One circuit gives \(\exp(-2\pi\cos\theta J)\). To compare them at one fixed base frame, adjoin an outgoing meridian and its reverse. This conjugates the rotation by an oriented isometry; conjugation in \(\mathrm{SO}(2)\) has no effect. These based lassos are contractible, and their values exhaust \(\mathrm{SO}(2)\) as \(\theta\) varies. Transport preserves orientation and the metric, so the full and restricted holonomy groups are exactly \(\mathrm{SO}(2)\). The projected connection is torsion-free: for tangent fields its torsion is the tangential projection of \(D_XY-D_YX-[X,Y]=0\), which follows from the coordinate formula for the bracket. The later uniqueness theorem therefore identifies it with the Levi-Civita connection.

For a flat torus \(\mathbb R^n/\Lambda\), the constant coordinate frame descends to a global frame and its potential is zero. All transport preserves that frame, so both holonomy groups are trivial for this connection. Again it is metric-compatible and torsion-free, hence is the Levi-Civita connection once that theorem has been proved.

For a nonclosed example, take the trivial \(U(1)\)-bundle over the circle with potential \(A=i\alpha\,d\theta\), where \(\alpha\) is irrational and \(d\theta\) is the global one-form induced from the real line. A loop lifts to an angle path on \(\mathbb R\): choose inverses on successive circle arcs and adjust them by multiples of \(2\pi\) at the joining points. Its final minus initial angle is \(2\pi n\), so transport is \(e^{-2\pi i\alpha n}\). Every integer occurs. A loop with zero angle increment contracts by linearly contracting its lifted angle path and projecting to the circle; a nullhomotopic loop has zero increment, since this integer is unchanged continuously during a homotopy. Thus restricted holonomy is trivial, while full holonomy is the dense countable cyclic subgroup generated by \(e^{-2\pi i\alpha}\). Its Lie-group topology is discrete. Its closure in \(U(1)\) has positive dimension, illustrating why taking the closure would give the wrong holonomy Lie algebra.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** For a product \(U(1)\)-bundle over \(\mathbb R^2\) with potential \(A=i(x\,dy-y\,dx)\), compute curvature and transport around a circle of radius \(r\).

**Solution.** The bracket term is zero, so \(F=2i\,dx\wedge dy\). On the circle, \(A=ir^2d\phi\), and the scalar transport equation gives multiplier \(e^{-2\pi ir^2}\). All loops used here are contractible.

**Exercise 8.2 (medium).** For a matrix-group connection, verify the Bianchi identity in a local chart and explain why replacing it by \(dF=0\) is incorrect.

**Solution.** Write \(F=dA+A\wedge A\). Then \(dF=dA\wedge A-A\wedge dA\), while \(A\wedge F-F\wedge A=A\wedge dA-dA\wedge A\); the cubic terms cancel. Thus \(dF+A\wedge F-F\wedge A=0\). For a concrete failure of \(dF=0\), on \(\mathbb R^3\) choose \(A=zB\,dx+C\,dy\), with constant matrices \([B,C]\ne0\). Then \(F=B\,dz\wedge dx+z[B,C]\,dx\wedge dy\), so \(dF=[B,C]\,dz\wedge dx\wedge dy\ne0\).

**Exercise 8.3 (medium).** On the trivial \(U(1)\)-bundle over the two-torus take \(A=i\alpha\,d\theta+i\beta\,d\psi\). Determine curvature and holonomy.

**Solution.** Curvature is zero. Lift a loop coordinatewise to the universal angle coordinates; its increments are \((2\pi m,2\pi n)\). The multiplier is \(e^{-2\pi i(\alpha m+\beta n)}\). Every pair occurs. Nullhomotopic loops have zero increments by the continuous-integer argument in the circle example, and zero-increment loops contract by linear contraction of their lift. Therefore restricted holonomy is trivial and full holonomy is the subgroup generated by \(e^{-2\pi i\alpha}\) and \(e^{-2\pi i\beta}\). It is finite when both parameters are rational modulo integers; if either is irrational it is dense in \(U(1)\), with its holonomy Lie-group topology still discrete.

**Exercise 8.4 (hard).** Prove that if the base is simply connected, full holonomy is connected. Explain why this does not assert that it is closed.

**Solution.** Every loop is nullhomotopic, so the two holonomy groups coincide. Theorem 6.1 makes this group connected in its immersed Lie topology. Connected immersed subgroups can nevertheless be nonclosed: the irrational one-parameter subgroup of \(\mathbb T^2\) in Exercise 6.4 of the local-tools lesson is a connected immersed subgroup whose image is dense and proper. The theorem's connectedness conclusion supplies no embeddedness or closedness hypothesis. The reduction and holonomy theorem in the next lesson will work with the immersed subgroup itself.

## References

[Meinrenken] Eckhard Meinrenken, *Principal bundles and connections*, lecture notes, [University of Toronto](https://www.math.toronto.edu/mein/teaching/moduli.pdf).

