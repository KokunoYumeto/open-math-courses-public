# Dense, complete and median pretrees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A pretree may have gaps of three kinds. Two points may be *adjacent*, with nothing between them. An arc may run towards a place where no point is. And three points may branch around a place where no point is, so that they have no median. A pretree is *dense* if it has no gaps of the first kind, *complete* if every arc is an interval, and *median* if every three points have a median. The real interval \([0,1]\) has all three properties.

This lesson studies how the three properties interact.

- In a dense pretree a half-open interval determines its open end (Lemma 1.2).
- Completeness and density together do **not** imply that medians exist. Proposition 3.2 gives a complete dense pretree, a tripod with a short segment next to the centre removed, in which three points have no median.
- In a dense *median* pretree, an interval \([x,y)\) that lies in \([x,z]\) has its end \(y\) in \([x,z]\) (Lemma 4.1). In a complete dense median pretree, every cut of an interval into two arcs is made at a point of the interval (Theorem 4.3). So the intervals of such a pretree are ordered sets without gaps.

The statements of Section 4 are those of Lemmas 2.8 and 2.10 of Bowditch's memoir [Bowditch], with the hypothesis "median" added; the example of Section 3 shows that the hypothesis cannot be dropped, and that a complete dense pretree need not be median.

We use [Betweenness and pretrees](betweenness-and-pretrees.md) throughout: the axioms, intervals, Lemmas 3.1 and 3.2, the finite trees of Corollary 4.5, arcs and directions, Corollary 5.3, Lemma 6.1 and Proposition 6.2.

## 1. Dense pretrees

A pretree \(T\) is *dense* if for any two distinct points \(x,y\) there is a point \(z\) with \(xzy\); that is, no two points are adjacent.

For three points \(x,y,z\) of a pretree and a finite tree \(\tau\) that contains them with the same betweenness (Corollary 4.5 of the first lesson), the *branch vertex* of \(x,y,z\) in \(\tau\) is the unique vertex \(m\) of \([x,y]_\tau\cap[y,z]_\tau\cap[z,x]_\tau\) (Lemma 6.1 there). It need not be a point of \(T\). By Lemma 1.1 there,
\[
\begin{gathered}
[x,y]_\tau=[x,m]_\tau\cup[m,y]_\tau,\\
[x,m]_\tau\cap[m,y]_\tau=\{m\},
\end{gathered}
\]
and the same for the other two pairs. So the three paths \([m,x]_\tau\), \([m,y]_\tau\), \([m,z]_\tau\) meet pairwise only in \(m\).

**Lemma 1.1.** Let \(x,y,z\) be points of a pretree, \(\tau\) a finite tree as above with branch vertex \(m\), and \(u\) a vertex of \(\tau\) that is a point of the pretree, with \(u\in[m,y]_\tau\) and \(u\ne m\). Then \(u\in[x,y]\), \(u\ne x\), and \(u\notin[x,z]\).

**Proof.** \(u\) lies on the path from \(x\) to \(y\), so \(u\in[x,y]\). It does not lie on \([x,m]_\tau\) or on \([m,z]_\tau\), which meet \([m,y]_\tau\) only in \(m\); so \(u\ne x\), and \(u\) is not on the path from \(x\) to \(z\). \(\blacksquare\)

**Lemma 1.2.** Let \(T\) be a dense pretree and \(x,y,z\in T\). If \([x,y)=[x,z)\), then \(y=z\).

**Proof.** Suppose \(y\ne z\). If \(y=x\), then \([x,y)\) is empty while \([x,z)\) contains \(x\); so \(y\ne x\), and likewise \(z\ne x\). Choose \(u\in(y,z)\) and a finite tree \(\tau\) containing \(x,y,z,u\) with the same betweenness; let \(m\) be the branch vertex of \(x,y,z\). The point \(u\) lies on \([y,z]_\tau=[y,m]_\tau\cup[m,z]_\tau\) and is not \(y\) or \(z\).

*If \(u\in[m,y]_\tau\) and \(u\ne m\)*: by Lemma 1.1, \(u\in[x,y)\) and \(u\notin[x,z]\), which contradicts \([x,y)=[x,z)\).

*If \(u\in[m,z]_\tau\) and \(u\ne m\)*: the same with \(y\) and \(z\) exchanged.

*If \(u=m\)*: then \(u\) is a median of \(x,y,z\) in \(T\), and \(u\ne y\). Choose \(v\in(u,y)\) and a finite tree \(\tau'\) containing \(x,y,z,u,v\). In \(\tau'\) the point \(u\) is again the branch vertex of \(x,y,z\), because it lies on all three paths. Now \(v\in[u,y]_{\tau'}\) and \(v\ne u\), so by Lemma 1.1, \(v\in[x,y)\) and \(v\notin[x,z]\), a contradiction. \(\blacksquare\)

## 2. Complete pretrees

Recall that an *arc* is a nonempty subset that is full and linear, and that the *intervals* of \(T\) are the sets \((x,y)\), \([x,y)\), \((x,y]\), \([x,y]\) with \(x,y\in T\), among them the single points \([x,x]\). Every interval is an arc (Corollary 5.3 of the first lesson and its proof).

A pretree is *complete* if every arc is an interval.

**Example 2.1.** The interval \([0,1]\) of the real line, with the betweenness of the line, is complete: its arcs are its nonempty convex subsets, and such a set is an interval whose ends are its infimum and supremum, which lie in \([0,1]\). It is also dense and median. The real line itself is dense and median but not complete: the arc \(\{x:x>0\}\) is not an interval. The rational numbers are dense and median but not complete (Exercise 7.1 of the first lesson).

**Lemma 2.2.** Let \(T\) be a dense pretree, \(A\) an arc that is an interval with ends \(p\ne p'\), and \(<\) a direction on \(A\). If \(A\) has a least point \(a\) for \(<\), then \(a\) is \(p\) or \(p'\), and \(A\) is \([a,x)\) or \([a,x]\), where \(x\) is the other end.

**Proof.** \(A\) lies in \([p,p']\), and the two directions of \(A\) are the restrictions of the two directions of \([p,p']\) (Proposition 5.2 of the first lesson; \(A\) has more than one point because \(T\) is dense). Let the direction be the one with \(p<p'\). If \(p\notin A\), then for every \(t\in A\) there is \(t'\in(p,t)\), which lies in \((p,p')\subseteq A\) and has \(t'<t\); so \(A\) has no least point. Hence \(p\in A\), and \(p\) is the least point of \([p,p']\), so \(a=p\). With the other direction, \(a=p'\). \(\blacksquare\)

## 3. A complete dense pretree without medians

*The tripod.* Let \(R\) consist of a point \(m\), the *centre*, and of the points \((i,t)\) with \(i\in\{1,2,3\}\) and \(0<t\le1\); the points \((i,t)\) with fixed \(i\) form the \(i\)th *leg*, and \(t\) is the *height* of \((i,t)\); the centre has height \(0\) and belongs to every leg. For \(a,b\in R\) the *segment* \([a,b]_R\) is defined as follows. If \(a\) and \(b\) lie on a common leg, it consists of the points of that leg whose height lies between the heights of \(a\) and \(b\), ends included. If \(a=(i,s)\) and \(b=(j,t)\) with \(i\ne j\), it consists of \(m\), the points of leg \(i\) of height at most \(s\), and the points of leg \(j\) of height at most \(t\). A point \(p\) *lies between* \(a\) and \(b\) if \(p\in[a,b]_R\) and \(p\ne a,b\).

**Lemma 3.1.** With this relation \(R\) is a pretree, and for \(a\ne b\) the closed interval of the pretree is \([a,b]_R\).

**Proof.** Let \(F\subseteq R\) be finite and \(V=F\cup\{m\}\). Join the points of \(V\) on each leg in the order of their heights, starting at \(m\). The result is a finite tree with vertex set \(V\), and the path between two of its vertices \(a,b\) has the vertex set \(V\cap[a,b]_R\). So on \(F\) the relation is the betweenness of a tree. The axioms of a pretree involve at most four points, and they hold for the vertices of a tree (Lemma 1.2 of the first lesson). \(\blacksquare\)

*The example.* Let
\[
T=R\setminus\bigl(\{m\}\cup\{(1,t):\ t<\tfrac12\}\bigr),
\]
with the betweenness of \(R\). So \(T\) consists of the points of leg 1 of height at least \(\frac12\), and of the points of legs 2 and 3 of positive height. Put
\[
\begin{gathered}
x=(1,1),\quad q=(1,\tfrac12),\\
y=(2,1),\quad z=(3,1).
\end{gathered}
\]

**Proposition 3.2.** The pretree \(T\) is dense and complete. In \(T\):

1. \([y,q)\subseteq[y,z]\), but \(q\notin[y,z]\);
2. \([y,z]\) is the disjoint union of the arcs \([y,q)\) and \([z,q)\), and neither of them is \([y,c)\), \([y,c]\), \((c,z]\) or \([c,z]\) for a point \(c\in[y,z]\);
3. the points \(x,y,z\) have no median.

**Proof.** The intervals of \(T\) are the intersections of \(T\) with the segments of \(R\). Let \(I_1=[\frac12,1]\) and \(I_2=I_3=(0,1]\) be the sets of heights that occur on the three legs of \(T\).

*Dense.* Let \(a\ne b\) in \(T\). If they lie on one leg \(i\), the heights strictly between theirs lie in \(I_i\). If they lie on different legs, one of the legs is leg 2 or leg 3, and the points of that leg below the given point lie in \(T\) and between \(a\) and \(b\).

*Complete.* Let \(A\) be an arc of \(T\). It does not contain points \(a_1,a_2,a_3\) of three different legs, since none of them would lie between the other two. For each leg \(i\) that \(A\) meets, let \(J_i\subseteq I_i\) be the set of heights of the points of \(A\) on leg \(i\). Since \(A\) is full, \(J_i\) is convex.

Suppose \(A\) meets two legs \(i\ne j\). For \(a\in A\) on leg \(i\) and \(b\in A\) on leg \(j\), all points of \(T\) on these legs below \(a\) and below \(b\) lie between \(a\) and \(b\), hence in \(A\). So \(J_i\) consists of all heights in \(I_i\) below, or up to, its supremum \(\sigma\), and \(J_j\) of all heights in \(I_j\) below, or up to, its supremum \(\rho\); and \(\sigma\in I_i\), \(\rho\in I_j\). Then \(A\) is the interval of \(T\) with the ends \((i,\sigma)\) and \((j,\rho)\), each end included or not according as the supremum is attained.

Suppose \(A\) lies on one leg \(i\), and let \(\alpha\le\beta\) be the infimum and the supremum of \(J_i\). If \(\alpha\in I_i\), then \(A\) is the interval with the ends \((i,\alpha)\) and \((i,\beta)\), each included or not. If \(\alpha\notin I_i\), then \(i\) is \(2\) or \(3\) and \(\alpha=0\); now the points of \(T\) between \(q\) and \((i,\beta)\) are exactly the points of leg \(i\) of height less than \(\beta\), because the segment of \(R\) from \(q\) to \((i,\beta)\) meets \(T\) on leg 1 only in \(q\). So \(A\) is \((q,(i,\beta))\) or \((q,(i,\beta)]\).

*(1).* \([y,q)\) consists of all points of leg 2 in \(T\), and \([y,z]\) of all points of legs 2 and 3 in \(T\). The point \(q\) lies on leg 1.

*(2).* Likewise \([z,q)\) consists of the points of leg 3. An interval \([y,c)\) or \([y,c]\) with \(c\in[y,z]\) either omits points of leg 2, if \(c\) lies on leg 2 and \(c\ne y\) or the interval is \([y,y)\), or contains points of leg 3, if \(c\) lies on leg 3; and \([y,y]\) is a single point. So it is not the set of points of leg 2. The same holds for leg 3.

*(3).* \([x,y]\cap[x,z]\) consists of the points of leg 1 in \(T\), and none of them lies in \([y,z]\). \(\blacksquare\)

In \(T\) the two legs through \(y\) and \(z\) run towards the removed centre, and the nearest point of \(T\) in that direction, \(q\), lies off the interval \([y,z]\). Completeness asks only that an arc be an interval of \(T\); it does not ask that the ends of that interval lie in a given interval containing the arc.

## 4. Median pretrees: ends and cuts

**Lemma 4.1.** Let \(T\) be a dense median pretree and \(x,y,z\in T\). If \([x,y)\subseteq[x,z]\), then \(y\in[x,z]\).

**Proof.** Let \(c=\operatorname{med}(x,y,z)\) and suppose \(y\notin[x,z]\). Then \(c\ne y\), because \(c\in[x,z]\). Choose \(v\in(c,y)\). Since \(c\in[x,y]\), Lemma 3.2 of the first lesson gives \([c,y]\subseteq[x,y]\); so \(v\in[x,y)\), and by assumption \(v\in[x,z]\). Since \(c\in[y,z]\), also \([c,y]\subseteq[y,z]\), so \(v\in[y,z]\). Thus \(v\) lies in \([x,y]\cap[y,z]\cap[z,x]\): it is a median of \(x,y,z\). By the uniqueness of medians, \(v=c\). But \(v\in(c,y)\). \(\blacksquare\)

By Proposition 3.2(1) the lemma fails in dense pretrees that are not median, even complete ones.

Let \(a\ne b\) be points of a pretree. A *cut* of \([a,b]\) is a partition of \([a,b]\) into two arcs \(A\) and \(B\). An arc that contains \(a\) and \(b\) contains \([a,b]\); so one of the two arcs contains \(a\) and the other \(b\), and we name them so that \(a\in A\) and \(b\in B\).

**Lemma 4.2.** Let \([a,b]=A\cup B\) be a cut with \(a\in A\), \(b\in B\), and let \(<\) be the direction of \([a,b]\) with \(a<b\). If \(s\in A\) and \(t\in B\), then \(s<t\).

**Proof.** If \(t<s\), then \(t\in[a,s)\) by Corollary 5.3 of the first lesson, and \([a,s]\subseteq A\) because \(A\) is full. So \(t\in A\), which is false. \(\blacksquare\)

**Theorem 4.3** (cuts are made at points). Let \(T\) be a complete dense median pretree, \(a\ne b\) in \(T\), and \([a,b]=A\cup B\) a cut with \(a\in A\), \(b\in B\). Then there is a point \(c\in[a,b]\) such that
\[
\begin{gathered}
A=[a,c],\ B=(c,b]\qquad\text{or}\\
A=[a,c),\ B=[c,b].
\end{gathered}
\]

**Proof.** Let \(<\) be the direction of \([a,b]\) with \(a<b\). By Lemma 4.2, \(a\) is the least point of \(A\) and \(b\) the greatest point of \(B\).

*The form of \(A\).* If \(A=\{a\}\), then \(A=[a,a]\) and \(B=(a,b]\), and \(c=a\) works. Otherwise \(A\) is an interval with two different ends, because \(T\) is complete, and by Lemma 2.2 it is \([a,x]\) or \([a,x)\) for some \(x\in T\), \(x\ne a\). In the first case \(x\in A\subseteq[a,b]\). In the second case \([a,x)\subseteq[a,b]\), and Lemma 4.1 gives \(x\in[a,b]\). Since \(x\in[a,b]\), the interval \([a,x]\) of \(T\) is the set of \(t\in[a,b]\) with \(t\le x\) (Corollary 5.3 of the first lesson). So
\[
\begin{gathered}
A=\{t\in[a,b]:t\le x\}\quad\text{or}\\
A=\{t\in[a,b]:t<x\}.
\end{gathered}
\]

*The form of \(B\).* In the same way, with the reverse direction, either \(B=\{b\}\), or there is \(w\in[a,b]\) with \(B=\{t:t\ge w\}\) or \(B=\{t:t>w\}\). The case \(B=\{b\}\) has \(A=[a,b)\) and \(c=b\).

*Conclusion.* If \(x<w\), a point \(s\) with \(x<s<w\), which exists because \(T\) is dense, lies in neither \(A\) nor \(B\). If \(w<x\), a point \(s\) with \(w<s<x\) lies in both. So \(x=w\). This point lies in exactly one of \(A\) and \(B\), which gives the two cases, with \(c=x\). \(\blacksquare\)

By Proposition 3.2(2) the theorem fails without the hypothesis that \(T\) is median.

**Corollary 4.4.** Let \(T\) be a complete dense median pretree and \(a\ne b\). With the direction \(a<b\), the ordered set \([a,b]\) has the following properties: between any two points there is a third; and every nonempty subset \(Y\) has a least upper bound in \([a,b]\).

**Proof.** The first property is density. For the second, let \(A\) be the set of points \(s\in[a,b]\) such that \(s\le t\) for some \(t\in Y\), and \(B\) its complement in \([a,b]\). If \(B\) is empty, then \(b\) is the least upper bound of \(Y\): it is an upper bound, and it lies in \(A\), so \(b\le t\) for some \(t\in Y\), that is, \(b\in Y\). Otherwise both \(A\) and \(B\) are arcs: they are nonempty; subsets of \([a,b]\) are linear; and they are full, because \(A\) contains with each point all smaller points of \([a,b]\) and \(B\) all larger ones, while the interval between two points of \([a,b]\) consists of the points between them in the order. By Theorem 4.3 there is \(c\) with \(A=\{s\le c\}\) or \(A=\{s<c\}\). In both cases \(c\) is an upper bound of \(Y\subseteq A\), and no \(c'<c\) is one: a point \(s\) with \(c'<s<c\) lies in \(A\), so \(s\le t\) for some \(t\in Y\), and \(c'<t\). \(\blacksquare\)

*A remark on the literature.* Lemma 2.11 of [Bowditch] asserts that every complete dense pretree is median, and Lemmas 2.8 and 2.10 there state Lemma 4.1 and Theorem 4.3 without the hypothesis "median". Proposition 3.2 is a counterexample to these three statements. In the proof of Lemma 2.8 there, a point \(w\) with \(w\in(y,z)\) and \(w\in(z,x)\) is taken to be the median of \(x,y,z\); this also requires \(w\in[x,y]\), which in the example fails for every \(w\).

## 5. Exercises

**5.1.** Show that the tripod \(R\) of Section 3 is dense, complete and median.

**5.2.** Let \(T\) be the pretree of Proposition 3.2. Find all pairs \((a,b)\) with \(a\ne b\) for which the cut property of Theorem 4.3 holds for every cut of \([a,b]\).

**5.3.** Show that a finite pretree with more than one point is complete and not dense, and that it is median if and only if it is the vertex set of a finite tree with the betweenness of the tree.

**5.4.** Let \(T\) be a dense pretree and \(x\ne y\). Show that \(x\) is the only point of \([x,y)\) that does not lie between two points of \([x,y)\), and deduce that \([x,y)=[x',y')\) implies \(x=x'\) and \(y=y'\).

**5.5.** In the proof of Theorem 4.3, where is each of the three hypotheses used?

## 6. Solutions

**5.1.** Dense: as for \(T\), with all heights allowed. Median: for three points on one leg the median is the one of middle height; for two points on one leg and one on another, it is the lower of the two; for points on three legs it is \(m\); in each case one checks the three segments. Complete: as in the proof of Proposition 3.2, an arc meets at most two legs; if it meets two, it is the interval between the points at the suprema of the heights, ends included or not; if it lies on one leg, it is the interval between the points at the infimum and the supremum of the heights, where the infimum \(0\) now corresponds to the point \(m\in R\).

**5.2.** The property fails exactly when \(a\) and \(b\) lie on legs 2 and 3, one on each: then \([a,b]\) is cut into its parts on the two legs, as in Proposition 3.2(2). If \(a\) and \(b\) lie on one leg, the heights of the points of \([a,b]\) form a closed interval of real numbers, and every cut of it is made at a point. Let \(a\) lie on leg 1 and \(b=(i,t)\) on leg \(i\in\{2,3\}\). Then \([a,b]\) consists of the points of leg 1 from \(a\) down to \(q\), followed, in the direction from \(a\) to \(b\), by the points of leg \(i\) of heights in \((0,t]\) in increasing order. Let \([a,b]=A\cup B\) be a cut. If \(B\) contains a point of leg 1, the cut is a cut of the closed interval of heights on leg 1 and is made at a point. If \(A\) contains a point of leg \(i\), the heights of the points of \(A\) on leg \(i\) form the set \((0,\rho)\) or \((0,\rho]\) with \(0<\rho\le t\), and the cut is made at \((i,\rho)\). Otherwise \(A\) is the part on leg 1 and \(B\) the part on leg \(i\), and the cut is made at \(q\): \(A=[a,q]\) and \(B=(q,b]\).

**5.3.** In a finite pretree \(F\) let \(A\) be an arc, and \(<\) a direction on it if it has more than one point (Proposition 5.2 of the first lesson). Let \(p\) be its least and \(p'\) its greatest point. Then \(A\subseteq[p,p']\) by the definition of a direction, and \([p,p']\subseteq A\) because \(A\) is full. So \(A\) is an interval. Two points at the ends of an interval with the fewest points are adjacent, so \(F\) is not dense. If \(F\) is the vertex set of a tree, it is median (Lemma 6.1 of the first lesson). Conversely let \(F\) be median and \(\tau\) the tree of Theorem 4.1 of the first lesson. A vertex of \(\tau\) outside \(F\) is a maximal clique with three points \(u,v,w\) pairwise adjacent; their median would lie in \([u,v]\cap[v,w]\cap[w,u]\). Since the points are pairwise adjacent, this is \(\{u,v\}\cap\{v,w\}\cap\{w,u\}\), which is empty. So \(\tau\) has no vertices outside \(F\).

**5.4.** In the direction of \([x,y]\) with \(x<y\), \(x\) is the least point of \([x,y)\), so it does not lie between two of its points. A point \(t\) with \(x<t<y\) lies between \(x\) and a point of \((t,y)\), which exists by density. So \(x\) is determined by the set \([x,y)\), and \(x=x'\). Then \(y=y'\) by Lemma 1.2.

**5.5.** Completeness makes \(A\) and \(B\) intervals of \(T\). Density is used in Lemma 2.2, to see that the least point of \(A\) is one of its ends, in Lemma 4.1, and at the end, to find a point between \(x\) and \(w\). The median is used in Lemma 4.1, to see that the open end of \(A\) lies in \([a,b]\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 2. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
