# The tree of cut points

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let a group \(\Gamma\) act as a minimal convergence group on a compact connected metric space \(B\) that has cut points. [The dendrite quotient is not a point](the-dendrite-quotient-is-not-a-point.md) shows that the dendrite quotient of \(B\) has no fixed point when some cut point has a stabilizer that is finite or contains a loxodromic element. This lesson treats the opposite situation, in which the group does fix a point of the dendrite quotient, for instance because the dendrite quotient is a single point. Then the cut points are arranged along a tree in the sense of graph theory, and the group acts on it (Theorem 1.1):

- every cut point is fixed by a parabolic element, and its stabilizer is infinite and contains no loxodromic element;
- the set \(P\) of cut points is a set of vertices of a tree \(\mathcal T\) on which \(\Gamma\) acts without inversions; every edge joins a cut point to a vertex that is not a cut point;
- if a cut point \(q\) separates two cut points \(a\) and \(b\) in \(B\), then \(q\) lies on the path from \(a\) to \(b\) in \(\mathcal T\);
- the tree has no invariant subtree other than itself, it has finitely many orbits of vertices and of edges, and all its edge stabilizers are infinite.

This is the tree of cut points used in OpenAI's proof (2026) of the Singer conjecture in dimension four outside the middle degree; the statement and its proof follow Section 6 of [OpenAI-S], with the hypotheses on the group in the form given below. The lesson uses the earlier lessons of this course.

## 1. The statement

Throughout, \(B\) is a compact connected metric space with more than one point, \(\Gamma\) a convergence group acting minimally on \(B\), and \(P\) the set of all cut points of \(B\), which is mapped to itself by \(\Gamma\). We assume \(P\ne\varnothing\). We use the objects of the earlier lessons, formed with \(T=P\): the completion \(\Phi=\Phi(P)\) with its betweenness \(\langle prq\rangle\), in which \(\bar P\) is the set of the flows \(\bar a\) towards points \(a\in P\); the action of \(\Gamma\) on \(\Phi\); and the dendrite quotient \(D=D_P(B)\) with the equivariant map \(f\colon B\to D\).

The hypotheses on the group are:

- (a) \(\Gamma\) is finitely generated;
- (b) \(\Gamma\) has the fixed-point property for trees with finite edge stabilizers ([Trees and classes of finite intervals](trees-and-classes-of-finite-intervals.md), Definition 1.1);
- (c) every infinite subgroup of \(\Gamma\) contains an element of infinite order;
- (z) \(\Gamma\) fixes a point of the dendrite quotient \(D_P(B)\).

Condition (z) holds if \(D_P(B)\) is a single point. In the application mentioned above, the group is finitely presented, has one end, has no elements of finite order, and does not split over a finite or two-ended subgroup; then (b) holds by Theorem 5.1 of [The fixed-point property for groups with one end](the-fixed-point-property-for-groups-with-one-end.md), and \(D_P(B)\) is a point by a theorem on convergence actions on dendrites ([Bowditch 2], Lemma 1.4), whose proof uses the theory of group actions on real trees. That theorem is not proved in this course; here (z) is a hypothesis.

A *tree* is, as in the lesson on trees, a nonempty discrete median pretree; its edges are the pairs of adjacent points. A *subtree* of a tree is a nonempty full subset.

**Theorem 1.1.** Let \(\Gamma\) be a convergence group acting minimally on a compact connected metric space \(B\) with more than one point, whose set \(P\) of cut points is not empty, and suppose (a), (b), (c) and (z). Then:

1. For every \(p\in P\), the stabilizer of \(p\) is infinite and contains no loxodromic element; it contains a parabolic element.
2. There is a class \(C\) of the finite interval relation of \(\Phi(P)\) that is mapped to itself by \(\Gamma\), and it contains \(\bar P\).
3. Let \(\mathcal T\) be the union of the intervals \([\bar a,\bar b]_\Phi\), \(a,b\in P\). Then \(\mathcal T\) is a tree with more than one point, \(\Gamma\) acts on it without inversions, every edge of \(\mathcal T\) has one end in \(\bar P\) and one end outside, and every point of \(\mathcal T\) outside \(\bar P\) has at least two neighbours in \(\mathcal T\).
4. If \(a,b,q\in P\) and \(q\) separates \(a\) from \(b\) in \(B\), then \(\bar q\) lies between \(\bar a\) and \(\bar b\) in \(\mathcal T\).
5. The only subtree of \(\mathcal T\) that is mapped to itself by \(\Gamma\) is \(\mathcal T\).
6. \(\mathcal T\) has finitely many orbits of points and finitely many orbits of edges.
7. The stabilizer of every edge of \(\mathcal T\) is infinite.

The proof takes the rest of the lesson.

## 2. Stabilizers of cut points

**Proposition 2.1.** Under the assumptions of Theorem 1.1, the stabilizer of every \(p\in P\) is infinite and contains no loxodromic element, and it contains a parabolic element.

**Proof.** Suppose the stabilizer of \(p\) is finite or contains a loxodromic element, and let \(T_0\) be the orbit of \(p\). The stabilizers of the points of \(T_0\) are conjugate to that of \(p\). By Theorem 1.1 of the lesson The dendrite quotient is not a point, applied to the set \(T_0\), \(\Gamma\) fixes no point of \(D_{T_0}(B)\).

Let \(f_0\colon B\to D_{T_0}(B)\) be the quotient map for \(T_0\). By Proposition 1.2 of [The dendrite quotient of a continuum](course:pretrees/the-dendrite-quotient-of-a-continuum), \(f(x)=f(y)\) means that no rational subset of points of \(P\) lies between \(x\) and \(y\); then none of points of \(T_0\) does, so \(f_0(x)=f_0(y)\). Hence there is a map \(g\colon D\to D_{T_0}(B)\) with \(g\circ f=f_0\). It is equivariant, because \(f\) and \(f_0\) are and \(f\) is surjective. So \(g\) maps the point of \(D\) fixed by \(\Gamma\) to a point of \(D_{T_0}(B)\) fixed by \(\Gamma\). This is a contradiction.

So the stabilizer of \(p\) is infinite and contains no loxodromic element. By (c) it contains an element of infinite order, which is parabolic or loxodromic, hence parabolic. \(\blacksquare\)

## 3. The invariant class

**Proposition 3.1.** Under the assumptions of Theorem 1.1, there is a class \(C\) of the finite interval relation of \(\Phi\) with \(gC=C\) for all \(g\in\Gamma\). It has more than one point, and it contains \(\bar P\).

**Proof.** By (z) a class of the least codense relation of \(\Phi\) is mapped to itself by \(\Gamma\). By Theorem 1.3 of the lesson The dendrite quotient is not a point, \(\Gamma\) fixes a point of \(\Phi\) or preserves a class \(C\) of the finite interval relation. The first is excluded by Theorem 3.1 of [Supports and fixed points in the completion](supports-and-fixed-points-in-the-completion.md), because the action is minimal and \(P\) is not empty. For the same reason \(C\) is not a single point.

*\(C\) contains a point of \(\bar P\).* The class \(C\) is full, and its intervals are finite. Take two points of \(C\); the first two points in the list of the interval between them are adjacent, and of two adjacent points of \(\Phi\) one lies in \(\bar P\) (Theorem 2.3 of [Adjacent points of the completion](course:pretrees/adjacent-points-of-the-completion)).

*\(C\) contains \(\bar P\).* Let \(\bar p\in C\). The orbit of \(p\) is dense in \(B\), because the action is minimal (Lemma 2.1 of [Quotients and minimal actions](quotients-and-minimal-actions.md)), and the points \(\overline{gp}=g\bar p\) lie in \(C\). Let \(q\in P\). It is a cut point, so \(B\setminus\{q\}\) is the union of two disjoint nonempty open sets \(U\) and \(V\). Each of them contains a point of the orbit: \(a\in U\), \(b\in V\). Then \(aqb\) in the pretree of \(B\), so \(\langle\bar a\,\bar q\,\bar b\rangle\) in \(\Phi\), and \(\bar q\in C\) because \(C\) is full. \(\blacksquare\)

## 4. The tree

Let \(C\) be the class of Proposition 3.1, and
\[
\mathcal T=\bigcup_{a,b\in P}[\bar a,\bar b]_\Phi .
\]
It lies in \(C\), because \(C\) is full and contains \(\bar P\).

**Lemma 4.1.** \(\mathcal T\) is a full subset of \(\Phi\), and it is mapped to itself by \(\Gamma\). It is a tree with more than one point; two points of \(\mathcal T\) are adjacent in \(\mathcal T\) exactly when they are adjacent in \(\Phi\). Every edge of \(\mathcal T\) has one end in \(\bar P\) and one outside, the action of \(\Gamma\) on \(\mathcal T\) is without inversions, and a point of \(\mathcal T\) outside \(\bar P\) has at least two neighbours in \(\mathcal T\).

**Proof.** Let \(u\in[\bar a,\bar b]_\Phi\) and \(v\in[\bar c,\bar d]_\Phi\) with \(a,b,c,d\in P\). By Lemma 3.1 of [Betweenness and pretrees](course:pretrees/betweenness-and-pretrees), \([u,v]_\Phi\) lies in the union of \([u,\bar a]_\Phi\), \([\bar a,\bar c]_\Phi\) and \([\bar c,v]_\Phi\). The first lies in \([\bar a,\bar b]_\Phi\) and the third in \([\bar c,\bar d]_\Phi\), because intervals are full. So \(\mathcal T\) is full. The group maps \(\bar P\) to itself and intervals to intervals.

A full subset of the median pretree \(\Phi\) is median, and the intervals of \(\mathcal T\) are intervals of \(\Phi\) inside \(C\), hence finite. So \(\mathcal T\) is a tree, with the adjacency of \(\Phi\). It contains \(\bar P\). If \(\bar P\) is a single point \(\bar a\), then \(a\) is fixed by \(\Gamma\), against minimality (Lemma 2.1 of the lesson on quotients and minimal actions). So \(\mathcal T\) has more than one point.

Of two adjacent points of \(\Phi\) exactly one lies in \(\bar P\). An element of \(\Gamma\) that exchanged the ends of an edge would map a point of \(\bar P\) to a point outside. A point \(u\in\mathcal T\) outside \(\bar P\) lies in some \([\bar a,\bar b]_\Phi\) and is not one of its ends; in the list of this interval it has a point before it and a point after it, which are its neighbours and lie in \(\mathcal T\). \(\blacksquare\)

This proves statements 2 and 3 of Theorem 1.1. Statement 4: if \(q\) separates \(a\) from \(b\), then \(\langle\bar a\,\bar q\,\bar b\rangle\) in \(\Phi\), and \(\mathcal T\) has the betweenness of \(\Phi\).

**Lemma 4.2** (statement 5). Let \(\mathcal S\subseteq\mathcal T\) be a nonempty full subset with \(g\mathcal S=\mathcal S\) for all \(g\in\Gamma\). Then \(\mathcal S=\mathcal T\).

**Proof.** \(\mathcal S\) is not a single point, because \(\Gamma\) fixes no point of \(\Phi\). As in the proof of Proposition 3.1, \(\mathcal S\) then contains two adjacent points, hence a point \(\bar p\) with \(p\in P\), and then, by the argument with the dense orbit of \(p\), every \(\bar q\) with \(q\in P\). Since \(\mathcal S\) is full, it contains all intervals \([\bar a,\bar b]_\Phi\). \(\blacksquare\)

**Lemma 4.3** (statement 6). \(\mathcal T\) has finitely many orbits of points and finitely many orbits of edges.

**Proof.** Choose \(o\in\mathcal T\) and generators \(s_1,\dots,s_n\) of \(\Gamma\), by (a); we may assume that the inverse of each generator is among them. Let \(K\) be the union of the finite intervals \([o,s_io]_\Phi\), and \(\mathcal E_K\) the finite set of the edges of these intervals. Let \(\mathcal K\) be the union of the sets \(gK\), \(g\in\Gamma\), and \(\mathcal E\) the set of the edges \(ge\), \(e\in\mathcal E_K\), \(g\in\Gamma\).

Call a sequence of points a *chain* if consecutive points form an edge of \(\mathcal E\). Every point of \(\mathcal K\) is joined to \(o\) by a chain. Indeed, for \(g=s_{i_1}\cdots s_{i_k}\) the points \(o,\ s_{i_1}o,\ s_{i_1}s_{i_2}o,\ \dots,\ go\) are such that each is joined to the next by the list of a translate of some \([o,s_io]_\Phi\); and a point of \(gK\) is joined to \(go\) by the list of an interval \(g[o,s_io]_\Phi\).

*\(\mathcal K\) is full.* Let \(x,y\in\mathcal K\), joined by a chain, which we take without repeated points by removing the part between two occurrences of a point. A chain without repetition from \(x\) to \(y\) is the list of \([x,y]_\Phi\): it is a path from \(x\) to \(y\) in the tree \(\mathcal T\), and such a path is unique. So \([x,y]_\Phi\subseteq\mathcal K\).

By Lemma 4.2, \(\mathcal K=\mathcal T\). So every point of \(\mathcal T\) is a translate of one of the finitely many points of \(K\). Let \(\{x,y\}\) be an edge of \(\mathcal T\). The points \(x\) and \(y\) are joined by a chain without repetition, which is the list of \([x,y]_\Phi=\{x,y\}\). So \(\{x,y\}\) is an edge of \(\mathcal E\), a translate of one of the finitely many edges of \(\mathcal E_K\). \(\blacksquare\)

**Lemma 4.4** (statement 7). The stabilizer of every edge of \(\mathcal T\) is infinite.

**Proof.** Suppose the edge \(e\) has a finite stabilizer. Let \(\mathcal E'\) be the set of edges of \(\mathcal T\) that are not translates of \(e\); it is mapped to itself by \(\Gamma\). Contract these edges: let \(\sim\) be the relation of Proposition 2.1 of the lesson on trees, for the tree \(\mathcal T\) and the set \(\mathcal E'\). Then \(\mathcal T/{\sim}\) is a tree on which \(\Gamma\) acts. Its edges correspond to the edges of \(\mathcal T\) outside \(\mathcal E'\), the translates of \(e\), and the stabilizer of an edge of \(\mathcal T/{\sim}\) is the stabilizer of the corresponding translate of \(e\), which is conjugate to that of \(e\) and finite.

The action on \(\mathcal T/{\sim}\) is without inversions: an element that exchanged two adjacent classes would map the edge of \(\mathcal T\) between them to itself and exchange its ends, which is excluded by Lemma 4.1.

By (b), \(\Gamma\) fixes a point of \(\mathcal T/{\sim}\), that is, a class \(X\). A class is a nonempty full subset of \(\mathcal T\). By Lemma 4.2, \(X=\mathcal T\). But the ends of \(e\) are not related, because \(e\notin\mathcal E'\) (Proposition 2.1(2) there). This is a contradiction. \(\blacksquare\)

Statement 1 of Theorem 1.1 is Proposition 2.1. This proves the theorem.

## 5. Exercises

**5.1.** Show that, under the assumptions of Theorem 1.1, every point of \(\bar P\) has at least two neighbours in \(\mathcal T\).

**5.2.** Under the assumptions of Theorem 1.1, let \(r\in\mathcal T\) be a point outside \(\bar P\). Show that the stabilizer of \(r\) is infinite.

**5.3.** In the proof of Lemma 4.4, where is the minimality of the action on \(B\) used?

**5.4.** Let \(\{\bar a,r\}\) be an edge of \(\mathcal T\), with \(a\in P\). Show that its stabilizer contains no loxodromic element.

## 6. Solutions

**5.1.** Let \(p\in P\). Since \(p\) is a cut point, \(B\setminus\{p\}\) is the union of two disjoint nonempty open sets, and each contains a point of the dense orbit of \(p\); these are cut points \(a,b\) with \(apb\). So \(\bar p\) lies between \(\bar a\) and \(\bar b\) in \(\mathcal T\), and in the list of \([\bar a,\bar b]_\Phi\) it has a neighbour before it and one after it.

**5.2.** The point \(r\) has a neighbour \(\bar a\) in \(\mathcal T\), and the stabilizer of the edge \(\{\bar a,r\}\) is infinite by Lemma 4.4; it is contained in the stabilizer of \(r\).

**5.3.** Through Lemma 4.2: the class \(X\) fixed by the group is a full invariant subset, and Lemma 4.2, which rests on the density of the orbits of cut points and on the absence of fixed points in \(\Phi\), shows that it is all of \(\mathcal T\).

**5.4.** The stabilizer of the edge is contained in the stabilizer of the point \(a\in B\), which contains no loxodromic element by Proposition 2.1.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
- [Bowditch 2] B. H. Bowditch, *Connectedness properties of limit sets*, Transactions of the American Mathematical Society 351 (1999). Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-connected.pdf
- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
