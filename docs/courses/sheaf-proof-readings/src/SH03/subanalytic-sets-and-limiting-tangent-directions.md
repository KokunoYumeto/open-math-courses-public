# Subanalytic sets and limiting tangent directions

At a smooth point, a one-form can be tested on the tangent space. At a singular point, an approach to the set may have zero first derivative, and the first useful displacement may occur several orders later. Subanalytic geometry lets us replace such a limiting approach by an analytic curve and retain its first nonzero term. This gives a precise meaning to a one-form vanishing on a singular set, and explains why that condition survives analytic maps.

We work with finite-dimensional real analytic manifolds, Hausdorff and countable at infinity. All maps called analytic are real analytic. No coefficient ring or sheaf boundedness condition enters this geometric lesson. Later, these results will control cotangent supports of constructible sheaves.

The proof has three routes. Analytic curves turn limiting displacements into leading Taylor coefficients; proper uniformization lets tangent vectors detect a one-form; ordered radial graphs produce compatible triangulations. These routes share subanalytic set calculus but use different additional inputs. The signed normal-deformation criterion comes from the normal-geometry course.

*Original exposition by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026; revised by GPT-6 Astra (OpenAI), Ultra, October 2026. Original programme expression is public domain (CC0). Human results retain their named credit, and the linked Valette adaptations retain CC BY 4.0.*

## A local class with controlled boundaries

A subset \(S\subset X\) is **subanalytic** if, near every point of the ambient manifold, it has a presentation

\[
S\cap U
=U\cap\bigcup_{j=1}^N
\left(f_j^1(Y_j^1)\setminus f_j^2(Y_j^2)\right),
\tag{1}
\]

where the \(Y_j^i\) are compact real analytic manifolds and the \(f_j^i:Y_j^i\to X\) are analytic. Both the neighborhood \(U\) and the finite presentation can depend on the ambient point. In particular, behavior at a boundary point outside \(S\) still matters.

An equivalent description uses local projections of relatively compact semianalytic sets. A semianalytic set is locally a finite Boolean combination of analytic equalities and strict inequalities. This description makes analytic rank conditions, specified by minors of a differential, available inside the subanalytic calculus. The [compact-image construction below](#from-resolved-signs-to-compact-analytic-images) proves the equivalence with (1), including the converse for arbitrary subsets by a terminating sequence of frontier differences.

The following six statements fix the scope of the lesson. The [compact-image construction](#from-resolved-signs-to-compact-analytic-images) proves the set and map calculus in item 1. The [dimension-controlled proper uniformization](#dimension-controlled-proper-uniformization) proves item 4 on arbitrary noncompact manifolds as well, with a source of the same dimension as the set. The [analytic-descent and squared-distance argument](#detecting-the-entire-analytic-regular-locus) proves every fixed-dimensional intrinsic regular-locus statement in item 2. Curve selection is connected below to its explicit local-chart and Puiseux providers, and compatible triangulation is constructed first on a relative polyhedron and then on an arbitrary manifold. The analytic-function resolution in item 5 is proved below by constructing the local invariant, closed canonical centres and finite local towers, and then comparing and gluing those towers. The proof retains the entire function and its multiplicities.

1. **Set operations and analytic maps.** Closure, interior, finite union, intersection and difference preserve subanalyticity. Connected components are subanalytic and form a locally finite family in the ambient manifold. Analytic inverse images are subanalytic. If \(f:Y\to X\) is analytic, \(W\subset Y\) is subanalytic, and \(f|_{\overline W}:\overline W\to X\) is proper, then \(f(W)\) is subanalytic. The bar in this properness hypothesis is essential.
2. **Regular points.** A point of \(S\) is regular when \(S\cap U\) is a closed analytic submanifold of some ambient neighborhood \(U\). Write \(S_{\mathrm{reg}}\) for these points. The regular locus and its complement in \(S\) are subanalytic; \(S\subset\overline{S_{\mathrm{reg}}}\). For each fixed dimension \(d\), the dimension-\(d\) part of the regular locus is subanalytic. We set \(\dim S=\sup_{x\in S_{\mathrm{reg}}}\dim_x S\), with the usual empty-set convention. The [intrinsic regular-locus proof below](#detecting-the-entire-analytic-regular-locus) establishes these statements using analytic descent and squared distance, with the Bierstone–Milman source credited there.
3. **Curve selection.** If \(x\in\overline S\), there is an analytic curve \(a:(-1,1)\to X\) with \(a(0)=x\) and \(a(t)\in S\) for every \(t\ne0\). Its first derivative may vanish. The two-sided parameter is compatible with a one-sided set: squaring an initially positive parameter produces it.
4. **Uniformization.** A closed subanalytic set \(S\subset X\) is the image of an analytic manifold \(Y\) under a proper analytic map \(f:Y\to X\). For nonempty \(S\), the source can have pure dimension \(\dim S\); if \(S\) is compact, the source can be compact.
5. **Resolution of an analytic function.** Suppose \(\varphi:X\to\mathbb R\) is analytic and is not identically zero on any connected component. Put \(Z=\{\varphi=0,d\varphi=0\}\). There is a proper analytic \(f:Y\to X\), an isomorphism over \(X\setminus Z\), such that near each point of \(f^{-1}Z\), in analytic coordinates,
   \[
   \varphi\circ f=\pm\prod_i y_i^{r_i},\qquad r_i\in\mathbb Z_{\ge0}.
   \tag{2}
   \]
   Exponents equal to zero are allowed.
6. **Compatible triangulation.** Every locally finite subanalytic partition of \(X\) admits a locally finite simplicial triangulation whose open simplices have subanalytic analytic-submanifold images, each lying in one member of the partition. The triangulating map is a homeomorphism. Its global analyticity is not asserted. This is the bridge to Constructible sheaves on a triangulation.

Local finiteness extends the finite set-operation statements to a locally finite union: near any ambient point, only finitely many members occur. It does not authorize arbitrary unions. Likewise, analytic maps need not preserve subanalyticity of their images without the stated control at infinity.

## Analytic coordinates and uniqueness with parameters

The coordinate arguments here require analytic charts and inverses. Their starting point is the proved holomorphic inverse and implicit function theorem, Lemma 2.2. The proof uses a uniformly contracting iteration on a small complex ball; its iterates are holomorphic, and Cauchy's formula makes their locally uniform limit holomorphic. We record the passage to real analytic maps, including parameters, and the differential-equation fact needed by the finite-jet construction.

### Real analytic inverse, implicit and constant-rank coordinates

A real analytic power series, on a sufficiently small neighborhood of its centre, extends to a holomorphic power series on a complex polydisc. Indeed, absolute convergence on a smaller real box bounds the series with the absolute values of its coefficients; the same bound applies to complex arguments of those moduli. Its coefficients are real, so this extension commutes with conjugation.

**Analytic inverse theorem with parameters.** Let \(F(x,\lambda)\) be real analytic near \((a,\lambda_0)\), with \(x\in\mathbb R^m\), \(\lambda\in\mathbb R^p\), and assume \(D_xF(a,\lambda_0)\) is invertible. There is a unique local real analytic map \(G(y,\lambda)\) solving
\[
F(G(y,\lambda),\lambda)=y,
\qquad
G(F(x,\lambda),\lambda)=x.
\tag{LAF1}
\]

**Proof.** Complexify \(F\) near the specified point. The block map
\[
(x,\lambda)\longmapsto(F(x,\lambda),\lambda)
\tag{LAF2}
\]
has invertible derivative there. Apply the holomorphic inverse theorem. Its inverse preserves the last coordinate because the map itself does. After taking conjugation-invariant neighborhoods, uniqueness implies that the inverse commutes with conjugation: conjugating the unique preimage of a real target gives that same preimage. Restriction to real points therefore gives a real analytic inverse. The convergent complex power series of its components restrict to the required real power series. Both identities follow from the two inverse identities. \(\square\)

Consequently, if \(H(x,z,\lambda)\) is real analytic, \(H(a,b,\lambda_0)=0\), and \(D_zH(a,b,\lambda_0)\) is invertible, the map
\[
(x,z,\lambda)\longmapsto(x,H(x,z,\lambda),\lambda)
\]
has a real analytic inverse. Its middle target coordinate equal to zero gives a unique real analytic solution \(z=h(x,\lambda)\). More generally, independent defining differentials can be completed by linear coordinate functions to an invertible square Jacobian. This gives analytic submersion coordinates, analytic local sections, and analytic level submanifolds, with tangent space the kernel of the differential.

**Analytic constant-rank theorem with parameters.** Suppose \(F(x,\lambda)\in\mathbb R^n\) is real analytic and
\[
\operatorname{rank}D_xF(x,\lambda)=r
\tag{LAF3}
\]
throughout a neighborhood of \((a,\lambda_0)\). There are real analytic source and target coordinate changes, both preserving \(\lambda\), in which the map becomes
\[
(u,z,\lambda)\longmapsto(u,0,\lambda).
\tag{LAF4}
\]
The hypothesis is constant rank in the \(x\) variables on a neighborhood, not merely a rank calculation at the central point.

**Proof.** For \(r>0\), reorder source and target coordinates so an \(r\)-by-\(r\) minor is invertible at the specified point. The map
\[
(x,\lambda)\longmapsto
(F_1(x,\lambda),\ldots,F_r(x,\lambda),
 x_{r+1},\ldots,x_m,\lambda)
\]
has invertible derivative and is an analytic coordinate change by (LAF1). On a smaller product box, the transformed map has the form
\[
(u,z,\lambda)\longmapsto(u,K(u,z,\lambda),\lambda).
\]
At each fixed parameter its derivative in \((u,z)\) is
\[
\begin{pmatrix}I_r&0\\ D_uK&D_zK\end{pmatrix}.
\]
Its rank equals \(r+\operatorname{rank}D_zK\), by subtracting \(D_uK\) times the upper block rows from the lower block rows. Condition (LAF3) forces \(D_zK=0\). Integrating each derivative along coordinate segments inside the product box shows \(K(u,z,\lambda)=k(u,\lambda)\). The analytic target change
\[
(u,w,\lambda)\longmapsto(u,w-k(u,\lambda),\lambda)
\]
has the explicit analytic inverse which adds \(k\), and gives (LAF4). For \(r=0\), the same segment argument makes \(F\) independent of \(x\), and subtraction of this parameter-dependent value finishes the proof. \(\square\)

Taking no parameters gives the analytic constant-rank theorem on manifolds by using charts. It proves, in particular, that a local constant-rank fibre is an analytic manifold with tangent space \(\ker dF\). A map with injective differential is locally an analytic embedding. If it is also a homeomorphism onto its image, these local descriptions give an embedded analytic submanifold globally on that image.

### Analytic differential equations

For the finite-jet argument, uniqueness is already supplied by Local tools for bundles and transport, Theorem 2.1. That theorem proves uniqueness among differentiable solutions and smooth dependence on all initial data. Analytic dependence is a stronger assertion; the following direct construction establishes it when the vector field is analytic.

**Analytic parameter theorem.** For a real analytic finite system
\[
\dot x=V(t,x,\lambda),\qquad x(t_0)=a,
\tag{LAF5}
\]
the local solution is real analytic jointly in \(t,t_0,a,\lambda\). It is the unique differentiable real solution with those data on any common connected interval where the solutions are defined.

**Proof.** Translate a fixed datum to the origin and extend \(V\) holomorphically to a complex product neighborhood. Use the maximum norm on coordinates and its induced operator norm for matrices. Choose positive \(T,R,P\) whose closed product polydisc is inside that neighborhood, and bounds \(M,L\) for \(\lVert V\rVert\) and \(\lVert D_xV\rVert\) there. The spatial segment formula gives
\[
\lVert V(t,x,\lambda)-V(t,y,\lambda)\rVert
\le L\lVert x-y\rVert
\]
inside the convex spatial polydisc. Choose \(\rho>0\) so
\[
\rho<T/4,\qquad \rho M<R/4,\qquad q=\rho L<1/2.
\tag{LAF6}
\]
Restrict \(|t_0|<T/4\), \(\lVert a\rVert<R/4\), and \(\lVert\lambda\rVert<P/2\). If a bound is zero, its corresponding inequality imposes no restriction.

Starting with \(u_0(s,a,t_0,\lambda)=a\), define, for \(|s|<\rho\),
\[
u_{k+1}(s,a,t_0,\lambda)
=a+\int_0^s
 V(t_0+\zeta,u_k(\zeta,a,t_0,\lambda),\lambda)\,d\zeta.
\tag{LAF7}
\]
The integral is over the straight complex segment. Every iterate has spatial norm at most \(R/2\): its norm is at most \(R/4+\rho M<R/2\) whenever the preceding iterate has that bound. Its time argument stays inside \(|t|<T/2\).

Every iterate is jointly holomorphic. To verify the integration step, write the integral as
\(s\int_0^1 V(t_0+\theta s,u_k(\theta s,a,t_0,\lambda),\lambda)\,d\theta\).
On each smaller closed parameter polydisc the integrand is uniformly continuous in \(\theta\); the Riemann sums are holomorphic and converge uniformly. The holomorphic convergence theorem, Theorem 3.1, makes the integral holomorphic.

Take suprema over the entire smaller data product and \(|s|<\rho\). The spatial estimate gives
\[
\lVert u_{k+1}-u_k\rVert_\infty
\le q\,\lVert u_k-u_{k-1}\rVert_\infty,
\qquad
\lVert u_1-u_0\rVert_\infty\le\rho M.
\]
The geometric tail bound proves uniform convergence to a jointly holomorphic \(u\). Uniform convergence of the integrands passes (LAF7) to the limit. For fixed data the integrand is holomorphic in \(s\), so its integral is a primitive; consequently
\(\partial_su=V(t_0+s,u,\lambda)\) and \(u(0)=a\).
Substitution \(s=t-t_0\) gives joint holomorphy in the stated variables on \(|t-t_0|<\rho\).

All real data and real \(s\) give real iterates, because the vector field's extension agrees with the real vector field there. Hence the limit restricts to a jointly real analytic solution. If two differentiable real solutions have the same datum, restrict to a common small interval on which both remain in the spatial polydisc. Their integral equations give a supremum difference at most \(L\epsilon\) times itself; choose \(L\epsilon<1\). They agree there. The set of agreement times on a common connected interval is closed by continuity and open by this local argument applied at each agreement point. It is the whole interval. \(\square\)

Uniqueness gives the local composition law for solution maps:
\[
\Phi_\lambda(t,s,\Phi_\lambda(s,t_0,a))
=\Phi_\lambda(t,t_0,a).
\tag{LAF8}
\]
Thus the time-\(t_0\)-to-\(t\) map is an analytic local diffeomorphism, with inverse the time-\(t\)-to-\(t_0\) map. These assertions hold on the neighborhoods where the indicated solutions exist. Along an already existing solution on a compact time interval, finitely many local constructions compose to give joint analytic dependence near that trajectory. No existence for all real time is inferred.

For the line-incidence construction, put \(g_j=L^jh\), where \(L=v\cdot\partial_x\). A local identity
\(g_{q+1}=\sum_{j=0}^q a_j(x,v)g_j\)
gives, along \(x+tv\), the system
\[
U_j'=U_{j+1}\ (j<q),\qquad
U_q'=\sum_{j=0}^q a_j(x+tv,v)U_j.
\tag{LAF9}
\]
Choose a smaller parameter box and a common time interval whose line segments remain inside the coefficient neighborhood. Its coefficient matrix has a common bound \(B\). When \(U(0)=0\), integration gives
\(\sup_{|t|\le\epsilon}\lVert U(t)\rVert
\le B\epsilon\sup_{|t|\le\epsilon}\lVert U(t)\rVert\).
For \(B\epsilon<1\), \(U=0\). This proves the exact zero-solution uniqueness used there, uniformly on that smaller parameter box. It does not require the stronger analytic parameter theorem.

### A parameter-preserving normal form

For
\[
F_\lambda(x,y)=(x+y^2+\lambda y,\ (x+y^2+\lambda y)^2),
\]
the spatial derivative has rank one everywhere. Set
\(u=x+y^2+\lambda y,\ z=y\) in the source and
\((a,b)\mapsto(a,b-a^2)\) in the target. The inverse source change is
\(x=u-z^2-\lambda z,\ y=z\). Both changes preserve \(\lambda\) and are analytic, and the transformed map is exactly \((u,z)\mapsto(u,0)\). This illustrates why a parameter-dependent coordinate change is allowed while the parameter itself remains fixed.

<p class="figure"><img src="figures/SH03-analytic-normal-form.svg" alt="At a fixed parameter, three exact curved fibres map to points on a parabola, which an analytic target change straightens to a line." /></p>

The example uses the source coordinates and target change displayed above. At the fixed parameter shown, each coloured fibre maps to its matching point on the parabola; subtraction of the square of the first coordinate puts the image on a straight line. The coordinate calculation proves the identity for every parameter, not only the plotted one. Full-size diagram · Reproducible Python source.

## From a local analytic presentation to analytic curve selection

The human treatment of curve selection and Łojasiewicz inequalities, adapted from Guillaume Valette's 2025 survey under CC BY 4.0, gives its arguments in globally subanalytic Euclidean spaces. Its cell-decomposition and Puiseux prerequisites are stated explicitly. The following chart argument explains how its curve-selection proof applies to the local sets in this lesson.

The companion analytic finiteness treatment now proves a prerequisite for that cell construction: real analytic Noetherianity via the existing Demailly division provider, Artin–Rees and Krull intersection, convergent replacements of formal linear solutions with prescribed jets, a finite Taylor family with analytic units, and the signed uniform-order normalization. The full analytic-composition and inverse-power reduction remains distinct from this finiteness proof.

**Local comparison.** Given \(x\in X\) and a subanalytic \(S\subset X\) with presentation (1) near \(x\), there is an analytic coordinate neighborhood and a smaller bounded coordinate ball \(B\) about \(x\) such that the coordinate image of \(S\cap B\) is globally subanalytic.

**Proof.** Choose the ball with compact closure inside both the presentation neighborhood and an analytic chart \(V\). For one of the finitely many maps \(f:Y\to X\) in (1), the set \(K=f^{-1}(\overline B)\) is compact because \(Y\) is compact. Cover \(K\) by finitely many closed coordinate boxes \(Q_\ell\) whose interiors cover \(K\) and whose neighborhoods lie in \(f^{-1}(V)\). This follows by first choosing such a box around each point of \(K\) and then taking a finite subcover. In their coordinates, each \(Q_\ell\) is a compact rectangle and the coordinate functions of \(f\) are analytic on a neighborhood of that rectangle.

The graph of \(f|_{Q_\ell}\) in these coordinates is bounded and semianalytic in its whole ambient Euclidean space: on a neighborhood of the box it is given by the rectangle inequalities and analytic graph equations; away from the closed box it is locally empty. A bounded ambient semianalytic set is globally semianalytic. Indeed, compactification \(z\mapsto z/\sqrt{1+|z|^2}\) is an analytic coordinate change on a neighborhood of its compact closure, whose image stays strictly inside the unit ball. The compactified set is therefore semianalytic, and is empty near the compactification boundary. In the projective-product convention of the preparation theorem, boundedness makes the compact closure lie entirely in the finite affine chart; the set is empty near every point at infinity, so is globally semianalytic there as well.

Projecting this graph proves that \(f(Q_\ell)\) is globally subanalytic. Every point of \(f(Y)\cap B\) has a preimage in \(K\), so

\[
f(Y)\cap B=\left(\bigcup_\ell f(Q_\ell)\right)\cap B.
\]

This is a finite union and intersection of globally subanalytic sets. Apply the same argument to every map in (1), and then apply the globally subanalytic Boolean-operation theorem to its finite differences and unions. The result is precisely \(S\cap B\). \(\square\)

**The full two-sided curve.** Suppose \(x\in\overline S\). Apply the cited component's proved choice-and-Puiseux argument to the bounded coordinate set \(S\cap B\). It gives an arc \(\gamma:[0,\epsilon)\to S\cap B\) with endpoint \(x\), analytic across zero. Choose \(0<c<\epsilon\) small enough that the power series and chart inverse are defined whenever \(|r|<c\). The analytic map

\[
a(t)=\gamma(c t^2),\qquad -1<t<1,
\]

interpreted in the analytic chart, has \(a(0)=x\) and \(a(t)\in S\) for every \(t\ne0\). If \(x\notin S\), it is nonconstant. This proves the exact two-sided statement from the local comparison and the explicit cell/Puiseux inputs; it imposes no global definability assumption on \(S\) or \(X\).

No assertion of finiteness at infinity has entered this argument. For instance, \(\{(u,\sin u):u\in\mathbb R\}\) is analytic locally but cannot be globally subanalytic: intersecting with the horizontal axis and projecting would make its infinite discrete set of zeroes a definable subset of the line, contrary to finite cell decomposition. Each bounded chart piece nevertheless has the local comparison just proved. The ambient local finiteness and properness qualifications elsewhere in this lesson therefore remain in force.

## Removing the unit from a resolved function

A resolution is often expressed with a nonvanishing analytic factor:
\(\varphi\circ f=u(y)\prod_i y_i^{r_i}\).
The precise sign-only expression (2) follows from that form near a point of the zero set. This last coordinate step changes neither the map \(f\) nor its isomorphism over \(X\setminus Z\).

**Unit normalization.** Suppose a nonzero analytic function has the displayed form near a point \(a\) where its value is zero. There are analytic coordinates centred at \(a\) in which it is a sign times a monomial. The coordinate change preserves the normal-crossing coordinate hyperplanes through \(a\).

**Proof.** Any factor with \(y_i(a)\ne0\) is a local analytic unit; absorb it into \(u\). Centre the remaining coordinates at \(a\). At least one active exponent is positive, since the function vanishes there. Relabel it \(r_1>0\). Shrink so that \(u\) has constant sign \(\varepsilon\in\{1,-1\}\). The positive function \(|u|=\varepsilon u\) has a positive analytic \(r_1\)-th root \(b\). Indeed, the implicit function theorem applied to \(b^{r_1}-|u(y)|=0\) has nonzero derivative in \(b\) at its positive root. Set

\[
z_1=y_1b(y),\qquad z_i=y_i\ (i>1).
\]

The Jacobian determinant at the centre is \(b(a)>0\); all extra derivatives in the first row carry the factor \(y_1(a)=0\). The analytic inverse function theorem supplies a coordinate change. Substitution gives \(\varphi\circ f=\varepsilon\prod_i z_i^{r_i}\). Because \(b\) never vanishes, \(\{z_1=0\}=\{y_1=0\}\), and the other active hyperplanes are unchanged. This proves every claim. \(\square\)

The zero-set qualification matters. A nonconstant unit such as \(e^x\) has no positive vanishing exponent to absorb it and cannot become the constant monomial \(1\) by an invertible coordinate change. In the resolution input, points of \(f^{-1}Z\) lie above \(\{\varphi=0\}\), so the needed qualification holds. This coordinate argument supplies the last step from a unit-monomial resolution, not the construction of a singular-locus-preserving resolution itself.

## Reducing marked equations to their coefficients

The source for the following coefficient construction is [Edward Bierstone and Pierre D. Milman, *Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant*, author manuscript of 25 November 1996](https://www.math.toronto.edu/bierston/inventionnes.ps), Proposition 4.12, Construction 4.18 and Proposition 4.19, with the proofs on pp. 33–34. The edition cited here is the complete 70-page author manuscript. The argument uses a distinguished derivative to select a hypersurface and transfers each marked order to finitely many coefficients on it. Ordinary permissible blowings-up divide by the exceptional coordinate with the assigned weight; exceptional tests pull back without that division. Keeping these two transformation rules separate is essential to persistence.

Our real analytic proof uses a convergent implicit coordinate change, then verifies coefficient divisibility along the whole smooth centre, the ordinary charts, the omitted transverse direction and the two other test transformations. Its hypothesis that the transverse direction is compatible with the existing exceptional hypersurfaces is exactly the additional hypothesis needed in the source’s Proposition 4.12. The conclusion is a local reduction with finite persistence under those hypotheses. The residual invariant, exceptional history and choice of centres in the surrounding desingularization construction require further arguments, identified after the proof.

Let \(U\) be an analytic coordinate neighborhood, with coordinates \((x,t)\in\mathbb R^{m-1}\times\mathbb R\), and let \(\mathcal F=\{(h,b_h)\}\) be a finite nonempty collection of analytic functions with positive integer marks. Its **equimultiple locus** is

\[
S_{\mathcal F}=\{p\in U:\operatorname{ord}_p h\ge b_h\text{ for every }(h,b_h)\in\mathcal F\}.
\]

The order of the zero germ is infinite. Assume that at a chosen \(a\in S_{\mathcal F}\), one distinguished pair \((h_*,d)\) satisfies \(\operatorname{ord}_a h_*=d\) and \(\partial_t^d h_*(a)\ne0\). If exceptional hypersurfaces are present, assume they are coordinate hypersurfaces in the \(x\) variables. Thus the distinguished transverse direction is compatible with them. This is an explicit hypothesis when exceptional divisors have already appeared.

**Coefficient reduction and persistence.** After an analytic change of the transverse coordinate, there is a smooth hypersurface \(N=\{t=0\}\), transverse to these exceptional hypersurfaces, and expansions

\[
h(x,t)=\sum_{q=0}^{b_h-1}c_{h,q}(x)t^q+t^{b_h}R_h(x,t).
\]

Here \(c_{*,d-1}=0\) and \(R_*(a)\ne0\). In a neighborhood of \(a\),

\[
S_{\mathcal F}
=\{p\in N:\operatorname{ord}_p c_{h,q}\ge b_h-q
\text{ for every }h,\ 0\le q<b_h\}.
\]

The orders on the right are computed on \(N\). If a smooth centre \(C\subset S_{\mathcal F}\) has normal crossings with the exceptional hypersurfaces and \(N\), this equality persists near every point above \(a\) where the transformed marked equations still have their marked orders. In a chart with exceptional coordinate \(y_k\), the coefficients transform with their own marks:

\[
h'=y_k^{-b_h}(h\circ\sigma),\qquad
c'_{h,q}=y_k^{-(b_h-q)}(c_{h,q}\circ\sigma_N).
\]

The hypersurface \(N\) transforms strictly, with local equation \(t'=t/y_k\). Its transforms remain smooth and have normal crossings with the transformed exceptional hypersurfaces. The same coefficient reduction also persists under adjoining an independent variable and under an exceptional blowing-up in two existing exceptional hypersurfaces. For the latter test transformation the functions are pulled back without dividing by an exceptional power. Repeated applications give the corresponding assertion along every finite sequence of these transformations, at points satisfying the marked order conditions.

**Proof of the initial reduction.** Put \(z=\partial_t^{d-1}h_*\). Its derivative with respect to \(t\) is nonzero at \(a\), so the analytic implicit function theorem gives \(z=0\) as a graph \(t=\psi(x)\). Replace \(t\) by \(t-\psi(x)\), leaving \(x\) unchanged. Shrinking the neighborhood, \(z=t\,u(x,t)\) with \(u\) an analytic unit. Differentiation in the new \(t\) coordinate is the same as differentiation in the old one with \(x\) held fixed. The exceptional coordinate equations are unchanged.

Taylor expansion in \(t\), with analytic remainder, gives the displayed expansions. Since \(z(x,0)=0\), \(c_{*,d-1}=0\). The coefficient \(R_*(a)=\partial_t^d h_*(a)/d!\) is nonzero. If the order of \(h_*\) at a nearby point is at least \(d\), its derivative \(z\) vanishes there. Thus every point of \(S_{\mathcal F}\) lies on \(N\).

At \(p=(x_0,0)\), expand each coefficient in \(x-x_0\). Terms with distinct powers \(t^q\) cannot cancel. The remainder \(t^{b_h}R_h\) has total order at least \(b_h\). Consequently,

\[
\operatorname{ord}_{(x_0,0)}h\ge b_h
\quad\Longleftrightarrow\quad
\operatorname{ord}_{x_0}c_{h,q}\ge b_h-q
\quad(0\le q<b_h).
\]

This proves the equality of loci. The distinguished \(t^d\) coefficient also shows that the order of \(h_*\) at any point of this locus is exactly \(d\).

**Divisibility along a permissible centre.** Straighten \(C\) inside \(N\), keeping \(t\) as transverse coordinate and the exceptional equations as coordinate equations. Locally,

\[
C=\{t=0,\ x_i=0\ (i\in J)\}.
\]

Write \(I_J=(x_i:i\in J)\) on \(N\). The coefficient conditions hold at every point of \(C\), not merely at \(a\). Hence \(c_{h,q}\in I_J^{b_h-q}\). To see this directly, expand a coefficient in the normal variables \(x_i\), \(i\in J\), with analytic coefficients in the tangential variables. Every normal derivative of total degree less than \(b_h-q\) vanishes at every point of \(C\), by the order condition there. All the corresponding tangential coefficient functions are therefore identically zero. This proves membership in the stated ideal power and makes every division in the transform formula analytic.

**The ordinary blow-up charts.** For \(k\in J\), the \(x_k\) chart is

\[
x_k=y_k,\qquad x_i=y_ky_i\ (i\in J\setminus\{k\}),\qquad
t=y_ks,\qquad x_i=y_i\ (i\notin J).
\]

Substitution and division give

\[
h'(y,s)=
\sum_{q<b_h}y_k^{-(b_h-q)}c_{h,q}(\sigma_N(y))s^q
+s^{b_h}R_h(\sigma(y,s)).
\]

The strict transform \(N'\) is \(s=0\). In the distinguished equation the coefficient of \(s^{d-1}\) is zero. Near any point above \(a\),

\[
\partial_s^{d-1}h'_*
=s\bigl(d!R_*(\sigma(y,s))+y_ks\,A(y,s)\bigr)
\]

for an analytic \(A\). The factor in parentheses restricts to the nonzero constant \(d!R_*(a)\) on that exceptional fibre. It is a unit locally. The distinguished \(d\)-th derivative is likewise nonzero there. The initial coefficient argument therefore applies to \(h'\): its equimultiple locus lies on \(N'\) and equals the locus of the displayed coefficient conditions with marks \(b_h-q\).

The remaining points above \(a\) must be checked in the \(t\) chart. Here \(t=v\), \(x_i=vw_i\) for \(i\in J\), and the other \(x_i\) are unchanged. A point in this chart that belongs to no \(x_k\) chart has \(w_i=0\) for every \(i\in J\). Since \(c_{*,q}\in I_J^{d-q}\), the quotient \(v^{-(d-q)}c_{*,q}(vw,x_{\notin J})\) restricts to zero at such a point. The transformed \(h_*\) therefore has value \(R_*(a)\ne0\). Its order is zero, so that point is outside the transformed equimultiple locus. This covers every projective direction. If \(J\) is empty, all lower coefficients vanish identically and this same \(t\)-chart argument removes the whole marked locus.

In the \(x_k\) charts, the new exceptional divisor is \(y_k=0\); each surviving old exceptional divisor is another coordinate hypersurface in the \(y\) variables. Together with \(s=0\) they have normal crossings. This proves the geometric assertion as well as the coefficient formula.

**The two other test transformations.** An independent product variable changes none of the expansions, orders or equations. For a blowing-up of two exceptional hypersurfaces, choose equations \(x_1=0,x_2=0\). In the relevant chart the substitution is \(x_1=y_1,x_2=y_1y_2\), with \(t\) unchanged. The controlled test transform is now \(h'=h\circ\sigma\), so \(c'_{h,q}=c_{h,q}\circ\sigma_N\). Pullback cannot decrease the order of a coefficient at a point above \(a\): substituting analytic germs vanishing at \(a\) into every Taylor monomial preserves its minimum degree. The distinguished \(t^d\) coefficient remains a unit and \(c'_{*,d-1}=0\). Thus the same order-locus equality and the transverse coordinate equation \(t=0\) hold. The other chart is identical with the two exceptional coordinates interchanged; the prescribed distinguished point of an exceptional test is included in these charts.

After any of the transformations, the data again satisfy the initial hypotheses at a point where all marked orders persist. The distinguished order is exactly \(d\), the distinguished derivative is nonzero, and the coefficient expansions and exceptional coordinate equations have the required form. Applying the argument successively proves persistence for every finite allowed sequence. \(\square\)

This is the local dimension reduction: it replaces conditions on functions of \(m\) variables by weighted conditions on functions of \(m-1\) variables. The later sections prove recovery of divisor orders, the recursive history and coefficient construction, closed canonical centre selection, compact-local termination, and overlap compatibility. A multiplicity drop alone also need not give normal crossings with the exceptional divisor, as the cusp exercise below demonstrates.

## Gluing canonical local resolutions into a proper global map

A function-resolution construction must fit across coordinate neighborhoods. The same [Bierstone–Milman author manuscript](https://www.math.toronto.edu/bierston/inventionnes.ps), Theorem 13.2 and the proof of Theorem 13.3, passes from resolutions on relatively compact open sets to a global analytic map by unique compatible lifts. Its proof relies on the previously constructed invariant and local algorithm. Theorem 13.4 then treats the stronger requirement of a locally finite sequence of global blowings-up by extending and resolving centres.

The lemma below isolates the descent argument: the local proper maps and their isomorphisms over the full overlaps are hypotheses. Density forces uniqueness and the cocycle; quotient charts give the manifold; a finite compact-cover argument proves properness. This supplies the gluing step once compatibility exists, while leaving the construction of compatible local resolutions and the extension of centres to their separate proofs.

**Gluing lemma.** Let \(X\) be a real analytic manifold with a countable locally finite relatively compact open cover \((U_i)\), and let \(Z\subset X\) be closed. Suppose that each \(U_i\) has a proper surjective analytic map \(f_i:Y_i\to U_i\) from an analytic manifold, an analytic isomorphism over \(U_i\setminus Z\), with \(f_i^{-1}(U_i\setminus Z)\) dense in \(Y_i\). Suppose also that for every overlap there is an analytic isomorphism

\[
g_{ji}:f_i^{-1}(U_i\cap U_j)\longrightarrow f_j^{-1}(U_i\cap U_j),
\qquad f_jg_{ji}=f_i.
\]

Then these maps glue to an analytic manifold \(Y\) and a proper surjective analytic map \(f:Y\to X\), an analytic isomorphism over all of \(X\setminus Z\). If an analytic function \(\varphi\) pulls back under every \(f_i\) to an analytic unit times a coordinate monomial near \(f_i^{-1}Z\), the same holds for \(f\).

**Proof.** The overlap isomorphisms are unique. On the dense open inverse image of \((U_i\cap U_j)\setminus Z\), any such isomorphism must be \(f_j^{-1}f_i\). Two continuous maps to the Hausdorff manifold \(Y_j\) that agree on this dense set agree everywhere: their equality set is closed, being the inverse image of the diagonal. Density restricts to every open overlap. In particular,

\[
g_{ii}=\mathrm{id},\qquad g_{ij}g_{ji}=\mathrm{id},\qquad
g_{kj}g_{ji}=g_{ki}
\]

on their respective domains. The last equality follows by comparing both maps over a triple overlap. Thus the required cocycle is a consequence of uniqueness.

Take the disjoint union of the \(Y_i\) and identify a point of \(Y_i\) with its image under \(g_{ji}\) whenever its base point belongs to the overlap. The cocycle shows that each \(Y_i\) injects into the quotient, that its image is open, and that the induced topology and analytic charts there are its original ones. More precisely, the preimage over \(U_i\) of this quotient is precisely \(Y_i\): every representative over \(U_i\) has a unique representative in that chart. The \(f_i\) therefore descend to a map \(f\) with \(f^{-1}(U_i)\cong Y_i\).

The quotient is Hausdorff. If two points have different base points, disjoint base neighborhoods separate them. If they have the same base point, choose \(U_i\) containing it; both points lie in the same open Hausdorff chart \(Y_i\), which separates them by open subsets of the quotient. It is second countable because it is the union of countably many open second-countable \(Y_i\); the union of their countable bases is a basis. The analytic transition maps now make \(Y\) an analytic manifold. The map \(f\) is analytic and surjective by its local descriptions.

To check properness, let \(C\subset X\) be compact. Choose finitely many open neighborhoods \(V_1,\ldots,V_m\) covering \(C\), with each compact closure \(\overline V_\ell\) contained in some \(U_{i(\ell)}\). Such neighborhoods exist by local compactness and regularity of a manifold. Each \(C\cap\overline V_\ell\) is a compact subset of that \(U_{i(\ell)}\). Hence

\[
f^{-1}(C)=\bigcup_{\ell=1}^{m}
f_{i(\ell)}^{-1}(C\cap\overline V_\ell)
\]

is a finite union of compact subsets of \(Y\). This proves properness. Merely gluing maps that are proper over smaller pieces, without control over their full inverse images on overlaps, would not justify this step.

Over \(X\setminus Z\), the local inverses \(f_i^{-1}\) agree on overlaps, so they give a global analytic inverse. The coordinate monomial expressions are local statements in the charts \(Y_i\), and therefore remain true on \(Y\). If \(\varphi=0\) on \(Z\), the preceding unit-normalization lemma gives the exact sign-only expression near every point of \(f^{-1}Z\), while preserving the map \(f\) itself. This proves the lemma. \(\square\)

The density hypothesis makes the canonical transition unique. For a local construction by blowings-up, it is supplied by the dense complement of the exceptional sets in the coordinate charts. The later centre, termination and independent-tower comparison theorems construct the local maps and their full-overlap isomorphisms required here. The gluing proof does not turn the global map into a prescribed sequence of global blowings-up: that stronger construction has its own extension-of-centres argument.

## Why the real zero set does not determine the resolved function

The function

\[
\varphi(x,y)=xy(x^2+y^2)
\]

has the two coordinate axes as its real zero set. They already cross normally. Nevertheless, \(\varphi\) is not a unit times a coordinate monomial at their intersection, even after an invertible analytic coordinate change.

**Proof.** At a nonzero point of either axis, the other factors are units, so the order of vanishing along that branch is one. If a coordinate monomial had exactly these two branches, each exponent would consequently be one. Its order at their intersection would be two. But the displayed \(\varphi\) has order four at the origin. The order of an analytic germ is unchanged by an analytic coordinate change: its first nonzero homogeneous term is composed with the invertible linear part of the change and remains nonzero in the same degree. Multiplication by an analytic unit does not change that degree either. Thus the two orders contradict the proposed monomial form. \(\square\)

The missing factor \(x^2+y^2\) vanishes at the crossing, although it contributes no additional real branch. Resolving only the pictured real support loses this information. One real analytic blowing-up of the origin resolves this particular function:

\[
(x,y)=(u,uv)
\quad\Longrightarrow\quad
\varphi=u^4v(1+v^2).
\]

The factor \(1+v^2\) is a positive analytic unit. The other chart gives the corresponding expression at the vertical direction. The following exercise proves the complete proper-map and isomorphism assertions, rather than treating one affine substitution as the whole resolution.

## Keeping the whole function through a resolution

A resolution of a function retains its vanishing multiplicities. Resolving only the reduced real zero set does not supply this information. We first prove the complete-function calculation for a supplied tower of blowings-up, identify the centre condition which protects the original regular-zero locus, and carry out a complete cusp example. The canonical construction and termination theorems later in the lesson supply such towers in general.

The ideal-theoretic endpoint is treated in Edward Bierstone and Pierre D. Milman, *Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant*, complete author manuscript of 25 November 1996, [Remark 1.8 and Theorem 1.10, pp. 7–8](https://www.math.toronto.edu/bierston/inventionnes.ps). The principal-ideal calculation below explains directly why an endpoint with unit weak ideal gives the required multiplicities of the actual function. 

### The total exponent belongs to the function

Let \(M\) be a finite-dimensional Hausdorff second-countable real analytic manifold. Let \(f:M\to\mathbb R\) be analytic and not identically zero on any connected component. A **supplied admissible principal tower** consists of finitely many real projective blowings-up

\[
M_j\xrightarrow{\sigma_j}M_{j-1}\longrightarrow\cdots
\xrightarrow{\sigma_1}M_0=M,
\qquad
\pi_j=\sigma_1\circ\cdots\circ\sigma_j:M_j\longrightarrow M,
\tag{PF1}
\]

with \(\pi_0=\operatorname{id}_M\), and the following data. The centre of \(\sigma_{j+1}\) is a closed embedded smooth analytic submanifold \(C_j\subset M_j\) of positive codimension. Disconnected centres are allowed; the conditions below are imposed locally on each component. Empty steps can be omitted.

There is a locally principal analytic ideal sheaf \(I_j\subset\mathcal O_{M_j}\), with nonzero local generator \(h_j\), and a locally finite labelled family \(E_j\) of distinct smooth analytic hypersurfaces with simple normal crossings. Initially \(I_0=(f)\) and \(E_0=\varnothing\). For every \(H\in E_j\), every point of \(H\), and every local equation \(z_H\) of \(H\), the germ of \(h_j\) is **not divisible by \(z_H\)**. Equivalently, its restriction to the germ of \(H\) is not the zero analytic germ. It may still vanish at individual points of \(H\).

The centre lies in \(V(I_j)\). The point order \(\operatorname{ord}_p h_j\) is a constant positive integer \(m_j\) on each connected centre component; this is independent of the generator, since multiplication by an analytic unit preserves order. The centre and the old divisors admit simultaneous coordinates: locally the centre is a coordinate subspace, and the divisors through the point are distinct coordinate hyperplanes. This is the normal-crossing condition used below.

Put \(F_{j+1}=\sigma_{j+1}^{-1}(C_j)\). Its ideal \(I(F_{j+1})\) is invertible. Define

\[
I_{j+1}=I(F_{j+1})^{-m_j}
             \bigl(I_j\mathcal O_{M_{j+1}}\bigr),
\qquad
h_{j+1}=e^{-m_j}(h_j\circ\sigma_{j+1}),
\tag{PF2}
\]

where \(e\) is a local generator of \(I(F_{j+1})\). Here \(I_j\mathcal O_{M_{j+1}}\) denotes the ideal generated by the analytic pullbacks of sections of \(I_j\); the negative power in (PF2) is multiplication by the inverse invertible ideal. When the centre orders differ between components, the formula is read with their locally constant values. The chart calculation below proves that the result is an analytic ideal, rather than merely a fractional one. Changes of \(h_j\) or \(e\) multiply \(h_{j+1}\) by analytic units.

The updated family \(E_{j+1}\) consists of the nonempty strict transforms of the old hypersurfaces, retaining their labels, and the components of \(F_{j+1}\), with new labels. The strict transform of \(H\) is the closure of \(\sigma_{j+1}^{-1}(H\setminus C_j)\). We also record \(F_{j+1}\) when the centre is Cartier; that records a divisor factor even when the underlying blow-up is an isomorphism.

**Total-transform lemma.** Formula (PF2) gives nonzero analytic weak generators. They have no factor from any germ of the updated divisor family, and that family has simple normal crossings. Locally the actual function has the equality

\[
f\circ\pi_j=u_jh_j\prod_{H\in E_j}z_H^{a_{H,j}},
\qquad a_{H,j}\in\mathbb Z_{\geq0},
\tag{PF3}
\]

where \(u_j\) is an analytic unit and only the hypersurfaces meeting the coordinate neighbourhood are included. The exponents are locally constant along the corresponding labelled hypersurfaces. The old strict-transform exponents are unchanged. At a new divisor over a connected centre piece,

\[
a_{F_{j+1},j+1}
 =m_j+\sum_{H\supset C_j}a_{H,j}.
\tag{PF4}
\]

The containment condition in (PF4) means containment of the local centre germ. A divisor meeting the centre transversely, without containing it, contributes no exceptional factor.

**Proof of analytic divisibility and exact exceptional order.** Work in simultaneous coordinates \((x_1,\ldots,x_c,w)\), with \(C_j=\{x=0\}\). A convergent expansion in the normal variables has the form

\[
h_j(x,w)=\sum_\alpha A_\alpha(w)x^\alpha.
\]

For \(|\alpha|<m_j\), the normal derivative \(\partial_x^\alpha h_j(0,w)\) vanishes at every nearby centre point, because the point order there is at least \(m_j\). Thus \(A_\alpha\) is identically zero. In particular,

\[
h_j\in I(C_j)^{m_j},\qquad
h_j(x,w)=\sum_{|\alpha|\geq m_j}A_\alpha(w)x^\alpha.
\tag{PF5}
\]

For a fixed centre point \((0,w_0)\), its degree-\(m_j\) homogeneous normal polynomial
\(P_{w_0}(X)=\sum_{|\alpha|=m_j}A_\alpha(w_0)X^\alpha\)
is nonzero. Otherwise (PF5) shows that every term in the Taylor expansion at \((0,w_0)\) has total degree at least \(m_j+1\), contradicting the exact point order.

The \(x_\ell\)-chart of the real projective blow-up has coordinates \((e,v,w)\) and analytic map
\(x_\ell=e\), \(x_i=ev_i\) for \(i\ne\ell\), with \(w\) unchanged. Substitution in (PF5) proves the analyticity of (PF2). On the fibre over \((0,w_0)\), its restriction is
\(P_{w_0}(v_1,\ldots,v_{\ell-1},1,v_{\ell+1},\ldots,v_c)\).
This is a nonzero polynomial: dehomogenization in any one coordinate is injective on the vector space of homogeneous polynomials of this fixed degree. A nonzero real polynomial is not identically zero on any open neighbourhood of any finite \(v\)-point. If the germ of \(h_{j+1}\) at such a fibre point were divisible by \(e\), its restriction to \(e=0,w=w_0\) would instead vanish on a neighbourhood. This contradiction proves that the exceptional equation divides none of these germs. The charts cover the whole projective normal fibre. For \(c=1\), the dehomogenized polynomial is a nonzero constant, so the argument includes Cartier centres.

**Proof for the old divisors and the total exponents.** In the same coordinates an old hypersurface containing the centre has equation \(x_i=0\). If \(i\ne\ell\), its pullback is \(ev_i\) and its strict transform in this chart is \(v_i=0\). If \(i=\ell\), its pullback is \(e\) and its strict transform is absent from the chart. An old hypersurface not containing the centre has one of the tangential coordinate equations, say \(w_k=0\), and its pullback is the same equation. These descriptions exhibit \(F_{j+1}=\{e=0\}\) and all nonempty old strict transforms as distinct coordinate hyperplanes. They prove the updated simple-normal-crossing assertion.

Suppose a weak generator vanished identically on the germ of an old strict hypersurface at some point. Its vanishing would hold on a small open piece of that hypersurface. Points of this piece off \(F_{j+1}\) are dense, as is immediate from the coordinate description. At any such point the blow-up is an analytic isomorphism and \(e\) is a unit; thus the original \(h_j\) would vanish on an open germ of the original \(H\). That contradicts the assumed exclusion of every local divisor germ. This proves the assertion for old strict transforms as well.

Substitute the displayed pullbacks of old equations and
\(h_j\circ\sigma_{j+1}=e^{m_j}h_{j+1}\)
into (PF3). Every containing old divisor contributes exactly one additional copy of its exponent to the power of \(e\); the transverse ones contribute none. The remaining nonzero factors join the analytic unit. This proves (PF4) and the equality (PF3) by induction from \(u_0=1\), \(h_0=f\).

These are the actual divisorial multiplicities. Indeed, after removing \(z_H^{a_{H,j}}\) from (PF3), restriction of the remaining factors to the germ of \(H\) is a product of nonzero analytic germs: the weak generator has that property, the unit does, and every other coordinate equation does. The local ring of the smooth germ \(H\) is an integral domain, as follows from convergent power series. The product is nonzero, so one further power of \(z_H\) cannot divide the total function. At an intersection of divisors this divisorial order is distinct from the point order, which may be larger. \(\square\)

Division in (PF2) removes a factor from the weak ideal. Equation (PF4) retains that factor in the total function. Neither a reduced support nor a discarded unit is substituted for the equality of functions (PF3).

### Cartier steps and the proper analytic map

**Cartier lemma.** Blowing up a closed smooth analytic hypersurface is canonically an analytic isomorphism. If its local equation is \(x=0\) and \(h\) has constant point order \(m>0\) along it, then near each point of that hypersurface

\[
h=x^m v,\qquad v\text{ an analytic unit}.
\tag{PF6}
\]

The weak ideal becomes the unit ideal near the centre, while the total function retains the exponent \(m\).

**Proof.** The centre-divisibility argument (PF5) gives \(h=x^m v\) with \(v\) analytic. If \(v\) vanished at a centre point, the point order of \(h\) would exceed \(m\); hence \(v\) is nonzero there and is a unit on a smaller neighbourhood.

The normal projective fibre of a hypersurface is \(\mathbb{RP}^{0}\), a point. Its sole incidence chart has coordinate map \(x=e\), with all other coordinates unchanged. The analytic map from the blow-up to the original chart is therefore the identity in these coordinates. These chart inverses agree on their overlaps because they are inverses of the same blow-up map. They give the asserted global isomorphism, including when the hypersurface has no global defining function. Formula (PF2) leaves the unit \(v\); the total-transform identity retains \(x^m\). The newly recorded divisor need not be an exceptional locus of a nontrivial modification. \(\square\)

**Properness and endpoint.** Every blow-up in (PF1) is a surjective proper analytic map between manifolds of the same dimension. If the supplied tower ends with \(I_N=\mathcal O_{M_N}\), then \(\pi_N:M_N\to M\) is proper and surjective, and (PF3) is a unit times a coordinate monomial at every point.

**Proof.** Near a centre of codimension \(c\geq1\), the blow-up is the incidence manifold
\[
\{((x,w),[\lambda]) : x_i\lambda_k=x_k\lambda_i
       \text{ for all }i,k\}
\subset V\times\mathbb{RP}^{c-1}.
\]
Its chart \(\lambda_\ell\ne0\) has the coordinates \((e,v,w)\) already used, so its dimension equals that of \(V\), and its projection is analytic. Off the centre the projective coordinate is uniquely \([x]\), giving an analytic inverse there; over a centre point the fibre is exactly \(\mathbb{RP}^{c-1}\). This proves surjectivity, including \(c=1\).

These local incidence descriptions also retain the manifold separation and countability conditions. Points with different images are separated by inverse images of disjoint base neighbourhoods; points with the same image lie in one Hausdorff incidence neighbourhood and can be separated there. A countable base-chart cover, with finitely many projective charts over each centre chart, gives second countability.

The incidence equations define a closed subset. For a compact set \(Q\) contained in such a coordinate neighbourhood, its full inverse image is a closed subset of the compact space \(Q\times\mathbb{RP}^{c-1}\), hence compact. The same assertion holds in an open chart disjoint from the centre, where the map is an isomorphism. Now let \(K\subset M_j\) be any compact set. Choose finitely many compact coordinate neighbourhoods \(Q_1,\ldots,Q_r\), each contained in one of these charts, whose interiors cover \(K\). The inverse image of \(K\) is a closed subset of the finite compact union \(\bigcup_i\sigma_{j+1}^{-1}(Q_i)\). It is compact. Thus \(\sigma_{j+1}\) is proper, and finite composition proves properness of \(\pi_N\).

At the endpoint every local weak generator is a unit, so it joins \(u_N\) in (PF3). This is the asserted unit-monomial expression. The positive-codimension condition rules out an empty projective fibre; it is automatic for centres contained in the zero set of a nonzero analytic germ. In dimension zero the original function is already a unit on each point, and the identity map suffices. \(\square\)

At a zero of the total pullback, the preceding unit-normalization lemma gives a sign times a coordinate monomial, preserving its crossing hyperplanes. At least one exponent is then positive, as required by that lemma. Away from the zero set a nonconstant unit need not become a constant under an invertible coordinate change.

### The original regular-zero locus is protected

Set

\[
Z=\{p\in M:f(p)=0,\ df_p=0\},
\qquad U=M\setminus Z.
\tag{PF7}
\]

The centre hypotheses above do not by themselves make the tower an isomorphism over \(U\). For \(f(x,y)=x\), the origin is a smooth constant-order-one centre with no old divisors, yet blowing it up introduces a projective line over a point where \(df\ne0\). Thus the centre-selection rule must enter the argument.

We use this precise additional condition:

> **(R)** At a point where the weak generator has order one and no member of the current divisor family passes through the point, any chosen centre meeting the point has germ equal to the entire smooth weak-zero hypersurface there.

Centres also avoid the unit-ideal locus by the already imposed condition \(C_j\subset V(I_j)\).

The **full terminal-component rule** has (R), with the following meaning of “full.” A chosen centre germ is a whole local component of the terminal equal-invariant stratum, rather than a smaller smooth submanifold merely contained in that stratum. Here is the entire calculation needed at an order-one point without old divisors. Take \(t=h_j\) as an analytic coordinate, using \(dh_j\ne0\), and present the weak equation with mark one. Its coefficient hypersurface is \(N=\{t=0\}\); its sole coefficient below degree one is \(h_j|_N=0\). There are no old-divisor entries. In the order/history notation, the word is therefore \((1,0;\infty)\). After shrinking, every point of \(N\) has exactly this word, whereas off \(N\) the weak ideal is a unit. Thus its equal-word germ is precisely the single smooth hypersurface germ \(N\). A full local component through the point is \(N\) itself, which proves (R). This verification assumes that the rule chooses a centre with the stated full-component property; it does not construct a global closed centre or prove compatibility of independently chosen towers.

**Protected-complement lemma.** Every supplied admissible principal tower satisfying (R) restricts to an analytic isomorphism
\(\pi_j^{-1}(U)\xrightarrow{\;\pi_j\;}U\)
at each stage.

**Proof.** We prove the assertion together with this local description over \(U\): the weak ideal is either a unit, or its generator is a smooth coordinate and the divisor family is empty near that point. Initially this holds because \(f\ne0\) gives a unit and \(f=0,df\ne0\) gives a coordinate by the analytic inverse function theorem.

Assume the description and the isomorphism through stage \(j\). At a point with unit weak ideal, the centre is absent on a neighbourhood, so the next blow-up is an isomorphism there and the ideal remains a unit. At a point with nonunit weak ideal, the generator has order one and there are no old divisors nearby. If the point is outside \(C_j\), closedness of \(C_j\) supplies a neighbourhood avoiding the centre; the same description persists there. If the point belongs to \(C_j\), condition (R) makes that centre locally the full smooth weak-zero hypersurface. The Cartier lemma says that the blow-up is an isomorphism there and makes the weak ideal a unit. A divisor can be recorded in this last case, but the alternative “weak ideal is a unit” places no emptiness requirement on the divisor family.

These alternatives cover every point over \(U\), and the local inverses agree wherever their domains overlap because they invert the same map. They therefore give an analytic inverse on the entire inverse image of \(U\). This proves the induction and the conclusion for every finite composite. \(\square\)

Combining the endpoint and protected-complement lemmas gives the desired principal-function conclusion for any admissible tower satisfying (R) and reaching the unit weak ideal. The later [compact-fibre termination theorem](#finite-termination-over-a-compact-fibre) constructs these towers on neighborhoods of every base point. Their [independent-tower comparison](#independently-constructed-towers-on-overlaps) supplies analytic isomorphisms over full overlaps. The [global assembly](#from-finite-local-towers-to-the-global-function-resolution) then applies the proper-gluing lemma. The total-function factorization and the isomorphism over \(U\) pass through those comparison maps because they are local properties over the base. No uniform finite tower on the whole noncompact manifold is required.

### Completing the cusp calculation

For \(f(x,y)=y^2-x^3\), one has \(df=(-3x^2,2y)\), so \(Z=\{(0,0)\}\). The first blow-up makes the weak zero curve smooth but leaves it tangent to the first divisor. We keep both projective charts at each subsequent blow-up.

The first two charts, with their analytic maps to the original plane, are

\[
\begin{array}{lll}
x=u,\ y=uv: & f\circ\pi_1=u^2(v^2-u), & E_1=\{u=0\},\\
x=rs,\ y=s: & f\circ\pi_1=s^2(1-r^3s), & E_1=\{s=0\}.
\end{array}
\tag{PF8}
\]

The weak factor in the second chart is nonzero at every point of \(s=0\). In the first chart its zero curve is \(u=v^2\), tangent to \(E_1\) at the unique meeting point \((0,0)\). Blow up that point. The two charts over the first chart of (PF8) are

\[
\begin{array}{lll}
u=ab,\ v=a: & f\circ\pi_2=a^3b^2(a-b),
  & E_2=\{a=0\},\ E_1'=\{b=0\},\\
u=c,\ v=cd: & f\circ\pi_2=c^3(cd^2-1),
  & E_2=\{c=0\}.
\end{array}
\tag{PF9}
\]

The order of the weak equation \(v^2-u\) at the second centre is one, so (PF4) gives the new total exponent \(1+2=3\). The second chart of (PF9) has unit weak factor near each point of its exceptional divisor. In the first chart, the two old/new divisor axes and the weak line \(a=b\) meet at the origin. All three are smooth, but three distinct branches at one point of a surface do not form a simple-normal-crossing divisor. Blow up that one point.

The two resulting charts are

\[
\begin{array}{lll}
a=p,\ b=pq: & f\circ\pi_3=p^6q^2(1-q),
 & E_3=\{p=0\},\ E_1''=\{q=0\},\\
b=t,\ a=tw: & f\circ\pi_3=t^6w^3(w-1),
 & E_3=\{t=0\},\ E_2'=\{w=0\}.
\end{array}
\tag{PF10}
\]

Their composite maps to the original plane are, respectively,
\((p,q)\mapsto(p^2q,p^3q)\) and
\((t,w)\mapsto(t^2w,t^3w^2)\).
They also check the total pullback formulas directly. At the third centre the weak equation has order one, and both existing divisors contain the centre. The new total exponent is therefore \(1+3+2=6\), exactly as in (PF4).

The remaining weak curve is \(q=1\) in the first chart and \(w=1\) in the second. On their overlap,
\(w=1/q\) and \(t=pq\), so these represent the same curve and its same meeting point with \(E_3\). The curve is transverse to \(E_3\). The old strict divisors meet \(E_3\) at the other two distinct projective directions: \(E_1''\) at \(q=0\) and \(E_2'\) at \(w=0\). The latter point is outside the \(q\)-chart. At each final intersection, the two local branch equations have independent differentials; no three branches meet.

This also gives the monomial expression directly in each relevant neighbourhood. Near \(q=0\), use \((p,q)\), with unit \(1-q\). Near \(q=1\), use \((p,q-1)\), with unit \(-q^2\), giving \(-q^2p^6(q-1)\). At other finite points of \(E_3\) in that chart, \(q^2(1-q)\) is a unit and only \(p^6\) remains. In the other chart near \(w=0\), the unit is \(w-1\), leaving \(t^6w^3\). These neighbourhoods cover the complete third projective fibre.

To check the entire surface, retain the unaffected \((r,s)\)-chart from
the first blow-up and the unaffected \((c,d)\)-chart from the second.
Together with the two charts in (PF10), these four charts cover \(M_3\).
Their maps and complete functions are

| Final coordinates | \(\pi\) in original \((x,y)\)-coordinates | \(f\circ\pi\) |
|---|---|---|
| \((r,s)\) | \((rs,s)\) | \(s^2(1-r^3s)\) |
| \((c,d)\) | \((c,c^2d)\) | \(c^3(cd^2-1)\) |
| \((p,q)\) | \((p^2q,p^3q)\) | \(p^6q^2(1-q)\) |
| \((t,w)\) | \((t^2w,t^3w^2)\) | \(t^6w^3(w-1)\) |

For completeness, all six pairwise overlaps can be read from these
blow-up coordinates. Domains are stated in the coordinates on the left;
the inverse domain is stated in the last column.

| Transition | Domain | Inverse | Inverse domain |
|---|---|---|---|
| \((c,d)\mapsto(r,s)=(1/(cd),c^2d)\) | \(cd\ne0\) | \((c,d)=(rs,1/(r^2s))\) | \(rs\ne0\) |
| \((p,q)\mapsto(r,s)=(1/p,p^3q)\) | \(p\ne0\) | \((p,q)=(1/r,r^3s)\) | \(r\ne0\) |
| \((t,w)\mapsto(r,s)=(1/(tw),t^3w^2)\) | \(tw\ne0\) | \((t,w)=(r^2s,1/(r^3s))\) | \(rs\ne0\) |
| \((p,q)\mapsto(c,d)=(p^2q,1/(pq))\) | \(pq\ne0\) | \((p,q)=(cd,1/(cd^2))\) | \(cd\ne0\) |
| \((t,w)\mapsto(c,d)=(t^2w,1/t)\) | \(t\ne0\) | \((t,w)=(1/d,cd^2)\) | \(d\ne0\) |
| \((p,q)\mapsto(t,w)=(pq,1/q)\) | \(q\ne0\) | \((p,q)=(tw,1/w)\) | \(w\ne0\) |

Each pair consists of mutually inverse analytic maps on the displayed
open sets. Substituting in the preceding table proves agreement of the
original coordinates and of the total function. These transitions are
composites of the three elementary blow-up transitions already given,
so they obey the cocycle identities on triple overlaps. The zero values
allowed by the stated domains are essential: for example, the
\((r,s)\)/\((p,q)\) overlap includes \(s=q=0\), whereas the inverse
formula \(p=y/x\) in original coordinates would not be defined there.

In the first final chart the weak zero locus is disjoint from \(s=0\)
and smooth: on \(1-r^3s=0\) one has \(r\ne0\) and
\(\partial_s(1-r^3s)=-r^3\ne0\). In the second it is disjoint from
\(c=0\) and smooth: on \(cd^2-1=0\) one has \(d\ne0\) and
\(\partial_c(cd^2-1)=d^2\ne0\). In each of the last two charts the
weak curve and old exceptional component are disjoint parallel coordinate
lines, each transverse to \(E_3\). At every point of \(M_3\), therefore,
at most two branches of the total zero divisor meet and their local
defining equations have independent differentials. This proves the
simple normal-crossing assertion and all four displayed multiplicities.

All three centres lie above the origin. The properness argument proves that their composite \(\pi_3:M_3\to\mathbb R^2\) is proper and surjective; it is an analytic isomorphism over \(\mathbb R^2\setminus\{0\}\). The unit-normalization lemma gives sign-only monomial coordinates at every point above the origin. Thus this example proves the complete function-resolution conclusion, with all multiplicities and every projective direction retained.

One may also continue to the unit weak ideal. The final weak-zero curve is a closed smooth analytic hypersurface, and it meets the existing divisors normally. Blowing it up is a Cartier identity step with weak order one. It records the residual-curve exponent and makes the weak ideal a unit everywhere, without changing the manifold or the total pullback formulas.

```{=html}
<figure id="cusp-total-transform-figure" style="margin:1rem 0"><img src="figures/SH03-cusp-total-transform.svg" alt="Four coordinate charts showing the cusp tangency, three concurrent branches, and the two final transverse charts with total multiplicities" style="display:block;width:100%;max-width:680px;height:auto;margin:1rem auto;"><figcaption>The cusp after its first, second and third blow-ups. The final two affine charts together retain all projective directions. Labels give the multiplicities of the total function. Equations (PF8)–(PF10) and the following tables give every chart map and overlap.</figcaption></figure>
```

Open the full-size diagram · Reproduce the diagram.

### Exercise: distinguish the weak order from the total order

At each of the three point centres, compute the weak order and the order
of the complete function. Recover the new exceptional multiplicity, and
explain why two point blow-ups do not suffice for simple normal crossings.

**Solution.** Initially the weak and total functions coincide, and
\(y^2-x^3\) has order two. Thus \(E_1\) has multiplicity two. At the
second centre \((u,v)=(0,0)\), the weak factor \(v^2-u\) has order one,
while \(u^2(v^2-u)\) has order three. Its new exceptional exponent is
\(1+2=3\). At the third centre \((a,b)=(0,0)\), the weak factor
\(a-b\) again has order one, while \(a^3b^2(a-b)\) has order six.
Both old exceptional divisors contain that centre, so its new exponent
is \(1+3+2=6\). After two blow-ups there are three distinct divisor
branches at one point of a surface. An analytic coordinate change has
an invertible derivative and preserves distinct tangent lines; it
cannot turn those three branches into the at most two coordinate
hyperplanes available in dimension two. The third point blow-up is
therefore needed in this tower.

### Exercise: identify the final curve and normalize the three crossings

Write \(C_3\) for the final strict curve. Show that the whole curve is \(q=1\) in the
\((p,q)\)-chart and that \(\pi\) restricts to
\(p\mapsto(p^2,p^3)\). Find exact sign-monomial coordinates at the
three points where \(E_3\) meets \(E_1''\), \(E_2'\), and \(C_3\).

**Solution.** In the \((r,s)\)-chart a weak zero satisfies
\(r^3s=1\), hence lies in the overlap \(r\ne0\) and has
\(p=1/r, q=r^3s=1\). In the \((c,d)\)-chart it satisfies
\(cd^2=1\), hence lies in the overlap \(cd\ne0\) and again has
\(q=1\). In the \((t,w)\)-chart it has \(w=1\), hence lies in the
\((p,q)\)-chart with \(p=t,q=1\). Thus the entire curve is covered
by \(q=1\), with \(p\in\mathbb R\); the direct map in the table gives
\((x,y)=(p^2,p^3)\). This is a computation on the resolved curve, not
an assertion that the singular cusp is an analytic manifold.

Near \(E_3\cap E_1''\), namely \((p,q)=(0,0)\), set
\(P=p(1-q)^{1/6}\), \(Q=q\). The positive real sixth root is
analytic near \(q=0\), and the coordinate change has nonzero Jacobian.
Then \(f\circ\pi=P^6Q^2\). Near \(E_3\cap E_2'\), namely
\((t,w)=(0,0)\), set \(T=t(1-w)^{1/6}\), \(W=w\); this gives
\(f\circ\pi=-T^6W^3\). Finally, near \(E_3\cap C_3\), write
\(z=q-1\) and set \(P=p(1+z)^{1/3}\), \(Z=z\). Since
\(f\circ\pi=-p^6(1+z)^2z\), this gives
\(f\circ\pi=-P^6Z\). All roots are taken only of positive units
near the specified points, and each change preserves the displayed
coordinate crossing hypersurfaces. No root is taken of the possibly
zero exceptional coordinate.


## Fixed-chart history and the first analytic resolution prefix

The local resolution invariant remembers when an exceptional divisor appeared. Its history must vary correctly over an entire fixed analytic chart, including points at which the present invariant value first appeared at different stages. The following argument proves that history step and its application to the first order/history prefix. It is a reconstruction of [Bierstone–Milman, *Canonical desingularization in characteristic zero*, author manuscript, Proposition 6.6 and §§6.8–6.10, pp.36–37](https://www.math.toronto.edu/bierston/inventionnes.ps), with explicit analytic neighborhood witnesses. It does not construct the complete resolution algorithm.

Here a blowing-up is the real analytic **projective** blowing-up along a closed smooth analytic centre. Exceptional hypersurfaces retain labels recording their creation stage; a new exceptional hypersurface receives a new label. Labels follow strict transforms. At a point, only incident labels are counted. The initial exceptional family can be empty.

### Fixed charts and history incidence

Fix a finite given tower of smooth analytic blowings-up with normal crossings between every centre and its current exceptional hypersurfaces. Work on a finite stack of coordinate charts
\[
 U_j\xrightarrow{\sigma_j}U_{j-1}\longrightarrow\cdots
 \xrightarrow{\sigma_1}U_0.
\tag{AR1}
\]
Each map is the restriction of the corresponding blowing-up map. The charts are chosen before choosing pointwise presentations. On each chart, the centre is given by finitely many analytic equations and the finitely many exceptional hypersurfaces have analytic defining equations. Such chart stacks exist for a given finite tower: use coordinates adapted to the smooth centre and the normal-crossing divisor, then restrict a next-stage chart so its map lands in the preceding one.

For \(D\in O(U)\) with \(D(a)\ne0\), the set
\[
 U_D=\{x\in U:D(x)\ne0\}
\tag{AR2}
\]
is a principal relative Zariski neighborhood of \(a\). Call a totally ordered invariant \(\lambda\) *nonincreasing on fixed-chart neighborhoods* if every \(a\) has such a neighborhood on which \(\lambda(x)\le\lambda(a)\). This definition does not assert local finiteness of all invariant values, or the stronger analytic threshold properties needed for the full noncompact algorithm.

Here \(O(U)\) is the ring of real analytic functions on the fixed chart. For an open subset \(V\subset U\), write
\[
 O(U)_V=\{F/G:F,G\in O(U),\ G(x)\ne0\text{ for every }x\in V\}.
\]
These fractions are interpreted as analytic functions on \(V\). This ring need not contain every analytic germ at a point of \(V\).

**History lemma.** Suppose an invariant \(\lambda_k\) is defined at every stage of (AR1), is nonincreasing on fixed-chart neighborhoods, and satisfies:

- \(\lambda_{k+1}(x)\le\lambda_k(\sigma_{k+1}x)\);
- equality holds off the centre, where the map is an analytic isomorphism and the data are unchanged;
- \(\lambda_k\) takes one value on the entire centre portion \(C_k\cap U_k\). The chosen chart stacks must satisfy this condition at every stage.

For \(a\in U_j\), let \(a_k\) be its ancestor at stage \(k\), and set
\[
 b(a)=\min\{k:\lambda_k(a_k)=\lambda_j(a)\}.
\tag{AR3}
\]
Let \(E(a)\) be the incident exceptional labels at \(a\). Call a label *old for \(\lambda\)* if it is the strict transform of a label already present at \(a_{b(a)}\), and write \(E_\lambda(a)\) for the old set. Then there is a neighborhood (AR2) such that, for every \(x\) in it with \(\lambda_j(x)\ge\lambda_j(a)\),
\[
 \lambda_j(x)=\lambda_j(a),\qquad
 E(x)\subset E(a),\qquad
 E_\lambda(x)=E(x)\cap E_\lambda(a).
\tag{AR4}
\]

**Proof.** Induct on \(j\). At stage zero the old set is the initial incident divisor set; exclude the finitely many chart divisors not through \(a\) by their nonzero defining equations.

At a later stage, take a finite product of analytic functions nonzero at \(a\) to arrange the following conditions on one neighborhood (AR2). Pullback of an analytic witness at an ancestor is analytic on the current chart.

1. \(\lambda_j(x)\le\lambda_j(a)\), and \(\lambda_k(x_k)\le\lambda_k(a_k)\) at every earlier stage.
2. \(E(x)\subset E(a)\), by including equations for all chart divisors that miss \(a\).
3. The inductive old-set equality applies at \(x_{j-1}\) whenever its value equals that at \(a_{j-1}\).
4. Whenever \(a_k\notin C_k\), also \(x_k\notin C_k\). For this use one centre equation nonzero at \(a_k\) and pull it back.

All products are finite and all their factors are nonzero at \(a\). Thus this really produces a principal relative Zariski neighborhood on the fixed chart; no arbitrary ordinary shrinking has been relabelled as Zariski shrinking. On the upper stratum put \(L=\lambda_j(x)=\lambda_j(a)\).

If \(\lambda_{j-1}(a_{j-1})=L\), then
\[
 L\le\lambda_{j-1}(x_{j-1})
   \le\lambda_{j-1}(a_{j-1})=L.
\]
The value therefore persists at both points. At each point the old labels are the incident strict transforms of the preceding old labels; the fresh exceptional label is not old. The inductive equality proves (AR4).

If both preceding values exceed \(L\), both birth stages are \(j\), so every currently incident divisor is old at both points. Again (AR4) holds.

It remains to handle
\[
 \lambda_{j-1}(a_{j-1})>L
     =\lambda_{j-1}(x_{j-1}).
\tag{AR5}
\]
Let \(i=b(x)<j\). For every \(i\le k<j\), monotonicity gives
\[
 \lambda_k(x_k)=L<\lambda_k(a_k).
\]
If \(a_k\notin C_k\), condition 4 excludes \(x_k\) from the centre. If \(a_k\in C_k\), constancy on the centre and the strict inequality do the same. Thus every step from \(x_i\) to \(x\) is an analytic isomorphism near the point and creates no incident exceptional divisor. All divisors incident at \(x\) were already present at its birth, so \(E_\lambda(x)=E(x)\). The drop at \(a\) means \(E_\lambda(a)=E(a)\), proving (AR4) in this last case. \(\square\)

The last case explains why birth times need not be locally constant. The incidence conclusion remains true because the comparison point acquires no new incident exceptional divisor during its longer constant-value history.

Put \(s(a)=|E_\lambda(a)|\) and order \(P=(\lambda,s)\) lexicographically. The lemma immediately proves that \(P\) is nonincreasing on fixed-chart neighborhoods. On its witness neighborhood, its entire upper stratum is
\[
 \{x:P(x)\ge P(a)\}
 =\{x:\lambda(x)=\lambda(a),\ x\in H
                       \text{ for every }H\in E_\lambda(a)\}.
\tag{AR6}
\]
Indeed, a drop of the first entry makes the pair smaller, while equality of the first entry makes the old set a subset of \(E_\lambda(a)\); equality of cardinalities then means that all these old labels remain incident. The complementary new labels satisfy
\[
 E(x)\setminus E_\lambda(x)
   =E(x)\cap\bigl(E(a)\setminus E_\lambda(a)\bigr)
\tag{AR7}
\]
on the upper \(\lambda\)-stratum.

### Why analytic order satisfies the step hypotheses

The order \(\operatorname{ord}_a g\) of a nonzero analytic germ is the degree of its first nonzero Taylor term; a unit has order zero. It is unchanged by multiplication by an analytic unit. If \(g\) is analytic on a coordinate chart and has order \(d\) at \(a\), some coordinate derivative of degree \(d\) is nonzero there. Where that derivative remains nonzero, every order is at most \(d\). Thus order is nonincreasing on a neighborhood of the precise form (AR2).

Here is the transformation calculation, including its hypotheses. Let the centre be
\(C=\{u_1=\cdots=u_c=0\}\) in coordinates \((u,z)\). Suppose \(g\) has the same finite order \(d\ge1\) at every point of this centre portion. The derivatives in the normal variables of degrees less than \(d\) vanish at every \((0,z)\). Taylor expansion in \(u\), with analytic coefficient functions of \(z\), therefore gives
\[
 g(u,z)=\sum_{|\alpha|\ge d}a_\alpha(z)u^\alpha.
\tag{AR8}
\]
In a blowing-up chart write \(u_l=e\) and \(u_i=e v_i\) for \(i\ne l\), \(i\le c\), retaining \(z\). The quotient
\[
 g'=e^{-d}g\circ\sigma
\tag{AR9}
\]
is analytic, by (AR8). Fix a point \((0,z_0)\) of the centre. The degree-\(d\) Taylor term of \(g\) there is a nonzero homogeneous polynomial \(P(u)\) in the normal variables alone: all terms of normal degree below \(d\) vanished identically in (AR8). Consequently
\[
 g'(0,v,z_0)=P(v_1,\ldots,v_{l-1},1,v_{l+1},\ldots,v_c)
\tag{AR10}
\]
is a nonzero polynomial of degree at most \(d\). At every real projective direction in this chart its vanishing order is at most \(d\). Restricting an analytic germ to \(e=0,z=z_0\) can only increase its order, so \(\operatorname{ord}g'\le d\) at every point over \((0,z_0)\).

Equation (AR10) also shows that \(g'\) has no exceptional factor \(e\). Thus (AR9) is the strict transform of the principal analytic ideal, equivalently its total transform with the exceptional factor removed. To see the saturation assertion without assuming factoriality, if \(e h=g'q\), restriction to \(e=0\) gives \(0=g'(0,v,z)q(0,v,z)\). The ring of analytic germs on this smooth coordinate hyperplane is an integral domain, and the first factor is nonzero, so \(q\) is divisible by \(e\). Cancellation gives \(h\in(g')\); iteration treats higher powers. This is the ideal-theoretic strict transform. No assertion identifying it with the closure of the real zero set is needed.

Off the centre the map is an analytic isomorphism, so order is preserved. We have therefore proved both step hypotheses of the history lemma for the order of a principal analytic ideal along a tower whose centres have constant current order. Each finite stage has charts with one analytic generator of this ideal; these charts can be chosen as part of (AR1).

### The first order/history presentation on its full upper stratum

Set
\[
 \nu_1(a)=\operatorname{ord}_a g_j,\qquad
 E^1(a)=E_{\nu_1}(a),\qquad
 s_1(a)=|E^1(a)|,\qquad P_1=(\nu_1,s_1).
\tag{AR11}
\]
The history lemma applies to \(\nu_1\). For a marked analytic function \((h,b)\), with positive integer \(b\), its marked condition at \(x\) is \(\operatorname{ord}_x h\ge b\); for a finite family, impose every condition.

**First-prefix proposition.** Let \(a\) be a point of positive order \(d\) at a stage of a given order-constant SNC tower. There is a principal relative Zariski neighborhood \(V_a\) on which \(P_1(x)\le P_1(a)\), and the one family
\[
 \mathcal F_a=\{(g_j,d)\}
        \cup\{(\ell_H,1):H\in E^1(a)\}
\tag{AR12}
\]
has marked locus exactly \(\{x\in V_a:P_1(x)=P_1(a)\}\). Here \(\ell_H\) is the fixed chart equation of \(H\). At every point of this locus, the same functions and marks give that point's order/history family. Its remaining formal exceptional labels are precisely those members of \(E(a)\setminus E^1(a)\) incident at the point.

**Proof.** Multiply the history witness by a degree-\(d\) derivative of \(g_j\) nonzero at \(a\). On the resulting neighborhood, \(\operatorname{ord}_x g_j\le d\). Thus the first marked condition in (AR12) is equality of the order. Its remaining conditions say exactly that every old divisor at \(a\) passes through \(x\). Equations (AR6) and (AR7) prove all assertions. Every function in (AR12) is analytic on the original fixed chart, so it also belongs to the localization \(O(U_j)_{V_a}\). \(\square\)

This is a full upper-stratum statement, not merely an equality of germs at the selected point. Points where the order or the history count drops receive their own families. Unit points require no marking zero: the neighborhood \(\{g_j\ne0\}\) misses the current hypersurface.

There is also an ordinary transformation check. Suppose a next centre lies in a constant \(P_1\)-stratum and has normal crossings with the divisor. Near \(a\), (AR12) shows that it lies in every old divisor. The controlled transform of its mark-one equation is \(\ell_H\circ\sigma/e\), a strict-divisor equation or a unit in a chart missing that strict divisor. The controlled transform of \((g_j,d)\) is (AR9), of order at most \(d\). If that order remains \(d\), the birth stage remains the same and the old divisors are exactly the incident strict transforms of the preceding old divisors. Hence the transformed family has its marked condition exactly at the points where \(P_1\) persists. If the order drops, the first mark fails and the pair drops. This proves the claimed presentation behavior along ordinary admissible steps. Product and exceptional test transformations used later for coefficient-choice independence are a separate part of the full algorithm.

### A residual extension once the common parent data exist

The next elementary lemma states its analytic inputs explicitly. The subsequent fixed-chart witness and higher-prefix theorems construct those inputs through the recursive invariant.

Suppose a parent prefix \(P\) is bounded above by \(P(a)\) on a principal relative Zariski neighborhood \(V\). Suppose its entire equality locus there is the marked locus, on one smooth analytic coefficient manifold \(N\), of a finite family \(\{(h_i,d)\}\) with common positive integer mark. Assume that these are valid common coefficient data at every point of that parent locus, and that on \(N\cap V\) there are analytic identities
\[
 h_i=M g_i,\qquad M=\prod_H\ell_H^{m_H},\qquad m_H\in\mathbb Z_{\ge0},
\tag{AR13}
\]
where every remaining divisor equation restricts to a nonzero hypersurface germ on \(N\), and the incident restrictions are distinct normal-crossing coordinate factors on \(N\). Divisors containing \(N\), already consumed in the coefficient flag, are excluded from this product. The exponents are the exact common divisor orders at every point of the parent locus; absent divisor factors are units. Thus \(M\) is a nonzero germ and has finite order at every point under consideration. Assume the next intrinsic residual value there is
\(\nu(x)=d^{-1}\min_i\operatorname{ord}_x g_i\). The functions, coefficient manifold, and chosen coordinate derivations must be given by fractions of functions on the fixed chart with denominators nonzero on \(V\).

Let \(k=\min_i\operatorname{ord}_a g_i<\infty\). Suppose a degree-\(k\) coordinate derivative of one \(g_i\) is nonzero throughout \(N\cap V\). It follows that \(\min_i\operatorname{ord}_xg_i\le k\) there. Then \(Q=(P,\nu)\) is bounded above by \(Q(a)\) on \(V\), and for \(k>0\) its entire upper stratum is the marked locus of
\[
 \{(g_i,k)\}_i\quad\text{together with }(M,d-k)
       \text{ if }k<d.
\tag{AR14}
\]
For \(k\ge d\) there is no monomial pair. For \(k=0\), the parent and new upper strata coincide and are given on \(N\) by \((M,d)\). If all coefficient functions vanish identically on \(N\cap V\), the residual value is identically infinite there and the zero family remains the presentation.

**Proof.** At points where \(P\) drops, the pair \(Q\) drops lexicographically. On the parent equality locus, the derivative bound gives \(\nu\le k/d\). For a point of \(N\cap V\), put \(m=\operatorname{ord}M\) and \(l=\min_i\operatorname{ord}g_i\). Multiplication of first nonzero homogeneous Taylor terms gives additivity of order, so the parent marked condition is exactly \(m+l\ge d\). On the new upper stratum \(l=k\), which implies the conditions (AR14). Conversely, (AR14) implies \(m+l\ge d\), so the point belongs to the parent equality locus. The derivative bound then forces \(l=k\). If \(k=0\), one residual function is a unit throughout, so the parent condition is just \(m\ge d\). The all-zero case is immediate from the stated identities. \(\square\)

The hypothesis about fractions is substantive. An analytic quotient in a germ ring is not automatically a fraction of analytic functions on a previously fixed chart. Nor do represented equations alone prove that they describe the intrinsic parent invariant on the full upper stratum. The first-prefix proposition supplies that semantic assertion at the first stage; further coefficient, quotient, history and test-equivalence arguments must supply it at each later stage.

### Descent of matched analytic centres

One part of the algebraic resolution bridge, §5 has a direct analytic proof, under an exact matching hypothesis. Let \((U_i)\) be a countable open cover of a real analytic manifold \(M\), and suppose \(C_i\subset U_i\) are closed smooth analytic centres of positive codimension, with normal crossings with the given exceptional divisor, and
\[
 C_i\cap U_j=C_j\cap U_i
\tag{AR15}
\]
as embedded analytic submanifolds on every full overlap. Then \(C=\bigcup_i C_i\) is a unique closed smooth analytic centre in \(M\). Indeed, (AR15) gives \(C\cap U_i=C_i\); its complement is open on each member of the cover and hence open in \(M\). Smoothness, analyticity and the normal-crossing property are local.

The corresponding analytic blowings-up glue. In coordinates with \(C=\{x_1=\cdots=x_c=0\}\), the local map is the projection of
\[
 \{(x,[t])\in U\times\mathbb{RP}^{c-1}:
            x_it_l=x_lt_i\text{ for every }i,l\}.
\tag{AR16}
\]
Its \(t_l\ne0\) chart has coordinates \(x_l=e\), \(x_i=e v_i\) for \(i\le c\), \(i\ne l\), and the other \(x_i\); thus it is smooth. It is proper over \(U\), since (AR16) is closed in a product with compact projective space, and is an analytic isomorphism off the centre.

Two local regular sets of generators of the centre ideal are related, near a centre point, by an invertible analytic matrix \(A(x)\). The lifted change is \([t]\mapsto[A(x)t]\). It is forced off the exceptional hypersurface, whose complement is dense in the displayed smooth charts, and therefore is unique everywhere. The lifts satisfy the cocycle and glue. The result is Hausdorff because points with distinct images can be separated in the base, while points with the same image lie in one open local blowing-up space. A countable cover gives second countability. Properness follows by covering any compact subset of the base by finitely many compact pieces contained in these coordinate neighborhoods. Controlled ideals and labelled strict divisors agree because their defining pullback and division operations agree on the overlaps.

This proves analytic descent for a finite sequence once the centre at every stage has been matched on every full overlap; identity stages can be inserted beforehand. It does not match independently chosen algorithms, choose a globally closed maximum stratum, or prove a locally finite bound on their number of steps.

The following sections extend these first-prefix arguments to the higher local invariant and its fixed-chart presentations. They then prove analytic closed thresholds and finite values on compact sets, choose closed canonical centres, establish compact-local termination, and compare independently constructed local algorithms before the global assembly.


## What blow-up tests determine about a marked family

The next coefficient step divides out exceptional factors. To show that its numerical answer is independent of the chosen coefficient equations, we need to recover two quantities from the transformations those equations allow: their normalized point order and their normalized order along each labelled divisor. The distinction between ordinary and exceptional tests is essential. An ordinary test divides by the assigned exceptional power; an exceptional test in this argument uses plain pullback.

These tests come from [Bierstone–Milman, *Canonical desingularization in characteristic zero*, author manuscript of 25 November 1996, Propositions 4.8 and 4.11, with proofs in §5, pp.31–33](https://www.math.toronto.edu/bierston/inventionnes.ps). We give the convergent analytic calculation, including the criterion along an entire divisor section and an explicit bound for stabilization.

### Marked equations and what it means to compare their tests

Let \(N\) be a smooth analytic germ of codimension \(p\) in an ambient manifold at \(a\). A finite marked family consists of analytic germs \((h_i,b_i)\) on \(N\), with positive integer marks and \(\operatorname{ord}_a h_i\ge b_i\). Its marked locus is

\[
 S_{\mathcal H}=\{x\in N:\operatorname{ord}_x h_i\ge b_i
                          \text{ for every }i\}.
\tag{OR1}
\]

The zero germ has infinite order. Fix labelled smooth divisor germs \(\mathcal E\) in the ambient manifold which meet \(N\) in distinct normal-crossing coordinate hypersurfaces. In particular, none contains \(N\).

We use the following operations on these data.

* An **ordinary test** blows up a smooth local centre contained in the marked locus and having normal crossings with the divisor family. On the strict transform of \(N\), replace \((h_i,b_i)\) by \((e^{-b_i}h_i\circ\sigma,b_i)\), where \(e\) is a local equation of the new divisor. The centre-wide Taylor argument in [Reducing marked equations to their coefficients](#reducing-marked-equations-to-their-coefficients) proves this quotient analytic. Continue at points where all assigned marked orders persist.
* A **product test** adjoins a variable \(t\), pulls back the family, and records the divisor \(t=0\).
* An **exceptional test string** starts with such a product and a selected old divisor \(H\). Blow up the intersection of its strict transform with the most recently created divisor, repeatedly following the point on the strict transform of \(H\). Throughout this string the marked functions undergo plain pullback. In simultaneous normal-crossing coordinates these are ordinary analytic blow-ups of intersections of coordinate hypersurfaces; they need not have centres in (OR1).

After an exceptional string, ordinary and product tests are again allowed. The strings can be appended at intermediate stages, always starting a new string with its own product. No statement below requires unrestricted exceptional transformations with arbitrarily recomputed marks.

Two presentations with the same ambient germ, the same codimension \(p\), and the same labelled divisor germs are *test equivalent* here if their marked loci agree as ambient germs after every such allowed continuation, including agreement of the points at which an ordinary transform can continue. The presenting submanifolds need not be equal. This definition is stable under any allowed initial part of a sequence: further tests can simply be appended to it.

To calculate, one can make all marks a common positive integer \(d\). Choose a common multiple of the \(b_i\) and replace

\[
 (h_i,b_i)\quad\text{by}\quad(h_i^{d/b_i},d).
\tag{OR2}
\]

The order of a power is the exponent times the order of the original germ. Under an ordinary test its controlled transform is exactly the corresponding power of the old controlled transform; products and plain pullbacks also commute with powers. Thus (OR2) preserves every test, not just the initial locus. Multiplication by an analytic unit has the same invariance. All calculations below use integral powers of analytic functions.

### Recovering the point order by measuring how many section tests remain

For common mark \(d\), write

\[
 m=\min_i\operatorname{ord}_a h_i,\qquad \mu=m/d.
\tag{OR3}
\]

**Order-recovery lemma.** The value \(\mu\), including infinity, is the same for two test-equivalent presentations of the same codimension. For this assertion ordinary and product tests alone suffice.

**Proof.** If \(m=\infty\), all functions are zero germs and the marked locus is the whole germ \(N\). Conversely, a marked locus which is a smooth ambient germ of codimension \(p\) and is contained in \(N\) must coincide with \(N\) near \(a\): the inclusion of equal-dimensional submanifolds is a local isomorphism. Each \(h_i\) then vanishes at every point of a neighborhood in \(N\), since its mark is positive, and is the zero germ. Thus infinity can be recognized from the common ambient marked locus and the codimension.

Suppose now \(m<\infty\). Take a product with a line and follow the arc \(t\mapsto(a,t)\). Blow up its endpoint \(\beta\) times, each time following the lifted endpoint. In local coordinates \(x\) on \(N\), centred at \(a\) and adapted to the divisors, the chart following this arc has

\[
 x=t^\beta y,\qquad
 h_{i,\beta}(y,t)=t^{-\beta d}h_i(t^\beta y)
     =\sum_\alpha c_{i,\alpha}
          t^{\beta(|\alpha|-d)}y^\alpha.
\tag{OR4}
\]

This series converges on a small chart. Every exponent of \(t\) is nonnegative, since \(|\alpha|\ge m\ge d\). At the lifted endpoint its order is
\((\beta+1)\operatorname{ord}_a h_i-\beta d\), hence at least \(d\). All the point centres and lifted marked points used in this calculation are therefore permitted. The point centres have normal crossings with the current divisor family. In this chart each old incident divisor remains a coordinate hyperplane, the most recent exceptional divisor is \(t=0\), and the preceding exceptional divisors from the point string miss the followed point.

The exact common power of \(t\) in (OR4) is \(t^{\beta(m-d)}\). Indeed, the restriction after dividing by that power includes the nonzero homogeneous degree-\(m\) part of one \(h_i\), viewed as a polynomial in \(y\). That polynomial need not be nonzero at \(y=0\); it is nonzero as a germ on the divisor, which is what exact divisorial order requires.

Let \(W_\beta\) be the intersection of the latest exceptional divisor with the current presenting submanifold. Its germ is \(t=0\) in (OR4). It lies in the marked locus as a whole germ exactly when
\(\beta(m-d)\ge d\). For sufficiency, every function is divisible by \(t^d\), so its point order is at least \(d\) at every point of the section. For necessity, if the common power is less than \(d\), the nonzero homogeneous polynomial just exhibited is nonzero at points of \(t=0\) arbitrarily close to the endpoint. The corresponding point order there is that smaller power; the entire section cannot be marked.

This section is recognizable without choosing \(N\). Any smooth germ of codimension \(p\) in the latest exceptional hypersurface, contained in the ambient marked locus, lies in \(W_\beta\) and has the same dimension as \(W_\beta\). It must equal \(W_\beta\) as a germ. Thus two equivalent presentations identify the very same section whenever it exists. It is a permissible smooth centre, normal crossing with the other coordinate divisors.

Blowing up this section restricts to a Cartier identity on the presenting submanifold. Its controlled functions are nevertheless divided by \(t^d\). After \(\alpha\) such section blow-ups, the remaining common exceptional power is
\(\beta(m-d)-\alpha d\). Whenever a section blow-up is allowed, the lifted endpoint is still marked: the least point order there is this remaining power plus \(m\), and the remaining power is nonnegative. The next entire section is marked precisely when the remaining power is at least \(d\).

After a common section blow-up, the followed point for either presentation is still marked by this calculation. Equality of the transformed ambient marked loci forces the two lifts to coincide: each presenting submanifold has only one point over that endpoint, because its restricted blow-up is the Cartier identity. Thus the section tests really continue at common ambient points.

Consequently the observable successful section tests form the set

\[
 T=\{(\beta,\alpha):\beta\ge1,\ \alpha\ge0,
                         \beta(\mu-1)-\alpha\ge1\}.
\tag{OR5}
\]

Here \(\alpha\) counts section blow-ups already performed after the \(\beta\) point blow-ups. Every preceding section test in a successful pair also succeeds, by the same inequality. The set is empty precisely when \(\mu=1\). Otherwise it determines

\[
 \mu=1+\sup_{(\beta,\alpha)\in T}\frac{\alpha+1}{\beta}.
\tag{OR6}
\]

The inequality in (OR5) proves the upper bound for the supremum. Taking \(\alpha+1=\lfloor\beta(\mu-1)\rfloor\) for sufficiently large \(\beta\) proves the reverse bound; these positive integers give pairs in \(T\) and their ratios approach \(\mu-1\). All the operations defining \(T\) and the test for its entire section are common to equivalent presentations. They therefore have the same value of \(\mu\). \(\square\)

### Recovering one divisor order from an eventual slope

For an incident labelled divisor \(H\), set
\(q_H=\min_i\operatorname{ord}_{H,a}h_i\). Its normalized order is \(\mu_H=q_H/d\). Divisor order means the exponent of its local equation dividing the analytic germ; it is not the point order at an intersection of divisors.

**Divisor-recovery lemma.** If \(\mu<\infty\), every \(\mu_H\) is determined by the allowed tests. Thus test-equivalent presentations of the same codimension have the same residual number
\(\nu=\mu-\sum_H\mu_H\). These statements also hold at any intermediate common marked stage of an allowed sequence.

**Proof.** Choose normal-crossing coordinates on \(N\) with \(H\cap N=\{x_1=0\}\). After adjoining \(t\) and performing \(j\) exceptional tests following \(H\), the chart substitution is
\(x_1=t^j y_1\), \(x_i=y_i\) for \(i>1\). Because these tests use plain pullback, their normalized point orders at \((y,t)=0\) are

\[
 \mu_j=\frac1d
   \min_{i,\alpha:c_{i,\alpha}\ne0}
                      (|\alpha|+j\alpha_1).
\tag{OR7}
\]

Distinct monomials remain distinct under this substitution, so cancellation cannot alter the minimum. The transformed marked order stays at least \(d\), since pullback only adds nonnegative weights to the initial exponents. The two divisors defining every exceptional centre remain transverse coordinate hypersurfaces, so the full string is defined.

Put \(q=\min\alpha_1=q_H\), over all the nonzero terms of the family, and let \(\ell\) be the least \(|\alpha|\) among terms with \(\alpha_1=q\). Both minima exist, as nonnegative integers, because at least one germ is nonzero. If \(j>\ell\), a term with \(\alpha_1\ge q+1\) has weight at least \(j(q+1)>jq+\ell\). Among terms with \(\alpha_1=q\) the smallest weight is exactly \(jq+\ell\). Hence

\[
 \mu_j=(jq+\ell)/d,
 \qquad \mu_{j+1}-\mu_j=q/d=\mu_H
 \quad(j>\ell).
\tag{OR8}
\]

The order-recovery lemma recovers each \(\mu_j\) by appending its ordinary/product tests to the chosen exceptional string. The string itself is determined by the labelled divisor and the new product divisor. Equivalent presentations therefore give the same sequence \((\mu_j)\), and so the same eventual slope. Repeating this separately for each label proves the assertion for \(\nu\). Starting all these tests after any common marked stage proves the stagewise statement as well. \(\square\)

For completeness, \(\nu\ge0\) follows directly from analytic division. In simultaneous divisor coordinates, every Taylor monomial of every \(h_i\) contains \(\prod_H x_H^{q_H}\). Dividing out that integral monomial leaves a convergent analytic family \(g_i\) after shrinking. Additivity of order in the convergent power-series domain gives
\(\nu=d^{-1}\min_i\operatorname{ord}_a g_i\). This is exactly the residual number used in (AR13)–(AR14). The tests establish its independence once coefficient families are test equivalent. They do not by themselves construct a coefficient family or prove the whole recursive equivalence.

### Exercise: read an exceptional multiplicity from three tests

Take \(N=\mathbb R^2\), coordinates \((x,y)\), marked family
\(\{(x^2+y^5,2)\}\), and labelled divisor \(H=\{x=0\}\).
Compute its normalized point order and the normalized orders after \(j\) exceptional tests following \(H\). Explain why using only the first exceptional test would give the wrong divisor order.

**Solution.** At the origin the point order is two, so \(\mu=1\). A product followed by \(j\) exceptional tests substitutes \(x=t^j u\) and gives \(t^{2j}u^2+y^5\), without division by a power of \(t\). Its normalized order is
\(\mu_j=\min(2j+2,5)/2\). Thus \(\mu_0=1\), \(\mu_1=2\), and \(\mu_j=5/2\) for every \(j\ge2\). The first difference is one, but the eventual difference is zero. The latter is the correct normalized divisor order: restricting \(x^2+y^5\) to \(x=0\) gives the nonzero germ \(y^5\), so no factor \(x\) divides the original function. In particular, \(\nu=1\). The slope must be taken after stabilization; the changing minimum in (OR7) explains the misleading first test.

## Analytic representatives on one fixed chart

A coefficient quotient may be analytic on a smooth germ without yet being represented by functions on the original chart. We now supply that representation, including when the divided monomial vanishes at the selected point. The analytic inputs are the programme proofs of Oka coherence and Cartan's Theorem A. The latter is proved there from Theorem B, whose bump, approximation and inverse-limit arguments are supplied in that course. Thus the needed global section theorem has an explicit internal proof provider; it is not inferred merely from local coherence or from the existence of analytic quotient germs.

### The maintained ring and the denominator lemma

Choose a conjugation-invariant complex polydisc \(\Omega\subset\mathbb C^n\), with real centre and finite positive radii, and put \(U=\Omega\cap\mathbb R^n\). The finite initial real analytic data are assumed to extend holomorphically to this polydisc; such charts can be chosen locally for any finite analytic input. Write
\[
 A=\{F\in\mathcal O(\Omega):F(\bar z)=\overline{F(z)}\},
 \qquad R_a=\{F/G:F,G\in A,\ G(a)\ne0\},\quad a\in U.
 \tag{AW1}
\]
Restriction embeds \(R_a\) into the fixed real-chart localization \(O(U)_a\). We maintain this stronger ring, rather than identifying either localization with the full analytic germ ring. Sums, products, nonnegative integral powers, quotients by represented units, and derivatives in the original coordinates preserve \(R_a\).

**Finite denominator lemma.** If \(F,f_0,\ldots,f_p\in A\) and
\(F_a\in(f_0,\ldots,f_p)\mathcal O_{\Omega,a}\), there are \(q,B_0,\ldots,B_p\in A\) such that
\[
 q(a)=1,\qquad qF=\sum_{i=0}^p f_iB_i\quad\hbox{on }\Omega.
 \tag{AW2}
\]

**Proof.** The sheaf
\[
 K=\ker\bigl(\mathcal O_\Omega^{p+2}\longrightarrow\mathcal O_\Omega,
       \ (q,B_0,\ldots,B_p)\longmapsto qF-\sum_i f_iB_i\bigr)
\]
is coherent by Oka coherence and the kernel theorem for coherent sheaves. The local membership hypothesis supplies a section germ of \(K_a\) whose first coordinate is one. Cartan's Theorem A expresses this germ as a finite \(\mathcal O_{\Omega,a}\)-linear combination of germs of global sections of \(K\). At least one of those global sections has first coordinate nonzero at \(a\): otherwise evaluation of the first coordinate would give \(1=0\). Select it and divide by its first-coordinate value at \(a\), so that its first coordinate is one there. Its entries satisfy (AW2) as a global holomorphic identity.

The polydisc is Stein in the precise exhaustion sense needed by the provider. For example,
\(\sum_\ell(R_\ell^2-|z_\ell-c_\ell|^2)^{-1}\)
is a smooth strictly plurisubharmonic exhaustion: its Levi matrix is diagonal with positive diagonal entries, and it tends to infinity at every boundary point. Theorem A therefore applies.

Finally reflect every entry by \(H^*(z)=\overline{H(\bar z)}\) and average the section with its reflection. The row functions are in \(A\), so the averaged tuple is still in \(K(\Omega)\); its first coordinate still has value one at the real point \(a\). All its entries are now in \(A\). This proves the real-witness statement. \(\square\)

Only one consequence of the section theorem was used: a global relation with first coordinate nonzero at the chosen point. Equivalently, it follows from \(H^1(\Omega,\mathfrak m_aK)=0\), where \(\mathfrak m_a\) is the coherent ideal of the point. The quotient \(K/\mathfrak m_aK\) is supported at \(a\); its section represented by the local relation lifts by the cohomology exact sequence. The cited internal Theorem B supplies precisely this vanishing as well.

### Division on the coefficient manifold

Suppose a smooth real analytic germ \(N_a\subset U\) of codimension \(p\) is defined by represented functions
\(z_j=Z_j/E_j\in R_a\), with \(z_j(a)=0\) and independent differentials. Suppose
\[
 h=H/T\in R_a,\qquad M=P/S\in R_a,
 \qquad h|_{N_a}=M|_{N_a}\,g,
 \tag{AW3}
\]
where \(g\) is an analytic germ on \(N_a\), \(M|_{N_a}\) is a nonzero germ, and \(T(a)S(a)\ne0\). In the residual construction \(M\) is a monomial with nonnegative integral exponents in divisor coordinates; it may vanish at \(a\).

**Quotient lemma.** There exist \(q,B,B_1,\ldots,B_p\in A\), with \(q(a)=1\), for which
\[
 qSH=PB+\sum_{j=1}^p Z_jB_j\quad\hbox{on }\Omega,
 \qquad
 g=\left.\frac{B}{qT}\right|_{N_a}.
 \tag{AW4}
\]
In particular, the denominator representing \(g\) is nonzero at \(a\). It contains no factor that one has merely assumed invertible because it is part of \(M\).

**Proof.** Since \(E_j(a)\ne0\), the germs \(Z_j\) generate the same smooth-germ ideal as the \(z_j\), and their differentials at \(a\) are independent. Complexify the real analytic identity in (AW3). In local holomorphic coordinates \((u,v)\) with \(v_j=Z_j\), the germ of \(g\) has an ambient lift \(G(u,v)=g(u)\). Hence \(SH-PTG\) vanishes on \(\{v=0\}\). A holomorphic germ \(L\) vanishing there belongs to \((v_1,\ldots,v_p)\); for instance
\[
 L(u,v)-L(u,0)
   =\sum_jv_j\int_0^1\partial_{v_j}L(u,tv)\,dt.
\]
Thus \((SH)_a\in(P,Z_1,\ldots,Z_p)\mathcal O_{\Omega,a}\). Apply (AW2) to obtain the first identity in (AW4). On \(N_a\) it gives
\(h=M\,B/(qT)\). The local ring of a smooth analytic germ is a domain, so the nonzero germ \(M|_{N_a}\) can be cancelled. This proves the displayed representative for \(g\). The local lift \(G\), and the inverse coordinate map used to construct it, need not extend to \(\Omega\); their only role was to establish the local ideal membership to which (AW2) applies. \(\square\)

The same argument records zero identities. If \(H/T\) restricts to zero on \(N_a\), there are \(q,B_j\in A\), with \(q(a)=1\), satisfying
\[
 qH=\sum_j Z_jB_j\quad\hbox{on }\Omega.
 \tag{AW5}
\]
This is the certificate that makes a zero germ vanish on all of the subsequently chosen coefficient manifold inside a common principal open set. The ambient case \(p=0\) of (AW4) also represents an analytic controlled quotient \(h/e^b\), where \(e\) is a represented exceptional equation and \(b\) is a nonnegative integer.

### Represented coordinates and their derivatives

The quotient lemma does not authorize arbitrary local coordinates as elements of \(R_a\). We choose coordinates with representatives. Suppose represented functions on \(N_a\) already have independent differentials there; these can include incident divisor equations and a retained transverse equation. The restrictions of the original ambient coordinate differentials span \(T_a^*N\). Complete the given list using constant real linear combinations of those coordinates. With the defining equations \(z_1,\ldots,z_p\), this gives an ambient list
\[
 Y=(z_1,\ldots,z_p,x_1,\ldots,x_{n-p}),\qquad
 J=\frac{\partial Y}{\partial \xi},\qquad \det J(a)\ne0,
 \tag{AW6}
\]
all in \(R_a\). Here \(\xi\) denotes the original ambient coordinates. The analytic inverse function theorem supplies local coordinates, while the adjugate formula represents \(J^{-1}\) in \(R_a\). No global inverse of \(Y\) is asserted.

If coordinates adapted to a supplied smooth centre \(C\cap N\) are needed, assume that its defining equations are represented as well. Retain the divisor equations which contain that centre, complete their conormal differentials by a subset of the centre equations, and complete the remaining tangent differentials by ambient linear functions while retaining the other divisor coordinates. The stated normal-crossing hypothesis gives the required independence. The chosen normal equations vanish on the centre and have its codimension, so their common zero germ is the centre germ. This is a represented adapted completion on the fixed chart.

The derivations
\[
 \mathcal D_i=\sum_{\ell=1}^n (J^{-1})_{\ell,p+i}\,
                   \partial_{\xi_\ell}
 \tag{AW7}
\]
annihilate the defining equations \(z_j\) and satisfy \(\mathcal D_i x_k=\delta_{ik}\). Their restrictions to \(N_a\) are its coordinate derivatives. Quotient differentiation shows that every finite iterate applied to a represented function remains represented. These restrictions are independent of the chosen ambient representative because the derivations preserve the ideal generated by the \(z_j\).

For a fresh transverse choice, when the ordinary coefficient construction supplies a compatible tangent vector \(v\in T_aN\), choose the completing covectors so that all but the transverse one annihilate \(v\), while the transverse covector takes value one. This is possible when the retained divisor covectors annihilate \(v\), as required by compatibility. The resulting transverse derivation has value \(v\) at \(a\). If a marked function has exact order \(d\) and leading form nonzero on \(v\), its \(d\)-th derivative in this direction is nonzero. Terms differentiating the vector-field coefficients involve lower derivatives of the function and vanish at \(a\). Consequently the coefficient construction's defining equation \(\mathcal D_t^{d-1}h_*\) and coefficients
\[
 \left.\frac{1}{q!}\mathcal D_t^q h\right|_{\widetilde N},
 \qquad
 \widetilde N=\{\mathcal D_t^{d-1}h_*=0\}\subset N,
 \tag{AW8}
\]
have representatives. The nonzero distinguished derivative certifies that the extra equation is independent. Existence and persistence of a compatible transverse direction belong to the coefficient construction; the calculation here preserves its representation once that geometric input is supplied.

### One principal open set for all the finite witnesses

Consider one finite presentation at \(a\), with the quotient identities (AW4), any zero identities (AW5), and its finite coordinate flag. Multiply together all the following functions in \(A\): the denominators of its representatives, the factors \(q\) in its quotient and zero identities, and numerator representatives of the nonzero Jacobian determinants used in (AW6). Include the distinguished derivative witnesses used for each smooth coefficient hypersurface. Every factor is nonzero at \(a\). Their finite product \(D\) gives
\[
 V_a=\{x\in U:D(x)\ne0\}.
 \tag{AW9}
\]
Every finite function belongs to \(O(U)_{V_a}\), the selected Jacobians remain nonzero, and the global identities hold on the smooth coefficient manifolds cut out by these equations throughout \(V_a\). The represented coordinates are local coordinates at every point of those manifolds; global injectivity of their coordinate map is unnecessary.

There are two more finite certificates needed for residual orders. Suppose on a coefficient manifold the identities are
\(h_i=M g_i\), with \(M=\prod_Hx_H^{m_H}\), where the incident \(x_H\) belong to its represented coordinate list.

First assume \(m_H\) is the exact common divisor exponent at \(a\). Some residual \(g_i\) has nonzero germ on \(\{x_H=0\}\). A derivative of its restriction in the other coordinate directions is nonzero at \(a\). That derivative is represented by (AW7). Include its nonzero numerator, as well as its denominator, in \(D\). At every point of \(N\cap V_a\cap\{x_H=0\}\), this tangential derivative remains nonzero. Therefore \(g_i\) cannot be divisible by \(x_H\) there. The common exponent \(m_H\) is exact throughout that set. Repeat for the finitely many incident formal divisors. Divisor equations nonzero at \(a\) may also be included in \(D\), excluding those labels throughout \(V_a\).

Second let \(k=\min_i\operatorname{ord}_a g_i<\infty\), where orders are computed on the smooth coefficient manifold. Choose a nonzero coordinate derivative of total degree \(k\) of one \(g_i\), and include its represented numerator in \(D\). Then
\[
 \min_i\operatorname{ord}_xg_i\le k
       \quad\text{for every }x\in N\cap V_a.
 \tag{AW10}
\]
For \(k=0\), this keeps one residual function nonzero. For an all-zero coefficient family, use (AW5) instead: it makes the family identically zero on \(N\cap V_a\), rather than inferring this from a zero germ alone. These are precisely the quotient, exponent and derivative witnesses required by the preceding residual-extension lemma. Identifying the parent invariant's entire equality stratum, and the correct divisor histories there, is a separate semantic assertion.

### Elementary division and its exact limit

There is a direct alternative to (AW4) when the coefficient manifold and divided factors are coordinates on the fixed polydisc itself. Suppose
\(N=\{\xi_1=\cdots=\xi_p=0\}\cap\Omega\),
and \(M\) is a monomial in some of the remaining coordinate variables vanishing at \(a\). If \((F/G)|_{N_a}\) is divisible by \(M\), with \(G(a)\ne0\), then \(F|_{N_a}\) is divisible by \(M\). For each factor \(x_H^{m_H}\), the derivatives of \(F|_N\) of degrees below \(m_H\) in that variable vanish on a neighbourhood of \(a\) in \(N\cap\{x_H=0\}\). That coordinate slice is a connected polydisc, so the holomorphic identity theorem makes them vanish on the whole slice. Taylor expansion in the coordinate variables then shows that \((F|_N)/M\) is holomorphic on the entire polydisc \(N\). Extend this function to \(\Omega\) independently of its first \(p\) coordinates. This gives a global numerator \(B\) with
\[
 ((F/G)|_N)/M=(B/G)|_N
 \tag{AW11}
\]
near \(a\). In particular this elementary argument handles division by an actual exceptional coordinate on a fixed blow-up chart.

It does not replace the quotient lemma for a general implicitly defined coefficient manifold on a previously fixed chart. Straightening that manifold produces local coordinates; it need not provide a global coordinate product or a global inverse coordinate map on that same chart. To illustrate the ring distinction, for \(0<b<1\) the germ \(\exp(1/(b-x))\) at zero is not \(F/G\) with \(F,G\) real analytic on \((-1,1)\) and \(G(0)\ne0\). Such an equality would give \(F=G\exp(1/(b-x))\) throughout \((-1,b)\) by the identity theorem. At \(b\), the nonzero analytic function \(G\) has finite order, so the right side grows faster than every inverse power as \(x\uparrow b\), whereas \(F\) remains bounded. This is a contradiction. The example concerns arbitrary germs; (AW4) proves the stronger representation that is available for the particular quotients of represented data used here.

### Finite analytic towers and the remaining resolution problem

For a supplied finite analytic blow-up tower, choose chart stacks whose analytic maps extend to holomorphic maps
\(\Omega_j\to\Omega_{j-1}\)
on the whole chosen polydiscs. They exist locally: choose coordinates adapted to each given smooth centre and its normal-crossing divisor, complexify the finite coordinate data, and shrink each next polydisc so that its map lands in the preceding one. A cover of each stage by such fixed stacks is enough. Once a stack is chosen, it is fixed before the pointwise coefficient recursion on its charts.

Pullback through such a map sends a global numerator or denominator on \(\Omega_{j-1}\) to one on \(\Omega_j\), and preserves nonvanishing at the point over its ancestor. Equations for the currently listed divisor hypersurfaces are represented. Ordinary controlled divisions, divisions defining strict coefficient flags when the centre geometry permits them, and residual monomial divisions are represented by (AW4). Derivatives and coefficient restrictions are represented by (AW6)–(AW8). Integral powers used to clear marks preserve the same class. Therefore every finite branch made from these operations has represented functions and equations on its fixed chart, including branches rebuilt after an earlier invariant prefix drops. Different points and different branches may have different numerators and denominators on that same chart; no finite enumeration of all branches is claimed.

For transport along a persisting prefix, this statement applies to the actual data being transported. If an old-divisor count drops, the representation argument does not authorize retaining a positive-mark equation for a divisor now absent: the geometric recursion must transport its unadjoined family and then adjoin the currently incident old block. Representation preserves the inputs of that operation; it does not change the history rule.

This proves the fixed-chart analytic witness step using an existing internal analytic theorem, with a direct elementary proof for coordinate-monomial division as well. The higher-prefix argument below uses these witnesses. The analytic-threshold theorem then derives the topology and finite-value properties needed for centre selection; the compact-fibre and overlap theorems complete the tower construction. The total-function and protected-complement lemmas apply to those towers. The target remains an arbitrary-dimensional real analytic manifold.

## Higher analytic prefixes, current history, and rebirth

We now continue the first order/history prefix through its higher coefficient and residual steps. This part concerns a finite given tower of permissible analytic blowings-up. It constructs the local word and its compatible local presentations, including points at which an earlier entry drops. The later centre and termination theorems use this local construction to produce the canonical towers themselves.

The argument uses three proved ingredients in this lesson: [coefficient reduction and persistence](#reducing-marked-equations-to-their-coefficients), [recovery of marked point and divisor orders by tests](#what-blow-up-tests-determine-about-a-marked-family), and [history incidence on fixed charts](#fixed-chart-history-and-the-first-analytic-resolution-prefix). For the fixed-chart conclusion it also uses [analytic representatives on one fixed chart](#analytic-representatives-on-one-fixed-chart), with the analytic input stated there. The last ingredient supplies actual quotient and derivative representatives; the proof below supplies the missing assertion that they describe the invariant on the entire upper stratum of a principal relative Zariski neighborhood.

The human source comparison is [Bierstone–Milman, *Canonical desingularization in characteristic zero*, author manuscript of 25 November 1996](https://www.math.toronto.edu/bierston/inventionnes.ps): Example 4.16 and the statements of Construction 4.23 and Proposition 4.24 are on pp.29–30; the coefficient and residual proofs are on pp.33–35; the recursive history construction is in §§6.9–6.15, pp.37–39. These are the page numbers of the 70-page author manuscript. We keep fixed marks during tests and distinguish them from marks recomputed at an ordinary stage.

### Exact residual transport under an ordinary step

Let \(N\) be a smooth analytic coefficient manifold and \(\mathcal E\) a finite labelled divisor family whose restrictions to \(N\) are distinct normal-crossing coordinate hypersurfaces. No member of \(\mathcal E\) contains \(N\). Clear the marks of a finite nonzero family to one positive integer \(d\), and factor
\[
 \mathcal H=\{(h_i,d)\}_i,\qquad
 h_i=M g_i,\qquad
 M=\prod_{H\in\mathcal E}x_H^{q_H},\quad
 q_H=\min_i\operatorname{ord}_H h_i,
 \qquad k=\min_i\operatorname{ord}_a g_i.
\tag{RX1}
\]
The division is analytic: in simultaneous coordinate series, every term of each \(h_i\) has exponent at least \(q_H\) in every divisor coordinate, and shifting those finitely many exponents preserves convergence on a smaller chart. No divisor coordinate divides all the \(g_i\). The residual value is \(\nu=k/d\), independently of the common mark, by the order-recovery result.

For \(0<k<\infty\), its normalized residual family is
\[
 \mathcal G=\{(g_i,k)\}_i\ \cup\
 \begin{cases}
  \{(M,d-k)\},& k<d,\\
  \varnothing,& k\ge d.
 \end{cases}
\tag{RX2}
\]
At least one residual function has its assigned order exactly, so this family has normalized order one. For \(k=0\), one residual function is a unit and the terminal family is \(\{(M,d)\}\). The all-zero coefficient family is the separate terminal value \(\infty\); no common exceptional factor is assigned to it.

Suppose a smooth centre \(C\subset N\) lies in the marked locus of (RX2) and has normal crossings with the divisor coordinates. Put \(q_C=\sum_{H\supset C}q_H\), using the divisor germs containing the centre germ. The marked conditions along the whole centre give
\(g_i\in I_C^k\), and, when \(k<d\), \(M\in I_C^{d-k}\). This is a centre-wide statement: expand in normal coordinates of \(C\); their derivatives below the assigned degree vanish at every point of \(C\), so the corresponding analytic coefficient functions vanish. For the coordinate monomial the second membership is \(q_C\ge d-k\).

In a blowing-up chart with new exceptional equation \(e\), the controlled coefficient transforms factor as
\[
 h_i'=e^{-d}h_i\circ\sigma_N=M'g_i',\qquad
 M'=e^{-(d-k)}M\circ\sigma_N,
 \qquad g_i'=e^{-k}g_i\circ\sigma_N.
\tag{RX3}
\]
Both factors are analytic. If \(k\ge d\), the first is \(e^{k-d}M\circ\sigma_N\); if \(k<d\), its analyticity follows from the monomial marked condition. Its new exponent is
\[
 q_{\rm new}=q_C+k-d\ge0,
\tag{RX4}
\]
and the exponents of the old strict divisors are unchanged.

This is the **exact** common exceptional factor, not merely a possible factor. Choose \(g_*\) of order \(k\) at \(a\). The normal Taylor-polynomial argument in (AR8)–(AR10), applied to \(g_*\in I_C^k\), shows that \(g_*'\) has order at most \(k\) at every point over \(a\) and has no factor \(e\). For an old strict divisor that is present, its complement of the new exceptional divisor is dense in that strict divisor germ. There the map is an isomorphism and a common old factor of all the \(g_i'\) would give a common old factor of all the original \(g_i\). That is impossible: one restriction to the old divisor is a nonzero analytic germ, and the analytic identity theorem makes it nonzero as a germ at every point of a sufficiently small connected divisor piece. Pulling to the strict transform preserves that property. If an old divisor equals the centre in \(N\), its strict transform is absent and makes no claim here.

Consequently the freshly computed residual value at a point \(a'\) over \(a\), whenever the preceding coefficient presentation persists, is
\[
 \nu(a')=\frac{\min_i\operatorname{ord}_{a'}g_i'}d
       \le\frac{k}{d}.
\tag{RX5}
\]
Equality holds exactly where the transformed residual family has its marked condition. One direction follows from its marks. For the other, the preceding marked condition says \(\operatorname{ord}M'+\min\operatorname{ord}g_i'\ge d\); if the second term is \(k\), it supplies the optional monomial mark \(d-k\). Thus at a persisting point the transported family is a valid fresh normalized residual presentation with its original marks. It need not be the literal choice of functions made by another presentation.

For \(k=0\), the residual unit pulls back to a unit, and \(M'=e^{-d}M\circ\sigma_N\) has new exponent \(q_C-d\ge0\). The residual value stays zero wherever the parent persists. Zero coefficient functions remain zero; the infinite case needs no finite factor calculation.

### Comparing residual presentations while their marks stay fixed

Two compatible coefficient choices for the same normalized parent family have the same ambient marked loci after every allowed test: each equals the corresponding transformed parent locus by the coefficient-persistence theorem, including its exclusion of irrelevant projective directions. The same conclusion holds for coefficient choices from two test-equivalent normalized parent presentations of the same codimension: compare each coefficient locus to its own parent locus, and then use parent equivalence. Their coefficient manifolds have the same codimension. The order-recovery result therefore gives equal normalized point orders and equal normalized orders along each labelled divisor, at the current point and at every common marked stage of a test sequence. It also identifies the all-zero case: the common ambient marked locus is the whole presenting manifold of that codimension, so both coefficient families are zero and give the same terminal value and germ.

Clear the two coefficient families to the same common mark \(d\). They now have the same integers \(q_H\) and the same \(k=d\nu\). We prove that their residual families (RX2) are test equivalent. During the test sequence retain a factor identity
\[
 h_{i,j}=M_jg_{i,j},\qquad
 M_j=u_j\prod_{H\in\mathcal E_j}x_H^{q_{H,j}},
 \qquad q_{H,j}\in\mathbb Z_{\ge0},
\tag{RX6}
\]
where \(u_j\) is a unit. The initial marks \(d,k,d-k\) remain fixed. At an intermediate exceptional test, \(M_j\) need not be the greatest common exceptional factor.

For an ordinary centre in the transported residual marked locus, use exactly (RX3) with these fixed marks. The monomial exponents update by (RX4), with their current values. A product pulls back the factors and gives its new divisor exponent zero. In a distinguished exceptional-test chart,
\[
 x_{H_0}=y_{H_0},\qquad x_{H_1}=y_{H_0}y_{H_1},
\tag{RX7}
\]
both factors undergo plain pullback. The new divisor exponent is \(q_{H_0,j}+q_{H_1,j}\); the strict transform of \(H_1\) keeps its exponent and that of \(H_0\) is absent in this chart. No other divisor contains this intersection in the normal-crossing coordinates. These operations prove (RX6) along every allowed test string.

At a point of the transformed coefficient manifold let
\[
 m_j=\min_i\operatorname{ord}h_{i,j},\qquad
 Q_j=\operatorname{ord}M_j=\sum_{H\ni x}q_{H,j},\qquad
 \rho_j=m_j-Q_j=\min_i\operatorname{ord}g_{i,j}.
\tag{RX8}
\]
There is no infinite-minus-infinite subtraction: a nonzero analytic germ stays nonzero under these modifications and products, so \(m_j\) and \(Q_j\) are finite in this branch. The transported residual condition is exactly
\[
 \begin{cases}
  \rho_j\ge k,\ Q_j\ge d-k,&0<k<d,\\
  \rho_j\ge k,&k\ge d,\\
  Q_j\ge d,&k=0.
 \end{cases}
\tag{RX9}
\]
For \(k=0\), the initially unit residual remains a unit. Each condition in (RX9) implies the marked parent condition \(m_j\ge d\).

We compare the two residual families by induction along a proposed residual test sequence. Their exponent ledgers agree initially. Outside the common coefficient marked locus, both residual loci are empty by (RX9). On that locus, append a fresh product and the order-recovery tests. The stagewise order-recovery theorem gives the same \(m_j/d\) for both coefficient presentations. Their common labelled divisor incidence and equal ledgers give the same \(Q_j\), and therefore the same conditions (RX9). An ordinary centre in this common locus is permissible for both coefficient presentations; its ledger update depends only on which common labelled divisors contain the centre. Products and exceptional strings also have the same updates. The induction proves equality after every allowed continuation.

This proves test-choice independence of the residual class with the full formal divisor set. It uses the marked-locus comparison of the parent and the proved recovery tests, rather than assuming that a residual class is canonical. It also explains why an exceptional test must not be followed by silently changing the residual marks to fresh ones: (RX9) concerns the transported marks.

### Removing an old block while adjoining its current equations

We use a coordinate fact for nested centres. Suppose a smooth \(N\) is transverse to a normal-crossing divisor family, and a smooth \(C\subset N\) has normal crossings with that family in the ambient manifold. Its restriction to \(N\) then has coordinates simultaneously adapted to \(C\) and the restricted divisors. To construct them, retain the restricted equations of divisors containing \(C\) among its normal coordinates; their differentials are independent. Complete them by equations of \(C\) inside \(N\). The remaining divisor coordinates restrict independently to \(C\), and can be completed to coordinates there; extend them together with the chosen normal equations. The analytic inverse-function theorem gives the required coordinates. Extending by normal coordinates for \(N\), while retaining the ambient divisor equations, gives an ambient adapted system. Thus the centre charts used below are genuine simultaneous charts, not a consequence inferred from point orders alone.

Let \(B\subset\mathcal E\) be a labelled block of incident divisors, and put \(\mathcal E_{\rm rem}=\mathcal E\setminus B\). For a residual family define
\[
 \mathcal F=\mathcal G\cup
       \{(\ell_H|_N,1):H\in B\},
       \qquad\text{formal divisor set }\mathcal E_{\rm rem}.
\tag{RX10}
\]
Its marked locus is \(S_{\mathcal G}\cap\bigcap_{H\in B}H\). We show that the class of (RX10) for the reduced formal set is independent of the compatible coefficient choice.

An ordinary centre in this locus lies in every divisor of \(B\). If it has normal crossings with the remaining divisor family, it has normal crossings with the full one. Indeed, on \(N\), the equations of \(B\) are independent coordinates for their smooth intersection. Restrict the remaining divisor coordinates to that intersection, straighten the centre there while retaining those coordinates, and extend by the equations of \(B\). These coordinates straighten the centre with the full divisor family. The same argument, extended by normal coordinates to \(N\), gives the ambient statement.

The controlled transform of \((\ell_H,1)\) is a strict-divisor equation; in a chart missing that strict divisor it is a unit, so there are no continuing marked points there. A product preserves this description. An exceptional test permitted by \(\mathcal E_{\rm rem}\) uses two remaining coordinate divisors, and its centre is not contained in any old \(H\in B\). Its plain pullback of \(\ell_H\) is therefore a strict-divisor equation without an additional exceptional factor. Repeating these arguments shows that every reduced-set test of (RX10) is a full-set comparison test for its residual part, with the old equations enforcing the required intersections.

The residual comparison just proved, followed by intersection with these same ambient old-divisor loci, now proves equality of the two classes (RX10). This is the operation required by the recursion. We have not used a claim that deleting arbitrary divisors from an **unadjoined** residual family preserves every test equivalence.

### Prefixes and the new history block

At stage \(j\) let \(f_j\) generate the principal strict-transform ideal. Set \(\nu_1=\operatorname{ord}f_j\), stop if it is zero, and otherwise use the first history prefix already proved. Write the later prefixes as
\[
 Q_1=\nu_1,\qquad P_r=(Q_r;s_r),\qquad
 Q_r=(P_{r-1};\nu_r)\quad(r\ge2).
\tag{RX11}
\]
Only a positive finite \(\nu_r\) receives a history count and a successor. A residual zero or infinity terminates the word. Comparisons are lexicographic, with \(0<\nu<\infty\) for positive finite \(\nu\). If a word has already terminated, use that terminal shorter prefix in comparisons; do not invent further numerical entries.

Suppose the prefix \(P_{r-1}\), with its compatible coefficient class, has been constructed. Take coefficients on one more smooth maximal-contact hypersurface, clear the marks to \(d\), and use (RX1) to define \(\nu_r\). The coefficient-choice comparison and recovery tests prove that this number and its residual class with the current formal divisor set are independent of the compatible coefficient choice. The parent marked locus and (AR13)–(AR14) identify the new upper stratum. Under an ordinary centre where \(Q_r\) is constant, either \(P_{r-1}\) drops above it, making \(Q_r\) smaller, or the coefficient presentation persists and (RX5) proves nonincrease of \(\nu_r\). Only after this step is justified do we define the birth of \(Q_r\).

For a point \(a\) with positive finite \(\nu_r\), let
\[
 b_r(a)=\min\{i:Q_r(a_i)=Q_r(a)\},\qquad
 \mathcal E_{r-1}(a)=E(a)\setminus\bigcup_{h<r}E^h(a).
\tag{RX12}
\]
The old block \(E^r(a)\) consists of those currently unassigned labels in \(\mathcal E_{r-1}(a)\) that were already present at \(a_{b_r(a)}\). Set
\[
 s_r(a)=|E^r(a)|,\qquad
 \mathcal E_r(a)=\mathcal E_{r-1}(a)\setminus E^r(a).
\tag{RX13}
\]
Earlier blocks persist by strict transform along a \(Q_r\)-constant ancestor suffix, because all their integer prefixes are then constant. The definition is consequently unambiguous, and the blocks are disjoint. At the birth stage every unassigned incident divisor is old for this new prefix, so \(\mathcal E_r(a_{b_r})=\varnothing\).

There is no need to postulate a separate history lemma for an arbitrarily varying unassigned family. Apply the proved history lemma to \(Q_r\) using **all** exceptional labels, and denote its old set by \(B_{Q_r}\). The definition is precisely
\[
 E^r(a)=\mathcal E_{r-1}(a)\cap B_{Q_r}(a).
\tag{RX14}
\]
On a principal relative Zariski neighborhood and the upper \(Q_r\)-stratum, the preceding integer prefixes are equal, so their already proved incidence identities give
\(\mathcal E_{r-1}(x)=E(x)\cap\mathcal E_{r-1}(a)\). The all-divisor history lemma gives the same formula for \(B_{Q_r}\). Intersecting them proves
\[
 E^r(x)=E(x)\cap E^r(a),\qquad
 s_r(x)\le s_r(a),\qquad
 \mathcal E_r(x)=E(x)\cap\mathcal E_r(a).
\tag{RX15}
\]
Equality of the count holds exactly where every old divisor at \(a\) remains incident. Thus adjoining their mark-one equations as in (RX10) gives the full upper-stratum presentation of \(P_r\). The reduced-set comparison above proves independence of its test class. Along an ordinary step, a drop of \(Q_r\) makes \(P_r\) drop; when \(Q_r\) persists, no new divisor is old and the old count can only decrease. The old strict-divisor equations detect equality of that count.

### Transport the unadjoined birth family when a count drops

The remaining existence issue is a compatible next coefficient hypersurface after the formal old block has been removed. A fresh transverse direction cannot simply be assumed for a family with an arbitrary existing exceptional boundary.

At \(b=b_r(a)\), the normalized family \(\mathcal G_b\) has a function of order equal to its mark and the reduced formal set is empty. A nonzero leading homogeneous polynomial has a vector on which it is nonzero. Taking that vector as a transverse coordinate gives the nonzero assigned-order derivative required by the coefficient theorem. This constructs a maximal-contact equation for \(\mathcal G_b\).

Transport \(\mathcal G_b\) **without old-divisor adjunction** along the \(Q_r\)-constant suffix from \(b\) to the current point. Its fixed residual marks remain valid. Each centre is in its marked locus: the lower prefix persists and the residual value is the same. Equations (RX3)–(RX5) make the transported family a fresh residual presentation at each persisting point. The coefficient-persistence theorem transports its chosen transverse equation and proves that it remains regular and transverse to the divisors created in this suffix. These are exactly the reduced formal divisors \(\mathcal E_r\), since that set was empty at birth. The original full boundary can still be retained as a comparison ledger, because the actual centres have normal crossings with the total exceptional divisor.

At the current point adjoin exactly the equations of the old divisors which are incident **now**:
\[
 \mathcal F_r(a)=\mathcal G_{b\to a}\cup
        \{(\ell_H|_{N_{r-1}},1):H\in E^r(a)\},
 \qquad\text{formal set }\mathcal E_r(a).
\tag{RX16}
\]
The same transverse witness still works after adjunction: its distinguished residual function has not been removed, and adding equations only reduces the marked locus. The full-boundary residual comparison and then (RX10) identify this class with the class formed from any compatible current coefficient choice. Thus a compatible coefficient representative exists and its next coefficient class is independent of that choice.

This order of operations is necessary when \(Q_r\) stays constant but \(s_r\) drops. If an old divisor present at birth no longer passes through the current point, its transported mark-one equation is a unit. Keeping it would make the marked locus empty and would incorrectly discard the new, smaller history stratum. It is omitted from (RX16), while the unadjoined residual functions and their transverse witness are retained. This handles a drop of the history count without pretending that the half-prefix was born again.

### The full upper stratum can have different birth times

We prove the fixed-chart semantic step; it is stronger than choosing ordinary neighborhoods separately at each point. Work with the fixed chart stacks and represented data supplied by the analytic-representative theorem. Finite products of denominator, Jacobian, derivative and divisor-incidence witnesses define principal relative Zariski neighborhoods. Quotient identities and zero identities hold on those neighborhoods. Every assertion about such a neighborhood below uses these witnesses; ordinary shrinking is used only when initially choosing the chart cover.

Assume first that the parent prefix has a common presentation on its entire upper stratum near \(a\). Choose its coefficient coordinates, transverse derivative and coefficient family. Include the nonzero transverse-derivative and Jacobian numerators in the witness product. The same coefficient theorem then applies at every point of that parent stratum in the resulting neighborhood. Its coefficient germs represent the already assigned parent class there. Include the exact-divisorial-order and residual-order derivative witnesses. The factor identities now give (AR13) at every such point with the actual residual number: its independence was proved above by the test comparison. The argument of (AR14) proves nonincrease of \(Q_r\) on the whole neighborhood and gives one common residual presentation on its entire upper stratum. Intersecting the history witnesses proves (RX15) there, hence the common marked-locus assertion for \(P_r\).

It remains to spread the **compatible** representative (RX16), since it was chosen using the reference point's birth. Fix \(b=b_r(a)\). Choose witnesses at the finitely many ancestors and pull them to the current fixed chart. On the upper \(Q_r(a)\)-stratum they give, for every \(b\le i\le j\),
\[
 Q_r(a)=Q_r(x)\le Q_r(x_i)
                  \le Q_r(a_i)=Q_r(a).
\tag{RX17}
\]
Thus the comparison point's value is constant over the *same* suffix beginning at \(b\), even if its earliest birth is earlier.

At stage \(b\), every unassigned divisor at \(a_b\) belongs to its new old block. Apply (RX15) at that stage, using its history witness as well. It follows that at every comparison point \(x_b\) in the upper stratum,
\[
 E^r(x_b)=\mathcal E_{r-1}(x_b),\qquad
 \mathcal E_r(x_b)=\varnothing.
\tag{RX18}
\]
This is the decisive conclusion: the comparison point may have an earlier birth, but it has no incident reduced formal divisor at stage \(b\). In the history lemma's earlier-birth case, all its current divisors are already old.

The common residual family at stage \(b\) is valid on that whole upper stratum. Include its selected order-exact transverse derivative in the witness product. It then supplies the same birth transverse equation at every \(x_b\); (RX18) removes any formal-divisor obstruction to that choice. Ordinary coefficient persistence and (RX3) transport this one family and its transverse equation over the common suffix (RX17). The represented transform identities and nonzero Jacobians are valid on a principal neighborhood of the current chart. Consequently they give the same compatible family at every current comparison point. Divisors from the birth block which are absent at \(a\) are excluded from this neighborhood by their nonzero current equations; the incident old ones obey (RX15). Current adjunction therefore gives exactly the family (RX16) on the whole upper \(P_r\)-stratum.

If \(b<j\), the needed semantic assertions at stage \(b\) were established by induction on the number of stages. If \(b=j\), the current common residual family and the history identity were just established before choosing the transverse direction. Thus (RX17)–(RX18) use no future prefix assertion. They close the different-birth case without assuming that an arbitrary ordinary neighborhood contains a relative Zariski neighborhood.

### Earlier entries that drop, and the finite recursion

The construction is a double induction: first on the number of actual blowing-up stages, then on prefix depth at a stage. At stage zero there is no exceptional history. At later stages, all prefixes on the preceding stages are already defined. At the current point start with the current principal equation and the order/history construction (AR11)–(AR12). At each subsequent depth:

1. take coefficients of the already constructed compatible current presentation;
2. define the residual value and prove its choice independence and nonincrease;
3. define its birth and unassigned old block;
4. use unadjoined birth transport and current adjunction to obtain the compatible next presentation;
5. spread its data over the whole upper stratum by (RX17)–(RX18).

The centres in the given tower are required to be locally constant loci of the prefixes already constructed on their stage and to have normal crossings with the total divisor. Equivalently, one constructs the word on a stage before checking the next given centre. No assertion selecting a global centre is hidden in this requirement.

If an earlier entry has dropped at a point, an ancestor's higher family is not reused to define its new tail. That former family is needed only to detect the first strict lexicographic decrease. The current tail is rebuilt from the current lower prefix and its current birth. The pointwise representative theorem supplies the new finite functions on the same previously selected chart, even when the marks, divisorial exponents, birth stages and coefficient manifold differ from those of the former branch. At each equal upper stratum the argument above then supplies common representatives of the assigned classes. This proves existence at reborn points, not merely continuation on one ancestor's persistent stratum.

Every nonterminal coefficient step lowers the dimension of its presenting manifold by one. In dimension zero an analytic germ is either a unit or zero. A marked point for positive marks cannot contain a unit among its equations, so its coefficient family is zero and the branch terminates at infinity. It can also terminate at residual zero or infinity earlier. Thus at each point the recursion has depth at most the ambient dimension. On the finite list of prefixes of the reference word, multiply the corresponding witnesses: at a comparison point the first differing prefix decreases, or every entry persists through the same terminal value. Rebuilt tails cannot reverse that first decrease. This proves nonincrease of the complete local word on fixed-chart neighborhoods and over ordinary permissible steps.

The same induction proves invariance under an analytic isomorphism of already matched labelled towers. Initial orders and ideals are invariant; coefficient/residual classes are independent of compatible choices; ancestor births correspond; and divisor equations differ only by units. It does not prove that independently selected towers match.

### The terminal coefficient manifold and the total divisor

The formal divisor set excludes old blocks. Some excluded divisors eventually contain the coefficient manifold, so they cannot be treated as additional transverse formal divisors. A convenient choice of the coefficient flag keeps track of this geometry explicitly.

Call an old divisor *pending* until its equation has been used as an equation of the coefficient flag, and *consumed* afterward. Maintain ambient coordinates in which the current coefficient manifold is a coordinate submanifold, consumed old divisors are coordinate hypersurfaces containing it, and pending old divisors together with formal remaining divisors restrict to distinct coordinate hypersurfaces on it. Maintain a mark-one pair for every pending divisor in the chosen equivalent presentation.

If there is a pending divisor \(H\), use its own mark-one equation as the next transverse coordinate. This consumes \(H\). Every other pending equation \(\ell_K\) can be retained as a different coordinate, independent of that transverse coordinate, so its coefficient family still includes \((\ell_K,1)\). After clearing coefficient marks to \(d\), it includes \((\ell_K^d,d)\). No formal remaining coordinate divides \(\ell_K^d\), and that function has order exactly \(d\). Thus, while any pending divisor remains after the coefficient step, the common exceptional monomial is a unit and the next residual value is exactly one. Its residual family keeps the same pending pairs, using the proved integer-power equivalence to write them again with mark one.

If there is no pending divisor, take the transverse witness supplied by the unadjoined birth transport. It is transverse to the current formal family, which now contains all divisors not already consumed. The next flag therefore has the required coordinate description. When an ordinary centre is encountered along a persistent prefix, it lies in the current flag and has normal crossings with the total divisor. The nested-centre coordinate fact above gives blowing-up charts inside the flag, extended by its normal coordinates. In these charts the strict flag stays smooth; consumed strict divisors still contain it; and the pending/formal strict divisors and the new divisor retain their coordinate description. Charts with no strict flag contain no persistent prefix points. A dropped old divisor is absent at the current point and is omitted as in (RX16). This verifies the flag induction along a persistent suffix as well as at a fresh birth.

At a terminal residual value, no pending old divisor can remain: the preceding paragraph would otherwise force that residual value to be one. Consequently all incident assigned old divisors are consumed and contain the terminal coefficient manifold; the remaining formal divisors are precisely its transverse coordinate divisors. In the infinite terminal case, all coefficients are zero and the equal-word locus is that smooth coefficient manifold. In the zero terminal case it is the marked locus of its coordinate monomial. The minimal coordinate components of that locus are therefore smooth and have normal crossings with the **total** exceptional divisor, including the consumed hypersurfaces which contain the coefficient manifold. The [minimal monomial-centre calculation](#the-strict-decrease-at-a-minimal-monomial-centre) supplies their explicit decrease under a permissible local blowing-up. This proves the local permissible-component assertion; it does not extend a selected component germ to a closed global centre.

The conclusion is the local recursive presentation theorem for a finite given admissible tower, together with the fixed-chart upper-stratum and history-incidence assertions, under the stated analytic-representative theorem. Numerical histories are defined only on the actual ordinary tower. Product and exceptional tests prove equivalence of marked classes; they have not been assigned a new numerical history by convention. These results are the local input for the analytic-threshold, canonical-centre and compact-fibre termination arguments below.

### The strict decrease at a minimal monomial centre

There is a concrete numerical decrease in the terminal monomial case. Let \(N\) have analytic coordinates \((x_1,\ldots,x_r,z)\), let \(q_i\) be nonnegative integers and \(d\) a positive integer, and consider the marked monomial
\[
 (M,d)=\left(\prod_{i=1}^r x_i^{q_i},d\right),\qquad d>0.
\tag{MC1}
\]
Zero exponents can be omitted. At a point \(b\), its order is
\(\sum_{i:x_i(b)=0}q_i\). Therefore its marked locus is the union of coordinate subspaces
\[
 C_J=\{x_i=0:i\in J\},
 \qquad \sum_{i\in J}q_i\ge d,
\tag{MC2}
\]
where it suffices to take inclusion-minimal qualifying sets \(J\). This is a finite union in the coordinate chart. Each individual \(C_J\) is smooth and has normal crossings with the coordinate divisor. The union need not itself be smooth, so it cannot automatically be used as one smooth centre.

Fix such a minimal \(J\) and blow up \(C_J\). In its \(x_\ell\)-chart, for \(\ell\in J\), set \(x_\ell=e\), \(x_i=e y_i\) for \(i\in J\setminus\{\ell\}\), and leave the other coordinates unchanged. The controlled transform is exactly
\[
 e^{-d}(M\circ\sigma)
 =e^{\sum_{i\in J}q_i-d}
    \prod_{i\in J\setminus\{\ell\}}y_i^{q_i}
    \prod_{i\notin J}x_i^{q_i}.
\tag{MC3}
\]
Its new exceptional exponent is nonnegative by (MC2). Minimality also gives
\(\sum_{i\in J\setminus\{\ell\}}q_i<d\), hence
\[
 0\le q_{\mathrm{new}}:=\sum_{i\in J}q_i-d<q_\ell.
\tag{MC4}
\]
Thus the chart replaces one exponent \(q_\ell\) by a strictly smaller nonnegative integer, leaving the other exponents unchanged. The charts for \(\ell\in J\) cover the entire projective normal fibre, including every direction.

More locally, define the weight at a point to be the sum of the exponents of the divisor components incident there. At any point over the chosen centre, the new divisor is incident; the \(\ell\)-th old strict divisor is absent, and some other old strict divisors may also be absent. Formula (MC4) proves that this weight drops by at least one from the ancestor point. Off the centre the map is an isomorphism and the incident weight is unchanged. For \(|J|=1\), the underlying blow-up is the Cartier identity, and the assigned exponent still decreases from \(q_\ell\) to \(q_\ell-d\).

Consequently, in a tower formed entirely from these monomial tests with a fixed mark \(d\), a chain of points can meet at most its initial incident weight many chosen minimal centres. In a sequence starting above one point, each step meeting a centre lowers a nonnegative integer, and the steps avoiding centres leave that integer unchanged. This is a termination statement along that chain. Choosing globally compatible centres for the full resolution invariant, and proving termination on a relatively compact region, still require the global construction; the pointwise decrease alone does not supply it.

### Why the residual presentation must retain its monomial condition

The additional pair in (AR14) can exclude points arbitrarily close to the
chosen point. The following polynomial example supplies actual common
coefficient data and lets us compute both the parent stratum and its
residual refinement everywhere on the coefficient manifold.

Use coordinates \((t,x,y,z,w)\) on \(U=\mathbb R^5\), and let the two
labelled exceptional hypersurfaces be \(H_x=\{x=0\}\) and
\(H_y=\{y=0\}\). They have normal crossings and are transverse to
\(N=\{t=0\}\). For an integer \(e\ge0\), put

\[
 M=x^2y^2,\qquad
 g_j^{(e)}=z^{e-j}w^j,\qquad
 h_j^{(e)}=M g_j^{(e)},\qquad
 F_j^{(e)}=t^4+h_j^{(e)}
 \quad(0\le j\le e).
\]

For \(e=0\), the residual family consists of the single function
\(g_0^{(0)}=1\). Give every \(F_j^{(e)}\) mark \(4\). Define the
parent value for this example by
\(P(p)=\min_j\operatorname{ord}_pF_j^{(e)}\). This is a concrete
minimum-order parent, without any assertion that these data are the
output of a full resolution algorithm.

**The coefficient reduction is exact.** The derivative
\(\partial_t^4F_j^{(e)}=24\) shows \(P\le4\) on \(U\). If
\(P(p)=4\), then \(\partial_t^3F_j^{(e)}(p)=24t(p)=0\), so
\(p\in N\). At a point \(p\in N\), the term \(t^4\) and the
Taylor series of \(h_j^{(e)}\), which is independent of \(t\), cannot
cancel one another. Consequently

\[
 P(p)=\min\left(4,\min_j\operatorname{ord}_p h_j^{(e)}\right)
 \qquad(p\in N).
\]

The coefficient family on \(N\) is exactly
\(\{(h_j^{(e)},4):0\le j\le e\}\); the coefficients of
\(t,t^2,t^3\) are zero and impose no conditions. Thus its marked
locus is the entire parent upper stratum \(S_P=\{P=4\}\).
At the origin \(a\), every \(F_j^{(e)}\) has order four, so this is
indeed the upper stratum through \(a\). All functions and derivatives
are polynomial on the one fixed chart, hence are fractions with
denominator one; no extension of a germ quotient is being assumed.

**The exceptional factor is exact.** Each \(h_j^{(e)}\) is divisible
by \(x^2y^2\). Its quotient is a nonzero polynomial in \(z,w\) alone,
so at every incident point it is divisible by neither the coordinate
\(x\) nor the coordinate \(y\). The common divisor orders along
\(H_x|_N\) and \(H_y|_N\) are therefore exactly two. Where one of
these divisors is absent, its coordinate factor is a unit. Both divisor
restrictions are genuine, distinct hypersurfaces of \(N\); neither
contains \(N\).

Write, on \(N\),

\[
 L=\{z=w=0\},\qquad D=\{x=y=0\},\qquad
 E=\{x=0\}\cup\{y=0\}.
\]

For \(p\in N\), define

\[
 m(p)=\operatorname{ord}_pM
      =2\mathbf1_{\{x(p)=0\}}+2\mathbf1_{\{y(p)=0\}},\qquad
 l_e(p)=\min_j\operatorname{ord}_p g_j^{(e)}.
\]

If \(e>0\), then \(l_e=e\) on \(L\), because all the residual
monomials are homogeneous of degree \(e\) in the vanishing coordinates
\(z,w\). Off \(L\), one of \(z^e,w^e\) is a unit, so \(l_e=0\).
For \(e=0\), one has \(l_0=0\) everywhere. Additivity of orders
now gives the exact parent condition

\[
 p\in S_P \quad\Longleftrightarrow\quad
 p\in N\text{ and }m(p)+l_e(p)\ge4.
\]

At the origin the residual order is \(k=e\), and
\(\partial_z^e g_0^{(e)}=e!\) is nonzero throughout \(N\), including
the degree-zero case \(g_0^{(0)}=1\). This verifies the derivative
bound in (AR14) on the whole fixed chart. On the parent stratum define
the residual value \(\nu=l_e/4\). We compare \(Q=(P,\nu)\) with
\(Q(a)\): a point outside \(S_P\) already has a smaller first entry,
so no residual continuation off the parent stratum is needed for this
comparison.

**The instructive case \(e=2\).** Here

\[
 (h_0,h_1,h_2)=x^2y^2(z^2,zw,w^2),\qquad
 d=4,\quad k=2,\quad \nu(a)=\tfrac12.
\]

Since \(m\) takes only the values \(0,2,4\), the parent upper
stratum and the residual upper stratum are respectively

\[
 S_P=D\cup(E\cap L),\qquad S_Q=E\cap L.
\]

Indeed, off \(L\) the residual order is zero, and the parent condition
requires \(m=4\), which means \(x=y=0\). On \(L\) the residual
order is two, and the parent condition requires \(m\ge2\), which
means \(x=0\) or \(y=0\). The points of \(D\setminus L\) remain
in the parent stratum but have residual value zero, so they leave the
upper stratum when the new entry \(\nu\) is added. In coordinates on
\(N\), \(E\cap L\) is the union of the \(x\)-axis and the
\(y\)-axis; \(D\) is the \((z,w)\)-plane.

Formula (AR14) gives the marked family

\[
 \boxed{\{(z^2,2),(zw,2),(w^2,2),(x^2y^2,2)\}.}
\]

The first three pairs alone have marked locus \(L\), the entire
\((x,y)\)-plane. The last pair imposes \(m\ge2\), leaving precisely
its two coordinate axes \(E\cap L\).
For any \(\varepsilon\ne0\), the point
\(b_\varepsilon=(x,y,z,w)=(\varepsilon,\varepsilon,0,0)\) lies
in the residual marked locus \(L\), but has
\(m=0\), \(l_2=2\), and \(P=2<4\). Thus it would be wrongly
included if the monomial pair were omitted. Taking \(\varepsilon\)
arbitrarily small shows that this is already an error of germs at the
origin, as well as an error on the full upper stratum.

Retaining the actual exceptional exponents matters too. At
\(c_\varepsilon=(\varepsilon,0,0,0)\), one has \(m=2\),
\(l_2=2\), \(P=4\), and \(\nu=1/2\), so this point belongs to
\(S_Q\). Replacing \((x^2y^2,2)\) by the squarefree pair
\((xy,2)\) would wrongly exclude it, because
\(\operatorname{ord}_{c_\varepsilon}(xy)=1\). The pair \((xy,1)\)
has the same marked locus as \((x^2y^2,2)\), since
\(\operatorname{ord}(x^2y^2)=2\operatorname{ord}(xy)\); this changes
the mark as well as the function. Replacing only the function does not
preserve the marked locus.

**Boundary comparisons.** The same family gives the following exact
comparison. The marked residual family in a row is
\(\{(z^{e-j}w^j,e):0\le j\le e\}\) when \(e>0\).

| Residual order at the origin | Parent upper stratum \(S_P\) | Refined upper stratum \(S_Q\) | Additional monomial condition |
|---|---|---|---|
| \(e=0\) | \(D\) | \(D\) | \((M,4)\) is the complete presentation |
| \(e=2<4\) | \(D\cup(E\cap L)\) | \(E\cap L\) | \((M,2)\) |
| \(e=4\) | \(D\cup L\) | \(L\) | None |
| \(e=5>4\) | \(D\cup L\) | \(L\) | None |

For \(e=0\), the residual function is the unit \(1\), so the parent
condition is \(m\ge4\), exactly \(D\); there is no mark-zero
residual pair. For \(e\ge4\), the residual marked locus is \(L\),
and on it \(m+l_e\ge e\ge4\) automatically. This is exactly why
no monomial pair is needed when \(k\ge d\). These statements concern
the displayed common coefficient data and their order strata; they do
not select centres, establish choice independence, or prove termination
of a resolution algorithm.

### Exercise: compare two positive residual marks below the parent mark

Keep the same functions with \(d=4\), and take first \(e=1\), then
\(e=3\). Compute the parent and refined upper strata at the origin.
Explain why the two positive residual orders lead to different upper
strata, even though the residual marked locus is \(L\) in both cases.

**Solution.** When \(e=1\), the residual marked family is
\(\{(z,1),(w,1)\}\), with locus \(L\), and the required monomial
pair is \((M,3)\). Since \(m\in\{0,2,4\}\), the inequality
\(m\ge3\) means \(m=4\), or \(x=y=0\). Thus
\(S_Q=D\cap L=\{0\}\) in \(N\). Off \(L\), the parent
condition still requires \(m=4\); on \(L\), it requires
\(m+1\ge4\), again \(m=4\). Hence \(S_P=D\) and
\(\nu(a)=1/4\).

When \(e=3\), the residual family is
\(\{(z^3,3),(z^2w,3),(zw^2,3),(w^3,3)\}\), again with locus
\(L\). The monomial pair is now \((M,1)\), so its condition is
\(m\ge1\), equivalently \(x=0\) or \(y=0\). Therefore
\(S_Q=E\cap L\). The parent condition off \(L\) still gives
\(D\), while on \(L\) it is \(m+3\ge4\), giving \(E\cap L\).
Thus \(S_P=D\cup(E\cap L)\) and \(\nu(a)=3/4\). The difference
comes from the exact threshold \(d-k\), which is three in the first
case and one in the second.

### Exercise: a zero residual value within the same coefficient family

Return to \(e=2\), but choose the parent point
\(a'=(x,y,z,w)=(0,0,1,0)\). Work on the principal relative Zariski
neighbourhood \(V=\{z\ne0\}\subset U\). Compute the residual
order at \(a'\) and give the full upper-stratum presentation on
\(N\cap V\). Explain why the residual mark two used at the origin
cannot be reused at \(a'\).

**Solution.** The function \(g_0=z^2\) is a unit everywhere on
\(N\cap V\), so \(l_2=0\) throughout this neighbourhood. Its value
is itself the nonzero degree-zero derivative required for the case
\(k=0\). The parent condition is now exactly \(m\ge4\), or
\(x=y=0\). Thus both upper strata through \(a'\) are
\(D\cap V\), with \(Q(a')=(4,0)\), and the complete presentation
is \(\{(M,4)\}\). The residual pair \((z^2,2)\) has empty marked
locus on this neighbourhood, because its function is a unit. Reusing
the origin's residual mark would therefore delete every point of the
actual upper stratum. The mark is the local residual order at the
selected base point; the exceptional factor and the coefficient
functions themselves have not changed.

## Prefix-controlled denominators and well-founded words

The recursive construction gives nonincrease of the complete word under an ordinary permissible transformation. Rational entries alone would not imply that a decreasing sequence stops. We first prove the precise discreteness that the construction supplies, and then prove finite termination near each base point. The second argument must control whole maximum loci, rather than a single chain of points above successive centres.

The human-source comparison is [Bierstone–Milman, *Canonical desingularization in characteristic zero*, complete author manuscript of 25 November 1996, proof of Theorem 1.14, pp.39–40](https://www.math.toronto.edu/bierston/inventionnes.ps). Those pages give the factorial denominator recursion and the two terminal decreases. The compact-fibre argument below supplies the finite maximum-locus bookkeeping explicitly. It uses the already proved analytic thresholds, recursive presentations and history transport, and the containing-label centre rule. The page references concern the 70-page author manuscript.

Write a positive-order complete word as
\[
 v=(\nu _1,s_1;\nu _2,s_2;\ldots;\nu_t,s_t;\nu_{t+1}),
 \qquad \nu_{t+1}\in\{0,\infty\},
 \tag{TN1}
\]
where the entries before the terminal one are positive and finite. The order-zero word is the stopping value. The recursive coefficient dimension drops at every nonterminal step, so \(t\le n\), with \(n\) the fixed ambient dimension. Each history count \(s_r\) is a nonnegative integer. At a fixed preceding prefix, the possible next numerical entries are ordered by \(0<\text{positive finite}<\infty\); there are no entries after a terminal entry.

**Denominator lemma.** For each finite numerical prefix define positive integers inductively by
\[
 e_1=\nu _1,\qquad D_r=e_r!,\qquad
 e_{r+1}=\max\{D_r,D_r\nu_{r+1}\}
       \quad(0<\nu_{r+1}<\infty).
 \tag{TN2}
\]
Then \(D_r\nu_{r+1}\) is an integer whenever the next entry is finite. This assertion applies at every stage, including a freshly recomputed tail after a prefix drop. In particular, its bound depends only on the preceding numerical prefix, and not on the number of previous blowings-up or the total number of exceptional labels.

**Proof.** Present the first order by the weak generator with mark \(\nu_1\), adjoining old divisor equations with mark one. All its marks are at most \(e_1\). Suppose a normalized presentation at the current depth has positive integer marks at most \(e_r\). Its coefficient equations have marks \(b-q\), where \(1\le b-q\le b\le e_r\). Thus every such mark divides \(D_r=e_r!\). Replacing an equation of mark \(c\) by its power \(D_r/c\) makes all marks equal to \(D_r\). These are integral powers, and (OR2) proves preservation of all the tests used by the construction.

Factor the exact common exceptional monomial out of this common-mark coefficient family. Its residual numerator \(k\), the least order of the residual functions, is a nonnegative integer, unless all functions vanish. Hence
\[
 \nu_{r+1}=k/D_r.
 \tag{TN3}
\]
If \(k=0\) or the family is zero, the construction is terminal. Otherwise the next normalized residual family has marks \(k\) and, when \(k<D_r\), the additional monomial mark \(D_r-k\). The old divisor equations have mark one. Every one of these marks is at most \(\max\{D_r,k\}=e_{r+1}\), proving the induction.

During a constant-prefix part of a tower, residual transport keeps exactly these fixed marks; the formula \(q_{\rm new}=q_C+k-D_r\) is the transport formula, not a change of mark. If an earlier prefix drops, the recursive construction recomputes the tail from the current data. Applying the same induction to that new numerical prefix proves the same bound there. History changes add equations of mark one and therefore do not alter this estimate. \(\square\)

**Well-foundedness lemma.** Every nonincreasing sequence of complete words (TN1) in fixed dimension eventually stabilizes.

**Proof.** Its first entries are nonnegative integers and are nonincreasing, so eventually they are constant. If that constant is zero, the words have stopped. Otherwise the first history counts are then nonincreasing nonnegative integers and eventually constant. Once a prefix is constant, the next finite numerical entries belong to the fixed lattice \(D_r^{-1}\mathbb Z_{\ge0}\), by the denominator lemma. A nonincreasing sequence in this lattice stabilizes: after its first finite term there are only finitely many lattice points between zero and that term. An initial infinite value can either remain infinite, terminating the word, or drop once to a finite value. A zero value also terminates the word.

When the next value stabilizes at a positive finite value, its following history count is again a nonincreasing integer and stabilizes. Continue through at most \(n\) coefficient depths. This proves stabilization of the whole word, including its length. A tail can restart with larger marks or different old blocks when an earlier prefix falls; the proof first discards the finitely many falls of that prefix before treating its tail. It therefore makes no assumption that a higher entry decreases independently of the earlier entries. \(\square\)

This is a descending-chain assertion. It does not give a uniform denominator for all words, or a finite set of values on an arbitrary noncompact stage. The analytic threshold argument uses this assertion separately to prove finite image on compact sets.

## Analytic thresholds and finite values on compact sets

The fixed-chart proof gives a principal neighborhood on which the invariant cannot increase. We now prove the stronger analytic conclusions needed to select a closed maximum locus: every upper threshold is a closed real analytic set, and the invariant takes only finitely many values on each compact subset of a finite stage. The argument does not require an open analytic chart to be a Noetherian topological space.

The same results are treated in [Bierstone–Milman, *Canonical desingularization in characteristic zero*, the 70-page author manuscript of 25 November 1996](https://www.math.toronto.edu/bierston/inventionnes.ps), Lemma 3.10 and Definition 3.11 on p.21, the analytic discussion on p.22, and Definition 6.4 on p.35. The complex-analytic ingredients used below have existing proofs in Analytic germs, local parametrization and the Nullstellensatz, Proposition 1.2 and Theorem 4.1: a complex analytic germ has finitely many irreducible components, and an irreducible germ has a small representative containing a connected dense complex manifold. We first derive the uniform-neighborhood consequences actually required here.

### From germ containment to one common neighborhood

Let \(\Omega\subset\mathbb C^n\) be open, let \(B\subset\Omega\) be a closed complex analytic set, and let \(p\in\Omega\).

**Uniform continuation lemma.** There is an open neighborhood \(W\subset\Omega\) of \(p\), depending only on \(B\) and \(p\), such that
\[
 (B,p)\subset(Z,p)\quad\Longrightarrow\quad B\cap W\subset Z
 \tag{AT1}
\]
for every closed complex analytic subset \(Z\subset\Omega\).

**Proof.** If \(p\notin B\), choose \(W\) disjoint from \(B\). Otherwise decompose \((B,p)\) into its finitely many irreducible germs. For each component choose a representative \(B_i\) on a small neighborhood of \(p\), with a connected dense complex manifold \(S_i\subset B_i\), as provided by the local parametrization theorem. Shrink a common neighborhood \(W\) so that \(B\cap W\) is the union of the restrictions of these representatives. The larger chosen domains of the \(B_i\) are kept inside \(\Omega\).

Suppose the germ containment in (AT1) holds. Then \(Z\cap S_i\) contains a nonempty open subset of \(S_i\): the germ containment holds on some neighborhood of \(p\), and density of \(S_i\) supplies points there. It is also a closed complex analytic subset of the connected manifold \(S_i\).

Such an analytic subset with nonempty interior is the whole manifold. Indeed, its interior is open; at a limit point of that interior take a connected coordinate neighborhood with finitely many local defining holomorphic functions. Each defining function vanishes on a nonempty open subset and hence identically by the identity theorem. Thus the interior is also closed, and connectedness proves the assertion. Therefore \(S_i\subset Z\). Since \(Z\) is closed and \(S_i\) is dense in \(B_i\), also \(B_i\subset Z\). This proves (AT1) on the chosen \(W\). The neighborhood was selected before \(Z\), so it works simultaneously for all such analytic sets. A zero-dimensional component is a point and satisfies the same argument. \(\square\)

This is the step that a bare assertion about Noetherian stalks does not supply. The individual germ containments may initially hold on different neighborhoods; continuation through the fixed finite branch representatives gives a single neighborhood for all of them.

**Finite-equation lemma.** Let \(\mathscr F\subset\mathcal O(\Omega)\) be any family of holomorphic functions, possibly infinite. Its common zero set is closed complex analytic. More precisely, for each \(p\in\Omega\) there are \(F_1,\ldots,F_q\in\mathscr F\) and an open \(W\ni p\) such that
\[
 W\cap\bigcap_{F\in\mathscr F}Z(F)
       =W\cap Z(F_1,\ldots,F_q).
 \tag{AT2}
\]

**Proof.** The ideal generated by the germs \(F_p\), \(F\in\mathscr F\), in the Noetherian ring \(\mathcal O_{\Omega,p}\) is generated by finitely many of them. To see that the generators may be taken from the family, express a finite set of ideal generators as finite combinations of the \(F_p\) and collect the finitely many functions occurring. Choose \(F_1,\ldots,F_q\) accordingly and put \(B=Z(F_1,\ldots,F_q)\) on \(\Omega\). Every \(F\in\mathscr F\) vanishes on the germ \((B,p)\). Apply (AT1) with \(Z=Z(F)\), using the same \(W\) for every \(F\). This proves the inclusion from right to left in (AT2); the reverse inclusion follows because the selected functions belong to \(\mathscr F\). The common zero set is closed as an intersection of closed sets, and (AT2) proves local analyticity. An empty family has common zero set \(\Omega\) and needs no equations. \(\square\)

### Decreasing analytic sets stabilize near compact subsets

**Compact stabilization lemma.** Suppose
\[
 A_1\supset A_2\supset A_3\supset\cdots
 \tag{AT3}
\]
are closed complex analytic subsets of one open complex manifold \(\Omega\). For each compact \(K\subset\Omega\), there are an integer \(N\) and an open neighborhood \(W\) of \(K\) such that \(A_m\cap W=A_N\cap W\) for every \(m\ge N\).

**Proof.** Fix \(p\in\Omega\). The ideals of analytic germs vanishing on \((A_m,p)\) form an increasing sequence in the Noetherian local holomorphic ring, so they stabilize at some \(N_p\). An analytic germ equals the common zero germ of its vanishing ideal: its own finite defining equations belong to that ideal. Hence \((A_m,p)=(A_{N_p},p)\) for all \(m\ge N_p\).

Use (AT1) for \(B=A_{N_p}\). There is one neighborhood \(W_p\) on which \(A_{N_p}\subset A_m\) for every \(m\ge N_p\). The reverse inclusion is already in (AT3), so the entire chain is constant on \(W_p\) after \(N_p\). Finitely many such neighborhoods cover \(K\). Taking the largest of their indices and the union of their neighborhoods proves the assertion. \(\square\)

The compact restriction is essential. In the unit disc, the sets
\(\{1-1/(j+2):j\ge m\}\), for \(m=1,2,\ldots\), are closed discrete analytic subsets and strictly decrease forever. Their points accumulate only at the boundary of the disc. The lemma states eventual constancy near each compact subset of the fixed domain, with an index that may depend on that subset and that chain.

### Holomorphic witnesses cut out the real upper thresholds

Let \(\lambda\) be the complete local resolution word on one finite stage of the given admissible tower. On a fixed chart stack, [the analytic-representative theorem](#analytic-representatives-on-one-fixed-chart) uses a conjugation-invariant complex polydisc \(\Omega\) and its real part \(U=\Omega\cap\mathbb R^n\). Combined with [the recursive semantic proof](#higher-analytic-prefixes-current-history-and-rebirth), it supplies, for every \(a\in U\), a holomorphic function \(D_a\in\mathcal O(\Omega)\), real on \(U\), such that
\[
 D_a(a)\ne0,\qquad
 x\in U,\ D_a(x)\ne0\quad\Longrightarrow\quad
                    \lambda(x)\le\lambda(a).
 \tag{AT4}
\]
The functions \(D_a\) are finite products of the represented denominator, Jacobian, derivative and history witnesses. They can depend on \(a\). What matters here is that they are all holomorphic on the same previously fixed \(\Omega\), rather than merely germs at their individual points.

For a value \(\gamma\) in the ordered value set, put
\[
 Z_\gamma
   =\bigcap_{\substack{a\in U\\\lambda(a)<\gamma}}Z(D_a)
       \subset\Omega,
 \qquad
 T_\gamma=\{x\in U:\lambda(x)\ge\gamma\}.
 \tag{AT5}
\]
Then
\[
 T_\gamma=U\cap Z_\gamma.
 \tag{AT6}
\]
Indeed, if \(\lambda(x)\ge\gamma\), a nonzero \(D_a(x)\) with \(\lambda(a)<\gamma\) would contradict (AT4), so every function in (AT5) vanishes at \(x\). Conversely, if \(\lambda(x)<\gamma\), the index \(a=x\) occurs in (AT5), and \(D_x(x)\ne0\) excludes \(x\) from that common zero set.

By (AT2), \(Z_\gamma\) is closed complex analytic. Near each real point, its equations in (AT2) are selected from the \(D_a\), so their restrictions are real analytic equations. Thus \(T_\gamma\) is a closed real analytic subset of \(U\). This proves closed analytic thresholds before using any finiteness property of the invariant's value set. It neither defines a resolution invariant at nonreal points nor assumes compatibility of an entire complex resolution algorithm: the complex sets are made directly from the existing real-point witnesses.

The equality (AT6) identifies the threshold intrinsically on each real chart. These sets therefore agree on real chart overlaps, proving that every upper threshold of \(\lambda\) is a closed real analytic subset of the whole current manifold. Here “real analytic subset” means a closed subset locally cut out by finitely many real analytic equations; no separate reduced-space structure is being asserted.

### Why only finitely many words occur on a compact set

We use the order-theoretic conclusion of [Prefix-controlled denominators and well-founded words](#prefix-controlled-denominators-and-well-founded-words): every nonincreasing sequence of possible principal-function words eventually stabilizes. Its proof uses the integer marks and the denominator bound determined by the preceding numerical prefix; it is not a property of arbitrary positive rational sequences.

Let \(K\subset U\) be compact. If \(\lambda(K)\) were infinite, it would contain a strictly increasing sequence
\(\gamma_1<\gamma_2<\cdots\). For completeness, a totally ordered set with no infinite strict decrease has a least element in every nonempty subset: otherwise successive smaller choices give such a decrease. Starting with the least element of an infinite subset and successively taking the least remaining element therefore constructs the asserted increasing sequence.

The sets \(Z_{\gamma_i}\) of (AT5) are decreasing closed complex analytic subsets of the same \(\Omega\). They strictly decrease on \(K\): choose \(x_i\in K\) with \(\lambda(x_i)=\gamma_i\); then
\[
 x_i\in K\cap Z_{\gamma_i},\qquad
 x_i\notin Z_{\gamma_{i+1}}.
 \tag{AT7}
\]
This contradicts the compact stabilization lemma. Hence \(\lambda(K)\) is finite.

Every point has a compact coordinate neighborhood whose interior contains it, so the values are locally finite. More generally, a compact subset of the current manifold is covered by finitely many open chart pieces with compact closures inside fixed chart stacks. Intersecting the given compact set with these closures produces finitely many compact subsets to which the argument applies. Their finite value sets have finite union. Thus the complete word takes finitely many values on every compact subset of any finite stage. In particular it takes finitely many values on any relatively compact open working domain whose closure lies in that stage.

On a nonempty working domain with finitely many values, a largest value \(\gamma_{\max}\) exists, and its maximum locus is exactly \(T_{\gamma_{\max}}\) restricted to that domain. It is therefore closed analytic in the working domain. Each value locus is locally a difference of two closed analytic threshold sets: in a finite local list, use its own threshold and that of the next larger occurring value. This does not make every value locus smooth; the terminal coefficient and boundary-refinement arguments are needed to obtain smooth centres.

### Finitely many terminal component branches near a compact set

There is a more concrete finiteness statement for a maximum locus. Suppose \(\gamma\) is the maximum word on an open working domain \(W\), and let \(S=\{x\in W:\lambda(x)=\gamma\}\). For every compact \(K\subset W\), there are finitely many ordinary coordinate neighborhoods \(V_1,\ldots,V_m\) covering \(S\cap K\) such that
\[
 S\cap V_i=B_{i1}\cup\cdots\cup B_{iq_i},
 \qquad q_i<\infty,
 \tag{AT8}
\]
where each \(B_{ij}\) is a connected smooth coordinate submanifold and the listed branches are the maximal coordinate subspaces in that union. They have normal crossings with the total exceptional divisor.

To prove this, use the adapted terminal flag from [the recursive construction](#the-terminal-coefficient-manifold-and-the-total-divisor) at each \(a\in S\). In the infinite terminal case the local equality locus is its smooth coefficient manifold. In the zero terminal case it is the marked locus of one coordinate monomial, hence the finite union of coordinate subspaces determined by inclusion-minimal exponent subsets of total weight at least its mark. The terminal flag includes the consumed old divisors, so this is a simultaneous coordinate description with the total divisor. Choose an ordinary coordinate box small enough that all these subspaces are connected and the description holds. Since \(S\) is closed and \(K\) is compact, \(S\cap K\) is compact; finitely many such boxes suffice.

The centre and compact-fibre arguments below use these finite coordinate descriptions. Compact stabilization here concerns thresholds on one fixed finite stage; it is not applied across different ambient spaces created by successive blowings-up.

## Choosing closed smooth centres and matching their restrictions

The terminal local geometry gives permissible component germs, but a union of crossing components is not a smooth centre. We now give an explicit choice that extends across charts and commutes with restriction. Its input is the complete local word and its terminal-component geometry proved above, together with the analytic closed-threshold theorem. Existence of a finite maximum procedure on relatively compact regions uses the separate termination argument. The component refinement is the one in [Bierstone–Milman, *Canonical desingularization in characteristic zero*, complete author manuscript of 25 November 1996, Remarks 1.15–1.16 and 6.17, pp. 11 and 40](https://www.math.toronto.edu/bierston/inventionnes.ps); the restriction principle is also used in §13, pp. 65–67. Here we prove the required real analytic centre and overlap assertions explicitly.

### Chronological labels and the precise inputs

Work at a finite stage of a principal analytic tower on a Hausdorff second-countable real analytic manifold \(X\). Its current weak ideal is locally principal, with a nonzero local generator on each connected coordinate neighbourhood. Let \(v(x)\) denote the complete order/history word. Its first entry is the nonnegative integer order of that ideal. The construction stops where this order is zero.

Give the exceptional hypersurface introduced by the \(i\)-th blowing-up the label \(i\). One labelled hypersurface may be disconnected: it is the whole exceptional hypersurface of that step. Retain its label under strict transform, allowing its current transform \(H_i\) to be empty. Different connected pieces born at that same step do not receive arbitrarily ordered extra labels. Each \(H_i\) is a closed smooth analytic hypersurface where nonempty, and the family has simple normal crossings. At a point there is at most one local branch of any one \(H_i\). These assertions follow from the adapted blow-up charts and hold for a Cartier step as well. At stage \(j\) the ordered label list is therefore
\[
 (H_1,\ldots,H_j).
 \tag{CC1}
\]
There are finitely many labels even when a hypersurface has infinitely many connected components. Empty labels can be kept as zero entries.

We use the following already separated properties of the invariant.

1. On the current stage, every upper threshold \(\{v\ge\lambda\}\) is a closed real analytic subset, and the values are locally finite. We perform centre selection on a working domain where a largest value \(v_*\) is attained and the weak ideal is not everywhere a unit. Its first entry is then positive. Finite image is sufficient for the existence of this maximum; an attained upper bound is sufficient as well.
2. Near a point of value \(v_*\), the set of points with that same value is the terminal locus of one common presentation. It is either a smooth coefficient manifold \(N\), in the infinite terminal case, or the union
   \[
   C_A=N\cap\bigcap_{i\in A}H_i,
   \qquad A\text{ inclusion-minimal with }
                 \sum_{i\in A}q_i\ge d,
   \tag{CC2}
   \]
   in the zero terminal case. Here \(d\) is a positive integer, the \(q_i\) are positive integers after omitting zero exponents, and the indicated \(H_i\) are the remaining transverse formal divisors. All consumed old divisors contain \(N\). There are simultaneous analytic coordinates for \(N\) and the total divisor. The terminal locus and every component in (CC2) are the actual equal-word germs, independent of the coefficient presentation.
3. On a matched labelled tower, the word, its birth history, and its terminal locus are invariant under analytic isomorphisms. The controlled weak transform, coefficient presentations and history construction commute with restricting the tower to an open subset.

The last restriction assertion includes a harmless reindexing after steps whose centres miss that subset; we verify it below. The first property is an analytic topology input, not a consequence of a finite number of coefficients at one point. We do not assume that an arbitrary noncompact stage has a global maximum.

### A component is identified by the divisors which contain it

Let \(S=\{x:v(x)=v_*\}=\{x:v(x)\ge v_*\}\) on such a working domain. It is closed analytic by the first property. For a local component germ \(Z\) of \(S\) at \(a\), define
\[
 I_a(Z)=\{i\in\{1,\ldots,j\}: Z\subset(H_i)_a\},
 \qquad
 \epsilon(I)=(\mathbf1_{1\in I},\ldots,\mathbf1_{j\in I}).
 \tag{CC3}
\]
Containment here concerns the entire component germ, not just whether \(a\in H_i\). Order these bit vectors lexicographically, with \(1>0\), so the oldest differing label has priority.

**Component lemma.** Distinct component germs at a point have distinct sets (CC3). In a sufficiently small simultaneous-coordinate neighbourhood, the label set of each component is constant along that component, and the component germs at any nearby point are exactly those of the displayed components which pass through that point.

**Proof.** In the infinite case there is just the smooth germ \(N\), so uniqueness is immediate. Its containing labels are exactly the consumed divisors; every other incident divisor restricts to a genuine coordinate hypersurface on \(N\), and therefore does not contain its germ. This description persists on a small coordinate neighbourhood.

In the zero case write \(B\) for the labels of the consumed divisors. In the adapted coordinates, (CC2) is a finite union of distinct coordinate submanifolds. Inclusion-minimality of \(A\) means that none of these submanifolds is contained in another. Its containing-label set is precisely
\[
 I(C_A)=B\cup A.
 \tag{CC4}
\]
An additional transverse coordinate hypersurface cannot contain \(C_A\): its coordinate remains a free variable there. The sets in (CC4) are distinct. Shrink the neighbourhood to exclude divisors absent at \(a\) and to retain the coordinate description. The same argument at every point of a displayed component proves constancy of its containing-label set. The local components through a nearby point are exactly the members of this finite coordinate union which pass through it. Two distinct members cannot become equal as germs at an intersection, since their different free-coordinate directions remain different. \(\square\)

Define the extra entry and the extended word by
\[
 J(a)=\max\{\epsilon(I_a(Z)): Z\text{ a component germ of }S\text{ at }a\},
 \qquad \widetilde v(a)=(v(a),J(a)).
 \tag{CC5}
\]
The same germwise definition can be made at every point using its own upper equal-word germ. For centre selection we need it only on the largest-word locus \(S\). The component lemma makes the definition intrinsic. It does not require choosing a global irreducible decomposition of a real analytic set.

### The maximum of the refinement is a closed permissible centre

Let \(J_*\) be the largest bit vector attained on \(S\). It exists because there are at most \(2^j\) possibilities, even if \(S\) is not compact. Define
\[
 C=\{a\in S:J(a)=J_*\}.
 \tag{CC6}
\]

**Centre theorem.** The set \(C\) is a nonempty closed embedded smooth real analytic submanifold of the working domain. At each of its points it is one entire local component of the terminal equal-word locus. It has normal crossings with the total exceptional divisor, the weak order is constant and positive on it, and blowing it up is an admissible principal transformation.

**Proof.** Fix \(a\in S\) and use the finite coordinate-component description of the component lemma. Write its components as \(Z_1,\ldots,Z_s\) with constant label vectors \(I_1,\ldots,I_s\). At every nearby point \(x\in S\),
\[
 J(x)=\max\{I_k:x\in Z_k\}.
 \tag{CC7}
\]
Every \(I_k\) occurs at \(a\), so it is at most \(J_*\). Formula (CC7) shows that, on this neighbourhood, \(C\) is exactly the union of the \(Z_k\) labelled \(J_*\). At most one such component exists, by the injectivity in the component lemma. Thus the germ of \(C\) at every \(a\in S\) is either empty or one whole smooth coordinate component. It is closed analytic locally along \(S\). Since \(S\) is closed in the working domain, points outside \(S\) have neighbourhoods missing \(C\). This proves global closedness and embedded smoothness; no closure of a locally chosen component across a different invariant stratum has been taken.

The simultaneous coordinates show normal crossings with every exceptional divisor, including the consumed divisors which contain the coefficient manifold. The first entry of \(v_*\) is one fixed positive integer \(m\), so the weak order is exactly \(m\) at all points of \(C\). In particular \(C\) lies in the zero locus of the weak ideal. It has positive codimension, because that nonzero principal ideal cannot vanish on an open subset of a connected coordinate neighbourhood. The centre-wide Taylor argument gives the analytic controlled weak transform. The standard analytic blowing-up charts preserve the total normal-crossing divisor, and the properness and Cartier lemmas apply. \(\square\)

The centre can be disconnected. Its entire union is smooth because the proof gives just one component germ at every point; arbitrary unions of crossing terminal components would not have this property. On the infinite terminal branch, the centre is the whole local coefficient manifold. On the zero branch, it is one of the minimal monomial components (CC2), so the strict decrease (MC4) applies in every persisting chart. In particular the centre theorem supplies exactly the full-terminal-component condition used in the protected-complement lemma.

More generally, on \(S\) every threshold \(\{J\ge L\}\) is locally the union of the displayed components whose label vector is at least \(L\), and is therefore closed analytic. The label entry serves to choose the component. Termination uses decrease of the primary word, or the terminal monomial weight while that word persists; it does not assume a well-founded decrease for bit vectors of increasing length.

For example, a local terminal monomial \((x_1x_2,1)\) has locus \(H_1\cup H_2\). The containing-label vectors of its two components are \((1,0)\) and \((0,1)\). If label 1 is older, (CC6) chooses \(H_1\), including their intersection, and not their crossing union. At the intersection the selected germ is still the whole smooth hypersurface \(H_1\).

### Deleting empty steps preserves the history and label order

Let \(U\) be an open subset of the original base of a finite tower, and restrict every stage to the inverse image of \(U\). If a centre misses that stage's inverse image of \(U\), its blowing-up restricts canonically to the identity there. The weak ideal and all old divisors are unchanged there, and the new exceptional hypersurface has empty restriction. Every later strict transform of that hypersurface also misses the inverse image of \(U\).

Remove just these empty-centre steps. Inserting or removing them repeats or deletes identical local data in the ancestor list. For each prefix its earliest occurrence may receive a different integer index, but the divisors already present at that occurrence are the same. Thus its old block, currently incident old block, and birth-transported presentation are unchanged. Induction on prefix depth proves that the full word and all assigned old blocks agree with those of the shortened tower. This uses the actual ancestor definition of birth; it does not reset history at each restricted stage.

The remaining chronological labels are identified by their order of creation. Passing from their bit vectors to those of the unshortened tower inserts zero entries at the labels of empty steps. This preserves lexicographic comparison: the first position where two vectors differ is carried to the first position where their zero-padded vectors differ. Hence
\[
 v\text{ and the ordering by }J
 \quad\text{are unchanged by empty-step deletion.}
 \tag{CC8}
\]
An open restriction can disconnect an exceptional hypersurface. All of those pieces retain the same creation label; they must not be assigned fresh arbitrary priorities.

Only empty-centre steps are deleted here. A nonempty Cartier centre can give an identity on underlying manifolds while dividing the weak ideal and introducing a recorded divisor. That data transformation is retained, on both sides of every comparison.

### A maximum procedure commutes with open restriction

Call the following a maximum procedure on a working domain: while the weak ideal is nonunit somewhere, select (CC6) using the current data, blow it up, perform the prescribed weak and divisor transforms, and recompute the invariant with the resulting history. Assume that its current largest value exists at each step. The compact termination argument separately supplies the finite instances used for resolution.

**Restriction theorem.** Restrict a maximum procedure on a domain \(V\) to an open subset \(U\subset V\) and delete its empty-centre steps. The remaining steps are exactly the maximum procedure on \(U\), for as long as the procedures in question are defined. The equality includes the transformed ideals, old blocks and ordered boundary data, through the canonical analytic identifications of the blowings-up.

**Proof.** At a current stage, write \(V\) and \(U\) for the corresponding current inverse images of the original domains. Suppose that their data have already been matched. Let \(C_V\) be the selected centre in \(V\). If \(C_V\cap U=\varnothing\), restriction makes this step empty and (CC8) applies. There is no local change to the data on \(U\).

If \(C_V\cap U\ne\varnothing\), the largest primary value on \(U\) is the same as on \(V\): restriction cannot create a larger value, and the intersection supplies a point attaining the larger domain's maximum. On that common maximum stratum, the largest component-label vector is also the same, by precisely the same argument. The local component germs and their containing labels are unchanged by open restriction. Therefore
\[
 C_U=C_V\cap U.
 \tag{CC9}
\]
This also proves existence of the required maximum on \(U\) at that step without a compactness assumption on \(U\). By the analytic blow-up restriction lemma,
\[
 \operatorname{Bl}_{C_V}(V)\big|_U
       \simeq\operatorname{Bl}_{C_U}(U)
 \tag{CC10}
\]
as real analytic manifolds over \(U\); the exceptional and strict-divisor ideals correspond under this isomorphism. The controlled weak ideal therefore corresponds as well. Invariance on a matched tower and (CC8) give the same next word and ordered history. This is the induction step. \(\square\)

For a finite procedure ending with unit weak ideal, the restricted procedure also ends with unit weak ideal. It cannot finish all of its retained steps with an unresolved open subset left over, because the final ideal is the restriction of that unit ideal. Thus it is the complete finite maximum procedure there. In particular, larger-domain steps of higher value that are disjoint from \(U\) cannot change when a lower local value will be processed or how its eventual centre is selected.

### Independently constructed towers on overlaps

Suppose finite maximum procedures ending with unit weak ideals have been constructed on two open analytic domains \(U\) and \(V\) for restrictions of the same principal data. Write their real analytic composite maps as \(\pi_U:Y_U\to U\) and \(\pi_V:Y_V\to V\). Restrict both to \(O=U\cap V\) and delete empty-centre steps. They start with identical data. Their first nonempty centres are both the centre (CC6) of those data, so they agree. The canonical isomorphism of their blowings-up identifies the next data. Repeating proves by induction that every subsequent nonempty centre and transformed datum agrees. If one tower ends first, its weak ideal is a unit on \(O\); hence no nonempty step remains in the other tower. With \(Y_U|_O=\pi_U^{-1}(O)\) and \(Y_V|_O=\pi_V^{-1}(O)\), the final towers therefore give an analytic isomorphism
\[
 \theta_{UV}:Y_U|_O\xrightarrow{\ \simeq\ }Y_V|_O
 \quad\text{over }O.
 \tag{CC11}
\]
This is an existence proof of the overlap map, obtained by matching centres of independently run procedures. It is stronger than the earlier statement that already matched centres have matching blow-ups.

The same argument applies to an analytic isomorphism between two open base domains carrying one principal ideal to the other. It identifies the initial orders and terminal germs, carries each selected centre to its counterpart, and lifts canonically at every step. Since the label rule uses only chronological order and no chart numbering, it is preserved by these lifts.

The comparison maps are compatible with further open restriction, satisfy \(\theta_{UU}=\mathrm{id}\), and obey
\[
 \theta_{VW}\circ\theta_{UV}=\theta_{UW}
 \tag{CC12}
\]
on each triple overlap. One can see this directly from the functorial coordinate identification of each common blowing-up. Alternatively, the final maps are isomorphisms over the dense complement of the original zero divisor; any two analytic comparison maps over the base agree there and hence everywhere by continuity and the Hausdorff property. The dense unchanged locus proves uniqueness after (CC11) has supplied existence.

These results provide closed smooth centres on each domain where the maximum procedure is used and give the full-overlap isomorphisms needed by the proper-gluing lemma. For an arbitrary noncompact analytic base, the separate compact termination argument must first produce finite maximum procedures on an appropriate relatively compact open cover. The centre theorem does not assert a global maximum on that base or a finite sequence of global blowings-up. Once those finite procedures exist, (CC11)–(CC12), the total-function ledger and the protected-complement lemma have exactly the hypotheses needed for the proper analytic resolution map.

## Finite termination over a compact fibre

Fix a base point \(a\) in a smooth real analytic manifold \(X\), and a nonzero locally principal analytic ideal. We prove that some open neighborhood of \(a\) admits a finite maximum procedure ending with unit weak ideal. The dimensions, controlled ideal transforms, divisor labels, and birth histories are those already constructed. Every centre is the maximum-word centre refined by the lexicographically maximal set of containing exceptional labels. In particular, it is closed, smooth, permissible, and one full terminal component at each of its points.

The proof works on the compact fibre of each finite composite. It does not assume that a stage over a relatively compact open base embeds with relatively compact closure into a larger smooth stage. Such an extension across the boundary of the base has not been established and is not needed.

### The two strict decreases at the end of a fixed word

Suppose a centre lies in the maximum locus of one complete positive-order word \(\lambda\).

In the infinite terminal case the equality locus is its whole coefficient manifold \(N\). Near any point of the selected centre, that centre is exactly \(N\). Under blowing-up of the whole \(N\), its strict transform is empty: it is the closure of the inverse image of \(N\setminus N=\varnothing\). The coefficient-persistence theorem puts every point with unchanged word in that strict transform. Thus
\[
 v(a')<\lambda\quad\hbox{for every point above the selected centre}
 \qquad(\text{terminal }\infty).
 \tag{TN4}
\]
This statement concerns all projective charts; the exclusion of directions outside the coefficient strict transform is part of coefficient persistence.

In the zero terminal case the coefficient family has common mark
\(d=D_t=e_t!\), determined by \(\lambda\), and its residual family contains a unit. Its terminal marked family is therefore
\[
 (M,d),\qquad M=\prod_H x_H^{q_H}.
 \tag{TN5}
\]
Only the current transverse formal divisors occur in this product; the old divisors consumed by the coefficient flag already contain \(N\). Define
\[
 W(b)=d\,\mu_{t+1}(b)=\operatorname{ord}_b M
       =\sum_{H\ni b}q_H
       \quad\hbox{on }\{v=\lambda\}.
 \tag{TN6}
\]
The point-order recovery theorem makes \(\mu_{t+1}\) independent of the coefficient presentation of this fixed prefix. Thus (TN6) is an intrinsic nonnegative integer on the fixed-word locus. It is finite. On one terminal coordinate neighborhood the exponents are fixed and \(W\le\sum_Hq_H\), so \(W\) is bounded on compact subsets of that locus.

The selected centre inside \(N\) is a minimal coordinate component
\(C_J=\{x_H=0:H\in J\}\), where \(\sum_{H\in J}q_H\ge d\) and no proper subset has this property. In the chart indexed by \(\ell\in J\), the new divisor exponent is
\[
 q_{\rm new}=\sum_{H\in J}q_H-d,
 \qquad 0\le q_{\rm new}<q_\ell.
 \tag{TN7}
\]
The old \(\ell\)-divisor is absent from that chart. All other incident old exponents are unchanged, and some old divisors may miss the point under consideration. Consequently, at every point above the centre where the whole word persists,
\[
 W(b')\le W(b)-1.
 \tag{TN8}
\]
Outside the centre the transformation is an isomorphism with unchanged presentation, so \(W(b')=W(b)\). The fixed-prefix transport theorem justifies using the same \(d\) on the two sides. In particular, (TN8) includes the full residual and history construction, rather than applying a monomial estimate to a newly and arbitrarily marked presentation. A nonempty Cartier step still changes the controlled ideal and the labelled history and still satisfies (TN7); it is retained in the procedure.

### Constructing successive steps on actual base neighborhoods

Suppose a finite initial part has been constructed over an open neighborhood \(U_j\ni a\), with proper composite
\[
 \pi_j:X_j\longrightarrow U_j,
 \qquad K_j=\pi_j^{-1}(a).
 \tag{TN9}
\]
The fibre \(K_j\) is compact and nonempty. Properness follows by finite composition of the analytic blowings-up. Initially \(\pi_0\) is the identity. Let \(\lambda_j\) be the largest word on \(K_j\); it exists by finite image on compact sets.

There is an open neighborhood \(O_j\) of \(K_j\) in \(X_j\) on which \(v\le\lambda_j\). To see this directly, at each fibre point use a small neighborhood on which only finitely many values occur. The union of its finitely many thresholds higher than \(\lambda_j\) is closed there and misses that point, so a smaller neighborhood excludes those values. The union of these smaller neighborhoods gives \(O_j\).

If \(\lambda_j=0\), the weak ideal is a unit throughout \(O_j\). Otherwise put \(S_j=\{v=\lambda_j\}\) on \(O_j\), and let \(I_j^*\) be the largest component-label vector occurring at a point of \(S_j\cap K_j\). Such vectors form a finite set. The refined threshold \(\{b\in S_j:J(b)>I_j^*\}\) is closed in \(O_j\) and misses \(K_j\). Remove it. After this removal the maximum word and the maximum component vector on \(O_j\) are both attained on the fibre. The canonical centre therefore meets \(K_j\).

One can also make the terminal coordinate descriptions and the weight bound explicit on this neighborhood. The closed set \(S_j\cap K_j\) is compact. Cover it by finitely many simultaneous terminal-coordinate neighborhoods. At the remaining points of \(K_j\), the closed threshold \(\{v\ge\lambda_j\}\) can be excluded. Shrink \(O_j\) inside the union of these neighborhoods. Then every point of \(S_j\cap O_j\) lies in one of the chosen terminal charts; in the zero case their finitely many sums of exponents bound \(W\).

To make this an actual working domain over the base, use properness. The closed set \(X_j\setminus O_j\) has closed image under \(\pi_j\), and that image does not contain \(a\). Thus
\[
 U_{j+1}=U_j\setminus\pi_j(X_j\setminus O_j)
 \quad\hbox{is open, contains }a,
 \qquad \pi_j^{-1}(U_{j+1})\subset O_j.
 \tag{TN10}
\]
Restrict the finite tower to \(U_{j+1}\). If the maximum was zero, it is now a finite terminal procedure. Otherwise select its canonical closed centre and blow it up. This constructs the next finite stage, properly over \(U_{j+1}\), and repeats the construction.

All restrictions in this construction are full inverse images of open base neighborhoods. They preserve the entire fibre. No step assumes that a centre extends smoothly across \(\partial U_j\). At each finite stage the procedure and every preceding centre are defined on an actual neighborhood of \(a\); an infinite intersection of shrinking neighborhoods will never be used.

The numbers \(\lambda_j\) do not increase. Indeed, every point of the next fibre maps to a point of the current fibre, and the full recursive invariant does not increase under the chosen permissible transformation. If this construction were infinite, the well-foundedness lemma would give an index after which
\[
 \lambda_j=\lambda
 \tag{TN11}
\]
is one fixed positive-order word. It remains to rule out such an infinite plateau of maximum words.

### Component types survive restriction without splitting into new types

At stage \(j\), retain all chronological labels \(H_1,\ldots,H_j\), including empty transforms. For each local component germ \(Z\) of the maximum locus, its **type** is
\[
 I(Z)=\{i:Z\subset H_i\}\subset\{1,\ldots,j\}.
 \tag{TN12}
\]
There are at most \(2^j\) types. Distinct component germs at one point have distinct types, and a type is constant along each component in a sufficiently small terminal coordinate neighborhood. The centre rule selects all components of its largest type at once: if \(I^*\) is that type, the centre is locally precisely the component of type \(I^*\), wherever such a component is present. This follows from (CC7), including at intersections with lower-priority components.

For the plateau argument retain only types having a component germ at a point of the compact fibre. Shrinking a base neighborhood does not alter these germs. It can disconnect a representative, but both pieces have the same type and are counted together. Thus this finite bookkeeping uses neither global irreducible components nor a claim that open real analytic charts are Noetherian.

**Transformation lemma for types.** Suppose both stages have largest fibre word \(\lambda\), and restrict to the maximum-bounded working domains just constructed. Let \(I^*\) be the type selected for the centre. Every type meeting the new fibre is of one of the following forms:

1. A surviving old type \(I\ne I^*\), with a zero appended for the new exceptional label. Its local components are strict transforms of unselected old components.
2. A new type whose new exceptional bit is one. Its components lie above the selected centre.

There is no surviving old type \(I^*\). Distinct surviving old types remain distinct, and no type in the first list equals one in the second.

**Proof.** Off the new exceptional divisor the blow-up is an isomorphism, including the controlled ideal and the history after insertion of the empty new label. Hence the new maximum locus there is exactly the old maximum locus off the centre.

The terminal coordinate description gives a direct local description of its strict transforms. In the zero case choose coordinates \((z,x,u)\) with \(N=\{z=0\}\), the selected component
\(C_A=\{z=0,x_i=0\ (i\in A)\}\), and another component
\(C_B=\{z=0,x_i=0\ (i\in B)\}\). The distinct inclusion-minimal subsets \(A,B\) are incomparable, so \(A\setminus B\ne\varnothing\). The ambient centre ideal is generated by the \(z_h\) and \(x_i\), \(i\in A\). On \(C_B\setminus C_A\), its projective normal vector has zero entries at every \(z_h\) and every \(i\in A\cap B\); at least one entry in \(A\setminus B\) is nonzero. These equalities remain true on taking the closure. Thus the strict transform of \(C_B\) is covered exactly by charts indexed by \(\ell\in A\setminus B\), with maps
\[
 x_\ell=e,\qquad x_i=e y_i\ (i\in A\setminus\{\ell\}),
 \qquad z_h=e v_h,
 \tag{TN12a}
\]
and the other coordinates unchanged. In such a chart its equations are precisely
\[
 v_h=0\ \text{for every }h,\qquad
 y_i=0\ (i\in A\cap B),\qquad
 x_i=0\ (i\in B\setminus A).
 \tag{TN12b}
\]
They hold on the nonexceptional inverse image; conversely their coordinate zero set has free coordinate \(e\), and its points with \(e\ne0\) are dense and belong to that inverse image. This proves equality with the actual real strict transform. Restricting (TN12a) to (TN12b) gives exactly the projective charts of
\(\operatorname{Bl}_{C_A\cap C_B}(C_B)\), since the centre in \(C_B\) is defined by its free coordinates indexed by \(A\setminus B\). The overlap maps are the ratios of those same coordinates. This strict transform is smooth and, as a germ at every point, is not contained in the new exceptional divisor \(e=0\). If \(|A\setminus B|=1\), its intrinsic blow-up is a Cartier identity, and the same coordinate proof applies. Charts indexed by \(z_h\) or by \(A\cap B\) contain no points of this strict transform.

The entire strict transform lies in the new \(\lambda\)-locus. Its complement of the exceptional divisor has word \(\lambda\); the threshold \(\{v\ge\lambda\}\) is closed and the new word is at most \(\lambda\), so the closure has that word too. It remains a full component. Indeed, its smooth germ is contained in one member of the finite new coordinate-component union: otherwise finitely many proper analytic subset germs would cover a smooth germ, and the product of one nonzero defining germ for each subset would be zero in its power-series domain. A new component containing it has the same dimension, as seen at nonexceptional nearby points where the old \(C_B\) was a full component. Inclusion of equal-dimensional smooth germs is equality. Distinct old strict components cannot merge, since equality of their germs would hold also at nearby nonexceptional points, contradicting the original distinct full coordinate germs.

Conversely, let a new full component have germ not contained in the exceptional divisor. On a connected small coordinate representative it has a nonempty open part off that divisor. There it is covered by the finite union of old unselected strict transforms. One of those analytic subsets contains an open part of the component, by the same finite-union argument. The analytic identity theorem then gives containment of its whole germ in that strict transform. The full-component assertion already proved makes these germs equal. In the infinite case there is only one local component at each point; the selected one has no persisting-word point over it by (TN4), and all other local components are unaffected near their generic points.

The old containing labels of an unselected strict component do not change. Off the exceptional divisor, containment in an old divisor is exactly the old containment. If an old containing divisor is present, taking closures preserves containment in its strict transform. If a label did not contain the old component, it cannot contain the strict component: off the exceptional divisor their common open component would then be contained in that old divisor, contradicting the terminal coordinate model. The new exceptional divisor does not contain this strict component. Its type is therefore precisely the old type with a zero appended.

Every remaining new component is contained in the new exceptional divisor, whose image is the centre, and so has new bit one. The whole selected old component has empty strict transform; every occurrence of its type was selected, so that old type cannot survive. Finally, a component meeting the new fibre maps to a point of the old fibre. Whenever it is an old strict component, its old component germ therefore occurred at that old fibre point and was already among the tracked types. \(\square\)

### The finite genealogy on a constant-word plateau

If \(\lambda\) has terminal value \(\infty\), (TN4) excludes every new component in the second list of the transformation lemma. Each step removes the selected type, and all remaining types merely acquire a zero bit. The finite set of types at the start of the plateau therefore allows only finitely many steps. The varying length of the label vector plays no role in this count.

Suppose instead that \(\lambda\) has terminal value zero. For every type \(I\) meeting the current fibre define its integer bound
\[
 B_j(I)=\max\{W(b):b\in K_j\cap\{v=\lambda\},
           \text{ a component germ of type }I\text{ passes through }b\}.
 \tag{TN13}
\]
The set is nonempty by the meaning of a tracked type. Its integer values are bounded by the finite terminal-chart cover of the fibre. A nonempty bounded subset of the nonnegative integers has a maximum, so (TN13) does not require the type set itself to be compact.

A surviving old type has bound at most its former bound. Indeed, its points map to fibre points on the corresponding old component, and \(W\) is unchanged off the centre and decreases above the centre. A new type has bound at most
\[
 B_j(I^*)-1,
 \tag{TN14}
\]
because every one of its fibre points maps to a point of the selected type \(I^*\), and (TN8) applies there.

Make a rooted forest as follows. At the first stage of the plateau create one root for each tracked type, with rank its bound (TN13). While a type survives with appended zero bits, retain the same vertex; its current bound can only fall. When its type is selected, remove that vertex from the current list and attach one child for each new type meeting the next fibre. Give the child its bound at birth as rank. Types that disappear without being selected are simply removed. The transformation lemma ensures that every tracked type belongs to exactly one current vertex: old types do not merge with each other or with new types. Formula (TN14) makes every child rank strictly smaller than its parent's birth rank.

There are finitely many roots. Each vertex has finitely many children, since only finitely many labels exist at its selection stage. All ranks are nonnegative integers and strictly decrease along an edge. Such a forest is finite. For an explicit proof, use induction on the rank of a root: a rank-zero vertex has no children; a rank-\(r\) vertex has finitely many children, each of rank less than \(r\), and the induction hypothesis makes each child subtree finite. A finite union of these finite trees is finite. No bound uniform in the number of stages is assumed for the number of children.

Every plateau step selects a type meeting the fibre and therefore removes a distinct current vertex. It follows that there are only finitely many plateau steps, contradicting (TN11). This proves termination of the construction.

The distinction between a type and a connected component is useful here. A type may represent several disjoint pieces, all selected together. Restriction may split such pieces, but cannot create a second copy of its label set. A genuinely new type is recognized by the new exceptional bit and pays for its birth by the strict integer decrease (TN14).

### An exact component-type transition

For the marked monomial \((x^2y^2z^2,3)\) on \(\mathbb R^3\), order the three original divisor labels as \(x=0,y=0,z=0\). The minimal component types are \(110,101,011\), so the rule selects \(110\), the centre \(x=y=0\). In the two projective charts the controlled monomials are \(uv^2z^2\) and \(tw^2z^2\), still marked by \(3\). The new exceptional exponent is \(2+2-3=1\). Listing their minimal components gives exactly the two surviving types \(1010,0110\) and the three new types \(1001,0101,0011\).

<figure style="margin:1em 0"><img src="figures/SH03-terminal-type-genealogy.svg" width="720" style="max-width:100%;height:auto" alt="Both blow-up charts and the component-type genealogy for the marked monomial x squared y squared z squared with mark three."></figure>

Over the original origin the old weight is \(6\). The new fibre is the exceptional projective line with \(z=0\); each of the five displayed types meets a chart endpoint with incident weight \(1+2+2=5\). Thus its bound on that fibre is \(5\). The diagram illustrates the type transformation and rank estimate (TN12a)–(TN14) in one terminal-monomial step; it does not identify this marked example with the full recursive invariant of the unmarked function. The general mechanism is compared with [Bierstone–Milman's 25 November 1996 author manuscript, pp.39–40](https://www.math.toronto.edu/bierston/inventionnes.ps); the displayed example and figure are independently calculated here. Reproducible Python source enumerates the minimal subsets and checks the exact chart types.

### The resulting local resolution and the compact-local conclusion

We have proved that the construction stops after finitely many steps. At that stage the maximum on the compact fibre is zero. Apply (TN10) once more to the open unit locus. There are only finitely many previously chosen base neighborhoods, so the final one is an actual open neighborhood \(U\ni a\). Restrict every stage to \(U\). This gives a finite composite
\[
 \pi_U:Y_U\longrightarrow U
 \tag{TN15}
\]
of proper analytic blowings-up with closed smooth permissible centres, ending with a unit weak ideal. Each restricted nonempty centre is still the canonical maximum centre: its word and label vector were upper bounds on the larger domain and were attained on the fibre, which all restrictions preserve. More generally, the restriction theorem (CC8)–(CC10) gives this conclusion and the correct history after deletion of genuinely empty-centre steps. Nonempty Cartier steps are never deleted.

The whole-function ledger now writes every pulled-back local generator as a unit times an integral monomial in a simple-normal-crossing divisor. Its support is precisely the zero set of the pulled-back function. The composite is surjective and proper, and the protected-complement lemma makes it an analytic isomorphism above the complement of the original critical-zero set \(\{\varphi=0,d\varphi=0\}\). This set is intrinsic to a locally principal ideal: replacing a generator by a unit multiple multiplies its differential at a zero by that same unit. These properties follow from the established ledger and blow-up lemmas, not from merely resolving the reduced zero set.

Every compact subset of the base is covered by finitely many neighborhoods \(U\) constructed this way. Each carries an actual finite canonical terminal tower. Their restrictions match by (CC11)–(CC12). This is the compact-local finiteness input for the subsequent proper analytic assembly. It does not assert a finite global blow-up sequence on an arbitrary noncompact base. The assembly uses these finite local maps and their canonical comparisons; it needs no additional termination claim across an infinite global tower.

The proof has covered finite and infinite terminal values, prefix drops and rebirth, residual normalization, old-divisor history, identity maps coming from Cartier centres, and the boundary of shrinking working domains. The finite-chart bounds are taken only near compact fibres of already constructed proper maps. No finite-type replacement of the analytic problem, global Noetherian topology of an open chart, or unproved extension across a working-domain boundary enters the argument.

## From finite local towers to the global function resolution

We explain the passage from the finite local algorithm to the full real analytic statement. The relevant inputs are the preceding canonical-centre and termination results: around every base point there is a finite terminal tower, its centres are the full selected components of the maximum stratum, and the same centre rule is used after restriction to an open subset. Empty restricted steps are omitted. The argument must compare independently run finite towers before applying the earlier gluing lemma.

The corresponding analytic passage is treated in [Bierstone–Milman, *Canonical desingularization in characteristic zero*, author manuscript of 25 November 1996, Theorems 13.2–13.3, pp.66–67](https://www.math.toronto.edu/bierston/inventionnes.ps). The construction below retains the ambient manifold and the full principal ideal throughout.

The [independent-tower comparison](#independently-constructed-towers-on-overlaps) has already constructed analytic comparison maps on full overlaps by matching every nonempty restricted centre. It also proves their compatibility with restriction and the cocycle identity. We use those maps here.

### A finite tower over a neighborhood of a compact set

Suppose finitely many open sets \(U_1,\ldots,U_m\) carry finite terminal runs. Their union \(U\) also carries a finite run. This is useful when a compact set is covered by finitely many of the local neighborhoods obtained in the termination theorem.

Before comparing component refinements, embed each patch's incidence vector into the current global chronological label positions, padding labels absent from that patch with zero. This common label list is retained throughout the merge. At the start, each nonterminal local run has a greatest extended invariant value: that is the value of its prescribed first centre. Take the largest of these finitely many values. On a patch with smaller local maximum, the global centre is empty. On a patch with that largest value, use its prescribed first centre. These descriptions agree on overlaps by the common invariant and centre rule. Hence they give a smooth closed analytic centre in \(U\), with normal crossings with the total divisor. Its blow-up restricts to the prescribed first step on the patches it meets, and to an isomorphism on the other patches.

Maintain the chronological order of global exceptional labels. A label born on a step disjoint from a patch is absent there, so inserting its zero incidence coordinate does not change that patch's next selected component. The preceding overlap comparison therefore continues to identify each patch with the unconsumed suffix of its given local run.

Each global step consumes at least one local step, and never adds a step to a local run. If the local runs have lengths \(n_1,\ldots,n_m\), the merged run has at most

\[
                         n_1+\cdots+n_m
\tag{LG1}
\]

nonempty steps. At its endpoint all local weak ideals are units, so the global weak ideal is a unit. This proves a finite tower over the union without imposing a bound on the invariant throughout a noncompact manifold. Any compact set has such a neighborhood, by a finite subcover of the local termination neighborhoods.

### The proper map and the protected complement

Take a countable locally finite cover of \(X\) by relatively compact open sets, each contained in a neighborhood with a finite terminal run. Such a refinement is supplied by the nested-ball construction later in this lesson. Restrict the runs to those sets. Every resulting terminal map is proper and surjective, by the projective-incidence and finite-composition proof for the supplied tower. The overlap argument above supplies its full analytic comparison maps.

Put \(Z=\{\varphi=0,d\varphi=0\}\). At an order-one point with no old divisor the full-component centre rule is exactly the smooth weak-zero hypersurface, as calculated in the protected-complement lemma. Thus condition (R) holds. That lemma shows that every local terminal map is an isomorphism over the complement of \(Z\).

This unchanged locus has dense inverse image. The original zero set has empty interior, because \(\varphi\) is not identically zero on any connected component. In every blow-up chart the pulled-back function is a nonzero analytic function: the total-transform formula gives a nonzero weak generator times a unit and integral coordinate powers. Its nonzero locus is dense by the analytic identity theorem, and is contained in the inverse image of \(X\setminus Z\).

All hypotheses of [the proper gluing lemma](#gluing-canonical-local-resolutions-into-a-proper-global-map) now hold. The resulting manifold \(Y\) is Hausdorff and second countable, and the glued analytic map \(f:Y\to X\) is proper, surjective and an analytic isomorphism over \(X\setminus Z\). The finite-cover argument in that lemma proves properness on every compact subset of \(X\); it does not require one finite tower on all of \(X\).

The terminal weak ideal is a unit on each local model. Hence the total-transform formula gives

\[
                 \varphi\circ f=u\prod_i y_i^{r_i},
                 \qquad r_i\in\mathbb Z_{\ge0},
\tag{LG2}
\]

with \(u\) a nonvanishing analytic unit. At a point of \(f^{-1}Z\), at least one exponent is positive. The unit-normalization lemma absorbs the positive magnitude of \(u\) into that coordinate, preserving all crossing hyperplanes. Its sign is constant after shrinking. Thus

\[
                    \varphi\circ f=\pm\prod_i y_i^{r_i}
\tag{LG3}
\]

in analytic coordinates near that point. This is the function-resolution statement in item 5, with the entire function and its multiplicities retained. Dimension zero uses the identity map: the hypothesis on connected components makes \(\varphi\) a unit there.

### Exercise: why the number of global steps need not be finite

Let \(X\) be the disjoint union of countably many copies \(X_n=\mathbb R^2\), \(n\ge1\), and define \(\varphi|_{X_n}(x,y)=y^2-x^{2n+1}\). Show that \(X\) is a second-countable real analytic manifold and that each compact subset meets only finitely many of its components. Explain why no single finite sequence of blow-ups with closed smooth centres of positive codimension can make these functions normal crossing everywhere, although finite resolution in neighborhoods of each compact set is compatible with a global proper map.

**Solution.** Countably many countable Euclidean bases give a countable basis for the disjoint union. Its component charts supply its real analytic structure. The open components cover any compact subset; a finite subcover shows that only finitely many components are met.

At the origin of \(X_n\), the germ \(y^2-x^{2n+1}\) is not a coordinate monomial. Its zero curve is singular and has a single tangent line, the \(x\)-axis: all of its nonzero points have \(x>0\), and \(y/x\to0\) on approach to zero. If it were a smooth embedded curve there, its nonzero tangent in the \(x\)-direction and the inverse-function theorem would give points of both signs of \(x\), a contradiction. Blowing up that point, in the chart following this line, gives

\[
 y=xv,\qquad y^2-x^{2n+1}=x^2(v^2-x^{2n-1}).
\tag{LG4}
\]

For \(n\ge2\), the strict weak curve at the chart origin is again singular, of the same form with \(n\) replaced by \(n-1\). Inductively, after \(k<n\) point blow-ups following this branch, its equation is \(v^2-x^{2(n-k)+1}\), still singular. A total coordinate monomial cannot have such a singular strict branch: its branches outside exceptional components are smooth coordinate hypersurfaces.

On a surface, a positive-codimension smooth centre through that point is either the point itself or a smooth curve. A curve is a Cartier centre and its blow-up is an isomorphism, so it cannot remove the singularity. Centres missing the point likewise have no effect near it. At least \(n\) point blow-ups along this chain are therefore necessary, regardless of additional steps elsewhere. Since \(n\) is unbounded, no finite global smooth-centre tower suffices. Every compact set meets only finitely many \(X_n\), however, so this does not contradict compact-local finiteness or the glued proper resolution map. Additional steps needed to make a final smooth branch transverse to the exceptional divisor only strengthen the absence of a uniform global bound.

## From resolved signs to compact analytic images

We now prove the equivalence used in (1), the set and map assertions in item 1, and the compact closed-set case of item 4. The argument uses the function resolution just proved and the earlier finite-cell and complement theorems, bounded-chart comparison, and strict frontier decrease, (D12). None of these steps uses an intrinsic analytic regular-locus theorem or a uniformization theorem as an input.

For this section write \(\mathcal P\) for the class defined locally by projections of relatively compact semianalytic sets with compact closure in their analytic domains. Write \(\mathcal C\) for the class defined by (1). The local comparison near the beginning of this lesson, followed by the earlier bounded-chart comparison, already proves \(\mathcal C\subset\mathcal P\). The converse requires compact parametrizations of closed sets. We construct those first.

### Resolving a finite sign formula simultaneously

**Factor lemma.** Suppose analytic germs \(h_1,\ldots,h_s\) at the origin satisfy

\[
\prod_{j=1}^s h_j=u\prod_{i=1}^n y_i^{a_i},\qquad u(0)\ne0.
\tag{U1}
\]

Then each \(h_j\) is an analytic unit times a monomial in the same coordinates.

**Proof.** The convergent real power-series ring is a domain: the lowest nonzero homogeneous parts of two nonzero series have nonzero product. The quotient by \((y_i)\) is another such domain. Hence \(y_i\) divides a product only if it divides a factor. The largest exponent of \(y_i\) dividing a nonzero analytic germ is finite, and division by that power leaves a convergent series. The exponent for a product is the sum of those exponents: after extracting the powers, reduce modulo \((y_i)\) and use its domain property.

Extract from every \(h_j\) its powers of each coordinate. Extracting a power of a different coordinate does not change the remaining divisibility by \(y_i\), again by reduction modulo \((y_i)\). Equation (U1) then says that the product of the residual factors is the unit \(u\). Each residual factor is a unit: its inverse is the product of all the others divided by \(u\). This proves the assertion without importing unique factorization of arbitrary analytic germs. \(\square\)

Consequently, resolve the product of the finitely many nonzero analytic functions in a sign formula. Near a point above its zero set, (LG2), or the ordinary implicit-function coordinate at a regular zero point outside the protected centre, gives (U1). Above a point where the product is nonzero, every factor is already a unit. On a sufficiently small connected coordinate box every residual unit has constant sign. Each equality or inequality in the pulled-back formula therefore depends only on whether each coordinate is positive, negative or zero. The set described by the formula is a union of coordinate sign strata. Identically zero functions cause no difficulty: evaluate their sign predicates first and discard them before forming the product; if none remain, use the identity map.

### A compact source for a semianalytic closure

**Compact sign theorem.** Let \(E\) be a relatively compact semianalytic subset of a real analytic manifold, with closure contained in its analytic domain. Then \(\overline E\) is the image of a compact real analytic manifold under an analytic map.

**Proof.** Cover \(\overline E\) by finitely many closed coordinate boxes \(Q_j\), whose interiors cover it and whose closures lie in connected coordinate neighborhoods \(V_j\) on which one finite analytic sign formula defines \(E\). Put \(E_j=E\cap Q_j\). The box inequalities join that sign formula. Every point of \(\overline E\) belongs to the interior of some \(Q_j\), so limits of points of \(E\) show that

\[
\overline E=\bigcup_j\overline{E_j}.
\tag{U2}
\]

It suffices to treat one \(E_j\). Resolve the product of its nonzero defining functions on \(V_j\), as above. This gives a proper surjective analytic map \(p:Y\to V_j\), with the pulled-back sign formula a union of coordinate sign strata on suitable charts of \(Y\). Define

\[
K=\overline{p^{-1}(E_j)}^{\,Y}.
\tag{U3}
\]

This is a closed subset of \(p^{-1}(\overline{E_j})\); it is compact because \(\overline{E_j}\subset Q_j\) is compact and \(p\) is proper. Its image is exactly

\[
p(K)=\overline{E_j}.
\tag{U4}
\]

One inclusion follows from continuity. For the other, if \(x_\nu\in E_j\) tends to \(x\in\overline{E_j}\), choose \(y_\nu\in p^{-1}(x_\nu)\) using surjectivity. The set formed by this convergent sequence and its limit is compact. Properness gives a convergent subsequence of the \(y_\nu\), with limit \(y\in K\) and \(p(y)=x\). Analytic manifolds are metrizable, so sequential compactness suffices here. It is essential to use the closure in (U3); the full inverse image \(p^{-1}(\overline{E_j})\) can contain exceptional directions not approached from \(E_j\).

At each point of \(K\), take a monomial chart centered at that point and a smaller closed coordinate box centered at zero, contained in the chart. Finitely many such boxes cover \(K\) by their interiors. In the larger open chart, closure of the finite union of selected sign strata is the union of their closed coordinate quadrants. Restricting those quadrants to the smaller box therefore covers exactly the part of \(K\) in that box. Each resulting piece is a product of intervals of the form \([0,b]\), \([-b,0]\), or the singleton \(\{0\}\). Coordinates absent from the formula may instead use \([-b,b]\), or its two half-intervals.

Each interval has an analytic parametrization by the compact circle \(S^1=\{(u,v):u^2+v^2=1\}\):

\[
(u,v)\longmapsto b u^2,\qquad
(u,v)\longmapsto-bu^2,\qquad
(u,v)\longmapsto bu,
\tag{U5}
\]

for the positive, negative and two-sided intervals respectively; use the constant map for a singleton. Products give analytic surjections from tori onto every selected quadrant box. Compose with the analytic inverse chart and with \(p\). The images stay inside \(p(K)\) and cover it. A finite disjoint union gives the required compact source for \(\overline{E_j}\), and (U2) gives one for \(\overline E\). If source pieces have different dimensions, add unused circle factors to reach their finite maximum; the images are unchanged. Dimension zero uses a point, and the empty set uses the empty manifold. \(\square\)

### Compact uniformization for the projection-defined class

**Compact uniformization theorem.** Every compact closed \(\mathcal P\)-subset \(S\) of a real analytic manifold \(X\) is the image of a compact finite-dimensional real analytic manifold under an analytic map to \(X\). In particular the map is proper.

**Proof.** Near each point of \(S\), choose a presentation \(S\cap V=\pi E\), with \(E\) a relatively compact semianalytic witness and compact closure in its analytic domain. Choose a closed base coordinate box \(Q\subset V\), with the point in its interior. Restrict the witness to \(E_Q=E\cap\pi^{-1}(Q)\). This remains relatively compact semianalytic, and

\[
\pi(E_Q)=S\cap Q,\qquad
\pi(\overline{E_Q})=\overline{\pi(E_Q)}=S\cap Q.
\tag{U6}
\]

For the middle equality, continuity gives one inclusion, and compactness of \(\overline{E_Q}\) makes its image closed and supplies the other. The last equality uses that \(S\cap Q\) is closed. Thus no point outside the desired trace is introduced by closing the witness.

Apply the compact sign theorem to \(E_Q\), then compose its parametrization with \(\pi\) and the target chart inverse. This gives a compact analytic source with image exactly \(S\cap Q\). Finitely many such boxes have interiors covering \(S\). Take their finite disjoint union, padding with unused circles if necessary to make the source dimension constant. A continuous map from a compact space to the Hausdorff manifold \(X\) is proper. \(\square\)

### The two definitions agree

Fix a \(\mathcal P\)-set \(S\) and an ambient point \(x\). Restrict to a sufficiently small open coordinate box about \(x\), with compact closure inside the witness neighborhood. In coordinates its trace \(B_0\) is globally subanalytic by the earlier bounded-chart comparison. Its closure is compact in the target chart. Recursively put

\[
C_j=\overline{B_j},\qquad B_{j+1}=C_j\setminus B_j.
\tag{U7}
\]

All these sets are globally subanalytic by the proved Boolean and closure calculus; all \(C_j\) are compact. The strict frontier theorem gives \(\dim B_{j+1}<\dim B_j\) whenever \(B_j\ne\varnothing\). With the empty-set dimension equal to \(-1\), the sequence therefore reaches the empty set after finitely many steps. Also \(C_{j+1}\subset C_j\), and two successive substitutions in (U7) give

\[
B_j=(C_j\setminus C_{j+1})\cup B_{j+2}.
\tag{U8}
\]

Consequently \(B_0\) is the finite union of the alternating differences

\[
(C_0\setminus C_1)\ \cup\ (C_2\setminus C_3)\ \cup\cdots,
\tag{U9}
\]

where all sufficiently late \(C_j\) are empty. Each compact closed \(C_j\) is a \(\mathcal P\)-set also when viewed in \(X\), because its closure stays inside the chart. Compact uniformization represents it as one compact-manifold image in \(X\). Equation (U9) is exactly the form (1) near \(x\). This proves \(\mathcal P\subset\mathcal C\), and hence the equivalence of the two definitions.

The dimension used in this terminating argument is the finite-cell dimension already proved in the preparation lesson. It does not use the separate intrinsic regular-locus theorem in item 2.

### The local calculus with the precise properness hypothesis

We can now transfer the proved bounded global calculus to the class in (1). Given finitely many local subanalytic sets near an ambient point, choose one smaller closed chart box inside all their witness neighborhoods. Their traces are globally subanalytic. Finite unions, intersections, differences, closures and interiors are globally subanalytic there, and on the interior of the box their closures and interiors agree with the corresponding local operations. Restriction and the definition equivalence prove the asserted local set calculus.

**Connected components.** On such a bounded chart trace there are finitely many connected components, each globally subanalytic by the finite-cell theorem. Every global connected component of \(S\) meeting the interior chart contains one of these whole local components: a connected subset meeting a connected component is contained in it. Thus only finitely many global components meet that neighborhood. The intersection of any particular global component with the neighborhood is a union of some of the finitely many local components, restricted back to the neighborhood, so is subanalytic. This proves component subanalyticity and local finiteness at every ambient point, including points outside \(S\).

**Analytic inverse images.** For an analytic \(f:Y\to X\), choose a target chart inside the target set's witness neighborhood and a smaller bounded region around the image of the point under consideration. By continuity choose a small closed source chart box whose image lies in that region. On that box the graph of \(f\) is globally semianalytic: its analytic coordinate functions extend to a neighborhood of the compact box, and the box inequalities bound the graph. Intersect it with the target set's bounded subanalytic trace, then project to the source coordinates. This is globally subanalytic by graph calculus. Restricting to the source box's interior proves that \(f^{-1}(S)\) is locally subanalytic. No properness hypothesis is needed for this direction.

**Images proper on the selected closure.** Let \(W\subset Y\) be subanalytic and suppose only that \(f|_{\overline W}:\overline W\to X\) is proper. Around a target point choose a compact coordinate box \(Q\), with that point in its interior. Then

\[
K_Q=\overline W\cap f^{-1}(Q)
\tag{U10}
\]

is compact. Cover it by finitely many closed source chart boxes \(P_\ell\) whose interiors cover \(K_Q\), each lying in a bounded witness chart for \(W\) and in the inverse image of the target coordinate chart. Graph intersection and projection on these compact boxes show that each \(f(W\cap P_\ell)\) is subanalytic in target coordinates. More explicitly, intersect the compact analytic graph with the globally subanalytic source trace \(W\cap P_\ell\), and project. Every preimage in \(W\) of a point in \(\operatorname{int}Q\) belongs to \(K_Q\), so

\[
f(W)\cap\operatorname{int}Q
=\left(\bigcup_\ell f(W\cap P_\ell)\right)\cap\operatorname{int}Q.
\tag{U11}
\]

This proves the image assertion with exactly its stated closure-properness hypothesis. The map need not be proper on all of \(Y\), and the argument does not replace \(f(W)\) by the larger \(f(\overline W)\).

These results prove item 1 and compact closed-set uniformization. Local compact parametrizations alone would not control the dimensions of the sources over a noncompact base. The [rank-minor reduction and locally finite assembly below](#dimension-controlled-proper-uniformization) supply that control and complete item 4. A finite analytic partition does not by itself identify every intrinsic regular point; the [analytic-descent argument](#detecting-the-entire-analytic-regular-locus) establishes that stronger assertion.

### Exercises on the compact construction

**Exercise U1 (intermediate: the exceptional fibre is too large).** In the real blow-up of the origin of \(\mathbb R^2\), consider the chart \(p(u,v)=(u,uv)\) and the positive horizontal ray \(E=\{(x,0):x>0\}\). Compare \(\overline{p^{-1}E}\) and \(p^{-1}\overline E\) in this chart.

**Solution.** The inverse image of \(E\) in this chart is \(\{u>0,v=0\}\). Its closure is \(\{u\ge0,v=0\}\), meeting the exceptional line only at \((0,0)\). The inverse image of \(\overline E\) contains that set and the whole line \(\{u=0\}\), because every point of the line maps to the origin. Globally the latter inverse image contains the whole exceptional projective line, whereas the former closure meets it only in the horizontal direction. Formula (U3) retains precisely the directions actually approached by the chosen set.

**Exercise U2 (intermediate: an alternating boundary expansion).** Let \(B_0=(0,1)^2\cup\{(1/2,0)\}\subset\mathbb R^2\). Compute the nonempty sets in (U7) and verify (U9).

**Solution.** Put \(p=(1/2,0)\) and \(Q=[0,1]^2\). Then \(C_0=Q\), \(B_1=\partial Q\setminus\{p\}\), \(C_1=\partial Q\), \(B_2=C_2=\{p\}\), and \(B_3=C_3=\varnothing\). The dimensions of the nonempty \(B_j\) are \(2,1,0\), decreasing strictly. The alternating formula gives \((C_0\setminus C_1)\cup(C_2\setminus C_3)=(0,1)^2\cup\{p\}\), as required. Using only \(C_0\setminus C_1\) would incorrectly lose the selected boundary point.

## Dimension-controlled proper uniformization

Compact source maps carry more parameters than their images need. A height function detects a smaller analytic subset meeting every compact fibre. Resolving its rank-minor equation reduces the source dimension without losing any image points. Repetition gives one dimension bound for all local pieces; a locally finite target cover then makes their disjoint union proper.

The classical dimension-preserving uniformization theorem is proved in Bierstone and Milman, [*Semianalytic and subanalytic sets*](https://www.numdam.org/item/PMIHES_1988__67__5_0/), Proposition 3.12 and Theorem 5.1, printed pp. 19–20 and 30–32. The argument below uses the compact torus parametrizations and the function resolution already established in this lesson.

### Reducing the dimension of a compact analytic source

The compact construction above gives finite unions of torus sources, but their dimensions initially depend on the semianalytic witnesses. We now reduce those dimensions while preserving each image exactly. The inputs are the proved proper function resolution (LG2), the analytic constant-rank and inverse-function theorems, and compactness. The rank reduction itself uses no subanalytic regular-locus theorem or analytic-set uniformization.

Write
\[
 T^m=(S^1)^m
 =\{(u_1,v_1,\ldots,u_m,v_m):u_j^2+v_j^2=1\},
 \qquad
 E_j=-v_j\partial_{u_j}+u_j\partial_{v_j}.
 \tag{N1}
\]
The fields \(E_1,\ldots,E_m\) form a global analytic tangent frame. We take \(T^0\) to be one point. Both \(u_j\) and \(v_j\) are globally defined analytic functions on the torus.

**One-step reduction lemma.** Let \(F:T^m\to\mathbb R^n\) be analytic, let
\(r=\max_{z\in T^m}\operatorname{rank}dF_z\), and suppose \(m>r\). There are finitely many analytic maps \(a_\alpha:T^{m-1}\to T^m\) such that
\[
 F(T^m)=\bigcup_\alpha F\bigl(a_\alpha(T^{m-1})\bigr).
\]
Every replacement map is a composition with \(F\). In particular its differential rank is at most \(r\).

**Proof.** Choose \(z_0\) of rank \(r\), and a nonzero vector \(w\in\ker dF_{z_0}\). The differential of the displayed inclusion \(T^m\hookrightarrow\mathbb R^{2m}\) is injective. Consequently at least one of its coordinate functions, denoted by \(h\), satisfies \(dh_{z_0}(w)\ne0\). Thus \(dh_{z_0}\) is not in the row space of \(dF_{z_0}\), and \(d(F,h)_{z_0}\) has rank \(r+1\).

Form the global analytic \((n+1)\)-by-\(m\) matrix whose rows are the derivatives of \(F_1,\ldots,F_n,h\) along the frame (N1). Define
\[
 A(z)=
 \begin{pmatrix}
 E_1F_1(z)&\cdots&E_mF_1(z)\\
 \vdots&&\vdots\\
 E_1F_n(z)&\cdots&E_mF_n(z)\\
 E_1h(z)&\cdots&E_mh(z)
 \end{pmatrix},
 \qquad
 g(z)=\sum_{\substack{|I|=r+1\\|J|=r+1}}
                 \bigl(\det A_{I,J}(z)\bigr)^2,
 \qquad Z=g^{-1}(0).
 \tag{N2}
\]
There are enough rows and columns because \(r\le n\) and \(r<m\). The sum is finite, and it is positive at \(z_0\). Moreover, over the real numbers,
\(g(z)=0\) if and only if \(\operatorname{rank}d(F,h)_z\le r\). Since \(m\ge1\), the torus is connected; the nonzero value at \(z_0\) verifies the nonidentical-vanishing hypothesis of function resolution on every connected component of this source.

We claim that
\[
                         F(Z)=F(T^m).
 \tag{N3}
\]
Fix \(x\in F(T^m)\). The fibre \(F^{-1}(x)\) is a nonempty closed subset of the compact torus. Let \(z\) minimize \(h\) on it. If \(\operatorname{rank}dF_z<r\), adjoining one row gives rank at most \(r\), so \(z\in Z\). If \(\operatorname{rank}dF_z=r\), a nonzero \(r\)-minor stays nonzero near \(z\), while the global maximality of \(r\) gives the opposite rank bound. Thus \(F\) has constant rank \(r\) there. The constant-rank theorem makes its local fibre a smooth analytic manifold with tangent space \(\ker dF_z\). The minimum of \(h\) on that fibre implies \(dh_z|_{\ker dF_z}=0\). Hence adjoining \(dh_z\) does not increase rank, and again \(z\in Z\). For \(r=0\), this latter argument simply uses a locally constant \(F\), whose local fibre is the whole source neighborhood. Every fibre meets \(Z\), proving (N3); the reverse inclusion was automatic.

At every zero of \(g\), all minors in (N2) vanish. Differentiating their sum of squares therefore gives \(dg=0\) there. Thus \(Z=\{g=0,dg=0\}\), and the existing resolution theorem's singular-zero conclusion covers every point of the inverse image of \(Z\).

Apply the proved proper function resolution to the single nonzero analytic function \(g\). It gives a proper surjective analytic map \(p:Y\to T^m\), with \(Y\) an \(m\)-dimensional analytic manifold, and local coordinates in which
\(g\circ p\) is a nonvanishing unit times a monomial. The source dimension is unchanged by the blow-up charts and their analytic gluing in that theorem. Because \(T^m\) is compact, properness makes \(Y\) compact. Put \(K=p^{-1}(Z)\). Then \(K\) is compact and \(p(K)=Z\), by surjectivity and the equality defining this inverse image.

At each point of \(K\), choose a monomial coordinate neighborhood and a smaller centered closed coordinate box
\(Q=\prod_{j=1}^m[-b_j,b_j]\), with all \(b_j>0\), whose closure stays inside that neighborhood. The interiors of finitely many such boxes cover \(K\). In any one of these charts, if
\(g\circ p=u\prod_j y_j^{e_j}\), then the part of \(K\) in the box is exactly the union of
\(Q\cap\{y_i=0\}\) for those \(i\) with \(e_i>0\). There is at least one such index at the chosen centre of the chart.

Each of these closed hyperplane boxes is the analytic image of \(T^{m-1}\): give its circle factors the indices \(j\ne i\), and set
\[
             y_i=0,\qquad y_j=b_j u_j\quad(j\ne i).
 \tag{N4}
\]
The coordinate functions \(u_j:S^1\to[-1,1]\) are surjective, so the image is the entire hyperplane box. Composing (N4) with the analytic inverse chart gives an analytic map into \(Y\). This is analytic also at points mapping to the edges of the box: the inverse chart is defined on a neighborhood of the whole closed box. Its image lies in \(K\), not merely in an approximation or closure of \(K\). For \(m=1\), (N4) is the map from one point to the zero coordinate.

Compose these finitely many maps with \(p\), calling the resulting maps \(a_\alpha:T^{m-1}\to T^m\). Their images lie in \(Z\) and cover \(Z\). Therefore (N3) yields
\[
             F(T^m)=F(Z)
                  =\bigcup_\alpha(F\circ a_\alpha)(T^{m-1}).
 \tag{N5}
\]
The chain rule gives \(\operatorname{rank}d(F\circ a_\alpha)\le r\). This proves the lemma. Notice that singular fibres were retained in the lower-rank case, and exceptional components were retained in \(K\). Neither was discarded. \(\square\)

**Finite rank-bound reduction.** If \(R\ge\max\operatorname{rank}dF\) is a nonnegative integer, then the image of an analytic \(F:T^m\to\mathbb R^n\) is a finite union of analytic images of \(T^R\). These maps can all be written as \(F\circ b_\beta\), with \(b_\beta:T^R\to T^m\).

If \(m<R\), compose with the projection \(T^R\to T^m\), which preserves the image. If \(m=R\), do nothing. If \(m>R\), apply the one-step lemma. Each new map has rank at most \(R\) by the chain rule, so the same argument applies whenever its source dimension still exceeds \(R\). The dimension drops by exactly one at every replacement, and each replacement has finitely many outputs. Induction on \(m-R\) therefore ends after at most \(m-R\) levels with finitely many maps and gives
\[
                 F(T^m)=\bigcup_\beta(F\circ b_\beta)(T^R).
 \tag{N6}
\]
All compositions are analytic on their entire compact source. The number of branches need not have a uniform bound across different initial compact problems; the conclusion of each individual problem is finite. Taking \(R=n\) already gives the uniform ambient-dimension bound required for the noncompact construction.

The same conclusion holds for an analytic map from an arbitrary nonempty compact analytic manifold \(C\) into a finite-dimensional analytic manifold \(X\), with \(R=\max_{z\in C}\operatorname{rank}df_z\). To see this without an embedding theorem, cover \(C\) by the interiors of finitely many closed coordinate boxes, each lying inside a source chart and mapping into one target chart. Each box is an analytic image of a torus of its dimension by the product version of (N4), now with no coordinate fixed to zero. The inverse source chart is defined on a neighborhood of the closed box. Composing with \(f\) gives finitely many torus maps whose images cover \(f(C)\) exactly. Their ranks are at most \(R\). Apply (N6) in their target charts, padding smaller initial torus dimensions if necessary, and compose back with the target chart inverse. The result is a finite union of compact \(R\)-tori mapping analytically into \(X\), with image exactly \(f(C)\). Empty sources are omitted.

### Comparing the rank bound with cell dimension

The sharper bound \(R\le\dim S\) uses the already proved finite-cell dimension, not an intrinsic regular-locus assertion. The relevant provider is Why cell dimension is intrinsic: (D4) gives inclusion monotonicity, and the paragraph following it identifies the cell dimension of a definable differentiable manifold with its manifold dimension. The same provider proves invariance under bounded analytic changes of coordinates. Its established attribution and CC BY 4.0 component notice remain in force.

Here is the exact application, including the boundedness needed for that provider. Suppose an analytic \(f:C\to X\) has image in a locally subanalytic set \(S\), and let \(D\) bound the cell dimensions of the bounded coordinate traces of \(S\). At a point \(z\) where \(df\) has rank \(r>0\), choose an invertible \(r\)-by-\(r\) derivative minor in source and target analytic coordinates. Fix the remaining source coordinates at their values at \(z\). The analytic inverse-function theorem on this transverse \(r\)-dimensional slice parametrizes a part of its image as a graph over the corresponding \(r\) target coordinates. Choose a nonempty open box in those coordinates whose compact closure stays inside the graph domain and whose graph stays in a target chart trace used to define \(D\). The graph functions are analytic on a neighborhood of that closed box. Their restricted graph is therefore globally subanalytic by the proved bounded-chart comparison; it is an embedded analytic \(r\)-manifold and is contained in \(S\).

The manifold-dimension statement gives this graph cell dimension \(r\), and inclusion monotonicity bounds it by the dimension of the chosen trace of \(S\), hence by \(D\). Rank zero satisfies the same inequality whenever \(S\) is nonempty. Thus
\[
                   \operatorname{rank}df_z\le D
                   \quad(z\in C),
                   \qquad
                   \max_{z\in C}\operatorname{rank}df_z\le D.
 \tag{N7}
\]
No analyticity of the intrinsic regular locus of \(S\) is used: the graph is constructed directly inside the image of \(f\).

For a nonempty \(S\) in an \(n\)-manifold, its locally defined cell dimension is an integer \(D\) with \(0\le D\le n\). It is well defined by the proved chart invariance and finite-union rule, and the maximum exists because the possible dimensions lie in this finite set. Combining (N6)–(N7), every compact parametrization supplied above can be replaced by a finite union of compact analytic sources of dimension at most \(D\), with exactly the same image. Multiplying a source of dimension \(d<D\) by the unused compact factor \(T^{D-d}\) makes its dimension exactly \(D\), preserves its image and preserves compactness. Alternatively apply (N6) with \(R=D\) directly. These are the dimension-controlled compact sources needed for the locally finite proper assembly. The empty set uses the empty manifold, without assigning it a negative manifold dimension.

**Example for the mechanism.** On \(T^2\), take \(F=u_1=\cos\theta_1\) and \(h=u_2=\cos\theta_2\). Then \(r=1\),
\(A=\operatorname{diag}(-v_1,-v_2)\), and \(g=v_1^2v_2^2\). Its zero set is the union of four coordinate circles, two given by \(v_1=0\) and two by \(v_2=0\). On every fibre of \(F\), the minimum of \(h\) occurs on the circle \((u_2,v_2)=(-1,0)\), which still maps onto the whole interval \([-1,1]\). The circles \(v_1=0\) retain the lower-rank fibres over the endpoints. This explicit example explains the equality of images; the general proof uses the full zero set and its compact monomial charts.

### A locally finite assembly with a fixed source dimension

**Proper uniformization.** Let \(S\) be a nonempty closed subanalytic subset of a finite-dimensional real analytic manifold \(X\), Hausdorff and countable at infinity. Let \(D\) be its finite-cell dimension. There is a Hausdorff, second-countable real analytic manifold \(Y\), of pure dimension \(D\), and a proper analytic map

\[
F:Y\longrightarrow X,\qquad F(Y)=S.
\tag{N8}
\]

If \(S\) is compact, \(Y\) can be compact. The empty set is represented by the empty manifold. Properness is relative to the stated ambient manifold \(X\).

**Proof.** The elementary [locally finite compact chart construction](#locally-finite-compact-chart-supports), (F2)–(F4), gives a countable family of closed coordinate boxes \(Q_i\), each contained in an analytic coordinate neighborhood \(V_i\), with locally finite family \((Q_i)\) and with interiors covering \(X\). The boxes can be chosen subordinate to the witness neighborhoods used in the projection definition of \(S\). This construction uses only an exhaustion by nested compact sets and finite covers of its compact bands. It does not use uniformization or an analytic partition of unity.

Since \(S\) is closed in \(X\), each \(S_i=S\cap Q_i\) is compact and subanalytic. The compact construction above represents \(S_i\) as a finite union of analytic images of tori. Every such image lies in \(S_i\), hence entirely in the target chart \(V_i\). Apply the preceding dimension-reduction lemma in that chart. It produces finitely many maps

\[
f_{ij}:T^{e_{ij}}\longrightarrow X,\qquad
e_{ij}\le D,\qquad
\bigcup_j f_{ij}(T^{e_{ij}})=S_i,
\quad f_{ij}(T^{e_{ij}})\subset Q_i.
\tag{N9}
\]

An empty \(S_i\) contributes no maps. For \(e_{ij}<D\), add \(D-e_{ij}\) unused circle factors and let \(f_{ij}\) ignore them. This preserves its analyticity, compactness and image. Define \(Y\) as the disjoint union of these copies of \(T^D\), and define \(F\) componentwise by the corresponding maps.

There are countably many components, each a Hausdorff second-countable analytic \(D\)-manifold. Their disjoint union is Hausdorff and second countable: unite one countable basis from each component. It has the same finite dimension \(D\) everywhere. Componentwise charts and transition maps make \(F\) analytic. The cover by the interiors of \(Q_i\) and (N9) prove \(F(Y)=S\).

To check properness, let \(K\subset X\) be compact. Local finiteness and a finite subcover of \(K\) show that only finitely many \(Q_i\) meet \(K\). Thus \(F^{-1}(K)\) lies in finitely many of the compact source tori. It is closed there, because \(K\) is closed in the Hausdorff space \(X\) and \(F\) is continuous. Consequently \(F^{-1}(K)\) is compact. This proves properness without requiring the images of different source components to be disjoint.

When \(S\) is compact, finitely many of the chosen interior boxes cover it. Using just those boxes and their finitely many tori gives a compact \(Y\), and the same image equality. The dimension-zero case uses \(T^0\), a point, and the same locally finite argument. \(\square\)

The dimension in (N8) also equals the supremum of the dimensions of intrinsic analytic regular points, as used in item 2. Here only that numerical equality is needed; it does not assert subanalyticity of the entire regular locus. To prove it, choose a bounded open coordinate box \(U\), with closure inside a witness neighborhood, such that \(\dim(S\cap U)=D\). Take a finite analytic cell decomposition of \(S\cap U\) containing a cell \(C\) of dimension \(D\). Every point of this trace lies in the open set \(U\), so its cells describe \(S\) near that point. For every other cell \(C'\), its intersection with \(C\) is empty, and

\[
C\cap\overline{C'}\subset\overline{C'}\setminus C',
\qquad \dim(\overline{C'}\setminus C')<\dim C'\le D.
\tag{N10}
\]

The finite-cell dimension and strict-frontier theorems imply that these finitely many intersections cannot cover \(C\). Choose \(p\in C\) outside every \(\overline{C'}\). A small ambient neighborhood meets no other cell. As an embedded analytic submanifold, \(C\) is closed in a sufficiently small neighborhood of \(p\), and there \(S=C\). Thus \(p\) is an intrinsic regular point of dimension \(D\). Conversely, a regular \(d\)-dimensional manifold piece contained in \(S\) has \(d\le D\) by manifold dimension and monotonicity. This gives the claimed numerical equality. The [analytic-descent proof below](#detecting-the-entire-analytic-regular-locus) establishes definability of the entire intrinsic regular locus.

### A compact fibre meets the minimizing circle

<a href="figures/SH03-critical-height-dimension-reduction.svg"><img src="figures/SH03-critical-height-dimension-reduction.svg" alt="A parameter square for the two-dimensional torus: the rank-drop grid contains a horizontal minimizing circle, which maps onto the complete interval from minus one to one." style="max-width:100%;height:auto"></a>

**Figure.** Write each circle as \((\cos\theta,\sin\theta)\) or \((\cos\phi,\sin\phi)\). For \(f(\theta,\phi)=\cos\theta\) and \(h(\theta,\phi)=\cos\phi\), the squared determinant is \(g=\sin^2\theta\sin^2\phi\). The blue grid is \(Z=\{g=0\}\); opposite edges of the square are identified. The gold circle \(\phi=\pi\) is part of \(Z\) and minimizes \(h\) on every fibre. The two dashed circles form \(f^{-1}(1/2)\), and their two intersections with the gold circle map to the indicated green point. The image is preserved even though the minimizing circle maps two-to-one over \((-1,1)\). This is the explicit model of the rank-minor and fibre-extremum argument, not an injective parametrization. Original programme diagram, GPT-6 Astra (OpenAI), Ultra, CC0. Full-size diagram · Reproducible Python source.

### Exercises on dimension control and properness

**Exercise N1 (intermediate: retaining singular fibres).** In the displayed torus model, compute the set \(Z\), verify that it meets the fibres over \(1\) and \(-1\), and exhibit a one-dimensional compact analytic source with the same image as the original two-dimensional torus.

**Solution.** The matrix of \(d(f,h)\) in the angular frame is diagonal with entries \(-\sin\theta\) and \(-\sin\phi\). Hence \(Z\) is the union of the circles \(\theta=0\), \(\theta=\pi\), \(\phi=0\), and \(\phi=\pi\), with angles interpreted modulo \(2\pi\). The endpoint fibres are the entire first two circles, so they are retained, not discarded as exceptional. The circle \(\phi=\pi\) maps by \(\theta\mapsto\cos\theta\) onto \([-1,1]\). It is a compact one-dimensional analytic source with the full image. An interior fibre has two points on this selected circle; an endpoint fibre has one. No injectivity or preservation of the original fibres is part of uniformization.

**Exercise N2 (intermediate: componentwise properness is insufficient).** Let \(Y\) be a countable disjoint union of points and map every point to \(0\in\mathbb R\). Explain why every component map is proper, but the combined map is not. Also distinguish properness of the identity of \((0,1)\) from properness of its inclusion into \(\mathbb R\).

**Solution.** Each point is compact, so its map is proper. The inverse image of the compact set \(\{0\}\) under the combined map is the infinite discrete space \(Y\); its cover by singleton open sets has no finite subcover. The image supports are not a locally finite family, which is exactly the hypothesis used in the proof of (N8). The identity of \((0,1)\) is proper because inverse images of compact subsets are those same subsets. Its inclusion into \(\mathbb R\) is not proper: the inverse image of \([0,1]\) is all of \((0,1)\), which is not compact. Therefore the ambient target in a proper uniformization statement must be retained.

## Detecting the entire analytic regular locus

A cell partition supplies many analytic manifold points. Recognizing every such point, including points crossed by an unnecessary cell boundary, requires a test independent of the partition. We will use analyticity of squared distance to a closed set, after proving that a continuous subanalytic function has a subanalytic analyticity locus.

The graphic-point mechanism comes from Malgrange, as used by Bierstone and Milman in [Semianalytic and subanalytic sets, §7, printed pp. 37–41](https://www.numdam.org/article/PMIHES_1988__67__5_0.pdf), especially Proposition 7.4 and Theorems 7.5–7.10. The proof below expands the local convergence and compact descent arguments. It uses compact uniformization and the compact rank reduction (N6); the locally finite noncompact uniformization assembly and a finite-smoothness version of Tamm's theorem are not inputs.

The complex analytic providers are the proved contour preparation and division theorem, unique factorization of holomorphic germs, and finite branches with connected dense smooth cores. These concern complex analytic sets and do not assume the real subanalytic regular-locus statement being proved.

### Convergence at a critical source point

First, if \(a,b\) are convergent complex power series, \(b\ne0\), and \(a=bH\) for a formal series \(H\), then \(H\) converges. Make \(b\) regular in one variable and write \(b=uP\), with \(P\) distinguished. Divide \(a/u\) analytically by \(P\). Uniqueness of formal division by the same distinguished polynomial makes the analytic remainder zero and identifies the analytic quotient with \(H\). Formal division follows coefficient by coefficient in the other variables: modulo their successive powers, division by the leading power of the distinguished variable determines quotient and remainder.

**Lemma.** Let \(\psi:(\mathbb C^m,0)\to(\mathbb C^n,0)\) be holomorphic of generic rank \(n\). If \(G\in\mathbb C[[y]]\) and \(f=G\circ\psi\) converges, then \(G\) converges.

**Proof.** The case \(n=0\) is constant and immediate. Choose a nonzero \(n\)-rowed Jacobian minor \(\delta\), after reordering source coordinates. On \(\delta\ne0\), differentiation with respect to the first coordinates in \((\psi_1,\ldots,\psi_n,x_{n+1},\ldots,x_m)\) has the form
\[
D_j=\delta^{-1}\sum_{\ell=1}^n A_{j\ell}(x)\partial_{x_\ell},
\qquad D_j\psi_i=\delta_{ij},
\]
with holomorphic cofactors \(A_{j\ell}\). Set \(F_\beta=D^\beta f\). Its numerator is holomorphic on one fixed sufficiently small source neighborhood and its denominator is a power of \(\delta\). Formal differentiation gives
\[
F_\beta=(\partial^\beta G)\circ\psi\in\mathbb C[[x]],
\qquad F_\beta(0)=\partial^\beta G(0).
\]
Here the equality is first in the fraction field of formal series; its right side lies in the formal series ring. The divisibility observation makes every \(F_\beta\) holomorphic as a germ at zero.

Moreover \(df=\sum_jF_{e_j}\,d\psi_j\) as a germ. The meromorphic identity extends to the fixed connected source neighborhood. Thus, wherever \(\delta\ne0\), \(f\) is independent of the unused local coordinates, and is a holomorphic function of \(\psi\) alone. The \(D_j\) commute there, so the derivative order used to define \(F_\beta\) is immaterial.

We now obtain one neighborhood for all \(F_\beta\). Make an additional linear source change so \(\delta\) is regular in a variable \(z\), and prepare
\[
\delta(z,x')=u(z,x')P(z,x').
\]
The already defined meromorphic operators are simply transported under this change. Retain the original complementary functions \(\ell=(x_{n+1},\ldots,x_m)\) as fixed linear functions in the new coordinates; they are not replaced by arbitrary new coordinate functions. The map \((\psi,\ell)\) remains a local coordinate system wherever \(\delta\ne0\). Choose a circle \(|z|=r\) and a connected smaller \(x'\)-polydisc such that \(P\ne0\) on the circle and all roots of \(P(\,\cdot\,,x')\) lie strictly inside it. The original holomorphic functions and the unit \(u\) are defined on a neighborhood of the closed cylinder.

For every \(\beta\), write \(F_\beta=h_\beta/P^{q_\beta}\), with \(h_\beta\) holomorphic on that fixed neighborhood. The contour division formula divides \(h_\beta\) by the monic polynomial \(P^{q_\beta}\) on the same cylinder, producing a polynomial remainder whose coefficients are holomorphic throughout the fixed \(x'\)-polydisc. At the origin this remainder vanishes as a germ: \(F_\beta\) was holomorphic there, so uniqueness of Weierstrass division applies. The coefficient identity theorem makes it zero on the whole connected \(x'\)-polydisc. Consequently every \(F_\beta\) is holomorphic on the common interior cylinder. No bound on \(q_\beta\) is required; the same circle avoids the zeros of all denominators.

On the compact circle \(K=\{(z,0):|z|=r\}\), use the local inverse of \((\psi,\ell)\) to form
\[
H_i(x,t)=f\bigl((\psi,\ell)^{-1}(\psi(x)+t,\ell(x))\bigr).
\]
At each point of \(K\), this is holomorphic on a product of a source neighborhood and a positive target polydisc. Shrink both so it is bounded on their closures. The source neighborhoods have a finite subcover of \(K\). Taking the largest of their bounds and the smallest target radius gives constants \(C,\rho>0\) such that Cauchy's estimate yields
\[
|F_\beta(x)|=|\partial_t^\beta H_i(x,0)|
\le C\,\beta!\,\rho^{-|\beta|}
\qquad(x\in K)
\]
for every multi-index. The equality uses the retained complementary functions, so these are exactly the transported operators \(D_j\). No gluing of the functions \(H_i\) is needed for the estimate.

The common-cylinder holomorphic extension and Cauchy's formula in \(z\), with \(x'=0\), give
\[
|\partial^\beta G(0)|=|F_\beta(0)|
\le C\,\beta!\,\rho^{-|\beta|}.
\]
Thus the coefficients of \(G=\sum_\beta c_\beta y^\beta\) satisfy
\(|c_\beta|\le C\rho^{-|\beta|}\). The product of the \(n\) geometric series proves absolute convergence when every \(|y_j|<\rho\). This proves convergence at the original, possibly critical, source point. \(\square\)


### The local obstruction to an analytic graph

Let \(\phi:M\to N\) and \(f:M\to\mathbb R\) be analytic, with \(\dim N=n\). Assume that \(\phi\) has generic rank \(n\) on every component of \(M\), and that
\[
\operatorname{rank}d(\phi,f)=n
\quad\text{where }\operatorname{rank}d\phi=n.
\tag{IR1}
\]
A point \(a\in M\) is **graphic** if an analytic germ \(h\) at \(\phi(a)\) satisfies \(f_a=h\circ\phi_a\). Such an \(h\) is unique. Regular points of \(\phi\) occur arbitrarily near \(a\), and their images contain open target sets. Equality of two pullbacks therefore forces equality of the two target germs by the analytic identity theorem.

Condition (IR1) is necessary: \(\phi(x,z)=x\), \(f(x,z)=z\) has no graphic points, although \(\phi\) has full rank. For a parametrization of a function's graph, (IR1) is automatic, since \(f\) is constant on each local fibre at a submersion point.

**One-point obstruction lemma.** The non-graphic set \(E\) is closed real analytic and lies in the critical set of \(\phi\).

**Proof.** Complexify small real coordinate neighborhoods. The differential identities in (IR1) extend holomorphically. Choose a nonzero Jacobian minor \(\delta\), and form the meromorphic functions \(F_\beta=D^\beta f\) used in the convergence lemma. Off \(\delta=0\), condition (IR1) makes \(f\) locally a function of \(\phi\), and the \(F_\beta\) are its descended derivatives. Their denominators are powers of \(\delta\).

Suppose all \(F_\beta\) are holomorphic at \(a\). Define
\[
G_a(t)=\sum_\beta\frac{F_\beta(a)}{\beta!}t^\beta .
\tag{IR2}
\]
For every \(k\), the Taylor-composition identities through degree \(k\) hold at regular points. They are holomorphic identities involving only finitely many \(F_\beta\), so extend to \(a\). Hence
\[
\widehat f_a=G_a(\widehat\phi_a-\phi(a)).
\]
The convergence lemma makes \(G_a\) convergent, so \(a\) is graphic. Conversely, a graphic germ \(h\) gives \(F_\beta=(\partial^\beta h)\circ\phi\), so every \(F_\beta\) is holomorphic. Thus \(E\) is exactly the union of their pole loci.

This infinite union is analytic for a specific reason. Shrink to a fixed complex neighborhood where \(\{\delta=0\}\) has finitely many irreducible hypersurface components. Each meromorphic function with denominator a power of \(\delta\) has pole locus equal to a union of some of these components. Local unique factorization tests which denominator factors cancel. On the connected dense smooth core of an irreducible component, the identity theorem propagates such cancellation along the component; local factorization then extends it at its remaining points. A genuine uncancelled factor instead gives a pole along the entire component, because the holomorphic locus is open. Local unique factorization also excludes a pole supported only in smaller codimension. Therefore the union of all the pole loci is a union of a subset of the same finite list of components, hence analytic.

Conjugation preserves the construction. Denote its complex analytic pole set by \(E^{\mathbb C}\). At a real point any complex descended germ equals its conjugate, since their pullbacks agree and descent is unique. Thus the real non-graphic set is exactly \(E=E^{\mathbb C}\cap M\). Retain the constructed complex set, which can be larger than a minimal complexification of this real trace. Using any nonzero minor shows that every regular point of \(\phi\) is graphic. These local sets agree because their defining property is intrinsic. \(\square\)

### Comparing two points of a fibre

The fibre product
\[
R=M\times_NM=\{(a,b):\phi(a)=\phi(b)\}
\tag{IR3}
\]
is analytic. A pair is graphic if one germ \(h\) works at both points. Write \(E_2\) for the pairs that are not graphic.

**Two-point obstruction lemma.** The subset \(E_2\) is closed analytic.

**Proof.** Work directly on complexifications of the two source charts and their common target chart, and use the complex pole sets \(E^{\mathbb C}\) constructed in the preceding proof. Write \(R^{\mathbb C}\) for the resulting holomorphic fibre product. A complex graphic pair stays graphic on a neighborhood, using the same representative \(h\), so its non-graphic set \(E_2^{\mathbb C}\) is closed. Put
\[
B^{\mathbb C}=R^{\mathbb C}\cap
\bigl((E^{\mathbb C}\times M^{\mathbb C})
\cup(M^{\mathbb C}\times E^{\mathbb C})\bigr),
\]
using the appropriate source chart in each factor. This analytic set is contained in \(E_2^{\mathbb C}\). In particular, \(B^{\mathbb C}\) is formed from the actual complex pole loci, not from an arbitrary complexification of their possibly smaller real traces.

On \(R^{\mathbb C}\setminus B^{\mathbb C}\), agreement of the two descended germs is locally constant. Near a pair, represent the two germs by holomorphic functions \(h_1,h_2\) on one connected target ball. Either they agree identically, or their germs agree nowhere on that ball: germ equality would imply equality on an open set and then everywhere. Uniqueness of descent identifies these with the germs at all nearby pairs.

Take finite irreducible branch representatives \(R_i\) of \(R^{\mathbb C}\) at the pair. A branch contained in \(B^{\mathbb C}\) is wholly bad. On every other branch, take a connected dense smooth core and delete \(B^{\mathbb C}\). The complex branch and analytic-deletion results make this a connected dense set, on which the locally constant condition is either always good or always bad. In the bad case, closedness puts the whole branch in \(E_2^{\mathbb C}\). In the good case, every point of the branch outside \(B^{\mathbb C}\) is good, since its neighborhood meets the dense good core and the condition is locally constant there. Hence, after a common shrinking,
\[
E_2^{\mathbb C}=B^{\mathbb C}\ \cup\!\!\bigcup_{\text{bad branches }i}R_i .
\tag{IR4}
\]
This is analytic. Connected cores are retained on their original larger representatives until the final shrinking; connectedness of an arbitrary smaller branch intersection is not assumed. Conjugation and uniqueness identify the real trace with \(E_2\), proving the claim. \(\square\)

### Analyticity of a continuous subanalytic function

**Analytic-locus theorem.** If \(g:V\to\mathbb R\) is continuous and subanalytic on an open subset of an analytic manifold, then
\[
\mathcal A(g)=\{x\in V:g\text{ is analytic on a neighborhood of }x\}
\tag{IR5}
\]
is open and subanalytic.

**Proof.** Openness is part of the definition. In a coordinate chart, choose a closed box \(Q\) whose interior contains the point being considered and whose closure lies in \(V\). The graph of \(g|_Q\) is compact, closed and subanalytic. Compact uniformization gives a compact analytic manifold \(M\) and an analytic map
\[
\Phi=(\phi,f):M\longrightarrow\mathbb R^n\times\mathbb R,
\qquad \Phi(M)=\operatorname{graph}(g|_Q).
\]

Discard components on which the generic rank of \(\phi\) is less than \(n\). There are finitely many components, since \(M\) is compact. For a discarded component \(C\), put \(r=\max_C\operatorname{rank}d\phi<n\). The compact rank reduction (N6) writes \(\phi(C)\) as a finite union of analytic images of \(T^r\). The image-dimension inequality (D5), applied to those compact torus maps in bounded charts, gives \(\dim\phi(C)\le r<n\). Thus each discarded image has empty interior. The images of the retained components form a compact, hence closed, set containing the dense complement in \(Q\) of the discarded images. They therefore cover all of \(Q\). The retained map still covers the graph, has generic rank \(n\) on every component, and \(f=g\circ\phi\) supplies (IR1).

The closed analytic set \(E_2\) in the compact fibre product has compact subanalytic image under \((a,b)\mapsto\phi(a)\), by the already proved proper-image calculus. We claim
\[
\mathcal A(g)\cap\operatorname{int}Q
=\operatorname{int}Q\setminus\phi(E_2).
\tag{IR6}
\]
If \(g\) is analytic near \(y\), its germ works at every pair above \(y\).

Conversely, suppose there is no bad pair above \(y\). Diagonal pairs show that each individual point of the fibre is graphic. Fix \(a_0\) in the fibre. Its pairs with all other points, and uniqueness of descent at \(a_0\), show that every descended germ is one common germ \(h\). Compactness of the fibre gives finitely many source neighborhoods \(W_i\) covering it on which \(f=h\circ\phi\), after choosing a common representative and shrinking its target neighborhood. The compact set \(M\setminus\bigcup_iW_i\) has closed image missing \(y\). A smaller target neighborhood \(U\subset\operatorname{int}Q\) thus has \(\phi^{-1}(U)\subset\bigcup_iW_i\). Every point of \(U\) has a preimage; there \(g=f=h\). Hence \(g\) is analytic near \(y\), proving (IR6) and subanalyticity.

The test considers every pair of points of each fibre. Neither a bound on fibre components nor a dimension bound shared with parametrizations on other target charts is needed. \(\square\)

### Squared distance recognizes an analytic submanifold

For a nonempty closed \(C\subset\mathbb R^n\), put \(q(x)=d(x,C)^2\). At \(a\in C\),
\[
q\text{ is analytic near }a
\quad\Longleftrightarrow\quad
C\text{ is an analytic submanifold near }a.
\tag{IR7}
\]

**Proof.** If \(C\) is analytic near \(a=0\), rotate coordinates so it is the graph \((u,\eta(u))\), with \(\eta(0)=0\), \(D\eta(0)=0\). The analytic normal-coordinate map
\[
(u,w)\longmapsto(u,\eta(u))+(-D\eta(u)^tw,w)
\]
has invertible derivative at zero. A nearest point to \(x\) sufficiently close to zero lies in this graph, since its distance from zero is at most \(2|x|\). Its displacement from \(x\) is normal to the graph by stationarity of squared distance. The inverse-function theorem gives a unique such point \(\pi(x)\), analytic in \(x\). Thus \(q(x)=|x-\pi(x)|^2\) is analytic.

Conversely assume \(q\) analytic near \(a\). Every first derivative of \(q\) vanishes on \(C\), since \(q\ge0\) and \(q|_C=0\). Choose an analytic submanifold \(L\) of smallest dimension containing the germ of \(C\) at \(a\); the ambient space is one candidate. If \(q|_L=0\) near \(a\), then \(C=L\) there. Otherwise choose \(x_\nu\in L\setminus C\) tending to \(a\), and nearest points \(y_\nu\in C\). Both sequences tend to \(a\) and eventually lie in \(L\). Pass to a subsequence with
\[
v_\nu=\frac{x_\nu-y_\nu}{|x_\nu-y_\nu|}\longrightarrow v\in T_aL,
\qquad |v|=1.
\]
The tangent assertion follows by expressing \(L\) as a differentiable graph and estimating the difference of two graph values by its derivative near \(a\).

On the segment from \(y_\nu\) to \(x_\nu\), distance to \(C\) equals distance to \(y_\nu\). One inequality uses \(y_\nu\in C\); the reverse follows by the triangle inequality measured from \(x_\nu\). Thus
\[
D^2q(y_\nu)[v_\nu,v_\nu]=2,
\qquad D^2q(a)[v,v]=2.
\]
The function \(x\mapsto dq_x(v)\) vanishes on \(C\) and has nonzero derivative in the tangent direction \(v\) at \(a\). Its zero hypersurface cuts \(L\) transversely, producing a smaller-dimensional analytic submanifold still containing the germ of \(C\). This contradiction proves (IR7). \(\square\)

At a regular point of local dimension \(d\), the same normal coordinates give
\[
D^2q(a)=2\,\operatorname{pr}_{(T_aC)^\perp},
\qquad \operatorname{rank}D^2q(a)=n-d.
\tag{IR8}
\]

### Every intrinsic regular point, in each dimension

Let \(S\) be subanalytic in an \(n\)-dimensional analytic manifold. Work in a relatively compact chart and close a slightly larger bounded trace of \(S\) to get a compact subanalytic set \(C\); in a smaller region \(C\) is the ambient closure of \(S\). The empty case is immediate.

The function \(q=d(\,\cdot\,,C)^2\) is continuous and globally subanalytic in these coordinates. Its graph is given by the minimum of polynomial squared distance over the compact definable set \(C\); the minimum and its equality condition are formulas with quantifiers over definable sets. Boolean and projection closure therefore give subanalyticity. The triangle inequality gives continuity. Equations (IR5)–(IR7) yield
\[
\operatorname{Reg}(C)=C\cap\mathcal A(q).
\]

On any smaller bounded working region, bounded-chart comparison makes the subanalytic open set \(\mathcal A(q)\) definable. Its Hessian entries are subanalytic. Indeed, the graph of a derivative wherever it exists is expressed by the quantified \(\varepsilon,\delta\) condition for the difference-quotient limit. Boolean and projection closure give definability; apply this twice on the analytic open set. Rank is expressed by finitely many minors. Hence
\[
\operatorname{Reg}_d(C)
=C\cap\mathcal A(q)\cap\{\operatorname{rank}D^2q=n-d\}
\tag{IR9}
\]
is subanalytic for every \(d\).

For a set that is not closed, the exact local identity is
\[
\operatorname{Reg}_d(S)
=\operatorname{Reg}_d(\overline S)
 \setminus\overline{\overline S\setminus S}.
\tag{IR10}
\]
If \(S\) agrees with a closed analytic submanifold on a neighborhood, so does its ambient closure, and missing points cannot approach the selected point. Conversely, outside the second closure in (IR10), \(S\) and \(\overline S\) agree on a neighborhood. This proves the identity. The previously proved local calculus now makes every \(\operatorname{Reg}_d(S)\), their finite union \(\operatorname{Reg}(S)\), and \(S\setminus\operatorname{Reg}(S)\) subanalytic. Regularity is relatively open in \(S\), so its complement is relatively closed.

Regular points are dense in \(S\). In any sufficiently small bounded open chart meeting \(S\), choose a finite analytic cell partition of the trace and a cell \(A\) of maximal dimension \(d\). For every other cell \(B\),
\[
A\cap\overline B\subset\overline B\setminus B.
\]
The strict frontier theorem gives dimension less than \(d\) for this intersection, since \(\dim B\le d\). These finitely many intersections cannot cover \(A\). At a point of \(A\) outside all the other cell closures, the entire set agrees locally with \(A\). An embedded analytic cell is locally closed; shrinking the neighborhood makes it a closed analytic submanifold there. This is an intrinsic regular point. Every ambient neighborhood meeting \(S\) consequently meets \(\operatorname{Reg}(S)\).

The same argument identifies cell dimension with the supremum of dimensions of regular germs. It produces a regular germ of maximal cell dimension, while a \(d\)-dimensional regular germ cannot be covered by finitely many smaller-dimensional cells, by the cell-dimension volume argument. This proves all assertions of item 2, including every fixed-dimensional part. It does not identify regularity with membership in a chosen top stratum.

### Exercise: separate graphic germs need not agree

Let \(M\) be two disjoint circles \(u^2+v^2=1\), and define
\[
(\phi_+,f_+)(u,v)=(u^2,u^2),\qquad
(\phi_-,f_-)(u,v)=(-u^2,u^2).
\]
Their union parametrizes the compact graph of \(g(x)=|x|\), \(-1\le x\le1\). Show that every source point is graphic, while the target germ at zero is not analytic.

**Solution.** On the positive circle the descended germ is \(h_+(x)=x\); on the negative circle it is \(h_-(x)=-x\). The identities hold even where \(d\phi_\pm=0\), so the one-point obstruction is empty. At zero a pair with one point from each circle cannot share one descended germ: uniqueness would require \(x=-x\) as germs. Thus the two-point obstruction has an image at zero. The one-sided derivatives of \(g\) there are \(1\) and \(-1\). Equality of fibre values alone misses this disagreement of germs.

<p class="figure"><img src="figures/SH03-graphic-pair-obstruction.svg" alt="Two circle parametrizations of the graph of absolute value: separate analytic germs x and minus x disagree over zero." /></p>

The two maps in the exercise are analytic on their full source circles. The purple points all lie over zero; a pair from opposite circles has the same function value but no common analytic germ. This is the distinction tested by (IR3)–(IR6). Full-size diagram · Reproducible Python source.

## Compatible locally finite analytic partitions

The finite analytic cell theorem, its Boolean and projection calculus, and its bounded-chart comparison give the following manifold partition. The compact chart-ball refinement is proved below in [Section 2 of the cutoff construction](#a-countable-locally-finite-nested-coordinate-ball-refinement). These are the exact inputs; no analytic regular-locus theorem or uniformization theorem is needed for this partition.

**Partition theorem.** Let \(M\) be a finite-dimensional Hausdorff second-countable real analytic manifold without boundary, and let \(\{A_a\}_{a\in I}\) be a locally finite family of locally subanalytic subsets. There is a countable locally finite partition of \(M\) into connected locally subanalytic embedded analytic submanifolds compatible with every \(A_a\): each partition member is contained in or disjoint from each \(A_a\). Given finitely many analytic maps \(f_j:M\to N_j\) to real analytic manifolds, the partition can also make every restriction \(f_j|_S\) have constant rank.

### Compact chart pieces and compatibility

The compact exhaustion and shell construction in the linked cutoff proof supplies a countable cover by open coordinate balls \(B_i\) with compact closures \(L_i=\overline{B_i}\) contained in analytic charts; the family of these closures is locally finite. For instance, use the inner balls in that construction: their closures are contained in its locally finite outer compact balls. Each ball and its closure is locally semianalytic. In its chart it has a squared-norm inequality, and outside its compact closure it is empty on a neighborhood. The exhaustion sets need not be subanalytic; only the selected balls enter the partition.

For the map assertion apply this refinement to the open cover consisting of intersections of a source chart and inverse images of target charts for the finitely many \(f_j\). Thus each \(L_i\) lies in one source chart, and every \(f_j(L_i)\) lies in one selected target chart. The source and target coordinate images of these compact sets are bounded. The maps in these coordinates are analytic on a neighborhood of \(L_i\).

Every compact set meets only finitely many members of a locally finite family. Indeed, cover the compact set by finitely many neighborhoods, each meeting finitely many family members; combine their finite lists. In particular \(L_i\) meets only finitely many \(L_k\) and finitely many nonempty \(A_a\).

Enumerate the balls and put

\[
E_i=B_i\setminus\bigcup_{k<i}B_k.
\tag{P1}
\]

These sets are disjoint and cover \(M\), because each point has a first containing ball. For fixed \(i\) the earlier union is finite; its trace near \(L_i\) uses only the finitely many earlier closures that meet a sufficiently small neighborhood of \(L_i\). To justify that neighborhood, first take a finite cover of \(L_i\) by neighborhoods meeting only finitely many closures, then discard the finitely many closures missing \(L_i\) by shrinking around that compact set. Thus \(E_i\) is a finite Boolean combination of locally semianalytic balls near \(L_i\). The local Boolean calculus also makes every relevant \(A_a\cap E_i\) locally subanalytic there.

In the chosen source coordinates, these traces are bounded and locally subanalytic at every point of their ambient closures. Their closures lie inside the compact coordinate image of \(L_i\), strictly inside the source chart. Extension by the empty set therefore creates no chart-boundary obstruction. The proved bounded-chart comparison makes \(E_i\) and all the finitely many relevant \(A_a\cap E_i\) globally subanalytic in this Euclidean space.

Apply the finite analytic cell theorem compatibly with these sets, and keep just the cells in \(E_i\). Each kept cell is a connected embedded analytic submanifold. Its global subanalyticity gives local subanalyticity in the source chart, including at points of its closure; compact containment gives local emptiness outside that chart. It is therefore locally subanalytic in \(M\). It lies in or misses every \(A_a\), including those whose trace on \(L_i\) is empty.

There are finitely many kept cells for each \(i\), and each is contained in \(L_i\). A neighborhood meeting only finitely many \(L_i\) consequently meets only finitely many kept cells. They give a countable locally finite partition of \(M\). This proves the first assertion. It uses local finiteness of the compact closures; a merely countable atlas does not supply that conclusion.

### Analytic coordinates on a cell

We spell out the cell coordinates needed for rank refinement. A cylindrical analytic cell \(C\) of dimension \(d\) has a coordinate projection \(q:C\to V\) which is a definable analytic diffeomorphism onto an open definable \(V\subset\mathbb R^d\). Keep precisely its band coordinates and discard its graph coordinates.

This follows by induction through the cylindrical construction. For a graph over a cell with inverse parametrization \(\phi\), use \(u\mapsto(\phi(u),\zeta(\phi(u)))\); the old free-coordinate domain remains open. For a band over that cell, the new free domain is

\[
\{(u,t):u\in V,\ \zeta_-(\phi(u))<t<\zeta_+(\phi(u))\}.
\tag{P2}
\]

It is open because the endpoints are continuous, omitting the corresponding inequality for an infinite endpoint. Its inverse parametrization is \((u,t)\mapsto(\phi(u),t)\). These maps and their inverses are analytic. Their graphs are definable by the graph, composition and projection calculus; hence the domains are definable too. In dimension zero use the single point \(\mathbb R^0\). This proves the coordinate assertion, including the analytic embedding and its inverse, directly from the cell definition.

### Definable derivatives and restriction ranks

Fix a kept cell \(C\subset E_i\), and write \(\phi:V\to C\) for this inverse parametrization. In the chosen target coordinates the maps \(g_j=f_j\circ\phi\) are analytic and definable. To check the latter assertion, the coordinate graph of \(f_j\) over \(L_i\) is bounded and locally semianalytic at every point of its compact closure: its defining analytic equation is valid on a neighborhood of \(L_i\), and the closed coordinate ball supplies the domain condition. The bounded-chart comparison gives a globally subanalytic graph. Restriction to \(C\) and composition with \(\phi\) preserve definability.

For a scalar analytic definable \(g:V\to\mathbb R\), the derivative graph, with \(u\in V\), is described by

\[
\begin{aligned}
v=\partial_\ell g(u)
\quad\Longleftrightarrow\quad
&\forall\epsilon>0\ \exists\delta>0\ \forall h\in\mathbb R,\\
&\bigl(0<|h|<\delta\ \text{and }u+he_\ell\in V\bigr)\\
&\hspace{1em}\Longrightarrow
\left|\frac{g(u+he_\ell)-g(u)}h-v\right|<\epsilon.
\end{aligned}
\tag{P3}
\]

Function values here can be written using extra real variables in the graph of \(g\); division by \(h\ne0\) is a polynomial graph condition. The formula uses finitely many real quantifiers. Existential quantification is projection, and universal quantification is complement of an existentially quantified complement. Thus the established Boolean and projection calculus makes this derivative graph definable. Openness of \(V\) supplies a nontrivial interval of allowed \(h\) at every \(u\), so the limit condition specifies the derivative uniquely. Applying this to every scalar coordinate gives definable differential matrices for all \(g_j\).

All rank sets are consequently definable: rank \(r\) means that every \((r+1)\)-minor vanishes and, when \(r>0\), some \(r\)-minor is nonzero. Rank zero means every matrix entry vanishes. Include all finitely many rank sets for the finitely many maps in a finite analytic cell decomposition of \(V\).

Every resulting \(d\)-dimensional cell \(D\subset V\) is open in \(V\). Indeed, a full-dimensional cylindrical cell has only band steps, and (P2) proves openness at every such step. Therefore \(\phi(D)\) is open in \(C\); its tangent space is that of \(C\), and every \(f_j|_{\phi(D)}\) has the constant rank selected on \(D\). Retain these members as finished.

On a smaller cell \(D\), the old differential rank is insufficient: restricting a rank-one map to one of its level curves can give rank zero. Take the cell's own free-coordinate parametrization \(\psi:W\to D\), and repeat the rank calculation for all \(g_j\circ\psi\). These are still definable analytic maps on an open definable domain. Their images under \(\phi\circ\psi\) are connected embedded analytic submanifolds and definable in the original source chart. Repeat the same finite refinement and finish its full-dimensional members.

An unfinished branch now has strictly smaller dimension. Induction on \(d\) terminates: dimension zero has rank zero for every map, and each positive-dimensional step finishes its full-dimensional cells and passes only finitely many smaller cells to already established lower-dimensional cases. The final refinement of each original \(C\) is finite. Its members remain inside \(L_i\), so refining the finitely many cells for each \(i\) preserves countability, local finiteness and compatibility with all \(A_a\). This proves simultaneous constant rank on every final member. \(\square\)

If \(M\) is compact, this locally finite partition is finite by the compactness argument above. Similarly a compact subanalytic subset contained in one analytic chart has a finite compatible analytic partition, by bounded-chart comparison and finite cells. A connected cell lies in a single connected component; hence each component of a finite union of cells is a union of whole cells. There are finitely many components. For a compact subanalytic subset meeting several charts, intersect with finitely many compact coordinate boxes whose interiors cover it, apply the same finite-cell argument in each box, and take the resulting finite union of connected cells. This proves finiteness of its connected components as well.

The theorem supplies compatible analytic partitions and constant-rank refinements for the relative triangulation construction. Whitney and Verdier conditions and a frontier condition between partition members require additional arguments. The [intrinsic analytic regular-locus theorem](#detecting-the-entire-analytic-regular-locus) is established separately above.

**Sources.** Guillaume Valette, [*On subanalytic geometry*, arXiv:2507.23622v1](https://arxiv.org/abs/2507.23622v1), §1.2, gives the graph/band cell definition and cell theorem; §2.1 gives first-order definable formulas and the definability of derivatives. The linked preparation component proves its finite-cell and Boolean/projection inputs in the stated projective product convention and retains its human credit and reuse terms. The manifold globalization, explicit derivative-limit formula, and simultaneous restriction-rank induction are written out here.

## How a compatible triangulation is assembled

The triangulation input has a useful relative form: one may adapt a fixed locally finite polyhedron while preserving every old simplex setwise. Its geometric source is [Masahiro Shiota, *Piecewise Linearization of Real Analytic Functions*](https://ems.press/journals/prims/articles/3179), Proposition 3.1 and the closed-polyhedron form 3.1′, with Lemmas 3.2–3.7 and Remark 3.8. Shiota first chooses nonsingular projections, completes the finite graph families so that projection is open, and then straightens consecutive radial branches compatibly across faces. The proof below follows those mechanisms, spelling out the finite-jet argument for exceptional directions, the cap reflection, the reciprocal interpolation heights and the treatment of collapsed branch intervals. In particular, the inner simplex is chosen after graph completion; choosing it using only the original sets would not justify the subsequent graph ordering.

The lower subanalytic prerequisites used in this construction are uniformization, the set calculus, and the following forms of the regularity and dimension calculus. A nonempty subanalytic set has lower-dimensional frontier \(\overline A\setminus A\), as proved in Dimension, fibrewise closure and the frontier. This is distinct from the topological boundary, whose dimension can equal the dimension of the set. The [compatible analytic partition theorem above](#compatible-locally-finite-analytic-partitions) proves that a locally finite family has a compatible locally finite partition into analytic submanifolds and that finitely many analytic maps have constant-rank restrictions after refinement. Compact subanalytic sets consequently have finite such partitions and finitely many connected components. These are inputs to the construction, rather than consequences of the triangulation being constructed. Analytic Noetherianity is supplied by the linked preparation proof. The [analytic coordinate theorem](#real-analytic-inverse-implicit-and-constant-rank-coordinates) gives constant-rank fibres and local analytic sections; the [finite-system estimate (LAF9)](#analytic-differential-equations) proves the uniform zero-solution uniqueness used in the jet argument.

**Relative polyhedron theorem.** Let \(K\) be a finite-dimensional locally finite linear simplicial complex with closed support in \(\mathbb R^N\). Let \(\{A_i\}\) be locally finite in the ambient space, with each \(A_i\) subanalytic and contained in \(|K|\). There are a locally finite subdivision \(K'\) and a subanalytic homeomorphism

\[
T:|K|\longrightarrow |K|
\]

such that \(T(\sigma)=\sigma\) for every old closed simplex \(\sigma\), each restriction to an open simplex of \(K'\) is an analytic diffeomorphism onto a subanalytic analytic submanifold, and every such image is contained in or disjoint from each \(A_i\). No analyticity across simplex boundaries is asserted.

We first prove the ingredients that make the induction possible.

### Choosing a point from which lines have finite intersections

Call a line singular for a set if it contains a nontrivial interval in that set. For a compact subanalytic set with no such intervals, every intersection with a line is finite: it is a compact zero-dimensional subanalytic set. For any countable collection of subanalytic sets of dimension less than \(n\), the union of their singular lines is meagre in \(\mathbb R^n\). Their singular parallel directions form a meagre subset of \(\mathbb{RP}^{n-1}\). Here, a meagre set is a countable union of nowhere dense sets.

**Proof.** A compatible analytic partition reduces the claim to countably many analytic submanifolds. A line interval in the original set contains an interval in one partition member: on a compact subinterval only finitely many members occur, and their intersections with the line are subanalytic. Work on a small open set where one such member is the zero set of an analytic function \(h\); a sum of squares of local defining functions supplies \(h\) in higher codimension.

Choose analytic coordinates for a unit direction \(v\). Put \(L=v\cdot\partial_x\) and \(g_j=L^j h\). The germ of the ascending chain of ideals \((g_0),(g_0,g_1),\ldots\) stabilizes. Thus, on a neighborhood of any specified \((x,v)\), for some \(q\),

\[
g_{q+1}=\sum_{j=0}^{q}a_j(x,v)g_j
\]

with analytic coefficients. Along \(x+tv\), the vector \((g_0,\ldots,g_q)\) satisfies a finite homogeneous linear differential system. If it is zero at \(t=0\), uniqueness makes it zero for all sufficiently small \(t\). Conversely, vanishing of \(h(x+tv)\) on an interval makes all these initial jets zero. Hence the incidence of analytic line germs in the chosen submanifold is locally an analytic set defined by finitely many jet equations. This proves local finiteness of the equations; an infinite jet intersection has not been treated as automatically analytic.

Cover this incidence by countably many relatively compact closed subanalytic pieces and uniformize each piece. On its uniformizing manifold \(W\), write the analytic incidence parameters as \(x(w),v(w)\). The map

\[
F:W\times\mathbb R\longrightarrow\mathbb R^n,
\qquad F(w,s)=x(w)+sv(w)
\]

has rank less than \(n\) for \(s\) in a neighborhood of zero: locally its image lies in the lower-dimensional analytic zero set. At a fixed \(w\), every \(n\)-rowed minor of its differential is a polynomial in \(s\), since its columns are \(dx+s\,dv\) and \(v\). Vanishing on an interval makes that polynomial identically zero. Thus \(F\) has rank less than \(n\) for every real \(s\), including values for which the line has left the original coordinate neighborhood.

Sard's theorem makes the image measure zero. Exhaust \(W\times\mathbb R\) by countably many compact sets. Each compact image is closed, has empty interior and is nowhere dense. This proves the assertion about all points on singular lines.

For directions, suppose \(w\mapsto[v(w)]\) had surjective differential somewhere. A local analytic section over an open direction chart would give \(x=x(v)\). For the resulting map \((v,s)\mapsto x(v)+sv\), the determinant of its \(n\) differential columns has leading coefficient

\[
\det(\partial_1v,\ldots,\partial_{n-1}v,v)
\]

in its polynomial in \(s\). That coefficient is nonzero for a direction chart on the unit sphere. This contradicts the preceding rank calculation. The direction map therefore has only critical values. Sard and compact exhaustion again make its image meagre, now in projective space. In dimension one there are no line germs in a zero-dimensional set, so the assertion is immediate. Countable unions finish both claims. \(\square\)

In particular, inside any open simplex one can choose a centre outside a finite family of compact lower-dimensional sets and all their singular lines. One can also choose a parallel direction avoiding all singular directions of such a family. Baire's theorem gives the choices in any prescribed open neighborhood.

### Completing a finite-fibre set so its projection is open

For \(p:\mathbb R^d\times\mathbb R\to\mathbb R^d\), call a set projection-open when \(p\) restricted to that set is an open map. Suppose \(A\) is compact subanalytic and every vertical fibre is finite. A finite analytic partition of \(A\), compatible with a prescribed finite family of subsets, can be chosen in analytic graph pieces.

**Proof of the graph assertion.** Refine an analytic partition by the rank of \(p\). A constant-rank restriction cannot have rank smaller than the dimension of its partition member: the constant-rank theorem would give a positive-dimensional subset of a fibre. Remove the images of lower-dimensional pieces and frontiers, and partition the remaining image into connected analytic pieces. Over each such piece, compactness supplies a proper finite analytic covering. Its sheets have a canonical order in the last real coordinate. Following the first, second and subsequent values trivializes the covering, so each sheet is an analytic graph. Apply the same argument to the remaining lower-dimensional compact part. Dimension decreases strictly, and compactness gives finitely many pieces at every step. This yields the claimed finite graph partition. The properness used here is that of the projection on the compact closed set, including its frontier. \(\square\)

There is a compact finite-fibre subanalytic enlargement \(B\supset A\) that is projection-open near a specified point of \(A\).

**Proof by induction on \(d\).** The case \(d=0\) is immediate. Separate the \(d\)-dimensional graph pieces, whose projection is open, from a closed compact remainder \(A_2\) of dimension less than \(d\). Choose a parallel direction in the base that is nonsingular for \(p(A_2)\), by the preceding lemma, and take it as the last base coordinate. For fixed \(x'\in\mathbb R^{d-1}\), only finitely many base points \((x',x_d)\) occur in \(p(A_2)\). Each has only finitely many heights. Thus the image of \(A_2\) under

\[
p_2(x',x_d,y)=(x',y)
\]

has finite vertical fibres. Enlarge that compact image, by induction, to a set \(B_2\subset\mathbb R^{d-1}\times\mathbb R\) whose projection is open near the specified point. Pull it back by \(p_2\) and intersect with a sufficiently large closed ball. Near the specified point the ball has no effect. The resulting \(B'\) has finite vertical fibres and is projection-open; its projection has the free \(x_d\)-coordinate. It contains \(A_2\). Therefore \(A\cup B'\) is projection-open there: points of the remainder lie in the projection-open enlargement, while the other pieces already have open projection. This completes the induction. \(\square\)

The same statements hold for radial projection from a centre \(a\), using polar coordinates away from \(a\). A local enlargement near \(b\ne a\) can be turned into a compact one that is projection-open everywhere without losing local membership data. Here is the boundary step. Rotate and scale so \(a=0\), \(b=(0,\ldots,0,1)\). Intersect the local enlargement with a narrow conical neighborhood and a radial band about radius one. Choose the band endpoints to avoid its finite fibre over \(b/|b|\); narrow the cone so no points meet those radial endpoints. Its only boundary is then on the side of the cone. Reflect the spherical cap across its boundary sphere, leaving radial distance unchanged, and adjoin the reflected copy.

For completeness, such a reflection is analytic. Write a unit vector as \((v',v_n)\), let the cap boundary be \(v_n=c\in(0,1)\), and put \(k=(1-c)/(1+c)>0\). The formula

\[
J(v',v_n)=\left(
\frac{2k\,v'}{1-v_n+k^2(1+v_n)},
\frac{1-v_n-k^2(1+v_n)}{1-v_n+k^2(1+v_n)}
\right)
\]

is an analytic involution of the sphere. Its denominator is positive; in stereographic coordinates it is inversion in the sphere of radius \(\sqrt{k}\). It fixes the cap boundary pointwise and exchanges its two sides. Near the common boundary, relative openness on the cap and its reflected copy gives openness in the whole sphere. The doubled compact set still has finite radial fibres. Partition it into graph pieces, also respecting its intersection with the original set and the cap boundary. Near \(b\), the original set is a union of these pieces. In dimension one radial directions form two points, and no cap construction is needed.

### Extending the skeleton without changing old simplices

We prove the relative theorem by induction on \(m=\dim K\). The assertion for \(m=0\) is immediate. Suppose it is proved in lower dimensions.

First reduce membership to closed sets. For a subanalytic \(A\) in a compact old simplex, put \(B_0=A\), \(B_{j+1}=\overline{B_j}\setminus B_j\). The strict frontier inequality (D12) in the linked dimension provider makes this sequence terminate when the first empty set is reached. Membership in \(A\) is a Boolean combination of the finitely many closed sets \(\overline{B_j}\), obtained by substituting \(B_j=\overline{B_j}\setminus B_{j+1}\) backwards. For a full-dimensional closed set, its boundary is lower-dimensional; a connected piece avoiding that boundary lies wholly in its interior or wholly outside it. Thus lower-dimensional closed obstacles, and the membership information on the old skeleton, suffice. Each compact old simplex meets only finitely many \(A_i\), so these local reductions preserve ambient local finiteness.

Fix an old \(m\)-simplex \(\sigma\), and choose a nonsingular centre \(a\in\sigma^\circ\) outside its finite union of lower-dimensional closed obstacles. Such a choice is possible because that union and the excluded singular-line sets are meagre. Let \(p_a:\sigma\setminus\{a\}\to\partial\sigma\) send a point along its ray to the boundary. Each obstacle has finite radial fibres. At each of its points use the preceding compact radial completion, with an analytic graph partition that records its local membership. Finitely many such neighborhoods cover the compact obstacles.

Let \(C\) be the finite union of all the completed compact sets. Every completion was constructed away from \(a\), so \(C\) is compact and avoids \(a\). Choose \(0<\delta<1\) only now, small enough that the closed inner simplex \(a+\delta(\sigma-a)\) is disjoint from \(C\). Explicitly, if \(C\ne\varnothing\), take \(\delta R<\operatorname{dist}(a,C)\), where \(R=\max_{x\in\sigma}|x-a|>0\); compactness makes the distance positive. If \(C\) is empty, any \(\delta\in(0,1)\) suffices. Avoiding only the original obstacles would not ensure this property, because their completions can approach the centre more closely. Clip \(C\) to \(\sigma\), then add both \(\partial\sigma\) and the inner boundary \(a+\delta(\partial\sigma-a)\). Call the resulting compact set \(\Gamma\). All completed points in it have radial height strictly greater than \(\delta\), so the adjoined inner boundary is the least radial branch and the open inner simplex contains no other part of \(\Gamma\). It has finite radial fibres and open radial projection. Clipping does not spoil openness at an outer or inner boundary: the full boundary graph itself supplies the missing neighboring fibres.

Refine its finite graph partition to respect the partitions of every completion. Any connected piece compatible with this refinement is compatible with each original closed obstacle. Indeed, its intersection with that obstacle is closed. At an intersection point, a chosen completion neighborhood makes membership locally constant on the piece, so the intersection is also open. Connectedness makes it either the entire piece or empty.

Project all graph pieces and their relevant frontiers to the old skeleton, and include the original membership data on that skeleton. The images are subanalytic by properness on compact closures. The resulting family is locally finite: its members from \(\sigma\) remain on \(\partial\sigma\), and the old complex is locally finite. The induction hypothesis supplies a subdivision \(H\) of the skeleton and a homeomorphism \(\tau\) that fixes every old face setwise, is analytic on each new open simplex, and respects this projected data.

### Ordered branches, including their values on faces

Over an open base simplex \(\eta\) of \(H\), after the boundary map \(\tau\), the graph pieces of \(\Gamma\) give finitely many strictly ordered positive radial functions

\[
\delta=r_0(u)<r_1(u)<\cdots<r_s(u)=1,
\qquad u\in\eta^\circ,
\]

where the actual point on a branch is \(a+r_i(u)(\tau(u)-a)\). The functions are analytic on the open simplex. The boundary partition ensures that each branch either occurs on the entire base simplex or is absent there.

Each branch extends continuously to the closed base simplex. To see this at a boundary point \(u_0\), intersect the open simplex with successively smaller balls centred at \(u_0\). These intersections are connected. The closures of their branch graphs are nested compact connected sets. Their intersection is the cluster set over \(\tau(u_0)\), and is finite because \(\Gamma\) has finite fibres. A nonempty finite connected set has one point. This gives a unique limiting value. The same argument at every boundary point, together with compactness, proves continuity of the extension.

On an open face, the limit is one of its finitely many graph branches. Its choice is locally constant, hence constant on the connected face. Consecutive branches upstairs restrict either to the same branch or to consecutive branches on a face. Otherwise a third branch strictly between their two limiting values would, by open projection, have nearby values over the interior base simplex. Those values would lie between the original consecutive branches, a contradiction. This is precisely where openness of the completed projection is needed.

Take a barycentric subdivision of \(H\). If two branches are distinct on an open base simplex, one vertex of each new simplex is the barycentre of its largest old carrier and lies in that carrier's interior. Their values are strictly ordered at that vertex. They may agree at other vertices on lower faces; this causes a permitted collapse on that face, not a collapsed interior cell.

### The straight model and its analytic lifting map

Let \(u_0,\ldots,u_d\) be the vertices of one of the subdivided base simplices, with barycentric coordinates \(\lambda_j(u)\). Model branch \(i\) by the straight simplex with vertices

\[
a+r_i(u_j)(u_j-a).
\]

Its radial height over \(u\) is

\[
R_i(u)=\left(\sum_{j=0}^{d}\frac{\lambda_j(u)}{r_i(u_j)}\right)^{-1}.
\]

This is reciprocal, rather than arithmetic, interpolation. Indeed, if a point in the straight face has affine coefficients \(\mu_j\), radial projection gives \(\lambda_j=\mu_jr_i(u_j)/t\). The condition \(\sum\mu_j=1\) then gives the displayed height \(t=R_i(u)\). All vertex heights are positive. The strict order at an interior-carrier vertex makes \(R_i<R_{i+1}\) throughout each open base simplex.

Between two consecutive straight faces, define

\
T\bigl(a+t(u-a)\bigr)
=a+\left[
r_i(u)+\frac{t-R_i(u)}{R_{i+1}(u)-R_i(u)}
\bigl(r_{i+1}(u)-r_i(u)\bigr)
\right-a).
\]

On a straight branch use its endpoint value, and inside the inner simplex use the conical extension \(a+t(u-a)\mapsto a+t(\tau(u)-a)\), including \(a\mapsto a\). The annular map is strictly increasing on each radial interval. On every open annular cell it is analytic with an analytic inverse: \(\tau\) and the branch functions are analytic there, radial projection is analytic on each old open face, and the radial derivative is

\[
\frac{r_{i+1}(u)-r_i(u)}{R_{i+1}(u)-R_i(u)}>0.
\]

The maps agree on their common boundaries. If the two branches collapse on a lower face, every interpolated value lies between them, so continuity of their common limit supplies continuity there. There is no division by zero on an open annular cell. At the centre, the factor \(t\) supplies continuity of the conical map. Thus \(T\) is a homeomorphism of \(\sigma\), agrees with \(\tau\) on its boundary, and takes straight branch faces and cells between them to the prescribed analytic branches and bands.

The straight faces and the closed regions between consecutive faces form a finite polyhedral cell complex. Over a fixed base face, their defining inequalities are the linear half-space inequalities of the two branch hyperplanes inside the cone over that face. The face restriction and consecutive-or-collapsed property just proved makes intersections common faces. A barycentric subdivision turns this into a simplicial subdivision. On every open simplex the restriction of the preceding analytic cell map is an analytic embedding, hence an analytic diffeomorphism onto its image.

The graph is subanalytic. On compact branch faces this follows from the subanalytic graph functions and \(\tau\). For interpolation between two faces, take the closed subanalytic graph of the two endpoint maps over the same base ray, multiply by the compact parameter interval \([0,1]\), and apply the analytic affine interpolation map to both its input and output coordinates. Its domain is compact, so this is a proper-image argument. The conical extension has the same compact graph construction, with the centre included. This avoids assuming that arbitrary nonproper compositions or images are subanalytic.

Do this on each old top simplex. The maps coincide on the skeleton, so they glue. Each map preserves its old simplex setwise. Local finiteness therefore gives a global homeomorphism, subanalytic graph and locally finite subdivision, with no accumulation of new cells in a compact neighborhood. Compatibility follows from the completed graph partition and the connected-piece argument. This proves the relative polyhedron theorem. \(\square\)

### Relative support and a continuous isotopy

The construction can preserve a region that already needs no change. Let \(L\) be a subcomplex of \(K\), and suppose every old open simplex outside \(L\) is already compatible with the family. All interior membership obstacles then lie in \(|L|\). Their projected data stay in \(|L|\), since every face of a simplex of \(L\) belongs to \(L\). Inductively retain the old simplices disjoint from \(|L|\) and use the identity there. On a top simplex outside \(L\), the only remaining operation is conical extension of its already chosen boundary map. It is the identity when that closed simplex is disjoint from \(|L|\). Thus the final subdivision retains those disjoint simplices and \(T\) fixes them pointwise. This is the relative support refinement, not a claim that the map must fix every simplex merely absent from \(L\).

There is also a subanalytic isotopy from the identity to \(T\), preserving every old simplex setwise and stationary on those unchanged regions. Prove it with the same skeleton induction. Suppose \(\tau_s\), \(0\le s\le1\), is the boundary isotopy. On an old top simplex let \(C_{\tau_s}\) be its conical extension. Put \(D=C_{\tau_1}^{-1}T\). This is an increasing homeomorphism on each radial fibre, fixes the outer boundary, and has the form

\[
D(a+t(u-a))=a+q(u,t)(u-a).
\]

Interpolate its radial coordinate by \(q_s(u,t)=(1-s)t+s\,q(u,t)\). Both summands are increasing, so \(q_s\) is strictly increasing, has the same endpoints and gives a fibre homeomorphism \(D_s\). Define \(T_s=C_{\tau_s}D_s\). Then \(T_0=\mathrm{id}\), \(T_1=T\), and its boundary restriction is \(\tau_s\). The formulas are continuous, including collapsed face intervals and the centre by the endpoint arguments above. On the compact old simplex, a continuous family of these bijections has a continuous family of inverses: the map \((x,s)\mapsto(T_s(x),s)\) is a continuous bijection from a compact space to a Hausdorff space. Its graph is subanalytic by the same compact interpolation constructions. Local finiteness glues the family over all old simplices. This proves the asserted subanalytic isotopy; no global analyticity across cells is implied.

<img src="figures/radial-triangulation-lift.svg" alt="Straight radial faces and their analytic target branches" style="display:block;width:100%;max-width:680px;height:auto;margin:1rem auto;">

*An exact two-dimensional instance.* The centre is \(a=(0,0)\), the outer base is \((u,1)\), \(-1\le u\le1\), and the target radial heights are \(r_1(u)=1/3+u^2/6\), \(r_2(u)=2/3+u^2/6\). Subdivide the base at \(u=0\). The corresponding straight-face heights are \(R_1(u)=1/(3-|u|)\), \(R_2(u)=10/(15-3|u|)\). The displayed lifting map is affine along each ray between the two straight faces. Curves are shown through their stated exact parametrizations; the picture is a sampled illustration, not a substitute for the proof.

For the original manifold input, this proves the global Euclidean relative construction and its restriction to a closed subanalytic subset. The complete globalization to an arbitrary real analytic manifold is proved below through finite-colour chart blocks, differentiable subanalytic cutoffs and analytic coordinate recovery on open simplices. The lower subanalytic prerequisites stated at the start of the relative construction remain explicit.

## The signed normal-cone prerequisite

For a closed analytic submanifold \(M\subset X\), the normal deformation \(\mathcal D_MX\) has central fibre \(N_MX=(TX|_M)/TM\), a parameter \(s\), and a map \(p:\mathcal D_MX\to X\). In adapted coordinates \((u,z)\), with \(M=\{u=0\}\), its maps are

\[
p(v,z,s)=(sv,z),\qquad s(v,z,s)=s.
\tag{3}
\]

Put \(\Omega=\{s>0\}\). For any subset \(A\subset X\), its normal cone is

\[
C_M(A)=N_MX\cap\overline{p^{-1}(A)\cap\Omega}.
\tag{4}
\]

The closure is taken in the deformation manifold. For locally closed \(M\), make this definition in an open ambient neighborhood where \(M\) is closed. The normal-geometry locality comparison makes it independent of that choice.

For two subsets, the diagonal construction gives

\[
C(A,B)=C_\Delta(A\times B)\subset TX,
\qquad [(v,w)]\longmapsto v-w.
\tag{5}
\]

Thus the first member of the pair contributes with a plus sign. In a coordinate chart, the exact sequence criterion is

\[
(x;v)\in C(A,B)
\iff
\begin{cases}
a_j\in A,\ b_j\in B,\quad a_j,b_j\to x,\\
c_j>0,\quad c_j\to\infty,\quad c_j(a_j-b_j)\to v.
\end{cases}
\tag{6}
\]

For \(C_x(A):=C_{\{x\}}(A)\), take \(b_j=x\). The scale tending to infinity is also valid at the zero vector; it is part of the prerequisite criterion. Exchanging the two sets in (5) negates the cone. These are positive-conic sets, with no assumption that they are vector subspaces or convex.

**Normal-cone subanalyticity.** If \(A\) is subanalytic and \(M\) is an analytic submanifold, then \(C_M(A)\) is subanalytic. If \(A,B\) are subanalytic, then \(C(A,B)\) is subanalytic.

**Proof.** The maps in (3) are analytic. The lifted set \(p^{-1}(A)\cap\{s>0\}\) is therefore subanalytic. Its closure and intersection with the analytic central fibre remain subanalytic by the set-operation input. For pairs, apply this argument to the diagonal and \(A\times B\); the latter is subanalytic by analytic inverse images and intersection. All assertions are local, so the same proof covers a locally closed \(M\). No image of a nonproper projection was used. \(\square\)

## A curve that represents the exact limiting vector

**Curve realization.** Let \(A,B\subset\mathbb R^n\) be subanalytic and \(v\in C_x(A,B)\). There are analytic curve germs \(a(t),b(t)\), both equal to \(x\) at zero, lying respectively in \(A,B\) for nonzero \(t\), such that

\[
a(t)-b(t)=t^k v+O(t^{k+1})
\quad\text{for some integer }k>0.
\tag{7}
\]

The coefficient of \(v\) in (7) is exactly one.

**Proof.** In \(\mathbb R^n_a\times\mathbb R^n_y\times\mathbb R_s\), consider

\[
D=\{(a,y,s):s>0,\ a\in A,\ a-sy\in B\}.
\tag{8}
\]

This is subanalytic by analytic inverse images and intersection. Criterion (6), with \(s_j=c_j^{-1}\) and \(y_j=c_j(a_j-b_j)\), says that \((x,v,0)\in\overline D\). Curve selection gives analytic \(a(t),y(t),s(t)\) through that point and in \(D\) for \(t\ne0\). Set \(b(t)=a(t)-s(t)y(t)\). Both required set memberships hold, and \(b(0)=x\).

The analytic function \(s\) is positive on both sides of zero and vanishes at zero. Hence

\[
s(t)=t^k h(t),\qquad k\ge2\text{ even},\quad h(0)>0.
\tag{9}
\]

Choose the positive analytic \(k\)-th root of \(h\) near zero and put \(u=t\,h(t)^{1/k}\). Its derivative at zero is positive, so it has an analytic local inverse \(t=t(u)\). After this reparametrization, \(s(t(u))=u^k\) and \(y(t(u))=v+O(u)\). The difference is therefore \(u^k v+O(u^{k+1})\), which is (7) after renaming the parameter. This also works for \(v=0\). The even exponent is a consequence of this particular two-sided construction; the theorem only needs a positive integer.

If curves on \((-1,1)\) are desired, choose a small interval \((-\varepsilon,\varepsilon)\) on which the germs are defined and compose them with \(t\mapsto\varepsilon\tanh(t/\varepsilon)\). This map takes \((-1,1)\) into that interval and has Taylor expansion \(t+O(t^3)\), so the coefficient and order in (7) are preserved. \(\square\)

The rescaling in (9) matters. Without it, a selected curve initially gives \(c\,t^k v\), with \(c=h(0)>0\), and only a positive multiple of the specified leading vector has been normalized.

## One-forms on a singular set

For an analytic one-form \(\theta\) on \(X\), define \(\theta|_S=0\) to mean that its pullback to the analytic manifold \(S_{\mathrm{reg}}\) is zero. This restriction is on tangent vectors, rather than the assertion that the ambient covector \(\theta_x\) itself is zero.

**Cone test.** For a subanalytic set \(S\),

\[
\theta|_S=0
\iff
\theta_x(v)=0
\text{ for every }x\in X\text{ and }v\in C_x(S).
\tag{10}
\]

This includes points in \(\overline S\setminus S\).

**Proof.** First we verify a density statement with its scales intact:

\[
C_x(S)=C_x(S_{\mathrm{reg}}).
\tag{11}
\]

One inclusion follows from \(S_{\mathrm{reg}}\subset S\). For the other, use a sequence \(z_j\in S\) and scales \(c_j\to\infty\) representing a cone vector. Density of \(S_{\mathrm{reg}}\) in \(S\) lets us choose \(w_j\in S_{\mathrm{reg}}\) with \(\|w_j-z_j\|<1/(j c_j)\), in a fixed local chart for large \(j\). Then \(w_j\to x\) and \(c_j(w_j-x)-c_j(z_j-x)\to0\). This proves (11).

Suppose \(\theta|_S=0\) and \(v\ne0\) belongs to \(C_x(S)\). Apply (7) to \(S_{\mathrm{reg}}\) and \(\{x\}\), using (11). We obtain

\[
a(t)=x+t^k v+O(t^{k+1}),\qquad a(t)\in S_{\mathrm{reg}}\quad(t\ne0).
\tag{12}
\]

At nonzero parameter the curve is tangent to \(S_{\mathrm{reg}}\). Consequently \(\theta_{a(t)}(\dot a(t))=0\). Analytic Taylor expansion gives

\[
0=k t^{k-1}\theta_x(v)+O(t^k).
\tag{13}
\]

Divide by \(t^{k-1}\) and let \(t\to0\). The integer \(k\) is nonzero, so \(\theta_x(v)=0\). The zero vector is automatic, and empty cone fibres make no demands.

Conversely, at a regular point \(x\), every tangent vector to \(S_{\mathrm{reg}}\) belongs to \(C_x(S)\): realize it by a smooth local curve and apply (6). Thus the right side of (10) kills every such tangent vector, which is the left side. \(\square\)

For example, on the parabola \(S=\{(u,v):v=u^2\}\), the nonzero ambient form \(dv-2u\,du\) vanishes on \(S\). At the origin its value is \(dv\), which kills the horizontal tangent cone. Vanishing on a set is consequently weaker than vanishing as a section of the ambient cotangent bundle.

## Analytic maps and locally finite unions

**Pullback and union rules.** Let \(h:X'\to X\) be analytic and let \(S'\subset X'\), \(S\subset X\) be subanalytic with \(h(S')\subset S\). Then

\[
\theta|_S=0\quad\Longrightarrow\quad(h^*\theta)|_{S'}=0.
\tag{14}
\]

If \(\{S_i\}\) is locally finite and subanalytic, then vanishing on every \(S_i\) implies vanishing on \(\bigcup_iS_i\).

**Proof.** For \(v\in C_{x'}(S')\), take a sequence \(z_j\to x'\) and scales \(c_j\to\infty\) representing it. Taylor expansion at \(x'\) gives

\[
c_j\bigl(h(z_j)-h(x')\bigr)
\longrightarrow dh_{x'}v.
\tag{15}
\]

Indeed, \(c_j\|z_j-x'\|\) is bounded, so multiplying the first-order remainder \(o(\|z_j-x'\|)\) by \(c_j\) makes it tend to zero. Therefore \(dh_{x'}v\in C_{h(x')}(S)\). The cone test yields \((h^*\theta)_{x'}(v)=\theta_{h(x')}(dh_{x'}v)=0\), proving (14).

Near a fixed point, a locally finite union has only finitely many members. Its point-normal cone is the union of their point-normal cones, because closure commutes with a finite union in (4). Apply (10) to each member and then to the subanalytic union. \(\square\)

In particular, vanishing passes to every subanalytic subset of \(S\), even a subset contained in its singular locus. This follows by taking \(h\) to be the identity and \(S'\subset S\).

Vanishing also passes to the closure. Here is the approximation argument, since uniformization applies to a closed set. For every ambient point \(x\),

\[
C_x(S)=C_x(\overline S).
\]

The inclusion from left to right is immediate. For the reverse, represent a vector by \(z_j\in\overline S\), scales \(c_j\to\infty\), and \(c_j(z_j-x)\to v\). Choose \(w_j\in S\) with \(\|w_j-z_j\|<1/(j c_j)\). Then \(w_j\to x\) and \(c_j(w_j-x)\to v\). Both sets are subanalytic, so the cone test proves
\(\theta|_S=0\) if and only if \(\theta|_{\overline S}=0\).
This uses approximation at the chosen scales; density alone without that estimate would not identify the cones.

The reverse direction needs surjectivity onto the set, but does not need an everywhere surjective differential.

**Surjective detection.** Under the same assumptions, if \(h(S')=S\), then

\[
\theta|_S=0\quad\Longleftrightarrow\quad(h^*\theta)|_{S'}=0.
\tag{16}
\]

**Proof.** Only detection remains. Set \(T=\overline{S'}\). The closure argument just proved gives \((h^*\theta)|_T=0\). Choose a proper analytic uniformization \(\pi:W\to X'\) with image \(T\). The manifold \(W\), like our other manifolds, is Hausdorff and countable at infinity. By (14), \((h\pi)^*\theta=0\) on \(W\).

Fix a regular point of \(S\) and a neighborhood \(V\) in which \(S\cap V\) is a closed analytic manifold \(N\), of dimension \(d\). Shrink within that neighborhood if necessary. Then \(\overline S\cap V=N\): taking closure introduces no new point inside a neighborhood where the set is already closed. Continuity gives \(h(T)\subset\overline S\), whereas \(h(S')=S\) implies that \(h(T)\) contains \(S\). Consequently the following map is analytic and surjective:

\[
g:(h\pi)^{-1}(V)\longrightarrow N,
\qquad g=h\pi.
\tag{17}
\]

The open source manifold has a countable atlas. The classical Sard theorem therefore makes its critical values a measure-zero subset in each chart of \(N\). Surjectivity implies that a dense set of points \(y\in N\) has a lift \(z\) with \(dg_z\) onto \(T_yN\). At such a point, every \(w\in T_yN\) has a tangent lift \(v\), and

\[
\theta_y(w)=(g^*\theta)_z(v)=0.
\tag{18}
\]

Continuity makes \(\theta|_N\) zero everywhere. When \(d=0\) the conclusion already holds, since tangent spaces are zero. This works near every regular point of \(S\), proving (16). The differential-topology inputs are Sard and the usual submersion criterion. Properness is used for the available uniformization, not imposed on \(h\); we never assert that a nonproper analytic image is subanalytic. \(\square\)

## Generalized conormals retain limiting normal covectors

For a locally closed subanalytic \(S\subset X\), define

\[
T_S^*X
=\overline{T_{S_{\mathrm{reg}}}^*X}\cap\pi^{-1}(S),
\qquad \pi:T^*X\to X.
\tag{19}
\]

The ordinary conormal on the right kills the tangent space of the regular locus. Its closure retains limiting covectors, while the last intersection restricts their base points back to \(S\). Formula (19) need not give the annihilator of \(C_x(S)\) at a singular point.

**Generalized-conormal subanalyticity.** The set \(T_S^*X\) is subanalytic.

**Proof.** Work in an ambient open set where \(S\) is closed, and choose a proper uniformization \(f:Y\to X\) with image \(S\). Let

\[
Y_0=\{y\in f^{-1}(S_{\mathrm{reg}}):
df_y:T_yY\to T_{f(y)}S_{\mathrm{reg}}
\text{ is onto}\},\qquad S_0=f(Y_0).
\tag{20}
\]

Here \(Y_0\) is subanalytic. For each possible dimension \(d\) of the regular locus, intersect its inverse image with \(\{\operatorname{rank}df=d\}\). The regular dimension parts are subanalytic, and the rank conditions are semianalytic minors. Near a point mapping to the regular locus, the image of \(df\) is tangent to that locus, so rank \(d\) is exactly the surjectivity in (20).

The set \(Y_0\) is open in \(Y\), because \(S_{\mathrm{reg}}\) is open in \(S\) and surjectivity is open over a fixed-dimensional manifold. Properness of \(f\) implies properness on \(\overline{Y_0}\), so \(S_0\) is subanalytic. The submersion theorem makes \(S_0\) open in \(S_{\mathrm{reg}}\). It is dense there: over any regular neighborhood, \(f\) is a surjective analytic map onto that neighborhood, and Sard shows that regular values are dense. Thus \(S_0\) is also dense in \(S\).

Use the typed cotangent correspondence

\[
C=Y\times_XT^*X,
\qquad f_\pi:C\to T^*X,
\qquad f_d:C\to T^*Y,
\quad f_d(y;\xi)=df_y^t\xi.
\tag{21}
\]

The first map is a base change of the proper map \(f\); hence it is proper on all of \(C\). Let \(\dot T^*Y_0\) denote the nonzero covectors over \(Y_0\), as a subanalytic subset of \(T^*Y\), and set

\[
P=T^*X\setminus f_\pi\bigl(f_d^{-1}(\dot T^*Y_0)\bigr).
\tag{22}
\]

Analytic inverse image, proper image and difference prove that \(P\) is subanalytic. Explicitly, \((x;\xi)\in P\) means that \(df_y^t\xi=0\) for every \(y\in Y_0\cap f^{-1}(x)\). Over \(S_0\) at least one such lift exists and every such differential is onto \(T_xS_{\mathrm{reg}}\). Consequently

\[
P\cap\pi^{-1}(S_0)=T_{S_0}^*X.
\tag{23}
\]

The two conormal bundles over \(S_0\) and \(S_{\mathrm{reg}}\) have the same closure. To see the nontrivial inclusion, choose local conormal-bundle coordinates around a regular point, approximate its base point by points of the dense open \(S_0\), and keep the normal-fibre coordinates fixed. Every regular conormal covector is then a limit from \(T_{S_0}^*X\). Taking closure in (23) and intersecting with \(\pi^{-1}(S)\) proves (19) subanalytic. The normal-cone arguments earlier supplied a different construction; no equality between these two kinds of cone was assumed. \(\square\)

At the crossing \(S=\{uv=0\}\subset\mathbb R^2\), the generalized-conormal fibre at the origin is the union of the two covector axes. The point-normal cone is the union of the two tangent axes; the covectors annihilating *all* of it consist only of zero. These two answers encode different questions. A subsequent stratification includes the origin as its own stratum, whose ordinary conormal is the entire cotangent fibre.

## Exercises with solutions

### Two notions of a normal covector

*Difficulty: Intermediate.*

Compute \((T_S^*\mathbb R^2)_0\) and the annihilator of \(C_0(S)\) for \(S=\{uv=0\}\). Then compute \(T_A^*\mathbb R\) for \(A=[0,\infty)\). Compare its fibre at zero with the conormal of the point stratum.

**Solution.** Away from zero, the horizontal axis has conormal \(\xi=0\), and the vertical axis has conormal \(\eta=0\), where a covector is \(\xi\,du+\eta\,dv\). Their closures give \(\{\xi=0\}\cup\{\eta=0\}\) at zero. Every scaled displacement in \(S\) lies on a tangent axis, and every vector on either axis is attained. Thus \(C_0(S)\) is their union. A covector killing both axes has \(\xi=\eta=0\).

For \(A\), the regular locus is \((0,\infty)\), whose conormal is the zero covector. Its closure, restricted to \(A\), is the zero section over \([0,\infty)\). In particular, (19) gives only zero at the endpoint. The conormal of \(\{0\}\subset\mathbb R\) is the whole one-dimensional fibre. The stratified conormal union therefore contains more endpoint covectors than the generalized conormal of the entire half-line.

### A two-sided curve in a one-sided cone

*Difficulty: Introductory.*

Let \(A=(0,\infty)\subset\mathbb R\). Compute \(C_0(A)\). For every \(v>0\), give an analytic curve in \(A\) for both signs of its nonzero parameter with leading coefficient \(v\). Explain why a nonzero first-order term cannot work.

**Solution.** Positive scales of positive points are positive, so every limiting vector is nonnegative. Conversely \(a_j=v/j\), \(c_j=j\) realize \(v>0\), while \(a_j=1/j^2\), \(c_j=j\) realize zero. Hence \(C_0(A)=[0,\infty)\). The curve \(a(t)=v t^2\) has exactly the required coefficient and belongs to \(A\) for every nonzero \(t\). A real analytic function with nonzero linear term changes sign across zero. It therefore cannot remain in \(A\) on both sides.

### Quadratic tangency enlarges a pair cone

*Difficulty: Advanced.*

At the origin, compute \(C(A,B)\) for \(A=\{(u,u^2):u\in\mathbb R\}\) and \(B=\{(u,0):u\in\mathbb R\}\). Compare it with the difference of their tangent spaces. Realize every vector in the answer by two analytic curves as in (7).

**Solution.** A difference from \(A\) to \(B\) has nonnegative vertical coordinate, and positive scaling preserves it. Therefore the cone is contained in \(\mathbb R\times[0,\infty)\). Given \((a,b)\) with \(b>0\), use

\[
a_1(t)=(\sqrt b\,t,b t^2),\qquad
b_1(t)=(\sqrt b\,t-a t^2,0).
\tag{24}
\]

They lie in the respective sets and their difference is \(t^2(a,b)\). For \(b=0\), take \(a_1(t)=(0,0)\) and \(b_1(t)=(-a t^2,0)\). Evaluating at \(t=1/j\) with scale \(j^2\) proves the reverse inclusion, including the zero vector. Both tangent spaces at the origin are horizontal, so their difference is only the horizontal line. The pair cone also sees the second-order separation. Reversing the ordered pair gives \(\mathbb R\times(-\infty,0]\).

### An analytic image that escapes the properness hypothesis

*Difficulty: Intermediate.*

Show that the image of \(f:\mathbb R\to\mathbb R^2\), \(f(t)=(e^{-t},\sin t)\), is not subanalytic in \(\mathbb R^2\). Identify a compact set whose inverse image proves that \(f\) is not proper.

**Solution.** If the image were subanalytic, its intersection with the analytic line \(\{y=0\}\) would be subanalytic. That intersection is

\[
\{(e^{-m\pi},0):m\in\mathbb Z\}.
\tag{25}
\]

Each member is an isolated connected component. Infinitely many approach the ambient point \((0,0)\), so these components are not locally finite there. This contradicts the connected-component theorem, even though the accumulation point is not in the image. The compact rectangle \([0,1]\times[-1,1]\) has inverse image \([0,\infty)\), which is noncompact. Thus the proper-image theorem does not apply.

### Detection through a critical point

*Difficulty: Introductory.*

Let \(h(t)=t^3\) and \(\theta=a(x)\,dx\), with \(a\) analytic on \(\mathbb R\). Prove directly that \(h^*\theta=0\) implies \(\theta=0\), although \(dh_0=0\). Give a failure of detection when surjectivity onto the specified set is dropped.

**Solution.** The pullback is \(3t^2a(t^3)\,dt\). Its vanishing gives \(a(t^3)=0\) for \(t\ne0\). Every nonzero \(x\) is a nonzero cube, and continuity gives \(a(0)=0\) as well. Therefore \(\theta=0\). For failure, take a constant map \(h:\mathbb R\to\mathbb R\), \(h(t)=0\), and specify \(S'=S=\mathbb R\). Then \(h^*dx=0\) whereas \(dx|_S\ne0\). Its image is \(\{0\}\), rather than \(S\).

### A connected subanalytic set cannot vary under a vanishing differential

*Difficulty: Advanced.*

Let \(S\subset X\) be connected and subanalytic, and let \(g:X\to\mathbb R\) be analytic with \(dg|_S=0\). Prove that \(g\) is constant on \(S\), without a properness assumption on \(g\).

**Solution.** The empty case is vacuous. The closure consequence of the cone test gives \(dg|_{\overline S}=0\). Uniformize that closed set by a proper analytic \(\pi:W\to X\). Rule (14) gives \(d(g\pi)=0\) on \(W\), so \(g\pi\) is constant on each connected component. A second-countable manifold has at most countably many components: each is open and contains a member of a fixed countable basis, and different components contain different such members. Thus \(g(\overline S)\), and hence \(g(S)\), is countable. It is connected because \(g\) is continuous and \(S\) is connected. A connected subset of \(\mathbb R\) containing two different points contains the interval between them, which is uncountable. Hence \(g(S)\) contains one point. This proof uses neither subanalyticity of \(g(S)\) nor properness of \(g\), and needs no triangulation.

### Division at a normal-crossing boundary

*Difficulty: Advanced.*

Near \((0,0)\), let \(A,C,B\) be analytic functions and put \(r=u^2v^3\), \(\alpha=A\,du+C\,dv\). Suppose \(r\alpha+B\,dr=0\) as an analytic one-form. Show that \(B=uvH\) for an analytic \(H\), and that \(B\) and the tangential restriction of \(\alpha\) vanish on the normal-crossing set \(\{uv=0\}\).

**Solution.** Comparing coefficients and cancelling analytic factors in the local ring gives

\[
uA+2B=0,\qquad vC+3B=0.
\tag{26}
\]

Thus both \(u\) and \(v\) divide \(B\). Expand \(B\) as a convergent power series: divisibility by \(u\) removes all terms of \(u\)-degree zero and divisibility by \(v\) removes all terms of \(v\)-degree zero. Factoring \(uv\) leaves a convergent analytic series \(H\). Equations (26) give \(A=-2vH\), \(C=-3uH\). Hence \(B=0\) on both axes. Along \(\{u=0\}\) the tangent differential is \(dv\), whose coefficient \(C\) is zero; along \(\{v=0\}\) it is \(du\), whose coefficient \(A\) is zero. These are exactly the restrictions on the regular locus of the crossing. The cone test supplies the same vanishing at its singular point. This is the local division mechanism used when a resolved analytic function has monomial zeros.

### Absorbing a unit while preserving two boundary axes

*Difficulty: Intermediate.*

For \(\varphi(u,v)=-e^v u^2v^3\) near \((0,0)\), give analytic coordinates expressing \(\varphi\) as a sign times a monomial. Verify invertibility and preservation of both zero-set axes. Explain why the same coordinate step cannot make the nonconstant function \(e^v\) into the monomial with every exponent zero.

**Solution.** Put \(z_1=e^{v/2}u\), \(z_2=v\). Then \(\varphi=-z_1^2z_2^3\). The Jacobian determinant is \(e^{v/2}\), which is positive; the inverse is \(u=e^{-z_2/2}z_1\), \(v=z_2\). Thus both axes and their crossing remain the same sets. An all-zero-exponent monomial is constant. If \(e^v\) became constant after a coordinate change with an inverse, composing back would make \(e^v\) constant on an open neighborhood, contradicting its nonzero \(v\)-derivative. The point of the unit lemma is the available positive exponent at a zero, not an assertion that every unit is constant in suitable coordinates.

### Centres, parallel directions and a projection-open enlargement

*Difficulty: Intermediate.*

Let \(A\) be the union of the two axis segments in \([-1,1]^2\). Determine its singular lines, choose a centre from which every line has finite intersection with \(A\), and choose a good parallel direction. Then explain why the projection of the one-point set \(\{(0,0)\}\) to the first coordinate is not open and give a compact finite-fibre enlargement whose projection is open near that point.

**Solution.** An interval in \(A\) lies on one of its axes, so the only singular lines are the two coordinate axes. Any centre with both coordinates nonzero, for example \((1/2,1/2)\), lies on neither; a line through it cannot coincide with an axis and meets the two segments in at most two points. The direction \((1,1)\) is nonsingular for every translate: its lines are parallel to neither axis. In contrast, either axis direction has a singular translate. The image of the one-point set is \(\{0\}\), which is not open in the base line, although the singleton is open in its own subspace topology. The enlargement \([-1,1]\times\{0\}\) has one-point vertical fibres and open projection near the origin. Projection openness is local here; at its two endpoints the map to the whole base line is not open. The example also shows that an enlargement may have larger dimension than the original set.

### Reciprocal heights and the exact radial lift

*Difficulty: Advanced.*

Use the two target branches in the figure, with base subdivided at \(u=0\). Compute the straight heights on \(0\le u\le1\). On the ray \(u=1/2\), compute the domain and image of the midpoint between the two straight faces under the lifting map. Explain why averaging the vertex heights would not describe a straight face.

**Solution.** On that base interval the vertex weights are \(1-u,u\). The lower vertex heights are \(1/3,1/2\), and the upper ones are \(2/3,5/6\). Therefore

\[
R_1(u)=\frac{1}{3-u},\qquad
R_2(u)=\frac{1}{(3/2)(1-u)+(6/5)u}
=\frac{10}{15-3u}.
\]

At \(u=1/2\), these are \(2/5,20/27\), and their midpoint is \(77/135\). Thus the domain point is \(p=(77/270,77/135)\). The target heights are \(3/8,17/24\). Since the map is affine on this radial interval, its midpoint has height \(13/24\), giving \(T(p)=(13/48,13/24)\). Both points lie on the ray with base \((1/2,1)\). The arithmetic average of the lower vertex heights is \(5/12\), whereas the straight face has radial height \(2/5\). The difference comes from radial projection: the affine coefficients of a point in the straight face are proportional to \(\lambda_j/r_j\), rather than to the base weights \(\lambda_j\) themselves. This is the reciprocal-height calculation in the proof.

### Resolving a function whose real zero set already crosses normally

*Difficulty: Advanced.*

For \(\varphi(x,y)=xy(x^2+y^2)\), compute \(Z=\{\varphi=0,d\varphi=0\}\). Let

\[
Y=\{((x,y),[\alpha:\beta])\in\mathbb R^2\times\mathbb{RP}^1:
x\beta=y\alpha\},
\qquad f((x,y),[\alpha:\beta])=(x,y).
\]

Prove that \(Y\) is an analytic manifold, that \(f\) is proper and is an analytic isomorphism over \(\mathbb R^2\setminus Z\), and that \(\varphi\circ f\) has the required sign-monomial coordinates near every point of \(f^{-1}Z\).

**Solution.** The derivatives are

\[
\partial_x\varphi=y(3x^2+y^2),\qquad
\partial_y\varphi=x(x^2+3y^2).
\]

The real zero set consists of the axes. On \(y=0\), the second derivative is \(x^3\); on \(x=0\), the first is \(y^3\). Thus the zero-critical set is exactly \(Z=\{(0,0)\}\).

On the projective chart \(\alpha\ne0\), put \(v=\beta/\alpha\) and \(u=x\). The incidence relation says \(y=uv\), so \((u,v)\) are unrestricted analytic coordinates. On \(\beta\ne0\), put \(s=\alpha/\beta\) and \(w=y\); there \(x=sw\), with analytic coordinates \((s,w)\). On their overlap the transition is

\[
s=1/v,\qquad w=uv,
\]

with nonzero determinant \(1/v\). These charts cover \(Y\), including its whole exceptional fibre over the origin. They make it an analytic two-manifold and make \(f\) analytic.

The incidence set is closed in \(\mathbb R^2\times\mathbb{RP}^1\): in each projective chart it is the zero set of the displayed continuous equation, so its complement is open. The projective line is compact, being the quotient of the unit circle by its antipodal involution. For compact \(C\subset\mathbb R^2\), the set \(f^{-1}(C)\) is consequently closed in the compact product \(C\times\mathbb{RP}^1\) and is compact. Hence \(f\) is proper. It is surjective; the origin has a projective line of preimages, and each nonzero \((x,y)\) has the unique preimage with direction \([x:y]\). The inverse \((x,y)\mapsto((x,y),[x:y])\) is analytic on the punctured plane, as one sees on \(x\ne0\) and \(y\ne0\). This proves the isomorphism over precisely the required complement.

In the first chart,

\[
\varphi\circ f=u^4v(1+v^2).
\]

At the exceptional point \((u,v)=(0,0)\), set \(U=u(1+v^2)^{1/4}\), \(V=v\). The Jacobian determinant there is one, the axes are preserved, and \(\varphi\circ f=U^4V\). At \((0,v_0)\) with \(v_0\ne0\), let \(\varepsilon=\operatorname{sign}(v_0)\) and shrink so that \(v\) keeps this sign. Use coordinates

\[
U=u\,|v(1+v^2)|^{1/4},\qquad V=v-v_0.
\]

The root is positive and analytic, the Jacobian determinant at the point is \(|v_0(1+v_0^2)|^{1/4}>0\), and \(\varphi\circ f=\varepsilon U^4\).

The second chart supplies the remaining direction \([\alpha:\beta]=[0:1]\):

\[
\varphi\circ f=sw^4(1+s^2).
\]

At \((s,w)=(0,0)\), set \(S=s\), \(W=w(1+s^2)^{1/4}\), giving \(SW^4\) with invertible Jacobian. If \(s_0\ne0\), set \(S=s-s_0\), \(W=w|s(1+s^2)|^{1/4}\); the expression becomes \(\operatorname{sign}(s_0)W^4\). Thus every point of \(f^{-1}Z\) has a sign-only coordinate monomial. Only the two axis directions require two positive exponents; every other exceptional direction requires one. The real zero-set picture had concealed the extra vanishing factor, and the complete two-chart construction retains it.

### Coefficients, a cusp and an unresolved exceptional tangency

**Level:** advanced. For \(h(x,t)=t^2-x^3\) marked with \(2\), compute its coefficient conditions, the two charts of the blowing-up of the origin, and the order at the exceptional points. Explain why the first multiplicity drop does not yet give normal crossings of the total function divisor.

**Solution.** The distinguished derivative is \(\partial_t^2h=2\); \(N=\{t=0\}\), \(c_0=-x^3\) with mark \(2\), and \(c_1=0\) with mark \(1\). The coefficient order is at least two only at \(x=0\), so the equimultiple locus is the origin. The coefficient's normalized order there is \(3/2\).

In the \(x\) chart, \(x=u,t=uv\). The total and controlled transforms are

\[
h\circ\sigma=u^2(v^2-u),\qquad h'=v^2-u.
\]

The transformed coefficient is \(-u\) with mark \(2\), exactly \((-u^3)/u^2\), so its order has dropped below its mark. At the exceptional point \((0,0)\), \(h'\) has order one because \(\partial_u h'=-1\). At an exceptional point \((0,v_0)\) with \(v_0\ne0\), \(h'\) is a unit. In the \(t\) chart, \(t=w,x=wz\), the controlled transform is \(1-wz^3\); it is a unit on the entire exceptional line \(w=0\). These computations cover every projective direction.

The strict transform \(u=v^2\) is smooth but tangent to the exceptional line \(u=0\) at the origin. Their differentials there are proportional. Thus their union is not normal crossing, despite the distinguished multiplicity having dropped from two to one. The total transform retains the exceptional exponent two. Both the exceptional-incidence conditions and the coefficient weights must remain visible in the resolution algorithm.

### The necessary gradient exponent on a flat direction

**Level:** intermediate. For \(f(x,y)=x^2+y^4\), prove a local Łojasiewicz gradient inequality with exponent \(3/4\), and show that a smaller exponent cannot hold in any neighborhood of the origin.

**Solution.** The Euclidean gradient is \((2x,4y^3)\). For \(|x|,|y|\le1\), concavity of the power \(r^{3/4}\) gives

\[
f^{3/4}\le |x|^{3/2}+|y|^3
\le |x|+|y|^3
\le \frac34|\nabla f|.
\]

For completeness, subadditivity \((a+b)^p\le a^p+b^p\), \(0<p<1\), follows by fixing \(a\ge0\) and differentiating \((a+b)^p-b^p\) for \(b>0\): its derivative is nonpositive, so its value is at most \(a^p\). The last inequality uses \(|\nabla f|\ge2|x|\) and \(|\nabla f|\ge4|y|^3\).

On \(x=0,y\ne0\), an inequality \(f^\rho\le C|\nabla f|\) would require \(|y|^{4\rho-3}\le4C\). If \(\rho<3/4\), its left side tends to infinity as \(y\to0\), which is impossible. Thus the flat direction determines the necessary exponent. The full gradient theorem in the human component explains why some rational exponent below one exists; this calculation determines the optimal exponent for this function.

### Formal replacement and signed analytic normalization

**Exercise 14 (intermediate).** Explain why the formal linear convergence theorem does not claim convergence of every formal solution. Give a divergent formal solution of \(f_1-f_2=1\) in \(\mathbb R[[x]]\), and a convergent solution with the same jet through any fixed degree. For \(\psi(u,z)=u-z\), \(|u|\le1\), normalize by the coefficient of largest absolute value, using the \(z\) coefficient at a tie. Determine the normalizing parameters and a uniform bound on the order in \(z\).

**Solution.** Let

\[
\widehat h(x)=\sum_{n\ge0}n!x^n,\qquad
(\widehat f_1,\widehat f_2)=(1+\widehat h,\widehat h).
\]

The difference is \(1\) coefficientwise. For any \(x\ne0\), the absolute terms of \(\widehat h\) have ratio \((n+1)|x|\), which eventually exceeds two. They therefore do not tend to zero, so this series has convergence radius zero. Both components of the displayed formal solution diverge.

For any fixed \(q\ge0\), put \(p_q(x)=\sum_{n=0}^{q}n!x^n\). The pair \((1+p_q,p_q)\) is a polynomial solution and agrees with the formal pair in degrees \(0,\ldots,q\). Thus a convergent replacement can preserve every prescribed finite jet, although there is no single convergent series with *all* those Taylor coefficients. The distinction persists even for this elementary finite linear equation.

For the second part, \(c_0=u\), \(c_1=-1\), and the units are \(A_0=A_1=1\). On \(|u|\le1\), take \(m=1\), \(g_m=-1\). Then

\[
t_0=-u,\qquad t_1=1,\qquad
Q(t,u,z)=t_0+t_1z=-u+z,\qquad
\psi(u,z)=(-1)Q(t,u,z).
\]

The first parameter takes both signs. Restricting it to \([0,1]\) would omit positive \(u\). On the correct signed compact interval, \(\partial_zQ=1\) everywhere. Therefore the order is at most one uniformly; at \(z=u\) it is exactly one, and elsewhere it is zero. This verifies the derivative criterion even where the normalized value itself vanishes.

## References and the next cotangent question

[Bierstone–Milman, *Semianalytic and subanalytic sets*](https://www.numdam.org/item/PMIHES_1988__67__5_0/), Definition 3.1 and §§3, 5 and 7, treats the local projection language, complement theorem, proper uniformization and fixed-dimensional regularity. Proposition 3.12, printed pp. 19–20, gives a dimension-preserving analytic presentation. Theorem 5.1, pp. 30–32, proves analytic-set uniformization using normal-crossing charts and induction through lower-dimensional centres; the deduction for closed subanalytic sets follows on p. 32. The torus argument here uses a compact fibre extremum and squared differential minors to reduce the source dimension directly from the proved function resolution. The uniformization conclusion supplies a proper map onto the set; the separate function-resolution theorem also retains its asserted isomorphism away from the singular zero set.

Valette’s [*On subanalytic geometry*, §1.2 and §§2.1–2.2](https://arxiv.org/abs/2507.23622v1), supplies finite analytic cells, definable derivative tests and the choice-plus-Puiseux route to analytic curves in the globally subanalytic setting. The bounded-chart comparison is what permits their use on the local sets here. The two-sided curve and exact leading-vector normalizations are then checked in this lesson. The linked adapted components retain Valette’s attribution and CC BY 4.0 terms.

Shiota’s relative polyhedron proof is the triangulation source described above. The later manifold argument proves its globalization through finite-colour chart blocks, finite-regularity subanalytic cutoffs and analytic coordinate recovery on open simplices; its specific Kankaanrinta and Milnor credits appear at those constructions. The arbitrary-manifold conclusion is therefore proved here from the stated lower inputs. The separate function-resolution proof proceeds through the marked coefficient construction, recursive exceptional histories, analytic thresholds, closed canonical centres, compact-fibre termination, and proper gluing of the independently matched local towers.

For the cotangent setting, Kashiwara–Schapira’s freely readable [*Microlocal Study of Sheaves*, §§8.1–8.2](https://www.numdam.org/item/AST_1985__128__1_0/) explains how Whitney limits control conormals and how isotropic sets lie in conormal unions. Its §8.2 convention restricts “subanalytic set” to locally closed sets, so it is not a substitute for the arbitrary-subset calculus used here. Our closure and surjective-detection proofs retain that broader stated scope and use the explicit curve and uniformization inputs; they do not require triangulation.

Guillaume Valette's [*On subanalytic geometry*](https://arxiv.org/abs/2507.23622v1), §2.2, supplies the separately licensed choice, curve-selection and Łojasiewicz treatment linked above. The linked analytic preparation treatment now proves its Chapter1 cell, complement and Puiseux inputs in the projective product convention. The local comparison here proves the manifold curve-selection consequence without a global definability assumption. The marked coefficient argument proves the local dimension reduction and its test-transform persistence. [Higher analytic prefixes, current history, and rebirth](#higher-analytic-prefixes-current-history-and-rebirth) supplies the recursive exceptional histories, and [Finite termination over a compact fibre](#finite-termination-over-a-compact-fibre) proves termination for the local towers used in the proper global construction.

For the next step, take the canonical one-form on \(T^*X\). Its vanishing on a positive-conic subanalytic set defines isotropy. The cone test and surjective detection just proved will then turn cotangent correspondences into rigorous statements about isotropic images and stratifications.

## Further exercises on preparation

### 15. A bounded function that needs a negative preparation exponent

**Level:** advanced. On

\[
C=\{(x,y):0<x<\epsilon,\ x^2<y<x\},\qquad 0<\epsilon<1,
\]

consider \(f(x,y)=x^3/y\). It is positive and bounded. Show that a finite preparation of \(f\) cannot have only nonnegative last-coordinate exponents, even if translations and analytic units are allowed. Use the convergent Puiseux theorem proved in the analytic preparation treatment.

**Solution.** We have \(0<f<x<\epsilon\). The formula \(f=x^3y^{-1}\) is already a reduction with translation zero, unit one and exponent \(-1\).

Suppose there is a finite cell preparation with all exponents nonnegative. Refine its one-dimensional base and shrink \(\epsilon\) so its base interval next to zero is \((0,\epsilon)\). Over it, list the finitely many endpoints within the original band, including \(x^2\) and \(x\):

\[
x^2=\alpha_0(x)<\alpha_1(x)<\cdots<\alpha_N(x)=x.
\]

Duplicate endpoints are removed; every open interval between consecutive endpoints is a preparation cell. Each positive endpoint has a convergent Puiseux expansion with leading term \(c_jx^{\nu_j}\), where \(c_j>0\). The bounds \(x^2\le\alpha_j\le x\) force \(1\le\nu_j\le2\). Since \(\nu_0=2\) and \(\nu_N=1\), some consecutive pair \(\alpha<\beta\) has strictly decreasing leading order. Thus \(\alpha/\beta\to0\).

On the corresponding band, write the supposed reduction as

\[
f(x,y)=a(x)|y-\theta(x)|^rU(x,y),\qquad r\ge0,
\qquad 0<m\le|U|\le M.
\]

The coefficient cannot vanish, since \(f>0\). The center is outside the band, hence either \(\theta\le\alpha\) or \(\theta\ge\beta\) throughout this connected base interval. After shrinking it, take

\[
y_\ell=2\alpha,\qquad y_h=\beta/2,
\qquad \alpha<y_\ell<y_h<\beta.
\]

The actual ratio is

\[
\frac{f(x,y_h)}{f(x,y_\ell)}
=\frac{4\alpha(x)}{\beta(x)}\longrightarrow0.
\]

If \(\theta\le\alpha\), the distance ratio is at least one, so the prepared ratio is at least \(m/M\). If \(\theta\ge\beta\), then

\[
\frac{\theta-y_h}{\theta-y_\ell}\ge\frac12,
\]

so the prepared ratio is at least \(2^{-r}m/M\). Both contradict its limit zero. Some negative exponent is therefore necessary. Boundedness of the whole function does not force nondegenerate preparation; its base coefficient can compensate for an inverse power on a narrowing band.

### 16. Even substitutions and parameter-dependent poles

**Level:** intermediate. Explain why the substitution \(t=\tau^2\) does not make \(\sqrt t\) analytic on a two-sided neighborhood of zero, while \(t=\tau^4\) does. Then analyze the globally subanalytic function

\[
f(x,t)=xt^{-1/2}+t^{1/3},
\qquad x\in\mathbb R,\quad 0<t<1.
\]

Give one common root-variable Laurent expansion and one even substitution that agrees with the actual function for both signs of the new variable. Determine the parameter pieces on which a continuous analytic extension at zero is possible.

**Solution.** The two compositions are \(|\tau|\) and \(\tau^2\). A two-sided analytic substitution must make every cleared exponent even, not merely make the substitution exponent even.

With \(t=\tau^6\) on the positive \(\tau\)-axis the Laurent expansion is

\[
f(x,\tau^6)=x\tau^{-3}+\tau^2,\qquad \tau>0.
\]

For both signs, choose \(t=\tau^{12}\). Then

\[
f(x,\tau^{12})=x\tau^{-6}+\tau^4,\qquad \tau\ne0.
\]

For \(x\ne0\) the pole remains; no continuous extension is possible there. On the parameter cell \(\{0\}\), the function becomes \(\tau^4\), analytic across zero. The cells \((-\infty,0),\{0\},(0,\infty)\) give one finite analytic parameter partition.

Even at \((x,t)=(0,0)\), continuity fails if one keeps all parameters together. Along \(x=t^{1/4}\), the first summand equals \(t^{-1/4}\) and diverges. The continuous-parameter theorem requires joint continuity on its stated neighborhood; continuity on the one slice \(x=0\) does not supply that hypothesis.

## Compatible triangulations on arbitrary analytic manifolds

**Manifold triangulation theorem.** Let M be a Hausdorff second-countable real analytic manifold without boundary, of finite dimension, and let its subanalytic subsets form a locally finite family. There is a countable locally finite linear simplicial complex with closed support in a finite Euclidean space and a subanalytic homeomorphism from that support to M, compatible with the family. On every open simplex the map is an analytic diffeomorphism onto an analytic embedded submanifold.

We prove the globalization from the relative polyhedron theorem above. The proof includes the finite-colour covering lemma, finite-regularity subanalytic cutoffs, a proper embedding, bounded proper-image calculus, the extraction of a closed subcomplex and analytic chart-coordinate recovery. The relative theorem's expressly stated lower prerequisites remain in force. They are separate from the elementary covering and cutoff arguments proved here.

### Finite-regularity subanalytic cutoffs on arbitrary analytic manifolds

This is a bounded teaching proof for the cutoff and partition-of-unity dependency in the SH-03 manifold embedding construction. It treats Hausdorff, second-countable, finite-dimensional real analytic manifolds. Fix a finite integer \(r\geq1\). Every function constructed below is \(C^r\), and its graph is locally semianalytic, hence locally subanalytic, in the indicated analytic manifold. The word “subanalytic” here concerns every ambient point of that graph; it does not assert a single globally definable Euclidean presentation at infinity.

Related cutoff constructions are treated in Marja Kankaanrinta, [*A subanalytic triangulation theorem for real analytic orbifolds*, arXiv:1105.0209v2](https://arxiv.org/abs/1105.0209v2), §5. Its closed-set separation lemma cites Proposition 5.4 of Kankaanrinta's 1991 dissertation. The proof below supplies the manifold separation and support construction directly, without taking that unread proposition as a prerequisite. It also supplies the finite \(C^r\) regularity needed for the embedding's differential-rank argument. Kankaanrinta's §5 is the comparison source for the construction, not the source of this stronger stated regularity.

#### Statements and support convention

For a function \(f\) on \(M\), write

\[
\operatorname{supp}_M f=\overline{\{x\in M:f(x)\ne0\}}^{\,M}.
\]

The following statements will be proved.

1. Every open cover \(\mathcal U\) of \(M\), with no subanalyticity hypothesis on its members, admits a countable \(C^r\), locally subanalytic partition of unity \((\lambda_i)\). Each support is compact, lies in one analytic chart and in one member of \(\mathcal U\), and the support family is locally finite in \(M\).
2. For arbitrary disjoint closed subsets \(A,B\subset M\), there is a \(C^r\), locally subanalytic \(f:M\to[0,1]\) with \(f|_A=0\) and \(f|_B=1\).
3. If \(A\subset M\) is closed and \(A\subset W\), where \(W\) is open, there is a \(C^r\), locally subanalytic \(h:M\to[0,1]\) with \(h|_A=1\) and \(\operatorname{supp}_M h\subset W\). If \(A\) is compact, \(h\) can have compact support in \(W\); if \(W\) lies in an analytic chart, that compact support lies in that chart.

Compactness in statement 3 requires a compact inner set. If \(A\) is noncompact, a compactly supported function equal to one on \(A\) is impossible. The general statement instead supplies a support contained in a locally finite union of compact coordinate-ball supports. All partition members in statement 1 individually have compact supports.

The empty manifold and an empty inner set have the empty partition and zero cutoff, respectively. All remaining arguments assume the relevant set is nonempty.

#### 1. The compact radial bump, including derivative checks

Choose rational data \(c\in\mathbb Q^n\) and \(0<\rho<R\) in \(\mathbb Q\). Set \(a=\rho^2\), \(b=R^2\), \(p=r+1\), and \(t_+=\max(t,0)\). For a real variable \(q\), define

\[
u(q)=(b-q)_+^p,\qquad v(q)=(q-a)_+^p,
\qquad\theta(q)=\frac{u(q)}{u(q)+v(q)}.
\tag{C1}
\]

The denominator is strictly positive for every real \(q\): if \(q\leq a\), then \(b-q>0\); if \(q\geq b\), then \(q-a>0\); and between \(a\) and \(b\) both are positive. Thus

\[
\theta(q)=
\begin{cases}
1,&q\leq a,\\
\displaystyle\frac{(b-q)^p}{(b-q)^p+(q-a)^p},&a\leq q\leq b,\\
0,&q\geq b.
\end{cases}
\tag{C2}
\]

The graph of this function is semialgebraic: on the three polynomial-inequality regions it is specified by \(t=1\), \(tD=(b-q)^p\) with \(D=(b-q)^p+(q-a)^p>0\), and \(t=0\), respectively. Overlapping endpoints give the same value. Non-strict inequalities are expressible using strict inequalities and equalities. Consequently, no projection theorem or o-minimal result is needed for this graph description.

The function \(t\mapsto t_+^p\) is \(C^{p-1}=C^r\). Indeed, its derivatives through order \(p-1\) on the positive half-line are constant multiples of \(t^{p-k}\), which tend to zero at the origin, matching the zero derivatives on the negative half-line. Its quotient in (C1) is therefore \(C^r\). Equivalently, near \(a\) from above,

\[
1-\theta(q)=\frac{(q-a)^p}{D(q)},
\]

and near \(b\) from below,

\[
\theta(q)=\frac{(b-q)^p}{D(q)}.
\]

Since \(D(a)=D(b)=(b-a)^p>0\), these expressions have zero derivatives of all orders \(1,\ldots,r\) at their joining endpoints. In particular, for the required \(C^1\) case \(p=2\), and more generally for \(p\geq2\),

\[
\theta'(q)=
-\frac{p(b-a)(b-q)^{p-1}(q-a)^{p-1}}{\big((b-q)^p+(q-a)^p\big)^2}
\quad(a<q<b),
\tag{C3}
\]

and \(\theta'=0\) outside this interval and at both endpoints. The displayed derivative tends to zero there.

Let \(\phi:V\to\Omega\subset\mathbb R^n\) be an analytic chart such that \(\overline{B(c,R)}\subset\Omega\). Define

\[
\beta(x)=
\begin{cases}
\theta\bigl(|\phi(x)-c|^2\bigr),&x\in V,\\
0,&x\notin V.
\end{cases}
\tag{C4}
\]

On \(V\), composition with the analytic squared norm makes \(\beta\) a \(C^r\) function, equal to one on the closed inner ball and strictly positive exactly on the open outer ball. In chart coordinates its gradient is

\[
\nabla_z\bigl(\theta(|z-c|^2)\bigr)=2(z-c)\theta'(|z-c|^2),
\]

which tends to zero at both joining spheres. Its support in \(M\) is exactly

\[
K=\phi^{-1}(\overline{B(c,R)}).
\tag{C5}
\]

This is compact and therefore closed in the Hausdorff manifold \(M\), and it lies in \(V\). Every point of \(M\setminus K\), including every point outside \(V\), has an open neighborhood disjoint from \(K\); on that neighborhood \(\beta=0\). Thus zero extension introduces neither a continuity nor a differentiability defect at the chart boundary.

The graph is locally semianalytic on \(V\), by the three analytic branch conditions from (C2) with \(q=|\phi(x)-c|^2\); at every point outside \(K\), the graph is locally the analytic zero graph. These cases cover all ambient graph points, so \(\beta:M\to\mathbb R\) is locally semianalytic and locally subanalytic globally on \(M\). A different analytic chart does not change this conclusion: analytic coordinate transitions substitute analytic functions in the finitely many local equations and inequalities. The construction also works for a zero-dimensional chart, where the coordinate ball is the singleton \(\mathbb R^0\).

#### 2. A countable locally finite nested coordinate-ball refinement

We prove the topological refinement needed above instead of assuming an analytic partition of unity or requiring a cover member to be subanalytic.

First, there is a countable cover \((E_j)_{j\geq1}\) by open coordinate balls with compact closures in \(M\). For every point, take a coordinate ball whose closed coordinate ball lies in a chart image; its closure in \(M\) is compact. Second countability gives a countable subcover: for each basis element contained in some member of this cover, select one such member. The selected members cover because a point and a covering neighborhood contain an appropriate basis element. This argument also proves the particular Lindelöf assertion being used.

Construct compact sets \(K_n\), \(n\geq1\), with

\[
K_{n-1}\subset\operatorname{int}K_n,
\qquad \overline E_1\cup\cdots\cup\overline E_n\subset\operatorname{int}K_n,
\qquad M=\bigcup_{n\geq1}\operatorname{int}K_n,
\tag{C6}
\]

where \(K_0=K_{-1}=\varnothing\). At stage \(n\), cover the compact set \(K_{n-1}\cup\overline E_1\cup\cdots\cup\overline E_n\) by finitely many precompact open coordinate balls, and let \(K_n\) be the union of their compact closures. The original open balls are an open subset of this union containing the target compact set, which proves its inclusion in \(\operatorname{int}K_n\). The resulting \(K_n\) need not be subanalytic. They are only used to organize the choices.

Given any open cover \(\mathcal U\), put

\[
S_n=K_n\setminus\operatorname{int}K_{n-1},
\qquad H_n=\operatorname{int}K_{n+1}\setminus K_{n-2}.
\tag{C7}
\]

The sets \(S_n\) are compact and cover \(M\): for any \(x\), its first membership in some \(K_n\) places it in \(S_n\). Also \(S_n\subset H_n\), since \(K_n\subset\operatorname{int}K_{n+1}\) and \(K_{n-2}\subset\operatorname{int}K_{n-1}\).

At \(x\in S_n\), choose \(U_{n,x}\in\mathcal U\) containing \(x\) and an analytic chart around \(x\). The intersection of this chart, \(U_{n,x}\), and \(H_n\) is open. In its chart coordinates, choose a rational center \(c\) and rational \(0<\rho<R\) such that the inner ball contains the coordinate of \(x\) and the closed outer ball lies in that intersection. To justify the rational choice, first take a small Euclidean neighborhood contained in the target open set, then take \(c\in\mathbb Q^n\) close enough to the coordinate of \(x\), and choose rational radii satisfying

\[
|\phi(x)-c|<\rho<R
\]

with \(R\) smaller than the remaining distance to the boundary of the chosen Euclidean neighborhood. Density of the rationals provides such data.

By compactness, finitely many resulting inner balls cover \(S_n\). Write them as \(P_{n,j}\) and their corresponding compact outer balls as \(L_{n,j}\), \(1\leq j\leq m_n\). We have

\[
\overline{P_{n,j}}\subset\operatorname{int}L_{n,j},
\qquad L_{n,j}\subset U_{n,j}\cap H_n,
\tag{C8}
\]

and every \(L_{n,j}\) lies compactly inside an analytic chart. The family of all \(L_{n,j}\) is locally finite in \(M\). Indeed, if \(x\in\operatorname{int}K_N\), this open neighborhood is disjoint from \(L_{n,j}\) for every \(n\geq N+2\), because those balls avoid \(K_{n-2}\supset K_N\). Only finitely many earlier levels remain, with finitely many balls at each level. The inner balls cover \(M\), and the family is countable.

This proves precisely the needed refinement by nested balls with locally finite compact outer closures. It uses only second countability, the Hausdorff condition, elementary coordinate topology, and finite subcovers of compact sets.

#### 3. Local graph calculus, with the boundedness hypotheses made explicit

For the particular radial bumps and their combinations, even the full general subanalytic image calculus can be avoided. Near any point, only finitely many compact supports from (C8) meet a neighborhood. A member whose support misses the point is identically zero after a further shrinking. For every other member the point lies in its analytic chart. Intersecting these finitely many neighborhoods gives a neighborhood on which each bump has finitely many semianalytic branches with an analytic expression. On a middle branch that expression is rational in analytic functions and its denominator is positive on the branch, as in (C2). Refine by the finitely many simultaneous branch choices. Each resulting piece is semianalytic, and sums, products, and quotients with a positive denominator have analytic expressions on a neighborhood of that piece. Their graphs are specified by analytic equations, or by the same equations after clearing positive denominators. Finite union gives a locally semianalytic graph. This observation will cover all the cutoffs, separation functions, and partitions constructed below.

Here are the corresponding general local subanalytic graph statements useful for other parts of the embedding argument. In these statements functions are continuous; this ensures bounded auxiliary graph coordinates near a fixed point.

**G1 — finite tuples.** If continuous \(f_j:M\to\mathbb R\) have locally subanalytic graphs, then the graph of \((f_1,\ldots,f_k)\) is locally subanalytic. In local coordinates, it is the intersection of the analytic inverse images of \(\Gamma_{f_j}\) under \((x,t_1,\ldots,t_k)\mapsto(x,t_j)\). This uses finite intersection and analytic inverse-image closure.

**G2 — sums and products.** If \(f,g\) are continuous with locally subanalytic graphs, then \(f+g\) and \(fg\) have locally subanalytic graphs. Fix \(x_0\), take a relatively compact coordinate neighborhood \(V\), and shrink it so \(f,g\) are bounded on a neighborhood of \(\overline V\). Take bounded open auxiliary intervals containing their ranges there. Intersect the two graph conditions and the analytic equation \(t=u+v\), respectively \(t=uv\), inside these bounded coordinates, also bounding \(t\). This subanalytic set has compact closure in a larger chart-and-interval neighborhood. Projection to \((x,t)\) is analytic and proper on that compact closure, so its image is subanalytic near \(x_0\). The projection describes exactly the desired graph. The properness on the closure, not just on the graph set, is the relevant image hypothesis.

**G3 — reciprocal and division.** If \(s\) is continuous, locally subanalytic, and nonzero everywhere, the graph of \(1/s\) is the analytic inverse image of \(\Gamma_s\) under \((x,t)\mapsto(x,1/t)\), on the open manifold \(t\ne0\). At an ambient point with \(t=0\), continuity of \(s\) makes \(s\) bounded near its base point, so reciprocals cannot approach zero there; the graph is locally empty. Alternatively, near \(x_0\), \(|s|\) is bounded above and bounded away from zero, and the bounded graph projection argument applies. Together with G2 this proves the division statement. A positive continuous denominator admits these local bounds even if its global infimum is zero.

**G4 — analytic compositions.** A continuous locally subanalytic map composed with an analytic map defined on a neighborhood of its local image remains locally subanalytic. Use G1 and the graph equation \(t=F(u)\), restricting \(u\) to a compact neighborhood of the image and \(t\) to bounded coordinates, and project as in G2. Analytic chart changes and products with analytic chart coordinates are special cases. For the constructed piecewise analytic functions these cases also follow directly from their finite branch equations.

**G5 — locally finite sums.** If \((f_i)\) is a family of \(C^r\) locally subanalytic functions with locally finite supports in the ambient manifold, then \(\sum_i f_i\) is \(C^r\) and locally subanalytic. Around every point, all but finitely many functions vanish on one neighborhood, so this is a finite sum there. The assertion concerns supports, not merely a pointwise finite count of nonzero values. Derivatives through order \(r\) are those of the finite local sum.

**G6 — controlled zero extension.** Let \(V\subset M\) be open and let \(g:V\to\mathbb R^k\) be \(C^r\) and locally subanalytic. If

\[
K=\overline{\{x\in V:g(x)\ne0\}}^{\,M}\subset V,
\tag{C9}
\]

then extending \(g\) by zero to \(M\) preserves both properties. On \(V\) there is no change; each point outside \(V\) lies in the open set \(M\setminus K\), where the extension is identically zero. Compact containment is a sufficient instance of (C9), not a replacement for local subanalyticity of the original graph. In particular, if \(h\) has compact support in an analytic chart \(\phi:V\to\mathbb R^n\), the zero extension of \(h\phi\) is \(C^r\) and locally subanalytic by G2/G4/G6. Chart coordinates may be unbounded towards the chart boundary, but every point of that boundary has a neighborhood where this product is zero.

The general facts G1–G4 use the exact lower-calculus prerequisites “finite intersection,” “analytic inverse images,” and “analytic images proper on the closure,” used here with their precise conditions: finite intersections and analytic inverse images preserve local subanalyticity; an analytic image is locally subanalytic when its restriction to the closure of the source set is proper. G5 and G6 are proved here from locality. Their globally subanalytic Euclidean analogues are actually read in Guillaume Valette, *On subanalytic geometry*, arXiv:2507.23622v1, native `analytic_geometry.tex`, lines 61–127 (graph definition and Basic Properties). Those global analogues are not applied to an arbitrary open cover or to the whole manifold. The direct finite-branch argument at the start of this section makes the present partition and cutoff conclusions independent of these deeper general closure theorems; they need only the elementary inclusion of semianalytic sets among subanalytic sets.

#### 4. Partition of unity subordinate to an arbitrary open cover

Apply Section 2 to \(\mathcal U\), and index the chosen pairs of nested balls by \(i\). Let \(\beta_i\) be the \(C^r\) bump from Section 1, equal to one on the corresponding inner ball and supported on its compact outer ball \(L_i\). Define

\[
S(x)=\sum_i\beta_i(x),
\qquad \lambda_i(x)=\frac{\beta_i(x)}{S(x)}.
\tag{C10}
\]

The sums are locally finite in a neighborhood, so \(S\) is \(C^r\) and locally semianalytic by Section 3. Some inner ball contains every \(x\), and its bump equals one there, hence \(S(x)\geq1\). Division preserves \(C^r\) regularity, and the finite branch descriptions prove each quotient locally semianalytic. Alternatively, G3 proves local subanalyticity directly. Thus

\[
0\leq\lambda_i\leq1,\qquad\sum_i\lambda_i=1,
\qquad\operatorname{supp}_M\lambda_i
=\operatorname{supp}_M\beta_i=L_i\subset U_i\in\mathcal U.
\tag{C11}
\]

The support equality holds because \(S\) is strictly positive: \(\lambda_i\ne0\) exactly where \(\beta_i\ne0\). These supports are compact, contained in analytic charts, and locally finite. They cover \(M\) since at every point some \(\lambda_i\) is positive. This proves statement 1, including all support and smoothness conditions.

If a partition indexed by the original cover members is wanted, choose the recorded assignment \(i\mapsto\alpha(i)\) and put

\[
\mu_\alpha=\sum_{\alpha(i)=\alpha}\lambda_i.
\]

It is \(C^r\) and locally subanalytic; only countably many members are nonzero. Its support is contained in \(U_\alpha\) and the grouped support family is locally finite. To check this last support assertion rather than assume it, a locally finite union of closed sets is closed: near a point outside the union, first discard all but finitely many sets using local finiteness and then avoid those finitely many closed sets. Therefore the union of \(L_i\) with \(\alpha(i)=\alpha\) is a closed subset of \(U_\alpha\) containing \(\operatorname{supp}\mu_\alpha\). A neighborhood meeting only finitely many \(L_i\) can meet only the finitely many grouped supports with their labels. Grouping can lose compact support in one chart, so the refined partition (C10) is the version used when those conditions matter.

#### 5. Arbitrary closed-set separation without realizing an arbitrary zero set

For disjoint closed \(A,B\subset M\), the two open sets

\[
M\setminus A,\qquad M\setminus B
\]

cover \(M\). Apply the refined partition of Section 4, with each support assigned to one of these two sets. Write \(I_A\) for indices assigned to \(M\setminus A\), and put

\[
f=\sum_{i\in I_A}\lambda_i.
\tag{C12}
\]

This is a locally finite sum, is \(C^r\) and locally subanalytic, and lies in \([0,1]\). At a point of \(A\), every term in this sum vanishes, since its support is disjoint from \(A\); hence \(f|_A=0\). At a point of \(B\), every partition term assigned to \(M\setminus B\) vanishes, so the remaining terms sum to one; hence \(f|_B=1\). This proves statement 2.

In particular, we never cover all of \(M\setminus A\) by a support family that is locally finite in \(M\) and demand positivity at every point there. Such a construction would force \(f^{-1}(0)=A\), an unjustified condition for an arbitrary closed set. In (C12) the zero set merely contains \(A\) and the one set contains \(B\). The arbitrary sets are inputs to open-neighborhood choices, not analytic graph constraints.

#### 6. Cutoff plateaus and the nested-shrink use

Let \(A\subset W\) with \(A\) closed and \(W\) open. Apply Section 4 to the open cover \(\{W,M\setminus A\}\). If \(I_W\) consists of indices assigned to \(W\), set

\[
h=\sum_{i\in I_W}\lambda_i.
\tag{C13}
\]

Exactly as in Section 5, \(0\leq h\leq1\), \(h\) is \(C^r\) and locally subanalytic, and \(h|_A=1\). The closed, locally finite union \(\bigcup_{i\in I_W}L_i\) lies in \(W\), so

\[
\operatorname{supp}_M h\subset\bigcup_{i\in I_W}L_i\subset W.
\tag{C14}
\]

This proves the general cutoff assertion. Notice that zero values on \(M\setminus W\), by themselves, would not establish (C14); the locally finite closed union is the support control.

There is a shorter compact construction that also gives a plateau on an open neighborhood of \(A\). If \(A\) is compact, choose finitely many nested coordinate balls with outer compact balls contained in \(W\) and with inner open balls covering \(A\). Let their bumps be \(\beta_1,\ldots,\beta_m\), and set

\[
h=1-\prod_{j=1}^m(1-\beta_j).
\tag{C15}
\]

Each factor lies in \([0,1]\), so \(h\in[0,1]\). On every inner ball some \(\beta_j=1\), hence \(h=1\). Outside the finite union of outer compact balls all \(\beta_j=0\), hence \(h=0\). The finite union is a compact subset of \(W\). Finite products preserve \(C^r\) regularity and the local finite branch graph description. Thus (C15) is a compactly supported \(C^r\), locally subanalytic cutoff equal to one on an open neighborhood of \(A\). When \(W\) lies in one analytic chart, all the balls can be selected in that chart, so the support lies compactly inside it. One can also form the product locally for a locally finite ball family, but the partition proof (C13) already supplies the general noncompact statement.

For the intended nested-shrink application, assume

\[
\overline V^{\,M}\subset W\subset U,
\quad U\text{ an analytic chart},
\quad \overline V^{\,M}\text{ compact}.
\tag{C16}
\]

Formula (C15), applied to \(A=\overline V^{\,M}\), gives

\[
h=1\text{ on }\overline V^{\,M},
\qquad\operatorname{supp}_M h\Subset W\subset U,
\qquad0\leq h\leq1,
\tag{C17}
\]

with \(C^r\) regularity and a locally semianalytic graph. Here \(K\Subset W\) means that \(K\) is compact and contained in \(W\); \(W\) need not be subanalytic. If a locally finite family \((W_i)\) and compact inner sets \(A_i\subset W_i\) are supplied, construct \(h_i\) independently this way. The supports remain locally finite because they are contained in \(W_i\). If the inner sets cover \(M\), then \(\sum_i h_i\geq1\), and (C10) with \(h_i\) in place of \(\beta_i\) gives the desired partition. This applies to a finite-color family just as to an uncolored locally finite family; no coloring hypothesis enters the cutoff proof.

Finally, for each chart \(\phi_i:U_i\to\mathbb R^n\), the vector map

\[
x\longmapsto
\begin{cases}
h_i(x)\phi_i(x),&x\in U_i,\\
0,&x\notin U_i
\end{cases}
\tag{C18}
\]

is \(C^r\) and locally subanalytic by the finite branch equations or G2/G4/G6. On the plateau neighborhood it equals \(\phi_i\), with exactly the chart's derivatives. This is the cutoff fact needed for the later \(C^1\) embedding and coordinate-recovery argument; the embedding itself is outside this bounded proof.

#### 7. Optional finite-group chart statement

Suppose a finite group \(G\) acts analytically on \(M\), and \(A,B\) are invariant disjoint closed sets. Apply Section 5, then average:

\[
\overline f(x)=\frac1{|G|}\sum_{g\in G}f(gx).
\]

This function is invariant, \(C^r\), locally subanalytic, still in \([0,1]\), and has the same prescribed zero and one values. Analytic diffeomorphisms preserve the local finite branch equations; the finite sum preserves all regularity. Likewise, if \(A\subset W\) are invariant and a compact cutoff \(h\) is available, the average is one on \(A\) and has support contained in the finite compact union \(\bigcup_{g\in G}g^{-1}(\operatorname{supp}h)\subset W\). This supplies a bounded finite-group lift of the separation/cutoff fact. No full orbifold atlas-gluing or global quotient theorem is claimed here.

#### Exact dependency boundary

For the constructed \(C^r\) partitions and cutoffs, the dependencies are finite-dimensional analytic chart topology; second countability and Hausdorff compactness; density of rational coordinate data; finite subcovers of compact sets; elementary differentiation and division by a nonvanishing \(C^r\) function; the definition of locally semianalytic sets and its invariance under analytic coordinate changes; and semianalytic inclusion in the local subanalytic class. The compact-exhaustion and locally finite refinement steps are fully proved in Section 2. No analytic partition of unity, analytic embedding theorem, arbitrary globally definable cover, or prescribed subanalyticity of an arbitrary open/closed input set is assumed. General local graph consequences G1–G4 additionally use only the lower calculus stated with its proper-on-closure condition in this lesson; those deeper statements are not needed for the explicit finite-branch construction.

### Finite-colour refinement for a manifold

This is a complete proof of the manifold case needed by SH-03. It applies to a topological manifold; no differentiable structure is required. The auxiliary nerve need not have a global dimension bound. The construction never triangulates the manifold.

#### Statement

Let \(M\) be a second-countable Hausdorff topological \(n\)-manifold, \(n\geq0\), and let \(\mathcal U\) be any open cover. Then there is a countable locally finite open refinement

\[
\mathcal O=\bigcup_{k=0}^{n}\mathcal O_k
\]

which covers \(M\), such that distinct members of each \(\mathcal O_k\) are disjoint. We can require more: for every \(O\in\mathcal O\) there are an original cover member \(U\in\mathcal U\) and a prescribed-atlas chart domain \(C\subset M\) such that

\[
\overline O\text{ is compact},\qquad \overline O\subset U\cap C.
\tag{F1}
\]

Thus the statement requested for a second-countable Hausdorff paracompact manifold follows. Paracompactness need not be used separately: the elementary exhaustion below provides the needed locally finite covers. The empty manifold is immediate. The usual convention here is that manifold charts are open subsets of \(\mathbb R^n\), so no boundary is involved.

#### Source comparison and attribution

Marja Kankaanrinta, [*A subanalytic triangulation theorem for real analytic orbifolds*](https://arxiv.org/abs/1105.0209), arXiv:1105.0209v2, Section 2, states the finite-colour theorem for a paracompact space of covering dimension \(n\), attributes the result originally to J. Milnor, and also credits R. S. Palais. Its next paragraph explains the indexing by finite unordered tuples.

John Milnor's *Differential Topology*, Princeton lectures, Fall 1958, notes by James Munkres, Lemma 2.19, gives the colouring by strict inequalities between partition coordinates. That text assumes the covering-dimension bound for a manifold. The actual source was read at the opening page (attribution and chapter structure) and printed pages 18–19, especially Lemma 2.19 on printed page 19, PDF page index 18. [Available lecture notes](https://www.maths.ed.ac.uk/~v1ranick/papers/difftop.pdf).

The strict-inequality colouring in the last section below is this Milnor construction, with its openness and local finiteness checked explicitly. The missing manifold dimension input is supplied here by a proved local approximation lemma and a locally finite elimination of nerve simplices. The resulting proof is an elementary argument. In particular, Palais’s theorem and an asserted equality of manifold and covering dimensions are not dependencies of this proof.

#### 1. Locally finite compact chart supports

We first construct the elementary neighbourhood data used twice in the proof.

A point in an open set \(A\subset M\) has nested chart cubes \(W,V\) such that

\[
x\in W,\qquad \overline W\subset V,\qquad
\overline V\subset A,\qquad \overline V\text{ compact}.
\tag{F2}
\]

Indeed, restrict a chart around the point to \(A\), and choose two nested Euclidean open cubes whose closures lie in its coordinate image. Their closed-cube inverse images are compact and hence closed in the Hausdorff space \(M\); they are consequently the closures in \(M\). The chart may be chosen from a supplied atlas and restricted. The same argument works for \(n=0\), when a chart cube is a single isolated point.

There is a countable cover \(B_1,B_2,\ldots\) by such relatively compact chart neighbourhoods. To see the countability, a second-countable space is Lindelöf: from an open cover, select one cover member for each basis element which lies in a cover member. These selected members still cover. Apply this to the cover of all the neighbourhoods just constructed.

There are compact sets \(K_j\), \(j\geq0\), with

\[
K_0=\varnothing,\qquad K_j\subset\operatorname{int}K_{j+1},\qquad
\bigcup_{j\geq1}\operatorname{int}K_j=M.
\tag{F3}
\]

Inductively cover the compact set \(K_{j-1}\cup\overline B_j\) by finitely many relatively compact chart neighbourhoods and let \(K_j\) be the union of their closures. The open neighbourhoods in that finite cover show that \(K_{j-1}\cup\overline B_j\subset\operatorname{int}K_j\). The sets are compact, and every \(B_j\) is eventually in an interior. Set \(K_j=\varnothing\) for negative \(j\).

The compact band

\[
A_j=K_j\setminus\operatorname{int}K_{j-1}
\]

lies in the open set

\[
D_j=\operatorname{int}K_{j+1}\setminus K_{j-2}.
\]

For every point of \(A_j\), use (F2) inside \(D_j\cap U\cap C\), with \(U\in\mathcal U\) containing the point and \(C\) a chosen atlas chart containing it. Select finitely many inner cubes \(W_{j,l}\) covering \(A_j\), and retain their paired outer cubes \(V_{j,l}\). Enumerate the pairs as \((W_i,V_i)_{i\in I}\), where \(I\) is finite or countable. They satisfy

\[
\bigcup_i W_i=M,\qquad \overline W_i\subset V_i,
\qquad \overline V_i\text{ compact in }U_i\cap C_i.
\tag{F4}
\]

The outer family is locally finite. If \(x\in\operatorname{int}K_m\), the neighbourhood \(\operatorname{int}K_m\) meets none of the cubes belonging to a band \(j\geq m+2\), because these cubes avoid \(K_{j-2}\supset K_m\). Only finitely many smaller bands exist, and each contributes finitely many cubes. In particular every compact set meets only finitely many \(V_i\): use finitely many of these local neighbourhoods to cover the compact set.

Within the coordinates of \(V_i\), take a continuous product of one-dimensional hat functions which equals one on \(\overline W_i\) and vanishes outside a smaller closed cube inside \(V_i\). Extend it by zero to \(M\). This gives

\[
0\leq b_i\leq1,\qquad b_i=1\text{ on }\overline W_i,
\qquad Q_i:=\operatorname{supp}b_i\text{ compact},\quad Q_i\subset V_i.
\tag{F5}
\]

The zero extension is continuous, since its support is contained in the interior of its chart domain. The family of supports is locally finite. The sum \(b=\sum_i b_i\) is therefore continuous and positive, and

\[
f_i=b_i/b,\qquad f_i\geq0,\qquad \sum_i f_i=1
\tag{F6}
\]

is a continuous partition with compact chart supports. All sums are finite on a neighbourhood of each point. This constructs the partition needed here, rather than invoking a partition-of-unity theorem.

Exactly the same construction applies to any open submanifold \(P\subset M\), using its own compact exhaustion. It supplies a locally finite family of closed inner cubes covering \(P\), continuous functions equal to one on those inner cubes, and larger compact chart cubes containing their supports.

#### 2. A proved point-avoidance approximation lemma

**Lemma.** Suppose \(P\) is a second-countable Hausdorff topological \(n\)-manifold, \(m>n\), \(u:P\to\mathbb R^m\) is continuous, \(a\in\mathbb R^m\), and \(\epsilon:P\to(0,\infty)\) is continuous. There is a continuous \(v:P\to\mathbb R^m\setminus\{a\}\) with

\[
\|v(x)-u(x)\|<\epsilon(x)\quad(x\in P).
\tag{F7}
\]

**Local approximation.** On a closed Euclidean \(n\)-cube \(L\), every continuous map to \(\mathbb R^m\) can be approximated uniformly within any \(\delta>0\) by a piecewise affine map missing \(a\). Subdivide \(L\) into a sufficiently fine finite cubical grid. Each small grid cube is divided into the \(n!\) simplexes obtained by ordering its \(n\) coordinate increments; these divisions agree on shared faces. Uniform continuity makes the oscillation of \(u\) on each small simplex less than \(\delta/2\).

Choose the images of the finitely many vertices within \(\delta/2\) of their original images, as follows. When a new vertex image is chosen, avoid the affine spans of \(a\) together with each collection of at most \(n\) previously chosen vertex images. There are finitely many spans, each of dimension at most \(n<m\). A proper affine subspace is closed with empty interior; a finite union of such subspaces cannot contain a nonempty open ball, by successively choosing a smaller open ball disjoint from each subspace. Thus a permissible new image always exists in the required small ball. The construction ensures that \(a\) together with any at most \(n+1\) chosen vertex images is affinely independent.

Extend the vertex images affinely over each simplex. The extensions agree on faces. No simplex image contains \(a\), because that would put \(a\) in the affine span of at most \(n+1\) of its vertex images. Barycentric interpolation and the oscillation bound give uniform error less than \(\delta\). This is only an explicit finite decomposition of a Euclidean cube, not a triangulation of \(P\).

**Global construction.** Use the end of Section 1 on \(P\) to obtain closed inner chart cubes \(H_i\) covering \(P\), larger closed chart cubes \(L_i\), and continuous functions \(\chi_i\) such that

\[
0\leq\chi_i\leq1,\quad \chi_i=1\text{ on }H_i,
\quad\operatorname{supp}\chi_i\subset\operatorname{int}L_i.
\]

Choose these so that the family \(L_i\) is locally finite. Put \(u_0=u\). Inductively choose \(\delta_i>0\) satisfying

\[
\delta_i<2^{-i-1}\min_{L_i}\epsilon
\tag{F8}
\]

and, when \(i>1\),

\[
\delta_i<\frac12\min_{H_1\cup\cdots\cup H_{i-1}}
\|u_{i-1}-a\|.
\tag{F9}
\]

The second minimum is positive by the preceding stages and compactness. Empty unions impose no condition. Approximate \(u_{i-1}|L_i\), in its chart coordinates, by a piecewise affine map \(p_i\) missing \(a\) with error less than \(\delta_i\), and define

\[
u_i=u_{i-1}+\chi_i(p_i-u_{i-1})\text{ on }L_i,
\qquad u_i=u_{i-1}\text{ elsewhere}.
\tag{F10}
\]

The formula is continuous across the boundary of \(L_i\), since \(\chi_i\) vanishes on a neighbourhood of that boundary. On \(H_i\), the new map equals \(p_i\) and avoids \(a\). Condition (F9) preserves avoidance on all earlier \(H_j\). Hence \(u_i\) avoids \(a\) on \(H_1\cup\cdots\cup H_i\).

Every point has a neighbourhood meeting only finitely many \(L_i\). Thus \(u_i\) is eventually constant on that neighbourhood, and the pointwise limit \(v\) is continuous. Each point belongs to some \(H_j\), and its final value is a finite-stage value after stage \(j\); it still avoids \(a\). At a point changed at stage \(i\), (F8) bounds the change by \(2^{-i-1}\epsilon(x)\). Therefore

\[
\|v(x)-u(x)\|<\sum_{i\geq1}2^{-i-1}\epsilon(x)
=\tfrac12\epsilon(x)<\epsilon(x).
\]

This proves the lemma. It uses neither Sard's theorem, a smooth approximation theorem, the Baire theorem, nor covering dimension.

#### 3. The nerve is locally finite, and the partition map is proper

Let \(N\) be the nerve of the cover \((V_i)_{i\in I}\): a nonempty finite set of vertices \(\sigma\subset I\) is a simplex when \(\bigcap_{i\in\sigma}V_i\ne\varnothing\). Its realization consists of the finitely supported vectors

\[
|N|=\{(t_i):t_i\geq0,\ \sum_i t_i=1,\
\{i:t_i>0\}\text{ is a simplex of }N\}
\]

in \(\ell^2(I)\), with the subspace topology. This agrees with the usual simplex topology for this locally finite complex.

In fact each vertex belongs to only finitely many simplexes. The compact set \(\overline V_i\) meets only finitely many cover members; any simplex containing \(i\) has all its vertices among these finitely many neighbours. There are only finitely many such finite vertex subsets. This proves local finiteness of the complex, but does **not** supply a uniform bound on its simplex dimensions.

Here are the topology details we will use. At \(t\in|N|\), choose an index \(i\) with \(t_i>0\). The open neighbourhood

\[
\{s\in|N|:s_i>t_i/2\}
\tag{F11}
\]

meets only the finitely many simplexes containing \(i\). It lies in a finite subcomplex; its closure lies in a compact union of finitely many closed simplexes. Thus \(|N|\) is locally compact and Hausdorff. The same finite-subcomplex description proves agreement of the two topologies. A compact subset of \(|N|\) lies in a finite subcomplex: cover it by finitely many neighbourhoods (F11), then take the union of their finite subcomplexes.

The functions (F6) define a map

\[
F:M\longrightarrow|N|,\qquad F(x)=(f_i(x)).
\tag{F12}
\]

Its support is a simplex because \(f_i(x)>0\) implies \(x\in V_i\). Continuity follows from the fact that locally only finitely many of the \(f_i\) occur. If a compact set \(D\subset|N|\) lies in a subcomplex with finite vertex set \(J\), then

\[
F^{-1}(D)\subset\bigcup_{i\in J}Q_i.
\tag{F13}
\]

The inverse image is closed and the right side is compact, so \(F\) is proper. It is also a closed map: for a closed \(A\subset M\) and \(y\notin F(A)\), take a compact neighbourhood \(D\) of \(y\). The set \(F(A\cap F^{-1}(D))\) is compact and closed, so its complement in the interior of \(D\) gives a neighbourhood of \(y\) missing \(F(A)\). In particular \(F(M)\) is closed in \(|N|\).

The same argument applies to **any** continuous \(G:M\to|N|\) for which

\[
G_i(x)>0\ \Longrightarrow\ f_i(x)>0.
\tag{F14}
\]

Such a map remains proper and closed. We will maintain this support condition during the compression. Properness is verified here because it is useful to the intended nerve route; point avoidance itself was proved in Section 2 and does not require closedness of the image.

#### 4. Compress into the \(n\)-skeleton without enlarging supports

We explain one simplex removal first. Let \(L\subset N\) be a subcomplex, let \(\sigma\) be a maximal simplex of \(L\) with dimension \(m>n\), and let \(u:M\to|L|\) be continuous. Choose \(a\in\operatorname{int}\sigma\), for example its barycentre, and put

\[
P=u^{-1}(\operatorname{int}\sigma).
\]

The interior of this maximal simplex is open in \(|L|\). Indeed, near an interior point all its vertex coordinates are positive; any simplex with those coordinates positive must contain \(\sigma\), and maximality forces it to equal \(\sigma\). Therefore \(P\) is an open \(n\)-manifold. If \(P\) is empty, the simplex may simply be removed.

Otherwise identify the affine span of \(\sigma\) with \(\mathbb R^m\). Apply Section 2 on \(P\) to \(u|P\), the point \(a\), and the continuous positive tolerance

\[
\epsilon(x)=\tfrac14\min\{1,\operatorname{dist}(u(x),\partial\sigma)\}.
\tag{F15}
\]

We obtain \(v:P\to\operatorname{int}\sigma\setminus\{a\}\). The image stays in the simplex interior because its displacement is less than the distance to the boundary. Define \(\widetilde u=v\) on \(P\) and \(\widetilde u=u\) elsewhere. This extension is continuous: at \(z\in\partial P\), continuity and closedness of \(\sigma\) give \(u(z)\in\partial\sigma\); as \(x\in P\) tends to \(z\), the bound (F15) tends to zero. The modification has not changed any coordinate outside the carrier \(\sigma\), nor introduced or removed vertices within its interior. Thus

\[
\operatorname{supp}\widetilde u(x)=\operatorname{supp}u(x)
\quad\text{for }x\in P,
\]

and it is unchanged elsewhere. The map \(\widetilde u\) now misses \(a\) everywhere.

Radially retract \(\sigma\setminus\{a\}\) to its boundary. In the vertex coordinates of \(\sigma\), with \(a_i>0\), write

\[
d(q)=\max_{i\in\sigma}(1-q_i/a_i)>0,
\qquad r(q)=a+\frac{q-a}{d(q)}.
\tag{F16}
\]

The maximum is positive for \(q\ne a\), because the coordinates of both \(q\) and \(a\) sum to one. Since \(0<d(q)\leq1\), the ray reaches the simplex boundary at this parameter; every coordinate of \(r(q)\) is nonnegative, at least one is zero, and their sum is one. If \(q\in\partial\sigma\), some \(q_i=0\), so \(d(q)=1\) and \(r(q)=q\). The formula is continuous away from \(a\).

Extend \(r\) by the identity outside \(\operatorname{int}\sigma\). This is a continuous map on \(|L|\setminus\{a\}\): the two closed pieces \(\sigma\setminus\{a\}\) and \(|L|\setminus\operatorname{int}\sigma\) agree on the boundary. Hence

\[
u'=r\circ\widetilde u:M\longrightarrow|L\setminus\{\sigma\}|
\tag{F17}
\]

is continuous, where removing the maximal simplex means removing its interior while retaining all its proper faces. It satisfies

\[
\operatorname{supp}u'(x)\subset\operatorname{supp}u(x).
\tag{F18}
\]

At a point changed by (F17), its former carrier was exactly \(\sigma\); the radial retraction replaces this carrier by a proper face.

We now perform such removals for **all** simplexes of dimension greater than \(n\). Their dimensions may be unbounded. An ordinary instruction to start at a highest dimension would consequently be invalid. Instead enumerate these simplexes in an arbitrary fixed countable list, and repeatedly remove the first unremoved simplex in that list whose proper cofaces have all been removed.

This process is well defined and eventually removes every listed simplex. Each simplex has only finitely many cofaces, since any one of its vertices belongs to only finitely many simplexes of \(N\). Among the unremoved cofaces of any unremoved simplex, a maximal one is available for removal. To see eventual removal, induct on the maximum length of a proper-coface chain above a given simplex. Maximal simplexes are immediately available. Once the finitely many proper cofaces of a simplex have been removed, it is available permanently, and only finitely many entries earlier in the fixed list can precede it. Thus it is removed after finitely many more steps. This induction has finite height for each simplex, even though heights are not globally bounded.

Starting with \(F\), apply (F17) at these stages. Denote the successive maps by \(F^{(s)}\). Their supports decrease pointwise. At a given \(x\in M\), choose a neighbourhood \(H\) meeting only finitely many \(Q_i\), with their indices in a finite set \(J\). Throughout the construction every image of a point of \(H\) has its support in \(J\), by (F18). A simplex removal can change that map on \(H\) only if all vertices of the removed simplex belong to \(J\). There are only finitely many such simplexes, and each is removed once. Consequently the maps \(F^{(s)}\) are eventually constant on \(H\).

Their pointwise limit

\[
G:M\longrightarrow|N^{(n)}|
\tag{F19}
\]

is therefore continuous. Its image lies in the \(n\)-skeleton: the interior of every simplex of larger dimension is removed at a finite stage and is never reintroduced. The support condition (F14) holds. In particular

\[
g_i\geq0,\qquad \sum_i g_i=1,\qquad
\#\{i:g_i(x)>0\}\leq n+1,
\qquad g_i(x)>0\Longrightarrow f_i(x)>0.
\tag{F20}
\]

The family of coordinate supports is still locally finite, each support lies in \(Q_i\), and \(G\), viewed as a map to \(|N|\), is proper and closed by (F13)–(F14). These conclusions are valid despite the original nerve's unbounded global dimension.

#### 5. Colour by the number of strictly dominant coordinates

For every nonempty finite \(S\subset I\) with \(1\leq|S|\leq n+1\), put

\[
O_S=\left\{x\in M:
\min_{i\in S}g_i(x)>\max\bigl(\{0\}\cup\{g_j(x):j\notin S\}\bigr)
\right\}.
\tag{F21}
\]

Use the colour \(k=|S|-1\), and discard empty sets. Formula (F21) is the strict coordinate version of the open stars of barycentres indexed by faces; the following direct checks avoid needing a barycentric-subdivision theorem.

**Openness.** On a neighbourhood where the original supports have indices in a finite set \(J\), the maximum on the right is the maximum of zero and finitely many continuous functions with indices in \(J\setminus S\). The minimum on the left is also continuous. Its strict inequality defines an open set. No infinite-intersection openness assertion is being used.

**Covering.** At \(x\), let \(S_x=\{i:g_i(x)>0\}\). By (F20), this is a nonempty set of at most \(n+1\) indices. Its minimum is positive and all outside coordinates are zero, so \(x\in O_{S_x}\).

**Disjointness within one colour.** If \(S\ne T\) and \(|S|=|T|\), choose \(i\in S\setminus T\) and \(j\in T\setminus S\). Membership in \(O_S\) would give \(g_i>g_j\), while membership in \(O_T\) would give \(g_j>g_i\). Thus \(O_S\cap O_T=\varnothing\).

**Refinement and closure control.** For every \(i\in S\), (F21) implies \(g_i>0\). By (F20) and (F5),

\[
O_S\subset\{g_i>0\}\subset\{f_i>0\}\subset Q_i,
\qquad \overline{O_S}\subset Q_i\subset V_i\subset U_i\cap C_i.
\tag{F22}
\]

Since \(Q_i\) is compact and closed, \(\overline{O_S}\) is compact. This proves (F1). In fact (F22) holds simultaneously for all \(i\in S\).

**Countability and local finiteness.** The collection of finite subsets of a countable \(I\) is countable. On the neighbourhood \(H\) used above, a set \(O_S\) can meet \(H\) only if \(S\subset J\): every index in \(S\) must have positive coordinate there. There are only finitely many such subsets. Thus the whole cover is locally finite. Its family of closures is locally finite as well, since a closure meeting the open set \(H\) implies the corresponding open set meets \(H\).

This proves the theorem in its full manifold scope.

#### Dependency and scope verdict

The complete logical route is: compact chart cubes and exhaustion → explicit continuous compact-support partition → locally finite nerve → proved point avoidance on an open manifold → coface-first simplex elimination → Milnor's strict-inequality colouring. Every step is proved above. The elementary background used is compactness, the Hausdorff property, second countability, uniform continuity on a compact cube, finite affine geometry and finite maxima/minima. No global manifold triangulation, finite-covering-dimension theorem, smoothing theorem, smooth partition theorem or Sard theorem is an unproved primitive. The only simplex decomposition is the explicitly described finite grid decomposition inside one Euclidean chart cube.

The output even gives a cover of multiplicity at most \(n+1\), so the upper covering-dimension bound follows from the construction when that convention is used. Equality of covering dimension with \(n\) is unnecessary and is not claimed as proved here.

For an analytic manifold, \(C_i\) may be chosen from its analytic atlas. The sets \(O_S\) are arbitrary open subsets with compact closures inside those charts. The proof does **not** assert that \(O_S\) is subanalytic, connected, a ball, or contractible. Subanalytic cutoff functions or any separate definability requirement must be supplied by their own argument. Distinct same-colour **open** sets are disjoint; pairwise disjointness of their closures is not asserted. The stronger closure inclusion (F22) is the chart-control input established here.

### Proper embedding and transport to the manifold

The relative polyhedron theorem above concerns a closed linear polyhedron in Euclidean space. Here we supply the globalization step for an arbitrary Hausdorff second-countable real analytic manifold \(M\) of dimension \(n\). The family \(\{S_a\}\) to be triangulated is locally finite in \(M\); each \(S_a\) is locally subanalytic. Neither compactness of \(M\) nor a globally definable atlas is assumed.

The construction follows the finite-colour and proper-normalization mechanism in [Marja Kankaanrinta, *A subanalytic triangulation theorem for real analytic orbifolds*, §§5–6](https://arxiv.org/abs/1105.0209). In the manifold case ordinary analytic chart coordinates replace the invariant maps needed for an orbifold. The finite-colour covering and continuously differentiable cutoff lemmas proved above are the topological and function-theoretic ingredients. The relative polyhedron theorem retains its stated lower subanalytic prerequisites; this globalization argument does not supply uniformization or a resolution algorithm.

#### A finite-coordinate embedding with locally recoverable charts

Choose a countable locally finite refinement \(O_{j\beta}\) of a relatively compact analytic chart cover, where \(1\leq j\leq k=n+1\), \(\beta\) is a positive integer, and distinct sets of the same colour are disjoint. The closure of each member stays in its assigned chart. Repeated shrinking of this locally finite cover gives three open covers with the same indices and

\[
\overline{U_{j\beta}}\subset W_{j\beta},\qquad
\overline{W_{j\beta}}\subset Y_{j\beta},\qquad
\overline{Y_{j\beta}}\subset O_{j\beta}.
\]

Here is the shrinking argument with its support condition. Take the proved compact-support partition subordinate to the cover \(\{O_{j\beta}\}\), and group its terms by their assigned member. The grouped functions still form a partition. Their supports \(K_{j\beta}\) lie in \(O_{j\beta}\): a locally finite union of the assigned compact supports is closed in \(M\), and contained in that member. Each \(K_{j\beta}\) is compact, because it is closed and lies in the compact closure of \(O_{j\beta}\). These supports cover \(M\). In the assigned chart, the compact image of \(K_{j\beta}\) has positive distance from the complement of the open image of \(O_{j\beta}\). Take three successively larger sufficiently small distance neighborhoods, with compact closures, to obtain \(U_{j\beta},W_{j\beta},Y_{j\beta}\). They all contain \(K_{j\beta}\), so each family covers \(M\). They remain locally finite and preserve same-colour disjointness because they are subsets of the original members. This proves the displayed shrinkings without a separate shrinking theorem.

Empty members can be omitted. Local finiteness implies that the closure of the union for one colour equals the union of its member closures. Write \(U_j,W_j,Y_j,O_j\) for these unions. By the cutoff lemma there are \(C^1\), locally subanalytic functions \(h_j,h'_j:M\to[0,1]\) such that

\[
h_j=1\text{ on }\overline{U_j},\quad
\operatorname{supp}h_j\subset W_j,\qquad
h'_j=1\text{ on }\overline{W_j},\quad
\operatorname{supp}h'_j\subset Y_j.
\]

Let \(c_{j\beta}\) be the analytic coordinate map of the assigned chart, restricted to \(O_{j\beta}\). On the disjoint union \(O_j\), define

\[
f_j(x)=(c_{j\beta}(x),\beta)\in\mathbb R^{n+1}
\quad (x\in O_{j\beta}),
\qquad
b_j(x)=
\begin{cases}
h'_j(x)f_j(x),&x\in O_j,\\
0,&x\notin O_j.
\end{cases}
\]

Each \(f_j\) is analytic on its open domain. At a point outside \(O_j\), local finiteness and \(\overline{Y_{j\beta}}\subset O_{j\beta}\) give a neighborhood meeting none of the relevant supports. Thus zero extension makes \(b_j\) a \(C^1\), locally subanalytic map on all of \(M\). Although the integer labels and chart coordinates need not be bounded globally, only finitely many labelled chart pieces occur near any point. This is precisely the local assertion required for these operations.

Set \(q=k(n+2)\), and define

\[
F_0=(h_1,\ldots,h_k,b_1,\ldots,b_k):M\longrightarrow\mathbb R^q.
\]

We prove that \(F_0\) is a topological embedding. If \(F_0(x)=F_0(y)\), choose \((j,\beta)\) with \(x\in U_{j\beta}\). Then \(h_j(x)=h_j(y)=1\), so \(y\in W_j\). Since \(h'_j=1\) throughout \(W_j\), equality of the last coordinate of \(b_j\) forces \(y\in W_{j\beta}\). Equality of its first \(n\) coordinates gives \(c_{j\beta}(x)=c_{j\beta}(y)\), hence \(x=y\).

For continuity of the inverse, suppose \(F_0(x_m)\to F_0(x)\). Again choose \(x\in U_{j\beta}\). Eventually \(h_j(x_m)>0\), so \(x_m\in W_j\), where \(b_j(x_m)=f_j(x_m)\). The integer coordinate of \(b_j(x_m)\) tends to \(\beta\). It therefore equals \(\beta\) eventually. Now \(x_m\in W_{j\beta}\), and convergence of the chart coordinates implies \(x_m\to x\). Manifolds and Euclidean subspaces are first countable, so this sequential criterion proves continuity of \(F_0^{-1}\).

The integer coordinate is essential in this proof. Positivity of \(h_j\) alone locates a point in the union \(W_j\), not in one specified \(W_{j\beta}\).

There is also a differential observation we will use later. At every \(x\) some \(h_j(x)>0\). On a neighborhood of that point in \(W_{j\beta}\), the first \(n\) coordinates of \(b_j\) are the analytic chart coordinates themselves, since \(h'_j=1\). Consequently \(dF_0\) is injective. Thus \(F_0\) is a \(C^1\) embedding with local analytic coordinates among its blocks, despite not being analytic across all cutoff boundaries.

#### Properness by one extra coordinate

Choose a countable locally finite \(C^1\), locally subanalytic partition of unity \(\{\lambda_i\}_{i\geq1}\) with compact supports, and put

\[
\lambda(x)=\sum_{i\geq1}2^{-i}\lambda_i(x),\qquad
F(x)=\frac{(F_0(x),1)}{\lambda(x)}\in\mathbb R^{q+1}.
\]

The sum is finite near every point. It follows that \(\lambda\) is \(C^1\), locally subanalytic and strictly positive, with \(\lambda\leq1/2\). Coordinate ratios recover \(F_0\) from \(F\), so \(F\) remains a \(C^1\) topological embedding and an immersion.

For \(\epsilon>0\), choose \(N\) with \(2^{-(N+1)}<\epsilon\). Outside \(\bigcup_{i=1}^N\operatorname{supp}\lambda_i\),

\[
\lambda(x)=\sum_{i>N}2^{-i}\lambda_i(x)
\leq 2^{-(N+1)}\sum_{i>N}\lambda_i(x)
\leq2^{-(N+1)}<\epsilon.
\]

Thus \(\{\lambda\geq\epsilon\}\) is a closed subset of a finite union of compact supports and is compact. If \(C\subset\mathbb R^{q+1}\) is compact, its last coordinate is bounded above by some \(R>0\). Since the last coordinate of \(F\) is \(1/\lambda\), its inverse image is a closed subset of \(\{\lambda\geq1/R\}\). Hence \(F^{-1}(C)\) is compact. This proves properness directly, without a second limit-point argument.

A proper map from a locally compact space to Euclidean space is closed here: if \(F(x_m)\) converges, the sequence lies in a compact Euclidean set, its inverse image is compact, and a convergent subsequence has the required image limit. Therefore \(Z=F(M)\) is closed.

#### The proper-image calculus needed in this construction

We give the bounded local argument rather than infer global definability from the existence of an atlas. Let \(P:M\to\mathbb R^r\) be continuous, proper and locally subanalytic, and let \(A\subset M\) be locally subanalytic. Fix a target point \(y\) and \(\rho>0\). The set

\[
K=P^{-1}\bigl(\overline B(y,2\rho)\bigr)
\]

is compact. Cover \(K\) by finitely many closed analytic coordinate boxes \(Q_\ell\), each contained in a chart neighborhood where \(A\) and the graph of \(P\) are locally subanalytic. Choose the boxes small enough that their interiors cover \(K\). By continuity, \(P(Q_\ell)\) is bounded. The bounded-chart comparison proved in the analytic preparation component makes

\[
\{(u,P(u)):u\in Q_\ell\cap A\}
\]

a bounded globally subanalytic set in chart and target coordinates. One can see this comparison at every point of its ambient closure: the source coordinate is in \(Q_\ell\), the target coordinate is \(P(u)\) by continuity, and the box lies strictly inside the chart. Thus no witness is being extended past its analytic domain.

Project these finitely many graph traces to the target and intersect with \(B(y,\rho)\). Their union is exactly \(P(A)\cap B(y,\rho)\). Indeed any source point mapping into that ball belongs to \(K\), which the boxes cover. Conversely every projected point comes from \(A\). The proved finite Boolean and projection calculus therefore makes \(P(A)\) locally subanalytic. This establishes the proper-image assertion in the generality used here, including the \(C^1\) map \(F\).

Properness also carries local finiteness to the target. A compact inverse image of \(\overline B(y,2\rho)\) has a finite neighborhood cover, each member meeting only finitely many \(S_a\). Hence only finitely many \(F(S_a)\) meet \(B(y,\rho)\). This proves ambient local finiteness even at points outside \(Z\), rather than just local finiteness in \(Z\).

The subanalytic structure does not depend on the chosen proper embedding. If \(G:M\to\mathbb R^s\) is another continuous proper locally subanalytic topological embedding, then \((F,G)\) is proper: the inverse image of a compact product is closed in the compact inverse image under \(F\) of its first projection. Its image is the graph of \(G\circ F^{-1}\), and is locally subanalytic by the argument just given. Swapping the factors gives the graph of the inverse. Thus the comparison is a subanalytic homeomorphism.

#### A closed ambient polyhedron and the subcomplex it induces

Put \(d=q+1\). There is an explicit locally finite linear triangulation \(K\) of all of \(\mathbb R^d\). For each integer vector \(m\) and each permutation \(\pi\) of \(\{1,\ldots,d\}\), take the simplex with vertices

\[
m,\quad m+e_{\pi(1)},\quad
m+e_{\pi(1)}+e_{\pi(2)},\quad\ldots,\quad
m+e_{\pi(1)}+\cdots+e_{\pi(d)}.
\]

These simplices fill the unit cube \(m+[0,1]^d\): order the fractional coordinates of a point, and express it by the successive coordinate differences as nonnegative barycentric weights. On a cube face, the coordinates fixed at zero or one drop out, leaving the same construction in the remaining coordinates. Thus adjacent cubes give the same subdivision of their common face. Include every simplex face. Any compact set meets finitely many unit cubes and finitely many of their simplices, proving local finiteness. Its support is the closed set \(\mathbb R^d\).

Apply the relative polyhedron theorem to \(K\), with the locally finite subanalytic family consisting of \(Z\) and all \(F(S_a)\). It gives a subdivision \(K'\) and a subanalytic homeomorphism \(T:\mathbb R^d\to\mathbb R^d\), analytic with injective differential on each new open simplex, compatible with the whole family.

Let \(L\) consist of the simplices \(\sigma\in K'\) for which \(T(\sigma^\circ)\subset Z\). This is a subcomplex. In fact, closedness of \(Z\) implies

\[
T(\sigma)=\overline{T(\sigma^\circ)}\subset Z.
\]

Every face of \(\sigma\) consequently has its open image in \(Z\), and belongs to \(L\). Conversely compatibility says that every point of \(Z\) lies in the image of an included open simplex. Hence \(T(|L|)=Z\). As a subcomplex, \(L\) is locally finite. It is countable, since each compact integer box meets finitely many simplices and these boxes exhaust the ambient space. Its support \(|L|=T^{-1}(Z)\) is closed.

The map

\[
t=F^{-1}\circ T|_{|L|}:|L|\longrightarrow M
\]

is a homeomorphism, compatible with every \(S_a\). It and its inverse are locally subanalytic. To verify this without a nonproper-composition assumption, restrict to compact coordinate and simplex boxes. The graph of the composition is obtained by intersecting the two bounded subanalytic graphs along their common \(Z\)-coordinate and projecting; the middle coordinate is bounded because the maps are continuous on the chosen compact sets. The bounded comparison and projection calculus apply. Such boxes cover neighborhoods of every graph point in both directions.

#### Why the open simplices are analytic embedded submanifolds

Subanalyticity of \(t\) alone does not imply analyticity on an open simplex. We use the special coordinate blocks in \(F\).

Let \(\sigma\in L\), and write \(v(u)=T(u)\) for \(u\in\sigma^\circ\). The last coordinate \(v_d\) is positive. Every coordinate of \(F_0(t(u))\) is the analytic ratio \(v_\ell(u)/v_d(u)\). Given \(u_0\), choose \((j,\beta)\) with \(t(u_0)\in U_{j\beta}\). Near \(u_0\) we have \(h_j(t(u))>0\), so \(t(u)\in W_j\) and \(h'_j(t(u))=1\). The corresponding integer coordinate is continuous and integer-valued there, and hence locally equals \(\beta\). The first \(n\) coordinates of the \(j\)-th block are therefore exactly

\[
c_{j\beta}(t(u)).
\]

They are the analytic coordinate ratios just identified. The analytic inverse of the chart shows that \(t|_{\sigma^\circ}\) is analytic near \(u_0\). Since \(u_0\) was arbitrary, it is analytic throughout the open simplex.

Its differential is injective. Indeed \(T|_{\sigma^\circ}=F\circ t|_{\sigma^\circ}\), and \(F\) is \(C^1\). The chain rule gives

\[
\operatorname{rank}d(T|_{\sigma^\circ})
\leq\operatorname{rank}d(t|_{\sigma^\circ})
\leq\dim\sigma.
\]

The left side equals \(\dim\sigma\) by the relative polyhedron theorem. Thus both inequalities are equalities. The analytic constant-rank theorem gives local analytic immersion charts. Since \(t\) is a homeomorphism on the entire support, its restriction is a homeomorphism onto its image with the subspace topology. Consequently the image is an analytic embedded submanifold and the restriction is an analytic diffeomorphism onto it. In particular no simplex has dimension greater than \(n\).

We have proved the arbitrary-manifold triangulation statement from the displayed lower prerequisites, with no analytic embedding theorem for \(M\) and no global analyticity assertion for the cutoff construction. The \(C^1\) regularity was used only in the chain-rule rank argument; finite-colour chart blocks supplied the analyticity of each transported simplex. \(\square\)

## Exercises on the globalization mechanism

### Integer labels identify the chart piece

Suppose \(W=\coprod_{\beta\geq1}W_\beta\) is a disjoint union of open chart pieces and the coordinate map on each piece is \(c_\beta\). On \(W\) consider \(b(x)=(c_\beta(x),\beta)\). If \(b(x_m)\to b(x)\) with \(x\in W_\beta\), prove that \(x_m\) eventually belongs to \(W_\beta\), and explain why merely knowing \(x_m\in W\) is insufficient. Give a counterexample to discarding the integer coordinate.

**Solution.** The last coordinates are positive integers tending to \(\beta\). Eventually their distance from \(\beta\) is less than \(1/2\), which forces equality. Hence eventually \(x_m\in W_\beta\). The first coordinates then converge to \(c_\beta(x)\); the continuous inverse of the one fixed chart gives \(x_m\to x\).

For the counterexample let \(M=\coprod_{\beta\geq1}(-1,1)_\beta\), a second-countable real analytic one-manifold, with its usual coordinate on each component. Take \(x=(0,1)\) and \(x_m=(0,m+1)\). The unlabelled coordinate map sends all these points to zero, although the sequence does not converge to \(x\): the open first component is a neighborhood containing none of its terms. It also fails injectivity. The example concerns the local chart-piece identification step; it is not a proposed compact-support atlas for the global construction. In that construction positivity of \(h_j\) first places the sequence in \(W_j\), and the unscaled integer coordinate then provides the additional localization.

### A weighted partition detects escape from every compact set

Let \(\{\lambda_i\}_{i\geq1}\) be a locally finite partition of unity on \(M\), with compact supports, and let \(\lambda=\sum_i2^{-i}\lambda_i\). Prove that \(\{\lambda\geq\epsilon\}\) is compact for every \(\epsilon>0\). If a sequence \(x_m\) eventually leaves every compact subset of \(M\), show that \(1/\lambda(x_m)\to+\infty\). Explain how this makes \((F_0,1)/\lambda\) proper even when the image of \(F_0\) is bounded.

**Solution.** Choose \(N\) with \(2^{-(N+1)}<\epsilon\). Outside the finite compact union \(C_N=\bigcup_{i\leq N}\operatorname{supp}\lambda_i\), the partition identity gives

\[
\lambda(x)\leq2^{-(N+1)}\sum_{i>N}\lambda_i(x)
\leq2^{-(N+1)}<\epsilon.
\]

Consequently \(\{\lambda\geq\epsilon\}\) is a closed subset of \(C_N\), and is compact. An escaping sequence eventually avoids this set for every \(\epsilon>0\); hence \(\lambda(x_m)\to0\) and its reciprocal tends to infinity.

For a compact target set, bound its last coordinate above by \(R>0\). Its inverse image under \((F_0,1)/\lambda\) is closed and lies in the compact set \(\{\lambda\geq1/R\}\). It is therefore compact. Boundedness of the other coordinates has no effect on this conclusion. The single positive last coordinate carries the entire properness argument.

### An analytic homeomorphism can have a zero differential

On \((-1,1)\), let \(t(u)=u^3\), \(F(x)=\sqrt[3]{x}\), and \(T=F\circ t\). Check that \(F\) is a proper locally subanalytic topological embedding, that \(T\) is an analytic immersion, and that \(t\) is an analytic homeomorphism whose differential is not injective at zero. Identify the missing hypothesis in an attempted chain-rule rank argument. Contrast this with the \(C^1\) map in the globalization proof.

**Solution.** Regard all three maps as maps from \((-1,1)\) to itself. The cube-root map is a homeomorphism, so the inverse image of a compact set is compact. Its graph is given by \(y^3=x\), and is semialgebraic, hence locally subanalytic. The composite is \(T(u)=u\), with differential equal to one. The map \(t\) is analytic and bijective with continuous inverse, but \(t'(0)=0\). Thus an analytic homeomorphism need not be an analytic immersion or an analytic diffeomorphism.

The cube root is not differentiable at zero: \(\sqrt[3]{h}/h=|h|^{-2/3}\) for nonzero \(h\), which diverges. One cannot apply the chain rule there. In the globalization proof the constructed embedding is \(C^1\); once chart-coordinate ratios prove that the transported simplex map is analytic, the chain rule is valid. Since \(T\) has rank \(\dim\sigma\), it forces the transported map to have the same rank. The cutoff's finite differentiability is therefore a substantive hypothesis in that step.

### Closedness and ambient local finiteness do different jobs

Triangulate \([0,1]\) by its two vertices and one edge. For \(Z=(0,1)\), collect simplices whose open interiors are contained in \(Z\). Explain why this collection is not a subcomplex. Next let \(F:\mathbb R\to(-1,1)\subset\mathbb R\) be \(F(x)=x/\sqrt{1+x^2}\), and let \(S_m=\{m\}\), \(m\geq1\). Verify that \(\{S_m\}\) is locally finite in \(\mathbb R\), whereas \(\{F(S_m)\}\) is not locally finite in the ambient target \(\mathbb R\). State where properness repairs each problem in the theorem.

**Solution.** The open edge is \((0,1)\), so the edge is selected. Neither endpoint is in \(Z\), so neither vertex is selected. A simplicial subcomplex must contain every face of a selected simplex, and this collection fails that condition. When \(Z\) is closed instead, \(T(\sigma^\circ)\subset Z\) implies \(T(\sigma)\subset Z\), because a continuous homeomorphism takes the closure of the open simplex to the closed simplex image. Every face is then selected as well.

Every bounded interval in the source meets finitely many positive integers; this proves local finiteness of the family \(\{S_m\}\). But

\[
F(m)=\frac{m}{\sqrt{1+m^2}}\longrightarrow1.
\]

Every ambient neighborhood of \(1\) meets infinitely many of these singleton images. The map is not proper as a map to \(\mathbb R\): the inverse image of the compact set \([0,1]\) is the noncompact set \([0,\infty)\). Its image is also not closed in that ambient space.

For the theorem's proper embedding, the image is closed, which makes the selected simplices face-closed. Separately, the compact inverse image of a closed target ball meets only finitely many members of a locally finite source family, which establishes local finiteness in the whole target. Local finiteness only inside the image would not justify the ambient relative polyhedron theorem.

## Exercises on compatible analytic partitions

### Restriction rank must be calculated again

**Exercise P1 (intermediate).** Let \(f(x,y)=x\), \(g(x,y)=y\) on \(\mathbb R^2\), and prescribe compatibility with the analytic line \(S=\{x=0\}\). Both ambient maps have constant rank one. Give a connected analytic partition compatible with \(S\), compute both restriction ranks, and explain why decomposing only by ambient rank misses a necessary calculation.

**Solution.** The three members \(\{x<0\}\), \(S\), and \(\{x>0\}\) form a finite compatible partition into connected analytic embedded submanifolds. On each open half-plane, the tangent space is \(\mathbb R^2\), so both coordinate projections have rank one. On \(S\), the tangent vectors are \((0,v)\). The differential of \(f|_S\) is zero, while that of \(g|_S\) sends \((0,v)\) to \(v\); their ranks are zero and one respectively. An ambient rank decomposition has only the rank-one set for each map, so it gives no information about the rank after a lower-dimensional compatibility refinement. The partition proof recalculates the differentials in each smaller member's own coordinates.

### Accumulation prevents local finiteness

**Exercise P2 (introductory).** On \(\mathbb R\), each singleton \(A_n=\{1/n\}\), \(n\geq1\), is semianalytic. Prove that there is no locally finite partition into connected analytic submanifolds compatible with every \(A_n\). Compare with the family \(\{\{m\}:m\in\mathbb Z\}\), and give an explicit compatible locally finite partition for that family.

**Solution.** If a partition member contains \(1/n\), compatibility makes it a subset of \(A_n\), so that member must be exactly \(\{1/n\}\). Every neighborhood of zero contains infinitely many of these distinct members, contradicting local finiteness. The prescribed family itself is not locally finite at zero; the theorem's family hypothesis is therefore substantive even though each individual set has a very simple analytic definition. For the integers, take all singletons \(\{m\}\) and all intervals \((m,m+1)\), \(m\in\mathbb Z\). They are connected analytic submanifolds, cover \(\mathbb R\) disjointly, and are compatible with every integer singleton. A bounded neighborhood of any point meets only finitely many of these members. The partition is locally finite and countable, as required.

## Dimension and frontier exercises

These exercises use the complete linked dimension, frontier and parameter-continuity provider. Their adaptation credit and CC BY4.0 terms remain at that provider.

**Exercise D1 (basic: two boundaries).** In \(\mathbb R^2\), calculate the frontier and topological boundary of the unit circle \(S^1\) and of the open unit disc. Give their dimensions and identify which strict inequality applies.

**Solution.** The circle is closed with empty interior in \(\mathbb R^2\). Therefore \(\operatorname{fr}S^1=\varnothing\), of dimension \(-1\), and \(\partial S^1=S^1\), of dimension one. Its own dimension is one, so strict frontier decrease holds while strict decrease of topological boundary relative to the set fails. The open disc has dimension two; its closure is the closed disc and both its frontier and its topological boundary are the circle, of dimension one. In both examples the topological boundary has dimension less than the ambient dimension two.

**Exercise D2 (intermediate: the exceptional parameter).** Let \(A=\{(t,x):t>0,\ x=t\}\subset\mathbb R^2\). Determine exactly where \((\overline A)_t=\overline{A_t}\) fails. Give a base partition satisfying (D10), and explain why restricting before taking closure matters.

**Solution.** For \(t>0\), both sets are \(\{t\}\); for \(t<0\), both are empty. At \(t=0\), \(A_0=\varnothing\) but \((\overline A)_0=\{0\}\), so this is the unique exception. Use the partition \(( -\infty,0),\{0\},(0,\infty)\). On its first two pieces the restricted family is empty, and its closure is empty. On the positive piece the fibre equality holds at each parameter in that piece. Although its closure accumulates at parameter zero, zero is not a parameter of that positive piece. Thus (D10) asserts equality on each piece only after restricting the family; it does not assert that the original ambient closure commutes with all fibres.

**Exercise D3 (advanced: continuity and bounded transforms).** Define

\[
f(t,x)=
\begin{cases}
\dfrac{tx}{t^2+x^2},&(t,x)\ne(0,0),\\
0,&(t,x)=(0,0).
\end{cases}
\]

Show that every \(x\)-fibre is continuous although \(f\) is not jointly continuous. Find a base partition making it continuous on the corresponding product pieces. Finally show why \(s/(1+s^2)\) cannot replace the injective transform (D16).

**Solution.** For \(t\ne0\) the denominator is everywhere positive, so the fibre is continuous. For \(t=0\) the function is identically zero, including at \(x=0\), so that fibre is continuous too. Along \(x=t\ne0\) its value is \(1/2\), whereas at the origin its value is zero. Thus it is not jointly continuous. The partition \(( -\infty,0),\{0\},(0,\infty)\) works: on either open parameter half-line the same positive-denominator formula is continuous jointly; on the zero piece the function is zero. For the last claim let \(g(0)=1/2\) and \(g(t)=2\) when \(t\ne0\). This definable function is discontinuous at zero, but \(g/(1+g^2)=2/5\) everywhere. Continuity of the bounded composite therefore does not imply continuity of \(g\). The inverse in (D16) is precisely what prevents this loss of information.
