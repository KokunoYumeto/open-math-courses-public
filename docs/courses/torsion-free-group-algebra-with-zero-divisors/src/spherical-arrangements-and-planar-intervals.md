# Spherical arrangements and planar intervals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In [Cone pictures and asphericity](cone-pictures-and-asphericity.md), a failure of asphericity or of root separation will be turned into a configuration on a sphere: disjoint disks whose boundaries carry paths in the random graph \(\Gamma\), with all letter occurrences paired by disjoint arcs between the disks. This lesson defines these reduced spherical arrangements and proves two deterministic tools for them [OpenAI-KZ, Section 4]. Every segment of a path can be closed up by appending a short path, without cancellation (Section 2). And the pairing of an arrangement whose boundary paths are cut into \(N'\) pieces is described by at most \(6N'\) comparisons of intervals (Section 4); the proof counts the regions of the sphere by their Euler characteristics. [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md) uses both tools to extract from every arrangement, however large, a bounded system as in the bounded-pattern estimate.

- Reduced spherical arrangements (Section 1).
- Short closures (Section 2).
- Surfaces in the sphere (Section 3).
- Planar intervals (Section 4).

We keep the random graph \(\Gamma=\Gamma_A\sqcup\Gamma_B\) of [Random matchings with large girth](random-matchings-with-large-girth.md), with \(q=128\), girth at least \(L=\lfloor c\log n\rfloor\), the prescribed vertices \(x_A\in A\), \(x_B\in B\), and the constant \(D_0\) of the diameter lemma, Lemma 4.1 of that lesson. Paths, letters, immersed and cyclically immersed paths, occurrences and interval pairs are as in [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md). A path has *no backtracking* if it never traverses an edge and immediately the same edge back. In the immersed labelled graph \(\Gamma\) this is the same as having no cancelling turn: if consecutive edges carry \(t\) and \(\bar t\) at their common vertex \(w\), the second edge and the reverse of the first are both the edge leaving \(w\) with letter \(\bar t\), so they coincide. Disks, arcs and surfaces in a sphere are piecewise linear (PL) with respect to some triangulation.

## 1. Reduced spherical arrangements

**Definition 1.1** (reduced spherical arrangements; [OpenAI-KZ, Definition 4.1]). A *reduced spherical arrangement* over \(\Gamma\) consists of the following data on an oriented sphere \(S\).

1. *Disks and boundary paths.* Pairwise disjoint closed disks \(D_1,\ldots,D_N\subset S\), \(N\ge1\), oriented by \(S\), with the induced boundary orientations. Each \(\partial D_i\) carries a path \(p_i\) in \(\Gamma\) of positive length \(h_i\): the circle \(\partial D_i\) is divided into \(h_i\) consecutive closed arcs, the *occurrences*, which follow the edges of \(p_i\) in the boundary orientation, and each occurrence carries the letter of its edge read along \(p_i\). All the \(p_i\) are closed and cyclically immersed, except possibly one, the *exceptional path*, which is an immersed path starting at \(x_A\) or \(x_B\); its occurrences run from a marked point of its circle, the *break*, once around the circle back to the break. At least one boundary path is closed and cyclically immersed.
2. *Pairing arcs.* Pairwise disjoint arcs \(\alpha_1,\ldots,\alpha_E\subset S\), whose interiors lie outside the disks and whose endpoints lie on the disk boundaries, such that each occurrence contains exactly one endpoint of an arc, in its interior. The two occurrences at the ends of an arc are *partners*.
3. *Reduction.* Partners carry inverse letters, and they traverse distinct edges of \(\Gamma\).

The common endpoints of consecutive occurrences on a circle are its *junctions*: \(\partial D_i\) has \(h_i\) junctions, and for the exceptional path one of them is the break. At every junction other than the break, the two letters do not form a cancelling turn, because the boundary paths are immersed, and the closed ones cyclically. There are \(2E\) occurrences. The paths may traverse an edge of \(\Gamma\) many times; their occurrences remain distinct. An arc may have both ends on one disk, and the *arc graph*, with the disks as vertices and the arcs as edges, may have loops, parallel edges and several components. Condition 3 is the reduction condition (1.1) of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md) for the pairing given by the arcs.

## 2. Short closures

**Lemma 2.1** (short closures; [OpenAI-KZ, Lemma 4.2]). Fix an integer
\[
D\ge D_0+\frac8{c\log2}+8 .
\]
For all sufficiently large \(n\) the following holds whenever every component of \(\Gamma\) has diameter at most \(D_0L\). For every path \(P\) in \(\Gamma\) of positive length without backtracking there is a path \(P'\) of length at most \(DL\), from the end of \(P\) to its start, such that the closed path \(PP'\) is cyclically immersed.

*Proof.* For large \(n\) we have \(L\ge3\), so \(\Gamma\) has no loops and no two edges with the same ends, since both would be cycles of length less than \(3\).

*Loops avoiding two edges.* Put \(k=\lceil\log_2n\rceil+1\). Let \(z\) be a vertex and \(\epsilon_1,\epsilon_2\) at most two edges at \(z\). We find a closed path \(J\) at \(z\) of length at most \(2k\), without backtracking, whose first and last edges differ from \(\epsilon_1\) and \(\epsilon_2\). Remove \(\epsilon_1,\epsilon_2\) from the side of \(\Gamma\) containing \(z\). Every vertex keeps degree at least \(q+1-2\ge3\), so there are at least \(3\cdot2^{k-1}\ge3n\) walks of length \(k\) from \(z\) without backtracking in the remaining graph: the first step has at least \(3\) choices and every later step at least \(2\). The side has \(n\) vertices, so two distinct such walks \(W_1,W_2\) end at the same vertex. Let \(V\) be their longest common final segment; it is shorter than \(k\), since \(W_1\ne W_2\). Write \(W_1=P_1V\) and \(W_2=P_2V\), where \(P_1,P_2\) have positive length and different last edges. Then \(J=P_1P_2^{-1}\) is a closed path at \(z\) of length at most \(2k\). It has no backtracking: inside \(P_1\) and \(P_2^{-1}\) because the walks have none, and at the junction because the last edges of \(P_1\) and \(P_2\) differ. Its first edge is the first edge of \(W_1\), and its last edge is the reverse of the first edge of \(W_2\); both avoid \(\epsilon_1,\epsilon_2\).

*The closure.* Let \(P\) run from \(a\) to \(b\). These vertices lie in one component, so there is a shortest path \(U\) from \(b\) to \(a\), of length at most \(D_0L\); a shortest path has no backtracking. If \(U\) has positive length, choose \(J_b\) at \(b\) avoiding the last edge of \(P\) and the first edge of \(U\), and \(J_a\) at \(a\) avoiding the last edge of \(U\) and the first edge of \(P\), and put \(P'=J_bUJ_a\). A backtrack at a junction of two paths would require the second path to start with the reverse of the last edge of the first, in particular with the same edge. The choices exclude this at the junctions of \(P\) with \(J_b\), of \(J_b\) with \(U\), of \(U\) with \(J_a\), and, cyclically, of \(J_a\) with \(P\). If \(U\) has length \(0\), so that \(a=b\), put \(P'=J_a\) with \(J_a\) avoiding the last and the first edge of \(P\). In both cases \(PP'\) is a closed path without backtracking, also cyclically, hence cyclically immersed.

The length of \(P'\) is at most \(D_0L+4k\). For large \(n\), \(L\ge c\log n-1\ge\frac c2\log n\) and \(L\ge1\), so
\[
k\le\frac{\log n}{\log2}+2\le\Bigl(\frac2{c\log2}+2\Bigr)L,
\]
and \(D_0L+4k\le DL\). \(\square\)

## 3. Surfaces in the sphere

The counting in Section 4 uses the following standard facts about surfaces in a sphere. They are not proved in this course. Hatcher's *Algebraic Topology* contains the homological tools from which parts 2 and 3 follow: the Euler characteristic as an alternating sum of ranks of homology groups [Hatcher, Theorem 2.44], the Mayer–Vietoris sequence [Hatcher, Section 2.2] and Alexander duality in spheres [Hatcher, Corollary 3.45]; part 5 is a consequence of the Schoenflies theorem, which strengthens the Jordan curve theorem [Hatcher, Proposition 2B.1]. A course proving these facts is recorded as an open obligation of this course. Parts 4 and 5 are used in [Cone pictures and asphericity](cone-pictures-and-asphericity.md).

**(SURF)** (surfaces in the sphere). Let \(D_1,\ldots,D_N\) and \(\alpha_1,\ldots,\alpha_E\) be disks and arcs on an oriented sphere \(S\) as in parts 1 and 2 of Definition 1.1. There are pairwise disjoint closed disks \(B_1,\ldots,B_E\), the *bands*, such that \(B_j\) contains \(\alpha_j\) and meets the disks \(D_i\) exactly in two short arcs of their boundaries, around the two endpoints of \(\alpha_j\) and inside the two occurrences containing them; the rest of \(\partial B_j\) consists of two arcs, the *sides* of the band. Put \(R=D_1\cup\cdots\cup D_N\cup B_1\cup\cdots\cup B_E\). Then:

1. The closure of \(S\setminus R\) is the disjoint union of finitely many compact connected surfaces, the *regions*. Every boundary circle of \(R\) is a boundary circle of exactly one region, and every boundary circle of a region is one of \(R\).
2. \(\chi(R)=N-E\), and the Euler characteristics of the regions add up to \(2-N+E\).
3. A region with \(b\) boundary circles has Euler characteristic \(2-b\).
4. If two compact surfaces in \(S\), oriented by \(S\), meet along an arc of their boundaries and lie on opposite sides of it, their boundary orientations along that arc are opposite. In particular this holds for a disk \(D_i\) and a region along a gap.
5. The closure of each component of the complement of a circle in \(S\) is a closed disk. Consequently, the closure of \(S\) minus a closed disk is a closed disk, and the closure of \(S\) minus a closed annulus is the disjoint union of two closed disks, each bounded by one of the boundary circles of the annulus.

In this situation, a *gap* is an arc of a disk boundary between two consecutive band attachments. Since each occurrence contains exactly one arc end, consecutive arc ends lie in consecutive occurrences, and the gap between them contains exactly one junction; so gaps and junctions correspond, and there are \(2E\) gaps. The boundary of \(R\) consists of the gaps and the band sides, and along each boundary circle of \(R\) gaps and band sides alternate: a gap ends at a band attachment, where the boundary turns onto a band side, which ends at a band attachment on the other end of the arc, where a gap begins. For a region \(Q\) let \(l_Q\) be the number of gaps on its boundary. It is also the number of band sides on its boundary, so the \(l_Q\) add up to \(2E\). Every disk carries an occurrence and so an arc end, hence every boundary circle of \(R\) contains a band side, and \(l_Q\ge1\). By (SURF 2),
\[
\begin{aligned}&\sum_Q\bigl(l_Q-2\chi(Q)\bigr)\\&\quad=2E-2(2-N+E)\\&\quad=2N-4.\end{aligned}\tag{3.1}
\]

## 4. Planar intervals

Consider an arrangement with \(N\) boundaries, and divide every boundary path into consecutive segments, the *pieces*, \(N'\) pieces in all; the exceptional path is divided as a path from its first to its last occurrence, so that no piece runs across the break. A boundary path that is not divided is one piece.

**Lemma 4.1** (planar intervals; [OpenAI-KZ, Lemma 4.3]). Number the occurrences of every piece consecutively from its first occurrence, where for a closed boundary path forming one piece a suitable first occurrence is chosen. Then the pairing of the arrangement consists of at most \(6N'\) interval pairs. Each consists of two disjoint intervals, each inside one piece, with an order-reversing bijection that carries inverse letters.

*Proof.* We use the bands and regions of (SURF). A region is *simple* if it has one boundary circle; by (SURF 3), \(\chi(Q)=1\) for simple regions and \(\chi(Q)\le0\) for the others.

*Good gaps.* A *digon* is a simple region with \(l_Q=2\). Its boundary circle runs through a gap, a side of one band, a second gap and a side of a band; the digon is *proper* if the two band sides belong to different arcs. A gap on a proper digon is *good*.

Let \(g\) be a good gap, between consecutive occurrences \(e\) and \(f\) of a disk \(D\), with \(e\) before \(f\) in the boundary orientation of \(D\), and let \(e',f'\) be the partners of \(e,f\). Walk around the digon in its boundary orientation. By (SURF 4) the gap \(g\) is traversed against the orientation of \(D\), from the band at \(f\) to the band at \(e\). The walk continues along the side of the band of the arc at \(e\), to the other end of that arc, in \(e'\); then along the second gap \(g'\) on the disk \(D'\) of \(e'\), against the orientation of \(D'\); then along the side of the band of the arc at \(f\), back to \(f\). So \(g'\) lies between the arc ends in \(e'\) and \(f'\): these are consecutive occurrences of \(D'\), and since \(g'\) is traversed from \(e'\) to \(f'\) against the orientation of \(D'\), \(f'\) comes before \(e'\). Thus, if \(g\) lies between \(e\) and \(f\) in this order, the other gap \(g'\) of the digon lies between \(f'\) and \(e'\) in this order; briefly,
\[
(e,f)\longmapsto(f',e').\tag{4.1}
\]
The map \(\iota(g)=g'\) is an involution of the good gaps without fixed points.

*Counting the other gaps.* Let \(M\) be the number of simple regions with \(l_Q=1\), the *monogons*. The boundary circle of a monogon consists of one gap, between occurrences \(e,f\), and one band side, so the arc at \(e\) ends at \(f\): \(e\) and \(f\) are partners, consecutive and with inverse letters. This is a cancelling turn at their junction, so the junction is the break, and \(M\le1\). A monogon contributes \(1-2=-1\) to (3.1).

A digon that is not proper has both band sides from one arc \(\alpha\): its boundary runs along one side of the band of \(\alpha\), then along a gap, then back along the other side. This gap starts and ends at the same end of \(\alpha\), so it goes once around a disk carrying only one occurrence. Different such digons contain different gaps, and such a disk has only one gap, so there are at most \(N\) digons that are not proper, with at most \(2N\) gaps. Digons contribute \(0\) to (3.1). For arrangements over \(\Gamma\) such digons do not occur, as Ivanov observes [Ivanov 2026, Remark A.4]: by the same argument at the other end of \(\alpha\), both ends of \(\alpha\) lie on disks carrying a single occurrence, at most one of which is the exceptional one, and a closed cyclically immersed path of length one would be a loop, which the girth excludes. The coarse count suffices here.

Every other region contributes a positive amount \(l_Q-2\chi(Q)\) to (3.1): a simple region with \(l_Q\ge3\) contributes \(l_Q-2\ge1\), and a region that is not simple contributes at least \(l_Q\ge1\). In both cases \(l_Q\le3(l_Q-2\chi(Q))\). By (3.1) these contributions add up to \(2N-4+M\). So the number \(B_{\rm gap}\) of gaps that are not good satisfies
\[
\begin{aligned}
B_{\rm gap}&\le M+2N+3(2N-4+M)\\
&=8N-12+4M\le8N-8 .
\end{aligned}
\]

*Cuts.* *Mark* one gap on every boundary, the break on the exceptional one, and the gaps at the junctions between consecutive pieces. A closed boundary path divided into \(m\ge2\) pieces has \(m\) such junctions, and the exceptional path divided into \(m\) pieces has \(m-1\) besides the break, so at most \(N+N'\) gaps are marked. The *cuts* are the gaps that are not good, the marked gaps, and the images under \(\iota\) of the marked good gaps. There are at most
\[
B_{\rm gap}+2(N+N')\le12N'
\]
cuts, since \(N\le N'\). A good gap is a cut exactly when its image under \(\iota\) is one.

*Runs.* On each boundary circle the cuts, of which there is at least one, divide the occurrences into maximal *runs* of consecutive occurrences whose internal gaps are not cuts. A circle with \(j\ge1\) cuts has exactly \(j\) runs, so there are at most \(12N'\) runs. Every run lies inside one piece and does not run across the break, since these junctions are cuts.

Let \(r=(o_1,\ldots,o_k)\) be a run, in the boundary order, and \(o_1',\ldots,o_k'\) the partners. For \(i<k\) the gap between \(o_i\) and \(o_{i+1}\) is not a cut, hence good, so by (4.1) \(o_{i+1}'\) comes immediately before \(o_i'\), and the gap between them, its image under \(\iota\), is not a cut. So \(o_k',\ldots,o_1'\) are consecutive in this order, with no cut between them. The gap after \(o_1'\) is a cut: if it is good, it lies between \(o_1'\) and an occurrence \(s\), and by (4.1) its image lies between \(s'\) and \(o_1\), that is, it is the gap before \(o_1\), which is a cut because \(r\) is maximal. In the same way the gap before \(o_k'\) is a cut. So the partners of \(r\) form a run \(r'\), in reverse order.

The run \(r'\) differs from \(r\). Otherwise the partner of \(o_i\) would be \(o_{k+1-i}\). For odd \(k\), the middle occurrence would be its own partner. For even \(k\), \(o_{k/2}\) and \(o_{k/2+1}\) would be partners, consecutive and with inverse letters, a cancelling turn at a junction that is not a cut, hence not the break.

So the runs fall into pairs \(\{r,r'\}\), at most \(6N'\) of them. Number the occurrences of each piece from its first occurrence, and those of a closed path that forms one piece from a cut on it. Every run is then an interval of its piece, and the pair \(r,r'\) with \(o_i\mapsto o_i'\) is an order-reversing interval pair carrying inverse letters. The runs partition the occurrences, so the intervals of different pairs are disjoint. \(\square\)

The proof never uses that the arc graph is connected or that the regions are disks: Euler characteristics account for all regions at once, and each digon that is not proper is paid for by a disk with a single occurrence.

## 5. Exercises

**5.1.** Compute the bound \(D_0+\frac8{c\log2}+8\) of Lemma 2.1 for \(c=1/100\).

**5.2.** Give an example of a path \(P\) without backtracking and a shortest return path \(U\) such that the closed path \(PU\) is not cyclically immersed.

**5.3.** Let \(D_1,D_2\) be two disks on a sphere and \(\alpha_1,\ldots,\alpha_h\) disjoint arcs from \(\partial D_1\) to \(\partial D_2\), \(h\ge2\), as in parts 1 and 2 of Definition 1.1. Describe the regions, check (3.1), and determine which gaps are good.

**5.4.** In the situation of Exercise 5.3, let each circle carry \(h\) occurrences, each disk forming one piece. Mark a gap \(g\) on \(\partial D_1\) and the gap \(\iota(g)\) on \(\partial D_2\). Show that the cuts are \(g\) and \(\iota(g)\), that there are exactly two runs, and that they are partners.

**5.5.** Show that a circle with \(j\ge1\) cuts carries exactly \(j\) runs, and that a circle without cuts would carry no run in the sense of the proof.

## 6. Solutions

**5.1.** \(\frac8{c\log2}=\frac{800}{\log2}\approx1154.2\), so every integer \(D\ge D_0+1163\) is allowed.

**5.2.** Let \(P\) be a single edge from \(a\) to \(b\). The shortest path from \(b\) to \(a\) is the same edge backwards, and \(PU\) traverses the edge and immediately back.

**5.3.** The arcs, in their cyclic order around \(D_1\), cut the annulus between the disks into \(h\) regions, each bounded by two consecutive arcs: a gap on \(\partial D_1\), a band side, a gap on \(\partial D_2\) and a band side. Each region is a proper digon, \(N=2\), \(E=h\), and both sides of (3.1) are \(0\). All gaps are good, and \(\iota\) exchanges the gap between the \(i\)-th and \((i+1)\)-st arc ends on \(\partial D_1\) with the gap between the same arcs on \(\partial D_2\).

**5.4.** All gaps are good, and the marked gaps \(g,\iota(g)\) are exchanged by \(\iota\), so they are the only cuts. Each circle has one cut, hence one run, consisting of all its \(h\) occurrences. By the proof of Lemma 4.1 the partners of a run form a run, so the run of \(\partial D_1\) is paired with the run of \(\partial D_2\), in reverse order.

**5.5.** Going around the circle, every cut ends one run and starts the next, so the runs correspond to the cuts. Without cuts, the occurrences would form a cyclic sequence rather than a run with a first and a last element; the marked gap on every boundary excludes this.

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
- [Ivanov 2026] S. V. Ivanov, *Zero divisors in group algebras of torsion-free groups in odd characteristic*, arXiv:2610.17662, 13 October 2026, Appendix A. https://arxiv.org/abs/2610.17662
