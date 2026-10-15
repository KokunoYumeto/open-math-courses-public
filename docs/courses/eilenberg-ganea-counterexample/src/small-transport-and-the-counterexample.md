# Small transport and the counterexample

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the second statement of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md), Section 4, and with it the last step of the proof of its Theorem 4.1: the group \(G\) has cohomological dimension two and geometric dimension three [OpenAI-EG, Section 5 and the conclusion].

**Proposition 4.1** (small transport with nontrivial holonomy; [OpenAI-EG, Proposition 5.1]). For every \(\epsilon>0\) the oriented edges \(e\) of the level complex \(X\) admit labels \(h_e\in H\) with \(h_{\bar e}=h_e^{-1}\) for the reversed edge \(\bar e\) and \(|h_e-1|<\epsilon\), such that the product of the labels around every triangle of \(X\) is \(1\), and the product around some closed edge path of \(X\) is not \(1\).

For labels in an abelian group this would be impossible: products along closed paths would factor through \(H_1(X;\mathbb Z)=0\). The labels are obtained by pulling back, along a map of the graph of \(X\) into \(L\) that moves little along every edge, the parallel transport of a flat bundle over \(L\) whose holonomy is the representation \(\alpha\) of [An acyclic seed with quaternion monodromy](an-acyclic-seed-with-quaternion-monodromy.md). The map is built from the direction vectors of [Traces and direction vectors](traces-and-direction-vectors.md), evaluated far from the identity, where they vary slowly, and it maps certain long paths of \(X\) exactly onto edges of \(L\), so that the loops of \(L\) detected by \(\alpha\) are traced.

- A slowly varying map of the level graph (Section 1).
- Commuting-power paths (Section 2).
- A developing map (Section 3).
- Pulling back transport (Section 4).
- The counterexample (Section 5).

Throughout, \(L\) and \(\alpha\colon\pi_1(L)\to H\) are those of Lemma 3.1 of [An acyclic seed with quaternion monodromy](an-acyclic-seed-with-quaternion-monodromy.md), \(P=A_L\), \(\lambda\colon P\to\mathbb Z\) the height, \(G=\ker\lambda\), and \(X\) the level complex of [The level complex and its acyclicity](the-level-complex-and-its-acyclicity.md), with the cells described in its Lemma 4.2; \(|L|\subseteq\mathbb R^V\) carries the \(\ell^1\) metric, and \(b\) is the direction vector of [Traces and direction vectors](traces-and-direction-vectors.md). We use the facts (PI1) and (COV) stated in [Cone pictures and asphericity](course:torsion-free-group-algebra-with-zero-divisors/cone-pictures-and-asphericity), Section 2, the Lebesgue number lemma for compact metric spaces from the core course [Point-Set Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90), and the following standard facts, used without proof; a course proving them is recorded as an open obligation of this course.

**(SC)** (spheres and covering maps; [Hatcher, Proposition 1.14 and Section 1.3]).

1. The group \(H\), the three-sphere, is simply connected.
2. The universal cover \(p\colon\widetilde L\to L\) is a covering map: every point of \(L\) has an open neighbourhood \(U\) whose preimage is a disjoint union of open sets, the *sheets*, each mapped homeomorphically onto \(U\) by \(p\); the deck group permutes the sheets over \(U\) transitively. Paths in \(L\) lift uniquely from any point over their starting point, and a closed path in \(L\) representing \(\gamma\in\pi_1(L,q_0)\), lifted from a base point \(\xi_0\) over \(q_0\), ends at \(\gamma\xi_0\) for the deck action, suitably normalized.

## 1. A slowly varying map of the level graph

Fix \(N\ge2\) and an element \(d\in P\) with \(\lambda(d)=N\), for example \(d=a_v^N\). For a vertex \(g\in G\) of \(X\) put
\[
f_N(g)=b(d^{-1}g)\in|L| .\tag{1.1}
\]
It is defined, since \(\lambda(d^{-1}g)=-N\ne0\) (Exercise 4.4 of the lesson on traces), and \(|d^{-1}g|_P\ge N\).

By Lemma 4.2 of the lesson on the level complex, every edge of \(X\) is the level diagonal \(\{ka_q,ka_r\}\) of a square \(\chi_{k,\{q,r\}}\) of \(E\) with \(\lambda(k)=-1\). Its corners have heights \(-1,0,0,1\); write \(g=ka_q\), \(h=ka_r\) and \(u=ka_qa_r\) for the corner of height \(1\), so that \(u=ga_r=ha_q\). The translates \(d^{-1}g\), \(d^{-1}u\), \(d^{-1}h\) have heights \(-N\), \(1-N\), \(-N\), so word lengths at least \(N\), \(N-1\), \(N\), and consecutive ones differ by a generator, \(d^{-1}u=d^{-1}g\,a_r=d^{-1}h\,a_q\). By Lemma 2.2 of the lesson on traces, the word lengths in each of the two steps differ by \(1\), so the larger one is at least \(N\). By Lemma 3.1 there,
\[
\begin{aligned}
&\|b(d^{-1}g)-b(d^{-1}u)\|_1\\
&\qquad\le\frac2N,\\
&\|b(d^{-1}u)-b(d^{-1}h)\|_1\\
&\qquad\le\frac2N,
\end{aligned}\tag{1.2}
\]
and each of the two pairs lies in a common simplex of \(L\), so the straight segments joining them lie in \(|L|\).

Extend \(f_N\) over the oriented edge from \(g\) to \(h\) as the path that runs along the segment from \(f_N(g)\) to \(b(d^{-1}u)\) and then along the segment to \(f_N(h)\), parametrized proportionally, with one exception: if \(f_N(g)\) and \(f_N(h)\) lie in a common simplex of \(L\), use the single segment from \(f_N(g)\) to \(f_N(h)\). This segment is well defined, since in barycentric coordinates it is the segment of \(\mathbb R^V\), and it lies in every simplex containing both end points. Use the reversed path for the reversed edge. The corner \(u\) is determined by the edge, so this defines a continuous map
\[
f_N\colon X^{(1)}\to|L|
\]
on the \(1\)-skeleton of \(X\), a CW complex.

**Lemma 1.1** (small images). The image of every edge has \(\ell^1\)-diameter at most \(4/N\), and the image of the boundary of every triangle of \(X\) has diameter at most \(8/N\).

*Proof.* By (1.2) and the triangle inequality, every point of an edge image is within \(4/N\) of every other: the two segments have lengths at most \(2/N\) each, and the single segment, when used, joins points at distance at most \(4/N\). The three edge images of a triangle pairwise meet at the images of common vertices, so two points of the boundary image are at distance at most \(4/N+4/N\). \(\square\)

## 2. Commuting-power paths

**Lemma 2.1** (commuting-power paths; [OpenAI-EG, Section 5.2]). Let \(\{q,r\}\) be an edge of \(L\), and put
\[
\begin{gathered}
p_j=d\,a_q^{-(N-j)}a_r^{-j}\\
(0\le j\le N).
\end{gathered}\tag{2.1}
\]
These are vertices of \(X\), consecutive ones are joined by an edge of \(X\), and \(f_N\) maps the edge path \(p_0,p_1,\ldots,p_N\) onto the edge \([q,r]\) of \(|L|\), the vertex \(p_j\) to the point \(\bigl(1-\frac jN\bigr)e_q+\frac jNe_r\) and each edge onto the segment between consecutive such points.

*Proof.* \(\lambda(p_j)=N-(N-j)-j=0\), so \(p_j\in G\). Since \(a_q\) and \(a_r\) commute, \(p_{j+1}=p_ja_qa_r^{-1}\). For \(k=p_ja_r^{-1}\), of height \(-1\), the square \(\chi_{k,\{q,r\}}\) has the level diagonal \(\{ka_q,ka_r\}=\{p_{j+1},p_j\}\), an edge of \(X\). By Example 3.2 of the lesson on traces, \(f_N(p_j)=b(a_q^{-(N-j)}a_r^{-j})=\bigl(1-\frac jN\bigr)e_q+\frac jNe_r\). Consecutive points lie in the simplex \(\{q,r\}\), so by the convention of Section 1 each edge \(\{p_j,p_{j+1}\}\) is mapped onto the single segment between them. \(\square\)

## 3. A developing map

Let \(p\colon\widetilde L\to L\) be the universal cover, with base vertex \(q_0\) of \(L\) and \(\xi_0\) over it, and let \(\pi_1(L,q_0)\) act by deck transformations, normalized as in (SC 2). By (COV 1), \(\widetilde L\) is a CW complex whose cells are the lifts of the simplices of \(L\), permuted freely by the deck group.

**Lemma 3.1** (developing map). There is a continuous map \(D\colon\widetilde L\to H\) with
\[
\begin{gathered}
D(\gamma\xi)=\alpha(\gamma)\,D(\xi)\\
(\gamma\in\pi_1(L,q_0),\ \xi\in\widetilde L).
\end{gathered}\tag{3.1}
\]

*Proof.* Choose one cell in each orbit of cells of \(\widetilde L\). Define \(D\) on the chosen vertices arbitrarily and extend to all vertices by (3.1); this is consistent, since the deck group acts freely. On a chosen edge, the values at its end points are already defined; join them by a path in \(H\), which is path connected, and extend to the other edges of the orbit by (3.1). On a chosen triangle, \(D\) is defined on its boundary circle; since \(H\) is simply connected (SC 1), the map on the circle extends over the triangle; extend to its orbit by (3.1). \(L\) has dimension two, so this defines \(D\) on all of \(\widetilde L\). It satisfies (3.1) by construction, since \(\alpha\) is a homomorphism, and it is continuous on every closed cell, hence continuous. \(\square\)

**Lemma 3.2** (a uniform cover). Let \(\epsilon>0\). There are a finite open cover \((U_i)\) of \(L\) by evenly covered sets and a number \(\ell>0\) such that \(D\) varies by less than \(\epsilon\) on every sheet over every \(U_i\), and every subset of \(L\) of diameter less than \(\ell\) lies in some \(U_i\).

*Proof.* Let \(x\in L\) and \(\tilde x\) a point over it. By (SC 2) and the continuity of \(D\) there is an evenly covered open \(U_x\ni x\) such that \(D\) varies by less than \(\epsilon\) on the sheet over \(U_x\) containing \(\tilde x\). The other sheets are its images under deck transformations \(\gamma\), on which \(D\) is \(\alpha(\gamma)D\) by (3.1), and left multiplication by a unit quaternion preserves distances; so \(D\) varies by less than \(\epsilon\) on every sheet over \(U_x\). The space \(L\) is compact, so finitely many \(U_x\) cover it, and the Lebesgue number lemma gives \(\ell\). \(\square\)

## 4. Pulling back transport

*Proof of Proposition 4.1.* Let \(\epsilon>0\), take \((U_i)\) and \(\ell\) as in Lemma 3.2, choose \(N\ge2\) with \(8/N<\ell\), and let \(f_N\) be the map of Section 1.

*Labels.* For an oriented edge \(e\) of \(X\), lift the path \(f_N(e)\) to \(\widetilde L\), from some \(\xi\) to \(\xi'\), and put
\[
h_e=D(\xi)^{-1}D(\xi').\tag{4.1}
\]
Another lift is the image of this one under a deck transformation \(\gamma\), which multiplies both values of \(D\) on the left by \(\alpha(\gamma)\), so \(h_e\) does not depend on the lift. The reversed path has the reversed lift, so \(h_{\bar e}=h_e^{-1}\). The path \(f_N(e)\) has diameter at most \(4/N<\ell\) (Lemma 1.1), so it lies in some \(U_i\), its lift stays in one sheet, and \(|h_e-1|=|D(\xi')-D(\xi)|<\epsilon\), by bi-invariance of the distance.

*Triangles.* Let \(\sigma\) be a triangle of \(X\) with boundary edges \(e_1,e_2,e_3\) traversed in order. By Lemma 1.1 the image \(f_N(\partial\sigma)\) has diameter at most \(8/N<\ell\), so it lies in some \(U_i\). Lift the three paths \(f_N(e_k)\) consecutively into one sheet over \(U_i\), by the inverse of the homeomorphism from the sheet to \(U_i\): the lifts run from \(\xi_1\) to \(\xi_2\), \(\xi_2\) to \(\xi_3\), and \(\xi_3\) back to \(\xi_1\). With these lifts in (4.1), the product of the three labels telescopes:
\[
\begin{aligned}
&h_{e_1}h_{e_2}h_{e_3}\\
&\quad=D(\xi_1)^{-1}D(\xi_2)\,D(\xi_2)^{-1}D(\xi_3)\\
&\qquad\cdot D(\xi_3)^{-1}D(\xi_1)=1 .
\end{aligned}
\]
For another starting edge or the opposite direction the product is a conjugate of this one or its inverse, hence also \(1\).

*A closed path with nontrivial product.* By (PI1), \(\pi_1(L,q_0)\) is generated by the classes of closed edge paths, so since \(\alpha\) is nontrivial there is a closed edge path \(q_0,q_1,\ldots,q_k=q_0\) of \(L\), consecutive vertices joined by edges of \(L\), whose class \(\gamma\) has \(\alpha(\gamma)\ne1\). For each \(i\), Lemma 2.1 for the edge \(\{q_i,q_{i+1}\}\) gives an edge path of \(X\) from \(da_{q_i}^{-N}\) to \(da_{q_{i+1}}^{-N}\), mapped by \(f_N\) onto the edge \([q_i,q_{i+1}]\), subdivided into \(N\) segments. Concatenating them gives a closed edge path \(c\) of \(X\) based at \(da_{q_0}^{-N}\), whose image under \(f_N\) is the chosen closed path of \(L\), with its edges subdivided. Lift this image from \(\xi_0\), segment after segment; by (SC 2) the lift ends at \(\gamma\xi_0\). The product of the labels along \(c\), computed with these consecutive lifts, telescopes to
\[
\begin{aligned}
D(\xi_0)^{-1}D(\gamma\xi_0)&=D(\xi_0)^{-1}\alpha(\gamma)D(\xi_0)\\
&\ne1 .
\end{aligned}
\]
This proves the proposition. \(\square\)

## 5. The counterexample

*Proof of Theorem 4.1 of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md).* Let \(L\) be the finite acyclic flag complex of dimension two of Lemma 3.1 of [An acyclic seed with quaternion monodromy](an-acyclic-seed-with-quaternion-monodromy.md), the flag triangulation of the presentation complex of (0.1) there, and \(G\) the kernel of the height homomorphism of \(A_L\). By Proposition 5.1 of [The level complex and its acyclicity](the-level-complex-and-its-acyclicity.md), \(G\) is finitely generated and residually finite, \(\operatorname{cd}G=2\), \(\operatorname{gd}G\le3\), and the finite alphabet \(S\) and the finite list \(\mathcal D\) of that proposition satisfy the hypotheses of the comparison theorem, Theorem 4.1 of [Finite quotients and the comparison theorem](finite-quotients-and-the-comparison-theorem.md); the \(1\)-skeleton of \(X\) is the generator graph of \(S\) over \(G\), and the triangles of \(X\) are the translates \(g\cdot z\) of the boundary paths of the words \(z\in\mathcal D\).

Suppose that \(G\) had a classifying space of dimension at most two, with any number of cells. The comparison theorem gives \(\eta>0\). Proposition 4.1, with \(\epsilon=\eta\), gives labels of the edges of the generator graph with \(|h_e-1|<\eta\), with product \(1\) along the path reading \(z\) from every \(g\in G\), since that path is the boundary of a triangle of \(X\), and with a product different from \(1\) along some closed edge path, that is, along some word of value \(1\) read from some vertex. This contradicts the conclusion of the comparison theorem. So \(\operatorname{gd}G\ge3\), and with \(\operatorname{gd}G\le3\), \(\operatorname{gd}G=3\), while \(\operatorname{cd}G=2\). \(\square\)

**What the course proves and what it assumes.** The lessons prove every step of the argument above, with these standard inputs from outside the programme, each stated where it is used and recorded as an open obligation: the facts (CW) on covering spaces and cellular chains (the first lesson); the degree properties (DEG) (the second lesson); the homotopy facts (HE) (the third lesson); (CUBE) on cube complexes (the seventh lesson); (SIMP) on simplicial and polyhedral complexes (the eighth lesson); (BARY) on subdivisions of regular complexes (the ninth lesson); and (SC) on spheres and covering maps (this lesson). The facts (PI1), (COV) and (CELL) are those stated, and also not proved, in the course on the torsion-free group algebra with zero divisors. The Hurewicz and Whitehead theorems, Sard's theorem, Tychonoff's theorem, the homotopy invariance of singular homology and the Lebesgue number lemma come from other courses of the programme.

## 6. Exercises

**6.1** (easy). Show that if all labels \(h_e\) of Proposition 4.1 lay in an abelian subgroup of \(H\), the product around every closed edge path would be \(1\). (Hint: products around closed paths then define a homomorphism from \(H_1\) of the graph to the subgroup that vanishes on the boundaries of triangles, and \(H_1(X)=0\).)

**6.2** (easy). In Lemma 2.1, compute the edge path for \(N=2\), and check that \(p_1\) is the common corner of height \(0\) of two squares of \(E\) used for the two edges.

**6.3** (medium). For an edge \(\{p_j,p_{j+1}\}\) of a commuting-power path, compute the corner \(u\) of height \(1\) and the direction vector \(b(d^{-1}u)\), and show that the two-segment path of Section 1 would also run monotonically along the edge \([q,r]\) from \(f_N(p_j)\) to \(f_N(p_{j+1})\).

**6.4** (medium). Why does the proof choose the triangle lifts in one sheet, instead of using arbitrary lifts of the three edge paths?

## 7. Solutions

**6.1.** If the labels lie in an abelian group \(A\), the products along paths define a homomorphism from the chains of the graph to \(A\), \(e\mapsto h_e\), the product along a path depending only on its chain. It vanishes on the boundaries of triangles, where the product is \(1\). Closed paths have cycles as chains, and every cycle of \(X\) is a combination of boundaries of triangles, since \(H_1(X)=0\). So every closed path has product \(1\).

**6.2.** \(p_0=da_q^{-2}\), \(p_1=da_q^{-1}a_r^{-1}\), \(p_2=da_r^{-2}\). The edge \(\{p_0,p_1\}\) is the level diagonal of the square at \(k=p_0a_r^{-1}\), with corners \(k,\ ka_q=p_1,\ ka_r=p_0,\ ka_qa_r\); the edge \(\{p_1,p_2\}\) is that of the square at \(p_1a_r^{-1}\). The vertex \(p_1\) is a corner of height \(0\) of both squares.

**6.3.** For the edge \(\{p_j,p_{j+1}\}\), \(0\le j\le N-1\), with \(k=p_ja_r^{-1}\), the corner of height \(1\) is \(u=ka_qa_r=p_ja_q\), and \(d^{-1}u=a_q^{-(N-j)}a_r^{-j}a_q=a_q^{-(N-j-1)}a_r^{-j}\), a reduced word of length \(N-1\ge1\). By Example 3.2 of the lesson on traces, with \(N-1\) in place of \(N\), \(b(d^{-1}u)=\frac{N-j-1}{N-1}e_q+\frac j{N-1}e_r\), a point of \([q,r]\). Its \(r\)-coordinate satisfies \(\frac jN\le\frac j{N-1}\le\frac{j+1}N\), the second inequality because \(j\le N-1\). So both segments lie on \([q,r]\), and the two-segment path runs monotonically from \(f_N(p_j)\) to \(f_N(p_{j+1})\); it has the same image as the single segment used by the convention.

**6.4.** The labels do not depend on the lifts, but the telescoping identity needs the end point of each lift to be the starting point of the next. Consecutive lifts in one sheet guarantee this and close up, because the sheet is mapped homeomorphically onto \(U_i\) and the boundary image is a closed path in \(U_i\). Lifts of a closed path in general need not close up: the lift of a closed path ends at a deck translate of its starting point.

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 5 and the completion of the proof. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
