# Closing paths through reservoirs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An expanding piece found in [Splitting a graph at a scale](splitting-a-graph-at-a-scale.md) can be decomposed into linearly many cycles and edges, apart from a residue that lives on a small part of its vertex set. This lesson proves it. The edges are first cut into paths with few ends at every vertex, by [Lovász's theorem](paths-cycles-and-lovasz-decompositions.md); every path is then closed into a cycle through one of three small random *reservoirs*, using connecting paths supplied by the [routing theorem](routing-in-graphs-with-cut-expansion.md). The reservoirs keep only edges that were reserved for connections and remained unused. Reserving vertices and edges to close paths is central to the cycle decompositions of Conlon, Fox and Sudakov [CFS, Section 3], and the use of three vertex classes, with every path closed through a class it avoids, is due to Bucić and Montgomery [BM, Section 5].

The scale notation of [Random sampling in expanding graphs](random-sampling-in-expanding-graphs.md) is used: \(D\) is large, \(\sigma=D^{0.90}\) and \(\tau=D^{0.74}\). A *completed part* is a cycle or a single edge.

## 1. Statement

**Lemma 1.1** (small residue). Fix \(\eta>0\) and \(c>0\). For all sufficiently large \(D\), the following holds. Let \(G\) be a graph of order \(r\) with \(D^{0.90}\le r\le D^{1.02}\) that contains a spanning subgraph of cut expansion at least \(cD^{0.90}\). Then \(E(G)\) can be partitioned into the edge sets of at most \(9r\) completed parts and of at most three *residual* graphs. The residual graphs have pairwise disjoint vertex sets contained in \(V(G)\), their orders add up to at most \(\eta r\), and each has order less than \(r\).

The residual graphs may contain many edges; what matters later is that their total order is a small fraction of \(r\), so that they can be handled by induction at a small cost.

## 2. Proof

Put \(c_0=\min\{c,1\}\) and fix
\[
p=\min\Bigl\{\frac\eta{12},\frac1{12}\Bigr\},\qquad h=\frac{c_0}6\sigma .
\]
Then \(3p<1\) and \(6p\le\eta\).

**2.1. Three sparse expanding layers.** The spanning subgraph has cut expansion at least \(c_0\sigma\). By the edge splitting lemma (Lemma 2.1 of [Random sampling in expanding graphs](random-sampling-in-expanding-graphs.md), with \(l=3\)), its edges can be partitioned into three spanning subgraphs \(P_1,P_2,P_3\), each of cut expansion at least \(c_0\sigma/6=h\).

**2.2. Three reservoirs.** Give every vertex one of the labels \(1,2,3\), each with probability \(p\), or the label \(0\) with probability \(1-3p\), independently. Let \(V_i\) be the set of vertices labelled \(i\). These sets are pairwise disjoint, and each \(V_i\) on its own is a sample in which every vertex is chosen independently with probability \(p\). By the vertex sampling lemma (Lemma 3.1 of the same lesson, applied to \(P_i\) with \(c'=c_0/6\)) and the union bound over \(i\), for large \(D\) there is a labelling with, for every \(i\),
\[
\begin{gathered}
|V_i|\le2pr,\\
|N_{P_i}(v)\cap V_i|\ge\frac{ph}2\quad(v\in V(G)),\\
P_i[V_i]\text{ has cut expansion at least }\tau .
\end{gathered}
\]
The success events need not be independent. The second property makes \(V_i\) nonempty and gives every vertex of \(V_i\) a neighbour in \(V_i\), so \(|V_i|\ge2\).

**2.3. Reserved edges.** For every \(i\), reserve the edges of \(P_i[V_i]\), forming \(E_i^{\rm in}\). Also reserve, for every vertex \(v\notin V_i\), two edges of \(P_i\) from \(v\) to two distinct vertices of \(V_i\), its *representatives*, forming \(E_i^{\rm out}\). We choose the representatives so that every vertex of \(V_i\) receives at most
\[
k_0=\Bigl\lceil\frac{8r}{ph}\Bigr\rceil
\]
of these edges. Make the choices one at a time. Fewer than \(2r\) edges are chosen before any choice, so fewer than \(2r/k_0\le ph/4\) vertices of \(V_i\) have already received \(k_0\) edges. The vertex \(v\) has at least \(ph/2\) neighbours in \(V_i\) in \(P_i\); excluding the saturated ones and, for the second choice, the first representative leaves at least \(ph/4-1>0\) candidates for large \(D\).

For one \(i\), the sets \(E_i^{\rm in}\) and \(E_i^{\rm out}\) are disjoint: the edges of the first have both ends in \(V_i\), those of the second only one. Reservations for different \(i\) are disjoint because they lie in the edge-disjoint graphs \(P_i\). Let \(E_{\rm res}\) be the union of all reserved edges.

**2.4. Paths outside the reservoirs.** An edge has two ends, which lie in at most two of the three disjoint reservoirs; so every edge of \(E(G)\setminus E_{\rm res}\) has both ends outside some \(V_i\). Assign each such edge to one such \(i\). This gives edge-disjoint graphs \(G_i\) on \(V(G)\setminus V_i\) whose edge sets partition the unreserved edges. By Corollary 3.1 of [Paths, cycles and Lovász's decomposition theorem](paths-cycles-and-lovasz-decompositions.md), each \(G_i\) has a decomposition \(\mathcal P_i\) into paths in which every vertex is an end of at most two paths; in particular \(|\mathcal P_i|\le|V(G)\setminus V_i|\le r\).

For every end occurrence of a vertex \(v\) in \(\mathcal P_i\), assign one of the two reserved edges of \(v\) in \(E_i^{\rm out}\), different edges to different occurrences; two edges suffice by the bound on end occurrences. For a path \(Q\in\mathcal P_i\) with ends \(x\ne y\), let \(x',y'\in V_i\) be the representatives reached by the assigned edges. If \(x'\ne y'\), record a *demand* between \(x'\) and \(y'\) in \(P_i[V_i]\). Every demand end uses a different reserved edge at its representative, so every vertex of \(V_i\) is an end of at most \(k_0\) demands.

**2.5. Routing.** Apply the routing theorem (Theorem 2.1 of [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md)) in \(P_i[V_i]\), of order \(r_i=|V_i|\ge2\) and cut expansion at least \(\tau\), with \(k=k_0\), teams of one demand (\(b=1\)) and no forbidden vertices (\(z=0\)). By Corollary 2.2 there, its length parameter satisfies \(\ell_i\le108(r_i/\tau)\log^2r_i=O((r/\tau)\log^2r)\), and \(k_0=O(r/h)\) with a constant depending on \(p\) and \(c\). Hence
\[
\begin{aligned}
\ell_i^2(k_0+1)&=O\Bigl(\frac{r^3\log^4r}{\tau^2h}\Bigr)\\
&=O(D^{0.68}\log^4D)=o(\tau),
\end{aligned}
\]
because \(3\cdot1.02-2\cdot0.74-0.90=0.68<0.74\). For large \(D\) the hypothesis \(\tau\ge128\,\ell_i^2(k_0+1)\) holds, and the theorem supplies pairwise edge-disjoint paths in \(P_i[V_i]\) joining the ends of all demands. They use only edges of \(E_i^{\rm in}\).

**2.6. Closing the paths.** Let \(Q\in\mathcal P_i\) have ends \(x\ne y\). If \(x'\ne y'\), the edge \(xx'\), the routing path from \(x'\) to \(y'\), and the edge \(y'y\), together with \(Q\), form a closed walk; \(Q\) lies outside \(V_i\) and all the new vertices lie in \(V_i\), so it is a cycle, with at least four edges. If \(x'=y'\), the two reserved edges \(xx'\) and \(x'y\) close \(Q\) into a cycle through \(x'\); they are distinct because \(x\ne y\), and the cycle has at least three edges.

These cycles are edge-disjoint: their path edges partition the unreserved edges, each assigned reserved edge of \(E_i^{\rm out}\) is used once, and the routing paths in each \(P_i[V_i]\) are edge-disjoint; the three kinds of edges are disjoint, and so are the reservations for different \(i\).

**2.7. Counting.** There are at most \(\sum_i|\mathcal P_i|\le3r\) cycles. Every unused edge of \(E_i^{\rm out}\), for all \(i\), becomes a single-edge part; there are at most \(\sum_i2|V(G)\setminus V_i|\le6r\) of them. So there are at most \(9r\) completed parts.

For every \(i\), let \(H_i\) be the graph on \(V_i\) formed by the edges of \(E_i^{\rm in}\) not used by routing paths. Every unreserved edge lies on a closed path, every edge of \(E_i^{\rm out}\) lies in a cycle or is a single-edge part, and every edge of \(E_i^{\rm in}\) lies on a routing path or in \(H_i\); so the completed parts and \(H_1,H_2,H_3\) partition \(E(G)\). The graph \(H_i\) is not the graph induced by \(G\) on \(V_i\): an unreserved edge with both ends in \(V_i\) was assigned to a complementary graph \(G_j\), \(j\ne i\). The residual graphs \(H_i\) have the disjoint vertex sets \(V_i\), and
\[
\begin{gathered}
\sum_{i=1}^3|V(H_i)|\le6pr\le\eta r,\\
|V(H_i)|\le2pr\le\frac r6<r .
\end{gathered}
\]
All thresholds depend only on \(\eta\) and \(c\). \(\square\)

## 3. Exercises

**3.1** (easy). Explain why one or two reservoirs would not suffice for Section 2.4.

**3.2** (easy). Why does a path \(Q\in\mathcal P_i\) with one edge and \(x'=y'\) give a triangle, and why can a path with \(x'\ne y'\) not produce a cycle of length three?

**3.3** (medium). Suppose every vertex were an end of at most \(m\) paths of \(\mathcal P_i\) instead of two. How should the reservations change, and how does the bound \(9r\) change?

**3.4** (medium). Show that the bound \(\ell_i^2(k_0+1)=o(\tau)\) would fail if the reservoirs had cut expansion only \(D^{0.70}\), and identify which exponent comparison breaks.

## 4. Solutions

**3.1.** With a single reservoir \(V_1\), an unreserved edge with an end in \(V_1\) has no complementary graph to go to. With two, an edge between \(V_1\) and \(V_2\) has an end in each. With three disjoint reservoirs, the two ends of an edge miss at least one of them.

**3.2.** If \(Q\) is the single edge \(xy\) and \(x'=y'\), the cycle is \(x\,y\,x'\). If \(x'\ne y'\), the cycle contains \(Q\), the two reserved edges and a routing path with at least one edge, so at least four edges.

**3.3.** Reserve \(m\) edges from every vertex outside \(V_i\) to \(m\) distinct representatives, with capacity \(\lceil4mr/(ph)\rceil\); the greedy argument needs \(ph/2\) to exceed the number of saturated vertices plus \(m-1\), which holds for large \(D\). The number of paths becomes at most \(mr/2\) per reservoir and the single edges at most \(3mr\), so the bound becomes \(\frac92mr\).

**3.4.** With \(\tau=D^{0.70}\), \(r^3/(\tau^2h)\) can be as large as \(D^{3.06-1.40-0.90}=D^{0.76}\), which exceeds \(\tau=D^{0.70}\). The comparison \(3\cdot1.02-2\theta-0.90<\theta\) requires \(\theta>0.72\).

## References

- [CFS] D. Conlon, J. Fox and B. Sudakov, *Cycle packing*, Random Structures & Algorithms 45 (2014), 608–626; arXiv:1310.0632. https://arxiv.org/abs/1310.0632
- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
