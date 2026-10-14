# Reduced planar fillings

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A closed edge path that is nullhomotopic in a triangle complex bounds a map of a disk. For counting angles one needs more: a planar complex of triangles, mapped cell by cell to the complex, whose boundary walk is the given path and which has no cancelling pair of adjacent triangles. This lesson constructs such *reduced fillings* (Theorem 2.3). The construction approximates a filling disk simplicially, records where the largest barycentric coordinate changes as a labelled planar *picture*, removes cancelling pairs from the picture, and takes the planar dual.

- Planar diagrams and their exterior walks (Definition 1.1, Lemma 1.2).
- Edge approximation of maps and loops (Lemma 2.1).
- Pictures and their minimality (Lemma 2.2).
- Reduced fillings (Theorem 2.3).

The lesson follows [OpenAI-RF, Section 3.2]. It uses the facts on polygons and plane graphs of [Polygons and plane graphs](polygons-and-plane-graphs.md): Euler's formula (Proposition 3.1), the triangulations of polygons (Theorem 2.4) and the models of faces (Proposition 3.3). Throughout, \(S\) is the barycentric subdivision of a finite Euclidean triangle complex \(K\), or a further compatible Euclidean simplicial subdivision ([Triangle complexes and their links](triangle-complexes-and-their-links.md), Section 3); it is a simplicial complex of dimension at most \(2\).

## 1. Planar diagrams

**Definition 1.1.** A *planar diagram* \(\Delta\) is a connected plane graph, with polygonal edges and without loops, together with triangles filling all its bounded faces: every bounded face is bounded by a cycle of three edges and is *filled*. Its points are the points of its edges, vertices and filled faces. The *exterior walk* of \(\Delta\) is the boundary walk of its unbounded face: enclose \(\Delta\) in a large convex polygon \(D'\), join a vertex of \(\partial D'\) to a vertex of \(\Delta\) by one straight edge, and take the boundary walk of the face between \(\partial D'\) and \(\Delta\) given by Proposition 3.3 of the previous lesson, omitting \(\partial D'\) and the joining edge. For a vertex \(y\), \(n_y\) is the number of visits of the exterior walk to \(y\); \(y\) is *interior* if \(n_y=0\).

A *diagram map* \(\Delta\to S\) sends vertices to vertices, edges to edges and triangles to triangles, compatibly; each edge and triangle of \(\Delta\) is then given the Euclidean metric of its image, and \(\Delta\) becomes a planar complex with an intrinsic metric as in Section 4 of the first lesson. The embedding in the plane fixes the cyclic order of the edges and corners at each vertex, but its metric plays no role.

**Lemma 1.2.** Let \(\Delta\) be a planar diagram with \(v\) vertices, \(e\) edges and \(t\) triangles. Then
\[
v-e+t=1,\qquad\sum_yn_y=2e-3t .
\]
Every closed edge walk in \(\Delta\) is nullhomotopic in \(\Delta\), and the exterior walk passes once along every side of an edge that faces no triangle.

*Proof.* The graph has \(t+1\) faces, so Euler's formula gives \(v-e+t=1\). Each edge has two sides; \(3t\) of these sides face triangles, and the others face the unbounded face, whose boundary walk passes once along each of them (Proposition 3.3 of the previous lesson, condition 2). So the exterior walk has length \(2e-3t\), which is the number of its visits to vertices. A simple cycle of edges is a simple polygon whose inside misses the unbounded face, which is connected, unbounded and disjoint from the cycle; so the inside consists of points of \(\Delta\), and the cycle is nullhomotopic in the closure of the inside, which is contractible (Theorem 2.4 of the previous lesson). A closed edge walk that repeats a vertex splits there into two shorter closed walks, and a walk of length two goes along an edge and back; by induction every closed edge walk is a product of conjugates of such loops, and is nullhomotopic. \(\blacksquare\)

## 2. Pictures and reduced fillings

For a vertex \(s\) of \(S\), let \(\varphi_s\colon S\to[0,1]\) be its barycentric coordinate, extended by \(0\) outside the closed star of \(s\); it is continuous, and \(\sum_s\varphi_s=1\). At every point at most three coordinates are positive, so the largest is at least \(\frac13\).

**Lemma 2.1** (edge approximation). Let \(D\) be a convex polygon and \(F\colon D\to S\) continuous. Suppose that \(D\) is subdivided by marked points on its boundary, and that \(F\) maps each arc between consecutive marks, with constant speed, along an edge of \(S\), or to a vertex. Then there is a triangulation of \(D\), including the marks among its vertices, and a simplicial map \(f\) from it to \(S\), such that \(f(x)\) and \(F(x)\) lie in a common simplex for every \(x\in D\), and such that along each marked arc mapped along an edge \([s,s']\) the boundary edges of the triangulation are mapped to \(s\) up to some point and to \(s'\) after it. In particular \(f\) and \(F\) are homotopic relative to the marks. The same holds for a parameter interval or circle in place of \(D\): every loop in \(S\) at a vertex is homotopic, relative to the base point, to an edge loop.

*Proof.* Triangulate \(D\), with the marks as vertices, so finely that every \(\varphi_s\circ F\) varies by less than \(\frac14\) on each triangle (uniform continuity). Label every vertex \(x\) of the triangulation by a vertex \(s\) of \(S\) with \(\varphi_s(F(x))\) largest, so \(\varphi_s(F(x))\ge\frac13\). For a triangle \(\tau\) and \(x'\in\tau\), each label \(s\) of a vertex of \(\tau\) has \(\varphi_s(F(x'))>\frac13-\frac14>0\); so all these labels are vertices of the smallest simplex \(\sigma(x')\) containing \(F(x')\), and they span a face of it. Extending the labels linearly on each triangle gives a simplicial map \(f\), and \(f(x')\) lies in that face, hence in \(\sigma(x')\). The straight-line homotopy in \(\sigma(x')\) joins \(f(x')\) to \(F(x')\), continuously in \(x'\), and fixes the marks, which are labelled by their own images. Along a marked arc mapped along \([s,s']\), only \(s\) and \(s'\) have positive coordinates, and with constant speed \(\varphi_s\) decreases while \(\varphi_{s'}\) increases; so the label changes from \(s\) to \(s'\) exactly once (at a tie either choice has this property). \(\blacksquare\)

Now fix a nonempty closed edge path \(c\) in \(S\) that is nullhomotopic. It is the boundary of a continuous map \(F\colon D\to S\) from a convex polygon \(D\) whose boundary vertices are the marks, the \(k\)-th side going with constant speed along the \(k\)-th edge of \(c\). Lemma 2.1 gives a simplicial map \(f\) from a triangulation of \(D\).

*The picture.* In each triangle \(\tau\) of the triangulation, \(f\) is linear onto a simplex of \(S\). Mark in \(\tau\) the points where the largest coordinate of \(f\) is attained by at least two vertices of \(S\): if \(f(\tau)\) is a triangle, three segments from the point mapped to its barycenter to the midpoints of the sides of \(\tau\); if \(f(\tau)\) is an edge, one segment joining the midpoints of the two sides of \(\tau\) mapped onto that edge; if \(f(\tau)\) is a vertex, nothing. The pieces in adjacent triangles agree on common sides. Their union is a plane graph in \(D\) with *nodes* of valence three at the barycenter points, *leaves* at the midpoints of boundary edges mapped onto edges, one for each edge of \(c\) and in its order, and otherwise vertices of valence two, which we suppress; components may be closed curves. On each component of its complement in \(D\), a *region*, the vertex of \(S\) with the largest coordinate is constant, its *label*.

A *labelled picture* with these boundary data is a plane graph \(P\subset D\) whose vertices of valence one, the leaves, lie on \(\partial D\) at the given points, whose other vertices, the nodes, have valence three and lie inside \(D\) (closed curves without vertices are allowed), with a vertex of \(S\), the label, on each region, such that the two sides of every arc have distinct labels spanning an edge of \(S\), the three regions at every node have labels spanning a triangle of \(S\), and the regions along \(\partial D\) between consecutive leaves carry the vertices of \(c\) in order. The construction above produces one.

**Lemma 2.2** (minimal pictures). Among labelled pictures with these boundary data, let \(P\) have the fewest nodes. Then no arc of \(P\) joins two nodes whose labels span the same triangle of \(S\), and no arc joins a node to itself. Deleting the components of \(P\) that miss \(\partial D\), and relabelling, gives a labelled picture with the same boundary data and no more nodes, in which every component meets \(\partial D\).

*Proof.* An arc joining a node to itself would separate the same two labels at both ends, but the three arcs at a node separate three different pairs.

Let an arc \(\alpha\) join two nodes whose labels span the same triangle \(\{a,b,d\}\), with \(a\) and \(b\) on the two sides of \(\alpha\) and \(d\) the third label at both ends. Take a thin polygonal disk \(N\) around \(\alpha\) and its end nodes, meeting \(P\) only in \(\alpha\) and in initial pieces of the four other arcs at the two nodes, each crossing \(\partial N\) once. In cyclic order around \(\partial N\), the two crossings on the \(a\)-side separate \(a\) from \(d\), and the two on the \(b\)-side separate \(b\) from \(d\). Replace \(P\cap N\) by two disjoint arcs inside \(N\), one joining the two \(a\)-side crossings and one joining the two \(b\)-side crossings, and label the strip between them \(d\). All labels outside \(N\) and on \(\partial N\) are unchanged, also if some of the four arcs reconnect outside \(N\), and the new picture has two fewer nodes, contradicting minimality.

Now delete the components that miss \(\partial D\). The remaining picture together with \(\partial D\) is a connected plane graph \(H\) containing \(\partial D\). Let \(\Phi\) be an inner face of \(H\), with a model given by Proposition 3.3 of the previous lesson. A closed curve in \(\Phi\), close enough to its frontier to miss the deleted components, which are compact and disjoint from \(H\), follows the whole boundary walk of \(\Phi\) and crosses no arc of the old picture; so it lies in one old region, and all old labels along the sides of \(\Phi\) are equal. Give \(\Phi\) this label. The conditions on arcs, nodes and the boundary only concern labels next to retained arcs and \(\partial D\), which are unchanged. \(\blacksquare\)

**Theorem 2.3** (reduced fillings; [OpenAI-RF, Lemma 3.2]). Every nonempty nullhomotopic closed edge path \(c\) in \(S\) is the exterior walk of a planar diagram \(\Delta\) with a diagram map \(\Delta\to S\), such that every triangle of \(\Delta\) has three distinct vertices and three distinct edges, and at every interior vertex of \(\Delta\) the cyclic sequence of corners maps to a nonempty cyclically reduced closed walk in the link of the image vertex.

*Proof.* Take a labelled picture \(P\) with the fewest nodes, and in which every component meets \(\partial D\) (Lemma 2.2). Let \(H=P\cup\partial D\), with \(N\) nodes, \(L\) leaves (\(L\ge2\), the length of \(c\)), \(E\) arcs and \(F\) inner faces.

*The dual graph.* For each inner face \(\Phi\), with a model \((C,\kappa)\), put a *dual vertex* at the image of the center of \(C\), and *radii* at the images of the segments from the center to the midpoints of the sides of \(C\) that lie on arcs of \(P\). For each arc, the two faces on its two sides are different, because their labels differ; join their two radii to the midpoint of one segment of the arc, to form a *dual edge*. The dual edges are polygonal arcs meeting only at dual vertices, so they form a plane graph \(\Gamma^*\) with \(F\) vertices and \(E\) edges, connected because \(D\) is.

*The triangles.* At a node \(\nu\), the three arcs and the three faces around it give three dual edges between three different dual vertices, a cycle. In each of the three faces, the two radii to the sides at \(\nu\) are consecutive, and the sector of the model between them, containing the corner at \(\nu\), maps to a region of the face next to \(\nu\). These three regions and the pieces of the three arcs from their midpoints to \(\nu\) form an open set \(R_\nu\) containing \(\nu\), bounded by the cycle and disjoint from \(\Gamma^*\). By Theorem 1.1 of the previous lesson, \(R_\nu\) is the inside of the cycle: it is connected, open and closed in the inside. So each node gives a bounded face of \(\Gamma^*\) bounded by three dual edges, and different nodes give different faces.

*No holes.* Adding to \(H\) the leaves as vertices on \(\partial D\), Euler's formula for the connected plane graph \(H\) gives \((N+L)-(E+L)+(F+1)=2\), so \(F=E-N+1\). Euler's formula for \(\Gamma^*\) shows that it has \(E-F+1=N\) bounded faces. So the bounded faces of \(\Gamma^*\) are exactly the \(N\) node triangles, and filling them gives a planar diagram \(\Delta\).

*The map.* Send the dual vertex of a face to its label, the dual edge of an arc to the edge of \(S\) spanned by the labels on its sides, and the triangle of a node to the triangle spanned by its three labels. The three dual vertices of a triangle have three distinct labels, so they are distinct, and so are its edges.

*The exterior walk.* Along \(\partial D\), between consecutive leaves, the boundary runs along one face; in its model, the sector between the radii to the two arcs ending at these leaves contains the boundary piece and lies in the unbounded face of \(\Gamma^*\). Following \(\partial D\) once around, the unbounded face therefore passes the dual edges of the arcs at the leaves in the order of the leaves, and between them the dual vertices of the faces along \(\partial D\), whose labels are the vertices of \(c\). An arc with both ends at leaves gives an edge with no triangle, passed twice. So the exterior walk maps to \(c\).

*Reduced links.* An interior vertex is the dual vertex of a face \(\Phi\) whose frontier misses \(\partial D\); its boundary walk passes only along arcs between nodes, so it has corners, the node triangles of these nodes in the order of the walk. Two consecutive corners share the dual edge of the arc between their nodes. If their images in the link of the label of \(\Phi\) were the same link edge traversed back, the two node triangles would map to the same triangle of \(S\), and the arc between their nodes would join two nodes with the same labelled triangle, contrary to Lemma 2.2. This includes the last and the first corner. \(\blacksquare\)

By Lemma 1.2, every closed edge walk in such a diagram is nullhomotopic in the diagram.

## 3. Exercises

**3.1.** Describe the labelled picture of a disk mapped onto a single triangle of \(S\), and the dual diagram.

**3.2.** Let \(c\) go along an edge \([s,s']\) and back. Show that a minimal picture has no nodes, and that the reduced filling is one edge traversed twice by the exterior walk.

**3.3.** Show that the label of a region is constant, that is, that the vertex with the largest coordinate does not change inside a region.

**3.4.** Check the two formulas of Lemma 1.2 for a diagram consisting of two triangles sharing an edge.

## 4. Solutions

**3.1.** With \(f\) linear onto the triangle, the picture is one node joined to three leaves; the three regions carry the three vertices. The dual diagram is one triangle, its exterior walk the boundary of the triangle.

**3.2.** The boundary data have two leaves, and the region between them on one side of \(\partial D\) is labelled \(s\), on the other \(s'\). A single arc between the two leaves, separating \(s\) from \(s'\), is a labelled picture without nodes, so minimal pictures have none; then every arc joins two leaves, and here there is one. The dual is one edge from the \(s\)-face to the \(s'\)-face, with no triangle, so the exterior walk passes along it twice.

**3.3.** In a triangle \(\tau\) of the triangulation, the complement of the marked set consists of the parts where one vertex has the strictly largest coordinate, and across a common side the coordinates of the two triangles agree. So the label is locally constant off the picture, hence constant on each region.

**3.4.** \(v=4\), \(e=5\), \(t=2\): \(4-5+2=1\); the exterior walk is the boundary of the quadrilateral, of length \(4=2\cdot5-3\cdot2\).

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Section 3.2. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
