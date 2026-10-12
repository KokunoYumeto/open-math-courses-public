# The dendrite quotient is not a point

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A compact connected metric space \(M\) with a set \(T\) of cut points has a dendrite quotient \(D\), in which two points are identified unless a set of points of \(T\) ordered like the rational numbers separates them ([The dendrite quotient of a continuum](course:pretrees/the-dendrite-quotient-of-a-continuum)). It can be a single point. This lesson proves that it is not, when a suitable group acts: for a minimal convergence action of a group \(\Gamma\) satisfying three conditions, and an invariant set of cut points whose stabilizers are finite or contain loxodromic elements, the group fixes no point of \(D\) (Theorem 1.1). In particular \(D\) has more than one point, and \(M\) has, between suitable points, sets of cut points ordered like the rational numbers. A second statement (Theorem 1.3) covers the opposite case: if the group fixes a point of \(D\), for example because \(D\) is a single point, and fixes no point of the completion \(\Phi(T)\), then it preserves a class of the finite interval relation of \(\Phi(T)\), which is a tree.

The proof follows the construction of \(D\) step by step. The dendrite quotient is the quotient of the completion \(\Phi(T)\) by its least codense relation, and this relation is reached from equality by repeating one step along the ordinal numbers ([The dense quotient of a pretree](course:pretrees/the-dense-quotient-of-a-pretree)). One shows by transfinite induction that at no stage a class is invariant under \(\Gamma\). At each successor step the classes of the previous stage that are identified form a tree, and the hypothesis on actions on trees is applied.

The statement is Theorem 6.1 of [Bowditch], for groups in which infinite subgroups contain elements of infinite order; the proof follows Lemma 6.13 and the proof of Theorem 6.1 there. The lesson uses all earlier lessons of this course.

## 1. The statement

Throughout, \(M\) is a compact connected metric space with more than one point, \(\Gamma\) a convergence group on \(M\), and \(T\) a set of cut points of \(M\) with \(gT=T\) for all \(g\in\Gamma\). As in the earlier lessons, \(\Phi=\Phi(T)\) is the completion of the pretree \(T\), with betweenness \(\langle prq\rangle\); \(\Gamma\) acts on it by automorphisms. The dendrite quotient \(D=D_T(M)\) is, as a set, the quotient of \(\Phi\) by its least codense relation \(\approx\), and \(\Gamma\) acts on \(D\) ([Quotients and minimal actions](quotients-and-minimal-actions.md), Theorem 4.1).

For every ordinal \(\alpha\) let \(R_\alpha\) be the relation on \(\Phi\) of the lesson on the dense quotient: \(R_0\) is equality; \(p\,R_{\alpha+1}\,q\) holds if the interval \([p,q]_\Phi\) meets only finitely many classes of \(R_\alpha\); and \(R_\lambda\) is the union of the \(R_\beta\), \(\beta<\lambda\), for a limit ordinal \(\lambda\). These are full relations, they increase with \(\alpha\), and \(R_\alpha\) is the relation \(\approx\) for all sufficiently large \(\alpha\) (Lemma 5.1 and Theorem 5.2 there). The relation \(R_1\) is the finite interval relation.

**Theorem 1.1.** Let \(\Gamma\) be a convergence group acting minimally on a compact connected metric space \(M\) with more than one point, and \(T\) a nonempty invariant set of cut points. Suppose that:

- (a) \(\Gamma\) is finitely generated;
- (b) \(\Gamma\) has the fixed-point property for trees with finite edge stabilizers ([Trees and classes of finite intervals](trees-and-classes-of-finite-intervals.md), Definition 1.1);
- (c) every infinite subgroup of \(\Gamma\) contains an element of infinite order;
- (d) for every \(a\in T\), the stabilizer of \(a\) is finite or contains a loxodromic element.

Then for every ordinal \(\alpha\), no class of \(R_\alpha\) is mapped to itself by all of \(\Gamma\). Consequently \(\Gamma\) fixes no point of the dendrite quotient \(D_T(M)\), and \(D_T(M)\) has more than one point.

Condition (c) holds for groups without elements of finite order other than the identity. The consequence follows from the first statement: for large \(\alpha\) the classes of \(R_\alpha\) are the points of \(D\), and a space with one point has a fixed point.

**Corollary 1.2.** Let \(\Gamma\) satisfy (a), (b) and (c) and act as a minimal convergence group on \(M\). If \(M\) has a cut point whose stabilizer is finite or contains a loxodromic element, then the dendrite quotient of \(M\) formed with the set of all cut points has more than one point.

**Proof.** Let \(T_0\) be the orbit of this cut point. The stabilizers of its points are conjugate, so (d) holds for \(T_0\), and \(D_{T_0}(M)\) has more than one point: there are \(x,y\in M\) with different images. By Proposition 1.2 of the lesson on the dendrite quotient, the interval \((x,y)\) of the pretree \(M\) contains a rational subset consisting of points of \(T_0\). These are cut points, so by the same proposition \(x\) and \(y\) have different images in the dendrite quotient formed with all cut points. \(\blacksquare\)

Conditions (d), minimality and \(T\ne\varnothing\) are needed only for the first two relations, equality and the finite interval relation. The rest of the induction is the following statement, which is also of use when the dendrite quotient is a point.

**Theorem 1.3.** Let \(\Gamma\) be a convergence group on a compact connected metric space \(M\) with more than one point, and \(T\) an invariant set of cut points. Suppose that \(\Gamma\) satisfies (a), (b) and (c). If for some ordinal \(\alpha\) a class of \(R_\alpha\) is mapped to itself by all of \(\Gamma\), then \(\Gamma\) fixes a point of \(\Phi(T)\) or maps a class of the finite interval relation of \(\Phi(T)\) to itself.

In particular, if \(\Gamma\) fixes a point of the dendrite quotient, for example if the dendrite quotient is a single point, then \(\Gamma\) fixes a point of \(\Phi(T)\) or preserves a class of the finite interval relation.

## 2. Two full sets next to each other

Let \(\Theta\) be a median pretree, and \(X,Y\) disjoint nonempty full subsets such that \(X\cup Y\) is full. A point \(p\in Y\) is an *entry point of \(Y\) from \(X\)* if \([x,p]\cap Y=\{p\}\) for some \(x\in X\).

**Lemma 2.1.** Let \(p\) be an entry point of \(Y\) from \(X\).

1. \([x,p]\cap Y=\{p\}\) for every \(x\in X\).
2. For \(x\in X\) and \(y\in Y\): \(p\in[x,y]\), and \([x,y]\cap Y=[p,y]\).
3. \(p\) is the only entry point of \(Y\) from \(X\).

**Proof.** (1) Let \([x_0,p]\cap Y=\{p\}\) and \(x\in X\). The median \(m\) of \(x_0,x,p\) lies in \([x_0,x]\subseteq X\), so \(m\ne p\). It lies in \([x,p]\), so \([x,p]=[x,m]\cup[m,p]\). Here \([x,m]\subseteq X\), and \([m,p]\subseteq[x_0,p]\) meets \(Y\) only in \(p\).

(2) The median \(q\) of \(x,y,p\) lies in \([y,p]\subseteq Y\) and in \([x,p]\); by (1), \(q=p\). So \(p\in[x,y]\), and \([x,y]=[x,p]\cup[p,y]\), where \([x,p]\) meets \(Y\) only in \(p\) and \([p,y]\subseteq Y\).

(3) Let \(p'\) be another entry point and \(x\in X\). The median of \(x,p,p'\) lies in \([p,p']\subseteq Y\), in \([x,p]\) and in \([x,p']\); by (1) it is \(p\), and it is \(p'\). \(\blacksquare\)

**Lemma 2.2.** Let \(\Theta\) be a complete median pretree, and \(X,Y\) disjoint nonempty full subsets such that \(X\cup Y\) is full. Then \(Y\) has an entry point from \(X\), or \(X\) has an entry point from \(Y\).

**Proof.** Choose \(x\in X\), \(y\in Y\), and let \(A=[x,y]\cap X\). It is full and linear and contains \(x\); with the direction of \([x,y]\) in which \(x\) is least, it is a directed arc with least point \(x\). Since \(\Theta\) is complete, \(A\) has a supremum (Theorem 4.3 of [Directed arcs and suprema](course:pretrees/directed-arcs-and-suprema)).

*If \(A\) has a greatest point \(p\)*: then \(p\in X\). A point of \([y,p]\cap X\) lies in \(A\), so it is not after \(p\), and it lies in \([p,y]\), so it is not before \(p\). Hence \([y,p]\cap X=\{p\}\), and \(p\) is an entry point of \(X\) from \(Y\).

*If \(A\) has no greatest point*: let \(p\) be its supremum. Then \([x,p)\) is a final segment of \(A\) that contains the least point, so \(A=[x,p)\), and \(p\notin A\). Let \(q\) be the median of \(x,y,p\); we show \(q=p\). Suppose \(q\ne p\). Then \(q\in[x,p)=A\), and there is \(w\in A\) after \(q\). The direction of \(A\) is also the direction of \([x,p)\) with \(x\) least, since a linear set has only one direction with a given least point. So \(w\in(q,p)\); and \(w\in(q,y]\), because \(w\) lies in \([x,y]\) after \(q\). Now \(q\in[y,p]\). If \(q=y\), then \((q,y]\) is empty. Otherwise \(q\in(y,p)\), and \([y,q]\cap[q,p]=\{q\}\) by Lemma 3.2 of [Betweenness and pretrees](course:pretrees/betweenness-and-pretrees); but \(w\) lies in both sets. This is a contradiction.

So \(p=q\in[x,y]\). Since \(p\notin A\), it is not in \(X\); so \(p\in Y\). And \([x,p]\cap Y=\{p\}\), because \([x,p)=A\subseteq X\). So \(p\) is an entry point of \(Y\) from \(X\). \(\blacksquare\)

## 3. The relations and the group

**Lemma 3.1.** Let \(g\) be an automorphism of a pretree \(S\), and \(R_\alpha\) the relations defined on \(S\) as in Section 1. Then for every ordinal \(\alpha\) and all \(p,q\in S\): \(p\,R_\alpha\,q\) if and only if \(gp\,R_\alpha\,gq\).

**Proof.** By transfinite induction. For \(\alpha=0\) this is clear. If \(g\) and its inverse map classes of \(R_\alpha\) to classes of \(R_\alpha\), then the interval \([p,q]\) meets finitely many classes exactly when its image \([gp,gq]\) does. At a limit ordinal the relation is a union of relations for which the statement holds. \(\blacksquare\)

So \(\Gamma\) maps classes of \(R_\alpha\) to classes of \(R_\alpha\), and it acts on the pretree \(\Phi/R_\alpha\) by automorphisms, because the betweenness of classes is defined through points. Recall from the lesson on the dense quotient (Lemma 4.2) that \(\Phi/R_{\beta+1}\) is the quotient of the pretree \(\Phi/R_\beta\) by its finite interval relation: the classes of \(R_\beta\) contained in one class of \(R_{\beta+1}\) form a class of the finite interval relation of \(\Phi/R_\beta\).

**Lemma 3.2.** Let \(\gamma\in\Gamma\) have infinite order and fix two points \(p,q\) of \(\Phi\) such that \([p,q]_\Phi\) is infinite. Then \(\gamma\) is loxodromic, \(p\) and \(q\) are the only points of \(\Phi\) fixed by \(\gamma\), and they lie between no two points of \(\Phi\).

**Proof.** The element \(\gamma\) is parabolic or loxodromic. Suppose it is parabolic, with fixed point \(c\in M\). If \(c\notin T\), then \(\gamma\) fixes only one point of \(\Phi\) (Theorem 4.1 of [Supports and fixed points in the completion](supports-and-fixed-points-in-the-completion.md)). Let \(c\in T\). A point \(r\ne\bar c\) of \(\Phi\) fixed by \(\gamma\) is not in \(\bar T\), because \(\gamma\) fixes no point of \(T\) but \(c\); and its support is a closed set mapped to itself by \(\gamma\), so it contains \(c\) (Lemma 2.1(1) there). Since \(\varphi(c)=\bar c\ne r\), the point \(\bar c\) is adjacent to \(r\) (Proposition 1.2 there). So \(p\) and \(q\) are equal or adjacent to \(\bar c\), and \([p,q]_\Phi\) lies in the union of \([p,\bar c]_\Phi\) and \([\bar c,q]_\Phi\), which has at most three points. This is a contradiction. So \(\gamma\) is loxodromic.

We apply Theorem 1.2 of [Loxodromic elements and the completion](loxodromic-elements-and-the-completion.md). If \(p\) is a point outside \(\bar T\) with exactly one neighbour, let \(p_1\) be this neighbour, which is fixed by \(\gamma\) and lies in \(\bar T\); otherwise let \(p_1=p\). Define \(q_1\) from \(q\) in the same way. Then \(p_1,q_1\) are fixed points of \(\gamma\) in \(\Phi_0\), and \([p_1,q_1]_\Phi\) is infinite, because \([p,q]_\Phi\) lies in the union of \([p,p_1]_\Phi\), \([p_1,q_1]_\Phi\) and \([q_1,q]_\Phi\), and the first and third have at most two points. So case 2 of that theorem holds: \(\gamma\) fixes exactly two points of \(\Phi\), and they lie between no two points of \(\Phi\). The points \(p\) and \(q\) are fixed, so they are these two points. \(\blacksquare\)

## 4. The induction

Let \(P(\alpha)\) be the statement: no class of \(R_\alpha\) is mapped to itself by \(\Gamma\). We show, under the assumptions of Theorem 1.3:

> if \(\alpha\ge2\) and \(P(\beta)\) holds for all \(\beta<\alpha\), then \(P(\alpha)\) holds.

This proves Theorem 1.3: if some class of some \(R_\alpha\) is invariant, the least such \(\alpha\) is \(0\) or \(1\). It also proves Theorem 1.1 by transfinite induction, because under the assumptions made there \(P(0)\) and \(P(1)\) hold: \(\Gamma\) fixes no point of \(\Phi\) by Theorem 3.1 of the lesson on supports, which uses that the action is minimal and \(T\) not empty; and \(P(1)\) is Theorem 3.1 of the lesson on trees and classes of finite intervals, which uses (b) and (d).

*\(\alpha\) a limit ordinal.* Suppose the class of \(x\in\Phi\) under \(R_\alpha\) is invariant, and let \(\gamma_1,\dots,\gamma_n\) generate \(\Gamma\), by (a). For each \(i\), \(x\,R_\alpha\,\gamma_ix\), so \(x\,R_{\beta_i}\,\gamma_ix\) for some \(\beta_i<\alpha\). Let \(\beta\) be the largest of the \(\beta_i\). The set of \(g\in\Gamma\) with \(x\,R_\beta\,gx\) contains the generators, and by Lemma 3.1 it is a subgroup: from \(x\,R_\beta\,gx\) and \(x\,R_\beta\,hx\) one gets \(gx\,R_\beta\,ghx\), hence \(x\,R_\beta\,ghx\), and \(g^{-1}x\,R_\beta\,x\). So it is \(\Gamma\), and the class of \(x\) under \(R_\beta\) is invariant, against \(P(\beta)\).

*\(\alpha=\beta+1\) with \(\beta\ge1\).* Suppose \(P(\beta)\) holds and a class \(\Xi\) of \(R_\alpha\) is invariant. Let \(\Sigma\) be the set of classes of \(R_\beta\) contained in \(\Xi\).

**Step 1: \(\Sigma\) is a tree on which \(\Gamma\) acts, and no point of \(\Sigma\) is fixed.** By Section 3, \(\Sigma\) is a class of the finite interval relation of \(\Phi/R_\beta\). So it is full, and its intervals are finite. The pretree \(\Phi/R_\beta\) is median, as a quotient of the median pretree \(\Phi\) (Theorem 4.1 of [Quotients of pretrees](course:pretrees/quotients-of-pretrees)); so the full subset \(\Sigma\) is median. Hence \(\Sigma\) is a tree, and two points of \(\Sigma\) are adjacent in \(\Sigma\) exactly when they are adjacent in \(\Phi/R_\beta\). The group maps \(\Xi\) to itself, so it acts on \(\Sigma\). A fixed point would be an invariant class of \(R_\beta\).

**Step 2: the action on \(\Sigma\) is without inversions.** Let \(X,Y\in\Sigma\) be adjacent. As subsets of \(\Phi\) they are disjoint, nonempty and full, and \(X\cup Y\) is full (Corollary 3.2(4) of the lesson on quotients). The pretree \(\Phi\) is complete and median. By Lemma 2.2, \(Y\) has an entry point from \(X\), or \(X\) from \(Y\).

Not both: let \(p\) be an entry point of \(Y\) from \(X\) and \(p'\) one of \(X\) from \(Y\). By Lemma 2.1(1), \([p',p]\) meets \(Y\) only in \(p\) and \(X\) only in \(p'\). Since \([p',p]\subseteq X\cup Y\), the points \(p\) and \(p'\) are adjacent in \(\Phi\). Then \(p\,R_1\,p'\), so \(p\,R_\beta\,p'\) because \(\beta\ge1\), and \(X=Y\).

An element of \(\Gamma\) that exchanges \(X\) and \(Y\) would map an entry point of \(Y\) from \(X\) to an entry point of \(X\) from \(Y\). So there is none.

**Step 3: an edge with infinite stabilizer.** Let \(X,Y\in\Sigma\) be adjacent, with \(G=\Gamma(X)\cap\Gamma(Y)\) infinite, and named so that \(Y\) has an entry point \(p\) from \(X\). We show that \(Y=\{p\}\) and that \(p\) lies between no two points of \(\Phi\).

*(i) An element.* By Lemma 2.1(3), every element of \(G\) fixes \(p\). By (c) there is \(\gamma\in G\) of infinite order.

*(ii) The set \(W\).* Let \(W\) be the set of points \(w\ne p\) of \(\Phi\) such that \(\langle w\,p\,x\rangle\) fails for all \(x\in X\). It contains \(X\), because \(X\) is full and \(p\notin X\). It does not meet \(Y\): for \(y\in Y\), \(y\ne p\), and \(x\in X\) we have \(\langle x\,p\,y\rangle\) by Lemma 2.1(2). And \(\gamma W=W\). To show that a point \(w\ne p\) lies in \(W\) it suffices that \(\langle w\,p\,x\rangle\) fails for one \(x\in X\): if \(w\notin X\), Lemma 1.1 of the lesson on quotients, applied to the full sets \(\{w\}\) and \(X\), shows that it then fails for all \(x\in X\).

*(iii) \(\gamma\) fixes a point of \(W\).* Suppose not. Choose \(y\in X\), and let \(x\) be the median of \(y,\gamma y,p\). It lies in \([y,\gamma y]\subseteq X\), and in \([y,p]\) and \([\gamma y,p]\). The point \(\gamma x\) lies in \(\gamma[y,p]=[\gamma y,p]\) as well. The points \(x\) and \(\gamma x\) are different, because \(x\in W\), and different from \(p\). They lie in the linearly ordered set \([\gamma y,p]\), so one of them lies between \(p\) and the other. If \(\gamma x\) lies between \(p\) and \(x\), replace \(\gamma\) by \(\gamma^{-1}\) and \(x\) by \(\gamma x\). After this,
\[
x\in X,\qquad\langle p\,x\,\gamma x\rangle .
\]
Applying \(\gamma^n\) gives \(\langle p\,\gamma^nx\,\gamma^{n+1}x\rangle\) for all \(n\ge0\). So the intervals \((p,\gamma^nx)_\Phi\) increase with \(n\), and \(\gamma^nx\) lies in the next one and not in its own. Let \(A\) be their union. It contains \(x\); it is full and linear, as the union of an increasing sequence of full linear sets; and \(\gamma A=A\). Direct \(A\) by: \(u<v\) if \(u\) lies between \(p\) and \(v\). This is the direction of each interval \([p,\gamma^nx]_\Phi\) with \(p\) least, so it is a direction of \(A\), and \(\gamma\) preserves it. Every \(u\in A\) lies in some \((p,\gamma^nx)_\Phi\), so \(u<\gamma^nx\): the directed arc \(A\) has no greatest point.

Since \(\Phi\) is complete, \(A\) has a supremum \(z\): for \(u\in A\), the points of \(A\) from \(u\) on form the interval \([u,z)_\Phi\). In particular \(\gamma x\in(x,z)_\Phi\). With \(\langle p\,x\,\gamma x\rangle\), Lemma 2.3(1) of the lesson on betweenness gives \(\langle p\,x\,z\rangle\). So \(z\ne p\), and \(\langle z\,p\,x\rangle\) fails; hence \(z\in W\).

The supremum is unique. Let \(z'\) be a supremum too, and \(B=[x,z)_\Phi=[x,z')_\Phi\), which has no greatest point. Let \(m\) be the median of \(x,z,z'\). If \(m\in B\), take \(v\in B\) after \(m\); then \(v\in(m,z)_\Phi\) and \(v\in(m,z')_\Phi\). Since \(m\in[z,z']_\Phi\) and \(m\) is neither \(z\) nor \(z'\), these two intervals have no common point, by Lemma 3.2 of the lesson on betweenness. So \(m\notin B\). Then \(m\in[x,z]_\Phi\) gives \(m=z\), and \(m\in[x,z']_\Phi\) gives \(m=z'\).

The automorphism \(\gamma\) maps the directed arc \(A\) to itself, so it maps its supremum to its supremum: \(\gamma z=z\). So \(z\) is a point of \(W\) fixed by \(\gamma\), a contradiction.

*(iv) An infinite interval.* Let \(q\in W\) with \(\gamma q=q\). Then \(q\notin Y\), while \(p\in Y\). So \(p\) and \(q\) are not related by \(R_\beta\), and not by \(R_1\), because \(R_1\le R_\beta\): the interval \([p,q]_\Phi\) is infinite.

*(v) \(p\) lies between no two points.* By Lemma 3.2, applied to \(\gamma\) and its fixed points \(p,q\).

*(vi) \(Y=\{p\}\).* Let \(y\in Y\) and \(x\in X\). By Lemma 2.1(2), \(p\in[x,y]_\Phi\). Since \(p\ne x\) and \(p\) is not between \(x\) and \(y\), we get \(y=p\).

**Step 4: removing leaves.** Let \(\mathcal Y\) be the set of all \(Y\in\Sigma\) for which there is an edge \(\{X,Y\}\) of \(\Sigma\) with infinite stabilizer such that \(Y\) has an entry point from \(X\). By Step 3, each \(Y\in\mathcal Y\) consists of one point of \(\Phi\) that lies between no two points of \(\Phi\). So \(Y\) lies between no two points of \(\Phi/R_\beta\), by the definition of the betweenness of classes. The set \(\mathcal Y\) is mapped to itself by \(\Gamma\). Let
\[
S=\Sigma\setminus\mathcal Y .
\]

*\(S\) is not empty.* If \(\Sigma\) has one point, \(\mathcal Y\) is empty. If \(\Sigma\) has two points, they are adjacent, and by Step 2 only one of them has an entry point from the other. If \(\Sigma\) has at least three points, two of them are not adjacent, because a tree has no three pairwise adjacent points; a point between them is not in \(\mathcal Y\).

*\(S\) is a tree with finite edge stabilizers.* A point of \(\Sigma\) between two points of \(S\) is not in \(\mathcal Y\). So \(S\) is a nonempty full subset of the tree \(\Sigma\), hence a tree, and its edges are edges of \(\Sigma\). If an edge \(\{X,Y\}\) of \(S\) had an infinite stabilizer, one of its ends would have an entry point from the other, by Step 2, and would lie in \(\mathcal Y\).

*Conclusion.* \(\Gamma\) acts on the tree \(S\) without inversions, by Step 2, and with finite edge stabilizers. By (b) it fixes a point of \(S\). This is an invariant class of \(R_\beta\), against \(P(\beta)\). \(\blacksquare\)

## 5. Exercises

**5.1.** Let \(\Theta\) be the real line, \(X\) the set of numbers \(\le0\) and \(Y\) the set of numbers \(>0\). Which of the two sets has an entry point from the other? Do the same in the pretree of the rational numbers for the sets of rational numbers below and above \(\sqrt2\), and explain why this does not contradict Lemma 2.2.

**5.2.** Where does the proof of Theorem 1.1 use that \(\beta\ge1\) in the successor step?

**5.3.** Let \(M=\mathbb R\cup\{-\infty,\infty\}\) with the group of integer translations (Exercise 4.1 of the lesson on loxodromic elements) and \(T=\mathbb R\). Show that the dendrite quotient is \(M\) itself and that the group fixes two points of it. Which assumptions of Theorem 1.1 fail?

## 6. Solutions

**5.1.** On the real line, \([y,0]\cap X=\{0\}\) for \(y>0\), so \(0\) is an entry point of \(X\) from \(Y\); \(Y\) has no entry point from \(X\), because \([x,p]\) contains points of \(Y\) below \(p\) for every \(p>0\). For the rational numbers neither set has an entry point from the other: for rational \(p>\sqrt2\) there are rational numbers between \(\sqrt2\) and \(p\), and likewise below. The pretree of the rational numbers is not complete, so Lemma 2.2 does not apply.

**5.2.** In Step 2, to conclude from \(p\,R_1\,p'\) that \(p\) and \(p'\) lie in the same class of \(R_\beta\); and in Step 3(iv), to conclude that \([p,q]_\Phi\) is infinite. For \(\beta=0\) the classes are points, adjacent points of \(\Phi\) can be exchanged by a group element in principle, and the argument is replaced by the one of the lesson on trees and classes of finite intervals.

**5.3.** Any two points of \(M\) are separated by the rational numbers between them, which are cut points; so by Proposition 1.2 of the lesson on the dendrite quotient the quotient map is injective, hence a homeomorphism onto \(D\). The translations fix \(-\infty\) and \(\infty\). The action is not minimal, since \(\{\infty\}\) is a closed invariant set; and the group of integers does not have the fixed-point property for trees with finite edge stabilizers (Exercise 4.2 of the lesson on trees). Conditions (a), (c) and (d) hold: the group is generated by one element, it has no elements of finite order other than the identity, and the stabilizers of the points of \(T\) are trivial.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
