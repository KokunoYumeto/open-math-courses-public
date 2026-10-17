# Halving lines and rank sweeps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(P\) be a set of \(n\) points in the plane, \(n\) even, with no three on a line. A pair of points of \(P\) is a *halving pair* if the line through them has exactly \((n-2)/2\) points of \(P\) on each side. Let \(h(P)\) be the number of halving pairs. How large can \(h(P)\) be? Erdős, Lovász, Simmons and Straus proved \(h(P)=O(n^{3/2})\) and constructed sets with at least \(cn\log n\) halving pairs [ELSS]. Dey improved the upper bound to \(O(n^{4/3})\) in 1998, with an argument through convex chains and the crossing inequality; an exposition is [ORourke]. Later constructions raised the lower bound to \(n\exp(c\sqrt{\log n})\), still below every power \(n^{1+\delta}\); [OpenAI-HL, Section 1] gives references. This course proves the first improvement of the exponent \(4/3\), found by OpenAI [OpenAI-HL].

## The theorem

**Theorem A** (OpenAI). There are absolute constants \(\varepsilon>0\) and \(C\) such that every set \(P\) of \(n\) points in the plane, \(n\) even, with no three on a line, satisfies
\[
h(P)\le Cn^{4/3-\varepsilon}.
\]

The proof gives no numerical value of \(\varepsilon\) or \(C\): a limit argument by contradiction produces a constant, and an induction turns it into a power.

The lesson sets up the language of rank sweeps, in which halving pairs are the switches at the middle rank, and states the stronger Theorem B, uniform over all ranks, and Corollary C on \(k\)-sets.

**The course.**

1. This lesson: general position, rank sweeps, switches, and the statements.
2. [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md): activity, batches of exchanges, convex and concave chains, and the crossing inequality with designated endpoints.
3. [From packing to a power saving](from-packing-to-a-power-saving.md): the packing estimate and the induction that turns it into Theorems A and B.
4. [Measures on compact metric spaces](measures-on-compact-metric-spaces.md): weak limits, Hausdorff limits and conditional measures.
5. [Rank coordinates](rank-coordinates.md): smoothed ranks, which turn two time windows into a coordinate system of the plane.
6. [Limiting measures](limiting-measures.md): vertex, edge and crossing measures and their relations.
7. [Monotone functions of two variables](monotone-functions-of-two-variables.md): differentiability almost everywhere and critical images.
8. [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md).
9. [Three transverse foliations](three-transverse-foliations.md): a compactness theorem for maps preserving three families of parallel lines.
10. [The zoom at a rank point](the-zoom-at-a-rank-point.md).
11. [A spatial measure](a-spatial-measure.md): a limit position with disk mass \(O(r^{32/17})\).
12. [Boundary activity](boundary-activity.md): three strips, tokens, and the proof of the packing estimate.
13. [Levels and k-sets](levels-and-k-sets.md): duality, random sampling below a lower envelope, and Corollary C.

**What the course assumes.** Real analysis in one and several variables, from the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20); measure theory from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), whose results are cited by number where they are used; the Riesz representation theorem from the programme's lesson [Haar measure on locally compact groups](course:AN-01/prerequisites/riesz/positive-riesz) (Theorem 2.2); Brouwer's fixed-point theorem from the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) (Theorem 30.1); and the bound of \(3n-6\) edges for planar graphs from the core course [Applied Combinatorics](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C70) (Theorem 5.34). Everything else is proved in the lessons.

## 1. General position

Write \(p=(x,y)\) for points of the plane. For three points put
\[
\Delta(p,q,r)=\det(q-p,\;r-p),
\]
which is positive, negative or zero according as \(p,q,r\) turn counterclockwise, turn clockwise, or lie on a line. A point \(r\) lies on the left of the directed line from \(p\) to \(q\) exactly when \(\Delta(p,q,r)>0\).

A finite configuration \(P=(p_1,\dots,p_N)\) of distinct points is *generic* if:

- (G1) no three points lie on a line;
- (G2) the first coordinates \(x_i\) are distinct;
- (G3) the slopes of the \(\binom N2\) segments \(p_ip_j\) are distinct;
- (G4) no point where two of these segments cross in their interiors lies on a third of them.

**Lemma 1.1** (perturbation). Let \(P=(p_1,\dots,p_N)\) satisfy (G1), and let \(\delta>0\). There is a generic \(P'=(p_1',\dots,p_N')\) with \(|p_i'-p_i|<\delta\) for all \(i\) and
\[
\operatorname{sign}\Delta(p_i',p_j',p_m')=\operatorname{sign}\Delta(p_i,p_j,p_m)
\]
for all distinct \(i,j,m\). If the \(x_i\) are distinct, \(P'\) can be chosen with the same order of first coordinates.

*Proof.* View configurations as points of \(\mathbb R^{2N}\). Each \(\Delta(p_i,p_j,p_m)\) is a polynomial in the coordinates, nonzero at \(P\) by (G1), so its sign is constant on a neighbourhood \(U\) of \(P\); shrinking \(U\), its points also lie within \(\delta\) of \(P\) coordinatewise and keep the order of distinct first coordinates. A configuration in \(U\) fails (G2), (G3) or (G4) only if it is a zero of one of finitely many polynomials:

- \(x_i-x_j\) for (G2);
- \(\det\begin{pmatrix}y_i-y_j&x_i-x_j\\y_k-y_l&x_k-x_l\end{pmatrix}\), for distinct pairs \(\{i,j\}\ne\{k,l\}\), for (G3);
- for (G4), the determinant \(\det(L_{ij},L_{kl},L_{mn})\) of the coefficient rows of the three lines, where \(L_{ij}\) is the row \((y_i-y_j,\ x_j-x_i,\ x_iy_j-x_jy_i)\) and \(\{i,j\},\{k,l\}\) have four distinct indices and \(\{m,n\}\) is a third pair. If two segments cross at an interior point \(X\) lying on a third segment, the three lines pass through \(X\) and the determinant vanishes.

Each of these polynomials is nonzero, because it is nonzero at some configuration. For the first two this is immediate. For the determinant, take any configuration with no three points on a line. The lines \(p_ip_j\) and \(p_kp_l\) are distinct and meet in at most one point \(X\). If \(\{m,n\}\) contains an index outside \(\{i,j,k,l\}\), move that point off the line through \(X\) and the other point of the pair (or off any line through \(X\), if both indices are outside), keeping no three points on a line. If \(\{m,n\}\subset\{i,j,k,l\}\), say \(\{m,n\}=\{i,k\}\), the line \(p_ip_k\) meets \(p_ip_j\) only at \(p_i\), so it contains \(X\) only if \(X=p_i\), which would put \(p_i\) on the line \(p_kp_l\). In all cases the three lines are not concurrent, and they are not all parallel, so the determinant is nonzero.

By Lemma 3.1 of [Drawings and crossing numbers](course:crossing-numbers-of-complete-graphs/drawings-and-crossing-numbers), finitely many nonzero polynomials do not all have a zero at every point of the nonempty open set \(U\); more precisely their product is a nonzero polynomial, which does not vanish identically on \(U\). A point of \(U\) where the product is nonzero is the required \(P'\). \(\square\)

The point \(p_m\) lies on a given side of the line through \(p_i\) and \(p_j\) according to the sign of \(\Delta(p_i,p_j,p_m)\). So for \(P'\) as in the lemma, every line through two points has the same points on each side as for \(P\), and \(h(P')=h(P)\). It suffices to prove Theorem A for generic sets.

## 2. Rank sweeps

Fix a generic configuration \(P\) of \(N\) points. For a real number \(s\) put
\[
\varphi_s(x,y)=y-sx .
\]
Two points \(p_i,p_j\) have \(\varphi_s(p_i)=\varphi_s(p_j)\) exactly when \(s\) is the slope \(\sigma_{ij}\) of the segment \(p_ip_j\), by (G2). By (G3) the slopes of the segments are \(L=\binom N2\) distinct numbers
\[
\sigma_1<\sigma_2<\dots<\sigma_L .
\]
Choose numbers \(s_0<\sigma_1<s_1<\sigma_2<\dots<\sigma_L<s_L\), one in each of the \(L+1\) open intervals; they are the *states*. At a state the values \(\varphi_{s_t}(p_i)\) are distinct, and the points are ordered by increasing value. Moving from \(s_{t-1}\) to \(s_t\) is the \(t\)th *step*.

For \(0\le k\le N\), the *marked set* \(M_k(s)\) at a state \(s\) consists of the \(k\) points with the smallest values of \(\varphi_s\). The family \((M_k(s_t))_{t=0}^L\) is the *rank-\(k\) sweep* of \(P\). A step at which the marked set changes is a *switch*, and \(S_k(P)\) is the number of switches.

**Lemma 2.1.** Let \(\{p_i,p_j\}\) be the pair with slope \(\sigma_t\).

(a) The order at \(s_t\) arises from the order at \(s_{t-1}\) by exchanging \(p_i\) and \(p_j\), which are adjacent in both orders.

(b) The \(t\)th step is a switch of the rank-\(k\) sweep exactly when \(p_i\) and \(p_j\) occupy the positions \(k\) and \(k+1\); then one point leaves the marked set and the other enters.

(c) At a switch, the entering point has a larger first coordinate than the leaving point. Hence the sum of the first coordinates of the marked points increases strictly at every switch.

(d) Every pair is exchanged at exactly one step. In particular \(S_k(P)\le\binom N2\), and \(S_0(P)=S_N(P)=0\).

*Proof.* (a) The difference \(\varphi_s(p_a)-\varphi_s(p_b)\), which equals \((y_a-y_b)-s(x_a-x_b)\), is an affine function of \(s\) vanishing only at \(\sigma_{ab}\). So between \(s_{t-1}\) and \(s_t\) the pair \(\{p_i,p_j\}\) changes order and every other pair keeps it. If a point \(p_m\) lay strictly between \(p_i\) and \(p_j\) at \(s_{t-1}\), say \(p_i<p_m<p_j\), then at \(s_t\) still \(p_i<p_m<p_j\), against \(p_j<p_i\). So \(p_i\) and \(p_j\) are adjacent, and exchanging them gives the new order.

(b) The marked set consists of the first \(k\) points. By (a) it changes exactly when one of \(p_i,p_j\) is in position \(k\) and the other in position \(k+1\).

(c) Let \(u\) leave and \(v\) enter. Then \(\varphi_s(v)-\varphi_s(u)\) is positive at \(s_{t-1}\) and negative at \(s_t>s_{t-1}\), so its slope \(-(x_v-x_u)\) is negative: \(x_v>x_u\).

(d) The pair \(\{p_a,p_b\}\) is exchanged exactly at the step that crosses \(\sigma_{ab}\). At ranks \(0\) and \(N\) the marked set is empty or everything. \(\square\)

**Lemma 2.2** (halving pairs are middle switches). Let \(N=2m\). A pair \(\{p_i,p_j\}\) of a generic configuration is halving exactly when the step crossing \(\sigma_{ij}\) is a switch of the rank-\(m\) sweep. Hence \(h(P)=S_m(P)\).

*Proof.* Let \(\sigma=\sigma_{ij}\) be crossed at the \(t\)th step. A point \(p_a\notin\{p_i,p_j\}\) lies below the line through \(p_i\) and \(p_j\) exactly when \(\varphi_\sigma(p_a)<\varphi_\sigma(p_i)\), and above it when \(\varphi_\sigma(p_a)>\varphi_\sigma(p_i)\). These comparisons are the same at \(s_{t-1}\), since only the pair \(\{p_i,p_j\}\) changes order between \(s_{t-1}\) and \(\sigma\). So the number of points below the line equals the number of points before the adjacent pair \(p_i,p_j\) at \(s_{t-1}\). The pair is halving exactly when \(m-1\) points precede it, that is, when it occupies positions \(m\) and \(m+1\), which by Lemma 2.1(b) is a switch at rank \(m\). \(\square\)

## 3. The statements

By Lemmas 1.1 and 2.2, Theorem A follows from the case \(k=N/2\) of the following theorem.

**Theorem B** (OpenAI; uniform over ranks). There are absolute constants \(\varepsilon>0\) and \(C\) such that for every \(N\ge1\), every generic configuration \(P\) of \(N\) points and every \(0\le k\le N\),
\[
S_k(P)\le CN^{4/3-\varepsilon}.
\]

The uniformity in \(k\) is not a luxury. The induction in [From packing to a power saving](from-packing-to-a-power-saving.md) restricts a block of the sweep to the points that change membership in it, and the restricted sweep has a different rank.

A *\(k\)-set* of a finite set \(Q\) is a subset of \(k\) points that can be separated from the other points by a line containing no point of \(Q\). The last lesson deduces the following bound, which improves Dey's \(O(n(k+1)^{1/3})\).

**Corollary C** (OpenAI). There are absolute constants \(\varepsilon_0>0\) and \(C_0\) such that for every \(n\ge2\) and \(1\le k\le n/2\), every set of \(n\) points in the plane with no three on a line has at most \(C_0n(k+1)^{1/3-\varepsilon_0}\) subsets that are \(k\)-sets.

**The shape of the proof.** Lessons 2 and 3 reduce Theorem B to a *packing estimate*: for a sweep of \(N\) points, any family of step-disjoint intervals in each of which at least \(b\) points change membership has \(o((N/b)^{4/3})\) members as \(N/b\to\infty\). The classical argument gives \(O((N/b)^{4/3})\). Lessons 5 to 12 prove the improvement by contradiction: a sequence of configurations attaining \((N/b)^{4/3}\) up to constants is turned, through smoothed rank functions and weak limits of measures, into a limiting picture in which the activity concentrates on a set of large dimension and must cross the boundary of a fixed region too often.

## 4. Exercises

**4.1** (easy). Let \(n\) points be in convex position, \(n\) even. Show that there are exactly \(n/2\) halving pairs.

**4.2** (easy). Show that \(S_1(P)\) is one less than the number of vertices of the lower convex hull of a generic \(P\), that is, of the points \(p\) for which some line through \(p\) has all other points strictly above it.

**4.3** (medium). Let \(P'\) be the reflection of a generic \(P\) in the first axis, \((x,y)\mapsto(x,-y)\). Show that \(P'\) is generic and that \(S_k(P')=S_{N-k}(P)\).

**4.4** (medium). Show that the six points \((-2,-6),(-4,2),(3,0)\) and \((-1,-3),(1,-1),(-3,1)\) form a generic configuration with \(h(P)=6\), twice the value for six points in convex position.

## 5. Solutions

**4.1.** Order the points along the boundary of their convex hull. The line through two of them leaves on its two sides the two arcs of points between them. It is halving exactly when both arcs have \((n-2)/2\) points, so each point has exactly one halving partner, the opposite one, and the \(n\) points form \(n/2\) halving pairs.

**4.2.** The point with the smallest value of \(\varphi_s\) is the lowest point in the direction perpendicular to lines of slope \(s\): the line of slope \(s\) through it has all other points above it. As \(s\) increases from \(-\infty\) to \(+\infty\), this point moves from the leftmost to the rightmost vertex of the lower hull, visiting each vertex once, by Lemma 2.1(c). Each change is a switch at rank \(1\).

**4.3.** Reflection preserves (G1)–(G4) and changes every slope \(\sigma\) into \(-\sigma\). For \(P'\), \(\varphi_s(x,-y)=-(y+sx)=-\varphi_{-s}(x,y)\). So the \(k\) smallest values for \(P'\) at slope \(s\) belong to the \(k\) largest points of \(P\) at slope \(-s\), the complement of \(M_{N-k}(-s)\). As \(s\) increases, \(-s\) decreases, and the switches correspond one to one.

**4.4.** The first coordinates \(-4,-3,-2,-1,1,3\) are distinct, and a computation of the \(20\) determinants \(\Delta\), the \(15\) slopes and the crossing points of pairs of segments shows (G1), (G3) and (G4). The first three points span a triangle containing the other three. Of the \(15\) lines, six have two points on each side: the three lines through two inner points, for example the line through \((1,-1)\) and \((-3,1)\), with \((-2,-6),(-1,-3)\) on one side and \((-4,2),(3,0)\) on the other; and the three lines \((-2,-6)(-1,-3)\), \((-4,2)(-3,1)\) and \((3,0)(1,-1)\) joining an outer vertex to an inner point. Each of the other nine lines has at most one point on one of its sides.

## References

- [ELSS] P. Erdős, L. Lovász, A. Simmons and E. G. Straus, *Dissection graphs of planar point sets*, in *A Survey of Combinatorial Theory*, North-Holland, Amsterdam, 1973, 139–149. https://users.renyi.hu/~p_erdos/1973-07.pdf
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
- [ORourke] J. O'Rourke, *Computational Geometry Column 32*, arXiv:cs/9810021 (1998). https://arxiv.org/abs/cs/9810021
