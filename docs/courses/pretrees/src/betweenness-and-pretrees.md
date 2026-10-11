# Betweenness and pretrees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a tree, a vertex \(y\) *lies between* two vertices \(x\) and \(z\) if the path from \(x\) to \(z\) passes through \(y\). A *pretree* is a set with a ternary relation that satisfies four simple properties of this relation, and nothing else: no vertices, edges, metric or topology are given. Pretrees describe sets that are arranged like a tree without being one. The main example in view is the set of cut points of a continuum, where "\(y\) lies between \(x\) and \(z\)" means that \(y\) separates \(x\) from \(z\); that example is the subject of later lessons, and it is how pretrees enter OpenAI's proof of the Singer conjecture in dimension four outside the middle degree.

This lesson develops the first properties, following Section 2 of Bowditch's memoir [Bowditch].

- The axioms and their immediate consequences for four points (Section 2).
- Intervals, and the fact that an interval is covered by the intervals along any chain from one end to the other (Lemma 3.1).
- The main result: every *finite* pretree is a set of vertices of a finite tree, with the betweenness of the tree (Theorem 4.1). The tree is constructed explicitly. So every statement about finitely many points of a pretree can be checked in a finite tree.
- Three applications of this principle: a set of points that are pairwise comparable in the sense of betweenness can be ordered in exactly two ways (Proposition 5.2); intervals are ordered (Corollary 5.3); and three points have at most one median (Proposition 6.2).

We assume only the notions of graph, path, cycle and connected graph.

## 1. Betweenness in a tree

A *graph* has a set of vertices and a set of edges, each edge joining two different vertices; at most one edge joins two given vertices. A *path* from \(x\) to \(z\) is a sequence of distinct vertices \(x=v_0,v_1,\dots,v_n=z\) in which consecutive vertices are joined by edges. A *cycle* is a sequence of \(n\ge3\) distinct vertices \(v_0,\dots,v_{n-1}\) such that \(v_i\) is joined to \(v_{i+1}\) for all \(i\), with \(v_n=v_0\). A *tree* is a connected graph without cycles.

**Lemma 1.1.** In a tree \(\tau\) any two vertices \(x,z\) are joined by exactly one path. Write \([x,z]_\tau\) for its set of vertices. Then, for vertices \(x,y,z\):

1. \([x,z]_\tau\subseteq[x,y]_\tau\cup[y,z]_\tau\);
2. if \(y\in[x,z]_\tau\), then \([x,z]_\tau=[x,y]_\tau\cup[y,z]_\tau\) and \([x,y]_\tau\cap[y,z]_\tau=\{y\}\).

**Proof.** A path exists because \(\tau\) is connected. Suppose \(P\) and \(Q\) are two different paths from \(x\) to \(z\). Let \(u\) be the last vertex up to which they agree, and let \(v\) be the first vertex of \(P\) after \(u\) that lies on \(Q\); it exists because \(z\) is such a vertex. The part of \(P\) from \(u\) to \(v\) and the part of \(Q\) between \(u\) and \(v\) are paths that have only \(u\) and \(v\) in common, and they are not both the single edge \(uv\), because \(P\) and \(Q\) leave \(u\) by different edges. Together they form a cycle, which is impossible.

(1) Following the path from \(x\) to \(y\) and then the path from \(y\) to \(z\) gives a sequence of vertices from \(x\) to \(z\) with consecutive ones joined by edges. Removing the part between two occurrences of a repeated vertex, as often as needed, leaves a path from \(x\) to \(z\), which is the path. (2) The parts of the path from \(x\) to \(z\) before and after \(y\) are paths from \(x\) to \(y\) and from \(y\) to \(z\). \(\blacksquare\)

For vertices \(x,y,z\) of a tree we say that \(y\) *lies between* \(x\) and \(z\) if \(y\in[x,z]_\tau\), \(y\ne x\) and \(y\ne z\).

**Lemma 1.2.** For vertices \(x,y,z,w\) of a tree:

- (T0) \(y\) does not lie between \(x\) and \(x\);
- (T1) if \(y\) lies between \(x\) and \(z\), it lies between \(z\) and \(x\);
- (T2) if \(y\) lies between \(x\) and \(z\), then \(z\) does not lie between \(x\) and \(y\);
- (T3) if \(z\) lies between \(x\) and \(y\), and \(w\ne z\), then \(z\) lies between \(x\) and \(w\) or between \(y\) and \(w\).

**Proof.** (T0) and (T1) are clear. (T2): if \(y\) lies between \(x\) and \(z\), then \([x,y]_\tau\) is the part of the path from \(x\) to \(z\) up to \(y\), which does not contain the last vertex \(z\). (T3): we have \(z\ne x\), \(z\ne y\) and \(z\ne w\). If \(z\) lay neither between \(x\) and \(w\) nor between \(y\) and \(w\), then \(z\notin[x,w]_\tau\cup[w,y]_\tau\). This union contains \([x,y]_\tau\) by Lemma 1.1(1), and \(z\in[x,y]_\tau\): a contradiction. \(\blacksquare\)

## 2. Pretrees

**Definition 2.1.** A *pretree* is a set \(T\) with a ternary relation, written \(xyz\) and read "\(y\) lies between \(x\) and \(z\)", such that for all \(x,y,z,w\in T\):

- (T0) \(xyx\) does not hold;
- (T1) \(xyz\) implies \(zyx\);
- (T2) \(xyz\) and \(xzy\) do not both hold;
- (T3) if \(xzy\) and \(w\ne z\), then \(xzw\) or \(yzw\).

By Lemma 1.2 the vertex set of a tree is a pretree. Every subset of a pretree is a pretree with the restricted relation, because the axioms speak about all points. The real line with the relation "\(x<y<z\) or \(z<y<x\)" is a pretree (Exercise 7.1). A set with the empty relation is a pretree.

**Lemma 2.2.** If \(xyz\), then \(x,y,z\) are distinct.

**Proof.** \(x\ne z\) by (T0). Axiom (T2) with equal second and third points says that \(xyy\) never holds, and then (T1) says that \(yyx\) never holds. So \(y\ne z\) and \(y\ne x\). \(\blacksquare\)

For four points we write \(xyzw\) if all four relations \(xyz\), \(yzw\), \(xyw\), \(xzw\) hold: the points lie "in a row".

**Lemma 2.3.** Let \(x,y,z,w\) be points of a pretree.

1. If \(xyz\) and \(yzw\), then \(xyzw\).
2. If \(xyw\) and \(yzw\), then \(xyzw\).
3. If \(xyw\), \(xzw\) and \(y\ne z\), then \(xyzw\) or \(xzyw\).

**Proof.** (1) We must show \(xyw\) and \(xzw\). From \(yzw\) we get \(wzy\), so \(wyz\) fails by (T2), and so \(zyw\) fails. Apply (T3) to \(xyz\) and the point \(w\ne y\): \(xyw\) or \(zyw\). Hence \(xyw\). In the same way, from \(xyz\) the relation \(xzy\) fails, so \(yzx\) fails; (T3) applied to \(wzy\) and the point \(x\ne z\) gives \(wzx\) or \(yzx\), hence \(wzx\), that is \(xzw\).

(2) By (1) it suffices to show \(xyz\). First \(z\ne y\) because \(yzw\). Apply (T3) to \(xyw\) and \(z\): \(xyz\) or \(wyz\). But \(wzy\) holds, so \(wyz\) fails by (T2). Hence \(xyz\).

(3) Apply (T3) to \(xzw\) and the point \(y\ne z\): \(xzy\) or \(wzy\). If \(wzy\), that is \(yzw\), then (2) applied to \(xyw\) and \(yzw\) gives \(xyzw\). If \(xzy\), that is \(yzx\), then (2) applied to \(wyx\) and \(yzx\) gives \(wyzx\), which by (T1) is \(xzyw\). \(\blacksquare\)

## 3. Intervals

Let \(T\) be a pretree. For \(x\ne y\) put
\[
\begin{gathered}
(x,y)=\{z\in T:\ xzy\},\\
[x,y]=(x,y)\cup\{x,y\},
\end{gathered}
\]
and \([x,y)=(x,y)\cup\{x\}\), \((x,y]=(x,y)\cup\{y\}\). Also \((x,x)=\varnothing\) and \([x,x]=\{x\}\). These sets are the open, closed and half-open *intervals*. By (T1), \([x,y]=[y,x]\). Two distinct points \(x,y\) are *adjacent* if \((x,y)=\varnothing\).

**Lemma 3.1.** For points \(x_0,x_1,\dots,x_n\) of a pretree,
\[
[x_0,x_n]\subseteq\bigcup_{i=1}^n[x_{i-1},x_i].
\]

**Proof.** For \(n=2\): let \(c\in[x_0,x_2]\). If \(c\) is \(x_0\), \(x_1\) or \(x_2\), there is nothing to show. Otherwise \(x_0cx_2\), and (T3) with the point \(x_1\ne c\) gives \(x_0cx_1\) or \(x_2cx_1\). The general case follows by induction, from \([x_0,x_n]\subseteq[x_0,x_{n-1}]\cup[x_{n-1},x_n]\). \(\blacksquare\)

**Lemma 3.2.** Let \(z\in(x,y)\). Then \([x,y]=[x,z]\cup[z,y]\) and \([x,z]\cap[z,y]=\{z\}\). In particular \((x,z)\) and \((z,y)\) are subsets of \((x,y)\) that do not contain \(z\).

**Proof.** If \(c\in(x,z)\), then \(yzx\) and \(zcx\) give \(yzcx\) by Lemma 2.3(2), that is, \(xczy\); so \(c\in(x,y)\) and \(czy\). Similarly \((z,y)\subseteq(x,y)\). With Lemma 3.1 this gives the first equality. For the second: a point \(c\in(x,z)\) has \(czy\), that is \(yzc\), so \(ycz\) fails by (T2), and \(c\notin(z,y)\); it is not \(y\) because \(c\in(x,y)\). The point \(x\) is not in \([z,y]\): it is not \(z\) or \(y\), and \(zxy\) would contradict \(yzx\) by (T2). Likewise \(y\notin[x,z]\). \(\blacksquare\)

## 4. Finite pretrees are sets of vertices of finite trees

**Theorem 4.1.** Let \(F\) be a finite pretree. There is a finite tree \(\tau\) whose vertex set contains \(F\) such that for all \(x,y,z\in F\):
\[
\begin{gathered}
xyz\quad\Longleftrightarrow\\
y\text{ lies between }x\text{ and }z\text{ in }\tau .
\end{gathered}
\]

The proof constructs \(\tau\) from the adjacency of points of \(F\). It takes four steps.

**Lemma 4.2** (intervals are chains). Let \(x\ne z\) be points of a finite pretree \(F\). The points of \([x,z]\) can be listed as \(x=x_0,x_1,\dots,x_n=z\), without repetition, so that \(x_{i-1}\) and \(x_i\) are adjacent for all \(i\). For every such list, \(x_ax_bx_c\) holds whenever \(a<b<c\).

**Proof.** *Existence*, by induction on the number of points of \((x,z)\). If \((x,z)\) is empty, the list is \(x,z\). Otherwise choose \(y\in(x,z)\). By Lemma 3.2 the sets \((x,y)\) and \((y,z)\) have fewer points than \((x,z)\), so \([x,y]\) and \([y,z]\) have such lists; and since \([x,y]\cap[y,z]=\{y\}\) and \([x,y]\cup[y,z]=[x,z]\), putting the two lists together gives a list for \([x,z]\).

*Order.* Let \(a<b<c\). Since consecutive points are adjacent, Lemma 3.1 gives \([x_0,x_a]\subseteq\{x_0,\dots,x_a\}\) and \([x_c,x_n]\subseteq\{x_c,\dots,x_n\}\); neither set contains \(x_b\). Now \(x_b\in[x,z]\) is not \(x\) or \(z\), so \(xx_bz\). By (T3) with the point \(x_a\), \(xx_bx_a\) or \(zx_bx_a\); the first is impossible because \(x_b\notin[x_0,x_a]\). So \(x_ax_bz\). By (T3) with the point \(x_c\), \(x_ax_bx_c\) or \(zx_bx_c\); the second is impossible because \(x_b\notin[x_c,x_n]\). \(\blacksquare\)

**Lemma 4.3** (cycles of adjacent points). Let \(x_0,x_1,\dots,x_{n-1}\), \(n\ge3\), be distinct points of a pretree such that \(x_i\) is adjacent to \(x_{i+1}\) for all \(i\), where \(x_n=x_0\). Then any two of the points are adjacent.

**Proof.** Let \(i<j\). By Lemma 3.1 along \(x_i,x_{i+1},\dots,x_j\), the interval \([x_i,x_j]\) lies in \(\{x_i,\dots,x_j\}\). By Lemma 3.1 along \(x_j,x_{j+1},\dots,x_{n-1},x_0,\dots,x_i\), it lies in \(\{x_j,\dots,x_{n-1},x_0,\dots,x_i\}\). The two sets have only \(x_i\) and \(x_j\) in common. \(\blacksquare\)

Call a subset \(K\) of a pretree a *clique* if any two distinct points of \(K\) are adjacent.

**Lemma 4.4.** If \(K\) and \(K'\) are cliques with at least two common points, then \(K\cup K'\) is a clique. Consequently, in a finite pretree every pair of adjacent points \(u,v\) lies in exactly one maximal clique \(K(u,v)\), and two different maximal cliques have at most one common point.

**Proof.** Let \(u\ne v\) be common points, \(a\in K\setminus K'\) and \(b\in K'\setminus K\). The four points \(a,u,b,v\) are distinct and each is adjacent to the next, cyclically. By Lemma 4.3, \(a\) and \(b\) are adjacent. For the consequence: if two maximal cliques both contain \(u\) and \(v\), their union is a clique, so they are equal. \(\blacksquare\)

**Proof of Theorem 4.1.** *The tree.* Let \(\mathcal N\) be the set of maximal cliques of \(F\) with at least three points. The graph \(\tau\) has the vertex set \(F\sqcup\mathcal N\) and the following edges:

- an edge between \(x\in F\) and \(K\in\mathcal N\) whenever \(x\in K\);
- an edge between adjacent points \(x,y\in F\) whenever \(K(x,y)=\{x,y\}\).

For adjacent \(x,y\in F\) the *link* of \(x\) and \(y\) is the path \(x,y\) if \(K(x,y)=\{x,y\}\), and the path \(x,K(x,y),y\) otherwise. Two points of \(F\) that are joined in \(\tau\) by an edge, or by two edges through a vertex \(K\in\mathcal N\), are adjacent in \(F\), and that piece of \(\tau\) is their link; in the second case because \(K\) is a maximal clique containing both, so \(K=K(x,y)\).

*\(\tau\) is connected.* By Lemma 4.2 any two points of \(F\) are joined by a chain of adjacent points, hence by links; and every \(K\in\mathcal N\) is joined to its points.

*\(\tau\) has no cycle.* Suppose \(C\) is a cycle. No two vertices of \(\mathcal N\) are joined by an edge, so the vertices of \(C\) in \(F\), in cyclic order \(x_0,\dots,x_{n-1}\), are such that consecutive ones are joined along \(C\) by their link. If \(n\le2\), then \(C\) would consist of one link, or of the same link traversed twice, and would not have three distinct vertices. So \(n\ge3\), and by Lemma 4.3 the set \(\{x_0,\dots,x_{n-1}\}\) is a clique. It lies in a maximal clique \(K\), which has at least three points, and \(K=K(x_i,x_{i+1})\) for every \(i\) by Lemma 4.4. So every one of the \(n\ge3\) links passes through the vertex \(K\), and \(K\) occurs more than once on \(C\). This is impossible.

*Betweenness.* Let \(x\ne z\) in \(F\) and take a list \(x=x_0,\dots,x_n=z\) of \([x,z]\) as in Lemma 4.2. Follow the links from \(x_0\) to \(x_1\), from \(x_1\) to \(x_2\), and so on. No vertex is visited twice: the \(x_i\) are distinct, and if the links of \(x_{i-1},x_i\) and of \(x_{j-1},x_j\), with \(i<j\), passed through the same \(K\in\mathcal N\), then \(x_{i-1}\) and \(x_j\) would be adjacent, as points of the clique \(K\), while \(x_{i-1}x_ix_j\) holds by Lemma 4.2. So the links form the path from \(x\) to \(z\) in \(\tau\), and the points of \(F\) on this path are exactly the points of \([x,z]\). Hence, for \(y\in F\), \(y\) lies between \(x\) and \(z\) in \(\tau\) if and only if \(y\in(x,z)\), that is, \(xyz\). For \(x=z\) neither holds. \(\blacksquare\)

**Corollary 4.5** (checking in finite trees). Let \(x_1,\dots,x_k\) be points of a pretree. There is a finite tree whose vertex set contains \(x_1,\dots,x_k\) and in which \(x_b\) lies between \(x_a\) and \(x_c\) exactly when \(x_ax_bx_c\).

**Proof.** The finite set \(\{x_1,\dots,x_k\}\) is a pretree; apply Theorem 4.1. \(\blacksquare\)

## 5. Linear sets and their two orders

Let \(T\) be a pretree. A subset \(A\) is *full* if \([x,y]\subseteq A\) for all \(x,y\in A\). It is *linear* if for any three distinct points of \(A\) one lies between the other two. An *arc* is a nonempty full linear subset. A *direction* on a linear set \(A\) is a total order \(<\) on \(A\) such that for all \(x,y,z\in A\)
\[
xyz\quad\Longleftrightarrow\quad x<y<z\ \text{ or }\ z<y<x .
\]
The reverse of a direction is a direction.

**Lemma 5.1.** Let \(A\) be a finite linear set of vertices of a tree \(\tau\) with at least two points. Then there are \(a,b\in A\) with \(A\subseteq[a,b]_\tau\), and the order in which the path from \(a\) to \(b\) visits the points of \(A\) is a direction on \(A\).

**Proof.** Choose \(a,b\in A\) for which the path from \(a\) to \(b\) is longest. Let \(c\in A\) be a third point. If \(a\) lay between \(c\) and \(b\), then \([c,b]_\tau=[c,a]_\tau\cup[a,b]_\tau\) by Lemma 1.1 would be a longer path; likewise \(b\) does not lie between \(a\) and \(c\). Since \(A\) is linear, \(c\) lies between \(a\) and \(b\). For points \(x,y,z\) on a path, \(y\) lies between \(x\) and \(z\) exactly when the path visits \(y\) between its visits of \(x\) and \(z\), because the path from \(x\) to \(z\) is a part of the given path. \(\blacksquare\)

**Proposition 5.2.** Let \(A\) be a linear subset of a pretree and \(a\ne b\) two points of \(A\). There is exactly one direction \(<\) on \(A\) with \(a<b\). So a linear set with at least two points has exactly two directions, each the reverse of the other.

**Proof.** *Finite \(A\), existence.* By Theorem 4.1, \(A\) is a set of vertices of a finite tree with the same betweenness. Lemma 5.1 gives a direction; reverse it if \(b<a\).

*Finite \(A\), uniqueness.* Let \(<\) be a direction and \(x_1<x_2<\dots<x_n\) the points of \(A\). A point \(x_i\) with \(1<i<n\) lies between \(x_{i-1}\) and \(x_{i+1}\), and \(x_1\) and \(x_n\) lie between no two points of \(A\). So the pair \(\{x_1,x_n\}\) is determined by the betweenness relation. Moreover, for distinct \(x,y\ne x_1\): \(x<y\) if and only if \(x_1xy\). So a direction is determined by the betweenness relation and by its least point, which is one of two points. Hence there are at most two directions; a direction and its reverse are two, and exactly one of them has \(a<b\).

*General \(A\).* For distinct \(x,y\in A\) define \(x<y\) to mean that \(x\) precedes \(y\) in the unique direction on \(\{a,b,x,y\}\) in which \(a\) precedes \(b\). If \(B\) is a finite subset of \(A\) containing \(a,b,x,y\), the direction on \(B\) in which \(a\) precedes \(b\) restricts to a direction on \(\{a,b,x,y\}\), so by uniqueness \(x<y\) if and only if \(x\) precedes \(y\) in \(B\). Applying this to the sets \(B=\{a,b,x,y,z\}\) shows that \(<\) is a total order and a direction on \(A\), with \(a<b\). If \(<'\) is any direction on \(A\) with \(a<'b\), its restriction to \(\{a,b,x,y\}\) is the direction used in the definition, so \(<'\) equals \(<\). \(\blacksquare\)

**Corollary 5.3** (intervals are ordered). Let \(a\ne b\) be points of a pretree. The interval \([a,b]\) is an arc. Its direction with \(a<b\) is given, for distinct \(x,y\in[a,b]\), by
\[
x<y\quad\Longleftrightarrow\quad x\in[a,y).
\]
In it \(a\) is the least and \(b\) the greatest point, and these are the only two points of \([a,b]\) that lie between no two points of \([a,b]\). In particular \([a,b]=[a',b']\) implies \(\{a,b\}=\{a',b'\}\).

**Proof.** Let \(x,y,z\in[a,b]\) be distinct and \(c\in[x,y]\). By Corollary 4.5 there is a finite tree \(\tau\) containing \(a,b,x,y,z,c\) with the same betweenness. Then \(x,y,z\) lie on the path from \(a\) to \(b\), so one of them lies between the other two; and \(c\) lies on the part of this path between \(x\) and \(y\), so \(c\in[a,b]\). Hence \([a,b]\) is linear and full. In \(\tau\) the direction on \(\{a,b,x,y\}\) with \(a\) before \(b\) is the order along the path from \(a\) to \(b\), in which \(x\) precedes \(y\) exactly when \(x\) lies on the part from \(a\) to \(y\) and \(x\ne y\). This gives the formula. For \(x\ne a\) the formula gives \(a<x\), since \(a\in[a,x)\); similarly \(x<b\) for \(x\ne b\). A point \(x\) with \(a<x<b\) lies between \(a\) and \(b\), and the least and the greatest point of a direction lie between no two points. \(\blacksquare\)

## 6. Medians

A point \(c\) of a pretree is a *median* of \(x,y,z\) if
\[
c\in[x,y]\cap[y,z]\cap[z,x].
\]

**Lemma 6.1.** For three vertices \(x,y,z\) of a tree \(\tau\), the set \([x,y]_\tau\cap[y,z]_\tau\cap[z,x]_\tau\) consists of exactly one vertex.

**Proof.** Let \(m\) be the last vertex of the path from \(x\) to \(y\) that lies on the path from \(x\) to \(z\). The parts of the two paths from \(x\) to \(m\) are both the path from \(x\) to \(m\), so \([x,y]_\tau\cap[x,z]_\tau\supseteq[x,m]_\tau\), and equality holds by the choice of \(m\). So \([m,y]_\tau\cap[m,z]_\tau=\{m\}\), and following the path from \(y\) to \(m\) and then the path from \(m\) to \(z\) visits no vertex twice: this is the path from \(y\) to \(z\). Hence \(m\) lies in all three sets. Conversely, a vertex \(c\) in all three sets lies in \([x,m]_\tau\) and in \([y,m]_\tau\cup[m,z]_\tau\). But \([x,m]_\tau\) meets \([m,y]_\tau\) only in \(m\), as parts of the path from \(x\) to \(y\), and meets \([m,z]_\tau\) only in \(m\). So \(c=m\). \(\blacksquare\)

**Proposition 6.2.** Three points of a pretree have at most one median.

**Proof.** Let \(c,c'\) be medians of \(x,y,z\). By Corollary 4.5 there is a finite tree \(\tau\) containing the five points with the same betweenness. For points \(u,v,p\) of the pretree among these five, \(p\in[u,v]\) if and only if \(p\in[u,v]_\tau\). So \(c\) and \(c'\) lie in the set of Lemma 6.1, and \(c=c'\). \(\blacksquare\)

When the median exists it is written \(\operatorname{med}(x,y,z)\). A *median pretree* is a pretree in which every three points have a median. The vertex set of a tree is a median pretree by Lemma 6.1. A set of three points with the empty relation is a pretree without a median for its three points; in the tree of Theorem 4.1 the missing median appears as the added vertex.

## 7. Exercises

**7.1.** Show that the real line with the relation "\(x<y<z\) or \(z<y<x\)" is a pretree, that every interval of the pretree is an interval of the line, and that the set of rational numbers \(x\) with \(x^2<2\) is an arc of the pretree \(\mathbb Q\) that is not an interval of \(\mathbb Q\).

**7.2.** A point \(p\) of a pretree is *terminal* if it lies between no two points. Show that a finite pretree with at least two points has at least two terminal points.

**7.3.** Show that Lemma 2.3(3) fails without the assumption \(y\ne z\), and that in Lemma 2.3(3) at most one of the two conclusions holds.

**7.4.** Let \(\tau\) be the tree of Theorem 4.1 for a finite pretree \(F\). Show that every vertex of \(\tau\) outside \(F\) has at least three neighbours, all in \(F\). Show that if \(F\) is the vertex set of a finite tree \(\tau_0\) with its betweenness, then \(\tau=\tau_0\).

**7.5.** Let \(F=\{x,y,z,w\}\) with the relations \(xyz\), \(xyw\) and their reverses \(zyx\), \(wyx\), and no others. Check that \(F\) is a pretree and determine the tree of Theorem 4.1. Show also that the four points with only the relations \(xyz\) and \(zyx\) do not form a pretree.

## 8. Solutions

**7.1.** (T0) and (T1) are clear. (T2): \(y\) strictly between \(x\) and \(z\) excludes \(z\) strictly between \(x\) and \(y\). (T3): let \(z\) be strictly between \(x\) and \(y\), say \(x<z<y\), and \(w\ne z\); if \(w>z\) then \(x<z<w\), and if \(w<z\) then \(w<z<y\). The interval \((x,y)\) of the pretree is the set of reals strictly between \(x\) and \(y\). In \(\mathbb Q\) the set \(A=\{x:x^2<2\}\) is linear, and it is full because a rational between two elements of \(A\) lies in \(A\). Suppose \(A\) is an interval of \(\mathbb Q\) with ends \(p\le q\). It has more than one point, so \(p<q\), and it consists of the rationals strictly between \(p\) and \(q\) and possibly \(p\) or \(q\). Then the greatest lower bound of \(A\) in \(\mathbb R\) is the rational number \(p\). But the greatest lower bound of \(A\) is \(-\sqrt2\), which is irrational.

**7.2.** Among all pairs of distinct points choose \(a,b\) for which \([a,b]\) has the most points. Suppose \(a\) is not terminal: \(yaz\) for some \(y,z\). By (T3) with the point \(b\ne a\), \(yab\) or \(zab\); say \(yab\). For \(c\in(a,b)\), \(yab\) and \(acb\) give \(yacb\) by Lemma 2.3(2), so \(c\in(y,b)\). Hence \([a,b]\subseteq[y,b]\). And \(y\notin[a,b]\): it is not \(a\) or \(b\), and \(ayb\), that is \(bya\), would contradict \(bay\) by (T2). So \([y,b]\) has more points than \([a,b]\), a contradiction. The same holds for \(b\).

**7.3.** If \(y=z\), the conclusions \(xyyw\) and \(xyyw\) contain the relation \(xyy\), which never holds. If both \(xyzw\) and \(xzyw\) held, then \(xyz\) and \(xzy\) would both hold, against (T2).

**7.4.** A vertex outside \(F\) is a maximal clique \(K\) with at least three points, and its neighbours are the points of \(K\). Let \(F\) be the vertex set of a tree \(\tau_0\). Two vertices are adjacent in the pretree exactly when the path between them has no interior vertex, that is, when they are joined by an edge of \(\tau_0\). Three pairwise adjacent points would form a cycle of \(\tau_0\), so there are no cliques with three points: \(\mathcal N\) is empty, \(K(x,y)=\{x,y\}\) for adjacent \(x,y\), and the edges of \(\tau\) are the edges of \(\tau_0\).

**7.5.** All relations have \(y\) in the middle. (T0) and (T1) hold. (T2): no relation has \(y\) at an end. (T3): given a relation \(uyv\) and a point \(t\ne y\), one of \(uyt\), \(vyt\) must hold. If \(t\) is \(u\) or \(v\), this is \(vyu\) or \(uyv\). Otherwise \(\{u,v\}\) is \(\{x,z\}\) and \(t=w\), where \(xyw\) holds, or \(\{u,v\}\) is \(\{x,w\}\) and \(t=z\), where \(xyz\) holds. So \(F\) is a pretree. The adjacent pairs are \(\{x,y\}\), \(\{y,z\}\), \(\{y,w\}\) and \(\{z,w\}\). The maximal cliques are \(\{x,y\}\) and \(K=\{y,z,w\}\). The tree has the vertices \(x,y,z,w,K\) and the edges \(x\)–\(y\), \(y\)–\(K\), \(z\)–\(K\), \(w\)–\(K\): the points \(z\) and \(w\) hang on a branch vertex that is not a point of \(F\). With only \(xyz\) and \(zyx\), axiom (T3) fails for the relation \(xyz\) and the point \(w\): neither \(xyw\) nor \(zyw\) holds.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 2. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
