# Paths, cycles and Lovász's decomposition theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Graphs in this course are finite, simple and undirected. A *path* has at least one edge and no repeated vertex; a *cycle* has at least three edges and no repeated vertex. A *cycle-and-edge partition* of a graph \(G\) is a family of subgraphs of \(G\), each a cycle or a single edge, such that every edge of \(G\) lies in exactly one member. Taking every edge singly is always such a partition; the question is how few members suffice.

A tree with \(n\) vertices contains no cycle, so it needs \(n-1\) members. Erdős and Gallai asked whether a linear number always suffices. The question appears in the 1966 paper of Erdős, Goodman and Pósa, which also gives the bound \(O(n\log n)\) and Gallai's example of graphs that need about \(4n/3\) members [EGP, Section 5]. This course proves the answer found by OpenAI [OpenAI-EG]:

**Theorem** (the Erdős–Gallai cycle decomposition theorem). There is an absolute constant \(C\) such that the edge set of every graph with \(n\) vertices can be partitioned into at most \(Cn\) cycles and single edges.

The members of the partition may share vertices but no edge. The proof gives an absolute constant without a numerical value. Before it, the best general bounds were \(O(n\log\log n)\), due to Conlon, Fox and Sudakov [CFS], and \(O(n\log^*n)\), due to Bucić and Montgomery [BM], where \(\log^*n\) is the number of times the logarithm must be applied to bring \(n\) down to at most one. The argument of [OpenAI-EG] builds on their expansion, matching and path-closing methods. An independent proof by J. Kim appeared in October 2026 [Kim].

The linear order is optimal, and the constant cannot be below \(3/2\): Exercise 5.2 shows that complete bipartite graphs need about \(\frac32n\) members. If the members may share edges, the problem is different and easier: Pyber showed that \(n-1\) cycles and edges always cover the edges of a graph with \(n\) vertices (see [BM, Section 1]). A cover does not give a partition, because deleting repeated edges breaks cycles into paths.

**What the course assumes.** Basic finite probability: independence, expectation and its linearity, as in the core course [Probability](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B90) [GS]. All probability spaces in the course are finite. Every result used is proved in the lessons, with one exception: the second assertion of Corollary 7.2 of the last lesson uses a theorem of Girão, Granet, Kühn and Osthus [GGKO], stated there as a named statement.

**The course.**

1. This lesson: decompositions into paths and cycles, Lovász's theorem, and path decompositions with at most two ends at each vertex.
2. [Disjoint representatives in hypergraphs](disjoint-representatives-in-hypergraphs.md): Haxell's condition for choosing pairwise disjoint edges from several hypergraphs.
3. [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md): short edge-disjoint connecting paths, with disjointness of inner vertices within prescribed teams.
4. [Splitting a graph at a scale](splitting-a-graph-at-a-scale.md): long cycles, overlapping boxes and expanding pieces.
5. [Random sampling in expanding graphs](random-sampling-in-expanding-graphs.md): Chernoff bounds and the expansion of random vertex samples.
6. [Closing paths through reservoirs](closing-paths-through-reservoirs.md): an expanding graph leaves residual graphs of arbitrarily small total order.
7. [Folding pairs and lifting cycles](folding-pairs-and-lifting-cycles.md): identifying pairs of vertices, and lifting the cycles of the smaller graph.
8. [The linear bound](the-linear-bound.md): the induction over scales, and two consequences for graphs with even degrees.

## 1. Decompositions into paths and cycles

A *decomposition* of a graph \(G\) into paths and cycles is a family \(\mathcal D\) of subgraphs of \(G\), each a path or a cycle, such that every edge of \(G\) lies in exactly one member. Members carry only their own edges. For a vertex \(v\), the *end count* \(e_{\mathcal D}(v)\) is the number of paths of \(\mathcal D\) that have \(v\) as an end. A vertex is *odd* or *even* according to the parity of its degree \(d_G(v)\).

**Lemma 1.1** (parity of end counts). For every decomposition \(\mathcal D\) of \(G\) into paths and cycles and every vertex \(v\),
\[
e_{\mathcal D}(v)\equiv d_G(v)\pmod 2 .
\]
In particular, every odd vertex is an end of at least one path of \(\mathcal D\).

*Proof.* Each edge at \(v\) lies in one member. A cycle through \(v\), and a path with \(v\) as an inner vertex, contain exactly two edges at \(v\); a path with \(v\) as an end contains exactly one. Hence \(d_G(v)\) is \(e_{\mathcal D}(v)\) plus an even number. \(\square\)

If every vertex of \(G\) is odd, Lemma 1.1 shows that every decomposition has at least \(n/2\) paths, since each path has two ends.

Two further counts are used throughout. For a graph \(G\) let \(e(G)\) be its number of edges and \(\sigma(G)\) its number of vertices of positive degree. Since every vertex of positive degree has degree at least one,
\[
2e(G)=\sum_vd_G(v)\ge\sigma(G).
\]

## 2. At most n/2 paths and cycles

**Theorem 2.1** (Lovász [Lov]). Every graph \(G\) has a decomposition into at most \(\lfloor\sigma(G)/2\rfloor\) paths and cycles. In particular, a graph with \(n\) vertices has a decomposition into at most \(\lfloor n/2\rfloor\) paths and cycles.

*Proof.* Put \(\lambda(G)=2e(G)-\sigma(G)\), an integer with \(\lambda(G)\ge0\). We use induction on \(\lambda(G)\).

If \(\lambda(G)=0\), the inequality above is an equality, so every vertex of positive degree has degree one. Then \(G\) is a matching together with isolated vertices, and its \(\sigma(G)/2\) edges, taken singly, form the required decomposition.

Let \(\lambda(G)>0\), and assume the theorem for every graph \(G'\) with \(\lambda(G')<\lambda(G)\).

*Step 1: an even vertex.* We choose a graph \(G_1\) and adjacent vertices \(x,y\) of \(G_1\), where \(y\) has even positive degree in \(G_1\).

- **Case A.** If \(G\) has a vertex of even positive degree, let \(G_1=G\), let \(y\) be such a vertex and let \(x\) be a neighbour of \(y\).
- **Case B.** Otherwise every vertex of positive degree is odd. Since \(\lambda(G)>0\), the graph \(G\) is not a matching, so some vertex \(x\) has degree at least two, hence at least three. Choose a neighbour \(z\) of \(x\), and let \(G_1\) arise from \(G\) by replacing the edge \(xz\) with the two edges \(xy\) and \(yz\), where \(y\) is a new vertex.

In Case B every vertex of \(G\) has the same degree in \(G_1\) as in \(G\), and \(y\) has degree two. Put \(s=\sigma(G_1)\); thus \(s=\sigma(G)\) in Case A and \(s=\sigma(G)+1\) in Case B.

*Step 2: a graph with smaller \(\lambda\).* Let \(G'\) arise from \(G_1\) by deleting every edge that joins \(x\) to a vertex of even degree in \(G_1\). We claim that \(\lambda(G')<\lambda(G)\) and \(\sigma(G')\le s\).

In Case A, let \(k\ge1\) be the number of deleted edges; the edge \(xy\) is one of them. A deleted edge joins \(x\) to an even vertex of positive degree, whose degree is at least two and drops by exactly one. So no vertex other than \(x\) loses all its edges, and \(\sigma(G')\ge\sigma(G)-1\). Hence
\[
\begin{aligned}
\lambda(G')&\le2(e(G)-k)-\sigma(G)+1\\
&\le\lambda(G)-1 .
\end{aligned}
\]
In Case B, the only even neighbour of \(x\) in \(G_1\) is \(y\): every other neighbour is a vertex of \(G\), whose degree is odd. So \(G'=G_1-xy\). It has \(e(G)\) edges; the vertex \(y\) keeps the edge \(yz\), and \(x\) keeps at least two edges. Thus \(\sigma(G')=\sigma(G)+1\) and \(\lambda(G')=\lambda(G)-1\).

In both cases deleting edges creates no vertex of positive degree, so \(\sigma(G')\le\sigma(G_1)=s\). By the induction hypothesis \(G'\) has a decomposition \(\Sigma\) into at most \(\lfloor s/2\rfloor\) paths and cycles.

*Step 3: the neighbours of \(x\).* Let \(N\) be the set of neighbours of \(x\) in \(G_1\), and let \(a_1,\dots,a_k\) be those of even degree in \(G_1\). Every vertex of \(N\) is odd in \(G'\): each \(a_i\) lost exactly the edge \(a_ix\), and a vertex of \(N\) of odd degree lost no edge, because every deleted edge joins \(x\) to an even vertex. By Lemma 1.1, every \(h\in N\) is an end of at least one path of \(\Sigma\). For every \(h\in N\) fix one such path and call it \(U(h)\); we read \(U(h)\) starting at \(h\). This choice is made once and is used throughout the rest of the proof.

*Step 4: chains of vertices.* For each \(i\le k\) define vertices \(a_{i,0},a_{i,1},\dots\) recursively. Put \(a_{i,0}=a_i\). If \(a_{i,\mu}\) is defined and the path \(U(a_{i,\mu})\) does not contain \(x\), the chain stops at \(a_{i,\mu}\). Otherwise let \(a_{i,\mu+1}\) be the vertex of \(U(a_{i,\mu})\) immediately before \(x\), reading from \(a_{i,\mu}\). The edge \(a_{i,\mu+1}x\) belongs to \(U(a_{i,\mu})\), so it is an edge of \(G'\) and \(a_{i,\mu+1}\in N\). Thus:

- (C1) for \(\mu\ge1\), the vertex \(a_{i,\mu}\) is adjacent to \(x\) in \(G'\), and the edge \(a_{i,\mu}x\) lies in the path \(U(a_{i,\mu-1})\);
- (C2) the vertex \(a_{i,0}=a_i\) is not adjacent to \(x\) in \(G'\).

**Claim.** If \(a_{i,\mu}=a_{j,\nu}\), then \(i=j\) and \(\mu=\nu\). Consequently every chain stops.

Let \(a_{i,\mu}=a_{j,\nu}\) with \(\mu\le\nu\). If \(\mu=0\), then \(a_{j,\nu}=a_i\) is not adjacent to \(x\) in \(G'\), so \(\nu=0\) by (C1), and \(a_i=a_j\) gives \(i=j\). If \(\mu\ge1\), the edge \(a_{i,\mu}x\) of \(G'\) lies in exactly one member \(W\) of \(\Sigma\). By (C1), \(W=U(a_{i,\mu-1})\) and \(W=U(a_{j,\nu-1})\). Walk along \(W\) from \(x\) through its neighbour \(a_{i,\mu}\) until the end of \(W\). Reading \(W\) from \(a_{i,\mu-1}\), the vertex \(a_{i,\mu}\) comes immediately before \(x\); so this walk ends at \(a_{i,\mu-1}\). In the same way it ends at \(a_{j,\nu-1}\). Hence \(a_{i,\mu-1}=a_{j,\nu-1}\). Repeating this \(\mu\) times gives \(a_{i,0}=a_{j,\nu-\mu}\), and the case \(\mu=0\) gives \(\nu=\mu\) and \(i=j\).

Since \(N\) is finite and the vertices of a chain are distinct, every chain stops. Let \(N'\) be the set of all \(a_{i,\mu}\). The claim shows in particular that \(a_{i,\mu+1}\ne a_{i,\mu}\): the vertex before \(x\) on \(U(a_{i,\mu})\) is never its first vertex.

*Step 5: a decomposition of \(G_1\).* Say that \(h\in N'\) *chooses* the member \(U(h)\) of \(\Sigma\). Only an end of a path can choose it, so every member is chosen by at most two vertices of \(N'\). A member may end at two vertices of \(N'\) and be chosen by only one of them; it is then treated as a member with one chooser. For every member \(V\) of \(\Sigma\) define \(f(V)\):

- If no vertex of \(N'\) chooses \(V\), put \(f(V)=V\).
- If exactly one vertex \(h\) chooses \(V\), read \(V\) from \(h\). If \(x\) lies on \(V\), write \(V=h\cdots p\,x\,R\), where \(p\) is the vertex before \(x\) and \(R\) is the remainder after \(x\), possibly empty; let \(f(V)\) be the path \(p\cdots h\,x\,R\), obtained by adding the edge \(hx\) and deleting the edge \(px\). If \(x\) is not on \(V\), let \(f(V)\) be the path \(x\,h\cdots\) obtained by adding \(hx\).
- If two vertices \(h,h'\) choose \(V\), they are its two ends. If \(x\) lies on \(V\), it is an inner vertex, since \(x\notin N\); write \(V=h\cdots p\,x\,q\cdots h'\) and let \(f(V)\) be the path \(p\cdots h\,x\,h'\cdots q\), obtained by adding \(hx\) and \(h'x\) and deleting \(px\) and \(qx\). If \(x\) is not on \(V\), let \(f(V)\) be the cycle formed by \(V\) and the edges \(hx\) and \(h'x\).

Each \(f(V)\) is a path or a cycle of \(G_1\): the pieces of \(V\) that are joined are disjoint, the vertex \(x\) is added at most once, and the cycle in the last case has at least three edges because \(h\ne h'\). In the first rotation \(p\ne h\), by the end of Step 4.

The members \(f(V)\) partition \(E(G_1)\). Indeed, \(f\) only adds and deletes edges of the form \(hx\) with \(h\in N'\). Each such edge is added exactly once, to \(U(h)\). If \(h=a_{i,\mu}\) with \(\mu\ge1\), the edge \(hx\) lies in \(G'\) in the member \(U(a_{i,\mu-1})\), and it is deleted from that member: there \(h\) is the vertex before \(x\), read from the chooser \(a_{i,\mu-1}\). If \(\mu=0\), the edge \(a_ix\) is one of the edges deleted in Step 2, and it returns. Every other edge stays in its member of \(\Sigma\). Hence \(\{f(V):V\in\Sigma\}\) is a decomposition of \(G_1\) into at most \(\lfloor s/2\rfloor\) paths and cycles.

*Step 6: back to \(G\).* In Case A, \(G_1=G\) and \(s=\sigma(G)\), so the proof is finished. In Case B every vertex of positive degree of \(G\) is odd, and the number of odd vertices of a graph is even; so \(\sigma(G)\) is even and \(\lfloor s/2\rfloor=\sigma(G)/2\). In the decomposition of \(G_1\), each of the \(\sigma(G)\) vertices of positive degree other than \(y\) is odd and is therefore an end of some path. At most \(\sigma(G)/2\) members provide at most \(\sigma(G)\) ends. So every member is a path, each of these vertices is an end of exactly one path, and \(y\) is an end of none. The vertex \(y\) has degree two, so it is an inner vertex of one path, which contains \(x\,y\,z\) consecutively. Replacing \(x\,y\,z\) by the edge \(xz\) gives a decomposition of \(G\) into at most \(\sigma(G)/2\) paths. \(\square\)

The construction of Steps 3 to 5 is a sequence of rotations. A path ending at \(h\) and passing through \(x\) is turned around its segment from \(h\) to the vertex before \(x\), and the edge set changes by one edge at \(x\). The claim of Step 4 guarantees that the chains of rotations never collide.

## 3. Paths with few ends at each vertex

Theorem 2.1 allows cycles. The later lessons need decompositions into paths only, in which no vertex is the end of many paths.

**Corollary 3.1.** Every graph \(G\) with \(n\) vertices has a decomposition into paths in which every vertex is an end of at most two paths. Such a decomposition has at most \(n\) paths.

*Proof.* For \(n=0\) there is nothing to prove. Otherwise add a new vertex \(v_0\) and join it to every vertex of even degree in \(G\), isolated vertices included. In the resulting graph \(G^+\) every old vertex is odd. By Theorem 2.1, \(G^+\) has a decomposition \(\mathcal D\) into at most \(\lfloor(n+1)/2\rfloor\) paths and cycles. Let \(p\) be its number of paths. By Lemma 1.1 each of the \(n\) old vertices is an end of a path, so \(2p\ge n\). Hence
\[
\Bigl\lceil\frac n2\Bigr\rceil\le p\le|\mathcal D|\le\Bigl\lfloor\frac{n+1}2\Bigr\rfloor=\Bigl\lceil\frac n2\Bigr\rceil .
\]
So every member of \(\mathcal D\) is a path, and \(2p\le n+1\). The end count of an old vertex is odd. If one old vertex were an end of three or more paths, the old vertices would provide at least \(n+2\) ends, more than \(2p\). So every old vertex is an end of exactly one path.

Delete \(v_0\). A path through \(v_0\) falls into at most two paths; discard pieces without edges. An old vertex \(v\) is incident with at most one edge to \(v_0\), so it becomes an end of at most one new piece. Its end count is therefore at most two. The resulting paths partition \(E(G)\), and since every path has two ends, there are at most \(2n/2=n\) of them. \(\square\)

## 4. Two decomposition facts about cycles

**Lemma 4.1.** A graph in which every vertex has even degree has a decomposition into cycles.

*Proof.* Induction on the number of edges. If there is an edge, take a longest path \(v_0v_1\cdots v_m\). The vertex \(v_0\) has a second neighbour besides \(v_1\), since its degree is even and positive. By maximality this neighbour lies on the path, say \(v_j\) with \(j\ge2\), and \(v_0v_1\cdots v_jv_0\) is a cycle. Deleting its edges keeps all degrees even. \(\square\)

**Lemma 4.2.** Deleting the edges of a cycle from a graph does not change the parity of any degree.

*Proof.* A cycle contains either two edges or no edge at each vertex. \(\square\)

## 5. Exercises

**5.1** (easy). Show that a forest with \(n\) vertices and \(c\) components needs exactly \(n-c\) members in every cycle-and-edge partition.

**5.2** (medium). Let \(G\) be the complete bipartite graph with classes \(A\) and \(B\), where \(|A|=2k+1\) and \(|B|=m\). Show that every cycle-and-edge partition of \(G\) has at least \(\bigl(\frac32-\frac1{4k+2}\bigr)m\) members. Conclude that the constant in the theorem is at least \(3/2\).

**5.3** (medium). Use Theorem 2.1 to show that the complete graph on \(2k+1\) vertices decomposes into \(k\) Hamiltonian cycles, and that the complete graph on \(2k\) vertices decomposes into \(k\) Hamiltonian paths.

**5.4** (easy). Show that the bound of Theorem 2.1 is attained by every graph in which all vertices have odd degree.

**5.5** (medium). Deduce from Theorem 2.1 that every graph with \(u\) odd vertices and \(g\ge1\) even vertices has a decomposition into at most \(u/2+g-1\) paths. (Join \(g-1\) new vertices to \(g-1\) of the even vertices, one each.)

## 6. Solutions

**5.1.** A forest has no cycle, so every member is a single edge, and a forest with \(c\) components has \(n-c\) edges.

**5.2.** Every vertex of \(B\) has odd degree \(2k+1\). The members containing a vertex \(b\in B\) use two edges at \(b\) if they are cycles and one if they are single edges, so at least one single edge contains \(b\). No edge joins two vertices of \(B\), so these single edges are distinct, and there are \(s\ge m\) single edges. A cycle alternates between \(A\) and \(B\) and uses each vertex of \(A\) at most once, so it has at most \(2(2k+1)\) edges. The cycles cover the other \((2k+1)m-s\) edges, so the number of members is at least
\[
\begin{aligned}
&s+\frac{(2k+1)m-s}{4k+2}\\
&\quad=s\Bigl(1-\frac1{4k+2}\Bigr)+\frac m2 ,
\end{aligned}
\]
which is at least \(\bigl(\frac32-\frac1{4k+2}\bigr)m\) because \(s\ge m\). The graph has \(n=m+2k+1\) vertices; letting \(k\) grow and \(m/k\to\infty\), the ratio of the bound to \(n\) tends to \(3/2\).

**5.3.** The complete graph on \(2k+1\) vertices has \(k(2k+1)\) edges, and Theorem 2.1 decomposes it into at most \(k\) paths and cycles. A path has at most \(2k\) edges and a cycle at most \(2k+1\). So there are exactly \(k\) members, each a cycle through all vertices. On \(2k\) vertices every degree is \(2k-1\), odd, so Lemma 1.1 forces at least \(k\) paths; at most \(k\) members are allowed, so there are exactly \(k\) paths and no cycle. The \(k(2k-1)\) edges are covered by \(k\) paths of at most \(2k-1\) edges each, so every path passes through all vertices.

**5.4.** With all degrees odd, every vertex is an end of a path (Lemma 1.1), so there are at least \(n/2\) members; \(n\) is even, and Theorem 2.1 gives at most \(n/2\).

**5.5.** Let \(G'\) be the graph with \(g-1\) new vertices, each joined to a different even vertex of \(G\). It has \(n'=u+2g-1\) vertices and exactly one even vertex. By Theorem 2.1 it decomposes into at most \(\lfloor n'/2\rfloor=u/2+g-1\) members. By Lemma 1.1 the \(n'-1\) odd vertices are ends of paths, so there are at least \((n'-1)/2\) paths, which is the whole allowance: every member is a path. Delete the new vertices. Each has degree one, so it is the end of exactly one path, and deleting it shortens that path; a path consisting of its edge alone disappears. The result is a decomposition of \(G\) into at most \(u/2+g-1\) paths.

## References

- [OpenAI-EG] OpenAI, *A linear cycle-and-edge decomposition of every graph*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026
- [EGP] P. Erdős, A. W. Goodman and L. Pósa, *The representation of a graph by set intersections*, Canadian Journal of Mathematics 18 (1966), 106–112. https://www.renyi.hu/~p_erdos/1966-21.pdf
- [CFS] D. Conlon, J. Fox and B. Sudakov, *Cycle packing*, Random Structures & Algorithms 45 (2014), 608–626; arXiv:1310.0632. https://arxiv.org/abs/1310.0632
- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
- [Kim] J. Kim, *A proof of the Erdős–Gallai cycle decomposition conjecture*, arXiv:2610.07840 (2026). https://arxiv.org/abs/2610.07840
- [Lov] L. Lovász, *On covering of graphs*, in P. Erdős and G. Katona (eds.), *Theory of Graphs*, Proceedings of the Colloquium held at Tihany, Hungary, September 1966, Akadémiai Kiadó, Budapest, 1968, 231–236. https://real-eod.mtak.hu/14547/
- [GGKO] A. Girão, B. Granet, D. Kühn and D. Osthus, *Path and cycle decompositions of dense graphs*, Journal of the London Mathematical Society 104 (2021), 1085–1134; arXiv:1911.05501. https://arxiv.org/abs/1911.05501
- [GS] C. M. Grinstead and J. L. Snell, *Introduction to Probability*, the basis of the core course [Probability](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B90). https://math.dartmouth.edu/~prob/prob/prob.pdf
