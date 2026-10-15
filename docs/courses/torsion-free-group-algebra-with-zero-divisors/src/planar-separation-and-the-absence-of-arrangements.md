# Planar separation and the absence of arrangements

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The bounded-pattern estimate excludes systems of a bounded number of paths of total length comparable to \(L\). A reduced spherical arrangement, as defined in [Spherical arrangements and planar intervals](spherical-arrangements-and-planar-intervals.md), may have arbitrarily many disks of arbitrary total length. This lesson shows that every arrangement nevertheless contains an excluded bounded system, so that with high probability the random graph admits no arrangement at all [OpenAI-KZ, Section 4]. Long boundary paths are cut into pieces of length comparable to \(L\) and closed up cheaply. The pieces, joined by the pairing arcs, form a planar graph, and the planar separator theorem of Lipton and Tarjan deletes a small proportion of the pieces so that the rest falls into clusters of boundedly many pieces. A counting argument finds one cluster that is almost completely paired by few interval pairs. The proportion \(\varepsilon\) of the bounded-pattern estimate is fixed before the bounds on the number and lengths of the paths, so a single application of that estimate covers arrangements of every size.

- Recursive planar separation (Section 1).
- The parameters (Section 2).
- The absence of arrangements (Section 3).

We keep the random graph \(\Gamma\) conditioned on girth at least \(L=\lfloor c\log n\rfloor\), the constant \(D_0\) of the diameter lemma, Lemma 4.1 of [Random matchings with large girth](random-matchings-with-large-girth.md), and the bounded-pattern estimate, Proposition 1.2 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md), proved in [The bounded-pattern estimate](the-bounded-pattern-estimate.md), with its constant \(\varepsilon>0\). Systems, pairings, interval pairs and the reduction condition (1.1) are as in Definition 1.1 of that lesson. A closed cyclically immersed path of positive length in \(\Gamma\) contains a cycle, as in the proof of Lemma 3.1 there, so it has length at least \(L\).

## 1. Recursive planar separation

A *planar multigraph* is a multigraph drawn on a sphere, or equivalently in the plane, without crossings; loops and parallel edges are allowed. We use the following theorem without proof; a course proving it is recorded as an open obligation of this course.

**(SEP)** (planar separator theorem; [Lipton–Tarjan 1977, Corollary 2]). Let \(G\) be a planar graph with \(s\) vertices, without loops and parallel edges. The vertices of \(G\) can be partitioned into three sets \(A,B,C\) such that no edge joins a vertex of \(A\) to a vertex of \(B\), neither \(A\) nor \(B\) has more than \(2s/3\) vertices, and \(C\) has at most \(2\sqrt2\sqrt s\) vertices.

**Lemma 1.1** (recursive separation; [OpenAI-KZ, Lemma 4.4]). Put
\[
C_{\rm sep}=\frac{2\sqrt2}{1-\sqrt{2/3}} .
\]
For every integer \(K\ge1\), every planar multigraph with \(m\) vertices has a set of at most \(C_{\rm sep}m/\sqrt K\) vertices whose deletion leaves components of at most \(K\) vertices each.

*Proof.* Removing loops and merging parallel edges gives a planar graph without loops and parallel edges, with the same components after the deletion of any set of vertices. Process the components as follows: a component with \(s>K\) vertices is separated by (SEP), the set \(C\) is deleted, and the components of what remains, each inside \(A\) or inside \(B\) and so of at most \(2s/3\) vertices, are processed in the same way. Components of at most \(K\) vertices are left alone. Sizes decrease, so the procedure stops, and the remaining components have at most \(K\) vertices.

At the step on a component of \(s>K\) vertices, charge \(2\sqrt2/\sqrt s\) to each of its vertices. The total charge \(2\sqrt2\sqrt s\) of the step bounds the number of vertices deleted there. Fix a vertex and let \(s_1>s_2>\cdots>s_r>K\) be the sizes of the components containing it at the steps where it is charged. It survives each of these steps except possibly the last, so \(s_{i+1}\le\frac23s_i\), and \(s_{r-j}\ge(\frac32)^js_r>(\frac32)^jK\). Its total charge is therefore at most
\[
\frac{2\sqrt2}{\sqrt K}\sum_{j\ge0}\Bigl(\frac23\Bigr)^{j/2}=\frac{C_{\rm sep}}{\sqrt K}.
\]
Summing over the \(m\) vertices bounds the number of deleted vertices by \(C_{\rm sep}m/\sqrt K\). \(\square\)

## 2. The parameters

Fix the constant \(D\) of the short-closure lemma, Lemma 2.1 of [Spherical arrangements and planar intervals](spherical-arrangements-and-planar-intervals.md), and choose, in this order,
\[
\begin{aligned}
U&=\max\Bigl\{3,\Bigl\lceil\frac{96D}\varepsilon\Bigr\rceil\Bigr\},\\
\eta&=\min\Bigl\{\frac1{32U},\frac\varepsilon{64U}\Bigr\},\\
K&=\Bigl\lceil\Bigl(\frac{C_{\rm sep}}\eta\Bigr)^2\Bigr\rceil,\\
C&=K(U+D),\\
I&=\lceil192\,C\rceil .
\end{aligned}\tag{2.1}
\]
These choices give
\[
\begin{aligned}\frac{3D}U&\le\frac\varepsilon{32},\\ 2\eta U&\le\frac1{16},\\ 2\eta U&\le\frac\varepsilon{32},\end{aligned}\tag{2.2}
\]
and \(\sqrt K\ge C_{\rm sep}/\eta\). The order of dependence is
\[
\begin{aligned}&\text{types},\,c,\,\delta;\ \ \varepsilon,\,D_0;\ \ D;\ \ U;\\&\eta;\ \ K;\ \ C,\,I;\ \ n .\end{aligned}
\]
Everything before \(n\) is fixed before \(n\) tends to infinity. In particular the bounded-pattern estimate is applied to one fixed triple \((K,C,I)\). This is possible because \(\varepsilon\) does not depend on \(K,C,I\): Proposition 1.2 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md) chooses \(\varepsilon\) first.

## 3. The absence of arrangements

**Proposition 3.1** (absence of arrangements; [OpenAI-KZ, Proposition 4.5]). With probability tending to \(1\) as \(n\to\infty\), the graph \(\Gamma\) admits no reduced spherical arrangement. In particular, for all sufficiently large multiples \(n\) of \(2v^2\) there are graphs \(\Gamma\) with the prescribed types, of girth at least \(L\), whose components have diameter at most \(D_0L\), and which admit no reduced spherical arrangement.

*Proof.* By the diameter lemma, every component of \(\Gamma\) has diameter at most \(D_0L\) with probability tending to \(1\). By the bounded-pattern estimate for the fixed \(K,C,I\) of (2.1), with probability tending to \(1\) the graph \(\Gamma\) carries no system of at most \(K\) paths with total length \(L\le H\le CL\) and a pairing satisfying (1.1) with at most \(I\) interval pairs and at most \(\varepsilon H\) unpaired occurrences. We show that for all sufficiently large \(n\), if the diameters are at most \(D_0L\), every reduced spherical arrangement over \(\Gamma\) produces such a system. Then the probability that an arrangement exists tends to \(0\).

Let an arrangement have \(N\) boundaries of total length \(H_0\). It has a closed cyclically immersed boundary path, so \(H_0\ge L\).

*Splitting and closing long paths.* Keep every boundary path of length at most \(UL\). Divide a path of length \(h>UL\) into \(m=\lceil h/(UL)\rceil\) consecutive segments whose lengths differ by at most one, the exceptional path as a path from its start. Then \(m<h/(UL)+1<2h/(UL)\), so the average length \(h/m\) exceeds \(UL/2\); every segment has length at least \(h/m-1\ge UL/3\) for \(UL\ge6\), and at most \(UL\), because \(h/m\le UL\) and \(UL\) is an integer. A segment has no backtracking, and by the short-closure lemma it extends to a closed cyclically immersed path by a path of length at most \(DL\). Replace every segment by this closed path; its new occurrences, those of the closure, are unpaired. If the exceptional path was divided, no interval path remains; otherwise it remains as it is, starting at \(x_A\) or \(x_B\).

Call the resulting paths the *pieces*, \(N'\) of them. Each has length at most \((U+D)L\) and contains at most \(UL\) original occurrences. The closures add total length
\[
\begin{aligned}H_{\rm add}&\le\sum\frac{2h}{UL}\,DL\\&\le\frac{2D}U\,H_0\le\frac{3D}UH_0,\end{aligned}\tag{3.1}
\]
the sum running over the divided paths. Every piece contains at least \(L\) original occurrences, except possibly the undivided exceptional path: an undivided closed path has length at least \(L\) by the girth, and a segment has length at least \(UL/3\ge L\). Hence
\[
\begin{aligned}N&\le N',\\N'L&\le H_0+L\le2H_0.\end{aligned}\tag{3.2}
\]

Apply Lemma 4.1 of [Spherical arrangements and planar intervals](spherical-arrangements-and-planar-intervals.md) to this division of the boundary paths. It numbers the occurrences of every piece from a first occurrence, and describes the pairing of all original occurrences by at most \(6N'\) interval pairs, with each interval inside one piece. Read every closed piece from that first occurrence, so that the original segment comes first and its closure afterwards, and the undivided exceptional path from its start. Then every interval is an interval of the positions of its piece.

*Deleting a few pieces.* Form the *piece graph*: its vertices are the pieces, and every pairing arc gives an edge between the pieces containing its two ends. It is a planar multigraph. To draw it on the sphere of the arrangement, identify each disk with the unit disk. The pieces of its boundary path occupy consecutive angular intervals of the boundary circle, and in polar coordinates \((\theta,r)\), \(0<r\le1\), the sector over such an interval is a rectangle. Place the vertex of the piece in the middle of its rectangle at \(r=\frac12\), and join it by straight segments in these coordinates to the arc ends in its interval. Segments in one rectangle meet only at that vertex, different rectangles are disjoint, and the arcs lie outside the disks; so arcs and segments draw the piece graph without crossings. Pieces without arcs are isolated vertices.

By Lemma 1.1 and \(\sqrt K\ge C_{\rm sep}/\eta\), there is a set of at most \(\eta N'\) pieces whose deletion leaves components of at most \(K\) pieces, the *clusters*. The number of original occurrences in the deleted pieces is
\[
M\le\eta N'\cdot UL\le2\eta U\,H_0 .\tag{3.3}
\]
Keep the interval pairs whose two intervals lie in pieces that are not deleted, and discard the others. A kept original occurrence becomes unpaired only if its partner was deleted, so at most \(M\) original occurrences become unpaired. The two intervals of a kept pair lie in pieces joined by an arc, so they lie in one cluster.

Every cluster \(Z\) is a system with a pairing: its pieces are closed cyclically immersed paths, except possibly the undivided exceptional path, an immersed path starting at \(x_A\) or \(x_B\); its pairing consists of the kept interval pairs inside \(Z\); and it satisfies (1.1), since partners traverse distinct edges. The occurrences of the closures may traverse edges of \(\Gamma\) repeatedly; they are unpaired. Let \(H_Z\) be its total length, \(b_Z\) its number of unpaired occurrences and \(I_Z\) its number of interval pairs. By (3.1)–(3.3),
\[
\begin{aligned}
\sum_ZH_Z&\ge H_0-M\\
&\ge(1-2\eta U)H_0,\\
\sum_Zb_Z&\le H_{\rm add}+M\\
&\le\Bigl(\frac{3D}U+2\eta U\Bigr)H_0,\\
\sum_ZI_Z&\le6N'\le\frac{12H_0}L,
\end{aligned}
\]
and \(H_Z\le K(U+D)L=CL\) for every cluster.

*A good cluster.* By (2.2), the clusters have total length at least \(\frac{15}{16}H_0\), and \(\sum_Zb_Z\le\frac\varepsilon{16}H_0\). The clusters with \(b_Z>\varepsilon H_Z\) have total length at most \(\frac1\varepsilon\sum_Zb_Z\le\frac1{16}H_0\). The clusters with \(I_Z>192H_Z/L\) have total length at most \(\frac L{192}\sum_ZI_Z\le\frac{12}{192}H_0=\frac1{16}H_0\). A cluster of length less than \(L\) contains no closed cyclically immersed path of positive length, so it consists of the undivided exceptional path alone, of some length \(h<L\); since the arrangement also has a closed cyclically immersed boundary path, of length at least \(L\), we get \(H_0\ge h+L>2h\), and this cluster has length less than \(\frac12H_0\). The clusters of none of these three kinds have total length more than
\[
\begin{aligned}&\Bigl(\frac{15}{16}-\frac1{16}-\frac1{16}-\frac12\Bigr)H_0\\&\quad=\frac5{16}H_0>0 .\end{aligned}
\]
Choose one, \(Z\). It is a system of at most \(K\) paths with
\[
\begin{aligned}&L\le H_Z\le CL,\qquad b_Z\le\varepsilon H_Z,\\&I_Z\le\frac{192H_Z}L\le192C\le I,\end{aligned}
\]
and a pairing satisfying (1.1): a system excluded by the bounded-pattern estimate.

Finally, the distribution conditioned on girth at least \(L\) is defined for all large \(n\), by Lemma 2.1 of [Random matchings with large girth](random-matchings-with-large-girth.md), and an event of probability tending to \(1\) is nonempty for large \(n\). \(\square\)

Every arrangement, of any size, is converted into a system with the same fixed bounds \(K,C,I\): the cost of the closures is a proportion \(3D/U\) of the length, the deleted pieces a proportion \(2\eta U\), and the bound \(6N'\le12H_0/L\) on the interval pairs is linear in the length. No union bound over the sizes of arrangements is needed.

## 4. Exercises

**4.1.** Compute \(C_{\rm sep}\) numerically, and the bound of Lemma 1.1 for \(m=10^6\) and \(K=10^4\).

**4.2.** Show that a path of length \(h>UL\) divided into \(m=\lceil h/(UL)\rceil\) segments with lengths differing by at most one has segments of lengths between \(UL/3\) and \(UL\) when \(UL\ge6\), and give an example with \(UL=6\) and \(h=7\).

**4.3.** Let \(\varepsilon=10^{-5}\) and \(D=2000\). Compute \(U\) and \(\eta\) from (2.1), and estimate \(K\).

**4.4.** Explain why the proof would fail if the constant \(\varepsilon\) of the bounded-pattern estimate were allowed to depend on \(K\).

**4.5.** A cluster consists of one piece: a segment of length \(UL/3\) closed by a path of length \(DL\), with all original occurrences paired inside the cluster. Show that \(b_Z/H_Z\le3D/U\).

## 5. Solutions

**4.1.** \(\sqrt{2/3}\approx0.8165\), so \(C_{\rm sep}\approx2.8284/0.1835\approx15.41\). For \(m=10^6\) and \(K=10^4\) the bound is \(15.41\cdot10^6/100\approx1.54\cdot10^5\) vertices.

**4.2.** Since \(h>UL\), we have \(m\ge2\) and \(m<h/(UL)+1\), so \(h/m>UL\cdot h/(h+UL)>UL/2\). The segment lengths are at least \(\lfloor h/m\rfloor\ge h/m-1>UL/2-1\), which is at least \(UL/3\) for \(UL\ge6\), and at most \(\lceil h/m\rceil\le UL\), since \(h/m\le UL\) and \(UL\) is an integer. For \(UL=6\), \(h=7\): \(m=2\), segments of lengths \(3\) and \(4\), between \(2\) and \(6\).

**4.3.** \(U=\lceil96\cdot2000/10^{-5}\rceil=1.92\cdot10^{10}\). Then \(\frac\varepsilon{64U}\approx8.1\cdot10^{-18}\) is smaller than \(\frac1{32U}\), so \(\eta\approx8.1\cdot10^{-18}\), and \(K\approx(15.41/\eta)^2\approx3.6\cdot10^{36}\). The constants are enormous but fixed.

**4.4.** The bounds \(K\) and \(I\) are chosen through \(\eta\) and \(U\), which depend on \(\varepsilon\). If \(\varepsilon\) depended on \(K\), the choice would be circular, and no single application of the bounded-pattern estimate would cover all arrangements.

**4.5.** The cluster has \(H_Z=UL/3+DL\) and \(b_Z=DL\), so \(b_Z/H_Z\le DL/(UL/3)=3D/U\), which is at most \(\varepsilon/32\) by (2.2).

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
- [Lipton–Tarjan 1977] R. J. Lipton and R. E. Tarjan, *A separator theorem for planar graphs*, Stanford University, Computer Science Department, report STAN-CS-77-627, October 1977; published in SIAM J. Appl. Math. 36 (1979), 177–189. http://i.stanford.edu/pub/cstr/reports/cs/tr/77/627/CS-TR-77-627.pdf
