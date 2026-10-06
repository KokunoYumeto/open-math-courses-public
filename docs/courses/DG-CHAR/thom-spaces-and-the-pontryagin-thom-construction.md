# Thom spaces, transversality and the Pontryagin–Thom construction

Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0.

A closed manifold gives a map to a universal Thom space by collapsing the complement of a normal tube. Conversely a transverse map gives a manifold as its inverse image of zero. We prove that these constructions identify homotopy and bordism in the stated dimension range, including the topological, analytic and relative-embedding foundations they need.

The exact earlier proofs are in [Vector bundles](vector-bundles-and-their-constructions.md), [Classifying maps](grassmannians-and-classifying-maps.md), [Thom and Euler classes](thom-classes-and-euler-classes.md), [Schubert cells](schubert-cells-and-grassmannian-cohomology.md), [Frame fields and primary obstructions](frame-fields-and-primary-obstructions.md), [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), [Characteristic numbers](characteristic-numbers-and-projective-product-independence.md) and [The oriented cobordism ring](the-oriented-cobordism-ring.md). This chapter develops the geometric part of assigned lesson13. Its rational homotopy estimates and rational cobordism computation remain for the continuation.


## A. Sard's theorem and the measure-zero prerequisite

The inverse-function theorem in the manifold-duality chapter tells us what a transverse inverse image looks like. Sard's theorem supplies the regular values needed to make one. We prove the smooth theorem here, including the elementary measure argument in its proof.

A subset of \(\mathbb R^b\), \(b\geq1\), has **measure zero** if for every \(\varepsilon>0\) it has a countable cover by open coordinate boxes whose total \(b\)-dimensional volume is less than \(\varepsilon\). A box's volume is the product of its edge lengths. Countable unions of zero-measure sets have measure zero: use budgets \(\varepsilon/2^{i+1}\) for the individual covers. Cubes give the equivalent definition, since subdividing each box into sufficiently small cubes enlarges its covering volume by an arbitrarily small amount; distribute those extra amounts in the same geometric budgets.

A zero-measure set contains no nonempty open box. For a closed smaller box inside such an open box, any countable open cover has a finite subcover by compactness. A finite box cover has total volume at least the volume of the smaller box: partition at all its box-coordinate endpoints, so each small grid box inside is counted at least once. This contradicts a covering volume smaller than that positive volume. Consequently the complement of a zero-measure set is dense.

**Lemma A.1 — Compact slice lemma.** Suppose \(K\subset\mathbb R\times\mathbb R^b\) is compact, \(b\geq1\), and every slice
\(K_t=\{y:(t,y)\in K\}\) has measure zero in \(\mathbb R^b\). Then \(K\) has measure zero in \(\mathbb R^{b+1}\).

**Proof.** Place \(K\) in \([-R,R]\times[-R,R]^b\), taking \(R>0\). Fix \(\varepsilon>0\). For each \(t\in[-R,R]\), cover the compact \(K_t\) by finitely many open boxes of total volume less than \(\varepsilon\), and call their union \(O_t\). Empty slices use the empty union. There is an interval \(J_t\) about \(t\) with
\[
K\cap(J_t\times\mathbb R^b)\subset J_t\times O_t.
\tag{A.1}
\]
Otherwise points \((t_i,y_i)\in K\), with \(t_i\to t\) and \(y_i\notin O_t\), have by compactness a subsequence converging to a point \((t,y)\in K\) outside \(O_t\), contradicting its slice cover.

The intervals \(J_t\) cover the compact base interval. A finite subcover has a Lebesgue number, by the compact metric argument already proved in the frame-obstruction chapter. Partition the base into sufficiently short closed subintervals, each inside one of those \(J_t\). On each such subinterval cover \(K\) by its product with the finitely many boxes making up the corresponding \(O_t\). The total product volume is less than \(2R\varepsilon\). Enlarge the finitely many base subintervals slightly to open intervals, staying in their assigned \(J_t\); their extra covering volume can be made less than \(\varepsilon\). Thus the compact set has an open-box cover of volume less than \((2R+1)\varepsilon\). Letting \(\varepsilon\) tend to zero proves the claim. This is the special slice argument we need; no general Fubini theorem is being assumed. ∎

We also record a dimension estimate. If a smooth map sends a compact cube in \(\mathbb R^a\) into \(\mathbb R^b\) with \(a<b\), its image has measure zero. Bounded first derivatives give a Lipschitz bound on that cube by integrating the derivative along each line segment. Divide the cube into \(N^a\) small cubes. Each image lies in a target cube of edge at most \(C/N\), with \(C\) fixed, so their total target volume is at most \(C' N^{a-b}\), tending to zero. Cover an open source by countably many compact cubes contained in it to obtain the same result globally. At \(a=0\), a point has zero measure by arbitrarily small boxes.

**Theorem A.2 — Smooth Sard theorem.** If \(f:W\to\mathbb R^b\) is smooth on an open \(W\subset\mathbb R^a\), \(b\geq1\), the set of its critical values has measure zero. Here a critical point is one where \(\operatorname{rank}Df<b\); a regular value has no critical point in its inverse image, which may be empty. Thus regular values are dense.

**Proof.** Induct on the source dimension \(a\), with the point case just established. The dimension estimate already treats \(a<b\). In the remaining case let \(C\) be the critical set and let
\[
C_s=\{x: D^\alpha f(x)=0\text{ for every multi-index }\alpha
\text{ with }1\leq|\alpha|\leq s\},\qquad s\geq1.
\tag{A.2}
\]
These are closed subsets of \(W\), nested in \(C\). We treat the three parts of this filtration.

First consider \(C\setminus C_1\). If \(b=1\), this set is empty. Otherwise at each of its points some first derivative is nonzero. Permute source and target coordinates so that \(\partial f_1/\partial x_1\ne0\). The already proved inverse-function theorem makes
\(x\mapsto(f_1(x),x_2,\ldots,x_a)\) a diffeomorphism on a neighbourhood. In these source coordinates the map has the form
\[
f(t,z)=(t,g(t,z)),\qquad z\in\mathbb R^{a-1}.
\tag{A.3}
\]
Its derivative has first row \((1,0,\ldots,0)\), so it is critical exactly when
\(D_z g(t,z)\) has rank less than \(b-1\). By induction, for every fixed \(t\) the critical values of this slice map have measure zero in \(\mathbb R^{b-1}\).

Take any compact cube in this coordinate neighbourhood and the image of its closed critical subset. That image is compact; its \(t\)-slice lies in the critical values of the slice map. Lemma A.1 therefore makes its full image have measure zero. A countable collection of such compact cubes covers all these neighbourhoods: Euclidean space has a countable rational-box basis, and every point has a box with closure inside one permitted neighbourhood. Countable unions show that \(f(C\setminus C_1)\) has measure zero.

Next consider \(C_s\setminus C_{s+1}\), for any fixed \(s\geq1\). A derivative of order \(s+1\) is nonzero there. Choose a scalar component derivative \(h=D^\alpha f_i\) of order \(s\) whose first derivative is nonzero at that point. The function \(h\) vanishes on \(C_s\). Applying the inverse-function theorem to \((h,x_2,\ldots,x_a)\), after a coordinate permutation, puts \(C_s\) inside the coordinate hypersurface \(h=0\). On that hypersurface every point of \(C_s\) is critical for the restriction of \(f\), since its original first derivative is zero. The induction hypothesis in source dimension \(a-1\), now with target dimension \(b\), makes the image of this subset have measure zero. Countably many such neighbourhoods cover \(C_s\setminus C_{s+1}\). Its image is consequently null too.

Finally choose \(s\) so large that \((s+1)b>a\). On a compact cube \(Q\subset W\), derivatives of order \(s+1\) are bounded. If \(x\in C_s\cap Q\) and \(x+v\in Q\), Taylor's remainder gives
\[
\|f(x+v)-f(x)\|\leq K\|v\|^{s+1},
\tag{A.4}
\]
with one constant \(K\) for this cube. For completeness, restrict each component to the line \(x+tv\) and integrate its \((s+1)\)-st derivative \(s+1\) times. All derivatives of orders one through \(s\) at \(t=0\) vanish, giving the integral remainder with weight \((1-t)^s/s!\). The bounded partial derivatives bound that directional derivative by a fixed multiple of \(\|v\|^{s+1}\), which proves (A.4).

Subdivide \(Q\) into \(N^a\) cubes. For each small cube meeting \(C_s\), choose one such point \(x\). Formula (A.4) places the image of its entire intersection with \(C_s\) inside a target cube of edge at most \(K'/N^{s+1}\). The total covering volume is at most
\[
K'' N^{a-(s+1)b}\longrightarrow0.
\tag{A.5}
\]
Thus \(f(C_s\cap Q)\) is null. Countably many interior compact cubes cover \(W\), so \(f(C_s)\) is null. The decomposition of \(C\) into \(C\setminus C_1\), the finitely many differences through this \(C_s\), and \(C_s\) completes the proof. Density follows from the initial open-box argument. ∎

For a smooth map between Hausdorff second-countable manifolds, the same statement holds in every target chart. Cover the relevant source open sets by countably many coordinate charts and apply Theorem A.2 to each coordinate map. Their critical images have a countable union of measure-zero coordinate sets, so their complement is dense in that target chart. This proves the manifold regular-value assertion used below.

## B. Cellular approximation with its local proof

The Thom-space connectivity argument needs cellular approximation, beyond the finite simplicial approximation already proved. We give the full CW version, using the explicit homotopy extension in Section E of [Frame fields and primary obstructions](frame-fields-and-primary-obstructions.md).

**Lemma B.1 — Removing a higher target cell.** Suppose \(Z\) is a finite CW complex, \(e^b\) is one of its highest-dimensional cells, and \(F:I^a\to Z\) sends its boundary into a subcomplex not containing \(e^b\). If \(b>a\), there is a homotopy relative boundary after which the image misses \(e^b\).

**Proof.** Let \(W=Z\setminus e^b\), which is a closed subcomplex because this cell has maximal dimension. Identify its interior with \(\mathbb R^b\), and choose closed coordinate balls \(B_1,B_2\) of radii one and two. These are compact subsets inside the cell, hence closed in the Hausdorff \(Z\). If \(F^{-1}(B_1)\) is empty, the origin is already missed. Otherwise that inverse image is compact, separated in the source cube from both its boundary and the closed complement of \(F^{-1}(\operatorname{int}B_2)\).

Subdivide the source into small cubes. Let \(K_1\) be the union of the closed cubes meeting \(F^{-1}(B_1)\), and let \(K_2\) include all their neighbouring cubes. Choose the mesh sufficiently small that \(K_2\) is in the source interior and lies in \(F^{-1}(\operatorname{int}B_2)\). Also make the coordinate oscillation of \(F\) on each such cube less than \(1/4\). This is possible by uniform continuity on the compact \(F^{-1}(B_2)\).

Triangulate this finite cubical union compatibly: triangulate each boundary face first, and cone to the centre of each cube, dimension by dimension. Let \(G\) be the affine interpolation of the values of \(F\) at these vertices, interpreted in \(\mathbb R^b\). On each simplex,
\(\|G(x)-F(x)\|<1/4\), since its vertices all lie within that oscillation of \(F(x)\). Choose a piecewise affine function \(\chi\) equal to one on \(K_1\) and zero on the boundary of \(K_2\), with values in \([0,1]\). The extra ring of cubes permits this: assign one to vertices in \(K_1\), zero to the other vertices, then interpolate. Set, in the cell coordinates,
\[
F_t(x)=F(x)+t\chi(x)\bigl(G(x)-F(x)\bigr)
\quad(x\in K_2),
\tag{B.1}
\]
and use the unchanged \(F\) outside \(K_2\). The formula agrees on its boundary, stays in the open cell on the modified set, and fixes the source boundary.

Every point outside \(K_1\) that is in \(K_2\) has original coordinate norm greater than one; on its boundary limit the norm is at least one. Its final norm is consequently at least \(3/4\). Points outside \(K_2\) remain outside \(B_1\). Thus \(F_1^{-1}(B_{1/2})\subset K_1\), where \(F_1=G\). The image of \(G\) there lies in finitely many affine subspaces of dimension at most \(a<b\). They cannot cover the open \(b\)-ball: the complement of each proper affine subspace is open dense, and a finite intersection of such complements remains dense, by successively choosing a smaller ball. Choose \(p\) in that ball outside this finite image. The final map misses \(p\) everywhere.

Radially retract \(Z\setminus\{p\}\) onto \(W\). In the characteristic \(b\)-disk, draw the ray from the interior point representing \(p\) through every other point and extend it to the boundary. Interpolate along that same ray to obtain a deformation fixing the disk boundary. Its endpoint is continuous away from \(p\): the positive intersection of a ray with the unit sphere is given by the positive root of its quadratic equation. It stays away from \(p\) during the interpolation. On \(W\) use the constant deformation. These agree on the attaching boundary and descend through the attachment quotient; its restriction away from \(p\), and its product with \(I\), remain quotient. Composing \(F_1\) with this deformation removes the whole cell and keeps its prescribed boundary fixed. Combining the two homotopies proves the lemma. ∎

**Theorem B.2 — Full cellular approximation.** Every continuous map \(f:X\to Y\) of CW complexes is homotopic to a cellular map \(g\), meaning \(g(X^a)\subset Y^a\) for all \(a\). If \(f\) is already cellular on a subcomplex \(A\subset X\), the homotopy fixes \(A\).

**Proof.** Induct over source dimension. At the \(a\)-th step the map is already cellular on \(X^{a-1}\), and remains its original cellular map on \(A\). For a characteristic \(a\)-cube, its image is compact and therefore lies in a finite target subcomplex, by the full compact-subcomplex lemma in the classifying-map chapter. Its boundary lies in \(Y^{a-1}\). Choose a highest-dimensional target cell of that finite subcomplex with dimension greater than \(a\), and remove it by Lemma B.1. Repeating this finitely many times leaves the image in \(Y^a\), with the boundary fixed throughout. If the source cell belongs to \(A\), leave it fixed instead. The same argument at \(a=0\), with empty source boundary, moves each vertex to a target vertex.

Do this for all \(a\)-cells. Their homotopies agree on \(X^{a-1}\), so glue to a homotopy on \(X^a\cup A\), fixing \(X^{a-1}\cup A\). The weak topology and quotient-times-interval lemma make it continuous, including an arbitrary number of cells. Extend it to \(X\) by the already proved CW homotopy extension property.

Perform the \(a\)-th step during
\([1-2^{-a},\,1-2^{-(a+1)}]\), beginning with \(a=0\), and take the stabilized value at time one. Every characteristic \(a\)-disk is fixed after its own step, so its whole disk-cylinder homotopy is continuous at time one. The quotient-times-interval test consequently gives continuity on \(X\times I\), despite infinitely many dimensions. The endpoint is cellular and the homotopy fixes \(A\). ∎

For CW pairs, first approximate the map on the source subcomplex into the target subcomplex, extend that homotopy, and then apply Theorem B.2 to the whole map fixing the now cellular subcomplex. This proves cellular approximation through maps of pairs too.

One immediate consequence will be used for Thom spaces. A CW complex with just one zero-cell and no cells of dimensions one through \(k-1\), \(k\geq1\), is \((k-1)\)-connected. It is path connected: from a point in a positive-dimensional cell follow a characteristic-disk ray to its boundary, then repeat in the lower-dimensional cell containing that endpoint; dimension strictly decreases until the zero-cell is reached. Concatenate those finitely many paths. For \(1\leq r<k\), give a based \(S^r\) its standard CW structure, with its basepoint a zero-cell. Relative cellular approximation deforms every based sphere map into the target \(r\)-skeleton, which is only that point. Thus every such \(\pi_r\) vanishes. This supplies connectivity by an actual homotopy argument, rather than inferring it from homology alone.

## C. Thom spaces, cells and homology

Throughout this section the base \(B\) is Hausdorff. Give a real rank-\(k\) bundle \(\xi\to B\) a Euclidean metric. On any CW base such a metric exists by the cellwise classifying map of Lemma H.1 in the frame chapter: pull back the ambient metric of the canonical bundle. Smooth bundles on smooth manifolds have smooth metrics by the proved smooth partition construction in the bundle chapter. Write \(D(\xi)\) for its closed unit-disk bundle and \(S(\xi)\) for its unit-sphere bundle. Its **Thom space** is the pointed quotient
\[
T(\xi)=D(\xi)/S(\xi),
\tag{C.1}
\]
in which the entire sphere bundle is identified to one point \(t_0\). An empty sphere bundle uses the pointed-quotient convention of adjoining a disjoint basepoint. In particular \(T(\varepsilon^0)=B_+\), where \(B_+=B\sqcup\{t_0\}\).

For positive rank this is equivalently the quotient of the whole total space by all vectors of norm at least one. Radial clipping \(v\mapsto v/\max(1,\|v\|)\) and inclusion of the disk bundle induce inverse continuous maps of the two quotients. The complement of \(t_0\) is the open unit-disk bundle, identified with the whole vector bundle by
\[
v\longmapsto\frac{v}{\sqrt{1-\|v\|^2}},
\qquad
w\longmapsto\frac{w}{\sqrt{1+\|w\|^2}}.
\tag{C.2}
\]
These are inverse homeomorphisms, and diffeomorphisms when the bundle and metric are smooth.

The quotient is Hausdorff. Two distinct points outside \(t_0\) have disjoint neighbourhoods in the open disk bundle. To separate \(t_0\) from a point of norm \(r<1\), choose \(r<c<1\). The norm conditions \(\|v\|>c\) and \(\|v\|<c\) give disjoint saturated open sets containing the sphere bundle and that point, respectively. They descend to disjoint quotient neighbourhoods.

Changing the metric gives a based homeomorphism of the Thom spaces. For metrics \(g_0,g_1\), the following map of closed disk bundles is particularly useful:
\[
v\longmapsto
\frac{v}{\sqrt{\,1-g_0(v,v)+g_1(v,v)\,}},
\qquad g_0(v,v)\leq1.
\tag{C.3}
\]
Its denominator is positive. The new \(g_1\)-norm is at most one and equals one exactly on the old sphere bundle. Swapping the metrics gives its inverse, as substitution verifies. The induced pointed map is consequently a homeomorphism; for smooth metrics it is smooth on the complement of the collapsed point and has identity derivative along the zero section. This avoids choosing matrix square roots to compare metrics.

If \(B\) is compact, \(D(\xi)\) is compact. Cover \(B\) by finitely many metric-trivializing charts and shrink to closed subsets still covering it; each restricted disk bundle is the compact product of that subset with \(D^k\). Their finite union is the entire disk bundle. Hence \(T(\xi)\) is compact Hausdorff. Equation (C.2) identifies it with the one-point compactification of \(E(\xi)\): a complement of a neighbourhood of \(t_0\) is compact inside \(E(\xi)\), and conversely a compact subset there is closed in the compact Hausdorff Thom space. The compact-base hypothesis is essential.

**Theorem C.1 — Thom cells (MS 18.1).** If \(B\) is a CW complex, \(T(\xi)\) is a CW complex with its one basepoint zero-cell and one cell of dimension \(a+k\) for each \(a\)-cell of \(B\). For \(k\geq1\) it is \((k-1)\)-connected. A finite base gives a finite Thom complex.

**Proof.** Pull \(\xi\) back to a characteristic disk \(D^a\). It is trivial by the complete disk homotopy-invariance proof; Gram–Schmidt applied to its pulled-back metric gives an orthonormal trivialization. Thus its closed disk bundle is \(D^a\times D^k\). This product is homeomorphic to \(D^{a+k}\), preserving its boundary: use radial coordinates for the product norm \(\max(\|x\|,\|y\|)\) and for the Euclidean norm on their direct sum, as in the cube/disk proof of the frame chapter.

The characteristic bundle map followed by (C.1) gives the Thom characteristic map. Its interior is exactly the open base cell times the open fibre disk. The original characteristic map is a homeomorphism on that base cell, so this product maps homeomorphically onto a single open \((a+k)\)-cell. Boundary points with fibre norm one go to \(t_0\); the other boundary points lie over the original attaching boundary and hence in cells of smaller base dimension. Different interiors are disjoint and cover the complement of \(t_0\).

Closure finiteness follows from closure finiteness on \(B\): one Thom cell's boundary involves only the finitely many cells in that base cell's characteristic closure, and the point \(t_0\). The topology is the weak cell topology too. The characteristic disk-bundle maps together are a quotient onto \(D(\xi)\). In a local orthonormal bundle chart this is the base characteristic quotient multiplied by \(D^k\), a compact locally compact factor; the quotient-product proof in the frame chapter applies. Composing with the sphere-collapse quotient gives precisely the test for closedness on all these Thom characteristic disks, with the basepoint included. This proves the CW topology, not merely a partition into open cells.

For positive \(k\), there are no nonbasepoint cells below dimension \(k\). The final connectivity consequence of Theorem B.2 gives \((k-1)\)-connectivity. Rank zero is the separate \(B_+\) convention, with one additional zero-cell. Finiteness follows immediately from the cell correspondence. ∎

**Theorem C.2 — Homological Thom isomorphism (MS 18.2).** For an oriented rank-\(k\) bundle, with \(k\geq1\), the positive Thom class gives natural isomorphisms
\[
H_{k+i}(T(\xi),t_0;\mathbb Z)\cong H_i(B;\mathbb Z).
\tag{C.4}
\]
There is the analogous mod-two isomorphism without an orientation. The cohomological Thom isomorphism also identifies \(H^{k+i}(T(\xi),t_0;G)\) with \(H^i(B;G)\), for every abelian \(G\) in the oriented case.

**Proof.** Compare the quotient pair with the disk/sphere pair before applying the already proved Thom isomorphism. Let \(N\subset D(\xi)\) be the open outer annulus \(\|v\|>1/3\). Its radial deformation retract onto \(S(\xi)\) fixes that sphere. The quotient \(N/S(\xi)\) is open in \(T(\xi)\) and contracts to \(t_0\), by the same radial deformation after collapse. Its continuity follows from the quotient-times-interval proof. The pair exact sequences therefore identify the relative groups for \((D(\xi),S(\xi))\) with those for \((D(\xi),N)\), and for \((T(\xi),t_0)\) with those for \((T(\xi),N/S(\xi))\).

Use the additional open inner disk bundle \(V=\{\|v\|<2/3\}\). It and \(N\) cover \(D(\xi)\). Their quotient images cover \(T(\xi)\), and the quotient is a homeomorphism on \(V\) and on its intersection with \(N\). Small-chain excision, with the explicit subdivisions and homotopies proved in the Thom/Euler chapter, identifies both relative pairs just obtained with \((V,V\cap N)\). Thus the quotient induces homology and cohomology isomorphisms
\[
q_*:H_*(D(\xi),S(\xi))\xrightarrow{\cong}H_*(T(\xi),t_0),
\qquad
q^*:H^*(T(\xi),t_0)\xrightarrow{\cong}H^*(D(\xi),S(\xi)).
\tag{C.5}
\]
The same argument works with every coefficient group. All maps are actual pair maps, so the identifications are natural.

Next \((D(\xi),D(\xi)\setminus B)\) is a deformation retract of \((E(\xi),E(\xi)\setminus B)\) by radial clipping. Inclusion of \(S(\xi)\) into \(D(\xi)\setminus B\) is a homotopy equivalence by unit normalization. The pair sequences identify the disk/sphere relative groups with the total-space Thom pair groups. Therefore the positive Thom class there corresponds to a class \(u_D\) on \((D(\xi),S(\xi))\), and then to a class \(u_T\) on \((T(\xi),t_0)\) by (C.5).

The complete homological Thom theorem in the Thom/Euler chapter, Theorem 7.1, proved that the cap map \(\pi_*R_u\) is an isomorphism to base homology, including its compact-support passage. Its naturality with the disk pair and (C.5) gives (C.4), explicitly as
\(\pi_*R_{u_D}q_*^{-1}\). The stated cohomology conclusion follows by the same pair comparisons from that theorem's full coefficient version. We are using the proved homology theorem too, rather than trying to infer it from cohomology with integer coefficients alone. ∎

**Example — A trivial bundle.** There is a natural based homeomorphism
\[
T(\varepsilon^k_B)\cong B_+\wedge S^k=\Sigma^k B_+.
\tag{C.6}
\]
Here smash means collapsing the two basepoint factors in a product, and \(\Sigma\) is reduced suspension. Both sides collapse the same subsets of \(B_+\times D^k\): \(B\times\partial D^k\) and the extra basepoint factor. Their quotient topologies agree. In detail, the compact disk quotient \(D^k\to D^k/\partial D^k\) remains quotient after product with any \(B_+\). It is a closed map with compact fibres: given a point outside the image of a closed product subset, finitely many product neighbourhoods around that fibre give a common neighbourhood in \(B_+\), and closedness of the disk quotient gives a target neighbourhood whose entire inverse image is in their union. The product map is therefore closed. Composing these quotient maps in either order proves (C.6). At \(k=0\) it says \(B_+\wedge S^0=B_+\).

For instance the trivial line over \(\mathbb R\) has Thom homology \(\widetilde H_1=\mathbb Z\) and no other reduced homology, by (C.4). The one-point compactification of its total space \(\mathbb R^2\) is instead \(S^2\). Thus replacing a noncompact-base Thom space by a total-space one-point compactification would change the answer.

## D. Compact images, universal stages and stabilization

The collapsed point in a noncompact-base Thom space does not permit an arbitrary escape in the base. The following topology fact will let us localize the smooth approximation argument precisely.

**Lemma D.1 — Compact-stage property.** Suppose a Hausdorff base \(B\) has nested compact subsets \(K_i\) whose interiors cover \(B\). For a positive-rank Euclidean bundle, put \(T_i=T(\xi|_{K_i})\), viewed inside \(T(\xi)\) with the same collapsed point. Then \(T(\xi)\) has their weak direct-limit topology, each \(T_i\) is compact Hausdorff and closed, and every compact subset of \(T(\xi)\) lies in one \(T_i\).

**Proof.** The restricted disk bundles \(D_i\) are compact, as proved in Section C, and their sphere quotients are compact Hausdorff. Their maps into the Hausdorff \(T(\xi)\) are continuous injections, so are embeddings onto closed subsets.

The disk bundle has the weak topology of the \(D_i\). Indeed if a subset meets each \(D_i\) in a closed set, examine any point over \(b\in\operatorname{int}K_i\). On that open restricted disk bundle the set is the restriction of its closed intersection with \(D_i\), so is locally closed at every point. Its complement is consequently open globally. Now if a subset \(F\subset T(\xi)\) has closed intersection with every \(T_i\), its inverse image in each \(D_i\) is closed by the restricted quotient. The disk-bundle weak topology makes its full inverse image closed. The defining quotient topology therefore makes \(F\) closed in \(T(\xi)\). The converse is immediate, proving the asserted direct limit.

Finally suppose a compact subset meets points outside every stage. Choose such points in stages of strictly increasing index, with each chosen point outside all earlier stages that have already occurred. Every fixed stage then contains only finitely many chosen points. Every subset of the chosen set is closed in each stage and hence closed in the whole direct limit. The chosen set is therefore closed and discrete, also in the given compact subset. It would be an infinite compact discrete space, impossible because its singletons form an open cover with no finite subcover. Thus the compact subset lies in one stage. ∎

Smooth Hausdorff second-countable manifolds have the required compact exhaustion, with nested interiors, by the explicit chart/shell construction in the bundle chapter. In particular, for a map from a compact space into the Thom space of a smooth bundle, all its nonbasepoint values project into one compact subset of the base. We will keep that fact separate from the compactness of the source: it depends on the Thom quotient topology just proved.

Universal Thom spaces have another finite-stage description. Let
\[
MO(k)=T(\gamma_k\to BO(k)),\qquad
MSO(k)=T(\widetilde\gamma_k\to BSO(k)),\qquad k\geq1.
\tag{D.1}
\]
The universal metrics are the ambient Euclidean metrics on their finite-support planes. These are continuous at the direct limit, since their restrictions to every finite stage are continuous, with the product topology already established in the classifying-map chapter.

**Lemma D.2 — Finite universal carrier.** Every continuous map, or homotopy of maps, from a compact space into \(MO(k)\) or \(MSO(k)\) has image in the Thom space of the canonical bundle over a sufficiently large finite Grassmannian, unoriented or oriented respectively. Those finite base spaces are compact smooth manifolds, and their Thom spaces are finite CW complexes.

**Proof.** Theorem C.1 gives the universal Thom CW structure. The compact-subcomplex lemma therefore confines the image to finitely many Thom cells and their closures. Each such cell comes from a Schubert cell with finitely many coordinate indices; choose \(N\) larger than all of them. Their characteristic base disks, and the canonical bundle over them, lie in \(G_k(\mathbb R^N)\) and its ambient \(\mathbb R^N\). Thus their Thom characteristic images lie in \(T(\gamma_k^N)\).

For the oriented case, lift the Schubert cells and their characteristic disks to the orientation double cover. A disk's lift is determined by one sheet choice, by the proved path-cover construction. The same finite coordinate bound places these lifts in the orientation cover of \(G_k(\mathbb R^N)\). The lifted disks give its CW structure, not just its open cells. Locally on a covering chart, the characteristic quotient is the base characteristic quotient multiplied by the discrete two-point fibre, after changing the sheet coordinate in each pulled-back disk. Restriction to that open chart remains quotient, and product with a discrete fibre is quotient. Thus closedness is tested on exactly the two lifts of each characteristic disk. Their boundaries meet only the finitely many lifts of the cells in the original attaching closure, so closure finiteness holds too. This proves both the finite and the infinite lifted weak CW structures.

The finite Grassmannian is a compact smooth manifold by its projection/graph charts. Its orientation cover is the unit-sphere bundle of the determinant line; the latter is compact by finite compact-chart shrinking, with fibre \(S^0\). Local determinant frames identify it with the two smooth copies of each base chart, so it is a compact smooth manifold too. Their canonical bundles are smooth in the graph charts and the cover charts. Theorem C.1 now makes their Thom spaces finite CW complexes. A homotopy has compact parameter product, so the same argument covers it simultaneously. ∎

For either universal space, its homotopy groups are consequently the filtered limits of the corresponding finite-stage homotopy groups. Surjectivity follows by placing a sphere representative in a finite stage; injectivity follows by placing a null-homotopy in a common larger finite stage. This statement concerns homotopy classes and their actual compact witnesses, rather than assuming that an arbitrary infinite quotient is well behaved.

Thom spaces also supply the stabilization map. There is a natural based homeomorphism
\[
T(\xi\oplus\varepsilon^1)\cong T(\xi)\wedge S^1=\Sigma T(\xi).
\tag{D.2}
\]
To prove it, use the product disk \(D(\xi)\times D^1\) and its boundary union
\[
S(\xi)\times D^1\ \cup\ D(\xi)\times S^0.
\]
Radial comparison of the block-maximum norm with the Euclidean direct-sum norm sends that product disk homeomorphically to \(D(\xi\oplus\varepsilon^1)\), carrying its boundary union to the unit sphere bundle. Collapsing that union gives the left side. Collapsing the two boundary factors successively gives the smash on the right. The first sphere-collapse quotient remains quotient after product with the compact \(D^1\), by the quotient-product lemma; the compact disk quotient in the other factor remains quotient after any product, by the proof of (C.6). Hence these equal equivalence relations have the same quotient topology.

Add a fixed positive unit vector to an oriented universal \(k\)-plane, or a fixed line in the unoriented case. This gives the base inclusion \(BSO(k)\to BSO(k+1)\), or \(BO(k)\to BO(k+1)\), and identifies the pulled-back canonical bundle with \(\widetilde\gamma_k\oplus\varepsilon^1\), or \(\gamma_k\oplus\varepsilon^1\). The bundle map preserves the induced metric and sends sphere bundle to sphere bundle, so induces a continuous based Thom map. Composing it with (D.2) gives
\[
\Sigma MSO(k)\longrightarrow MSO(k+1),
\qquad
\Sigma MO(k)\longrightarrow MO(k+1).
\tag{D.3}
\]
These define stabilization on the homotopy groups by suspension followed by the indicated map. Their existence is purely geometric; a later stable-range assertion will require its own proof.

## E. Compact stability and a controlled regular-value perturbation

We use the smooth inverse-function and flow lemmas already proved in Section 3 of the manifold-duality chapter. The following quantitative observation supplies the stability step in MS 18.5 and solves its accompanying Problem 18-A.

**Lemma E.1 — Stability on a compact set.** Let \(f:W\to\mathbb R^k\) be smooth, where \(W\subset\mathbb R^a\) is open and \(k\geq1\). Suppose zero is a regular value throughout a compact subset \(Y\subset W\): \(Df_y\) is surjective whenever \(y\in Y\) and \(f(y)=0\). There are positive constants \(\delta,\eta\) such that every smooth \(g\) satisfying
\[
\sup_Y\|g-f\|<\delta,\qquad
\sup_Y\|Dg-Df\|<\eta
\tag{E.1}
\]
also has zero as a regular value throughout \(Y\).

**Proof.** If \(Y\) is empty, the estimates and conclusion are vacuous, so any positive constants work. If \(f\) has no zero in the nonempty \(Y\), compactness gives a positive minimum of \(\|f\|\) there. Any smaller value of \(\delta\) prevents a zero of \(g\) in \(Y\), and any positive \(\eta\) works.

Otherwise the zero set in \(Y\) is compact. Surjectivity is an open condition: a nonzero maximal minor stays nonzero nearby. Hence some open neighbourhood \(V\) of that zero set has surjective \(Df\) everywhere. The compact complement \(Y\setminus V\), when nonempty, has a positive minimum of \(\|f\|\). Choose \(\delta>0\) so small that
\[
Y_\delta=\{y\in Y:\|f(y)\|\leq\delta\}\subset V.
\]
This is compact. On it the matrix
\[
R_y=Df_y^{\,T}\bigl(Df_yDf_y^{\,T}\bigr)^{-1}
\tag{E.2}
\]
is a continuous right inverse of \(Df_y\). Indeed \(Df_yDf_y^T\) is positive definite: its quadratic form is \(\|Df_y^Tz\|^2\), positive for \(z\ne0\) because \(Df_y\) is surjective. Matrix inversion is continuous by its adjugate formula. Consequently \(\|R_y\|\leq C\) on \(Y_\delta\), for one finite positive \(C\).

Take \(\eta<1/(2C)\). If \(g(y)=0\) with \(y\in Y\), the first estimate in (E.1) puts \(y\) in \(Y_\delta\), and
\[
Dg_yR_y=I+(Dg_y-Df_y)R_y
\tag{E.3}
\]
is invertible. In fact the perturbation on the right has norm less than \(1/2\); the convergent geometric series \(\sum_{j\geq0}(-A)^j\) is the inverse of \(I+A\), as multiplying its finite partial sums and passing to the limit shows. Thus \(R_y(Dg_yR_y)^{-1}\) is a right inverse of \(Dg_y\). This proves its surjectivity at every relevant zero. ∎

Smooth cutoffs with a plateau will be used repeatedly. If \(K\) is compact inside an open subset \(V\) of a smooth manifold, finitely many of the coordinate bumps constructed in the bundle chapter have supports in \(V\) and a sum \(\psi>0\) on \(K\). Let \(m=\min_K\psi>0\). Apply to \(\psi\) a smooth scalar function that is zero up to \(m/4\), one from \(m/2\) onward, and lies in \([0,1]\). Such a function is explicit: with \(b(t)=e^{-1/t}\) for \(t>0\), zero otherwise, the function \(b(t)/(b(t)+b(1-t))\) rises smoothly from zero to one on \([0,1]\); rescale its argument. The resulting cutoff \(\lambda\) equals one on a neighbourhood of \(K\) and has compact support in \(V\). Empty \(K\) can use \(\lambda=0\).

**Lemma E.2 — Local transversality perturbation (MS 18.5).** Let \(f:W\to\mathbb R^k\) be smooth on open \(W\subset\mathbb R^a\), and suppose zero is a regular value throughout a relatively closed subset \(X\subset W\). For every compact \(K\subset W\) and every \(\varepsilon>0\), there is a smooth \(g\) such that:

- \(g=f\) outside a compact subset of \(W\);
- \(\|g(x)-f(x)\|<\varepsilon\) everywhere;
- zero is a regular value throughout \(X\cup K\).

Moreover \(g\) is joined to \(f\) by a smooth homotopy with the same compact support, and every map of that homotopy retains regularity throughout \(X\).

**Proof.** If \(K\) is empty, take \(g=f\) and the constant homotopy. Otherwise choose a cutoff \(\lambda:W\to[0,1]\) equal to one near \(K\), with compact support \(K'\subset W\). Since \(X\) is relatively closed, \(Y=X\cap K'\) is compact. Apply Lemma E.1 to this compact set. For a constant vector \(v\in\mathbb R^k\), consider
\[
g=f-\lambda v,\qquad f_t=f-t\lambda v,\quad 0\leq t\leq1.
\tag{E.4}
\]
On \(K'\) their changes in value are bounded by \(\|v\|\), and their changes in derivative by
\(\|v\|\sup_{K'}\|D\lambda\|\). Choose \(\|v\|\) small enough for both stability estimates and for \(\|v\|<\varepsilon\). Sard's theorem, proved in Section A, supplies a regular value \(v\) of \(f\) as close to zero as required.

Near \(K\) the endpoint is \(g=f-v\), so its zeros there have surjective derivative. Throughout \(Y\), Lemma E.1 applies simultaneously to every \(f_t\). Outside \(K'\) each \(f_t=f\), so regularity on the rest of \(X\) is retained. Formula (E.4) gives all the stated support and closeness claims. This proves the lemma, including its relative stability rather than leaving that step to an assertion that transversality is open. ∎

The same local statement holds in a source manifold chart. Its application to a bundle will change the fibre coordinate and keep the base coordinate fixed; this is why the perturbation can be assembled chart by chart.

## F. Smooth approximation in a Thom space

The complement of the collapsed point is a smooth manifold, but the Thom space itself need not be one. We therefore prove exactly the approximation statement that transversality needs. In particular, we control the map near the collapsed-point preimage; smoothing only a neighbourhood of the zero set would not give the full statement.

**Lemma F.1 — Fine Euclidean approximation.** Let \(U\) be a Hausdorff second-countable smooth manifold, possibly with boundary, and \(h:U\to\mathbb R^L\) continuous. Given a positive continuous function \(\delta\) on \(U\), there is a smooth \(H:U\to\mathbb R^L\) with
\[
\|H(x)-h(x)\|<\delta(x)\quad(x\in U).
\tag{F.1}
\]
If \(R\subset U\) is closed and \(h\) is smooth on a neighbourhood of \(R\), \(H\) can equal \(h\) on a possibly smaller neighbourhood of \(R\).

**Proof.** At each \(x\) choose a neighbourhood \(V_x\) so small that, for \(y\in V_x\), \(\delta(y)>\delta(x)/2\) and \(\|h(y)-h(x)\|<\delta(x)/4\). The smooth partition theorem from the bundle chapter gives a locally finite subordinate partition \(\theta_i\), with each support inside some \(V_{x_i}\). Set
\[
H_0(y)=\sum_i\theta_i(y)h(x_i).
\tag{F.2}
\]
This is a locally finite sum of smooth functions times constant vectors. Every active summand differs from \(h(y)\) by less than \(\delta(y)/2\); their convex average does too. Thus (F.1) holds with room to spare. For boundary charts the same partition proof uses the restrictions of smooth ambient coordinate bumps to the half-chart. They are smooth up to the boundary, and the same locally finite normalization works.

For the relative assertion let \(V\) be an open neighbourhood of \(R\) where \(h\) is smooth. Use a smooth partition subordinate to the two-set cover \(\{V,U\setminus R\}\), and add all the functions assigned to \(V\), obtaining \(\chi\in[0,1]\). Its support is contained in \(V\): the assigned supports form a locally finite family of closed subsets, so their union is closed and contained there. Also \(\chi=1\) on a neighbourhood of \(R\), because the other locally finite supports avoid each point of \(R\). Then
\[
H=\chi h+(1-\chi)H_0
\tag{F.3}
\]
is smooth. The first term extends smoothly by zero away from \(V\), by its support condition. The error is at most that of \(H_0\), and \(H=h\) near \(R\). ∎

We also need a small-neighbourhood choice with a varying tolerance. Suppose \(h:U\to N\subset\mathbb R^L\) is continuous, \(N\) is open, \(r:N\to Z\) is continuous into a metric space, and \(e:U\to(0,\infty)\) is continuous. There is a smooth positive \(\delta\) such that
\[
\|z-h(x)\|<\delta(x)\ \Longrightarrow\
z\in N,\quad d(r(z),r(h(x)))<e(x).
\tag{F.4}
\]
Indeed the relation on the right is open in \(U\times\mathbb R^L\) and contains the graph of \(h\). Around each graph point choose a product neighbourhood \(V_x\times B(h(x),2a_x)\) contained in it; shrink \(V_x\) so that \(\|h(y)-h(x)\|<a_x\). For \(y\in V_x\), the ball \(B(h(y),a_x)\) is then permitted. A smooth locally finite subordinate partition gives
\(\delta(y)=\tfrac12\sum_i\theta_i(y)a_{x_i}>0\).
At a fixed \(y\) this average is less than the largest active permitted radius, whose ball is itself permitted. This proves (F.4), including the uniform control on every point of the straight segment to a \(\delta\)-close approximation.

**Lemma F.2 — An embedding over a precompact base region.** Let \(\xi\to B\) be a smooth finite-rank bundle over a Hausdorff second-countable manifold without boundary. For any compact \(K\subset B\) there is an open \(B_0\) containing \(K\), with compact closure, for which \(E(\xi|_{B_0})\) embeds smoothly as a closed submanifold of an open subset of a finite Euclidean space. It consequently has a smooth neighbourhood retraction there.

**Proof.** Choose finitely many base coordinate charts \(V_i\) that also trivialize \(\xi\), and nonnegative smooth \(\phi_i\) with compact supports in them, with at least one \(\phi_i\) positive at each point of \(K\). Write \(c_i\) for the base coordinate map and \(v_i\) for the fibre coordinate. Let
\[
B_0=\{b\in B\mid \sum_i\phi_i(b)>0\}.
\]
Its closure lies in the finite union of the compact supports. Define, extending every chart block by zero off its support,
\[
F(b)=\bigl(\phi_i(b),\,\phi_i(b)c_i(b)\bigr)_i,\qquad
J(b,v)=\bigl(F(b),\,(\phi_i(b)v_i(v))_i\bigr).
\tag{F.5}
\]
All blocks are smooth. Put \(O=\{(t_i,z_i)_i:\sum_i t_i>0\}\) in the base-block Euclidean space; \(J\) takes values in the open ambient manifold \(O\times\mathbb R^q\), for the finite total number \(q\) of fibre coordinates.

A positive block recovers the base coordinates by division, so \(F\) is injective. The derivative argument is just as explicit: if \(DF\) kills a tangent vector, a positive block first gives \(d\phi_i=0\), then \(dc_i=0\), so that vector is zero. If \(DJ\) kills a total-space tangent vector, this proves its base part is zero, and the positive fibre block then proves its fibre part is zero. Thus \(J\) is an injective immersion.

It is a homeomorphism onto a closed image in the indicated open ambient space. To see both claims locally, take a convergent sequence of its images with limit in \(O\times\mathbb R^q\). The bases lie in the compact union of the supports, so have a convergent subsequence, with limit \(b\). Some limiting \(\phi_i(b)>0\), since the limit lies in \(O\). In that chart division by \(\phi_i\) recovers both the converging base coordinates and the converging fibre coordinates. They define a vector \(v\in E_b\), and continuity gives the limiting image \(J(b,v)\). Injectivity and this same division show the inverse is continuous around every image point. Sequential closedness here is closedness, because the ambient space is Euclidean. The inverse-function lemma on a full-rank coordinate projection of \(DJ\) now gives local submanifold charts. Hence this is a closed smooth embedding.

The complete tubular-neighbourhood theorem in the manifold-duality chapter, Theorem 3.2, applies to this closed, possibly noncompact embedded total space in the open Euclidean ambient manifold. Its normal projection yields a smooth retraction \(r:N\to J(E(\xi|_{B_0}))\) on an open neighbourhood \(N\) of the image. ∎

Here is the metric fact that makes the collapsed-point control precise. For compact \(K\subset B\), the restricted disk bundle is compact metrizable. For example, finitely many blocks (F.5) over charts covering \(K\) give a continuous injection of that disk bundle into Euclidean space; compactness and Hausdorffness make it an embedding. Let \(d_D\) be an induced metric, and \(S=S(\xi|_K)\), a closed compact subset for positive rank. On its quotient the formula
\[
d_T([x],[y])=
\min\{d_D(x,y),\,d_D(x,S)+d_D(y,S)\},
\quad x,y\notin S,
\qquad
d_T([x],t_0)=d_D(x,S)
\tag{F.6}
\]
defines a metric. It is positive at distinct noncollapsed points and at every such point versus \(t_0\). For the triangle inequality, a direct route through an intermediate point bounds the direct distance, and a route through \(S\) bounds the second term. Mixed routes use
\(d_D(x,S)\leq d_D(x,y)+d_D(y,S)\); these cover the four choices of the two minima. The quotient map is continuous since these distances are at most the original distances, including at \(S\). The resulting continuous bijection from the compact quotient onto this metric space is a homeomorphism. Thus (F.6) is a compatible metric on \(T(\xi|_K)\).

**Theorem F.3 — Relative smooth Thom approximation.** Let \(P\) be a compact smooth manifold, possibly with boundary, and let \(\xi\to B\) be a positive-rank smooth bundle over a Hausdorff second-countable manifold without boundary. Every continuous \(f:P\to T(\xi)\) is homotopic to a map \(g\) such that
\[
g^{-1}(t_0)=f^{-1}(t_0),\qquad
g:P\setminus f^{-1}(t_0)\longrightarrow T(\xi)\setminus\{t_0\}
\text{ is smooth}.
\tag{F.7}
\]
The homotopy fixes \(f^{-1}(t_0)\) pointwise. If \(R\) is closed in its complement and \(f\) is already smooth on a neighbourhood of \(R\), it can also fix a neighbourhood of \(R\).

**Proof.** Put \(A=f^{-1}(t_0)\) and \(U=P\setminus A\). If \(U\) is empty there is nothing to do. By Lemma D.1, the compact image of \(f\) lies in \(T(\xi|_K)\) for some compact exhaustion stage \(K\). All its nonbasepoint values therefore have bases in \(K\).

Apply Lemma F.2 to \(K\), using \(J\) to identify \(E_0=E(\xi|_{B_0})\) with its closed embedded image, and \(r:N\to E_0\) as its smooth retraction. Choose a larger compact exhaustion stage \(K_*\) containing the closures of the finitely many chart supports. Thus \(B_0\subset K_*\). Give \(T_*=T(\xi|_{K_*})\) the compatible metric (F.6). The inverse radial identification of (C.2) gives a smooth map
\(\kappa:E_0\to T_*\setminus\{t_0\}\).
On \(U\) write \(f=\kappa h\), where \(h:U\to E_0\subset\mathbb R^L\) is continuous, possibly with unbounded fibre coordinates.

Choose a compatible metric on compact \(P\), available from the same finite chart-block injection used above, with half-charts if necessary. If \(A\ne\varnothing\), let \(e(x)=d_P(x,A)\) on \(U\); if \(A=\varnothing\), let \(e=1\). This is positive and continuous on \(U\). Apply (F.4) to the map \(h\), the continuous target map \(\kappa r:N\to T_*\), and this tolerance. We obtain a smooth positive \(\delta\) such that
\[
\|z-h(x)\|<\delta(x)\ \Longrightarrow\
z\in N,\quad d_T(\kappa r(z),f(x))<e(x).
\tag{F.8}
\]
By Lemma F.1 choose a smooth ambient approximation \(H\) with \(\|H-h\|<\delta\), equal to \(h\) near \(R\) when that relative condition is prescribed. Define on \(U\)
\[
f_t(x)=\kappa r\bigl((1-t)h(x)+tH(x)\bigr),
\quad 0\leq t\leq1,
\tag{F.9}
\]
and on \(A\) define \(f_t=t_0\). Every straight segment in (F.9) stays in \(N\) by (F.8). At time zero \(r(h)=h\), so \(f_0=f\); at time one \(\kappa rH\) is smooth on all of \(U\). Every value there is noncollapsed, giving the exact preimage equality in (F.7), and the relative region is fixed.

It remains to check continuity along \(A\), rather than assuming it. Uniformly in \(t\), inequality (F.8) gives
\[
d_T(f_t(x),t_0)
\leq e(x)+d_T(f(x),t_0).
\tag{F.10}
\]
Both right-hand terms tend to zero as \(x\to a\in A\), by their continuity on the compact metric spaces just chosen. Thus (F.9) extends continuously at every \((a,t)\), uniformly in the time coordinate. Its values lie in the embedded compact stage \(T_*\), so this also proves continuity into the full Thom space. The endpoint is the required \(g\). ∎

No boundedness of the fibre coordinates of \(h\) was used: the fine tolerance shrinks as needed. The compact carrier controls the base, and (F.10) separately controls approach to the collapsed point. Both are needed for a noncompact base.

## G. Transverse inverse images and the bordism map

At a point of the zero section of \(E(\xi)\), the normal quotient of its tangent space by the tangent space of the base is canonically \(\xi_b\). In a bundle chart the quotient map is the derivative of the fibre coordinate. For a smooth \(h:V\to E(\xi)\), **transversality to the zero section** therefore means that this fibre derivative is surjective at every zero of \(h\). Changing a bundle frame multiplies it by an invertible matrix at a zero, so this condition is intrinsic.

**Lemma G.1 — Inverse-image manifold and its normal bundle.** If \(h:V^a\to E(\xi)\) is smooth and transverse to the zero section of a rank-\(k\) bundle, its inverse image \(M\) is a smooth embedded submanifold of dimension \(a-k\), or is empty. Its normal quotient is canonically
\[
TV|_M/TM\ \cong\ (h|_M)^*\xi.
\tag{G.1}
\]
If \(V\) and \(\xi\) are oriented, orient \(M\) by putting its tangent orientation first and this normal orientation second, obtaining the orientation of \(V\).

For a source with boundary, assume additionally that the boundary restriction is transverse. Then \(M\) is a manifold with boundary, \(\partial M=M\cap\partial V\), and its boundary orientation agrees with the inverse-image orientation induced from the outward-oriented \(\partial V\).

**Proof.** In a source chart and a bundle chart write \(h=(b,w)\), where \(w\) has \(k\) components. At a zero, \(Dw\) has rank \(k\). Complete those \(k\) component functions with \(a-k\) of the original source coordinates so that the resulting \(a\) by \(a\) derivative is invertible. The proved inverse-function theorem makes these new functions a coordinate system. In it \(M\) is precisely \(w=0\), showing its local submanifold structure and its tangent space \(\ker Dw\). The induced map \(TV/TM\to\mathbb R^k\) is an isomorphism. Under a change of bundle trivialization \(w'=A(b)w\), its derivative at a zero is \(Dw'=A(b)Dw\), since the term involving \(w\) vanishes. These quotient isomorphisms thus glue to (G.1), smoothly and with the stated orientation.

At a boundary point let \(\rho\geq0\) be its inward boundary coordinate. Boundary transversality says that the \(w\)-derivative already has rank \(k\) on the tangential coordinates. Keep \(\rho\), complete \(w\) with \(a-k-1\) tangential coordinates, and apply the inverse-function theorem to their smooth extensions across the coordinate boundary. The resulting chart preserves the half-space because its first coordinate is still \(\rho\). It identifies \(M\) with a half-space of dimension \(a-k\), with boundary exactly its intersection with \(\rho=0\).

For the orientation assertion choose a vector \(N\in TM\) with outward boundary component. Starting with any outward source vector, subtract a boundary-tangent vector with the same \(Dw\)-image; the surjectivity on boundary tangents permits this and gives such \(N\). Choose the normal lifts in \(T\partial V\) too. The equality of ordered orientations
\((N,T\partial M,\xi)=(N,T\partial V)\)
then says exactly that \((T\partial M,\xi)\) is the boundary orientation of \(V\). This proves the boundary sign, with no unspecified permutation. If \(a<k\), surjectivity is impossible at a zero, so the inverse image is empty. ∎

The same proof works for an arbitrary embedded submanifold \(Y\subset N\): use its local normal-coordinate functions, whose derivative represents \(TN|_Y/TY\). Thus the usual inverse-image normal theorem is also established by this calculation.

**Lemma G.2 — Transversality on a compact source.** Let \(P\) be a compact smooth manifold without boundary and \(\xi\to B\) a positive-rank smooth bundle as in Theorem F.3. A map \(f_0:P\to T(\xi)\) that is smooth off its collapsed-point preimage is homotopic to a map \(g\) smooth on the same complement and transverse to the zero section. The homotopy fixes that collapsed-point preimage.

There is also a relative version on \(P=[0,1]\times Q\), with \(Q\) compact without boundary: if \(f_0\) is constant in the time coordinate and transverse on end collars, the deformation can fix smaller end collars and make it transverse everywhere.

**Proof.** Let \(U=f_0^{-1}(T(\xi)\setminus\{t_0\})\). The disk norm descends to a continuous function
\[
\rho:T(\xi)\to[0,1],\qquad
\rho(t_0)=1,\qquad
\rho(\kappa(w))=\frac{\|w\|}{\sqrt{1+\|w\|^2}},
\tag{G.2}
\]
where \(\kappa\) is (C.2)'s inverse radial identification. It vanishes exactly on the zero section. Hence \(Z=f_0^{-1}(B)=\{\rho f_0=0\}\) is a compact subset of \(U\). If it is empty, no perturbation is needed.

Cover \(Z\) by finitely many source charts \(W_i\) with closures inside \(U\), on each of which the base projection \(b=\pi\kappa^{-1}f_0\) lies in a single smoothly orthonormalized bundle chart. Choose compact \(K_i\subset W_i\) whose interiors cover \(Z\). Set \(X_0=\varnothing\). In the cylinder version take instead \(X_0\) to be closed end collars on which transversality already holds, and choose the \(K_i\) in interior source charts. This is possible: start with slightly smaller end collars than the given ones, and cover the remaining compact part of \(Z\) by charts in the interior. Arrange that the relative interior of \(X_0\cup\bigcup_iK_i\) contains all of \(Z\). The finite perturbation supports are then disjoint from the smaller end collars to be fixed.

If no charts are needed in the relative case, every zero already lies in the transverse end collars and the original map is transverse everywhere. Otherwise \(r\geq1\). Inductively write the current map on \(W_i\) as \(\kappa(b(x),w_{i-1}(x))\) in that bundle chart. Its base projection is kept equal to the original \(b\) at every step. Previously attained transversality is exactly regularity of zero for \(w_{i-1}\) on the relatively closed subset
\[
(X_0\cup K_1\cup\cdots\cup K_{i-1})\cap W_i.
\]
Apply Lemma E.2 to this subset and \(K_i\), replacing the fibre coordinate by \(w_{i-1}-\lambda_i v_i\), with compact support in \(W_i\). This agrees with the previous map outside that support, gives regularity on \(K_i\), and preserves regularity on all the earlier sets throughout its straight fibre homotopy. It also stays inside \(E(\xi)\), so introduces no collapsed-point value and leaves its preimage fixed. Agreement outside compact subsets of \(U\) makes both the map and its homotopy continuous across the collapsed-point preimage.

It remains to exclude new zeros elsewhere. Let \(r\) be the number of charts, and let \(L=X_0\cup\bigcup_iK_i\). On the compact complement of its relative interior, \(\rho f_0\) has a positive minimum \(c\), because this complement misses \(Z\). If the complement is empty, choose any \(c>0\). The radial function \(s(t)=t/\sqrt{1+t^2}\) is \(1\)-Lipschitz for \(t\geq0\), since \(s'(t)=(1+t^2)^{-3/2}\leq1\). Also \(|\|u\|-\|v\||\leq\|u-v\|\). In an orthonormal fibre chart, therefore, changing the fibre vector by less than \(\varepsilon\) changes \(\rho\) by less than \(\varepsilon\).

Choose each perturbing \(v_i\) with norm less than \(c/(2r)\), in addition to its stability requirements. Summing the finitely many changes gives \(\rho g>c/2\) off the relative interior of \(L\). Every zero of \(g\) consequently lies in \(L\), where the induction established transversality. Smoothness holds on all of \(U\), and the compact support, fixed base projection and end-collar claims follow from the construction. ∎

**Theorem G.3 — Thom inverse-image homomorphism (MS 18.6).** Let \(\xi\to B\) be a smooth oriented rank-\(k\) bundle, \(k\geq1\), over a Hausdorff second-countable manifold without boundary. Every continuous \(f:S^m\to T(\xi)\) is homotopic to a map \(g\) smooth throughout \(g^{-1}(T(\xi)\setminus\{t_0\})\) and transverse to the zero section. Its inverse image is a closed oriented \((m-k)\)-manifold when \(m\geq k\), and is empty when \(m<k\). For based maps and \(m\geq k\), the construction gives a well-defined homomorphism
\[
\Phi_\xi:\pi_m(T(\xi),t_0)\longrightarrow\Omega_{m-k},
\qquad [f]\longmapsto[g^{-1}(B)].
\tag{G.3}
\]
For an unoriented bundle the same construction takes values in unoriented bordism.

**Proof.** First apply Theorem F.3 and then Lemma G.2. Both homotopies fix the collapsed-point preimage, so are based if the original map is based. The inverse image is compact because it is the zero set of the continuous function (G.2) on a compact sphere. Lemma G.1 supplies its smooth structure, normal bundle and tangent-first orientation; it has no boundary.

Suppose \(g_0,g_1\) are homotopic transverse representatives. Begin with their continuous homotopy \(H:[0,1]\times S^m\to T(\xi)\). Reparametrize time by a continuous map constant at zero near zero and at one near one. This makes \(H=g_0\) and \(H=g_1\) on end collars, where it is smooth off the collapsed-point preimage and transverse. Apply Theorem F.3 relatively to closed smaller end collars, considered as a closed subset of that complement. It gives a homotopy map smooth on its entire noncollapsed region, retaining those end collars. Apply the cylinder version of Lemma G.2, fixing still smaller end collars. The resulting map \(H'\) is transverse everywhere, with transverse boundary restrictions \(g_0,g_1\).

Its zero inverse image \(W\) is compact and is a smooth manifold with boundary by Lemma G.1. Orient the cylinder by its time direction first, followed by the positive sphere orientation. On each constant end collar, the ordered splitting is
\[
(T W,\xi)=(\partial_t,Tg_i^{-1}(B),\xi)
=(\partial_t,TS^m).
\]
Thus \(W\) has the time-first product orientation on those collars. The boundary assertion of Lemma G.1 gives
\[
\partial W=(-g_0^{-1}(B))\sqcup g_1^{-1}(B).
\tag{G.4}
\]
This is an oriented cobordism between the two inverse images, using the smooth-collar and bordism definitions already proved in the cobordism chapter. If the homotopy was based, its basepoint line is in the collapsed-point preimage and was fixed; thus this reasoning respects based homotopy as well. It also compares any two choices of approximations of the same \(f\), by joining their homotopies.

Finally the group operation corresponds to disjoint union. Here is its geometric representative, including the collar issue. Precompose a based transverse map with an orientation-preserving degree-one collapse of a small closed spherical cap about its basepoint. In polar angle \(\theta\) from that point, use a smooth increasing angle function equal to zero on the cap, strictly increasing from its boundary to the opposite pole, and linear near the opposite pole. One is obtained by integrating a nonnegative smooth function which is flat at the cap boundary, positive beyond it and constant near \(\pi\), then normalizing its integral to \(\pi\). The polar formula is smooth wherever its value is not the collapsed pole and is a diffeomorphism from the cap complement onto the punctured sphere. Near the opposite pole its linear angle formula is smooth in Cartesian coordinates: \(\sin(cu)/\sin u\) is an even smooth function of \(u\), as are the corresponding cosine expressions. Interpolating its angle with \(\theta\) gives a based homotopy to the identity. The zero inverse image is carried by an orientation-preserving diffeomorphism and so represents the same oriented manifold.

The precomposed map is constant near the basepoint. To represent the sum, pinch an equator of an oriented sphere, using each resulting disk with its inherited orientation and identifying its interior orientation-preservingly with a punctured sphere. Insert one of these precomposed maps in each disk. They are constant on collars of their common boundary, so the assembled map is smooth at every noncollapsed point and is transverse at its zeros. Its zero set is the disjoint union of the two original inverse images, with their original orientations. This pinching is the based-cube concatenation defining \(\pi_m\): splitting the first cube coordinate into two halves has positive Jacobian on both interiors. It works also for \(m=1\). Therefore \(\Phi_\xi([f]+[f'])=\Phi_\xi([f])+\Phi_\xi([f'])\); the constant map has empty inverse image and maps to zero. The unoriented proof omits the orientation choices and signs, with all geometric constructions retained. ∎

## H. Dimension-controlled embeddings, including fixed boundary collars

The collapse construction needs an embedding in a specified dimension. Its inverse also needs an embedding of a cobordism with its two existing end embeddings retained. We prove both statements using the Sard theorem just established.

First extend the finite chart-block construction of Lemma 3.3 in the manifold-duality chapter to a compact manifold \(W\) with boundary. Use finitely many interior charts and boundary half-charts, and smooth bumps with supports inside them. The map with blocks \((\phi_i,\phi_i c_i)\) is injective, because a positive block recovers the point's chart coordinates. If its derivative kills a tangent vector, that block first gives \(d\phi_i=0\) and then \(dc_i=0\), so the vector vanishes. Compactness makes the map a homeomorphism onto its image; full-rank coordinate projection and the inverse-function theorem give its local embedded half-charts. Thus every compact smooth \(d\)-manifold, with or without boundary, has a smooth embedding \(F:W\to\mathbb R^L\) in some finite dimension.

**Lemma H.1 — Avoiding zero with a finite-dimensional parameter.** Let \(X\) be a Hausdorff second-countable smooth manifold of dimension \(s\), and
\(\Psi:X\times\mathbb R^p\to\mathbb R^D\) smooth. Suppose the derivative in the parameter alone is surjective at every zero of \(\Psi\). If \(s<D\), the set of parameters \(A\) for which \(\Psi(x,A)=0\) for some \(x\) has measure zero. In particular there is a parameter avoiding all zeros in every nonempty open parameter ball.

**Proof.** When \(p=0\), the parameter derivative cannot surject onto the positive-dimensional target at a zero, so there are no zeros and the assertion holds. For positive parameter dimension, the full derivative is surjective at every zero, so Lemma G.1 for the trivial \(D\)-plane bundle makes \(\Sigma=\Psi^{-1}(0)\) a smooth submanifold of dimension \(s+p-D<p\). Its projection to \(\mathbb R^p\) has image of measure zero, by the dimension case of Sard's theorem. Countably many charts cover \(\Sigma\), since it is a submanifold of a second-countable product. The bad parameter set is exactly this projected image. A null set contains no open ball by Section A. ∎

**Parametric transversality.** More generally, let \(P,X,Y\) be Hausdorff second-countable finite-dimensional smooth manifolds without boundary, let \(Z\subset Y\) be an embedded smooth submanifold, and suppose \(F:P\times X\to Y\) is smooth and transverse to \(Z\). Then outside a set of measure zero in each parameter chart, \(f_p(x)=F(p,x)\) is transverse to \(Z\). In particular good parameters are dense. This includes the submersion formulation in Tomasz Mrowka's *Geometry of Manifolds* notes.

To prove it, Lemma G.1's normal-coordinate argument makes \(\Sigma=F^{-1}(Z)\) a smooth submanifold. At \((p,x)\in\Sigma\), put \(Q=T_{F(p,x)}Y/T_{F(p,x)}Z\) and write \(L:T_pP\oplus T_xX\to Q\) for the surjective derivative of \(F\) followed by the normal quotient. The tangent space of \(\Sigma\) is \(\ker L\). The derivative of its projection to \(P\) is onto precisely when, for every \(v\in T_pP\), some \(w\in T_xX\) has \(L(v,w)=0\). If \(L(0,\cdot)\) is onto, choose \(w\) with image \(-L(v,0)\), proving this condition. Conversely, for any \(q\in Q\), choose \((v,w)\) with \(L(v,w)=q\) by surjectivity, then choose \(w'\) with \(L(v,w')=0\). It follows that \(L(0,w-w')=q\). Thus regularity of the projection at every point over \(p\) is equivalent to transversality of \(f_p\). Sard's theorem applied to that projection proves the assertion; its source is second countable, so countably many chart applications suffice. If the parameter manifold has dimension zero, transversality of \(F\) already says that every \(f_p\) is transverse. ∎

We may apply this lemma separately to finitely many boundary strata; each is a manifold without boundary. This includes a product of two compact manifolds with boundary, by using its interior–interior, interior–boundary, boundary–interior and boundary–boundary strata.

**Theorem H.2 — The required Whitney embedding bound.** Every compact smooth \(d\)-manifold without boundary embeds smoothly in \(\mathbb R^{2d+1}\), hence in every larger Euclidean dimension.

**Proof.** Take the finite embedding \(F\) just constructed and put \(h(w)=(1,F(w))\in\mathbb R^{L+1}\). For a matrix \(A:\mathbb R^{L+1}\to\mathbb R^{2d+1}\), consider \(G_A(w)=Ah(w)\).

On \(X=(W\times W)\setminus\Delta\), the difference \(h(w)-h(w')\) is nonzero. Therefore the parameter derivative of
\(\Psi(w,w',A)=A(h(w)-h(w'))\)
is surjective: for a nonzero vector \(z\), the linear map \(B\mapsto Bz\) onto the target is surjective, since \(B=yz^T/\|z\|^2\) sends \(z\) to any prescribed \(y\). The source-pair dimension is \(2d<2d+1\), so Lemma H.1 says that outside a null parameter set, \(G_A\) has no double point.

Choose a smooth metric on \(W\). On its unit tangent bundle, of dimension \(2d-1\) when \(d\geq1\), the vector \(Dh_wv=(0,DF_wv)\) is nonzero, since \(F\) is an immersion. Apply Lemma H.1 to \(A(Dh_wv)\). Outside another null parameter set, no nonzero tangent vector is killed by \(DG_A\). For \(d=0\) this tangent test is empty. A parameter outside both null sets gives an injective immersion. Compactness and the local inverse argument make it an embedding. Adding zero coordinates proves the larger-dimension assertion. ∎

This proves the bound used below. It does not need the stronger \(2d\)-dimensional Whitney theorem.

**The immersion bound.** Every compact smooth \(d\)-manifold without boundary also admits a smooth immersion into \(\mathbb R^{2d}\). For \(d\geq1\), use the same finite embedding \(F\) and \(h=(1,F)\) as above, now with matrices \(A:\mathbb R^{L+1}\to\mathbb R^{2d}\). On the unit tangent bundle the vector \(Dh_wv\) is nonzero, so the derivative in \(A\) of \(A(Dh_wv)\) is onto by the explicit matrix calculation in Theorem H.2. The source dimension is \(2d-1<2d\); Lemma H.1 therefore gives a parameter for which no unit tangent vector is killed. Every nonzero tangent vector is a positive scalar multiple of a unit vector, so \(D(Ah)\) is injective everywhere, proving immersion. At \(d=0\), the constant map into \(\mathbb R^0\) has injective zero-dimensional tangent maps. Injectivity on distinct points was not required. This is the immersion consequence of the tangent-direction argument in Mrowka's notes. ∎

**Theorem H.3 — Relative embedding of a cobordism.** Let \(W^{n+1}\) be a compact smooth cobordism with boundary identified with \(M_0\sqcup M_1\), and let \(j_i:M_i\hookrightarrow\mathbb R^m\) be given smooth embeddings. If
\[
m\geq2n+2,
\tag{H.1}
\]
there is a smooth embedding
\[
e:W\hookrightarrow[0,1]\times\mathbb R^m
\tag{H.2}
\]
which meets the boundary of the ambient cylinder only in \(\partial W\), and on sufficiently small inward collars has the formulas
\[
e(y,s)=(s,j_0(y)),\qquad
e(y,s)=(1-s,j_1(y)).
\tag{H.3}
\]
Closed components of \(W\) are allowed.

**Proof.** Use the full smooth-collar theorem from the cobordism chapter to choose disjoint collars at the two ends. Construct a smooth \(t:W\to[0,1]\) equal to \(s\) on a small bottom collar and \(1-s\) on a small top collar, with \(0<t<1\) elsewhere. For example use the collar cutoffs of Section E to interpolate these functions with the constant \(1/2\) away from the collars, retaining only collar segments of length less than \(1/4\). Define a smooth \(J:W\to\mathbb R^m\) equal to \(j_i(y)\) on slightly smaller collars, by multiplying each such boundary-coordinate function by a cutoff supported in its collar and extending by zero. Put \(G_0=(t,J)\).

Choose a smooth nonnegative \(\lambda\) equal to zero on closed still smaller end collars, positive everywhere else, and equal to one away from larger end collars. A smooth scalar step in the collar coordinate gives this explicitly. Choose its zero set inside the region where \(G_0\) has precisely the product formulas (H.3). The support of \(\lambda\) is compact and disjoint from \(\partial W\). On that support both \(t\) and \(1-t\) consequently have a common positive lower bound.

Take a finite smooth embedding \(F:W\to\mathbb R^L\) as above and set
\[
h(w)=\lambda(w)(1,F(w)),\qquad
G_A(w)=G_0(w)+Ah(w),
\tag{H.4}
\]
where \(A\) is a matrix with target \(\mathbb R^{m+1}\). For all sufficiently small \(A\), the change of the time coordinate is smaller than half that positive lower bound: use the finite maximum of \(\|h\|\) on compact \(W\). Thus \(G_A\) maps the interior to \((0,1)\times\mathbb R^m\) and has the prescribed end values.

We choose such a small \(A\) with no double point and no singular tangent. For distinct \(w,w'\) with at least one \(\lambda\) positive, \(h(w)-h(w')\ne0\). If one is zero this follows from the first coordinate of \(h\); if both are positive and those first coordinates agree, division recovers \(F(w)\) and \(F(w')\), which are different. Hence the parameter derivative of \(G_A(w)-G_A(w')\) is surjective. On each of the boundary strata of these pairs, the source dimension is at most \(2(n+1)\), whereas the target dimension is \(m+1\geq2n+3\). Lemma H.1 removes all these double points outside a null parameter set. Pairs where both \(\lambda=0\) already have different \(G_0\)-images: the two end collars have disjoint time intervals, and within either collar \((s,j_i(y))\) is injective. Their images are unchanged by (H.4).

For tangent injectivity, if \(\lambda(w)>0\) and \(v\ne0\), then \(Dh_wv\ne0\). Indeed its first component would otherwise give \(d\lambda_wv=0\), and its remaining components then give \(\lambda(w)DF_wv=0\), impossible for an immersion. On the unit tangent bundle over this interior region, dimension \(2(n+1)-1\), the parameter derivative of
\(DG_0(w)v+A(Dh_wv)\)
is again surjective. Lemma H.1 excludes all its zeros outside a null parameter set. Where \(\lambda=0\), its derivative is zero too: at an interior point this is the derivative of a smooth nonnegative function at its minimum, and on the boundary collar it is identically zero. Thus \(DG_A=DG_0\) there, and the product formulas already make it injective.

Choose \(A\) in the required small open parameter ball outside the finitely many null sets. The resulting map is an injective immersion of compact \(W\), hence a smooth embedding by the same compactness and local chart proof. It is exactly \(G_0\) on the zero collars of \(\lambda\), so satisfies (H.3); the time bound establishes the ambient-boundary claim. ∎

The normal bundle of this embedded cobordism has rank \(m-n\). On its collars it is the normal bundle of \(j_i\) in the spatial Euclidean factor. If \(W\) is an oriented cobordism and the ambient cylinder has time-first orientation, its tangent-first normal orientation restricts to the previously defined normal orientation at both ends: the time direction occurs first in both splittings. This compatibility will be used in the collapse homotopy.

## I. The collapse map and surjectivity

The universal target is a CW space, with its smooth finite Grassmannian stages from Lemma D.2. Thus Theorem G.3 defines homomorphisms
\[
\Phi:\pi_{n+k}(MSO(k),t_0)\longrightarrow\Omega_n,\qquad
\Phi^O:\pi_{n+k}(MO(k),t_0)\longrightarrow\mathcal N_n,
\tag{I.1}
\]
for \(k\geq1\) and \(n\geq0\). Here \(\mathcal N_n\) denotes unoriented bordism. To define one, place a sphere representative in a finite canonical Thom space and take its transverse inverse image there. Increasing the finite stage leaves that manifold unchanged: the inclusion is the canonical bundle inclusion and induces the identity on the rank-\(k\) normal quotient along the zero section. If two representatives are homotopic in the universal space, their homotopy lies in a common finite stage by Lemma D.2, where Theorem G.3 proves equality of their bordism classes. A common stage also compares sums. This establishes the universal maps without assigning a smooth structure to the infinite Thom space.

We give the collapse map with a useful exact local form. Let \(j:M^n\hookrightarrow\mathbb R^m\) be a smooth embedding of a closed manifold, \(m=n+k\), \(k\geq1\). Its Euclidean normal bundle \(\nu\) is the orthogonal complement of \(TM\). If \(M\) is oriented, orient \(\nu\) by
\[
(TM,\nu)=T\mathbb R^m
\tag{I.2}
\]
in that order. The smooth Gauss map \(b:M\to G_k(\mathbb R^m)\), with the induced orientation in the oriented case, sends \(y\) to its normal plane. The bundle embedding \(\beta_y:\nu_y\hookrightarrow\mathbb R^m\) is the ordinary inclusion, identifying \(\nu\) with the pullback of the canonical bundle.

The Euclidean case of the full tubular theorem provides a number \(\rho>0\) for which
\[
\Psi(y,v)=j(y)+v,\qquad \|v\|\leq\rho,
\tag{I.3}
\]
is injective and a diffeomorphism on the open disk bundle onto its open image. Choose \(\rho\) strictly smaller than the theorem's injectivity radius; the closed disk bundle is compact and hence maps homeomorphically onto a closed subset of \(\mathbb R^m\). Its derivative at zero is the tangent/normal direct sum, so the stated open-image property is the inverse-function theorem. The compact radius exists by the same contradiction used in the earlier tubular proof: coincident images of distinct normal vectors with norms tending to zero would have the same limiting base and contradict the local inverse there.

Choose a smooth positive radial factor \(a(r)\), smooth as a function of \(r^2\) for \(r<\rho\), with
\[
a(r)=1\quad(r\leq\rho/3),\qquad
a(r)=\frac1{\sqrt{1-r^2/\rho^2}}\quad(r\geq2\rho/3).
\tag{I.4}
\]
A smooth cutoff between these two positive functions gives one. In the total-vector coordinates \(E(\gamma_k^m)=T(\gamma_k^m)\setminus\{t_0\}\), set
\[
c_j(\Psi(y,v))=\kappa\bigl(b(y),a(\|v\|)\beta_y(v)\bigr)
\quad(\|v\|<\rho),
\tag{I.5}
\]
and send the complement of that open tube to \(t_0\). Here \(\kappa\) is the inverse radial map in (C.2).

This is continuous, including along the tube boundary. For \(\|v\|\geq2\rho/3\), its closed-disk representative is
\[
\frac{\beta_y(v)}
{\sqrt{\,1-\|v\|^2/\rho^2+\|\beta_y(v)\|^2\,}}.
\tag{I.6}
\]
At \(\|v\|=\rho\) it has norm one, so extends continuously to the collapsed sphere bundle. Near zero it is defined smoothly by (I.5), and these two disk formulas agree where both are used. The resulting map on the closed normal disk bundle followed by the Thom quotient agrees with the constant map on its boundary. Paste it with the constant map on the closed complement of the open tube, a finite closed cover of \(S^m=\mathbb R^m\cup\{\infty\}\). This proves continuity on the sphere. The support is in a compact tube, so it is based at \(\infty\).

The map is smooth at every noncollapsed point and transverse to zero. Near \(M\) its total-vector form is exactly
\[
(y,v)\longmapsto(b(y),\beta_y(v)).
\tag{I.7}
\]
Its zero inverse image is \(j(M)\), and its induced orientation is the original one by (I.2). Thus
\[
\Phi([c_j])=[M],
\qquad\text{or}\qquad
\Phi^O([c_j])=[M]
\tag{I.8}
\]
in the respective case.

The same construction works for any smooth fibrewise injection
\(q:\nu\to\mathbb R^N\), taking \(b_q(y)=q(\nu_y)\) with the orientation carried from \(\nu_y\) when required, and replacing \(\beta\) by \(q\) in (I.5)–(I.6). Its boundary formula still has norm one, because at \(r=\rho\) the denominator is \(\|q(v)\|>0\). Its exact germ is \((b_q(y),q(v))\). A smooth family of such injections defines a based homotopy of collapse maps: over compact \(M\times[0,1]\), their smallest singular values have a common positive lower bound, ensuring the same boundary extension, and all values lie in one finite Grassmannian Thom space.

**Theorem I.1 — Surjectivity with a finite target (MS 18.7).** If \(k>n\) and \(p\geq n\), the finite inverse-image homomorphism for the canonical rank-\(k\) bundle over the oriented \(G_k(\mathbb R^{k+p})\) surjects onto \(\Omega_n\). The analogous unoriented map surjects onto \(\mathcal N_n\).

**Proof.** Theorem H.2 embeds every closed \(n\)-manifold in \(\mathbb R^{2n+1}\). Since \(k>n\) means \(n+k\geq2n+1\), adding zero coordinates embeds it in \(\mathbb R^{n+k}\). Its normal Gauss bundle and (I.5) give a map into the canonical Thom space over \(G_k(\mathbb R^{n+k})\), oriented or not. Include this in \(G_k(\mathbb R^{k+p})\) using \(p\geq n\). Its inverse image is the given manifold by (I.8). This proves surjectivity using the embedding bound actually established, rather than citing Whitney's theorem as a prerequisite. It also proves surjectivity of (I.1) in that range. ∎

For \(n=0\) a closed oriented zero-manifold is a finite set of signed points. Formula (I.2) assigns to a negative point the opposite normal orientation, so (I.8) records its negative contribution. An unoriented zero-manifold records only its number of points modulo the unoriented interval-boundary relation. These conventions agree with the earlier signed \(\Omega_0=\mathbb Z\) computation.

## J. Why a transverse map is homotopic to its collapse

The inverse of the Thom correspondence requires more than constructing one map with a prescribed inverse image. We must show that the original transverse map carries no additional homotopy data once its embedded inverse image and its universal normal structure are accounted for.

**Lemma J.1 — The complement of zero contracts.** In a positive-rank Thom space, the complement \(T(\xi)\setminus B\) contracts to \(t_0\), fixing \(t_0\). If two based maps from a compact smooth manifold have the same compact zero inverse image \(M\) and agree on a neighbourhood of \(M\), they are based homotopic.

**Proof.** In the closed disk model, for \(v\ne0\) use
\[
R_s([v])=\left[\left(1-s+\frac{s}{\|v\|}\right)v\right],
\quad 0\leq s\leq1,
\qquad R_s(t_0)=t_0.
\tag{J.1}
\]
The norm is \((1-s)\|v\|+s\), positive and at most one. On the unit sphere the vector is unchanged, so the formula descends through its collapse. The restriction of that quotient to the complement of zero is quotient, since this is an open saturated subset, and its product with \(I\) is quotient by the proved locally compact product lemma. This proves continuity, also at the collapsed point. At \(s=1\) every vector has norm one and maps to \(t_0\).

For the map comparison, choose an open \(V\) on which \(f=g\), containing their common compact inverse image \(M\). A smooth cutoff gives \(\chi=0\) near \(M\) and \(\chi=1\) outside \(V\). Deform \(f(x)\) by \(R_{s\chi(x)}\) wherever \(\chi(x)>0\), and leave it unchanged where \(\chi=0\). The former values avoid zero; near \(M\) the deformation is identically \(f\), so it is continuous there too. Do the same for \(g\). At time one both maps are \(t_0\) outside \(V\), and inside \(V\) they have equal initial values and equal deformation amounts. Their endpoints therefore agree. Joining the first deformation to the reverse of the second gives a homotopy. Equation (J.1) fixes the target basepoint, so this is a based homotopy. If \(M\) is empty, apply the contraction to both maps everywhere. ∎

**Lemma J.2 — Straightening the normal germ.** Let
\(f:S^m\to T(\gamma_k^N)\) be based, smooth off its collapsed-point preimage and transverse to the zero section of the finite canonical bundle, oriented or not. Put \(M=f^{-1}(G_k(\mathbb R^N))\), and view \(M\) in the oriented Euclidean chart \(S^m\setminus\{\infty\}=\mathbb R^m\). There is a based homotopy to a map which, in a Euclidean normal tube of \(M\), has the exact total-vector form
\[
(y,v)\longmapsto(b(y),\alpha_y(v)).
\tag{J.2}
\]
Here \(b=f|_M\) and
\(\alpha:\nu_M\to b^*\gamma_k^N\)
is the normal isomorphism induced by \(Df\). The homotopy has compact support in that tube and introduces no new zero.

**Proof.** The case \(M=\varnothing\) follows from Lemma J.1. Otherwise compactness and the smooth noncollapsed region give a small closed Euclidean normal tube \(\Psi(y,v)=y+v\) entirely in that region. Write its total-vector map as
\[
f_E\Psi(y,v)=\bigl(b(y,v),w(y,v)\bigr),
\]
where \(w(y,v)\) lies in the plane \(b(y,v)\subset\mathbb R^N\), \(b(y,0)=b(y)\), and \(w(y,0)=0\).

Let \(P(y,v)\) be the orthogonal projection onto \(b(y,v)\), and \(P_0(y)=P(y,0)\). On a sufficiently small uniform tube, compactness gives
\(\|P(y,v)-P_0(y)\|<1/2\).
Thus
\[
A(y,v)=P_0(y)|_{b(y,v)}:b(y,v)\longrightarrow b(y)
\tag{J.3}
\]
is an isomorphism: if \(P_0u=0\) and \(u=P(y,v)u\), then
\(\|u\|\leq\|P(y,v)-P_0\|\|u\|<\|u\|/2\), forcing \(u=0\); equal dimensions give surjectivity. Its inverse is smooth in local bundle frames by the adjugate formula. In the oriented case it preserves the indicated orientations, because the path \(v\mapsto tv\) keeps it invertible and ends at the identity at zero.

Put \(\varphi(y,v)=P_0(y)w(y,v)\in b(y)\). Its normal derivative at zero is \(\alpha_y\), an isomorphism by Lemma G.1. The minimum of \(\|\alpha_yv\|\) on the compact unit normal sphere bundle is a positive \(c\). Bounded second fibre derivatives on finitely many charts covering a compact tube, and the iterated fundamental theorem of calculus along \(tv\), give a uniform estimate
\[
\|\varphi(y,v)-\alpha_yv\|\leq C\|v\|^2.
\tag{J.4}
\]
Shrink the radius so that \(C\|v\|<c/2\) at nonzero vectors there. Every convex interpolation
\(\varphi_\tau=(1-\tau)\varphi+\tau\alpha_yv\)
then stays within \(\|\alpha_yv\|/2\) of \(\alpha_yv\), and consequently is nonzero for \(v\ne0\).

For \(0\leq\tau\leq1\) use the base plane \(b(y,(1-\tau)v)\) and vector
\[
A(y,(1-\tau)v)^{-1}
\bigl((1-\tau)\varphi(y,v)+\tau\alpha_yv\bigr)
\tag{J.5}
\]
in that plane. At \(\tau=0\) this is the original \(w(y,v)\); at \(\tau=1\) it is \(\alpha_yv\) over \(b(y)\). Its only zeros are \(v=0\), where the base stays \(b(y)\). To localize, replace \(\tau\) everywhere by \(t\lambda(\|v\|^2)\), with \(\lambda=1\) on a smaller tube and zero near the chosen tube boundary. This equals \(f\) outside a compact subset of the tube, so pastes to a continuous based homotopy on the sphere. It is smooth in the tube and has the exact endpoint (J.2) on its smaller part. No zero was introduced by the interpolation or by the fixed outside map. ∎

**Proposition J.3 — Universal normal structure adds no further choice.** Every based map \(S^{n+k}\to MSO(k)\), after the transverse approximation, is based homotopic to the canonical Gauss collapse of its embedded oriented inverse-image manifold in \(\mathbb R^{n+k}\). The same assertion holds for \(MO(k)\) without orientations.

**Proof.** Place the transverse map in a finite canonical stage. In the oriented case give \(M\) its inverse-image orientation and its Euclidean normal bundle the orientation (I.2). The normal isomorphism \(\alpha\) of Lemma J.2 preserves this orientation: both are defined by the same ordered tangent/normal splitting of the positive source tangent space. Regard \(\alpha:\nu_M\to\mathbb R^N\) as a fibrewise injection.

By Lemma J.2 the original map is homotopic to one with the linear germ \((b,\alpha v)\). Section I constructs a collapse \(c_\alpha\) with precisely that germ and precisely the same zero set \(M\). Lemma J.1 makes the two maps homotopic in their common finite canonical Thom space.

Let \(\beta:\nu_M\to\mathbb R^m\), \(m=n+k\), be the usual Euclidean normal inclusion. Increase \(N\) if needed so \(N\geq m\). In \(\mathbb R^N\oplus\mathbb R^m\), the following two paths of bundle injections join \((\alpha,0)\) to \((\beta,0)\):
\[
q_t(v)=\bigl(\cos(\pi t/2)\alpha(v),\,\sin(\pi t/2)\beta(v)\bigr),
\tag{J.6}
\]
followed by
\[
q'_t(v)=\bigl(\sin(\pi t/2)\beta(v),\,\cos(\pi t/2)\beta(v)\bigr),
\tag{J.7}
\]
where the first \(\beta\) in (J.7) occupies the first \(m\) coordinates of \(\mathbb R^N\). Neither path has a kernel, because at least one nonzero coefficient multiplies an injection. The intermediate plane is oriented by pushing forward the fixed orientation of \(\nu_M\). Smoothly reparametrize each interval with a scalar step flat at its endpoints; concatenation is then a smooth family. By the family assertion following (I.8), this defines a based homotopy \(c_\alpha\simeq c_\beta\) in one finite larger Thom stage.

The final collapse \(c_\beta\) is the canonical Gauss collapse of the embedded \(M\), with the standard finite-stage coordinate inclusion. This proves the proposition. The unoriented argument uses the same injections and homotopies, retaining no plane orientation. ∎

In particular, choices of tube radius and radial cutoff in the canonical collapse do not affect its based class: they have the same exact germ (I.7) on a sufficiently small common Euclidean tube and the same zero set, so Lemma J.1 applies. This deals with the actual collapse choices before using them on a cobordism.

## K. The full Pontryagin–Thom correspondence

**Theorem K.1 — Thom's correspondence in the stated range.** For \(n\geq0\) and \(k>n+1\), the inverse-image homomorphisms are isomorphisms
\[
\pi_{n+k}(MSO(k),t_0)\cong\Omega_n,\qquad
\pi_{n+k}(MO(k),t_0)\cong\mathcal N_n.
\tag{K.1}
\]
The map from left to right is transverse inverse image, with the tangent-first normal orientation in the oriented case. The inverse is the normal Gauss collapse of any embedding in \(\mathbb R^{n+k}\).

**Proof.** Put \(m=n+k\). Surjectivity was proved in Theorem I.1 already for \(k>n\). For injectivity, let two based classes have equal bordism images. Proposition J.3 represents them by the canonical collapse maps \(c_{j_0}\) and \(c_{j_1}\) of their embedded inverse images \(j_i:M_i\subset\mathbb R^m\). In the oriented case the equality means there is a compact oriented cobordism \(W\) with
\(\partial W=(-M_0)\sqcup M_1\); this is the established definition of equality in \(\Omega_n\). In the unoriented case use the corresponding unoriented cobordism.

The dimension hypothesis gives \(m\geq2n+2\), so Theorem H.3 embeds \(W\) in \([0,1]\times\mathbb R^m\), retaining the product end collars \((s,j_0(y))\) and \((1-s,j_1(y))\). In the oriented case give this ambient cylinder the time-first orientation. Give its rank-\(k\) Euclidean normal bundle \(\nu_W\) the orientation determined by
\[
(TW,\nu_W)=T([0,1]\times\mathbb R^m).
\tag{K.2}
\]
On the end collars, the normal vectors are purely spatial, and their normal orientation is precisely that of \(\nu_{j_i}\), by the end-orientation compatibility in Theorem H.3.

There is a compact closed normal disk tube of \(W\) in the ambient cylinder, with the usual spatial Euclidean tube on its ends. Here are the boundary details. Extend each product collar a small distance across the ambient end boundary, using the same formula \((t,j_i(y))\). The extended embedded submanifold has no boundary near the original \(W\); thus the normal map \(e(y)+v\) has a local inverse there, including at the original boundary points. Compactness of \(W\) gives one uniform injectivity radius by the limiting-pair contradiction of Section I. On a smaller end collar its normal vectors have time component zero, so its normal tube stays at the same time. Away from those collars the time coordinate of \(e(W)\) is bounded away from zero and one; shrink the uniform radius below half that bound. The tube therefore lies in the ambient cylinder and is relatively open there, with precisely its product end intersections. Its closed disk bundle is compact and embedded.

Classify \(\nu_W\) by its normal inclusion in \(\mathbb R^{m+1}\). For this bundle embedding record the spatial coordinates first and the time coordinate last. This fixed orthogonal coordinate permutation is used only in the target normal-vector space; the ambient cylinder orientation remains time first. On an end collar its bundle embedding is then exactly
\[
v\in\nu_{j_i}\longmapsto(v,0)\in\mathbb R^m\oplus\mathbb R,
\tag{K.3}
\]
with the normal orientation just checked.

Apply the collapse formula of Section I fibrewise to this tube over compact \(W\), using the same radial factor with plateau one near zero, and send its complement to \(t_0\). The closed-cover pasting proof works on the cylinder too. The result is a continuous map
\[
C_W:[0,1]\times S^m\longrightarrow MSO(k)
\tag{K.4}
\]
or \(MO(k)\), with values in the finite canonical Thom stage over \(G_k(\mathbb R^{m+1})\). Since the tube is spatially bounded uniformly in time, \([0,1]\times\{\infty\}\) is mapped to \(t_0\). This is consequently a based homotopy. At each end, (K.3) makes its restriction the canonical collapse of \(j_i\), included in that finite stage, with the common small radius. Changing the radius or cutoff from the choices in \(c_{j_i}\) does not alter their based classes, by the exact-germ conclusion of Proposition J.3. Thus (K.4) proves \([c_{j_0}]=[c_{j_1}]\).

This proves injectivity, and hence (K.1). It simultaneously shows that the collapse inverse depends only on the abstract bordism class, even when the chosen embedding and its finite target stage vary. All orientation calculations were retained at both ends; the unoriented proof uses the identical embeddings, normal tubes, contraction and collapse without orientation data. ∎

The two dimension bounds have different jobs. The weaker \(k>n\) provides an embedding of a closed \(n\)-manifold and gives surjectivity. The stated \(k>n+1\) provides a relative embedding of an \((n+1)\)-dimensional cobordism and gives injectivity. No unproved ambient isotopy or classification of knots was used to pass between them.

## L. Examples: the real line and the first bordism classes

**Example L.1 — The canonical real-line Thom space.** For the tautological line over \(\mathbb RP^{N-1}\), \(N\geq1\),
\[
T(\gamma^1_{N-1})\cong\mathbb RP^N
\tag{L.1}
\]
as pointed spaces, with basepoint \([1:0:\cdots:0]\). Represent a base line by a unit vector \(u\in S^{N-1}\), and a total-space vector by \(su\), \(-1\leq s\leq1\), in its closed unit disk. The formula
\[
([u],su)\longmapsto[s:\sqrt{1-s^2}\,u]
\tag{L.2}
\]
is independent of the choice \(u\): replacing \(u,s\) by \(-u,-s\) changes every projective coordinate by the same sign. It is continuous in the local choices of \(u\). At \(|s|=1\) it gives the one stated basepoint, so descends through the entire sphere-bundle collapse.

It is bijective after that collapse. Away from the basepoint, a projective point \([a:x]\) with \(x\ne0\) recovers the base \([x]\); normalization of \((a,x)\) to unit length recovers \(s\) and \(\sqrt{1-s^2}u\), up to their common sign. At the basepoint the sphere bundle is exactly its inverse image. The domain quotient is compact and the projective target Hausdorff, so this continuous bijection is a homeomorphism.

Increasing \(N\) appends a zero coordinate in (L.2), preserving its distinguished first coordinate. The finite homeomorphisms are therefore compatible. Both infinite spaces have the weak topology of these finite stages: for the Thom space test on its characteristic cells from Section C, and for projective space use its standard CW structure. Hence
\[
MO(1)=T(\gamma^1\to\mathbb RP^\infty)\cong\mathbb RP^\infty.
\tag{L.3}
\]
This is a pointed homeomorphism, not just a comparison of their cohomology.

To compute the first unoriented bordism groups we need the following elementary smooth classification in its compact closed case.

**Lemma L.2 — Closed one-manifolds.** Every closed smooth one-manifold is a finite disjoint union of smooth circles.

**Proof.** Choose finitely many closed coordinate arcs \(A_i\), each lying in a larger open coordinate arc, whose interiors cover the compact manifold. Let \(V\) be the finite set of their endpoints. Each connected component of the manifold meets \(V\), and there are only finitely many components: each connected covering arc lies in one component, and finitely many such arcs cover all points.

A component \(U\) of the complement of \(V\) lies inside one \(A_i\). Choose \(A_i\) whose interior contains one point of \(U\). Its boundary consists of its two endpoints in \(V\). Thus the disjoint relatively open sets \(U\cap\operatorname{int}A_i\) and \(U\setminus A_i\) partition \(U\); connectedness and the first set's nonemptiness force the second to be empty. Inside that coordinate arc, \(U\) is one of the open intervals between the finitely many points of \(V\). Finitely many such interval pieces cover the complement, so only finitely many \(U\) occur. Their closures are coordinate closed intervals with endpoints in \(V\). Around each vertex of \(V\) a sufficiently small coordinate interval misses every other vertex and has exactly two sides. Consequently these arcs form a finite graph in which every vertex has valence two.

Each connected graph component is a cycle: follow an edge and at each vertex take the other incident edge. Finiteness forces return to the starting cycle, and no remaining edge can attach to it without giving a vertex a third incidence. Traversing the cycle gives consistent choices of positive tangent direction on all open edges and in the small vertex charts. They define an orientation of the smooth one-manifold component.

A smooth partition subordinate to positively oriented charts now yields a smooth nowhere-zero field: sum the positive coordinate fields with nonnegative partition weights. Every active term points in the same positive direction, so their sum never vanishes. The proved local-flow lemma supplies its flow. On a compact component it exists for all real times: finitely many local flow neighbourhoods give a common positive existence time, and uniqueness lets us concatenate such intervals indefinitely in either direction.

Every flow orbit is open, since its nonzero time derivative and the one-dimensional inverse-function theorem give a local arc parametrization. Distinct orbits partition the connected component into open sets, so one orbit fills it. The map \(\mathbb R\to C\), \(t\mapsto\varphi_t(p)\), is therefore a surjective local diffeomorphism. Its period set is a closed additive subgroup, isolated at zero by local injectivity. It cannot be \(\{0\}\), since then this map would be a bijective local diffeomorphism, hence a diffeomorphism from noncompact \(\mathbb R\) onto compact \(C\). A nonzero period gives a positive one; closedness and isolation show that the smallest positive period \(T\) exists. Division with remainder then gives the period subgroup \(T\mathbb Z\). The induced bijective local diffeomorphism \(\mathbb R/T\mathbb Z\to C\) is a diffeomorphism. The exponential parametrization identifies its source with \(S^1\). This proves the assertion on each of the finitely many components. ∎

**Example L.3 — Unoriented degrees zero, one and a degree-two witness.** The groups in the first two degrees are
\[
\mathcal N_0=\mathbb F_2,\qquad \mathcal N_1=0.
\tag{L.4}
\]
A zero-manifold is a finite set of points, and an interval bounds two of them. The parity of a boundary is zero: the proved mod-two boundary-fundamental identity sends \([\partial W]\) to zero in \(H_0(W;\mathbb F_2)\); the augmentation to \(\mathbb F_2\), which sums point coefficients, therefore gives zero. Thus parity is the complete zero-dimensional invariant, since disjoint intervals fill every even number of points.

Lemma L.2 makes a closed one-manifold a finite disjoint union of circles, and a disjoint union of disks fills it. This proves the degree-one assertion. In degree two, \(\mathbb RP^2\) is nonzero in \(\mathcal N_2\): its proved tangent formula gives \(w_1=a\), \(w_2=a^2\), and
\[
\langle w_1^2,[\mathbb RP^2]_2\rangle
=\langle w_2,[\mathbb RP^2]_2\rangle=1.
\tag{L.5}
\]
These numbers vanish on boundaries, as already proved. Formula (L.5) is a nonzero class witness; the complete detection theorem for unoriented bordism is a further obligation of the course.

**Example L.4 — A projective collapse of infinite order.** Give \(\mathbb CP^2\) its complex orientation. Its tangent Pontryagin calculation gives \(p_1[\mathbb CP^2]=3\). Choose an embedding in \(\mathbb R^{10}\), supplied by Theorem H.2 and adding one coordinate, and its oriented rank-six normal Gauss collapse. Theorem K.1 identifies its class in
\(\pi_{10}(MSO(6))\) with \([\mathbb CP^2]\in\Omega_4\). It has infinite order because the integer homomorphism \(p_1:\Omega_4\to\mathbb Z\) sends its \(r\)-fold multiple to \(3r\). This exhibits the nonzero rational class. Proving that it spans all of \(\Omega_4\otimes\mathbb Q\) requires the rational homotopy estimate in the continuation of this lesson.

## M. Graded exercises with solutions

**Exercise M.1 — Easy: trivial bundles and the basepoint.** Identify \(T(\varepsilon^k_B)\), including \(k=0\), and explain why the trivial line over \(\mathbb R\) does not have Thom space \(S^2\).

**Solution.** The disk bundle is \(B\times D^k\), and its sphere bundle is \(B\times\partial D^k\). After adjoining the disjoint basepoint of \(B_+\), the equivalence relation is exactly the smash relation, so
\(T(\varepsilon^k_B)=B_+\wedge S^k=\Sigma^kB_+\).
The quotient-product proof of (C.6) verifies the topology for arbitrary Hausdorff \(B\); at \(k=0\) the empty sphere convention gives \(B_+\wedge S^0=B_+\). For \(B=\mathbb R\), the homological Thom isomorphism gives only \(\widetilde H_1=\mathbb Z\). In contrast the total space \(\mathbb R^2\) has one-point compactification \(S^2\), with its nonzero reduced homology in degree two. The compact-base hypothesis for that replacement has failed.

**Exercise M.2 — Easy: the finite real-line model.** Prove (L.1) directly from the closed disk bundle, and verify that its inclusions give (L.3).

**Solution.** Write a disk vector as \(su\) with \(u\) unit in its unoriented base line. Send it to \([s:\sqrt{1-s^2}u]\). The two choices of \(u\) negate all coordinates simultaneously. At both endpoints \(|s|=1\) the value is \([1:0]\); every other projective point uniquely recovers its base line and disk vector by normalizing its coordinates. Thus this defines a continuous bijection from the compact sphere-collapse quotient onto Hausdorff \(\mathbb RP^N\), hence a homeomorphism. Appending a zero coordinate commutes with the formula and fixes \([1:0]\). The weak finite-stage topologies make the resulting infinite bijection and its inverse continuous, proving \(MO(1)\cong\mathbb RP^\infty\).

**Exercise M.3 — Medium: the regular-value perturbation.** Prove MS 18.5 with its relatively closed set \(X\), including retention of regularity on \(X\) throughout the perturbing homotopy.

**Solution.** For empty \(K\), the original map and constant homotopy suffice. For nonempty \(K\), choose a smooth \(\lambda\in[0,1]\) equal to one near the prescribed compact \(K\), supported in compact \(K'\subset W\). The set \(Y=X\cap K'\) is compact. Lemma E.1 supplies value and derivative tolerances \(\delta,\eta\) there. Sard supplies a regular value \(v\) of \(f\) with
\[
\|v\|<\min\{\varepsilon,\delta,\eta/(1+\sup_{K'}\|D\lambda\|)\}.
\]
Set \(f_t=f-t\lambda v\). The value and derivative changes satisfy both tolerances uniformly for \(0\leq t\leq1\), so each map retains regularity on \(Y\). Off \(K'\) nothing changed; thus it retains regularity on all \(X\). At the endpoint and near \(K\), \(g=f-v\), whose zeros are regular since \(v\) was a regular value. The support and uniform \(\varepsilon\)-bound are immediate. The right-inverse and Neumann-series proof in Lemma E.1 supplies the stability premise.

**Exercise M.4 — Medium: why a derivative bound is needed.** Find smooth maps \(\mathbb R^2\to\mathbb R\) uniformly approaching \(f(x,y)=x\), each with a critical zero. Explain why this does not contradict Lemma E.1.

**Solution.** For \(\varepsilon>0\), put
\[
g_\varepsilon(x,y)=x-\varepsilon\sin(x/\varepsilon).
\]
Its uniform difference from \(f\) is at most \(\varepsilon\), tending to zero. But at \(x=0\) it vanishes, and its derivative is
\((1-\cos(x/\varepsilon),0)=(0,0)\).
Thus every point \((0,y)\) is a critical zero. The derivative difference at those points has norm one and does not tend to zero. Lemma E.1 requires both types of estimate, precisely excluding this example.

**Exercise M.5 — Medium: the cobordism endpoint signs.** Orient \([0,1]\times S^m\) by time first. For a transverse homotopy constant near both ends, compute the oriented boundary of its zero inverse image. Also explain why placing the time coordinate last in the normal bundle's target coordinates in (K.3) introduces no extra sign.

**Solution.** On an end collar the tangent/normal splitting is
\((\partial_t,TM_i,\xi)=(\partial_t,TS^m)\).
Thus the inverse-image cobordism has time-first product orientation. Its outward vector is \(-\partial_t\) at zero and \(+\partial_t\) at one, so the boundary is \((-M_0)\sqcup M_1\). This agrees with the boundary inverse-image theorem because normal lifts can be chosen tangent to the ambient boundary. In (K.3) a fixed coordinate permutation is applied to the bundle injection, and the target plane is oriented by the pushforward of its already fixed normal orientation. It is not being assigned an orientation from the ambient target coordinate order. The source cylinder orientation stays time first, and the end normal map is exactly the spatial inclusion. Hence there is no additional \((-1)^m\) factor.

**Exercise M.6 — Hard: an explicit normal straightening.** Near \(v=0\), let \(b(v)\subset\mathbb R^2\) be the oriented line spanned positively by \((1,v)\), and let \(w(v)=(v+v^2)(1,v)\). Compute (J.5) and verify that it has no zero for \(0<|v|<1/2\).

**Solution.** The zero plane is \(\mathbb Re_1\), so \(P_0w=(v+v^2)e_1\), and the normal linear term is \(\alpha v=ve_1\). The base line at time \(\tau\) is spanned by \((1,(1-\tau)v)\). Projection onto the first coordinate has inverse \(ze_1\mapsto z(1,(1-\tau)v)\) on that line. Therefore the vector in (J.5) is
\[
\bigl(v+(1-\tau)v^2\bigr)\bigl(1,(1-\tau)v\bigr).
\]
Its scalar factor is \(v(1+(1-\tau)v)\). The second factor is strictly positive when \(|v|<1/2\), for every \(0\leq\tau\leq1\); the line vector itself is nonzero. At time zero this is \(w(v)\), and at time one it is \(ve_1\) over the fixed zero plane. A radial cutoff in the effective time parameter makes the homotopy local exactly as in Lemma J.2.

**Exercise M.7 — Hard: the two embedding bounds.** Explain why the proven \(2d+1\) bound yields surjectivity for \(k>n\), but the proof of injectivity uses \(k>n+1\). Give the parameter argument for retaining arbitrary boundary collars.

**Solution.** A closed \(n\)-manifold embeds in \(\mathbb R^{2n+1}\), so a rank-\(k\) normal embedding in \(\mathbb R^{n+k}\) is available for \(k\geq n+1\). This gives its collapse representative and surjectivity. A cobordism has dimension \(d=n+1\); its relative embedding must lie in a target cylinder of dimension \(n+k+1\). The bound \(n+k+1\geq2(n+1)+1\) is exactly \(k\geq n+2\).

For the relative construction begin with \(G_0=(t,J)\) having the fixed end products, and a finite embedding \(F\) of the whole compact cobordism. Let \(h=\lambda(1,F)\), where \(\lambda=0\) on smaller end collars and positive elsewhere, and consider \(G_A=G_0+Ah\). At a pair of distinct points with at least one \(\lambda>0\), the vector \(h(w)-h(w')\) is nonzero; thus varying \(A\) surjects onto the difference target. Pair strata have dimension at most \(2d<D\), so Lemma H.1 excludes double points for parameters outside a null set. At \(\lambda>0\), \(Dh(v)\ne0\) for \(v\ne0\); the same lemma on the unit tangent bundle, dimension \(2d-1<D\), excludes singular tangents. At \(\lambda=0\) the original product immersion and injection remain unchanged. A sufficiently small good parameter keeps interior time in \((0,1)\). Compactness then makes \(G_A\) an embedding with the prescribed collars. The smaller surjectivity bound alone would not justify this relative step.

**Exercise M.8 — Medium: the first unoriented classes.** Compute \(\mathcal N_0,\mathcal N_1\) and exhibit a nonzero degree-two class using the proved characteristic-number obstruction.

**Solution.** The parity of a zero-manifold is invariant under boundaries by the mod-two boundary-fundamental identity and augmentation of \(H_0\). Two points bound an interval; pair every point of an even set to fill it. Hence \(\mathcal N_0=\mathbb F_2\). Lemma L.2 proves that every closed smooth one-manifold is a finite union of circles; disks fill them, so \(\mathcal N_1=0\). On \(\mathbb RP^2\), \(w_1=a\), \(w_2=a^2\), and evaluation of either \(w_1^2\) or \(w_2\) is one. The boundary-vanishing theorem therefore makes its degree-two bordism class nonzero. This last argument exhibits a class and does not supply the later completeness theorem for characteristic-number detection.

## References and scope of this chapter

Allen Hatcher's [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) gives the cellular-approximation treatment. Tomasz Mrowka's [*Geometry of Manifolds*](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/) offers accessible lecture notes on Sard's theorem, dimension-controlled embeddings and parametric transversality. Haynes Miller's [*Notes on Cobordism*](https://math.mit.edu/~hrm/papers/cobordism.pdf), from lectures typed by Dan Christensen and Gerd Laures, develops the bordism and Thom-space viewpoint.

The chapter proves the compact-slice measure estimate, cellular approximation, smooth approximation at the collapsed point, relative embedding with prescribed end collars and normal-germ comparison used in the Pontryagin–Thom correspondence. The free lecture notes linked above are further reading; each step used in the correspondence has its proof here or in the earlier chapters named below.

The earlier prerequisites are proved in this course's bundle, classifying-map, Thom/Euler, frame-obstruction, manifold-duality, characteristic-number and smooth-cobordism chapters. The present chapter proves the full correspondence (K.1). The [rational-homotopy companion](rational-homotopy-and-the-hurewicz-range.md) treats Serre finiteness and the rational stable Hurewicz estimate. The [rational-bordism conclusion](rational-oriented-bordism-and-projective-generators.md) develops finite-stage stabilization, the rational polynomial ring and the positive-multiple criterion. The full unoriented characteristic-number detection theorem is treated in [the unoriented detection companion](stiefel-whitney-numbers-and-unoriented-bordism.md).
