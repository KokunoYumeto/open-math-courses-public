# A block of the boundary

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The boundary \(B\) of the earlier lessons is a compact connected metric space of dimension at most one. If it has cut points, they form the vertices of a tree on which the group acts ([The tree of cut points](course:convergence-groups/the-tree-of-cut-points)). This lesson uses the tree to cut out of \(B\) a piece without cut points. Fix a vertex \(r\) of the tree that is not a cut point, let \(R\) be the set of cut points next to \(r\) in the tree, and \(L\) the closure of \(R\) in \(B\). The results:

- there is a graph on \(R\), connected and with finitely many orbits under the stabilizer of \(r\), whose edges join cut points at distance two in the tree (Proposition 2.1);
- two cut points close to a point of \(B\) are joined by a path of cut points close to that point (Proposition 3.1);
- there is a continuous retraction of \(B\) onto \(L\) that is locally constant outside \(L\); and \(L\) is a compact connected space with more than one point, without cut points, of dimension at most one, with vanishing first Čech cohomology if that of \(B\) vanishes (Theorem 4.1).

The space \(L\) is a *block* of \(B\). The lesson follows the first two parts of Section 7 of [OpenAI-S]. It uses the earlier lessons of this course and the lesson on the tree of cut points.

## 1. The setting

We keep the standing assumptions and the notation of [The compact space and its boundary](the-compact-space-and-its-boundary.md) and [The convergence action](the-convergence-action.md): \(\Gamma\) is a group with a finite generating set \(S\), and \(S'\) denotes the set of the elements of \(S\) and their inverses; \(G\) is the Cayley graph, in which the neighbours of \(g\) are the vertices \(gs\) with \(s\in S'\); \(X=\Gamma\cup B\) is the compact metric space with metric \(\rho\) in which the points of \(\Gamma\) are isolated and dense; and \(\Gamma\) acts on \(X\) by homeomorphisms. The boundary \(B\) is a compact connected space with more than one point, and \(\Gamma\) acts on it as a convergence group. A sequence \((g_n)\) in \(\Gamma\) *tends to infinity* if it leaves every finite subset of \(\Gamma\).

In this lesson we assume in addition:

- \(\Gamma\) has no element of finite order other than the identity; then every orbit in \(B\) is dense (Theorem 5.2 of the lesson on the convergence action), so the action on \(B\) is minimal;
- the set \(P\) of cut points of \(B\) is not empty;
- \(\Gamma\) satisfies the hypotheses (b) and (z) of the lesson on the tree of cut points, for its action on \(B\): it has the fixed-point property for trees with finite edge stabilizers, and it fixes a point of the dendrite quotient of \(B\).

Then Theorem 1.1 of that lesson applies, and we use its conclusions in the following form. We write the vertex \(\bar p\) of the tree simply as \(p\).

- (T1) There is a tree \(\mathcal T\) on which \(\Gamma\) acts. Its vertex set contains \(P\), with the action of \(\Gamma\) on \(P\). Every edge joins a point of \(P\) to a vertex outside \(P\), and a vertex outside \(P\) has at least two neighbours.
- (T2) \(\mathcal T\) has finitely many orbits of vertices, and the stabilizer of every edge is infinite.
- (T3) If \(a,b,q\in P\) and \(q\) separates \(a\) from \(b\) in \(B\), then \(q\) lies between \(a\) and \(b\) in \(\mathcal T\).
- (T4) Every \(p\in P\) is the fixed point of a parabolic element of \(\Gamma\).

By (T4) and the parabolic comparison (Theorem 4.2 of the lesson on the convergence action), for every \(p\in P\),
\[
\begin{gathered}
\rho(g,gp)\longrightarrow0\\
(g\to\infty\text{ in }\Gamma).
\end{gathered}\tag{1}
\]

Intervals of the tree are written \([u,v]_{\mathcal T}\); the points of such an interval, in their order from \(u\) to \(v\), form the path from \(u\) to \(v\), and they lie alternately in \(P\) and outside \(P\).

*The block.* Fix a vertex \(r\) of \(\mathcal T\) outside \(P\), and let
\[
\begin{gathered}
R=\{p\in P\mid p\text{ is adjacent to }r\},\\
H=\{g\in\Gamma\mid gr=r\},\qquad L=\overline R ,
\end{gathered}
\]
the closure taken in \(B\).

**Lemma 1.1.**

1. \(R\) has at least two points, and for \(a\ne b\) in \(R\) the interval \([a,b]_{\mathcal T}\) is \(\{a,r,b\}\).
2. No cut point of \(B\) separates two points of \(R\).
3. \(H\) is the set of all \(g\in\Gamma\) with \(gR=R\), and for \(p\in R\) the group \(H_p=\{h\in H\mid hp=p\}\) is infinite.

**Proof.** (1) By (T1), \(r\) has at least two neighbours, and they lie in \(P\). Let \(a\ne b\) be neighbours of \(r\). The median of \(a,b,r\) in the tree lies in \([a,r]_{\mathcal T}\cap[b,r]_{\mathcal T}=\{r\}\), so \(r\) lies between \(a\) and \(b\). A second point \(u\) between \(a\) and \(b\) would lie between \(a\) and \(r\) or between \(r\) and \(b\), because the points between \(a\) and \(b\) are linearly ordered; but \(r\) is adjacent to both.

(2) By (T3) such a cut point would lie between \(a\) and \(b\) in \(\mathcal T\); by (1) it would be \(r\), which is not in \(P\).

(3) An element that fixes \(r\) maps its neighbours to its neighbours. Conversely let \(gR=R\) and \(a\ne b\) in \(R\). Then \(g\) maps the only point between \(a\) and \(b\), which is \(r\), to the only point between \(ga\) and \(gb\), which is \(r\). The group \(H_p\) is the stabilizer of the edge \(\{r,p\}\), which is infinite by (T2). \(\blacksquare\)

## 2. A graph on the cut points

A *graph on a set \(V\)* is given by a set of *edges*, which are sets of two points of \(V\). A *path* is a finite sequence of points of \(V\) in which consecutive points form an edge. The graph is *connected* if any two points of \(V\) are joined by a path.

Let \(\pi\colon P\to R\) be the following map: for \(p\in P\), \(\pi(p)\) is the second point of the path from \(r\) to \(p\) in \(\mathcal T\). It is a neighbour of \(r\), so it lies in \(R\); and \(\pi(p)=p\) for \(p\in R\).

**Proposition 2.1.** There is a graph \(K^*\) on \(P\) with the following properties.

1. \(K^*\) is connected, \(\Gamma\) maps edges to edges, and there are finitely many orbits of edges.
2. The two ends of every edge of \(K^*\) have a common neighbour in \(\mathcal T\).
3. Let \(\{a,b\}\) be an edge of \(K^*\). If the common neighbour of \(a\) and \(b\) is \(r\), then \(a,b\in R\). Otherwise \(\pi(a)=\pi(b)\).
4. Let \(K\) be the graph on \(R\) whose edges are the edges of \(K^*\) with both ends in \(R\). Then \(K\) is connected, \(H\) maps its edges to edges, and there are finitely many orbits under \(H\) of edges and of vertices of \(K\).

**Proof.** *A first graph.* By (T2) there are finitely many orbits of \(\Gamma\) in \(P\); choose one point in each, \(p_0,p_1,\dots,p_k\). Let \(K_0\) be the graph on \(P\) whose edges are the translates \(g\{p_0,sp_0\}\), for \(s\in S'\) with \(sp_0\ne p_0\), and \(g\{p_0,p_i\}\), for \(1\le i\le k\), with \(g\in\Gamma\). It has finitely many orbits of edges. It is connected: for \(g=s_1\cdots s_m\) with \(s_j\in S'\), the points \(p_0,\ s_1p_0,\ s_1s_2p_0,\ \dots,\ gp_0\) are such that consecutive ones are equal or form an edge; and \(gp_i\) forms an edge with \(gp_0\).

*The graph \(K^*\).* For an edge \(\{a,b\}\) of \(K_0\), the path from \(a\) to \(b\) in \(\mathcal T\) is \(a=x_0,x_1,\dots,x_{2m}=b\), where the points with even index lie in \(P\) and the others do not. Let the edges of \(K^*\) be all the pairs \(\{x_{2i},x_{2i+2}\}\) obtained in this way. Each of them has the common neighbour \(x_{2i+1}\). The construction commutes with the action of \(\Gamma\), each edge of \(K_0\) is replaced by a path of \(K^*\) with the same ends, and each orbit of edges of \(K_0\) gives finitely many orbits of edges of \(K^*\). This proves (1) and (2).

(3) Let \(s\) be the common neighbour of \(a\) and \(b\); it is not in \(P\), and \([a,b]_{\mathcal T}=\{a,s,b\}\) as in Lemma 1.1. If \(s=r\), then \(a,b\in R\). Let \(s\ne r\). Then \(r\notin[a,b]_{\mathcal T}\). The median \(m\) of \(r,a,b\) lies in \([a,b]_{\mathcal T}\), so \(m\ne r\). It lies in \([r,a]_{\mathcal T}\) and in \([r,b]_{\mathcal T}\), so the paths from \(r\) to \(a\) and from \(r\) to \(b\) both begin with the path from \(r\) to \(m\), which has at least two points. So they have the same second point: \(\pi(a)=\pi(b)\).

(4) *Connected.* Let \(a,b\in R\) and \(a=v_0,v_1,\dots,v_n=b\) a path in \(K^*\). By (3), consecutive points of the sequence \(\pi(v_0),\dots,\pi(v_n)\) are equal, or they are \(v_{i-1},v_i\) themselves and form an edge of \(K\). Removing repetitions gives a path in \(K\) from \(\pi(a)=a\) to \(\pi(b)=b\).

*Orbits.* By Lemma 1.1(3), \(H\) maps \(R\) to itself, hence edges of \(K\) to edges of \(K\). If \(g\in\Gamma\) maps an edge of \(K\) to an edge of \(K\), it maps the common neighbour of the ends to the common neighbour of the ends; both are \(r\) by Lemma 1.1(1), so \(g\in H\). Hence every orbit of \(\Gamma\) on the edges of \(K^*\) contains at most one orbit of \(H\) on the edges of \(K\), and there are finitely many of these. Since \(K\) is connected and \(R\) has at least two points, every point of \(R\) lies on an edge of \(K\); so there are finitely many orbits of vertices too. \(\blacksquare\)

For a path \(v_0,\dots,v_n\) in \(K^*\), the *projected path* is the sequence \(\pi(v_0),\dots,\pi(v_n)\) with repetitions of consecutive equal points removed. By the proof of (4) it is a path in \(K\) or a single point.

**Lemma 2.2.** Let \(v_0,\dots,v_n\) be a path in \(K^*\) with \(\pi(v_0)\ne\pi(v_n)\). Then every point of the projected path is one of the points \(v_0,\dots,v_n\).

**Proof.** The projected path has at least two points, so each of its points is an end of a pair \(\pi(v_{i-1})\ne\pi(v_i)\). By Proposition 2.1(3), for such a pair \(v_{i-1},v_i\in R\), so \(\pi(v_{i-1})=v_{i-1}\) and \(\pi(v_i)=v_i\). \(\blacksquare\)

## 3. Paths of cut points near a point

**Proposition 3.1.** Let \(a_n,b_n\in P\) be two sequences that converge in \(B\) to the same point \(x\). Then there are paths in \(K^*\) from \(a_n\) to \(b_n\) such that the largest distance from \(x\) to a point of the \(n\)-th path tends to \(0\).

**Proof.** *Group elements.* Write \(a_n=g_np_{i_n}\) and \(b_n=h_np_{j_n}\) with the points \(p_0,\dots,p_k\) of the proof of Proposition 2.1. The stabilizer of each \(p_i\) is infinite, by (T4), so there are infinitely many possible choices of \(g_n\) and of \(h_n\) for each \(n\), and we can choose them so that \((g_n)\) and \((h_n)\) tend to infinity. By (1), applied to the finitely many points \(p_i\), \(\rho(g_n,a_n)\to0\) and \(\rho(h_n,b_n)\to0\). So \(g_n\to x\) and \(h_n\to x\) in \(X\).

*Paths in the Cayley graph.* By Corollary 6.3 of the lesson on the compact space, there are paths in \(G\) from \(g_n\) to \(h_n\) such that the largest distance from \(x\) to a vertex of the \(n\)-th path tends to \(0\).

*Transfer.* Fix for every \(s\in S'\) a path in \(K^*\) from \(p_0\) to \(sp_0\), and for every \(i\) a path in \(K^*\) from \(p_0\) to \(p_i\). Let \(Q\) be the finite set of all points of these paths. A step from \(g\) to \(gs\) in the Cayley graph is replaced by the translate by \(g\) of the path from \(p_0\) to \(sp_0\), which leads from \(gp_0\) to \(gsp_0\). At the two ends we add the translate by \(g_n\) of the path between \(p_{i_n}\) and \(p_0\), and the translate by \(h_n\) of the path between \(p_0\) and \(p_{j_n}\). The result is a path in \(K^*\) from \(a_n\) to \(b_n\), and each of its points has the form \(gt\) with \(g\) a vertex of the \(n\)-th Cayley path and \(t\in Q\).

*Estimate.* Let \(\varepsilon>0\). By (1) there is a finite set \(A\subseteq\Gamma\) such that \(\rho(g,gt)<\varepsilon\) for all \(t\in Q\) and all \(g\notin A\). The points of \(A\) have positive distance from \(x\in B\). So for large \(n\) the vertices \(g\) of the \(n\)-th Cayley path are outside \(A\) and satisfy \(\rho(g,x)<\varepsilon\); then \(\rho(gt,x)<2\varepsilon\) for all points \(gt\) of the \(n\)-th path in \(K^*\). \(\blacksquare\)

## 4. The retraction

**Theorem 4.1.** Under the assumptions of Section 1:

1. There is a continuous map \(\mathfrak r\colon B\to L\) with \(\mathfrak r(x)=x\) for \(x\in L\) and \(\mathfrak r(p)=\pi(p)\) for \(p\in P\). Every point of \(B\setminus L\) has a neighbourhood on which \(\mathfrak r\) is constant.
2. \(L\) is a compact connected space with more than one point, and \(L\) has no cut point.
3. \(\dim L\le1\). If \(\check H^1(B;k)=0\) for an abelian group \(k\), then \(\check H^1(L;k)=0\).

**Proof.** The set \(P\) is not empty and mapped to itself by \(\Gamma\); since all orbits are dense, \(P\) is dense in \(B\).

*Step 1: near a point outside \(L\).* Let \(x\in B\setminus L\). We show that there is a neighbourhood \(V\) of \(x\) in \(B\) such that \(\pi\) is constant on \(P\cap V\). Choose a neighbourhood \(O\) of \(x\) disjoint from the closed set \(L\). If there were no such \(V\), there would be \(a_n,b_n\in P\) tending to \(x\) with \(\pi(a_n)\ne\pi(b_n)\). Join them by the paths of Proposition 3.1; for large \(n\) all points of the path lie in \(O\). By Lemma 2.2 the points of the projected path are points of the path, so they lie in \(O\); but they lie in \(R\subseteq L\).

*Step 2: near a point of \(L\).* Let \(x\in L\) and \(a_n\in P\) with \(a_n\to x\). We show \(\pi(a_n)\to x\). Choose \(b_n\in R\) with \(b_n\to x\), and join \(a_n\) to \(b_n\) by the paths of Proposition 3.1. If \(\pi(a_n)\ne b_n=\pi(b_n)\), then \(\pi(a_n)\) is a point of the \(n\)-th path, by Lemma 2.2. If \(\pi(a_n)=b_n\), it is the point \(b_n\). In both cases its distance from \(x\) tends to \(0\).

*Step 3: the map.* Let \(Z\subseteq B\times L\) be the closure of the set of pairs \((p,\pi(p))\), \(p\in P\). It is compact. Every \(x\in B\) is the first coordinate of a point of \(Z\): take \(p_n\in P\) with \(p_n\to x\) and a convergent subsequence of \((\pi(p_n))\) in the compact space \(L\). And only of one: if \((x,y)\in Z\), there are \(p_n\to x\) with \(\pi(p_n)\to y\); for \(x\notin L\), Step 1 shows that \(\pi(p_n)\) is, for large \(n\), the constant value of \(\pi\) on \(P\cap V\); for \(x\in L\), Step 2 shows \(y=x\). So \(Z\) is the graph of a map \(\mathfrak r\colon B\to L\). The projection of \(Z\) to \(B\) is a continuous bijection of a compact space onto a Hausdorff space, hence a homeomorphism; so \(\mathfrak r\), the composition of its inverse with the projection to \(L\), is continuous. By construction \(\mathfrak r(p)=\pi(p)\) for \(p\in P\), \(\mathfrak r(x)=x\) for \(x\in L\), and \(\mathfrak r\) is constant on the neighbourhood \(V\) of Step 1, which we may take open.

*Step 4: properties of \(L\).* \(L=\mathfrak r(B)\) is compact and connected, and it contains \(R\), which has two points.

A closed subset \(A\) of a compact metric space \(Z'\) with \(\dim Z'\le n\) has \(\dim A\le n\): a finite cover of \(A\) by sets open in \(A\) is the trace of a family of open subsets of \(Z'\), which together with \(Z'\setminus A\) covers \(Z'\); an open refinement of this cover in which every point lies in at most \(n+1\) sets (Definition 2.1 of [Covering dimension and finite trivializing covers](course:index-theory-of-elliptic-operators/covering-dimension-and-finite-trivializing-covers#2-covering-dimension)) has as its trace on \(A\) a refinement of the given cover with the same property. Since \(\dim B\le1\) ([Dimension and cohomology of the boundary](dimension-and-cohomology-of-the-boundary.md), Theorem 2.3), \(\dim L\le1\).

If \(\check H^1(B;k)=0\), then \(\check H^1(L;k)=0\), because \(L\) is a retract of \(B\) (Corollary 4.4 of [First Čech cohomology of a compact metric space](course:continua-arcs-and-cut-points/first-cech-cohomology-of-a-compact-metric-space)).

*Step 5: \(L\) has no cut point.* Suppose \(q\in L\) and \(L\setminus\{q\}=U\cup V\) with \(U,V\) disjoint, nonempty and open in \(L\). Since \(R\) is dense in \(L\), there are \(a\in R\cap U\) and \(b\in R\cap V\). Let
\[
F=\mathfrak r^{-1}(q)\setminus\{q\}.
\]
It is closed in \(B\setminus\{q\}\). It lies in \(B\setminus L\), because \(\mathfrak r\) is the identity on \(L\); there \(\mathfrak r\) is locally constant, so \(F\) is open. The sets \(\mathfrak r^{-1}(U)\) and \(\mathfrak r^{-1}(V)\) are open in \(B\). So
\[
\begin{gathered}
B\setminus\{q\}=\bigl(\mathfrak r^{-1}(U)\cup F\bigr)\\
\cup\ \mathfrak r^{-1}(V)
\end{gathered}
\]
is a decomposition into two disjoint nonempty open sets, with \(a\) in the first and \(b\) in the second. So \(q\) is a cut point of \(B\) that separates two points of \(R\), against Lemma 1.1(2). \(\blacksquare\)

## 5. Exercises

**5.1.** Show that \(\pi(gp)=g\pi(p)\) for \(g\in H\) and \(p\in P\), and that \(\mathfrak r(hx)=h\mathfrak r(x)\) for \(h\in H\) and \(x\in B\).

**5.2.** Show that \(R\) is infinite and that \(L\) has no isolated point.

**5.3.** In Step 1 of the proof of Theorem 4.1, where is it used that the paths of Proposition 3.1 consist of cut points, and not of arbitrary points of \(B\)?

**5.4.** Show that for \(x\in B\setminus L\) the point \(\mathfrak r(x)\) lies in \(R\).

## 6. Solutions

**5.1.** An element \(g\in H\) fixes \(r\) and maps the path from \(r\) to \(p\) to the path from \(r\) to \(gp\); so it maps the second point to the second point. For the second statement, both sides are continuous in \(x\) and agree on the dense set \(P\); note that \(hL=L\) because \(hR=R\).

**5.2.** For \(p\in R\) the infinite group \(H_p\) acts on \(R\). If \(R\) were finite, a subgroup of finite index in \(H_p\), still infinite, would fix a second point \(p'\in R\). An element \(h\ne1\) of it has infinite order and fixes the cut points \(p\) and \(p'\); it is not loxodromic, by Theorem 1.1(1) of the lesson on the tree of cut points, and a parabolic element has only one fixed point. So \(R\) is infinite. A compact connected metric space with more than one point has no isolated point: an isolated point would be an open and closed subset.

**5.3.** In the use of Lemma 2.2: the projected path is formed with \(\pi\), which is defined on \(P\) through the tree, and the statement that its points are points of the original path rests on Proposition 2.1(3).

**5.4.** Let \(V\) be an open neighbourhood of \(x\) on which \(\mathfrak r\) is constant. It contains a point \(p\in P\), because \(P\) is dense. So \(\mathfrak r(x)=\mathfrak r(p)=\pi(p)\in R\).

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
