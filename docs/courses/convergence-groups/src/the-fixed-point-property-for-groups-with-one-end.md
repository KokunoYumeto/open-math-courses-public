# The fixed-point property for groups with one end

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A group has the *fixed-point property for trees with finite edge stabilizers* if each of its actions on a tree, without inversions and with finite edge stabilizers, fixes a point ([Trees and classes of finite intervals](trees-and-classes-of-finite-intervals.md), Definition 1.1). In the lessons on the dendrite quotient and on the tree of cut points this property is a hypothesis on the group. This lesson proves it for a large class of groups:

> a finitely generated group whose Cayley graph has one end has the fixed-point property for trees with finite edge stabilizers (Theorem 5.1).

The proof has three steps. An edge of the tree divides the tree into two sides. For a base point \(o\) of the tree, the side on which the point \(yo\) lies is a function of \(y\in\Gamma\) with two values, and it changes across finitely many edges of the Cayley graph only. If the Cayley graph has one end, such a function is constant outside a finite set (Lemma 3.1). This bounds the number of edges of one orbit that the path from \(o\) to \(go\) contains (Lemma 4.1), so the orbit of \(o\) is bounded; and a bounded orbit has a centre, which is fixed (Corollary 2.2).

The statement is Lemma 6.6 of [Bowditch], where it is derived from the structure theory of groups acting on trees. The argument given here is the one of the lemma on tree actions in [OpenAI-S, Section 2], with the property of having one end in the place of the vanishing of a cohomology group. The lesson uses the lesson named above and no other lesson of this course.

## 1. Paths and sides in a tree

As in the lesson on trees, a *tree* is a nonempty discrete median pretree \(S\); its *edges* are the pairs of adjacent points; the points of an interval \([x,z]\), in their order from \(x\) to \(z\), form the *list* of \([x,z]\), in which consecutive points are adjacent; and the edges \(\{x_{i-1},x_i\}\) of the list are the *edges of \([x,z]\)*. If \(w\in[x,z]\), the list of \([x,z]\) is the list of \([x,w]\) followed by the list of \([w,z]\). A tree contains no *cycle*: no sequence of at least three distinct points in which each is adjacent to the next and the last to the first.

A *path* from \(x\) to \(z\) is a sequence \(x=y_0,y_1,\dots,y_n=z\) of pairwise distinct points in which consecutive points are adjacent. The list of \([x,z]\) is a path from \(x\) to \(z\).

**Lemma 1.1.** In a tree, the list of \([x,z]\) is the only path from \(x\) to \(z\).

**Proof.** Let \(u_0,\dots,u_m\) be the list of \([x,z]\) and \(y_0,\dots,y_n\) a path from \(x\) to \(z\) different from it. Neither sequence is a beginning of the other, because both end with \(z\) and \(z\) occurs once in each. So there is a least \(i\) with \(y_{i+1}\ne u_{i+1}\); then \(y_i=u_i\). Let \(j>i\) be the least index such that \(y_j\) is one of \(u_{i+1},\dots,u_m\); it exists because \(y_n=u_m\). Let \(y_j=u_l\). The points
\[
\begin{gathered}
y_i,\ y_{i+1},\ \dots,\ y_j=u_l,\\
u_{l-1},\ \dots,\ u_{i+1}
\end{gathered}
\]
are pairwise distinct: the \(y\) are, the \(u\) are, the points \(y_{i+1},\dots,y_{j-1}\) are not among \(u_{i+1},\dots,u_m\) by the choice of \(j\), and \(y_i=u_i\) is not among \(u_{i+1},\dots,u_l\). Each is adjacent to the next, and the last to the first. Their number is \(j+l-2i\), which is at least \(3\), because \(j\ge i+1\), \(l\ge i+1\), and \(j=l=i+1\) would give \(y_{i+1}=u_{i+1}\). This is a cycle, a contradiction. \(\blacksquare\)

Let \(\{a,b\}\) be an edge of \(S\). A point \(y\) lies *on the side of \(a\)* if \(b\notin[y,a]\), and *on the side of \(b\)* if \(a\notin[y,b]\).

**Lemma 1.2.** Let \(\{a,b\}\) be an edge of a tree \(S\).

1. Every point lies on exactly one of the two sides. All points of \([y,a]\) lie on the side of \(a\) if \(y\) does.
2. For \(x,z\in S\): \(\{a,b\}\) is an edge of \([x,z]\) if and only if \(x\) and \(z\) lie on different sides.
3. For \(x,z,w\in S\): every edge of \([x,z]\) is an edge of \([x,w]\) or an edge of \([w,z]\).

**Proof.** (1) Let \(y\in S\). If \(b\notin[y,a]\), the list of \([y,a]\) followed by \(b\) is a path from \(y\) to \(b\); by Lemma 1.1 it is the list of \([y,b]\), which therefore contains \(a\). If \(b\in[y,a]\), the list of \([y,a]\) is the list of \([y,b]\) followed by that of \([b,a]\), which is \(b,a\); so the list of \([y,b]\) does not contain \(a\). Hence exactly one of \(b\notin[y,a]\), \(a\notin[y,b]\) holds. If \(y\) lies on the side of \(a\) and \(w\in[y,a]\), then \([w,a]\subseteq[y,a]\) does not contain \(b\).

(2) Let \(\{a,b\}\) be an edge of \([x,z]\), with \(a\) before \(b\) in the list. The list of \([x,a]\) is the part up to \(a\), which does not contain \(b\); the list of \([z,b]\) is the part from \(b\) on, reversed, which does not contain \(a\). So \(x\) lies on the side of \(a\) and \(z\) on the side of \(b\). Conversely let \(x\) lie on the side of \(a\) and \(z\) on the side of \(b\). By (1) the points of \([x,a]\) lie on the side of \(a\) and those of \([b,z]\) on the side of \(b\), so these two lists have no common point. The list of \([x,a]\) followed by the list of \([b,z]\) is a path from \(x\) to \(z\). By Lemma 1.1 it is the list of \([x,z]\), and \(\{a,b\}\) is one of its edges.

(3) By (2) the points \(x\) and \(z\) lie on different sides of the edge. The point \(w\) lies on one side, so it lies on a different side from \(x\) or from \(z\). \(\blacksquare\)

For \(x,z\in S\) let \(d(x,z)\) be the number of edges of \([x,z]\). By Lemma 1.2(3),
\[
d(x,z)\le d(x,w)+d(w,z)
\]
for all \(w\), and equality holds if \(w\in[x,z]\), because then the list of \([x,z]\) is made of the lists of \([x,w]\) and \([w,z]\). An automorphism of \(S\) maps lists to lists, so it preserves \(d\).

## 2. Bounded sets have a centre

A set \(X\subseteq S\) is *bounded* if the numbers \(d(x,y)\), \(x,y\in X\), are bounded. Its *diameter* \(D\) is the largest of them.

**Proposition 2.1.** Let \(X\) be a nonempty bounded subset of a tree \(S\), of diameter \(D\), and let \(r\) be the least integer with \(2r\ge D\). Let \(c(X)\) be the set of all points \(w\in S\) with \(d(w,z)\le r\) for all \(z\in X\). If \(D\) is even, \(c(X)\) consists of one point. If \(D\) is odd, \(c(X)\) consists of two adjacent points.

**Proof.** Choose \(x_0,y_0\in X\) with \(d(x_0,y_0)=D\), and let \(u_0,\dots,u_D\) be the list of \([x_0,y_0]\). Then \(d(u_i,u_j)=|i-j|\).

*Every point of \(c(X)\) is some \(u_i\) with \(i\le r\) and \(D-i\le r\).* Let \(w\in c(X)\) and let \(p\) be the median of \(x_0,y_0,w\). It lies in \([x_0,w]\), in \([y_0,w]\) and in \([x_0,y_0]\), so
\[
\begin{aligned}
&d(x_0,w)+d(y_0,w)\\
&\quad=d(x_0,p)+d(y_0,p)+2d(p,w)\\
&\quad=D+2d(p,w).
\end{aligned}
\]
The left side is at most \(2r\le D+1\). So \(d(p,w)=0\), that is, \(w=p=u_i\) for some \(i\), and \(i=d(x_0,w)\le r\), \(D-i=d(y_0,w)\le r\).

*Every such \(u_i\) lies in \(c(X)\).* Let \(z\in X\) and let \(u_j\) be the median of \(x_0,y_0,z\). As above,
\[
\begin{gathered}
d(z,x_0)=d(z,u_j)+j\le D,\\
d(z,y_0)=d(z,u_j)+D-j\le D,
\end{gathered}
\]
so \(d(z,u_j)\le j\) and \(d(z,u_j)\le D-j\). If \(j\le i\), then \(d(z,u_i)\le d(z,u_j)+(i-j)\le i\le r\). If \(j\ge i\), then \(d(z,u_i)\le d(z,u_j)+(j-i)\le D-i\le r\).

If \(D=2r\), the conditions \(i\le r\), \(D-i\le r\) hold for \(i=r\) only. If \(D=2r-1\), they hold for \(i=r-1\) and \(i=r\), and \(u_{r-1},u_r\) are adjacent. \(\blacksquare\)

The set \(c(X)\) is the *centre* of \(X\). It is defined by \(X\) and the function \(d\) alone. So \(c(gX)=g\,c(X)\) for every automorphism \(g\) of \(S\).

**Corollary 2.2.** Let a group \(\Gamma\) act on a tree \(S\) without inversions, and suppose that for some \(o\in S\) the numbers \(d(o,go)\), \(g\in\Gamma\), are bounded. Then \(\Gamma\) fixes a point of \(S\).

**Proof.** Let \(X\) be the orbit of \(o\). Since \(d(go,ho)=d(o,g^{-1}ho)\), the set \(X\) is bounded, and \(gX=X\) for all \(g\). So every \(g\) maps \(c(X)\) to itself. If \(c(X)\) is one point, it is fixed. If \(c(X)\) consists of two adjacent points, every \(g\) fixes both or exchanges them; the action is without inversions, so both are fixed. \(\blacksquare\)

## 3. Cayley graphs with one end

Let \(\Gamma\) be a group with a finite generating set \(\Sigma\), and let \(\Sigma'\) be the set of the elements of \(\Sigma\) and their inverses. The *Cayley graph* \(G\) has the vertex set \(\Gamma\); the vertices \(y\) and \(yh\) are adjacent for \(y\in\Gamma\) and \(h\in\Sigma'\), \(h\ne1\). It is connected, because every element is a product of elements of \(\Sigma'\), and every vertex has finitely many neighbours.

For a finite set \(A\subseteq\Gamma\) let \(G\setminus A\) be the graph on \(\Gamma\setminus A\) with the edges of \(G\) between its vertices. The graph \(G\) is *one-ended* if for every finite set \(A\) the graph \(G\setminus A\) has exactly one infinite component.

**Lemma 3.1.** Let \(G\) be one-ended, and let \(s\) be a function on \(\Gamma\) with values \(0,1\) such that the set \(N\) of all \(y\in\Gamma\) with \(s(y)\ne s(yh)\) for some \(h\in\Sigma'\) is finite. Then there is a finite set \(W\subseteq\Gamma\) such that \(s\) is constant on \(\Gamma\setminus W\).

**Proof.** If \(N\) is empty, \(s\) takes the same value at adjacent vertices, and it is constant because \(G\) is connected. Let \(N\) be not empty.

*\(G\setminus N\) has finitely many components.* Let \(C\) be a component and \(v\in C\). Take a path in \(G\) from \(v\) to a point of \(N\), and let \(w\) be its last vertex before the first vertex in \(N\). Then \(w\in C\), and \(w\) is a neighbour of a point of \(N\). The finite set \(N\) has finitely many neighbours, and different components contain different ones.

*\(s\) is constant on each component of \(G\setminus N\).* Two vertices of a component are joined by a path in \(G\setminus N\), and consecutive vertices \(y\), \(yh\) of it have \(s(y)=s(yh)\), because \(y\notin N\).

Exactly one component is infinite. Let \(W\) be the union of \(N\) and the other components; it is finite. \(\blacksquare\)

## 4. Edges of one orbit on a path

**Lemma 4.1.** Let \(\Gamma\) be a group with a finite generating set \(\Sigma\) whose Cayley graph is one-ended. Let \(\Gamma\) act on a tree \(S\) without inversions, let \(o\in S\), and let \(\{a,b\}\) be an edge of \(S\) with finite stabilizer. Then there is a number \(n\) such that for every \(g\in\Gamma\) at most \(n\) of the edges of \([o,go]\) are images \(x\{a,b\}\), \(x\in\Gamma\), of the edge \(\{a,b\}\).

**Proof.** For \(y\in\Gamma\) let \(s(y)=0\) if the point \(yo\) lies on the side of \(a\), and \(s(y)=1\) if it lies on the side of \(b\) (Lemma 1.2(1)). For \(x,g\in\Gamma\), the automorphism \(x^{-1}\) maps the list of \([o,go]\) to the list of \([x^{-1}o,x^{-1}go]\). So, by Lemma 1.2(2),
\[
\begin{gathered}
x\{a,b\}\ \text{is an edge of }[o,go]\\
\Longleftrightarrow\quad s(x^{-1})\ne s(x^{-1}g).
\end{gathered}\tag{1}
\]

*The set \(N\) of Lemma 3.1 is finite.* Let \(h\in\Sigma'\). By (1) with \(x=y^{-1}\) and \(g=h\), \(s(y)\ne s(yh)\) holds exactly if \(y^{-1}\{a,b\}\) is an edge of \([o,ho]\). The interval \([o,ho]\) has finitely many edges. For one of them, \(\varepsilon\), let \(y_1\) and \(y\) be two elements with \(y_1^{-1}\{a,b\}=\varepsilon=y^{-1}\{a,b\}\). Then \(j=y_1y^{-1}\) maps the pair \(\{a,b\}\) to itself. It does not exchange \(a\) and \(b\), because the action is without inversions; so \(j\) lies in the stabilizer \(J=\Gamma(a)\cap\Gamma(b)\) of the edge, and \(y=j^{-1}y_1\). So at most as many \(y\) belong to \(\varepsilon\) as \(J\) has elements. Since \(\Sigma'\) is finite, \(N\) is finite.

*The bound.* By Lemma 3.1 there is a finite set \(W\) outside which \(s\) is constant. Let \(x\{a,b\}\) be an edge of \([o,go]\). By (1), one of \(x^{-1}\), \(x^{-1}g\) lies in \(W\); that is, \(x\) lies in \(W^{-1}\) or in \(gW^{-1}\), where \(W^{-1}\) is the set of the inverses of the elements of \(W\). There are at most \(2|W|\) such \(x\). So \(n=2|W|\) has the required property. \(\blacksquare\)

## 5. The theorem

**Theorem 5.1.** Let \(\Gamma\) be a group with a finite generating set whose Cayley graph is one-ended. Then \(\Gamma\) has the fixed-point property for trees with finite edge stabilizers.

**Proof.** Let \(\Gamma\) act on a tree \(S\) without inversions, such that every edge has a finite stabilizer, and let \(o\in S\). Let \(\varepsilon_1,\dots,\varepsilon_q\) be the edges of the intervals \([o,ho]\), \(h\in\Sigma'\); they are finitely many. For each \(\varepsilon_t\) let \(n_t\) be the number of Lemma 4.1.

Let \(g\in\Gamma\). Write \(g=h_1h_2\cdots h_m\) with \(h_i\in\Sigma'\), and let \(g_i=h_1\cdots h_i\), \(g_0=1\). By Lemma 1.2(3), applied \(m-1\) times, every edge of \([o,go]\) is an edge of one of the intervals
\[
[g_{i-1}o,\ g_io]=g_{i-1}[o,h_io]
\]
with \(1\le i\le m\), so it is an image of one of \(\varepsilon_1,\dots,\varepsilon_q\) under an element of \(\Gamma\). By Lemma 4.1, at most \(n_t\) edges of \([o,go]\) are images of \(\varepsilon_t\). Hence
\[
d(o,go)\le n_1+\dots+n_q\qquad(g\in\Gamma).
\]
By Corollary 2.2, \(\Gamma\) fixes a point of \(S\). \(\blacksquare\)

So the hypothesis on the group in Theorem 3.1 of the lesson on trees, in the theorems of [The dendrite quotient is not a point](the-dendrite-quotient-is-not-a-point.md), and hypothesis (b) of [The tree of cut points](the-tree-of-cut-points.md) hold for every group with a finite generating set whose Cayley graph is one-ended.

The proof used the generating set \(\Sigma\) only through the Cayley graph, and the theorem applies as soon as the Cayley graph of one finite generating set is one-ended. The converse direction, that a finitely generated group whose Cayley graph is not one-ended and which is infinite acts on a tree with finite edge stabilizers and without a fixed point, is a theorem of Stallings; it is much deeper and is not used in this course.

## 6. Exercises

**6.1.** Show that the Cayley graph of the group of integers with \(\Sigma=\{1\}\) is not one-ended. Which step of the proof of Lemma 4.1 fails for the action of the integers on themselves by translations?

**6.2.** Show that the Cayley graph of \(\mathbb Z^2\) with \(\Sigma=\{(1,0),(0,1)\}\) is one-ended.

**6.3.** Show that a finite group that acts on a tree without inversions fixes a point. Give an action of the group with two elements on a tree that fixes no point.

**6.4.** Let \(\Gamma\) be the free group on two generators \(s,t\), with \(\Sigma=\{s,t\}\). Its Cayley graph \(G\) is a tree in the sense of graph theory, and \(\Gamma\) acts on it by left multiplication. Deduce from Theorem 5.1 that \(G\) is not one-ended, and confirm this directly.

## 7. Solutions

**6.1.** The graph is the line: \(y\) is adjacent to \(y+1\) and \(y-1\). Removing \(A=\{0\}\) leaves two infinite components, the positive and the negative integers. For the action on the tree of integers by translations, with \(o=0\) and the edge \(\{0,1\}\): \(s(y)=0\) for \(y\le0\) and \(s(y)=1\) for \(y\ge1\). The set \(N\) is \(\{0,1\}\), finite, but \(s\) is not constant outside a finite set; Lemma 3.1 is not available.

**6.2.** Let \(A\) be finite and \(n\) such that \(A\) lies in the square \(Q\) of the points \((p,q)\) with \(|p|\le n\), \(|q|\le n\). The points with \(\max(|p|,|q|)=n+1\) form a closed walk around the square, the *frame*; it lies outside \(Q\) and is connected. Let \((p,q)\) be outside \(Q\). If \(|p|>n\), change \(p\) step by step towards \(n+1\) or \(-(n+1)\), whichever has the sign of \(p\); all these points have \(|p|\ge n+1\). Then, if \(|q|>n+1\), change \(q\) step by step until \(|q|=n+1\); all these points have \(|p|=n+1\). The end point is on the frame. If \(|p|\le n\), then \(|q|>n\), and the same is done with the roles of \(p\) and \(q\) exchanged. So all points outside \(Q\) lie in one component of \(G\setminus A\). The other components lie in the finite set \(Q\). Hence there is exactly one infinite component.

**6.3.** The orbit of a point under a finite group is finite, hence bounded, and Corollary 2.2 applies. The tree with two adjacent points \(a,b\) and the map that exchanges them: the group with two elements acts, with an inversion, and fixes no point.

**6.4.** The stabilizer of every vertex is trivial, since \(gy=y\) implies \(g=1\). So the edge stabilizers are trivial, and no element other than \(1\) maps an edge to itself: such an element would fix both ends or have a square that fixes both ends, and the free group has no element of order two. So the action is without inversions and without fixed points. By Theorem 5.1, \(G\) is not one-ended. Directly: after removing the vertex \(1\), the four neighbours \(s,s^{-1},t,t^{-1}\) lie in four different components, because \(G\) is a tree and every path between two of them passes through \(1\); each of the four components is infinite, since it contains the powers of \(s\), of \(s^{-1}\), of \(t\) or of \(t^{-1}\).

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Lemma 6.6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
