# Directed arcs and suprema

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An arc of a pretree with a chosen direction runs towards something: towards its last point if it has one, and otherwise towards a place that may or may not be a point of the pretree. This lesson makes this precise in two ways. First, every directed arc \(A\) defines a flow, \(\operatorname{flow}(A)\), which is the flow towards the last point if there is one (Proposition 2.4). Two directed arcs that share a final part define the same flow, and conversely two directed arcs that meet and define the same flow share a final part (Lemmas 2.3 and 2.6). Second, a point \(b\) is a *supremum* of a directed arc if the arc ends at \(b\) or runs up to \(b\) without reaching it. The main result (Theorem 4.3) says that a pretree is complete, in the sense that every arc is an interval, exactly when every directed arc has a supremum.

The lesson follows Lemmas 3.5 to 3.13 of [Bowditch]. It uses the lessons [Betweenness and pretrees](betweenness-and-pretrees.md), for arcs, directions and intervals, and [Flows on a pretree](flows-on-a-pretree.md).

## 1. Directed arcs and final segments

Let \(T\) be a pretree. A *directed arc* is an arc \(A\), that is, a nonempty full linear subset, together with a direction \(<\): a total order on \(A\) such that for \(x,y,z\in A\) the relation \(xyz\) holds exactly when \(x<y<z\) or \(z<y<x\). Since \(A\) is full, for \(x<y\) in \(A\),
\[
[x,y]=\{w\in A:\ x\le w\le y\}.
\]

A *final segment* of \((A,<)\) is a nonempty subset \(B\subseteq A\) such that \(x\in B\), \(y\in A\) and \(x\le y\) imply \(y\in B\). With the restricted order it is a directed arc. For \(x\in A\) the set \(\{y\in A:x\le y\}\) is a final segment. A point \(a\in A\) is the *maximum* of \(A\) if \(x\le a\) for all \(x\in A\); it then lies in every final segment. \(A\) is *endless* if it has no maximum. A final segment of an endless arc is endless.

Two directed arcs \((A,<)\) and \((A',<')\) are *cofinal* if there is a set \(C\) that is a final segment of both and on which the two orders agree.

**Lemma 1.1.** Let \((A,<)\) be a directed arc.

1. If \(B\subseteq A\) is an arc that contains a final segment of \(A\), then \(B\) is a final segment of \(A\).
2. If \((A',<')\) is a directed arc cofinal with \(A\), then \(A\cap A'\) is a final segment of both, and the two orders agree on it.

**Proof.** (1) Let \(C\subseteq B\) be a final segment of \(A\) and \(z\in C\). Let \(x\in B\) and \(y\in A\) with \(x\le y\). If \(y\ge z\), then \(y\in C\subseteq B\). If \(y\le z\), then \(y\in[x,z]\subseteq B\), because \(B\) is full.

(2) Let \(C\) be a common final segment on which the orders agree. The set \(A\cap A'\) is full and linear and contains \(C\), so by (1) it is a final segment of \(A\) and of \(A'\). The restrictions of \(<\) and \(<'\) to \(A\cap A'\) are directions of this linear set. If \(C\) has two points, the two directions agree on them and are equal (Proposition 5.2 of the first lesson). If \(C=\{c\}\), then \(c\) is the maximum for both; a linear set with more than one point has two directions, each the reverse of the other, and only one of them has \(c\) as its maximum. \(\blacksquare\)

## 2. The flow of a directed arc

**Lemma 2.1.** Let \((A,<)\) be an endless directed arc and \(x,y\in T\). The following are equivalent.

1. For every \(z\in A\) there is \(w\in A\) with \(z<w\) and \(xyw\).
2. There is \(z\in A\) such that \(xyw\) for all \(w\in A\) with \(w>z\).

**Proof.** (2) implies (1): let \(z_0\) be as in (2); given \(z\), choose \(w\in A\) larger than \(z\) and \(z_0\).

(1) implies (2): suppose (1) holds and (2) fails. Choose \(z_0\in A\), with \(z_0=y\) if \(y\in A\). Since (2) fails there is \(a>z_0\) with \(xya\) false; by (1) there is \(b>a\) with \(xyb\); since (2) fails there is \(c>b\) with \(xyc\) false. The points \(a,b,c\) differ from \(y\). By (T3), from \(xyb\) and the point \(a\): \(xya\) or \(bya\); so \(bya\). In the same way \(byc\). So \(y\) lies in \((a,b)\) and in \((b,c)\). But \(a<b<c\) gives \(abc\), and then \([a,b]\cap[b,c]=\{b\}\) (Lemma 3.2 of the first lesson). \(\blacksquare\)

**Definition 2.2.** Let \((A,<)\) be a directed arc. If \(A\) has a maximum \(a\), then \(\operatorname{flow}(A)\) is the flow \(\bar a\) towards \(a\). If \(A\) is endless, \(\operatorname{flow}(A)\) is the binary relation, written \(xy.A\), that holds when the two equivalent conditions of Lemma 2.1 hold.

**Lemma 2.3.** Cofinal directed arcs have the same flow.

**Proof.** Let \(C\) be a common final segment of \(A\) and \(B\) on which the orders agree. If \(A\) has a maximum \(a\), then \(a\in C\), and \(a\) is the maximum of \(B\): an element \(b\in B\) above \(a\) would lie in \(C\subseteq A\) and be above \(a\) there. So both flows are \(\bar a\). The same holds if \(B\) has a maximum. Let \(A\) and \(B\) be endless; it suffices to compare \(A\) with \(C\). If \(xy.A\) holds with \(z\) as in condition 2, replace \(z\) by a larger element of \(C\); condition 2 then holds for \(C\). If \(xy.C\) holds with \(z\in C\) as in condition 2, the elements of \(A\) above \(z\) lie in \(C\), so condition 2 holds for \(A\). \(\blacksquare\)

**Proposition 2.4.** Let \((A,<)\) be a directed arc.

1. If \(x,y\in A\), then \(xy.A\) if and only if \(x<y\).
2. If \(x,y\notin A\), then \(xy.A\) if and only if \(xyz\) for some \(z\in A\), and if and only if \(xyz\) for all \(z\in A\).
3. \(\operatorname{flow}(A)\) is a flow on \(T\).
4. If \(x\in A\) and \(y\in T\), then \(xy.A\) if and only if \(y\in A\) and \(x<y\).

**Proof.** (1) If \(A\) has the maximum \(a\): \(y\in(x,a]\) means \(x<y\le a\), by the description of intervals in \(A\). Let \(A\) be endless. If \(x<y\), then \(xyw\) for all \(w>y\), which is condition 2. If \(xy.A\), condition 1 with \(z=y\) gives \(w>y\) with \(xyw\); then \(y\) lies between \(x\) and \(w\) in the order and \(y<w\), so \(x<y\).

(2) Let \(x,y\notin A\) and \(z,w\in A\). Then \(zyw\) fails, because \(A\) is full and \(y\notin A\). So if \(xyz\), then (T3) with the point \(w\ne y\) gives \(xyw\). Hence \(xyz\) holds for some \(z\in A\) if and only if it holds for all. If \(A\) has the maximum \(a\), then \(xy.\bar a\) means \(xya\), since \(y\ne a\). If \(A\) is endless, condition 2 of Lemma 2.1 holds if and only if \(xyw\) for all \(w\in A\).

(3) For \(A\) with a maximum this is Lemma 2.1 of the lesson on flows. Let \(A\) be endless and \(x,y,z\in T\). The set of \(w\in A\) that are larger than those of \(x,y,z\) that lie in \(A\) is a final segment \(A'\) of \(A\) containing none of the three points, and \(\operatorname{flow}(A')=\operatorname{flow}(A)\) by Lemma 2.3. Fix \(a\in A'\). By (2), for \(u,v\in\{x,y,z\}\): \(uv.A'\) if and only if \(uva\), that is, if and only if \(uv.\bar a\). Each of the axioms (F1), (F2), (F3) for the points \(x,y,z\) involves only such pairs and the betweenness of \(T\), and \(\bar a\) is a flow. So the axioms hold for \(\operatorname{flow}(A)\).

(4) If \(A\) has the maximum \(a\): \(y\in(x,a]\) if and only if \(y\in A\) and \(x<y\). Let \(A\) be endless. If \(xy.A\), condition 1 gives \(w\in A\) with \(xyw\), so \(y\in[x,w]\subseteq A\), and \(x<y\) by (1). The converse is (1). \(\blacksquare\)

So the flow of a directed arc flows along the arc in its direction, and from outside it flows towards the arc.

**Lemma 2.5.** Let \(p=\operatorname{flow}(A)\) for a directed arc \((A,<)\), and consider the pretree \(T\sqcup\{p\}\) of Proposition 3.1 of the lesson on flows. Then \(A\cup\{p\}\) is linear, and for \(w\in A\) and \(y\in T\): \(w\,y\,p\) holds if and only if \(y\in A\) and \(w<y\).

**Proof.** The second statement is Proposition 2.4(4), since \(w\,y\,p\) means \(wy.A\). For \(u<v\) in \(A\) it gives \(u\,v\,p\); with the linearity of \(A\) this shows that \(A\cup\{p\}\) is linear. \(\blacksquare\)

**Lemma 2.6.** Let \((A,<)\) and \((B,<')\) be directed arcs with a common point and with \(\operatorname{flow}(A)=\operatorname{flow}(B)\). Then they are cofinal.

**Proof.** Let \(x\in A\cap B\), and let \(C\) be the set of all \(y\in T\) with \(xy.A\). By Proposition 2.4(4), \(C=\{y\in A:x<y\}\), and also \(C=\{y\in B:x<'y\}\). If \(C\) is empty, \(x\) is the maximum of both, and \(\{x\}\) is a common final segment. Otherwise \(C\) is a final segment of both. The orders agree on \(C\): for \(y,y'\in C\), \(y<y'\) holds if and only if \(x\,y\,y'\), and the same is true for \(<'\). \(\blacksquare\)

## 3. Full subsets

A subset \(S\subseteq T\) is a pretree, and an arc of \(T\) that lies in \(S\) is an arc of \(S\) when \(S\) is full. For a directed arc \(B\) of \(S\), \(\operatorname{flow}_S(B)\) denotes its flow as a relation on \(S\), and \(\operatorname{flow}_T\) the flow on \(T\).

**Lemma 3.1.** Let \(S\subseteq T\) be full and \((A,<)\) a directed arc of \(T\) that meets \(S\). Then \(B=A\cap S\), with the restricted order, is a directed arc. If \(B\) is endless, then
\[
\operatorname{flow}_T(A)\,|\,S=\operatorname{flow}_S(B).
\]

**Proof.** \(B\) is nonempty, linear, and full as an intersection of full sets.

Let \(B\) be endless, \(p=\operatorname{flow}_T(A)\), and \(x,y\in S\). In \(T\sqcup\{p\}\), \(xy.A\) means \(x\,y\,p\). Call \(w\in B\) *late* if \(w>y\) in case \(y\in B\); if \(y\notin B\), every \(w\in B\) is late. Since \(B\) is endless, above every element of \(B\) there is a late one. For late \(w\), the relation \(w\,y\,p\) fails: by Lemma 2.5 it would require \(y\in A\) and \(w<y\); but \(y\in A\) gives \(y\in A\cap S=B\), and then \(w>y\).

If \(x\,y\,p\), then for every late \(w\), (T3) with the point \(w\ne y\) gives \(xyw\) or \(p\,y\,w\); so \(xyw\). The late elements contain all elements of \(B\) above some element, so condition 2 of Lemma 2.1 holds for \(B\): \(xy.B\).

If \(xy.B\), choose a late \(w\) with \(xyw\), by condition 1. By (T3) in \(T\sqcup\{p\}\) with the point \(p\): \(x\,y\,p\) or \(w\,y\,p\). The second fails. So \(xy.A\). \(\blacksquare\)

## 4. Suprema and completeness

*Intervals as directed arcs.* For \(x\ne b\) the interval \([x,b)\) is an arc, and we direct it by the direction of \([x,b]\) in which \(x\) is the least point. For \(y\in[x,b)\) the set \([y,b)\) is the final segment \(\{w\in[x,b):w\ge y\}\), with the same direction (Corollary 5.3 of the first lesson).

**Lemma 4.1.** Let \((A,<)\) be a directed arc, \(x\in A\) and \(b\in T\), \(b\ne x\). If \([x,b)\) is cofinal with \(A\), then \([x,b)\) is a final segment of \(A\), with the same order.

**Proof.** Let \(C\) be a common final segment on which the orders agree, and \(y\in C\). Then \([y,b)\) is a final segment of \([x,b)\) contained in \(C\), so it is a final segment of \(C\) and hence of \(A\). Now \([x,b)\subseteq[x,y]\cup[y,b)\) by Lemma 3.1 of the first lesson, and \([x,y]\subseteq A\) because \(A\) is full. So \([x,b)\) is an arc inside \(A\) containing a final segment of \(A\); by Lemma 1.1(1) it is a final segment of \(A\), and the orders agree on it by the argument of Lemma 1.1(2). \(\blacksquare\)

**Lemma 4.2.** Let \((A,<)\) be an endless directed arc, \(x,y\in A\) and \(b\in T\). Then \([x,b)\) is a final segment of \(A\) with the order of \(A\) if and only if \([y,b)\) is.

**Proof.** Let \(x<y\). If \([x,b)\) is such a final segment, it contains \(y\), and \([y,b)\) is a final segment of \([x,b)\), hence of \(A\).

Conversely let \([y,b)\) be such a final segment. Since \(A\) is endless there is \(z\in A\) with \(z>y\); then \(z\in(y,b)\), so \(yzb\), and \(byz\) fails by (T2). From \(x<y<z\) we have \(xyz\), and (T3) with the point \(b\ne y\) gives \(xyb\) or \(zyb\); so \(xyb\). Hence \(y\in[x,b)\), and \([y,b)\) is a final segment of \([x,b)\) and of \(A\), with the same orders: \([x,b)\) is cofinal with \(A\). By Lemma 4.1 it is a final segment of \(A\). \(\blacksquare\)

**Definition.** A point \(b\in T\) is a *supremum* of a directed arc \((A,<)\) if \(b\) is the maximum of \(A\), or if \(A\) is endless and for some \(x\in A\) the interval \([x,b)\) is a final segment of \(A\) with the order of \(A\). By Lemma 4.2 this then holds for every \(x\in A\).

So a supremum of an endless arc is a point \(b\notin A\) such that \(A\) runs up to \(b\): from each of its points \(x\) on, \(A\) is the interval \([x,b)\).

**Theorem 4.3.** A pretree is complete if and only if every directed arc has a supremum.

**Proof.** *Let \(T\) be complete* and \((A,<)\) a directed arc. If \(A\) has a maximum, that is a supremum. Let \(A\) be endless. Then \(A\) has more than one point, and it is an interval with ends \(p\ne q\). So \(A\subseteq[p,q]\), and \(<\) is the restriction of one of the two directions of \([p,q]\); name the ends so that it is the one with \(p<q\). Since \(A\) has no maximum, \(q\notin A\). So \(A\) is \([p,q)\) or \((p,q)\), and for \(x\in A\) the set \(\{w\in A:w\ge x\}\) is \(\{w\in[p,q]:x\le w<q\}=[x,q)\). Hence \(q\) is a supremum.

*Let every directed arc have a supremum* and let \(A\) be an arc. If \(A\) is a single point \(x\), it is the interval \([x,x]\). Otherwise choose a direction \(<\) (Proposition 5.2 of the first lesson), let \(b\) be a supremum of \((A,<)\) and \(a\) a supremum of \(A\) with the reverse direction.

If \(A\) has a least point and a greatest point, these are \(a\) and \(b\), and \(A=[a,b]\): every other point lies between them, and \(A\) is full.

If \(A\) has a least point \(a\) and no greatest point, then \([a,b)\) is a final segment of \(A\) containing the least point, so \(A=[a,b)\). In the same way, if \(A\) has a greatest point \(b\) and no least point, \(A=(a,b]\).

Let \(A\) have neither. For \(x\in A\) we have \(\{w\in A:w\ge x\}=[x,b)\) and \(\{w\in A:w\le x\}=(a,x]\). Choose \(u<x<w\) in \(A\). Then \(aux\), \(uxw\) and \(xwb\). By Lemma 2.3(1) of the first lesson, \(aux\) and \(uxw\) give \(axw\); then \(axw\) and \(xwb\) give \(axb\). So \(x\in(a,b)\), and by Lemma 3.2 of the first lesson \((a,b)=(a,x]\cup[x,b)=A\). \(\blacksquare\)

## 5. Exercises

**5.1.** In the pretree \(\mathbb Q\), find a directed arc without a supremum, and describe its flow.

**5.2.** Let \(T\) be the complete dense pretree of Proposition 3.2 of [Dense, complete and median pretrees](dense-complete-and-median-pretrees.md). Find a supremum of the arc formed by the points of leg 2, directed towards the centre, and show that the arc formed by the points of legs 2 and 3, in either direction, has its end \(y\) or \(z\) as supremum.

**5.3.** Give two directed arcs that have the same underlying set and are not cofinal, and compare their flows.

**5.4.** Show that in Lemma 2.6 the assumption that the arcs have a common point cannot be dropped.

**5.5.** Let \((A,<)\) be an endless directed arc with a supremum \(b\). Show that \(\operatorname{flow}(A)\) and \(\bar b\) agree on all pairs \((x,y)\) with \(y\ne b\), and that \(xb.A\) fails for \(x\in A\). So \(\operatorname{flow}(A)\ne\bar b\).

## 6. Solutions

**5.1.** Let \(A\) be the set of rational numbers \(x\) with \(x^2<2\), with the usual order. It is endless. A supremum would be a rational \(b\) such that for \(x\in A\) the set of \(w\in A\) with \(w\ge x\) is \([x,b)\); this set consists of the rationals in \([x,\sqrt2)\), so \(b\) would be \(\sqrt2\). The flow: \(xy.A\) holds exactly when \(y\) lies strictly between \(x\) and \(\sqrt2\) on the real line. Indeed, by Lemma 2.1, \(xy.A\) means that \(y\) lies strictly between \(x\) and \(w\) for all \(w\in A\) close enough to \(\sqrt2\); since \(y\) is rational, this is the stated condition.

**5.2.** The points of leg 2 form the interval \([y,q)\) with \(y=(2,1)\) and \(q=(1,\frac12)\) (Proposition 3.2 there); directed towards the centre it is \([y,q)\) with \(y\) least, and \(q\) is a supremum by definition. The points of legs 2 and 3 form the interval \([y,z]\), which has a greatest point in either direction.

**5.3.** The real line with the usual order and with the reverse order. A common final segment on which the orders agree would be a set unbounded above and below on which \(<\) and \(>\) agree. The flows are \(x<y\) and \(y<x\).

**5.4.** Let \(T\) be the real line without the point \(0\), a pretree as a subset of the line. Let \(A\) be the set of negative numbers with the usual order and \(B\) the set of positive numbers with the reverse order. Both are endless directed arcs of \(T\), and they are disjoint, so they are not cofinal. As in the solution of 5.1, \(xy.A\) holds exactly when \(y\) lies strictly between \(x\) and \(0\), and the same is true for \(B\). So the two flows are equal.

**5.5.** Recall that for \(w\in A\) the set of elements of \(A\) above \(w\) is \([w,b)\); in particular \(b\notin A\), and \((w,b)\subseteq A\). Let \(y\ne b\).

*\(x\in A\).* By Proposition 2.4(4), \(xy.A\) means \(y\in A\) and \(x<y\), that is, \(y\in(x,b)\); for \(y\ne b\) this is \(xy.\bar b\).

*\(x\notin A\), \(y\notin A\).* By Proposition 2.4(2), \(xy.A\) means \(xyw\) for all \(w\in A\), and \(xy.\bar b\) means \(xyb\). If \(xyb\) and \(w\in A\), then (T3) gives \(xyw\) or \(byw\); the second would put \(y\) into \((w,b)\subseteq A\). If \(xyw\), then (T3) with the point \(b\) gives \(xyb\) or \(wyb\), and again the second is impossible.

*\(x\notin A\), \(y\in A\).* For \(w\in A\) with \(w>y\) we have \(ywb\), so \(wyb\) fails by (T2). If \(xyb\), then (T3) with the point \(w\) gives \(xyw\) or \(byw\); so \(xyw\) for all \(w>y\), which is condition 2 of Lemma 2.1. If \(xy.A\), choose \(w>y\) with \(xyw\); (T3) with the point \(b\) gives \(xyb\) or \(wyb\); so \(xyb\).

Finally, for \(x\in A\) the relation \(xb.A\) fails by Proposition 2.4(4), because \(b\notin A\), while \(xb.\bar b\) holds.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 3. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
