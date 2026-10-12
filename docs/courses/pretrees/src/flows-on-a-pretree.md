# Flows on a pretree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A pretree may lack points where one expects them: the end of an arc, or the place around which three points branch ([Dense, complete and median pretrees](dense-complete-and-median-pretrees.md)). To add such points one needs a way to speak about a place that is not there. A *flow* does this. Seen from a point \(a\) of a pretree, every other point \(x\) has a direction towards \(a\): the points \(y\) with \(y\in(x,a]\) are those one passes on the way from \(x\) to \(a\). A flow is a binary relation "from \(x\) one passes \(y\)" with the three properties that this relation has, whether or not a point exists towards which everything flows.

This lesson contains the first steps of the theory, following the beginning of Section 3 of [Bowditch].

- The flow towards a point, and its characterization among flows (Lemmas 2.1 and 2.2).
- A flow becomes the flow towards a point after one point is added to the pretree (Proposition 3.1).
- All flows can be added at once: the pretree \(T\) together with the set \(P\) of its flows is a pretree \(T\sqcup P\) in which every flow is the flow towards exactly one new point (Theorem 4.1).

The pretree \(T\sqcup P\) is an auxiliary object: all its new points are terminal. In the next lessons a different betweenness on \(P\) will make the set of flows a complete median pretree containing \(T\).

We use the first lesson, [Betweenness and pretrees](betweenness-and-pretrees.md): the axioms (T0) to (T3) and intervals.

## 1. Flows

Let \(T\) be a pretree. A *flow* on \(T\) is a binary relation \(p\) on \(T\), written \(xy.p\) and read "\(p\) flows from \(x\) to \(y\)", such that for all \(x,y,z\in T\):

- (F1) \(xy.p\) and \(yx.p\) do not both hold;
- (F2) if \(xzy\), then \(xz.p\) or \(yz.p\);
- (F3) if \(xy.p\) and \(z\ne y\), then \(xyz\) or \(zy.p\).

By (F1) with \(x=y\), \(xx.p\) never holds. In (F2) the point \(z\) between \(x\) and \(y\) is reached from at least one side. In (F3), if the flow passes from \(x\) to \(y\), then from any other point \(z\) it also passes to \(y\), unless \(z\) lies beyond \(y\) as seen from \(x\).

If \(S\subseteq T\), the restriction of a flow \(p\) on \(T\) to pairs of points of \(S\) is a flow on the pretree \(S\), written \(p|S\): the axioms speak about all points.

## 2. The flow towards a point

For \(a\in T\) define the relation \(\bar a\) by
\[
xy.\bar a\quad\Longleftrightarrow\quad y\in(x,a] .
\]
That is, \(xy.\bar a\) holds if \(xya\), or if \(y=a\) and \(x\ne a\).

**Lemma 2.1.** \(\bar a\) is a flow on \(T\).

**Proof.** (F1): suppose \(y\in(x,a]\) and \(x\in(y,a]\). If \(y=a\), then \(x\in(a,a]\), which is empty; so \(y\ne a\), and likewise \(x\ne a\). Then \(xya\) and \(yxa\), that is, \(ayx\) and \(axy\), against (T2).

(F2): let \(xzy\). If \(z=a\), then \(z\ne x\) and \(z\in(x,a]\). If \(z\ne a\), (T3) gives \(xza\) or \(yza\).

(F3): let \(y\in(x,a]\) and \(z\ne y\). If \(y=a\), then \(z\ne a\) and \(y\in(z,a]\), so \(zy.\bar a\). If \(xya\), (T3) with the point \(z\) gives \(xyz\) or \(ayz\); the second says \(y\in(z,a)\), so \(zy.\bar a\). \(\blacksquare\)

\(\bar a\) is the *flow towards \(a\)*. It determines \(a\): the point \(a\) is the only point \(y\) with \(xy.\bar a\) for all \(x\ne y\) (for \(y\ne a\), \(ay.\bar a\) fails).

**Lemma 2.2.** Let \(p\) be a flow on \(T\) and \(a\in T\). Then \(p=\bar a\) if and only if \(xa.p\) for every \(x\ne a\).

**Proof.** If \(p=\bar a\) and \(x\ne a\), then \(a\in(x,a]\). Conversely suppose \(xa.p\) for all \(x\ne a\). We show \(xy.p\iff xy.\bar a\). For \(y=a\) both sides say \(x\ne a\); recall that \(aa.p\) fails. Let \(y\ne a\). Then \(ya.p\), so \(ay.p\) fails by (F1). If \(xy.p\), then (F3) with the point \(a\ne y\) gives \(xya\) or \(ay.p\); so \(xya\), that is, \(xy.\bar a\). If \(xy.\bar a\), then \(xya\), and (F2) gives \(xy.p\) or \(ay.p\); so \(xy.p\). \(\blacksquare\)

## 3. Adding one point

**Proposition 3.1.** Let \(p\) be a flow on a pretree \(T\). On the set \(T\sqcup\{p\}\), with a new point named \(p\), define a ternary relation by keeping the relation of \(T\) on points of \(T\), and by declaring for \(x,y\in T\)
\[
xyp\ \text{ and }\ pyx\quad\Longleftrightarrow\quad xy.p ,
\]
with no other relations involving the new point. Then \(T\sqcup\{p\}\) is a pretree, the new point lies between no two points, and \(p\) is the restriction to \(T\) of the flow towards the new point.

**Proof.** The new point is never a middle point, by definition. (T0): a relation \(uvu\) would have \(v\in T\) and \(u\in T\), since no relation has the new point at both ends; it fails in \(T\). (T1) holds by definition. (T2): relations \(uvw\) and \(uwv\) have \(v,w\in T\). For \(u\in T\) this is (T2) in \(T\). For \(u=p\): \(pvw\) and \(pwv\) mean \(wv.p\) and \(vw.p\), against (F1).

(T3): let \(uzv\) hold and \(t\ne z\); then \(z\in T\). If \(u,v,t\in T\), this is (T3) in \(T\). If \(u,v\in T\) and \(t\) is the new point, we need \(uz.p\) or \(vz.p\), which is (F2). If one of \(u,v\) is the new point, say the relation is \(xzp\) with \(x\in T\), that is, \(xz.p\): for \(t\in T\) we need \(xzt\) or \(tz.p\), which is (F3); for \(t\) the new point, \(xzp\) itself is one of the two required relations.

Finally, for \(x,y\in T\), \(y\) lies in \((x,p]\) exactly when \(xyp\), that is, when \(xy.p\). \(\blacksquare\)

So every flow is the trace on \(T\) of a flow towards a point, in a pretree that may be larger than \(T\) by one point. If \(p=\bar a\) for a point \(a\in T\), the new point is a second point with the same trace; it is adjacent to \(a\) (Exercise 5.4).

## 4. Adding all flows

Let \(P\) be the set of all flows on \(T\). On the disjoint union \(T\sqcup P\) define a ternary relation as follows. On points of \(T\) it is the relation of \(T\). For the other triples:

- (C1) a point of \(P\) is never a middle point: \(upv\) holds for no \(p\in P\);
- (C2) for \(x,y\in T\) and \(p\in P\): \(xyp\) and \(pyx\) hold if and only if \(xy.p\);
- (C3) for \(p\ne q\) in \(P\) and \(x\in T\): \(pxq\) holds if and only if for every \(y\in T\setminus\{x\}\), \(yx.p\) or \(yx.q\).

In (C3), \(x\) lies between two flows if every other point flows to \(x\) under at least one of them. The condition \(p\ne q\) is needed: for \(p=\bar x\) the condition of (C3) holds with \(q=p\).

**Theorem 4.1.** With this relation \(T\sqcup P\) is a pretree. Moreover:

1. every point of \(P\) is terminal, that is, lies between no two points;
2. for every \(p\in P\), the flow towards the point \(p\) of \(T\sqcup P\), restricted to \(T\), is the flow \(p\);
3. for \(a\in T\) and a flow \(q\ne\bar a\), the relation \(\bar a\,a\,q\) holds; in particular \(a\) and the point \(\bar a\) are adjacent in \(T\sqcup P\).

**Proof.** Throughout, \(x,y,z\) are points of \(T\) and \(p,q,r\) points of \(P\).

(T0): in a relation \(uvu\) the middle point lies in \(T\) by (C1). For \(u\in T\) it fails in \(T\); for \(u\in P\), (C3) gives no relation with equal ends. (T1): the definition is symmetric in the two outer points. (T2): in relations \(uvw\) and \(uwv\), the points \(v,w\) lie in \(T\). For \(u\in T\) this is (T2) in \(T\); for \(u=p\), \(pvw\) and \(pwv\) mean \(wv.p\) and \(vw.p\), against (F1).

(T3): let \(uzv\) hold and \(t\ne z\). The middle point \(z\) lies in \(T\). We go through the cases.

*\(u,v,t\in T\)*: (T3) in \(T\).

*\(u=x\), \(v=y\) in \(T\), \(t=p\)*: we need \(xz.p\) or \(yz.p\), which is (F2).

*\(u=x\in T\), \(v=p\), \(t=y\in T\)*: we have \(xz.p\) and need \(xzy\) or \(yz.p\), which is (F3).

*\(u=x\in T\), \(v=p\), \(t=q\in P\)*: we have \(xz.p\) and need \(xz.q\) or \(pzq\). If \(q=p\), the first holds. Let \(q\ne p\) and suppose both fail. Since \(pzq\) fails, there is \(y\in T\), \(y\ne z\), with neither \(yz.p\) nor \(yz.q\). By (F3) for \(p\), from \(xz.p\) and \(y\ne z\): \(xzy\) or \(yz.p\); so \(xzy\). By (F2) for \(q\): \(xz.q\) or \(yz.q\). Both fail, a contradiction.

*\(u=p\), \(v=q\), \(t=y\in T\)*: we have \(pzq\) and \(y\ne z\), so \(yz.p\) or \(yz.q\) by (C3); these are the relations \(pzy\) and \(qzy\).

*\(u=p\), \(v=q\), \(t=r\in P\)*: we have \(pzq\) and need \(pzr\) or \(qzr\). If \(r=q\), the first is \(pzq\); if \(r=p\), the second is \(qzp\). Let \(r\ne p,q\) and suppose both fail. Then there are \(y\ne z\) with neither \(yz.p\) nor \(yz.r\), and \(y'\ne z\) with neither \(y'z.q\) nor \(y'z.r\). From \(pzq\): \(yz.q\) holds, since \(yz.p\) fails. By (F3) for \(q\), from \(yz.q\) and \(y'\ne z\): \(yzy'\) or \(y'z.q\); so \(yzy'\). By (F2) for \(r\): \(yz.r\) or \(y'z.r\). Both fail, a contradiction.

The remaining cases follow from these by exchanging \(u\) and \(v\).

(1) is (C1). (2): for \(x,y\in T\), \(y\in(x,p]\) in \(T\sqcup P\) means \(xyp\), that is, \(xy.p\). (3): by (C3) we must show that every \(y\ne a\) has \(ya.\bar a\) or \(ya.q\); the first holds. The points \(a\) and \(\bar a\) are adjacent: a point between them lies in \(T\) by (C1), and \(a\,y\,\bar a\) means \(ay.\bar a\), that is, \(y\in(a,a]\), which is empty. \(\blacksquare\)

By (1), no three points of \(P\) are related in \(T\sqcup P\). The structure of interest on \(P\) is a different one, defined through \(T\sqcup P\) in the next lesson.

## 5. Exercises

**5.1.** On the real line let \(xy.p\) mean \(x<y\). Show that \(p\) is a flow that is not the flow towards a point.

**5.2.** On the real line fix \(a\) and let \(xy.p\) mean: \(x<y\le a\), or \(a<y<x\). Show that \(p\) is a flow, that it is not the flow towards a point, and that it differs from \(\bar a\) only in the pairs \((x,a)\) with \(x>a\).

**5.3.** Let \(T=\{x,y,z\}\) with the empty betweenness relation. Find all flows on \(T\), and determine which points of \(T\) lie between which pairs of flows in \(T\sqcup P\).

**5.4.** Let \(p=\bar a\) with \(a\in T\). Show that in the pretree \(T\sqcup\{p\}\) of Proposition 3.1 the new point is adjacent to \(a\), and that \(x\,a\,p\) holds for every \(x\in T\setminus\{a\}\).

**5.5.** Let \(p\) be a flow on \(T\) and \(x\in T\). Show that the set of all \(y\) with \(xy.p\) is linear, and that for \(y,y'\) in it, with \(y\ne y'\), exactly one of \(xyy'\), \(xy'y\) holds.

## 6. Solutions

**5.1.** (F1) is clear. (F2): if \(z\) lies between \(x\) and \(y\), it is larger than the smaller of them. (F3): let \(x<y\) and \(z\ne y\); if \(z<y\) then \(zy.p\), and if \(z>y\) then \(y\) lies between \(x\) and \(z\). By Lemma 2.2, \(p=\bar a\) would require \(xa.p\) for all \(x\ne a\), which fails for \(x>a\).

**5.2.** (F1): let \(xy.p\). If \(x<y\le a\), then \(yx.p\) would need \(y<x\) or \(a<x\), and both are false. If \(a<y<x\), it would need \(x\le a\) or \(x<y\), and both are false. (F2): let \(z\) lie strictly between \(x<y\). If \(z\le a\), then \(x<z\le a\): \(xz.p\). If \(z>a\), then \(a<z<y\): \(yz.p\). (F3): let \(xy.p\) and \(z\ne y\). If \(x<y\le a\): for \(z<y\), \(zy.p\); for \(z>y\), \(xyz\). If \(a<y<x\): for \(z>y\), \(zy.p\); for \(z<y\), \(xyz\). Comparison with \(\bar a\): for \(y<a\), \(xy.p\) holds exactly when \(x<y\), which is \(y\in(x,a]\); for \(y>a\) it holds exactly when \(y<x\), which is again \(y\in(x,a]\); for \(y=a\) it holds exactly when \(x<a\), while \(xa.\bar a\) holds for all \(x\ne a\). So \(p\) and \(\bar a\) differ exactly in the pairs \((x,a)\) with \(x>a\). By Lemma 2.2, \(p\ne\bar a\); and \(p\ne\bar b\) for \(b\ne a\): for \(b<a\) the relation \(ab.p\) fails, and for \(b>a\) the relation \(xb.p\) fails for \(x<a\).

**5.3.** (F2) is empty. (F3) says: if \(uv.p\), then \(wv.p\) for the third point \(w\), since no betweenness holds. With (F1): if anything flows to \(v\), both other points flow to \(v\), and nothing flows from \(v\). So a flow is either empty or the flow towards one of the three points: there are four flows, \(\bar x,\bar y,\bar z\) and the empty flow \(e\). By (C3), a point \(v\in T\) lies between two different flows if each of the two other points flows to \(v\) under one of them: \(v\) lies between \(\bar v\) and each of the three other flows, and between no other pair. In particular the relations that involve the empty flow \(e\) are \(\bar x\,x\,e\), \(\bar y\,y\,e\), \(\bar z\,z\,e\) and their reverses. The empty flow is the flow towards the missing centre: in the tree with a centre joined to \(x,y,z\), it is the restriction of the flow towards the centre.

**5.4.** For \(x\ne a\), \(xa.p\) holds, so \(xap\). A point \(y\in T\) between \(a\) and the new point would have \(ay.\bar a\), that is \(y\in(a,a]\), which is empty.

**5.5.** In \(T\sqcup\{p\}\) the set is \((x,p)\), an open interval, which is linear (Corollary 5.3 of the first lesson). For \(y\ne y'\) in it, \(xyp\) and \(xy'p\) give \(xyy'p\) or \(xy'yp\) by Lemma 2.3(3) of the first lesson, so \(xyy'\) or \(xy'y\); not both, by (T2).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 3. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
