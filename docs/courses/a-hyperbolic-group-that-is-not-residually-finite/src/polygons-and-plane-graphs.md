# Polygons and plane graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson fills a nullhomotopic closed path by a planar diagram, and the lessons after it count angles in such diagrams. Both need a few facts about polygons and graphs drawn in the plane with straight edges: a simple closed polygon bounds a disk that can be triangulated by diagonals (Theorem 2.4); an arc across a polygonal disk cuts it into two such disks (Lemma 2.2); a connected plane graph satisfies Euler's formula (Proposition 3.1); and each face of a connected plane graph inside a convex polygon is a disk, bounded by a closed walk of the graph and modelled by a convex polygon (Proposition 3.3). The separation of the plane by a simple closed polygon, with the index that distinguishes its two sides, is taken from the lesson [Polygonal regions and the directions on a circle](course:constant-coefficient-equations-and-solvability/AN02-L047).

- Simple polygons: diagonals, cross-cuts and triangulations (Section 2).
- Euler's formula (Proposition 3.1).
- Models of faces (Proposition 3.3).

These facts are classical; they are proved here in the generality needed by [OpenAI-RF, Section 3.2].

## 1. Polygons and their index

All paths in this lesson are *polygonal*: finite concatenations of straight segments. A *polygonal arc* is an injective polygonal path, and a *simple polygon* is the image \(\Pi\) of a closed polygonal path whose vertices are distinct, whose consecutive edges meet only at their common endpoint, and whose other edges are disjoint. For a closed polygonal path \(\gamma\) and a point \(a\) off it, the *index* is
\[
I_\gamma(a)=\frac1{2\pi i}\int_\gamma\frac{dz}{z-a},
\]
with the plane identified with \(\mathbb C\).

**Theorem 1.1** ([Polygonal regions and the directions on a circle](course:constant-coefficient-equations-and-solvability/AN02-L047), Lemma 2.1 and Theorem 3.1). For a simple polygon \(\Pi\), traversed by \(\gamma\), the complement \(\mathbb R^2\setminus\Pi\) has exactly two components, one bounded and one unbounded, both with boundary \(\Pi\). The index \(I_\gamma\) is an integer, locally constant off \(\Pi\), and jumps by \(1\) across every edge, from its right side to its left side.

Since \(I_\gamma(a)\to0\) as \(|a|\to\infty\), the index is \(0\) on the unbounded component, and hence \(\varepsilon=\pm1\) on the bounded one, by the jump across an edge. We call the bounded component the *inside* \(\operatorname{ins}(\Pi)\) and \(\varepsilon\) the *orientation* of \(\gamma\). The index is additive: if closed polygonal paths \(\gamma_1\) and \(\gamma_2\) traverse a common segment in opposite directions and \(\gamma\) is obtained by deleting it from their concatenation, then \(I_\gamma=I_{\gamma_1}+I_{\gamma_2}\) off the paths, because the integral over a segment and over its reverse cancel.

## 2. Simple polygons: diagonals, cross-cuts and triangulations

A *diagonal* of a simple polygon \(\Pi\) is a segment joining two of its vertices that are not adjacent, whose interior lies in \(\operatorname{ins}(\Pi)\).

**Lemma 2.1** (diagonals). Every simple polygon with at least four vertices has a diagonal.

*Proof.* Let \(v\) be a vertex with the smallest first coordinate, and among those the smallest second coordinate; let \(u\) and \(w\) be its neighbours. The angle of \(\Pi\) at \(v\) between the edges to \(u\) and \(w\) is less than \(\pi\): both edges point into the closed half-plane to the right of the vertical line through \(v\), and they cannot both point vertically upward, since they would then overlap. The open half-plane to the left of \(v\) misses \(\Pi\), is connected and unbounded, so it lies outside. Near \(v\), the two edges divide a small disk into two sectors, which lie on different sides of \(\Pi\) by the jump of the index; the sector of angle greater than \(\pi\) contains points to the left of \(v\), so the sector of angle less than \(\pi\) lies inside.

Let \(T\) be the closed triangle with vertices \(u\), \(v\), \(w\). An edge of \(\Pi\) other than \(vu\) and \(vw\) that meets the interior of \(T\) or the open segment \((u,w)\) has an endpoint in \(T\) other than \(u\), \(v\), \(w\): it cannot cross the edges \(vu\), \(vw\), and a segment cannot leave \(T\) through the side \(uw\) after entering through it.

If no vertex of \(\Pi\) other than \(u\), \(v\), \(w\) lies in \(T\), then the interior of \(T\) and the open segment \((u,w)\) miss \(\Pi\). The interior of \(T\) is connected and contains points of the small inner sector at \(v\), so it lies inside; so does \((u,w)\), which lies in its closure and off \(\Pi\). Since \(\Pi\) has at least four vertices, \(u\) and \(w\) are not adjacent, and \(uw\) is a diagonal.

Otherwise, among the vertices of \(\Pi\) in \(T\) other than \(u\), \(v\), \(w\), choose \(z\) at the largest distance from the line through \(u\) and \(w\). Let \(\lambda\) be the line through \(z\) parallel to \(uw\), and \(T_z\) the closed part of \(T\) on the side of \(\lambda\) that contains \(v\). By the choice of \(z\), no vertex of \(\Pi\) other than \(v\) lies in \(T_z\setminus\lambda\). The open segment \((v,z)\) lies in \(T_z\setminus\lambda\). An edge of \(\Pi\) meeting it cannot cross \(vu\) or \(vw\); so either it has an endpoint in \(T_z\setminus\lambda\) other than \(v\), which is impossible, or both its endpoints lie on \(\lambda\) or beyond it, and then it misses \(T_z\setminus\lambda\). Hence \((v,z)\) misses \(\Pi\), and near \(v\) it lies in the inner sector, so \((v,z)\subset\operatorname{ins}(\Pi)\). As \(z\notin\{u,w\}\), the vertex \(z\) is not adjacent to \(v\), and \(vz\) is a diagonal. \(\blacksquare\)

A *cross-cut* of a simple polygon \(\Pi\) is a polygonal arc \(\alpha\) that meets \(\Pi\) exactly in its two endpoints \(p\ne p'\) and has its interior in \(\operatorname{ins}(\Pi)\). The two arcs of \(\Pi\) between \(p\) and \(p'\) form, with \(\alpha\), two simple polygons \(\Pi_1\) and \(\Pi_2\).

**Lemma 2.2** (cross-cuts). In this situation \(\operatorname{ins}(\Pi)\setminus\alpha\) is the disjoint union of \(\operatorname{ins}(\Pi_1)\) and \(\operatorname{ins}(\Pi_2)\), and these are its two components.

*Proof.* Traverse \(\Pi\) by \(\gamma\), and let \(\gamma_1\) and \(\gamma_2\) traverse \(\Pi_1\) and \(\Pi_2\), each following its arc of \(\Pi\) in the direction of \(\gamma\), so that they traverse \(\alpha\) in opposite directions. By additivity, \(I_\gamma=I_{\gamma_1}+I_{\gamma_2}\) off \(\Pi\cup\alpha\). Let \(\varepsilon\), \(\varepsilon_1\), \(\varepsilon_2\) be the orientations. Across \(\alpha\), at points near an interior point of \(\alpha\), which are inside \(\Pi\), the index of \(\gamma\) does not jump, while \(I_{\gamma_1}\) and \(I_{\gamma_2}\) jump by \(1\) in opposite directions. So on one side of \(\alpha\) the pair \((I_{\gamma_1},I_{\gamma_2})\) is \((\varepsilon,0)\) and on the other \((0,\varepsilon)\); this forces \(\varepsilon_1=\varepsilon_2=\varepsilon\).

Now let \(a\notin\Pi\cup\alpha\). If \(a\) is inside \(\Pi\), then \(I_{\gamma_1}(a)+I_{\gamma_2}(a)=\varepsilon\) with both terms in \(\{0,\varepsilon\}\), so \(a\) is inside exactly one of \(\Pi_1\), \(\Pi_2\). If \(a\) is outside \(\Pi\), the sum is \(0\), so both terms are \(0\), and \(a\) is inside neither. The inside of \(\Pi_k\) also contains no point \(q\) of \(\Pi\): it misses \(\Pi_k\), and if it contained a point \(q\) of the other arc, it would contain a neighbourhood of \(q\), hence points outside \(\Pi\), which are inside neither. So \(\operatorname{ins}(\Pi)\setminus\alpha\) is the disjoint union of \(\operatorname{ins}(\Pi_1)\) and \(\operatorname{ins}(\Pi_2)\), which are open and connected by Theorem 1.1, hence its two components. \(\blacksquare\)

A *triangulation* of a simple polygon \(\Pi\) is a finite set of closed triangles whose vertices are vertices of \(\Pi\), whose union is the closure \(\overline{\operatorname{ins}}(\Pi)\), and any two of which meet in a common side, a common vertex, or not at all. A triangle of a triangulation with at least two triangles is an *ear* if two of its sides are edges of \(\Pi\).

**Lemma 2.3** (gluing). Let \(P_1\) and \(P_2\) be closed convex polygons meeting in a common side \(s\), with \(P_1\cup P_2\) having a simple polygon as boundary. Then there is a homeomorphism from \(P_1\cup P_2\) onto a convex polygon, linear on each triangle of a triangulation of \(P_1\cup P_2\), that maps vertices to vertices in their cyclic order.

*Proof.* Let \(c\) be the midpoint of \(s\). Coning from \(c\) triangulates \(P_1\) and \(P_2\) by triangles with apex \(c\) and opposite sides the boundary edges of \(P_1\cup P_2\); each ray from \(c\) into \(P_1\cup P_2\) meets the boundary once. If the boundary has \(n\) vertices, choose a regular \(n\)-gon \(Q\) with center \(c'\), and map the cone triangles at \(c\) linearly onto the cone triangles at \(c'\), vertex to vertex in the same cyclic order. The pieces agree on common sides, and the map is a bijection of the cone structures, hence a homeomorphism. \(\blacksquare\)

**Theorem 2.4** (triangulated disks). Every simple polygon \(\Pi\) has a triangulation. For every triangulation, with \(v\), \(e\), \(t\) the numbers of vertices, edges and triangles,
\[
v-e+t=1 ;
\]
a triangulation with at least two triangles has an ear; and there is a homeomorphism from \(\overline{\operatorname{ins}}(\Pi)\) onto a convex polygon that maps \(\Pi\) onto its boundary, vertices to vertices in order, and is linear on each triangle of a triangulation.

*Proof.* *Existence*, by induction on the number \(n\) of vertices. For \(n=3\), \(\Pi\) is a triangle, and its inside is the open triangle. For \(n\ge4\), Lemma 2.1 gives a diagonal, a cross-cut joining two vertices; by Lemma 2.2 the closure of the inside is the union of the closures of the insides of two simple polygons with fewer vertices, meeting along the diagonal. Their triangulations together triangulate \(\Pi\).

*Euler characteristic*, by induction on \(t\). A single triangle has \(3-3+1=1\). If \(t\ge2\), some interior edge of the triangulation is a diagonal, a cross-cut; by Lemma 2.2 it splits the triangulation into triangulations of two smaller polygons, with \(v_1+v_2=v+2\), \(e_1+e_2=e+1\) and \(t_1+t_2=t\), so \(v-e+t=(1+1)-2+1=1\).

*Ears.* Join two triangles of the triangulation when they share a side. This graph is connected, since a path in \(\operatorname{ins}(\Pi)\) avoiding the vertices passes from triangle to triangle through common sides. Every shared side is a diagonal, hence a cross-cut, and by Lemma 2.2 the triangles on its two sides lie in different pieces; so removing any edge disconnects the graph, and the graph is a tree. A leaf of the tree is a triangle with one interior side, hence two sides on \(\Pi\): an ear.

*Homeomorphism*, by induction on \(t\). For \(t=1\) use the identity. For \(t\ge2\), remove an ear \(E\), with apex \(x\) and interior side \(s\); the remaining triangles triangulate a polygon \(\Pi'\) with one vertex fewer, and by induction there is a piecewise linear homeomorphism \(h'\) onto a regular polygon. Attach to the image a triangle \(E'\) along \(h'(s)\), small enough that the union is star-shaped with respect to the center, map \(E\) linearly onto \(E'\), and apply the coning argument of Lemma 2.3 with the center as apex to map the union onto a regular polygon with one more vertex. \(\blacksquare\)

In particular, \(\overline{\operatorname{ins}}(\Pi)\) is contractible, and every closed path in it is nullhomotopic in it.

## 3. Plane graphs and their faces

A *plane graph* is a finite graph whose vertices are points of the plane and whose edges are polygonal arcs between them, any two of which meet only in common endpoints. Its *faces* are the components of the complement of the union of its edges and vertices.

**Proposition 3.1** (Euler's formula). A connected plane graph with \(V\) vertices, \(E\) edges and \(F\) faces satisfies \(V-E+F=2\).

*Proof.* Subdividing an edge at a bend adds one vertex and one edge, so we may assume that all edges are straight. Choose a spanning tree and add the remaining edges one by one. For a tree, \(E=V-1\) and \(F=1\). Indeed, the complement of a tree is connected, by induction over its edges: let \(T'=T\cup e\), where \(e\) joins a vertex \(x\) of \(T\) to a new vertex \(y\), and \(\mathbb R^2\setminus T\) is connected. A component of \(\mathbb R^2\setminus T'\) whose closure missed the open segment \(e\setminus\{x\}\) would be open and closed in \(\mathbb R^2\setminus T\), hence equal to it, which is impossible because \(\mathbb R^2\setminus T\) contains \(e\setminus\{x\}\). So every component contains points close to \(e\), on one of its two sides; moving parallel to \(e\) away from \(x\), such points are joined to points close to \(y\), and around \(y\) the two sides are joined. Now add an edge \(e\) whose endpoints already lie in the graph. Its interior lies in one face \(\Phi\). With a path of the graph between its endpoints, \(e\) forms a simple polygon \(\Pi\); points on the two sides of \(e\) near an interior point are on different sides of \(\Pi\) by Theorem 1.1, so they lie in different components of \(\Phi\setminus e\). Every point of \(\Phi\setminus e\) is joined inside \(\Phi\) to points near \(e\), and a path in \(\Phi\) that meets \(e\) can be stopped at its first approach to \(e\); the points near \(e\) on one side form a connected set. So \(\Phi\setminus e\) has exactly two components, and the other faces do not change: adding \(e\) increases \(E\) and \(F\) by one each. \(\blacksquare\)

From now on \(D\) is a closed convex polygon, and \(\Gamma\) is a connected plane graph contained in \(D\) that contains the boundary \(\partial D\) as a union of edges. Its *inner faces* are the faces inside \(D\).

**Definition 3.2** (face models). A *model* of an inner face \(\Phi\) is a convex polygon \(C\) with a continuous map \(\kappa\colon C\to\overline\Phi\) such that

1. \(\kappa\) maps the interior of \(C\) homeomorphically onto \(\Phi\), and is linear on the triangles of some triangulation of \(C\);
2. \(\kappa\) maps every side of \(C\) homeomorphically onto an edge of \(\Gamma\), so that the sides, in cyclic order, map to a closed walk in \(\Gamma\), the *boundary walk* of \(\Phi\);
3. every point \(p\) of \(\partial C\) has a neighbourhood \(U\) in \(C\) such that \(\kappa\) is injective on \(U\), and \(\kappa(U)\) is a neighbourhood of \(\kappa(p)\) in \(\Phi\cup\{\kappa(p)\}\) cut out by the edges of \(\Gamma\) at \(\kappa(p)\), within one of the sectors of \(\Phi\) at \(\kappa(p)\).

Condition 3 says that the boundary walk passes through the *sectors* of \(\Phi\) at its vertices one at a time: the occurrences of a vertex \(x\) in the walk correspond bijectively to the sectors of \(\Phi\) between consecutive edges at \(x\), and an edge of \(\Gamma\) appears in the walk once for each of its sides that faces \(\Phi\).

**Proposition 3.3** (models of faces). Every inner face of \(\Gamma\) has a model.

*Proof.* Subdivide the edges of \(\Gamma\) at their bends, so that all edges are straight; a model for the subdivided graph gives one for \(\Gamma\) by merging consecutive sides. Since \(\Gamma\) is connected, its edges outside \(\partial D\) can be added to \(\partial D\) one at a time so that every intermediate graph is connected: each new edge has an endpoint in the current graph. We prove the claim for every intermediate graph by induction. For \(\partial D\) alone, the only inner face is the interior of \(D\), and \(C=D\) with \(\kappa\) the identity is a model.

Let \(e\) be the next edge, with an endpoint \(x\) in the current graph; its interior lies in one inner face \(\Phi\) with a model \((C,\kappa)\), and near \(x\) it lies in one sector of \(\Phi\) at \(x\). By condition 3 this sector corresponds to one point \(\tilde x\in\partial C\), and \(\tilde e=\kappa^{-1}(e\cap\Phi)\), closed up at \(\tilde x\), is a polygonal arc in \(C\) from \(\tilde x\), meeting \(\partial C\) only at \(\tilde x\) unless the other end of \(e\) is also in the current graph. The other inner faces keep their models.

*A chord.* If the other endpoint \(y\) of \(e\) is in the current graph, \(\tilde e\) ends at the point \(\tilde y\in\partial C\) of the sector of \(\Phi\) at \(y\) containing the end of \(e\); then \(\tilde e\) is a cross-cut of \(\partial C\) (\(\tilde y\ne\tilde x\), since \(\kappa\) is injective near each boundary point and \(e\) is an arc). By Lemma 2.2, it cuts \(C\) into the closures of the insides of two simple polygons, whose interiors \(\kappa\) maps onto the two components of \(\Phi\setminus e\), the new faces. Theorem 2.4 maps each closure piecewise linearly onto a convex polygon, vertices in order, and composing \(\kappa\) with the inverse gives models: conditions 1 and 2 are inherited, and condition 3 holds at the new boundary points on \(\tilde e\) because \(e\) has two sides, one facing each new face.

*A pendant edge.* If the other endpoint \(y\) is new, \(\tilde e\) ends at an interior point \(\tilde y\) of \(C\), and the new face is \(\Phi\setminus e\). Continue \(\tilde e\) beyond \(\tilde y\) by a polygonal arc \(\tilde e'\) to a point of \(\partial C\), missing \(\tilde e\) otherwise: for instance, follow \(\tilde e\) backwards at a small distance on one side and then run to \(\partial C\) next to \(\tilde x\). Then \(\tilde e\cup\tilde e'\) is a cross-cut, and by Lemma 2.2 and Theorem 2.4, \(C\) is the union of two convex-modelled pieces \(C_1\), \(C_2\) meeting along it. The interior of \(C\) minus \(\tilde e\) is the union of the interiors of \(C_1\) and \(C_2\) and the open arc \(\tilde e'\). By Theorem 2.4, followed by coning from the center to merge the consecutive sides that correspond to \(\tilde e'\) into one side, map \(C_1\) and \(C_2\) piecewise linearly onto two convex polygons \(P_1\), \(P_2\) in which \(\tilde e'\) corresponds to one common side \(s\), with \(P_1\) and \(P_2\) on opposite sides of \(s\), and the two maps agreeing along \(\tilde e'\). By Lemma 2.3, \(P_1\cup P_2\) is piecewise linearly homeomorphic to a convex polygon \(C'\). Composing, \(\kappa\) induces a map \(C'\to\overline{\Phi\setminus e}\) which is a homeomorphism on the interior of \(C'\) onto \(\Phi\setminus e\), and whose boundary runs along \(\partial C\) and twice along \(\tilde e\), once on each side. Conditions 1–3 follow, with the new sector at \(y\) of angle \(2\pi\) corresponding to the one occurrence of \(y\) in the new boundary walk. \(\blacksquare\)

In particular, every inner face is homeomorphic to an open disk, its boundary walk passes along every edge side facing it, and a closed curve in the face close to its frontier follows the whole boundary walk.

## 4. Exercises

**4.1.** Show that a triangulation of a simple polygon with \(n\) vertices has \(n-2\) triangles and \(n-3\) diagonals.

**4.2.** Give a simple polygon in which the segment between two non-adjacent vertices lies outside, and check Lemma 2.1 on it.

**4.3.** Find the boundary walk of the unique inner face when \(\Gamma\) consists of \(\partial D\) and a path of two edges from a vertex of \(\partial D\) into the interior of \(D\). How often does each edge occur?

**4.4.** Verify Euler's formula for \(\partial D\) together with one diagonal of \(D\).

## 5. Solutions

**4.1.** By Theorem 2.4, \(n-e+t=1\), and counting sides, \(3t=2(e-n)+n\). So \(e=2n-3\), \(t=n-2\), and the number of diagonals, the interior edges, is \(e-n=n-3\).

**4.2.** In the polygon with vertices \((0,0)\), \((4,0)\), \((4,4)\), \((2,1)\), \((0,4)\) the segment from \((4,4)\) to \((0,4)\) lies above the reflex vertex \((2,1)\), outside the polygon. The leftmost lowest vertex is \(v=(0,0)\), with neighbours \((4,0)\) and \((0,4)\); the triangle they span contains \((2,1)\), which is the vertex chosen in the proof, and the segment from \((0,0)\) to \((2,1)\) is a diagonal.

**4.3.** The walk runs once around \(\partial D\), and at the vertex where the path starts it runs along the two edges of the path to the free end and back. Each edge of \(\partial D\) occurs once, each edge of the path twice, once for each side.

**4.4.** \(V=n\), \(E=n+1\), and there are three faces: the two inner faces and the outside. \(n-(n+1)+3=2\).

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Section 3.2. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
