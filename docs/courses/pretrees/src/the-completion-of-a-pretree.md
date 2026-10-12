# The completion of a pretree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Every pretree \(T\) sits inside a complete median pretree. This lesson constructs one: its points are the flows on \(T\), a point \(x\in T\) is represented by the flow \(\bar x\) towards \(x\), and the betweenness of three flows is read off from the points of \(T\) that lie between them. The result (Theorems 3.1, 4.1 and 5.2) is that the set \(\Phi(T)\) of all flows, with this betweenness, is a pretree, that every three of its points have a median, and that every arc in it is an interval. Of the three kinds of gaps described in [Dense, complete and median pretrees](dense-complete-and-median-pretrees.md), \(\Phi(T)\) has none of the second and third kind; it may still have adjacent points.

The construction and the order of the argument are those of Section 3 of [Bowditch] (Lemmas 3.14 to 3.18 and Theorem 3.19); the proofs are written out in full.

We use the earlier lessons of the course: [Betweenness and pretrees](betweenness-and-pretrees.md) for the axioms (T0) to (T3), Lemmas 2.3, 3.1 and 3.2 and uniqueness of medians; [Flows on a pretree](flows-on-a-pretree.md) for the pretree \(T\sqcup P\); and [Directed arcs and suprema](directed-arcs-and-suprema.md) for the flow of a directed arc and for Theorem 4.3 there.

## 1. Intervals between flows

Throughout, \(T\) is a pretree, \(P\) the set of its flows, and \(T\sqcup P\) the pretree of Theorem 4.1 of the lesson on flows. Recall: a point of \(P\) is never between two points; for \(x,y\in T\) and \(p\in P\), \(xyp\) means \(xy.p\); and for \(p\ne q\) in \(P\), \(pxq\) means that every \(y\ne x\) has \(yx.p\) or \(yx.q\). Intervals such as \((p,q)\) are taken in \(T\sqcup P\). For \(p,q\in P\) they consist of points of \(T\):
\[
(p,q)\subseteq T .
\]
Letters \(p,q,r,s,m\) denote flows, and \(a,x,y,z\) points of \(T\).

**Lemma 1.1.**

1. If \(p\ne q\), then \((p,q)\) is not empty.
2. If \(p\ne\bar x\), then \(p\,x\,\bar x\), and \((p,\bar x)=(p,x]\).
3. For \(a,x\in T\): \([a,\bar x)=[a,x]\).
4. For \(x\ne y\): \((\bar x,\bar y)=[x,y]\).

**Proof.** (1) Suppose \((p,q)\) is empty and let \(x,y\in T\) with \(xyp\). By (T3) with the point \(q\ne y\): \(xyq\) or \(pyq\); the second would put \(y\) into \((p,q)\). So \(xy.p\) implies \(xy.q\), and conversely. The two flows are the same relation.

(2) The relation \(p\,x\,\bar x\) is Theorem 4.1(3) of the lesson on flows, which also says that \(x\) and \(\bar x\) are adjacent. So \(x\in(p,\bar x)\), and by Lemma 3.2 of the first lesson \((p,\bar x)=(p,x]\cup[x,\bar x)=(p,x]\).

(3) For \(a=x\) both sides are \(\{x\}\). For \(a\ne x\), \(a\,x\,\bar x\) holds because \(ax.\bar x\); as in (2), \([a,\bar x)=[a,x]\cup[x,\bar x)=[a,x]\).

(4) By (2), applied to \(p=\bar y\), we have \(x\in(\bar x,\bar y)\). Splitting at \(x\): \((\bar x,\bar y)=(\bar x,x]\cup[x,\bar y)=\{x\}\cup[x,y]\) by (3). \(\blacksquare\)

**Lemma 1.2.** Let \(p,q,r\in P\).

1. \((p,q)\subseteq(p,r)\cup(r,q)\).
2. The following are equivalent: \((p,q)=(p,r)\cup(r,q)\); \((p,r)\subseteq(p,q)\); \((q,r)\subseteq(p,q)\).
3. If \((p,r)\cap(r,q)=\varnothing\), then \((p,q)=(p,r)\cup(r,q)\).
4. Suppose \((p,q)=(p,r)\cup(r,q)\), and let \(x\in(p,r)\), \(y\in(r,q)\) with \(x\ne y\). Then \(pxyq\).

**Proof.** (1) By Lemma 3.1 of the first lesson, \([p,q]\subseteq[p,r]\cup[r,q]\); now intersect with \(T\).

(2) The first statement implies the other two. If \((p,r)\subseteq(p,q)\), then by (1), \((q,r)\subseteq(q,p)\cup(p,r)\subseteq(p,q)\); in the same way the third implies the second. The second and the third together with (1) give the first.

(3) Let \(x\in(p,r)\). By (T3) with the point \(q\): \(pxq\) or \(rxq\); the second is excluded. So \((p,r)\subseteq(p,q)\); apply (2).

(4) Both points lie in \((p,q)\), so by Lemma 2.3(3) of the first lesson \(pxyq\) or \(pyxq\). In the second case \(y\in(p,x)\subseteq(p,r)\) and \(x\in(y,q)\subseteq(r,q)\), by Lemma 3.2 of the first lesson. So \(x\) and \(y\) both lie in \((p,r)\cap(r,q)\), hence in \([p,q]\cap[q,r]\cap[r,p]\): they are medians of \(p,q,r\) in \(T\sqcup P\), and \(x=y\) by the uniqueness of medians. \(\blacksquare\)

**Lemma 1.3.** Let \((A,<)\) be an endless directed arc of \(T\) with a least point \(a\), and \(m=\operatorname{flow}(A)\in P\). Then \(A=[a,m)\).

**Proof.** For \(y\in T\), \(a\,y\,m\) means \(ay.A\), which holds exactly when \(y\in A\) and \(a<y\) (Proposition 2.4(4) of the lesson on directed arcs). \(\blacksquare\)

## 2. The betweenness of flows

Let \(\bar T=\{\bar x\mid x\in T\}\subseteq P\).

**Definition 2.1.** For \(p,q,r\in P\) we write \(\langle prq\rangle\) if \(p,q,r\) are distinct and one of the following holds:

- \(r=\bar x\) for some \(x\in T\), and \(pxq\);
- \(r\notin\bar T\), and \((p,r)\cap(r,q)=\varnothing\).

The set \(P\) with this ternary relation is denoted \(\Phi(T)\), or \(\Phi\).

In the first case \(x\) is determined by \(r\). The definition is symmetric in \(p\) and \(q\).

**Lemma 2.2.** Let \(p,q,r\in P\) be distinct.

1. If \((p,r)\cap(r,q)=\varnothing\), then \(r\notin\bar T\), and so \(\langle prq\rangle\).
2. If \(\langle prq\rangle\), then \((p,q)=(p,r)\cup(r,q)\).
3. For \(x,y,z\in T\): \(\langle\bar x\bar y\bar z\rangle\) if and only if \(xyz\). So \(x\mapsto\bar x\) identifies \(T\) with the subset \(\bar T\) of \(\Phi\), with its betweenness.

**Proof.** (1) If \(r=\bar x\), then \(x\) lies in \((p,r)\) and in \((r,q)\) by Lemma 1.1(2).

(2) If \(r\notin\bar T\), this is Lemma 1.2(3). If \(r=\bar x\) with \(pxq\), then \((p,q)=(p,x]\cup[x,q)\) by Lemma 3.2 of the first lesson, and \((p,x]=(p,r)\), \([x,q)=(r,q)\) by Lemma 1.1(2).

(3) The map is injective. For distinct \(x,y,z\), \(\langle\bar x\bar y\bar z\rangle\) means \(\bar x\,y\,\bar z\), that is, \(y\in(\bar x,\bar z)=[x,z]\) by Lemma 1.1(4); since \(y\ne x,z\), this is \(xyz\). \(\blacksquare\)

## 3. The pretree axioms

**Theorem 3.1.** \(\Phi(T)\) is a pretree.

**Proof.** (T0) and (T1) hold by the definition.

(T2): suppose \(\langle prq\rangle\) and \(\langle pqr\rangle\). *If \(q=\bar x\) and \(r=\bar y\)*, then \(p\,y\,\bar x\) and \(p\,x\,\bar y\). By Lemma 1.1(2), \(y\in(p,x]\) and \(x\in(p,y]\); since \(x\ne y\), \(pyx\) and \(pxy\), against (T2) in \(T\sqcup P\). *If \(r\notin\bar T\)*: from \(\langle prq\rangle\), \((p,r)\cap(r,q)=\varnothing\); from \(\langle pqr\rangle\) and Lemma 2.2(2), \((q,r)\subseteq(p,r)\). So \((q,r)=\varnothing\), and \(q=r\) by Lemma 1.1(1), a contradiction. *If \(q\notin\bar T\)*: the same with \(q\) and \(r\) exchanged.

(T3): let \(\langle prq\rangle\) and \(s\ne r\); we must show \(\langle prs\rangle\) or \(\langle qrs\rangle\). If \(s=p\) or \(s=q\), one of them is \(\langle prq\rangle\) itself. Let \(s\) differ from \(p,q,r\). *If \(r=\bar x\)*, then \(pxq\), and (T3) in \(T\sqcup P\) gives \(pxs\) or \(qxs\). *If \(r\notin\bar T\)*, then \((p,r)\cap(q,r)=\varnothing\). Suppose neither \(\langle prs\rangle\) nor \(\langle qrs\rangle\). By Lemma 2.2(1) there are \(x\in(p,r)\cap(r,s)\) and \(y\in(q,r)\cap(r,s)\), and \(x\ne y\). Both lie in \((r,s)\), so \(rxys\) or \(ryxs\) by Lemma 2.3(3) of the first lesson. If \(rxy\): since \(y\in(r,q)\), we get \(x\in(r,y)\subseteq(r,q)\), so \(x\in(p,r)\cap(q,r)\). If \(ryx\): in the same way \(y\in(r,x)\subseteq(r,p)\), so \(y\in(p,r)\cap(q,r)\). Both are impossible. \(\blacksquare\)

Intervals of \(\Phi\) are written \([p,q]_\Phi\), \((p,q)_\Phi\) and so on.

## 4. Medians

**Theorem 4.1.** Every three points of \(\Phi(T)\) have a median.

**Proof.** Let \(p,q,r\in P\). If two of them are equal, that point is a median. Let them be distinct.

*Case 1: one of the sets \((p,r)\cap(r,q)\), \((r,q)\cap(q,p)\), \((q,p)\cap(p,r)\) is empty.* If the first is empty, then \(\langle prq\rangle\) by Lemma 2.2(1), and \(r\) lies in \([p,q]_\Phi\cap[q,r]_\Phi\cap[r,p]_\Phi\). Similarly in the other cases.

*Case 2: there is a point \(x\in(q,p)\cap(p,r)\cap(r,q)\).* If \(\bar x=r\), then \(pxq\) gives \(\langle prq\rangle\), and \(r\) is a median; likewise if \(\bar x\) is \(p\) or \(q\). Otherwise \(\bar x\) differs from \(p,q,r\), and \(pxq\), \(qxr\), \(rxp\) give \(\langle p\bar xq\rangle\), \(\langle q\bar xr\rangle\), \(\langle r\bar xp\rangle\): \(\bar x\) is a median.

*Case 3: the three sets of Case 1 are nonempty, and \((q,p)\cap(p,r)\cap(r,q)=\varnothing\).* Define a relation \(s\) on \(T\): \(xy.s\) holds if at least two of the relations \(xyp\), \(xyq\), \(xyr\) hold.

*\(s\) is a flow.* (F1): if \(xy.s\) and \(yx.s\), then for one of the three flows, say \(p\), both \(xyp\) and \(yxp\) hold, against (T2). (F2): let \(xzy\). By (T3) in \(T\sqcup P\), for each of the three flows \(p'\in\{p,q,r\}\): \(xzp'\) or \(yzp'\). So for two of them the same alternative holds, and \(xz.s\) or \(yz.s\). (F3): let \(xy.s\) and \(z\ne y\), say \(xyp\) and \(xyq\). If \(xyz\) fails, (T3) gives \(pyz\) and \(qyz\), so \(zy.s\).

So \(s\in P\), and \(xys\) holds exactly when \(xy.s\).

*\((p,s)\subseteq(p,q)\cap(p,r)\).* Let \(pxs\) and \(y\in T\), \(y\ne x\). By (T3): \(yxp\) or \(yxs\). In the second case two of \(yxp\), \(yxq\), \(yxr\) hold, so one of \(yxp\), \(yxq\) holds. Hence \(yx.p\) or \(yx.q\) for every \(y\ne x\), which is \(pxq\). In the same way \(pxr\).

*\(s\) differs from \(p,q,r\), and the sets \((p,s)\), \((q,s)\), \((r,s)\) are pairwise disjoint.* By the last step and its analogues,
\[
\begin{gathered}
(p,s)\subseteq(q,p)\cap(p,r),\\
(q,s)\subseteq(r,q)\cap(q,p),\\
(r,s)\subseteq(p,r)\cap(r,q).
\end{gathered}
\]
The intersection of any two of the right sides is the triple intersection, which is empty. If \(s=p\), the last two inclusions read \((q,p)\subseteq(r,q)\) and \((r,p)\subseteq(r,q)\); then \((q,p)\cap(p,r)\) lies in the triple intersection and is empty, against the assumption of Case 3. Likewise \(s\ne q,r\).

By Lemma 2.2(1), \(\langle psq\rangle\), \(\langle qsr\rangle\) and \(\langle rsp\rangle\). So \(s\) is a median. \(\blacksquare\)

In Case 3 the median is the flow that goes wherever two of the three flows go: it points to the place around which \(p,q,r\) branch.

## 5. Completeness

**Lemma 5.1.** If \(\langle pqr\rangle\), \(\langle qrs\rangle\), \(\langle pqs\rangle\) and \(\langle prs\rangle\) hold, then \((p,q)\cap(r,s)=\varnothing\).

**Proof.** Let \(x\in(p,q)\cap(r,s)\). From \(\langle pqr\rangle\) and Lemma 2.2(2), \((p,q)\subseteq(p,r)\), so \(x\in(p,r)\cap(r,s)\). Since \(\langle prs\rangle\), the second case of Definition 2.1 is excluded, so \(r=\bar z\) with \(pzs\). By Lemma 1.1(2), \((p,r)=(p,z]\) and \((r,s)=[z,s)\), which meet only in \(z\). So \(x=z\) and \(r=\bar x\). The same argument with the four points in the reverse order gives \(q=\bar x\). But \(q\ne r\). \(\blacksquare\)

**Theorem 5.2.** \(\Phi(T)\) is complete.

**Proof.** By Theorem 4.3 of the lesson on directed arcs it suffices to show that every directed arc \((B,\prec)\) of \(\Phi\) has a supremum in \(\Phi\). If \(B\) has a maximum, that is one. Let \(B\) be endless.

*Step 1: reduction.* \(B\) contains a point of \(\bar T\): take \(p\ne q\) in \(B\) and \(a\in(p,q)\); if \(\bar a\) is \(p\) or \(q\) it lies in \(B\), and otherwise \(paq\) gives \(\langle p\bar aq\rangle\), so \(\bar a\in B\) because \(B\) is full. A supremum of the final segment of the elements \(\succeq\bar a\) is a supremum of \(B\). So we may assume that \(\bar a\) is the least point of \(B\). Then for \(p,q\in B\setminus\{\bar a\}\): \(p\prec q\) if and only if \(\langle\bar apq\rangle\).

*Step 2: an arc of \(T\).* For \(p\ne\bar a\), Lemma 1.1(2) gives \((\bar a,p)=[a,p)\). If \(p\prec q\) in \(B\), then \([a,p)\subseteq[a,q)\): for \(p=\bar a\) the left side is \(\{a\}\), and otherwise \(\langle\bar apq\rangle\) and Lemma 2.2(2) give \((\bar a,p)\subseteq(\bar a,q)\). Let
\[
A=\bigcup_{p\in B}[a,p)\subseteq T .
\]
Each \([a,p)\) is full and linear, and they form a chain under inclusion; so \(A\) is an arc of \(T\). We direct it so that \(a\) is its least point. For \(p\preceq q\) in \(B\) we have \((p,q)\subseteq(\bar a,q)\subseteq A\), again by Lemma 2.2(2).

*Step 3: \(A\) is endless.* Suppose \(A\) has a greatest point \(b\). Then \(b\in[a,p)\) for some \(p\in B\), and so \(A=[a,b]\subseteq[a,p)\subseteq A\). Choose \(q,r,s\in B\) with \(p\prec q\prec r\prec s\). The four points \(\bar a,q,r,s\) are in a row in \(\Phi\), so \((\bar a,q)\cap(r,s)=\varnothing\) by Lemma 5.1. But \((\bar a,q)=[a,q)=A\), and \((r,s)\subseteq A\). So \((r,s)\) is empty, and \(r=s\) by Lemma 1.1(1), a contradiction.

*Step 4: the candidate.* By Lemma 1.3 there is \(m\in P\) with \(A=[a,m)\). Since \([a,\bar a)=\{a\}\) and \(A\) is endless, \(m\ne\bar a\); so \(A=(\bar a,m)\). Moreover \(m\notin B\): otherwise choose \(p,q\in B\) with \(m\prec p\prec q\); then \(\bar a,m,p,q\) are in a row, so \((\bar a,m)\cap(p,q)=\varnothing\) by Lemma 5.1, while \((p,q)\subseteq A=(\bar a,m)\); so \((p,q)=\varnothing\) and \(p=q\).

We show that \(B=[\bar a,m)_\Phi\). Then \(m\) is a supremum of \(B\), by definition.

*Step 5: \([\bar a,m)_\Phi\subseteq B\).* Let \(\langle\bar apm\rangle\).

If \(p=\bar x\), then \(\bar a\,x\,m\), so \(x\in A\), and \(x\in[a,q)=(\bar a,q)\) for some \(q\in B\). If \(q=p\), then \(p\in B\). Otherwise \(\bar a\,x\,q\) gives \(\langle\bar apq\rangle\), and \(p\in B\) because \(B\) is full.

Let \(p\notin\bar T\). Then \((\bar a,p)\cap(p,m)=\varnothing\) and \((\bar a,m)=(\bar a,p)\cup(p,m)\). Choose \(y\in(p,m)\). Since \(y\in A\), there is \(q\in B\) with \(\bar a\,y\,q\). If \(q=p\), then \(p\in B\). Otherwise we show \((\bar a,p)\cap(p,q)=\varnothing\); then \(\langle\bar apq\rangle\) by Lemma 2.2(1), and \(p\in B\). Let \(x\in(\bar a,p)\). By Lemma 1.2(4), \(\bar a\,x\,y\,m\); in particular \(\bar a\,x\,y\) and \(xym\). From \(\bar a\,x\,y\) and \(\bar a\,y\,q\), Lemma 2.3(2) of the first lesson, read from \(q\), gives \(xyq\). Now \(qxm\) is impossible: by (T3) it would give \(yxq\) or \(yxm\), against \(xyq\), \(xym\) and (T2). And \(pxm\) is impossible, because \(x\in(\bar a,p)\) and \((\bar a,p)\cap(p,m)=\varnothing\). So \(pxq\) is impossible: by (T3) with the point \(m\) it would give \(pxm\) or \(qxm\). Hence \(x\notin(p,q)\).

*Step 6: \(B\subseteq[\bar a,m)_\Phi\).* Let \(p\in B\), \(p\ne\bar a\). We show \(\langle\bar apm\rangle\); note \(p\ne m\).

If \(p=\bar x\): then \(x\ne a\), and \(x\in[a,x]=[a,p)\subseteq A=(\bar a,m)\), so \(\bar a\,x\,m\).

Let \(p\notin\bar T\). We show \((\bar a,p)\cap(p,m)=\varnothing\) and apply Lemma 2.2(1). Suppose \(x\) lies in both sets. Since \(A\) is endless there is \(y\in A\) above \(x\), so \(\bar a\,x\,y\) and \(\bar a\,x\,y\,m\). There is \(q\in B\) with \(y\in(\bar a,q)\), and we may take \(p\prec q\). As in Step 5, \(xyq\). From \(pxm\) and \(xym\), Lemma 2.3(2) of the first lesson gives \(pxy\); from \(pxy\) and \(xyq\), Lemma 2.3(1) there gives \(pxq\). So \(x\in(\bar a,p)\cap(p,q)\). But \(\langle\bar apq\rangle\) with \(p\notin\bar T\) says that this set is empty. \(\blacksquare\)

**Corollary 5.3.** For every pretree \(T\), the set \(\Phi(T)\) of its flows is a complete median pretree, and \(x\mapsto\bar x\) is an injective map \(T\to\Phi(T)\) that preserves and reflects betweenness.

This is Theorems 3.1, 4.1, 5.2 and Lemma 2.2(3).

## 6. Exercises

**6.1.** Let \(T\) consist of one point \(x\). Show that \(\Phi(T)\) is a single point.

**6.2.** Let \(T=\{x,y\}\) with the empty relation. Find all flows on \(T\) and determine \(\Phi(T)\).

**6.3.** Let \(T=\{x,y,z\}\) with the empty relation, and \(e\) the empty flow (Exercise 5.3 of the lesson on flows). Show that in \(\Phi(T)\) the point \(e\) is the median of \(\bar x,\bar y,\bar z\), and that \(\Phi(T)\) is the vertex set of the tree with centre \(e\) and three further vertices.

**6.4.** In the proof of Theorem 4.1, Case 3, where is the assumption that the three pairwise intersections are nonempty used?

**6.5.** Show that for \(p\ne q\) in \(\Phi(T)\) and \(x\in(p,q)\) with \(\bar x\ne p,q\), the point \(\bar x\) lies in \((p,q)_\Phi\). Deduce that \(\bar T\) meets every interval \((p,q)_\Phi\) with \(p,q\notin\bar T\), \(p\ne q\).

## 7. Solutions

**6.1.** A flow on a one-point pretree is a relation on \(\{x\}\) in which \(xx.p\) fails; so the only flow is the empty relation, which is \(\bar x\).

**6.2.** Axiom (F2) is empty, and (F3) says nothing new for two points. By (F1) a flow is one of: the empty relation \(e\); \(\{(x,y)\}\), which is \(\bar y\); \(\{(y,x)\}\), which is \(\bar x\). In \(T\sqcup P\): \(\bar x\,x\,q\) for \(q\ne\bar x\), and \(\bar y\,y\,q\) for \(q\ne\bar y\); and \(x\) lies between \(e\) and \(\bar y\) only if \(yx.e\) or \(yx.\bar y\), which fail. So \((\bar x,e)=\{x\}\), \((\bar y,e)=\{y\}\), \((\bar x,\bar y)=\{x,y\}\). The point \(e\) is not in \(\bar T\), and \((\bar x,e)\cap(e,\bar y)=\varnothing\), so \(\langle\bar x\,e\,\bar y\rangle\). No other relation holds: \(\langle e\,\bar x\,\bar y\rangle\) would need \(e\,x\,\bar y\). So \(\Phi(T)\) is a path of three points with \(e\) in the middle.

**6.3.** From that exercise: \((\bar v,q)=\{v\}\) for \(v\in T\) and every flow \(q\ne\bar v\) among \(e\) and the two other \(\bar w\), except that \((\bar v,\bar w)=\{v,w\}\). So \((\bar x,e)\cap(e,\bar y)=\varnothing\), and \(\langle\bar x\,e\,\bar y\rangle\); likewise for the other pairs. So \(e\) is the median. No point \(\bar v\) lies between two others: \(\langle q\,\bar v\,q'\rangle\) needs \(q\,v\,q'\), that is, \(v\in(q,q')\) with \(q,q'\ne\bar v\), and no such interval contains \(v\). So the relations of \(\Phi(T)\) are exactly those of the tree with centre \(e\).

**6.4.** In the step showing \(s\ne p\): from \(s=p\) one gets that \((q,p)\cap(p,r)\) is empty, which contradicts the assumption. Without it, \(s\) could coincide with one of the three points; that is Case 1.

**6.5.** \(pxq\) with \(\bar x\ne p,q\) is the first case of Definition 2.1 for \(\langle p\bar xq\rangle\). For \(p\ne q\) the set \((p,q)\) is not empty (Lemma 1.1(1)); if \(p,q\notin\bar T\), any \(x\) in it has \(\bar x\ne p,q\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 3. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
