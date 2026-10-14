# Triangle complexes and their links

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A group is *residually finite* if every nonidentity element survives in some finite quotient. Finitely generated linear groups have this property, and so do many groups of geometric origin; whether every word-hyperbolic group is residually finite was a central question in Gromov's theory of hyperbolic groups. This course proves the theorem of [OpenAI-RF]: there is a torsion-free word-hyperbolic group that is not residually finite. The group is the fundamental group of a finite complex of Euclidean triangles with three vertices, and one of finitely many explicit elements dies in every finite quotient. As a consequence, this element is killed by every finite-dimensional linear representation over every field.

The course has two parts. Lessons 1 to 5 prove a criterion: if every closed walk in every vertex link of a finite Euclidean triangle complex has angular length at least \(2\pi+\eta\), then its fundamental group is torsion-free and word-hyperbolic, and closed edge paths with large turns are nontrivial. Lessons 6 and 7 construct the complex from punctured lines over a finite field and prove, by comparing ranks of matrices over the reals and over a fixed prime field, that no finite quotient keeps certain nontrivial elements alive.

This lesson states the theorem and the criterion and proves the metric facts used throughout.

- Hyperbolic groups and residual finiteness; the theorem (Theorem 1.1).
- Triangle complexes, links and turns; the criterion (Theorem 2.1).
- Subdivisions (Section 3).
- The intrinsic metric (Lemma 4.1).

The lesson follows [OpenAI-RF, Sections 1, 2.1 and 3.1].

## 1. Hyperbolic groups and residual finiteness

Let \(G\) be a group with a finite generating set \(S\) that is symmetric (\(S=S^{-1}\)) and does not contain \(1\). The *Cayley graph* \(\operatorname{Cay}(G,S)\) has the elements of \(G\) as vertices and an edge of length \(1\) between \(g\) and \(gs\) for \(s\in S\); with the path metric it is a geodesic metric space, and its distance between vertices is the *word distance* \(d_S\). A *geodesic triangle* in a geodesic metric space consists of three points and three shortest paths between them, its *sides*. It is *\(\delta\)-thin* if every point of each side is within distance \(\delta\) of the union of the other two sides. The group \(G\) is *word-hyperbolic* if for some finite symmetric generating set there is \(\delta\ge0\) such that all geodesic triangles of the Cayley graph are \(\delta\)-thin.

A group \(G\) is *residually finite* if every \(g\ne1\) has a nonidentity image under some homomorphism from \(G\) to a finite group. The *finite residual* \(R_f(G)\) is the intersection of the kernels of all homomorphisms from \(G\) to finite groups; \(G\) is residually finite if and only if \(R_f(G)=1\).

**Theorem 1.1** ([OpenAI-RF, Theorem 1.1]). There is a torsion-free word-hyperbolic group that is not residually finite.

**Corollary 1.2** ([OpenAI-RF, Corollary 1.2]). The group of Theorem 1.1 can be chosen finitely generated with a nonidentity element that lies in the kernel of every homomorphism to \(\mathrm{GL}_n(F)\), for every field \(F\) and every \(n\ge1\). In particular it is not linear over any field.

Both are proved in [The rank obstruction](the-rank-obstruction.md) (Theorem 4.1 and Corollary 4.3 there).

## 2. Triangle complexes, links and turns

A *finite Euclidean triangle complex* is a finite graph with finitely many Euclidean triangles attached along their full boundaries, side to edge, with positive edge lengths and isometric gluings. Each closed edge and each closed triangle is required to embed, and different cells may meet in a union of faces. Several edges may join the same two vertices, and several triangles may have the same three vertices.

The *link* of a vertex \(x\) is the graph with one vertex for each edge germ at \(x\) (an *edge direction* at \(x\)) and one edge for each corner of a triangle at \(x\), joining the two directions of its sides at \(x\). The link is a metric graph: the length of a link edge is the angle of its corner. A walk in a graph is *reduced* if it never traverses an edge and immediately the same edge back, and a closed walk is *cyclically reduced* if this also holds across its closing point. The *link distance* between two directions at \(x\) is the length of a shortest link path between them, and infinite if they lie in different components of the link.

An *edge path* is a finite sequence of oriented edges, each starting where the previous one ends. At an interior vertex \(x\) of an edge path, and for a closed edge path also at its closing point, the *turn* compares two directions at \(x\): the direction back along the arriving edge and the direction of the departing edge. Its size is their link distance.

**Theorem 2.1** (triangle complex criterion; [OpenAI-RF, Theorem 2.1]). Let \(K\) be a connected finite Euclidean triangle complex, and suppose that there is \(\eta>0\) such that every nonempty cyclically reduced closed walk in each vertex link has angular length at least \(2\pi+\eta\). Then:

1. a nonempty closed edge path in \(K\) whose every turn, including the turn at its closing point, has link distance at least \(\pi\) is not nullhomotopic;
2. \(\pi_1(K)\) is torsion-free;
3. \(\pi_1(K)\) is word-hyperbolic.

Part 1 is Proposition 2.2 of [Angular curvature, closed paths and torsion](angular-curvature-closed-paths-and-torsion.md), part 2 is Proposition 3.1 there, and part 3 is Proposition 3.2 of [Thin diagrams and hyperbolicity](thin-diagrams-and-hyperbolicity.md). The condition is a strict form of the link condition for nonpositive curvature of piecewise Euclidean complexes; the course proves the precise statements needed, with the turns measured in the Euclidean metric of \(K\) [OpenAI-RF, Section 2.1].

## 3. Subdivisions

Barycentrically subdivide \(K\): the new vertices are the barycenters of the original edges and triangles, together with the original vertices, and the new simplices correspond to strict inclusion chains of original cells. This is a genuine simplicial complex: parallel original edges have different barycenters, and triangles meeting in several faces cause no identifications within a simplex. Realize the subdivision by straight segments in each Euclidean triangle; it is again a finite Euclidean triangle complex, with the same underlying metric space.

The links of the subdivision are as follows.

1. At an original vertex the link is the original link with each edge subdivided into pieces of the same total length. A cyclically reduced closed walk in the subdivided link cannot turn back at a subdivision point, so it is a cyclically reduced closed walk of the original link, of the same length.
2. At the barycenter of an original triangle the link is a circle of length \(2\pi\).
3. At the barycenter of an original edge, the two directions along the edge are joined by one path of length \(\pi\) for each incident triangle, and are isolated if there is none.

So every nonempty cyclically reduced closed walk in the link of a new vertex has length at least \(2\pi\): on a circle such a walk goes around at least once, and in the third case it uses two different paths of length \(\pi\). In the link of an original vertex the bound \(2\pi+\eta\) of Theorem 2.1 persists. The same holds for every further *compatible Euclidean subdivision*, that is, a subdivision of the cells into Euclidean triangles by straight segments that agree on common edges: at points inside an original triangle or edge the links are as in 2 and 3, and at original vertices the links are subdivided.

## 4. The intrinsic metric

The *intrinsic distance* on a connected finite Euclidean triangle complex is the infimum of the lengths of finite paths made of straight segments in its cells. The same definition is used below for planar complexes that may have edges belonging to no triangle and pieces meeting only at a vertex. The *length* of a continuous path \(\sigma\colon[u,v]\to X\) is the supremum, over partitions \(u=t_0<\dots<t_k=v\), of \(\sum_jd(\sigma(t_{j-1}),\sigma(t_j))\); it is at least the distance of the endpoints, by the triangle inequality. A *shortest path* has length equal to the distance of its endpoints, and a *local geodesic* is a path of constant speed whose restriction to some neighborhood of each parameter value is a shortest path.

**Lemma 4.1** (metric preliminaries; [OpenAI-RF, Lemma 3.1]). The intrinsic distance \(d\) is a metric inducing the topology of the complex, and the complex is compact. Any two points are joined by a shortest path. Every local geodesic on a compact parameter interval, or a parameter circle, consists of finitely many straight pieces in cells. If such a path lies in the edges of a Euclidean subdivision, then the link distance at each of its turns is at least \(\pi\).

*Proof.* *Stars.* At a point \(x\), cut the cells containing \(x\) into sectors with apex \(x\), and choose \(\rho>0\) smaller than the Euclidean distance from \(x\) to every face of these cells that does not contain \(x\). The *truncated star* of \(x\) is the union of the parts of these sectors, and of edges with no triangle, within Euclidean distance \(\rho\) of \(x\). On it the Euclidean distance \(r\) to \(x\) in each cell is well defined, agrees across the gluings, and changes along a straight segment in a cell by at most the segment's length. Hence a path from \(x\) that leaves the truncated star has length at least \(\rho\), and a polygonal path from \(x\) to a point \(y\) of the star has length at least \(r(y)\). The radial segment from \(x\) to \(y\) has length \(r(y)\), so \(d(x,y)=r(y)\) for every \(y\) in the truncated star.

*Metric and topology.* In particular \(d(x,y)>0\) for \(y\ne x\), so \(d\) is a metric; symmetry and the triangle inequality hold for infima of path lengths. The metric balls of radius less than \(\rho\) about \(x\) are the truncated stars of that radius, which form a neighborhood basis of \(x\) in the complex topology; so \(d\) induces this topology. The complex is a finite union of compact cells, hence compact. Truncated stars contract to their apex along radial segments.

*Shortest paths.* Take polygonal paths \(\sigma_k\) from \(x\) to \(y\) whose lengths \(\ell_k\) decrease to \(d(x,y)\), parametrized proportionally to arclength on \([0,1]\). They are \(\ell_1\)-Lipschitz. Choose a countable dense set of parameters; by compactness and a diagonal choice, a subsequence converges at each of them, and the common Lipschitz bound makes it converge uniformly on \([0,1]\) to a path \(\sigma\). For every fixed partition, the sum \(\sum_jd(\sigma(t_{j-1}),\sigma(t_j))\) is the limit of the corresponding sums for \(\sigma_k\), which are at most \(\ell_k\). So the length of \(\sigma\) is at most \(d(x,y)\), and \(\sigma\) is a shortest path.

*Short minimizing arcs.* Let \(\sigma\) be a unit-speed shortest path starting at \(x\), short enough to stay in the truncated star. By the radial formula, \(r(\sigma(t))=d(x,\sigma(t))=t\). For \(t>0\), the direction of \(\sigma(t)\) seen from \(x\), a point of the link of \(x\) viewed as a metric graph, varies continuously. If it were not constant, it would move through an interval inside one link edge, since a continuous path in the finite set of link vertices and isolated directions is constant. Choose a subarc inside the corresponding open sector whose endpoint directions differ. The sector is a piece of the Euclidean plane, so the length of this subarc is at least the Euclidean distance of its endpoints, which is strictly larger than the difference of their radii. This contradicts \(r(\sigma(t))=t\) and unit speed. So \(\sigma\) is a radial segment in one sector or one edge.

*Local geodesics.* At each parameter value of a local geodesic, apply this on both sides: near the value the path consists of at most two straight pieces. A finite subcover of the compact parameter interval, or circle, gives finitely many straight pieces, including at the seam of a closed path.

*Turns.* Suppose a local geodesic turns at \(x\) with link distance less than \(\pi\) between the direction back along the arriving piece and the direction of the departing piece. A link path of length less than \(\pi\) between them traverses consecutive sectors at \(x\), which unfold isometrically into a planar sector of angle less than \(\pi\). Take two points at equal small distance from \(x\) on the arriving and departing pieces. In the unfolded sector, the straight chord between them is shorter than the sum of their distances to the apex, because the angle is less than \(\pi\). The chord maps back to a path in the complex, possibly through the same cells more than once, that is shorter than the part of the local geodesic between the two points. This contradicts local minimality. \(\blacksquare\)

## 5. Exercises

**5.1.** Show that \(\mathbb Z\) is residually finite and that \(R_f(G)\) is a normal subgroup of \(G\).

**5.2.** Describe the link of the vertex of a cone made of six equilateral triangles around a common vertex, and of five. Which of them satisfies the strict bound of Theorem 2.1?

**5.3.** Show that a single Euclidean triangle satisfies the hypothesis of Theorem 2.1, and use it to show that part 1 of the theorem fails without the bound \(\pi\) on the turns.

**5.4.** In the third case of Section 3, show that the link distance between the two directions along an original edge is \(\pi\) when the edge lies in a triangle.

**5.5.** Show that the length of a polygonal path, as defined by partitions, equals the sum of the lengths of its straight pieces.

## 6. Solutions

**5.1.** For \(n\ne0\), the quotient map to \(\mathbb Z/(2|n|)\) does not kill \(n\). The kernel of a homomorphism is normal, and intersections of normal subgroups are normal.

**5.2.** The link is a cycle of six, respectively five, edges of length \(\pi/3\): total length \(2\pi\), respectively \(5\pi/3\). Neither satisfies the strict bound; the first is flat, the second has positive curvature at the cone point.

**5.3.** Each vertex link is a single edge between two directions, so there is no nonempty cyclically reduced closed walk, and the hypothesis holds for every \(\eta\). The boundary path of the triangle is nullhomotopic, and its turns have the angles of the triangle as link distances, all less than \(\pi\).

**5.4.** The two directions are joined, for each incident triangle, by a path of length \(\pi\) in the link of the barycenter: the two corners of the two small triangles on one side, of angles adding to \(\pi\). Every path between them uses one of these, so the distance is \(\pi\).

**5.5.** Two points of one straight piece have distance at most their Euclidean distance, since the segment between them is a path. If the second point lies in the truncated star of the first, the radial formula gives equality. The open truncated stars of half their radii cover the compact piece; for a partition finer than a Lebesgue number of this cover, consecutive points satisfy the equality, so its sum is the Euclidean length of the piece. Refining partitions only increases the sums, and the sums are at most the Euclidean length, so the length of the piece is its Euclidean length; lengths add over consecutive pieces.

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Sections 1, 2.1 and 3.1. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
