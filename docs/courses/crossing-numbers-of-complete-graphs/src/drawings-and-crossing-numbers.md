# Drawings and crossing numbers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The crossing number of a graph is the least number of crossing points in a drawing of the graph in the plane. For the complete bipartite graph \(K_{m,n}\), drawings found in the 1950s have
\[
\Bigl\lfloor\frac m2\Bigr\rfloor\Bigl\lfloor\frac{m-1}2\Bigr\rfloor\Bigl\lfloor\frac n2\Bigr\rfloor\Bigl\lfloor\frac{n-1}2\Bigr\rfloor
\]
crossings, and for the complete graph \(K_n\), drawings found in the 1960s have
\[
\frac14\Bigl\lfloor\frac n2\Bigr\rfloor\Bigl\lfloor\frac{n-1}2\Bigr\rfloor\Bigl\lfloor\frac{n-2}2\Bigr\rfloor\Bigl\lfloor\frac{n-3}2\Bigr\rfloor
\]
crossings. The conjectures of Zarankiewicz and of Harary and Hill assert that no drawing does better. OpenAI proved both formulas in 2026 [OpenAI-B, Theorem 1.1], [OpenAI-C, Theorem 1.1]. This course proves them in full. The present lesson fixes the definitions, proves the upper bound for \(K_{m,n}\) with Zarankiewicz's drawing, and describes the plan of the lower bounds.

- Drawings and the crossing number (Section 1).
- The two formulas (Section 2).
- Polynomials that vanish on open sets (Section 3).
- Zarankiewicz's drawing (Section 4).
- The plan of the course (Section 5).
- Earlier work (Section 6).

## 1. Drawings and the crossing number

Graphs in this course are finite and simple: no loops and no multiple edges. A *simple arc* from a point \(p\) to a point \(q\ne p\) of the plane \(\mathbb R^2\) is the image of a continuous injective map \(\gamma:[0,1]\to\mathbb R^2\) with \(\gamma(0)=p\) and \(\gamma(1)=q\); its *interior* is \(\gamma((0,1))\). The arc determines \(\gamma\) up to reparametrization, and its interior does not depend on the choice.

**Definition 1.1.** A *drawing* \(D\) of a graph \(G\) consists of distinct points of the plane, one for each vertex, and for each edge \(uv\) a simple arc between the points of \(u\) and \(v\), such that:

1. no edge interior contains the point of a vertex;
2. the interiors of two distinct edges meet in finitely many points;
3. each point \(x\) where the interiors of two distinct edges \(e,f\) meet lies on no third edge, and it is a *proper crossing*: there are an open neighbourhood \(U\) of \(x\) and a homeomorphism \(h\) from \(U\) onto the open unit disc with \(h(x)=0\), mapping \(U\cap e\) onto the horizontal diameter and \(U\cap f\) onto the vertical diameter.

The points of the third kind are the *crossing points* of \(D\), and \(c(D)\) is their number. The *crossing number* of \(G\) is
\[
\operatorname{cr}(G)=\min_D c(D),
\]
the least value over all drawings of \(G\).

We identify a vertex with its point and an edge with its arc. Condition 3 excludes tangencies, common subarcs and three edges through one point. Two edges may cross several times, and every crossing point counts; two edges with a common endpoint may cross. There are no other restrictions on the positions of the vertices or the routes of the edges. Every graph has drawings (Proposition 1.3), and the minimum exists because \(c(D)\) is a nonnegative integer.

Two straight segments whose interiors meet in one point \(x\), and which are not parallel, cross properly at \(x\): an affine bijection of the plane maps the two lines onto the coordinate axes and \(x\) to the origin, and restricted to a small disc around \(x\), followed by a rescaling, it gives the homeomorphism of condition 3.

**Proposition 1.3** (straight-line drawings). Every graph has a drawing with straight edges.

*Proof.* Place the vertices \(v_1,v_2,\ldots\) one at a time. When \(v_j\) is placed, avoid the finitely many lines through two earlier vertices, and the finitely many lines through an earlier vertex and a point where two segments between earlier vertices meet. Then no three vertices are collinear, so no segment contains a third vertex, and two segments with distinct endpoints are not collinear and meet in at most one point, interior to both, where they cross properly. Two segments with a common endpoint meet only there. Three segments through one point would have six distinct endpoints; when the last of these six vertices was placed, it avoided the line through its partner and the meeting point of the other two segments. So no point lies on three edges, and the segments form a drawing. \(\square\)

**Remark 1.2.** The word "crossing number" has several meanings in the literature: some authors count pairs of crossing edges instead of crossing points, some count only pairs that cross an odd number of times, and some exclude crossings of edges with a common endpoint. These numbers can differ; Schaefer's survey [Schaefer, Section 1] describes them and what is known about their relations. In this course the crossing number always counts crossing points, as in Definition 1.1.

## 2. The two formulas

For an integer \(r\ge1\) put
\[
d_r=\Bigl\lfloor\frac r2\Bigr\rfloor\Bigl\lfloor\frac{r-1}2\Bigr\rfloor .
\]
Thus \(d_1=d_2=0\), \(d_3=1\), \(d_4=2\), \(d_5=4\), \(d_6=6\), \(d_7=9\). Writing \(r=2t\) or \(r=2t+1\),
\[
\begin{gathered}
d_{2t}=t(t-1),\\
d_{2t+1}=t^2,\\
d_r=\binom{\lfloor r/2\rfloor}{2}+\binom{\lceil r/2\rceil}{2},
\end{gathered}\tag{2.1}
\]
the last because \(\binom t2+\binom t2=t(t-1)\) and \(\binom t2+\binom{t+1}2=t^2\). Put
\[
\begin{gathered}
Z(m,n)=d_md_n\quad(m,n\ge1),\\
Z(n)=\frac14\,d_nd_{n-2}\quad(n\ge3).
\end{gathered}
\]
For \(n=2s+1\) and \(n=2s\) this gives
\[
\begin{gathered}
Z(2s+1)=\binom s2^{\!2},\\
Z(2s)=\frac{s(s-1)^2(s-2)}4 .
\end{gathered}\tag{2.2}
\]
For example \(Z(5)=1\), \(Z(6)=3\), \(Z(7)=9\), \(Z(8)=18\), \(Z(9)=36\). The two theorems of the course are the following.

**Theorem A** (Zarankiewicz's formula; [OpenAI-B, Theorem 1.1]). For all integers \(m,n\ge1\),
\[
\operatorname{cr}(K_{m,n})=Z(m,n)=d_md_n .
\]

**Theorem B** (the Harary–Hill formula; [OpenAI-C, Theorem 1.1]). For every integer \(n\ge3\),
\[
\operatorname{cr}(K_n)=Z(n).
\]

The upper bound of Theorem A is Proposition 4.1 below. The upper bound of Theorem B is a two-page drawing, constructed and counted in [Two-page drawings and the Harary–Hill formula](two-page-drawings-and-the-harary-hill-formula.md). The lower bounds take the remaining lessons.

## 3. Polynomials that vanish on open sets

Positions in general position are found with the following lemma.

**Lemma 3.1.** A real polynomial in \(k\) variables that vanishes on a nonempty open subset of \(\mathbb R^k\) is the zero polynomial. Consequently, if \(P_1,\ldots,P_N\) are nonzero polynomials and \(O\subseteq\mathbb R^k\) is open and nonempty, some point of \(O\) is a zero of none of them.

*Proof.* A nonempty open set contains a box \(I_1\times\cdots\times I_k\) of nondegenerate open intervals. Induct on \(k\). For \(k=1\), a polynomial with infinitely many roots is zero. For \(k>1\), write \(P=\sum_jc_j(x_1,\ldots,x_{k-1})x_k^j\). For fixed \((x_1,\ldots,x_{k-1})\) in \(I_1\times\cdots\times I_{k-1}\), the one-variable polynomial \(P(x_1,\ldots,x_{k-1},\cdot)\) vanishes on \(I_k\), so all \(c_j(x_1,\ldots,x_{k-1})\) are \(0\); by induction every \(c_j\) is zero. For the second statement apply the first to the product \(P_1\cdots P_N\), which is nonzero because polynomials in several variables form an integral domain [Judson, Proposition 17.1.4, applied one variable at a time]. \(\square\)

## 4. Zarankiewicz's drawing

Let the vertex classes of \(K_{m,n}\) be \(\{a_1,\ldots,a_m\}\) and \(\{b_1,\ldots,b_n\}\).

**Proposition 4.1** (the upper bound; [OpenAI-B, Section 5.1]). There is a drawing of \(K_{m,n}\) with straight edges and exactly \(d_md_n\) crossing points. Hence \(\operatorname{cr}(K_{m,n})\le d_md_n\).

*Proof.* Place \(\lfloor m/2\rfloor\) of the vertices \(a_i\) on the positive vertical half-axis and the other \(\lceil m/2\rceil\) on the negative one, and similarly \(\lfloor n/2\rfloor\) of the \(b_p\) on the positive horizontal half-axis and \(\lceil n/2\rceil\) on the negative one, all at distinct nonzero coordinates, to be fixed in a moment. Draw each edge \(a_ib_p\) as the straight segment between its endpoints.

The segment from \((0,y)\) to \((x,0)\), \(x,y\ne0\), lies except for its endpoints in the open quadrant determined by the signs of \(x\) and \(y\); so no edge interior contains a vertex, and segments in different quadrants have disjoint interiors. Two segments with a common endpoint meet only there, as they lie on different lines through it.

Consider two segments in one quadrant, say the first quadrant, from \((0,y_1)\) to \((x_1,0)\) and from \((0,y_2)\) to \((x_2,0)\) with \(0<y_1<y_2\) and \(x_1\ne x_2\). The first lies on the line \(\ell(x,y)=x/x_1+y/y_1-1=0\). At the endpoints of the second segment, \(\ell(0,y_2)=y_2/y_1-1>0\) and \(\ell(x_2,0)=x_2/x_1-1\), which is negative exactly when \(x_2<x_1\). Likewise the endpoints of the first segment lie on opposite sides of the line of the second exactly when \(x_1>x_2\). Two segments meet in an interior point exactly when each separates the endpoints of the other, so they cross exactly when \(x_2<x_1\), that is, when the lower of the two vertical endpoints is joined to the farther horizontal one; then they meet in one point, and not being parallel they cross properly there (Section 1). Hence, for two vertices \(a_i,a_k\) on the vertical half-axis and two vertices \(b_p,b_q\) on the horizontal half-axis of a quadrant, exactly one of the two pairs of disjoint edges among them crosses, once. If a quadrant has \(u\) vertices of the first class and \(v\) of the second on its two half-axes, its edges cross \(\binom u2\binom v2\) times, and summing over the four quadrants with (2.1),
\[
\begin{gathered}
\Bigl(\binom{\lfloor m/2\rfloor}2+\binom{\lceil m/2\rceil}2\Bigr)\\
\cdot\Bigl(\binom{\lfloor n/2\rfloor}2+\binom{\lceil n/2\rceil}2\Bigr)=d_md_n .
\end{gathered}
\]

It remains to choose the coordinates so that no three segments pass through one point; then every crossing point lies on exactly two edges and the drawing satisfies Definition 1.1. Three segments through one point lie in one quadrant and have six distinct endpoints, since segments with a common endpoint meet only there; write the vertical endpoints as \((0,y_1),(0,y_2),(0,y_3)\) and the horizontal ones as \((x_1,0),(x_2,0),(x_3,0)\). The \(j\)-th segment lies on the line \(y_jx+x_jy=x_jy_j\), and three lines through one point have linearly dependent coefficient vectors, so
\[
\det\begin{pmatrix}y_1&x_1&x_1y_1\\ y_2&x_2&x_2y_2\\ y_3&x_3&x_3y_3\end{pmatrix}=0 .
\]
This determinant is a nonzero polynomial in the six coordinates: at \((y_1,y_2,y_3,x_1,x_2,x_3)=(1,2,3,1,2,4)\) it equals \(-2\). The coordinates range over a nonempty open subset of \(\mathbb R^{m+n}\) (prescribed signs, distinct values), there are finitely many triples of segments, and by Lemma 3.1 some choice of coordinates is a zero of none of these determinants. \(\square\)

## 5. The plan of the course

The lower bounds are algebraic. A minimum drawing is first replaced by a *normal* one: polygonal, straight near vertices and crossing points, and without crossings between edges with a common endpoint, with no more crossing points ([Polygonal drawings](polygonal-drawings.md)). Orienting the edges, every crossing gets a sign, and at every vertex the edges leave in a cyclic order. [Signed crossings and cycles](signed-crossings-and-cycles.md) combines the signed crossing counts with these orders into a bilinear form \(J\) on the edge space and proves that \(J\) vanishes on every pair of cycles; this is the only place where the geometry of the plane enters.

The rest is linear algebra. [Interpolation](interpolation.md) collects facts on polynomial interpolation, and [An intersection inequality for subspaces](an-intersection-inequality-for-subspaces.md) proves that subspaces \(U_1,\ldots,U_m\), \(V_1,\ldots,V_m\) of an \(N\)-dimensional space with \(U_i\cap V_i=0\) satisfy \(\sum_{i,j}\dim(U_i\cap V_j)\le\lfloor m^2/4\rfloor N\). [The Zarankiewicz formula](the-zarankiewicz-formula.md) applies an interpolation map to the blocks of \(J\) belonging to pairs of vertices of the first class: the diagonal blocks become invertible matrices, the off-diagonal blocks become matrices of rank at most the number of crossings between two stars, and the cycle relations put the blocks in the form \(X_i-Y_k\) to which the subspace inequality applies. [The lower bound for complete graphs](the-lower-bound-for-complete-graphs.md) evaluates polynomials at the pairs of crossing edges of \(K_n\); the cycle relations make the evaluation injective and its image isotropic for a nondegenerate form, which bounds its dimension by half the number of crossing pairs. [Two-page drawings and the Harary–Hill formula](two-page-drawings-and-the-harary-hill-formula.md) supplies the matching drawing of \(K_n\).

## 6. Earlier work

The problem for \(K_{m,n}\) is Turán's brick factory problem. Zarankiewicz described the drawing of Proposition 4.1 and claimed its optimality, but his argument, like Urbanik's, contained an error, found later by Kainen and Ringel and independently by Blažek; the formula became Zarankiewicz's conjecture [Schaefer, entry "Crossing number", Values and footnote 70]. Drawings of \(K_n\) with \(Z(n)\) crossings were found by Hill and by Guy, whose note of 1960 gave the first published upper bound, and Harary and Hill stated the formula for \(K_n\) as a conjecture in 1963 [Schaefer, entry "Crossing number"], [OpenAI-C, Section 1]. Before 2026 the formula for \(K_n\) was known for \(n\le12\), with a heavily computer-assisted proof of \(\operatorname{cr}(K_{13})=225\), and hence \(\operatorname{cr}(K_{14})=315\), reported by Aichholzer [Aichholzer]; Zarankiewicz's formula was known for \(\min(m,n)\le6\) and for \(n\le8\), \(m\le10\); asymptotically \(\operatorname{cr}(K_n)>0.985\,Z(n)\) and \(\operatorname{cr}(K_{n,n})\ge0.9118\,Z(n,n)\) were known, the latter two by flag-algebra methods [Schaefer, entry "Crossing number", Values]. Restricted classes of drawings of \(K_n\) were known to have at least \(Z(n)\) crossings: two-page drawings and monotone drawings [Schaefer, entries "Book crossing number" and "Monotone crossing number"] and shellable drawings [OpenAI-C, Section 1]; Hubard, Ndiaye and Solé-Pi prove the bound for antipodal drawings and formulate higher-dimensional analogues [HNS]. Clancy, Haythorpe and Newcombe survey the graphs whose crossing numbers are known [CHN].

OpenAI's two papers of 23 September 2026 prove both formulas for unrestricted drawings [OpenAI-B], [OpenAI-C], and the release reports a formal verification of both statements in Lean [OpenAI-Lean]. This course does not rely on that verification; it proves every step. The lessons follow the arguments of [OpenAI-B] and [OpenAI-C], with independent exposition and with several proofs written out in more detail: the normalization of drawings, the parallel copies in the cycle pairing, the divisibility argument for complete graphs, and the count of the two-page drawing.

## 7. Exercises

**7.1.** Draw \(K_4\) without crossings, and show that the straight-line drawing of \(K_4\) with its vertices at the corners of a square has exactly one crossing.

**7.2.** Show that \(Z(n)=\frac14d_nd_{n-2}\) agrees with the floor product in the introduction, and verify (2.2).

**7.3.** Show that the drawing of Proposition 4.1 for \(K_{3,3}\) has one crossing, and draw \(K_{2,n}\) without crossings.

**7.4.** Show that \(d_{2t}=\frac{2t}{2t-2}\,d_{2t-1}\) for \(t\ge2\), and that \(2s\,Z(2s-1)=(2s-4)\,Z(2s)\) for \(s\ge3\). (These identities return in the even cases of both theorems.)

## 8. Solutions

**7.1.** Put three vertices at the corners of a triangle and the fourth inside it, with straight edges: the three segments from the inner vertex stay inside the triangle and meet only there, so there is no crossing. With the vertices at the corners \((0,0),(1,0),(1,1),(0,1)\) of a square, the four sides meet only at corners, each diagonal meets the sides only at its endpoints, and the two diagonals cross once, at the centre.

**7.2.** \(\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor=d_n\), and \(\lfloor(n-2)/2\rfloor\lfloor(n-3)/2\rfloor=d_{n-2}\). For \(n=2s+1\), \(d_n=s^2\) and \(d_{n-2}=(s-1)^2\), so \(Z=s^2(s-1)^2/4=\binom s2^2\). For \(n=2s\), \(d_n=s(s-1)\) and \(d_{n-2}=(s-1)(s-2)\).

**7.3.** For \(K_{3,3}\): one \(a\)-vertex and one \(b\)-vertex on each positive half-axis, two on each negative one. Only the third quadrant has two vertices on both half-axes, so there is \(\binom22\binom22=1\) crossing. For \(K_{2,n}\) each half-axis of the first class carries one vertex, and no quadrant has two first-class vertices: \(d_2=0\) crossings.

**7.4.** \(d_{2t}=t(t-1)\) and \(d_{2t-1}=(t-1)^2\), so \(d_{2t}/d_{2t-1}=t/(t-1)=2t/(2t-2)\). By (2.2), \(2s\,Z(2s-1)=2s\binom{s-1}2^2\) and \((2s-4)Z(2s)=(2s-4)\frac{s(s-1)^2(s-2)}4\), and both equal \(\frac12s(s-1)^2(s-2)^2\).

## References

- [Aichholzer] O. Aichholzer, *Another small but long step for crossing numbers: cr(13) = 225 and cr(14) = 315*, Proceedings of the 33rd Canadian Conference on Computational Geometry (CCCG 2021), 72–77, in the open proceedings volume. https://cccg.ca/proceedings/2021/CCCG2021.pdf
- [CHN] K. Clancy, M. Haythorpe, A. Newcombe, *A survey of graphs with known or bounded crossing numbers*, Australas. J. Combin. 78 (2020); arXiv:1901.05155. https://arxiv.org/abs/1901.05155
- [HNS] A. Hubard, C. S. Ndiaye, O. Solé-Pi, *Crossing numbers of simplicial complexes*, preprint, 14 October 2026. https://arxiv.org/abs/2610.21017
- [Judson] T. W. Judson, *Abstract Algebra: Theory and Applications*, online edition, Proposition 17.1.4; the text of the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30). https://judsonbooks.org/aata-files/aata-html/poly-section-rings.html
- [OpenAI-B] OpenAI, *The crossing number of complete bipartite graphs*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1 and Section 5.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026
- [OpenAI-C] OpenAI, *The crossing number of complete graphs*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026
- [OpenAI-Lean] OpenAI, Lean documentation of release family 165 (the Harary–Hill and Zarankiewicz formulas). https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/165.md
- [Schaefer] M. Schaefer, *The graph crossing number and its variants: a survey*, Electron. J. Combin., Dynamic Survey DS21, ninth edition, 17 July 2026, Section 1 and the entry "Crossing number". https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS21
