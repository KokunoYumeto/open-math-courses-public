# Adjacent points of the completion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The completion \(\Phi(T)\) of a pretree \(T\), constructed in [The completion of a pretree](the-completion-of-a-pretree.md), is complete and median, but it is in general not dense: on the real line, the flow that runs up towards a number \(x\) without arriving is a point of the completion next to \(x\), with nothing between them. This lesson determines all pairs of adjacent points of \(\Phi(T)\).

- Two points of \(T\) are never adjacent in \(\Phi(T)\) (Proposition 1.1).
- Two points of \(\Phi(T)\) are adjacent exactly when one of them is a point \(a\) of \(T\) and the other is a flow, different from the flow towards \(a\), that runs nowhere from \(a\) (Theorem 2.3). So of two adjacent points exactly one is a point of \(T\).
- The points of \(\Phi(T)\) adjacent to a point \(a\) of \(T\) correspond to the *branches* of \(T\) at \(a\), the parts into which \(a\) separates the other points (Theorem 3.2).

The lesson follows Lemmas 3.26 to 3.29 of [Bowditch]; the last of them is proved here by a direct construction. It uses [Betweenness and pretrees](betweenness-and-pretrees.md), [Flows on a pretree](flows-on-a-pretree.md), the lesson on the completion, and [Stars and the three kinds of flows](stars-and-the-three-kinds-of-flows.md).

## 1. Points of the pretree are not adjacent

Throughout, \(T\) is a pretree, \(P\) the set of its flows, \(\bar x\) the flow towards a point \(x\), and \(\bar T\) the set of all \(\bar x\). We recall the notation and the facts of the lesson on the completion that are used below. In the pretree \(T\sqcup P\) the interval \((p,q)\) between two flows is a subset of \(T\), and \(xyp\) means \(xy.p\). Letters \(p,q,r\) denote flows and \(a,x,y,z\) points of \(T\).

- (R1) If \(p\ne q\), then \((p,q)\) is not empty.
- (R2) If \(p\ne\bar x\), then \((p,\bar x)=(p,x]\); this set consists of \(x\) and of the points \(y\) with \(xy.p\).
- (R3) For distinct \(p,q,r\), the relation \(\langle prq\rangle\) means: either \(r=\bar x\) for a point \(x\) with \(pxq\), or \(r\notin\bar T\) and \((p,r)\cap(r,q)=\varnothing\). Moreover, if \(p,q,r\) are distinct and \((p,r)\cap(r,q)=\varnothing\), then \(\langle prq\rangle\).
- (R4) If \(\langle prq\rangle\), then \((p,q)=(p,r)\cup(r,q)\).
- (R5) \(\langle\bar x\bar y\bar z\rangle\) if and only if \(xyz\).
- (R6) The set \(P\) with the relation \(\langle\ \rangle\) is a median pretree \(\Phi=\Phi(T)\).

These are Lemma 1.1, Definition 2.1, Lemma 2.2 and Theorems 3.1 and 4.1 of that lesson. Intervals of \(\Phi\) are written \([p,q]_\Phi\) and \((p,q)_\Phi\).

**Proposition 1.1.** Let \(x\ne y\) be points of \(T\). Then there is a flow \(p\) with \(\langle\bar x\,p\,\bar y\rangle\). So \(\bar x\) and \(\bar y\) are not adjacent in \(\Phi\).

**Proof.** *If there is \(z\in(x,y)\)*: then \(\langle\bar x\bar z\bar y\rangle\) by (R5).

*If \(x\) and \(y\) are adjacent and \(\{x,y,z\}\) is null for some third point \(z\)*: let \(m\) be the median of \(\bar x,\bar y,\bar z\) in \(\Phi\), by (R6). If \(m=\bar x\), then \(\bar x\in[\bar y,\bar z]_\Phi\), so \(\langle\bar y\bar x\bar z\rangle\) and \(yxz\) by (R5), against the assumption. In the same way \(m\ne\bar y\). Since \(m\in[\bar x,\bar y]_\Phi\), this gives \(\langle\bar x\,m\,\bar y\rangle\).

*Otherwise* \(F=\{x,y\}\) is null and full, because \(x\) and \(y\) are adjacent, and it is maximal null. So \(F\) is a star. Let \(p=\operatorname{flow}(F)\). By Theorem 3.1 of the lesson on stars, \(p\) runs nowhere from \(x\) and nowhere from \(y\). In particular \(yx.p\) fails, while \(yx.\bar x\) holds; so \(p\ne\bar x\), and likewise \(p\ne\bar y\). By (R2), \((p,\bar x)=\{x\}\) and \((p,\bar y)=\{y\}\). These sets are disjoint, so \(\langle\bar x\,p\,\bar y\rangle\) by (R3). \(\blacksquare\)

## 2. The neighbours of a point of the pretree

Two adjacent points are also called *neighbours* of each other. For \(a\in T\) let
\[
\begin{gathered}
L(a)=\{p\in P\mid p\ne\bar a,\ \text{and}\\
ay.p\ \text{for no}\ y\in T\}.
\end{gathered}
\]
So \(L(a)\) is the set of flows, other than the flow towards \(a\), that run nowhere from \(a\). By (R2), for \(p\ne\bar a\),
\[
p\in L(a)\quad\Longleftrightarrow\quad(p,\bar a)=\{a\}.
\]
No flow \(\bar x\) lies in \(L(a)\): for \(x\ne a\) we have \(ax.\bar x\).

**Lemma 2.1.** Let \(a\in T\). The points of \(\Phi\) adjacent to \(\bar a\) are exactly the points of \(L(a)\).

**Proof.** Let \(p\in L(a)\), and suppose \(\langle\bar a\,r\,p\rangle\). By (R4), \((\bar a,r)\) and \((r,p)\) are subsets of \((\bar a,p)=\{a\}\), and by (R1) they are not empty. So both are \(\{a\}\). They are not disjoint, so by (R3) \(r=\bar z\) for a point \(z\) with \(\bar a\,z\,p\). Then \(z\in(\bar a,p)=\{a\}\), and \(r=\bar a\), which is excluded. So \(p\) is adjacent to \(\bar a\).

Conversely let \(p\) be adjacent to \(\bar a\). By Proposition 1.1, \(p\notin\bar T\). Suppose \(ax.p\) for some \(x\). Then \(x\in(p,\bar a)\) by (R2), and \(\bar x\) differs from \(p\) and from \(\bar a\); so \(\langle\bar a\,\bar x\,p\rangle\) by (R3), against the adjacency. Hence \(p\in L(a)\). \(\blacksquare\)

**Lemma 2.2.** Let \(p\ne q\) be points of \(L(a)\). Then \(\langle p\,\bar a\,q\rangle\), and \(\bar a\) is the only point of \(\Phi\) between \(p\) and \(q\).

**Proof.** Let \(m\) be the median of \(p,q,\bar a\) in \(\Phi\). By Lemma 2.1, \([p,\bar a]_\Phi=\{p,\bar a\}\) and \([q,\bar a]_\Phi=\{q,\bar a\}\). The point \(m\) lies in both, so \(m=\bar a\). Hence \(\bar a\in[p,q]_\Phi\), and \(\langle p\,\bar a\,q\rangle\).

Let \(\langle prq\rangle\) with \(r\ne\bar a\). By Lemma 2.3(3) of the first lesson, applied in the pretree \(\Phi\), the points \(p,\bar a,r,q\) or the points \(p,r,\bar a,q\) lie in a row. In the first case \(\langle\bar a\,r\,q\rangle\), in the second \(\langle p\,r\,\bar a\rangle\). Both contradict Lemma 2.1. \(\blacksquare\)

**Theorem 2.3.** Two points \(p,q\) of \(\Phi(T)\) are adjacent if and only if there is a point \(a\in T\) such that one of them is \(\bar a\) and the other lies in \(L(a)\). In particular, of two adjacent points of \(\Phi(T)\) exactly one lies in \(\bar T\).

**Proof.** One direction is Lemma 2.1. Let \(p,q\) be adjacent. By (R1) there is \(a\in(p,q)\). If \(\bar a\) were different from \(p\) and \(q\), then \(\langle p\,\bar a\,q\rangle\) by (R3). So one of them is \(\bar a\), and the other lies in \(L(a)\) by Lemma 2.1. The last statement holds because \(L(a)\) does not meet \(\bar T\). \(\blacksquare\)

For a flow \(p\) let \(F_p\) be the set of points from which \(p\) runs nowhere, as in the lesson on stars. Recall that the type \((m,n)\) of \(p\) has as its second entry the number of points of \(F_p\) (Lemma 4.3 there).

**Corollary 2.4.**

1. Let \(p\in\Phi\setminus\bar T\). The neighbours of \(p\) are the points \(\bar a\) with \(a\in F_p\). So a flow of type \((m,n)\) that is not a flow towards a point has exactly \(n\) neighbours.
2. For \(a\in T\) the set \(L(a)\cup\{\bar a\}\) is full in \(\Phi\).
3. Let \([p,q]_\Phi\) be finite, and list its points in the direction from \(p\) to \(q\). Then consecutive points are adjacent, and the points lie alternately in \(\bar T\) and outside \(\bar T\).

**Proof.** (1) By Theorem 2.3 the neighbours of \(p\) are the \(\bar a\) with \(p\in L(a)\). Since \(p\ne\bar a\) for all \(a\), this means \(a\in F_p\).

(2) By Lemmas 2.1 and 2.2, \([p,\bar a]_\Phi=\{p,\bar a\}\) and \([p,q]_\Phi=\{p,\bar a,q\}\) for \(p\ne q\) in \(L(a)\).

(3) Let \(r\) and \(r'\) be consecutive in the list. The interval \([p,q]_\Phi\) is an arc (Corollary 5.3 of the first lesson). A point between \(r\) and \(r'\) lies in it, because it is full, and comes between \(r\) and \(r'\) in the list, by the definition of a direction. There is no such point. So \(r\) and \(r'\) are adjacent, and Theorem 2.3 applies. \(\blacksquare\)

## 3. Branches

Let \(a\in T\). For \(x,y\in T\setminus\{a\}\) write \(x\approx y\) if \(xay\) does not hold.

**Lemma 3.1.** The relation \(\approx\) is an equivalence relation on \(T\setminus\{a\}\).

**Proof.** It is reflexive by (T0) and symmetric by (T1). Let \(x\approx y\) and \(y\approx z\). If \(xaz\) held, (T3) with the point \(y\ne a\) would give \(xay\) or \(zay\). \(\blacksquare\)

The classes of \(\approx\) are the *branches of \(T\) at \(a\)*. Two points lie in different branches exactly when \(a\) lies between them. In the vertex set of a tree, the branches at a vertex \(a\) are the vertex sets of the components that remain when \(a\) is removed: the path between two vertices avoids \(a\) exactly when \(a\) is not between them. On the real line there are two branches at every point.

For a branch \(H\) at \(a\) define a relation \(p_H\) on \(T\): it is the flow \(\bar a\) with the pairs \((x,a)\), \(x\in H\), removed. That is,
\[
\begin{gathered}
xy.p_H\iff y\in(x,a],\ \text{and not}\\
(y=a\ \text{and}\ x\in H).
\end{gathered}
\]
From the points of \(H\) the relation runs towards \(a\) and does not arrive; from the other points it runs to \(a\).

**Theorem 3.2.** Let \(a\in T\).

1. For every branch \(H\) at \(a\), \(p_H\) is a flow, and \(p_H\in L(a)\).
2. The map \(H\mapsto p_H\) is a bijection from the set of branches at \(a\) onto \(L(a)\). Its inverse sends \(p\in L(a)\) to the set of points \(x\ne a\) for which \(xa.p\) fails.

So the neighbours of \(\bar a\) in \(\Phi(T)\) correspond to the branches of \(T\) at \(a\).

**Proof.** (1) Write \(p=p_H\). Every relation \(xy.p\) is a relation \(xy.\bar a\), and \(\bar a\) is a flow.

(F1) holds because it holds for \(\bar a\).

(F2): let \(xzy\). Then \(xz.\bar a\) or \(yz.\bar a\). If \(z\ne a\), these are relations of \(p\). If \(z=a\), then \(x\) and \(y\) are different from \(a\) and lie in different branches, so one of them, say \(x\), is not in \(H\). Then \(xa.p\).

(F3): let \(xy.p\) and \(z\ne y\), and suppose \(xyz\) fails. Then \(zy.\bar a\), by (F3) for \(\bar a\). If \(zy.p\) fails, the pair \((z,y)\) is one of the removed pairs: \(y=a\) and \(z\in H\). Since \(xa.p\) holds, \(x\ne a\) and \(x\notin H\). So \(x\) and \(z\) lie in different branches, and \(xaz\). This is \(xyz\), which was assumed to fail. So \(zy.p\).

The flow \(p\) runs nowhere from \(a\), because \(\bar a\) does not. A branch is not empty, and for \(x\in H\) the relation \(xa.\bar a\) holds while \(xa.p\) fails; so \(p\ne\bar a\). Hence \(p\in L(a)\).

(2) *The map is injective*: for \(x\ne a\), the relation \(xa.p_H\) holds exactly when \(x\notin H\). So \(H\) is the set of points \(x\ne a\) for which \(xa.p_H\) fails.

*The map is surjective.* Let \(p\in L(a)\), and let \(H\) be the set of points \(x\ne a\) for which \(xa.p\) fails. Since \(p\ne\bar a\), the set \(H\) is not empty (Lemma 2.2 of the lesson on flows).

*\(H\) is a branch.* If \(x,y\in H\) and \(xay\), then (F2) gives \(xa.p\) or \(ya.p\), which both fail; so \(x\approx y\). Let \(x\in H\), \(y\ne a\) and \(x\approx y\). If \(ya.p\) held, (F3) with the point \(x\ne a\) would give \(yax\) or \(xa.p\), which both fail. So \(y\in H\).

*\(p=p_H\).* We compare the relations \(xy.p\) and \(xy.p_H\) for all pairs \((x,y)\). For \(x=a\) both fail. For \(x\ne a\) and \(y=a\), both hold exactly when \(x\notin H\). Let \(x\ne a\) and \(y\ne a\). Then \(xy.p_H\) means \(xya\). If \(xya\), then (F2) gives \(xy.p\) or \(ay.p\), and the second fails; so \(xy.p\). If \(xy.p\), then (F3) with the point \(a\ne y\) gives \(xya\) or \(ay.p\); so \(xya\). \(\blacksquare\)

**Corollary 3.3.** Let \(a\in T\). The number of neighbours of \(\bar a\) in \(\Phi(T)\) is the number of branches of \(T\) at \(a\). If \(T\) has more than one point, every point of \(\bar T\) has a neighbour, and \(\Phi(T)\) is not dense.

**Proof.** The first statement is Lemma 2.1 with Theorem 3.2. If \(T\) has a point other than \(a\), there is a branch at \(a\). \(\blacksquare\)

## 4. Examples

**Example 4.1** (the real line). By Example 6.1 of the lesson on stars, the flows on the real line other than the flows \(\bar x\) are the flows \(s^-\) and \(s^+\) for real \(s\), with \(F_p=\{s\}\), and two flows of type \((1,0)\), with \(F_p\) empty. So \(L(x)=\{x^-,x^+\}\): the point \(\bar x\) has two neighbours, one for each of the two branches at \(x\), and \(\langle x^-\,\bar x\,x^+\rangle\) by Lemma 2.2. The points \(x^-\) and \(x^+\) have the one neighbour \(\bar x\), and the two flows of type \((1,0)\) have no neighbour, by Corollary 2.4(1).

**Example 4.2** (the rational numbers). For an irrational number \(s\), the flow of Example 6.2 of the lesson on stars has type \((2,0)\). It has no neighbour in the completion of the rational numbers.

**Example 4.3** (finite trees). Let \(T\) be the vertex set of a finite tree. By Exercise 7.5 of the lesson on stars, the flows are the flows \(\bar v\) towards vertices and the flows of the edges, and for the flow \(p\) of an edge \(F_p\) is the set of the two ends of the edge. So the flow of an edge has two neighbours in \(\Phi(T)\), the flows towards its ends; and the neighbours of \(\bar v\) are the flows of the edges at \(v\). No other pairs are adjacent. The adjacent pairs of \(\Phi(T)\) are those of the tree in which every edge is divided by a new vertex in the middle.

## 5. Exercises

**5.1.** Let \(T\) be the interval \([0,1]\) of the real line. How many neighbours do the flows towards \(0\) and towards \(\tfrac12\) have in \(\Phi(T)\)?

**5.2.** Let \(H\) be a branch at \(a\) and \(x\in H\). Suppose that the arc \([x,a)\), directed with \(x\) as least point, is endless. Show that \(p_H\) is the flow of this directed arc.

**5.3.** Let \(F\) be a star and \(y\in F\). Show that \(T\setminus N(y)\) is a branch at \(y\), and that \(\operatorname{flow}(F)=p_H\) for this branch \(H\).

**5.4.** Show that a point \(a\) of \(T\) lies between two points of \(T\) if and only if \(\bar a\) lies between two points of \(\Phi(T)\).

**5.5.** Let \(T=\{x,y\}\) with the empty relation. Determine \(L(x)\) and \(L(y)\) and compare with Exercise 6.2 of the lesson on the completion.

## 6. Solutions

**5.1.** By Corollary 3.3 we count branches. For \(x,y>0\) the point \(0\) is not between \(x\) and \(y\): there is one branch at \(0\), and \(\bar 0\) has one neighbour. The point \(\tfrac12\) lies between \(x\) and \(y\) exactly when they lie on different sides of it: two branches, two neighbours.

**5.2.** Write \(p=p_H\). The set \([x,p)\) of Section 4 of the lesson on stars consists of \(x\) and the points \(y\) with \(xy.p\). Since \(x\in H\), these are the points of \((x,a]\) other than \(a\). So \([x,p)=[x,a)\). Both are directed with \(x\) as least point, so the directions are equal, and the arc is endless. By Theorem 5.1 of that lesson, Case 3, \(p\) is the flow of the directed arc \([x,p)\).

**5.3.** Let \(h\) be the foot map, and let \(x,x'\) be points outside \(N(y)\). By Lemma 2.4 of the lesson on stars, \([x,x']\subseteq[x,h(x)]\cup[x',h(x')]\), and these sets lie in \(N(h(x))\) and \(N(h(x'))\), which do not contain \(y\). So \(x\,y\,x'\) fails. If \(x\notin N(y)\) and \(x'\in N(y)\), \(x'\ne y\), then \(x'\,y\,x\) by Lemma 1.1 there. So \(H=T\setminus N(y)\), which is not empty because \(F\) has a second point, is a branch at \(y\). By Exercise 7.3 of that lesson, \(\operatorname{flow}(F)\) is \(\bar y\) with the pairs \((x,y)\), \(x\in H\), removed; this is \(p_H\).

**5.4.** If \(xay\), then \(\langle\bar x\bar a\bar y\rangle\) by (R5). Conversely let \(\langle q\,\bar a\,r\rangle\). By (R3), \(q\,a\,r\) in \(T\sqcup P\): every \(y\ne a\) has \(ya.q\) or \(ya.r\). Since \(q\ne\bar a\), there is \(y_0\ne a\) for which \(y_0a.q\) fails (Lemma 2.2 of the lesson on flows), and likewise \(y_1\ne a\) for which \(y_1a.r\) fails. Then \(y_1a.q\) holds. By (F3) for \(q\), with the point \(y_0\ne a\): \(y_1\,a\,y_0\) or \(y_0a.q\). So \(y_1\,a\,y_0\).

**5.5.** At \(x\) there is one branch, \(\{y\}\). The flow \(\bar x\) consists of the pair \((y,x)\); removing it gives the empty relation \(e\). So \(L(x)=\{e\}\), and in the same way \(L(y)=\{e\}\). The adjacent pairs of \(\Phi(T)\) are \(\bar x,e\) and \(e,\bar y\), and \(\langle\bar x\,e\,\bar y\rangle\) by Lemma 2.2: a path of three points with \(e\) in the middle, as found in that exercise.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 3. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
