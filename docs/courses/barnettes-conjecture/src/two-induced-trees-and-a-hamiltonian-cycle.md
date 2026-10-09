# Two induced trees and a Hamiltonian cycle

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof of Barnette's conjecture. A Hamiltonian cycle of a cubic sphere map corresponds to a partition of the vertices of the dual triangulation into two sets, each of which induces a tree; *induces* means that the tree contains every edge of the triangulation between its vertices. This dual formulation goes back to Stein's partition of regions [Ste], and Alt, Payne, Schmidt and Wood state it in the form used here [APSW]. Theorem 5.1 proves the partition for every coloured sphere triangulation, with the vertices of one prescribed face split in a prescribed way. For triangulations without separating triangles, the pair of states with a forest \(Q_s\) from [A cancelling sum over pairs](a-cancelling-sum-over-pairs.md) is converted into a tree on the white faces (Section 2), which selects one edge in every face (Section 3); the edges not selected are dual to one long cycle, whose two sides are the two trees (Section 4). Separating triangles are removed by cutting and gluing (Section 5), and Section 6 deduces the Hamiltonian cycle.

The setting of Sections 1 to 4 is that of [Pairs of states](pairs-of-states.md): \(T\) is a sphere triangulation with a face colouring and no separating triangle, \(t_0\) a black face with its three roots, \(\mathcal T\) the other black faces, \(X\) the non-roots, and \(k\) the number of black faces. In addition, \(e_0\) is a prescribed edge of \(t_0\). By Propositions 3.3 of [Pairs of states](pairs-of-states.md) and 4.2 of [A cancelling sum over pairs](a-cancelling-sum-over-pairs.md), there is a pair \((r,s)\) for which \(Q_s\) is a forest; we fix one. For \(t\in\mathcal T\), let \(u(t)\) be the vertex of \(t\) other than \(r(t)\) and \(s(t)\).

## 1. Root components

Direct the edge of \(Q_s\) in \(t\) from \(r(t)\) to \(u(t)\). Every non-root is the tail of exactly one of these darts, and the roots are tails of none.

**Lemma 1.1.** Every component of \(Q_s\) contains exactly one root.

*Proof.* A component with \(q\) vertices, \(a\) of them roots, is a tree with \(q-1\) edges. Each edge has its tail in the component, and the component contains \(q-a\) tails, so \(q-1=q-a\) and \(a=1\). \(\square\)

## 2. A tree on the white faces

Apply the construction of Lemma 3.2 of [A cancelling sum over pairs](a-cancelling-sum-over-pairs.md) to *all* black faces, \(t_0\) included: the result \(T^{++}\) is a sphere map whose faces are the white faces of \(T\) and, for every black face \(t\) and every edge \(e\) of \(t\), a sector containing the dart of \(e\) in \(t\) and two spokes. Let \(H\) be the spanning subgraph of \(T^{++}\) formed by the \(3k\) spokes.

**Lemma 2.1.** \(H\) is a connected sphere map with \(k\) faces, and its faces correspond to the white faces of \(T\): the region of a face of \(H\) consists of one white face \(w\) and the three sectors adjacent to \(w\) across the edges of \(w\). The dual edge of the spoke from the centre of a black face \(t\) to a vertex \(v\) joins the faces of \(H\) corresponding to the white faces across the two edges of \(t\) at \(v\).

*Proof.* Two vertices of \(T\) joined by an edge in the black face \(t\) are joined in \(H\) through the centre of \(t\), so \(H\) is connected, and it is a sphere map by Proposition 1.6(e) of [Sphere maps](sphere-maps.md). It has \((k+2)+k\) vertices and \(3k\) edges, hence \(2-(2k+2)+3k=k\) faces. The edges of \(T^{++}\) outside \(H\) are the edges of \(T\); each has a sector on its black side and a white face on the other. So every sector is \(H\)-adjacent to exactly one white face, and every white face to its three sectors, and the regions of \(H\) (Proposition 4.1 of [Sphere maps](sphere-maps.md)) are the \(k\) sets described. The two darts of the spoke from \(c_t\) to \(v\) lie in the two sectors of \(t\) at the edges of \(t\) through \(v\), whose regions contain the white faces across these edges. \(\square\)

Delete from \(H\) the spokes from \(c_t\) to \(s(t)\), \(t\in\mathcal T\). What remains consists of \(Q_s\) with each edge subdivided by the centre of its black face, together with the three spokes from the centre of \(t_0\) to the roots. By Lemma 1.1, \(Q_s\) has three components, one at each root, so the remainder is a spanning tree of \(H\). By Lemma 2.2 of [Sphere maps](sphere-maps.md), the dual edges of the deleted spokes form a spanning tree \(Y\) of the dual of \(H\); by Lemma 2.1 its vertices are the \(k\) white faces of \(T\), and the edge belonging to \(t\in\mathcal T\) joins the white faces across the two edges of \(t\) at \(s(t)\).

## 3. One selected edge in every face

Let \(y_0\) be the white face across \(e_0\) from \(t_0\). Root the tree \(Y\) at \(y_0\) and assign each edge of \(Y\) to its end farther from \(y_0\); this is a bijection from the edges of \(Y\) to the white faces other than \(y_0\). For \(t\in\mathcal T\), let \(w_t\) be the white face assigned to the edge of \(t\), and *select* the edge of \(t\) at \(s(t)\) that borders \(w_t\). Select also \(e_0\). Let \(P\) be the set of selected edges and \(P_0=P\setminus\{e_0\}\).

**Lemma 3.1.** Every black face and every white face of \(T\) contains exactly one edge of \(P\), and \(|P|=k\).

*Proof.* Each black face selects one of its edges, and an edge lies in only one black face, so the selections are distinct. The white face \(y_0\) contains \(e_0\), and every other white face \(w\) is \(w_t\) for exactly one \(t\), whose selected edge borders \(w\); the edge selected in a black face \(t'\) borders only the white face \(w_{t'}\) (or \(y_0\) for \(t_0\)). \(\square\)

Direct each edge of \(P_0\) away from \(s(t)\), where \(t\) is the black face that selected it. Every non-root is the tail of exactly one of these darts, the roots of none.

**Lemma 3.2.** \(P\) is a forest with two components, and the two ends of \(e_0\) lie in different components of \(P_0\).

*Proof.* Suppose \(P_0\) contains a cycle \(\Gamma\). As every vertex is the tail of at most one dart, \(\Gamma\) is traversed along the directed edges and avoids the roots. Let \(h\), \(\mathcal A\), \(B\), \(W\) and \(l\) be as in the proof of Lemma 1.1 of [A cancelling sum over pairs](a-cancelling-sum-over-pairs.md). Count the faces of \(\mathcal A\) with sign \(+1\) for black and \(-1\) for white: this gives \(B-W\). By Lemma 3.1, every face contains exactly one selected edge, and every selected edge is the selected edge of both of its faces. So the count can be taken over selected edges with a face in \(\mathcal A\): one with both faces in \(\mathcal A\) contributes \(1-1=0\), and an edge of \(\Gamma\) contributes \(+1\) or \(-1\) according to the colour of its face in \(\mathcal A\). Hence \(B-W=l-(h-l)=2l-h\). Lemma 3.2 of [Triangulations from cubic bipartite graphs](triangulations-from-cubic-bipartite-graphs.md) gives \(3(B-W)=2l-h\), so \(2l-h=0\). But the directed edges of \(P_0\) leave \(s(t)\) in each \(t\in\mathcal T\), so Lemma 1.1 of [A cancelling sum over pairs](a-cancelling-sum-over-pairs.md), applied to the state \(s\), gives \(2l-h=\pm3\). Hence \(P_0\) is a forest. As in Lemma 1.1, each of its components contains exactly one root. The edge \(e_0\) joins two roots, which lie in different components, so \(P\) is a forest. It has \(k+2\) vertices and \(k\) edges, hence two components. \(\square\)

## 4. The long dual cycle

**Theorem 4.1.** Let \(T\) be a sphere triangulation with a face colouring and no separating triangle, \(t_0\) a face and \(e_0\) an edge of \(t_0\). The vertices of \(T\) can be partitioned into two sets, each inducing a tree, such that the ends of \(e_0\) lie in one set and the third vertex of \(t_0\) in the other.

*Proof.* Exchanging colours if necessary, \(t_0\) is black, and the construction above applies. Let \(G=T^*\) be the dual map. By Lemma 3.2, \(P\) is a spanning forest of \(T\), so by Lemma 2.2 of [Sphere maps](sphere-maps.md) the dual edges of the edges outside \(P\) form a connected spanning subgraph \(Z\) of \(G\). Every vertex of \(G\) is a face of \(T\), which has two edges outside \(P\) by Lemma 3.1; so \(Z\) is connected with all degrees \(2\), that is, a single cycle through all vertices of \(G\).

By Theorem 3.2 of [Sphere maps](sphere-maps.md) applied in \(G\), the faces of \(G\), which are the vertices of \(T\), split into two nonempty sides \(V_1\), \(V_2\) of \(Z\), and an edge lies in \(Z\) exactly when its two darts have their faces in \(G\), which are their tails in \(T\), on different sides. Thus an edge of \(T\) lies in \(P\) exactly when its ends lie in the same set \(V_i\). Each component of \(P\) lies in one set, both sets are nonempty, and \(P\) has two components, so \(V_1\) and \(V_2\) are the vertex sets of the two trees of \(P\). An edge of \(T\) with both ends in \(V_i\) lies in \(P\), so \(V_i\) induces this tree. Finally \(e_0\in P\), while the other two edges of \(t_0\) are not in \(P\) (Lemma 3.1), so the third vertex of \(t_0\) lies in the other set. \(\square\)

## 5. Separating triangles

**Theorem 5.1** (OpenAI 2026). Let \(T\) be a sphere triangulation with a face colouring, \(t_0\) a face and \(e_0\) an edge of \(t_0\). The vertices of \(T\) can be partitioned into two sets, each inducing a tree, such that the ends of \(e_0\) lie in one set and the third vertex of \(t_0\) in the other.

*Proof.* By induction on the number of vertices. Without separating triangles this is Theorem 4.1. Otherwise let \(C\) be a separating triangle, with sides named so that \(t_0\in\mathcal A\), and let \(T_{\mathcal A}\), \(T_{\mathcal A'}\) be the two pieces of Lemma 4.2 of [Triangulations from cubic bipartite graphs](triangulations-from-cubic-bipartite-graphs.md). Both are coloured sphere triangulations with fewer vertices than \(T\); \(t_0\) is a face of \(T_{\mathcal A}\), and the triangle \(C\) bounds the cap of each piece.

By induction, \(T_{\mathcal A}\) has a partition \(V_1\cup V_2\) with the required property for \(t_0\) and \(e_0\). The three vertices of \(C\) do not lie in one set, since a triangle cannot lie in an induced tree; so exactly one edge \(e_C\) of \(C\) has both ends in one set. By induction, \(T_{\mathcal A'}\) has a partition \(W_1\cup W_2\) in which the ends of \(e_C\) lie in one set and the third vertex of \(C\) in the other; numbering the sets suitably, \(W_i\cap V(C)=V_i\cap V(C)\) for \(i=1,2\). Put \(U_i=V_i\cup W_i\).

The vertex sets of the pieces cover \(V(T)\) and meet exactly in \(V(C)\), so \(U_1,U_2\) partition \(V(T)\). Every edge of \(T\) has both darts in faces of \(\mathcal A\), or both in faces of \(\mathcal A'\), or lies in \(C\); an edge with an end strictly inside \(\mathcal A\) is of the first kind (Lemma 3.4(b) of [Sphere maps](sphere-maps.md)), and an edge between two vertices of \(C\) is an edge of \(C\) because \(T\) is simple. Hence the subgraph of \(T\) induced by \(U_i\) is the union of the trees induced by \(V_i\) in \(T_{\mathcal A}\) and by \(W_i\) in \(T_{\mathcal A'}\). These two trees meet in the subgraph induced by \(V_i\cap V(C)\), which is a single vertex or the edge \(e_C\) with its ends. If two trees with vertex sets \(V'\) and \(V''\) meet exactly in a tree with nonempty vertex set \(V'''\), their union is connected and has \((|V'|-1)+(|V''|-1)-(|V'''|-1)=|V'\cup V''|-1\) edges, so it is a tree; here the common edges are the edges of \(C\) with both ends in \(V_i\). The ends of \(e_0\) and the third vertex of \(t_0\) keep their sets from \(T_{\mathcal A}\). \(\square\)

## 6. The Hamiltonian cycle

**Theorem 6.1** (OpenAI 2026; Barnette's conjecture). Every finite simple graph that is cubic, bipartite and \(3\)-connected and carries a sphere map has a Hamiltonian cycle. Moreover, for every edge \(e\) there is a Hamiltonian cycle not containing \(e\).

*Proof.* By Theorem 2.3 of [Triangulations from cubic bipartite graphs](triangulations-from-cubic-bipartite-graphs.md), \(T=G^*\) is a sphere triangulation with a face colouring and \(T^*=G\). Given \(e\), its dual edge \(e^*\) is an edge of \(T\); choose a face \(t_0\) of \(T\) containing it and put \(e_0=e^*\). Theorem 5.1 gives a partition \(V_1\cup V_2\) of the vertices of \(T\) into two sets inducing trees, the ends of \(e_0\) in one set. Let \(P\) be the set of edges of \(T\) with both ends in one set; it is a spanning forest consisting of the two trees. A face of \(T\) has its three vertices in both sets, because an induced tree contains no triangle, so exactly one of its edges lies in \(P\). By Lemma 2.2 of [Sphere maps](sphere-maps.md), the dual edges of the edges outside \(P\) form a connected spanning subgraph of \(G\), in which every vertex of \(G\), a face of \(T\), has degree \(2\). It is a Hamiltonian cycle of \(G\), and it does not contain \(e\), because \(e^*=e_0\in P\). \(\square\)

**Corollary 6.2** (Barnette's conjecture for planar graphs). Every finite simple cubic bipartite \(3\)-connected planar graph has a Hamiltonian cycle, and one avoiding any prescribed edge.

*Proof.* A plane embedding gives a sphere map by Theorem 5.1 of [Sphere maps](sphere-maps.md), the embedding theorem, which this course records as an open obligation; then Theorem 6.1 applies. \(\square\)

**Remarks.** (a) As noted in [OpenAI-B], avoidance of a single edge is a known equivalent strengthening of Barnette's conjecture, through work of Kelmans explained by Hertel and by Gorsky, Steiner and Wiederrecht [GSW].

(b) Gorsky, Steiner and Wiederrecht proved that Barnette's conjecture is equivalent to the statement that every path with three edges in a cubic, \(3\)-connected, bipartite *Pfaffian* graph lies in a Hamiltonian cycle (Theorem 4.16 of [GSW], as cited in [OpenAI-B]); planar graphs are Pfaffian. Combined with Corollary 6.2 this gives that statement. The equivalence is not proved in this course, so this consequence is recorded as an open obligation.

## 7. Exercises

**7.1.** For the octahedron with vertices \(\pm e_1,\pm e_2,\pm e_3\), \(t_0\) the face \(e_1e_2e_3\) and \(e_0=e_1e_2\), find a partition as in Theorem 5.1, and the resulting Hamiltonian cycle of the cube.

**7.2.** For the bipyramid over a \(2n\)-gon (\(n\ge2\)) with apices \(N,S\) and equator \(v_1,\dots,v_{2n}\), show that \(\{N,v_1,v_3,\dots,v_{2n-1}\}\) and \(\{S,v_2,\dots,v_{2n}\}\) induce trees, and describe the Hamiltonian cycle of the prism that results.

**7.3.** In the proof of Theorem 5.1, explain why \(e_C\) is the only edge of \(C\) with both ends in one set, and why the two partitions can be numbered to agree on \(V(C)\).

## 8. Solutions

**7.1.** The sets \(\{e_1,e_2,-e_1\}\) and \(\{e_3,-e_2,-e_3\}\) work: the first induces the path \(e_1,e_2,-e_1\) (as \(e_1\) and \(-e_1\) are not adjacent), and the second the path \(e_3,-e_2,-e_3\). The ends of \(e_0\) are together, and \(e_3\) is in the other set. The edges of the octahedron between the two sets are dual to a Hamiltonian cycle of the cube: each face of the octahedron has exactly one edge inside a set, and the dual edges of the other \(12-4=8\) edges form a cycle through the eight vertices of the cube.

**7.2.** \(N\) is adjacent to every equatorial vertex, the odd-numbered equatorial vertices are pairwise non-adjacent because \(2n\ge4\), and \(N\) and \(S\) are not adjacent. So the first set induces a star with centre \(N\), and the second a star with centre \(S\). The edges between the sets are the equatorial edges and the edges \(Nv_{2j}\), \(Sv_{2j-1}\); their dual edges form a Hamiltonian cycle of the prism that uses every rung (the duals of the equatorial edges) and every second edge of each \(2n\)-gon, so it changes between the two \(2n\)-gons at every rung.

**7.3.** The vertices of \(C\) are split two and one between the sets, so exactly the edge between the two vertices in the same set has both ends in one set. Both partitions put the ends of \(e_C\) in one set and the third vertex of \(C\) in the other, so the sets of \(T_{\mathcal A'}\) can be numbered to match.

## References

- [OpenAI-B] OpenAI, *Paired states and Hamiltonian cycles in cubic bipartite planar graphs*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf
- [Ste] S. K. Stein, *B-sets and planar maps*, Pacific Journal of Mathematics 37 (1971), 217–224. https://msp.org/pjm/1971/37-1/pjm-v37-n1-p20-s.pdf
- [APSW] H. Alt, M. S. Payne, J. M. Schmidt and D. R. Wood, *Thoughts on Barnette's conjecture*, Australasian Journal of Combinatorics 64 (2016), 354–365. https://arxiv.org/abs/1312.3783
- [GSW] M. Gorsky, R. Steiner and S. Wiederrecht, *Matching theory and Barnette's conjecture*, Discrete Mathematics 346 (2023), 113249. https://arxiv.org/abs/2202.11641
