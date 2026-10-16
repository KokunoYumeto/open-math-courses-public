# Coherent returns, reconstruction and accumulated rank

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The labelled tower still contains short cycles and short *bicycles*. The pruning removes them by deleting the vertices of every short bad configuration; it must remove an arbitrarily small fraction of every layer. This is a first-moment count: the expected number of bad configurations rooted in a layer must be much smaller than the layer. The count separates *choices* from *constraints*. Once the labels and heights of a configuration are fixed, two incident evaluations reconstruct the state at each vertex, so the only free choices are a few endpoint bits; the constraints are the conditions that the reconstructed states really are states, with zero inactive coordinates, and these have small probability. This lesson defines the configurations counted first, *coherent returns*, proves that a pattern has at most one realization, and gives the probabilistic tool that multiplies the probabilities of constraints tested at successive source blocks [OpenAI-BCI, Sections 4.1-4.3].

- Depth and its propagation along edges (Section 1).
- Bands and coherent returns (Section 2).
- Patterns and their reconstruction (Section 3).
- Accumulated rank (Section 4).

The setting of the previous lessons is in force: the tower with its universal rules, the law of Proposition 6.1 of [Expansion and the sequential law](expansion-and-the-sequential-law.md) on the tables, and the graph \(X^{\rm good}\) of [Auxiliary incidences, deletions and recovery](auxiliary-incidences-deletions-and-recovery.md), defined for every realization of the tables. That a path lies in \(X^{\rm good}\) is used only as a condition on the configurations counted, never to condition the law of the tables. Lengths count edges. A *bicycle* is a finite connected graph of cycle rank two without vertices of valence one ([The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md), Section 3).

## 1. Depth and its propagation

Use the aligned depths of (3.1) of the lesson on auxiliary incidences: for an \(A\)-vertex, agreement to depth \((2j+1)s\) means agreement of both raw streams through \(r+js\) bits; for a \(B\)-vertex, agreement to depth \(2js\) means agreement of both raw streams through \(js\) bits. Depth is measured in state bits: on side \(A\) it is the number of specified bits minus \(2r-s\). Let \(D(v)\) be the largest aligned depth whose prefixes are active at \(v\).

**Lemma 1.1** (available depth). For \(v\in\mathscr A_i\sqcup\mathscr B_i\),
\[
H_i-2s\le D(v)\le H_i .\tag{1.1}
\]

*Proof.* Use the cutoff forms of Lemma 1.1 of [Streams, coefficient pools and universal corrections](streams-coefficient-pools-and-universal-corrections.md). In form (B), \(H_i=(2n+1)s+t\); an \(A\)-vertex has \(\ell_A=r+ns\), so \(D=(2n+1)s=H_i-t\); a \(B\)-vertex has \(\ell_B=ns+t\) and \(|v_B|=(n+1)s\), so \(D=2ns=H_i-s-t\) if \(t<s\) and \(D=2(n+1)s=H_i\) if \(t=s\). In form (A), \(H_i=(2n+2)s+t\); a \(B\)-vertex has \(\ell_B=(n+1)s\) and \(D=H_i-t\); an \(A\)-vertex has \(\ell_A=r+ns+t\) and \(|v_A|=r+(n+1)s\), so \(D=(2n+1)s=H_i-s-t\) if \(t<s\) and \(D=H_i\) if \(t=s\). In all cases \(0\le H_i-D(v)\le2s\). \(\square\)

**Lemma 1.2** (propagation). Let two vertices on the same side agree to an available depth, and follow from each an edge with the same label. If they agree through \(A_j\) (both raw \(A\)-streams through \(r+js\)), the endpoints agree through \(B_j\); if they agree through \(B_j\), the endpoints agree through \(A_{j-1}\). Each step loses exactly \(s\) of aligned depth, and the propagated prefixes are available at the new vertices.

*Proof.* Through \(A_j\): the corrected evaluations agree through \(r+js\), because the label is the same and the offsets read earlier raw blocks of the agreeing prefixes. After removing the common label head, successive inversion of the transformations recovers the \(B\)-inputs through \(B_j\), and the \(B\)-evaluation through position \(js\) uses \(A\)-inputs only through \(A_{j-1}\). So the endpoints agree through \(B_j\). Through \(B_j\): the \(B\)-evaluation through \(js\) determines the \(A\)-inputs through \(A_{j-1}\), and the \(A\)-evaluation through \(r+(j-1)s\) uses \(B\)-inputs only through \(B_{j-1}\). The depths are \((2j+1)s\to2js\to(2j-1)s\). An edge changes the height by at most one, so the cutoff moves by at most \(b<s\), while one whole block of depth has been given up; the propagated prefixes are therefore active at the new vertices. \(\square\)

## 2. Bands and coherent returns

For \(k\ge0\) put
\[
\begin{gathered}
T_k=H_0(11/10)^k,\qquad I_k=[\tfrac56T_k,\tfrac65T_k],\\
M_k=T_k/25 .
\end{gathered}
\]
A vertex belongs to *band* \(k\) when its scale \(H_i\) lies in \(I_k\). A scale belongs to at most four bands, since \(H\in I_k\) means \(T_k\in[\frac56H,\frac65H]\), an interval of ratio \(1.44<1.1^4\). For \(H_i\in I_k\),
\[
\tfrac1{30}\le\frac{M_k}{H_i}\le\tfrac6{125}<0.05 .\tag{2.1}
\]
If a finite subgraph through a vertex of height \(i\) has at most \(7m_i\) edges, where \(m_i=H_i/\log q\), its scales vary by at most \(7bm_i=7bH_i/(.50005s)\). For \(b/s\) small, choosing \(k\) with \(T_k\le H_i<T_{k+1}\) puts all its scales strictly inside \(I_k\). So every short configuration used below lies in one band, with room at both ends.

**Definition 2.1** (coherent return). In band \(k\), a *coherent return* is a nonbacktracking path \(v_0,e_1,v_1,\ldots,e_p,v_p\) with \(p\ge1\) in \(X^{\rm good}\), all of whose vertices lie in band \(k\), whose endpoints lie on the same side and agree to an available aligned depth \(h\) with
\[
\begin{gathered}
h\ge\frac{ps}2+M_k,\\
h\le\min\{D(v_0),D(v_p)\}.
\end{gathered}\tag{2.2}
\]
It is *minimal* if no proper contiguous subpath of positive length is a coherent return for the same band. Closed nonbacktracking paths, \(v_0=v_p\), are included whenever the depth condition holds.

The endpoints lie on the same side, so \(p\) is even. For a fixed length, side and band we always take the least aligned depth \(h\) satisfying the first inequality of (2.2); it exceeds \(ps/2+M_k\) by less than \(2s\), so it is not an additional parameter. Every coherent return contains a minimal one: take a shortest contiguous subpath that is a coherent return.

The threshold is chosen so that returns are rare. At the leading exponential scale, a length-\(p\) pattern at scale \(H\) costs about \(ps\) bits of label choices and \(H-h\) bits of free endpoint coordinates, while the terminal conditions impose about \(ps/2\) bits of constraints. The inequality \(h\ge ps/2+M_k\) leaves an exponent about \(H-M_k\), below the size \(2^H\) of a layer.

**Lemma 2.2** (the junction coefficients differ; [OpenAI-BCI, Lemma 4.2]). In a minimal coherent return, the names of the first edge at \(v_0\) and of the last edge at \(v_p\) (both read from the endpoint into the path) are different.

*Proof.* The coefficient pools are injective on all names, so equal names give the same family, serial number and extra, and on side \(B\) the same bucket. At an \(A\)-endpoint the label head is the first \(r\) bits of the corrected evaluation, which the two endpoints share since they agree to depth at least \(s\); at a \(B\)-endpoint the remaining part \(h_0'\) of the head is the first \(s-r\) bits of the evaluation, and the bucket is in the name. So equal names give the same full label on both edges, read from the endpoints. Remove one edge at each end. By Lemma 1.2 the new endpoints \(v_1,v_{p-1}\) agree to depth at least \(h-s\), available at both, and the new threshold is \((p-2)s/2+M_k=ps/2+M_k-s\), which is at most \(h-s\). The shorter path lies in the same band and in \(X^{\rm good}\). If \(p>2\), it is a proper coherent return, contradicting minimality. If \(p=2\), the two edges at the middle vertex \(v_1\) carry the same label read from \(v_1\), so by foldedness they are the same edge, and the path backtracks. \(\square\)

## 3. Patterns and their reconstruction

Once the labels and heights are fixed, two incident evaluations reconstruct the state at every vertex of a configuration. A coherent return leaves only the raw input bits beyond the common endpoint prefix to be chosen; a theta, the bicycle with two vertices of valence three, has no free bits. A reconstruction need not lie in the state spaces: its terminal coordinates must vanish beyond the cutoffs, and at a branch vertex of a theta the third incident evaluation must agree with the first two. These are the constraints whose probabilities are estimated.

**Patterns.** A *path pattern* consists of the length \(p\), the initial side and height, the band, the oriented labels of the edges, and for each edge the height of its endpoint; the label leaves at most three choices of the next height. A *theta pattern* consists of three positive branch lengths, the position of the root in the abstract theta, the initial side and height, the oriented labels and the allowed height changes. A pattern fixes all slot names, coefficients, extras and cutoffs. Patterns with inconsistent labels or heights are rejected before any table is queried, and so are patterns in which two incident slots at an internal vertex, or two of the three slots at a branch vertex, have equal names: equal names are the same slot, which carries one edge, so a configuration in the graph would backtrack or identify two branches. At the coherent junction the same exclusion is justified by Lemma 2.2. No immersed path or embedded theta is lost.

The number of choices of an oriented label together with the next height is at most \(L_s\), where, for large \(s\) after the type data are fixed,
\[
L_s\le2^{1.001s} .\tag{3.1}
\]
Indeed \(L_s\le3|\mathcal S|\), and \(\log|\mathcal S|\le1.00005s+O(\log s)\) by Proposition 5.1 of the lesson on auxiliary incidences. This loose bound is used only for counting.

**Free endpoint bits.** For a coherent return the endpoints are identified only through depth \(h\). Beyond that depth, all their remaining active raw input bits are chosen freely and fixed as part of the pattern; their inactive input bits are zero. There are no free evaluation bits. For a theta there are no free bits.

**Lemma 3.1** (unique reconstruction and the free-bit count; [OpenAI-BCI, Lemma 4.3]). Fix a path pattern with different junction names, and its free endpoint bits. For every realization of the tables there is at most one assignment of states realizing the pattern as a coherent return. If the endpoint scales are \(H_-\) and \(H_+\), the number of free bits is at most
\[
\frac{H_-+H_+}2-h .\tag{3.2}
\]
A theta pattern has at most one realizing assignment and no free bits. In both reconstructions, the inputs and keys queried at a source index are determined before the tables of that index are used.

*Proof.* At every internal vertex use its two incident slots; at a branch vertex of a theta choose two of its three; at the coherent junction use the two end slots, through depth \(h\); beyond depth \(h\), each endpoint uses its prescribed input block and its single incident evaluation.

Proceed in the source order \(A_0,B_1,A_1,B_2,\ldots\), at all vertices of the configuration at once. At an \(A\)-vertex the two evaluation heads are known from the labels; with coefficients \(c_1\ne c_2\), subtraction recovers the raw block \(A_0\) of the input and then of the evaluation. At later blocks the known offsets are moved to the right sides, which gives two equations
\[
\begin{gathered}
v+c_1u=E_1,\\
v+c_2u=E_2 ,
\end{gathered}\tag{3.3}
\]
with \(c_1-c_2\) a nonzero field element, invertible on the full padded block:
\[
\begin{gathered}
u=(c_1-c_2)^{-1}(E_1-E_2),\\
v=E_1-c_1u .
\end{gathered}
\]
At a free endpoint beyond depth \(h\), \(u\) is prescribed and one equation gives \(v\). The update of a \(B\)-block \(B_j\) uses the values of the tables of index \(2j-2\) at the neighboring blocks \(A_{j-1}\), already recovered; the update of \(A_j\) uses the tables of index \(2j-1\) at the blocks \(B_j\) just recovered. Every key consists of raw blocks of smaller index, and every correction gate ends before both coupled blocks; so all inputs, keys and gates are known before the current tables are read. This proves uniqueness by induction over the source indices.

The same induction is an unambiguous *formal* reconstruction when the pattern is not realized: solve on full padded blocks, stop after the blocks that can meet the candidate cutoffs, and test the required zeros, labels and vertex conditions afterwards. An assignment violating such a condition need not define vertices, but it causes no ambiguity in the earlier query data. Every actual realization is produced by the induction, so the number of realizations is bounded; ignoring some final conditions only increases the counts.

For the free bits, \(r-s\le\ell_A(i)-\ell_B(i)\le r\) and \(H_i=\ell_A(i)+\ell_B(i)+s-r\) give
\[
\begin{gathered}
\ell_A(i)\le\frac{H_i}2+\frac{2r-s}2,\\
\ell_B(i)\le\frac{H_i}2 .
\end{gathered}
\]
At aligned depth \(h\) an \(A\)-endpoint has \((h+2r-s)/2\) specified input bits and a \(B\)-endpoint has \(h/2\). So an endpoint of scale \(H\) has at most \((H-h)/2\) free input bits, and the two endpoints together at most (3.2). A theta has two chosen evaluations at every vertex and no prescribed coordinates. \(\square\)

## 4. Accumulated rank

Let \(\mathcal F_{<t}\) be generated by all tables at source indices before \(t\), in all families, together with the fixed pattern data. By the last assertion of Lemma 3.1, the keys, input arguments, gates, coefficients and the widths of the tests at index \(t\) are \(\mathcal F_{<t}\)-measurable; in particular no evaluation solved from a current table enters a current key. Proposition 6.1 of [Expansion and the sequential law](expansion-and-the-sequential-law.md) gives, for an event \(\mathcal B_t\) involving \(k_t\) whole current tables,
\[
\begin{aligned}
&\mathbb P(\mathcal B_t\mid\mathcal F_{<t})\\
&\quad\le e^{\varepsilon_sk_t}\,\mathbb P_{\rm prod}(\mathcal B_t\mid\mathcal F_{<t}),
\end{aligned}\tag{4.1}
\]
with \(\varepsilon_s\to0\), where \(\mathbb P_{\rm prod}\) is the law of independent uniform current tables, the earlier tables being fixed. The bound may be applied to any event determined by the current tables, such as a linear compatibility condition on several of their outputs; untested entries of the tables are integrated out. It is not a statement about one entry of a permutation after its other entries are prescribed.

**Lemma 4.1** (predictable accumulated rank; [OpenAI-BCI, Lemma 4.4]). Suppose that at each of finitely many source indices \(t\) a test is selected, determined by \(\mathcal F_{<t}\), whose probability under \(\mathbb P_{\rm prod}(\cdot\mid\mathcal F_{<t})\) is at most \(2^{-R_t}\), where the nonnegative integers \(R_t\) and \(k_t\) (the number of whole tables involved) are \(\mathcal F_{<t}\)-measurable. If an event \(\mathcal A\) implies that all the tests pass, that \(\sum_tR_t\ge R\) and that \(\sum_tk_t\le K\), then
\[
\mathbb P(\mathcal A)\le e^{\varepsilon_sK}2^{-R} .
\]
The event \(\mathcal A\) may impose further conditions, such as minimality, gate conditions, or consistency of the reconstructed states.

*Proof.* Define a process \(Y\): \(Y_0=1\); at index \(t\), if the test fails put \(Y_t=0\), and otherwise \(Y_t=Y_{t-1}\,2^{R_t}e^{-\varepsilon_sk_t}\). Since \(R_t,k_t\) and the test are determined before index \(t\), (4.1) gives
\[
\begin{gathered}
\mathbb E(Y_t\mid\mathcal F_{<t})\le Y_{t-1}2^{R_t}e^{-\varepsilon_sk_t}\\
\cdot e^{\varepsilon_sk_t}2^{-R_t}=Y_{t-1},
\end{gathered}
\]
so \(\mathbb EY_{\rm final}\le1\). On \(\mathcal A\) every test passes, so \(Y_{\rm final}=2^{\sum R_t}e^{-\varepsilon_s\sum k_t}\ge2^Re^{-\varepsilon_sK}\). Markov's inequality gives the claim. The further conditions of \(\mathcal A\) enter only in this last lower bound, not in any conditional probability. \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that the least aligned depth \(h\ge ps/2+M_k\) is less than \(ps/2+M_k+2s\), and that on side \(A\) it is an odd multiple of \(s\).

**Exercise 5.2.** In the proof of Lemma 2.2 with \(p=2\), describe the path \(v_0,e_1,v_1,e_2,v_2\) and explain why foldedness forces \(e_2=\bar e_1\).

**Exercise 5.3.** Show that Lemma 4.1 fails if the test at an index may depend on the outcome of the current tables.

**Exercise 5.4.** Check the count \(\ell_A(i)\le H_i/2+(2r-s)/2\) on the two cutoff forms.

## 6. Solutions

**5.1.** On side \(A\) the aligned depths are \((2j+1)s\) and on side \(B\) they are \(2js\); consecutive aligned depths on one side differ by \(2s\), so the least one above a given number exceeds it by less than \(2s\).

**5.2.** The endpoints \(v_0,v_2\) lie on one side, and \(v_1\) on the other. The label of \(e_1\) read from \(v_0\) equals the label of \(\bar e_2\) read from \(v_2\); hence the labels of \(\bar e_1\) and \(e_2\) read from \(v_1\) are equal (both are the inverse label). Foldedness at \(v_1\) says that at most one edge leaves \(v_1\) with that label, so \(e_2=\bar e_1\): the path backtracks.

**5.3.** Let the only current table be a uniform bit \(X\). If the test could be chosen as "\(X\) equals the value it actually takes", with rank \(R=1\), it would pass for every outcome, and the sure event would receive the bound \(2^{-1}\). Predictability excludes this: a test fixed before \(X\) is drawn, such as "\(X=0\)", passes with probability exactly \(\frac12\).

**5.4.** In form (B), \(\ell_A=r+ns\) and \(H_i=(2n+1)s+t\), so \(H_i/2+(2r-s)/2=r+ns+t/2\ge\ell_A\). In form (A), \(\ell_A=r+ns+t\) and \(H_i=(2n+2)s+t\), so \(H_i/2+(2r-s)/2\) equals \(r+ns+s/2+t/2\), which is at least \(\ell_A\) because \(t\le s\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 4.1-4.3, Definition 4.1, Lemmas 4.2-4.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
