# Terminal compatibility, key separation and base girth

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson counts coherent returns. The constraints are *terminal*: a reconstructed state must vanish beyond its cutoff, and at each vertex this costs about as many bits as the evaluation stream exceeds the input stream. Probabilities of terminal tests at different vertices multiply when the tested tables are different, that is, when their *keys* differ. A repeated key would identify two vertex prefixes, hence a shorter coherent return, unless the two vertices lie near opposite ends of the path; so tests in fixed end intervals are omitted. The resulting first-moment bound shows that deleting all minimal coherent returns removes a vanishing fraction of each layer, and leaves a graph without cycles shorter than \(0.93m_i\) [OpenAI-BCI, Sections 4.4-4.5, Lemmas 4.5-4.9].

- Surpluses and terminal compatibility (Section 1).
- Repeated keys (Section 2).
- The end guard (Section 3).
- The count of coherent returns and the base girth (Section 4).

The notation of [Coherent returns, reconstruction and accumulated rank](coherent-returns-reconstruction-and-accumulated-rank.md) is in force: aligned depths, \(D(v)\), bands \(I_k\) with margins \(M_k\), coherent returns, patterns, \(L_s\le2^{1.001s}\), the filtration \(\mathcal F_{<t}\), the product law \(\mathbb P_{\rm prod}\) and Lemma 4.1 there (accumulated rank). Throughout, \(s/b\) and then \(H_0/s\) are taken large; for definiteness \(s/b\ge10^{12}\) and \(H_0/s\ge10^{12}\) suffice.

## 1. Surpluses and terminal compatibility

For a vertex at height \(i\) put
\[
\begin{gathered}
\lambda_A(i)=r+\ell_B(i)-\ell_A(i),\\
\lambda_B(i)=s-r+\ell_A(i)-\ell_B(i),
\end{gathered}
\]
the *surplus* \(|v|-|u|\) of the evaluation over the input on each side. Since \(r-s\le\ell_A-\ell_B\le r\), both lie in \([0,s]\), and
\[
\begin{gathered}
\lambda_A(i)+\lambda_B(i)=s,\\
|\lambda_A(i)+\lambda_B(j)-s|\le b\\
(|i-j|\le1),
\end{gathered}\tag{1.1}
\]
the second because one height step changes exactly one input length by \(b\).

In a reconstruction (Lemma 3.1 of the previous lesson), a *receiver* is a vertex at which two incident evaluations are solved for its state. Its *terminal test* asks that the solution vanish beyond the cutoff.

**Lemma 1.1** (terminal compatibility; [OpenAI-BCI, Lemma 4.5]). Let \(v\) be a receiver whose two incident edges have distinct keys at the tested index, with arguments known beforehand and the required terminal gates open. If both incident common cutoffs equal the cutoff of \(v\), its terminal conditions have \(\mathbb P_{\rm prod}\)-probability exactly \(2^{-\lambda(v)}\). If each incident common cutoff is at most \(b\) bits below that of \(v\), one can choose an event on the two tested tables, implied by the terminal conditions, with \(\mathbb P_{\rm prod}\)-probability at most \(2^{-\max\{0,\lambda(v)-4b\}}\). Only the actual uniform active prefix of a partial permutation is used.

*Proof.* *Equal cutoffs.* The initial block is never terminal. There are two terminal shapes, by the cutoff forms of Lemma 1.1 of [Streams, coefficient pools and universal corrections](streams-coefficient-pools-and-universal-corrections.md).

If the last active input block of \(v\) has \(t\) bits, its last evaluation block has all \(s\) bits, and both incident evaluations of that block are outputs of full-block tables of the preceding index, uniform and independent given \(\mathcal F_{<t}\) because their keys differ. The map \((u,w)\mapsto(w+c_1u,\,w+c_2u)\) from \(\mathbb F_2^t\times\mathbb F_2^s\) (the \(t\) active input bits and the \(s\) evaluation bits) to \(\mathbb F_2^s\times\mathbb F_2^s\) is linear and injective, because \(c_1-c_2\) is invertible; its image has dimension \(s+t\), and the pair of evaluations lies in it with probability \(2^{-(s-t)}\). Here \(\lambda(v)=s-t\).

If instead the input of \(v\) has ended and its last evaluation block has \(t\) active bits, those bits are, on both incident edges, outputs of the current prefix tables, independent and uniform on \(\mathbb F_2^t\). Since \(u=0\) there, the two values must agree after their known offsets are removed: probability \(2^{-t}\), and \(\lambda(v)=t\). The boundary cases \(t=0\) and \(t=s\) move the whole surplus to the other shape.

*Adjacent cutoffs.* For an adjacent incidence the extras are label data and the gates read earlier raw blocks, so the correction of incidence \(a\) is a known vector \(o_a=C^v_a+K_aC^u_a\); move it to the other side of the equation. Its support may fill the output block, but a known translation costs no random dimension. On a common active random prefix of width \(w'\), with coordinate projection \(\pi\), the map
\[
\begin{aligned}
(u,w)\longmapsto\bigl(&\pi(w+K_1u-o_1),\\
&\pi(w+K_2u-o_2)\bigr)
\end{aligned}
\]
has affine image of dimension at most \(w'+t\) in \(2w'\) bits, where \(t\) is the number of free input bits involved; so the condition that the two random prefixes lie in it has codimension at least \(\max\{0,w'-t\}\). No invertibility of a truncated coefficient is needed. For the shape with no input, \(t\) is replaced by \(0\).

Let \(t\in\{b,2b,\ldots,s\}\) be the width of the last active block of \(v\) in the interleaved input order; each incident common cutoff equals that of \(v\) or lies \(b\) bits earlier. If \(t>b\), both evaluations of the partial-input shape lie in the preceding index and have \(s\) random bits, giving codimension at least \(s-t\); on the evaluation-only shape the common random prefix has width at least \(t-b\), giving at least \(t-b\) conditions. If \(t=b\), a cutoff may cross a block boundary. On the partial-input shape the preceding index still has full random width (an ordinary block, or the full active prefix of a marked block), so it still gives \(s-b\) conditions. On the other shape a lower incidence may already be in its deterministic zone after a mark; its surplus is only \(b\), and we charge nothing, which is allowed since \(\max\{0,b-4b\}=0\). The same holds with \(A\) and \(B\) exchanged, and \(t=s\) covers the boundary that appears as \(t=0\) on the other side. All retained outputs of positive width are actual independent uniform prefixes of current tables. These bounds are stronger than the stated loss of \(4b\). \(\square\)

## 2. Repeated keys

**Lemma 2.1** (a repeated key identifies prefixes; [OpenAI-BCI, Lemma 4.6]). Let \(H_*\) be the least scale of a vertex of a counted path or theta. If two distinct tested terminal edge occurrences at the same source index use the same table key, their receivers lie on the same side and agree in both raw streams to an available aligned depth of at least
\[
H_*-8s .
\]
At a nonterminal index, equality of keys identifies both receiver prefixes through the preceding complete receiver block.

*Proof.* At the update of a \(B\)-block \(B_j\) the table used is that of \(A_{j-1}\), of index \(2j-2\); its key contains the family, the full label, the raw \(A\)-inputs through \(A_{j-2}\) and the raw \(B\)-inputs through \(B_{j-1}\). So the two \(B\)-receivers have the same raw inputs through \(B_{j-1}\). Their evaluations through position \((j-1)s\) are computed from \(A\)-inputs through \(A_{j-2}\), the same earlier keys and the same offsets, so they agree, and \(v=Q-K_\nu u\) gives agreement of the evaluation streams through \(B_{j-1}\): aligned depth \(2(j-1)s\). At the update of \(A_j\) the table used is that of \(B_j\), of index \(2j-1\), with key containing the raw \(A\)-inputs through \(A_{j-1}\) and the raw \(B\)-inputs through \(B_{j-1}\); the \(A\)-evaluation through \(A_{j-1}\) uses only these, so the \(A\)-receivers agree to aligned depth \((2j-1)s\). In both cases a table of index \(k\) identifies the receivers to aligned depth exactly \(ks\).

For terminal tests, let \(\kappa\) be the final common source index of an incident edge and \(t\in\{b,\ldots,s\}\) its active length; its common scale is \(H_c=\kappa s+t\). The two terminal shapes test the index \(\kappa-1\) or \(\kappa\), so \(ks\ge H_c-2s\). The common scale is at least the receiver's scale minus \(b\), so \(ks\ge H_*-2s-b\). If two adjacent incidences straddle a block boundary, restricting both to their earlier common receiver prefix loses at most one more aligned step of \(2s\). The result exceeds \(H_*-8s\). These prefixes end before the first partial block of either receiver, so they are available at both. Finally, the two slots chosen at one receiver have different labels, so a repeated key never comes from one receiver. \(\square\)

## 3. The end guard

Fix a coherent pattern of length \(p\), initial scale \(H\) and margin \(M=M_k\). Every vertex scale \(H_v\) and the least one \(H_*\) satisfy
\[
\begin{gathered}
H-bp\le H_*\le H_v\\
\le H+bp .
\end{gathered}\tag{3.1}
\]
Put
\[
\begin{gathered}
E_p=100(s+bp),\\
J_p=\lceil4E_p/s\rceil+4 .
\end{gathered}
\]
The *end guard* consists of the receiver positions at distance at most \(J_p\) from either end of the abstract path; it depends only on the pattern.

**Lemma 3.1** (key separation outside the end guard; [OpenAI-BCI, Lemma 4.7]). In a minimal coherent return, at every source index, the terminal keys tested at receivers outside the end guard are distinct.

*Proof.* By (2.2) of the previous lesson and (3.1), \(ps/2+M\le h\le D(v_0)\le H_*+2bp\), so
\[
p\le2(H_*-M+E_p)/s .
\]
Suppose keys at receiver positions \(a<b'\) coincide. By Lemma 2.1 the two receivers lie on one side and agree to an available depth of at least \(H_*-8s\), which exceeds \(H_*-E_p\) by \(92s\) or more. The segment of the path between them is nonbacktracking and lies in the same band. If
\[
(b'-a)s/2+M\le H_*-E_p,
\]
the least aligned depth above the left side is at most \(H_*-E_p+2s\), still available, so the segment is a coherent return. Unless it is the whole path, whose ends lie in the guards, this contradicts minimality. Otherwise
\[
\begin{aligned}
b'-a&>2(H_*-M-E_p)/s\\
&\ge p-4E_p/s ,
\end{aligned}
\]
so \(a<4E_p/s\) and \(p-b'<4E_p/s\), and both positions lie in the guards. Only contiguous subpaths of the given return were used. \(\square\)

**The tests charged to a return.** In counting, a pattern is rejected at an index if its selected terminal keys outside the guard coincide, or if a required terminal gate is closed. These rejections are predictable, since keys and gates are known given \(\mathcal F_{<t}\), and by Lemma 3.1 no minimal coherent return in \(X^{\rm good}\) is lost; we do not condition on minimality. At each unguarded internal receiver with positive surplus, choose one terminal test; at one index these tests use distinct tables and their \(\mathbb P_{\rm prod}\)-probabilities multiply. Pair successive internal vertices along the path in (1.1): each pair has total surplus at least \(s-b\). Omitting the two endpoints and the guards loses at most \((2J_p+4)s\) bits of surplus, and the adjacent-cutoff allowance of Lemma 1.1 loses at most \(4bp\). So the accumulated rank of an actual minimal return satisfies
\[
R_{\rm ret}\ge\frac{ps}2-10^4(s+bp),\tag{3.2}
\]
trivially if the right side is negative; at most \(2p\) whole tables are charged. Outputs of current tables that are not tested still enter later steps of the formal reconstruction, but they are integrated out in the current estimate.

## 4. The count and the base girth

**Lemma 4.1** (expected number of coherent returns; [OpenAI-BCI, Lemma 4.8]). For large \(s/b\) and then large \(H_0/s\), the expected number of minimal coherent returns starting on either side at height \(i\), over all bands containing them, is at most
\[
2^{0.975H_i} .
\]
The count is of oriented rooted paths, with repetitions of vertices and edges allowed.

*Proof.* Put \(H=H_i\). Since the first endpoint has scale \(H\), (2.2) of the previous lesson gives \(p\le2(H-M)/s\le2H/s\). There are at most four bands and at most \(L_s^p\) label and height patterns of length \(p\). By Lemma 3.1 of the previous lesson the free endpoint bits number at most \((H_-+H_+)/2-h\le H-h+bp\), and each pattern with each choice of free bits has at most one realization. By Lemma 4.1 of the previous lesson and (3.2), applied to the event that this realization is a minimal coherent return in \(X^{\rm good}\), its probability is at most
\[
e^{2\varepsilon_sp}\,2^{-ps/2+10^4(s+bp)} .
\]
With \(L_s\le2^{1.001s}\), \(h\ge ps/2+M\) and \(e^{2\varepsilon_sp}\le2^{3p}\) for large \(s\), the contribution of one length and band is at most
\[
2^{\,H+0.001sp-M+10^5(s+bp)} .
\]
Since \(M\ge H/30>0.03H\) by (2.1) of the previous lesson and \(sp\le2H\), the exponent is at most \(0.972H+10^5(s+2bH/s)\), and the error term is below \(0.001H\) when \(s/b\ge10^{12}\) and \(H_0/s\ge10^{12}\). The number of lengths and bands is polynomial in \(H\), which costs at most \(0.002H\) more after increasing \(H_0\). \(\square\)

Delete every vertex of every minimal coherent return, in every band, from \(X^{\rm good}\); call the induced graph \(X^{(1)}\).

**Lemma 4.2** (the first deletion gives base girth; [OpenAI-BCI, Lemma 4.9]). In \(X^{(1)}\), every nonempty cyclically reduced closed path based at a vertex of height \(i\) has length greater than \(0.93m_i\).

*Proof.* Let such a path have length \(L\le0.93m_i\). It has fewer than \(7m_i\) edges, so it lies in one band, and its two ends are the same vertex, which agrees with itself to the available depth \(D(v)\ge H_i-2s\). The required threshold is
\[
\begin{gathered}
\frac{Ls}2+M_k\le\Bigl(\frac{0.93}{2\cdot0.50005}+0.05\Bigr)H_i\\
<0.98H_i ,
\end{gathered}
\]
using \(m_i=H_i/(0.50005s)\) and (2.1) of the previous lesson. The least aligned depth above it adds less than \(2s\), and \(0.98H_i+2s\le H_i-2s\) for large \(H_0/s\). A cyclically reduced closed path is nonbacktracking as a path, so it is a coherent return, and it contains a minimal one, all of whose vertices were deleted. This contradicts its presence in \(X^{(1)}\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Compute \(\lambda_A(i)\) and \(\lambda_B(i)\) in the two cutoff forms, and verify (1.1).

**Exercise 5.2.** In the first shape of Lemma 1.1, show directly that the image of \((u,w)\mapsto(w+c_1u,w+c_2u)\) is \(\{(E_1,E_2):E_1-E_2\in(c_1-c_2)\,\mathbb F_2^t\}\), and deduce the probability \(2^{-(s-t)}\).

**Exercise 5.3.** Why does Lemma 3.1 need the minimality of the return? Give a nonminimal coherent return with two equal keys outside the guard.

**Exercise 5.4.** Check the numerical inequality \(0.93/(2\cdot0.50005)+0.05<0.98\) and find the largest constant \(\gamma\) for which the same argument gives girth greater than \(\gamma m_i\) with threshold \(0.98H_i\).

## 6. Solutions

**5.1.** In form (B): \(\lambda_A=r+ns+t-(r+ns)=t\) and \(\lambda_B=s-r+r+ns-ns-t=s-t\). In form (A): \(\lambda_A=r+(n+1)s-r-ns-t=s-t\) and \(\lambda_B=s-r+r+ns+t-(n+1)s=t\). The sum is \(s\). From height \(i\) to \(i\pm1\) one input length changes by \(b\), which changes \(\lambda_A\) and \(\lambda_B\) by \(b\) in opposite directions, so \(\lambda_A(i)+\lambda_B(j)\) differs from \(s\) by at most \(b\).

**5.2.** \((E_1,E_2)\) is in the image iff \(E_1-E_2=(c_1-c_2)u\) for some \(u\in\mathbb F_2^t\) (then \(w=E_1-c_1u\)); the set \((c_1-c_2)\mathbb F_2^t\) has \(2^t\) elements, and for independent uniform \(E_1,E_2\) the difference \(E_1-E_2\) is uniform on \(\mathbb F_2^s\), so the probability is \(2^{t-s}\).

**5.3.** In the proof, a repeated key at positions \(a<b'\) produces a shorter coherent return; minimality makes that impossible. If a long path contains a shorter coherent return between positions \(a<b'\) far from both of its ends, the receivers at \(a\) and \(b'\) agree to a large depth, and the tables tested there may have the same key. Only minimality excludes this.

**5.4.** \(0.93/1.0001=0.92990\ldots\), plus \(0.05\) gives \(0.97990\ldots<0.98\). The argument needs \(\gamma/1.0001+0.05<0.98\), that is \(\gamma<0.93009\ldots\); the margin \(0.05\) is the upper bound \(M_k/H_i<0.05\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 4.4-4.5, Lemmas 4.5-4.9. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
