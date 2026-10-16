# Auxiliary incidences, deletions and recovery

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The edge equations of [Streams, coefficient pools and universal corrections](streams-coefficient-pools-and-universal-corrections.md) are now solved. At each pair of heights a slightly modified *auxiliary* rule gives exactly one edge at every slot, and the solution identifies a uniform endpoint with independent uniform bits. Two kinds of deletions make the auxiliary graph satisfy the universal equations and separate different heights. On the remaining graph, two occurrences of one long label word recover each other's states, even at different heights, and the result is a folded labelled tower in which every long word occurs at most once [OpenAI-BCI, Sections 2.4-2.7].

- The auxiliary incidence and uniform coordinates (Section 1).
- Gate deletions (Section 2).
- Recovery of padded prefixes (Section 3).
- Separation of heights (Section 4).
- The labelled tower (Section 5).

The notation of the previous lesson is in force: \(b,s,r,d,D,q,n_0\), the stream lengths \(\ell_A,\ell_B\), the scales \(H_i\), the cutoff forms of Lemma 1.1, types, families, extras, slots, labels \(\lambda=(f,j,e,h_0)\), marks, the names and the maps \(K_\nu\), the gates \(g_k\), the corrected streams, the transformations \(P_{A,\lambda},P_{B,\lambda}\) and the edge equations (4.3) there.

## 1. The auxiliary incidence

For a height pair of a type, the *auxiliary prescription* modifies the universal rules at that occurrence only: its extra correction, if there is one, is applied regardless of its gate, and the permutation of its marked cutoff is applied regardless of its gate. All other rules keep their gates. Write \(X^0\) for the graph whose edges between \(\mathscr A_i\) and \(\mathscr B_{i+\delta_\tau}\) are the solutions of the edge equations under the auxiliary prescription of that occurrence, over all types and height pairs; a vertex of \(X^0\) at height \(i\) is a state in \(\mathscr A_i\) or \(\mathscr B_i\). States for which a forced choice actually mattered will be deleted.

**Lemma 1.1** (inversion and uniform coordinates; [OpenAI-BCI, Lemma 2.2]). Fix all tables. For every type and height pair, the auxiliary prescription has exactly one edge at every endpoint state and slot. In a fixed extra slice the incidence is biregular with degrees \(d\) on side \(A\) and \(D\) on side \(B\). An endpoint state with a fixed slot, and its extra value when it is the larger endpoint, corresponds bijectively to the free label head bits together with all free raw input coordinates of both streams at the common cutoff. Consequently, for a uniform endpoint state, those raw coordinates and head bits are independent uniform bits.

*Proof.* Let \(h\) be the smaller height and \(\kappa\) the marked index.

*The common support is preserved.* At the larger endpoint the forced correction adds \(e\) to its extra interval, whose value is \(e\); the corrected stream is zero there. Corrections at earlier marks of the family lie inside the active coordinates. At later marks, the gate reads eight raw blocks of index at least \(\kappa+K-13>\kappa+2\) (Lemma 4.1 and (2.2) of the previous lesson), all beyond the raw support of the endpoint pair, which ends at most one index after \(\kappa\) (Lemma 2.1 there); so these gates are closed. Hence the corrected input streams are supported exactly on the common active coordinates at height \(h\).

The transformations preserve this support. At \(\kappa\) the permutation acts on the first \(t\) bits and is the identity on the rest. The twenty following indices are identities on zero corrected blocks. At an ordinary index \(k\ge\kappa+21\) the gate reads blocks of index at least \(2\lfloor(k-5)/2\rfloor-7\ge\kappa+8\), beyond the raw support, so it is closed, and so are the gates at later marks. In particular the raw extra bits of the larger endpoint, at index at most \(\kappa+1\), are read by no gate of an index \(\ge\kappa+21\), and gates of indices up to \(\kappa+20\) are not applied. The evaluation coordinates fit as well: by the table of Lemma 1.1 of the previous lesson, the output of \(K_\nu\) on the common inputs ends within the common evaluation length, and an extra interval in an evaluation stream lies beyond that output, where the direct term \(K_\nu\bar u\) of that side vanishes.

*Inversion from side \(A\).* Given an \(A\)-state and a slot, the extra is known, from the slot or from the state. The first \(r\) bits of its evaluation are \(h_0\): no mark lies in the initial blocks. So the bucket \(c\) and the \(B\)-name are known. Proceed through the source order. To recover the raw block \(u_{B,j}\), compute the \(A\)-evaluation block of index \(2j\), corrected by its offset; the gates of the offset read raw blocks of index at most \(2j-5\), already known. The key of the table at index \(2j-1\) consists of the label and of raw blocks of index less than \(2j-1\), all known, and its gate reads indices at most \(2j-6\). Invert this known permutation and undo the known input correction of index \(2j-1\): this gives \(u_{B,j}\). The second equation of (4.3), whose right side is now known through this position, gives the raw \(v_B\) block of index \(2j-1\). Continuing, all of \(u_B,v_B\) is determined, with the required support by the preceding paragraph.

*Inversion from side \(B\).* Given a \(B\)-state and a slot, the bucket \(c\) is in the slot, and the first \(s-r\) evaluation bits are \(h_0'\), so \(h_0=c\Vert h_0'\) and the label are known. The same procedure, with the roles exchanged, recovers \(u_A\) block by block from the \(B\)-evaluation, and then \(v_A\) from the first equation. The lag of the gates is essential here: a correction in the \(B\)-evaluation block of index \(2j-1\) does not read the unknown block \(u_{A,j-1}\) of index \(2j-2\), and a correction in the \(A\)-evaluation block of index \(2j\) does not read the unknown \(u_{B,j}\).

The two procedures solve the same triangular system and are inverse to each other. This gives exactly one edge at every state and slot, and biregularity with the degrees of the slot counts.

*Uniform coordinates.* Prescribe freely the raw input blocks of both streams through the common cutoff (omitting the extra interval of the larger endpoint if it lies in an input stream, where it equals \(e\)), and \(h_0\) for an \(A\)-slot, or \(h_0'\) for a \(B\)-slot whose bucket is fixed. Then every gate, correction and permutation is determined, the equations (4.3) determine both corrected evaluation streams, and undoing the corrections gives both raw evaluation streams; an extra interval in an evaluation stream comes out equal to \(e\). The number of free bits is
\[
\begin{gathered}
\ell_A(h)+\ell_B(h)+r=\log|\mathscr A_h|,\ \text{or}\\
\ell_A(h)+\ell_B(h)+s-r=\log|\mathscr B_h| ,
\end{gathered}
\]
respectively. The inversion shows that the map from these free bits to endpoint states is a bijection, not only that the dimensions agree. So the uniform measure on endpoint states is the product of uniform measures in these coordinates. \(\square\)

## 2. Gate deletions

At a slot, evaluate the *natural* gates along its auxiliary edge, also where the auxiliary prescription forced them. Let \(\kappa\) be its marked index. Delete an endpoint state if, for some incident slot:

1. one of \(g_\kappa,g_{\kappa-1},g_{\kappa-2}\) is zero; or
2. the natural gate of its extra correction is zero (adjacent pairs only); or
3. among the full active \(A\)-input blocks other than \(A_0\), more than \(1/250\) have a closed gate; or the same holds among the full active \(B\)-input blocks.

The two parities are tested separately. The deterministic identity rules at marks and in the twenty following indices are accounted for separately below.

**Lemma 2.1** (gate budget; [OpenAI-BCI, Lemma 2.3]). For every choice of tables, the fraction of either state space at any height deleted for gate reasons is at most
\[
\varepsilon_{\rm gate}=600\,T\,2^bD\,2^{-8s}.\tag{2.1}
\]
On an edge whose two endpoints survive, neither forced choice was necessary, so the edge satisfies the universal equations (4.3) of the previous lesson. At every surviving slot, separately among its full \(A\)-input blocks and its full \(B\)-input blocks, fewer than a fraction \(0.005\) of the blocks are *unavailable*, that is, have a closed gate or lie in a mark or one of the twenty indices after it; and the gates \(g_\kappa,g_{\kappa-1},g_{\kappa-2}\) and the gate of the extra correction are open.

*Proof.* Fix a slot and, at a larger endpoint, the extra value. Every gate of index at most \(\kappa+2\) with index above \(20\) reads eight full raw blocks of index at most \(\kappa-3\); these are free raw coordinates in the sense of Lemma 1.1, hence independent uniform. So each such gate is closed with probability exactly \(2^{-8s}\), and the gates of index at most \(20\) are never closed. Tests 1 and 2 fail with probability at most \(4\cdot2^{-8s}\). Each parity has at least \(n_0-1\) full active blocks; by linearity of expectation and Markov's inequality, the probability that more than \(1/250\) of them have closed gates is at most \(250\cdot2^{-8s}\), for each parity. A state has at most \(T2^bD\) slots, since \(D\ge d\). The union bound gives \(T2^bD(4+500)2^{-8s}\), which is at most (2.1); averaging over the extra value gives the same bound at a larger endpoint.

Tests 1 and 2 read only raw coordinates, which are the same for the auxiliary and the universal rule. If they pass, the natural gates of the marked permutation and of the extra correction are open, so the universal rule applies the same choices as the auxiliary one along this edge, and the support argument of Lemma 1.1 applies at both ends. So edges between surviving states satisfy (4.3).

For either parity, the marks and their twenty following indices contain at most eleven indices of that parity each, consecutive marks are \(K=2\cdot10^6b\) indices apart, and at most one zone is cut by the end of the counted range. So these zones contain a fraction at most \(22/K+22/n_0<10^{-4}\) of the full blocks of that parity. Together with the gate fraction \(1/250\), fewer than \(0.005\) of the blocks are unavailable. A marked partial block is counted as unavailable for a test on full blocks even if its gate is open. \(\square\)

## 3. Recovery of padded prefixes

Let \(X^{\rm surv}\) be the graph induced on the states surviving the gate deletions; by Lemma 2.1 all its edges satisfy the universal equations. The aligned *depths* are
\[
\begin{gathered}
\delta_A(j)=(2j+1)s,\\
\delta_B(j)=2js\qquad(j\ge0).
\end{gathered}\tag{3.1}
\]
Depth \(\delta_A(j)\) means both raw streams of an \(A\)-state through \(r+js\) bits; depth \(\delta_B(j)\) means both raw streams of a \(B\)-state through \(js\) bits. They satisfy \(\delta_A(j)-\delta_B(j)=s\) and \(\delta_B(j)-\delta_A(j-1)=s\). The *radius* of a position on a path is its smaller distance, in edges, to the two ends. A path is *immersed* if it never traverses an edge and immediately its reverse.

**Lemma 3.1** (padded-prefix recovery; [OpenAI-BCI, Lemma 2.4]). Let two immersed paths in \(X^{\rm surv}\) have the same oriented label word. At corresponding \(A\)-positions of radius at least \(2j+1\), the two states agree in both raw streams through \(r+js\) bits. At corresponding \(B\)-positions of radius at least \(2j\), they agree in both raw streams through \(js\) bits. The heights of the two states may differ.

*Proof.* The orientation of a label identifies the side, and the label identifies the family, both names, the extra and every universal rule. At an interior position, the two incident edges have distinct names on the side of that position: equal names would give the same slot (on side \(B\) the bucket is part of the label head), and the one edge at that slot (Lemma 1.1) would make the path backtrack. By the injectivity of the coefficient pools, the two coefficients are distinct.

For an incident name \(\nu\), rewrite the evaluation block in raw coordinates as
\[
\begin{aligned}
v+K_\nu u&=R_\nu+C^v_\nu\\
&\quad+K_\nu C^u_\nu ,
\end{aligned}\tag{3.2}
\]
where \(R_\nu\) is the right side of the edge equation in that block. If \(R_\nu\) and the offsets are known for both incident names, subtracting the two equations gives \((c_1-c_2)u\) and hence the raw input block \(u\), and then either equation gives the raw evaluation block. This holds for full padded blocks, also where an actual state has only a partial active block.

*Radius one.* At an \(A\)-position the two first evaluations are the two label heads, and the initial offsets vanish; this recovers \(u_{A,0}\) and the first \(r\) bits of \(v_A\).

*\(B\)-positions of radius \(2j\), \(j\ge1\).* Both neighbors are \(A\)-positions of radius at least \(2j-1\), so by induction their raw streams agree through \(r+(j-1)s\) bits, that is, through \(A_{j-1}\); the central state agrees through \(B_{j-1}\). The \(B\)-evaluation block of index \(2j-1\) is, on the right of (4.3), the transformed block \(A_{j-1}\) of the neighbor (or \(h_0'\) and \(A_0\) when \(j=1\)). Its table key consists of the neighbor's \(A\)-blocks before \(A_{j-1}\) and the central blocks \(B_1,\ldots,B_{j-1}\), and its argument is the neighbor's corrected \(A_{j-1}\), all known; the gates and offsets read still earlier raw blocks. So both right sides of (3.2) are known, and the central block \(B_j\) is recovered, identically along the two paths.

*\(A\)-positions of radius \(2j+1\).* Both neighbors have radius at least \(2j\) and agree through \(B_j\); the central state agrees through \(A_{j-1}\). The \(A\)-evaluation block of index \(2j\) is the transformed neighbor block \(B_j\), with key made of the central \(A_0,\ldots,A_{j-1}\) and the neighbor's \(B_1,\ldots,B_{j-1}\). Subtraction recovers the central \(A_j\).

The induction runs over individual source blocks. At each step the keys and arguments are known before any new output is used, and the universal rules are identical along the two paths, also at marks lying beyond the support of one of the states. Padding therefore causes no exception. \(\square\)

## 4. Separation of heights

Recovery determines the state at the middle of a long word, but not yet its height: a shorter state might coincide with the padded prefix of a longer one. The following deletion excludes exactly this. Put \(\eta_{\rm sep}=1/2500\). For a vertex on side \(C\in\{A,B\}\) at height \(i\), and each \(i'<i\) with \(i'\equiv i\pmod M\), let
\[
\begin{gathered}
\Delta=\ell_C(i)-\ell_C(i')\\
=(i-i')b/2,\\
q(i,i')\\
=\lfloor\min\{\eta_{\rm sep}H_{i'},\Delta\}\rfloor .
\end{gathered}\tag{4.1}
\]
(The second equality holds because \(b(i-i')\) is a multiple of \(bM\), hence of \(2s\), so both streams grow by the same amount.) *Delete* the vertex if its \(q(i,i')\) raw input bits immediately after position \(\ell_C(i')\) of its own input stream are all zero; these are active bits at height \(i\). Let \(X^{\rm good}\) be the graph induced on the vertices surviving the gate and separation deletions.

**Lemma 4.1** (separation budget; [OpenAI-BCI, Lemma 2.5]). The fraction of either side at any height deleted for separation is at most
\[
\begin{aligned}
\varepsilon_{\rm sep}=2\Bigl(&\frac{2^{-Mb/2}}{1-2^{-Mb/2}}\\
&+\frac{2^{-\eta_{\rm sep}H_0}}{1-2^{-\eta_{\rm sep}b}}\Bigr).
\end{aligned}\tag{4.2}
\]

*Proof.* The raw coordinates of a uniform state are independent uniform bits, so the test for \(i'\) fails with probability \(2^{-q(i,i')}\). For real \(x,y\), \(2^{-\lfloor\min\{x,y\}\rfloor}\le2\cdot2^{-\min\{x,y\}}\), and this is at most \(2(2^{-x}+2^{-y})\). The terms \(2^{-\Delta}\) over \(i'=i-M,i-2M,\ldots\) sum to at most \(2^{-Mb/2}/(1-2^{-Mb/2})\), and the terms \(2^{-\eta_{\rm sep}H_{i'}}\), even summed over all \(i'\ge0\), to \(2^{-\eta_{\rm sep}H_0}/(1-2^{-\eta_{\rm sep}b})\), since \(H_{i'}=H_0+bi'\). \(\square\)

## 5. The labelled tower

Put \(m_i=H_i/\log q\), the scale of height \(i\) measured in edges, and require, by taking \(s\) large,
\[
a:=\frac b{\log q}\le10^{-6}.\tag{5.1}
\]

**Proposition 5.1** (the labelled tower; [OpenAI-BCI, Proposition 2.6]). For every finite set of types and every large \(s\) as above:

1. The state sizes are those of Lemma 1.1 of the previous lesson. In a fixed extra slice an incidence has degrees \(d,D\); without slicing, the smaller endpoint has \(2^b\) times more slots. The total degree of a vertex is at most \(T2^bd\) on side \(A\) and \(T2^bD\) on side \(B\).
2. The labelling of \(X^0\), and of every induced subgraph, is *folded*: no two edges leaving a vertex carry the same label. The signed alphabet \(\mathcal S\) satisfies
\[
\begin{gathered}
|\mathcal S|\le2TM2^bd\,2^r,\\
\frac{\sqrt{|\mathcal S|}}q\le2^{O_{T,b}(1)}\\
\times2^{-.000025s+O(\log s)} .
\end{gathered}\tag{5.2}
\]
3. At every height, the fraction of vertices removed on each side is at most \(\varepsilon_{\rm gate}+\varepsilon_{\rm sep}\), which can be made as small as desired, uniformly in the height and the tables, by taking \(s\) and then \(n_0\) large. The conclusions of Lemma 2.1 on surviving slots hold.
4. Every immersed path in \(X^{\rm good}\) that starts at height \(i\) and has length at least \(\lceil1.002\,m_i\rceil\) is the only immersed path with its oriented word anywhere in \(X^{\rm good}\).

*Proof.* (1) is Lemma 1.1: at a larger endpoint the state fixes the extra, at a smaller one the extra is part of the slot. (2) At an \(A\)-endpoint, equal labels give the same family, serial number and extra, hence the same slot; at a \(B\)-endpoint they give the bucket as well. Each slot carries one edge, so the labelling is folded, and induced subgraphs inherit this. Counting (2.1) of the previous lesson, there are at most \(TM\cdot d\cdot2^b\cdot2^r\) positive labels. Since \(\log d+r=1.00005s\) and \(\log(q^2)=1.0001s\), and \(TM2^b\) contributes \(O(\log s)+O_{T,b}(1)\) to the logarithm, (5.2) follows. (3) is Lemmas 2.1 and 4.1; the first term of (4.2) is small for large \(s\) because \(Mb=2\cdot10^6sb\), and the second for large \(n_0\), since \(H_0\ge2n_0s\).

(4) Let \(N=\lceil1.002m_i\rceil\), and compare the first \(N\) edges of the given path with any immersed path with the same word. The middle positions have radius at least \(\lfloor N/2\rfloor\). If the first path's middle position has height \(j\), then, since heights change by at most one per edge,
\[
H_j\le H_i+bN\le(1+1.002a)H_i+b .
\]
By Lemma 3.1 the two middle states agree through an aligned depth \(\delta\) (in the sense of (3.1)) with
\[
\begin{gathered}
\delta\ge s(N/2-2)\ge\tfrac{1.002}{1.0001}H_i-2s\\
\ge1.001\,H_j,
\end{gathered}
\]
using \(sN/2\ge1.002H_i/(2\cdot.50005)\), \(a\le10^{-6}\) and \(H_i\ge(2n_0+1)s\ge2\cdot10^6s\).

For every height, \(H=\ell_A+\ell_B+s-r\) and \(r-s\le\ell_A-\ell_B\le r\) give
\[
\begin{gathered}
\ell_A\le H/2+.1s,\quad|v_A|\le H/2+.6s,\\
\ell_B\le H/2,\quad|v_B|\le H/2+.5s .
\end{gathered}
\]
An aligned \(A\)-depth \(\delta\) covers \(\delta/2+.1s\) bits of each stream, and a \(B\)-depth \(\delta/2\) bits. Since \(\delta\ge1.001H_j\) and \(H_j\ge1000s\), this covers every coordinate of a state at height \(j\).

The labels determine the height residues modulo \(M\), so the two middle states have congruent heights. Suppose they differ, with heights \(i_-<i_+\); note \(i_-\le j\). The test of (4.1) at the larger state, for \(i'=i_-\), concerns raw input bits of its side \(C\) from \(\ell_C(i_-)\) to at most
\[
\begin{gathered}
\ell_C(i_-)+\eta_{\rm sep}H_{i_-}\\
\le(\tfrac12+\eta_{\rm sep})H_{i_-}+.1s .
\end{gathered}
\]
Since \(H_{i_-}\le H_j\) and \(2\eta_{\rm sep}<0.001\), this interval lies inside the recovered prefix. There the smaller state is padded with zeros, so the larger state has zeros on the whole tested interval and would have been deleted. This contradiction shows that the heights are equal, and then the two middle states are equal. Foldedness identifies the two paths edge by edge in both directions from the middle, and determines any longer path with the same word. \(\square\)

**Remark 5.2** (terminal dimensions). In a state, the input and evaluation lengths of the last block differ. On the side whose last active input block has \(t\) coordinates, the last pair \((u,v)\) of blocks has dimensions \((t,s)\); on the other side it has dimensions \((0,t)\). Two independent incident evaluations of a full padded block determine \((u,v)\) uniquely, but only states with zero inactive coordinates exist. On the first side this imposes \(s-t\) conditions, because multiplication by a nonzero coefficient difference is injective on the \(t\)-dimensional active subspace; on the second it imposes \(t\) conditions, the equality of two \(t\)-bit evaluations. Together they are exactly \(s\) conditions. These counts are the source of the probability estimates of the pruning lessons [OpenAI-BCI, Remark 2.7].

## 6. Exercises

**Exercise 6.1.** In the proof of Lemma 1.1, why is it important that the twenty indices after a mark are identities unconditionally, rather than gated by the rule (4.1) of the previous lesson?

**Exercise 6.2.** Show that two different slots at one vertex of \(X^0\) carry different labels, and that a label and a vertex determine at most one edge.

**Exercise 6.3.** Compute \(\varepsilon_{\rm gate}\) as a power of two in terms of \(s\), and show that it tends to zero as \(s\to\infty\) for fixed \(T,b\).

**Exercise 6.4.** In Proposition 5.1(4), what goes wrong without the separation deletion? Construct, for two heights \(i'<i\) with \(i'\equiv i\pmod M\), a state at height \(i\) whose recovered prefix of depth \(1.001H_j\) agrees with a state at height \(i'\).

**Exercise 6.5.** Show that \(2^{-\lfloor\min\{x,y\}\rfloor}\le2(2^{-x}+2^{-y})\) for all real \(x,y\).

## 7. Solutions

**6.1.** The raw extra bits of the larger endpoint may lie one index after the mark, and a gate at index \(k\) reads indices up to \(k-5\). So a gate at an index between \(\kappa+6\) and \(\kappa+20\) could be opened by those raw bits. Its corrected input block is zero, but a permutation of the block may move the zero block to a nonzero one; the transformed stream would then be nonzero beyond the common cutoff, and the evaluation stream solved from (4.3) could leave the state space. Unconditional identities exclude this, and from index \(\kappa+21\) on the gates read only indices from \(\kappa+8\) on, beyond the raw support.

**6.2.** At an \(A\)-vertex a label determines the family, the serial number and the extra, and the type is part of the family; so it determines the slot. At a \(B\)-vertex it also determines the bucket. Lemma 1.1 gives one edge per slot.

**6.3.** \(\varepsilon_{\rm gate}=600T2^b2^{.60005s}2^{-8s}\), that is, \(600T2^{b-7.39995s}\), which tends to zero.

**6.4.** Take a state \(w\) at height \(i'\), and let \(w^+\) be the state at height \(i\) whose streams are those of \(w\), padded with zeros to the lengths at height \(i\). Every prefix of \(w\) agrees with the same prefix of \(w^+\), so recovery cannot distinguish them; the separation test for \(i'\) deletes \(w^+\), because its bits after \(\ell_C(i')\) are zero.

**6.5.** Since \(\lfloor m\rfloor>m-1\), \(2^{-\lfloor m\rfloor}<2\cdot2^{-m}\) with \(m=\min\{x,y\}\), and \(2^{-m}=\max\{2^{-x},2^{-y}\}\le2^{-x}+2^{-y}\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 2.4-2.7, Lemmas 2.2-2.5, Proposition 2.6, Remark 2.7. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
