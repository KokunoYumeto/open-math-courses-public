# Triangulations from cubic bipartite graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The dual of a cubic map has triangular faces, and a bipartition of the cubic graph colours these triangles black and white. This lesson shows that the dual of a cubic, bipartite, \(3\)-connected sphere map is a *sphere triangulation* (Theorem 2.3), counts the parts of a triangle-coloured map on one side of a cycle (Corollary 3.1 and Lemma 3.2), and shows how to cut a triangulation along a separating triangle (Lemma 4.2). Notation and results are those of [Sphere maps](sphere-maps.md): for a dart \(d\), \(\operatorname{face}(d)\) is the face on its left, a cycle has two sides (Theorem 3.2 there), and the Euler count \(I-E_{\mathcal A}+|\mathcal A|=1\) holds for each side (Proposition 3.5 there).

## 1. Sphere triangulations

**Definition 1.1.** A *sphere triangulation* is a sphere map whose underlying graph is simple (no loops, no parallel edges), which has at least four vertices, and in which every face has length \(3\).

**Lemma 1.2.** In a map whose underlying graph is simple, the three darts of a face of length \(3\) traverse a cycle of length \(3\): three distinct vertices joined pairwise by three distinct edges.

*Proof.* The face is a closed walk \(u\to v\to w\to u\) (Lemma 1.2 of [Sphere maps](sphere-maps.md)). Without loops, \(u\ne v\), \(v\ne w\), \(w\ne u\). The three edges join different pairs of vertices, so they are distinct. \(\square\)

A *face colouring* of a map colours each face black or white so that the two darts of every edge lie in faces of different colours.

**Lemma 1.3.** A sphere triangulation with a face colouring has as many black as white faces. If \(k\) is this number, it has \(3k\) edges and \(k+2\) vertices.

*Proof.* Every edge has exactly one dart in a black face, and every black face has three darts, so \(E=3B\); likewise \(E=3W\). Then \(\chi=V-3k+2k=2\) gives \(V=k+2\). \(\square\)

## 2. The dual of a cubic bipartite graph

A graph is *\(3\)-connected* if it has at least four vertices and deleting any one or two vertices leaves it connected. For a set \(X\) of vertices, the *cut* \(\delta(X)\) is the set of edges with exactly one end in \(X\).

**Lemma 2.1.** Let \(G\) be a simple, cubic, \(3\)-connected graph. Every cut \(\delta(X)\) with \(\varnothing\ne X\ne V(G)\) has at least three edges.

*Proof.* Suppose \(|\delta(X)|\le2\), and let \(Y\) be the complement of \(X\). If \(|X|=1\), the vertex of \(X\) has three edges, all in the cut. If \(|X|=2\), at most one edge joins the two vertices of \(X\), so at least \(3+3-2=4\) edge ends lie in the cut. Hence \(|X|\ge3\), and likewise \(|Y|\ge3\). Deleting the at most two ends in \(X\) of the cut edges leaves a nonempty part of \(X\) and all of \(Y\), with no edge between them, contrary to \(3\)-connectivity. \(\square\)

**Lemma 2.2** (Cycles of the dual are cuts). Let \(M\) be a sphere map and \(C^*\) a cycle of the dual map \(M^*\). There is a set \(X\) of vertices of \(M\) with \(\varnothing\ne X\ne V(M)\) such that the edges of \(C^*\) are exactly the edges of the cut \(\delta(X)\).

*Proof.* The faces of \(M^*\) are the vertices of \(M\), the face of \(M^*\) on the left of a dart being the tail of that dart in \(M\) (Lemma 2.1 of [Sphere maps](sphere-maps.md)). By Theorem 3.2 there, applied in the sphere map \(M^*\), the vertices of \(M\) split into two nonempty sides \(X\), \(X'\) such that an edge lies in \(C^*\) exactly when the tails of its two darts, which are its two ends in \(M\), lie on different sides. \(\square\)

**Theorem 2.3.** Let \(G\) be a simple, cubic, bipartite, \(3\)-connected graph with a sphere map. Then the dual map \(T=G^*\) is a sphere triangulation, and colouring each face of \(T\) by the bipartition class of the corresponding vertex of \(G\) is a face colouring of \(T\). The dual of \(T\) is \(G\), and \(T\) has \(2+|V(G)|/2\) vertices.

*Proof.* A loop of \(T\) is a cycle of length \(1\) of \(G^*\), and two parallel edges of \(T\) form a cycle of length \(2\). By Lemma 2.2 either would be a cut of \(G\) with one or two edges, which Lemma 2.1 excludes. So the underlying graph of \(T\) is simple. The faces of \(T\) are the vertices of \(G\), which have degree \(3\), so every face of \(T\) has length \(3\). The two darts of an edge lie in the faces of \(T\) corresponding to the two ends of the edge in \(G\), which lie in different bipartition classes. \(T\) is a sphere map by Lemma 2.1 of [Sphere maps](sphere-maps.md), with \(T^*=G\). Its number of vertices is the number of faces of \(G\), namely \(2-|V(G)|+|E(G)|=2+|V(G)|/2\ge4\), because \(|E(G)|=3|V(G)|/2\) and \(|V(G)|\ge4\). \(\square\)

## 3. Counting on one side of a cycle

**Corollary 3.1.** Let \(C\) be a cycle of length \(h\) in a sphere map all of whose faces have length \(3\), and let \(\mathcal A\) be a side of \(C\) with \(I\) vertices strictly inside it. Then
\[
|\mathcal A|=2I+h-2,\qquad E_{\mathcal A}=3I+h-3 .
\]

*Proof.* Each face of \(\mathcal A\) has three darts. An edge counted by \(E_{\mathcal A}\) has both darts in faces of \(\mathcal A\), an edge of \(C\) has exactly one, and no other edge has any (Theorem 3.2 of [Sphere maps](sphere-maps.md)). So \(3|\mathcal A|=2E_{\mathcal A}+h\). Together with \(I-E_{\mathcal A}+|\mathcal A|=1\) (Proposition 3.5 there) this gives both formulas. \(\square\)

For a map with a face colouring, define on darts
\[
\delta(d)=\begin{cases}+1&\text{if }\operatorname{face}(d)\text{ is black},\\-1&\text{if }\operatorname{face}(d)\text{ is white}.\end{cases}
\]
Since the two darts of an edge lie in faces of different colours, \(\delta(\theta d)=-\delta(d)\). For adjacent vertices \(v,w\) of a triangulation, which are joined by one edge, write \(\delta(v,w)\) for \(\delta\) of the dart from \(v\) to \(w\): it is \(+1\) when the black face of the edge is on the left of this dart.

**Lemma 3.2** (Signed count). In a sphere map with a face colouring all of whose faces have length \(3\), let \(C\) be a cycle of length \(h\), oriented so that a side \(\mathcal A\) lies on the left of its darts (Lemma 3.3 of [Sphere maps](sphere-maps.md)). Let \(B\), \(W\) be the numbers of black and white faces in \(\mathcal A\), and \(l\) the number of edges of \(C\) whose black face lies in \(\mathcal A\). Then
\[
3(B-W)=\sum_{d\in C}\delta(d)=2l-h .
\]

*Proof.* Sum \(\delta\) over all darts lying in faces of \(\mathcal A\). Grouped by faces, a black face contributes \(+3\) and a white face \(-3\). Grouped by edges, an edge with both darts in faces of \(\mathcal A\) contributes \(\delta(d)+\delta(\theta d)=0\); an edge of \(C\) contributes the value of \(\delta\) on its dart with \(\mathcal A\) on the left, which is the dart of the orientation; no other edge contributes. Finally \(\delta(d)=+1\) for a dart of the orientation exactly when its face, the face of the edge in \(\mathcal A\), is black. \(\square\)

## 4. Separating triangles

A cycle of length \(3\) in a sphere triangulation is a *triangle*; it is *separating* if both of its sides have vertices strictly inside them.

**Lemma 4.1.** If a triangle \(C\) of a sphere triangulation is not separating, one of its sides consists of a single face, whose three darts are the darts of \(C\) with this side on their left.

*Proof.* Let \(\mathcal A\) be a side with \(I=0\). Corollary 3.1 gives \(|\mathcal A|=1\) and \(E_{\mathcal A}=0\). The darts of the face in \(\mathcal A\) therefore belong to edges of \(C\), each of which has exactly one dart in a face of \(\mathcal A\). \(\square\)

**Lemma 4.2** (Cutting along a separating triangle). Let \(C\) be a separating triangle of a sphere triangulation \(T\), with sides \(\mathcal A\) and \(\mathcal A'\). Delete from \(T\) all edges both of whose darts lie in faces of \(\mathcal A'\), and then all vertices strictly inside \(\mathcal A'\). The result \(T_{\mathcal A}\) is a sphere triangulation with fewer vertices than \(T\). Its faces are the faces of \(\mathcal A\) and one further face \(f_C\), the *cap*, whose darts are the three darts of \(C\) with \(\mathcal A'\) on their left. If \(T\) has a face colouring, the three faces of \(\mathcal A'\) along \(C\) have the same colour, and giving \(f_C\) this colour, while keeping the colours of \(\mathcal A\), defines a face colouring of \(T_{\mathcal A}\).

*Proof.* A face of \(\mathcal A\) contains no dart of a deleted edge, so by Lemma 1.4 of [Sphere maps](sphere-maps.md) it survives every deletion unchanged. By Lemma 3.4(b) there, every edge at a vertex strictly inside \(\mathcal A'\) has both darts in faces of \(\mathcal A'\), so these vertices become isolated and are removed. What remains is the subgraph \(G_{\mathcal A}\) of the proof of Proposition 3.5 there: it is connected, with \(I+3\) vertices and \(E_{\mathcal A}+3\) edges, and by Proposition 1.6(e) there it is a sphere map. Let \(F_{\mathrm{rest}}\) be its number of faces other than those of \(\mathcal A\). Then
\[
2=(I+3)-(E_{\mathcal A}+3)+|\mathcal A|+F_{\mathrm{rest}}=1+F_{\mathrm{rest}},
\]
by Proposition 3.5 there, so there is exactly one further face. Its darts are the remaining darts, namely the darts of \(C\) not lying in faces of \(\mathcal A\), which are the three darts with \(\mathcal A'\) on the left. The underlying graph is a subgraph of a simple graph, every face has length \(3\), and there are \(I+3\ge4\) vertices because \(C\) is separating; the vertices strictly inside \(\mathcal A'\), at least one, have been removed.

For the colouring, Lemma 3.2 applied to the side \(\mathcal A'\) gives \(3(B'-W')=\sum\delta(d)\), the sum over the three darts of \(C\) with \(\mathcal A'\) on the left; a sum of three terms \(\pm1\) that is divisible by \(3\) has three equal terms. So the faces of \(\mathcal A'\) along the three edges of \(C\) have one colour, and the faces of \(\mathcal A\) along them have the other colour. Colouring the cap with the first colour gives every edge of \(C\) faces of different colours in \(T_{\mathcal A}\), and nothing changes for the other edges. \(\square\)

Exchanging the roles of the two sides gives a second sphere triangulation \(T_{\mathcal A'}\). The two pieces share the triangle \(C\), and every vertex of \(T\) belongs to at least one of them.

## 5. Exercises

**5.1.** Show that the dual of the cube is the octahedron, and that the bipartition of the cube colours the eight faces of the octahedron alternately, so that the four faces at each vertex alternate in colour.

**5.2.** Let \(n\ge2\). Show that the dual of the prism over a cycle of length \(2n\) is the bipyramid over a \(2n\)-gon, and that this triangulation has no separating triangle.

**5.3.** Let \(T\) be a sphere triangulation and \(xyz\) a face. Insert three new vertices \(a,b,c\) inside it, joined by the edges \(ab,bc,ca\), \(xb,xc\), \(ya,yc\), \(za,zb\). Show that the result is a sphere triangulation with \(T\)'s face colouring extended, that every vertex degree changes by an even number, and that \(xyz\) has become a separating triangle.

**5.4.** Check Corollary 3.1 for the equator of the octahedron.

## 6. Solutions

**5.1.** The cube has eight vertices and six faces; its dual has six vertices, one per face of the cube, and eight triangular faces, one per vertex of the cube, so it is the octahedron. Adjacent vertices of the cube correspond to faces of the octahedron sharing an edge, so the bipartition gives a face colouring. Around a vertex of the octahedron the four faces correspond to the four vertices of a square face of the cube, which alternate between the two classes.

**5.2.** The prism over a \(2n\)-cycle has two \(2n\)-gonal faces and \(2n\) quadrilaterals; its dual has two apices of degree \(2n\) and an equator of \(2n\) vertices of degree \(4\): the bipyramid. A triangle of the bipyramid contains an apex and two consecutive equatorial vertices, or three equatorial vertices; the latter is impossible for \(2n\ge4\) since the equator is an induced cycle of length \(2n\). So every triangle consists of an apex and two consecutive equatorial vertices, and it bounds a face \(f\). By Theorem 3.2 of [Sphere maps](sphere-maps.md), \(\{f\}\) is one of its sides, and no vertex is strictly inside it (Exercise 6.3 there), so the triangle is not separating.

**5.3.** The face \(xyz\) is replaced by the seven triangles \(xcb\), \(yac\), \(zba\), \(xyc\), \(yza\), \(zxb\) and \(abc\); vertices increase by \(3\), edges by \(9\) and faces by \(6\), so \(\chi\) is unchanged. The degrees of \(x,y,z\) increase by \(2\), and \(a,b,c\) have degree \(4\). Colour \(abc\) and \(xyc,yza,zxb\) with the colour of \(xyz\), and \(xcb,yac,zba\) with the other colour; then every new edge has faces of different colours, and the edges \(xy,yz,zx\) keep a face of the old colour of \(xyz\) on their inner side. The new vertices \(a,b,c\) lie strictly inside one side of the triangle \(xyz\), and the other vertices of \(T\) (at least one) inside the other.

**5.4.** For the equator, \(h=4\) and \(I=1\) on each side, so \(|\mathcal A|=2+4-2=4\) and \(E_{\mathcal A}=3+4-3=4\), as found in Exercise 6.4 of [Sphere maps](sphere-maps.md).

## References

- [OpenAI-B] OpenAI, *Paired states and Hamiltonian cycles in cubic bipartite planar graphs*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf
