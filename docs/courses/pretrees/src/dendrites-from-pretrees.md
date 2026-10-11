# Dendrites from pretrees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *dendrite* is a locally connected compact connected metric space that contains no simple closed curve ([Dendrites and cut points](course:continua-arcs-and-cut-points/dendrites-and-cut-points)). This lesson gives a way to recognize dendrites without looking for curves. Suppose a compact space with a countable dense subset carries a betweenness relation that makes it a complete dense median pretree, and suppose the relation is compatible with the topology in one respect: for \(x\ne y\), the set of points that are not "beyond \(y\) as seen from \(x\)" is open. Then the space is a dendrite, and the interval \([x,y]\) of the pretree is the only arc from \(x\) to \(y\) (Theorem 5.1).

The theorem is used to show that certain quotients of continua are dendrites: there the betweenness comes from separation by cut points, and the theorem turns it into topology.

The statement and the steps of the proof are those of Theorem 2.14 and Lemmas 2.15 to 2.19 of [Bowditch], with the hypothesis that the pretree is median made explicit; the sets \(H(x,y)\) of the hypothesis are only defined in a median pretree, and a complete dense pretree need not be median ([Dense, complete and median pretrees](dense-complete-and-median-pretrees.md), Proposition 3.2).

We use the three earlier lessons of this course, the lesson [Every path contains an arc](course:continua-arcs-and-cut-points/every-path-contains-an-arc) for arcs, and from the core course [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90) compactness and the Urysohn metrization theorem: a compact Hausdorff space with a countable base is metrizable.

## 1. Medians and gates

Let \(T\) be a median pretree and \(x\ne y\). Put
\[
\begin{gathered}
H(x,y)=\{w\in T:\\
\operatorname{med}(x,y,w)\ne y\}.
\end{gathered}
\]
It contains \(x\) and not \(y\). The set \(P(x,y)\) of the previous lesson is \(H(x,y)\cap H(y,x)\).

Statements about medians of finitely many points will be checked in finite trees. For this we fix the following convention: a *tree for* a finite set \(F\subseteq T\) is a finite tree that contains, with the same betweenness, the points of \(F\) and the medians of all triples of points of \(F\) (Corollary 4.5 of the first lesson, applied to the larger finite set). In such a tree the median of three points of \(F\) is their branch vertex, and the *gate* of a point \(w\in F\) on a path \([p,q]_\tau\) with \(p,q\in F\) is \(\operatorname{med}(p,q,w)\) (Section 1 of the previous lesson). So
\[
\begin{gathered}
w\in H(x,y)\iff\\
\text{the gate of }w\text{ on }[x,y]_\tau\text{ is not }y .
\end{gathered}
\]

**Lemma 1.1.** Let \(T\) be a median pretree.

1. If \(z\in(x,y)\), then \(H(x,z)\cap H(y,z)=\varnothing\).
2. If \(a\ne b\), \(x\notin[a,b]\), \(c=\operatorname{med}(a,b,x)\) and \(y\in(c,x)\), then \(H(x,y)\cap[a,b]=\varnothing\).
3. Let \(u,v,w\) be points of an interval \([a,b]\). Then \(\operatorname{med}(u,v,w)\) is the one of the three that lies between the other two in the order of \([a,b]\), or the repeated point if two coincide. Consequently, for \(y\in[a,b]\), \(y\ne a\), and the direction with \(a<b\): \([a,b]\cap H(a,y)=\{w\in[a,b]:w<y\}\).
4. Let \(x\ne z\), \(p,q\in(x,z)\) with \(p\in(x,q)\), and \(q'\in(q,z)\). Then \(x\in H(p,q)\), \(z\in H(z,q')\), and \(H(p,q)\cap H(z,q')=\varnothing\).
5. Let \(x\ne z\) and \(t\in(x,z)\). If \(y\in H(x,t)\) and \(w\in H(z,t)\), then \(\operatorname{med}(x,y,w)=\operatorname{med}(x,t,y)\in[x,t)\).

**Proof.** In each case take a tree \(\tau\) for the points named, and use Lemma 1.1 of the previous lesson on gates.

(1) Let \(w\in T\) and \(g\) its gate on \([x,y]_\tau\). If \(g\in[x,z]_\tau\), then \([w,y]_\tau=[w,g]_\tau\cup[g,y]_\tau\) contains \(z\), so \(z\) lies on the three paths of \(y,z,w\): \(\operatorname{med}(y,z,w)=z\) and \(w\notin H(y,z)\). If \(g\in[z,y]_\tau\), then in the same way \(w\notin H(x,z)\).

(2) Let \(w\in[a,b]\). The gate of \(x\) on \([a,b]_\tau\) is \(c\), so \([w,x]_\tau=[w,c]_\tau\cup[c,x]_\tau\), which contains \(y\). So \(y\) lies on the three paths of \(x,y,w\): \(\operatorname{med}(x,y,w)=y\).

(3) The three points lie on the path \([a,b]_\tau\), and the branch vertex of three vertices of a path is the middle one. For the consequence: for \(w\in[a,b]\), the median of \(a,y,w\) is \(y\) exactly when \(y\) is the middle one or \(w=y\), that is, when \(y\le w\).

(4) \(\operatorname{med}(p,q,x)=p\) and \(\operatorname{med}(z,q',z)=z\) by (3), applied in \([x,z]\). Let \(w\in H(z,q')\). The gate of \(w\) on \([q',z]_\tau\) is not \(q'\), so the gate \(g\) of \(w\) on \([x,z]_\tau\) lies in \([q',z]_\tau\) and is not \(q'\) (Lemma 1.1(2) of the previous lesson). Then \(g\notin[x,q]_\tau\), and applying that lemma to the paths \([x,z]_\tau\supseteq[x,q]_\tau\supseteq[p,q]_\tau\) shows that the gate of \(w\) on \([p,q]_\tau\) is \(q\). So \(w\notin H(p,q)\).

(5) Let \(g_y=\operatorname{med}(x,t,y)\) and \(g_w=\operatorname{med}(z,t,w)\); they are the gates of \(y\) on \([x,t]_\tau\) and of \(w\) on \([t,z]_\tau\), and \(g_y\ne t\), \(g_w\ne t\). As in (4) they are also the gates of \(y\) and \(w\) on \([x,z]_\tau\), and \(g_y\in[x,t)\), \(g_w\in(t,z]\). By Lemma 1.1 of the previous lesson, \([x,y]_\tau\) contains \(g_y\); \([x,w]_\tau=[x,g_w]_\tau\cup[g_w,w]_\tau\) contains \(g_y\); and \([y,w]_\tau=[y,g_y]_\tau\cup[g_y,g_w]_\tau\cup[g_w,w]_\tau\) contains \(g_y\). So \(g_y\) is the median of \(x,y,w\). \(\blacksquare\)

## 2. The standing assumptions

For the rest of the lesson \(T\) is a topological space and a pretree such that:

1. \(T\) is compact and has a countable dense subset;
2. the pretree \(T\) is complete, dense and median;
3. for all \(x\ne y\) the set \(H(x,y)\) is open.

**Lemma 2.1.** Under these assumptions:

1. \(T\) is a Hausdorff space.
2. The pretree \(T\) is separable. So every interval \([a,b]\) with \(a\ne b\) is ordered like \([0,1]\) (Theorem 4.1 of the previous lesson).
3. Every interval \([a,b]\) is closed in \(T\), hence compact.

**Proof.** (1) Let \(x\ne y\) and \(z\in(x,y)\). Then \(H(x,z)\) and \(H(y,z)\) are open, contain \(x\) and \(y\), and are disjoint by Lemma 1.1(1). (2) Let \(R\) be a countable dense subset of the space. For \(x\ne y\) the set \(P(x,y)=H(x,y)\cap H(y,x)\) is open, and it is not empty because it contains \((x,y)\). So it meets \(R\): \(R\) is weakly dense. (3) Let \(a\ne b\) and \(x\notin[a,b]\). With \(c\) and \(y\) as in Lemma 1.1(2), \(H(x,y)\) is an open set containing \(x\) and disjoint from \([a,b]\). For \(a=b\), points are closed in a Hausdorff space. \(\blacksquare\)

## 3. Intervals are arcs

**Proposition 3.1.** Let \(a\ne b\). The order isomorphism \(\Phi:[a,b]\to[0,1]\) of Theorem 4.1 of the previous lesson is a homeomorphism, for the topology of \([a,b]\) as a subspace of \(T\). So \([a,b]\) is an arc from \(a\) to \(b\).

**Proof.** By Lemma 1.1(3), for \(y\in[a,b]\), \(y\ne a\), the set \(\{w\in[a,b]:w<y\}\) is \([a,b]\cap H(a,y)\), which is open in \([a,b]\); in the same way \(\{w:w>x\}=[a,b]\cap H(b,x)\) is open for \(x\ne b\). The sets \([0,s)\) and \((s,1]\) form a subbase of the topology of \([0,1]\), and their preimages under \(\Phi\) are sets of these two kinds. So \(\Phi\) is continuous. It is a bijection from the compact space \([a,b]\) (Lemma 2.1) onto a Hausdorff space, hence a homeomorphism. \(\blacksquare\)

In particular \(T\) is connected, and any two of its points are joined by an arc.

## 4. Small intervals

**Lemma 4.1.** Let \(x\ne z\) and let \(V\) be a neighbourhood of \(x\). There are open sets \(U\ni x\) and \(O\ni z\) such that \(\operatorname{med}(x,y,w)\in V\) for all \(y\in U\) and \(w\in O\).

**Proof.** By Proposition 3.1 the arc \([x,z]\) has a point \(t\in(x,z)\) with \([x,t]\subseteq V\). Let \(U=H(x,t)\) and \(O=H(z,t)\); they are open and contain \(x\) and \(z\). By Lemma 1.1(5), for \(y\in U\) and \(w\in O\) the median of \(x,y,w\) lies in \([x,t)\subseteq V\). \(\blacksquare\)

**Proposition 4.2.** Let \(x\in T\) and let \(V\) be a neighbourhood of \(x\). There is a neighbourhood \(U\) of \(x\) such that \([x,y]\subseteq V\) for all \(y\in U\).

**Proof.** We may take \(V\) open. If \(V=T\), take \(U=T\). Otherwise, for every \(z\in T\setminus V\) choose \(U_z\) and \(O_z\) as in Lemma 4.1. The compact set \(T\setminus V\) is covered by finitely many sets \(O_{z_1},\dots,O_{z_n}\); let \(U=U_{z_1}\cap\dots\cap U_{z_n}\). Let \(y\in U\) and suppose some \(z\in[x,y]\) is not in \(V\). Then \(z\in O_{z_i}\) for some \(i\), and \(y\in U_{z_i}\), so \(\operatorname{med}(x,y,z)\in V\). But \(z\in[x,y]\), so \(\operatorname{med}(x,y,z)=z\notin V\). \(\blacksquare\)

**Corollary 4.3.** \(T\) is locally connected.

**Proof.** Let \(V\) be open, \(C\) a component of \(V\), and \(x\in C\). Take \(U\) as in Proposition 4.2. The union \(N\) of the arcs \([x,y]\), \(y\in U\), is connected, contains \(U\) and lies in \(V\). So \(N\subseteq C\), and \(C\) contains the neighbourhood \(U\) of \(x\). Hence every component of an open set is open; for an open \(V\ni x\) the component of \(V\) containing \(x\) is then a connected open set between \(x\) and \(V\). \(\blacksquare\)

**Proposition 4.4.** \(T\) has a countable base, and so \(T\) is metrizable.

**Proof.** Let \(R'\) be a countable strongly dense subset of the pretree (Lemma 2.1 and Proposition 2.2 of the previous lesson). We show that the countably many open sets \(H(p,q)\), \(p\ne q\) in \(R'\), form a subbase of the topology; their finite intersections then form a countable base.

Let \(x\in V\) with \(V\) open, \(V\ne T\). For \(z\in T\setminus V\) choose \(p\in R'\cap(x,z)\), then \(q\in R'\cap(p,z)\), then \(q'\in(q,z)\). By Lemma 1.1(4), \(x\in H(p,q)\), and the open set \(O_z=H(z,q')\) contains \(z\) and is disjoint from \(H(p,q)\). Finitely many \(O_{z_1},\dots,O_{z_n}\) cover \(T\setminus V\). The intersection of the corresponding sets \(H(p_i,q_i)\) contains \(x\) and is disjoint from \(T\setminus V\). \(\blacksquare\)

## 5. The theorem

**Theorem 5.1.** Let \(T\) be a compact topological space with a countable dense subset, carrying the structure of a complete dense median pretree such that \(H(x,y)\) is open for all \(x\ne y\). Then:

1. \(T\) is metrizable, connected and locally connected: a Peano continuum.
2. For \(x\ne y\) the interval \([x,y]\) of the pretree is an arc from \(x\) to \(y\), and it is the only arc in \(T\) from \(x\) to \(y\).
3. \(T\) contains no simple closed curve. So \(T\) is a dendrite.

**Proof.** (1) is Propositions 4.4 and 3.1 and Corollary 4.3. The first half of (2) is Proposition 3.1.

*Uniqueness of arcs.* Let \(A\) be an arc from \(x\) to \(y\) and \(h:[0,1]\to A\) a homeomorphism with \(h(0)=x\), \(h(1)=y\). We show \([x,y]\subseteq A\). Then \([x,y]\) is a connected subset of the arc \(A\) containing both its endpoints, so \([x,y]=A\) (Lemma 1.1 of the lesson on arcs).

Suppose \(z\in[x,y]\) and \(z\notin A\). For \(s\in[0,1]\), Proposition 4.2 with the neighbourhood \(T\setminus\{z\}\) of \(h(s)\) gives a neighbourhood \(U_s\) of \(h(s)\) such that \(z\notin[h(s),p]\) for \(p\in U_s\). The sets \(h^{-1}(U_s)\) cover \([0,1]\) by neighbourhoods of the points \(s\); let \(\lambda\) be a Lebesgue number of the cover by their interiors, and choose \(0=t_0<t_1<\dots<t_n=1\) with \(t_i-t_{i-1}<\lambda\). For each \(i\) there is \(s\) with \(h(t_{i-1}),h(t_i)\in U_s\), so \(z\) lies in neither \([h(s),h(t_{i-1})]\) nor \([h(s),h(t_i)]\); by Lemma 3.1 of the first lesson, \(z\notin[h(t_{i-1}),h(t_i)]\). By the same lemma,
\[
[x,y]\subseteq\bigcup_{i=1}^n[h(t_{i-1}),h(t_i)],
\]
so \(z\notin[x,y]\), a contradiction.

(3) A simple closed curve contains two points and two different arcs between them, the two parts into which the points divide it. This contradicts (2). \(\blacksquare\)

**Corollary 5.2.** Under the assumptions of Theorem 5.1, for distinct points \(x,y,z\) the relation \(xzy\) holds if and only if \(z\) lies on the arc from \(x\) to \(y\). So the pretree structure is determined by the topology.

**Proof.** \(xzy\) means \(z\in[x,y]\), \(z\ne x,y\), and \([x,y]\) is the arc from \(x\) to \(y\) by Theorem 5.1(2). \(\blacksquare\)

## 6. Exercises

**6.1.** Let \(T=[0,1]\) with its usual topology and betweenness. Determine \(H(x,y)\) and check the assumptions of Theorem 5.1.

**6.2.** Let \(T\) be the tripod \(R\) of the second lesson, with the topology in which a set is open if its intersection with each closed leg is open in the leg, a leg with the centre being a copy of \([0,1]\). Describe \(H(x,y)\) for two points \(x,y\) on one leg and for two points on different legs, and conclude that \(R\) is a dendrite.

**6.3.** Show that assumption 3 of Section 2 cannot be dropped: give a compact metric space with a countable dense subset and a complete dense median pretree structure on its set of points that is not the betweenness of its arcs.

**6.4.** In the proof of Theorem 5.1, where is each of the lemmas of Section 1 used?

**6.5.** Let \(T\) be as in Theorem 5.1 and \(x\ne y\). Show that \(H(x,y)\) is connected.

## 7. Solutions

**6.1.** For \(x<y\): \(H(x,y)=[0,y)\); for \(x>y\): \(H(x,y)=(y,1]\) (Lemma 1.1(3)). These sets are open. \([0,1]\) is compact, the rationals are dense, and \([0,1]\) is a complete dense median pretree (Example 2.1 of the second lesson).

**6.2.** Let \(x,y\) lie on one leg, with heights \(s\) and \(t\). If \(s<t\), then \(H(x,y)\) consists of the points of that leg of height less than \(t\) together with the two other legs; if \(s>t\), of the points of that leg of height greater than \(t\). If \(x,y\) lie on different legs, \(H(x,y)\) is the complement of the set of points of the leg of \(y\) of height at least that of \(y\). All these sets are open. \(R\) is compact, the points of rational height are dense, and \(R\) is a complete dense median pretree (Exercise 5.1 of the second lesson). Theorem 5.1 applies.

**6.3.** Let \(\beta:[0,1]\to[0,1]\) be a bijection that is not monotone, for example the map that exchanges \(0\) and \(\frac12\) and fixes all other points. Define a betweenness on \([0,1]\) by: \(z\) lies between \(x\) and \(y\) if \(\beta(z)\) lies between \(\beta(x)\) and \(\beta(y)\) on the line. This is a pretree isomorphic, through \(\beta\), to the pretree \([0,1]\), so it is complete, dense and median. But the point \(\frac14\) lies between \(\frac12\) and \(\frac13\) in this relation, because \(\beta(\frac12)=0<\frac14<\frac13\), and \(\frac14\) does not lie on the arc from \(\frac12\) to \(\frac13\). By Corollary 5.2, assumption 3 fails.

**6.4.** (1) for the Hausdorff property; (2) for the closedness of intervals; (3) for the continuity of \(\Phi\); (4) for the countable base; (5) for Lemma 4.1.

**6.5.** \(H(x,y)\) contains \(x\). Let \(w\in H(x,y)\). Every point \(p\in[x,w]\) lies in \(H(x,y)\): in a tree for \(x,y,w,p\), the gate of \(p\) on \([x,y]_\tau\) lies in \([x,g]_\tau\), where \(g\ne y\) is the gate of \(w\); for \([x,w]_\tau=[x,g]_\tau\cup[g,w]_\tau\), and a point of \([x,g]_\tau\) is its own gate while a point of \([g,w]_\tau\) has the gate \(g\). So \(H(x,y)\) is a union of arcs \([x,w]\) through \(x\), hence connected.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 2. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
