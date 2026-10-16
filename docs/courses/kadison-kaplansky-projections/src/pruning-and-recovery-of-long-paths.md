# Pruning and recovery of long paths

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two towers serve different purposes: \(Y^0\) has expanding incidences, and \(Y^\#\) has one family-wide labelling rule, from which the labels of a long path determine the path. This lesson deletes a small fraction of the vertices of every layer so that the two induced graphs coincide, so that layers of the same family can be told apart, and so that no short cycles remain. The surviving graph \(Y\) has all the properties needed later: expanding incidences, folded labels from a finite alphabet, recovery of long paths from their words, and large girth [OpenAI-KK, Section 6].

- Recovery of stream prefixes (Section 1).
- Few short cyclic paths (Section 2).
- The deletions (Section 3).
- The tower properties (Section 4).

The notation of the three preceding lessons is in force. A *path* is a finite walk; its *radius* at a position is the smaller of the numbers of its edges before and after that position. A path is *nonbacktracking* if it never follows an edge by its reverse, and a closed path is *cyclically nonbacktracking* if this also holds across its base point. Distances, degrees and lengths count edges, and parallel edges are distinct.

## 1. Recovery of stream prefixes

**Lemma 1.1** (recovery of prefixes; [OpenAI-KK, Lemma 6.1]). Let two nonbacktracking paths in \(Y^\#\) have the same word of oriented labels. At corresponding \(A\)-positions of radius at least \(2j+1\), the two vertices have the same \(u\)- and \(v\)-coordinates up to length \(r+sj\), for every \(j\ge0\). At corresponding \(B\)-positions of radius at least \(2j\), they have the same coordinates up to length \(sj\), for every \(j\ge1\). The positions may lie in different layers.

*Proof.* The orientation of a letter tells on which side each end lies, and its positive label gives the family, the serial number and \(x\), hence the slots at both ends. So at corresponding positions the two paths use the same slot names, diagonal coefficients, spill maps and family rules; the layers have the same sign and the same residue modulo \(K\), but their absolute values may differ.

At an interior position the incoming and the outgoing edge use different slots of the vertex: a slot carries one edge, so equal slots would mean a backtrack. For two different slots \(a,b\) at a vertex, the block equation (4.2) of [Streams, slots and slot evaluations](streams-slots-and-slot-evaluations.md) recovers the input block \(u_h\) and then \(v_h\) from the two evaluation blocks \(Q^a_h,Q^b_h\) and the preceding input block. Call the statement for side \(A\) and index \(j\) assertion \(\mathcal A_j\), for side \(B\) assertion \(\mathcal B_j\), and let \(\mathcal B_0\) be empty.

\(\mathcal A_0\): at an \(A\)-position of radius at least one, the label of each incident edge contains the first \(p=r+\alpha\ge r\) coordinates of the evaluation at its slot. Block \(0\) has no preceding spill, so the block equation recovers the first \(r\) coordinates, the same on both paths.

\(\mathcal B_j\), \(j\ge1\): at a \(B\)-position of radius at least \(2j\), both neighbours satisfy \(\mathcal A_{j-1}\), and the position satisfies \(\mathcal B_{j-1}\) by induction. By the second edge equation \(Q_B=x'\Vert\mathcal J(u_A)\), the evaluation at each incident slot up to length \(sj\) needs, besides \(x'\), the output of \(\mathcal J\) up to length \(sj-p'=r+s(j-1)-\beta\), at most \(r+s(j-1)\). Its source blocks are known at the neighbour, and the keys and gates of these blocks use \(B\)-blocks of the central vertex up to \(j-1\) and earlier blocks of the neighbour, all known. So both evaluations agree on the two paths up to length \(sj\), and the block equation, with the preceding block known by \(\mathcal B_{j-1}\), recovers \(B\)-block \(j\).

\(\mathcal A_j\), \(j\ge1\): at an \(A\)-position of radius at least \(2j+1\), both neighbours satisfy \(\mathcal B_j\). By the first edge equation, the evaluation up to length \(r+sj\) needs the output of \(\mathcal F\) up to length \(r+sj-p=sj-\alpha\le sj\), whose source blocks and keys are known. The block equation recovers \(A\)-block \(j\).

The rules are family-wide in \(Y^\#\), so they are the same on both paths even when a marked block lies beyond the cutoff of one of them; equal earlier blocks give equal keys and gates. \(\square\)

## 2. Few short cyclic paths

**Corollary 2.1** (few short cyclic paths; [OpenAI-KK, Corollary 6.2]). Fix a layer \(i\) and a side. A nonempty cyclically reduced word is the word of at most one cyclically nonbacktracking closed path in \(Y^\#\) based on that side of layer \(i\). The vertices of \(A_i\), or of \(B_i\), that are the base of such a closed path of length at most \(g_i\) number at most \(\sum_{a=1}^{\lfloor g_i\rfloor}(2m_\ell)^a\), and for large \(\ell\) this is at most a fraction \(2^{-0.9H_i}\) of the set, uniformly in \(i\).

*Proof.* Let two such closed paths have the same word. Traversing each of them many times is a nonbacktracking path, because they are cyclically nonbacktracking. At corresponding base positions Lemma 1.1 recovers arbitrarily long prefixes, and since the layer and the side are fixed, all active coordinates; so the base vertices coincide, and foldedness (Lemma 4.1 of [Gated permutations and the two towers](gated-permutations-and-the-two-towers.md)) determines the whole paths. The word of a cyclically nonbacktracking closed path is cyclically reduced: by foldedness, two cancelling consecutive letters are an edge followed by its reverse.

There are at most \((2m_\ell)^a\) words of length \(a\). Both sets have at least \(2^{H_i}\) elements, and by Lemma 4.1 of the lesson on gated permutations, \(\log_2(2m_\ell)/(100\log_2d)<\frac1{20}\) for large \(\ell\). If \(g_i\ge1\), the sum is at most \(2(2m_\ell)^{g_i}\le2^{1+H_i/20}\), a fraction at most \(2^{1-0.95H_i}\le2^{-0.9H_i}\). \(\square\)

## 3. The deletions

All deletions concern the common vertex set of \(Y^0\) and \(Y^\#\), and all fractions are relative to the original sets \(A_i,B_i\).

**Gate deletions.** At every vertex and every slot of every adjacent pair, evaluate the gate of the marked block of that pair, whether or not the rule uses it. Delete the vertex if one of these gates is closed. Fix an \(A\)-slot: the vertex corresponds bijectively to \((u_A,Q_A)\), hence, given \(x\), to \(u_A\) and the stream \(u_B\) of the other end, which are uniform for a uniform vertex. So the four full blocks before the marked block are zero with probability \(2^{-4s}\), and the same holds at a \(B\)-slot. A vertex has at most \(6D\) slots, so the deleted fraction is at most
\[
\varepsilon_{\mathrm{gate}}=6D\,2^{-4s}.
\]
On the surviving vertices the induced graphs of \(Y^0\) and \(Y^\#\) coincide: an edge between survivors has an open gate at the marked block of its pair, where the two rules then agree, and they agree at all earlier marked blocks.

**Separation of heights.** For a vertex on either side of layer \(i\), and every layer \(i'\) with the same sign, \(|i'|\equiv|i|\bmod K\) and \(|i'|<|i|\), put \(m=(|i|-|i'|)/K\) and
\[
q(i,i')=\min\{H_{i'},mK/2\} .
\]
Delete the vertex if its own \(u\)-coordinates in the \(q(i,i')\) positions after the cutoff of its side at layer \(i'\) all vanish. These positions are active at layer \(i\), because the length of each side grows by exactly \(mK/2\) from \(|i'|\) to \(|i|\). The probability is \(2^{-q(i,i')}\le2^{-mK/2}+2^{-H_{i'}}\), and summing over \(i'\), the deleted fraction is at most
\[
\begin{aligned}
\varepsilon_{\mathrm{sep}}&=\sum_{m\ge1}2^{-mK/2}+\sum_{i'\in\mathbb Z}2^{-H_{i'}}\\
&=\frac{2^{-K/2}}{1-2^{-K/2}}+3\cdot2^{-H_0} .
\end{aligned}
\]

**Short-cycle deletions.** At layer \(i\), delete every vertex that is the base of a nonempty cyclically nonbacktracking closed path in \(Y^\#\) of length at most \(g_i\). By Corollary 2.1 the deleted fraction is at most \(2^{-0.9H_i}\le2^{-0.9H_0}\).

Let \(Y\) be the graph induced on the surviving vertices, an induced subgraph of both \(Y^0\) and \(Y^\#\). The deleted fraction of every \(A_i\) and \(B_i\) is at most
\[
\begin{aligned}
\varepsilon_\ell&=6D\,2^{-4s}+\frac{2^{-K/2}}{1-2^{-K/2}}\\
&\quad+3\cdot2^{-H_0}+2^{-0.9H_0},
\end{aligned}
\]
which tends to \(0\) as \(\ell\to\infty\); for instance \(D2^{-4s}=2^{-32\ell}\).

## 4. The tower properties

**Proposition 4.1** (the tower; [OpenAI-KK, Proposition 6.3]). For large \(\ell\), the graph \(Y^0\) on the sets \(A_i\), \(B_i\) of sizes \(d2^{H_i}\) and \(2^{H_i}\), and its induced subgraph \(Y\), have these properties.

1. For every adjacent pair \((i,k)\), the incidence of \(Y^0\) between \(A_i\) and \(B_k\) has degrees \(d\) and \(D_{ik}=D2^{|i|-|k|}\); divided by \(\sqrt{dD_{ik}}\), it and its adjoint map normalized constants to normalized constants, and its norm between the orthogonal complements of the constants is at most \(1-\chi\), \(\chi=\frac1{800}\).
2. The fraction of vertices removed from every \(A_i\) and \(B_i\) is at most \(\varepsilon_\ell\).
3. The labels of \(Y\) are folded, from an alphabet of at most \(m_\ell\) positive labels.
4. A nonbacktracking path in \(Y\) that begins in layer \(i\) and has length at least \(L_i\) is determined by its word among all paths in \(Y\), wherever they begin.
5. \(Y\) has no nonempty cyclically nonbacktracking closed path based in layer \(i\) of length at most \(g_i\).

*Proof.* Statement 1 is Proposition 5.1 of [Expansion of the realized incidence](expansion-of-the-realized-incidence.md) with Lemma 3.1 of the lesson on streams and slots. Statements 2 and 3 have been shown. For 5, such a path in \(Y\) is a path in \(Y^\#\), and its base vertex was deleted.

For 4, take a path in \(Y\) beginning in layer \(i\) and a second path in \(Y\) with the same word. By foldedness the second path is nonbacktracking too. It suffices to show that the initial segments of length \(N=\lceil L_i\rceil\) coincide, since foldedness then propagates the identity forward. Take the middle position of the segment, of radius at least \(\lfloor N/2\rfloor\), and let \(j\) be its layer on the first path. Every edge changes the layer by at most one, so \(H_j\le H_i+N\). Lemma 1.1 recovers both vertices at the middle position up to length \(r+s\lfloor(R-1)/2\rfloor\) on side \(A\), or \(s\lfloor R/2\rfloor\) on side \(B\), with \(R\ge\lfloor N/2\rfloor\); in both cases at least
\[
\begin{aligned}
\frac{sN}4-2s&\ge\frac{25s}{\log_2d}H_i-2s\\
&=62.5\,H_i-2s ,
\end{aligned}
\]
which exceeds \(2H_j\) for large \(\ell\), uniformly in \(i\), because \(N\le100H_i/\log_2d+1\).

The two middle layers have the same sign and residue modulo \(K\). If they are equal, all active coordinates, of lengths at most \(H_j\), are recovered, and the middle vertices coincide. Otherwise let \(i_-\), \(i_+\) be the two layers ordered by absolute value, with \(|i_+|-|i_-|=mK\), \(m\ge1\), and put \(H_-=H_{i_-}\le H_j\). Let \(l_-\le H_-\) be the length of the \(u\)-stream of the vertex in layer \(i_-\). The positions tested at the vertex in layer \(i_+\) by the separation deletion for \(i'=i_-\) end at
\[
l_-+\min\{H_-,mK/2\}\le2H_-\le2H_j ,
\]
so they are recovered. There the stream of the lower vertex is zero padding, so the \(u\)-coordinates of the upper vertex vanish on all tested positions, and it would have been deleted. This contradiction shows that the middle vertices coincide; foldedness identifies the two segments forward and backward from the middle. \(\square\)

**Corollary 4.2** (deletion and constant vectors; [OpenAI-KK, Corollary 6.4]). Let \(\Pi\) be the projection on the counting space of all vertices, tensored with any Hilbert space, that keeps the vertices of \(Y\), and let \(\mathcal C\) be the space of vectors constant on each \(A_i\) and each \(B_i\) in the vertex coordinate. Then \(\|(1-\Pi)|_{\mathcal C}\|\le\sqrt{\varepsilon_\ell}\).

*Proof.* On a normalized constant vector of one set, the squared norm removed by \(1-\Pi\) is the deleted fraction of that set. The sets are disjoint, so the losses of different components add, each at most \(\varepsilon_\ell\) times the squared norm of the component; a tensor factor changes nothing. \(\square\)

## 5. Exercises

**5.1** (easy). Why does an interior position of a nonbacktracking path use two different slots, while the two ends of a path may use the same slot as another path?

**5.2** (medium). Let a vertex in layer \(i_-\) and a vertex on the same side in layer \(i_+\), with \(|i_+|=|i_-|+K\) and the same sign, have \(u\)-streams that agree on the first \(l_-\) coordinates, where the upper stream vanishes on the next \(K/2\) coordinates. Explain why prefix recovery up to length \(l_-+K/2\) cannot distinguish them, and which deletion removes the upper vertex.

**5.3** (medium). Compute the four terms of \(\varepsilon_\ell\) for \(\ell=1\) and \(\ell=2\).

**5.4** (medium). In Corollary 2.1, why does the count use all words of length at most \(g_i\), rather than reduced words only, and why is it still small?

## 6. Solutions

**5.1.** At an interior vertex, equal slots would mean the same edge entered and left, a backtrack. At an end there is only one incident edge of the path.

**5.2.** Padding makes the lower stream zero beyond \(l_-\), so on every prefix of length at most \(l_-+K/2\) the two streams agree, and their labels, which give only the family, agree too. The separation deletion for \(i'=i_-\) tests exactly these \(K/2\) positions, since \(q(i_+,i_-)=\min\{H_{i_-},K/2\}=K/2\), and removes the upper vertex.

**5.3.** For \(\ell=1\): \(D=2^8\) and \(s=10\), so \(\varepsilon_{\mathrm{gate}}=6\cdot2^{-32}\approx1.40\cdot10^{-9}\); \(K=320\) gives a separation term of about \(2^{-160}\); and \(H_0=20011\) makes \(3\cdot2^{-H_0}\) and \(2^{-0.9H_0}\) smaller than \(2^{-18000}\). So \(\varepsilon_1\approx1.40\cdot10^{-9}\). For \(\ell=2\): \(\varepsilon_{\mathrm{gate}}=6\cdot2^{16-80}\approx3.3\cdot10^{-19}\), the separation term is about \(2^{-320}\), and \(\varepsilon_2\approx3.3\cdot10^{-19}\).

**5.4.** Counting all words only enlarges the bound. It stays small because \(\log_2(2m_\ell)=11\ell+O(\log\ell)\) and \(g_i=H_i/(400\ell)\), so \((2m_\ell)^{g_i}=2^{(11/400+o(1))H_i}\), far smaller than the \(2^{H_i}\) vertices of the set.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 6, Lemma 6.1, Corollaries 6.2 and 6.4, Proposition 6.3. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
