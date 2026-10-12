# Cut points of a connected space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The pretrees of the earlier lessons were sets of vertices of trees, ordered sets, and structures built from them. This lesson gives the example for which the theory is used: a connected Hausdorff space \(M\) is a pretree, when "\(z\) lies between \(x\) and \(y\)" means that removing the point \(z\) separates \(x\) from \(y\). The points that lie between two others are the cut points of \(M\).

- If removing \(a\) splits \(M\) into two open parts \(U\) and \(V\), then \(U\cup\{a\}\) is closed and connected (Lemma 1.1). Two different cut points split \(M\) into three open parts arranged in a row (Lemma 1.2).
- With the relation "\(z\) separates \(x\) from \(y\)", \(M\) is a pretree (Theorem 2.1).
- A *branch* is a closed set with at least two points and a single boundary point. The branches are the sets \(U\cup\{a\}\) of the first item, and a branch meets every closed connected set in a connected set (Lemmas 3.1 and 3.2).
- A set is *coherent* if it is closed and meets every compact connected set in a connected set. Every intersection of branches is coherent; in a compact space it is therefore connected (Proposition 5.2).

The lesson follows Lemmas 5.1 to 5.9 of [Bowditch]. It uses the first lesson, [Betweenness and pretrees](betweenness-and-pretrees.md), for the axioms, and the notions of connected, compact and Hausdorff spaces from the core course [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90): a closed subset of a compact space is compact, and a compact subset of a Hausdorff space is closed. The empty set counts as connected.

## 1. Separations at a point

Let \(M\) be a connected Hausdorff space. Points of \(M\) are closed, so \(M\setminus\{a\}\) is open for every \(a\in M\).

A point \(a\in M\) is a *cut point* if \(M\setminus\{a\}\) is not connected. A *separation at \(a\)* is a pair \((U,V)\) of disjoint nonempty open subsets of \(M\) with \(U\cup V=M\setminus\{a\}\). We write
\[
U\,a\,V
\]
to say that \((U,V)\) is a separation at \(a\). So \(a\) is a cut point exactly when there is a separation at \(a\).

**Lemma 1.1.** Let \(U\,a\,V\). Then \(U\cup\{a\}\) is closed and connected, and it is the closure of \(U\).

**Proof.** The complement of \(U\cup\{a\}\) is the open set \(V\). Suppose \(U\cup\{a\}=F\cup G\) with \(F,G\) disjoint and closed in \(U\cup\{a\}\), hence closed in \(M\), and let \(a\in F\). Then \(G\subseteq U\), and
\[
M\setminus G=F\cup(V\cup\{a\})
\]
is closed, as a union of two closed sets. So \(G\) is open and closed in \(M\), and \(a\notin G\). Since \(M\) is connected, \(G\) is empty. Hence \(U\cup\{a\}\) is connected.

The set \(U\) is not closed, because it is open, not empty and not all of \(M\). So its closure is larger than \(U\) and contained in the closed set \(U\cup\{a\}\). \(\blacksquare\)

**Lemma 1.2.** Let \(a\ne b\) be cut points of \(M\), with separations \(U\,a\,U'\) and \(V\,b\,V'\) named so that \(b\in U'\) and \(a\in V'\). Then:

1. \(U\cup\{a\}\subseteq V'\) and \(V\cup\{b\}\subseteq U'\); in particular \(U\cap V=\varnothing\);
2. the set \(W=U'\cap V'\) is open and not empty, and \(M\) is the disjoint union of \(U\), \(\{a\}\), \(W\), \(\{b\}\) and \(V\).

**Proof.** (1) The set \(U\cup\{a\}\) is connected and does not contain \(b\). So it lies in one of the two disjoint open sets \(V,V'\) that cover \(M\setminus\{b\}\); it contains \(a\in V'\), so it lies in \(V'\). In the same way \(V\cup\{b\}\subseteq U'\). Then \(U\cap V\subseteq V'\cap V=\varnothing\).

(2) The complement of \(U\cup\{a\}\) is \(U'\). The points of \(U'\) other than \(b\) lie in \(V\) or in \(V'\), and \(V\subseteq U'\); so \(U'\) is the disjoint union of \(V\), \(\{b\}\) and \(W\). If \(W\) were empty, \(M\) would be the union of the two disjoint nonempty closed sets \(U\cup\{a\}\) and \(V\cup\{b\}\), and would not be connected. \(\blacksquare\)

In the situation of Lemma 1.2 the three open sets lie in a row: \(U\), then \(a\), then \(W\), then \(b\), then \(V\).

## 2. The pretree of a connected space

For points \(x,y,z\) of \(M\) write
\[
xzy
\]
if there is a separation \(U\,z\,V\) with \(x\in U\) and \(y\in V\). We then say that \(z\) *separates \(x\) from \(y\)*.

**Theorem 2.1.** Let \(M\) be a connected Hausdorff space. With this ternary relation \(M\) is a pretree. A point of \(M\) lies between two points if and only if it is a cut point.

**Proof.** (T0): \(xzx\) would put \(x\) into two disjoint sets. (T1): if \(U\,z\,V\), then \(V\,z\,U\).

(T2): suppose \(xab\) and \(xba\). There are separations \(U\,a\,U'\) with \(x\in U\), \(b\in U'\), and \(V\,b\,V'\) with \(x\in V\), \(a\in V'\). By Lemma 1.2(1), \(U\cap V\) is empty; but it contains \(x\).

(T3): let \(xay\) and \(z\ne a\). There is a separation \(U\,a\,V\) with \(x\in U\) and \(y\in V\). The point \(z\) lies in \(U\) or in \(V\). If \(z\in V\), then \(xaz\); if \(z\in U\), then \(zay\), that is, \(yaz\).

A point that lies between two points has a separation, so it is a cut point. If \(a\) is a cut point and \(U\,a\,V\), choose \(x\in U\) and \(y\in V\); then \(xay\). \(\blacksquare\)

So the interval \((x,y)\) of this pretree is the set of cut points of \(M\) that separate \(x\) from \(y\), and the points that are not cut points are the terminal points of the pretree. By Corollary 5.3 of the first lesson the set of points that separate \(x\) from \(y\) is linearly ordered, in the direction from \(x\) to \(y\).

If \(z\) separates \(x\) from \(y\), then \(x\) and \(y\) lie in different components of \(M\setminus\{z\}\), because a connected subset of \(M\setminus\{z\}\) lies in \(U\) or in \(V\). The two conditions agree when the components of \(M\setminus\{z\}\) are open, for example when \(M\) is locally connected.

**Example 2.2.** (a) Let \(M=[0,1]\). For \(0<z<1\) the two sets \([0,z)\) and \((z,1]\) are connected and open in \(M\), so they form the only separation at \(z\), up to the order of the pair. The points \(0\) and \(1\) are not cut points. So \(xzy\) holds exactly when \(z\) lies strictly between \(x\) and \(y\): the pretree of the space \([0,1]\) is the pretree of the ordered set \([0,1]\).

(b) A circle has no cut point: the complement of a point is homeomorphic to an open interval. Its pretree has the empty relation. The same holds for every connected Hausdorff space without cut points.

## 3. Branches

The *boundary* of a closed set \(B\subseteq M\) is the set of points of \(B\) that are not interior points of \(B\).

**Definition.** A *branch* of \(M\) is a closed subset with at least two points whose boundary consists of a single point.

**Lemma 3.1.** A subset \(B\subseteq M\) is a branch with boundary point \(a\) if and only if \(B=U\cup\{a\}\) for a separation \(U\,a\,V\).

**Proof.** Let \(U\,a\,V\) and \(B=U\cup\{a\}\). Then \(B\) is closed with at least two points, and the points of the open set \(U\) are interior points. The point \(a\) is not an interior point: otherwise \(B\) would be open and closed, and it is neither empty nor all of \(M\). So the boundary of \(B\) is \(\{a\}\).

Conversely let \(B\) be a branch with boundary \(\{a\}\). Then \(U=B\setminus\{a\}\) is the interior of \(B\); it is open, and not empty because \(B\) has two points. The set \(V=M\setminus B\) is open, and not empty: if \(B=M\), every point of \(B\) would be interior. So \(U\,a\,V\). \(\blacksquare\)

By Lemma 1.1 every branch is connected. More is true.

**Lemma 3.2.** Let \(K\subseteq M\) be closed and connected, and \(B\) a branch. Then \(B\cap K\) is connected.

**Proof.** Let \(a\) be the boundary point of \(B\); the set \(B\setminus\{a\}\) is open in \(M\). Suppose \(B\cap K=F\cup G\) with \(F,G\) disjoint and closed in \(B\cap K\), hence closed in \(M\), and name them so that \(a\notin F\). Then
\[
K\setminus F=G\cup\bigl(K\setminus(B\setminus\{a\})\bigr):
\]
a point of \(K\) outside \(F\) lies in \(G\) or outside \(B\); and if \(a\) lies in \(K\), it lies in \(G\), because \(a\notin F\). The right side is closed, because \(G\) and \(K\) are closed and \(B\setminus\{a\}\) is open. So \(F\) and \(K\setminus F\) are disjoint closed subsets of \(K\) with union \(K\). Since \(K\) is connected, \(F\) is empty, or \(K=F\); in the second case \(K\subseteq B\) and \(G\) is empty. \(\blacksquare\)

**Corollary 3.3.** In the situation of Lemma 1.2, the set \(W\cup\{a,b\}\) is closed and connected.

**Proof.** It is the intersection of \(U'\cup\{a\}\) and \(V'\cup\{b\}\). Both are branches, by Lemma 3.1, and the first is closed and connected. Apply Lemma 3.2. \(\blacksquare\)

## 4. Intersections of compact connected sets

**Lemma 4.1.** Let \(A\) and \(B\) be disjoint compact subsets of a Hausdorff space. Then there are disjoint open sets \(O_A\supseteq A\) and \(O_B\supseteq B\).

**Proof.** Fix \(a\in A\). For every \(b\in B\) choose disjoint open sets \(U_b\ni a\) and \(V_b\ni b\). Finitely many of the sets \(V_b\) cover \(B\); let \(V^a\) be their union and \(U^a\) the intersection of the corresponding sets \(U_b\). Then \(U^a\ni a\) and \(V^a\supseteq B\) are disjoint open sets. Finitely many of the sets \(U^a\) cover \(A\); let \(O_A\) be their union and \(O_B\) the intersection of the corresponding sets \(V^a\). \(\blacksquare\)

**Lemma 4.2.** Let \(\mathcal E\) be a nonempty set of compact connected subsets of a Hausdorff space such that the intersection of any two members of \(\mathcal E\) is a member of \(\mathcal E\). Then the intersection \(C\) of all members of \(\mathcal E\) is connected.

**Proof.** The set \(C\) is closed in each member of \(\mathcal E\), so it is compact. Suppose \(C=A\cup B\) with \(A,B\) disjoint, nonempty and closed in \(C\). They are compact, so Lemma 4.1 gives disjoint open sets \(O_A\supseteq A\) and \(O_B\supseteq B\). Let \(O=O_A\cup O_B\). The sets \(E\setminus O\), \(E\in\mathcal E\), are compact, and their intersection \(C\setminus O\) is empty. So finitely many of them have empty intersection; since \(\mathcal E\) is closed under finite intersections, \(E\setminus O\) is empty for one \(E\in\mathcal E\). This \(E\) is connected and lies in the union of the disjoint open sets \(O_A\) and \(O_B\), so it lies in one of them. But \(E\) contains \(A\) and \(B\). This is a contradiction. \(\blacksquare\)

In particular the intersection of a nonempty set of compact connected sets that is totally ordered by inclusion is connected.

## 5. Coherent sets

Let \(M\) again be a connected Hausdorff space.

**Definition 5.1.** A subset \(F\subseteq M\) is *coherent* if it is closed and \(F\cap K\) is connected for every compact connected subset \(K\subseteq M\).

If \(M\) is compact, a coherent set is connected: take \(K=M\).

**Proposition 5.2.**

1. Every branch of \(M\) is coherent.
2. The intersection of a nonempty set of coherent subsets of \(M\) is coherent.
3. The intersection of a nonempty set of branches of \(M\) is coherent. If \(M\) is compact, it is closed and connected.

**Proof.** (1) A compact subset of \(M\) is closed; apply Lemma 3.2.

(2) Let \(\mathcal F\) be the set and \(K\) compact and connected. First, for \(F_1,\dots,F_n\in\mathcal F\) the set \(K\cap F_1\cap\dots\cap F_n\) is compact and connected: by induction on \(n\), the set \(K\cap F_1\cap\dots\cap F_{n-1}\) is compact and connected, and \(F_n\) is coherent. Let \(\mathcal E\) be the set of all these finite intersections. It is closed under intersections of two members, so by Lemma 4.2 the intersection of all its members is connected. This intersection is \(K\cap\bigcap\mathcal F\). And \(\bigcap\mathcal F\) is closed.

(3) follows from (1) and (2). \(\blacksquare\)

## 6. Exercises

**6.1.** Let \(U\,a\,V\), \(x\in U\) and \(y\in V\). Show that every connected subset of \(M\) that contains \(x\) and \(y\) contains \(a\).

**6.2.** Let \(M\) be the union of three segments in the plane that have one common endpoint \(c\) and are otherwise disjoint. Determine the cut points of \(M\), all separations at \(c\), and the points between two given points.

**6.3.** Let \(B_1\) and \(B_2\) be branches with the same boundary point \(a\). Show that \(B_1\cap B_2\) is \(\{a\}\) or a branch with boundary point \(a\).

**6.4.** Give an example of a connected Hausdorff space \(M\) and a branch \(B\) such that \(B\) with its boundary point removed is not connected.

**6.5.** Let \(M\) be compact, and \(x,y\in M\). Show that the set of points \(w\) such that no cut point separates \(w\) from both \(x\) and \(y\) at once, that is, such that for no \(z\) both \(wzx\) and \(wzy\) hold, is closed and connected.

## 7. Solutions

**6.1.** A connected set that does not contain \(a\) lies in \(M\setminus\{a\}=U\cup V\), hence in \(U\) or in \(V\), and cannot contain both \(x\) and \(y\).

**6.2.** Write \(S_1,S_2,S_3\) for the segments without the point \(c\), and \(e_1,e_2,e_3\) for their other endpoints. The sets \(S_i\) are connected and open in \(M\), so every separation at \(c\) puts each \(S_i\) on one side: there are three separations up to the order of the pair, one for each \(i\), with \(S_i\) on one side and the two other \(S_j\) on the other. A point \(z\in S_i\) other than \(e_i\) splits \(M\) into the part of \(S_i\) beyond \(z\) and the rest, which are connected and open; this is the only separation at \(z\). The points \(e_i\) are not cut points. So the cut points are all points except \(e_1,e_2,e_3\). A point \(z\) lies between \(x\) and \(y\) exactly when it lies on the path in \(M\) from \(x\) to \(y\) and is different from both: for \(x,y\) on the same segment this is the part of the segment between them, and for \(x\in S_i\cup\{c\}\), \(y\in S_j\), \(i\ne j\), it is the part of \(S_i\) between \(x\) and \(c\), the point \(c\) if \(x\ne c\), and the part of \(S_j\) between \(c\) and \(y\).

**6.3.** By Lemma 3.1, \(B_i=U_i\cup\{a\}\) with separations \(U_i\,a\,V_i\). Then \(B_1\cap B_2=(U_1\cap U_2)\cup\{a\}\). If \(U_1\cap U_2\) is empty, this is \(\{a\}\). Otherwise \(U_1\cap U_2\) and \(V_1\cup V_2\) are disjoint nonempty open sets with union \(M\setminus\{a\}\), so they form a separation at \(a\), and \(B_1\cap B_2\) is a branch by Lemma 3.1.

**6.4.** In Exercise 6.2 let \(B=S_1\cup S_2\cup\{c\}\). By Lemma 3.1 it is a branch with boundary point \(c\), and \(B\setminus\{c\}=S_1\cup S_2\) is not connected.

**6.5.** Call the set \(R\). A point \(w\) lies outside \(R\) exactly when there are a point \(z\) and a separation \(U\,z\,V\) with \(w\in U\) and \(x,y\in V\): if \(wzx\) and \(wzy\) hold through separations \(U_1\,z\,V_1\) and \(U_2\,z\,V_2\) with \(w\in U_1\cap U_2\), then \(U_1\cap U_2\) and \(V_1\cup V_2\) form a separation at \(z\) as in 6.3, with \(w\) on one side and \(x,y\) on the other. So \(R\) is the intersection of all sets \(V\cup\{z\}\), over all separations \(U\,z\,V\) with \(x,y\in V\). These sets are branches. If there is no such separation, \(R=M\). Otherwise Proposition 5.2(3) shows that \(R\) is closed and connected.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 5. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
