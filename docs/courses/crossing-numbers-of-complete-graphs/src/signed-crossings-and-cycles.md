# Signed crossings and cycles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson attaches to a normal drawing a bilinear form \(J\) on the edge space: for two oriented edges, \(J\) adds up the signs of their crossings and, if they share an endpoint, half the sign of their order around it. The main theorem says that \(J\) vanishes on every pair of cycles [OpenAI-B, Lemma 3.1], [OpenAI-C, Lemma 2.1]. It is the only place in the course where the geometry of the plane enters, through one fact: two closed polygonal curves in general position cross as often from left to right as from right to left. The lower bounds of [The Zarankiewicz formula](the-zarankiewicz-formula.md) and [The lower bound for complete graphs](the-lower-bound-for-complete-graphs.md) are linear algebra built on this theorem.

- Orientations, cycles and the form \(J\) (Section 1).
- Closed polygonal walks (Section 2).
- Two chords in a disc (Section 3).
- The cycle pairing (Section 4).

## 1. Orientations, cycles and the form \(J\)

Let \(G\) be a graph with vertex set \(V\) and edge set \(E\). Fix an *orientation* of every edge \(e\), with tail \(t(e)\) and head \(h(e)\). The *edge space* \(\mathbb R^E\) has the edges as a basis, and the *boundary map* \(\partial:\mathbb R^E\to\mathbb R^V\) sends \(e\) to \(h(e)-t(e)\). Its kernel is the *cycle space*; its elements are the *cycles*.

An *oriented simple cycle* is a closed walk \(v_0,v_1,\ldots,v_{k-1},v_k=v_0\) with \(k\ge3\), distinct vertices \(v_0,\ldots,v_{k-1}\), and \(v_{i-1}v_i\) an edge for each \(i\). Its *signed edge vector* has entry \(+1\) on the edge \(v_{i-1}v_i\) if \(t=v_{i-1}\), entry \(-1\) if \(t=v_i\), and \(0\) on edges not used. It is a cycle: at each \(v_i\) the walk arrives along one edge and leaves along another, and the two contributions to the boundary cancel.

**Lemma 1.1.** The cycle space is spanned by the signed edge vectors of oriented simple cycles.

*Proof.* Choose a spanning forest \(F\) of \(G\). For an edge \(e\notin F\), its endpoints lie in one tree of \(F\), and the path between them in \(F\) together with \(e\) is a simple cycle; orient it so that it traverses \(e\) from \(t(e)\) to \(h(e)\), and let \(c_e\) be its signed edge vector, which has entry \(1\) on \(e\) and \(0\) on the other edges outside \(F\). For a cycle \(z\), the cycle \(z'=z-\sum_{e\notin F}z_ec_e\) is supported on \(F\). If \(z'\ne0\), its support is a nonempty forest, which has a vertex \(\ell\) incident with exactly one edge \(f\) of the support; then the coefficient of \(\ell\) in \(\partial z'\) is \(\pm z'_f\ne0\), a contradiction. So \(z'=0\). \(\square\)

From here on \(D\) is a normal drawing of \(G\) (Definition 1.1 of [Polygonal drawings](polygonal-drawings.md)). Edges are straight near every crossing point, so at a crossing point \(x\) of two distinct edges \(e,f\) each has a direction \(d_e,d_f\in\mathbb R^2\), following its orientation, and the two are not parallel. The *sign* of the crossing for the ordered pair \((e,f)\) is the sign of \(\det(d_e,d_f)\): \(+1\) if \(f\) passes from the right of \(e\) to its left. Let
\[
I(e,f)=\sum_{x}\operatorname{sign}\det(d_e,d_f),
\]
the sum over the crossing points of \(e\) and \(f\), and \(I(e,e)=0\). Then \(I(f,e)=-I(e,f)\).

At a vertex \(v\) the edges leave along straight spokes in distinct directions. A *cut* at \(v\) is a direction from \(v\) that is not the direction of a spoke. Listing the edges at \(v\) counterclockwise, starting from the cut, orders them linearly; for edges \(e,f\) at \(v\) put \(T_v(e,f)=1\) if \(e\) comes before \(f\), \(T_v(e,f)=-1\) if \(f\) comes before \(e\), and \(T_v(e,e)=0\). Let \(\sigma_v(e)=1\) if \(t(e)=v\) and \(\sigma_v(e)=-1\) if \(h(e)=v\). Fix a cut at every vertex.

**Definition 1.2.** The form \(J\) of the drawing is the bilinear form on \(\mathbb R^E\) with
\[
\begin{aligned}
J(e,f)&=I(e,f)\\
&\quad+\frac12\sum_{v}\sigma_v(e)\,\sigma_v(f)\,T_v(e,f),
\end{aligned}
\]
the sum over the common endpoints \(v\) of \(e\) and \(f\).

The form is skew-symmetric, since \(I\) and every \(T_v\) are. Reversing the orientation of an edge \(e\) changes the signs of \(I(e,\cdot)\) and of \(\sigma_v(e)\) and leaves \(T_v\) unchanged, so \(J(e,\cdot)\) changes sign, as it must when the basis vector \(e\) is replaced by \(-e\). Hence \(J\), as a bilinear form on the edge space, does not depend on the orientations. Its values on pairs of edges at a vertex depend on the cut there; its values on cycles do not (Exercise 5.3).

**Theorem 1.3** (cycle pairing; [OpenAI-B, Lemma 3.1], [OpenAI-C, Lemma 2.1]). For every normal drawing, all orientations and all cuts, \(J(z,y)=0\) for any two cycles \(z,y\).

The proof occupies Sections 2 to 4.

## 2. Closed polygonal walks

A *closed polygonal walk* is a sequence of points \(a_0,a_1,\ldots,a_k=a_0\), its *corners*, with consecutive corners distinct, together with the segments \(s_i=[a_{i-1},a_i]\) traversed from \(a_{i-1}\) to \(a_i\). Two closed polygonal walks \(\alpha,\beta\) are *in general position* if no corner of either lies on a segment of the other. Then a segment of \(\alpha\) and a segment of \(\beta\) that meet do so in a single point interior to both, and they are not parallel: collinear segments that meet would overlap along a segment containing an endpoint of one of them. Their *signed intersection* is
\[
I(\alpha,\beta)=\sum_{s,t}\operatorname{sign}\det(d_s,d_t),
\]
the sum over the pairs of a segment \(s\) of \(\alpha\) and a segment \(t\) of \(\beta\) that meet, with \(d_s,d_t\) their directions of traversal. A point where several pairs of segments meet is counted once for each pair; neither walk needs to be simple. The same formula defines \(I(\alpha,\beta)\) when \(\alpha\) is a single segment or a finite family of segments.

**Lemma 2.1** (triangles). Let \(T\) be a triangle with corners \(o,p,q\) not on a line, and \(\partial T\) the closed walk \(o,p,q,o\). If \(\partial T\) and a closed polygonal walk \(\beta\) are in general position, then \(I(\partial T,\beta)=0\).

*Proof.* Let \(\lambda_o,\lambda_p,\lambda_q\) be the barycentric coordinates of \(T\): the affine functions on the plane with \(\lambda_o+\lambda_p+\lambda_q=1\) and \(\lambda_o(o)=1\), \(\lambda_o(p)=\lambda_o(q)=0\), and similarly for the others. Let \(g\) be the smallest of the three. Then \(g>0\) on the interior of \(T\), \(g=0\) on \(\partial T\), and \(g<0\) outside \(T\). Follow \(\beta\) once around. It meets \(\partial T\) only at points interior to a side and interior to a segment of \(\beta\), where the two segments cross; at such a point on the side \([p,q]\), say, \(\lambda_p,\lambda_q>0\), so near it \(g=\lambda_o\), which is affine along the segment of \(\beta\) and changes sign there. Between two consecutive meetings \(g\) does not vanish along \(\beta\), so it keeps its sign by the intermediate value theorem. Hence the meetings alternate between *entrances*, where \(g\) becomes positive, and *exits*, and as \(\beta\) is closed there are as many of each.

Suppose \(\det(p-o,q-o)>0\). Then \(o\) lies to the left of the directed side from \(p\) to \(q\), because \(\det(q-p,o-p)=\det(p-o,q-o)\); likewise for the other two sides, so the interior of \(T\) lies to the left of every side traversed along \(\partial T\). At an entrance \(\beta\) crosses a side from its right to its left, and the sign is \(+1\); at an exit it is \(-1\). So \(I(\partial T,\beta)=0\). If \(\det(p-o,q-o)<0\), all signs are reversed. \(\square\)

**Lemma 2.2** (closed walks). If two closed polygonal walks \(\alpha\) and \(\beta\) are in general position, then \(I(\alpha,\beta)=0\).

*Proof.* Let \(\alpha\) have corners \(a_0,\ldots,a_k=a_0\). Choose a point \(o\) outside the finitely many lines that contain a segment of \(\alpha\) or that pass through two distinct corners of \(\alpha\) or \(\beta\). Each triangle \(T_i\) with corners \(o,a_{i-1},a_i\) is then nondegenerate. The walk \(\partial T_i\) and \(\beta\) are in general position: the corners \(a_{i-1},a_i\) are not on \(\beta\), and \(o\) is not on \(\beta\), since a segment of \(\beta\) through \(o\) would put \(o\) on the line through two corners of \(\beta\); a corner \(b\) of \(\beta\) is not on \([a_{i-1},a_i]\), and not on \([o,a_i]\), since then \(o\) would lie on the line through \(a_i\) and \(b\). The walk \(\partial T_i\) consists of \([o,a_{i-1}]\), the segment \(s_i\) of \(\alpha\), and \([a_i,o]\); a reversed segment has the opposite signed intersection with \(\beta\). With \(c_i=I([o,a_i],\beta)\), summing gives
\[
\begin{aligned}
\sum_{i=1}^kI(\partial T_i,\beta)&=I(\alpha,\beta)+\sum_{i=1}^k(c_{i-1}-c_i)\\
&=I(\alpha,\beta),
\end{aligned}
\]
because the last sum telescopes and \(a_k=a_0\). By Lemma 2.1 every term on the left is \(0\). \(\square\)

## 3. Two chords in a disc

Let \(B\) be a closed disc with boundary circle \(\partial B\). A *chord* is a segment between two distinct points of \(\partial B\); its interior lies in the open disc. Two chords whose four endpoints are distinct lie on distinct lines, so they meet in at most one point, interior to both.

For a directed chord \(C\) from \(c_-\) to \(c_+\) give the endpoints the coefficients \(\epsilon(c_-)=-1\) and \(\epsilon(c_+)=+1\). Choose a point \(\kappa\) of \(\partial B\), the *cut*, different from the endpoints considered, and for two distinct such points \(a,b\) of \(\partial B\) put \(T(a,b)=1\) if \(a\) comes before \(b\) on the way counterclockwise around \(\partial B\) from \(\kappa\), and \(T(a,b)=-1\) otherwise.

**Lemma 3.1** (two chords; [OpenAI-B, Lemma 3.1], [OpenAI-C, Lemma 2.1]). Let \(C\) and \(E\) be directed chords of \(B\) with four distinct endpoints. Then
\[
I(C,E)=\frac12\sum_{a,b}\epsilon(a)\,\epsilon(b)\,T(a,b),
\]
the sum over the endpoints \(a\) of \(C\) and \(b\) of \(E\), where \(I(C,E)\) is the sign of the crossing of \(C\) and \(E\) if they meet, and \(0\) otherwise. In particular the right-hand side does not depend on the cut.

*Proof.* *The cut does not matter.* Moving the cut counterclockwise past one endpoint, say \(b_0\) of \(E\), turns \(b_0\) from the first of the four points into the last, so \(T(a,b_0)\) changes from \(-1\) to \(+1\) for both endpoints \(a\) of \(C\), and the right-hand side changes by \(\epsilon(b_0)\sum_a\epsilon(a)=0\). The same holds for an endpoint of \(C\), and any cut is reached from any other by finitely many such moves.

*Evaluation.* The line of \(C\) divides \(\partial B\setminus\{c_-,c_+\}\) into two open arcs, \(A_R\) on the right of the directed chord and \(A_L\) on its left. The counterclockwise arc from \(c_-\) to \(c_+\) is \(A_R\): after a translation and a rotation, which preserve orientation, \(B\) is centred at the origin and \(C\) runs horizontally from \((-a,h)\) to \((a,h)\) with \(a>0\); the counterclockwise arc from \((-a,h)\) to \((a,h)\) passes through the lowest point of the circle, below the chord, and the right of the direction \((1,0)\) is below. Put the cut just before \(c_-\). Then \(T(c_-,b)=1\) for both endpoints \(b\) of \(E\), and \(T(c_+,b)=-1\) exactly for \(b\in A_R\). The terms with \(c_-\) add up to \(-\frac12\bigl(\epsilon(e_-)+\epsilon(e_+)\bigr)=0\), and the right-hand side becomes
\[
\frac12\Bigl(\sum_{b\notin A_R}\epsilon(b)-\sum_{b\in A_R}\epsilon(b)\Bigr)=-\sum_{b\in A_R}\epsilon(b),
\]
since the coefficients of the two endpoints of \(E\) add up to \(0\). If both endpoints of \(E\) lie on one arc, \(E\) lies on one side of the line of \(C\) and misses \(C\), and the value is \(0\). If \(e_-\in A_R\) and \(e_+\in A_L\), then \(E\) and \(C\) cross (each separates the endpoints of the other), \(E\) passes from the right of \(C\) to its left, the sign is \(+1\), and the value is \(-\epsilon(e_-)=1\). If \(e_+\in A_R\) and \(e_-\in A_L\), both are \(-1\). \(\square\)

## 4. The cycle pairing

*Proof of Theorem 1.3.* By bilinearity and Lemma 1.1 it suffices to treat the signed edge vectors \(z\) and \(y\) of two oriented simple cycles \(Z_1\) and \(Z_2\); they may share vertices and edges, and may traverse a shared edge in the same or in opposite directions.

*Step 1: straight edges.* Subdivide every edge of \(G\) at its bends, the points where its polygonal arc changes direction. A bend is not a crossing point, since edges are straight near crossing points, and it lies on no other edge, since all common points of two edges are vertices or crossing points. So the subdivided graph \(G'\), with the bends as new vertices of degree two, has a normal drawing with the same points, in which every edge is a single segment. Orient the pieces of an edge \(e\) along \(e\), keep the cuts at the old vertices, and choose any cuts at the new ones. The vector \(z'\) with \(z'_{e_i}=z_e\) on every piece \(e_i\) of \(e\) is the signed edge vector of the corresponding simple cycle of \(G'\). The crossings of \(e\) and \(f\) are the crossings of their pieces, the spokes at the old vertices are unchanged, and at a new vertex \(b\) between consecutive pieces \(e_i,e_{i+1}\) the two local terms of \(J'(z',y')\) are
\[
\begin{gathered}
\tfrac12z_ey_e\,\sigma_b(e_i)\sigma_b(e_{i+1})\\
\cdot\bigl(T_b(e_i,e_{i+1})+T_b(e_{i+1},e_i)\bigr)=0 .
\end{gathered}
\]
Hence \(J'(z',y')=J(z,y)\), and we may assume that every edge is a single segment. Two edges then meet at most once.

*Step 2: discs.* Choose \(r>0\) so small that the closed disc \(B_v\) of radius \(r\) around each vertex \(v\) meets only the edges at \(v\), each in a segment from \(v\) to \(\partial B_v\), that these discs are pairwise disjoint, and that they contain no crossing point. The part of an edge outside the open discs is its *stretch*, a segment from one circle to another. Let \(p_e^v\) be the point where the edge \(e\) at \(v\) meets \(\partial B_v\). At each vertex use as cut the point of \(\partial B_v\) in the direction of the cut at \(v\); then for distinct edges \(e,f\) at \(v\) the comparison \(T(p_e^v,p_f^v)\) of Section 3 equals \(T_v(e,f)\).

Let \(\gamma\) be the closed polygonal walk that follows \(Z_1\): it runs along the stretch of each edge of \(Z_1\), and in the disc of each vertex of \(Z_1\) along the chord from the point \(p^v_e\) of the edge \(e\) by which \(Z_1\) arrives to the point \(p^v_{e'}\) of the edge \(e'\) by which it leaves.

*Step 3: parallel copies.* For a real number \(\delta\ne0\) of small absolute value, let \(\eta_\delta\) be the closed polygonal walk that follows \(Z_2\) in the same way, except that the stretch of each edge \(f\) is replaced by the parallel segment at distance \(|\delta|\), on the left of the orientation of \(f\) if \(\delta>0\) and on its right if \(\delta<0\), cut off by the two circles at its ends near the ends of the stretch; in the disc of each vertex of \(Z_2\), \(\eta_\delta\) runs along the chord between the displaced points. Write \(p_f^v(\delta)\) for the displaced point of \(f\) on \(\partial B_v\); it tends to \(p^v_f\) as \(\delta\to0\). Since the spokes are radial, the displaced point lies on the circle just counterclockwise of \(p^v_f\) or just clockwise of it, and replacing \(\delta\) by \(-\delta\) moves it to the other side.

For small \(|\delta|\) the following hold, by compactness and continuity. A displaced stretch of \(f\) meets the stretch of an edge \(e\ne f\) of \(Z_1\) exactly when \(e\) and \(f\) cross, once, near their crossing point and transversally, with the same sign \(\det(d_e,d_f)\), because two lines that meet transversally still meet, near the same point, after one of them is moved slightly; it does not meet the stretch of \(f\) itself, being parallel to it; and it meets no other stretch of \(\gamma\), all of which have positive distance from the stretch of \(f\). The displaced stretches stay outside the open discs, and none of them meets a disc of a vertex not on \(f\). Inside the disc of a vertex \(v\) on both cycles, \(\gamma\) and \(\eta_\delta\) are two chords with four distinct endpoints, since a displaced point differs from every original point on the circle. Every corner of either walk is an endpoint of a stretch or a vertex of a chord on a circle, and lies on no segment of the other walk. So \(\gamma\) and \(\eta_\delta\) are in general position.

*Step 4: counting.* Along \(\gamma\) the stretch of \(e\) is traversed in the direction \(z_ed_e\), and along \(\eta_\delta\) the displaced stretch of \(f\) in the direction \(y_fd_f\). By Step 3, the meetings of stretches contribute
\[
\sum_{e,f}z_ey_f\,I(e,f)
\]
to \(I(\gamma,\eta_\delta)\), for either sign of \(\delta\); when \(e\) and \(f\) both lie on both cycles, the crossings of \(e\) with the displaced \(f\) and of \(f\) with the displaced \(e\) give the two terms \(z_ey_fI(e,f)\) and \(z_fy_eI(f,e)\).

In the disc of a vertex \(v\) on both cycles, the chord of \(\gamma\) starts at the point of the edge by which \(Z_1\) arrives and ends at the point of the edge by which it leaves. The cycle arrives along \(e\) exactly when \(z_e\) and \(\sigma_v(e)\) have opposite signs, so the coefficient of \(p^v_e\) in Lemma 3.1 is \(\sigma_v(e)z_e\), and likewise the coefficient of \(p^v_f(\delta)\) is \(\sigma_v(f)y_f\). By Lemma 3.1 the two chords contribute
\[
\frac12\sum_{e,f}\sigma_v(e)z_e\,\sigma_v(f)y_f\,T\bigl(p^v_e,p^v_f(\delta)\bigr),
\]
the sum over the edges \(e\) of \(Z_1\) and \(f\) of \(Z_2\) at \(v\). For \(e\ne f\) the comparison equals \(T_v(e,f)\) when \(|\delta|\) is small. For \(e=f\), a shared edge, the displaced point lies just on one side of \(p^v_e\) for \(\delta\) and on the other side for \(-\delta\), so the two comparisons are \(+1\) and \(-1\). Vertices on only one of the cycles contribute nothing, since the other walk does not enter their discs.

By Lemma 2.2, \(I(\gamma,\eta_\delta)=0=I(\gamma,\eta_{-\delta})\). Taking the average of the two equations, the comparisons for shared edges cancel, and what remains is
\[
\begin{aligned}
0&=\sum_{e,f}z_ey_f\,I(e,f)\\
&\quad+\frac12\sum_v\sum_{e,f}z_ey_f\,\sigma_v(e)\sigma_v(f)\,T_v(e,f)\\
&=J(z,y). \qquad\square
\end{aligned}
\]

**Remark 4.1.** The proof does not use condition 3 of normal drawings: Theorem 1.3 holds for polygonal drawings that are straight near vertices and crossing points, also when adjacent edges cross. The absence of adjacent crossings enters only later, where it makes \(J(e,f)\) for adjacent edges equal to the local term alone.

## 5. Exercises

**5.1.** Draw \(K_4\) with vertices \(1=(0,0)\), \(2=(2,0)\), \(3=(1,2)\), \(4=(1,0.7)\) and straight edges oriented from the smaller to the larger label, with the cut at each vertex pointing straight down. Compute the local terms of \(J(z,y)\) for the triangles \(z=1\to2\to3\to1\) and \(y=1\to2\to4\to1\), and check Theorem 1.3.

**5.2.** Do the same for the drawing with vertices at \((0,0),(2,0),(2,2),(0,2)\), where the diagonals cross.

**5.3.** Show directly from Definition 1.2 that \(J(z,y)\) for cycles \(z,y\) does not depend on the cuts. (Moving the cut at \(v\) past the spoke of \(g\) changes \(T_v(g,f)\) for all \(f\ne g\) at \(v\); use that \(\sum_f\sigma_v(f)y_f=0\) for a cycle \(y\).)

**5.4.** Let \(z\) and \(y\) be the signed edge vectors of two simple cycles with no common vertex. Show that \(\sum_{e,f}z_ey_fI(e,f)=0\), and interpret this as a statement about two disjoint closed curves.

## 6. Solutions

**5.1.** There are no crossings, so \(J(z,y)\) is the sum of the local terms at the common vertices \(1\) and \(2\). At \(1\) all edges point out; their directions have angles \(0^\circ\) for \(12\), about \(35^\circ\) for \(14\) and about \(63^\circ\) for \(13\), so the order from the cut is \(12,14,13\). With \(z_{12}=1,z_{13}=-1\) and \(y_{12}=1,y_{14}=-1\), the products \(z_ey_fT(e,f)\) for \((e,f)=(12,14),(13,12),(13,14)\) are \(-1,1,-1\), and the local term is \(\frac12(-1+1-1)=-\frac12\). At \(2\) the edge \(12\) points in (\(\sigma=-1\)) at angle \(180^\circ\), \(23\) out at about \(117^\circ\), \(24\) out at about \(145^\circ\); the order from the cut is \(23,24,12\); the products \(z_ey_f\sigma\sigma T\) for \((e,f)=(12,24),(23,12),(23,24)\) are \(1,-1,1\), and the local term is \(\frac12\). The sum is \(0\).

**5.2.** The diagonals \(13\) and \(24\) cross at \((1,1)\) with directions \((1,1)\) and \((-1,1)\), so \(I(13,24)=+1\), and the crossing contributes \(z_{13}y_{24}I(13,24)=(-1)(1)(1)=-1\). At \(1\) the order is \(12,13,14\) and the local term is \(\frac12(-1+1+1)=\frac12\); at \(2\) the order is \(23,24,12\) and the local term is \(\frac12(1-1+1)=\frac12\). The sum is \(0\).

**5.3.** Moving the cut past the spoke of \(g\) changes \(T_v(g,f)\) from \(-1\) to \(1\) and \(T_v(f,g)\) from \(1\) to \(-1\) for all \(f\ne g\) at \(v\), or the reverse. The change of \(J(z,y)\) is \(\pm\sigma_v(g)\) times
\[
z_g\sum_{f\ne g}\sigma_v(f)y_f-y_g\sum_{f\ne g}\sigma_v(f)z_f .
\] For a cycle \(y\), the coefficient of \(v\) in \(\partial y\) is \(-\sum_f\sigma_v(f)y_f=0\), so \(\sum_{f\ne g}\sigma_v(f)y_f=-\sigma_v(g)y_g\), and the change is \(\pm\sigma_v(g)^2\bigl(-z_gy_g+y_gz_g\bigr)=0\).

**5.4.** Without common vertices there are no local terms, so the sum equals \(J(z,y)=0\). The cycles are drawn as two closed curves that do not meet at vertices; the sum counts their crossings with signs, and Lemma 2.2 (after Step 1 of the proof of Theorem 1.3) says that it is zero.

## References

- [OpenAI-B] OpenAI, *The crossing number of complete bipartite graphs*, OpenAI Math Release preprint, 23 September 2026, Section 3, Lemma 3.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026
- [OpenAI-C] OpenAI, *The crossing number of complete graphs*, OpenAI Math Release preprint, 23 September 2026, Section 2, Lemma 2.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026
