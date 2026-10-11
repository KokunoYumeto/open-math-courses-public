# Global descriptions and the running time

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The construction of the previous four lessons is valid at every node (Proposition 4.1 of [Boundary invariants](boundary-invariants.md)). This lesson turns it into a bounded-description hierarchy, which proves the structure theorem (Theorem 4.3 of [Descriptions and a dynamic program](descriptions-and-a-dynamic-program.md)). Every child is described as a subset of *all* of \(J\), without intersecting with a description of its parent; this is what keeps the formulas of bounded size at every depth. Every mark receives a description of the jobs before it. The lesson ends with the running time and with the places where the number of machines enters.

Fix a node \(W\) with boundaries \(a,b\), center \(v\), and a side with working frame, open part \(E\), walk cutoffs \(S_0,\ldots,S_q\) and positions \(s_0,\ldots,s_{q+1}\).

## 1. Cutoff predicates

For every walk cutoff \(S_i\) choose a formula \(\widetilde S_i\) with
\[
\widetilde S_i\cap W=S_i .
\]

- *Same side.* Let \(\Phi_i\) be the union of the carry determined by \(O\setminus S_i\), before any injection (the empty union if \(O\subseteq S_i\)), and put \(\widetilde S_i=P_b\setminus\Phi_i\). In \(W\) the carry selects exactly the unpromoted jobs \(O\setminus S_i\), and the low jobs are \(S_0\) together with the promoted jobs of \(O\), all in \(P_b\); so \(\widetilde S_i\cap W=S_i\).
- *Switched side.* Put \(\widetilde S_i=(J\setminus D_a)\cap\{\lambda\leq r\}\), where \(r\) is the rank of the last promoted job of \(X\), or \(r=0\). In \(W\) this is the rank prefix of \(X\) promoted so far.

These formulas are defined for every walk cutoff, whether or not the corresponding gap is empty. Outside \(W\) they may describe anything.

## 2. A child as a global set

**Lemma 2.1.** Let \(W'\) be a child of \(W\) on this side, with edge data \(a'=s_i\), \(b'=s_{i+1}\), \(S=S_i\) and pruned list \(\mathcal K'\). In the working frame,
\[
\begin{aligned}
W'\setminus S&=\mathcal Q(\mathcal K')\cap P_{b'}\cap(J\setminus\widehat P_{a'}),\\
W'\cap S&=D_{a'}\cap P_b\cap(J\setminus\widehat D_{b'})\\
&\qquad\cap(J\setminus\widehat D_v)\cap\widetilde S_i .
\end{aligned}
\]

*Proof.* *High part.* A high job of \(W'\) qualifies (Lemma 2.1 of the fifth lesson), lies in \(P_{b'}\) (Lemma 4.2 of the fourth lesson), and, being scheduled after \(a'\), is not in \(\widehat P_{a'}\). Conversely, a job of the right side is scheduled before \(b'\), since it is in \(P_{b'}\). If it were scheduled at or before \(a'\), then, as a qualifier of the child's list, it would lie in \(\widehat P_{a'}\) by (I2) for the child (Lemma 2.1 of the seventh lesson). So it is scheduled strictly between \(a'\) and \(b'\), that is, it belongs to \(W'\), and as a qualifier in \(W'\) it is high.

*Low part.* Let \(z\) belong to the right side. Since \(z\in D_{a'}\), it is scheduled after \(a'\), hence after \(a\); since \(z\in P_b\), before \(b\). So \(z\in W\), and only now is \(\widetilde S_i\cap W=S_i\) used: \(z\in S_i\). The cutoff \(S_i\) is contained in the center cutoff \(S_*\). If \(z\) were in the center, it would be in \(\widehat D_v\); if it were after the center, it would lie in \(D_v\), because the center separates \(S_*\). So \(z\in E\). If \(z\) were in the slot \(b'\) or after it, it would lie in \(\widehat D_{b'}\), because \(b'\) separates \(S_i\) on \(E\) (Lemma 4.1 of the fourth lesson). So \(z\) is strictly between \(a'\) and \(b'\): \(z\in W'\cap S\). Conversely, a low job of \(W'\) lies in \(D_{a'}\cap P_b\) (Lemma 4.2 of the fourth lesson), in \(\widetilde S_i\), and, being scheduled before \(b'\) and before \(v\), in neither \(\widehat D_{b'}\) nor \(\widehat D_v\). \(\square\)

The order of the tests in the low part matters. The positive cone tests first place a job inside \(W\), where \(\widetilde S_i\) is known to agree with the cutoff; the exclusions then cut it down to the gap. No formula ever intersects with a description of the parent, so nothing accumulates along a branch.

The union of the two right sides is a global description of \(W'\).

## 3. The marks

**Lemma 3.1.** For every mark \(z\) of \(W\), the set of jobs of \(W\) scheduled before \(z\) in original time has a relative description inside \(W\).

*Proof.* Work in the working frame of the side containing \(z\), or of either side if \(z=v\), and put
\[
H_*=\begin{cases}P_b&\text{same side,}\\ J\setminus D_a&\text{switched side,}\end{cases}
\]
so that \(H_*\cap W\) is the center cutoff \(S_*\). Recall \(B_z(H)=P_z\cup(H\setminus\widehat D_z)\) from the third lesson.

*The center.* The center separates \(S_*\) with domain \(W\), so \(B_v(H_*)\cap W\) is the set of jobs of \(W\) before \(v\) (Lemma 1.2 of the third lesson).

*A mark in \(E\).* It is a position \(z=s_i\) with \(i\geq1\), and it separates \(S_i\) on \(E\). Put
\[
F_z=B_v(H_*)\cap B_z(\widetilde S_i).
\]
In \(W\), the first factor selects \(E\). Inside \(E\), the second factor selects the jobs before \(z\), by Lemma 1.2 of the third lesson with domain \(E\), since \(\widetilde S_i\cap E=S_i\cap E\). All jobs of \(W\) before \(z\) lie in \(E\), so \(F_z\cap W\) is the set of jobs of \(W\) before \(z\).

*Original time.* If the working frame is the forward frame, these are the required descriptions. Otherwise "before" in the working frame means "after" in original time. Then the formula \((J\setminus F_z)\setminus z\), a complement (Lemma 2.1 of the second lesson) intersected with the complement of a membership test, describes inside \(W\) the jobs before \(z\) in original time. The membership test is needed because the complement alone would contain the jobs of \(z\). The same conversion applies to the center. \(\square\)

## 4. Counting leaves

**Lemma 4.1.** The global descriptions of Lemma 2.1 have at most \(257\) leaves, and the relative descriptions of Lemma 3.1 at most \(132\). In particular all of them have fewer than \(500\) leaves.

*Proof.* A list or a carry has at most five entries (Lemma 3.2 of the fifth lesson) of at most \(25\) leaves each (Lemma 4.1 of the sixth lesson), so its union has at most \(125\) leaves; an empty union is the constant false. A same-side cutoff predicate has at most \(1+125=126\) leaves, a switched one two. The high part of Lemma 2.1 has at most \(125+2=127\) leaves, the low part at most \(4+126=130\), and their union at most \(257\). The center description \(B_v(H_*)\) has three leaves, \(B_z(\widetilde S_i)\) at most \(1+126+1=128\), so \(F_z\) has at most \(131\), and the conversion to original time adds one. Every cone in these formulas belongs to a slot or to a virtual boundary (a constant), and every rank test is in one of the two frames, so they are formulas in the sense of the second lesson. \(\square\)

**Proof of the structure theorem.** Start from any full schedule of \(J\) and build the marks and lists (Proposition 4.1 of the seventh lesson). The root \(J\) is described by the constant true. Every child has the global description of Lemma 2.1, and every mark the relative description of Lemma 3.1, all with fewer than \(500\) leaves (Lemma 4.1), however deep the node. Every node is cut at least at its center, its children are exactly the gaps between its marks, and every branch is finite. These are the conditions of a bounded-description hierarchy. \(\square\)

Together with the second lesson this proves that the dynamic program decides every deadline correctly and returns a schedule.

## 5. The running time

**Proposition 5.1.** For a fixed leaf bound \(K\), the dynamic program runs in time polynomial in the input length. With \(K=10000\), deciding a deadline and producing a schedule takes \(O(N^{15K+13})\) steps of a deterministic multitape Turing machine, and minimizing the makespan, including reading the input, takes \(O\bigl((L+2)^{150020}\bigr)\) steps, where \(L\) is the input length.

*Proof.* Let \(B=C_KN^{3K}\) bound the number of formulas (Lemma 2.2 of the second lesson). There are at most \(B\) sets in \(\mathcal F\), and for each set \(W\) at most \(S=BN^3\) states, given by a formula for \(L\) and a triple \(Z\). Store, on work tapes, the bit vector of every set, the explicit schedule of every accepted set (at most \(N\) entries of \(O(\log N)\) bits), and for the current \(W\) a record of every state with its parts, a reachability mark and the number of its predecessor record; a state record has \(O_K(N)\) bits.

Implement every operation by sequential scans. Fetching or updating one state record costs \(O_K(SN)=O_K(BN^4)\) steps; looking up the acceptance value of a set by comparing it with all stored bit vectors costs \(O_K(BN^2)\); a compatibility test by repeated scans of the \(N\times N\) table of \(\prec\) costs \(O(N^4)\). So testing one ordered pair of states for a transition and updating the marks costs \(O_K(BN^4)\). Starting from the initial states, make at most \(S\) passes over all \(S^2\) ordered pairs, marking a state when a marked state has a transition to it; this finds every reachable state. Over all \(B\) sets the cost is
\[
\begin{aligned}
&O_K\bigl(B\cdot S\cdot S^2\cdot BN^4\bigr)\\
&\quad=O_K\bigl(B^5N^{13}\bigr)\\
&\quad=O_K\bigl(N^{15K+13}\bigr).
\end{aligned}
\]
Generating, evaluating and deduplicating the formulas, computing \(\prec\), and assembling schedules along recorded paths fit within this bound. With \(K=10000\) and \(N\leq3n\leq3L\), at most \(n\leq L\) deadlines are tried, so the total is \(O(L\cdot(3L)^{150013})\), which is \(O((L+2)^{150020})\). \(\square\)

Lemma 4.1 shows that every description needed by the hierarchy has at most \(257\) leaves, so the dynamic program is already complete with \(K=257\), and the same accounting then gives the exponent \(15\cdot257+13=3868\) for a deadline decision. The theorem's larger \(K\) leaves room for coarser counting; neither value is meant to be practical.

**Remark 5.2 (isolated jobs given by their number).** The padded set can be enormous if the input lists only the arcs and gives the number \(n\) of jobs in binary, with many isolated jobs. For a deadline decision this does not matter. Reject if \(n>3T\). Let \(d\) be the number of jobs that occur in arcs. If \(T\geq d\), accept: run those \(d\) jobs one per slot in a topological order, and fill the remaining machine positions, of which there are \(3T-d\geq n-d\), with the isolated jobs. Otherwise \(N=3T<3d\leq6|E|\), and the padded instance has size polynomial in the input.

## 6. Where three is used

The number of machines appears in the definitions (slots of three jobs, padding to \(3T\) jobs, triples in the atomic tests and in the states of the dynamic program) and in the estimate of Lemma 3.2 of the fifth lesson, where at most three injections survive in a list because each of them contains a different job of a three-job slot. The bound of five entries per list, and with it every leaf count in this lesson, comes from that estimate.

## 7. Exercises

**7.1.** In the low part of Lemma 2.1, the cutoff predicate is used only after the tests \(D_{a'}\cap P_b\). Give a reason why using \(\widetilde S_i\) first would not work.

**7.2.** Why is the test \(J\setminus\widehat D_v\) needed in the low part, given that the test \(J\setminus\widehat D_{b'}\) is present?

**7.3.** Check the count \(1+126+1=128\) for \(B_z(\widetilde S_i)\) on a same side.

**7.4.** In Remark 5.2, why does \(T\geq d\) guarantee a schedule even though the \(d\) jobs may have precedence relations among themselves?

**7.5.** Show that the high part of Lemma 2.1 would be wrong without the invariant (I2): describe a qualifier that the formula could otherwise select.

## 8. Solutions

**7.1.** The predicate \(\widetilde S_i\) agrees with the cutoff only on \(W\). Outside \(W\) it may contain arbitrary jobs, for instance jobs before \(a\) that satisfy the other tests. The positive tests first place a job inside \(W\).

**7.2.** The test against \(b'\) relies on \(b'\) separating \(S_i\) on \(E\), which says nothing about jobs on the other side of the center. Low jobs after the center lie in \(D_v\), because the center separates the center cutoff with domain \(W\); the test against \(v\) removes them.

**7.3.** \(B_z(\widetilde S_i)=P_z\cup(\widetilde S_i\cap(J\setminus\widehat D_z))\): one leaf for \(P_z\), at most \(126\) for \(\widetilde S_i\), one for the complement of \(\widehat D_z\).

**7.4.** One job per slot in a topological order respects every precedence relation, and \(d\) slots suffice for \(d\) jobs. The other \(n-d\) jobs are isolated and fit into the \(3T-d\) free positions because \(n\leq3T\).

**7.5.** Without (I2), a qualifier \(z\) scheduled at or before \(a'\), for instance a job before the parent's boundary \(a\) that lies in a carried entry and precedes \(b'\), would satisfy \(z\in\mathcal Q(\mathcal K')\cap P_{b'}\) and possibly \(z\notin\widehat P_{a'}\). The formula would then select a job outside the child. (I2) says exactly that such a qualifier lies in \(\widehat P_{a'}\) and is excluded.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Sections 8 and 9 and the remark on compact encodings. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/124.md
