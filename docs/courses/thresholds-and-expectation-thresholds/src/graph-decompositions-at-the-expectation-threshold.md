# Graph decompositions at the expectation threshold

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By the theorem of Park and Pham, the containment threshold of a graph \(H\) in \(G(n,p)\) exceeds its integral expectation threshold \(q(H;n)\) by at most a factor of order \(\log e(H)\), and perfect matchings show that this logarithm is needed (Section 4 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md)). Ascoli, He, Park and Talagrand conjectured that the logarithm disappears if \(H\) may be cut into a bounded number of pieces, each of which only has to appear on its own [AHPT]. This lesson proves the conjecture, following OpenAI [OpenAI-GD]:

**Theorem 3.1** (OpenAI 2026; the Ascoli–He–Park–Talagrand conjecture). There are an absolute integer \(k\ge2\) and an absolute constant \(L\ge1\) such that for every \(n\ge2\) and every graph \(H\) on at most \(n\) vertices, the edge set of \(H\) is a disjoint union \(E(H)=E(H_1)\cup\dots\cup E(H_k)\) of edge sets of subgraphs with
\[
p_{\mathrm c}(H_i;n)\le L\,q(H;n)\qquad(1\le i\le k).
\]

The pieces may be empty and may share vertices; the partition depends only on \(H\) and \(n\), and each piece is embedded separately, so the embeddings need not agree on shared vertices. Allowing overlapping pieces gives an equivalent statement: assigning each edge to one piece that contains it cannot increase any threshold, by (1.1) of [Embedding sparse graphs in random graphs](embedding-sparse-graphs-in-random-graphs.md). Ascoli, He, Park and Talagrand proved the case of bounded degeneracy and further cases, and identified the edges between vertices of high and low degree as the main difficulty [AHPT].

We use the notation of [Embedding sparse graphs in random graphs](embedding-sparse-graphs-in-random-graphs.md): \(p_{\mathrm c}(J;n)\), \(q(J;n)\), \(V_+(J)\), degeneracy, the bound (1.2), Lemma 1.1, the parameter range (4.1) and Propositions 4.1, 5.1 and 6.1, with \(k_0=2^{75}\). The plan is as follows. Section 1 uses the discrete convexity theorem to place one copy of \(H\) inside a union of \(k_0\) typical graphs, which splits \(H\) into \(k_0\) pieces lying in typical graphs. If the degeneracy of \(H\) is large, Section 3 isolates a small set \(Y\) containing the vertices of high degree and splits further: edges across \(Y\) are handled by neighbourhood transfer, and the other edges by the embedding of graphs of small degeneracy. If the degeneracy is bounded, \(H\) splits into star forests.

## 1. A typical cover of one copy

**Corollary 1.1.** Let \(n\ge2\), let \(H\) have an edge and at most \(n\) vertices, and let \(q(H;n)<r<1\). If a family \(\mathcal D\) of graphs on \([n]\) satisfies \(\mu_r(\mathcal D)\ge1-\frac1{k_0}\), then some copy of \(H\) on \([n]\) has its edges in the union of \(k_0\) members of \(\mathcal D\).

**Proof.** Otherwise every edge set containing a copy of \(H\) lies outside all unions of \(k_0\) members of \(\mathcal D\), so \(\mathcal F_H\subseteq E_{k_0}(\mathcal D)\), in the notation of [The discrete convexity conjecture](the-discrete-convexity-conjecture.md), with ground set the edge set of \(K_n\). By Theorem 7.1 there, \(E_{k_0}(\mathcal D)\) has a cover of cost at most \(\frac12\) at density \(r\); it also covers \(\mathcal F_H\), so \(q(H;n)\ge r\), a contradiction. \(\square\)

## 2. Splitting by degeneracy

**Lemma 2.1** (degeneracy splitting; Ascoli, He, Park and Talagrand). For every integer \(m\ge1\), the edges of a graph of degeneracy \(d\) can be partitioned into \(m\) subgraphs of degeneracy at most \(\lceil d/m\rceil\).

**Proof.** Fix an order with at most \(d\) earlier neighbours at every vertex. At each vertex, split its edges to earlier neighbours into \(m\) groups of at most \(\lceil d/m\rceil\) edges, and put group \(j\) into subgraph \(j\). Every edge is assigned once, at its later endpoint, and in every subgraph the same order has at most \(\lceil d/m\rceil\) earlier neighbours at each vertex. \(\square\)

**Lemma 2.2.** A forest is the edge-disjoint union of two star forests.

**Proof.** Root each tree of the forest, and colour the edge between a vertex and its parent by the parity of the depth of the parent. In one colour class, every edge joins a vertex at a depth of the given parity to one of its children; each child has exactly one edge of this colour, the one to its parent, so the components of the colour class are stars centred at the parents. \(\square\)

A graph of degeneracy \(1\) is a forest: in an order with at most one earlier neighbour at each vertex, the last vertex of a cycle would have two.

## 3. The decomposition

**Proof of Theorem 3.1.** Let \(A=400\,\mathrm e^4\) and \(N_1,N_2,N_3\) be as in Propositions 4.1, 5.1 and 6.1 of [Embedding sparse graphs in random graphs](embedding-sparse-graphs-in-random-graphs.md). Fix
\[
M=B=1000,\qquad k=2k_0M(B+1)^2,
\]
and an absolute integer \(n_0\ge\max\{N_1,N_2,N_3\}\) such that for all \(n\ge n_0\)
\[
\frac{8\log n}{\log2}\sqrt n\le n^{2/3},\qquad n^{2/3}\le\frac n4,\qquad2\Bigl\lceil\frac nB\Bigr\rceil\le\frac n{100}.\tag{3.1}
\]
Let \(L=\max\{2A,64,n_0^2\}\). If \(H\) has no edge, take all pieces empty. Otherwise let \(q=q(H;n)>0\) and \(d=\operatorname{degen}(H)\ge1\).

*Trivial ranges.* If \(n<n_0\), Lemma 1.1 of [Embedding sparse graphs in random graphs](embedding-sparse-graphs-in-random-graphs.md) gives \(Lq\ge n_0^2/(n(n-1))\ge1\); if \(q\ge\frac1{2A}\), then \(Lq\ge2Aq\ge1\). In both cases put all edges into one piece, whose threshold is at most \(1\le Lq\), and leave the other pieces empty. From now on \(n\ge n_0\) and \(q<\frac1{2A}\).

*Large degeneracy, \(d\ge M\).* Let \(r=2q\) and \(s=\lceil2d/M\rceil\). By Lemma 1.1 there, \(n^{-2/d}\le r<\frac1A<\frac12\), so \(d<2\log n/\log2\); also \(s\le2d/M+1\le3d/M\) and \(r^s\ge n^{-2s/d}\ge n^{-6/M}\ge n^{-1/100}\), and \(s\le10\log n\). So \(r\) and \(s\) satisfy (4.1) there. Let \(\mathcal D=\mathcal D(n,r,s)\) be the family of Proposition 4.1 there. Since \(q<r<1\), Corollary 1.1 gives a copy of \(H\) and graphs \(G_1,\dots,G_{k_0}\in\mathcal D\) whose union contains it. Identify \(H\) with this copy, so \(V(H)\subseteq[n]\), and assign each edge of \(H\) to one \(G_i\) containing it. This gives \(k_0\) *initial pieces*, the \(i\)-th contained in \(G_i\).

Let \(Y_0=\{v:\deg_H(v)>\sqrt n\}\). By (1.2) there, \(|E(H)|\le dn\), so \(|Y_0|\le2dn/\sqrt n=2d\sqrt n\). Starting from \(Y_0\), add one at a time a vertex outside the current set with more than \(2d\) neighbours in it, until no such vertex remains, and call the final set \(Y\). If \(a\) vertices were added, each brought more than \(2d\) edges inside the set, so \(2da\le|E(H[Y])|\le d(|Y_0|+a)\) by (1.2), hence \(a\le|Y_0|\) and
\[
|Y|\le2|Y_0|\le4d\sqrt n\le\frac{8\log n}{\log2}\sqrt n\le n^{2/3}.
\]
Every \(w\notin Y\) has \(\deg_H(w)\le\sqrt n\) and \(|N_H(w)\cap Y|\le2d\). Partition \(V(H)\setminus Y\) into \(B\) blocks of at most \(\lceil n/B\rceil\) vertices. Split each initial piece \(P\) as follows.

- *Edges of \(P\) inside \(Y\).* Lemma 2.1 with \(m=M\) gives \(M\) graphs of degeneracy at most \(\lceil d/M\rceil\le s\), with at most \(|Y|\le n/4\) non-isolated vertices and maximum degree at most \(|Y|\le n^{2/3}\). By Proposition 5.1 there, each has threshold at most \(r\).
- *Edges of \(P\) outside \(Y\).* First split by the unordered pair of blocks containing the two endpoints (\(B(B+1)/2\) pairs, both endpoints in one block allowed), then apply Lemma 2.1 with \(m=M\). Each resulting graph has degeneracy at most \(s\), maximum degree at most \(\sqrt n\le n^{2/3}\) and at most \(2\lceil n/B\rceil\le n/100\) non-isolated vertices, so its threshold is at most \(r\) by Proposition 5.1.
- *Edges of \(P\) between \(Y\) and its complement.* First split by the block of the endpoint outside \(Y\). At each outside vertex \(w\), split its at most \(2d\) edges into \(Y\) into \(M\) groups of at most \(\lceil2d/M\rceil=s\) edges, and let piece \(j\) consist of the \(j\)-th groups. Each resulting graph is bipartite between \(Y\) and its complement, lies in \(G_i\in\mathcal D\), has at most \(\lceil n/B\rceil\le n/8\) outside vertices of positive degree, all of degree at most \(s\), and \(|Y|\le n^{2/3}\). By Proposition 4.1 there, its threshold is at most \(32r=64q\).

Every piece has threshold at most \(64q\le Lq\). Their number is at most \(k_0M\bigl(1+\frac{B(B+1)}2+B\bigr)=\frac{k_0M(B+1)(B+2)}2\le k\). The pieces are subgraphs of the copy of \(H\); transported back to \(H\) by the identification, they partition \(E(H)\).

*Bounded degeneracy, \(1\le d<M\).* Lemma 2.1 with \(m=d\) splits \(E(H)\) into \(d\) graphs of degeneracy at most \(1\), that is, forests, and Lemma 2.2 splits each forest into two star forests. Partition \(V(H)\) into \(B\) blocks of at most \(\lceil n/B\rceil\) vertices, and split each star forest by the unordered pair of blocks containing the endpoints of its edges. Each resulting piece \(J\) is a star forest with \(|V_+(J)|\le2\lceil n/B\rceil\le n/100\), so Proposition 6.1 there and (1.1) there give
\[
p_{\mathrm c}(J;n)\le2A\,q(J;n)\le2A\,q(H;n)\le Lq.
\]
There are at most \(2d\cdot B(B+1)/2\le k\) pieces.

In both cases add empty pieces to obtain exactly \(k\). All choices (the typical graphs, the copy of \(H\), the orders and the splittings) depend only on \(H\) and \(n\), not on the random graph used to test the thresholds of the pieces. \(\square\)

The constants \(k\) and \(L\) are absolute but not explicit, since \(N_1\), \(N_2\), \(N_3\) and \(n_0\) are given only by asymptotic estimates. The theorem compares each piece with the integral threshold \(q(H;n)\), which is at least \(p_{\mathrm E}(n,H)\) by Proposition 3.3 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md). For the whole graph, the ratio \(p_{\mathrm c}(n,H)/p_{\mathrm E}(n,H)\) can be of order \(\log n\), as it is for perfect matchings (Corollary 3.2 of [The second Kahn–Kalai conjecture](the-second-kahn-kalai-conjecture.md)).

## 4. Exercises

**Exercise 4.1** (easy). Apply the proof of Lemma 2.2 to the path \(v_0v_1v_2v_3v_4\), first rooted at \(v_0\) and then rooted at \(v_2\), and describe the two star forests in each case.

**Exercise 4.2** (easy). Show that the overlapping formulation implies the partition formulation: if \(E(H)=E(H_1')\cup\dots\cup E(H_k')\) with \(p_{\mathrm c}(H_i';n)\le Lq\), there is a partition into subgraphs \(H_i\subseteq H_i'\) with the same bounds.

**Exercise 4.3** (medium). In the large-degeneracy case, show that each piece of edges between \(Y\) and its complement has at most \(s\) edges at each outside vertex, and that the pieces obtained from one initial piece are pairwise edge-disjoint.

**Exercise 4.4** (medium). Show that in the construction of \(Y\), the inequality \(2da\le|E(H[Y])|\) holds even when \(Y_0=\varnothing\), and that the process stops after at most \(|Y_0|\) additions.

## 5. Solutions

**4.1.** Rooted at \(v_0\), the parent of \(v_{i+1}\) is \(v_i\), at depth \(i\); the edges \(v_0v_1\), \(v_2v_3\) get colour \(0\) and \(v_1v_2\), \(v_3v_4\) colour \(1\), so each star forest consists of two disjoint edges. Rooted at \(v_2\), the vertices \(v_1,v_3\) have depth \(1\) and \(v_0,v_4\) depth \(2\); the edges \(v_2v_1\), \(v_2v_3\) get colour \(0\) and form a star with centre \(v_2\) and two leaves, and \(v_1v_0\), \(v_3v_4\) get colour \(1\) and form two disjoint edges.

**4.2.** Assign each edge to the first \(H_i'\) containing it, and let \(H_i\) be the subgraph formed by the edges assigned to it. Then \(H_i\subseteq H_i'\) and \(p_{\mathrm c}(H_i;n)\le p_{\mathrm c}(H_i';n)\) by (1.1) of [Embedding sparse graphs in random graphs](embedding-sparse-graphs-in-random-graphs.md).

**4.3.** At an outside vertex \(w\), the edges of the initial piece into \(Y\) are at most \(|N_H(w)\cap Y|\le2d\), and the \(j\)-th group has at most \(\lceil2d/M\rceil=s\) of them. Each edge between \(Y\) and its complement has exactly one outside endpoint, so it lies in exactly one block class and exactly one group.

**4.4.** If \(a\) vertices are added, each has more than \(2d\) neighbours among the vertices present before it, all in \(Y\); counting each such edge at the added vertex counts distinct edges of \(H[Y]\), so \(|E(H[Y])|\ge2da\), also if \(Y_0=\varnothing\). Combined with \(|E(H[Y])|\le d(|Y_0|+a)\) this gives \(a\le|Y_0|\). If \(Y_0=\varnothing\), no vertex has a neighbour in the empty set, so nothing is added.

## References

- [OpenAI-GD] OpenAI, *Graph decompositions at the integral expectation threshold*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026
- [AHPT] R. Ascoli, X. He, J. Park and M. Talagrand, *A reformulation of the discrete convexity conjecture via k-thresholds*, 2026. https://arxiv.org/abs/2608.11183
