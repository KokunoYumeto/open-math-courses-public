# Smooth triangulations and the integral PL obstruction

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0. No independent mathematical review is recorded.*

A compatible triangulation gives a smooth manifold a PL structure. We construct such triangulations, extend prescribed boundary triangulations exactly, and compare two compact triangulations by a PL homeomorphism. The boundary comparison turns the explicit two-disk exotic seven-sphere into a PL sphere. Coning that sphere onto its disk-bundle filling produces a closed PL eight-manifold whose second rational Pontryagin number is \(81/7\). That fraction proves that the canonical rational PL classes cannot always be refined to integral classes.

This is the final companion for assigned lesson15. Sections L–N supply its general smooth-triangulation prerequisite and the relative compatibility needed by the eight-dimensional example. Section O supplies the integral-refinement obstruction, including an actual fibre comparison for the first class at the cone. Six graded exercises have complete solutions. These results finish the stated lesson15 proofs together with the earlier construction and comparison chapters. The full unoriented bordism detection proof and its further mod-two prerequisites are supplied in [the unoriented detection companion](stiefel-whitney-numbers-and-unoriented-bordism.md).

Sections A–H referenced here belong to [Combinatorial L-classes and piecewise linear fibres](combinatorial-l-classes-and-piecewise-linear-fibres.md): finite refinements, exact relative PL approximation, rational cohomotopy, generic fibre signatures, duality and stable L-classes. Sections I–K belong to [Smooth fibres, triangulation comparison and lens spaces](smooth-fibres-triangulation-comparison-and-lens-spaces.md): controlled interpolation, the finite-piece Lipschitz lemma, smooth comparison in all degrees and unoriented descent. The four-plane bundles, Thom square and two-disk decomposition used in Section O are proved in [Milnor's exotic seven-spheres](milnors-exotic-seven-spheres.md), Sections A–C. Smooth collars and signed seam charts are proved in [The oriented cobordism ring](the-oriented-cobordism-ring.md), Theorem1.1 and Lemma2.1. The [bundle chapter](vector-bundles-and-their-constructions.md), Section5, and the [Thom-space chapter](thom-spaces-and-the-pontryagin-thom-construction.md), SectionA, supply the compact exhaustion, smooth partitions and Sard theorem used in the optional noncompact existence result. The [manifold chapter](manifold-duality-the-diagonal-and-wu-classes.md) supplies the local inverse, local degree and point-local orientation proofs. The subsequent arguments use these complete prerequisites with their stated hypotheses.

## L. A given smooth triangulation has PL local charts

This section addresses a prerequisite different from existence. A smooth-compatible triangulation is already assumed. We prove that its local stars are PL charts; we do not construct the triangulation. All complexes here are finite, and the boundary, when present, is a specified subcomplex.

**Lemma L.1 — A finite local-degree test.** Let \(n\geq1\), and let \(X\) be a topological \(n\)-manifold without boundary, covered locally by the closed simplices of a finite pure \(n\)-complex. Let \(P:X\to\mathbb R^n\) be continuous and affine with injective linear part on each simplex. Suppose that the image of an interior point of any \(n\)-simplex has exactly one preimage in \(X\). Then \(P\) is an open embedding.

**Proof.** At every \(y\), discard the finitely many simplices not containing \(y\) by shrinking its neighbourhood. On each remaining simplex the affine map is injective. Consequently \(P^{-1}(P(y))\) meets that neighbourhood only at \(y\). Choose a closed topological coordinate ball \(B\) about \(y\) in that neighbourhood. Its boundary is compact and its image misses \(P(y)\), so the distance between them has a positive minimum. A sufficiently small target ball \(V\) about \(P(y)\) misses \(P(\partial B)\).

Choose an orientation on \(B\). The degree of \(P:(B,\partial B)\to(\mathbb R^n,\mathbb R^n-\{w\})\) is constant for \(w\in V\): the relative generator is transported along a segment in \(V\), which does not meet the image of the boundary. This is precisely the point-local degree and excision construction already proved in the manifold chapter. Full-dimensional simplex interiors are dense in \(X\). Choose a point \(z\) of one such interior in the interior of \(B\), sufficiently close to \(y\) that \(P(z)\in V\). By hypothesis this target point has just that one preimage. Near \(z\) the map is an invertible affine map, so its local degree is \(+1\) or \(-1\). Excision makes that its degree on \(B\). The constant degree on \(V\) is therefore nonzero. Every point of \(V\) is attained in the interior of \(B\), since a missing point has degree zero. This proves openness at \(y\).

Suppose two distinct points have the same image. Choose disjoint small coordinate balls around them. Openness supplies a common target ball in the images of both interiors. The images of all lower-dimensional simplices lie in finitely many proper affine subspaces; choose a target point in that ball outside their union. It has a preimage in each coordinate ball, and both preimages are interiors of full-dimensional simplices. This contradicts the uniqueness hypothesis. Thus \(P\) is injective. A continuous injective open map is a homeomorphism to its open image. Its restriction to every simplex is affine, so it is a PL embedding. ∎

**Theorem L.2 — Tangent stars.** Suppose \(t:|K|\to M^n\) is a homeomorphism from a finite triangulation to a smooth manifold. Assume its restriction to every closed full-dimensional simplex has a smooth extension with derivative of rank \(n\), including along its faces. If \(M\) has boundary, assume \(t^{-1}(\partial M)\) is a subcomplex, with the analogous smooth full-rank condition in dimension \(n-1\). At boundary points, extension means extension of the coordinate functions to the ambient Euclidean space of a half-space chart; the extension is allowed to leave that half-space. Then \(K\) has PL local charts to Euclidean space or its closed half-space, according as the point is interior or boundary. For \(n=0\), each point already has its single-point PL chart.

**Proof: the affine tangent map.** First treat an interior point. Insert a chosen point \(x\) as a vertex by stellar subdivision of its smallest face. Every resulting full-dimensional simplex is contained in an old simplex and spans its affine \(n\)-space, so the rank hypothesis survives. Choose smooth coordinates \(\psi\) about \(t(x)\), with \(\psi(t(x))=0\). On the open star \(N_x\), define
\[
 P_x(y)=D(\psi t|_\sigma)_x(y-x),\qquad y\in\sigma.
\tag{L.1}
\]
On a common face the two derivatives agree in directions tangent to that face. Indeed the original smooth extensions agree as functions on the face, first on its relative interior and then by continuity of their derivatives on its boundary. Thus (L.1) is well defined and continuous. On every full simplex it is affine and has invertible linear part. It sends \(x\) to zero and is radially homogeneous along segments starting there.

The complex is pure in dimension \(n\). To see this without a dimension convention, any maximal simplex of dimension \(r\) has an interior point whose neighbourhood in \(|K|\) is an open subset of its affine \(r\)-space. The already proved local homology of Euclidean space is nonzero precisely in degree \(r\). A boundary point of a manifold has zero local homology in every degree: in a half-space centred there, the half-space with the point removed retracts radially to a hemisphere, and both that hemisphere and the half-space are contractible. The pair sequence gives the assertion. Thus our simplex interior point maps to an interior manifold point, whose local homology is nonzero precisely in degree \(n\). Hence \(r=n\). This also proves that full-simplex interiors are dense in the open star.

**Proof: interior images are covered once.** Take \(y\) in the interior of a full simplex \(\sigma\) incident to \(x\), and suppose \(P_x(z)=P_x(y)=w\). The case \(w=0\) is impossible: the linear part on \(\sigma\) is injective and \(y\ne x\). For small \(s>0\), put
\[
 y_s=x+s(y-x),\qquad z_s=x+s(z-x).
\]
Both points stay in the open star, and the smooth simplex extension gives
\(\psi t(z_s)=s w+o(s)\). The extension of \(\psi t|_\sigma\) has a smooth local inverse at \(x\). Applying it to \(\psi t(z_s)\) gives
\[
 x+s(y-x)+o(s).
\tag{L.2}
\]
This inverse point is inside \(\sigma\) for sufficiently small \(s\). In its barycentric coordinates the coordinates at all vertices other than \(x\) have the positive leading terms \(s\lambda_i(y)\); the coordinate at \(x\) has leading value one. The \(o(s)\) errors cannot change those signs.

The restriction of the extension there is the actual map \(t\). Since \(t\) is injective, (L.2) must equal \(z_s\). Thus \(z_s\) belongs to the interior of \(\sigma\). A segment from the vertex \(x\) in an open star lies in the interior of \(\sigma\) at a positive parameter only if its endpoint also belongs to that simplex interior: in the geometric realization its nonzero barycentric support away from \(x\) does not change under this radial scaling. Hence \(z\in\operatorname{int}\sigma\). Injectivity of the affine restriction now gives \(z=y\).

The open star is a topological manifold through \(t\), although its PL structure has not been presumed. Lemma L.1 applies and proves that \(P_x\) is a PL homeomorphism onto an open subset of \(\mathbb R^n\). This supplies the interior local chart.

**Proof: boundary points.** Suppose \(x\) maps to the boundary and take \(\psi\) valued in \(\mathbb R^{n-1}\times[0,\infty)\). Construct the same affine map (L.1). Its last coordinate is nonnegative on every cone of the star: along every segment \(x+s(y-x)\), the actual smooth coordinate has nonnegative last coordinate, so its derivative at \(s=0\) does too. On an interior point of a full simplex that last derivative is strictly positive. Its values at the edge directions are nonnegative; if they were all zero the derivative would have image in the boundary hyperplane and could not have rank \(n\). All edge barycentric coefficients at such an interior point are positive, so at least one gives a positive contribution.

The restriction of \(P_x\) to the boundary star is the tangent-star map for \(t|_{\partial K}\). That is a triangulation of the smooth \((n-1)\)-manifold \(\partial M\) without boundary. The interior proof just given, now in dimension \(n-1\), makes this restriction an open embedding into the boundary hyperplane. In dimension zero the assertion is the identity between single-point neighbourhoods. No triangulation existence assertion is used in this reduction.

Double the open star along this boundary star. It is a topological manifold without boundary, as is seen by doubling the half-space charts transported from \(M\). On the first half use \(P_x\); on the second use its reflection in the target boundary hyperplane. The maps agree on the identified boundary, so they define a continuous, simplexwise affine map \(\widehat P_x\) to \(\mathbb R^n\). Each full simplex still has an injective linear part. The interior-image uniqueness argument above applies within either half. Images of full-simplex interiors in the two different halves are disjoint, since their last coordinates have opposite strict signs. An interior-simplex image cannot be a boundary-star image, whose last coordinate is zero. Thus every full-simplex interior image has exactly one preimage in the double.

Lemma L.1 makes \(\widehat P_x\) an open embedding. Its injectivity also excludes an interior point of either half, even on a lower-dimensional face, from mapping to the boundary hyperplane: such a point would have a distinct reflected copy with the same image. Thus the first-half preimage of the upper half-space is exactly that first half. Restricting the homeomorphism gives an open image in the relative topology of the closed half-space. This proves the boundary local chart.

Finally these charts form a PL atlas. On an overlap each chart is affine on the pieces of a common finite subdivision of the original simplices; both are injective there. Their transition is therefore affine on each image piece. Intersections of finitely many image polyhedra can be subdivided compatibly: cut by their finitely many affine face hyperplanes and triangulate the resulting convex polytopes by the ordered-vertex construction already proved in the combinatorial chapter. This supplies a common triangulation on every relatively compact overlap. The chart transition is PL in both directions. ∎

The source for the tangent-star argument is John Milnor, [On the relationship between differentiable manifolds and combinatorial manifolds](https://faculty.tcu.edu/gfriedman/notes/milnor3.pdf), AppendixII, Lemma7. The finite local-degree test, radial inverse estimate and boundary doubling proof above are independently supplied. Its statements W1–W3 refer to Whitehead for existence, uniqueness and the triangulated-disk comparison. Sections M–N below supply those arguments in the precise compact and boundary-relative scopes needed here.

## M. Quantitative tools for constructing triangulations

A **piecewise smooth map**, or PD map, on a polyhedron is a continuous map which, after a locally finite subdivision, has a smooth extension from every closed simplex to a neighbourhood in its affine hull. A PD embedding has, in addition, derivative rank equal to the simplex dimension at every point of that closed simplex and is a homeomorphism onto its image. For a manifold with boundary, smooth extensions in a boundary chart are allowed to leave the target half-space. A compatible triangulation is a PD homeomorphism to the manifold, with its boundary the image of a subcomplex and with the same rank condition on that boundary. Subdivision never changes the map or the meaning of compatibility.

In this section the domains are finite. First-derivative estimates are made in fixed affine coordinates on the old simplices and fixed smooth charts on compact parts of their images. A refinement is permitted, but the estimates on its pieces use these same old affine coordinates. There are finitely many coordinate changes, all with bounded first derivatives on the compact sets in use. Thus a change tending to zero in these estimates also tends to zero after any of those fixed changes of coordinates.

### M.1. A small PD change is a small Lipschitz change

**Lemma M.1 — Extension of a difference from a finite polyhedron.** Realize a finite complex \(P\) in a Euclidean space. Suppose \(a:P\to\mathbb R^q\) is continuous and piecewise smooth, with derivative norm at most \(\eta\) along every simplex of a subdivision of a fixed triangulation. There are a neighbourhood of \(P\), a finite collection of neighbourhoods covering it, and a constant \(C\) depending only on the fixed realization such that, in each of these neighbourhoods,
\[
 |a(x)-a(y)|\leq C\eta|x-y|\qquad(x,y\in P).
\tag{M.1}
\]
The constant does not depend on how finely the pieces of \(a\) have been subdivided.

**Proof.** Put the realization inside a large Euclidean box. A finite hyperplane cutting makes \(P\) a subcomplex of a triangulation of that box: include hyperplanes defining the affine hull and the relative facet inequalities of every simplex of \(P\), cut the box and its faces by them, and triangulate the resulting convex faces by face-chain coning. This is the common-refinement construction of combinatorial Lemma E.1. After barycentric subdivision, \(P\) is a full subcomplex: a simplex of the ambient subdivision is a chain of old faces; if all its vertices correspond to faces in \(P\), the entire chain lies in \(P\).

On an ambient simplex write its barycentric coordinates as \(\lambda_v\), and put
\[
 s(z)=\sum_{v\in P}\lambda_v(z),\qquad
 r(z)=\frac{\sum_{v\in P}\lambda_v(z)v}{s(z)}.
\tag{M.2}
\]
The formula is used where \(s>0\). Fullness makes its image lie in a simplex of \(P\). The formulas agree on shared faces and fix \(P\), where \(s=1\). The continuous function \(s\) is therefore larger than \(1/2\) on some neighbourhood of the compact set \(P\). On that neighbourhood \(r\) has finitely many rational smooth formulas, with denominators bounded away from zero and first derivatives bounded by one constant \(C\).

The composite \(a r\) has derivative norm at most \(C\eta\) on each of its pieces. More explicitly, the image of an ambient simplex lies in one fixed face \(F\) of \(P\). Cover \(F\) by the closed full-dimensional smooth pieces of the restriction of \(a\) to \(F\). Each has affine hull equal to that of \(F\). Intersect the ambient simplex with their inverse images under its formula for \(r\). These are finitely many closed sets. On each, a smooth extension of \(a\) in the affine hull of \(F\), composed with the rational formula, supplies a local smooth extension. The derivative of \(r\) has values in that affine hull, so the required bound is tangential; no unestimated normal derivative is used. The derivative bound at the assigned set gives bounds \(C\eta+\varepsilon\) in sufficiently small neighbourhoods, by continuity. Apply Lemma J.3 and let \(\varepsilon\) decrease to zero. Thus \(a r\) is \(C\eta\)-Lipschitz on a small convex ball inside \(s>1/2\). A finite collection of such balls covers \(P\), proving (M.1). ∎

The same proof applies on a closed subpolyhedron of a coordinate neighbourhood. In particular every finite PL homeomorphism between Euclidean polyhedra is locally bi-Lipschitz. Apply the lemma to its finitely many affine pieces and to the affine pieces of its inverse; on a smaller compact neighbourhood their constants are finite.

**Lemma M.2 — Stability of a partial embedding.** Let \(f:P\to M\) be a PD embedding of a finite polyhedron. Assume that in local smooth target coordinates it is locally bi-Lipschitz for the Euclidean metric of a fixed realization of \(P\). A sufficiently small piecewise smooth change in values and first derivatives is again a PD embedding and has that same local bi-Lipschitz property. A change supported in a compact part of one target chart can be made there and extended by the original map elsewhere.

**Proof.** On a sufficiently small neighbourhood of each source point, a target coordinate representation satisfies
\[
 |f(x)-f(y)|\geq c|x-y|\qquad(c>0).
\]
By Lemma M.1 the difference between the changed and original coordinate maps is \(C\eta\)-Lipschitz. Choose \(C\eta<c/2\). Subtraction gives a lower bound \((c/2)|x-y|\) for the changed map, and an upper Lipschitz bound follows in the same way. Compactness gives finitely many such neighbourhoods. Pairs outside a neighbourhood of the diagonal in \(P\times P\) have original image distance bounded below by a positive number, since the original map is injective. A sufficiently small value change keeps these pairs distinct. This proves global injectivity. Compactness of \(P\) makes the continuous injection a homeomorphism onto its image.

The smallest singular value of the derivative on each positive-dimensional old closed simplex has a positive minimum; the rank-zero vertex condition is automatic. A derivative change smaller than half these finitely many minima preserves its rank, also on all refined pieces. If the support is compact in a chart, choose the value change smaller than its distance to the chart edge, and make the difference zero on a neighbourhood of the support boundary. The changed coordinate formulas then glue to the old map. ∎

The bi-Lipschitz hypothesis matters: injectivity and ranks on separate simplices alone do not give a uniform separation between different tangent branches. The construction below maintains this additional hypothesis at every chart-gluing step.

### M.2. Stability of a full compatible triangulation

**Lemma M.3 — Full homeomorphism stability.** Let \(t:P\to M\) be a compatible triangulation of a compact smooth manifold. A sufficiently small PD change of its values and first derivatives is again a compatible homeomorphism, provided its source boundary maps into the target boundary. The assertion also allows first making the change in a smooth double of \(M\): the boundary condition and a sufficiently small change force its image back into \(M\).

**Proof in the interior.** The complex is pure in the manifold dimension by the local-homology argument in Theorem L.2. At every point of a full simplex, the smooth extension of \(t\) has an invertible derivative. The local inverse theorem gives a smooth inverse extension from its image, with bounded derivative after shrinking about that point. Take a finite collection of these inverse neighbourhoods on the compact closed full simplices.

In a small convex target coordinate ball, write the changed map, composed with the actual inverse of \(t\), as
\[
 G(x)=x+b(x).
\tag{M.3}
\]
Each closed full-simplex image, restricted further to the inverse neighbourhoods just chosen, is a closed piece on which \(b\) has a smooth local extension. The chain rule bounds its derivative by \(C\eta\), since the unperturbed composite is the identity. Lemma J.3 gives \(\operatorname{Lip}(b)\leq\theta<1/2\), after choosing \(\eta\) small. In particular \(G\) is injective on that ball.

It is locally open by a direct inverse construction. On a closed ball of radius \(r\) about \(x_0\), the map \(x\mapsto y-b(x)\) is a contraction and preserves the ball whenever
\[
 |y-G(x_0)|<(1-\theta)r.
\tag{M.4}
\]
Its iterates are Cauchy by the geometric-series estimate, converge in the closed ball, and give the unique inverse point. The estimate also gives continuity of the inverse. Thus \(G\) covers the ball specified in (M.4).

**Proof at the boundary.** Use a convex coordinate half-ball \(x_n\geq0\). The same inverse extensions from full simplices give the same Lipschitz estimate. The boundary condition says \(b_n(x',0)=0\). Extend \(b\) to the full ball by reflecting its tangential components evenly and its last component oddly. This is continuous at the equator. It is \(\theta\)-Lipschitz on each half; a segment crossing the equator splits into two segments, so it is \(\theta\)-Lipschitz on the whole ball. Moreover
\[
 |b_n(x',s)|\leq\theta |s|.
\tag{M.5}
\]
Consequently \(G\) preserves both half-spaces and their common hyperplane, and sends a positive last coordinate to a positive last coordinate. Apply the full-ball contraction construction and restrict its inverse to the required half. This proves relative openness, including at boundary points. It proves as well that a change initially made in the double still has its image on the correct side.

Finitely many such coordinate balls and half-balls handle all nearby pairs. Compactness and original injectivity handle the remaining pairs by the positive-separation argument in Lemma M.2. The image is now open in \(M\) and compact, hence closed. Every component is hit by a sufficiently small value change, so the image is all of \(M\). Ranks on the source and boundary simplices persist by their positive singular-value minima. ∎

This also proves that an existing full compatible triangulation is locally bi-Lipschitz. Apply Lemma J.3 to its inverse extensions in a ball or half-ball, and apply Lemma M.1 to its forward coordinate maps. No general topological invariance-of-domain theorem is required here.

### M.3. Relative linearization inside a chart

**Lemma M.4 — Linearization with support and fixed pieces.** Let \(f:P\to\mathbb R^q\) be PD on an open part of a finite polyhedron, and let \(C\) be a compact subset of that open part. One can change \(f\), arbitrarily little in values and first derivatives, to a PD map which is PL on a neighbourhood of \(C\) and is unchanged outside a compact subset of the open part. If \(A\) is a subpolyhedron and \(f\) is already PL there, the change can fix \(A\) pointwise.

**Proof.** Repeated finite subdivision, whose mesh tends to zero, gives finite subpolyhedra
\(C\subset\operatorname{int} P_0\subset P_0\subset\operatorname{int}P_1\)
inside the open domain. For example take the union of closed vertex stars meeting \(C\) in a sufficiently fine subdivision and then a second such star neighbourhood. There is a PL function \(\chi:P\to[0,1]\), equal to one near \(P_0\) and supported inside \(P_1\): subdivide once more and assign vertex values one on the smaller neighbourhood and zero outside the larger one, then interpolate. Refine \(P_1\) to respect the smooth pieces of \(f\), the linear pieces of \(\chi\), and \(A\), making \(f\) affine on its pieces in \(A\).

Let \(T_N f\) be the affine vertex interpolant on the shape-controlled subdivision of Lemma J.2. Define
\[
 f_N=f+\chi(T_Nf-f)
\tag{M.6}
\]
on \(P_1\), and use \(f\) elsewhere. The zero collar of the support makes the formulas agree smoothly piece by piece. The derivative of the difference is
\(\chi D(T_Nf-f)+(T_Nf-f)D\chi\).
Both its terms tend uniformly to zero by Lemma J.2; \(D\chi\) is a fixed finite bound. Where \(\chi=1\), the result is PL. On \(A\), interpolation of an affine function is exactly that function, so the result fixes \(A\). ∎

For a half-space target this construction preserves the boundary condition: if \(f_n=0\) on the boundary subcomplex, its vertex interpolant is zero there too. It also preserves nonnegativity wherever it is needed, since (M.6) is a convex combination of \(f\) and its vertex interpolant. Ranks and injectivity are supplied by Lemma M.2 or M.3, as appropriate. When linearization of a full triangulation is required over a particular closed target ball or box, take \(C\) to contain the preimage of a larger compact ball or box. A small value change makes the new preimage of the smaller region lie in this linearized neighbourhood.

### M.4. Extending a prescribed small change

**Lemma M.5 — Small PD extension.** Let \(A\subset P\) be a subpolyhedron of a finite polyhedron, and let \(f:P\to M\) be PD, where \(M\) has no boundary. Every sufficiently small PD change of \(f|_A\), in values and first derivatives, extends to a PD change of \(f\) on all of \(P\). The whole change tends to zero with the prescribed change. There is also the following boundary version: if \(f\) is a full compatible triangulation of a compact manifold with boundary and the prescribed change respects its boundary, the extension can respect that boundary and remain a compatible homeomorphism.

**Proof of the extension estimate.** Use a finite triangulation respecting \(A\) and the smooth pieces of \(f\), refined until every closed simplex image lies in one target coordinate chart. Extend over the remaining simplices in increasing dimension. The zero-dimensional step chooses the prescribed values on \(A\) and keeps all other vertices at their original values. At the next step the entire simplex boundary has already been assigned, with common values on shared faces.

In a standard \(d\)-simplex with barycentric coordinates \(\lambda_0,\ldots,\lambda_d\) and barycentre \(b\), set
\[
 t=(d+1)\min_i\lambda_i,
 \qquad y=\frac{x-tb}{1-t}.
\tag{M.7}
\]
For \(t<1\), the point \(y\) lies on the boundary, and \(x=(1-t)y+tb\). Choose a fixed \(0<a<1\) and a smooth function \(\beta\) of \(t\), equal to one at zero and zero on a neighbourhood of \([a,1]\). If the assigned boundary difference in the chosen target chart is \(v(y)\), extend it by
\[
 V(x)=\beta(t)v(y)\quad(t<a),\qquad V(x)=0\quad(t\geq a).
\tag{M.8}
\]
The choice of a minimal coordinate divides the simplex into finitely many polyhedral sectors. On each, \(t\) is linear and \(y\) is a rational smooth map with denominator at least \(1-a\). On a tie the two formulas have the same \(t,y\). Further split along the inverse images of the boundary smooth pieces of \(v\); their defining affine inequalities become affine inequalities after multiplication by the positive denominator \(1-t\). Thus they are polyhedral pieces and have a finite triangulation. Formula (M.8) is PD on those pieces, continuous across their faces, and zero near its inner support edge.

There is a constant \(C_d\), depending on this old simplex and \(\beta,a\), such that
\[
 \|V\|_{C^1}\leq C_d\|v\|_{C^1}.
\tag{M.9}
\]
This is the product and chain rule in (M.8), using the bounded derivatives of (M.7). The bound is independent of any further subdivision of \(v\): its tangential derivatives are evaluated in the old boundary faces. Add \(V\) to the original target coordinate map. If the assigned changes are small, the image stays in that chart. Changing to the chart for an adjacent simplex multiplies the estimates by finite bounds on first derivatives of the smooth transition and their moduli of continuity. The finite induction therefore gives a change tending to zero on every original simplex. Its values match on shared faces by construction.

**Boundary preservation.** First perform this induction on the source boundary, using charts of \(\partial M\), while keeping all prescribed values on \(A\cap\partial P\). This assigns a small boundary change. Next extend from \(A\cup\partial P\) into a smooth double of \(M\), using the same induction. The double is supplied by the collar and signed seam charts of cobordism Theorem 1.1 and Lemma 2.1; those charts also work when no orientation is chosen. When \(f\) is a full compatible triangulation, Lemma M.3 and (M.5) put the resulting image in \(M\), preserve its boundary and make it a homeomorphism. This proves the boundary version stated here. ∎

The boundary clause of this lemma is henceforth used only for full compatible triangulations. The increasing-dimension extension has fixed, finite constants before the small changes are chosen. It does not require a uniform collar estimate over an uncontrolled family of skinny subdivisions.

These tools use the already proved common refinements, controlled interpolation and finite-piece Lipschitz lemma. The chart-linearization and relative-extension strategy is informed by Jacob Lurie's [Lecture 3](https://www.math.ias.edu/~lurie/937notes/937Lecture3.pdf) and [Lecture 5](https://www.math.ias.edu/~lurie/937notes/937Lecture5.pdf). The neighbourhood retraction estimates, partial-embedding condition, contraction proof, explicit extension formula and half-space estimates above supply the details needed here.

### M.5. Why simplex shape matters for approximation

The mesh of a subdivision measures its largest diameter. It does not, by itself, control tangent planes. On the unit two-sphere, take the three points
\[
 (0,0,1),\qquad (\sin t,0,\cos t),\qquad(-\sin t,0,\cos t),
 \qquad 0<t<\pi/2.
\]
They determine the plane \(y=0\), whereas the tangent plane at the first point is \(z=1\). These planes remain perpendicular while the triangle diameter tends to zero. If thickness is the distance from its barycentre to its boundary divided by its longest edge, the triangle's thickness is at most
\[
 \frac{1-\cos t}{6\sin t}\longrightarrow0.
\]
Indeed its barycentre has distance \((1-\cos t)/3\) from the opposite edge, and its longest edge has length \(2\sin t\). Thus the example does not satisfy a uniform positive thickness bound. This is the issue identified in Cairns, Section7, and it explains the shape condition in Lemma J.2.

The approximation also controls volume when it controls first derivatives. Here is a precise finite version. Let \(P\) be a finite pure \(m\)-complex, \(m\geq1\), and let \(f:P\to\mathbb R^q\) be a PD embedding which is locally bi-Lipschitz. Choose a fixed triangulation on whose closed simplices \(f\) is smooth. Shape-controlled vertex interpolants \(g_N\) on refining triangulations are eventually PD embeddings, their images converge to \(f(P)\), and their Euclidean parametric \(m\)-volumes converge to that of \(f\). Any subpolyhedron on which \(f\) is already PL can be kept exactly fixed.

**Proof.** Lemma J.2 gives uniform value and first-derivative convergence in the affine coordinates of each old simplex. Lemma M.2 therefore makes \(g_N\) an embedding for all sufficiently large \(N\). The Hausdorff distance of the two images is bounded by \(\sup_P|g_N-f|\): every point in either image has its partner with the same source point in the other image.

For an old full simplex \(\sigma\), use its Euclidean affine volume and an orthonormal basis \(e_1,\ldots,e_m\) of its tangent space. Put
\[
 J_f(x)=|Df_x(e_1)\wedge\cdots\wedge Df_x(e_m)|,\qquad
 V(f)=\sum_{\sigma}\int_\sigma J_f(x)\,dx.
\]
This defines the parametric volume. Subdivision does not change it, since the old simplex is partitioned into its new full simplices, whose shared faces have Euclidean \(m\)-measure zero. The same formula defines \(V(g_N)\), using its affine derivatives on the new pieces. Let \(B\) bound all old derivative norms and let \(\eta_N\to0\) bound the derivative differences. For \(\eta_N\leq1\), telescoping the two wedge products and using the triangle inequality gives, on each new full piece,
\[
 |J_{g_N}-J_f|\leq m(B+1)^{m-1}\eta_N.
\]
Every term in the telescoping sum has one column difference of norm at most \(\eta_N\) and \(m-1\) other columns of norm at most \(B+1\). Integrating over the finitely many old simplices proves
\[
 |V(g_N)-V(f)|\leq
 m(B+1)^{m-1}\eta_N\sum_\sigma\operatorname{vol}_m(\sigma)
 \longrightarrow0.
\]
If a fixed subpolyhedron is already PL, first refine the old triangulation to make that restriction affine on its pieces. The subsequent vertex interpolation is identical there. This proves the final assertion. ∎

This is the finite approximation mechanism behind Cairns, Section11. Both small values and shape-controlled small first derivatives are used; point-set convergence alone gives no corresponding volume estimate.

## N. Existence, relative extension and PL comparison

The quantitative lemmas in Section M allow us to prove the triangulation results used here. We need finite triangulations of compact smooth manifolds, exact extension of prescribed boundary triangulations, and PL comparison for compact manifolds, including disks. A locally finite existence result for noncompact manifolds without boundary is included separately. No smoothing classification or parametrized triangulation theorem is being assumed.

### N.1. Chart gluing for a compact manifold

**Theorem N.1 — Compatible smooth triangulation.** Every compact smooth manifold without boundary has a finite compatible triangulation. If a compact smooth manifold has boundary, any prescribed finite compatible triangulation of its boundary extends to one of the whole manifold, without changing that boundary map or subdividing its prescribed boundary complex. In both cases the resulting complex is a PL manifold by Theorem L.2.

**Proof for a manifold without boundary.** The zero-dimensional case is the finite set of its points. Suppose the dimension is positive. Choose finitely many smooth charts \(\psi_j:W_j\to\mathbb R^n\) for which the inverse images of the inner cubes
\(Q_1=[-1,1]^n\) cover \(M\). We use the larger cubes \(Q_2=[-2,2]^n\) and \(Q_3=[-3,3]^n\) in the same charts. Such a choice is possible: first take charts with image an open ball, identify that ball smoothly with \(\mathbb R^n\), centre each at the required point, then take a finite inner-cube subcover.

We construct a finite polyhedron \(P\) and a PD embedding \(f:P\to M\), adding one closed coordinate cube at a time. Its coordinate representations will be locally bi-Lipschitz. In addition, the domain of each cube already added will be a subpolyhedron of \(P\). The first cube has all these properties, since its map is the inverse of a smooth chart. The domain is triangulated by a finite affine cube triangulation. The empty initial domain is equally harmless.

Suppose \(P,f\) have been constructed and the next chart is \(W_j\). The closed set
\(f^{-1}(\psi_j^{-1}Q_3)\) is compact and lies in the open set \(f^{-1}W_j\). Choose a finite subpolyhedral neighbourhood of this compact set inside the open set. Lemma M.4, applied to \(\psi_j f\), makes it PL on that neighbourhood, with support compact in \(f^{-1}W_j\). Make the value and derivative changes small enough for Lemma M.2. Thus the changed map \(g\) is still a PD embedding and remains locally bi-Lipschitz. Make the value change smaller than the margin between \(Q_2\) and \(\partial Q_3\). It follows that every old point now mapping into \(\psi_j^{-1}Q_2\) lies in the linearized neighbourhood.

Consequently
\[
 A=g^{-1}(\psi_j^{-1}Q_2)
\tag{N.1}
\]
is a finite subpolyhedron, and \(\psi_jg|_A\) is a PL homeomorphism to a subpolyhedron of \(Q_2\). Indeed, on each of the finitely many linearized source pieces, the inverse image of a cube is cut out by finitely many affine inequalities. The injective affine images of these pieces are convex polytopes. Their common faces and intersections admit the common refinement of combinatorial Lemma E.1. This makes the identification with the new cube PL on the actual overlap, rather than merely a topological identification.

Glue \(P\) and \(Q_2\) by this overlap. Here are the finite-complex details. Refine both complexes to make the overlap and its identification simplicial. Subdivide barycentrically once more, making each overlap a full subcomplex. Identify the corresponding vertices and faces there, keeping every other vertex distinct. Two simplices from opposite complexes meet only in their shared overlap vertices, which form a face of each; fullness prevents a simplex outside the overlap from having all its vertices identified. Thus the union is an abstract finite simplicial complex. Its map to \(g(P)\cup\psi_j^{-1}Q_2\) is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism.

This map is PD with the required ranks. On an old piece it is \(g\) composed with an affine subdivision identification; on a new piece it is the smooth chart inverse restricted to an affine simplex. At overlap points the entire image, in \(\psi_j\) coordinates, is a union of finitely many polyhedra, and the new domain map there is a PL homeomorphism onto that union. It is locally bi-Lipschitz by Lemma M.1 applied to that PL map and its inverse. Away from the overlap the old property or the smooth-cube property applies. Thus the strengthened inductive hypothesis has been preserved.

We must also retain coverage by earlier cubes while changing their embeddings. For a previously added cube domain \(D_i\cong Q_2\), require its map in its original chart to remain of the form
\[
 x\longmapsto x+a_i(x),\qquad
 \|a_i\|_\infty<\tfrac12,\quad
 \operatorname{Lip}(a_i)<\tfrac12.
\tag{N.2}
\]
Initially \(a_i=0\). Each later linearization can be arbitrarily small in values and first derivatives. The fixed PL identifications of \(D_i\) with the current domain give finite derivative constants, so Lemma J.3 on the convex cube bounds the additional Lipschitz change. There are only finitely many steps. Allocate a summable error budget, choosing each change after the current finite constants are known; its total can be less than either strict bound in (N.2). Also keep every image of \(D_i\) in its original chart, using its compact distance from that chart's edge.

Every such changed cube still covers its original inner cube. For \(y\in Q_1\), the map \(x\mapsto y-a_i(x)\) takes \(Q_2\) to itself by the sup-norm bound and is a contraction by the Lipschitz bound. Its convergent iterates give a point with \(x+a_i(x)=y\). This proves coverage without a boundary-degree assumption.

After the last chart is added, the inner cubes cover all of \(M\). The final PD embedding is therefore a homeomorphism onto \(M\), with full ranks on the closed simplices. Theorem L.2 makes its domain a PL manifold.

**Proof with prescribed boundary.** Let \(t_0:P_0\to\partial M\) be the prescribed compatible triangulation. The collar theorem, proved in cobordism Theorem 1.1, supplies a smooth collar
\(c: \partial M\times[0,\varepsilon]\to M\)
for some positive \(\varepsilon\), since the boundary is compact. Begin with
\[
 (z,s)\longmapsto c(t_0(z),s)
 \quad\text{on }P_0\times[0,\varepsilon].
\tag{N.3}
\]
Use the compatible prism triangulation of combinatorial Lemma E.2, split at heights \(\varepsilon/3\) and \(\varepsilon/2\). Its full simplices have rank \(n\): the boundary derivative has rank \(n-1\) and the collar derivative adds a transverse direction. The lower-dimensional restrictions have their corresponding ranks. The boundary map is exactly \(t_0\). This initial embedding is locally bi-Lipschitz, by the full-triangulation estimate on \(t_0\), product coordinates, and the smooth collar diffeomorphism.

Protect the closed inner collar \(P_0\times[0,\varepsilon/3]\) pointwise. The compact complement of the open collar of height \(\varepsilon/2\) is covered by finitely many inner cubes in interior smooth charts whose closures miss the protected collar. Apply the preceding chart-gluing induction there, taking all linearization supports disjoint from the protected collar.

Also retain coverage by the initial collar through height \(\varepsilon/2\). Here is the needed quantitative condition. Cover that compact target region by finitely many small coordinate balls and boundary half-balls whose larger closures lie in the relative interior, in \(M\), of the original collar of height \(\varepsilon\). The inverse of (N.3) has the full-simplex inverse extensions used in Lemma M.3. A sufficiently small accumulated first-derivative change therefore gives \(G=\mathrm{id}+b\) with \(\operatorname{Lip}(b)<1/2\) on each larger ball or half-ball. Choose the accumulated value change smaller than the positive contraction margin of its smaller ball. Formula (M.4), and the reflected version at the actual boundary, then show that the changed collar still covers each of those smaller balls. Impose these finitely many strict budgets along with (N.2) at every subsequent step. Thus coverage through height \(\varepsilon/2\) is preserved even though the outer part of the collar is allowed to move.

It remains to check that the required finite refinements can keep the protected triangulation exactly.

First establish that sufficiently fine nested stars can be chosen while retaining every protected simplex. Let \(R\) be the protected subcomplex of a finite complex \(K\). A relative derived subdivision is obtained by stellarly subdividing every face outside \(R\), in decreasing order of dimension, using its barycentre, and leaving faces of \(R\) unchanged. On each old simplex the resulting simplices are joins of a face \(\alpha\) in \(R\), possibly empty, with barycentres of a strictly increasing chain of old faces outside \(R\) containing \(\alpha\). This description follows by coning the already subdivided boundary to the barycentre, starting with the largest face and restricting to its boundary. It proves that the constructions agree on common faces and leave the whole triangulation of \(R\) unchanged. It also makes \(R\) full after the first such subdivision: a new simplex having only protected vertices is precisely a face in \(R\).

There is a useful quantitative shrinking argument. On that first finite subdivision define the continuous PL function
\[
 \rho(x)=\sum_{v\notin R}\lambda_v(x).
\]
Fullness gives \(\rho^{-1}(0)=|R|\), and all protected vertices have value zero. Write \(d=\dim K>0\). In every later relative derived subdivision, a simplex in the closed star of \(R\) has a nonempty protected face \(\alpha\). Each of its other vertices is the barycentre of an old face \(\tau\) containing a protected vertex. All vertices of \(\tau\) lie in the previous closed star, at least one has value zero, and \(\tau\) has at most \(d+1\) vertices. Since \(\rho\) is affine on \(\tau\), its value at this barycentre is at most \(d/(d+1)\) times the previous maximum on the star. The same bound holds throughout each new simplex. Thus on the \(j\)-th subsequent closed star,
\[
 0\leq\rho\leq\left(\frac d{d+1}\right)^j.
\]
For every open neighbourhood of \(|R|\), compactness gives a positive minimum of \(\rho\) on its complement. These closed stars therefore shrink into that neighbourhood, even when a protected simplex itself has a large diameter.

Now let \(C\) be the compact region to be refined and let \(W\) be an open neighbourhood of it whose closure misses \(|R|\). Empty \(C\) needs no refinement. For any compact \(T\) disjoint from \(|R|\), the preceding shrinking argument makes the closed star of \(R\) miss \(T\) after finitely many subdivisions. Every simplex then meeting \(T\) is disjoint from \(R\), and all its subsequent subdivisions are ordinary barycentric subdivisions. If \(R\) is empty this is true from the start. The largest diameter on those finitely many simplices tends to zero: for nested vertex faces \(F\subset G\), the barycentre of \(G\) is the average of the vertices of \(F\) and the remaining vertices, so the distance of the two face barycentres is at most \(d/(d+1)\) times the diameter of the old simplex. Every pair of vertices of a barycentric simplex comes from nested faces. Iteration therefore bounds every descendant diameter by this same geometric factor. Every later simplex meeting \(T\) descends from an old one meeting \(T\), which gives uniform mesh convergence there.

Choose a positive \(\eta\) so small that the compact relative neighbourhood
\[
 T=\{x\in|K|:\operatorname{dist}(x,C)\leq4\eta\}
 \quad\hbox{lies in }W.
\]
This is possible by compactness and relative openness. Choose a subdivision in which every simplex meeting \(T\) has diameter less than \(\eta\). Let \(B_0\) be the subcomplex generated by all closed simplices meeting \(C\), and let \(B_{i+1}\) be the closed star of \(B_i\), for \(i=0,1,2\). A point of \(B_0\) is within \(\eta\) of \(C\). Inductively every simplex meeting \(B_i\) meets \(T\), has diameter less than \(\eta\), and lies within \((i+2)\eta\) of \(C\). Hence \(B_3\) lies in \(T\), and therefore in \(W\). Every point of \(C\) has all its incident simplices in \(B_0\), and every point of \(B_i\) has all its incident simplices in \(B_{i+1}\). The finitely many closed simplices not containing a given point have positive distance from it. Thus
\[
 C\subset\operatorname{int}_{|K|}|B_0|,
 \qquad |B_i|\subset\operatorname{int}_{|K|}|B_{i+1}|
 \quad(0\leq i<3).
\]
These are the required nested subpolyhedral neighbourhoods; use \(B_1\) as the inner neighbourhood and \(B_3\) as the outer one. In dimension zero they are already unions of isolated points. No face of \(R\) has been subdivided.

The preliminary relative subdivisions may refine unprotected simplices outside \(W\); they change no map values or smooth rank conditions. The following local extension retains that prepared triangulation outside its larger neighbourhood, as well as retaining the original protected complex and all its map values exactly.

For this purpose, finite refinements made away from a protected subcomplex can be extended relative to it. Choose nested closed star neighbourhoods of the compact region requiring a refinement, with the larger star still disjoint from the protected subcomplex. Refine the smaller neighbourhood as needed. Extend its induced boundary subdivision to the larger one, retaining the old triangulation at the outer boundary: process the remaining old simplices in increasing dimension, and cone the already assigned boundary triangulation to an interior point of each simplex. Their assigned boundaries agree on faces. Taking the larger star to contain the closed star of the smaller one ensures that a prescribed inner boundary face never meets the prescribed outer boundary. Nothing outside the larger neighbourhood is changed. This supplies the relative finite refinement. It applies to the linearization supports and to the overlaps (N.1), all of which have positive distance from the protected collar. The extra barycentric subdivision that makes the overlap full is likewise made on a closed star of the overlap, then extended by this procedure; any outside simplex meeting an overlap face is in that star. Thus fullness is obtained without subdividing the protected boundary complex.

The final union covers the original collar through height \(\varepsilon/2\) and the compact complement covered by the added inner cubes. It is a compatible triangulation of \(M\), retaining \(P_0\) and \(t_0\) exactly. Its boundary satisfies the hypotheses of Theorem L.2. A compact boundary with several components is handled by the same disjoint collar, with all prescribed components protected. ∎

If no boundary triangulation has been prescribed, first apply the closed case to the compact manifold \(\partial M\), then apply the relative case. The empty boundary requires no collar. All refinements in this proof are finite and preserve the actual values of the maps on the protected subcomplex.

### N.2. Comparison of two compact triangulations

**Theorem N.2 — PL uniqueness for compact smooth manifolds.** If \(f:P\to M\) and \(g:Q\to M\) are finite compatible triangulations of the same compact smooth manifold, there are arbitrarily small PD changes \(f'\) and \(g'\), still compatible homeomorphisms, for which
\[
 (g')^{-1}f':P\longrightarrow Q
\tag{N.4}
\]
is a PL homeomorphism. If \(M\) has boundary, this homeomorphism preserves the boundary subcomplexes. Thus all such triangulations have the same PL type; the original transition \(g^{-1}f\) need not itself be PL.

**Proof.** Choose finitely many closed subpolyhedra \(P_1,\ldots,P_r\) covering \(P\), with each \(f(P_j)\) in a small smooth chart region. They can be taken to be closed simplices of a sufficiently fine subdivision: by compactness their images then fit inside smaller convex coordinate boxes. For each there are nested boxes with compact closure in the chart, leaving positive margins. At boundary points these are relative boxes in a half-space. Keep all subsequent value changes smaller than these margins.

Inductively construct compatible homeomorphisms \(f_i,g_i\) such that
\[
 h_i=g_i^{-1}f_i
 \quad\text{is PL on }A_i=P_1\cup\cdots\cup P_i,
\tag{N.5}
\]
and its image \(B_i\subset Q\) is a subpolyhedron. At \(i=0\) take the original maps and the empty subpolyhedra. Suppose the claim holds at \(i\). Linearize \(f_i\) in the chart for \(P_{i+1}\), using Lemma M.4 on the preimage of a sufficiently large closed inner box. By the final paragraph of that lemma, the new map \(\widehat f_i\) is PL in chart coordinates over the preimage of an open box \(U\) which contains \(\widehat f_i(P_{i+1})\) with room to spare. Lemma M.3 makes it a compatible homeomorphism, and the change is arbitrarily small.

On the fixed subpolyhedron \(B_i\), prescribe
\[
 \widehat g_i|_{B_i}=\widehat f_i h_i^{-1}.
\tag{N.6}
\]
This is a small PD change of \(g_i|_{B_i}=f_i h_i^{-1}\). The PL map \(h_i^{-1}\) has fixed finitely many derivative bounds; after common refinement these multiply the small derivative changes of \(\widehat f_i\) by fixed constants. Apply Lemma M.5 to extend (N.6) over \(Q\), and take it sufficiently small for Lemma M.3. Thus \(\widehat g_i\) is a compatible homeomorphism.

Let \(V=\widehat g_i^{-1}(U)\). In its chart coordinates the PD homeomorphism
\(k=\psi\widehat g_i:V\to\psi(U)\)
is already PL on \(B_i\cap V\), by (N.6) and the linearization of \(\widehat f_i\). Choose a smaller box \(U'\) with closure in \(U\) still containing \(\widehat f_i(P_{i+1})\). Apply the relative part of Lemma M.4 to \(k\): its change fixes \(B_i\cap V\), has support compact in \(V\), and is PL over the preimage of \(U'\). It fixes that whole intersection because a common finite triangulation on the compact support makes its already PL restriction affine, so vertex interpolation preserves it exactly. Extend by \(\widehat g_i\) outside \(V\); take the change small enough for Lemma M.3. Call the result \(g_{i+1}\), and put \(f_{i+1}=\widehat f_i\).

On \(A_i\), equation (N.6) still holds, since the last change fixed \(B_i\). On \(P_{i+1}\), both maps are PL in the same chart over \(U'\). Their inverse transition is therefore PL there: subdivide their affine pieces and their image intersections by combinatorial Lemma E.1. This also makes the image of \(P_{i+1}\) a subpolyhedron. Combining it with \(B_i\) proves (N.5) at \(i+1\). Common refinements reconcile the two PL descriptions on their intersection, since they are restrictions of the same homeomorphism.

At every stage all extension, stability and coordinate constants are finite before the changes are chosen. Choose those changes successively within both the required margins and an arbitrarily small summable error budget. At \(i=r\), (N.5) is a PL homeomorphism on all of \(P\), giving (N.4).

For a manifold with boundary, make the subdivision respect the two boundary subcomplexes and use half-space chart boxes. Linearization preserves the zero normal coordinate on the boundary by (M.6). In (N.6), \(h_i\) respects the source boundaries because both full homeomorphisms do; the prescribed change is therefore a boundary-respecting one. Use the boundary version of Lemma M.5. The reflection estimate (M.5) ensures that every ensuing full map stays in the manifold and preserves its boundary. The last relative linearization also fixes the old PL pieces and preserves the normal-zero condition. All the remaining PL inverse and common-refinement steps work in the relative boxes exactly as in the interior. The final transition consequently carries boundary to boundary. ∎

### N.3. Locally finite existence without compactness

**Corollary N.3.** A second-countable smooth manifold without boundary has a locally finite compatible triangulation. Its tangent-star charts are PL local charts.

**Proof.** A compact exhaustion \(C_j\subset\operatorname{int}C_{j+1}\) and the smooth bump functions already constructed in the bundle chapter give functions \(\rho_j\) equal to one on a neighbourhood of \(C_j\), with support in \(\operatorname{int}C_{j+1}\) and values in \([0,1]\). Set
\[
 u(x)=\sum_{j\geq1}(1-\rho_j(x)).
\tag{N.7}
\]
Near a point of \(C_N\), all terms with \(j\geq N\) vanish; hence this is locally a finite sum and is smooth. If \(x\notin C_N\), the first \(N-1\) terms equal one, so \(u(x)\geq N-1\). Thus \(u\geq0\) is proper. For a compact manifold the finite theorem already suffices. Otherwise choose increasing regular values \(b_j\to\infty\), using the proved smooth Sard theorem; its set of exceptional real values has measure zero and cannot fill any interval. Every level \(u^{-1}(b_j)\) is a compact smooth manifold by the local inverse theorem and properness.

Triangulate each level once by Theorem N.1. Each initial region \(u\leq b_1\) and each band \(b_j\leq u\leq b_{j+1}\) is a compact smooth manifold with boundary: the regular-level local coordinate is the normal boundary coordinate at either end. Use the relative part of Theorem N.1 to extend exactly the two prescribed level triangulations over each band, and the one top triangulation over the initial region. Glue the bands by their unchanged simplicial boundary maps. The result is locally finite, since a compact subset has bounded \(u\)-values and therefore meets only finitely many bands, each with finitely many simplices. The glued map is a homeomorphism, as can be checked on each band and on their common collars. It has the required smooth ranks simplexwise, including on seams. The proof of Theorem L.2 is local and uses only finitely many simplices in a star, so it supplies the claimed PL charts. ∎

This exhaustion argument does not require a Morse function or any isolated-critical-point claim. The noncompact boundary-relative uniqueness problem is not part of the assertion just proved.

### N.4. Disks, two-disk spheres and relative fillings

**Corollary N.4 — The triangulated disk and two-disk sphere.** Every finite compatible triangulation of a smooth closed \(n\)-disk is a PL ball. A closed smooth \(n\)-manifold obtained by gluing two smooth disks along a boundary diffeomorphism has a compatible triangulation whose domain is a PL sphere. These assertions include the boundary comparisons needed for the disk-bundle application.

**Proof of the disk assertion.** We first recall why convex polytope boundaries have the standard PL sphere type. Put the origins inside two full-dimensional convex polytopes. Intersect the cones on all faces of their boundaries; these form a common finite polyhedral fan. Cutting each boundary by this fan gives convex cells with the same face-incidence relations under radial identification. Choose matching interior rays in corresponding cells and triangulate each boundary by face-chain coning at their intersections with these rays. Sending corresponding vertices to each other, affinely on each resulting simplex, is a PL homeomorphism between the two boundaries. In particular a crosspolytope boundary is PL homeomorphic to a simplex boundary. Coning this map gives the corresponding PL ball comparison.

The crosspolytope
\(\sum_{i=1}^{n+1}|x_i|\leq1\)
has a simplicial boundary, with a facet for each choice of signs. Radial normalization \(x\mapsto x/|x|\) maps that boundary homeomorphically to \(S^n\). On every closed facet it is smooth with injective derivative: the kernel of the derivative of normalization is the radial line, and that line is transverse to the facet's affine hyperplane \(\sum\epsilon_i x_i=1\). The same holds on all its faces. The half with \(x_{n+1}\geq0\) is the cone from \(e_{n+1}\) on the equatorial crosspolytope boundary. It is a standard PL ball and maps to the closed northern hemisphere.

Stereographic projection from the south pole identifies that closed hemisphere smoothly with the closed Euclidean unit disk. In coordinates its inverse is
\[
 y\longmapsto\left(\frac{2y}{1+|y|^2},
                   \frac{1-|y|^2}{1+|y|^2}\right),
 \qquad |y|\leq1.
\tag{N.8}
\]
Its derivatives have full rank, also at the boundary, since stereographic projection and its inverse are smooth diffeomorphisms on open neighbourhoods of these closed sets in the sphere and Euclidean space. We have therefore exhibited a compatible triangulation of the standard smooth disk with domain a PL ball. Pull it across a disk diffeomorphism if required. Theorem N.2 compares any other finite compatible triangulation to this one by a PL homeomorphism preserving the boundary. This proves the disk assertion. Dimension zero is its single vertex case.

**Proof of the sphere assertion.** Choose the explicit sphere triangulation just described on the boundary of the first disk and transfer its map through the gluing diffeomorphism to the second boundary. Both are compatible boundary triangulations with exactly the same abstract domain. Extend them by the relative Theorem N.1. Each resulting disk complex is a PL ball by the first assertion. The gluing map is simplicial on the common boundary, hence PL. Any PL boundary homeomorphism of PL balls extends over them: identify them with cones on the standard boundary sphere, refine to make the boundary map simplicial, and map each cone simplex linearly by sending the cone vertex to the cone vertex. This is a PL homeomorphism and has the prescribed boundary map. The glued pair of balls is therefore PL homeomorphic to the double of a standard ball, namely the standard PL sphere. The seam maps remain PD in the smooth collar charts, so the glued triangulation is compatible with the original smooth manifold. ∎

In particular the explicit two-critical-point decomposition proved in exotic-spheres Theorem C.2 gives a PL sphere, once these relative triangulation arguments have been supplied. No smooth extension of the gluing diffeomorphism over a disk is inferred.

The construction and comparison strategy can be found in Jacob Lurie's [Lecture 4](https://www.math.ias.edu/~lurie/937notes/937Lecture4.pdf) and [Lecture 5](https://www.math.ias.edu/~lurie/937notes/937Lecture5.pdf). The partial-embedding estimates, protected refinements, coverage argument, boundary extension, exhaustion and explicit standard disk used here have been supplied with their proofs. Together with Section L these establish the exact triangulation prerequisites of the following application.

## O. An eight-dimensional obstruction to integral refinement

Write \(\mathcal P_i\) for the rational combinatorial Pontryagin classes recovered from the \(\ell_i\) by combinatorial (G.11). Their recovery starts with
\[
 \ell_1=\frac{\mathcal P_1}{3},\qquad
 \ell_2=\frac{7\mathcal P_2-\mathcal P_1^2}{45}.
\tag{O.1}
\]
The smooth comparison theorem and Theorem N.1 identify these classes with the ordinary rational tangent Pontryagin classes on every compact closed smooth manifold equipped with its compatible PL structure. We now prove that these canonical rational classes do not always lift to integral cohomology on PL manifolds. This is a different assertion from loss of torsion on a smooth lens space.

### O.1. A PL manifold from the explicit disk bundle

Use the four-plane bundle \(\xi=\xi_{-1,2}\to S^4\) of exotic-spheres Section A. Its normalization is
\[
 e(\xi)=u,\qquad p_1(\xi)=6u,
 \qquad \langle u,[S^4]\rangle=1.
\tag{O.2}
\]
Let \(W=D(\xi)\), with base-first, fibre-last orientation, and let \(M=\partial W=S(\xi)\), with its induced boundary orientation. The explicit global function of exotic-spheres Section C has exactly two nondegenerate critical points. Its complete flow argument identifies \(M\) as two smooth seven-disks glued by a boundary diffeomorphism. Corollary N.4 therefore provides a compatible triangulation of \(M\) whose domain is a PL seven-sphere. Extend this exact triangulation over \(W\) by Theorem N.1, retaining a product collar as in (N.3).

Form
\[
 T=W\cup_M CM,
\tag{O.3}
\]
where \(CM\) denotes the simplicial cone on that boundary complex. This is a compact closed oriented PL eight-manifold. Inside \(W\), Theorem L.2 gives its PL charts. The cone on a PL seven-sphere is a PL eight-ball, so its vertex has a ball chart. At the seam, both halves have PL product collars, giving the chart \(\mathbb R^7\times(-\varepsilon,\varepsilon)\). For the cone collar, triangulate the frusta between two homothetic cone levels by the compatible prism construction: the positive-denominator projective map used in smooth-comparison (J.4) carries prism simplices exactly to the straight frustum simplices. The affine vertex map then supplies the PL product identification. On the \(W\) side use its protected prism collar. Orient the cone so that its boundary orientation is opposite to that of \(W\); the product seam coordinate makes these orientations agree. This verifies the manifold assertion at every point, including the vertex and seam.

The positive Thom class \(U\in H^4(W,M;\mathbb Z)\) and \(x=\pi^*u\in H^4(W;\mathbb Z)\) satisfy the already proved identities
\[
 J(U)=x,\qquad U^2=xU,\qquad
 \langle xU,[W,M]\rangle=1,
 \qquad p_1(TW)=6x.
\tag{O.4}
\]
Here \(J\) forgets the relative condition. These are exotic-spheres (B.2)–(B.5), including their orientation and relative-product proofs.

A closed cone together with a short \(W\)-collar is a contractible subpolyhedron \(A_T\subset T\). The collar shrinks to the cone base, and the cone contracts to its vertex. For the exact excision step, remove \(CM\setminus M\). Its closure \(CM\) lies in the interior of \(A_T\), because that subpolyhedron also contains a positive-width \(W\)-collar. The remaining pair is \((W,\text{closed collar})\). The inclusion of \(M\) into the closed collar is a deformation equivalence, so the pair exact sequences identify its cohomology with \(H^*(W,M)\). These identifications respect relative cup products. Since \(T\) and \(A_T\) are connected and \(A_T\) is contractible, the pair exact sequence makes the forgetful map an isomorphism in every positive degree. Thus the Thom theorem and (O.4) give
\[
 H^q(T;\mathbb Z)=
 \begin{cases}\mathbb Z&q=0,4,8,\\0&\text{otherwise},\end{cases}
 \qquad
 a^2=b,\qquad \langle b,[T]\rangle=1,
\tag{O.5}
\]
where \(a\) comes from \(U\) and \(b\) from \(xU\). Evaluation has the sign shown because the orientation of \(T\) restricts to that of \(W\), so its relative restriction is \([W,M]\). In particular its rational middle form has matrix \((1)\), and
\[
 \sigma(T)=1.
\tag{O.6}
\]

### O.2. Computing the first class without assuming locality

It is not sufficient to say that \(\mathcal P_1(T)\) agrees with the smooth tangent class on the interior of \(W\). The construction in Sections F–G defines classes on closed PL rational homology manifolds; an unproved restriction theorem for open regions would introduce a gap. We instead compute the required coefficient from actual identical fibres in a smooth double.

**Lemma O.1 — The first class of the coned filling.** In the normalization (O.5),
\[
 \ell_1(T)=2a,\qquad \mathcal P_1(T)=6a.
\tag{O.7}
\]

**Proof.** Write \(\ell_1(T)=\lambda a\), with \(\lambda\in\mathbb Q\). Choose the even sphere dimension \(m=10\), let \(v\in H^m(S^m;\mathbb Z)\) be positive, and put \(k=m+4=14\). The product has dimension \(18<2k-1=27\), so the fully proved rational cohomotopy comparison, combinatorial Theorem C.3, applies. Its degree-\(k\) integral cohomology is the infinite cyclic group generated by \(a\times v\), by (O.5) and integral Künneth. The rational isomorphism therefore supplies a continuous map
\[
 F:T\times S^m\longrightarrow S^k,
 \qquad F^*u_k=d(a\times v)
\tag{O.8}
\]
for some positive integer \(d\). To see the integral assertion, represent the rational generator under the isomorphism by a fraction of a cohomotopy group element, and clear its denominator. The coefficient group here is torsion-free, so equality after rationalization is equality integrally. A negative denominator can be replaced by its positive version using the group inverse.

The restriction to \(A_T\times S^m\) is null-homotopic: this domain retracts to \(S^m\), and every map \(S^m\to S^k\) is null for \(m<k\), by the proved cellular compression and sphere connectivity. Homotopy extension for the finite CW pair makes \(F\) constant, say at \(z_0\), on all of \(A_T\times S^m\), without changing its cohomology pullback. Relative PL approximation, combinatorial Lemma E.3, then makes the map PL while keeping that constant region exactly fixed.

Let \(Z=W\cup_M(-W)\) be the smooth oriented double, built by the proved smooth collar gluing. Its compatible triangulation uses the same first \(W\), the same boundary triangulation and a copied triangulation on its second half. The seam charts have full simplex ranks; subdivision, if needed for the PL map, preserves this. Define a PL map
\[
 F_Z:Z\times S^m\longrightarrow S^k
\tag{O.9}
\]
by using exactly the just constructed map on the first \(W\times S^m\) and the constant \(z_0\) on the second half. The first map was already constant on a whole seam collar, so these rules agree. Refine the shared source pieces and extend their induced boundary subdivision over the second half by the finite relative refinement construction. The constant map is affine on every second-half piece, so the resulting map is PL with the claimed values.

For a generic target value different from \(z_0\), the two maps (O.8) and (O.9) have exactly the same fibre in the interior of the common first \(W\times S^m\). Choose the value outside the union of their finite target skeleta. Their induced orientations agree, because both source orientations there are \(W\) first, sphere last, and both use the same positive target sphere. Their signatures are consequently equal.

Let \(c\in H^4(Z;\mathbb Z)\) be extension by zero of the positive relative Thom generator on the first half. Its restrictions are \(x\) on the first \(W\) and zero on the second. These restrictions determine it uniquely: Mayer–Vietoris in degree four has zero outside terms \(H^3(M)=H^4(M)=0\), and identifies \(H^4(Z)\) with the two half groups. The same product Künneth computation as in (O.8), and the two restrictions of \(F_Z\), give
\[
 F_Z^*u_k=d(c\times v).
\tag{O.10}
\]
The tangent bundle of the smooth double restricts to \(TW\) on that half. Relative cup and evaluation, using (O.4), give
\[
 \langle p_1(TZ)c,[Z]\rangle
 =\langle 6xU,[W,M]\rangle=6.
\tag{O.11}
\]

Apply the fibre formula to both closed PL products. Stabilization gives \(\ell_1(T\times S^m)=\operatorname{pr}_T^*\ell_1(T)\). For the smooth double, smooth comparison gives \(\ell_1(Z\times S^m)=p_1(T(Z\times S^m))/3\); the sphere tangent is stably trivial, so its first class contributes zero. The equal fibre signatures, (O.5), (O.8), (O.10) and (O.11) now give
\[
 d\lambda
 =\langle \operatorname{pr}_T^*(\lambda a)
              \smile d(a\times v),[T]\times[S^m]\rangle
 =\frac d3\langle p_1(TZ)c,[Z]\rangle
 =2d.
\tag{O.12}
\]
There is no external-product sign: the first factor has sphere degree zero. Cancel the nonzero integer \(d\) to obtain \(\lambda=2\), and apply (O.1). ∎

### O.3. The denominator is a genuine obstruction

The top signature normalization of combinatorial Theorem G.3 says
\(\langle\ell_2(T),[T]\rangle=\sigma(T)=1\).
By (O.5), \(\ell_2(T)=b\). Substituting this and (O.7) into (O.1) gives
\[
 \mathcal P_2(T)
 =\frac{45\ell_2(T)+\mathcal P_1(T)^2}{7}
 =\frac{45+36}{7}\,b
 =\frac{81}{7}\,b.
\tag{O.13}
\]
Since \(H^8(T;\mathbb Z)=\mathbb Zb\), its integral-to-rational coefficient map has image precisely \(\mathbb Zb\). The number \(81/7\) is not an integer. Hence there is no integral class whose rationalization is \(\mathcal P_2(T)\).

**Theorem O.2 — No integral refinement on all PL manifolds.** The canonical rational combinatorial Pontryagin classes do not admit integral refinements on all closed PL manifolds. In particular no integral theory can refine these classes and agree with the smooth tangent Pontryagin classes everywhere in the smooth case. The PL eight-manifold (O.3) has no smooth structure compatible with its displayed PL structure.

**Proof.** An integral refinement in degree eight would have to supply an integral lift of (O.13) on this particular manifold; none exists. If a compatible smoothing existed, Theorem N.1, Theorem N.2 and PL invariance would identify the same combinatorial class with the rationalization of its integral tangent \(p_2\), by smooth comparison. That is the same impossible lift. ∎

The assertion concerns integral refinement of the constructed rational classes. It is not a proof that every possible unrelated integral invariant of PL manifolds is impossible, or that an integral torsion class on a smooth lens space fails PL invariance. Nor does it assert a statement about smoothings compatible only with the underlying topological space. Those would require additional hypotheses or theorems.

The eight-dimensional construction is due to René Thom and is presented in John Milnor's [1956 manuscript](https://faculty.tcu.edu/gfriedman/notes/milnor3.pdf), Section4, and the freely accessible [1957 lectures, with notes by James Stasheff](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf), ChapterXVI, Section5, Lemma7 and Example2. The compatible relative triangulation, PL-ball comparison, coned-manifold charts and the fibre calculation (O.8)–(O.12) above supply the prerequisites and the precise class calculation used in this course.

### O.4. The odd-parameter family

The same construction works for every odd integer \(s\). Take
\[
 h=(1-s)/2,\qquad j=(1+s)/2,\qquad
 \xi_s=\xi_{h,j},\qquad W_s=D(\xi_s).
\]
The bundle computations give \(e(\xi_s)=u\) and \(p_1(\xi_s)=2su\). The already proved quaternionic function applies to every pair with \(h+j=1\); its two critical points give a two-disk sphere boundary. Therefore the relative triangulation and cone construction give a closed oriented PL eight-manifold \(T_s\), with generators \(a_s,b_s\) satisfying
\[
 H^*(T_s;\mathbb Z)=\mathbb Z[a_s]/(a_s^3),\qquad
 |a_s|=4,\quad b_s=a_s^2,\quad \langle b_s,[T_s]\rangle=1.
\]
Its rational characteristic classes are
\[
 \mathcal P_1(T_s)=2s\,a_s,\qquad
 \mathcal P_2(T_s)=\frac{45+4s^2}{7}\,b_s.
\]
In particular the second class has an integral lift exactly when \(s\equiv1\) or \(-1\pmod7\). Whenever that congruence fails, this PL structure admits no compatible smoothing.

**Proof.** The parameter formulas are integers because \(s\) is odd; they have sum one and difference \(j-h=s\). Theorem A.3 and the global function in exotic-spheres Section C.3 supply the bundle classes and the smooth two-disk boundary with their exact signs. Corollary N.4 and relative Theorem N.1 apply without any change of scope. In the disk/sphere pair, \(J(U_s)=x_s\), \(U_s^2=x_sU_s\), and \(\langle x_sU_s,[W_s,\partial W_s]\rangle=1\), since the Euler class is still \(u\). The excision and contractible-region argument of (O.5) therefore gives the displayed integral ring and the positive signature one.

To compute the first class, repeat the actual fibre comparison of Lemma O.1 with this filling. The dimensions remain \(m=10,k=14\), and the degree-four group is still infinite cyclic. Thus a positive multiple \(d(a_s\times v)\) is realized by a sphere map, made constant on the cone-plus-collar and copied to the smooth double. Its two generic oriented fibres are identical. The double evaluation (O.11) becomes
\[
 \langle p_1(TZ_s)c_s,[Z_s]\rangle
 =\langle 2s\,x_sU_s,[W_s,\partial W_s]\rangle=2s.
\]
If \(\ell_1(T_s)=\lambda_s a_s\), the fibre formula gives \(d\lambda_s=(2s/3)d\). Hence \(\mathcal P_1=3\ell_1=2s\,a_s\). The top signature formula gives \(\ell_2(T_s)=b_s\), so (O.1) proves the stated second class.

Its coefficient is integral exactly when \(45+4s^2\equiv0\pmod7\), equivalently \(s^2\equiv1\pmod7\). Since \(\mathbb Z/7\) is a field, \((s-1)(s+1)=0\) is equivalent to the two stated residues. An integral coefficient supplies precisely that multiple of \(b_s\); a fractional coefficient cannot be the rationalization of an integral class. The incompatible-smoothing conclusion then follows by the same smooth comparison as Theorem O.2. ∎

For \(s=3\) this is the original coefficient \(81/7\); for \(s=7\) it is \(241/7\). The integral-lift congruence is only a necessary smoothing test: no compatible smoothing is inferred when it holds. This family is presented in Milnor's Section4 and the 1957 lectures, Example2; the fibre argument above supplies the precise class calculation for our construction.

## P. Six exercises with complete solutions

**Exercise P.1 — Easy: a boundary reflection.** Let \(b\) be \(\theta\)-Lipschitz on a convex upper half-ball, with \(b_n(x',0)=0\) and \(\theta<1\). Prove that its even-tangential, odd-normal reflection is \(\theta\)-Lipschitz on the full ball, and that \(x+b(x)\) carries a positive normal coordinate to a positive normal coordinate.

**Solution.** Reflection of the source and of the target normal coordinate is an isometry, so the same bound holds within either half. For points in opposite halves, split their joining segment where it meets the equator; continuity there and the triangle inequality give the sum of the two Lipschitz bounds, equal to \(\theta\) times the whole segment length. For \(s>0\), compare the normal component with its zero value at \((x',0)\): \(|b_n(x',s)|\leq\theta s\). Thus \(s+b_n(x',s)\geq(1-\theta)s>0\). The normal-zero condition also keeps the equator in itself. This is the side-preservation step used in Lemma M.3.

**Exercise P.2 — Easy: the explicit standard disk.** Verify that radial projection from a crosspolytope facet to the sphere has injective derivative. Explain why its northern half gives a compatible triangulation of the standard smooth disk with domain a PL ball.

**Solution.** For \(q(x)=x/|x|\), differentiation gives \(Dq_x(v)=(v-q(x)\langle q(x),v\rangle)/|x|\), whose kernel is the radial line. A facet lies in \(\ell(x)=1\), and its tangent vectors satisfy \(\ell(v)=0\), so a nonzero radial vector cannot be tangent. Restriction to that tangent space is injective, also on all smaller face tangent spaces. The northern half of the boundary complex is the cone from its northern vertex on the equatorial crosspolytope sphere, a PL ball. Radial normalization takes it to the closed northern hemisphere. Composing with stereographic projection from the south pole, whose inverse is (N.8), is a smooth map of maximal rank on every closed simplex, and a homeomorphism to the closed unit disk. The equator is a boundary subcomplex, with its own full ranks.

**Exercise P.3 — Medium: coverage during chart gluing.** Prove that a continuous map \(x\mapsto x+a(x)\) on \(Q_2=[-2,2]^n\), with \(\|a\|_\infty<1/2\) and \(\operatorname{Lip}(a)<1/2\), covers \(Q_1=[-1,1]^n\). Explain how finite chart gluing retains this estimate.

**Solution.** For each \(y\in Q_1\), the map \(x\mapsto y-a(x)\) has every coordinate of magnitude below \(3/2\), so it preserves \(Q_2\). Its contraction ratio is less than \(1/2\). Starting anywhere in \(Q_2\), the successive differences decrease geometrically, hence the iterates converge to its unique fixed point \(x\), which solves \(x+a(x)=y\). Each later PD perturbation can have its value change and derivative change chosen arbitrarily small. On the original convex cube, the finite-piece derivative bound in Lemma J.3 controls its Lipschitz change. At each finite step include the fixed PL identification and chart-transition constants before choosing that perturbation. Allocate a total value budget below \(1/2\) and a total Lipschitz budget below \(1/2\). Their finite sums then retain the two strict inequalities on every earlier cube.

**Exercise P.4 — Medium: the ring of the coned filling.** For a rank-four bundle on \(S^4\) with Euler class \(u\), derive the ring (O.5), including the sign of \(a^2[T]\).

**Solution.** The disk/sphere pair has positive Thom generator \(U\), and its Thom isomorphism identifies its positive groups with \(H^{*-4}(S^4;\mathbb Z)\). Thus the groups occur only in degrees four and eight. The forgetful map sends \(U\) to \(x=\pi^*u\); relative cup gives \(U^2=J(U)U=xU\). The positive base local generator and positive fibre local Thom generator evaluate on the base-first, fibre-last relative fundamental class as the product \(1\cdot1\), so \(\langle xU,[W,M]\rangle=1\). A contractible cone-plus-collar in the coned filling gives the pair isomorphism with \((W,M)\) by excision and the positive-degree forgetful isomorphism by the exact sequence. Consequently \(U,xU\) give \(a,b\), with \(a^2=b\). The closed fundamental class restricts to \([W,M]\), because the orientation extends that of \(W\), so \(\langle b,[T]\rangle=1\). Its middle form is therefore \((1)\).

**Exercise P.5 — Hard: justify the first class at the cone.** Reconstruct \(\mathcal P_1(T)=6a\) without presuming that combinatorial classes restrict to tangent classes on an open smooth region. State and check the sphere dimensions and every use of the constant region.

**Solution.** Stabilize with \(m=10\); the tested target has dimension \(k=14\), and the source has dimension \(18<27=2k-1\). Rational cohomotopy comparison realizes a positive multiple \(d(a\times v)\) as a sphere pullback. The cone-plus-collar region is contractible, so its product with \(S^{10}\) retracts to that sphere. Its map to \(S^{14}\) is null because \(10<14\). Homotopy extension makes the map constant there, and relative PL approximation retains the constant exactly. Copy its values on the first half of the smooth double, and use the constant on the second half; the collar makes them agree. At a generic value different from that constant, both PL maps have exactly the same oriented fibre in the common first half. On the double the pullback is \(d(c\times v)\), where \(c\) is extension of the relative Thom generator; Mayer–Vietoris determines its restrictions \((x,0)\) uniquely. The evaluation of \(p_1(TZ)c\) is \(6\), by the relative evaluation \(6xU[W,M]\). Smooth comparison and stabilization equate the two fibre signatures to \(d\lambda\) and \(2d\), respectively, where \(\ell_1(T)=\lambda a\). Hence \(\lambda=2\), and \(\mathcal P_1=3\ell_1=6a\). The constant region is used both to make the copying continuous and to exclude all second-half and cone points from the actual fibres; no restriction theorem for open regions has been inserted.

**Exercise P.6 — Hard: distinguish two rational/integral statements.** Explain why the lens-space example \(p_1(TL_5^5)=3t^2\ne0\), with zero rationalization, does not by itself prove failure of integral PL refinement. Then prove the obstruction from \(T\).

**Solution.** The lens-space calculation shows that the integral coefficient map kills a particular nonzero torsion class. It compares the class with its rational image on the same smooth manifold. It neither constructs a PL manifold lacking an integral lift nor compares two smooth structures by a PL homeomorphism. For \(T\), the compatible triangulations and disk comparison make the coned filling a closed PL eight-manifold. Its degree-eight integral group is \(\mathbb Zb\), with \(b[T]=1\). Its signature is one and its first rational Pontryagin class is \(6a\), with \(a^2=b\). Therefore \(45\ell_2=7\mathcal P_2-\mathcal P_1^2\) gives \(\mathcal P_2=(81/7)b\). The image of integral cohomology in the rational group is exactly the integer multiples of \(b\); this coefficient is outside that image. Thus the canonical rational PL class has no integral refinement on this manifold, and smooth comparison excludes every compatible smoothing of its PL structure.

## Sources and proof scope

Stewart S. Cairns, [The triangulation problem and its role in analysis](https://www.ams.org/journals/bull/1946-52-07/S0002-9904-1946-08610-3/S0002-9904-1946-08610-3.pdf) (1946), Sections7–11, explains the coordinate-gluing, simplex-shape and approximation mechanisms. Cairns credits J. H. C. Whitehead for the triangulation uniqueness and controlled interpolation results and Hassler Whitney for smooth embedding and approximate-normal constructions. The finite construction, relative estimates and approximation proofs used here are supplied in the chapter.

John Milnor, [On the relationship between differentiable manifolds and combinatorial manifolds](https://faculty.tcu.edu/gfriedman/notes/milnor3.pdf) (27November1956), AppendixII, Lemma7, gives the tangent-star argument. Its W1–W3 statements refer to Whitehead for triangulation existence and comparison. Sections L–N give the complete local-degree, boundary, finite chart-gluing, disk and exhaustion arguments in the scopes stated here.

Jacob Lurie's [Topics in Geometric Topology course](https://www.math.ias.edu/~lurie/937.html), Lectures2–5 (2009), supplies the PD linearization and chart-gluing strategy. The rational neighbourhood retraction, explicit small extension, partial-embedding hypothesis, protected refinements and coverage estimates explain the quantitative details needed for this construction.

The coned-filling obstruction is due to René Thom, as credited in Milnor's Section4 and [Lectures on Characteristic Classes, with notes by James Stasheff](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf) (1957), ChapterXVI, Section5, Lemma7 and Example2. Section O proves the integral obstruction using an equal-fibre comparison in a smooth double. The conclusion concerns the displayed PL structure and its canonical rational classes; it does not assume a classification or a topological-invariance theorem.

All proofs, examples and solutions here are independently authored. The human works and their contributions are cited at the constructions they inform.
