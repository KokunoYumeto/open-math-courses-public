# Streams, coefficient pools and universal corrections

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group of this course is built from an infinite layered graph, the *tower*, whose vertices are pairs of bit strings and whose edges are solutions of explicit equations. This lesson sets up the vertex sets and the edge equations. Two evaluations of a vertex state with different field coefficients determine the state block by block: over a finite field, \(E_1=v+c_1u\) and \(E_2=v+c_2u\) with \(c_1\ne c_2\) give \(u=(c_1-c_2)^{-1}(E_1-E_2)\) and then \(v\). The labels of the edges supply such evaluations, and the next lesson turns this into recovery of long paths from their words. The edge equations couple each evaluation to a permuted input stream at the other endpoint; *gates* switch the permutations off on zero data, and *universal corrections* make one system of equations serve all heights at once [OpenAI-BCI, Sections 2.1-2.3].

- Parameters, stream lengths and cutoffs (Section 1).
- Types, families, extra coordinates, slots and labels (Section 2).
- Coefficient pools (Section 3).
- Gates, corrections, permutation tables and the edge equations (Section 4).

We use the existence of a field with \(2^h\) elements for every \(h\ge1\), from the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40) (Judson, *Abstract Algebra: Theory and Applications*, [Theorem 22.1.6](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)), and the concentration bound for sampling without replacement, Lemma 5.1 of [Streams, slots and slot evaluations](course:kadison-kaplansky-projections/streams-slots-and-slot-evaluations#5-concentration-for-sampling-with-and-without-replacement). All logarithms have base two.

## 1. Parameters and streams

Fix a positive integer \(b\); it is chosen once, in the lesson [Expansion and the sequential law](expansion-and-the-sequential-law.md), and never changed. Let \(s\) be a large multiple of \(20000\) and of \(5b\), and put
\[
\begin{gathered}
r=\tfrac35s,\enspace d=2^{.40005s},\\
D=2^{.60005s},\enspace q=2^{.50005s}.
\end{gathered}\tag{1.1}
\]
The exponents are integers because \(.40005s=8001s/20000\), and similarly for the others; \(r\) is a multiple of \(b\), and \(q=\sqrt{dD}\). The numbers \(d,D\) will be the degrees of an incidence on its two sides, and \(q\) their geometric mean. Choose an integer \(n_0\ge10^6\), to be increased later. For \(i\ge0\) write \(bi=2sa_i+t_i\) with \(0\le t_i<2s\), and define the *stream lengths*
\[
\begin{aligned}
\ell_A(i)&=r+n_0s+a_is\\
&\quad+\max\{t_i-s,0\},\\
\ell_B(i)&=n_0s+a_is\\
&\quad+\min\{t_i,s\}.
\end{aligned}\tag{1.2}
\]
The vertex sets of the tower at *height* \(i\) are
\[
\begin{gathered}
\mathscr A_i=\mathbb F_2^{\ell_A(i)}\times\mathbb F_2^{r+\ell_B(i)},\\
\mathscr B_i=\mathbb F_2^{\ell_B(i)}\times\mathbb F_2^{s-r+\ell_A(i)} .
\end{gathered}
\]
A state is written \((u,v)\): \(u\) is the *input* and \(v\) the *evaluation* coordinate. Each coordinate is regarded as an infinite bit stream by adjoining zeros, the *padding*. The coordinates on side \(A\) are cut into an initial block \(A_0\) of length \(r\) followed by blocks \(A_1,A_2,\ldots\) of length \(s\); those on side \(B\) into blocks \(B_1,B_2,\ldots\) of length \(s\). The blocks of the two input streams are interleaved in the *source order*
\[
\begin{gathered}
A_0\ (0),\ B_1\ (1),\ A_1\ (2),\\
B_2\ (3),\ A_2\ (4),\ \ldots,
\end{gathered}\tag{1.3}
\]
so that \(A_j\) has *source index* \(2j\) and \(B_j\) has source index \(2j-1\). Evaluation blocks are indexed in the same way: the block of \(v_A\) in the positions of \(A_j\) has index \(2j\), and the block of \(v_B\) in the positions of \(B_j\) has index \(2j-1\). Put
\[
\begin{gathered}
L_i=r+2n_0s+bi,\\
H_i=L_i+s-r=(2n_0+1)s+bi .
\end{gathered}
\]
The number \(H_i\) is the *scale* of height \(i\); it grows by \(b\) from one height to the next.

**Lemma 1.1** (sizes and cutoffs). For every \(i\ge0\):

1. \(\ell_A(i)+\ell_B(i)=L_i\), \(|\mathscr B_i|=2^{H_i}\) and \(|\mathscr A_i|=2^{H_i+2r-s}\).
2. The active coordinates of the two input streams form an initial segment of the source order (1.3), of total length \(L_i\). There are \(n\ge n_0-1\) and \(t\in\{b,2b,\ldots,s\}\) such that one of the two *cutoff forms* holds:
\[
\begin{array}{c|cc}
&\text{(B)}&\text{(A)}\\\hline
\ell_A&r+ns&r+ns+t\\
\ell_B&ns+t&(n+1)s\\
|v_A|&r+ns+t&r+(n+1)s\\
|v_B|&(n+1)s&(n+1)s+t
\end{array}
\]
In form (B) the last active input block is \(B_{n+1}\) with \(t\) active coordinates; in form (A) it is \(A_{n+1}\).
3. From height \(i\) to \(i+1\) exactly one of \(\ell_A,\ell_B\) grows, by \(b\).

*Proof.* (1) For \(0\le t<2s\), \(\max\{t-s,0\}+\min\{t,s\}=t\), so \(\ell_A+\ell_B=r+2n_0s+2a_is+t_i=L_i\). Then \(\log|\mathscr B_i|=\ell_B+s-r+\ell_A=H_i\) and \(\log|\mathscr A_i|=\ell_A+r+\ell_B=L_i+r\), which is \(H_i+2r-s\).

(2) Put \(n'=n_0+a_i\). If \(0<t_i\le s\), then \(\ell_A=r+n's\) and \(\ell_B=n's+t_i\): form (B) with \(n=n'\), \(t=t_i\). If \(s<t_i<2s\), then \(\ell_A=r+n's+(t_i-s)\) and \(\ell_B=(n'+1)s\): form (A) with \(n=n'\), \(t=t_i-s\). If \(t_i=0\), then \(\ell_A=r+n's\) and \(\ell_B=n's\): form (A) with \(n=n'-1\), \(t=s\). In each case \(t\) is a multiple of \(b\) because \(b\) divides \(s\) and \(bi\). The evaluation lengths are \(|v_A|=r+\ell_B\) and \(|v_B|=s-r+\ell_A\). In form (B) the input streams are full through \(A_n\) and \(B_n\) and \(B_{n+1}\) has \(t\) coordinates; in form (A) they are full through \(B_{n+1}\) and \(A_{n+1}\) has \(t\) coordinates. Either way the active part is an initial segment of (1.3).

(3) Since \(s\) and \(t_i\) are multiples of \(b\): if \(t_i<s\), then \(t_{i+1}=t_i+b\le s\) and only \(\min\{t,s\}\) grows; if \(s\le t_i<2s-b\), only \(\max\{t-s,0\}\) grows; if \(t_i=2s-b\), then \(a_{i+1}=a_i+1\), \(t_{i+1}=0\), and \(\ell_A\) grows by \(b\) while \(\ell_B\) is unchanged. \(\square\)

## 2. Types, families, extras, slots and labels

Let \(\mathcal T\) be a fixed finite set of *incidence types*, \(T=|\mathcal T|\). A type \(\tau\) has an *offset* \(\delta_\tau\in\{-1,0,1\}\) and occurs between \(\mathscr A_i\) and \(\mathscr B_{i+\delta_\tau}\) whenever both indices are nonnegative; the pair is *adjacent* if \(\delta_\tau\ne0\) and of *equal height* otherwise. Its smaller height is \(h=\min\{i,i+\delta_\tau\}\). Put
\[
M=2\cdot10^6s .
\]
The *family* of the pair is \(f=(\tau,\,i\bmod M)\); there are at most \(TM\) families, and \(f\) determines the residues of both endpoint heights, of \(h\), and of \(bh\) modulo \(2s\).

**Extra coordinates.** In an adjacent pair, the endpoint at height \(h+1\) is the *larger* one. Truncating its state to the lengths at height \(h\) discards exactly \(b\) coordinates: by Lemma 1.1(3) exactly one input stream grows from \(h\) to \(h+1\); on side \(A\) the lengths are \((\ell_A,r+\ell_B)\) and on side \(B\) they are \((\ell_B,s-r+\ell_A)\), so the discarded coordinates are the last \(b\) active coordinates of \(u\) if that side's own input stream grows, and of \(v\) otherwise. They form one interval. Their value \(e\in\mathbb F_2^b\) is the *extra*. For an equal-height pair, \(e\) is the empty string. In a fixed *extra slice* (a fixed value of \(e\)), both truncated endpoint spaces are exactly the spaces at height \(h\).

**Slots.** A *slot* is a named candidate incidence at a vertex. At an \(A\)-endpoint a slot consists of the type and a serial number \(j\in\{1,\ldots,d\}\); at a \(B\)-endpoint it consists of the type, a serial number \(j\) and a *bucket* \(c\in\mathbb F_2^{2r-s}\). At the smaller endpoint of an adjacent pair the extra \(e\) is also part of the slot; at the larger endpoint \(e\) is read from the state. So in a fixed extra slice each type gives every \(A\)-vertex \(d\) slots and every \(B\)-vertex \(d\,2^{2r-s}=D\) slots, since \(2r-s=s/5\).

**Labels.** A *positive label* is
\[
\begin{gathered}
\lambda=(f,j,e,h_0),\\
h_0=c\Vert h_0',\\
|h_0|=r,\quad|h_0'|=s-r ,
\end{gathered}\tag{2.1}
\]
with \(f\) a family, \(j\) a serial number, \(e\) an extra of that family and \(h_0\) the *label head*; its first \(2r-s\) bits are the bucket \(c\). Every positive edge will run from its \(\mathscr A\)-endpoint to its \(\mathscr B\)-endpoint, and the reverse traversal reads the formal inverse label.

**Marks.** For each family and each occurrence of it, that is, each height pair of the family, *mark* its *common cutoff*: the end of the active initial segment of (1.3) at the smaller height \(h\), of length \(L_h\). Let \(\kappa\) be the source index of the last active block of that segment and \(t\in\{b,\ldots,s\}\) its number of active coordinates. At an adjacent occurrence also mark the interval of extra coordinates of the larger endpoint.

**Lemma 2.1** (marks). Within one family the side and the length \(t\) of the marked block are constant, and consecutive occurrences have marked indices exactly
\[
K=\frac{Mb}{s}=2\cdot10^6\,b\tag{2.2}
\]
apart. The active input coordinates of an occurrence extend at most one source block beyond its marked index, and its extra interval, if it lies in an evaluation stream, at most two source blocks beyond it.

*Proof.* Consecutive occurrences have smaller heights \(h\) and \(h+M\). Since \(bM=2s\cdot10^6b\) is a multiple of \(2s\), we have \(t_{h+M}=t_h\) and \(a_{h+M}=a_h+10^6b\), so both input lengths grow by \(10^6bs\), the cutoff form and \(t\) are unchanged, and \(\kappa\) grows by \(2\cdot10^6b\).

At the larger height the input streams have \(b\) more coordinates than at \(h\), on one side. In form (B) at \(h\) with \(t<s\) they lie in the same block \(B_{n+1}\); with \(t=s\) they are the first \(b\) coordinates of \(A_{n+1}\), one index later. In form (A) with \(t<s\) they lie in \(A_{n+1}\); with \(t=s\) in \(B_{n+2}\), one index later.

An extra interval in an evaluation stream occurs on side \(A\) when \(\ell_B\) grows, at positions \(r+\ell_B(h)\) to \(r+\ell_B(h)+b\) of \(v_A\), and on side \(B\) when \(\ell_A\) grows, at positions \(s-r+\ell_A(h)\) onward of \(v_B\). Using the table of Lemma 1.1: in form (B) with \(t<s\), \(\ell_B\) grows and the interval lies in the \(v_A\) block of index \(2n+2=\kappa+1\); in form (B) with \(t=s\), \(\ell_A\) grows and it lies in the \(v_B\) block of index \(2n+3=\kappa+2\); in form (A) with \(t<s\), \(\ell_A\) grows and it lies in the \(v_B\) block of index \(2n+3=\kappa+1\); in form (A) with \(t=s\), \(\ell_B\) grows and it lies in the \(v_A\) block of index \(2n+4=\kappa+2\). \(\square\)

## 3. Coefficient pools

An *\(A\)-name* is a triple \((f,j,e)\) and a *\(B\)-name* a quadruple \((f,j,c,e)\), over all legal values, including the extras read from a larger state. An \(A\)-name does not contain the bucket, which is not known when the label head is computed. Let \(\mathcal N_A,\mathcal N_B\) be these finite sets; then
\[
\begin{gathered}
|\mathcal N_A|\le TM2^bd,\\
|\mathcal N_B|\le TM2^bD .
\end{gathered}\tag{3.1}
\]
For large \(s\) these are less than \(2^r\) and \(2^s\) respectively, since \(TM2^b\) is a polynomial in \(s\) and \(r-.40005s\) and \(s-.60005s\) are positive multiples of \(s\). Fix fields \(\mathbb F_{2^r}\) and \(\mathbb F_{2^s}\), identified linearly with \(\mathbb F_2^r\) and \(\mathbb F_2^s\), and choose injections
\[
\iota_r:\mathcal N_A\to\mathbb F_{2^r},\qquad
\iota_s:\mathcal N_A\sqcup\mathcal N_B\to\mathbb F_{2^s} .
\]
For a name \(\nu\), let \(K_\nu\) be the *block-diagonal* map of padded streams that multiplies the block \(A_0\) by \(\iota_r(\nu)\) (for \(A\)-names) and every block of length \(s\) by \(\iota_s(\nu)\), in bit coordinates. The same coefficients are used on every block. A block whose active part is a proper prefix is multiplied as a full block, its padding being zero, so its output fills the whole block. By the table of Lemma 1.1 the output of \(K_\nu\) on an active input stream fits inside the active evaluation stream of the same side: for instance in form (B) on side \(B\) the output ends at \((n+1)s=|v_B|\).

**Lemma 3.1** (coefficient choice; [OpenAI-BCI, Lemma 2.1]). For large \(s\) the injections can be chosen so that the following holds within every family, extra value and side. Let \(n\) be the number of names there, \(\zeta\) a nonzero linear functional on \(\mathbb F_2^s\), and \(b\le t\le s\). Then each restricted functional
\[
(\zeta\circ K_\nu)|_{\mathbb F_2^t},
\]
where \(\mathbb F_2^t\) is the subspace of the first \(t\) input coordinates of a block, is the same for at most \(2^{1-b}n\) of the \(n\) names. The analogous statement holds on the initial block for \(\iota_r\), for every \(b\le t\le r\). Distinct names have distinct coefficients in each field.

*Proof.* Choose both injections uniformly at random among all injections. For a fixed nonzero \(\zeta\), the map \(c\mapsto\zeta(c\,\cdot)\) is linear from \(\mathbb F_{2^s}\) to the dual of \(\mathbb F_2^s\) and injective, since \(\{cu\}\) is the whole field for \(c\ne0\); both have \(2^s\) elements, so it is a bijection. Thus on any fixed set of \(n\) names the functionals \(\zeta\circ K_\nu\) are \(n\) draws without replacement from the set of all functionals. Restriction to the first \(t\) coordinates is a linear surjection onto the dual of \(\mathbb F_2^t\), so each restricted value is taken by a proportion \(p=2^{-t}\le2^{-b}\) of all functionals.

Fix a restricted value and let \(S\) be the number of the \(n\) names taking it; \(\mathbb ES=np\). By the bound for sampling without replacement (Lemma 5.1 of [Streams, slots and slot evaluations](course:kadison-kaplansky-projections/streams-slots-and-slot-evaluations#5-concentration-for-sampling-with-and-without-replacement)),
\[
\mathbb P\{S-np\ge2^{-b}n\}\le e^{-2^{1-2b}n} .
\]
Outside this event \(S<np+2^{-b}n\le2^{1-b}n\). The number of tests is at most \(s\,2^{2s}\) (functional, length \(t\) and restricted value) times the number of families, extra values and sides, which is \(2^{O(s)}\) for fixed \(T\) and \(b\); and \(n\ge d=2^{.40005s}\) in every test. So the total failure probability is at most \(2^{O(s)}e^{-2^{1-2b}2^{.40005s}}\), which tends to zero; the initial block is handled in the same way with \(n\ge d\) and \(t\le r\). Fix injections for which no test fails. \(\square\)

## 4. Gates, corrections and the edge equations

The edge equations are written once for arbitrary padded input streams \(u_A,u_B\), not only for actual states; this is what allows occurrences at different heights to be compared later. Raw blocks are denoted \(u_{A,j}\), \(u_{B,j}\).

**Gates.** For a source index \(k>20\) put \(J(k)=\lfloor(k-5)/2\rfloor\) and
\[
\begin{gathered}
g_k=1\\
\iff(u_{B,J-3},u_{A,J-3},\\
\ldots,u_{B,J},u_{A,J})\neq0,\\
J=J(k);
\end{gathered}\tag{4.1}
\]
for \(k\le20\) put \(g_k=1\). So every gate with \(k>20\) reads exactly the eight full raw input blocks of the pairs \((B_j,A_j)\), \(J-3\le j\le J\), whose source indices lie between \(2J-7\ge9\) and \(2J\le k-5\).

**Corrections.** Fix a positive label (2.1). At every marked extra interval of its family, add \(e\) (XOR) to the raw coordinates of that interval if \(g_k=1\), where \(k\) is the index of the block containing the interval; for an equal-height family there are no corrections. This defines *correction streams* \(C^u_{C,\lambda},C^v_{C,\lambda}\) and the *corrected streams*
\[
\begin{gathered}
\bar u_C=u_C+C^u_{C,\lambda},\\
\bar v_C=v_C+C^v_{C,\lambda},\\
C\in\{A,B\}.
\end{gathered}\tag{4.2}
\]
Each finite prefix meets finitely many marked intervals, so the sums are defined.

**Permutation tables.** For every family, label, source index \(k\), and tuple of all raw input blocks with source index less than \(k\), provide a *table*: at an unmarked index a permutation of the whole block, and at a marked cutoff with active length \(t\) a permutation of \(\mathbb F_2^t\). Distinct complete keys index distinct tables; each source index has finitely many tables. The *transformation* at source index \(k\) acts on the corrected block \(\bar u\) as follows:

1. At a marked cutoff: the table on the first \(t\) bits and the identity on the remaining bits if \(g_k=1\); the identity if \(g_k=0\).
2. At the twenty source indices immediately following a marked cutoff: the identity, unconditionally.
3. At every other index: the full-block table if \(g_k=1\), the identity if \(g_k=0\).

Tables act on corrected blocks, while their keys and the gates read raw earlier blocks. Write \(P_{A,\lambda}(\bar u_A)\) and \(P_{B,\lambda}(\bar u_B)\) for the transformed streams. For a slot with name \(\nu\), the *corrected evaluation* is \(Q_C=\bar v_C+K_\nu\bar u_C\); it differs from the raw evaluation \(v_C+K_\nu u_C\) by the *offset* \(C^v_{C,\lambda}+K_\nu C^u_{C,\lambda}\).

**The universal edge equations.** For an \(A\)-name \(\nu_A=(f,j,e)\) and a \(B\)-name \(\nu_B=(f,j,c,e)\) with \(h_0=c\Vert h_0'\):
\[
\begin{aligned}
&\bar v_A+K_{\nu_A}\bar u_A\\
&\quad=h_0\Vert P_{B,\lambda}(\bar u_B),\\
&\bar v_B+K_{\nu_B}\bar u_B\\
&\quad=h_0'\Vert P_{A,\lambda}(\bar u_A).
\end{aligned}\tag{4.3}
\]
These are equations of infinite padded streams. The \(A\)-evaluation block of index \(2j\) (\(j\ge1\)) contains \(K_{\nu_A}\bar u_{A,j}\) on the left and the transformed block of \(B_j\) on the right: it *couples* the source indices \(2j\) and \(2j-1\). The \(B\)-evaluation block of index \(2j-1\) occupies positions \((j-1)s\) to \(js\), which on the right are \(h_0'\) followed by \(P_{A,\lambda}(\bar u_A)\) shifted by \(s-r\); for \(j\ge2\) these are the positions of \(A_{j-1}\), so it couples the indices \(2j-1\) and \(2j-2\), and for \(j=1\) it couples \(B_1\) with \(h_0'\) and \(A_0\).

**Lemma 4.1** (causality). (1) Every gate \(g_k\) with \(k>20\) reads only raw input blocks of source index at most \(k-5\). (2) Every correction offset in an evaluation block is determined by the label and by raw input blocks of source index smaller than both source indices coupled by that block. (3) The key of the table at index \(k\) consists of the label and raw blocks of index less than \(k\). (4) Marked cutoffs of one family and their following twenty-index identity zones do not overlap.

*Proof.* (1) is the description after (4.1). (2) A correction in the evaluation block of index \(k\) uses the gate \(g_k\), which reads indices at most \(k-5\), and the coupled indices are \(k\) and \(k-1\). The input correction in the same block position has the same gate. (3) is the definition. (4) Consecutive marked indices are \(K=2\cdot10^6b>21\) apart by Lemma 2.1. \(\square\)

The lag in (4.1) is deliberate: a correction in an evaluation block never reads the input block that is recovered from that evaluation. The identity zones after each mark make it unnecessary to gate the transformations just beyond a cutoff, where they might otherwise read the raw extra bits.

**Remark 4.2.** The edge equations (4.3) are triangular. Starting from an \(A\)-endpoint state and a slot, the first \(r\) evaluation bits are the label head, which fixes the label. Then, in the source order, the key and gate of each table read only earlier raw blocks and are known before the table is used, and each evaluation block determines one new input block on the other side, after its known offset is removed and the known transformation is inverted. The next lesson uses this to construct exactly one edge at every slot and to recover states from labels.

## 5. Exercises

**Exercise 5.1.** Verify the cutoff forms of Lemma 1.1 for \(b=1\), \(s=5\) (ignoring the divisibility conditions on \(s\)), \(r=3\), \(n_0=1\) and \(i=0,\ldots,10\), and check that exactly one of \(\ell_A,\ell_B\) grows at each step.

**Exercise 5.2.** Show that two distinct names \(\nu\neq\nu'\) of the same side satisfy \(K_\nu u\ne K_{\nu'}u\) for every nonzero full block \(u\), and that the two-evaluation recovery \(u=(c_1-c_2)^{-1}(E_1-E_2)\) holds blockwise for padded streams.

**Exercise 5.3.** Why must the \(A\)-names exclude the bucket \(c\)? Consider how the \(A\)-endpoint of an edge finds its label from its state.

**Exercise 5.4.** Show that the count \(s\,2^{2s}\) in the proof of Lemma 3.1 bounds the number of triples (functional \(\zeta\), length \(t\), restricted value) for full blocks.

## 6. Solutions

**5.1.** With \(b=1\), \(s=5\): \(bi=10a_i+t_i\). For \(i=0\) we get \(t=0\), \(\ell_A=3+5=8\), \(\ell_B=5\), form (A) with \(n=0\), \(t=5\). For \(i=1,\ldots,5\), \(t_i=i\le5\): form (B), \(\ell_B=5+i\). For \(i=6,\ldots,9\): form (A), \(\ell_A=8+(i-5)\). For \(i=10\): \(a=1\), \(t=0\), \(\ell_A=13\), \(\ell_B=10\). At each step exactly one length grows by \(1\).

**5.2.** \(K_\nu u-K_{\nu'}u=(\iota_s(\nu)-\iota_s(\nu'))u\) in the field, a product of nonzero elements, hence nonzero. For padded streams the equations \(E_k=v+c_ku\) hold block by block, and in each full block the field computation applies; zero padding is preserved.

**5.3.** At an \(A\)-endpoint the first \(r\) evaluation bits equal \(\bar v_A[0,r)+\iota_r(\nu_A)\bar u_{A,0}\), and they are the label head \(h_0\), which contains the bucket. If the coefficient depended on the bucket, the endpoint would need the bucket to compute the head, and the head to know the bucket.

**5.4.** There are \(2^s-1\) nonzero functionals, at most \(s\) lengths, and at most \(2^t\le2^s\) restricted values; the product is at most \(s\,2^{2s}\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 2.1-2.3, Lemma 2.1. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [Judson] T. W. Judson, *Abstract Algebra: Theory and Applications*, Section 22.1. https://judsonbooks.org/aata-files/aata-html/finite-section-field.html
