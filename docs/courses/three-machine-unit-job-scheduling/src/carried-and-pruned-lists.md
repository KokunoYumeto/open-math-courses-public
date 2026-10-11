# Carried and pruned lists

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In [Centers, sides and edge cutoffs](centers-sides-and-edge-cutoffs.md) every node received a center, two sides, and children with edge cutoffs. Each child must now receive a list of upsets whose qualifiers inside the child are exactly its high jobs, and the list must stay short at every depth. This lesson defines the two ways a child's list is formed from its parent's, proves that the qualifiers come out right, and proves that a list never has more than five entries. That last bound is where the machine count enters: each extra entry has to be witnessed by a different job of a three-job slot.

Throughout, \(W\) is a node with tag frame, list \(\mathcal K=(K_1,\ldots,K_\ell)\), old high set \(O\) and keys as in the fourth lesson, and \(W'\) is a child of \(W\) on one of its sides, with edge data \(a',b',S\). Boundaries \(a,b\), the sets \(X\) and \(Y\), and ranks refer to the side's working frame.

## 1. Carrying and pruning

**Lemma 1.1 (suffix carry).** For \(1\leq d\leq\ell\) and \(0\leq r\leq N+1\) put
\[
\begin{aligned}
&\operatorname{carry}_{d,r}(\mathcal K)\\
&\quad=\bigl(K_d\cap\{\lambda\geq r\},K_{d+1},\ldots,K_\ell\bigr).
\end{aligned}
\]
Its qualifiers are exactly the qualifiers of \(\mathcal K\) whose key is at least \((d,r)\). Among them, the new keys are ordered like the old ones. Its entries are upsets.

*Proof.* Let \(x\) be a qualifier of \(\mathcal K\) with largest index \(j\). If \(j>d\), then \(K_j\) is kept and \(x\) qualifies. If \(j=d\), then \(x\) lies in no kept entry except possibly the first, so it qualifies exactly when \(\lambda(x)\geq r\). If \(j<d\), it lies in no kept entry. So the new qualifiers are those with \((j,\lambda(x))\geq(d,r)\). For each of them the entry giving its largest index is kept, with index lowered by \(d-1\); this shift is the same for all and preserves the order, and the ranks are unchanged. A rank suffix is an upset, so \(K_d\cap\{\lambda\geq r\}\) is an upset. \(\square\)

To *prune* a list on \(W'\) means to delete every entry disjoint from \(W'\), keeping the order of the others. Pruning never changes which jobs of \(W'\) qualify.

**Lemma 1.2 (pruning keeps comparisons).** Let a list be pruned on \(W'\). Let \(x\in W'\) and \(y\in J\) be qualifiers of the pruned list. If the pruned key of \(x\) is smaller than the pruned key of \(y\), then the key of \(x\) was smaller than the key of \(y\) before pruning.

*Proof.* Use the indices before pruning. Let \(M(z)\) be the largest index of an entry containing \(z\), and \(R(z)\) the largest index of a kept entry containing \(z\). Every entry containing \(x\) meets \(W'\) and is kept, so \(R(x)=M(x)\), while \(R(y)\leq M(y)\). If \(R(x)<R(y)\), then \(M(x)<M(y)\). If \(R(x)=R(y)\) and \(\lambda(x)<\lambda(y)\), then either \(M(x)<M(y)\) or \(M(x)=M(y)\) and the ranks decide. In both cases the old key of \(x\) is smaller. \(\square\)

## 2. The two updates

**Same side.** The working frame is the tag frame, and the old list is in it. If \(O\setminus S=\varnothing\), the *carry* is the empty list. Otherwise let \((d,r)\) be the smallest key of a job of \(O\setminus S\), and let the carry be \(\operatorname{carry}_{d,r}(\mathcal K)\). Append the *injection*
\[
I=D_a\setminus P_b
\]
as a last entry, and prune on \(W'\).

**Switched side.** The old list is discarded. Suppose a set \(G\subseteq J\) is given with three properties, in the working frame:
\[
\begin{aligned}
&G\text{ is an upset};\qquad X\subseteq G;\\
&\text{no job of }G\text{ is scheduled at or before }a.
\end{aligned}
\]
Note that \(G\) must contain all of the parent's \(X=W\setminus D_a\), not only the part inside \(W'\). The construction of such a \(G\) is the subject of the next lesson. The edge cutoff \(S\) is a rank prefix of \(X\), so there is a threshold \(h\) with \(X\setminus S=X\cap\{\lambda\geq h\}\); take \(h=N+1\) if \(X\subseteq S\). The new list is the *switch pair*
\[
\bigl(G\cap\{\lambda\geq h\},\ D_a\bigr),
\]
pruned on \(W'\).

**Lemma 2.1 (the new qualifiers).** In both cases, before pruning, the qualifiers in \(W\) are exactly the jobs of \(W\setminus S\), and on \(W\setminus S\) the new keys are ordered like the side's priority order. After pruning, the qualifiers in \(W'\) are exactly the high jobs \(W'\setminus S\), and the child satisfies (I1) in its tag frame, the working frame:
\[
W'\setminus S\subseteq P_{b'},\qquad W'\cap S\subseteq D_{a'}.
\]

*Proof.* *Same side.* By Lemma 1.1 and because \(O\) is promoted in key order, the carry's qualifiers in \(W\) are the jobs of \(O\) with key at least \((d,r)\), which are exactly the unpromoted ones, \(O\setminus S\), in their old key order. The injection meets \(W\) in \(W\cap D_a\setminus P_b=Y\), because \(Y\subseteq D_a\) (Lemma 2.1 of the fourth lesson). The jobs of \(Y\) are not in \(O\subseteq P_b\), so the injection's jobs in \(W\) are not carried qualifiers, and as the last entry it gives them the largest index. So the qualifiers in \(W\) are \((O\setminus S)\cup Y=W\setminus S\) (the low set is \(S_0\) together with the promoted part of \(O\), and \(W=S_0\cup O\cup Y\)). Their keys order \(O\setminus S\) by old key and then \(Y\) by rank, which is the priority order of the same side.

*Switched side.* The first entry contains \(X\), so in \(X\) it selects \(X\cap\{\lambda\geq h\}=X\setminus S\). The second entry selects all of \(W\cap D_a=W\setminus X\), and its larger index puts these jobs last, whether or not the first entry also contains them. So the qualifiers in \(W\) are \((X\setminus S)\cup(W\setminus X)=W\setminus S\), ordered by rank within \(X\) and then by rank within \(W\cap D_a\), as in the switched priority order.

Pruning does not change membership in \(W'\), so the qualifiers in \(W'\) are \(W'\setminus S\). The two inclusions are Lemma 4.2 of the fourth lesson, and together they say \(O'\subseteq P_{b'}\) and \(W'\setminus O'\subseteq D_{a'}\) for the child's old high set \(O'=W'\setminus S\). \(\square\)

## 3. Runs and the length of a list

A *run* is a chain of nodes with the same tag that starts at the root or at a child created on a switched side, and continues through children created on same sides. The *initial entries* of a run are the root's entry \(J\), or the two entries of the switch pair. Along a run, a same update keeps a suffix of the list, may intersect its first kept entry with a rank suffix, and appends an injection; a switched side starts a new run and discards the old list.

**Lemma 3.1 (the shape of an entry).** Every entry of a list is one of: an initial entry of its run, or an injection appended in its run, intersected with at most one rank suffix \(\{\lambda\geq r\}\) of the run's frame.

*Proof.* Entries are only kept, deleted or intersected with rank suffixes of the same frame, and \(\{\lambda\geq r\}\cap\{\lambda\geq r'\}=\{\lambda\geq\max(r,r')\}\). \(\square\)

**Lemma 3.2 (at most five entries).** Every pruned list has at most five entries. At most three of them are injections.

*Proof.* A list starts a run with at most two initial entries, so it suffices to count the injections in the list of a child \(W'\) created by a same update from \(W\). All of them were appended in the current run.

First, any two of them are disjoint inside \(W\). Consider two of them and the edge \(U\to U'\) at which the later one was appended, at a node \(U\) of the run containing \(W\). At that moment the older one was part of the carry, and by the proof of Lemma 2.1 the carry's union meets \(U\) only in qualifiers of \(U\)'s list, which lie in \(P_{b_U}\), while the new injection meets \(U\) in \(U\setminus P_{b_U}\). So the two are disjoint inside \(U\). Afterwards the entries were only shrunk by rank suffixes, and \(W\subseteq U\), so they remain disjoint inside \(W\).

Next, every injection that survives pruning contains a job \(x\in W'\). That job qualifies, so it is high (Lemma 2.1), and \(x\in P_{b'}\): there is a job \(z\) in the slot \(b'\) with \(x\prec z\). The entry is an upset, so \(z\) belongs to it as well, and \(z\in W\) because \(b'\) is a slot of \(W\) (Lemma 4.2 of the fourth lesson). By disjointness inside \(W\), different surviving injections give different jobs \(z\) of the triple \(b'\). So at most three injections survive. \(\square\)

A freshly formed list may have six entries before pruning. The bound is used only for pruned lists, and for a carry taken from a pruned list before the new injection is appended.

## 4. Exercises

**4.1.** Show that \(\operatorname{carry}_{1,0}(\mathcal K)=\mathcal K\), and that \(\operatorname{carry}_{d,r}\) applied twice in a row can be written as a single carry.

**4.2.** Give a list and a set \(W'\) for which pruning changes the key of a job of \(W'\), and check Lemma 1.2 in your example.

**4.3.** Why must the injection be appended as the *last* entry of the new list? What would go wrong in Lemma 2.1 if it were placed first?

**4.4.** On a switched side, why is the second entry \(D_a\) needed, when the first entry \(G\cap\{\lambda\geq h\}\) may already contain jobs of \(W\cap D_a\)?

**4.5.** In the proof of Lemma 3.2, where is it used that every entry is an upset of all of \(J\), and not only closed upwards inside \(W\)?

## 5. Solutions

**4.1.** With \(d=1\) and \(r=0\) the only change is the intersection of \(K_1\) with \(\{\lambda\geq0\}=J\). A carry takes a suffix and trims its first entry; a second carry takes a suffix of that suffix and trims its first entry, which is either the same entry (and the two thresholds combine into the larger one) or a later, untrimmed entry.

**4.2.** Take \(\mathcal K=(K_1,K_2)\) with \(K_2\) disjoint from \(W'\) and a job \(x\in W'\cap K_1\). Before pruning a job \(y\in K_2\) has key \((2,\lambda(y))\) and \(x\) has key \((1,\lambda(x))\). After pruning \(K_2\) is gone; if \(y\in K_1\), its key becomes \((1,\lambda(y))\). If \(\lambda(x)<\lambda(y)\), the pruned keys still satisfy \(\operatorname{key}(x)<\operatorname{key}(y)\), as before pruning. If instead \(\lambda(y)<\lambda(x)\), then before pruning \(x\) had the smaller key and after pruning the larger one. This does not contradict Lemma 1.2: the job with the smaller pruned key is \(y\), which is not in \(W'\). The lemma needs the job with the smaller pruned key to lie in \(W'\).

**4.3.** The jobs of \(Y\) come last in the same side's priority order. As the last entry, the injection gives them the largest index, so their keys exceed those of all carried jobs. Placed first, it would give them the smallest index, and the key order would no longer agree with the priority order used to normalize the side.

**4.4.** The first entry contains \(X\setminus S\) but need not contain all of \(W\cap D_a\); the high jobs of \(W\cap D_a\) must qualify. Moreover the second entry's larger index places all of \(W\cap D_a\) after \(X\setminus S\) in key order, as the switched priority order requires, even for the jobs that also lie in the first entry.

**4.5.** The witness \(z\) lies in the slot \(b'\), which is in \(W\) but outside the child \(W'\). Closure inside \(W'\) would not reach it; closure in all of \(J\) does.

## References

- [OpenAI-P] OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*, OpenAI Math Release preprint, 24 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026
