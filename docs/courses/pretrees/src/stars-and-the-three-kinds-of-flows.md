# Stars and the three kinds of flows

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two kinds of flows on a pretree \(T\) appear in the earlier lessons: the flow \(\bar a\) towards a point \(a\) ([Flows on a pretree](flows-on-a-pretree.md)), and the flow of an endless directed arc, which runs towards the place where the arc would end ([Directed arcs and suprema](directed-arcs-and-suprema.md)). A third kind appears there in one example: on a set of three points with no betweenness relation the empty relation is a flow, and it is the flow towards the missing centre around which the three points branch.

This lesson treats the third kind in general. A *star* is a set of at least two pairwise adjacent points that cannot be enlarged without creating a betweenness relation among its points. Every star \(F\) has a flow: from each point it runs to the nearest point of \(F\) and stops there (Theorem 3.1). The main result (Theorem 5.1) says that every flow on a nonempty pretree is of exactly one of three kinds:

- the flow towards a point;
- the flow of a star;
- the flow of an endless directed arc.

Which case holds is read off from the arcs along which the flow runs; this is the *type* of the flow, defined in Section 4.

The lesson follows Lemmas 3.20 to 3.24 and Proposition 3.25 of [Bowditch]; the proofs are written out in full. It uses [Betweenness and pretrees](betweenness-and-pretrees.md) for the axioms, intervals and arcs, the lesson on flows for the pretree \(T\sqcup\{p\}\), and the lesson on directed arcs for the flow of a directed arc and its restriction to a full subset.

## 1. Null sets

Let \(T\) be a pretree. A subset \(F\subseteq T\) is *null* if no relation \(xyz\) holds with \(x,y,z\in F\). Every set with at most two points is null.

For a subset \(F\subseteq T\) and a point \(y\in F\) let
\[
\begin{gathered}
N(y)=\{y\}\cup\{x\in T\mid xyz\\
\text{for some } z\in F\}.
\end{gathered}
\]
So \(N(y)\) consists of \(y\) and of the points \(x\) such that \(y\) lies between \(x\) and some point of \(F\). The set depends on \(F\); where this matters we write \(N_F(y)\).

**Lemma 1.1.** Let \(F\subseteq T\), \(y\in F\), \(x\in N(y)\setminus\{y\}\) and \(z\in T\setminus N(y)\). Then \(xyz\).

**Proof.** There is \(w\in F\) with \(xyw\). Since \(z\notin N(y)\), we have \(z\ne y\), and \(zyw\) fails. By (T3), applied to \(xyw\) and the point \(z\): \(xyz\) or \(wyz\). So \(xyz\). \(\blacksquare\)

**Lemma 1.2.** Let \(F\subseteq T\) and \(y\in F\). Then \(N(y)\) is full.

**Proof.** Let \(a,b\in N(y)\) and \(x\in(a,b)\), and suppose \(x\notin N(y)\).

*If \(y\) is neither \(a\) nor \(b\)*: Lemma 1.1 gives \(ayx\) and \(byx\). From \(bxa\) and \(xya\), Lemma 2.3(2) of the first lesson gives \(bxya\), in particular \(bxy\). This contradicts \(byx\), by (T2).

*If \(y=a\)*: then \(b\ne y\), and Lemma 1.1 gives \(byx\). But \(axb\) reads \(bxy\), against (T2). The case \(y=b\) is the same with \(a\) and \(b\) exchanged. \(\blacksquare\)

**Lemma 1.3.** Let \(F\subseteq T\) be null and \(y\in F\).

1. \(N(y)\cap F=\{y\}\).
2. If \(x\in N(y)\), then \([x,y]\subseteq N(y)\) and \([x,y]\cap F=\{y\}\).
3. If \(y'\in F\) and \(y'\ne y\), then \(N(y)\cap N(y')=\varnothing\).
4. \(F\) is full if and only if any two distinct points of \(F\) are adjacent.

**Proof.** (1) A point \(x\in F\cap N(y)\) other than \(y\) would have \(xyz\) with \(z\in F\), a relation among three points of \(F\).

(2) The first statement holds because \(N(y)\) is full and contains \(x\) and \(y\). Then \([x,y]\cap F\subseteq N(y)\cap F=\{y\}\) by (1).

(3) Let \(u\in N(y)\cap N(y')\). By (1), \(y'\notin N(y)\) and \(y\notin N(y')\); so \(u\ne y\) and \(u\ne y'\). Lemma 1.1 for \(N(y)\) gives \(u\,y\,y'\), and for \(N(y')\) it gives \(u\,y'\,y\). This contradicts (T2).

(4) Let \(F\) be full and \(x\ne y\) in \(F\). A point \(z\in(x,y)\) would lie in \(F\), and \(xzy\) would be a relation among points of \(F\). So \((x,y)=\varnothing\). Conversely, if any two distinct points of \(F\) are adjacent, then \([x,y]=\{x,y\}\subseteq F\) for \(x,y\in F\). \(\blacksquare\)

## 2. Stars

A null set is *maximal null* if it is not properly contained in a null subset of \(T\).

**Definition 2.1.** A *star* is a subset \(F\subseteq T\) with at least two points that is full and maximal null.

By Lemma 1.3(4) the points of a star are pairwise adjacent. If \(T\) has at least two points, every maximal null set has at least two points, because every set of two points is null.

**Example 2.2.** (a) Let \(T\) be a set with at least two points and the empty relation. Every subset is null and full, so the only star is \(T\).

(b) The real line has no star: a null set has at most two points, and a set of two points is not full.

(c) Let \(T\) be the vertex set of a tree. The stars are the pairs of vertices joined by an edge. Indeed, two vertices are adjacent in the pretree exactly when they are joined by an edge, since the path between them then has no inner vertex. A tree has no three vertices pairwise joined by edges, so a star has two points, joined by an edge. Conversely let \(x,y\) be joined by an edge; the set \(\{x,y\}\) is null and full. Let \(z\) be a third vertex. If the path from \(z\) to \(y\) passes through \(x\), then \(zxy\). If not, this path followed by the edge from \(y\) to \(x\) is the path from \(z\) to \(x\), and \(zyx\). In both cases \(\{x,y,z\}\) is not null. So \(\{x,y\}\) is maximal null.

**Lemma 2.3.** Let \(F\) be a star.

1. \(T\) is the disjoint union of the sets \(N(y)\), \(y\in F\).
2. For \(y\in F\) and \(x\in T\): \(x\in N(y)\) if and only if \([x,y]\cap F=\{y\}\).

**Proof.** (1) The sets are pairwise disjoint by Lemma 1.3(3). A point \(x\in F\) lies in \(N(x)\). Let \(x\notin F\). The set \(F\cup\{x\}\) is not null, so a relation holds among three of its points, and \(x\) is one of them. If \(x\) were the middle point, \(yxz\) with \(y,z\in F\), then \(x\in[y,z]\subseteq F\) because \(F\) is full. So the relation is \(xyz\) with \(y,z\in F\), and \(x\in N(y)\).

(2) One direction is Lemma 1.3(2). Let \(x\notin N(y)\). By (1), \(x\in N(z)\) for some \(z\in F\), \(z\ne y\). Then \(z\in[x,y]\): this is clear if \(x=z\), and otherwise Lemma 1.1, with \(y\notin N(z)\), gives \(xzy\). So \([x,y]\cap F\) contains \(z\ne y\). \(\blacksquare\)

By Lemma 2.3(1) there is a map
\[
h=h_F\colon T\to F,\qquad x\in N(h(x)).
\]
We call \(h(x)\) the *foot* of \(x\) in \(F\). It has the following properties.

- (H1) \(h(x)=x\) if and only if \(x\in F\).
- (H2) \([x,h(x)]\subseteq N(h(x))\). So every point of \([x,h(x)]\) has the foot \(h(x)\), and \([x,h(x)]\cap F=\{h(x)\}\).
- (H3) If \(x\notin F\) and \(h(z)\ne h(x)\), then \(x\,h(x)\,z\).

(H1) holds because \(x\in N(x)\) for \(x\in F\). (H2) is Lemma 1.3(2). (H3) is Lemma 1.1: \(x\in N(h(x))\setminus\{h(x)\}\), and \(z\) lies in \(N(h(z))\), which is disjoint from \(N(h(x))\).

**Lemma 2.4.** Let \(F\) be a star with foot map \(h\), and \(x,y\in T\). Then
\[
[x,y]\subseteq[x,h(x)]\cup[y,h(y)],
\]
and equality holds if \(h(x)\ne h(y)\).

**Proof.** By Lemma 3.1 of the first lesson,
\[
\begin{gathered}
{[x,y]}\subseteq[x,h(x)]\cup[h(x),h(y)]\\
\cup\,[h(y),y],
\end{gathered}
\]
and \([h(x),h(y)]=\{h(x),h(y)\}\) because two distinct points of \(F\) are adjacent.

Let \(h(x)\ne h(y)\). Then \(h(x)\in[x,y]\): this is clear if \(x=h(x)\), and otherwise it is (H3) with \(z=y\). In the same way \(h(y)\in[x,y]\). Since \([x,y]\) is full (Corollary 5.3 of the first lesson), it contains \([x,h(x)]\) and \([y,h(y)]\). \(\blacksquare\)

## 3. The flow of a star

Let \(F\) be a star with foot map \(h\). Define a binary relation \(\operatorname{flow}(F)\) on \(T\), written \(xy.F\), by
\[
xy.F\quad\Longleftrightarrow\quad y\in(x,h(x)] .
\]
From \(x\notin F\) the relation runs along the interval from \(x\) to its foot and ends there.

**Theorem 3.1.** Let \(F\) be a star. Then \(\operatorname{flow}(F)\) is a flow on \(T\). The points \(x\) such that \(xy.F\) holds for no \(y\) are exactly the points of \(F\).

**Proof.** (F1): let \(xy.F\) and \(yx.F\). Then \(y\in[x,h(x)]\), so \(h(y)=h(x)\) by (H2). Write \(u\) for this point. Then \(y\in(x,u]\) and \(x\in(y,u]\), that is, \(xy.\bar u\) and \(yx.\bar u\). This contradicts (F1) for the flow \(\bar u\) (Lemma 2.1 of the lesson on flows).

(F2): let \(xzy\). By Lemma 2.4, \(z\) lies in \([x,h(x)]\) or in \([y,h(y)]\). Since \(z\ne x\) and \(z\ne y\), this gives \(xz.F\) or \(yz.F\).

(F3): let \(xy.F\) and \(z\ne y\). Put \(u=h(x)\); then \(y\in(x,u]\), so \(x\ne u\) and \(x\notin F\).

*If \(h(z)\ne u\)*: by (H3), \(xuz\). If \(y=u\), this is \(xyz\). Otherwise \(y\in(x,u)\) and \(u\in(x,z)\), so \(y\in(x,z)\) by Lemma 3.2 of the first lesson; again \(xyz\).

*If \(h(z)=u\)*: by Lemma 3.1 of the first lesson, \([x,u]\subseteq[x,z]\cup[z,u]\). If \(y\in[x,z]\), then \(xyz\), because \(y\ne x\) and \(y\ne z\). If \(y\in[z,u]\), then \(y\in(z,h(z)]\), which is \(zy.F\).

The last statement: \((x,h(x)]\) is empty exactly when \(x=h(x)\), that is, when \(x\in F\). \(\blacksquare\)

In the pretree of three points with the empty relation, the star is the whole set, every point is its own foot, and \(\operatorname{flow}(F)\) is the empty relation.

## 4. The arcs of a flow

Let \(p\) be a flow on \(T\). We use the pretree \(T\sqcup\{p\}\) of Proposition 3.1 of the lesson on flows: for \(x,y\in T\), the relation \(xyp\) means \(xy.p\), and the new point lies between no two points. So for \(x,y\in T\) the interval \([x,y]\) is the same in \(T\) and in \(T\sqcup\{p\}\), and
\[
[x,p)=\{x\}\cup\{y\in T\mid xy.p\}
\]
is the set of points through which \(p\) flows from \(x\), together with \(x\).

The interval \([x,p]\) is an arc of \(T\sqcup\{p\}\), with the direction in which \(x\) is the least point (Corollary 5.3 of the first lesson). The set \([x,p)\) is an arc of \(T\): it is linear, and for \(u,v\in[x,p)\) the interval \([u,v]\) lies in \([x,p]\) and does not contain the new point. We direct \([x,p)\) by the same direction. By the remark on intervals as directed arcs in Section 4 of the lesson on directed arcs, applied in \(T\sqcup\{p\}\): for \(z\in[x,p)\) the set \([z,p)\) is the final segment of \([x,p)\) that consists of the points \(w\ge z\), and its own direction is the restricted one.

**Lemma 4.1.** Let \(x,y\in T\).

1. If \(z\in[x,p)\cap[y,p)\), then \([z,p)\) is a final segment of \([x,p)\) and of \([y,p)\), and both orders agree on it. If one of \([x,p)\), \([y,p)\) has a maximum, so does the other, and the maxima are equal.
2. \([x,y]\subseteq[x,p)\cup[y,p)\).
3. If \([x,p)\cap[y,p)=\varnothing\), then \([x,y]=[x,p)\cup[y,p)\).

**Proof.** (1) The first statement was just recalled. A maximum of \([x,p)\) lies in the final segment \([z,p)\) and is its maximum; and the maximum of a final segment of an arc is the maximum of the arc. So \([x,p)\), \([z,p)\) and \([y,p)\) have maxima together, and the same ones.

(2) By Lemma 3.1 of the first lesson in \(T\sqcup\{p\}\), \([x,y]\subseteq[x,p]\cup[p,y]\); and the new point is not in \([x,y]\).

(3) Let \(z\in[x,p)\), \(z\ne x\); then \(xzp\). The point \(y\) lies in \([y,p)\), so \(y\ne z\). By (T3), \(xzy\) or \(pzy\); the second says \(z\in[y,p)\), which is excluded. So \(z\in[x,y]\). In the same way \([y,p)\subseteq[x,y]\). With (2) this gives the equality. \(\blacksquare\)

Write \(x\sim y\) if \([x,p)\cap[y,p)\ne\varnothing\).

**Lemma 4.2.** The relation \(\sim\) is an equivalence relation on \(T\). Let \(C\) be a class.

1. \([x,p)\subseteq C\) for every \(x\in C\), and \(C\) is full.
2. Either \([x,p)\) is endless for every \(x\in C\), or \([x,p)\) has a maximum for every \(x\in C\). In the second case the maximum is the same point for all \(x\in C\), and it lies in \(C\).

**Proof.** The relation is reflexive and symmetric. Let \(u\in[x,p)\cap[y,p)\) and \(v\in[y,p)\cap[z,p)\). Both lie in the totally ordered set \([y,p)\). If \(u\le v\) there, then \(v\in[u,p)\subseteq[x,p)\), and \(v\) lies in \([x,p)\cap[z,p)\). If \(v\le u\), then \(u\in[v,p)\subseteq[z,p)\), and \(u\) lies in \([x,p)\cap[z,p)\). So \(x\sim z\).

(1) A point \(y\in[x,p)\) lies in \([x,p)\cap[y,p)\), so \(y\sim x\). For \(x,y\in C\), Lemma 4.1(2) gives \([x,y]\subseteq[x,p)\cup[y,p)\subseteq C\).

(2) This is Lemma 4.1(1); the maximum of \([x,p)\) lies in \([x,p)\subseteq C\). \(\blacksquare\)

A class of the first kind is called *endless*. A class of the second kind is called *ending*, and the common maximum is its *end*. The *type* of the flow \(p\) is the pair \((m,n)\), where \(m\) is the number of endless classes and \(n\) the number of ending classes; these are cardinal numbers and may be infinite.

**Lemma 4.3.** Let \(F_p\) be the set of all \(x\in T\) such that \(xy.p\) holds for no \(y\).

1. \(F_p\) is the set of ends of the ending classes, and every ending class contains exactly one point of \(F_p\).
2. If \(x\) lies in an ending class with end \(u\), then \([x,p)=[x,u]\) and \([x,u]\cap F_p=\{u\}\).
3. Any two distinct points of \(F_p\) are adjacent.

**Proof.** A point \(x\) lies in \(F_p\) exactly when \([x,p)=\{x\}\).

(1) Let \(u\) be the end of the class of \(x\). Then \(u\) is the maximum of \([x,p)\), and \([u,p)\), the set of points \(w\ge u\) of \([x,p)\), is \(\{u\}\). So \(u\in F_p\). Conversely, for \(x\in F_p\) the arc \([x,p)=\{x\}\) has the maximum \(x\), so \(x\) is the end of its class. A class has one end.

(2) If \(u=x\), both sides are \(\{x\}\). Otherwise \(x\,u\,p\). Since \([u,p)=\{u\}\), Lemma 3.2 of the first lesson gives
\[
[x,p)=[x,u]\cup[u,p)=[x,u] .
\]
A point \(w\in[x,u]\) other than \(u\) has \(u\in[w,p)\) and \(u\ne w\), so \(wu.p\) and \(w\notin F_p\).

(3) For \(u\ne v\) in \(F_p\), the sets \([u,p)=\{u\}\) and \([v,p)=\{v\}\) are disjoint, so \([u,v]=\{u,v\}\) by Lemma 4.1(3). \(\blacksquare\)

## 5. The classification

**Theorem 5.1.** Let \(p\) be a flow of type \((m,n)\) on a nonempty pretree \(T\), and \(F_p\) the set of points \(x\) such that \(xy.p\) holds for no \(y\). Exactly one of the following three cases occurs.

1. \(m=0\) and \(n=1\). Then \(F_p\) has one point \(a\), and \(p=\bar a\).
2. \(m=0\) and \(n\ge2\). Then \(F_p\) is a star, and \(p=\operatorname{flow}(F_p)\).
3. \(m\ge1\). Then for every \(x\) in an endless class, \([x,p)\) is an endless directed arc and \(p=\operatorname{flow}([x,p))\).

Conversely, the flow towards a point has type \((0,1)\); the flow of a star \(F\) has type \((0,n)\), where \(n\ge2\) is the number of points of \(F\), and \(F\) is determined by its flow; and the flow of an endless directed arc has a type \((m,n)\) with \(m\ge1\).

**Proof.** Since \(T\) is not empty there is at least one class, so exactly one of the three conditions on \((m,n)\) holds.

*Case 1.* There is one class, with end \(a\), and \(F_p=\{a\}\) by Lemma 4.3(1). For \(x\ne a\), Lemma 4.3(2) gives \([x,p)=[x,a]\), so \(a\in(x,p)\), that is, \(xa.p\). By Lemma 2.2 of the lesson on flows, \(p=\bar a\).

*Case 2.* Every class is ending. For \(x\in T\) let \(h(x)\) be the end of the class of \(x\). By Lemma 4.3, \(F_p\) has \(n\ge2\) points, \(h(x)\in F_p\), and
\[
\begin{gathered}
{[x,p)}=[x,h(x)],\\
[x,h(x)]\cap F_p=\{h(x)\}.
\end{gathered}
\]
The set \(F_p\) is null and full, by Lemma 4.3(3) and Lemma 1.3(4). It is maximal null: let \(x\notin F_p\), and choose \(y\in F_p\) with \(y\ne h(x)\). Then \(x\) and \(y\) lie in different classes, so \([x,p)\cap[y,p)=\varnothing\), and by Lemma 4.1(3)
\[
[x,y]=[x,h(x)]\cup\{y\}.
\]
So \(h(x)\in[x,y]\), and it differs from \(x\) and from \(y\): the relation \(x\,h(x)\,y\) holds, with \(h(x),y\in F_p\). Hence \(F_p\cup\{x\}\) is not null.

So \(F_p\) is a star. By Lemma 2.3(2) and the displayed equality, \(x\in N(h(x))\); that is, \(h\) is the foot map of \(F_p\). Finally, for \(x,y\in T\),
\[
\begin{gathered}
xy.p\iff y\in(x,p)=(x,h(x)]\\
\iff xy.F_p .
\end{gathered}
\]

*Case 3.* Let \(x\) lie in an endless class, so that \([x,p)\) is endless. In the pretree \(T\sqcup\{p\}\) the subset \(T\) is full, and \([x,p]\), directed with \(x\) as least point, is a directed arc with maximum \(p\). Its flow is the flow towards the point \(p\), whose restriction to \(T\) is the relation \(p\) (Proposition 3.1 of the lesson on flows). Its intersection with \(T\) is \([x,p)\), which is endless. So Lemma 3.1 of the lesson on directed arcs, applied to the pretree \(T\sqcup\{p\}\) and its full subset \(T\), says that the relation \(p\) is the flow of the directed arc \([x,p)\) of \(T\).

*The converse statements.* If \(p=\bar a\), then \([x,p)=\{x\}\cup(x,a]=[x,a]\) for every \(x\). All these sets contain \(a\), so there is one class, and \(a\) is the maximum of each \([x,a]\): the type is \((0,1)\).

If \(p=\operatorname{flow}(F)\) for a star \(F\) with foot map \(h\), then \([x,p)=\{x\}\cup(x,h(x)]=[x,h(x)]\), with maximum \(h(x)\). By (H2) this set lies in \(N(h(x))\). So \([x,p)\) and \([y,p)\) are disjoint if \(h(x)\ne h(y)\), and both contain the common foot if \(h(x)=h(y)\). The classes are the sets \(N(y)\), \(y\in F\), all of them ending; the type is \((0,n)\) with \(n\) the number of points of \(F\). By Theorem 3.1, \(F=F_p\).

If \(p=\operatorname{flow}(A)\) for an endless directed arc \((A,<)\) and \(x\in A\), then \([x,p)\) is the set of \(y\in A\) with \(y\ge x\), by Proposition 2.4(4) of the lesson on directed arcs. This is a final segment of an endless arc, so it is endless, and the class of \(x\) is endless. \(\blacksquare\)

So the type separates the three kinds, and in particular a flow of a star is neither a flow towards a point nor the flow of an endless directed arc. In Case 3 the arc is not determined by the flow, not even up to a common final segment: by Lemma 2.6 of the lesson on directed arcs, two directed arcs with a common point and the same flow are cofinal, but the arcs \([x,p)\) for \(x\) in different endless classes are disjoint (Example 6.2).

## 6. Examples

**Example 6.1** (the real line). The real line has no star (Example 2.2), so by Theorem 5.1 a flow on it is the flow towards a point or the flow of an endless directed arc. The arcs are the nonempty convex sets, and a direction on an arc with more than one point is the usual order or its reverse.

Let \(A\) be an endless arc directed by the usual order, and \(s\) its supremum, a real number or \(\infty\). For \(t\in A\), the set of all \(w\) with \(t\le w<s\) is a final segment of \(A\) and of the arc \(\{w\mid w<s\}\). So these two arcs have the same flow (Lemma 2.3 of the lesson on directed arcs); call it \(s^-\). For real \(s\),
\[
\begin{gathered}
xy.s^-\iff x<y<s\\
\text{or } s\le y<x .
\end{gathered}
\]
Indeed, write \(A=\{w\mid w<s\}\). For \(x,y<s\) this is Proposition 2.4(1) of that lesson. For \(x,y\ge s\) it is Proposition 2.4(2): \(y\) must lie between \(x\) and the points below \(s\). For \(x<s\le y\) the relation fails by Proposition 2.4(4). For \(y<s\le x\) it fails by Lemma 2.1 there, because \(y\) lies between \(x\) and no \(w\) with \(y<w<s\). For \(s=\infty\) the arc is the whole line and \(xy.s^-\) means \(x<y\).

The flow \(s^-\) for real \(s\) has two classes. For \(x<s\), \([x,p)\) is the set of \(w\) with \(x\le w<s\), which is endless. For \(x\ge s\), \([x,p)\) is the set of \(w\) with \(s\le w\le x\), with maximum \(s\). So the type is \((1,1)\), and \(F_p=\{s\}\). The flow \(\infty^-\) has one class, which is endless: type \((1,0)\).

The arcs directed by the reverse order give in the same way flows \(s^+\) for real \(s\), of type \((1,1)\), and one flow of type \((1,0)\), which runs downwards on the whole line. Together with the flows \(\bar x\), of type \((0,1)\), these are all flows on the real line.

**Example 6.2** (the rational numbers). Let \(T\) be the set of rational numbers with the betweenness of the line, and \(s\) an irrational number. The set \(A\) of rational numbers below \(s\), with the usual order, is an endless directed arc. By the argument of Example 6.1, with no rational number equal to \(s\),
\[
xy.A\iff x<y<s\ \text{ or }\ s<y<x .
\]
For \(x<s\) the arc \([x,p)\) is the set of rational \(w\) with \(x\le w<s\); for \(x>s\) it is the set of rational \(w\) with \(s<w\le x\), directed downwards. Both are endless. So there are two endless classes, the rational numbers below \(s\) and those above \(s\), and the type is \((2,0)\). The formula is symmetric: the rational numbers above \(s\), directed downwards, have the same flow as \(A\), although the two arcs are disjoint. This flow runs from both sides towards the missing number \(s\).

**Example 6.3** (a missing centre). On three points with the empty relation, the empty flow is the flow of the star formed by all three points, and its type is \((0,3)\). It is the restriction of the flow towards the centre of the tree in which a centre is joined to the three points.

## 7. Exercises

**7.1.** Let \(T\) be a set with at least two points and the empty relation. Show that the flows on \(T\) are the flows \(\bar a\), \(a\in T\), and the empty relation, and describe \(\bar a\).

**7.2.** On the real line let \(s^+\) be the flow of the arc \(\{w\mid w>s\}\) directed by the reverse of the usual order. Find the pairs \((x,y)\) with \(xy.s^+\), and compare with Exercise 5.2 of the lesson on flows.

**7.3.** Let \(F\) be a star and \(y\in F\). Show that \(\operatorname{flow}(F)\) is obtained from the flow \(\bar y\) by removing the pairs \((x,y)\) with \(x\notin N(y)\).

**7.4.** Let \(T\) be a dense pretree with at least two points. Show that every flow on \(T\) is the flow towards a point or the flow of an endless directed arc.

**7.5.** Let \(T\) be the vertex set of a finite tree with \(k\) vertices. Show that there are exactly \(2k-1\) flows on \(T\), and describe the flow of an edge.

## 8. Solutions

**7.1.** A subset with three distinct points is not linear, so an arc has at most two points and every directed arc has a maximum. By Example 2.2(a) the only star is \(T\); each point is its own foot, so \(\operatorname{flow}(T)\) is the empty relation. By Theorem 5.1 the flows are the \(\bar a\) and the empty relation. Since \((x,a]\) is \(\{a\}\) for \(x\ne a\), the relation \(xy.\bar a\) holds exactly when \(y=a\ne x\).

**7.2.** Let \(A=\{w\mid w>s\}\) with the reversed order. For \(x,y>s\): \(xy.A\) if and only if \(y<x\) (Proposition 2.4(1) of the lesson on directed arcs). For \(x,y\le s\): if and only if \(y\) lies between \(x\) and the points above \(s\), that is, \(x<y\) (Proposition 2.4(2)). For \(x>s\ge y\) it fails (Proposition 2.4(4)). For \(y>s\ge x\) it fails, because \(y\) is not between \(x\) and the points \(w\) with \(s<w<y\). So
\[
xy.s^+\iff s<y<x\ \text{ or }\ x<y\le s .
\]
This is the flow of Exercise 5.2 of the lesson on flows, with \(a=s\).

**7.3.** Let \(h\) be the foot map. For \(x\in N(y)\) we have \(h(x)=y\), so \(xz.F\) and \(xz.\bar y\) both mean \(z\in(x,y]\). Let \(x\notin N(y)\). Then \(h(x)\ne y=h(y)\), and Lemma 2.4 gives \([x,y]=[x,h(x)]\cup\{y\}\). So \((x,y]=(x,h(x)]\cup\{y\}\), and \(y\notin(x,h(x)]\) by (H2). Hence \(xz.\bar y\) holds if and only if \(xz.F\) or \(z=y\), and \(xy.F\) fails.

**7.4.** The points of a star are pairwise adjacent, and a star has at least two points. A dense pretree has no adjacent points, so it has no star. Apply Theorem 5.1.

**7.5.** A directed arc is a finite totally ordered set and has a maximum, so there is no endless directed arc. By Theorem 5.1 and Example 2.2(c), the flows are the \(k\) flows towards vertices and the flows of the \(k-1\) edges. They are pairwise different: for a flow \(p\) of the first kind \(F_p\) is the vertex, and for one of the second kind \(F_p\) is the edge. For an edge \(\{u,v\}\) and a vertex \(x\), the foot of \(x\) is the end of the edge that the path from \(x\) reaches first, by Lemma 2.3(2); the flow of the edge runs from \(x\) along this path up to that end.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 3. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
