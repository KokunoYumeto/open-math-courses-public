# Supports and fixed points in the completion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let a group \(\Gamma\) act on a compact connected metric space \(M\), and let \(T\) be an invariant set of cut points. By [Quotients and minimal actions](quotients-and-minimal-actions.md) the group acts on the completion \(\Phi(T)\) of the pretree \(T\). The points of \(\Phi(T)\) are abstract: they are flows of \(T\). This lesson attaches to each of them a closed connected subset of \(M\), its *support*, and uses the supports to find out which points of the completion a group element can fix.

- The support of a point \(p\) that is not a point of \(T\) consists of the points of \(M\) that are mapped to \(p\) and of the points of \(T\) adjacent to \(p\) (Proposition 1.2). Two supports meet in at most one point (Proposition 1.3).
- If the action on \(M\) is minimal and \(T\) is not empty, no point of \(\Phi(T)\) is fixed by the whole group (Theorem 3.1).
- In a convergence group, a parabolic element whose fixed point is not in \(T\) fixes exactly one point of \(\Phi(T)\) (Theorem 4.1).

The lesson follows Lemmas 6.8, 6.10 and 6.11 of [Bowditch]. It uses the two earlier lessons of this course and, from the course on pretrees, [Mapping a pretree to the completion of a subset](course:pretrees/mapping-a-pretree-to-the-completion-of-a-subset) and [Adjacent points of the completion](course:pretrees/adjacent-points-of-the-completion).

## 1. Supports

Throughout, \(M\) is a compact connected metric space with more than one point, and \(T\) is a set of cut points of \(M\). We use the objects of the lesson on mapping a pretree to the completion of a subset:

- \(\Phi=\Phi(T)\), the completion of the pretree \(T\), with betweenness \(\langle prq\rangle\) and intervals \([p,q]_\Phi\); \(\bar a\) is the flow towards \(a\in T\), and \(\bar T\) the set of these flows;
- the map \(\varphi\colon M\to\Phi\), with \(\varphi(a)=\bar a\) for \(a\in T\); for \(u,v\in T\), \(uv.\varphi(x)\) means \(v\in(u,x]\);
- for \(a\ne b\) in \(M\), the set \(R_M(a,b)\) of points \(x\) for which \(xab\) fails;
- for a flow \(p\ne\bar a\), the nonempty set \(H(a,p)\) of points \(b\in T\setminus\{a\}\) for which \(ba.p\) fails, and \(R_M(a,p)=R_M(a,b)\) for \(b\in H(a,p)\);
- for \(p\in\Phi\setminus\bar T\), the set \(R_M(p)\), the intersection of the sets \(R_M(a,p)\) over \(a\in T\). It is not empty, closed and connected (Theorem 3.2 there).

Two points of \(\Phi\) are *adjacent* if they are different and no point of \(\Phi\) lies between them. Of two adjacent points exactly one lies in \(\bar T\); and \(\bar a\) is adjacent to a flow \(p\ne\bar a\) exactly when \(p\) runs nowhere from \(a\), that is, when \(au.p\) holds for no \(u\) (Theorem 2.3 and Lemma 2.1 of the lesson on adjacent points).

**Definition 1.1.** The *support* of a point \(p\in\Phi\) is the set \(R(p)\subseteq M\) defined by \(R(p)=R_M(p)\) if \(p\notin\bar T\), and \(R(\bar a)=\{a\}\) for \(a\in T\).

Every support is not empty, closed and connected.

**Proposition 1.2.** Let \(p\in\Phi\setminus\bar T\). Then
\[
\begin{gathered}
R(p)=\varphi^{-1}(p)\ \cup\\
\{a\in T\mid\bar a\text{ is adjacent to }p\}.
\end{gathered}
\]

**Proof.** *The points mapped to \(p\) lie in \(R(p)\).* Let \(\varphi(x)=p\), \(a\in T\) and \(b\in H(a,p)\). Then \(ba.\varphi(x)\) fails, that is, \(a\notin(b,x]\). So \(bax\) fails, and \(x\in R_M(a,b)=R_M(a,p)\).

*The points of \(T\) adjacent to \(p\) lie in \(R(p)\).* Let \(\bar b\) be adjacent to \(p\), and \(a\in T\). If \(a=b\), then \(b\in R_M(b,p)\), since this set contains \(b\). If \(a\ne b\), then \(ba.p\) fails, because \(p\) runs nowhere from \(b\); so \(b\in H(a,p)\), and \(b\in R_M(a,b)=R_M(a,p)\).

*Conversely* let \(x\in R(p)\) with \(\varphi(x)\ne p\). By Proposition 2.3 of the lesson on mapping to the completion, \(\varphi(x)=\bar a\) for a point \(a\in T\) with \(\bar a\) adjacent to \(p\). We show \(x=a\). Choose \(b\in H(a,p)\). Since \(\varphi(x)=\bar a\) and \(b\ne a\), we have \(ba.\varphi(x)\), that is, \(a\in(b,x]\). So \(a=x\) or \(bax\). But \(x\in R_M(a,p)=R_M(a,b)\), so \(bax\) fails. \(\blacksquare\)

**Proposition 1.3.** Let \(p\ne q\) be points of \(\Phi\) whose supports meet. Then \(R(p)\cap R(q)\) consists of one point \(a\in T\), and either one of \(p,q\) is \(\bar a\) and the other is adjacent to \(\bar a\), or both \(p\) and \(q\) are adjacent to \(\bar a\). In particular the interval \([p,q]_\Phi\) has at most three points.

**Proof.** If \(p\) and \(q\) both lie in \(\bar T\), their supports are different single points. Let \(p\notin\bar T\) and \(q=\bar a\). Then \(a\in R(p)\), and \(\varphi(a)=\bar a\ne p\); by Proposition 1.2, \(\bar a\) is adjacent to \(p\).

Let \(p,q\notin\bar T\). A point of \(R(p)\cap R(q)\) is not mapped to both \(p\) and \(q\), so by Proposition 1.2 it is a point \(a\in T\) with \(\bar a\) adjacent to one of them, say to \(p\). Then \(\varphi(a)=\bar a\ne q\), so \(\bar a\) is adjacent to \(q\) as well. Suppose \(a\ne b\) are two such points. The median of \(\bar a,\bar b,p\) in the median pretree \(\Phi\) lies in \([\bar a,p]_\Phi\cap[\bar b,p]_\Phi=\{p\}\), so \(\langle\bar a\,p\,\bar b\rangle\); in the same way \(\langle\bar a\,q\,\bar b\rangle\). By Lemma 2.3(3) of [Betweenness and pretrees](course:pretrees/betweenness-and-pretrees), \(\bar a,p,q,\bar b\) or \(\bar a,q,p,\bar b\) are in a row. In the first case \(p\) lies between \(\bar a\) and \(q\), in the second \(q\) between \(\bar a\) and \(p\); both contradict adjacency. So there is only one such point.

In each case \([p,q]_\Phi\) is \(\{p,q\}\) or \(\{p,\bar a,q\}\): if \(p\) and \(q\) are adjacent to \(\bar a\), the median argument gives \(\langle p\,\bar a\,q\rangle\), and a further point between \(p\) and \(q\) would lie between \(\bar a\) and one of them. \(\blacksquare\)

## 2. The group action

Let a group \(\Gamma\) act on \(M\) by homeomorphisms, with \(gT=T\) for all \(g\in\Gamma\). By Theorem 4.1 of the lesson on quotients and minimal actions, \(\Gamma\) acts on \(\Phi\) by automorphisms of the pretree, \(\varphi\) is equivariant, and \(gR_M(p)=R_M(gp)\); we write \(gp\) for the image of \(p\in\Phi\). Since \(g\bar a=\overline{ga}\), this gives for all \(p\in\Phi\)
\[
gR(p)=R(gp).
\]
In particular, if \(gp=p\), then the support \(R(p)\) is a closed set with \(gR(p)=R(p)\).

**Lemma 2.1.** Let \(\Gamma\) be a convergence group on \(M\), \(\gamma\in\Gamma\), and \(F\subseteq M\) a nonempty closed set with \(\gamma F=F\).

1. If \(\gamma\) is parabolic with fixed point \(c\), then \(c\in F\).
2. If \(\gamma\) is loxodromic with fixed points \(\lambda,\mu\), then \(F\subseteq\{\lambda,\mu\}\) or \(\{\lambda,\mu\}\subseteq F\). If moreover \(F\) is connected, then \(F=\{\lambda\}\), or \(F=\{\mu\}\), or \(\{\lambda,\mu\}\subseteq F\).

**Proof.** A connected metric space with more than one point is infinite, so \(M\) has at least three points, and the first lesson applies.

(1) Let \(x\in F\). If \(x\ne c\), then \(\gamma^nx\to c\) as \(n\to\infty\), because the powers of \(\gamma\) collapse with the pair \((c,c)\) (Proposition 2.3 and Lemma 1.2(3) of the first lesson). The points \(\gamma^nx\) lie in the closed set \(F\).

(2) Name the fixed points so that \((\gamma^n)_{n\ge1}\) collapses with \((\lambda,\mu)\) and \((\gamma^{-n})_{n\ge1}\) with \((\mu,\lambda)\) (Proposition 3.1 of the first lesson). If \(F\) contains a point \(x\) other than \(\lambda,\mu\), then \(\gamma^nx\to\mu\) and \(\gamma^{-n}x\to\lambda\), so both lie in \(F\). A set of two points is not connected. \(\blacksquare\)

## 3. No point is fixed by a minimal action

**Theorem 3.1.** Let \(\Gamma\) act minimally by homeomorphisms on a compact connected metric space \(M\) with more than one point, and let \(T\) be a nonempty invariant set of cut points. Then no point of \(\Phi(T)\) is fixed by all of \(\Gamma\).

**Proof.** *No support is all of \(M\).* For \(p=\bar a\) the support is one point. Let \(p\notin\bar T\) and suppose \(R(p)=M\). Choose \(a\in T\). It is a cut point, so there are \(x,y\in M\) with \(xay\). Both lie in \(R_M(a,p)=R_M(a,b)\) for some \(b\in T\setminus\{a\}\): \(xab\) and \(yab\) fail. But (T3), applied to \(xay\) and the point \(b\ne a\), gives \(xab\) or \(yab\).

If \(p\) were fixed by \(\Gamma\), its support would be a nonempty closed invariant set, hence all of \(M\) by minimality. \(\blacksquare\)

The theorem does not use the convergence property.

## 4. Parabolic elements

**Theorem 4.1.** Let \(\Gamma\) be a convergence group on a compact connected metric space \(M\) with more than one point, \(T\) an invariant set of cut points, and \(\gamma\in\Gamma\) a parabolic element whose fixed point \(c\) does not lie in \(T\). Then \(\gamma\) fixes exactly one point of \(\Phi(T)\). This point is not in \(\bar T\), and it is not adjacent to exactly one point of \(\Phi(T)\).

**Proof.** *There is a fixed point.* The point \(\varphi(c)\) is fixed, because \(\varphi\) is equivariant.

*No fixed point lies in \(\bar T\).* If \(\gamma\bar a=\bar a\), then \(\gamma a=a\), so \(a=c\); but \(c\notin T\).

*A fixed point has not exactly one neighbour.* The neighbours of a point \(p\notin\bar T\) lie in \(\bar T\). If \(p\) is fixed and has exactly one neighbour, that neighbour is fixed, and it lies in \(\bar T\).

*There is only one fixed point.* Let \(p\ne q\) be fixed. By Lemma 2.1(1) the supports \(R(p)\) and \(R(q)\) both contain \(c\). By Proposition 1.3 their common point lies in \(T\). But \(c\notin T\). \(\blacksquare\)

## 5. Exercises

**5.1.** Let \(M=[0,1]\), \(T=(0,1)\), and for \(t\in T\) let \(t^-\) be the flow that runs upwards towards \(t\) from below and does not arrive, as in Section 4 of the lesson on mapping to the completion. Use Proposition 1.2 to determine \(R(t^-)\), and compare with Exercise 5.2 there.

**5.2.** In the situation of Proposition 1.3, show that a support with more than one point is infinite.

**5.3.** Let \(\Gamma\) be a convergence group on \(M\) as in Theorem 4.1, and \(\gamma\) a parabolic element whose fixed point \(c\) lies in \(T\). Show that every point of \(\Phi(T)\) fixed by \(\gamma\) is \(\bar c\) or adjacent to \(\bar c\).

**5.4.** Show that in Theorem 3.1 the assumption that \(T\) is not empty is needed.

## 6. Solutions

**5.1.** No point of \(M\) is mapped to \(t^-\): the image of \(\varphi\) consists of the flows \(\bar s\) and the two flows of \(T\) directed upwards and downwards. The only point of \(\bar T\) adjacent to \(t^-\) is \(\bar t\) (Example 4.1 of the lesson on adjacent points). So \(R(t^-)=\{t\}\), as computed there from the definition.

**5.2.** A support is connected, and a connected metric space with two points \(x\ne y\) contains, for every number \(r\) strictly between \(0\) and the distance of \(x\) and \(y\), a point at distance \(r\) from \(x\); otherwise the points at distance less than \(r\) and those at distance more than \(r\) would be two disjoint nonempty open sets covering it.

**5.3.** Let \(\gamma p=p\) with \(p\ne\bar c\). By Lemma 2.1(1), \(c\in R(p)\). If \(p=\bar a\), then \(a=c\), which is excluded. So \(p\notin\bar T\), and by Proposition 1.2, since \(\varphi(c)=\bar c\ne p\), the point \(\bar c\) is adjacent to \(p\).

**5.4.** If \(T\) is empty, \(\Phi(T)\) has one point, the empty flow, and it is fixed by every group. A circle with the group of all rotations is an example of a minimal action on a space without cut points.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
