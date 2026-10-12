# Loxodromic elements and the completion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\Gamma\) be a convergence group on a compact connected metric space \(M\), and \(T\) an invariant set of cut points. A loxodromic element \(\gamma\) has two fixed points in \(M\). This lesson determines the points that \(\gamma\) fixes in the completion \(\Phi(T)\) of the pretree \(T\). There are two possibilities (Theorem 1.2): either the fixed points form a small configuration, at most three points next to each other; or there are exactly two fixed points, far apart, which are ends of \(\Phi(T)\) in a precise sense, and whose supports in \(M\) are the two fixed points of \(\gamma\).

The result is Lemma 6.9 of [Bowditch]; it is used to control the stabilizers of edges when a tree is extracted from \(\Phi(T)\). The proof uses the supports of [Supports and fixed points in the completion](supports-and-fixed-points-in-the-completion.md) and, from the course on pretrees, [Adjacent points of the completion](course:pretrees/adjacent-points-of-the-completion) and [Mapping a pretree to the completion of a subset](course:pretrees/mapping-a-pretree-to-the-completion-of-a-subset).

## 1. The statement

Throughout, \(M\) is a compact connected metric space with more than one point, \(\Gamma\) a convergence group on \(M\), and \(T\) a set of cut points of \(M\) with \(gT=T\) for all \(g\in\Gamma\). We use the notation of the lesson on supports: the completion \(\Phi=\Phi(T)\) with betweenness \(\langle prq\rangle\); the set \(\bar T\) of the flows \(\bar a\), \(a\in T\); the equivariant map \(\varphi\colon M\to\Phi\); the action of \(\Gamma\) on \(\Phi\); and the support \(R(p)\subseteq M\) of a point \(p\in\Phi\), which is not empty, closed and connected, with \(gR(p)=R(gp)\).

Two adjacent points of \(\Phi\) are called *neighbours*. Of two neighbours exactly one lies in \(\bar T\). Let \(\Phi'\) be the set of points of \(\Phi\setminus\bar T\) that have exactly one neighbour, and
\[
\Phi_0=\Phi\setminus\Phi' .
\]
So \(\bar T\subseteq\Phi_0\), and a point of \(\Phi_0\) outside \(\bar T\) has no neighbour or at least two.

Let \(\gamma\in\Gamma\) be loxodromic, with fixed points \(\lambda,\mu\) in \(M\), and let \(F(\gamma)\) be the set of points of \(\Phi\) fixed by \(\gamma\).

**Lemma 1.1.**

1. A point of \(F(\gamma)\) outside \(\Phi_0\) is adjacent to a point of \(F(\gamma)\cap\bar T\).
2. \(F(\gamma)\cap\Phi_0\) is not empty.
3. \(F(\gamma)\cap\bar T\) has at most two points.
4. For \(p\in F(\gamma)\) the support \(R(p)\) is \(\{\lambda\}\), or \(\{\mu\}\), or it contains \(\lambda\) and \(\mu\).
5. If \(p\in\Phi_0\setminus\bar T\) and \(R(p)\) has only one point, then \(p\) has no neighbour.

**Proof.** (1) The automorphism \(\gamma\) of \(\Phi\) maps neighbours of \(p\) to neighbours of \(\gamma p\). If \(p\in\Phi'\) is fixed, its only neighbour is fixed, and it lies in \(\bar T\).

(2) The point \(\varphi(\lambda)\) is fixed, because \(\varphi\) is equivariant. If it is not in \(\Phi_0\), its neighbour is a fixed point in \(\bar T\subseteq\Phi_0\), by (1).

(3) If \(\gamma\bar a=\bar a\), then \(\gamma a=a\), so \(a\) is \(\lambda\) or \(\mu\).

(4) The support is a nonempty closed connected set with \(\gamma R(p)=R(p)\). Apply Lemma 2.1(2) of the lesson on supports.

(5) By Proposition 1.2 of that lesson, \(R(p)\) contains every point \(a\in T\) with \(\bar a\) adjacent to \(p\). So \(p\) has at most one neighbour, and since \(p\in\Phi_0\), it has none. \(\blacksquare\)

**Theorem 1.2.** Let \(\gamma\in\Gamma\) be loxodromic with fixed points \(\lambda,\mu\), and \(E=F(\gamma)\cap\Phi_0\).

1. Suppose that the interval \([p,q]_\Phi\) is finite for all \(p,q\in E\). Then \(E\) is one of the following: a single point; two adjacent points; three points \(\bar a,n,\bar b\), where \(a\ne b\) are points of \(T\), \(n\notin\bar T\), and \(n\) is adjacent to \(\bar a\) and to \(\bar b\).
2. Suppose that \([p,q]_\Phi\) is infinite for some \(p,q\in E\). Then \(F(\gamma)=\{p,q\}\). The points \(p\) and \(q\) do not lie in \(\bar T\), they have no neighbours, they lie between no two points of \(\Phi\), and their supports are the sets \(\{\lambda\}\) and \(\{\mu\}\).

In both cases every point of \(F(\gamma)\) outside \(E\) is adjacent to a point of \(F(\gamma)\cap\bar T\).

The last statement is Lemma 1.1(1). The two cases are proved in Sections 2 and 3.

## 2. Finite intervals

**Lemma 2.1.** There are no three points \(\bar a,p,q\) of \(F(\gamma)\cap\Phi_0\) such that \(a\in T\), \(p\ne q\), and \(p\) and \(q\) are both adjacent to \(\bar a\).

**Proof.** Suppose there are. Then \(p,q\notin\bar T\). Since \(p\in\Phi_0\) has the neighbour \(\bar a\), it has a second neighbour \(\bar b\), and its support contains \(a\) and \(b\) (Proposition 1.2 of the lesson on supports). By Lemma 1.1(4), \(R(p)\) contains \(\lambda\) and \(\mu\). The same holds for \(R(q)\). But \(R(p)\cap R(q)\) has at most one point (Proposition 1.3 there). \(\blacksquare\)

**Proof of Theorem 1.2(1).** Let \(p\ne q\) be points of \(E\). The automorphism \(\gamma\) fixes \(p\) and \(q\), so it maps the finite interval \([p,q]_\Phi\) onto itself and preserves its direction from \(p\) to \(q\); hence it fixes every point of the interval. List the points of the interval in this direction. By Corollary 2.4(3) of the lesson on adjacent points, consecutive points are adjacent, and the points lie alternately in \(\bar T\) and outside. A point of the list other than \(p\) and \(q\) has two neighbours, so it lies in \(\Phi_0\). Hence
\[
[p,q]_\Phi\subseteq E .
\]

*\(E\) has at most one point outside \(\bar T\).* Let \(n\ne n'\) be two such points. The list of \([n,n']_\Phi\) begins and ends outside \(\bar T\), so it has at least three points: \(n\), then a point \(\bar a\), then a point \(n''\notin\bar T\). These are three points of \(E\), and \(n,n''\) are adjacent to \(\bar a\). This contradicts Lemma 2.1.

*\(E\) has at most two points in \(\bar T\)*, by Lemma 1.1(3).

*Conclusion.* If \(E\) contains two points \(\bar a\ne\bar b\) of \(\bar T\), the list of \([\bar a,\bar b]_\Phi\) begins and ends in \(\bar T\) and contains at most one point outside \(\bar T\); so it is \(\bar a,n,\bar b\), and \(E=\{\bar a,n,\bar b\}\). If \(E\) contains one point \(\bar a\) of \(\bar T\) and a point \(n\) outside, the list of \([\bar a,n]_\Phi\) contains no further point of either kind, so \(\bar a\) and \(n\) are adjacent. Otherwise \(E\) has one point. \(\blacksquare\)

## 3. An infinite interval

Let \(p,q\in E\) with \([p,q]_\Phi\) infinite.

*Step 1: the supports of \(p\) and \(q\) are \(\{\lambda\}\) and \(\{\mu\}\).* If \(R(p)\) and \(R(q)\) had a common point, \([p,q]_\Phi\) would have at most three points (Proposition 1.3 of the lesson on supports). So they are disjoint. By Lemma 1.1(4), neither contains both \(\lambda\) and \(\mu\), so each is \(\{\lambda\}\) or \(\{\mu\}\), and they are different.

*Step 2: \(E=\{p,q\}\).* Let \(r\in E\) be a third point. By Lemma 3.1 of [Betweenness and pretrees](course:pretrees/betweenness-and-pretrees), \([p,q]_\Phi\subseteq[p,r]_\Phi\cup[r,q]_\Phi\); so one of these intervals is infinite, say \([p,r]_\Phi\). By Step 1 for the pair \(p,r\), the support \(R(r)\) is a single point different from that of \(R(p)\). So \(R(r)=R(q)\). By Proposition 1.3 of the lesson on supports, the common point is a point \(a\in T\), and either one of \(q,r\) is \(\bar a\) and the other is adjacent to it, or both are adjacent to \(\bar a\). In each case one of the points \(q,r\) lies outside \(\bar T\) and has a neighbour, while it lies in \(\Phi_0\) and its support has one point. This contradicts Lemma 1.1(5).

*Step 3: infinitely many points of \(\bar T\) lie between \(p\) and \(q\).* Two different points of \(\Phi\) outside \(\bar T\) have a point of \(\bar T\) between them (Lemma 6.1 of [The dense quotient of a pretree](course:pretrees/the-dense-quotient-of-a-pretree)). The interval \((p,q)_\Phi\) is infinite and linearly ordered, so if it contained only finitely many points of \(\bar T\), two of its points outside \(\bar T\) would have no point of \(\bar T\) between them.

*Step 4: the sets \(N(p)\) and \(N(q)\).* Call a pair \((a,b)\) of points of \(T\) a *\(p\)-pair* if \(\bar a\) and \(\bar b\) lie in \((p,q)_\Phi\) and \(\bar b\) lies between \(\bar a\) and \(p\). By Step 3 there are \(p\)-pairs. Let \(N(p)\subseteq M\) be the intersection of the sets \(R_M(a,b)\) over all \(p\)-pairs, where \(R_M(a,b)\) is the set of points \(x\) for which \(xab\) fails. Define \(q\)-pairs and \(N(q)\) in the same way with \(p\) and \(q\) exchanged.

(a) *\(N(p)\) is closed, connected, and \(\gamma N(p)=N(p)\).* Each \(R_M(a,b)\) with \(a\in T\) is coherent, and so is the intersection (Lemma 3.1 of the lesson on mapping to the completion and Proposition 5.2 of [Cut points of a connected space](course:pretrees/cut-points-of-a-connected-space)); in the compact space \(M\) a coherent set is closed and connected. Since \(\gamma\) fixes \(p\) and \(q\) and acts by automorphisms, it maps \(p\)-pairs to \(p\)-pairs, and \(\gamma R_M(a,b)=R_M(\gamma a,\gamma b)\).

(b) *\(R(p)\subseteq N(p)\).* Let \((a,b)\) be a \(p\)-pair. If \(p\notin\bar T\): \(\langle\bar a\,\bar b\,p\rangle\) means that \(ab.p\) holds, so \(ba.p\) fails, and \(R_M(a,b)=R_M(a,p)\) contains \(R(p)\), by the definitions. If \(p=\bar c\): \(\langle\bar a\,\bar b\,\bar c\rangle\) means \(abc\), so \(cab\) fails, and \(c\in R_M(a,b)\).

(c) *\(N(p)\cap N(q)=\varnothing\).* By Step 3 choose points \(a,b,c,d\in T\) such that \(p,\bar a,\bar b,\bar c,\bar d,q\) lie in this order in \([p,q]_\Phi\). Then \((b,a)\) is a \(p\)-pair and \((c,d)\) a \(q\)-pair, so it suffices to show that no \(x\) lies in \(R_M(b,a)\cap R_M(c,d)\). Suppose \(xba\) and \(xcd\) fail. Then \(x\ne c\), because \(cba\) holds, and \(x\ne b\), because \(bcd\) holds. By (T3), applied to \(abc\) and the point \(x\): \(abx\) or \(cbx\); the first fails, so \(xbc\). By (T3), applied to \(bcd\) and the point \(x\): \(bcx\) or \(dcx\); the second fails, so \(xcb\). But \(xbc\) and \(xcb\) contradict (T2).

By (a), (c) and Lemma 2.1(2) of the lesson on supports, \(N(p)\) and \(N(q)\) are single points: each is \(\{\lambda\}\), \(\{\mu\}\) or contains both, and they are disjoint and not empty by (b).

*Step 5: \(p\notin\bar T\).* Suppose \(p=\bar c\). By (b), \(N(p)=\{c\}\). Choose \(c'\in T\) with \(\bar c'\in(p,q)_\Phi\). Since \(c\) is a cut point, it has a separation, and on the side that does not contain \(c'\) there is a point \(x\); so \(xcc'\). We show \(x\in N(p)\), which is a contradiction because \(x\ne c\).

Let \((a,b)\) be a \(p\)-pair. The points \(\bar b\) and \(\bar c'\) lie in \((\bar c,q)_\Phi\), and \(\bar c\) is an end of the linearly ordered interval \([\bar c,q]_\Phi\); so \(\bar c\) is not between them, and \(bcc'\) fails. By (T3), applied to \(xcc'\) and the point \(b\ne c\): \(xcb\) or \(c'cb\); so \(xcb\). From \(abc\) and \(bcx\), Lemma 2.3(1) of the lesson Betweenness and pretrees gives \(abx\). So \(xab\) fails, and \(x\in R_M(a,b)\).

*Step 6: \(p\) has no neighbour.* By Steps 1 and 5 and Lemma 1.1(5).

*Step 7: \(p\) lies between no two points of \(\Phi\).* Suppose \(\langle upv\rangle\). By (T3) with the point \(q\ne p\): \(\langle upq\rangle\) or \(\langle vpq\rangle\); let \(\langle upq\rangle\). We find \(c\in T\) with \(\langle\bar c\,p\,q\rangle\): if \(u\in\bar T\), take \(\bar c=u\); otherwise \(u\ne p\) are points outside \(\bar T\), so there is \(\bar c\) with \(\langle u\,\bar c\,p\rangle\), and then \(u,\bar c,p,q\) lie in a row.

Let \((a,b)\) be a \(p\)-pair. Then \(q,\bar a,\bar b,p,\bar c\) lie in a row in \(\Phi\): this follows from \(\langle q\,\bar a\,\bar b\rangle\), \(\langle\bar a\,\bar b\,p\rangle\) and \(\langle q\,p\,\bar c\rangle\) by Lemma 2.3 of the lesson Betweenness and pretrees. In particular \(\langle\bar a\,\bar b\,\bar c\rangle\), that is, \(abc\). So \(cab\) fails, and \(c\in R_M(a,b)\). Hence \(c\in N(p)\), and by Step 4, \(N(p)=\{c\}\). By (b), \(R(p)=\{c\}\). By Proposition 1.2 of the lesson on supports, since \(\varphi(c)=\bar c\ne p\), the point \(\bar c\) is adjacent to \(p\). This contradicts Step 6.

*Step 8: conclusion.* Steps 5 to 7 hold for \(q\) as well. By Step 2, \(E=\{p,q\}\). A point of \(F(\gamma)\) outside \(E\) would be adjacent to a point of \(F(\gamma)\cap\bar T\subseteq E\), by Lemma 1.1(1); but \(p,q\notin\bar T\). So \(F(\gamma)=\{p,q\}\). \(\blacksquare\)

## 4. Exercises

**4.1.** Let \(M=\mathbb R\cup\{-\infty,\infty\}\) be the line with two ends added, a space homeomorphic to \([0,1]\), with \(T=\mathbb R\) and the group of the maps \(x\mapsto x+k\), \(k\) an integer, which fix the two ends. Show that this is a convergence group, that \(\gamma(x)=x+1\) is loxodromic, and that case 2 of Theorem 1.2 holds; name the two fixed points in \(\Phi(T)\).

**4.2.** In the proof of Theorem 1.2(1), where is it used that the points of \(E\) lie in \(\Phi_0\), and not only in \(F(\gamma)\)?

**4.3.** Let \(\gamma\) be loxodromic and suppose that both fixed points \(\lambda,\mu\) lie in \(T\) and that \(\bar\lambda\) and \(\bar\mu\) have a common neighbour \(n\). Show that \(n\) is fixed by \(\gamma\) and that \(E=\{\bar\lambda,n,\bar\mu\}\).

## 5. Solutions

**4.1.** A sequence \((\gamma^{k_i})\) with \(k_i\to\infty\) collapses with the pair \((-\infty,\infty)\): a closed set that does not contain \(-\infty\) lies in some \([r,\infty]\), and its image under \(\gamma^k\) lies in \([r+k,\infty]\). Likewise for \(k_i\to-\infty\) with the pair \((\infty,-\infty)\). Every sequence of pairwise distinct elements has a subsequence of one of these kinds. So the group is a convergence group, and \(\gamma\) has infinite order and exactly the two fixed points \(\pm\infty\): it is loxodromic. The cut points are the real numbers. The points \(\varphi(\infty)\) and \(\varphi(-\infty)\) are the flows of \(T\) directed upwards and downwards; they are fixed, they are not in \(\bar T\), and all the points \(\bar t\) lie between them (Lemma 1.2(1) of the lesson on mapping to the completion). So the interval between them is infinite. They have no neighbours: the upward flow runs from every \(t\) to \(t+1\), so there is no point of \(T\) from which it runs nowhere, and likewise for the downward flow (Corollary 2.4(1) of the lesson on adjacent points). So they lie in \(\Phi_0\), and case 2 holds with \(p=\varphi(-\infty)\), \(q=\varphi(\infty)\).

**4.2.** In the proof of Lemma 2.1: a point of \(\Phi_0\setminus\bar T\) with a neighbour has a second neighbour, which gives its support two points. A fixed point with exactly one neighbour has a support that may be a single point.

**4.3.** The points \(\bar\lambda\) and \(\bar\mu\) are fixed, and \(\gamma n\) is a common neighbour of both. Two points of \(\bar T\) have at most one common neighbour: for two common neighbours \(n,n'\) the supports \(R(n)\) and \(R(n')\) would both contain \(\lambda\) and \(\mu\), against Proposition 1.3 of the lesson on supports. So \(\gamma n=n\). The point \(n\) has two neighbours, so it lies in \(\Phi_0\), and \(E\) contains \(\bar\lambda\), \(n\) and \(\bar\mu\). Case 2 of Theorem 1.2 does not hold, because in that case no fixed point lies in \(\bar T\). So case 1 holds, and \(E\) is the three-point set.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
