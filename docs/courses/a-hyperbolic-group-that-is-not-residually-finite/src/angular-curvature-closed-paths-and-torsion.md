# Angular curvature, closed paths and torsion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a reduced filling, the angles around each vertex add up to at least \(2\pi\) at interior vertices, because the link condition bounds the length of reduced closed link walks. An angular form of the Gauss–Bonnet formula shows that the angle deficits of a planar diagram add up to \(2\pi\). Together they show that a closed edge path whose turns are all at least \(\pi\) cannot bound a filling (Proposition 2.2). Shortest loops in free homotopy classes are local geodesics, whose turns are at least \(\pi\); so no nontrivial element has finite order (Proposition 3.1). These are parts 1 and 2 of the triangle complex criterion, Theorem 2.1 of [Triangle complexes and their links](triangle-complexes-and-their-links.md).

- Angle sums in planar diagrams (Lemma 1.1).
- Closed paths with large turns (Lemma 2.1, Proposition 2.2).
- Shortest loops and torsion (Proposition 3.1).

The lesson follows [OpenAI-RF, Sections 3.3 and 3.4]. It uses the reduced fillings of [Reduced planar fillings](reduced-planar-fillings.md) (Theorem 2.3 and Lemma 1.2 there) and the metric facts of Lemma 4.1 of the first lesson. Throughout, \(K\) is a connected finite Euclidean triangle complex satisfying the hypothesis of the criterion with \(\eta>0\), and \(S\) is its barycentric subdivision or a further compatible Euclidean simplicial subdivision.

## 1. Angle sums in planar diagrams

Let \(\Delta\) be a planar diagram whose triangles carry Euclidean metrics, for instance the metrics of their images under a diagram map to \(S\). For a vertex \(y\), let \(\theta_y\) be the sum of the angles of the triangles of \(\Delta\) at \(y\), and \(n_y\) the number of visits of the exterior walk to \(y\).

**Lemma 1.1** (angular Gauss–Bonnet). 
\[
\sum_y\bigl((2-n_y)\pi-\theta_y\bigr)=2\pi .
\]

*Proof.* The angles of each triangle add up to \(\pi\), so \(\sum_y\theta_y=\pi t\). By Lemma 1.2 of the previous lesson, \(\sum_yn_y=2e-3t\) and \(v-e+t=1\). Hence the sum is \(2\pi v-\pi(2e-3t)-\pi t\), which equals \(2\pi(v-e+t)=2\pi\). \(\blacksquare\)

The identity counts the exterior visits with multiplicity; it does not need a simple boundary.

## 2. Closed paths with large turns

A planar diagram with a diagram map to \(S\) is *reduced* if at every interior vertex the cyclic sequence of corners maps to a nonempty cyclically reduced closed walk in the link of the image vertex. The fillings of Theorem 2.3 of the previous lesson are reduced diagrams.

**Lemma 2.1** (angles at vertices). Let \(\Delta\) be a planar diagram whose triangles carry Euclidean metrics, and \(y\) a vertex of \(\Delta\).

1. If \(\Delta\) is a reduced diagram, with the metrics of the images of its triangles, and \(y\) is interior, then \(\theta_y\ge2\pi\), and \(\theta_y\ge2\pi+\eta\) if \(y\) maps to an original vertex of \(K\).
2. If \(n_y=1\), the corners at \(y\) form a link path, of length \(\theta_y\), between the directions of the two edges of the exterior walk at its visit to \(y\); if there is no corner, \(y\) has a single edge, along which the exterior walk arrives and leaves.

*Proof.* (1) At an interior vertex the corners map to a nonempty cyclically reduced closed walk in the link of the image vertex, of length \(\theta_y\). By Section 3 of the first lesson, such walks have length at least \(2\pi\) at the new vertices of a subdivision and at least \(2\pi+\eta\) at the original vertices.

(2) The exterior walk passes through one sector at \(y\) between two consecutive edges; the corners at \(y\) fill the remaining angle, in order, from one of these edges to the other. Without corners, every pair of consecutive edges at \(y\) bounds an exterior sector, so the number of edges at \(y\) is \(n_y=1\). \(\blacksquare\)

**Proposition 2.2** (closed paths; [OpenAI-RF, Proposition 3.3]). In \(K\), or in any compatible Euclidean simplicial subdivision of it, a nonempty closed edge path whose every turn, including the turn at its closing point, has link distance at least \(\pi\) is not nullhomotopic.

*Proof.* First let the path \(c\) lie in a simplicial subdivision \(S\), and suppose that it is nullhomotopic. Let \(\Delta\) be a reduced filling of \(c\) (Theorem 2.3 of the previous lesson); its exterior walk maps to \(c\), so the turns of \(c\) are the images of the pairs of exterior edges at the visits of the walk. In Lemma 1.1 we show that every summand is at most \(0\), which contradicts the value \(2\pi\).

- If \(n_y=0\), then \(\theta_y\ge2\pi\) by Lemma 2.1(1), and the summand \(2\pi-\theta_y\) is at most \(0\).
- If \(n_y=1\) and there are corners at \(y\), they form a link path of length \(\theta_y\) between the directions of the turn of \(c\) at this visit, whose link distance is at least \(\pi\). So \(\theta_y\ge\pi\) and the summand \(\pi-\theta_y\) is at most \(0\). Without corners, the walk arrives and leaves along the same edge, a turn of link distance \(0\), which the hypothesis excludes.
- If \(n_y\ge2\), the summand \((2-n_y)\pi-\theta_y\) is at most \(0\).

For a path in \(K\), pass to the barycentric subdivision, replacing each edge by its two halves. The turns at the original vertices keep their link distances, since the links there are only subdivided. At the barycenter of an edge, the path goes straight through, and the two directions along the edge have link distance \(\pi\) if the edge lies in a triangle (one path of length \(\pi\) for each incident triangle), and are in different link components otherwise. So the subdivided path satisfies the hypothesis in \(S\), and it is the same loop. \(\blacksquare\)

The proposition uses only the bound \(2\pi\) at interior vertices; the strict excess \(\eta\) is needed for hyperbolicity in the next lesson.

## 3. Shortest loops and torsion

**Proposition 3.1** ([OpenAI-RF, Proposition 3.4]). The group \(\pi_1(K)\) is torsion-free.

*Proof.* *A scale.* The truncated stars of Lemma 4.1 of the first lesson contract to their apex, so they are contractible in \(K\). Cover the compact space \(K\) by finitely many of them, let \(a>0\) be a Lebesgue number of this cover, and choose \(\epsilon<a/20\). Every ball of radius \(5\epsilon\) has diameter less than \(a\), so it lies in one star of the cover and every loop in it is nullhomotopic in \(K\). In particular every loop of length less than \(5\epsilon\), which stays in the ball of radius \(5\epsilon\) about its initial point, is nullhomotopic.

*Close loops are freely homotopic.* Let \(\sigma,\sigma'\) be loops on the parameter circle with \(d(\sigma(t),\sigma'(t))<\epsilon\) for all \(t\). Partition the circle at \(t_0,\dots,t_k=t_0\) so that on each interval \([t_{j-1},t_j]\) the loop \(\sigma\) stays within \(\epsilon\) of \(\sigma(t_{j-1})\). Join \(\sigma(t_j)\) to \(\sigma'(t_j)\) by a shortest path \(\kappa_j\), of length less than \(\epsilon\), with the same connector at the seam. On each interval, \(\sigma'\) stays within \(2\epsilon\) of \(\sigma(t_{j-1})\), so the loop formed by the two subarcs and the connectors \(\kappa_{j-1}\), \(\kappa_j\) lies in the ball of radius \(3\epsilon\) about \(\sigma(t_{j-1})\), and is nullhomotopic. Filling these loops and gluing along the connectors gives a free homotopy from \(\sigma\) to \(\sigma'\).

*A shortest loop.* Let \(g\ne1\) in \(\pi_1(K)\). Its free homotopy class, the set of loops freely homotopic to a representative, contains no constant loop, and it contains edge loops (Lemma 2.1 of the previous lesson), which are rectifiable. Let \(\ell\) be the infimum of the lengths of the rectifiable loops in the class; by the first step, \(\ell\ge5\epsilon\). Parametrize a minimizing sequence proportionally to arclength on the parameter circle. The speeds are bounded, so the diagonal argument of Lemma 4.1 of the first lesson gives a uniformly convergent subsequence, whose limit \(\sigma\) is, by the previous step, in the same class, and has length at most \(\ell\), hence \(\ell\).

*It is a local geodesic.* Parametrize \(\sigma\) by arclength. If a subarc of length less than \(\epsilon\) were not a shortest path, replace it by a shortest path between its endpoints. Both lie within \(\epsilon\) of the initial endpoint, so the loop they form lies in a ball of radius \(2\epsilon\) and is nullhomotopic; the replacement stays in the free homotopy class and is shorter, a contradiction. So \(\sigma\) is a closed local geodesic, also across its seam.

*It is an edge path with large turns.* By Lemma 4.1 of the first lesson, \(\sigma\) consists of finitely many straight pieces. Subdivide the barycentric subdivision compatibly so that \(\sigma\) runs in its edges: mark the endpoints of the pieces; in each triangle, draw the finitely many lines carrying pieces of \(\sigma\), mark their intersections and the ends of overlaps, so that the lines cut the triangle into convex polygons; impose on every edge the marks of all incident cells; and cone each convex polygon from an interior point to the marked points on its boundary. This gives a finite compatible Euclidean triangulation containing \(\sigma\) in its edges, with the links described in Section 3 of the first lesson. By Lemma 4.1 of the first lesson, every turn of \(\sigma\), as a closed edge path, has link distance at least \(\pi\).

*No torsion.* If \(g^m=1\) for some \(m\ge1\), the \(m\)-fold repetition of \(\sigma\) represents a conjugate of \(g^m\), so it is nullhomotopic. It is a nonempty closed edge path all of whose turns, including the repeated seams, have link distance at least \(\pi\), contrary to Proposition 2.2. \(\blacksquare\)

## 4. Exercises

**4.1.** Check Lemma 1.1 for a single triangle and for a single edge.

**4.2.** In the proof of Proposition 2.2, why is the case \(n_y\ge2\) harmless even when \(\theta_y=0\)?

**4.3.** Show that the hypothesis of Proposition 2.2 forces a closed edge path to have length at least \(2\) in a simplicial complex, and give a path of length \(4\) in a flat square tiling of a torus (with link cycles of length \(2\pi\)) whose turns are all \(\pi\). Is it nullhomotopic?

**4.4.** Why does the torsion argument need loops that are local geodesics, rather than arbitrary edge loops?

## 5. Solutions

**4.1.** A triangle: three vertices with \(n_y=1\) and angles adding up to \(\pi\), so the sum is \(3\pi-\pi=2\pi\). A single edge: two vertices with \(n_y=1\) and \(\theta_y=0\), so the sum is \(\pi+\pi=2\pi\).

**4.2.** The summand \((2-n_y)\pi-\theta_y\) is then at most \(0\) without any condition on the turns.

**4.3.** A closed edge path of length one would be a loop, which a simplicial complex does not have. On the torus tiled by squares, each cut into two triangles, a straight closed edge path around one direction has length equal to the number of squares around the torus, here \(4\), and turns \(\pi\) everywhere. It is not nullhomotopic, in agreement with Proposition 2.2, whose proof needs only the bound \(2\pi\) at interior vertices.

**4.4.** The turns of an arbitrary edge loop can be small, and then Proposition 2.2 says nothing. A shortest loop in a free homotopy class has turns of at least \(\pi\) by Lemma 4.1 of the first lesson, and its repetitions inherit this property.

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Sections 3.3 and 3.4. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
