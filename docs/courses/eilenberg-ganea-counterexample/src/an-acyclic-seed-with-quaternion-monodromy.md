# An acyclic seed with quaternion monodromy

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group of the counterexample is built from a finite flag complex \(L\) with two properties that pull in opposite directions: \(L\) is acyclic, so that the level complex of [The level complex and its acyclicity](the-level-complex-and-its-acyclicity.md) is acyclic and the group has cohomological dimension two, and the fundamental group of \(L\) has a nontrivial homomorphism into the unit quaternions, which the last lesson turns into a labelling of the level complex with small labels and nontrivial holonomy [OpenAI-EG, Lemma 4.1]. This lesson constructs \(L\) as a flag triangulation of the presentation complex of
\[
\begin{aligned}
\langle x,y\mid{}&x^2=y^5,\\
&x^2=(xy^{-1})^3\rangle .
\end{aligned}\tag{0.1}
\]

- The presentation complex and its homology (Section 1).
- A representation in the unit quaternions (Section 2).
- A flag triangulation (Section 3).

We use: the unit quaternions \(H\) of [Word maps on unit quaternions and degree](word-maps-on-unit-quaternions-and-degree.md), Section 1; and the facts (PI1) on fundamental groups and (CELL) on cellular homology stated in [Cone pictures and asphericity](course:torsion-free-group-algebra-with-zero-divisors/cone-pictures-and-asphericity), Section 2. The following standard fact is used without proof; a course proving it is recorded as an open obligation of this course.

**(BARY)** (subdivision of regular complexes; [Hatcher, Section 2.1, on \(\Delta\)-complexes and barycentric subdivision]). Let \(K\) be a finite CW complex of dimension two whose cells are points, edges and triangles, such that the closure of every cell is embedded and is the union of cells, every edge has two distinct end points, and every triangle has three distinct vertices and three distinct edges in its boundary. Then the order complex of the poset of its cells, ordered by inclusion of closures, is a simplicial complex whose realization is homeomorphic to \(K\), by a homeomorphism that sends the vertex of a cell to a point of that cell and each chain of cells into the closure of its largest cell.

## 1. The presentation complex and its homology

Let \(K\) be the presentation complex of (0.1): one vertex, two edge loops \(x\) and \(y\), and two \(2\)-cells attached along the closed edge paths
\[
r_1=x^2y^{-5},\qquad r_2=x^2(xy^{-1})^{-3}.
\]

**Lemma 1.1** (acyclicity). \(K\) is acyclic: \(\widetilde H_*(K;\mathbb Z)=0\).

*Proof.* By (CELL 1), the homology of \(K\) is that of \(0\to\mathbb Z^2\xrightarrow{d_2}\mathbb Z^2\xrightarrow{d_1}\mathbb Z\to0\), where \(d_1=0\) since both edges are loops, and \(d_2\) sends each \(2\)-cell to the exponent sums of its attaching word in \(x\) and \(y\): \(r_1\mapsto(2,-5)\) and \(r_2\mapsto(2-3,\,3)=(-1,3)\). The determinant of \(\begin{pmatrix}2&-5\\-1&3\end{pmatrix}\) is \(1\), so \(d_2\) is an isomorphism, \(H_2=\ker d_2=0\), \(H_1=\mathbb Z^2/\operatorname{im}d_2=0\), and \(\widetilde H_0=0\) since \(K\) is connected. \(\square\)

By (PI1), \(\pi_1(K)\) is the group (0.1). With \(a=y\) and \(b=y^{-1}x\) it is the group \(\langle a,b\mid a^5=b^3=(ab)^2\rangle\) of [Hatcher, Example 2.38], the binary icosahedral group of order \(120\): indeed \(ab=x\), \(x^2=y^5\) is central since it commutes with \(x\) and with \(y\), and \((xy^{-1})^3=x(y^{-1}x)^3x^{-1}\), so \((xy^{-1})^3=x^2\) is equivalent to \(b^3=(y^{-1}x)^3=x^{-1}x^2x=x^2\). Hatcher shows that \(K\) is acyclic but not contractible through a surjection of this group onto the rotation group of the dodecahedron [Hatcher, Example 2.38]; the course needs the following homomorphism into \(H\), which is a lift of that rotation representation.

## 2. A representation in the unit quaternions

For imaginary quaternions \(u,v\) write \(u\cdot v\) for the Euclidean inner product in \(\operatorname{Im}\mathbb H=\mathbb R^3\) and \(u\times v\) for the cross product, so that \(uv=-u\cdot v+u\times v\). An imaginary unit quaternion \(v\) satisfies \(v^2=-1\), and therefore, as for complex numbers,
\[
\begin{aligned}
&(\cos\theta+v\sin\theta)^n\\
&\quad=\cos n\theta+v\sin n\theta\\
&\qquad(n\in\mathbb Z).
\end{aligned}\tag{2.1}
\]

**Lemma 2.1** (the seed representation; [OpenAI-EG, Lemma 4.1]). Let \(\theta=\pi/5\), and let \(u,v\) be imaginary unit quaternions with
\[
u\cdot v=\frac1{2\sin\theta};\tag{2.2}
\]
they exist, since \(\sin(\pi/5)>\sin(\pi/6)=\frac12\). Then \(x\mapsto u\), \(y\mapsto\cos\theta+v\sin\theta\) defines a homomorphism \(\alpha\colon\pi_1(K)\to H\), and \(\alpha\) is not trivial.

*Proof.* By (2.1), \(\alpha(y)^5=\cos\pi+v\sin\pi=-1\), and \(u^2=-1\); so \(\alpha(x)^2=\alpha(y)^5\). Next, \(\alpha(xy^{-1})=u(\cos\theta-v\sin\theta)=w\), a unit quaternion with real part
\[
\begin{aligned}
\operatorname{Re}w&=-\sin\theta\,\operatorname{Re}(uv)\\
&=\sin\theta\,(u\cdot v)=\tfrac12 .
\end{aligned}
\]
So \(w=\cos(\pi/3)+n\sin(\pi/3)\) for an imaginary unit quaternion \(n\), and \(w^3=\cos\pi+n\sin\pi=-1\) by (2.1). Hence \(\alpha(x)^2=-1=w^3\), and both relations of (0.1) hold. Finally \(\alpha(x)=u\ne1\). \(\square\)

For example, \(u=i\) and \(v=\cos\varphi\,i+\sin\varphi\,j\) with \(\cos\varphi=1/(2\sin(\pi/5))\approx0.8507\).

## 3. A flag triangulation

**Lemma 3.1** (the seed; [OpenAI-EG, Lemma 4.1]). There is a finite connected flag simplicial complex \(L\) of dimension two with \(\widetilde H_*(L;\mathbb Z)=0\) and a nontrivial homomorphism \(\alpha\colon\pi_1(L)\to H\).

*Proof.* *A regular cell structure.* Subdivide each of the two circles of the \(1\)-skeleton of \(K\) into three edges; the result is a graph \(\Gamma_0\) with five vertices, the base point and two further vertices on each circle, and six edges, each with two distinct end points, no two edges with the same pair of end points. The attaching words \(r_1\) and \(r_2\) become closed edge paths in \(\Gamma_0\), of lengths \(3\cdot7=21\) and \(3\cdot(2+6)=24\). Each \(2\)-cell of \(K\) is a polygon whose boundary is attached along such a path. Cone the boundary of each polygon from a new interior point, before the identifications, keeping a separate *radial* edge for each occurrence of a vertex on the boundary of the polygon, even when two occurrences are the same vertex of \(\Gamma_0\). This decomposes \(K\) into the vertices of \(\Gamma_0\) and the two cone points, the edges of \(\Gamma_0\) and the \(21+24\) radial edges, and \(21+24\) triangles, each triangle bounded by one edge of \(\Gamma_0\) and two radial edges. Every triangle has three distinct vertices: a cone point and the two distinct end points of an edge of \(\Gamma_0\). Its three boundary edges are distinct: the outer edge lies in \(\Gamma_0\), and the two radial edges belong to different occurrences. The closure of every cell is embedded, as its vertices and boundary edges are distinct and the open cells are embedded. So this cell structure satisfies the hypotheses of (BARY).

*The order complex.* Let \(L\) be the order complex of the poset of these cells. By (BARY) it is a finite simplicial complex homeomorphic to \(K\), of dimension two. It is flag: a set of cells that are pairwise comparable is a chain, so a set of vertices of \(L\) that are pairwise joined by edges spans a simplex.

For the subdivision just described, \(L\) has \(7+51+45=103\) vertices, one for each cell, \(2\cdot51+3\cdot45+3\cdot45=372\) edges, one for each pair of a cell and a face of it, and \(45\cdot3\cdot2=270\) triangles, one for each chain of a vertex, an edge and a triangle; its Euler characteristic is \(103-372+270=1\), as it must be for an acyclic complex.

*Homology and the representation.* Homology and fundamental group are invariant under homeomorphisms, so \(L\) is acyclic by Lemma 1.1, and composing the isomorphism \(\pi_1(L)\cong\pi_1(K)\) with the homomorphism of Lemma 2.1 gives a nontrivial homomorphism \(\pi_1(L)\to H\). \(\square\)

The flag condition is what makes the right-angled Artin group of \(L\) see the simplices of \(L\): its cliques are exactly the vertex sets of simplices, as used in [The level complex and its acyclicity](the-level-complex-and-its-acyclicity.md). From now on \(L\) and \(\alpha\) are fixed. Any finite acyclic flag complex of dimension two whose fundamental group has a nontrivial homomorphism into \(H\) would serve equally well in the rest of the course.

## 4. Exercises

**4.1** (easy). Verify (2.1) by induction on \(n\ge0\) and extend it to negative \(n\).

**4.2** (easy). Show that the presentation complex of \(\langle x\mid x^2\rangle\) is not acyclic, by computing its homology.

**4.3** (medium). Show that the homomorphism \(\alpha\) of Lemma 2.1 sends the central element \(x^2\) to \(-1\), and deduce that \(\alpha\) does not factor through Hatcher's surjection of \(\pi_1(K)\) onto the rotation group of the dodecahedron. Where does the course use that the values lie in \(H\)?

**4.4** (medium). Compute numerically, for \(u=i\) and \(v=\cos\varphi\,i+\sin\varphi\,j\) with \(\cos\varphi=1/(2\sin(\pi/5))\), the quaternion \(w=u(\cos\theta-v\sin\theta)\), and check that \(w^3=-1\).

## 5. Solutions

**4.1.** For \(n=0\) both sides are \(1\). If it holds for \(n\), then \((\cos\theta+v\sin\theta)^{n+1}=(\cos n\theta+v\sin n\theta)(\cos\theta+v\sin\theta)=\cos n\theta\cos\theta+v^2\sin n\theta\sin\theta+v(\sin n\theta\cos\theta+\cos n\theta\sin\theta)\), which is \(\cos(n+1)\theta+v\sin(n+1)\theta\) since \(v^2=-1\). The inverse of \(\cos\theta+v\sin\theta\) is its conjugate \(\cos\theta-v\sin\theta=\cos(-\theta)+v\sin(-\theta)\), which gives negative \(n\).

**4.2.** One vertex, one loop \(x\) and one \(2\)-cell with \(d_2=2\colon\mathbb Z\to\mathbb Z\). So \(H_1=\mathbb Z/2\ne0\).

**4.3.** \(\alpha(x^2)=u^2=-1\). Hatcher's surjection \(\rho\) sends \(a\) and \(b\) to rotations with \(\rho(ab)^2=1\), so \(\rho(x^2)=\rho(ab)^2=1\). If \(\alpha=\beta\circ\rho\) for a homomorphism \(\beta\) from the rotation group, then \(\alpha(x^2)=\beta(1)=1\), a contradiction. The values in \(H\) are used twice: the comparison theorem is proved for labels in \(H\), with the degree theory of [Word maps on unit quaternions and degree](word-maps-on-unit-quaternions-and-degree.md), and the transport of [Small transport and the counterexample](small-transport-and-the-counterexample.md) extends a map over the \(2\)-cells of the universal cover of \(L\) using that \(H\) is simply connected.

**4.4.** \(\sin\theta\approx0.5878\), \(\cos\theta\approx0.8090\), \(\cos\varphi\approx0.8507\), \(\sin\varphi\approx0.5257\). Then \(v\sin\theta\approx0.5000\,i+0.3090\,j\), \(\cos\theta-v\sin\theta\approx0.8090-0.5000\,i-0.3090\,j\), and \(w=i(0.8090-0.5000i-0.3090j)\approx0.5000+0.8090\,i-0.3090\,k\), using \(i^2=-1\) and \(ij=k\). Its real part is \(\frac12\) and its norm is \(1\); with \(w=\frac12+\frac{\sqrt3}2n\), \(w^3=-1\).

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Lemma 4.1. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page, Example 2.38. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
