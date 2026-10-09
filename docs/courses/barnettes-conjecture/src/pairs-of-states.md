# Pairs of states

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fix a black face of a coloured sphere triangulation and call its three vertices the roots. The remaining black faces and the remaining vertices are equally many. A *state* assigns to each remaining black face one of its vertices, using every non-root vertex exactly once, and a *pair* consists of two states that choose differently at every face. These face–vertex matchings are Tutte's states from his theory of trinity; Hine and Kálmán give a modern treatment and relate their moves to Kauffman's clock theorem [HK]. This lesson proves that a pair exists when the triangulation has no separating triangle (Proposition 3.3). The proof combines an integral flow argument (Section 2) with a density inequality for sets of vertices (Proposition 3.1), which is proved face by face with the regions of [Sphere maps](sphere-maps.md).

## 1. States and pairs

Throughout, \(T\) is a sphere triangulation with a face colouring and without separating triangles ([Triangulations from cubic bipartite graphs](triangulations-from-cubic-bipartite-graphs.md)), and \(t_0\) is a face of \(T\). Exchanging the two colours if necessary, we assume that \(t_0\) is black. The three vertices of \(t_0\) are the *roots*. Let \(k\) be the number of black faces, \(\mathcal T\) the set of black faces other than \(t_0\), and \(X\) the set of non-root vertices; by Lemma 1.3 of the previous lesson,
\[
|\mathcal T|=|X|=k-1 .
\]
For a face \(t\), \(V(t)\) is its set of three vertices.

**Definition 1.1.** A *state* is a bijection \(r:\mathcal T\to X\) with \(r(t)\in V(t)\) for every \(t\in\mathcal T\). A *pair* is an ordered pair \((r,s)\) of states with \(r(t)\ne s(t)\) for every \(t\in\mathcal T\).

Let \(\Gamma\) be the bipartite *incidence graph* with parts \(\mathcal T\) and \(X\), in which \(t\) is joined to each non-root vertex of \(t\). It is simple. States are perfect matchings of \(\Gamma\), and pairs are ordered pairs of edge-disjoint perfect matchings.

## 2. Integral flows and two disjoint matchings

A *network* is a finite directed graph with a source \(o\), a sink \(z\ne o\), and nonnegative integer capacities \(\kappa\) on its arcs. A *flow* assigns to each arc \(a\) a number \(0\le g(a)\le\kappa(a)\) such that inflow equals outflow at every vertex other than \(o,z\); its *value* is the net outflow at \(o\). A *cut* is a set \(Z\) of vertices with \(o\in Z\), \(z\notin Z\); its capacity is the sum of the capacities of the arcs leaving \(Z\).

**Lemma 2.1.** If every cut has capacity at least \(c\), there is a flow of value at least \(c\) with integer values on all arcs.

*Proof.* Summing the conservation equations over a cut \(Z\) shows that the value of any flow equals the flow on arcs leaving \(Z\) minus the flow on arcs entering \(Z\); in particular it is at most the capacity of \(Z\). Start with the zero flow. Given an integral flow \(g\), form the residual graph: an arc \(a\) from \(x\) to \(y\) gives a forward residual arc with capacity \(\kappa(a)-g(a)\) if this is positive, and a backward residual arc from \(y\) to \(x\) with capacity \(g(a)\) if this is positive. If the residual graph has a directed path from \(o\) to \(z\), increase the flow by the smallest residual capacity on it (forward arcs up, backward arcs down); this is a positive integer, conservation is kept, and the value increases by at least \(1\). The value is bounded by the capacity of any cut, so after finitely many steps no path exists. Then let \(Z\) be the set of vertices reachable from \(o\) in the residual graph. Every arc leaving \(Z\) is saturated and every arc entering \(Z\) carries zero flow, so the value equals the capacity of \(Z\), which is at least \(c\). \(\square\)

**Lemma 2.2.** Let \(\Gamma\) be a simple bipartite graph with parts \(P\), \(Q\) of equal size \(n\). If
\[
\sum_{p\in P}\min\bigl(2,|N(p)\cap S|\bigr)\ge2|S|\qquad\text{for every }S\subseteq Q, \tag{2.1}
\]
where \(N(p)\) is the set of neighbours of \(p\), then \(\Gamma\) has two edge-disjoint perfect matchings.

*Proof.* Build a network with arcs \(o\to q\) of capacity \(2\) for \(q\in Q\), arcs \(q\to p\) of capacity \(1\) for the edges of \(\Gamma\), and arcs \(p\to z\) of capacity \(2\) for \(p\in P\). For a cut \(Z\), put \(S=Q\cap Z\). The arcs \(o\to q\) with \(q\notin S\) contribute \(2(n-|S|)\). A vertex \(p\in Z\) contributes \(2\) through its arc to \(z\), and a vertex \(p\notin Z\) contributes \(|N(p)\cap S|\) through the arcs from \(S\). Hence the capacity of \(Z\) is at least
\[
2(n-|S|)+\sum_{p\in P}\min\bigl(2,|N(p)\cap S|\bigr)\ge2n
\]
by (2.1). Lemma 2.1 gives an integral flow of value \(2n\), which saturates all arcs at \(o\) and at \(z\). The edges of \(\Gamma\) carrying flow \(1\) therefore form a spanning subgraph in which every vertex has degree \(2\). Its components are cycles; they have even length because \(\Gamma\) is bipartite, and length at least \(4\) because \(\Gamma\) is simple. Taking alternate edges of every cycle gives two edge-disjoint perfect matchings. \(\square\)

## 3. The density inequality

For a set \(U\) of vertices of \(T\), let \(e(U)\) be the number of edges with both ends in \(U\), and \(b(U)\) the number of black faces, \(t_0\) included, with all three vertices in \(U\).

**Proposition 3.1.** For every set \(U\) of vertices containing the three roots,
\[
e(U)-b(U)\le2|U|-4 .
\]

The proof treats the components of the induced subgraph \(T[U]\) one at a time. A component \(K\) with at least one edge, with the rotations of \(T\) restricted to it, is a sphere map, and its faces correspond to its regions by Proposition 4.1 of [Sphere maps](sphere-maps.md): the region of a face \(f\) of \(K\) is a set \(R_f\) of faces of \(T\), the regions partition the faces of \(T\), and the darts of \(f\) are the darts of \(K\) whose face in \(T\) lies in \(R_f\).

**Lemma 3.2.** Let \(K\) be a component of \(T[U]\) with \(p\ge4\) vertices and \(m\) edges, and let \(b_K\) be the number of black faces of \(T\) with all vertices in \(K\). Then \(m-b_K\le2p-4\).

*Proof.* *Faces of \(K\) have length at least \(3\).* A face of length \(1\) would be a loop. A face \((d,x)\) of length \(2\) is a closed walk \(u\to v\to u\); without parallel edges \(x=\theta d\), so \(\sigma(\theta d)=\theta d\) and \(\sigma(d)=d\), and \(K\) would be a single edge.

*Faces of length \(3\) of \(K\) are faces of \(T\).* Let \(f=(d_1,d_2,d_3)\) be a face of \(K\) of length \(3\); by Lemma 1.2 of the previous lesson its darts traverse a triangle \(C\). Let \(\mathcal S\) be the side of \(C\) on the left of \(d_1,d_2,d_3\) (Lemma 3.3 of [Sphere maps](sphere-maps.md)). The faces of \(R_f\) lie in \(\mathcal S\): the face of \(T\) on the left of \(d_1\) belongs to \(R_f\) and to \(\mathcal S\), and \(K\)-adjacent faces share an edge outside \(K\), hence outside \(C\), so they lie on the same side. Since \(C\) is not separating, one side \(\mathcal S_0\) consists of a single face \(g_0\) whose darts are the darts of \(C\) with \(\mathcal S_0\) on their left (Lemma 4.1 of the previous lesson).

Suppose \(\mathcal S\ne\mathcal S_0\). As \(p\ge4\) and \(K\) is connected, some edge of \(K\) joins a vertex \(y\) of \(C\) to a vertex \(x\) not on \(C\); \(x\) is strictly inside \(\mathcal S\), because \(\mathcal S_0\) has no vertex strictly inside it (Corollary 3.1 of the previous lesson gives \(1=2I+1\)). Let \(d_i\) enter \(y\), so that \(d_{i+1}=\varphi_K(d_i)\) leaves \(y\) (indices modulo \(3\)). Since \(\varphi_K(d_i)=\sigma_K(\theta d_i)\), no dart of \(K\) lies strictly between \(\theta d_i\) and \(d_{i+1}\) in the rotation at \(y\), so the dart \(z_0\) from \(y\) to \(x\) lies strictly between \(d_{i+1}\) and \(\theta d_i\). Let \(y_1=\sigma(d_{i+1}),\dots,y_n\) be the darts at \(y\) strictly between \(d_{i+1}\) and \(\theta d_i\). The face on the left of \(\theta d_{i+1}\) contains \(\varphi(\theta d_{i+1})=y_1\), each \(\operatorname{face}(\theta y_j)\) contains \(\sigma(y_j)\), and \(\operatorname{face}(y_j)\), \(\operatorname{face}(\theta y_j)\) lie on one side because \(y_j\) is not a dart of \(C\). So all these faces lie on the side of \(\operatorname{face}(\theta d_{i+1})\), which is \(\mathcal S_0\). In particular the edge \(yx\) has its faces in \(\mathcal S_0\). But \(x\) is strictly inside \(\mathcal S\), so by Lemma 3.4(b) of [Sphere maps](sphere-maps.md) the faces of the edge \(yx\) lie in \(\mathcal S\). This contradiction shows \(\mathcal S=\mathcal S_0\). Then \(R_f=\{g_0\}\), and \(g_0\) contains the three darts of \(f\), so \(f\) is the face \(g_0\) of \(T\).

*Conversely*, a face \(g\) of \(T\) with all three vertices in \(K\) has its three edges in \(K\), so it is \(K\)-adjacent to no face and forms a region by itself; the corresponding face of \(K\) consists of the three darts of \(g\). Hence the faces of length \(3\) of \(K\) are exactly the faces of \(T\) with all vertices in \(K\); let \(b_K\) and \(w_K\) be the numbers of black and white ones.

*Faces of length \(d\ge4\).* For a face \(f\) of \(K\) of length \(d\), let \(b'_f\), \(w'_f\) be the numbers of black and white faces of \(T\) in \(R_f\). Summing \(\delta\) (Section 3 of the previous lesson) over the darts of the faces of \(R_f\): grouped by faces of \(T\) this gives \(3(b'_f-w'_f)\); grouped by edges, an edge outside \(K\) with a dart in a face of \(R_f\) has both faces in \(R_f\) and contributes \(0\), while the darts of edges of \(K\) whose face lies in \(R_f\) are exactly the \(d\) darts of \(f\). So \(3(b'_f-w'_f)\) is a sum of \(d\) terms \(\pm1\). For \(d=4\) such a sum is even and at most \(4\) in absolute value, hence \(0\) as a multiple of \(3\); for \(d=5\) it is odd and at most \(5\), hence at most \(3\); for \(d\ge6\), \(|b'_f-w'_f|\le d/3\le d-4\). In all cases \(|b'_f-w'_f|\le d-4\).

*Counting.* The regions partition the faces of \(T\), which has as many black as white faces (Lemma 1.3 of the previous lesson). The triangular faces of \(K\) are single faces of \(T\), so
\[
w_K-b_K=\sum_{d_f\ge4}(b'_f-w'_f)\le\sum_{d_f\ge4}(d_f-4),
\]
the sums running over the faces of \(K\) of length at least \(4\). With \(F_K\) the number of faces of \(K\),
\[
2m=\sum_fd_f=4F_K-(b_K+w_K)+\sum_{d_f\ge4}(d_f-4)\ge4F_K-2b_K .
\]
Since \(K\) is a sphere map, \(F_K=2-p+m\), and therefore \(2m\ge8-4p+4m-2b_K\), that is, \(m-b_K\le2p-4\). \(\square\)

*Proof of Proposition 3.1.* The three roots are pairwise adjacent, so they lie in one component \(K_0\) of \(T[U]\). If \(K_0\) has at least four vertices, Lemma 3.2 gives \(m_0-b_{K_0}\le2p_0-4\). If it has three, it is the triangle of \(t_0\), with \(m_0=3\) and \(b_{K_0}=1\): another black face on the same three vertices would also be bounded by this triangle, both sides of the triangle would then be single faces, and \(T\) would have only two faces. So \(m_0-b_{K_0}=2=2\cdot3-4\). Every other component \(K\) satisfies \(m_K-b_K\le2p_K\): by Lemma 3.2 if \(p_K\ge4\), and otherwise because a simple graph with \(p_K\le3\) vertices has at most \(\binom{p_K}{2}\le2p_K\) edges. The edges of \(T[U]\) and the black faces with all vertices in \(U\) are distributed among the components, so
\[
e(U)-b(U)=\sum_K(m_K-b_K)\le(2p_0-4)+\sum_{K\ne K_0}2p_K=2|U|-4.\qquad\square
\]

**Proposition 3.3.** If \(T\) has no separating triangle, a pair of states exists.

*Proof.* We verify (2.1) for the incidence graph, with \(P=\mathcal T\) and \(Q=X\). Let \(S\subseteq X\) and \(U=V(T)\setminus S\), which contains the roots. For a black face \(t\) with \(j\) vertices in \(U\), the number \(e_t(U)\) of its edges with both ends in \(U\) is \(0,0,1,3\) for \(j=0,1,2,3\), and
\[
\min\bigl(2,|V(t)\cap S|\bigr)=\min(2,3-j)=2-e_t(U)+\mathbf 1[j=3].
\]
For \(t_0\) both sides vanish. Every edge of \(T\) lies in exactly one black face, so summing over all \(k\) black faces gives
\[
\sum_{t\in\mathcal T}\min\bigl(2,|N(t)\cap S|\bigr)=2k-e(U)+b(U)\ge2k-2|U|+4=2|S|,
\]
by Proposition 3.1 and \(|U|+|S|=k+2\). Lemma 2.2 gives two edge-disjoint perfect matchings of \(\Gamma\), that is, a pair. \(\square\)

## 4. Exercises

**4.1.** In the octahedron with vertices \(\pm e_1,\pm e_2,\pm e_3\), colour the face with vertices \(\epsilon_1e_1,\epsilon_2e_2,\epsilon_3e_3\) black when \(\epsilon_1\epsilon_2\epsilon_3=1\). Take \(t_0\) the face \(e_1e_2e_3\). Find all states and all pairs.

**4.2.** Show that equality holds in Proposition 3.1 for \(U=V(T)\) and for \(U\) the set of roots.

**4.3.** Show that a simple graph in which every vertex has degree \(2\) is a disjoint union of cycles, and that in a bipartite such graph each cycle has even length.

## 5. Solutions

**4.1.** The black faces other than \(t_0\) are \(t_1=e_1(-e_2)(-e_3)\), \(t_2=(-e_1)e_2(-e_3)\), \(t_3=(-e_1)(-e_2)e_3\), and the non-roots are \(-e_1,-e_2,-e_3\). The incidence graph is the \(6\)-cycle \(t_1,-e_2,t_3,-e_1,t_2,-e_3,t_1\), which has two perfect matchings: \(r_1=(t_1\mapsto-e_2,\ t_3\mapsto-e_1,\ t_2\mapsto-e_3)\) and \(r_2=(t_1\mapsto-e_3,\ t_2\mapsto-e_1,\ t_3\mapsto-e_2)\). They are disjoint, so the pairs are \((r_1,r_2)\) and \((r_2,r_1)\).

**4.2.** For \(U=V(T)\): \(e(U)=3k\), \(b(U)=k\) and \(2|U|-4=2k\). For the roots: \(e(U)=3\), \(b(U)=1\) (Proof of Proposition 3.1) and \(2\cdot3-4=2\).

**4.3.** Starting at a vertex and leaving each vertex by the edge not used to enter it, one returns to the start, because the graph is finite and every vertex has exactly two edges; this traces a cycle, and the cycles through different vertices are disjoint or equal. In a bipartite graph the vertices of a cycle alternate between the two parts, so its length is even.

## References

- [OpenAI-B] OpenAI, *Paired states and Hamiltonian cycles in cubic bipartite planar graphs*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf
- [HK] C. Hine and T. Kálmán, *Clock theorems for triangulated surfaces*, 2018. https://arxiv.org/abs/1808.06091
