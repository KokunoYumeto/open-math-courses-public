# Trees and classes of finite intervals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\Gamma\) be a convergence group acting minimally on a compact connected metric space \(M\), and \(T\) a nonempty invariant set of cut points. By [Supports and fixed points in the completion](supports-and-fixed-points-in-the-completion.md), \(\Gamma\) fixes no point of the completion \(\Phi(T)\). The dendrite quotient of \(M\) is obtained from \(\Phi(T)\) by identifying points, and the question is whether \(\Gamma\) can fix a point after the identification. This lesson treats the first identification, in which two points are identified when the interval between them is finite. A class of this relation is a tree, and the group acts on it. The result (Theorem 3.1) is that no class is invariant, provided that:

- actions of \(\Gamma\) on trees with finite edge stabilizers have fixed vertices, a property of the group that is stated in Section 1; and
- every point of \(T\) has a stabilizer that is finite or contains a loxodromic element.

The lesson follows Lemmas 6.7 and 6.12 of [Bowditch]. Section 2 shows how to pass from a tree to a smaller tree by contracting edges, in the language of pretrees; this replaces the use of graphs of groups in the proof of Lemma 6.7 there. The lesson uses the earlier lessons of this course and, from the course on pretrees, [Discrete pretrees and trees](course:pretrees/discrete-pretrees-and-trees) and [Quotients of pretrees](course:pretrees/quotients-of-pretrees).

## 1. Trees and group actions

In this course a *tree* is a nonempty discrete median pretree \(S\): a set with a betweenness relation in which all intervals are finite and every three points have a median. By Theorem 2.1 of the lesson on discrete pretrees this is the same as the vertex set of a tree in the sense of graph theory: the *edges* are the pairs \(\{x,y\}\) of adjacent points, and \(y\) lies between \(x\) and \(z\) exactly when it is an inner vertex of the path from \(x\) to \(z\). The points of the interval \([x,z]\), listed in their order from \(x\) to \(z\), form this path; consecutive points are adjacent (Lemma 1.2 there). The edges \(\{x_{i-1},x_i\}\) of this list are called the *edges of \([x,z]\)*.

We use two facts from the course on pretrees. In a median pretree no three points are pairwise adjacent. And if distinct points \(x_0,\dots,x_{n-1}\), \(n\ge3\), of a pretree are such that each is adjacent to the next and \(x_{n-1}\) to \(x_0\), then any two of them are adjacent (Lemma 4.3 of [Betweenness and pretrees](course:pretrees/betweenness-and-pretrees)). So a tree contains no such cycle.

Let a group \(\Gamma\) act on a tree \(S\) by automorphisms of the pretree. Write \(\Gamma(x)\) for the stabilizer of a point \(x\). The *stabilizer of an edge* \(\{x,y\}\) is \(\Gamma(x)\cap\Gamma(y)\). The action is *without inversions* if no element of \(\Gamma\) exchanges two adjacent points.

**Definition 1.1.** A group \(\Gamma\) has the *fixed-point property for trees with finite edge stabilizers* if every action of \(\Gamma\) on a tree, without inversions and such that the stabilizer of every edge is finite, fixes a point of the tree.

The group of integers does not have this property (Exercise 4.2). A group with a finite generating set whose Cayley graph has one end has it; this is Lemma 6.6 of [Bowditch], and it is proved in [The fixed-point property for groups with one end](the-fixed-point-property-for-groups-with-one-end.md). In this lesson and the next the property is a hypothesis on the group.

## 2. Contracting edges

Let \(S\) be a tree and \(\mathcal E\) a set of edges of \(S\). For \(x,y\in S\) write \(x\sim y\) if every edge of \([x,y]\) lies in \(\mathcal E\); in particular \(x\sim x\).

**Proposition 2.1.**

1. The relation \(\sim\) is a full relation on the pretree \(S\), and \(S/{\sim}\) is a tree.
2. Two adjacent points \(x,y\) are related if and only if \(\{x,y\}\in\mathcal E\).
3. Two different classes \(X,Y\) are adjacent in \(S/{\sim}\) if and only if some edge \(\{x,y\}\) of \(S\) has \(x\in X\) and \(y\in Y\). This edge is then unique, and it does not lie in \(\mathcal E\).
4. Let a group \(\Gamma\) act on \(S\) by automorphisms that map \(\mathcal E\) to itself. Then \(\Gamma\) acts on the tree \(S/{\sim}\), and for adjacent classes \(X,Y\) with the edge \(\{x,y\}\) of (3), \(\Gamma(X)\cap\Gamma(Y)=\Gamma(x)\cap\Gamma(y)\).

**Proof.** (1) The relation is reflexive and symmetric. If \(w\in[x,y]\), the list of \([x,w]\) is the beginning of the list of \([x,y]\), so the edges of \([x,w]\) are edges of \([x,y]\). Hence \(x\sim y\) and \(w\in[x,y]\) imply \(x\sim w\): once \(\sim\) is known to be an equivalence relation, its classes are full. For transitivity let \(x\sim y\), \(y\sim z\), and \(m\) the median of \(x,y,z\). Then \([x,z]=[x,m]\cup[m,z]\), and its list is the list of \([x,m]\) followed by that of \([m,z]\). Since \(m\in[x,y]\) and \(m\in[y,z]\), the edges of \([x,m]\) are edges of \([x,y]\), and those of \([m,z]\) are edges of \([y,z]\). So \(x\sim z\).

The intervals of \(S/{\sim}\) are images of intervals of \(S\) (Proposition 3.1 of the lesson on quotients), so they are finite; and \(S/{\sim}\) is median (Theorem 4.1 there). So it is a tree.

(2) The interval between adjacent points has the one edge \(\{x,y\}\).

(3) By Corollary 3.2(4) of the lesson on quotients, \(X\) and \(Y\) are adjacent exactly when \(X\cup Y\) is full. Let \(X\cup Y\) be full, \(x'\in X\), \(y'\in Y\). The list of \([x',y']\) lies in \(X\cup Y\), begins in \(X\) and ends in \(Y\); so two consecutive points \(x\in X\), \(y\in Y\) occur in it, and they are adjacent. Conversely let \(\{x,y\}\) be an edge with \(x\in X\), \(y\in Y\). For \(x'\in X\), \(y'\in Y\) the interval \([x',y']\) lies in \([x',x]\cup[x,y]\cup[y,y']\subseteq X\cup Y\). So \(X\cup Y\) is full.

The edge is not in \(\mathcal E\), by (2). Suppose \(\{x,y\}\) and \(\{x',y'\}\) are two different such edges, with \(x,x'\in X\) and \(y,y'\in Y\). Follow the list of \([x,x']\), which lies in \(X\), then the list of \([y',y]\), which lies in \(Y\). This is a sequence of at least three distinct points in which each is adjacent to the next and the last to the first. A tree contains no such sequence.

(4) An automorphism of \(S\) that maps \(\mathcal E\) to itself maps the list of an interval to the list of the image interval, so it preserves \(\sim\) and maps classes to classes. The betweenness of classes is defined through the betweenness of points, so the induced map of \(S/{\sim}\) is an automorphism. If \(g\) fixes \(X\) and \(Y\), it maps the edge \(\{x,y\}\) to an edge between \(X\) and \(Y\), which is the same edge by (3); and \(gx\in X\), so \(gx=x\) and \(gy=y\). Conversely, if \(g\) fixes \(x\) and \(y\), it fixes their classes. \(\blacksquare\)

**Proposition 2.2.** Let \(\Gamma\) have the fixed-point property for trees with finite edge stabilizers. Let \(\Gamma\) act on a tree \(S\), and let \(S\) be the disjoint union of two sets \(S_0,S_1\) such that \(gS_0=S_0\) for all \(g\in\Gamma\) and every edge joins a point of \(S_0\) to a point of \(S_1\). Suppose that at every point of \(S_0\) at most one of the edges containing it has an infinite stabilizer. Then \(\Gamma\) fixes a point of \(S\).

**Proof.** Let \(\mathcal E\) be the set of edges with infinite stabilizer. The stabilizer of the edge \(g\{x,y\}\) is the conjugate by \(g\) of that of \(\{x,y\}\), so \(\Gamma\) maps \(\mathcal E\) to itself. Let \(\sim\) be the relation of Proposition 2.1.

*A class contains at most one point of \(S_1\).* Let \(p\ne p'\) be points of \(S_1\) with \(p\sim p'\). The list of \([p,p']\) begins \(p,a,p''\) with \(a\in S_0\) and \(p''\in S_1\), because edges join \(S_0\) to \(S_1\). The edges \(\{p,a\}\) and \(\{a,p''\}\) are two edges of \(\mathcal E\) at the point \(a\in S_0\), against the assumption.

*The action on \(S/{\sim}\) is without inversions.* Suppose \(g\) exchanges adjacent classes \(X,Y\). It maps the unique edge between them to itself. One end \(a\) of this edge lies in \(S_0\), the other in \(S_1\), so \(ga=a\). But \(a\) lies in one of the classes \(X,Y\), and \(ga\) in the other.

*Conclusion.* By Proposition 2.1(4) the stabilizer of an edge of \(S/{\sim}\) is the stabilizer of an edge of \(S\) outside \(\mathcal E\), which is finite. So \(\Gamma\) fixes a class \(X\). If \(X\) contains a point of \(S_1\), this point is the only one, and \(\Gamma\) fixes it, because \(\Gamma\) maps \(S_1\) to itself. Otherwise \(X\) lies in \(S_0\); two points of \(X\) would be joined by a list that passes through \(S_1\), so \(X\) is one point, fixed by \(\Gamma\). \(\blacksquare\)

## 3. Classes of the finite interval relation

We return to the setting of the earlier lessons: \(M\) is a compact connected metric space with more than one point, \(\Gamma\) a convergence group on \(M\), and \(T\) a set of cut points with \(gT=T\) for all \(g\). The group acts on the completion \(\Phi=\Phi(T)\), in which \(\bar T\) is the set of the flows \(\bar a\) towards points \(a\in T\); adjacent points of \(\Phi\) are called neighbours, and of two neighbours exactly one lies in \(\bar T\). As in [Loxodromic elements and the completion](loxodromic-elements-and-the-completion.md), \(\Phi'\) is the set of points outside \(\bar T\) with exactly one neighbour, and \(\Phi_0=\Phi\setminus\Phi'\).

Two points \(p,q\in\Phi\) are related by the *finite interval relation* if \([p,q]_\Phi\) is finite. This is a full relation ([The dense quotient of a pretree](course:pretrees/the-dense-quotient-of-a-pretree), Lemma 4.1). Adjacent points are related. An automorphism of \(\Phi\) maps classes to classes.

**Theorem 3.1.** Let \(\Gamma\) be a convergence group acting minimally on a compact connected metric space \(M\) with more than one point, and \(T\) a nonempty invariant set of cut points. Suppose that:

- \(\Gamma\) has the fixed-point property for trees with finite edge stabilizers;
- for every \(a\in T\), the stabilizer of \(a\) in \(\Gamma\) is finite or contains a loxodromic element.

Then no class of the finite interval relation of \(\Phi(T)\) is mapped to itself by all of \(\Gamma\).

**Proof.** Suppose the class \(X\) is mapped to itself by \(\Gamma\). Let \(S=X\cap\Phi_0\).

*\(S\) is not empty.* A point of \(X\) outside \(S\) lies in \(\Phi'\); its neighbour lies in \(\bar T\subseteq\Phi_0\) and in \(X\).

*\(S\) is full in \(\Phi\).* Let \(u,v\in S\) and \(w\) between them. Then \(w\in X\), and in the list of the finite interval \([u,v]_\Phi\) the point \(w\) has a point before it and a point after it, which are neighbours of \(w\) (Corollary 2.4(3) of [Adjacent points of the completion](course:pretrees/adjacent-points-of-the-completion)). So \(w\notin\Phi'\).

*\(S\) is a tree.* It is a full subset of the median pretree \(\Phi\), so it is a median pretree, and its intervals are intervals of \(\Phi\) inside \(X\), which are finite. Two points of \(S\) are adjacent in \(S\) exactly when they are neighbours in \(\Phi\).

*The action.* An automorphism of \(\Phi\) that comes from an element of \(\Gamma\) maps \(\bar T\) to itself and preserves the number of neighbours of a point; so it maps \(\Phi_0\) to itself. Hence \(\Gamma\) acts on \(S\), and it maps \(S_0=S\cap\bar T\) and \(S_1=S\setminus\bar T\) to themselves. Every edge of \(S\) joins \(S_0\) to \(S_1\).

*At a point of \(S_0\) at most one edge has an infinite stabilizer.* Let \(\bar a\in S_0\) have two neighbours \(p\ne q\) in \(S_1\) such that \(\Gamma(\bar a)\cap\Gamma(p)\) and \(\Gamma(\bar a)\cap\Gamma(q)\) are infinite. The group \(\Gamma(\bar a)\) is the stabilizer of the point \(a\in M\). It is infinite, so by assumption it contains a loxodromic element \(g\), and the cyclic group generated by \(g\) has finite index in it (Corollary 3.5 of [Convergence actions and their elements](convergence-actions-and-their-elements.md)). An infinite subgroup of \(\Gamma(\bar a)\) meets this cyclic group in a subgroup of finite index in itself, hence in an infinite subgroup; so it contains a power \(g^k\) with \(k\ge1\). So there are \(k,l\ge1\) such that \(g^k\) fixes \(p\) and \(g^l\) fixes \(q\). The element \(\gamma=g^{kl}\) is loxodromic (Corollary 2.2 there) and fixes \(\bar a\), \(p\) and \(q\), which are points of \(\Phi_0\). This contradicts Lemma 2.1 of the lesson on loxodromic elements and the completion.

*Conclusion.* By Proposition 2.2, \(\Gamma\) fixes a point of \(S\subseteq\Phi\). This contradicts Theorem 3.1 of the lesson on supports. \(\blacksquare\)

## 4. Exercises

**4.1.** Let \(S\) be the tree with points \(u,a,b,c\) in which \(u\) is adjacent to the three others, and let \(\mathcal E\) consist of the edge \(\{u,a\}\). Determine the classes of \(\sim\) and the tree \(S/{\sim}\).

**4.2.** Show that the group of integers does not have the fixed-point property for trees with finite edge stabilizers.

**4.3.** Let \(S\) be a tree with at least three points, and \(S'\) the set of points of \(S\) that have at least two neighbours. Show that \(S'\) is not empty and full, so that it is a tree.

**4.4.** In the proof of Theorem 3.1, why is the tree \(S\) used instead of the whole class \(X\)?

## 5. Solutions

**4.1.** The classes are \(\{u,a\}\), \(\{b\}\) and \(\{c\}\). The class \(\{u,a\}\) is adjacent to the two others, through the edges \(\{u,b\}\) and \(\{u,c\}\), and \(\{b\}\) and \(\{c\}\) are not adjacent, because no edge joins them. So \(S/{\sim}\) is a path of three points with \(\{u,a\}\) in the middle.

**4.2.** Let \(S\) be the set of integers with the betweenness of the line; it is a discrete median pretree, with edges \(\{n,n+1\}\). The integers act by translations \(n\mapsto n+k\). No translation with \(k\ne0\) fixes a point or exchanges two adjacent points, and the stabilizers of points and of edges are trivial. No point is fixed.

**4.3.** No three points of \(S\) are pairwise adjacent, so among three points of \(S\) two, say \(x\) and \(z\), are not adjacent. The list of \([x,z]\) has an inner point, and an inner point of a list has the point before it and the point after it as neighbours. So \(S'\) is not empty. Let \(u,v\in S'\) and \(w\) between them; then \(w\) is an inner point of the list of \([u,v]\), so \(w\in S'\). A nonempty full subset of a tree is a discrete median pretree: its intervals are intervals of \(S\), and the median of three of its points lies in the interval between two of them.

**4.4.** A point of \(X\) outside \(S\) lies outside \(\bar T\) and has one neighbour. A loxodromic element can fix such a point together with its neighbour in \(\bar T\) and a second neighbour of that point, without contradiction to the theorem on loxodromic elements; so the count of edges with infinite stabilizers at a point of \(\bar T\) is controlled only for neighbours in \(\Phi_0\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
