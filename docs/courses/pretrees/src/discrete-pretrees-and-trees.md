# Discrete pretrees and trees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The vertex set of a tree is a pretree in which every interval is finite: the interval between two vertices is the set of vertices of the path that joins them. A pretree with finite intervals is called *discrete*. This lesson shows how discrete pretrees and trees correspond.

- A discrete pretree in which every three points have a median is the vertex set of a tree, and of only one: the edges join the adjacent pairs (Theorem 2.1).
- Every discrete pretree is a set of vertices of a tree in which each further vertex is joined to at least three vertices, all of them points of the pretree (Theorem 3.2). For finite pretrees this is the theorem of the first lesson, [Betweenness and pretrees](betweenness-and-pretrees.md), and the proof is the same construction.
- The completion of a finite pretree is the vertex set of a finite tree (Proposition 4.1). The completion of an infinite discrete pretree need not be discrete: the integers are an example (Example 4.3).

The two theorems are Lemma 3.34 and Proposition 3.35 of [Bowditch]. The lesson uses the first lesson throughout, and in Section 4 the lessons [The completion of a pretree](the-completion-of-a-pretree.md) and [Adjacent points of the completion](adjacent-points-of-the-completion.md).

## 1. Discrete pretrees

**Definition 1.1.** A pretree is *discrete* if the interval \([x,y]\) is finite for all points \(x,y\).

Finite pretrees are discrete. A set with the empty relation is discrete: its intervals have at most two points. The integers with the betweenness of the line are discrete; the rational numbers and the real line are not. Every subset of a discrete pretree is discrete, because the interval between two points of the subset, formed in the subset, is contained in their interval in the whole pretree.

**Lemma 1.2** (finite intervals are chains). Let \(x\ne z\) be points of a pretree such that \([x,z]\) is finite. Then the points of \([x,z]\) can be listed as
\[
x=x_0,\ x_1,\ \dots,\ x_n=z
\]
without repetition, so that \(x_{i-1}\) and \(x_i\) are adjacent for all \(i\), and \(x_ax_bx_c\) holds whenever \(a<b<c\).

**Proof.** The set \(F=[x,z]\) is a finite pretree. It is full (Corollary 5.3 of the first lesson), so for \(u,v\in F\) the interval between \(u\) and \(v\) is the same in \(F\) and in the whole pretree; in particular \(F\) is the interval between \(x\) and \(z\) in the pretree \(F\), and two points of \(F\) are adjacent in \(F\) exactly when they are adjacent in the whole pretree. Now apply Lemma 4.2 of the first lesson to the finite pretree \(F\). \(\blacksquare\)

**Lemma 1.3.** A full subset of a median pretree is a median pretree.

**Proof.** Let \(X\) be full and \(x,y,z\in X\). Their median lies in \([x,y]\subseteq X\). Intervals between points of \(X\) are the same in \(X\) and in the whole pretree, so it is a median in \(X\). \(\blacksquare\)

## 2. Discrete median pretrees

**Theorem 2.1.**

1. The vertex set of a tree, with the betweenness of the tree, is a discrete median pretree. Two vertices are adjacent in this pretree exactly when they are joined by an edge.
2. Let \(S\) be a discrete median pretree, and let \(\tau\) be the graph with vertex set \(S\) in which two points are joined by an edge exactly when they are adjacent. Then \(\tau\) is a tree, and for \(x,y,z\in S\) the relation \(xyz\) holds if and only if \(y\) lies between \(x\) and \(z\) in \(\tau\).
3. A discrete median pretree is the vertex set of exactly one tree with this property, the tree \(\tau\) of (2).

**Proof.** (1) The vertex set is a pretree by Lemma 1.2 of the first lesson. For vertices \(x\ne z\), the interval \([x,z]\) of this pretree is the set \([x,z]_\tau\) of vertices of the path from \(x\) to \(z\), which is finite. Three vertices have a median by Lemma 6.1 of the first lesson. Two vertices are adjacent when the path between them has no inner vertex, that is, when it is an edge.

(2) *\(\tau\) is connected.* For \(x\ne z\) the list of Lemma 1.2 is a path of \(\tau\) from \(x\) to \(z\).

*\(\tau\) has no cycle.* Let \(x_0,\dots,x_{n-1}\), \(n\ge3\), be a cycle. By Lemma 4.3 of the first lesson any two of these points are adjacent. So
\[
\begin{gathered}
{[x_0,x_1]}\cap[x_1,x_2]\cap[x_2,x_0]\\
=\{x_0,x_1\}\cap\{x_1,x_2\}\cap\{x_2,x_0\},
\end{gathered}
\]
which is empty. But this set contains the median of \(x_0,x_1,x_2\).

*Betweenness.* Let \(x\ne z\). The list of Lemma 1.2 is a path from \(x\) to \(z\) in the tree \(\tau\), hence the path, and its set of vertices is \([x,z]\). So \([x,z]_\tau=[x,z]\), and \(y\) lies between \(x\) and \(z\) in \(\tau\) exactly when \(y\in(x,z)\).

(3) If \(S\) is the vertex set of a tree \(\tau'\) whose betweenness is that of \(S\), then by (1) the edges of \(\tau'\) are the adjacent pairs of \(S\). So \(\tau'=\tau\). \(\blacksquare\)

So "discrete median pretree" and "vertex set of a tree" are two descriptions of one structure. In particular, by Lemma 1.3, a full subset of a median pretree that is discrete as a pretree is the vertex set of a tree.

In a discrete median pretree no three points are pairwise adjacent, as the proof shows. So its cliques, in the sense of the first lesson, have at most two points.

## 3. Discrete pretrees in general

A discrete pretree need not be median: three points with the empty relation have no median. Such a pretree is a set of vertices of a tree with further vertices. The construction is that of Theorem 4.1 of the first lesson, and it adds a vertex for each maximal set of at least three pairwise adjacent points.

Recall that a *clique* is a set of points any two of which are adjacent, and that the union of two cliques with at least two common points is a clique (the first statement of Lemma 4.4 of the first lesson, which holds in every pretree). For adjacent points \(u,v\) of a pretree let \(K(u,v)\) be the union of all cliques that contain \(u\) and \(v\).

**Lemma 3.1.** \(K(u,v)\) is a clique. It is the only maximal clique that contains \(u\) and \(v\). Two different maximal cliques have at most one common point.

**Proof.** Two points of \(K(u,v)\) lie in cliques \(K\) and \(K'\) that both contain \(u\) and \(v\); they lie in the clique \(K\cup K'\), so they are equal or adjacent. A clique that contains \(u\) and \(v\) is contained in \(K(u,v)\), by the definition. So \(K(u,v)\) is a maximal clique, and a maximal clique containing \(u\) and \(v\) equals it. If two maximal cliques have common points \(u\ne v\), both are \(K(u,v)\). \(\blacksquare\)

**Theorem 3.2.** Let \(T\) be a discrete pretree. There is a tree \(\tau\) whose vertex set contains \(T\), such that for all \(x,y,z\in T\)
\[
\begin{gathered}
xyz\quad\Longleftrightarrow\\
y\text{ lies between }x\text{ and }z\text{ in }\tau ,
\end{gathered}
\]
and such that every vertex of \(\tau\) outside \(T\) is joined to at least three vertices, all of which are points of \(T\). If \(T\) is median, \(\tau\) has no vertex outside \(T\) and is the tree of Theorem 2.1.

**Proof.** *The tree.* Let \(\mathcal N\) be the set of maximal cliques of \(T\) with at least three points. The graph \(\tau\) has the vertex set \(T\sqcup\mathcal N\) and the following edges:

- an edge between \(x\in T\) and \(K\in\mathcal N\) whenever \(x\in K\);
- an edge between adjacent points \(x,y\in T\) whenever \(K(x,y)=\{x,y\}\).

For adjacent \(x,y\in T\) the *link* of \(x\) and \(y\) is the path \(x,y\) if \(K(x,y)=\{x,y\}\), and the path \(x,K(x,y),y\) otherwise. Two points of \(T\) that are joined in \(\tau\) by an edge, or by two edges through a vertex \(K\in\mathcal N\), are adjacent in \(T\), and that piece of \(\tau\) is their link; in the second case because \(K\) is a maximal clique containing both, so \(K=K(x,y)\) by Lemma 3.1.

*\(\tau\) is connected.* By Lemma 1.2 any two points of \(T\) are joined by a chain of adjacent points, hence by links; and every \(K\in\mathcal N\) is joined to its points.

*\(\tau\) has no cycle.* Suppose \(C\) is a cycle. No two vertices of \(\mathcal N\) are joined by an edge, so \(C\) contains points of \(T\), and the points of \(T\) on \(C\), in cyclic order \(x_0,\dots,x_{n-1}\), are such that consecutive ones are joined along \(C\) by their link. If \(n\le2\), then \(C\) would consist of one link, or of the same link traversed twice, and would not have three distinct vertices. So \(n\ge3\), and by Lemma 4.3 of the first lesson the set \(\{x_0,\dots,x_{n-1}\}\) is a clique. It is contained in \(K=K(x_0,x_1)\), which therefore has at least three points, and \(K=K(x_i,x_{i+1})\) for every \(i\) by Lemma 3.1. So every one of the \(n\ge3\) links passes through the vertex \(K\), and \(K\) occurs more than once on \(C\). This is impossible.

*Betweenness.* Let \(x\ne z\) in \(T\) and take the list \(x=x_0,\dots,x_n=z\) of \([x,z]\) from Lemma 1.2. Follow the links from \(x_0\) to \(x_1\), from \(x_1\) to \(x_2\), and so on. No vertex is visited twice: the \(x_i\) are distinct, and if the links of \(x_{i-1},x_i\) and of \(x_{j-1},x_j\), with \(i<j\), passed through the same \(K\in\mathcal N\), then \(x_{i-1}\) and \(x_j\) would be adjacent, as points of the clique \(K\), while \(x_{i-1}x_ix_j\) holds by Lemma 1.2. So the links form the path from \(x\) to \(z\) in \(\tau\), and the points of \(T\) on this path are exactly the points of \([x,z]\). Hence, for \(y\in T\), \(y\) lies between \(x\) and \(z\) in \(\tau\) if and only if \(y\in(x,z)\), that is, \(xyz\). For \(x=z\) neither holds.

*The added vertices.* A vertex \(K\in\mathcal N\) is joined exactly to the points of \(K\), of which there are at least three.

*The median case.* If \(T\) is median, no three points are pairwise adjacent (proof of Theorem 2.1). So \(\mathcal N\) is empty, \(K(x,y)=\{x,y\}\) for all adjacent \(x,y\), and the edges of \(\tau\) join the adjacent pairs. \(\blacksquare\)

The tree of Theorem 3.2 is determined by the pretree \(T\) alone. If \(T\) is given as a set of vertices of some tree \(\sigma\), with the betweenness of \(\sigma\), the tree \(\tau\) can be different from \(\sigma\) (Exercise 5.2).

## 4. Completions

Let \(\Phi(T)\) be the completion of a pretree \(T\): the set of its flows, with the betweenness defined in the lesson on the completion, in which \(T\) appears as the set \(\bar T\) of the flows towards its points.

**Proposition 4.1.** Let \(T\) be a finite pretree. Then \(\Phi(T)\) is the vertex set of a finite tree, with the betweenness of the tree. Every edge of this tree joins a point of \(\bar T\) to a point outside \(\bar T\).

**Proof.** A flow is a binary relation on \(T\), so \(\Phi(T)\) is finite. It is a median pretree (Theorems 3.1 and 4.1 of the lesson on the completion). By Theorem 2.1 it is the vertex set of the tree whose edges join the adjacent pairs, and of two adjacent points of \(\Phi(T)\) exactly one lies in \(\bar T\) (Theorem 2.3 of the lesson on adjacent points). \(\blacksquare\)

**Example 4.2** (the vertex set of a finite tree). Let \(T\) be the vertex set of a finite tree \(\sigma\). By Example 4.3 of the lesson on adjacent points, the points of \(\Phi(T)\) are the flows towards the vertices and the flows of the edges, and the flow of an edge is adjacent to the flows towards its two ends. So the tree of Proposition 4.1 is \(\sigma\) with every edge divided into two by a new vertex.

**Example 4.3** (the integers). Let \(T\) be the set of integers with the betweenness of the line; it is discrete. Let \(p\) be the relation with \(xy.p\) if and only if \(x<y\). It is a flow: (F1) is clear; if \(z\) lies between \(x\) and \(y\), then \(z\) is larger than the smaller of the two, which gives (F2); and if \(x<y\) and \(z\ne y\), then \(z<y\), so that \(zy.p\), or \(y<z\), so that \(xyz\), which gives (F3). It is not a flow towards a point: from every integer it runs to the next one, while the flow towards \(a\) runs nowhere from \(a\).

For every integer \(k\ge1\), the point \(\bar k\) lies between \(\bar 0\) and \(p\) in \(\Phi(T)\). By the definition of the betweenness of flows we must show that \(k\) lies between \(\bar 0\) and \(p\) in \(T\sqcup P\), that is: every \(y\ne k\) has \(yk.\bar 0\) or \(yk.p\). For \(y<k\) the second holds. For \(y>k\) the first holds, because \(k\) lies between \(y\) and \(0\).

So the interval between \(\bar 0\) and \(p\) in \(\Phi(T)\) is infinite: the completion of the discrete pretree of the integers is not discrete.

## 5. Exercises

**5.1.** Let \(T\) be a set with the empty relation. Describe the tree of Theorem 3.2.

**5.2.** Let \(\sigma\) be the tree with vertices \(a,b,c,d,u,v\) and edges \(au\), \(bu\), \(uv\), \(vc\), \(vd\), and let \(T=\{a,b,c,d\}\) with the betweenness of \(\sigma\). Determine the tree \(\tau\) of Theorem 3.2 and compare it with \(\sigma\).

**5.3.** Show that in a discrete median pretree the stars, in the sense of [Stars and the three kinds of flows](stars-and-the-three-kinds-of-flows.md), are exactly the pairs of adjacent points.

**5.4.** For points \(x,y\) of a discrete pretree let \(d(x,y)\) be the number of points of \([x,y]\) minus one. Show that
\[
d(x,z)\le d(x,y)+d(y,z),
\]
with equality if and only if \(y\in[x,z]\).

**5.5.** In Example 4.3, show that the flow \(p\) has no neighbour in \(\Phi(T)\).

## 6. Solutions

**5.1.** Any two distinct points are adjacent, so \(T\) is a clique. If \(T\) has at least three points, it is the only maximal clique, \(\mathcal N=\{T\}\), and \(\tau\) consists of a centre joined to every point of \(T\). If \(T\) has two points, \(\tau\) is one edge; if it has one point, \(\tau\) is one vertex; if \(T\) is empty, so is \(\tau\).

**5.2.** None of \(a,b,c,d\) lies on the path between two others: the paths pass through \(u\) and \(v\) only. So \(T\) has the empty relation, and by 5.1 the tree \(\tau\) has one added vertex joined to \(a,b,c,d\). It has five vertices, while \(\sigma\) has six: the tree \(\tau\) does not record that \(a,b\) branch off at a different vertex than \(c,d\). This information is not contained in the betweenness of the four points.

**5.3.** By Theorem 2.1 the pretree is the vertex set of a tree in which the edges join the adjacent pairs. By Example 2.2(c) of that lesson, the stars of the vertex set of a tree are the pairs of vertices joined by an edge.

**5.4.** By Lemma 3.1 of the first lesson, \([x,z]\subseteq[x,y]\cup[y,z]\), and \(y\) lies in both sets on the right. Counting points gives the inequality. Equality holds exactly when \([x,z]=[x,y]\cup[y,z]\) and \([x,y]\cap[y,z]=\{y\}\). If this holds, then \(y\in[x,z]\). Conversely, if \(y\in[x,z]\), both equalities hold: for \(y=x\) or \(y=z\) directly, and for \(y\in(x,z)\) by Lemma 3.2 of the first lesson.

**5.5.** From every integer \(x\) the flow runs to \(x+1\). So the set of points from which \(p\) runs nowhere is empty, and \(p\) is not a flow towards a point, since the flow towards \(a\) runs nowhere from \(a\). By Corollary 2.4(1) of the lesson on adjacent points, the neighbours of \(p\) are the flows towards the points from which \(p\) runs nowhere. There are none.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 3. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
